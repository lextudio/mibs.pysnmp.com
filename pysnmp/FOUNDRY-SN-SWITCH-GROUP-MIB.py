# SNMP MIB module (FOUNDRY-SN-SWITCH-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-SWITCH-GROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:27 2024
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

(DisplayString,
 MacAddress) = mibBuilder.importSymbols(
    "FOUNDRY-SN-AGENT-MIB",
    "DisplayString",
    "MacAddress")

(switch,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "switch")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

snSwitch = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3)
)
snSwitch.setRevisions(
        ("2013-10-25 00:00",
         "2010-06-02 00:00",
         "2009-09-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PhysAddress(OctetString, TextualConvention):
    status = "current"


class BridgeId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class Timeout(Integer32, TextualConvention):
    status = "current"


class PortMask(Integer32, TextualConvention):
    status = "current"


class InterfaceId(ObjectIdentifier, TextualConvention):
    status = "current"


class InterfaceId2(ObjectIdentifier, TextualConvention):
    status = "current"


class VlanTagMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dual", 3),
          ("tagged", 1),
          ("untagged", 2))
    )



class FdryVlanIdOrNoneTC(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )



class BrcdVlanIdTC(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4090),
    )



class BrcdVlanIdOrNoneTC(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4090),
    )



class PortQosTC(Integer32, TextualConvention):
    status = "current"
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
              127)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 127),
          ("level0", 0),
          ("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7))
    )



class PortPriorityTC(Integer32, TextualConvention):
    status = "current"
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
              128)
        )
    )
    namedValues = NamedValues(
        *(("nonPriority", 128),
          ("priority0", 1),
          ("priority1", 2),
          ("priority2", 3),
          ("priority3", 4),
          ("priority4", 5),
          ("priority5", 6),
          ("priority6", 7),
          ("priority7", 8))
    )



# MIB Managed Objects in the order of their OIDs

_SnSwInfo_ObjectIdentity = ObjectIdentity
snSwInfo = _SnSwInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1)
)


class _SnSwGroupOperMode_Type(Integer32):
    """Custom type snSwGroupOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noVLan", 1),
          ("vlanByPort", 2))
    )


_SnSwGroupOperMode_Type.__name__ = "Integer32"
_SnSwGroupOperMode_Object = MibScalar
snSwGroupOperMode = _SnSwGroupOperMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 1),
    _SnSwGroupOperMode_Type()
)
snSwGroupOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwGroupOperMode.setStatus("current")


class _SnSwGroupIpL3SwMode_Type(Integer32):
    """Custom type snSwGroupIpL3SwMode based on Integer32"""
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


_SnSwGroupIpL3SwMode_Type.__name__ = "Integer32"
_SnSwGroupIpL3SwMode_Object = MibScalar
snSwGroupIpL3SwMode = _SnSwGroupIpL3SwMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 2),
    _SnSwGroupIpL3SwMode_Type()
)
snSwGroupIpL3SwMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwGroupIpL3SwMode.setStatus("current")


class _SnSwGroupIpMcastMode_Type(Integer32):
    """Custom type snSwGroupIpMcastMode based on Integer32"""
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


_SnSwGroupIpMcastMode_Type.__name__ = "Integer32"
_SnSwGroupIpMcastMode_Object = MibScalar
snSwGroupIpMcastMode = _SnSwGroupIpMcastMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 3),
    _SnSwGroupIpMcastMode_Type()
)
snSwGroupIpMcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwGroupIpMcastMode.setStatus("current")


class _SnSwGroupDefaultCfgMode_Type(Integer32):
    """Custom type snSwGroupDefaultCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("nonDefault", 2))
    )


_SnSwGroupDefaultCfgMode_Type.__name__ = "Integer32"
_SnSwGroupDefaultCfgMode_Object = MibScalar
snSwGroupDefaultCfgMode = _SnSwGroupDefaultCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 4),
    _SnSwGroupDefaultCfgMode_Type()
)
snSwGroupDefaultCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwGroupDefaultCfgMode.setStatus("current")
_SnSwGroupSwitchAgeTime_Type = Integer32
_SnSwGroupSwitchAgeTime_Object = MibScalar
snSwGroupSwitchAgeTime = _SnSwGroupSwitchAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 5),
    _SnSwGroupSwitchAgeTime_Type()
)
snSwGroupSwitchAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwGroupSwitchAgeTime.setStatus("current")
_SnVLanGroupVlanCurEntry_Type = Integer32
_SnVLanGroupVlanCurEntry_Object = MibScalar
snVLanGroupVlanCurEntry = _SnVLanGroupVlanCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 6),
    _SnVLanGroupVlanCurEntry_Type()
)
snVLanGroupVlanCurEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanGroupVlanCurEntry.setStatus("current")
_SnVLanGroupSetAllVLan_Type = Integer32
_SnVLanGroupSetAllVLan_Object = MibScalar
snVLanGroupSetAllVLan = _SnVLanGroupSetAllVLan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 7),
    _SnVLanGroupSetAllVLan_Type()
)
snVLanGroupSetAllVLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanGroupSetAllVLan.setStatus("current")
_SnSwPortSetAll_Type = Integer32
_SnSwPortSetAll_Object = MibScalar
snSwPortSetAll = _SnSwPortSetAll_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 8),
    _SnSwPortSetAll_Type()
)
snSwPortSetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortSetAll.setStatus("current")
_SnFdbTableCurEntry_Type = Integer32
_SnFdbTableCurEntry_Object = MibScalar
snFdbTableCurEntry = _SnFdbTableCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 9),
    _SnFdbTableCurEntry_Type()
)
snFdbTableCurEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFdbTableCurEntry.setStatus("current")


class _SnFdbTableStationFlush_Type(Integer32):
    """Custom type snFdbTableStationFlush based on Integer32"""
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
        *(("error", 2),
          ("flush", 3),
          ("flushing", 4),
          ("normal", 1))
    )


_SnFdbTableStationFlush_Type.__name__ = "Integer32"
_SnFdbTableStationFlush_Object = MibScalar
snFdbTableStationFlush = _SnFdbTableStationFlush_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 10),
    _SnFdbTableStationFlush_Type()
)
snFdbTableStationFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFdbTableStationFlush.setStatus("current")
_SnPortStpSetAll_Type = Integer32
_SnPortStpSetAll_Object = MibScalar
snPortStpSetAll = _SnPortStpSetAll_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 11),
    _SnPortStpSetAll_Type()
)
snPortStpSetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortStpSetAll.setStatus("current")
_SnSwProbePortNum_Type = Integer32
_SnSwProbePortNum_Object = MibScalar
snSwProbePortNum = _SnSwProbePortNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 12),
    _SnSwProbePortNum_Type()
)
snSwProbePortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwProbePortNum.setStatus("current")


class _SnSw8021qTagMode_Type(Integer32):
    """Custom type snSw8021qTagMode based on Integer32"""
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


_SnSw8021qTagMode_Type.__name__ = "Integer32"
_SnSw8021qTagMode_Object = MibScalar
snSw8021qTagMode = _SnSw8021qTagMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 13),
    _SnSw8021qTagMode_Type()
)
snSw8021qTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSw8021qTagMode.setStatus("current")


class _SnSwGlobalStpMode_Type(Integer32):
    """Custom type snSwGlobalStpMode based on Integer32"""
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


_SnSwGlobalStpMode_Type.__name__ = "Integer32"
_SnSwGlobalStpMode_Object = MibScalar
snSwGlobalStpMode = _SnSwGlobalStpMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 14),
    _SnSwGlobalStpMode_Type()
)
snSwGlobalStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwGlobalStpMode.setStatus("current")


class _SnSwIpMcastQuerierMode_Type(Integer32):
    """Custom type snSwIpMcastQuerierMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonQuerier", 2),
          ("querier", 1))
    )


_SnSwIpMcastQuerierMode_Type.__name__ = "Integer32"
_SnSwIpMcastQuerierMode_Object = MibScalar
snSwIpMcastQuerierMode = _SnSwIpMcastQuerierMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 15),
    _SnSwIpMcastQuerierMode_Type()
)
snSwIpMcastQuerierMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIpMcastQuerierMode.setStatus("current")
_SnSwViolatorPortNumber_Type = Integer32
_SnSwViolatorPortNumber_Object = MibScalar
snSwViolatorPortNumber = _SnSwViolatorPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 17),
    _SnSwViolatorPortNumber_Type()
)
snSwViolatorPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwViolatorPortNumber.setStatus("current")
_SnSwViolatorMacAddress_Type = MacAddress
_SnSwViolatorMacAddress_Object = MibScalar
snSwViolatorMacAddress = _SnSwViolatorMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 18),
    _SnSwViolatorMacAddress_Type()
)
snSwViolatorMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwViolatorMacAddress.setStatus("current")
_SnVLanGroupVlanMaxEntry_Type = Integer32
_SnVLanGroupVlanMaxEntry_Object = MibScalar
snVLanGroupVlanMaxEntry = _SnVLanGroupVlanMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 19),
    _SnVLanGroupVlanMaxEntry_Type()
)
snVLanGroupVlanMaxEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanGroupVlanMaxEntry.setStatus("current")
_SnSwEosBufferSize_Type = Integer32
_SnSwEosBufferSize_Object = MibScalar
snSwEosBufferSize = _SnSwEosBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 20),
    _SnSwEosBufferSize_Type()
)
snSwEosBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwEosBufferSize.setStatus("current")
_SnVLanByPortEntrySize_Type = Integer32
_SnVLanByPortEntrySize_Object = MibScalar
snVLanByPortEntrySize = _SnVLanByPortEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 21),
    _SnVLanByPortEntrySize_Type()
)
snVLanByPortEntrySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortEntrySize.setStatus("current")
_SnSwPortEntrySize_Type = Integer32
_SnSwPortEntrySize_Object = MibScalar
snSwPortEntrySize = _SnSwPortEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 22),
    _SnSwPortEntrySize_Type()
)
snSwPortEntrySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortEntrySize.setStatus("current")
_SnFdbStationEntrySize_Type = Integer32
_SnFdbStationEntrySize_Object = MibScalar
snFdbStationEntrySize = _SnFdbStationEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 23),
    _SnFdbStationEntrySize_Type()
)
snFdbStationEntrySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFdbStationEntrySize.setStatus("current")
_SnPortStpEntrySize_Type = Integer32
_SnPortStpEntrySize_Object = MibScalar
snPortStpEntrySize = _SnPortStpEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 24),
    _SnPortStpEntrySize_Type()
)
snPortStpEntrySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortStpEntrySize.setStatus("current")


class _SnSwEnableBridgeNewRootTrap_Type(Integer32):
    """Custom type snSwEnableBridgeNewRootTrap based on Integer32"""
    defaultValue = 1

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


_SnSwEnableBridgeNewRootTrap_Type.__name__ = "Integer32"
_SnSwEnableBridgeNewRootTrap_Object = MibScalar
snSwEnableBridgeNewRootTrap = _SnSwEnableBridgeNewRootTrap_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 25),
    _SnSwEnableBridgeNewRootTrap_Type()
)
snSwEnableBridgeNewRootTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwEnableBridgeNewRootTrap.setStatus("current")


class _SnSwEnableBridgeTopoChangeTrap_Type(Integer32):
    """Custom type snSwEnableBridgeTopoChangeTrap based on Integer32"""
    defaultValue = 1

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


_SnSwEnableBridgeTopoChangeTrap_Type.__name__ = "Integer32"
_SnSwEnableBridgeTopoChangeTrap_Object = MibScalar
snSwEnableBridgeTopoChangeTrap = _SnSwEnableBridgeTopoChangeTrap_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 26),
    _SnSwEnableBridgeTopoChangeTrap_Type()
)
snSwEnableBridgeTopoChangeTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwEnableBridgeTopoChangeTrap.setStatus("current")


class _SnSwEnableLockedAddrViolationTrap_Type(Integer32):
    """Custom type snSwEnableLockedAddrViolationTrap based on Integer32"""
    defaultValue = 1

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


_SnSwEnableLockedAddrViolationTrap_Type.__name__ = "Integer32"
_SnSwEnableLockedAddrViolationTrap_Object = MibScalar
snSwEnableLockedAddrViolationTrap = _SnSwEnableLockedAddrViolationTrap_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 27),
    _SnSwEnableLockedAddrViolationTrap_Type()
)
snSwEnableLockedAddrViolationTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwEnableLockedAddrViolationTrap.setStatus("current")


class _SnSwIpxL3SwMode_Type(Integer32):
    """Custom type snSwIpxL3SwMode based on Integer32"""
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


_SnSwIpxL3SwMode_Type.__name__ = "Integer32"
_SnSwIpxL3SwMode_Object = MibScalar
snSwIpxL3SwMode = _SnSwIpxL3SwMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 28),
    _SnSwIpxL3SwMode_Type()
)
snSwIpxL3SwMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIpxL3SwMode.setStatus("current")
_SnVLanByIpSubnetMaxSubnets_Type = Integer32
_SnVLanByIpSubnetMaxSubnets_Object = MibScalar
snVLanByIpSubnetMaxSubnets = _SnVLanByIpSubnetMaxSubnets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 29),
    _SnVLanByIpSubnetMaxSubnets_Type()
)
snVLanByIpSubnetMaxSubnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByIpSubnetMaxSubnets.setStatus("current")
_SnVLanByIpxNetMaxNetworks_Type = Integer32
_SnVLanByIpxNetMaxNetworks_Object = MibScalar
snVLanByIpxNetMaxNetworks = _SnVLanByIpxNetMaxNetworks_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 30),
    _SnVLanByIpxNetMaxNetworks_Type()
)
snVLanByIpxNetMaxNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByIpxNetMaxNetworks.setStatus("current")


class _SnSwProtocolVLanMode_Type(Integer32):
    """Custom type snSwProtocolVLanMode based on Integer32"""
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


_SnSwProtocolVLanMode_Type.__name__ = "Integer32"
_SnSwProtocolVLanMode_Object = MibScalar
snSwProtocolVLanMode = _SnSwProtocolVLanMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 31),
    _SnSwProtocolVLanMode_Type()
)
snSwProtocolVLanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwProtocolVLanMode.setStatus("deprecated")


class _SnMacStationVLanId_Type(Integer32):
    """Custom type snMacStationVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SnMacStationVLanId_Type.__name__ = "Integer32"
_SnMacStationVLanId_Object = MibScalar
snMacStationVLanId = _SnMacStationVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 32),
    _SnMacStationVLanId_Type()
)
snMacStationVLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacStationVLanId.setStatus("deprecated")


class _SnSwClearCounters_Type(Integer32):
    """Custom type snSwClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("valid", 0))
    )


_SnSwClearCounters_Type.__name__ = "Integer32"
_SnSwClearCounters_Object = MibScalar
snSwClearCounters = _SnSwClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 33),
    _SnSwClearCounters_Type()
)
snSwClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwClearCounters.setStatus("current")


class _SnSw8021qTagType_Type(Integer32):
    """Custom type snSw8021qTagType based on Integer32"""
    defaultValue = 33024


_SnSw8021qTagType_Object = MibScalar
snSw8021qTagType = _SnSw8021qTagType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 34),
    _SnSw8021qTagType_Type()
)
snSw8021qTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSw8021qTagType.setStatus("current")


class _SnSwBroadcastLimit_Type(Integer32):
    """Custom type snSwBroadcastLimit based on Integer32"""
    defaultValue = 0


_SnSwBroadcastLimit_Object = MibScalar
snSwBroadcastLimit = _SnSwBroadcastLimit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 35),
    _SnSwBroadcastLimit_Type()
)
snSwBroadcastLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwBroadcastLimit.setStatus("current")
_SnSwMaxMacFilterPerSystem_Type = Integer32
_SnSwMaxMacFilterPerSystem_Object = MibScalar
snSwMaxMacFilterPerSystem = _SnSwMaxMacFilterPerSystem_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 36),
    _SnSwMaxMacFilterPerSystem_Type()
)
snSwMaxMacFilterPerSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwMaxMacFilterPerSystem.setStatus("current")
_SnSwMaxMacFilterPerPort_Type = Integer32
_SnSwMaxMacFilterPerPort_Object = MibScalar
snSwMaxMacFilterPerPort = _SnSwMaxMacFilterPerPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 37),
    _SnSwMaxMacFilterPerPort_Type()
)
snSwMaxMacFilterPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwMaxMacFilterPerPort.setStatus("current")


class _SnSwDefaultVLanId_Type(Integer32):
    """Custom type snSwDefaultVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SnSwDefaultVLanId_Type.__name__ = "Integer32"
_SnSwDefaultVLanId_Object = MibScalar
snSwDefaultVLanId = _SnSwDefaultVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 38),
    _SnSwDefaultVLanId_Type()
)
snSwDefaultVLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwDefaultVLanId.setStatus("current")


class _SnSwGlobalAutoNegotiate_Type(Integer32):
    """Custom type snSwGlobalAutoNegotiate based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 0),
          ("enabled", 1),
          ("negFullAuto", 2),
          ("other", 3))
    )


_SnSwGlobalAutoNegotiate_Type.__name__ = "Integer32"
_SnSwGlobalAutoNegotiate_Object = MibScalar
snSwGlobalAutoNegotiate = _SnSwGlobalAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 39),
    _SnSwGlobalAutoNegotiate_Type()
)
snSwGlobalAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwGlobalAutoNegotiate.setStatus("current")


class _SnSwQosMechanism_Type(Integer32):
    """Custom type snSwQosMechanism based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("strict", 0),
          ("weighted", 1))
    )


_SnSwQosMechanism_Type.__name__ = "Integer32"
_SnSwQosMechanism_Object = MibScalar
snSwQosMechanism = _SnSwQosMechanism_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 40),
    _SnSwQosMechanism_Type()
)
snSwQosMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwQosMechanism.setStatus("current")


class _SnSwSingleStpMode_Type(Integer32):
    """Custom type snSwSingleStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enableRstp", 2),
          ("enableStp", 1))
    )


_SnSwSingleStpMode_Type.__name__ = "Integer32"
_SnSwSingleStpMode_Object = MibScalar
snSwSingleStpMode = _SnSwSingleStpMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 41),
    _SnSwSingleStpMode_Type()
)
snSwSingleStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwSingleStpMode.setStatus("current")


class _SnSwFastStpMode_Type(Integer32):
    """Custom type snSwFastStpMode based on Integer32"""
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


_SnSwFastStpMode_Type.__name__ = "Integer32"
_SnSwFastStpMode_Object = MibScalar
snSwFastStpMode = _SnSwFastStpMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 42),
    _SnSwFastStpMode_Type()
)
snSwFastStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwFastStpMode.setStatus("current")
_SnSwViolatorIfIndex_Type = Integer32
_SnSwViolatorIfIndex_Object = MibScalar
snSwViolatorIfIndex = _SnSwViolatorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 43),
    _SnSwViolatorIfIndex_Type()
)
snSwViolatorIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwViolatorIfIndex.setStatus("current")
_SnSwSingleStpVLanId_Type = Integer32
_SnSwSingleStpVLanId_Object = MibScalar
snSwSingleStpVLanId = _SnSwSingleStpVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 44),
    _SnSwSingleStpVLanId_Type()
)
snSwSingleStpVLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwSingleStpVLanId.setStatus("current")


class _SnSwBroadcastLimit2_Type(Unsigned32):
    """Custom type snSwBroadcastLimit2 based on Unsigned32"""
    defaultValue = 4294967295


_SnSwBroadcastLimit2_Object = MibScalar
snSwBroadcastLimit2 = _SnSwBroadcastLimit2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 1, 45),
    _SnSwBroadcastLimit2_Type()
)
snSwBroadcastLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwBroadcastLimit2.setStatus("current")
_SnVLanInfo_ObjectIdentity = ObjectIdentity
snVLanInfo = _SnVLanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2)
)
_SnVLanByPortTable_Object = MibTable
snVLanByPortTable = _SnVLanByPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    snVLanByPortTable.setStatus("deprecated")
_SnVLanByPortEntry_Object = MibTableRow
snVLanByPortEntry = _SnVLanByPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1)
)
snVLanByPortEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByPortVLanIndex"),
)
if mibBuilder.loadTexts:
    snVLanByPortEntry.setStatus("deprecated")


class _SnVLanByPortVLanIndex_Type(Integer32):
    """Custom type snVLanByPortVLanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SnVLanByPortVLanIndex_Type.__name__ = "Integer32"
_SnVLanByPortVLanIndex_Object = MibTableColumn
snVLanByPortVLanIndex = _SnVLanByPortVLanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 1),
    _SnVLanByPortVLanIndex_Type()
)
snVLanByPortVLanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortVLanIndex.setStatus("deprecated")


class _SnVLanByPortVLanId_Type(Integer32):
    """Custom type snVLanByPortVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SnVLanByPortVLanId_Type.__name__ = "Integer32"
_SnVLanByPortVLanId_Object = MibTableColumn
snVLanByPortVLanId = _SnVLanByPortVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 2),
    _SnVLanByPortVLanId_Type()
)
snVLanByPortVLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortVLanId.setStatus("deprecated")
_SnVLanByPortPortMask_Type = PortMask
_SnVLanByPortPortMask_Object = MibTableColumn
snVLanByPortPortMask = _SnVLanByPortPortMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 3),
    _SnVLanByPortPortMask_Type()
)
snVLanByPortPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortPortMask.setStatus("deprecated")


class _SnVLanByPortQos_Type(Integer32):
    """Custom type snVLanByPortQos based on Integer32"""
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
        *(("level0", 0),
          ("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7))
    )


_SnVLanByPortQos_Type.__name__ = "Integer32"
_SnVLanByPortQos_Object = MibTableColumn
snVLanByPortQos = _SnVLanByPortQos_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 4),
    _SnVLanByPortQos_Type()
)
snVLanByPortQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortQos.setStatus("deprecated")


class _SnVLanByPortStpMode_Type(Integer32):
    """Custom type snVLanByPortStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enableRstp", 2),
          ("enableStp", 1))
    )


_SnVLanByPortStpMode_Type.__name__ = "Integer32"
_SnVLanByPortStpMode_Object = MibTableColumn
snVLanByPortStpMode = _SnVLanByPortStpMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 5),
    _SnVLanByPortStpMode_Type()
)
snVLanByPortStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortStpMode.setStatus("deprecated")


class _SnVLanByPortStpPriority_Type(Integer32):
    """Custom type snVLanByPortStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnVLanByPortStpPriority_Type.__name__ = "Integer32"
_SnVLanByPortStpPriority_Object = MibTableColumn
snVLanByPortStpPriority = _SnVLanByPortStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 6),
    _SnVLanByPortStpPriority_Type()
)
snVLanByPortStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortStpPriority.setStatus("deprecated")


class _SnVLanByPortStpGroupMaxAge_Type(Integer32):
    """Custom type snVLanByPortStpGroupMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_SnVLanByPortStpGroupMaxAge_Type.__name__ = "Integer32"
_SnVLanByPortStpGroupMaxAge_Object = MibTableColumn
snVLanByPortStpGroupMaxAge = _SnVLanByPortStpGroupMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 7),
    _SnVLanByPortStpGroupMaxAge_Type()
)
snVLanByPortStpGroupMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortStpGroupMaxAge.setStatus("deprecated")


class _SnVLanByPortStpGroupHelloTime_Type(Integer32):
    """Custom type snVLanByPortStpGroupHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SnVLanByPortStpGroupHelloTime_Type.__name__ = "Integer32"
_SnVLanByPortStpGroupHelloTime_Object = MibTableColumn
snVLanByPortStpGroupHelloTime = _SnVLanByPortStpGroupHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 8),
    _SnVLanByPortStpGroupHelloTime_Type()
)
snVLanByPortStpGroupHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortStpGroupHelloTime.setStatus("deprecated")


class _SnVLanByPortStpGroupForwardDelay_Type(Integer32):
    """Custom type snVLanByPortStpGroupForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SnVLanByPortStpGroupForwardDelay_Type.__name__ = "Integer32"
_SnVLanByPortStpGroupForwardDelay_Object = MibTableColumn
snVLanByPortStpGroupForwardDelay = _SnVLanByPortStpGroupForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 9),
    _SnVLanByPortStpGroupForwardDelay_Type()
)
snVLanByPortStpGroupForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortStpGroupForwardDelay.setStatus("deprecated")


class _SnVLanByPortRowStatus_Type(Integer32):
    """Custom type snVLanByPortRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("modify", 5),
          ("other", 1),
          ("valid", 2))
    )


_SnVLanByPortRowStatus_Type.__name__ = "Integer32"
_SnVLanByPortRowStatus_Object = MibTableColumn
snVLanByPortRowStatus = _SnVLanByPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 10),
    _SnVLanByPortRowStatus_Type()
)
snVLanByPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortRowStatus.setStatus("deprecated")


class _SnVLanByPortOperState_Type(Integer32):
    """Custom type snVLanByPortOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("notActivated", 0))
    )


_SnVLanByPortOperState_Type.__name__ = "Integer32"
_SnVLanByPortOperState_Object = MibTableColumn
snVLanByPortOperState = _SnVLanByPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 11),
    _SnVLanByPortOperState_Type()
)
snVLanByPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortOperState.setStatus("deprecated")
_SnVLanByPortBaseNumPorts_Type = Integer32
_SnVLanByPortBaseNumPorts_Object = MibTableColumn
snVLanByPortBaseNumPorts = _SnVLanByPortBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 12),
    _SnVLanByPortBaseNumPorts_Type()
)
snVLanByPortBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortBaseNumPorts.setStatus("deprecated")


class _SnVLanByPortBaseType_Type(Integer32):
    """Custom type snVLanByPortBaseType based on Integer32"""
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
        *(("sourcerouteOnly", 3),
          ("srt", 4),
          ("transparentOnly", 2),
          ("unknown", 1))
    )


_SnVLanByPortBaseType_Type.__name__ = "Integer32"
_SnVLanByPortBaseType_Object = MibTableColumn
snVLanByPortBaseType = _SnVLanByPortBaseType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 13),
    _SnVLanByPortBaseType_Type()
)
snVLanByPortBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortBaseType.setStatus("deprecated")


class _SnVLanByPortStpProtocolSpecification_Type(Integer32):
    """Custom type snVLanByPortStpProtocolSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decLb100", 2),
          ("ieee8021d", 3),
          ("unknown", 1))
    )


_SnVLanByPortStpProtocolSpecification_Type.__name__ = "Integer32"
_SnVLanByPortStpProtocolSpecification_Object = MibTableColumn
snVLanByPortStpProtocolSpecification = _SnVLanByPortStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 14),
    _SnVLanByPortStpProtocolSpecification_Type()
)
snVLanByPortStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortStpProtocolSpecification.setStatus("deprecated")
_SnVLanByPortStpMaxAge_Type = Timeout
_SnVLanByPortStpMaxAge_Object = MibTableColumn
snVLanByPortStpMaxAge = _SnVLanByPortStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 15),
    _SnVLanByPortStpMaxAge_Type()
)
snVLanByPortStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortStpMaxAge.setStatus("deprecated")
_SnVLanByPortStpHelloTime_Type = Timeout
_SnVLanByPortStpHelloTime_Object = MibTableColumn
snVLanByPortStpHelloTime = _SnVLanByPortStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 16),
    _SnVLanByPortStpHelloTime_Type()
)
snVLanByPortStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortStpHelloTime.setStatus("deprecated")
_SnVLanByPortStpHoldTime_Type = Integer32
_SnVLanByPortStpHoldTime_Object = MibTableColumn
snVLanByPortStpHoldTime = _SnVLanByPortStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 17),
    _SnVLanByPortStpHoldTime_Type()
)
snVLanByPortStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortStpHoldTime.setStatus("deprecated")
_SnVLanByPortStpForwardDelay_Type = Timeout
_SnVLanByPortStpForwardDelay_Object = MibTableColumn
snVLanByPortStpForwardDelay = _SnVLanByPortStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 18),
    _SnVLanByPortStpForwardDelay_Type()
)
snVLanByPortStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortStpForwardDelay.setStatus("deprecated")
_SnVLanByPortStpTimeSinceTopologyChange_Type = TimeTicks
_SnVLanByPortStpTimeSinceTopologyChange_Object = MibTableColumn
snVLanByPortStpTimeSinceTopologyChange = _SnVLanByPortStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 19),
    _SnVLanByPortStpTimeSinceTopologyChange_Type()
)
snVLanByPortStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortStpTimeSinceTopologyChange.setStatus("deprecated")
_SnVLanByPortStpTopChanges_Type = Counter32
_SnVLanByPortStpTopChanges_Object = MibTableColumn
snVLanByPortStpTopChanges = _SnVLanByPortStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 20),
    _SnVLanByPortStpTopChanges_Type()
)
snVLanByPortStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortStpTopChanges.setStatus("deprecated")
_SnVLanByPortStpRootCost_Type = Integer32
_SnVLanByPortStpRootCost_Object = MibTableColumn
snVLanByPortStpRootCost = _SnVLanByPortStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 21),
    _SnVLanByPortStpRootCost_Type()
)
snVLanByPortStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortStpRootCost.setStatus("deprecated")
_SnVLanByPortStpRootPort_Type = Integer32
_SnVLanByPortStpRootPort_Object = MibTableColumn
snVLanByPortStpRootPort = _SnVLanByPortStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 22),
    _SnVLanByPortStpRootPort_Type()
)
snVLanByPortStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortStpRootPort.setStatus("deprecated")
_SnVLanByPortStpDesignatedRoot_Type = BridgeId
_SnVLanByPortStpDesignatedRoot_Object = MibTableColumn
snVLanByPortStpDesignatedRoot = _SnVLanByPortStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 23),
    _SnVLanByPortStpDesignatedRoot_Type()
)
snVLanByPortStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortStpDesignatedRoot.setStatus("deprecated")
_SnVLanByPortBaseBridgeAddress_Type = MacAddress
_SnVLanByPortBaseBridgeAddress_Object = MibTableColumn
snVLanByPortBaseBridgeAddress = _SnVLanByPortBaseBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 24),
    _SnVLanByPortBaseBridgeAddress_Type()
)
snVLanByPortBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortBaseBridgeAddress.setStatus("deprecated")


class _SnVLanByPortVLanName_Type(DisplayString):
    """Custom type snVLanByPortVLanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnVLanByPortVLanName_Type.__name__ = "DisplayString"
_SnVLanByPortVLanName_Object = MibTableColumn
snVLanByPortVLanName = _SnVLanByPortVLanName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 25),
    _SnVLanByPortVLanName_Type()
)
snVLanByPortVLanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortVLanName.setStatus("deprecated")
_SnVLanByPortRouterIntf_Type = Integer32
_SnVLanByPortRouterIntf_Object = MibTableColumn
snVLanByPortRouterIntf = _SnVLanByPortRouterIntf_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 26),
    _SnVLanByPortRouterIntf_Type()
)
snVLanByPortRouterIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortRouterIntf.setStatus("deprecated")
_SnVLanByPortChassisPortMask_Type = OctetString
_SnVLanByPortChassisPortMask_Object = MibTableColumn
snVLanByPortChassisPortMask = _SnVLanByPortChassisPortMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 27),
    _SnVLanByPortChassisPortMask_Type()
)
snVLanByPortChassisPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortChassisPortMask.setStatus("deprecated")
_SnVLanByPortPortList_Type = OctetString
_SnVLanByPortPortList_Object = MibTableColumn
snVLanByPortPortList = _SnVLanByPortPortList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 1, 1, 28),
    _SnVLanByPortPortList_Type()
)
snVLanByPortPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortPortList.setStatus("deprecated")
_SnVLanByProtocolTable_Object = MibTable
snVLanByProtocolTable = _SnVLanByProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    snVLanByProtocolTable.setStatus("current")
_SnVLanByProtocolEntry_Object = MibTableRow
snVLanByProtocolEntry = _SnVLanByProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 2, 1)
)
snVLanByProtocolEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByProtocolVLanId"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByProtocolIndex"),
)
if mibBuilder.loadTexts:
    snVLanByProtocolEntry.setStatus("current")


class _SnVLanByProtocolVLanId_Type(Integer32):
    """Custom type snVLanByProtocolVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SnVLanByProtocolVLanId_Type.__name__ = "Integer32"
_SnVLanByProtocolVLanId_Object = MibTableColumn
snVLanByProtocolVLanId = _SnVLanByProtocolVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 2, 1, 1),
    _SnVLanByProtocolVLanId_Type()
)
snVLanByProtocolVLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByProtocolVLanId.setStatus("current")


class _SnVLanByProtocolIndex_Type(Integer32):
    """Custom type snVLanByProtocolIndex based on Integer32"""
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
        *(("appleTalk", 3),
          ("decNet", 4),
          ("ip", 1),
          ("ipv6", 7),
          ("ipx", 2),
          ("netBios", 5),
          ("others", 6))
    )


_SnVLanByProtocolIndex_Type.__name__ = "Integer32"
_SnVLanByProtocolIndex_Object = MibTableColumn
snVLanByProtocolIndex = _SnVLanByProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 2, 1, 2),
    _SnVLanByProtocolIndex_Type()
)
snVLanByProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByProtocolIndex.setStatus("current")


class _SnVLanByProtocolDynamic_Type(Integer32):
    """Custom type snVLanByProtocolDynamic based on Integer32"""
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


_SnVLanByProtocolDynamic_Type.__name__ = "Integer32"
_SnVLanByProtocolDynamic_Object = MibTableColumn
snVLanByProtocolDynamic = _SnVLanByProtocolDynamic_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 2, 1, 3),
    _SnVLanByProtocolDynamic_Type()
)
snVLanByProtocolDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByProtocolDynamic.setStatus("current")
_SnVLanByProtocolStaticMask_Type = PortMask
_SnVLanByProtocolStaticMask_Object = MibTableColumn
snVLanByProtocolStaticMask = _SnVLanByProtocolStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 2, 1, 4),
    _SnVLanByProtocolStaticMask_Type()
)
snVLanByProtocolStaticMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByProtocolStaticMask.setStatus("deprecated")
_SnVLanByProtocolExcludeMask_Type = PortMask
_SnVLanByProtocolExcludeMask_Object = MibTableColumn
snVLanByProtocolExcludeMask = _SnVLanByProtocolExcludeMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 2, 1, 5),
    _SnVLanByProtocolExcludeMask_Type()
)
snVLanByProtocolExcludeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByProtocolExcludeMask.setStatus("deprecated")


class _SnVLanByProtocolRouterIntf_Type(Integer32):
    """Custom type snVLanByProtocolRouterIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SnVLanByProtocolRouterIntf_Type.__name__ = "Integer32"
_SnVLanByProtocolRouterIntf_Object = MibTableColumn
snVLanByProtocolRouterIntf = _SnVLanByProtocolRouterIntf_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 2, 1, 6),
    _SnVLanByProtocolRouterIntf_Type()
)
snVLanByProtocolRouterIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByProtocolRouterIntf.setStatus("current")


class _SnVLanByProtocolRowStatus_Type(Integer32):
    """Custom type snVLanByProtocolRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("modify", 5),
          ("other", 1),
          ("valid", 2))
    )


_SnVLanByProtocolRowStatus_Type.__name__ = "Integer32"
_SnVLanByProtocolRowStatus_Object = MibTableColumn
snVLanByProtocolRowStatus = _SnVLanByProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 2, 1, 7),
    _SnVLanByProtocolRowStatus_Type()
)
snVLanByProtocolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByProtocolRowStatus.setStatus("current")
_SnVLanByProtocolDynamicMask_Type = PortMask
_SnVLanByProtocolDynamicMask_Object = MibTableColumn
snVLanByProtocolDynamicMask = _SnVLanByProtocolDynamicMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 2, 1, 8),
    _SnVLanByProtocolDynamicMask_Type()
)
snVLanByProtocolDynamicMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByProtocolDynamicMask.setStatus("deprecated")


class _SnVLanByProtocolChassisStaticMask_Type(OctetString):
    """Custom type snVLanByProtocolChassisStaticMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_SnVLanByProtocolChassisStaticMask_Type.__name__ = "OctetString"
_SnVLanByProtocolChassisStaticMask_Object = MibTableColumn
snVLanByProtocolChassisStaticMask = _SnVLanByProtocolChassisStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 2, 1, 9),
    _SnVLanByProtocolChassisStaticMask_Type()
)
snVLanByProtocolChassisStaticMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByProtocolChassisStaticMask.setStatus("deprecated")


class _SnVLanByProtocolChassisExcludeMask_Type(OctetString):
    """Custom type snVLanByProtocolChassisExcludeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_SnVLanByProtocolChassisExcludeMask_Type.__name__ = "OctetString"
_SnVLanByProtocolChassisExcludeMask_Object = MibTableColumn
snVLanByProtocolChassisExcludeMask = _SnVLanByProtocolChassisExcludeMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 2, 1, 10),
    _SnVLanByProtocolChassisExcludeMask_Type()
)
snVLanByProtocolChassisExcludeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByProtocolChassisExcludeMask.setStatus("deprecated")


class _SnVLanByProtocolChassisDynamicMask_Type(OctetString):
    """Custom type snVLanByProtocolChassisDynamicMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_SnVLanByProtocolChassisDynamicMask_Type.__name__ = "OctetString"
_SnVLanByProtocolChassisDynamicMask_Object = MibTableColumn
snVLanByProtocolChassisDynamicMask = _SnVLanByProtocolChassisDynamicMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 2, 1, 11),
    _SnVLanByProtocolChassisDynamicMask_Type()
)
snVLanByProtocolChassisDynamicMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByProtocolChassisDynamicMask.setStatus("deprecated")


class _SnVLanByProtocolVLanName_Type(DisplayString):
    """Custom type snVLanByProtocolVLanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnVLanByProtocolVLanName_Type.__name__ = "DisplayString"
_SnVLanByProtocolVLanName_Object = MibTableColumn
snVLanByProtocolVLanName = _SnVLanByProtocolVLanName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 2, 1, 12),
    _SnVLanByProtocolVLanName_Type()
)
snVLanByProtocolVLanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByProtocolVLanName.setStatus("current")
_SnVLanByProtocolStaticPortList_Type = OctetString
_SnVLanByProtocolStaticPortList_Object = MibTableColumn
snVLanByProtocolStaticPortList = _SnVLanByProtocolStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 2, 1, 13),
    _SnVLanByProtocolStaticPortList_Type()
)
snVLanByProtocolStaticPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByProtocolStaticPortList.setStatus("current")
_SnVLanByProtocolExcludePortList_Type = OctetString
_SnVLanByProtocolExcludePortList_Object = MibTableColumn
snVLanByProtocolExcludePortList = _SnVLanByProtocolExcludePortList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 2, 1, 14),
    _SnVLanByProtocolExcludePortList_Type()
)
snVLanByProtocolExcludePortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByProtocolExcludePortList.setStatus("current")
_SnVLanByProtocolDynamicPortList_Type = OctetString
_SnVLanByProtocolDynamicPortList_Object = MibTableColumn
snVLanByProtocolDynamicPortList = _SnVLanByProtocolDynamicPortList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 2, 1, 15),
    _SnVLanByProtocolDynamicPortList_Type()
)
snVLanByProtocolDynamicPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByProtocolDynamicPortList.setStatus("current")
_SnVLanByIpSubnetTable_Object = MibTable
snVLanByIpSubnetTable = _SnVLanByIpSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    snVLanByIpSubnetTable.setStatus("current")
_SnVLanByIpSubnetEntry_Object = MibTableRow
snVLanByIpSubnetEntry = _SnVLanByIpSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 3, 1)
)
snVLanByIpSubnetEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByIpSubnetVLanId"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByIpSubnetIpAddress"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByIpSubnetSubnetMask"),
)
if mibBuilder.loadTexts:
    snVLanByIpSubnetEntry.setStatus("current")


class _SnVLanByIpSubnetVLanId_Type(Integer32):
    """Custom type snVLanByIpSubnetVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SnVLanByIpSubnetVLanId_Type.__name__ = "Integer32"
_SnVLanByIpSubnetVLanId_Object = MibTableColumn
snVLanByIpSubnetVLanId = _SnVLanByIpSubnetVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 3, 1, 1),
    _SnVLanByIpSubnetVLanId_Type()
)
snVLanByIpSubnetVLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByIpSubnetVLanId.setStatus("current")
_SnVLanByIpSubnetIpAddress_Type = IpAddress
_SnVLanByIpSubnetIpAddress_Object = MibTableColumn
snVLanByIpSubnetIpAddress = _SnVLanByIpSubnetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 3, 1, 2),
    _SnVLanByIpSubnetIpAddress_Type()
)
snVLanByIpSubnetIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByIpSubnetIpAddress.setStatus("current")
_SnVLanByIpSubnetSubnetMask_Type = IpAddress
_SnVLanByIpSubnetSubnetMask_Object = MibTableColumn
snVLanByIpSubnetSubnetMask = _SnVLanByIpSubnetSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 3, 1, 3),
    _SnVLanByIpSubnetSubnetMask_Type()
)
snVLanByIpSubnetSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByIpSubnetSubnetMask.setStatus("current")


class _SnVLanByIpSubnetDynamic_Type(Integer32):
    """Custom type snVLanByIpSubnetDynamic based on Integer32"""
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


_SnVLanByIpSubnetDynamic_Type.__name__ = "Integer32"
_SnVLanByIpSubnetDynamic_Object = MibTableColumn
snVLanByIpSubnetDynamic = _SnVLanByIpSubnetDynamic_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 3, 1, 4),
    _SnVLanByIpSubnetDynamic_Type()
)
snVLanByIpSubnetDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpSubnetDynamic.setStatus("current")
_SnVLanByIpSubnetStaticMask_Type = PortMask
_SnVLanByIpSubnetStaticMask_Object = MibTableColumn
snVLanByIpSubnetStaticMask = _SnVLanByIpSubnetStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 3, 1, 5),
    _SnVLanByIpSubnetStaticMask_Type()
)
snVLanByIpSubnetStaticMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpSubnetStaticMask.setStatus("deprecated")
_SnVLanByIpSubnetExcludeMask_Type = PortMask
_SnVLanByIpSubnetExcludeMask_Object = MibTableColumn
snVLanByIpSubnetExcludeMask = _SnVLanByIpSubnetExcludeMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 3, 1, 6),
    _SnVLanByIpSubnetExcludeMask_Type()
)
snVLanByIpSubnetExcludeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpSubnetExcludeMask.setStatus("deprecated")


class _SnVLanByIpSubnetRouterIntf_Type(Integer32):
    """Custom type snVLanByIpSubnetRouterIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SnVLanByIpSubnetRouterIntf_Type.__name__ = "Integer32"
_SnVLanByIpSubnetRouterIntf_Object = MibTableColumn
snVLanByIpSubnetRouterIntf = _SnVLanByIpSubnetRouterIntf_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 3, 1, 7),
    _SnVLanByIpSubnetRouterIntf_Type()
)
snVLanByIpSubnetRouterIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpSubnetRouterIntf.setStatus("current")


class _SnVLanByIpSubnetRowStatus_Type(Integer32):
    """Custom type snVLanByIpSubnetRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("modify", 5),
          ("other", 1),
          ("valid", 2))
    )


_SnVLanByIpSubnetRowStatus_Type.__name__ = "Integer32"
_SnVLanByIpSubnetRowStatus_Object = MibTableColumn
snVLanByIpSubnetRowStatus = _SnVLanByIpSubnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 3, 1, 8),
    _SnVLanByIpSubnetRowStatus_Type()
)
snVLanByIpSubnetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpSubnetRowStatus.setStatus("current")
_SnVLanByIpSubnetDynamicMask_Type = PortMask
_SnVLanByIpSubnetDynamicMask_Object = MibTableColumn
snVLanByIpSubnetDynamicMask = _SnVLanByIpSubnetDynamicMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 3, 1, 9),
    _SnVLanByIpSubnetDynamicMask_Type()
)
snVLanByIpSubnetDynamicMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByIpSubnetDynamicMask.setStatus("deprecated")


class _SnVLanByIpSubnetChassisStaticMask_Type(OctetString):
    """Custom type snVLanByIpSubnetChassisStaticMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_SnVLanByIpSubnetChassisStaticMask_Type.__name__ = "OctetString"
_SnVLanByIpSubnetChassisStaticMask_Object = MibTableColumn
snVLanByIpSubnetChassisStaticMask = _SnVLanByIpSubnetChassisStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 3, 1, 10),
    _SnVLanByIpSubnetChassisStaticMask_Type()
)
snVLanByIpSubnetChassisStaticMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpSubnetChassisStaticMask.setStatus("deprecated")


class _SnVLanByIpSubnetChassisExcludeMask_Type(OctetString):
    """Custom type snVLanByIpSubnetChassisExcludeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_SnVLanByIpSubnetChassisExcludeMask_Type.__name__ = "OctetString"
_SnVLanByIpSubnetChassisExcludeMask_Object = MibTableColumn
snVLanByIpSubnetChassisExcludeMask = _SnVLanByIpSubnetChassisExcludeMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 3, 1, 11),
    _SnVLanByIpSubnetChassisExcludeMask_Type()
)
snVLanByIpSubnetChassisExcludeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpSubnetChassisExcludeMask.setStatus("deprecated")


class _SnVLanByIpSubnetChassisDynamicMask_Type(OctetString):
    """Custom type snVLanByIpSubnetChassisDynamicMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_SnVLanByIpSubnetChassisDynamicMask_Type.__name__ = "OctetString"
_SnVLanByIpSubnetChassisDynamicMask_Object = MibTableColumn
snVLanByIpSubnetChassisDynamicMask = _SnVLanByIpSubnetChassisDynamicMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 3, 1, 12),
    _SnVLanByIpSubnetChassisDynamicMask_Type()
)
snVLanByIpSubnetChassisDynamicMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByIpSubnetChassisDynamicMask.setStatus("deprecated")


class _SnVLanByIpSubnetVLanName_Type(DisplayString):
    """Custom type snVLanByIpSubnetVLanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnVLanByIpSubnetVLanName_Type.__name__ = "DisplayString"
_SnVLanByIpSubnetVLanName_Object = MibTableColumn
snVLanByIpSubnetVLanName = _SnVLanByIpSubnetVLanName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 3, 1, 13),
    _SnVLanByIpSubnetVLanName_Type()
)
snVLanByIpSubnetVLanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpSubnetVLanName.setStatus("current")
_SnVLanByIpSubnetStaticPortList_Type = OctetString
_SnVLanByIpSubnetStaticPortList_Object = MibTableColumn
snVLanByIpSubnetStaticPortList = _SnVLanByIpSubnetStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 3, 1, 14),
    _SnVLanByIpSubnetStaticPortList_Type()
)
snVLanByIpSubnetStaticPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpSubnetStaticPortList.setStatus("current")
_SnVLanByIpSubnetExcludePortList_Type = OctetString
_SnVLanByIpSubnetExcludePortList_Object = MibTableColumn
snVLanByIpSubnetExcludePortList = _SnVLanByIpSubnetExcludePortList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 3, 1, 15),
    _SnVLanByIpSubnetExcludePortList_Type()
)
snVLanByIpSubnetExcludePortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpSubnetExcludePortList.setStatus("current")
_SnVLanByIpSubnetDynamicPortList_Type = OctetString
_SnVLanByIpSubnetDynamicPortList_Object = MibTableColumn
snVLanByIpSubnetDynamicPortList = _SnVLanByIpSubnetDynamicPortList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 3, 1, 16),
    _SnVLanByIpSubnetDynamicPortList_Type()
)
snVLanByIpSubnetDynamicPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByIpSubnetDynamicPortList.setStatus("current")
_SnVLanByIpxNetTable_Object = MibTable
snVLanByIpxNetTable = _SnVLanByIpxNetTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    snVLanByIpxNetTable.setStatus("current")
_SnVLanByIpxNetEntry_Object = MibTableRow
snVLanByIpxNetEntry = _SnVLanByIpxNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 4, 1)
)
snVLanByIpxNetEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByIpxNetVLanId"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByIpxNetNetworkNum"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByIpxNetFrameType"),
)
if mibBuilder.loadTexts:
    snVLanByIpxNetEntry.setStatus("current")


class _SnVLanByIpxNetVLanId_Type(Integer32):
    """Custom type snVLanByIpxNetVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SnVLanByIpxNetVLanId_Type.__name__ = "Integer32"
_SnVLanByIpxNetVLanId_Object = MibTableColumn
snVLanByIpxNetVLanId = _SnVLanByIpxNetVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 4, 1, 1),
    _SnVLanByIpxNetVLanId_Type()
)
snVLanByIpxNetVLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByIpxNetVLanId.setStatus("current")


class _SnVLanByIpxNetNetworkNum_Type(OctetString):
    """Custom type snVLanByIpxNetNetworkNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SnVLanByIpxNetNetworkNum_Type.__name__ = "OctetString"
_SnVLanByIpxNetNetworkNum_Object = MibTableColumn
snVLanByIpxNetNetworkNum = _SnVLanByIpxNetNetworkNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 4, 1, 2),
    _SnVLanByIpxNetNetworkNum_Type()
)
snVLanByIpxNetNetworkNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByIpxNetNetworkNum.setStatus("current")


class _SnVLanByIpxNetFrameType_Type(Integer32):
    """Custom type snVLanByIpxNetFrameType based on Integer32"""
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
        *(("ipxEthernet8022", 1),
          ("ipxEthernet8023", 2),
          ("ipxEthernetII", 3),
          ("ipxEthernetSnap", 4),
          ("notApplicable", 0))
    )


_SnVLanByIpxNetFrameType_Type.__name__ = "Integer32"
_SnVLanByIpxNetFrameType_Object = MibTableColumn
snVLanByIpxNetFrameType = _SnVLanByIpxNetFrameType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 4, 1, 3),
    _SnVLanByIpxNetFrameType_Type()
)
snVLanByIpxNetFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByIpxNetFrameType.setStatus("current")


class _SnVLanByIpxNetDynamic_Type(Integer32):
    """Custom type snVLanByIpxNetDynamic based on Integer32"""
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


_SnVLanByIpxNetDynamic_Type.__name__ = "Integer32"
_SnVLanByIpxNetDynamic_Object = MibTableColumn
snVLanByIpxNetDynamic = _SnVLanByIpxNetDynamic_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 4, 1, 4),
    _SnVLanByIpxNetDynamic_Type()
)
snVLanByIpxNetDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpxNetDynamic.setStatus("current")
_SnVLanByIpxNetStaticMask_Type = PortMask
_SnVLanByIpxNetStaticMask_Object = MibTableColumn
snVLanByIpxNetStaticMask = _SnVLanByIpxNetStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 4, 1, 5),
    _SnVLanByIpxNetStaticMask_Type()
)
snVLanByIpxNetStaticMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpxNetStaticMask.setStatus("deprecated")
_SnVLanByIpxNetExcludeMask_Type = PortMask
_SnVLanByIpxNetExcludeMask_Object = MibTableColumn
snVLanByIpxNetExcludeMask = _SnVLanByIpxNetExcludeMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 4, 1, 6),
    _SnVLanByIpxNetExcludeMask_Type()
)
snVLanByIpxNetExcludeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpxNetExcludeMask.setStatus("deprecated")


class _SnVLanByIpxNetRouterIntf_Type(Integer32):
    """Custom type snVLanByIpxNetRouterIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SnVLanByIpxNetRouterIntf_Type.__name__ = "Integer32"
_SnVLanByIpxNetRouterIntf_Object = MibTableColumn
snVLanByIpxNetRouterIntf = _SnVLanByIpxNetRouterIntf_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 4, 1, 7),
    _SnVLanByIpxNetRouterIntf_Type()
)
snVLanByIpxNetRouterIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpxNetRouterIntf.setStatus("current")


class _SnVLanByIpxNetRowStatus_Type(Integer32):
    """Custom type snVLanByIpxNetRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("modify", 5),
          ("other", 1),
          ("valid", 2))
    )


_SnVLanByIpxNetRowStatus_Type.__name__ = "Integer32"
_SnVLanByIpxNetRowStatus_Object = MibTableColumn
snVLanByIpxNetRowStatus = _SnVLanByIpxNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 4, 1, 8),
    _SnVLanByIpxNetRowStatus_Type()
)
snVLanByIpxNetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpxNetRowStatus.setStatus("current")
_SnVLanByIpxNetDynamicMask_Type = PortMask
_SnVLanByIpxNetDynamicMask_Object = MibTableColumn
snVLanByIpxNetDynamicMask = _SnVLanByIpxNetDynamicMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 4, 1, 9),
    _SnVLanByIpxNetDynamicMask_Type()
)
snVLanByIpxNetDynamicMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByIpxNetDynamicMask.setStatus("deprecated")


class _SnVLanByIpxNetChassisStaticMask_Type(OctetString):
    """Custom type snVLanByIpxNetChassisStaticMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_SnVLanByIpxNetChassisStaticMask_Type.__name__ = "OctetString"
_SnVLanByIpxNetChassisStaticMask_Object = MibTableColumn
snVLanByIpxNetChassisStaticMask = _SnVLanByIpxNetChassisStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 4, 1, 10),
    _SnVLanByIpxNetChassisStaticMask_Type()
)
snVLanByIpxNetChassisStaticMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpxNetChassisStaticMask.setStatus("deprecated")


class _SnVLanByIpxNetChassisExcludeMask_Type(OctetString):
    """Custom type snVLanByIpxNetChassisExcludeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_SnVLanByIpxNetChassisExcludeMask_Type.__name__ = "OctetString"
_SnVLanByIpxNetChassisExcludeMask_Object = MibTableColumn
snVLanByIpxNetChassisExcludeMask = _SnVLanByIpxNetChassisExcludeMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 4, 1, 11),
    _SnVLanByIpxNetChassisExcludeMask_Type()
)
snVLanByIpxNetChassisExcludeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpxNetChassisExcludeMask.setStatus("deprecated")


class _SnVLanByIpxNetChassisDynamicMask_Type(OctetString):
    """Custom type snVLanByIpxNetChassisDynamicMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_SnVLanByIpxNetChassisDynamicMask_Type.__name__ = "OctetString"
_SnVLanByIpxNetChassisDynamicMask_Object = MibTableColumn
snVLanByIpxNetChassisDynamicMask = _SnVLanByIpxNetChassisDynamicMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 4, 1, 12),
    _SnVLanByIpxNetChassisDynamicMask_Type()
)
snVLanByIpxNetChassisDynamicMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByIpxNetChassisDynamicMask.setStatus("deprecated")


class _SnVLanByIpxNetVLanName_Type(DisplayString):
    """Custom type snVLanByIpxNetVLanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnVLanByIpxNetVLanName_Type.__name__ = "DisplayString"
_SnVLanByIpxNetVLanName_Object = MibTableColumn
snVLanByIpxNetVLanName = _SnVLanByIpxNetVLanName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 4, 1, 13),
    _SnVLanByIpxNetVLanName_Type()
)
snVLanByIpxNetVLanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpxNetVLanName.setStatus("current")
_SnVLanByIpxNetStaticPortList_Type = OctetString
_SnVLanByIpxNetStaticPortList_Object = MibTableColumn
snVLanByIpxNetStaticPortList = _SnVLanByIpxNetStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 4, 1, 14),
    _SnVLanByIpxNetStaticPortList_Type()
)
snVLanByIpxNetStaticPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpxNetStaticPortList.setStatus("current")
_SnVLanByIpxNetExcludePortList_Type = OctetString
_SnVLanByIpxNetExcludePortList_Object = MibTableColumn
snVLanByIpxNetExcludePortList = _SnVLanByIpxNetExcludePortList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 4, 1, 15),
    _SnVLanByIpxNetExcludePortList_Type()
)
snVLanByIpxNetExcludePortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByIpxNetExcludePortList.setStatus("current")
_SnVLanByIpxNetDynamicPortList_Type = OctetString
_SnVLanByIpxNetDynamicPortList_Object = MibTableColumn
snVLanByIpxNetDynamicPortList = _SnVLanByIpxNetDynamicPortList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 4, 1, 16),
    _SnVLanByIpxNetDynamicPortList_Type()
)
snVLanByIpxNetDynamicPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByIpxNetDynamicPortList.setStatus("current")
_SnVLanByATCableTable_Object = MibTable
snVLanByATCableTable = _SnVLanByATCableTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    snVLanByATCableTable.setStatus("current")
_SnVLanByATCableEntry_Object = MibTableRow
snVLanByATCableEntry = _SnVLanByATCableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 5, 1)
)
snVLanByATCableEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByATCableVLanId"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByATCableIndex"),
)
if mibBuilder.loadTexts:
    snVLanByATCableEntry.setStatus("current")


class _SnVLanByATCableVLanId_Type(Integer32):
    """Custom type snVLanByATCableVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SnVLanByATCableVLanId_Type.__name__ = "Integer32"
_SnVLanByATCableVLanId_Object = MibTableColumn
snVLanByATCableVLanId = _SnVLanByATCableVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 5, 1, 1),
    _SnVLanByATCableVLanId_Type()
)
snVLanByATCableVLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByATCableVLanId.setStatus("current")
_SnVLanByATCableIndex_Type = Integer32
_SnVLanByATCableIndex_Object = MibTableColumn
snVLanByATCableIndex = _SnVLanByATCableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 5, 1, 2),
    _SnVLanByATCableIndex_Type()
)
snVLanByATCableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByATCableIndex.setStatus("current")


class _SnVLanByATCableRouterIntf_Type(Integer32):
    """Custom type snVLanByATCableRouterIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SnVLanByATCableRouterIntf_Type.__name__ = "Integer32"
_SnVLanByATCableRouterIntf_Object = MibTableColumn
snVLanByATCableRouterIntf = _SnVLanByATCableRouterIntf_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 5, 1, 3),
    _SnVLanByATCableRouterIntf_Type()
)
snVLanByATCableRouterIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByATCableRouterIntf.setStatus("current")


class _SnVLanByATCableRowStatus_Type(Integer32):
    """Custom type snVLanByATCableRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("modify", 5),
          ("other", 1),
          ("valid", 2))
    )


_SnVLanByATCableRowStatus_Type.__name__ = "Integer32"
_SnVLanByATCableRowStatus_Object = MibTableColumn
snVLanByATCableRowStatus = _SnVLanByATCableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 5, 1, 4),
    _SnVLanByATCableRowStatus_Type()
)
snVLanByATCableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByATCableRowStatus.setStatus("current")


class _SnVLanByATCableChassisStaticMask_Type(OctetString):
    """Custom type snVLanByATCableChassisStaticMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_SnVLanByATCableChassisStaticMask_Type.__name__ = "OctetString"
_SnVLanByATCableChassisStaticMask_Object = MibTableColumn
snVLanByATCableChassisStaticMask = _SnVLanByATCableChassisStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 5, 1, 5),
    _SnVLanByATCableChassisStaticMask_Type()
)
snVLanByATCableChassisStaticMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByATCableChassisStaticMask.setStatus("deprecated")


class _SnVLanByATCableVLanName_Type(DisplayString):
    """Custom type snVLanByATCableVLanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnVLanByATCableVLanName_Type.__name__ = "DisplayString"
_SnVLanByATCableVLanName_Object = MibTableColumn
snVLanByATCableVLanName = _SnVLanByATCableVLanName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 5, 1, 6),
    _SnVLanByATCableVLanName_Type()
)
snVLanByATCableVLanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByATCableVLanName.setStatus("current")
_SnVLanByATCableStaticPortList_Type = OctetString
_SnVLanByATCableStaticPortList_Object = MibTableColumn
snVLanByATCableStaticPortList = _SnVLanByATCableStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 5, 1, 7),
    _SnVLanByATCableStaticPortList_Type()
)
snVLanByATCableStaticPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByATCableStaticPortList.setStatus("current")
_SnVLanByPortMemberTable_Object = MibTable
snVLanByPortMemberTable = _SnVLanByPortMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 6)
)
if mibBuilder.loadTexts:
    snVLanByPortMemberTable.setStatus("current")
_SnVLanByPortMemberEntry_Object = MibTableRow
snVLanByPortMemberEntry = _SnVLanByPortMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 6, 1)
)
snVLanByPortMemberEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByPortMemberVLanId"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByPortMemberPortId"),
)
if mibBuilder.loadTexts:
    snVLanByPortMemberEntry.setStatus("current")


class _SnVLanByPortMemberVLanId_Type(Integer32):
    """Custom type snVLanByPortMemberVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SnVLanByPortMemberVLanId_Type.__name__ = "Integer32"
_SnVLanByPortMemberVLanId_Object = MibTableColumn
snVLanByPortMemberVLanId = _SnVLanByPortMemberVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 6, 1, 1),
    _SnVLanByPortMemberVLanId_Type()
)
snVLanByPortMemberVLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortMemberVLanId.setStatus("current")
_SnVLanByPortMemberPortId_Type = InterfaceIndex
_SnVLanByPortMemberPortId_Object = MibTableColumn
snVLanByPortMemberPortId = _SnVLanByPortMemberPortId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 6, 1, 2),
    _SnVLanByPortMemberPortId_Type()
)
snVLanByPortMemberPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortMemberPortId.setStatus("current")


class _SnVLanByPortMemberRowStatus_Type(Integer32):
    """Custom type snVLanByPortMemberRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnVLanByPortMemberRowStatus_Type.__name__ = "Integer32"
_SnVLanByPortMemberRowStatus_Object = MibTableColumn
snVLanByPortMemberRowStatus = _SnVLanByPortMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 6, 1, 3),
    _SnVLanByPortMemberRowStatus_Type()
)
snVLanByPortMemberRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortMemberRowStatus.setStatus("current")


class _SnVLanByPortMemberTagMode_Type(Integer32):
    """Custom type snVLanByPortMemberTagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2))
    )


_SnVLanByPortMemberTagMode_Type.__name__ = "Integer32"
_SnVLanByPortMemberTagMode_Object = MibTableColumn
snVLanByPortMemberTagMode = _SnVLanByPortMemberTagMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 6, 1, 4),
    _SnVLanByPortMemberTagMode_Type()
)
snVLanByPortMemberTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortMemberTagMode.setStatus("current")
_SnVLanByPortCfgTable_Object = MibTable
snVLanByPortCfgTable = _SnVLanByPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7)
)
if mibBuilder.loadTexts:
    snVLanByPortCfgTable.setStatus("current")
_SnVLanByPortCfgEntry_Object = MibTableRow
snVLanByPortCfgEntry = _SnVLanByPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1)
)
snVLanByPortCfgEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snVLanByPortCfgVLanId"),
)
if mibBuilder.loadTexts:
    snVLanByPortCfgEntry.setStatus("current")


class _SnVLanByPortCfgVLanId_Type(Integer32):
    """Custom type snVLanByPortCfgVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SnVLanByPortCfgVLanId_Type.__name__ = "Integer32"
_SnVLanByPortCfgVLanId_Object = MibTableColumn
snVLanByPortCfgVLanId = _SnVLanByPortCfgVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 1),
    _SnVLanByPortCfgVLanId_Type()
)
snVLanByPortCfgVLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortCfgVLanId.setStatus("current")
_SnVLanByPortCfgQos_Type = PortQosTC
_SnVLanByPortCfgQos_Object = MibTableColumn
snVLanByPortCfgQos = _SnVLanByPortCfgQos_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 2),
    _SnVLanByPortCfgQos_Type()
)
snVLanByPortCfgQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortCfgQos.setStatus("current")


class _SnVLanByPortCfgStpMode_Type(Integer32):
    """Custom type snVLanByPortCfgStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enableRstp", 2),
          ("enableStp", 1))
    )


_SnVLanByPortCfgStpMode_Type.__name__ = "Integer32"
_SnVLanByPortCfgStpMode_Object = MibTableColumn
snVLanByPortCfgStpMode = _SnVLanByPortCfgStpMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 3),
    _SnVLanByPortCfgStpMode_Type()
)
snVLanByPortCfgStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortCfgStpMode.setStatus("current")


class _SnVLanByPortCfgStpPriority_Type(Integer32):
    """Custom type snVLanByPortCfgStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnVLanByPortCfgStpPriority_Type.__name__ = "Integer32"
_SnVLanByPortCfgStpPriority_Object = MibTableColumn
snVLanByPortCfgStpPriority = _SnVLanByPortCfgStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 4),
    _SnVLanByPortCfgStpPriority_Type()
)
snVLanByPortCfgStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortCfgStpPriority.setStatus("current")
_SnVLanByPortCfgStpGroupMaxAge_Type = Integer32
_SnVLanByPortCfgStpGroupMaxAge_Object = MibTableColumn
snVLanByPortCfgStpGroupMaxAge = _SnVLanByPortCfgStpGroupMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 5),
    _SnVLanByPortCfgStpGroupMaxAge_Type()
)
snVLanByPortCfgStpGroupMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortCfgStpGroupMaxAge.setStatus("current")
_SnVLanByPortCfgStpGroupHelloTime_Type = Integer32
_SnVLanByPortCfgStpGroupHelloTime_Object = MibTableColumn
snVLanByPortCfgStpGroupHelloTime = _SnVLanByPortCfgStpGroupHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 6),
    _SnVLanByPortCfgStpGroupHelloTime_Type()
)
snVLanByPortCfgStpGroupHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortCfgStpGroupHelloTime.setStatus("current")
_SnVLanByPortCfgStpGroupForwardDelay_Type = Integer32
_SnVLanByPortCfgStpGroupForwardDelay_Object = MibTableColumn
snVLanByPortCfgStpGroupForwardDelay = _SnVLanByPortCfgStpGroupForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 7),
    _SnVLanByPortCfgStpGroupForwardDelay_Type()
)
snVLanByPortCfgStpGroupForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortCfgStpGroupForwardDelay.setStatus("current")
_SnVLanByPortCfgBaseNumPorts_Type = Integer32
_SnVLanByPortCfgBaseNumPorts_Object = MibTableColumn
snVLanByPortCfgBaseNumPorts = _SnVLanByPortCfgBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 8),
    _SnVLanByPortCfgBaseNumPorts_Type()
)
snVLanByPortCfgBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortCfgBaseNumPorts.setStatus("current")


class _SnVLanByPortCfgBaseType_Type(Integer32):
    """Custom type snVLanByPortCfgBaseType based on Integer32"""
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
        *(("sourcerouteOnly", 3),
          ("srt", 4),
          ("transparentOnly", 2),
          ("unknown", 1))
    )


_SnVLanByPortCfgBaseType_Type.__name__ = "Integer32"
_SnVLanByPortCfgBaseType_Object = MibTableColumn
snVLanByPortCfgBaseType = _SnVLanByPortCfgBaseType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 9),
    _SnVLanByPortCfgBaseType_Type()
)
snVLanByPortCfgBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortCfgBaseType.setStatus("current")


class _SnVLanByPortCfgStpProtocolSpecification_Type(Integer32):
    """Custom type snVLanByPortCfgStpProtocolSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decLb100", 2),
          ("ieee8021d", 3),
          ("unknown", 1))
    )


_SnVLanByPortCfgStpProtocolSpecification_Type.__name__ = "Integer32"
_SnVLanByPortCfgStpProtocolSpecification_Object = MibTableColumn
snVLanByPortCfgStpProtocolSpecification = _SnVLanByPortCfgStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 10),
    _SnVLanByPortCfgStpProtocolSpecification_Type()
)
snVLanByPortCfgStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortCfgStpProtocolSpecification.setStatus("current")
_SnVLanByPortCfgStpMaxAge_Type = Timeout
_SnVLanByPortCfgStpMaxAge_Object = MibTableColumn
snVLanByPortCfgStpMaxAge = _SnVLanByPortCfgStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 11),
    _SnVLanByPortCfgStpMaxAge_Type()
)
snVLanByPortCfgStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortCfgStpMaxAge.setStatus("current")
_SnVLanByPortCfgStpHelloTime_Type = Timeout
_SnVLanByPortCfgStpHelloTime_Object = MibTableColumn
snVLanByPortCfgStpHelloTime = _SnVLanByPortCfgStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 12),
    _SnVLanByPortCfgStpHelloTime_Type()
)
snVLanByPortCfgStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortCfgStpHelloTime.setStatus("current")
_SnVLanByPortCfgStpHoldTime_Type = Integer32
_SnVLanByPortCfgStpHoldTime_Object = MibTableColumn
snVLanByPortCfgStpHoldTime = _SnVLanByPortCfgStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 13),
    _SnVLanByPortCfgStpHoldTime_Type()
)
snVLanByPortCfgStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortCfgStpHoldTime.setStatus("current")
_SnVLanByPortCfgStpForwardDelay_Type = Timeout
_SnVLanByPortCfgStpForwardDelay_Object = MibTableColumn
snVLanByPortCfgStpForwardDelay = _SnVLanByPortCfgStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 14),
    _SnVLanByPortCfgStpForwardDelay_Type()
)
snVLanByPortCfgStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortCfgStpForwardDelay.setStatus("current")
_SnVLanByPortCfgStpTimeSinceTopologyChange_Type = TimeTicks
_SnVLanByPortCfgStpTimeSinceTopologyChange_Object = MibTableColumn
snVLanByPortCfgStpTimeSinceTopologyChange = _SnVLanByPortCfgStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 15),
    _SnVLanByPortCfgStpTimeSinceTopologyChange_Type()
)
snVLanByPortCfgStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortCfgStpTimeSinceTopologyChange.setStatus("current")
_SnVLanByPortCfgStpTopChanges_Type = Counter32
_SnVLanByPortCfgStpTopChanges_Object = MibTableColumn
snVLanByPortCfgStpTopChanges = _SnVLanByPortCfgStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 16),
    _SnVLanByPortCfgStpTopChanges_Type()
)
snVLanByPortCfgStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortCfgStpTopChanges.setStatus("current")
_SnVLanByPortCfgStpRootCost_Type = Integer32
_SnVLanByPortCfgStpRootCost_Object = MibTableColumn
snVLanByPortCfgStpRootCost = _SnVLanByPortCfgStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 17),
    _SnVLanByPortCfgStpRootCost_Type()
)
snVLanByPortCfgStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortCfgStpRootCost.setStatus("current")
_SnVLanByPortCfgStpRootPort_Type = Integer32
_SnVLanByPortCfgStpRootPort_Object = MibTableColumn
snVLanByPortCfgStpRootPort = _SnVLanByPortCfgStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 18),
    _SnVLanByPortCfgStpRootPort_Type()
)
snVLanByPortCfgStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortCfgStpRootPort.setStatus("current")
_SnVLanByPortCfgStpDesignatedRoot_Type = BridgeId
_SnVLanByPortCfgStpDesignatedRoot_Object = MibTableColumn
snVLanByPortCfgStpDesignatedRoot = _SnVLanByPortCfgStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 19),
    _SnVLanByPortCfgStpDesignatedRoot_Type()
)
snVLanByPortCfgStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortCfgStpDesignatedRoot.setStatus("current")
_SnVLanByPortCfgBaseBridgeAddress_Type = MacAddress
_SnVLanByPortCfgBaseBridgeAddress_Object = MibTableColumn
snVLanByPortCfgBaseBridgeAddress = _SnVLanByPortCfgBaseBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 20),
    _SnVLanByPortCfgBaseBridgeAddress_Type()
)
snVLanByPortCfgBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortCfgBaseBridgeAddress.setStatus("current")


class _SnVLanByPortCfgVLanName_Type(DisplayString):
    """Custom type snVLanByPortCfgVLanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnVLanByPortCfgVLanName_Type.__name__ = "DisplayString"
_SnVLanByPortCfgVLanName_Object = MibTableColumn
snVLanByPortCfgVLanName = _SnVLanByPortCfgVLanName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 21),
    _SnVLanByPortCfgVLanName_Type()
)
snVLanByPortCfgVLanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortCfgVLanName.setStatus("current")
_SnVLanByPortCfgRouterIntf_Type = Integer32
_SnVLanByPortCfgRouterIntf_Object = MibTableColumn
snVLanByPortCfgRouterIntf = _SnVLanByPortCfgRouterIntf_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 22),
    _SnVLanByPortCfgRouterIntf_Type()
)
snVLanByPortCfgRouterIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortCfgRouterIntf.setStatus("current")


class _SnVLanByPortCfgRowStatus_Type(Integer32):
    """Custom type snVLanByPortCfgRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnVLanByPortCfgRowStatus_Type.__name__ = "Integer32"
_SnVLanByPortCfgRowStatus_Object = MibTableColumn
snVLanByPortCfgRowStatus = _SnVLanByPortCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 23),
    _SnVLanByPortCfgRowStatus_Type()
)
snVLanByPortCfgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortCfgRowStatus.setStatus("current")


class _SnVLanByPortCfgStpVersion_Type(Integer32):
    """Custom type snVLanByPortCfgStpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 2),
          ("stpCompatible", 0))
    )


_SnVLanByPortCfgStpVersion_Type.__name__ = "Integer32"
_SnVLanByPortCfgStpVersion_Object = MibTableColumn
snVLanByPortCfgStpVersion = _SnVLanByPortCfgStpVersion_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 24),
    _SnVLanByPortCfgStpVersion_Type()
)
snVLanByPortCfgStpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortCfgStpVersion.setStatus("current")
_SnVLanByPortCfgInOctets_Type = Counter64
_SnVLanByPortCfgInOctets_Object = MibTableColumn
snVLanByPortCfgInOctets = _SnVLanByPortCfgInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 25),
    _SnVLanByPortCfgInOctets_Type()
)
snVLanByPortCfgInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanByPortCfgInOctets.setStatus("current")


class _SnVLanByPortCfgTransparentHwFlooding_Type(Integer32):
    """Custom type snVLanByPortCfgTransparentHwFlooding based on Integer32"""
    defaultValue = 0

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


_SnVLanByPortCfgTransparentHwFlooding_Type.__name__ = "Integer32"
_SnVLanByPortCfgTransparentHwFlooding_Object = MibTableColumn
snVLanByPortCfgTransparentHwFlooding = _SnVLanByPortCfgTransparentHwFlooding_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 7, 1, 26),
    _SnVLanByPortCfgTransparentHwFlooding_Type()
)
snVLanByPortCfgTransparentHwFlooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snVLanByPortCfgTransparentHwFlooding.setStatus("current")
_BrcdVlanExtStatsTable_Object = MibTable
brcdVlanExtStatsTable = _BrcdVlanExtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 8)
)
if mibBuilder.loadTexts:
    brcdVlanExtStatsTable.setStatus("current")
_BrcdVlanExtStatsEntry_Object = MibTableRow
brcdVlanExtStatsEntry = _BrcdVlanExtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 8, 1)
)
brcdVlanExtStatsEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "brcdVlanExtStatsVlanId"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "brcdVlanExtStatsIfIndex"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "brcdVlanExtStatsPriorityId"),
)
if mibBuilder.loadTexts:
    brcdVlanExtStatsEntry.setStatus("current")
_BrcdVlanExtStatsVlanId_Type = BrcdVlanIdTC
_BrcdVlanExtStatsVlanId_Object = MibTableColumn
brcdVlanExtStatsVlanId = _BrcdVlanExtStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 8, 1, 1),
    _BrcdVlanExtStatsVlanId_Type()
)
brcdVlanExtStatsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdVlanExtStatsVlanId.setStatus("current")
_BrcdVlanExtStatsIfIndex_Type = InterfaceIndex
_BrcdVlanExtStatsIfIndex_Object = MibTableColumn
brcdVlanExtStatsIfIndex = _BrcdVlanExtStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 8, 1, 2),
    _BrcdVlanExtStatsIfIndex_Type()
)
brcdVlanExtStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdVlanExtStatsIfIndex.setStatus("current")
_BrcdVlanExtStatsPriorityId_Type = PortPriorityTC
_BrcdVlanExtStatsPriorityId_Object = MibTableColumn
brcdVlanExtStatsPriorityId = _BrcdVlanExtStatsPriorityId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 8, 1, 3),
    _BrcdVlanExtStatsPriorityId_Type()
)
brcdVlanExtStatsPriorityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdVlanExtStatsPriorityId.setStatus("current")
_BrcdVlanExtStatsInSwitchedPkts_Type = Counter64
_BrcdVlanExtStatsInSwitchedPkts_Object = MibTableColumn
brcdVlanExtStatsInSwitchedPkts = _BrcdVlanExtStatsInSwitchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 8, 1, 4),
    _BrcdVlanExtStatsInSwitchedPkts_Type()
)
brcdVlanExtStatsInSwitchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVlanExtStatsInSwitchedPkts.setStatus("current")
_BrcdVlanExtStatsInRoutedPkts_Type = Counter64
_BrcdVlanExtStatsInRoutedPkts_Object = MibTableColumn
brcdVlanExtStatsInRoutedPkts = _BrcdVlanExtStatsInRoutedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 8, 1, 5),
    _BrcdVlanExtStatsInRoutedPkts_Type()
)
brcdVlanExtStatsInRoutedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVlanExtStatsInRoutedPkts.setStatus("current")
_BrcdVlanExtStatsInPkts_Type = Counter64
_BrcdVlanExtStatsInPkts_Object = MibTableColumn
brcdVlanExtStatsInPkts = _BrcdVlanExtStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 8, 1, 6),
    _BrcdVlanExtStatsInPkts_Type()
)
brcdVlanExtStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVlanExtStatsInPkts.setStatus("current")
_BrcdVlanExtStatsOutSwitchedPkts_Type = Counter64
_BrcdVlanExtStatsOutSwitchedPkts_Object = MibTableColumn
brcdVlanExtStatsOutSwitchedPkts = _BrcdVlanExtStatsOutSwitchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 8, 1, 7),
    _BrcdVlanExtStatsOutSwitchedPkts_Type()
)
brcdVlanExtStatsOutSwitchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVlanExtStatsOutSwitchedPkts.setStatus("current")
_BrcdVlanExtStatsOutRoutedPkts_Type = Counter64
_BrcdVlanExtStatsOutRoutedPkts_Object = MibTableColumn
brcdVlanExtStatsOutRoutedPkts = _BrcdVlanExtStatsOutRoutedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 8, 1, 8),
    _BrcdVlanExtStatsOutRoutedPkts_Type()
)
brcdVlanExtStatsOutRoutedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVlanExtStatsOutRoutedPkts.setStatus("current")
_BrcdVlanExtStatsOutPkts_Type = Counter64
_BrcdVlanExtStatsOutPkts_Object = MibTableColumn
brcdVlanExtStatsOutPkts = _BrcdVlanExtStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 8, 1, 9),
    _BrcdVlanExtStatsOutPkts_Type()
)
brcdVlanExtStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVlanExtStatsOutPkts.setStatus("current")
_BrcdVlanExtStatsInSwitchedOctets_Type = Counter64
_BrcdVlanExtStatsInSwitchedOctets_Object = MibTableColumn
brcdVlanExtStatsInSwitchedOctets = _BrcdVlanExtStatsInSwitchedOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 8, 1, 10),
    _BrcdVlanExtStatsInSwitchedOctets_Type()
)
brcdVlanExtStatsInSwitchedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVlanExtStatsInSwitchedOctets.setStatus("current")
_BrcdVlanExtStatsInRoutedOctets_Type = Counter64
_BrcdVlanExtStatsInRoutedOctets_Object = MibTableColumn
brcdVlanExtStatsInRoutedOctets = _BrcdVlanExtStatsInRoutedOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 8, 1, 11),
    _BrcdVlanExtStatsInRoutedOctets_Type()
)
brcdVlanExtStatsInRoutedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVlanExtStatsInRoutedOctets.setStatus("current")
_BrcdVlanExtStatsInOctets_Type = Counter64
_BrcdVlanExtStatsInOctets_Object = MibTableColumn
brcdVlanExtStatsInOctets = _BrcdVlanExtStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 8, 1, 12),
    _BrcdVlanExtStatsInOctets_Type()
)
brcdVlanExtStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVlanExtStatsInOctets.setStatus("current")
_BrcdVlanExtStatsOutSwitchedOctets_Type = Counter64
_BrcdVlanExtStatsOutSwitchedOctets_Object = MibTableColumn
brcdVlanExtStatsOutSwitchedOctets = _BrcdVlanExtStatsOutSwitchedOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 8, 1, 13),
    _BrcdVlanExtStatsOutSwitchedOctets_Type()
)
brcdVlanExtStatsOutSwitchedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVlanExtStatsOutSwitchedOctets.setStatus("current")
_BrcdVlanExtStatsOutRoutedOctets_Type = Counter64
_BrcdVlanExtStatsOutRoutedOctets_Object = MibTableColumn
brcdVlanExtStatsOutRoutedOctets = _BrcdVlanExtStatsOutRoutedOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 8, 1, 14),
    _BrcdVlanExtStatsOutRoutedOctets_Type()
)
brcdVlanExtStatsOutRoutedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVlanExtStatsOutRoutedOctets.setStatus("current")
_BrcdVlanExtStatsOutOctets_Type = Counter64
_BrcdVlanExtStatsOutOctets_Object = MibTableColumn
brcdVlanExtStatsOutOctets = _BrcdVlanExtStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 2, 8, 1, 15),
    _BrcdVlanExtStatsOutOctets_Type()
)
brcdVlanExtStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdVlanExtStatsOutOctets.setStatus("current")
_SnSwPortInfo_ObjectIdentity = ObjectIdentity
snSwPortInfo = _SnSwPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3)
)
_SnSwPortInfoTable_Object = MibTable
snSwPortInfoTable = _SnSwPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    snSwPortInfoTable.setStatus("deprecated")
_SnSwPortInfoEntry_Object = MibTableRow
snSwPortInfoEntry = _SnSwPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1)
)
snSwPortInfoEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwPortInfoPortNum"),
)
if mibBuilder.loadTexts:
    snSwPortInfoEntry.setStatus("deprecated")
_SnSwPortInfoPortNum_Type = Integer32
_SnSwPortInfoPortNum_Object = MibTableColumn
snSwPortInfoPortNum = _SnSwPortInfoPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 1),
    _SnSwPortInfoPortNum_Type()
)
snSwPortInfoPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortInfoPortNum.setStatus("deprecated")


class _SnSwPortInfoMonitorMode_Type(Integer32):
    """Custom type snSwPortInfoMonitorMode based on Integer32"""
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
        *(("both", 3),
          ("disabled", 0),
          ("input", 1),
          ("output", 2))
    )


_SnSwPortInfoMonitorMode_Type.__name__ = "Integer32"
_SnSwPortInfoMonitorMode_Object = MibTableColumn
snSwPortInfoMonitorMode = _SnSwPortInfoMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 2),
    _SnSwPortInfoMonitorMode_Type()
)
snSwPortInfoMonitorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortInfoMonitorMode.setStatus("deprecated")


class _SnSwPortInfoTagMode_Type(Integer32):
    """Custom type snSwPortInfoTagMode based on Integer32"""
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
        *(("auto", 3),
          ("disabled", 4),
          ("tagged", 1),
          ("untagged", 2))
    )


_SnSwPortInfoTagMode_Type.__name__ = "Integer32"
_SnSwPortInfoTagMode_Object = MibTableColumn
snSwPortInfoTagMode = _SnSwPortInfoTagMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 3),
    _SnSwPortInfoTagMode_Type()
)
snSwPortInfoTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortInfoTagMode.setStatus("deprecated")


class _SnSwPortInfoChnMode_Type(Integer32):
    """Custom type snSwPortInfoChnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 2),
          ("halfDuplex", 1),
          ("none", 0))
    )


_SnSwPortInfoChnMode_Type.__name__ = "Integer32"
_SnSwPortInfoChnMode_Object = MibTableColumn
snSwPortInfoChnMode = _SnSwPortInfoChnMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 4),
    _SnSwPortInfoChnMode_Type()
)
snSwPortInfoChnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortInfoChnMode.setStatus("deprecated")


class _SnSwPortInfoSpeed_Type(Integer32):
    """Custom type snSwPortInfoSpeed based on Integer32"""
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
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("s100M", 3),
          ("s10G", 7),
          ("s10M", 2),
          ("s155M", 6),
          ("s16G", 11),
          ("s1G", 4),
          ("s1GM", 5),
          ("s2488M", 9),
          ("s2500M", 14),
          ("s40G", 13),
          ("s622M", 8),
          ("s9953M", 10),
          ("sAutoSense", 1))
    )


_SnSwPortInfoSpeed_Type.__name__ = "Integer32"
_SnSwPortInfoSpeed_Object = MibTableColumn
snSwPortInfoSpeed = _SnSwPortInfoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 5),
    _SnSwPortInfoSpeed_Type()
)
snSwPortInfoSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortInfoSpeed.setStatus("deprecated")


class _SnSwPortInfoMediaType_Type(Integer32):
    """Custom type snSwPortInfoMediaType based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("m10000BaseFX", 12),
          ("m10000BaseTX", 18),
          ("m1000BaseFX", 4),
          ("m1000BaseTX", 7),
          ("m100BaseFX", 3),
          ("m100BaseTX", 2),
          ("m100GBaseFX", 15),
          ("m155ATM", 6),
          ("m155POS", 9),
          ("m16GStacking", 14),
          ("m2488POS", 11),
          ("m2500BaseTX", 19),
          ("m40GBaseFX", 17),
          ("m40GStacking", 16),
          ("m622ATM", 8),
          ("m622POS", 10),
          ("m9953POS", 13),
          ("mT3", 5),
          ("other", 1))
    )


_SnSwPortInfoMediaType_Type.__name__ = "Integer32"
_SnSwPortInfoMediaType_Object = MibTableColumn
snSwPortInfoMediaType = _SnSwPortInfoMediaType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 6),
    _SnSwPortInfoMediaType_Type()
)
snSwPortInfoMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortInfoMediaType.setStatus("deprecated")


class _SnSwPortInfoConnectorType_Type(Integer32):
    """Custom type snSwPortInfoConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copper", 2),
          ("fiber", 3),
          ("other", 1))
    )


_SnSwPortInfoConnectorType_Type.__name__ = "Integer32"
_SnSwPortInfoConnectorType_Object = MibTableColumn
snSwPortInfoConnectorType = _SnSwPortInfoConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 7),
    _SnSwPortInfoConnectorType_Type()
)
snSwPortInfoConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortInfoConnectorType.setStatus("deprecated")


class _SnSwPortInfoAdminStatus_Type(Integer32):
    """Custom type snSwPortInfoAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_SnSwPortInfoAdminStatus_Type.__name__ = "Integer32"
_SnSwPortInfoAdminStatus_Object = MibTableColumn
snSwPortInfoAdminStatus = _SnSwPortInfoAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 8),
    _SnSwPortInfoAdminStatus_Type()
)
snSwPortInfoAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortInfoAdminStatus.setStatus("deprecated")


class _SnSwPortInfoLinkStatus_Type(Integer32):
    """Custom type snSwPortInfoLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_SnSwPortInfoLinkStatus_Type.__name__ = "Integer32"
_SnSwPortInfoLinkStatus_Object = MibTableColumn
snSwPortInfoLinkStatus = _SnSwPortInfoLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 9),
    _SnSwPortInfoLinkStatus_Type()
)
snSwPortInfoLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortInfoLinkStatus.setStatus("deprecated")


class _SnSwPortInfoPortQos_Type(Integer32):
    """Custom type snSwPortInfoPortQos based on Integer32"""
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
        *(("level0", 0),
          ("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7))
    )


_SnSwPortInfoPortQos_Type.__name__ = "Integer32"
_SnSwPortInfoPortQos_Object = MibTableColumn
snSwPortInfoPortQos = _SnSwPortInfoPortQos_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 10),
    _SnSwPortInfoPortQos_Type()
)
snSwPortInfoPortQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortInfoPortQos.setStatus("deprecated")
_SnSwPortInfoPhysAddress_Type = PhysAddress
_SnSwPortInfoPhysAddress_Object = MibTableColumn
snSwPortInfoPhysAddress = _SnSwPortInfoPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 11),
    _SnSwPortInfoPhysAddress_Type()
)
snSwPortInfoPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortInfoPhysAddress.setStatus("deprecated")
_SnSwPortStatsInFrames_Type = Counter32
_SnSwPortStatsInFrames_Object = MibTableColumn
snSwPortStatsInFrames = _SnSwPortStatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 12),
    _SnSwPortStatsInFrames_Type()
)
snSwPortStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsInFrames.setStatus("deprecated")
_SnSwPortStatsOutFrames_Type = Counter32
_SnSwPortStatsOutFrames_Object = MibTableColumn
snSwPortStatsOutFrames = _SnSwPortStatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 13),
    _SnSwPortStatsOutFrames_Type()
)
snSwPortStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsOutFrames.setStatus("deprecated")
_SnSwPortStatsAlignErrors_Type = Counter32
_SnSwPortStatsAlignErrors_Object = MibTableColumn
snSwPortStatsAlignErrors = _SnSwPortStatsAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 14),
    _SnSwPortStatsAlignErrors_Type()
)
snSwPortStatsAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsAlignErrors.setStatus("deprecated")
_SnSwPortStatsFCSErrors_Type = Counter32
_SnSwPortStatsFCSErrors_Object = MibTableColumn
snSwPortStatsFCSErrors = _SnSwPortStatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 15),
    _SnSwPortStatsFCSErrors_Type()
)
snSwPortStatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsFCSErrors.setStatus("deprecated")
_SnSwPortStatsMultiColliFrames_Type = Counter32
_SnSwPortStatsMultiColliFrames_Object = MibTableColumn
snSwPortStatsMultiColliFrames = _SnSwPortStatsMultiColliFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 16),
    _SnSwPortStatsMultiColliFrames_Type()
)
snSwPortStatsMultiColliFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsMultiColliFrames.setStatus("deprecated")
_SnSwPortStatsFrameTooLongs_Type = Counter32
_SnSwPortStatsFrameTooLongs_Object = MibTableColumn
snSwPortStatsFrameTooLongs = _SnSwPortStatsFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 17),
    _SnSwPortStatsFrameTooLongs_Type()
)
snSwPortStatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsFrameTooLongs.setStatus("deprecated")
_SnSwPortStatsTxColliFrames_Type = Counter32
_SnSwPortStatsTxColliFrames_Object = MibTableColumn
snSwPortStatsTxColliFrames = _SnSwPortStatsTxColliFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 18),
    _SnSwPortStatsTxColliFrames_Type()
)
snSwPortStatsTxColliFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsTxColliFrames.setStatus("deprecated")
_SnSwPortStatsRxColliFrames_Type = Counter32
_SnSwPortStatsRxColliFrames_Object = MibTableColumn
snSwPortStatsRxColliFrames = _SnSwPortStatsRxColliFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 19),
    _SnSwPortStatsRxColliFrames_Type()
)
snSwPortStatsRxColliFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsRxColliFrames.setStatus("deprecated")
_SnSwPortStatsFrameTooShorts_Type = Counter32
_SnSwPortStatsFrameTooShorts_Object = MibTableColumn
snSwPortStatsFrameTooShorts = _SnSwPortStatsFrameTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 20),
    _SnSwPortStatsFrameTooShorts_Type()
)
snSwPortStatsFrameTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsFrameTooShorts.setStatus("deprecated")


class _SnSwPortLockAddressCount_Type(Integer32):
    """Custom type snSwPortLockAddressCount based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_SnSwPortLockAddressCount_Type.__name__ = "Integer32"
_SnSwPortLockAddressCount_Object = MibTableColumn
snSwPortLockAddressCount = _SnSwPortLockAddressCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 21),
    _SnSwPortLockAddressCount_Type()
)
snSwPortLockAddressCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortLockAddressCount.setStatus("deprecated")


class _SnSwPortStpPortEnable_Type(Integer32):
    """Custom type snSwPortStpPortEnable based on Integer32"""
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


_SnSwPortStpPortEnable_Type.__name__ = "Integer32"
_SnSwPortStpPortEnable_Object = MibTableColumn
snSwPortStpPortEnable = _SnSwPortStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 22),
    _SnSwPortStpPortEnable_Type()
)
snSwPortStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortStpPortEnable.setStatus("deprecated")


class _SnSwPortDhcpGateListId_Type(Integer32):
    """Custom type snSwPortDhcpGateListId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SnSwPortDhcpGateListId_Type.__name__ = "Integer32"
_SnSwPortDhcpGateListId_Object = MibTableColumn
snSwPortDhcpGateListId = _SnSwPortDhcpGateListId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 23),
    _SnSwPortDhcpGateListId_Type()
)
snSwPortDhcpGateListId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortDhcpGateListId.setStatus("deprecated")


class _SnSwPortName_Type(DisplayString):
    """Custom type snSwPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnSwPortName_Type.__name__ = "DisplayString"
_SnSwPortName_Object = MibTableColumn
snSwPortName = _SnSwPortName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 24),
    _SnSwPortName_Type()
)
snSwPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortName.setStatus("deprecated")
_SnSwPortStatsInBcastFrames_Type = Counter32
_SnSwPortStatsInBcastFrames_Object = MibTableColumn
snSwPortStatsInBcastFrames = _SnSwPortStatsInBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 25),
    _SnSwPortStatsInBcastFrames_Type()
)
snSwPortStatsInBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsInBcastFrames.setStatus("deprecated")
_SnSwPortStatsOutBcastFrames_Type = Counter32
_SnSwPortStatsOutBcastFrames_Object = MibTableColumn
snSwPortStatsOutBcastFrames = _SnSwPortStatsOutBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 26),
    _SnSwPortStatsOutBcastFrames_Type()
)
snSwPortStatsOutBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsOutBcastFrames.setStatus("deprecated")
_SnSwPortStatsInMcastFrames_Type = Counter32
_SnSwPortStatsInMcastFrames_Object = MibTableColumn
snSwPortStatsInMcastFrames = _SnSwPortStatsInMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 27),
    _SnSwPortStatsInMcastFrames_Type()
)
snSwPortStatsInMcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsInMcastFrames.setStatus("deprecated")
_SnSwPortStatsOutMcastFrames_Type = Counter32
_SnSwPortStatsOutMcastFrames_Object = MibTableColumn
snSwPortStatsOutMcastFrames = _SnSwPortStatsOutMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 28),
    _SnSwPortStatsOutMcastFrames_Type()
)
snSwPortStatsOutMcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsOutMcastFrames.setStatus("deprecated")
_SnSwPortStatsInDiscard_Type = Counter32
_SnSwPortStatsInDiscard_Object = MibTableColumn
snSwPortStatsInDiscard = _SnSwPortStatsInDiscard_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 29),
    _SnSwPortStatsInDiscard_Type()
)
snSwPortStatsInDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsInDiscard.setStatus("deprecated")
_SnSwPortStatsOutDiscard_Type = Counter32
_SnSwPortStatsOutDiscard_Object = MibTableColumn
snSwPortStatsOutDiscard = _SnSwPortStatsOutDiscard_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 30),
    _SnSwPortStatsOutDiscard_Type()
)
snSwPortStatsOutDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsOutDiscard.setStatus("deprecated")
_SnSwPortStatsMacStations_Type = Integer32
_SnSwPortStatsMacStations_Object = MibTableColumn
snSwPortStatsMacStations = _SnSwPortStatsMacStations_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 31),
    _SnSwPortStatsMacStations_Type()
)
snSwPortStatsMacStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsMacStations.setStatus("deprecated")
_SnSwPortCacheGroupId_Type = Integer32
_SnSwPortCacheGroupId_Object = MibTableColumn
snSwPortCacheGroupId = _SnSwPortCacheGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 32),
    _SnSwPortCacheGroupId_Type()
)
snSwPortCacheGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortCacheGroupId.setStatus("deprecated")
_SnSwPortTransGroupId_Type = Integer32
_SnSwPortTransGroupId_Object = MibTableColumn
snSwPortTransGroupId = _SnSwPortTransGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 33),
    _SnSwPortTransGroupId_Type()
)
snSwPortTransGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortTransGroupId.setStatus("deprecated")


class _SnSwPortInfoAutoNegotiate_Type(Integer32):
    """Custom type snSwPortInfoAutoNegotiate based on Integer32"""
    defaultValue = 3

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
        *(("disabled", 0),
          ("enabled", 1),
          ("global", 3),
          ("negFullAuto", 2),
          ("other", 4))
    )


_SnSwPortInfoAutoNegotiate_Type.__name__ = "Integer32"
_SnSwPortInfoAutoNegotiate_Object = MibTableColumn
snSwPortInfoAutoNegotiate = _SnSwPortInfoAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 34),
    _SnSwPortInfoAutoNegotiate_Type()
)
snSwPortInfoAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortInfoAutoNegotiate.setStatus("deprecated")


class _SnSwPortInfoFlowControl_Type(Integer32):
    """Custom type snSwPortInfoFlowControl based on Integer32"""
    defaultValue = 1

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


_SnSwPortInfoFlowControl_Type.__name__ = "Integer32"
_SnSwPortInfoFlowControl_Object = MibTableColumn
snSwPortInfoFlowControl = _SnSwPortInfoFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 35),
    _SnSwPortInfoFlowControl_Type()
)
snSwPortInfoFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortInfoFlowControl.setStatus("deprecated")


class _SnSwPortInfoGigType_Type(Integer32):
    """Custom type snSwPortInfoGigType based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("m10000BaseER", 8),
          ("m10000BaseLR", 7),
          ("m10000BaseSR", 6),
          ("m1000BaseGBXD", 28),
          ("m1000BaseGBXU", 27),
          ("m1000BaseLH", 2),
          ("m1000BaseLHA", 3),
          ("m1000BaseLHB", 4),
          ("m1000BaseLHX", 25),
          ("m1000BaseLX", 1),
          ("m1000BaseSX", 0),
          ("m1000BaseSX2", 26),
          ("m1000BaseTX", 5),
          ("notApplicable", 255),
          ("sfpCWDM1470nm100Km", 17),
          ("sfpCWDM1470nm80Km", 9),
          ("sfpCWDM1490nm100Km", 18),
          ("sfpCWDM1490nm80Km", 10),
          ("sfpCWDM1510nm100Km", 19),
          ("sfpCWDM1510nm80Km", 11),
          ("sfpCWDM1530nm100Km", 20),
          ("sfpCWDM1530nm80Km", 12),
          ("sfpCWDM1550nm100Km", 21),
          ("sfpCWDM1550nm80Km", 13),
          ("sfpCWDM1570nm100Km", 22),
          ("sfpCWDM1570nm80Km", 14),
          ("sfpCWDM1590nm100Km", 23),
          ("sfpCWDM1590nm80Km", 15),
          ("sfpCWDM1610nm100Km", 24),
          ("sfpCWDM1610nm80Km", 16))
    )


_SnSwPortInfoGigType_Type.__name__ = "Integer32"
_SnSwPortInfoGigType_Object = MibTableColumn
snSwPortInfoGigType = _SnSwPortInfoGigType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 36),
    _SnSwPortInfoGigType_Type()
)
snSwPortInfoGigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortInfoGigType.setStatus("deprecated")
_SnSwPortStatsLinkChange_Type = Counter32
_SnSwPortStatsLinkChange_Object = MibTableColumn
snSwPortStatsLinkChange = _SnSwPortStatsLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 37),
    _SnSwPortStatsLinkChange_Type()
)
snSwPortStatsLinkChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsLinkChange.setStatus("deprecated")
_SnSwPortIfIndex_Type = Integer32
_SnSwPortIfIndex_Object = MibTableColumn
snSwPortIfIndex = _SnSwPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 38),
    _SnSwPortIfIndex_Type()
)
snSwPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortIfIndex.setStatus("deprecated")
_SnSwPortDescr_Type = DisplayString
_SnSwPortDescr_Object = MibTableColumn
snSwPortDescr = _SnSwPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 39),
    _SnSwPortDescr_Type()
)
snSwPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortDescr.setStatus("deprecated")


class _SnSwPortInOctets_Type(OctetString):
    """Custom type snSwPortInOctets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SnSwPortInOctets_Type.__name__ = "OctetString"
_SnSwPortInOctets_Object = MibTableColumn
snSwPortInOctets = _SnSwPortInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 40),
    _SnSwPortInOctets_Type()
)
snSwPortInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortInOctets.setStatus("deprecated")


class _SnSwPortOutOctets_Type(OctetString):
    """Custom type snSwPortOutOctets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SnSwPortOutOctets_Type.__name__ = "OctetString"
_SnSwPortOutOctets_Object = MibTableColumn
snSwPortOutOctets = _SnSwPortOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 41),
    _SnSwPortOutOctets_Type()
)
snSwPortOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortOutOctets.setStatus("deprecated")
_SnSwPortStatsInBitsPerSec_Type = Gauge32
_SnSwPortStatsInBitsPerSec_Object = MibTableColumn
snSwPortStatsInBitsPerSec = _SnSwPortStatsInBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 42),
    _SnSwPortStatsInBitsPerSec_Type()
)
snSwPortStatsInBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsInBitsPerSec.setStatus("deprecated")
_SnSwPortStatsOutBitsPerSec_Type = Gauge32
_SnSwPortStatsOutBitsPerSec_Object = MibTableColumn
snSwPortStatsOutBitsPerSec = _SnSwPortStatsOutBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 43),
    _SnSwPortStatsOutBitsPerSec_Type()
)
snSwPortStatsOutBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsOutBitsPerSec.setStatus("deprecated")
_SnSwPortStatsInPktsPerSec_Type = Gauge32
_SnSwPortStatsInPktsPerSec_Object = MibTableColumn
snSwPortStatsInPktsPerSec = _SnSwPortStatsInPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 44),
    _SnSwPortStatsInPktsPerSec_Type()
)
snSwPortStatsInPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsInPktsPerSec.setStatus("deprecated")
_SnSwPortStatsOutPktsPerSec_Type = Gauge32
_SnSwPortStatsOutPktsPerSec_Object = MibTableColumn
snSwPortStatsOutPktsPerSec = _SnSwPortStatsOutPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 45),
    _SnSwPortStatsOutPktsPerSec_Type()
)
snSwPortStatsOutPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsOutPktsPerSec.setStatus("deprecated")


class _SnSwPortStatsInUtilization_Type(Integer32):
    """Custom type snSwPortStatsInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SnSwPortStatsInUtilization_Type.__name__ = "Integer32"
_SnSwPortStatsInUtilization_Object = MibTableColumn
snSwPortStatsInUtilization = _SnSwPortStatsInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 46),
    _SnSwPortStatsInUtilization_Type()
)
snSwPortStatsInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsInUtilization.setStatus("deprecated")


class _SnSwPortStatsOutUtilization_Type(Integer32):
    """Custom type snSwPortStatsOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SnSwPortStatsOutUtilization_Type.__name__ = "Integer32"
_SnSwPortStatsOutUtilization_Object = MibTableColumn
snSwPortStatsOutUtilization = _SnSwPortStatsOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 47),
    _SnSwPortStatsOutUtilization_Type()
)
snSwPortStatsOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsOutUtilization.setStatus("deprecated")


class _SnSwPortFastSpanPortEnable_Type(Integer32):
    """Custom type snSwPortFastSpanPortEnable based on Integer32"""
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


_SnSwPortFastSpanPortEnable_Type.__name__ = "Integer32"
_SnSwPortFastSpanPortEnable_Object = MibTableColumn
snSwPortFastSpanPortEnable = _SnSwPortFastSpanPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 48),
    _SnSwPortFastSpanPortEnable_Type()
)
snSwPortFastSpanPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortFastSpanPortEnable.setStatus("deprecated")


class _SnSwPortFastSpanUplinkEnable_Type(Integer32):
    """Custom type snSwPortFastSpanUplinkEnable based on Integer32"""
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


_SnSwPortFastSpanUplinkEnable_Type.__name__ = "Integer32"
_SnSwPortFastSpanUplinkEnable_Object = MibTableColumn
snSwPortFastSpanUplinkEnable = _SnSwPortFastSpanUplinkEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 49),
    _SnSwPortFastSpanUplinkEnable_Type()
)
snSwPortFastSpanUplinkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortFastSpanUplinkEnable.setStatus("deprecated")


class _SnSwPortVlanId_Type(Integer32):
    """Custom type snSwPortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SnSwPortVlanId_Type.__name__ = "Integer32"
_SnSwPortVlanId_Object = MibTableColumn
snSwPortVlanId = _SnSwPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 50),
    _SnSwPortVlanId_Type()
)
snSwPortVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortVlanId.setStatus("deprecated")


class _SnSwPortRouteOnly_Type(Integer32):
    """Custom type snSwPortRouteOnly based on Integer32"""
    defaultValue = 0

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


_SnSwPortRouteOnly_Type.__name__ = "Integer32"
_SnSwPortRouteOnly_Object = MibTableColumn
snSwPortRouteOnly = _SnSwPortRouteOnly_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 51),
    _SnSwPortRouteOnly_Type()
)
snSwPortRouteOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortRouteOnly.setStatus("deprecated")


class _SnSwPortPresent_Type(Integer32):
    """Custom type snSwPortPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnSwPortPresent_Type.__name__ = "Integer32"
_SnSwPortPresent_Object = MibTableColumn
snSwPortPresent = _SnSwPortPresent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 52),
    _SnSwPortPresent_Type()
)
snSwPortPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortPresent.setStatus("deprecated")


class _SnSwPortGBICStatus_Type(Integer32):
    """Custom type snSwPortGBICStatus based on Integer32"""
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
        *(("empty", 3),
          ("gbic", 1),
          ("miniGBIC", 2),
          ("other", 4))
    )


_SnSwPortGBICStatus_Type.__name__ = "Integer32"
_SnSwPortGBICStatus_Object = MibTableColumn
snSwPortGBICStatus = _SnSwPortGBICStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 53),
    _SnSwPortGBICStatus_Type()
)
snSwPortGBICStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortGBICStatus.setStatus("deprecated")
_SnSwPortStatsInKiloBitsPerSec_Type = Unsigned32
_SnSwPortStatsInKiloBitsPerSec_Object = MibTableColumn
snSwPortStatsInKiloBitsPerSec = _SnSwPortStatsInKiloBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 54),
    _SnSwPortStatsInKiloBitsPerSec_Type()
)
snSwPortStatsInKiloBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsInKiloBitsPerSec.setStatus("deprecated")
_SnSwPortStatsOutKiloBitsPerSec_Type = Unsigned32
_SnSwPortStatsOutKiloBitsPerSec_Object = MibTableColumn
snSwPortStatsOutKiloBitsPerSec = _SnSwPortStatsOutKiloBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 55),
    _SnSwPortStatsOutKiloBitsPerSec_Type()
)
snSwPortStatsOutKiloBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsOutKiloBitsPerSec.setStatus("deprecated")


class _SnSwPortLoadInterval_Type(Integer32):
    """Custom type snSwPortLoadInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_SnSwPortLoadInterval_Type.__name__ = "Integer32"
_SnSwPortLoadInterval_Object = MibTableColumn
snSwPortLoadInterval = _SnSwPortLoadInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 56),
    _SnSwPortLoadInterval_Type()
)
snSwPortLoadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortLoadInterval.setStatus("deprecated")


class _SnSwPortTagType_Type(Integer32):
    """Custom type snSwPortTagType based on Integer32"""
    defaultValue = 33024


_SnSwPortTagType_Object = MibTableColumn
snSwPortTagType = _SnSwPortTagType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 57),
    _SnSwPortTagType_Type()
)
snSwPortTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortTagType.setStatus("deprecated")


class _SnSwPortInLinePowerControl_Type(Integer32):
    """Custom type snSwPortInLinePowerControl based on Integer32"""
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
        *(("disable", 2),
          ("enable", 3),
          ("enableLegacyDevice", 4),
          ("other", 1))
    )


_SnSwPortInLinePowerControl_Type.__name__ = "Integer32"
_SnSwPortInLinePowerControl_Object = MibTableColumn
snSwPortInLinePowerControl = _SnSwPortInLinePowerControl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 58),
    _SnSwPortInLinePowerControl_Type()
)
snSwPortInLinePowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortInLinePowerControl.setStatus("deprecated")
_SnSwPortInLinePowerWattage_Type = Integer32
_SnSwPortInLinePowerWattage_Object = MibTableColumn
snSwPortInLinePowerWattage = _SnSwPortInLinePowerWattage_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 59),
    _SnSwPortInLinePowerWattage_Type()
)
snSwPortInLinePowerWattage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortInLinePowerWattage.setStatus("deprecated")


class _SnSwPortInLinePowerClass_Type(Integer32):
    """Custom type snSwPortInLinePowerClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SnSwPortInLinePowerClass_Type.__name__ = "Integer32"
_SnSwPortInLinePowerClass_Object = MibTableColumn
snSwPortInLinePowerClass = _SnSwPortInLinePowerClass_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 60),
    _SnSwPortInLinePowerClass_Type()
)
snSwPortInLinePowerClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortInLinePowerClass.setStatus("deprecated")


class _SnSwPortInLinePowerPriority_Type(Integer32):
    """Custom type snSwPortInLinePowerPriority based on Integer32"""
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
        *(("critical", 1),
          ("high", 2),
          ("invalid", 0),
          ("low", 3),
          ("medium", 4),
          ("other", 5))
    )


_SnSwPortInLinePowerPriority_Type.__name__ = "Integer32"
_SnSwPortInLinePowerPriority_Object = MibTableColumn
snSwPortInLinePowerPriority = _SnSwPortInLinePowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 61),
    _SnSwPortInLinePowerPriority_Type()
)
snSwPortInLinePowerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortInLinePowerPriority.setStatus("deprecated")


class _SnSwPortInfoMirrorMode_Type(Integer32):
    """Custom type snSwPortInfoMirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SnSwPortInfoMirrorMode_Type.__name__ = "Integer32"
_SnSwPortInfoMirrorMode_Object = MibTableColumn
snSwPortInfoMirrorMode = _SnSwPortInfoMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 62),
    _SnSwPortInfoMirrorMode_Type()
)
snSwPortInfoMirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwPortInfoMirrorMode.setStatus("deprecated")
_SnSwPortStatsInJumboFrames_Type = Counter64
_SnSwPortStatsInJumboFrames_Object = MibTableColumn
snSwPortStatsInJumboFrames = _SnSwPortStatsInJumboFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 63),
    _SnSwPortStatsInJumboFrames_Type()
)
snSwPortStatsInJumboFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsInJumboFrames.setStatus("deprecated")
_SnSwPortStatsOutJumboFrames_Type = Counter64
_SnSwPortStatsOutJumboFrames_Object = MibTableColumn
snSwPortStatsOutJumboFrames = _SnSwPortStatsOutJumboFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 64),
    _SnSwPortStatsOutJumboFrames_Type()
)
snSwPortStatsOutJumboFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortStatsOutJumboFrames.setStatus("deprecated")
_SnSwPortInLinePowerConsumed_Type = Integer32
_SnSwPortInLinePowerConsumed_Object = MibTableColumn
snSwPortInLinePowerConsumed = _SnSwPortInLinePowerConsumed_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 66),
    _SnSwPortInLinePowerConsumed_Type()
)
snSwPortInLinePowerConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortInLinePowerConsumed.setStatus("deprecated")
_SnSwPortInLinePowerPDType_Type = DisplayString
_SnSwPortInLinePowerPDType_Object = MibTableColumn
snSwPortInLinePowerPDType = _SnSwPortInLinePowerPDType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 1, 1, 67),
    _SnSwPortInLinePowerPDType_Type()
)
snSwPortInLinePowerPDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwPortInLinePowerPDType.setStatus("deprecated")
_SnInterfaceId_ObjectIdentity = ObjectIdentity
snInterfaceId = _SnInterfaceId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 2)
)
_SnEthernetInterface_ObjectIdentity = ObjectIdentity
snEthernetInterface = _SnEthernetInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 2, 1)
)
_SnPosInterface_ObjectIdentity = ObjectIdentity
snPosInterface = _SnPosInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 2, 2)
)
_SnAtmInterface_ObjectIdentity = ObjectIdentity
snAtmInterface = _SnAtmInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 2, 3)
)
_SnVirtualInterface_ObjectIdentity = ObjectIdentity
snVirtualInterface = _SnVirtualInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 2, 4)
)
_SnLoopbackInterface_ObjectIdentity = ObjectIdentity
snLoopbackInterface = _SnLoopbackInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 2, 5)
)
_SnGreTunnelInterface_ObjectIdentity = ObjectIdentity
snGreTunnelInterface = _SnGreTunnelInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 2, 6)
)
_SnSubInterface_ObjectIdentity = ObjectIdentity
snSubInterface = _SnSubInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 2, 7)
)
_SnMplsTunnelInterface_ObjectIdentity = ObjectIdentity
snMplsTunnelInterface = _SnMplsTunnelInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 2, 8)
)
_SnPvcInterface_ObjectIdentity = ObjectIdentity
snPvcInterface = _SnPvcInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 2, 9)
)
_SnMgmtEthernetInterface_ObjectIdentity = ObjectIdentity
snMgmtEthernetInterface = _SnMgmtEthernetInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 2, 10)
)
_SnTrunkInterface_ObjectIdentity = ObjectIdentity
snTrunkInterface = _SnTrunkInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 2, 11)
)
_SnVirtualMgmtInterface_ObjectIdentity = ObjectIdentity
snVirtualMgmtInterface = _SnVirtualMgmtInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 2, 12)
)
_Sn6to4TunnelInterface_ObjectIdentity = ObjectIdentity
sn6to4TunnelInterface = _Sn6to4TunnelInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 2, 13)
)
_SnInterfaceLookupTable_Object = MibTable
snInterfaceLookupTable = _SnInterfaceLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    snInterfaceLookupTable.setStatus("current")
_SnInterfaceLookupEntry_Object = MibTableRow
snInterfaceLookupEntry = _SnInterfaceLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 3, 1)
)
snInterfaceLookupEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snInterfaceLookupInterfaceId"),
)
if mibBuilder.loadTexts:
    snInterfaceLookupEntry.setStatus("current")
_SnInterfaceLookupInterfaceId_Type = InterfaceId
_SnInterfaceLookupInterfaceId_Object = MibTableColumn
snInterfaceLookupInterfaceId = _SnInterfaceLookupInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 3, 1, 1),
    _SnInterfaceLookupInterfaceId_Type()
)
snInterfaceLookupInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snInterfaceLookupInterfaceId.setStatus("current")
_SnInterfaceLookupIfIndex_Type = Integer32
_SnInterfaceLookupIfIndex_Object = MibTableColumn
snInterfaceLookupIfIndex = _SnInterfaceLookupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 3, 1, 2),
    _SnInterfaceLookupIfIndex_Type()
)
snInterfaceLookupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snInterfaceLookupIfIndex.setStatus("current")
_SnIfIndexLookupTable_Object = MibTable
snIfIndexLookupTable = _SnIfIndexLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 4)
)
if mibBuilder.loadTexts:
    snIfIndexLookupTable.setStatus("current")
_SnIfIndexLookupEntry_Object = MibTableRow
snIfIndexLookupEntry = _SnIfIndexLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 4, 1)
)
snIfIndexLookupEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snIfIndexLookupIfIndex"),
)
if mibBuilder.loadTexts:
    snIfIndexLookupEntry.setStatus("current")
_SnIfIndexLookupIfIndex_Type = Integer32
_SnIfIndexLookupIfIndex_Object = MibTableColumn
snIfIndexLookupIfIndex = _SnIfIndexLookupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 4, 1, 1),
    _SnIfIndexLookupIfIndex_Type()
)
snIfIndexLookupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfIndexLookupIfIndex.setStatus("current")
_SnIfIndexLookupInterfaceId_Type = InterfaceId
_SnIfIndexLookupInterfaceId_Object = MibTableColumn
snIfIndexLookupInterfaceId = _SnIfIndexLookupInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 4, 1, 2),
    _SnIfIndexLookupInterfaceId_Type()
)
snIfIndexLookupInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfIndexLookupInterfaceId.setStatus("current")
_SnSwIfInfoTable_Object = MibTable
snSwIfInfoTable = _SnSwIfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5)
)
if mibBuilder.loadTexts:
    snSwIfInfoTable.setStatus("current")
_SnSwIfInfoEntry_Object = MibTableRow
snSwIfInfoEntry = _SnSwIfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1)
)
snSwIfInfoEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwIfInfoPortNum"),
)
if mibBuilder.loadTexts:
    snSwIfInfoEntry.setStatus("current")
_SnSwIfInfoPortNum_Type = InterfaceIndex
_SnSwIfInfoPortNum_Object = MibTableColumn
snSwIfInfoPortNum = _SnSwIfInfoPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 1),
    _SnSwIfInfoPortNum_Type()
)
snSwIfInfoPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfInfoPortNum.setStatus("current")


class _SnSwIfInfoMonitorMode_Type(Integer32):
    """Custom type snSwIfInfoMonitorMode based on Integer32"""
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
        *(("both", 3),
          ("disabled", 0),
          ("input", 1),
          ("output", 2))
    )


_SnSwIfInfoMonitorMode_Type.__name__ = "Integer32"
_SnSwIfInfoMonitorMode_Object = MibTableColumn
snSwIfInfoMonitorMode = _SnSwIfInfoMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 2),
    _SnSwIfInfoMonitorMode_Type()
)
snSwIfInfoMonitorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfInfoMonitorMode.setStatus("deprecated")
_SnSwIfInfoMirrorPorts_Type = OctetString
_SnSwIfInfoMirrorPorts_Object = MibTableColumn
snSwIfInfoMirrorPorts = _SnSwIfInfoMirrorPorts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 3),
    _SnSwIfInfoMirrorPorts_Type()
)
snSwIfInfoMirrorPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfInfoMirrorPorts.setStatus("current")


class _SnSwIfInfoTagMode_Type(Integer32):
    """Custom type snSwIfInfoTagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dual", 3),
          ("tagged", 1),
          ("untagged", 2))
    )


_SnSwIfInfoTagMode_Type.__name__ = "Integer32"
_SnSwIfInfoTagMode_Object = MibTableColumn
snSwIfInfoTagMode = _SnSwIfInfoTagMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 4),
    _SnSwIfInfoTagMode_Type()
)
snSwIfInfoTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfInfoTagMode.setStatus("current")


class _SnSwIfInfoTagType_Type(Integer32):
    """Custom type snSwIfInfoTagType based on Integer32"""
    defaultValue = 33024


_SnSwIfInfoTagType_Object = MibTableColumn
snSwIfInfoTagType = _SnSwIfInfoTagType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 5),
    _SnSwIfInfoTagType_Type()
)
snSwIfInfoTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfInfoTagType.setStatus("current")


class _SnSwIfInfoChnMode_Type(Integer32):
    """Custom type snSwIfInfoChnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 2),
          ("halfDuplex", 1),
          ("none", 0))
    )


_SnSwIfInfoChnMode_Type.__name__ = "Integer32"
_SnSwIfInfoChnMode_Object = MibTableColumn
snSwIfInfoChnMode = _SnSwIfInfoChnMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 6),
    _SnSwIfInfoChnMode_Type()
)
snSwIfInfoChnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfInfoChnMode.setStatus("current")


class _SnSwIfInfoSpeed_Type(Integer32):
    """Custom type snSwIfInfoSpeed based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("s100G", 12),
          ("s100M", 3),
          ("s10G", 7),
          ("s10M", 2),
          ("s155M", 6),
          ("s16G", 11),
          ("s1G", 4),
          ("s1GM", 5),
          ("s2488M", 9),
          ("s2500M", 14),
          ("s40G", 13),
          ("s622M", 8),
          ("s9953M", 10),
          ("sAutoSense", 1))
    )


_SnSwIfInfoSpeed_Type.__name__ = "Integer32"
_SnSwIfInfoSpeed_Object = MibTableColumn
snSwIfInfoSpeed = _SnSwIfInfoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 7),
    _SnSwIfInfoSpeed_Type()
)
snSwIfInfoSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfInfoSpeed.setStatus("current")


class _SnSwIfInfoMediaType_Type(Integer32):
    """Custom type snSwIfInfoMediaType based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("m10000BaseFX", 12),
          ("m10000BaseTX", 18),
          ("m1000BaseFX", 4),
          ("m1000BaseTX", 7),
          ("m100BaseFX", 3),
          ("m100BaseTX", 2),
          ("m100GBaseFX", 15),
          ("m155ATM", 6),
          ("m155POS", 9),
          ("m16GStacking", 14),
          ("m2488POS", 11),
          ("m2500BaseTX", 19),
          ("m40GBaseFX", 17),
          ("m40GStacking", 16),
          ("m622ATM", 8),
          ("m622POS", 10),
          ("m9953POS", 13),
          ("mT3", 5),
          ("other", 1))
    )


_SnSwIfInfoMediaType_Type.__name__ = "Integer32"
_SnSwIfInfoMediaType_Object = MibTableColumn
snSwIfInfoMediaType = _SnSwIfInfoMediaType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 8),
    _SnSwIfInfoMediaType_Type()
)
snSwIfInfoMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfInfoMediaType.setStatus("current")


class _SnSwIfInfoConnectorType_Type(Integer32):
    """Custom type snSwIfInfoConnectorType based on Integer32"""
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
          ("copper", 2),
          ("fiber", 3),
          ("other", 1))
    )


_SnSwIfInfoConnectorType_Type.__name__ = "Integer32"
_SnSwIfInfoConnectorType_Object = MibTableColumn
snSwIfInfoConnectorType = _SnSwIfInfoConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 9),
    _SnSwIfInfoConnectorType_Type()
)
snSwIfInfoConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfInfoConnectorType.setStatus("current")


class _SnSwIfInfoAdminStatus_Type(Integer32):
    """Custom type snSwIfInfoAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_SnSwIfInfoAdminStatus_Type.__name__ = "Integer32"
_SnSwIfInfoAdminStatus_Object = MibTableColumn
snSwIfInfoAdminStatus = _SnSwIfInfoAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 10),
    _SnSwIfInfoAdminStatus_Type()
)
snSwIfInfoAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfInfoAdminStatus.setStatus("current")


class _SnSwIfInfoLinkStatus_Type(Integer32):
    """Custom type snSwIfInfoLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_SnSwIfInfoLinkStatus_Type.__name__ = "Integer32"
_SnSwIfInfoLinkStatus_Object = MibTableColumn
snSwIfInfoLinkStatus = _SnSwIfInfoLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 11),
    _SnSwIfInfoLinkStatus_Type()
)
snSwIfInfoLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfInfoLinkStatus.setStatus("current")


class _SnSwIfInfoPortQos_Type(Integer32):
    """Custom type snSwIfInfoPortQos based on Integer32"""
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
        *(("level0", 0),
          ("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7))
    )


_SnSwIfInfoPortQos_Type.__name__ = "Integer32"
_SnSwIfInfoPortQos_Object = MibTableColumn
snSwIfInfoPortQos = _SnSwIfInfoPortQos_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 12),
    _SnSwIfInfoPortQos_Type()
)
snSwIfInfoPortQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfInfoPortQos.setStatus("current")
_SnSwIfInfoPhysAddress_Type = PhysAddress
_SnSwIfInfoPhysAddress_Object = MibTableColumn
snSwIfInfoPhysAddress = _SnSwIfInfoPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 13),
    _SnSwIfInfoPhysAddress_Type()
)
snSwIfInfoPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfInfoPhysAddress.setStatus("current")


class _SnSwIfLockAddressCount_Type(Integer32):
    """Custom type snSwIfLockAddressCount based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_SnSwIfLockAddressCount_Type.__name__ = "Integer32"
_SnSwIfLockAddressCount_Object = MibTableColumn
snSwIfLockAddressCount = _SnSwIfLockAddressCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 14),
    _SnSwIfLockAddressCount_Type()
)
snSwIfLockAddressCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfLockAddressCount.setStatus("current")


class _SnSwIfStpPortEnable_Type(Integer32):
    """Custom type snSwIfStpPortEnable based on Integer32"""
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


_SnSwIfStpPortEnable_Type.__name__ = "Integer32"
_SnSwIfStpPortEnable_Object = MibTableColumn
snSwIfStpPortEnable = _SnSwIfStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 15),
    _SnSwIfStpPortEnable_Type()
)
snSwIfStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfStpPortEnable.setStatus("current")


class _SnSwIfDhcpGateListId_Type(Integer32):
    """Custom type snSwIfDhcpGateListId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SnSwIfDhcpGateListId_Type.__name__ = "Integer32"
_SnSwIfDhcpGateListId_Object = MibTableColumn
snSwIfDhcpGateListId = _SnSwIfDhcpGateListId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 16),
    _SnSwIfDhcpGateListId_Type()
)
snSwIfDhcpGateListId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfDhcpGateListId.setStatus("current")


class _SnSwIfName_Type(DisplayString):
    """Custom type snSwIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnSwIfName_Type.__name__ = "DisplayString"
_SnSwIfName_Object = MibTableColumn
snSwIfName = _SnSwIfName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 17),
    _SnSwIfName_Type()
)
snSwIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfName.setStatus("current")
_SnSwIfDescr_Type = DisplayString
_SnSwIfDescr_Object = MibTableColumn
snSwIfDescr = _SnSwIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 18),
    _SnSwIfDescr_Type()
)
snSwIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfDescr.setStatus("current")


class _SnSwIfInfoAutoNegotiate_Type(Integer32):
    """Custom type snSwIfInfoAutoNegotiate based on Integer32"""
    defaultValue = 3

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
        *(("disabled", 0),
          ("enabled", 1),
          ("global", 3),
          ("negFullAuto", 2),
          ("other", 4))
    )


_SnSwIfInfoAutoNegotiate_Type.__name__ = "Integer32"
_SnSwIfInfoAutoNegotiate_Object = MibTableColumn
snSwIfInfoAutoNegotiate = _SnSwIfInfoAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 19),
    _SnSwIfInfoAutoNegotiate_Type()
)
snSwIfInfoAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfInfoAutoNegotiate.setStatus("current")


class _SnSwIfInfoFlowControl_Type(Integer32):
    """Custom type snSwIfInfoFlowControl based on Integer32"""
    defaultValue = 1

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


_SnSwIfInfoFlowControl_Type.__name__ = "Integer32"
_SnSwIfInfoFlowControl_Object = MibTableColumn
snSwIfInfoFlowControl = _SnSwIfInfoFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 20),
    _SnSwIfInfoFlowControl_Type()
)
snSwIfInfoFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfInfoFlowControl.setStatus("current")


class _SnSwIfInfoGigType_Type(Integer32):
    """Custom type snSwIfInfoGigType based on Integer32"""
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
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              255)
        )
    )
    namedValues = NamedValues(
        *(("m10000BaseER", 8),
          ("m10000BaseLR", 7),
          ("m10000BaseSR", 6),
          ("m10000BaseT", 49),
          ("m1000BaseC6553", 45),
          ("m1000BaseFBX", 129),
          ("m1000BaseFBXD", 131),
          ("m1000BaseFBXU", 130),
          ("m1000BaseFX", 132),
          ("m1000BaseFXIR", 133),
          ("m1000BaseFXLR", 134),
          ("m1000BaseGBXD", 128),
          ("m1000BaseGBXU", 127),
          ("m1000BaseLH", 2),
          ("m1000BaseLHA", 3),
          ("m1000BaseLHB", 4),
          ("m1000BaseLHX", 25),
          ("m1000BaseLMC", 35),
          ("m1000BaseLX", 1),
          ("m1000BaseSX", 0),
          ("m1000BaseSX2", 26),
          ("m1000BaseTX", 5),
          ("m1000BaseXGCX4", 142),
          ("m1000BaseXGER", 138),
          ("m1000BaseXGEW", 141),
          ("m1000BaseXGLR", 137),
          ("m1000BaseXGLW", 140),
          ("m1000BaseXGSR", 136),
          ("m1000BaseXGSW", 139),
          ("m1000BaseXGZR", 143),
          ("m1000BaseXGZRD", 144),
          ("m2500BaseTX", 50),
          ("mCFP100GBase10x10g10Km", 149),
          ("mCFP100GBase10x10g2Km", 148),
          ("mCFP100GBaseER4", 147),
          ("mCFP100GBaseLR4", 146),
          ("mCFP100GBaseSR10", 145),
          ("mCFP2-100GBase10x10g10Km", 158),
          ("mCFP2-100GBase10x10g2Km", 157),
          ("mCFP2-100GBaseER4", 156),
          ("mCFP2-100GBaseLR4", 155),
          ("mCFP2-100GBaseSR10", 154),
          ("mSFP1000BaseBXD", 28),
          ("mSFP1000BaseBXU", 27),
          ("mSFP100BaseBX", 29),
          ("mSFP100BaseBXD", 31),
          ("mSFP100BaseBXU", 30),
          ("mSFP100BaseFX", 32),
          ("mSFP100BaseFXIR", 33),
          ("mSFP100BaseFXLR", 34),
          ("mXFP10000BaseCX4", 42),
          ("mXFP10000BaseER", 38),
          ("mXFP10000BaseEREW", 48),
          ("mXFP10000BaseEW", 41),
          ("mXFP10000BaseLR", 37),
          ("mXFP10000BaseLRLW", 47),
          ("mXFP10000BaseLW", 40),
          ("mXFP10000BaseSR", 36),
          ("mXFP10000BaseSRSW", 46),
          ("mXFP10000BaseSW", 39),
          ("mXFP10000BaseTwinax", 153),
          ("mXFP10000BaseUSR", 152),
          ("mXFP10000BaseZR", 43),
          ("mXFP10000BaseZRD", 44),
          ("notApplicable", 255),
          ("qSFP40000Base10KmLR4", 151),
          ("qSFP40000BaseSR4", 150),
          ("sfpCWDM1470nm100Km", 17),
          ("sfpCWDM1470nm80Km", 9),
          ("sfpCWDM1490nm100Km", 18),
          ("sfpCWDM1490nm80Km", 10),
          ("sfpCWDM1510nm100Km", 19),
          ("sfpCWDM1510nm80Km", 11),
          ("sfpCWDM1530nm100Km", 20),
          ("sfpCWDM1530nm80Km", 12),
          ("sfpCWDM1550nm100Km", 21),
          ("sfpCWDM1550nm80Km", 13),
          ("sfpCWDM1570nm100Km", 22),
          ("sfpCWDM1570nm80Km", 14),
          ("sfpCWDM1590nm100Km", 23),
          ("sfpCWDM1590nm80Km", 15),
          ("sfpCWDM1610nm100Km", 24),
          ("sfpCWDM1610nm80Km", 16))
    )


_SnSwIfInfoGigType_Type.__name__ = "Integer32"
_SnSwIfInfoGigType_Object = MibTableColumn
snSwIfInfoGigType = _SnSwIfInfoGigType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 21),
    _SnSwIfInfoGigType_Type()
)
snSwIfInfoGigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfInfoGigType.setStatus("current")


class _SnSwIfFastSpanPortEnable_Type(Integer32):
    """Custom type snSwIfFastSpanPortEnable based on Integer32"""
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


_SnSwIfFastSpanPortEnable_Type.__name__ = "Integer32"
_SnSwIfFastSpanPortEnable_Object = MibTableColumn
snSwIfFastSpanPortEnable = _SnSwIfFastSpanPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 22),
    _SnSwIfFastSpanPortEnable_Type()
)
snSwIfFastSpanPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfFastSpanPortEnable.setStatus("current")


class _SnSwIfFastSpanUplinkEnable_Type(Integer32):
    """Custom type snSwIfFastSpanUplinkEnable based on Integer32"""
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


_SnSwIfFastSpanUplinkEnable_Type.__name__ = "Integer32"
_SnSwIfFastSpanUplinkEnable_Object = MibTableColumn
snSwIfFastSpanUplinkEnable = _SnSwIfFastSpanUplinkEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 23),
    _SnSwIfFastSpanUplinkEnable_Type()
)
snSwIfFastSpanUplinkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfFastSpanUplinkEnable.setStatus("current")


class _SnSwIfVlanId_Type(Integer32):
    """Custom type snSwIfVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SnSwIfVlanId_Type.__name__ = "Integer32"
_SnSwIfVlanId_Object = MibTableColumn
snSwIfVlanId = _SnSwIfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 24),
    _SnSwIfVlanId_Type()
)
snSwIfVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfVlanId.setStatus("current")


class _SnSwIfRouteOnly_Type(Integer32):
    """Custom type snSwIfRouteOnly based on Integer32"""
    defaultValue = 0

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


_SnSwIfRouteOnly_Type.__name__ = "Integer32"
_SnSwIfRouteOnly_Object = MibTableColumn
snSwIfRouteOnly = _SnSwIfRouteOnly_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 25),
    _SnSwIfRouteOnly_Type()
)
snSwIfRouteOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfRouteOnly.setStatus("current")


class _SnSwIfPresent_Type(Integer32):
    """Custom type snSwIfPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnSwIfPresent_Type.__name__ = "Integer32"
_SnSwIfPresent_Object = MibTableColumn
snSwIfPresent = _SnSwIfPresent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 26),
    _SnSwIfPresent_Type()
)
snSwIfPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfPresent.setStatus("current")


class _SnSwIfGBICStatus_Type(Integer32):
    """Custom type snSwIfGBICStatus based on Integer32"""
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
        *(("empty", 3),
          ("gbic", 1),
          ("miniGBIC", 2),
          ("other", 4))
    )


_SnSwIfGBICStatus_Type.__name__ = "Integer32"
_SnSwIfGBICStatus_Object = MibTableColumn
snSwIfGBICStatus = _SnSwIfGBICStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 27),
    _SnSwIfGBICStatus_Type()
)
snSwIfGBICStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfGBICStatus.setStatus("current")


class _SnSwIfLoadInterval_Type(Integer32):
    """Custom type snSwIfLoadInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_SnSwIfLoadInterval_Type.__name__ = "Integer32"
_SnSwIfLoadInterval_Object = MibTableColumn
snSwIfLoadInterval = _SnSwIfLoadInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 28),
    _SnSwIfLoadInterval_Type()
)
snSwIfLoadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfLoadInterval.setStatus("current")
_SnSwIfStatsInFrames_Type = Counter32
_SnSwIfStatsInFrames_Object = MibTableColumn
snSwIfStatsInFrames = _SnSwIfStatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 29),
    _SnSwIfStatsInFrames_Type()
)
snSwIfStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsInFrames.setStatus("current")
_SnSwIfStatsOutFrames_Type = Counter32
_SnSwIfStatsOutFrames_Object = MibTableColumn
snSwIfStatsOutFrames = _SnSwIfStatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 30),
    _SnSwIfStatsOutFrames_Type()
)
snSwIfStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsOutFrames.setStatus("current")
_SnSwIfStatsAlignErrors_Type = Counter32
_SnSwIfStatsAlignErrors_Object = MibTableColumn
snSwIfStatsAlignErrors = _SnSwIfStatsAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 31),
    _SnSwIfStatsAlignErrors_Type()
)
snSwIfStatsAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsAlignErrors.setStatus("current")
_SnSwIfStatsFCSErrors_Type = Counter32
_SnSwIfStatsFCSErrors_Object = MibTableColumn
snSwIfStatsFCSErrors = _SnSwIfStatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 32),
    _SnSwIfStatsFCSErrors_Type()
)
snSwIfStatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsFCSErrors.setStatus("current")
_SnSwIfStatsMultiColliFrames_Type = Counter32
_SnSwIfStatsMultiColliFrames_Object = MibTableColumn
snSwIfStatsMultiColliFrames = _SnSwIfStatsMultiColliFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 33),
    _SnSwIfStatsMultiColliFrames_Type()
)
snSwIfStatsMultiColliFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsMultiColliFrames.setStatus("current")
_SnSwIfStatsTxColliFrames_Type = Counter32
_SnSwIfStatsTxColliFrames_Object = MibTableColumn
snSwIfStatsTxColliFrames = _SnSwIfStatsTxColliFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 34),
    _SnSwIfStatsTxColliFrames_Type()
)
snSwIfStatsTxColliFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsTxColliFrames.setStatus("current")
_SnSwIfStatsRxColliFrames_Type = Counter32
_SnSwIfStatsRxColliFrames_Object = MibTableColumn
snSwIfStatsRxColliFrames = _SnSwIfStatsRxColliFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 35),
    _SnSwIfStatsRxColliFrames_Type()
)
snSwIfStatsRxColliFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsRxColliFrames.setStatus("current")
_SnSwIfStatsFrameTooLongs_Type = Counter32
_SnSwIfStatsFrameTooLongs_Object = MibTableColumn
snSwIfStatsFrameTooLongs = _SnSwIfStatsFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 36),
    _SnSwIfStatsFrameTooLongs_Type()
)
snSwIfStatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsFrameTooLongs.setStatus("current")
_SnSwIfStatsFrameTooShorts_Type = Counter32
_SnSwIfStatsFrameTooShorts_Object = MibTableColumn
snSwIfStatsFrameTooShorts = _SnSwIfStatsFrameTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 37),
    _SnSwIfStatsFrameTooShorts_Type()
)
snSwIfStatsFrameTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsFrameTooShorts.setStatus("current")
_SnSwIfStatsInBcastFrames_Type = Counter32
_SnSwIfStatsInBcastFrames_Object = MibTableColumn
snSwIfStatsInBcastFrames = _SnSwIfStatsInBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 38),
    _SnSwIfStatsInBcastFrames_Type()
)
snSwIfStatsInBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsInBcastFrames.setStatus("current")
_SnSwIfStatsOutBcastFrames_Type = Counter32
_SnSwIfStatsOutBcastFrames_Object = MibTableColumn
snSwIfStatsOutBcastFrames = _SnSwIfStatsOutBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 39),
    _SnSwIfStatsOutBcastFrames_Type()
)
snSwIfStatsOutBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsOutBcastFrames.setStatus("current")
_SnSwIfStatsInMcastFrames_Type = Counter32
_SnSwIfStatsInMcastFrames_Object = MibTableColumn
snSwIfStatsInMcastFrames = _SnSwIfStatsInMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 40),
    _SnSwIfStatsInMcastFrames_Type()
)
snSwIfStatsInMcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsInMcastFrames.setStatus("current")
_SnSwIfStatsOutMcastFrames_Type = Counter32
_SnSwIfStatsOutMcastFrames_Object = MibTableColumn
snSwIfStatsOutMcastFrames = _SnSwIfStatsOutMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 41),
    _SnSwIfStatsOutMcastFrames_Type()
)
snSwIfStatsOutMcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsOutMcastFrames.setStatus("current")
_SnSwIfStatsInDiscard_Type = Counter32
_SnSwIfStatsInDiscard_Object = MibTableColumn
snSwIfStatsInDiscard = _SnSwIfStatsInDiscard_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 42),
    _SnSwIfStatsInDiscard_Type()
)
snSwIfStatsInDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsInDiscard.setStatus("current")
_SnSwIfStatsOutDiscard_Type = Counter32
_SnSwIfStatsOutDiscard_Object = MibTableColumn
snSwIfStatsOutDiscard = _SnSwIfStatsOutDiscard_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 43),
    _SnSwIfStatsOutDiscard_Type()
)
snSwIfStatsOutDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsOutDiscard.setStatus("current")
_SnSwIfStatsMacStations_Type = Integer32
_SnSwIfStatsMacStations_Object = MibTableColumn
snSwIfStatsMacStations = _SnSwIfStatsMacStations_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 44),
    _SnSwIfStatsMacStations_Type()
)
snSwIfStatsMacStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsMacStations.setStatus("current")
_SnSwIfStatsLinkChange_Type = Counter32
_SnSwIfStatsLinkChange_Object = MibTableColumn
snSwIfStatsLinkChange = _SnSwIfStatsLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 45),
    _SnSwIfStatsLinkChange_Type()
)
snSwIfStatsLinkChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsLinkChange.setStatus("current")
_SnSwIfInOctets_Type = Counter64
_SnSwIfInOctets_Object = MibTableColumn
snSwIfInOctets = _SnSwIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 46),
    _SnSwIfInOctets_Type()
)
snSwIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfInOctets.setStatus("current")
_SnSwIfOutOctets_Type = Counter64
_SnSwIfOutOctets_Object = MibTableColumn
snSwIfOutOctets = _SnSwIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 47),
    _SnSwIfOutOctets_Type()
)
snSwIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfOutOctets.setStatus("current")
_SnSwIfStatsInBitsPerSec_Type = Gauge32
_SnSwIfStatsInBitsPerSec_Object = MibTableColumn
snSwIfStatsInBitsPerSec = _SnSwIfStatsInBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 48),
    _SnSwIfStatsInBitsPerSec_Type()
)
snSwIfStatsInBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsInBitsPerSec.setStatus("current")
_SnSwIfStatsOutBitsPerSec_Type = Gauge32
_SnSwIfStatsOutBitsPerSec_Object = MibTableColumn
snSwIfStatsOutBitsPerSec = _SnSwIfStatsOutBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 49),
    _SnSwIfStatsOutBitsPerSec_Type()
)
snSwIfStatsOutBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsOutBitsPerSec.setStatus("current")
_SnSwIfStatsInPktsPerSec_Type = Gauge32
_SnSwIfStatsInPktsPerSec_Object = MibTableColumn
snSwIfStatsInPktsPerSec = _SnSwIfStatsInPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 50),
    _SnSwIfStatsInPktsPerSec_Type()
)
snSwIfStatsInPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsInPktsPerSec.setStatus("current")
_SnSwIfStatsOutPktsPerSec_Type = Gauge32
_SnSwIfStatsOutPktsPerSec_Object = MibTableColumn
snSwIfStatsOutPktsPerSec = _SnSwIfStatsOutPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 51),
    _SnSwIfStatsOutPktsPerSec_Type()
)
snSwIfStatsOutPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsOutPktsPerSec.setStatus("current")


class _SnSwIfStatsInUtilization_Type(Integer32):
    """Custom type snSwIfStatsInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SnSwIfStatsInUtilization_Type.__name__ = "Integer32"
_SnSwIfStatsInUtilization_Object = MibTableColumn
snSwIfStatsInUtilization = _SnSwIfStatsInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 52),
    _SnSwIfStatsInUtilization_Type()
)
snSwIfStatsInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsInUtilization.setStatus("current")


class _SnSwIfStatsOutUtilization_Type(Integer32):
    """Custom type snSwIfStatsOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SnSwIfStatsOutUtilization_Type.__name__ = "Integer32"
_SnSwIfStatsOutUtilization_Object = MibTableColumn
snSwIfStatsOutUtilization = _SnSwIfStatsOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 53),
    _SnSwIfStatsOutUtilization_Type()
)
snSwIfStatsOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsOutUtilization.setStatus("current")
_SnSwIfStatsInKiloBitsPerSec_Type = Unsigned32
_SnSwIfStatsInKiloBitsPerSec_Object = MibTableColumn
snSwIfStatsInKiloBitsPerSec = _SnSwIfStatsInKiloBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 54),
    _SnSwIfStatsInKiloBitsPerSec_Type()
)
snSwIfStatsInKiloBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsInKiloBitsPerSec.setStatus("current")
_SnSwIfStatsOutKiloBitsPerSec_Type = Unsigned32
_SnSwIfStatsOutKiloBitsPerSec_Object = MibTableColumn
snSwIfStatsOutKiloBitsPerSec = _SnSwIfStatsOutKiloBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 55),
    _SnSwIfStatsOutKiloBitsPerSec_Type()
)
snSwIfStatsOutKiloBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsOutKiloBitsPerSec.setStatus("current")
_SnSwIfStatsInJumboFrames_Type = Counter64
_SnSwIfStatsInJumboFrames_Object = MibTableColumn
snSwIfStatsInJumboFrames = _SnSwIfStatsInJumboFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 56),
    _SnSwIfStatsInJumboFrames_Type()
)
snSwIfStatsInJumboFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsInJumboFrames.setStatus("current")
_SnSwIfStatsOutJumboFrames_Type = Counter64
_SnSwIfStatsOutJumboFrames_Object = MibTableColumn
snSwIfStatsOutJumboFrames = _SnSwIfStatsOutJumboFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 57),
    _SnSwIfStatsOutJumboFrames_Type()
)
snSwIfStatsOutJumboFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfStatsOutJumboFrames.setStatus("current")


class _SnSwIfInfoMirrorMode_Type(Integer32):
    """Custom type snSwIfInfoMirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SnSwIfInfoMirrorMode_Type.__name__ = "Integer32"
_SnSwIfInfoMirrorMode_Object = MibTableColumn
snSwIfInfoMirrorMode = _SnSwIfInfoMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 58),
    _SnSwIfInfoMirrorMode_Type()
)
snSwIfInfoMirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfInfoMirrorMode.setStatus("current")


class _SnSwIfMacLearningDisable_Type(TruthValue):
    """Custom type snSwIfMacLearningDisable based on TruthValue"""


_SnSwIfMacLearningDisable_Object = MibTableColumn
snSwIfMacLearningDisable = _SnSwIfMacLearningDisable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 59),
    _SnSwIfMacLearningDisable_Type()
)
snSwIfMacLearningDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfMacLearningDisable.setStatus("current")


class _SnSwIfInfoL2FowardEnable_Type(Integer32):
    """Custom type snSwIfInfoL2FowardEnable based on Integer32"""
    defaultValue = 3

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
          ("globalConfig", 3))
    )


_SnSwIfInfoL2FowardEnable_Type.__name__ = "Integer32"
_SnSwIfInfoL2FowardEnable_Object = MibTableColumn
snSwIfInfoL2FowardEnable = _SnSwIfInfoL2FowardEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 60),
    _SnSwIfInfoL2FowardEnable_Type()
)
snSwIfInfoL2FowardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfInfoL2FowardEnable.setStatus("current")


class _SnSwIfInfoAllowAllVlan_Type(TruthValue):
    """Custom type snSwIfInfoAllowAllVlan based on TruthValue"""


_SnSwIfInfoAllowAllVlan_Object = MibTableColumn
snSwIfInfoAllowAllVlan = _SnSwIfInfoAllowAllVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 61),
    _SnSwIfInfoAllowAllVlan_Type()
)
snSwIfInfoAllowAllVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwIfInfoAllowAllVlan.setStatus("current")
_SnSwIfInfoNativeMacAddress_Type = PhysAddress
_SnSwIfInfoNativeMacAddress_Object = MibTableColumn
snSwIfInfoNativeMacAddress = _SnSwIfInfoNativeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 5, 1, 62),
    _SnSwIfInfoNativeMacAddress_Type()
)
snSwIfInfoNativeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSwIfInfoNativeMacAddress.setStatus("current")
_SnIfOpticalMonitoringInfoTable_Object = MibTable
snIfOpticalMonitoringInfoTable = _SnIfOpticalMonitoringInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 6)
)
if mibBuilder.loadTexts:
    snIfOpticalMonitoringInfoTable.setStatus("current")
_SnIfOpticalMonitoringInfoEntry_Object = MibTableRow
snIfOpticalMonitoringInfoEntry = _SnIfOpticalMonitoringInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 6, 1)
)
snIfOpticalMonitoringInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    snIfOpticalMonitoringInfoEntry.setStatus("current")


class _SnIfOpticalMonitoringTemperature_Type(DisplayString):
    """Custom type snIfOpticalMonitoringTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnIfOpticalMonitoringTemperature_Type.__name__ = "DisplayString"
_SnIfOpticalMonitoringTemperature_Object = MibTableColumn
snIfOpticalMonitoringTemperature = _SnIfOpticalMonitoringTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 6, 1, 1),
    _SnIfOpticalMonitoringTemperature_Type()
)
snIfOpticalMonitoringTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfOpticalMonitoringTemperature.setStatus("current")


class _SnIfOpticalMonitoringTxPower_Type(DisplayString):
    """Custom type snIfOpticalMonitoringTxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnIfOpticalMonitoringTxPower_Type.__name__ = "DisplayString"
_SnIfOpticalMonitoringTxPower_Object = MibTableColumn
snIfOpticalMonitoringTxPower = _SnIfOpticalMonitoringTxPower_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 6, 1, 2),
    _SnIfOpticalMonitoringTxPower_Type()
)
snIfOpticalMonitoringTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfOpticalMonitoringTxPower.setStatus("current")


class _SnIfOpticalMonitoringRxPower_Type(DisplayString):
    """Custom type snIfOpticalMonitoringRxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnIfOpticalMonitoringRxPower_Type.__name__ = "DisplayString"
_SnIfOpticalMonitoringRxPower_Object = MibTableColumn
snIfOpticalMonitoringRxPower = _SnIfOpticalMonitoringRxPower_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 6, 1, 3),
    _SnIfOpticalMonitoringRxPower_Type()
)
snIfOpticalMonitoringRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfOpticalMonitoringRxPower.setStatus("current")


class _SnIfOpticalMonitoringTxBiasCurrent_Type(DisplayString):
    """Custom type snIfOpticalMonitoringTxBiasCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnIfOpticalMonitoringTxBiasCurrent_Type.__name__ = "DisplayString"
_SnIfOpticalMonitoringTxBiasCurrent_Object = MibTableColumn
snIfOpticalMonitoringTxBiasCurrent = _SnIfOpticalMonitoringTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 6, 1, 4),
    _SnIfOpticalMonitoringTxBiasCurrent_Type()
)
snIfOpticalMonitoringTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfOpticalMonitoringTxBiasCurrent.setStatus("current")
_SnInterfaceLookup2Table_Object = MibTable
snInterfaceLookup2Table = _SnInterfaceLookup2Table_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 7)
)
if mibBuilder.loadTexts:
    snInterfaceLookup2Table.setStatus("current")
_SnInterfaceLookup2Entry_Object = MibTableRow
snInterfaceLookup2Entry = _SnInterfaceLookup2Entry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 7, 1)
)
snInterfaceLookup2Entry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snInterfaceLookup2InterfaceId"),
)
if mibBuilder.loadTexts:
    snInterfaceLookup2Entry.setStatus("current")
_SnInterfaceLookup2InterfaceId_Type = InterfaceId2
_SnInterfaceLookup2InterfaceId_Object = MibTableColumn
snInterfaceLookup2InterfaceId = _SnInterfaceLookup2InterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 7, 1, 1),
    _SnInterfaceLookup2InterfaceId_Type()
)
snInterfaceLookup2InterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snInterfaceLookup2InterfaceId.setStatus("current")
_SnInterfaceLookup2IfIndex_Type = Integer32
_SnInterfaceLookup2IfIndex_Object = MibTableColumn
snInterfaceLookup2IfIndex = _SnInterfaceLookup2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 7, 1, 2),
    _SnInterfaceLookup2IfIndex_Type()
)
snInterfaceLookup2IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snInterfaceLookup2IfIndex.setStatus("current")
_SnIfIndexLookup2Table_Object = MibTable
snIfIndexLookup2Table = _SnIfIndexLookup2Table_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 8)
)
if mibBuilder.loadTexts:
    snIfIndexLookup2Table.setStatus("current")
_SnIfIndexLookup2Entry_Object = MibTableRow
snIfIndexLookup2Entry = _SnIfIndexLookup2Entry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 8, 1)
)
snIfIndexLookup2Entry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snIfIndexLookup2IfIndex"),
)
if mibBuilder.loadTexts:
    snIfIndexLookup2Entry.setStatus("current")
_SnIfIndexLookup2IfIndex_Type = Integer32
_SnIfIndexLookup2IfIndex_Object = MibTableColumn
snIfIndexLookup2IfIndex = _SnIfIndexLookup2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 8, 1, 1),
    _SnIfIndexLookup2IfIndex_Type()
)
snIfIndexLookup2IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snIfIndexLookup2IfIndex.setStatus("current")
_SnIfIndexLookup2InterfaceId_Type = InterfaceId2
_SnIfIndexLookup2InterfaceId_Object = MibTableColumn
snIfIndexLookup2InterfaceId = _SnIfIndexLookup2InterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 8, 1, 2),
    _SnIfIndexLookup2InterfaceId_Type()
)
snIfIndexLookup2InterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfIndexLookup2InterfaceId.setStatus("current")
_SnIfMediaInfoTable_Object = MibTable
snIfMediaInfoTable = _SnIfMediaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 9)
)
if mibBuilder.loadTexts:
    snIfMediaInfoTable.setStatus("current")
_SnIfMediaInfoEntry_Object = MibTableRow
snIfMediaInfoEntry = _SnIfMediaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 9, 1)
)
snIfMediaInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    snIfMediaInfoEntry.setStatus("current")


class _SnIfMediaType_Type(DisplayString):
    """Custom type snIfMediaType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnIfMediaType_Type.__name__ = "DisplayString"
_SnIfMediaType_Object = MibTableColumn
snIfMediaType = _SnIfMediaType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 9, 1, 1),
    _SnIfMediaType_Type()
)
snIfMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfMediaType.setStatus("current")


class _SnIfMediaVendorName_Type(DisplayString):
    """Custom type snIfMediaVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnIfMediaVendorName_Type.__name__ = "DisplayString"
_SnIfMediaVendorName_Object = MibTableColumn
snIfMediaVendorName = _SnIfMediaVendorName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 9, 1, 2),
    _SnIfMediaVendorName_Type()
)
snIfMediaVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfMediaVendorName.setStatus("current")


class _SnIfMediaVersion_Type(DisplayString):
    """Custom type snIfMediaVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnIfMediaVersion_Type.__name__ = "DisplayString"
_SnIfMediaVersion_Object = MibTableColumn
snIfMediaVersion = _SnIfMediaVersion_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 9, 1, 3),
    _SnIfMediaVersion_Type()
)
snIfMediaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfMediaVersion.setStatus("current")


class _SnIfMediaPartNumber_Type(DisplayString):
    """Custom type snIfMediaPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnIfMediaPartNumber_Type.__name__ = "DisplayString"
_SnIfMediaPartNumber_Object = MibTableColumn
snIfMediaPartNumber = _SnIfMediaPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 9, 1, 4),
    _SnIfMediaPartNumber_Type()
)
snIfMediaPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfMediaPartNumber.setStatus("current")


class _SnIfMediaSerialNumber_Type(DisplayString):
    """Custom type snIfMediaSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnIfMediaSerialNumber_Type.__name__ = "DisplayString"
_SnIfMediaSerialNumber_Object = MibTableColumn
snIfMediaSerialNumber = _SnIfMediaSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 9, 1, 5),
    _SnIfMediaSerialNumber_Type()
)
snIfMediaSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfMediaSerialNumber.setStatus("current")
_SnIfOpticalLaneMonitoringTable_Object = MibTable
snIfOpticalLaneMonitoringTable = _SnIfOpticalLaneMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 10)
)
if mibBuilder.loadTexts:
    snIfOpticalLaneMonitoringTable.setStatus("current")
_SnIfOpticalLaneMonitoringEntry_Object = MibTableRow
snIfOpticalLaneMonitoringEntry = _SnIfOpticalLaneMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 10, 1)
)
snIfOpticalLaneMonitoringEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snIfOpticalLaneMonitoringLane"),
)
if mibBuilder.loadTexts:
    snIfOpticalLaneMonitoringEntry.setStatus("current")
_SnIfOpticalLaneMonitoringLane_Type = Unsigned32
_SnIfOpticalLaneMonitoringLane_Object = MibTableColumn
snIfOpticalLaneMonitoringLane = _SnIfOpticalLaneMonitoringLane_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 10, 1, 1),
    _SnIfOpticalLaneMonitoringLane_Type()
)
snIfOpticalLaneMonitoringLane.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snIfOpticalLaneMonitoringLane.setStatus("current")


class _SnIfOpticalLaneMonitoringTemperature_Type(DisplayString):
    """Custom type snIfOpticalLaneMonitoringTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnIfOpticalLaneMonitoringTemperature_Type.__name__ = "DisplayString"
_SnIfOpticalLaneMonitoringTemperature_Object = MibTableColumn
snIfOpticalLaneMonitoringTemperature = _SnIfOpticalLaneMonitoringTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 10, 1, 2),
    _SnIfOpticalLaneMonitoringTemperature_Type()
)
snIfOpticalLaneMonitoringTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfOpticalLaneMonitoringTemperature.setStatus("current")


class _SnIfOpticalLaneMonitoringTxPower_Type(DisplayString):
    """Custom type snIfOpticalLaneMonitoringTxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnIfOpticalLaneMonitoringTxPower_Type.__name__ = "DisplayString"
_SnIfOpticalLaneMonitoringTxPower_Object = MibTableColumn
snIfOpticalLaneMonitoringTxPower = _SnIfOpticalLaneMonitoringTxPower_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 10, 1, 3),
    _SnIfOpticalLaneMonitoringTxPower_Type()
)
snIfOpticalLaneMonitoringTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfOpticalLaneMonitoringTxPower.setStatus("current")


class _SnIfOpticalLaneMonitoringRxPower_Type(DisplayString):
    """Custom type snIfOpticalLaneMonitoringRxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnIfOpticalLaneMonitoringRxPower_Type.__name__ = "DisplayString"
_SnIfOpticalLaneMonitoringRxPower_Object = MibTableColumn
snIfOpticalLaneMonitoringRxPower = _SnIfOpticalLaneMonitoringRxPower_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 10, 1, 4),
    _SnIfOpticalLaneMonitoringRxPower_Type()
)
snIfOpticalLaneMonitoringRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfOpticalLaneMonitoringRxPower.setStatus("current")


class _SnIfOpticalLaneMonitoringTxBiasCurrent_Type(DisplayString):
    """Custom type snIfOpticalLaneMonitoringTxBiasCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnIfOpticalLaneMonitoringTxBiasCurrent_Type.__name__ = "DisplayString"
_SnIfOpticalLaneMonitoringTxBiasCurrent_Object = MibTableColumn
snIfOpticalLaneMonitoringTxBiasCurrent = _SnIfOpticalLaneMonitoringTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 10, 1, 5),
    _SnIfOpticalLaneMonitoringTxBiasCurrent_Type()
)
snIfOpticalLaneMonitoringTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfOpticalLaneMonitoringTxBiasCurrent.setStatus("current")
_BrcdIfEgressCounterInfoTable_Object = MibTable
brcdIfEgressCounterInfoTable = _BrcdIfEgressCounterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 11)
)
if mibBuilder.loadTexts:
    brcdIfEgressCounterInfoTable.setStatus("current")
_BrcdIfEgressCounterInfoEntry_Object = MibTableRow
brcdIfEgressCounterInfoEntry = _BrcdIfEgressCounterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 11, 1)
)
brcdIfEgressCounterInfoEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "brcdIfEgressCounterIfIndex"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "brcdIfEgressCounterQueueId"),
)
if mibBuilder.loadTexts:
    brcdIfEgressCounterInfoEntry.setStatus("current")
_BrcdIfEgressCounterIfIndex_Type = InterfaceIndex
_BrcdIfEgressCounterIfIndex_Object = MibTableColumn
brcdIfEgressCounterIfIndex = _BrcdIfEgressCounterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 11, 1, 1),
    _BrcdIfEgressCounterIfIndex_Type()
)
brcdIfEgressCounterIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdIfEgressCounterIfIndex.setStatus("current")
_BrcdIfEgressCounterQueueId_Type = Integer32
_BrcdIfEgressCounterQueueId_Object = MibTableColumn
brcdIfEgressCounterQueueId = _BrcdIfEgressCounterQueueId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 11, 1, 2),
    _BrcdIfEgressCounterQueueId_Type()
)
brcdIfEgressCounterQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdIfEgressCounterQueueId.setStatus("current")


class _BrcdIfEgressCounterType_Type(Integer32):
    """Custom type brcdIfEgressCounterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 3),
          ("other", 1),
          ("unicast", 2))
    )


_BrcdIfEgressCounterType_Type.__name__ = "Integer32"
_BrcdIfEgressCounterType_Object = MibTableColumn
brcdIfEgressCounterType = _BrcdIfEgressCounterType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 11, 1, 3),
    _BrcdIfEgressCounterType_Type()
)
brcdIfEgressCounterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdIfEgressCounterType.setStatus("current")
_BrcdIfEgressCounterPkts_Type = Counter64
_BrcdIfEgressCounterPkts_Object = MibTableColumn
brcdIfEgressCounterPkts = _BrcdIfEgressCounterPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 11, 1, 4),
    _BrcdIfEgressCounterPkts_Type()
)
brcdIfEgressCounterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdIfEgressCounterPkts.setStatus("current")
_BrcdIfEgressCounterDropPkts_Type = Counter64
_BrcdIfEgressCounterDropPkts_Object = MibTableColumn
brcdIfEgressCounterDropPkts = _BrcdIfEgressCounterDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 3, 11, 1, 5),
    _BrcdIfEgressCounterDropPkts_Type()
)
brcdIfEgressCounterDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdIfEgressCounterDropPkts.setStatus("current")
_SnFdbInfo_ObjectIdentity = ObjectIdentity
snFdbInfo = _SnFdbInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 4)
)
_SnFdbTable_Object = MibTable
snFdbTable = _SnFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    snFdbTable.setStatus("current")
_SnFdbEntry_Object = MibTableRow
snFdbEntry = _SnFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 4, 1, 1)
)
snFdbEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snFdbStationIndex"),
)
if mibBuilder.loadTexts:
    snFdbEntry.setStatus("current")


class _SnFdbStationIndex_Type(Integer32):
    """Custom type snFdbStationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SnFdbStationIndex_Type.__name__ = "Integer32"
_SnFdbStationIndex_Object = MibTableColumn
snFdbStationIndex = _SnFdbStationIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 4, 1, 1, 1),
    _SnFdbStationIndex_Type()
)
snFdbStationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFdbStationIndex.setStatus("current")
_SnFdbStationAddr_Type = PhysAddress
_SnFdbStationAddr_Object = MibTableColumn
snFdbStationAddr = _SnFdbStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 4, 1, 1, 2),
    _SnFdbStationAddr_Type()
)
snFdbStationAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFdbStationAddr.setStatus("current")
_SnFdbStationPort_Type = Integer32
_SnFdbStationPort_Object = MibTableColumn
snFdbStationPort = _SnFdbStationPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 4, 1, 1, 3),
    _SnFdbStationPort_Type()
)
snFdbStationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFdbStationPort.setStatus("current")


class _SnFdbVLanId_Type(Integer32):
    """Custom type snFdbVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnFdbVLanId_Type.__name__ = "Integer32"
_SnFdbVLanId_Object = MibTableColumn
snFdbVLanId = _SnFdbVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 4, 1, 1, 4),
    _SnFdbVLanId_Type()
)
snFdbVLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFdbVLanId.setStatus("current")


class _SnFdbStationQos_Type(Integer32):
    """Custom type snFdbStationQos based on Integer32"""
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
        *(("level0", 0),
          ("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7))
    )


_SnFdbStationQos_Type.__name__ = "Integer32"
_SnFdbStationQos_Object = MibTableColumn
snFdbStationQos = _SnFdbStationQos_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 4, 1, 1, 5),
    _SnFdbStationQos_Type()
)
snFdbStationQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFdbStationQos.setStatus("current")


class _SnFdbStationType_Type(Integer32):
    """Custom type snFdbStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("notSupported", 0),
          ("router", 2))
    )


_SnFdbStationType_Type.__name__ = "Integer32"
_SnFdbStationType_Object = MibTableColumn
snFdbStationType = _SnFdbStationType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 4, 1, 1, 6),
    _SnFdbStationType_Type()
)
snFdbStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFdbStationType.setStatus("current")


class _SnFdbRowStatus_Type(Integer32):
    """Custom type snFdbRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnFdbRowStatus_Type.__name__ = "Integer32"
_SnFdbRowStatus_Object = MibTableColumn
snFdbRowStatus = _SnFdbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 4, 1, 1, 7),
    _SnFdbRowStatus_Type()
)
snFdbRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFdbRowStatus.setStatus("current")
_SnFdbStationIf_Type = InterfaceIndex
_SnFdbStationIf_Object = MibTableColumn
snFdbStationIf = _SnFdbStationIf_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 4, 1, 1, 8),
    _SnFdbStationIf_Type()
)
snFdbStationIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFdbStationIf.setStatus("current")
_SnPortStpInfo_ObjectIdentity = ObjectIdentity
snPortStpInfo = _SnPortStpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5)
)
_SnPortStpTable_Object = MibTable
snPortStpTable = _SnPortStpTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    snPortStpTable.setStatus("deprecated")
_SnPortStpEntry_Object = MibTableRow
snPortStpEntry = _SnPortStpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 1, 1)
)
snPortStpEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snPortStpVLanId"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snPortStpPortNum"),
)
if mibBuilder.loadTexts:
    snPortStpEntry.setStatus("deprecated")


class _SnPortStpVLanId_Type(Integer32):
    """Custom type snPortStpVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnPortStpVLanId_Type.__name__ = "Integer32"
_SnPortStpVLanId_Object = MibTableColumn
snPortStpVLanId = _SnPortStpVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 1, 1, 1),
    _SnPortStpVLanId_Type()
)
snPortStpVLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortStpVLanId.setStatus("deprecated")
_SnPortStpPortNum_Type = Integer32
_SnPortStpPortNum_Object = MibTableColumn
snPortStpPortNum = _SnPortStpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 1, 1, 2),
    _SnPortStpPortNum_Type()
)
snPortStpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortStpPortNum.setStatus("deprecated")


class _SnPortStpPortPriority_Type(Integer32):
    """Custom type snPortStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnPortStpPortPriority_Type.__name__ = "Integer32"
_SnPortStpPortPriority_Object = MibTableColumn
snPortStpPortPriority = _SnPortStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 1, 1, 3),
    _SnPortStpPortPriority_Type()
)
snPortStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortStpPortPriority.setStatus("deprecated")


class _SnPortStpPathCost_Type(Integer32):
    """Custom type snPortStpPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnPortStpPathCost_Type.__name__ = "Integer32"
_SnPortStpPathCost_Object = MibTableColumn
snPortStpPathCost = _SnPortStpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 1, 1, 4),
    _SnPortStpPathCost_Type()
)
snPortStpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortStpPathCost.setStatus("deprecated")


class _SnPortStpOperState_Type(Integer32):
    """Custom type snPortStpOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("notActivated", 0))
    )


_SnPortStpOperState_Type.__name__ = "Integer32"
_SnPortStpOperState_Object = MibTableColumn
snPortStpOperState = _SnPortStpOperState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 1, 1, 5),
    _SnPortStpOperState_Type()
)
snPortStpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortStpOperState.setStatus("deprecated")


class _SnPortStpPortEnable_Type(Integer32):
    """Custom type snPortStpPortEnable based on Integer32"""
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


_SnPortStpPortEnable_Type.__name__ = "Integer32"
_SnPortStpPortEnable_Object = MibTableColumn
snPortStpPortEnable = _SnPortStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 1, 1, 6),
    _SnPortStpPortEnable_Type()
)
snPortStpPortEnable.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snPortStpPortEnable.setStatus("deprecated")
_SnPortStpPortForwardTransitions_Type = Counter32
_SnPortStpPortForwardTransitions_Object = MibTableColumn
snPortStpPortForwardTransitions = _SnPortStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 1, 1, 7),
    _SnPortStpPortForwardTransitions_Type()
)
snPortStpPortForwardTransitions.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snPortStpPortForwardTransitions.setStatus("deprecated")


class _SnPortStpPortState_Type(Integer32):
    """Custom type snPortStpPortState based on Integer32"""
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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3),
          ("preforwarding", 7))
    )


_SnPortStpPortState_Type.__name__ = "Integer32"
_SnPortStpPortState_Object = MibTableColumn
snPortStpPortState = _SnPortStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 1, 1, 8),
    _SnPortStpPortState_Type()
)
snPortStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortStpPortState.setStatus("deprecated")
_SnPortStpPortDesignatedCost_Type = Integer32
_SnPortStpPortDesignatedCost_Object = MibTableColumn
snPortStpPortDesignatedCost = _SnPortStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 1, 1, 9),
    _SnPortStpPortDesignatedCost_Type()
)
snPortStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortStpPortDesignatedCost.setStatus("deprecated")
_SnPortStpPortDesignatedRoot_Type = BridgeId
_SnPortStpPortDesignatedRoot_Object = MibTableColumn
snPortStpPortDesignatedRoot = _SnPortStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 1, 1, 10),
    _SnPortStpPortDesignatedRoot_Type()
)
snPortStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortStpPortDesignatedRoot.setStatus("deprecated")
_SnPortStpPortDesignatedBridge_Type = BridgeId
_SnPortStpPortDesignatedBridge_Object = MibTableColumn
snPortStpPortDesignatedBridge = _SnPortStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 1, 1, 11),
    _SnPortStpPortDesignatedBridge_Type()
)
snPortStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortStpPortDesignatedBridge.setStatus("deprecated")


class _SnPortStpPortDesignatedPort_Type(OctetString):
    """Custom type snPortStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SnPortStpPortDesignatedPort_Type.__name__ = "OctetString"
_SnPortStpPortDesignatedPort_Object = MibTableColumn
snPortStpPortDesignatedPort = _SnPortStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 1, 1, 12),
    _SnPortStpPortDesignatedPort_Type()
)
snPortStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortStpPortDesignatedPort.setStatus("deprecated")


class _SnPortStpPortAdminRstp_Type(Integer32):
    """Custom type snPortStpPortAdminRstp based on Integer32"""
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


_SnPortStpPortAdminRstp_Type.__name__ = "Integer32"
_SnPortStpPortAdminRstp_Object = MibTableColumn
snPortStpPortAdminRstp = _SnPortStpPortAdminRstp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 1, 1, 13),
    _SnPortStpPortAdminRstp_Type()
)
snPortStpPortAdminRstp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortStpPortAdminRstp.setStatus("deprecated")


class _SnPortStpPortProtocolMigration_Type(Integer32):
    """Custom type snPortStpPortProtocolMigration based on Integer32"""
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


_SnPortStpPortProtocolMigration_Type.__name__ = "Integer32"
_SnPortStpPortProtocolMigration_Object = MibTableColumn
snPortStpPortProtocolMigration = _SnPortStpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 1, 1, 14),
    _SnPortStpPortProtocolMigration_Type()
)
snPortStpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortStpPortProtocolMigration.setStatus("deprecated")


class _SnPortStpPortAdminEdgePort_Type(Integer32):
    """Custom type snPortStpPortAdminEdgePort based on Integer32"""
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


_SnPortStpPortAdminEdgePort_Type.__name__ = "Integer32"
_SnPortStpPortAdminEdgePort_Object = MibTableColumn
snPortStpPortAdminEdgePort = _SnPortStpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 1, 1, 15),
    _SnPortStpPortAdminEdgePort_Type()
)
snPortStpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortStpPortAdminEdgePort.setStatus("deprecated")


class _SnPortStpPortAdminPointToPoint_Type(Integer32):
    """Custom type snPortStpPortAdminPointToPoint based on Integer32"""
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


_SnPortStpPortAdminPointToPoint_Type.__name__ = "Integer32"
_SnPortStpPortAdminPointToPoint_Object = MibTableColumn
snPortStpPortAdminPointToPoint = _SnPortStpPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 1, 1, 16),
    _SnPortStpPortAdminPointToPoint_Type()
)
snPortStpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortStpPortAdminPointToPoint.setStatus("deprecated")
_SnIfStpTable_Object = MibTable
snIfStpTable = _SnIfStpTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    snIfStpTable.setStatus("current")
_SnIfStpEntry_Object = MibTableRow
snIfStpEntry = _SnIfStpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1)
)
snIfStpEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snIfStpVLanId"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snIfStpPortNum"),
)
if mibBuilder.loadTexts:
    snIfStpEntry.setStatus("current")


class _SnIfStpVLanId_Type(Integer32):
    """Custom type snIfStpVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnIfStpVLanId_Type.__name__ = "Integer32"
_SnIfStpVLanId_Object = MibTableColumn
snIfStpVLanId = _SnIfStpVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 1),
    _SnIfStpVLanId_Type()
)
snIfStpVLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfStpVLanId.setStatus("current")
_SnIfStpPortNum_Type = InterfaceIndex
_SnIfStpPortNum_Object = MibTableColumn
snIfStpPortNum = _SnIfStpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 2),
    _SnIfStpPortNum_Type()
)
snIfStpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfStpPortNum.setStatus("current")


class _SnIfStpPortPriority_Type(Integer32):
    """Custom type snIfStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnIfStpPortPriority_Type.__name__ = "Integer32"
_SnIfStpPortPriority_Object = MibTableColumn
snIfStpPortPriority = _SnIfStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 3),
    _SnIfStpPortPriority_Type()
)
snIfStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIfStpPortPriority.setStatus("current")


class _SnIfStpCfgPathCost_Type(Integer32):
    """Custom type snIfStpCfgPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_SnIfStpCfgPathCost_Type.__name__ = "Integer32"
_SnIfStpCfgPathCost_Object = MibTableColumn
snIfStpCfgPathCost = _SnIfStpCfgPathCost_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 4),
    _SnIfStpCfgPathCost_Type()
)
snIfStpCfgPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIfStpCfgPathCost.setStatus("current")


class _SnIfStpOperState_Type(Integer32):
    """Custom type snIfStpOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("notActivated", 0))
    )


_SnIfStpOperState_Type.__name__ = "Integer32"
_SnIfStpOperState_Object = MibTableColumn
snIfStpOperState = _SnIfStpOperState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 5),
    _SnIfStpOperState_Type()
)
snIfStpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfStpOperState.setStatus("current")


class _SnIfStpPortState_Type(Integer32):
    """Custom type snIfStpPortState based on Integer32"""
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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3),
          ("preforwarding", 7))
    )


_SnIfStpPortState_Type.__name__ = "Integer32"
_SnIfStpPortState_Object = MibTableColumn
snIfStpPortState = _SnIfStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 8),
    _SnIfStpPortState_Type()
)
snIfStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfStpPortState.setStatus("current")
_SnIfStpPortDesignatedCost_Type = Integer32
_SnIfStpPortDesignatedCost_Object = MibTableColumn
snIfStpPortDesignatedCost = _SnIfStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 9),
    _SnIfStpPortDesignatedCost_Type()
)
snIfStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfStpPortDesignatedCost.setStatus("current")
_SnIfStpPortDesignatedRoot_Type = BridgeId
_SnIfStpPortDesignatedRoot_Object = MibTableColumn
snIfStpPortDesignatedRoot = _SnIfStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 10),
    _SnIfStpPortDesignatedRoot_Type()
)
snIfStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfStpPortDesignatedRoot.setStatus("current")
_SnIfStpPortDesignatedBridge_Type = BridgeId
_SnIfStpPortDesignatedBridge_Object = MibTableColumn
snIfStpPortDesignatedBridge = _SnIfStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 11),
    _SnIfStpPortDesignatedBridge_Type()
)
snIfStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfStpPortDesignatedBridge.setStatus("current")


class _SnIfStpPortDesignatedPort_Type(OctetString):
    """Custom type snIfStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SnIfStpPortDesignatedPort_Type.__name__ = "OctetString"
_SnIfStpPortDesignatedPort_Object = MibTableColumn
snIfStpPortDesignatedPort = _SnIfStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 12),
    _SnIfStpPortDesignatedPort_Type()
)
snIfStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfStpPortDesignatedPort.setStatus("current")
_SnIfStpPortAdminRstp_Type = TruthValue
_SnIfStpPortAdminRstp_Object = MibTableColumn
snIfStpPortAdminRstp = _SnIfStpPortAdminRstp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 13),
    _SnIfStpPortAdminRstp_Type()
)
snIfStpPortAdminRstp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIfStpPortAdminRstp.setStatus("current")
_SnIfStpPortProtocolMigration_Type = TruthValue
_SnIfStpPortProtocolMigration_Object = MibTableColumn
snIfStpPortProtocolMigration = _SnIfStpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 14),
    _SnIfStpPortProtocolMigration_Type()
)
snIfStpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIfStpPortProtocolMigration.setStatus("current")
_SnIfStpPortAdminEdgePort_Type = TruthValue
_SnIfStpPortAdminEdgePort_Object = MibTableColumn
snIfStpPortAdminEdgePort = _SnIfStpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 15),
    _SnIfStpPortAdminEdgePort_Type()
)
snIfStpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIfStpPortAdminEdgePort.setStatus("current")
_SnIfStpPortAdminPointToPoint_Type = TruthValue
_SnIfStpPortAdminPointToPoint_Object = MibTableColumn
snIfStpPortAdminPointToPoint = _SnIfStpPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 16),
    _SnIfStpPortAdminPointToPoint_Type()
)
snIfStpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIfStpPortAdminPointToPoint.setStatus("current")


class _SnIfStpOperPathCost_Type(Integer32):
    """Custom type snIfStpOperPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_SnIfStpOperPathCost_Type.__name__ = "Integer32"
_SnIfStpOperPathCost_Object = MibTableColumn
snIfStpOperPathCost = _SnIfStpOperPathCost_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 17),
    _SnIfStpOperPathCost_Type()
)
snIfStpOperPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfStpOperPathCost.setStatus("current")


class _SnIfStpPortRole_Type(Integer32):
    """Custom type snIfStpPortRole based on Integer32"""
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
        *(("alternate", 1),
          ("backupRole", 4),
          ("designated", 3),
          ("disabledRole", 5),
          ("root", 2),
          ("unknown", 0))
    )


_SnIfStpPortRole_Type.__name__ = "Integer32"
_SnIfStpPortRole_Object = MibTableColumn
snIfStpPortRole = _SnIfStpPortRole_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 18),
    _SnIfStpPortRole_Type()
)
snIfStpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfStpPortRole.setStatus("current")
_SnIfStpBPDUTransmitted_Type = Counter32
_SnIfStpBPDUTransmitted_Object = MibTableColumn
snIfStpBPDUTransmitted = _SnIfStpBPDUTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 19),
    _SnIfStpBPDUTransmitted_Type()
)
snIfStpBPDUTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfStpBPDUTransmitted.setStatus("current")
_SnIfStpBPDUReceived_Type = Counter32
_SnIfStpBPDUReceived_Object = MibTableColumn
snIfStpBPDUReceived = _SnIfStpBPDUReceived_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 20),
    _SnIfStpBPDUReceived_Type()
)
snIfStpBPDUReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfStpBPDUReceived.setStatus("current")
_SnIfRstpConfigBPDUReceived_Type = Counter32
_SnIfRstpConfigBPDUReceived_Object = MibTableColumn
snIfRstpConfigBPDUReceived = _SnIfRstpConfigBPDUReceived_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 21),
    _SnIfRstpConfigBPDUReceived_Type()
)
snIfRstpConfigBPDUReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfRstpConfigBPDUReceived.setStatus("current")
_SnIfRstpTCNBPDUReceived_Type = Counter32
_SnIfRstpTCNBPDUReceived_Object = MibTableColumn
snIfRstpTCNBPDUReceived = _SnIfRstpTCNBPDUReceived_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 22),
    _SnIfRstpTCNBPDUReceived_Type()
)
snIfRstpTCNBPDUReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfRstpTCNBPDUReceived.setStatus("current")
_SnIfRstpConfigBPDUTransmitted_Type = Counter32
_SnIfRstpConfigBPDUTransmitted_Object = MibTableColumn
snIfRstpConfigBPDUTransmitted = _SnIfRstpConfigBPDUTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 23),
    _SnIfRstpConfigBPDUTransmitted_Type()
)
snIfRstpConfigBPDUTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfRstpConfigBPDUTransmitted.setStatus("current")
_SnIfRstpTCNBPDUTransmitted_Type = Counter32
_SnIfRstpTCNBPDUTransmitted_Object = MibTableColumn
snIfRstpTCNBPDUTransmitted = _SnIfRstpTCNBPDUTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 5, 2, 1, 24),
    _SnIfRstpTCNBPDUTransmitted_Type()
)
snIfRstpTCNBPDUTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIfRstpTCNBPDUTransmitted.setStatus("current")
_SnTrunkInfo_ObjectIdentity = ObjectIdentity
snTrunkInfo = _SnTrunkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 6)
)
_SnTrunkTable_Object = MibTable
snTrunkTable = _SnTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 6, 1)
)
if mibBuilder.loadTexts:
    snTrunkTable.setStatus("current")
_SnTrunkEntry_Object = MibTableRow
snTrunkEntry = _SnTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 6, 1, 1)
)
snTrunkEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snTrunkIndex"),
)
if mibBuilder.loadTexts:
    snTrunkEntry.setStatus("current")
_SnTrunkIndex_Type = Integer32
_SnTrunkIndex_Object = MibTableColumn
snTrunkIndex = _SnTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 6, 1, 1, 1),
    _SnTrunkIndex_Type()
)
snTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snTrunkIndex.setStatus("current")
_SnTrunkPortMask_Type = PortMask
_SnTrunkPortMask_Object = MibTableColumn
snTrunkPortMask = _SnTrunkPortMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 6, 1, 1, 2),
    _SnTrunkPortMask_Type()
)
snTrunkPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snTrunkPortMask.setStatus("current")


class _SnTrunkType_Type(Integer32):
    """Custom type snTrunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("server", 2),
          ("switch", 1))
    )


_SnTrunkType_Type.__name__ = "Integer32"
_SnTrunkType_Object = MibTableColumn
snTrunkType = _SnTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 6, 1, 1, 3),
    _SnTrunkType_Type()
)
snTrunkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snTrunkType.setStatus("current")
_SnMSTrunkTable_Object = MibTable
snMSTrunkTable = _SnMSTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 6, 2)
)
if mibBuilder.loadTexts:
    snMSTrunkTable.setStatus("current")
_SnMSTrunkEntry_Object = MibTableRow
snMSTrunkEntry = _SnMSTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 6, 2, 1)
)
snMSTrunkEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snMSTrunkPortIndex"),
)
if mibBuilder.loadTexts:
    snMSTrunkEntry.setStatus("current")
_SnMSTrunkPortIndex_Type = Integer32
_SnMSTrunkPortIndex_Object = MibTableColumn
snMSTrunkPortIndex = _SnMSTrunkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 6, 2, 1, 1),
    _SnMSTrunkPortIndex_Type()
)
snMSTrunkPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMSTrunkPortIndex.setStatus("current")
_SnMSTrunkPortList_Type = OctetString
_SnMSTrunkPortList_Object = MibTableColumn
snMSTrunkPortList = _SnMSTrunkPortList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 6, 2, 1, 2),
    _SnMSTrunkPortList_Type()
)
snMSTrunkPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMSTrunkPortList.setStatus("current")


class _SnMSTrunkType_Type(Integer32):
    """Custom type snMSTrunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("server", 2),
          ("switch", 1))
    )


_SnMSTrunkType_Type.__name__ = "Integer32"
_SnMSTrunkType_Object = MibTableColumn
snMSTrunkType = _SnMSTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 6, 2, 1, 3),
    _SnMSTrunkType_Type()
)
snMSTrunkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMSTrunkType.setStatus("current")


class _SnMSTrunkRowStatus_Type(Integer32):
    """Custom type snMSTrunkRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnMSTrunkRowStatus_Type.__name__ = "Integer32"
_SnMSTrunkRowStatus_Object = MibTableColumn
snMSTrunkRowStatus = _SnMSTrunkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 6, 2, 1, 4),
    _SnMSTrunkRowStatus_Type()
)
snMSTrunkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMSTrunkRowStatus.setStatus("current")
_SnMSTrunkIfTable_Object = MibTable
snMSTrunkIfTable = _SnMSTrunkIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 6, 3)
)
if mibBuilder.loadTexts:
    snMSTrunkIfTable.setStatus("current")
_SnMSTrunkIfEntry_Object = MibTableRow
snMSTrunkIfEntry = _SnMSTrunkIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 6, 3, 1)
)
snMSTrunkIfEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snMSTrunkIfIndex"),
)
if mibBuilder.loadTexts:
    snMSTrunkIfEntry.setStatus("current")
_SnMSTrunkIfIndex_Type = Integer32
_SnMSTrunkIfIndex_Object = MibTableColumn
snMSTrunkIfIndex = _SnMSTrunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 6, 3, 1, 1),
    _SnMSTrunkIfIndex_Type()
)
snMSTrunkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMSTrunkIfIndex.setStatus("current")
_SnMSTrunkIfList_Type = OctetString
_SnMSTrunkIfList_Object = MibTableColumn
snMSTrunkIfList = _SnMSTrunkIfList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 6, 3, 1, 2),
    _SnMSTrunkIfList_Type()
)
snMSTrunkIfList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMSTrunkIfList.setStatus("current")


class _SnMSTrunkIfType_Type(Integer32):
    """Custom type snMSTrunkIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("server", 2),
          ("switch", 1))
    )


_SnMSTrunkIfType_Type.__name__ = "Integer32"
_SnMSTrunkIfType_Object = MibTableColumn
snMSTrunkIfType = _SnMSTrunkIfType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 6, 3, 1, 3),
    _SnMSTrunkIfType_Type()
)
snMSTrunkIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMSTrunkIfType.setStatus("current")


class _SnMSTrunkIfRowStatus_Type(Integer32):
    """Custom type snMSTrunkIfRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnMSTrunkIfRowStatus_Type.__name__ = "Integer32"
_SnMSTrunkIfRowStatus_Object = MibTableColumn
snMSTrunkIfRowStatus = _SnMSTrunkIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 6, 3, 1, 4),
    _SnMSTrunkIfRowStatus_Type()
)
snMSTrunkIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMSTrunkIfRowStatus.setStatus("current")
_SnSwSummary_ObjectIdentity = ObjectIdentity
snSwSummary = _SnSwSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 7)
)


class _SnSwSummaryMode_Type(Integer32):
    """Custom type snSwSummaryMode based on Integer32"""
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


_SnSwSummaryMode_Type.__name__ = "Integer32"
_SnSwSummaryMode_Object = MibScalar
snSwSummaryMode = _SnSwSummaryMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 7, 1),
    _SnSwSummaryMode_Type()
)
snSwSummaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSwSummaryMode.setStatus("current")
_SnDhcpGatewayListInfo_ObjectIdentity = ObjectIdentity
snDhcpGatewayListInfo = _SnDhcpGatewayListInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 8)
)
_SnDhcpGatewayListTable_Object = MibTable
snDhcpGatewayListTable = _SnDhcpGatewayListTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 8, 1)
)
if mibBuilder.loadTexts:
    snDhcpGatewayListTable.setStatus("current")
_SnDhcpGatewayListEntry_Object = MibTableRow
snDhcpGatewayListEntry = _SnDhcpGatewayListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 8, 1, 1)
)
snDhcpGatewayListEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snDhcpGatewayListId"),
)
if mibBuilder.loadTexts:
    snDhcpGatewayListEntry.setStatus("current")


class _SnDhcpGatewayListId_Type(Integer32):
    """Custom type snDhcpGatewayListId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SnDhcpGatewayListId_Type.__name__ = "Integer32"
_SnDhcpGatewayListId_Object = MibTableColumn
snDhcpGatewayListId = _SnDhcpGatewayListId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 8, 1, 1, 1),
    _SnDhcpGatewayListId_Type()
)
snDhcpGatewayListId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDhcpGatewayListId.setStatus("current")


class _SnDhcpGatewayListAddrList_Type(OctetString):
    """Custom type snDhcpGatewayListAddrList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 32),
    )


_SnDhcpGatewayListAddrList_Type.__name__ = "OctetString"
_SnDhcpGatewayListAddrList_Object = MibTableColumn
snDhcpGatewayListAddrList = _SnDhcpGatewayListAddrList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 8, 1, 1, 2),
    _SnDhcpGatewayListAddrList_Type()
)
snDhcpGatewayListAddrList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDhcpGatewayListAddrList.setStatus("current")


class _SnDhcpGatewayListRowStatus_Type(Integer32):
    """Custom type snDhcpGatewayListRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnDhcpGatewayListRowStatus_Type.__name__ = "Integer32"
_SnDhcpGatewayListRowStatus_Object = MibTableColumn
snDhcpGatewayListRowStatus = _SnDhcpGatewayListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 8, 1, 1, 3),
    _SnDhcpGatewayListRowStatus_Type()
)
snDhcpGatewayListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDhcpGatewayListRowStatus.setStatus("current")
_SnDnsInfo_ObjectIdentity = ObjectIdentity
snDnsInfo = _SnDnsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 9)
)


class _SnDnsDomainName_Type(DisplayString):
    """Custom type snDnsDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SnDnsDomainName_Type.__name__ = "DisplayString"
_SnDnsDomainName_Object = MibScalar
snDnsDomainName = _SnDnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 9, 1),
    _SnDnsDomainName_Type()
)
snDnsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDnsDomainName.setStatus("current")


class _SnDnsGatewayIpAddrList_Type(OctetString):
    """Custom type snDnsGatewayIpAddrList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SnDnsGatewayIpAddrList_Type.__name__ = "OctetString"
_SnDnsGatewayIpAddrList_Object = MibScalar
snDnsGatewayIpAddrList = _SnDnsGatewayIpAddrList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 9, 2),
    _SnDnsGatewayIpAddrList_Type()
)
snDnsGatewayIpAddrList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDnsGatewayIpAddrList.setStatus("current")
_SnMacFilter_ObjectIdentity = ObjectIdentity
snMacFilter = _SnMacFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10)
)
_SnMacFilterTable_Object = MibTable
snMacFilterTable = _SnMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 1)
)
if mibBuilder.loadTexts:
    snMacFilterTable.setStatus("current")
_SnMacFilterEntry_Object = MibTableRow
snMacFilterEntry = _SnMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 1, 1)
)
snMacFilterEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snMacFilterIndex"),
)
if mibBuilder.loadTexts:
    snMacFilterEntry.setStatus("current")
_SnMacFilterIndex_Type = Integer32
_SnMacFilterIndex_Object = MibTableColumn
snMacFilterIndex = _SnMacFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 1, 1, 1),
    _SnMacFilterIndex_Type()
)
snMacFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMacFilterIndex.setStatus("current")


class _SnMacFilterAction_Type(Integer32):
    """Custom type snMacFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_SnMacFilterAction_Type.__name__ = "Integer32"
_SnMacFilterAction_Object = MibTableColumn
snMacFilterAction = _SnMacFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 1, 1, 2),
    _SnMacFilterAction_Type()
)
snMacFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacFilterAction.setStatus("current")
_SnMacFilterSourceMac_Type = MacAddress
_SnMacFilterSourceMac_Object = MibTableColumn
snMacFilterSourceMac = _SnMacFilterSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 1, 1, 3),
    _SnMacFilterSourceMac_Type()
)
snMacFilterSourceMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacFilterSourceMac.setStatus("current")
_SnMacFilterSourceMask_Type = MacAddress
_SnMacFilterSourceMask_Object = MibTableColumn
snMacFilterSourceMask = _SnMacFilterSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 1, 1, 4),
    _SnMacFilterSourceMask_Type()
)
snMacFilterSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacFilterSourceMask.setStatus("current")
_SnMacFilterDestMac_Type = MacAddress
_SnMacFilterDestMac_Object = MibTableColumn
snMacFilterDestMac = _SnMacFilterDestMac_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 1, 1, 5),
    _SnMacFilterDestMac_Type()
)
snMacFilterDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacFilterDestMac.setStatus("current")
_SnMacFilterDestMask_Type = MacAddress
_SnMacFilterDestMask_Object = MibTableColumn
snMacFilterDestMask = _SnMacFilterDestMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 1, 1, 6),
    _SnMacFilterDestMask_Type()
)
snMacFilterDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacFilterDestMask.setStatus("current")


class _SnMacFilterOperator_Type(Integer32):
    """Custom type snMacFilterOperator based on Integer32"""
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
        *(("equal", 0),
          ("greater", 3),
          ("less", 2),
          ("notEqual", 1))
    )


_SnMacFilterOperator_Type.__name__ = "Integer32"
_SnMacFilterOperator_Object = MibTableColumn
snMacFilterOperator = _SnMacFilterOperator_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 1, 1, 7),
    _SnMacFilterOperator_Type()
)
snMacFilterOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacFilterOperator.setStatus("current")


class _SnMacFilterFrameType_Type(Integer32):
    """Custom type snMacFilterFrameType based on Integer32"""
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
        *(("ethernet", 1),
          ("llc", 2),
          ("notUsed", 0),
          ("snap", 3))
    )


_SnMacFilterFrameType_Type.__name__ = "Integer32"
_SnMacFilterFrameType_Object = MibTableColumn
snMacFilterFrameType = _SnMacFilterFrameType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 1, 1, 8),
    _SnMacFilterFrameType_Type()
)
snMacFilterFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacFilterFrameType.setStatus("current")


class _SnMacFilterFrameTypeNum_Type(Integer32):
    """Custom type snMacFilterFrameTypeNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnMacFilterFrameTypeNum_Type.__name__ = "Integer32"
_SnMacFilterFrameTypeNum_Object = MibTableColumn
snMacFilterFrameTypeNum = _SnMacFilterFrameTypeNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 1, 1, 9),
    _SnMacFilterFrameTypeNum_Type()
)
snMacFilterFrameTypeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacFilterFrameTypeNum.setStatus("current")


class _SnMacFilterRowStatus_Type(Integer32):
    """Custom type snMacFilterRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnMacFilterRowStatus_Type.__name__ = "Integer32"
_SnMacFilterRowStatus_Object = MibTableColumn
snMacFilterRowStatus = _SnMacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 1, 1, 10),
    _SnMacFilterRowStatus_Type()
)
snMacFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacFilterRowStatus.setStatus("current")
_SnMacFilterPortAccessTable_Object = MibTable
snMacFilterPortAccessTable = _SnMacFilterPortAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 2)
)
if mibBuilder.loadTexts:
    snMacFilterPortAccessTable.setStatus("deprecated")
_SnMacFilterPortAccessEntry_Object = MibTableRow
snMacFilterPortAccessEntry = _SnMacFilterPortAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 2, 1)
)
snMacFilterPortAccessEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snMacFilterPortAccessPortIndex"),
)
if mibBuilder.loadTexts:
    snMacFilterPortAccessEntry.setStatus("deprecated")


class _SnMacFilterPortAccessPortIndex_Type(Integer32):
    """Custom type snMacFilterPortAccessPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3900),
    )


_SnMacFilterPortAccessPortIndex_Type.__name__ = "Integer32"
_SnMacFilterPortAccessPortIndex_Object = MibTableColumn
snMacFilterPortAccessPortIndex = _SnMacFilterPortAccessPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 2, 1, 1),
    _SnMacFilterPortAccessPortIndex_Type()
)
snMacFilterPortAccessPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMacFilterPortAccessPortIndex.setStatus("deprecated")
_SnMacFilterPortAccessFilters_Type = OctetString
_SnMacFilterPortAccessFilters_Object = MibTableColumn
snMacFilterPortAccessFilters = _SnMacFilterPortAccessFilters_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 2, 1, 2),
    _SnMacFilterPortAccessFilters_Type()
)
snMacFilterPortAccessFilters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacFilterPortAccessFilters.setStatus("deprecated")


class _SnMacFilterPortAccessRowStatus_Type(Integer32):
    """Custom type snMacFilterPortAccessRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("valid", 2))
    )


_SnMacFilterPortAccessRowStatus_Type.__name__ = "Integer32"
_SnMacFilterPortAccessRowStatus_Object = MibTableColumn
snMacFilterPortAccessRowStatus = _SnMacFilterPortAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 2, 1, 3),
    _SnMacFilterPortAccessRowStatus_Type()
)
snMacFilterPortAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacFilterPortAccessRowStatus.setStatus("deprecated")
_SnMacFilterIfAccessTable_Object = MibTable
snMacFilterIfAccessTable = _SnMacFilterIfAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 3)
)
if mibBuilder.loadTexts:
    snMacFilterIfAccessTable.setStatus("current")
_SnMacFilterIfAccessEntry_Object = MibTableRow
snMacFilterIfAccessEntry = _SnMacFilterIfAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 3, 1)
)
snMacFilterIfAccessEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snMacFilterIfAccessPortIndex"),
)
if mibBuilder.loadTexts:
    snMacFilterIfAccessEntry.setStatus("current")
_SnMacFilterIfAccessPortIndex_Type = InterfaceIndex
_SnMacFilterIfAccessPortIndex_Object = MibTableColumn
snMacFilterIfAccessPortIndex = _SnMacFilterIfAccessPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 3, 1, 1),
    _SnMacFilterIfAccessPortIndex_Type()
)
snMacFilterIfAccessPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMacFilterIfAccessPortIndex.setStatus("current")
_SnMacFilterIfAccessFilters_Type = OctetString
_SnMacFilterIfAccessFilters_Object = MibTableColumn
snMacFilterIfAccessFilters = _SnMacFilterIfAccessFilters_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 3, 1, 2),
    _SnMacFilterIfAccessFilters_Type()
)
snMacFilterIfAccessFilters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacFilterIfAccessFilters.setStatus("current")


class _SnMacFilterIfAccessRowStatus_Type(Integer32):
    """Custom type snMacFilterIfAccessRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("valid", 2))
    )


_SnMacFilterIfAccessRowStatus_Type.__name__ = "Integer32"
_SnMacFilterIfAccessRowStatus_Object = MibTableColumn
snMacFilterIfAccessRowStatus = _SnMacFilterIfAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 10, 3, 1, 3),
    _SnMacFilterIfAccessRowStatus_Type()
)
snMacFilterIfAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacFilterIfAccessRowStatus.setStatus("current")
_SnNTP_ObjectIdentity = ObjectIdentity
snNTP = _SnNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 11)
)
_SnNTPGeneral_ObjectIdentity = ObjectIdentity
snNTPGeneral = _SnNTPGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 11, 1)
)


class _SnNTPPollInterval_Type(Integer32):
    """Custom type snNTPPollInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnNTPPollInterval_Type.__name__ = "Integer32"
_SnNTPPollInterval_Object = MibScalar
snNTPPollInterval = _SnNTPPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 11, 1, 1),
    _SnNTPPollInterval_Type()
)
snNTPPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNTPPollInterval.setStatus("current")


class _SnNTPTimeZone_Type(Integer32):
    """Custom type snNTPTimeZone based on Integer32"""
    defaultValue = 23

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
              45)
        )
    )
    namedValues = NamedValues(
        *(("alaska", 0),
          ("aleutian", 1),
          ("arizona", 2),
          ("central", 3),
          ("eastIndiana", 4),
          ("eastern", 5),
          ("gmt", 23),
          ("gmtMinus0100", 24),
          ("gmtMinus0200", 25),
          ("gmtMinus0300", 26),
          ("gmtMinus0330", 43),
          ("gmtMinus0400", 27),
          ("gmtMinus0500", 28),
          ("gmtMinus0600", 29),
          ("gmtMinus0700", 30),
          ("gmtMinus0800", 31),
          ("gmtMinus0830", 44),
          ("gmtMinus0900", 32),
          ("gmtMinus0930", 45),
          ("gmtMinus1000", 33),
          ("gmtMinus1100", 34),
          ("gmtMinus1200", 35),
          ("gmtPlus0100", 22),
          ("gmtPlus0200", 21),
          ("gmtPlus0300", 20),
          ("gmtPlus0330", 42),
          ("gmtPlus0400", 19),
          ("gmtPlus0430", 41),
          ("gmtPlus0500", 18),
          ("gmtPlus0530", 40),
          ("gmtPlus0600", 17),
          ("gmtPlus0630", 39),
          ("gmtPlus0700", 16),
          ("gmtPlus0800", 15),
          ("gmtPlus0900", 14),
          ("gmtPlus0930", 38),
          ("gmtPlus1000", 13),
          ("gmtPlus1030", 37),
          ("gmtPlus1100", 12),
          ("gmtPlus1130", 36),
          ("gmtPlus1200", 11),
          ("hawaii", 6),
          ("michigan", 7),
          ("mountain", 8),
          ("pacific", 9),
          ("samoa", 10))
    )


_SnNTPTimeZone_Type.__name__ = "Integer32"
_SnNTPTimeZone_Object = MibScalar
snNTPTimeZone = _SnNTPTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 11, 1, 2),
    _SnNTPTimeZone_Type()
)
snNTPTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNTPTimeZone.setStatus("current")


class _SnNTPSummerTimeEnable_Type(Integer32):
    """Custom type snNTPSummerTimeEnable based on Integer32"""
    defaultValue = 0

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


_SnNTPSummerTimeEnable_Type.__name__ = "Integer32"
_SnNTPSummerTimeEnable_Object = MibScalar
snNTPSummerTimeEnable = _SnNTPSummerTimeEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 11, 1, 3),
    _SnNTPSummerTimeEnable_Type()
)
snNTPSummerTimeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNTPSummerTimeEnable.setStatus("current")


class _SnNTPSystemClock_Type(OctetString):
    """Custom type snNTPSystemClock based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_SnNTPSystemClock_Type.__name__ = "OctetString"
_SnNTPSystemClock_Object = MibScalar
snNTPSystemClock = _SnNTPSystemClock_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 11, 1, 4),
    _SnNTPSystemClock_Type()
)
snNTPSystemClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNTPSystemClock.setStatus("current")


class _SnNTPSync_Type(Integer32):
    """Custom type snNTPSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("synchronize", 2))
    )


_SnNTPSync_Type.__name__ = "Integer32"
_SnNTPSync_Object = MibScalar
snNTPSync = _SnNTPSync_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 11, 1, 5),
    _SnNTPSync_Type()
)
snNTPSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNTPSync.setStatus("current")
_SnNTPServerTable_Object = MibTable
snNTPServerTable = _SnNTPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 11, 2)
)
if mibBuilder.loadTexts:
    snNTPServerTable.setStatus("current")
_SnNTPServerEntry_Object = MibTableRow
snNTPServerEntry = _SnNTPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 11, 2, 1)
)
snNTPServerEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snNTPServerIp"),
)
if mibBuilder.loadTexts:
    snNTPServerEntry.setStatus("current")
_SnNTPServerIp_Type = IpAddress
_SnNTPServerIp_Object = MibTableColumn
snNTPServerIp = _SnNTPServerIp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 11, 2, 1, 1),
    _SnNTPServerIp_Type()
)
snNTPServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snNTPServerIp.setStatus("current")


class _SnNTPServerVersion_Type(Integer32):
    """Custom type snNTPServerVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SnNTPServerVersion_Type.__name__ = "Integer32"
_SnNTPServerVersion_Object = MibTableColumn
snNTPServerVersion = _SnNTPServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 11, 2, 1, 2),
    _SnNTPServerVersion_Type()
)
snNTPServerVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNTPServerVersion.setStatus("current")


class _SnNTPServerRowStatus_Type(Integer32):
    """Custom type snNTPServerRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnNTPServerRowStatus_Type.__name__ = "Integer32"
_SnNTPServerRowStatus_Object = MibTableColumn
snNTPServerRowStatus = _SnNTPServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 11, 2, 1, 3),
    _SnNTPServerRowStatus_Type()
)
snNTPServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNTPServerRowStatus.setStatus("current")
_SnRadius_ObjectIdentity = ObjectIdentity
snRadius = _SnRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12)
)
_SnRadiusGeneral_ObjectIdentity = ObjectIdentity
snRadiusGeneral = _SnRadiusGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 1)
)


class _SnRadiusSNMPAccess_Type(Integer32):
    """Custom type snRadiusSNMPAccess based on Integer32"""
    defaultValue = 0

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


_SnRadiusSNMPAccess_Type.__name__ = "Integer32"
_SnRadiusSNMPAccess_Object = MibScalar
snRadiusSNMPAccess = _SnRadiusSNMPAccess_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 1, 1),
    _SnRadiusSNMPAccess_Type()
)
snRadiusSNMPAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRadiusSNMPAccess.setStatus("current")


class _SnRadiusEnableTelnetAuth_Type(Integer32):
    """Custom type snRadiusEnableTelnetAuth based on Integer32"""
    defaultValue = 0

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


_SnRadiusEnableTelnetAuth_Type.__name__ = "Integer32"
_SnRadiusEnableTelnetAuth_Object = MibScalar
snRadiusEnableTelnetAuth = _SnRadiusEnableTelnetAuth_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 1, 2),
    _SnRadiusEnableTelnetAuth_Type()
)
snRadiusEnableTelnetAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRadiusEnableTelnetAuth.setStatus("current")


class _SnRadiusRetransmit_Type(Integer32):
    """Custom type snRadiusRetransmit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SnRadiusRetransmit_Type.__name__ = "Integer32"
_SnRadiusRetransmit_Object = MibScalar
snRadiusRetransmit = _SnRadiusRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 1, 3),
    _SnRadiusRetransmit_Type()
)
snRadiusRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRadiusRetransmit.setStatus("current")


class _SnRadiusTimeOut_Type(Integer32):
    """Custom type snRadiusTimeOut based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SnRadiusTimeOut_Type.__name__ = "Integer32"
_SnRadiusTimeOut_Object = MibScalar
snRadiusTimeOut = _SnRadiusTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 1, 4),
    _SnRadiusTimeOut_Type()
)
snRadiusTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRadiusTimeOut.setStatus("current")


class _SnRadiusDeadTime_Type(Integer32):
    """Custom type snRadiusDeadTime based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SnRadiusDeadTime_Type.__name__ = "Integer32"
_SnRadiusDeadTime_Object = MibScalar
snRadiusDeadTime = _SnRadiusDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 1, 5),
    _SnRadiusDeadTime_Type()
)
snRadiusDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRadiusDeadTime.setStatus("current")
_SnRadiusKey_Type = DisplayString
_SnRadiusKey_Object = MibScalar
snRadiusKey = _SnRadiusKey_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 1, 6),
    _SnRadiusKey_Type()
)
snRadiusKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRadiusKey.setStatus("current")


class _SnRadiusLoginMethod_Type(OctetString):
    """Custom type snRadiusLoginMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_SnRadiusLoginMethod_Type.__name__ = "OctetString"
_SnRadiusLoginMethod_Object = MibScalar
snRadiusLoginMethod = _SnRadiusLoginMethod_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 1, 7),
    _SnRadiusLoginMethod_Type()
)
snRadiusLoginMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRadiusLoginMethod.setStatus("current")


class _SnRadiusEnableMethod_Type(OctetString):
    """Custom type snRadiusEnableMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_SnRadiusEnableMethod_Type.__name__ = "OctetString"
_SnRadiusEnableMethod_Object = MibScalar
snRadiusEnableMethod = _SnRadiusEnableMethod_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 1, 8),
    _SnRadiusEnableMethod_Type()
)
snRadiusEnableMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRadiusEnableMethod.setStatus("current")


class _SnRadiusWebServerMethod_Type(OctetString):
    """Custom type snRadiusWebServerMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_SnRadiusWebServerMethod_Type.__name__ = "OctetString"
_SnRadiusWebServerMethod_Object = MibScalar
snRadiusWebServerMethod = _SnRadiusWebServerMethod_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 1, 9),
    _SnRadiusWebServerMethod_Type()
)
snRadiusWebServerMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRadiusWebServerMethod.setStatus("current")


class _SnRadiusSNMPServerMethod_Type(OctetString):
    """Custom type snRadiusSNMPServerMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_SnRadiusSNMPServerMethod_Type.__name__ = "OctetString"
_SnRadiusSNMPServerMethod_Object = MibScalar
snRadiusSNMPServerMethod = _SnRadiusSNMPServerMethod_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 1, 10),
    _SnRadiusSNMPServerMethod_Type()
)
snRadiusSNMPServerMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRadiusSNMPServerMethod.setStatus("current")
_SnRadiusServerTable_Object = MibTable
snRadiusServerTable = _SnRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 2)
)
if mibBuilder.loadTexts:
    snRadiusServerTable.setStatus("current")
_SnRadiusServerEntry_Object = MibTableRow
snRadiusServerEntry = _SnRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 2, 1)
)
snRadiusServerEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snRadiusServerIp"),
)
if mibBuilder.loadTexts:
    snRadiusServerEntry.setStatus("current")
_SnRadiusServerIp_Type = IpAddress
_SnRadiusServerIp_Object = MibTableColumn
snRadiusServerIp = _SnRadiusServerIp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 2, 1, 1),
    _SnRadiusServerIp_Type()
)
snRadiusServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRadiusServerIp.setStatus("current")


class _SnRadiusServerAuthPort_Type(Integer32):
    """Custom type snRadiusServerAuthPort based on Integer32"""
    defaultValue = 1812


_SnRadiusServerAuthPort_Object = MibTableColumn
snRadiusServerAuthPort = _SnRadiusServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 2, 1, 2),
    _SnRadiusServerAuthPort_Type()
)
snRadiusServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRadiusServerAuthPort.setStatus("current")


class _SnRadiusServerAcctPort_Type(Integer32):
    """Custom type snRadiusServerAcctPort based on Integer32"""
    defaultValue = 1813


_SnRadiusServerAcctPort_Object = MibTableColumn
snRadiusServerAcctPort = _SnRadiusServerAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 2, 1, 3),
    _SnRadiusServerAcctPort_Type()
)
snRadiusServerAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRadiusServerAcctPort.setStatus("current")


class _SnRadiusServerRowStatus_Type(Integer32):
    """Custom type snRadiusServerRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnRadiusServerRowStatus_Type.__name__ = "Integer32"
_SnRadiusServerRowStatus_Object = MibTableColumn
snRadiusServerRowStatus = _SnRadiusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 2, 1, 4),
    _SnRadiusServerRowStatus_Type()
)
snRadiusServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRadiusServerRowStatus.setStatus("current")
_SnRadiusServerRowKey_Type = DisplayString
_SnRadiusServerRowKey_Object = MibTableColumn
snRadiusServerRowKey = _SnRadiusServerRowKey_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 2, 1, 5),
    _SnRadiusServerRowKey_Type()
)
snRadiusServerRowKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRadiusServerRowKey.setStatus("current")


class _SnRadiusServerUsage_Type(Integer32):
    """Custom type snRadiusServerUsage based on Integer32"""
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
        *(("accountingOnly", 4),
          ("authenticationOnly", 2),
          ("authorizationOnly", 3),
          ("default", 1))
    )


_SnRadiusServerUsage_Type.__name__ = "Integer32"
_SnRadiusServerUsage_Object = MibTableColumn
snRadiusServerUsage = _SnRadiusServerUsage_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 12, 2, 1, 6),
    _SnRadiusServerUsage_Type()
)
snRadiusServerUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRadiusServerUsage.setStatus("current")
_SnTacacs_ObjectIdentity = ObjectIdentity
snTacacs = _SnTacacs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 13)
)
_SnTacacsGeneral_ObjectIdentity = ObjectIdentity
snTacacsGeneral = _SnTacacsGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 13, 1)
)


class _SnTacacsRetransmit_Type(Integer32):
    """Custom type snTacacsRetransmit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SnTacacsRetransmit_Type.__name__ = "Integer32"
_SnTacacsRetransmit_Object = MibScalar
snTacacsRetransmit = _SnTacacsRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 13, 1, 1),
    _SnTacacsRetransmit_Type()
)
snTacacsRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snTacacsRetransmit.setStatus("current")


class _SnTacacsTimeOut_Type(Integer32):
    """Custom type snTacacsTimeOut based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SnTacacsTimeOut_Type.__name__ = "Integer32"
_SnTacacsTimeOut_Object = MibScalar
snTacacsTimeOut = _SnTacacsTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 13, 1, 2),
    _SnTacacsTimeOut_Type()
)
snTacacsTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snTacacsTimeOut.setStatus("current")


class _SnTacacsDeadTime_Type(Integer32):
    """Custom type snTacacsDeadTime based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SnTacacsDeadTime_Type.__name__ = "Integer32"
_SnTacacsDeadTime_Object = MibScalar
snTacacsDeadTime = _SnTacacsDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 13, 1, 3),
    _SnTacacsDeadTime_Type()
)
snTacacsDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snTacacsDeadTime.setStatus("current")
_SnTacacsKey_Type = DisplayString
_SnTacacsKey_Object = MibScalar
snTacacsKey = _SnTacacsKey_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 13, 1, 4),
    _SnTacacsKey_Type()
)
snTacacsKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snTacacsKey.setStatus("current")


class _SnTacacsSNMPAccess_Type(Integer32):
    """Custom type snTacacsSNMPAccess based on Integer32"""
    defaultValue = 0

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


_SnTacacsSNMPAccess_Type.__name__ = "Integer32"
_SnTacacsSNMPAccess_Object = MibScalar
snTacacsSNMPAccess = _SnTacacsSNMPAccess_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 13, 1, 5),
    _SnTacacsSNMPAccess_Type()
)
snTacacsSNMPAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snTacacsSNMPAccess.setStatus("current")
_SnTacacsServerTable_Object = MibTable
snTacacsServerTable = _SnTacacsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 13, 2)
)
if mibBuilder.loadTexts:
    snTacacsServerTable.setStatus("current")
_SnTacacsServerEntry_Object = MibTableRow
snTacacsServerEntry = _SnTacacsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 13, 2, 1)
)
snTacacsServerEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snTacacsServerIp"),
)
if mibBuilder.loadTexts:
    snTacacsServerEntry.setStatus("current")
_SnTacacsServerIp_Type = IpAddress
_SnTacacsServerIp_Object = MibTableColumn
snTacacsServerIp = _SnTacacsServerIp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 13, 2, 1, 1),
    _SnTacacsServerIp_Type()
)
snTacacsServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snTacacsServerIp.setStatus("current")


class _SnTacacsServerAuthPort_Type(Integer32):
    """Custom type snTacacsServerAuthPort based on Integer32"""
    defaultValue = 49


_SnTacacsServerAuthPort_Object = MibTableColumn
snTacacsServerAuthPort = _SnTacacsServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 13, 2, 1, 2),
    _SnTacacsServerAuthPort_Type()
)
snTacacsServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snTacacsServerAuthPort.setStatus("current")


class _SnTacacsServerRowStatus_Type(Integer32):
    """Custom type snTacacsServerRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnTacacsServerRowStatus_Type.__name__ = "Integer32"
_SnTacacsServerRowStatus_Object = MibTableColumn
snTacacsServerRowStatus = _SnTacacsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 13, 2, 1, 3),
    _SnTacacsServerRowStatus_Type()
)
snTacacsServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snTacacsServerRowStatus.setStatus("current")
_SnTacacsServerRowKey_Type = DisplayString
_SnTacacsServerRowKey_Object = MibTableColumn
snTacacsServerRowKey = _SnTacacsServerRowKey_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 13, 2, 1, 4),
    _SnTacacsServerRowKey_Type()
)
snTacacsServerRowKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snTacacsServerRowKey.setStatus("current")


class _SnTacacsServerUsage_Type(Integer32):
    """Custom type snTacacsServerUsage based on Integer32"""
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
        *(("accountingOnly", 4),
          ("authenticationOnly", 2),
          ("authorizationOnly", 3),
          ("default", 1))
    )


_SnTacacsServerUsage_Type.__name__ = "Integer32"
_SnTacacsServerUsage_Object = MibTableColumn
snTacacsServerUsage = _SnTacacsServerUsage_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 13, 2, 1, 5),
    _SnTacacsServerUsage_Type()
)
snTacacsServerUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snTacacsServerUsage.setStatus("current")
_SnQos_ObjectIdentity = ObjectIdentity
snQos = _SnQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14)
)
_SnQosProfileTable_Object = MibTable
snQosProfileTable = _SnQosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 1)
)
if mibBuilder.loadTexts:
    snQosProfileTable.setStatus("current")
_SnQosProfileEntry_Object = MibTableRow
snQosProfileEntry = _SnQosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 1, 1)
)
snQosProfileEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snQosProfileIndex"),
)
if mibBuilder.loadTexts:
    snQosProfileEntry.setStatus("current")


class _SnQosProfileIndex_Type(Integer32):
    """Custom type snQosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SnQosProfileIndex_Type.__name__ = "Integer32"
_SnQosProfileIndex_Object = MibTableColumn
snQosProfileIndex = _SnQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 1, 1, 1),
    _SnQosProfileIndex_Type()
)
snQosProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snQosProfileIndex.setStatus("current")


class _SnQosProfileName_Type(DisplayString):
    """Custom type snQosProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnQosProfileName_Type.__name__ = "DisplayString"
_SnQosProfileName_Object = MibTableColumn
snQosProfileName = _SnQosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 1, 1, 2),
    _SnQosProfileName_Type()
)
snQosProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snQosProfileName.setStatus("current")


class _SnQosProfileRequestedBandwidth_Type(Integer32):
    """Custom type snQosProfileRequestedBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SnQosProfileRequestedBandwidth_Type.__name__ = "Integer32"
_SnQosProfileRequestedBandwidth_Object = MibTableColumn
snQosProfileRequestedBandwidth = _SnQosProfileRequestedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 1, 1, 3),
    _SnQosProfileRequestedBandwidth_Type()
)
snQosProfileRequestedBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snQosProfileRequestedBandwidth.setStatus("current")


class _SnQosProfileCalculatedBandwidth_Type(Integer32):
    """Custom type snQosProfileCalculatedBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SnQosProfileCalculatedBandwidth_Type.__name__ = "Integer32"
_SnQosProfileCalculatedBandwidth_Object = MibTableColumn
snQosProfileCalculatedBandwidth = _SnQosProfileCalculatedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 1, 1, 4),
    _SnQosProfileCalculatedBandwidth_Type()
)
snQosProfileCalculatedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snQosProfileCalculatedBandwidth.setStatus("current")
_SnQosBindTable_Object = MibTable
snQosBindTable = _SnQosBindTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 2)
)
if mibBuilder.loadTexts:
    snQosBindTable.setStatus("current")
_SnQosBindEntry_Object = MibTableRow
snQosBindEntry = _SnQosBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 2, 1)
)
snQosBindEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snQosBindIndex"),
)
if mibBuilder.loadTexts:
    snQosBindEntry.setStatus("current")


class _SnQosBindIndex_Type(Integer32):
    """Custom type snQosBindIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SnQosBindIndex_Type.__name__ = "Integer32"
_SnQosBindIndex_Object = MibTableColumn
snQosBindIndex = _SnQosBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 2, 1, 1),
    _SnQosBindIndex_Type()
)
snQosBindIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snQosBindIndex.setStatus("current")
_SnQosBindPriority_Type = Integer32
_SnQosBindPriority_Object = MibTableColumn
snQosBindPriority = _SnQosBindPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 2, 1, 2),
    _SnQosBindPriority_Type()
)
snQosBindPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snQosBindPriority.setStatus("current")


class _SnQosBindProfileIndex_Type(Integer32):
    """Custom type snQosBindProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SnQosBindProfileIndex_Type.__name__ = "Integer32"
_SnQosBindProfileIndex_Object = MibTableColumn
snQosBindProfileIndex = _SnQosBindProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 2, 1, 3),
    _SnQosBindProfileIndex_Type()
)
snQosBindProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snQosBindProfileIndex.setStatus("current")
_SnDosAttack_ObjectIdentity = ObjectIdentity
snDosAttack = _SnDosAttack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 3)
)
_SnDosAttackGlobal_ObjectIdentity = ObjectIdentity
snDosAttackGlobal = _SnDosAttackGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 3, 1)
)
_SnDosAttackICMPDropCount_Type = Counter32
_SnDosAttackICMPDropCount_Object = MibScalar
snDosAttackICMPDropCount = _SnDosAttackICMPDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 3, 1, 1),
    _SnDosAttackICMPDropCount_Type()
)
snDosAttackICMPDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDosAttackICMPDropCount.setStatus("current")
_SnDosAttackICMPBlockCount_Type = Counter32
_SnDosAttackICMPBlockCount_Object = MibScalar
snDosAttackICMPBlockCount = _SnDosAttackICMPBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 3, 1, 2),
    _SnDosAttackICMPBlockCount_Type()
)
snDosAttackICMPBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDosAttackICMPBlockCount.setStatus("current")
_SnDosAttackSYNDropCount_Type = Counter32
_SnDosAttackSYNDropCount_Object = MibScalar
snDosAttackSYNDropCount = _SnDosAttackSYNDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 3, 1, 3),
    _SnDosAttackSYNDropCount_Type()
)
snDosAttackSYNDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDosAttackSYNDropCount.setStatus("current")
_SnDosAttackSYNBlockCount_Type = Counter32
_SnDosAttackSYNBlockCount_Object = MibScalar
snDosAttackSYNBlockCount = _SnDosAttackSYNBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 3, 1, 4),
    _SnDosAttackSYNBlockCount_Type()
)
snDosAttackSYNBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDosAttackSYNBlockCount.setStatus("current")
_SnDosAttackPortTable_Object = MibTable
snDosAttackPortTable = _SnDosAttackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 3, 2)
)
if mibBuilder.loadTexts:
    snDosAttackPortTable.setStatus("current")
_SnDosAttackPortEntry_Object = MibTableRow
snDosAttackPortEntry = _SnDosAttackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 3, 2, 1)
)
snDosAttackPortEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snDosAttackPort"),
)
if mibBuilder.loadTexts:
    snDosAttackPortEntry.setStatus("current")
_SnDosAttackPort_Type = Integer32
_SnDosAttackPort_Object = MibTableColumn
snDosAttackPort = _SnDosAttackPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 3, 2, 1, 1),
    _SnDosAttackPort_Type()
)
snDosAttackPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDosAttackPort.setStatus("current")
_SnDosAttackPortICMPDropCount_Type = Counter32
_SnDosAttackPortICMPDropCount_Object = MibTableColumn
snDosAttackPortICMPDropCount = _SnDosAttackPortICMPDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 3, 2, 1, 2),
    _SnDosAttackPortICMPDropCount_Type()
)
snDosAttackPortICMPDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDosAttackPortICMPDropCount.setStatus("current")
_SnDosAttackPortICMPBlockCount_Type = Counter32
_SnDosAttackPortICMPBlockCount_Object = MibTableColumn
snDosAttackPortICMPBlockCount = _SnDosAttackPortICMPBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 3, 2, 1, 3),
    _SnDosAttackPortICMPBlockCount_Type()
)
snDosAttackPortICMPBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDosAttackPortICMPBlockCount.setStatus("current")
_SnDosAttackPortSYNDropCount_Type = Counter32
_SnDosAttackPortSYNDropCount_Object = MibTableColumn
snDosAttackPortSYNDropCount = _SnDosAttackPortSYNDropCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 3, 2, 1, 4),
    _SnDosAttackPortSYNDropCount_Type()
)
snDosAttackPortSYNDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDosAttackPortSYNDropCount.setStatus("current")
_SnDosAttackPortSYNBlockCount_Type = Counter32
_SnDosAttackPortSYNBlockCount_Object = MibTableColumn
snDosAttackPortSYNBlockCount = _SnDosAttackPortSYNBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 14, 3, 2, 1, 5),
    _SnDosAttackPortSYNBlockCount_Type()
)
snDosAttackPortSYNBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDosAttackPortSYNBlockCount.setStatus("current")
_SnAAA_ObjectIdentity = ObjectIdentity
snAAA = _SnAAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 15)
)
_SnAuthentication_ObjectIdentity = ObjectIdentity
snAuthentication = _SnAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 15, 1)
)
_SnAuthorization_ObjectIdentity = ObjectIdentity
snAuthorization = _SnAuthorization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 15, 2)
)


class _SnAuthorizationCommandMethods_Type(OctetString):
    """Custom type snAuthorizationCommandMethods based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_SnAuthorizationCommandMethods_Type.__name__ = "OctetString"
_SnAuthorizationCommandMethods_Object = MibScalar
snAuthorizationCommandMethods = _SnAuthorizationCommandMethods_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 15, 2, 1),
    _SnAuthorizationCommandMethods_Type()
)
snAuthorizationCommandMethods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAuthorizationCommandMethods.setStatus("current")


class _SnAuthorizationCommandLevel_Type(Integer32):
    """Custom type snAuthorizationCommandLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("level0", 0),
          ("level4", 4),
          ("level5", 5))
    )


_SnAuthorizationCommandLevel_Type.__name__ = "Integer32"
_SnAuthorizationCommandLevel_Object = MibScalar
snAuthorizationCommandLevel = _SnAuthorizationCommandLevel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 15, 2, 2),
    _SnAuthorizationCommandLevel_Type()
)
snAuthorizationCommandLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAuthorizationCommandLevel.setStatus("current")


class _SnAuthorizationExec_Type(OctetString):
    """Custom type snAuthorizationExec based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_SnAuthorizationExec_Type.__name__ = "OctetString"
_SnAuthorizationExec_Object = MibScalar
snAuthorizationExec = _SnAuthorizationExec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 15, 2, 3),
    _SnAuthorizationExec_Type()
)
snAuthorizationExec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAuthorizationExec.setStatus("current")
_SnAccounting_ObjectIdentity = ObjectIdentity
snAccounting = _SnAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 15, 3)
)


class _SnAccountingCommandMethods_Type(OctetString):
    """Custom type snAccountingCommandMethods based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_SnAccountingCommandMethods_Type.__name__ = "OctetString"
_SnAccountingCommandMethods_Object = MibScalar
snAccountingCommandMethods = _SnAccountingCommandMethods_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 15, 3, 1),
    _SnAccountingCommandMethods_Type()
)
snAccountingCommandMethods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAccountingCommandMethods.setStatus("current")


class _SnAccountingCommandLevel_Type(Integer32):
    """Custom type snAccountingCommandLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("level0", 0),
          ("level4", 4),
          ("level5", 5))
    )


_SnAccountingCommandLevel_Type.__name__ = "Integer32"
_SnAccountingCommandLevel_Object = MibScalar
snAccountingCommandLevel = _SnAccountingCommandLevel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 15, 3, 2),
    _SnAccountingCommandLevel_Type()
)
snAccountingCommandLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAccountingCommandLevel.setStatus("current")


class _SnAccountingExec_Type(OctetString):
    """Custom type snAccountingExec based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_SnAccountingExec_Type.__name__ = "OctetString"
_SnAccountingExec_Object = MibScalar
snAccountingExec = _SnAccountingExec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 15, 3, 3),
    _SnAccountingExec_Type()
)
snAccountingExec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAccountingExec.setStatus("current")


class _SnAccountingSystem_Type(OctetString):
    """Custom type snAccountingSystem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_SnAccountingSystem_Type.__name__ = "OctetString"
_SnAccountingSystem_Object = MibScalar
snAccountingSystem = _SnAccountingSystem_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 15, 3, 4),
    _SnAccountingSystem_Type()
)
snAccountingSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAccountingSystem.setStatus("current")
_SnCAR_ObjectIdentity = ObjectIdentity
snCAR = _SnCAR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16)
)
_SnVLanCAR_ObjectIdentity = ObjectIdentity
snVLanCAR = _SnVLanCAR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17)
)
_SnNetFlow_ObjectIdentity = ObjectIdentity
snNetFlow = _SnNetFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18)
)
_SnNetFlowGlb_ObjectIdentity = ObjectIdentity
snNetFlowGlb = _SnNetFlowGlb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 1)
)


class _SnNetFlowGblEnable_Type(Integer32):
    """Custom type snNetFlowGblEnable based on Integer32"""
    defaultValue = 0

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


_SnNetFlowGblEnable_Type.__name__ = "Integer32"
_SnNetFlowGblEnable_Object = MibScalar
snNetFlowGblEnable = _SnNetFlowGblEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 1, 1),
    _SnNetFlowGblEnable_Type()
)
snNetFlowGblEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNetFlowGblEnable.setStatus("current")


class _SnNetFlowGblVersion_Type(Integer32):
    """Custom type snNetFlowGblVersion based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              5)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version5", 5),
          ("versionNotSet", 0))
    )


_SnNetFlowGblVersion_Type.__name__ = "Integer32"
_SnNetFlowGblVersion_Object = MibScalar
snNetFlowGblVersion = _SnNetFlowGblVersion_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 1, 2),
    _SnNetFlowGblVersion_Type()
)
snNetFlowGblVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNetFlowGblVersion.setStatus("current")


class _SnNetFlowGblProtocolDisable_Type(Integer32):
    """Custom type snNetFlowGblProtocolDisable based on Integer32"""
    defaultValue = 0


_SnNetFlowGblProtocolDisable_Object = MibScalar
snNetFlowGblProtocolDisable = _SnNetFlowGblProtocolDisable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 1, 3),
    _SnNetFlowGblProtocolDisable_Type()
)
snNetFlowGblProtocolDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNetFlowGblProtocolDisable.setStatus("current")


class _SnNetFlowGblActiveTimeout_Type(Integer32):
    """Custom type snNetFlowGblActiveTimeout based on Integer32"""
    defaultValue = 60


_SnNetFlowGblActiveTimeout_Object = MibScalar
snNetFlowGblActiveTimeout = _SnNetFlowGblActiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 1, 4),
    _SnNetFlowGblActiveTimeout_Type()
)
snNetFlowGblActiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNetFlowGblActiveTimeout.setStatus("current")


class _SnNetFlowGblInactiveTimeout_Type(Integer32):
    """Custom type snNetFlowGblInactiveTimeout based on Integer32"""
    defaultValue = 60


_SnNetFlowGblInactiveTimeout_Object = MibScalar
snNetFlowGblInactiveTimeout = _SnNetFlowGblInactiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 1, 5),
    _SnNetFlowGblInactiveTimeout_Type()
)
snNetFlowGblInactiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNetFlowGblInactiveTimeout.setStatus("current")
_SnNetFlowCollectorTable_Object = MibTable
snNetFlowCollectorTable = _SnNetFlowCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 2)
)
if mibBuilder.loadTexts:
    snNetFlowCollectorTable.setStatus("current")
_SnNetFlowCollectorEntry_Object = MibTableRow
snNetFlowCollectorEntry = _SnNetFlowCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 2, 1)
)
snNetFlowCollectorEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snNetFlowCollectorIndex"),
)
if mibBuilder.loadTexts:
    snNetFlowCollectorEntry.setStatus("current")


class _SnNetFlowCollectorIndex_Type(Integer32):
    """Custom type snNetFlowCollectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SnNetFlowCollectorIndex_Type.__name__ = "Integer32"
_SnNetFlowCollectorIndex_Object = MibTableColumn
snNetFlowCollectorIndex = _SnNetFlowCollectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 2, 1, 1),
    _SnNetFlowCollectorIndex_Type()
)
snNetFlowCollectorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snNetFlowCollectorIndex.setStatus("current")
_SnNetFlowCollectorIp_Type = IpAddress
_SnNetFlowCollectorIp_Object = MibTableColumn
snNetFlowCollectorIp = _SnNetFlowCollectorIp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 2, 1, 2),
    _SnNetFlowCollectorIp_Type()
)
snNetFlowCollectorIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNetFlowCollectorIp.setStatus("current")
_SnNetFlowCollectorUdpPort_Type = Integer32
_SnNetFlowCollectorUdpPort_Object = MibTableColumn
snNetFlowCollectorUdpPort = _SnNetFlowCollectorUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 2, 1, 3),
    _SnNetFlowCollectorUdpPort_Type()
)
snNetFlowCollectorUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNetFlowCollectorUdpPort.setStatus("current")
_SnNetFlowCollectorSourceInterface_Type = InterfaceIndex
_SnNetFlowCollectorSourceInterface_Object = MibTableColumn
snNetFlowCollectorSourceInterface = _SnNetFlowCollectorSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 2, 1, 4),
    _SnNetFlowCollectorSourceInterface_Type()
)
snNetFlowCollectorSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNetFlowCollectorSourceInterface.setStatus("current")


class _SnNetFlowCollectorRowStatus_Type(Integer32):
    """Custom type snNetFlowCollectorRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnNetFlowCollectorRowStatus_Type.__name__ = "Integer32"
_SnNetFlowCollectorRowStatus_Object = MibTableColumn
snNetFlowCollectorRowStatus = _SnNetFlowCollectorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 2, 1, 5),
    _SnNetFlowCollectorRowStatus_Type()
)
snNetFlowCollectorRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNetFlowCollectorRowStatus.setStatus("current")
_SnNetFlowAggregationTable_Object = MibTable
snNetFlowAggregationTable = _SnNetFlowAggregationTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 3)
)
if mibBuilder.loadTexts:
    snNetFlowAggregationTable.setStatus("current")
_SnNetFlowAggregationEntry_Object = MibTableRow
snNetFlowAggregationEntry = _SnNetFlowAggregationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 3, 1)
)
snNetFlowAggregationEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snNetFlowAggregationIndex"),
)
if mibBuilder.loadTexts:
    snNetFlowAggregationEntry.setStatus("current")


class _SnNetFlowAggregationIndex_Type(Integer32):
    """Custom type snNetFlowAggregationIndex based on Integer32"""
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
        *(("as", 1),
          ("destPrefix", 3),
          ("prefix", 5),
          ("protocolPort", 2),
          ("sourcePrefix", 4))
    )


_SnNetFlowAggregationIndex_Type.__name__ = "Integer32"
_SnNetFlowAggregationIndex_Object = MibTableColumn
snNetFlowAggregationIndex = _SnNetFlowAggregationIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 3, 1, 1),
    _SnNetFlowAggregationIndex_Type()
)
snNetFlowAggregationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snNetFlowAggregationIndex.setStatus("current")
_SnNetFlowAggregationIp_Type = IpAddress
_SnNetFlowAggregationIp_Object = MibTableColumn
snNetFlowAggregationIp = _SnNetFlowAggregationIp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 3, 1, 2),
    _SnNetFlowAggregationIp_Type()
)
snNetFlowAggregationIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNetFlowAggregationIp.setStatus("current")
_SnNetFlowAggregationUdpPort_Type = Integer32
_SnNetFlowAggregationUdpPort_Object = MibTableColumn
snNetFlowAggregationUdpPort = _SnNetFlowAggregationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 3, 1, 3),
    _SnNetFlowAggregationUdpPort_Type()
)
snNetFlowAggregationUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNetFlowAggregationUdpPort.setStatus("current")
_SnNetFlowAggregationSourceInterface_Type = InterfaceIndex
_SnNetFlowAggregationSourceInterface_Object = MibTableColumn
snNetFlowAggregationSourceInterface = _SnNetFlowAggregationSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 3, 1, 4),
    _SnNetFlowAggregationSourceInterface_Type()
)
snNetFlowAggregationSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNetFlowAggregationSourceInterface.setStatus("current")
_SnNetFlowAggregationNumberOfCacheEntries_Type = Integer32
_SnNetFlowAggregationNumberOfCacheEntries_Object = MibTableColumn
snNetFlowAggregationNumberOfCacheEntries = _SnNetFlowAggregationNumberOfCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 3, 1, 5),
    _SnNetFlowAggregationNumberOfCacheEntries_Type()
)
snNetFlowAggregationNumberOfCacheEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNetFlowAggregationNumberOfCacheEntries.setStatus("current")
_SnNetFlowAggregationActiveTimeout_Type = Integer32
_SnNetFlowAggregationActiveTimeout_Object = MibTableColumn
snNetFlowAggregationActiveTimeout = _SnNetFlowAggregationActiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 3, 1, 6),
    _SnNetFlowAggregationActiveTimeout_Type()
)
snNetFlowAggregationActiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNetFlowAggregationActiveTimeout.setStatus("current")
_SnNetFlowAggregationInactiveTimeout_Type = Integer32
_SnNetFlowAggregationInactiveTimeout_Object = MibTableColumn
snNetFlowAggregationInactiveTimeout = _SnNetFlowAggregationInactiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 3, 1, 7),
    _SnNetFlowAggregationInactiveTimeout_Type()
)
snNetFlowAggregationInactiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNetFlowAggregationInactiveTimeout.setStatus("current")


class _SnNetFlowAggregationEnable_Type(Integer32):
    """Custom type snNetFlowAggregationEnable based on Integer32"""
    defaultValue = 0

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


_SnNetFlowAggregationEnable_Type.__name__ = "Integer32"
_SnNetFlowAggregationEnable_Object = MibTableColumn
snNetFlowAggregationEnable = _SnNetFlowAggregationEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 3, 1, 8),
    _SnNetFlowAggregationEnable_Type()
)
snNetFlowAggregationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNetFlowAggregationEnable.setStatus("current")


class _SnNetFlowAggregationRowStatus_Type(Integer32):
    """Custom type snNetFlowAggregationRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnNetFlowAggregationRowStatus_Type.__name__ = "Integer32"
_SnNetFlowAggregationRowStatus_Object = MibTableColumn
snNetFlowAggregationRowStatus = _SnNetFlowAggregationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 3, 1, 9),
    _SnNetFlowAggregationRowStatus_Type()
)
snNetFlowAggregationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNetFlowAggregationRowStatus.setStatus("current")
_SnNetFlowIfTable_Object = MibTable
snNetFlowIfTable = _SnNetFlowIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 4)
)
if mibBuilder.loadTexts:
    snNetFlowIfTable.setStatus("current")
_SnNetFlowIfEntry_Object = MibTableRow
snNetFlowIfEntry = _SnNetFlowIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 4, 1)
)
snNetFlowIfEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snNetFlowIfIndex"),
)
if mibBuilder.loadTexts:
    snNetFlowIfEntry.setStatus("current")
_SnNetFlowIfIndex_Type = InterfaceIndex
_SnNetFlowIfIndex_Object = MibTableColumn
snNetFlowIfIndex = _SnNetFlowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 4, 1, 1),
    _SnNetFlowIfIndex_Type()
)
snNetFlowIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snNetFlowIfIndex.setStatus("current")


class _SnNetFlowIfFlowSwitching_Type(Integer32):
    """Custom type snNetFlowIfFlowSwitching based on Integer32"""
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


_SnNetFlowIfFlowSwitching_Type.__name__ = "Integer32"
_SnNetFlowIfFlowSwitching_Object = MibTableColumn
snNetFlowIfFlowSwitching = _SnNetFlowIfFlowSwitching_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 18, 4, 1, 2),
    _SnNetFlowIfFlowSwitching_Type()
)
snNetFlowIfFlowSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snNetFlowIfFlowSwitching.setStatus("current")
_SnSFlow_ObjectIdentity = ObjectIdentity
snSFlow = _SnSFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 19)
)
_SnSFlowGlb_ObjectIdentity = ObjectIdentity
snSFlowGlb = _SnSFlowGlb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 19, 1)
)
_SnSflowCollectorTable_Object = MibTable
snSflowCollectorTable = _SnSflowCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 19, 2)
)
if mibBuilder.loadTexts:
    snSflowCollectorTable.setStatus("current")
_SnSflowCollectorEntry_Object = MibTableRow
snSflowCollectorEntry = _SnSflowCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 19, 2, 1)
)
snSflowCollectorEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snSflowCollectorIndex"),
)
if mibBuilder.loadTexts:
    snSflowCollectorEntry.setStatus("current")
_SnSflowCollectorIndex_Type = Integer32
_SnSflowCollectorIndex_Object = MibTableColumn
snSflowCollectorIndex = _SnSflowCollectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 19, 2, 1, 1),
    _SnSflowCollectorIndex_Type()
)
snSflowCollectorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSflowCollectorIndex.setStatus("current")
_SnSflowCollectorIP_Type = IpAddress
_SnSflowCollectorIP_Object = MibTableColumn
snSflowCollectorIP = _SnSflowCollectorIP_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 19, 2, 1, 2),
    _SnSflowCollectorIP_Type()
)
snSflowCollectorIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSflowCollectorIP.setStatus("current")
_SnSflowCollectorUDPPort_Type = Integer32
_SnSflowCollectorUDPPort_Object = MibTableColumn
snSflowCollectorUDPPort = _SnSflowCollectorUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 19, 2, 1, 3),
    _SnSflowCollectorUDPPort_Type()
)
snSflowCollectorUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSflowCollectorUDPPort.setStatus("current")


class _SnSflowCollectorRowStatus_Type(Integer32):
    """Custom type snSflowCollectorRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("modify", 5),
          ("noSuch", 0),
          ("other", 1),
          ("valid", 2))
    )


_SnSflowCollectorRowStatus_Type.__name__ = "Integer32"
_SnSflowCollectorRowStatus_Object = MibTableColumn
snSflowCollectorRowStatus = _SnSflowCollectorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 19, 2, 1, 4),
    _SnSflowCollectorRowStatus_Type()
)
snSflowCollectorRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snSflowCollectorRowStatus.setStatus("current")
_SnFDP_ObjectIdentity = ObjectIdentity
snFDP = _SnFDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20)
)
_SnFdpMIBObjects_ObjectIdentity = ObjectIdentity
snFdpMIBObjects = _SnFdpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1)
)
_SnFdpInterface_ObjectIdentity = ObjectIdentity
snFdpInterface = _SnFdpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 1)
)
_SnFdpInterfaceTable_Object = MibTable
snFdpInterfaceTable = _SnFdpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 1, 1)
)
if mibBuilder.loadTexts:
    snFdpInterfaceTable.setStatus("current")
_SnFdpInterfaceEntry_Object = MibTableRow
snFdpInterfaceEntry = _SnFdpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 1, 1, 1)
)
snFdpInterfaceEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snFdpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    snFdpInterfaceEntry.setStatus("current")
_SnFdpInterfaceIfIndex_Type = InterfaceIndex
_SnFdpInterfaceIfIndex_Object = MibTableColumn
snFdpInterfaceIfIndex = _SnFdpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 1, 1, 1, 1),
    _SnFdpInterfaceIfIndex_Type()
)
snFdpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snFdpInterfaceIfIndex.setStatus("current")


class _SnFdpInterfaceFdpEnable_Type(Integer32):
    """Custom type snFdpInterfaceFdpEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnFdpInterfaceFdpEnable_Type.__name__ = "Integer32"
_SnFdpInterfaceFdpEnable_Object = MibTableColumn
snFdpInterfaceFdpEnable = _SnFdpInterfaceFdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 1, 1, 1, 2),
    _SnFdpInterfaceFdpEnable_Type()
)
snFdpInterfaceFdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFdpInterfaceFdpEnable.setStatus("current")


class _SnFdpInterfaceCdpEnable_Type(Integer32):
    """Custom type snFdpInterfaceCdpEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnFdpInterfaceCdpEnable_Type.__name__ = "Integer32"
_SnFdpInterfaceCdpEnable_Object = MibTableColumn
snFdpInterfaceCdpEnable = _SnFdpInterfaceCdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 1, 1, 1, 3),
    _SnFdpInterfaceCdpEnable_Type()
)
snFdpInterfaceCdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFdpInterfaceCdpEnable.setStatus("current")
_SnFdpCache_ObjectIdentity = ObjectIdentity
snFdpCache = _SnFdpCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 2)
)
_SnFdpCacheTable_Object = MibTable
snFdpCacheTable = _SnFdpCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 2, 1)
)
if mibBuilder.loadTexts:
    snFdpCacheTable.setStatus("current")
_SnFdpCacheEntry_Object = MibTableRow
snFdpCacheEntry = _SnFdpCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 2, 1, 1)
)
snFdpCacheEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snFdpCacheIfIndex"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snFdpCacheDeviceIndex"),
)
if mibBuilder.loadTexts:
    snFdpCacheEntry.setStatus("current")
_SnFdpCacheIfIndex_Type = InterfaceIndex
_SnFdpCacheIfIndex_Object = MibTableColumn
snFdpCacheIfIndex = _SnFdpCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 2, 1, 1, 1),
    _SnFdpCacheIfIndex_Type()
)
snFdpCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snFdpCacheIfIndex.setStatus("current")
_SnFdpCacheDeviceIndex_Type = Integer32
_SnFdpCacheDeviceIndex_Object = MibTableColumn
snFdpCacheDeviceIndex = _SnFdpCacheDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 2, 1, 1, 2),
    _SnFdpCacheDeviceIndex_Type()
)
snFdpCacheDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snFdpCacheDeviceIndex.setStatus("current")
_SnFdpCacheDeviceId_Type = DisplayString
_SnFdpCacheDeviceId_Object = MibTableColumn
snFdpCacheDeviceId = _SnFdpCacheDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 2, 1, 1, 3),
    _SnFdpCacheDeviceId_Type()
)
snFdpCacheDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFdpCacheDeviceId.setStatus("current")


class _SnFdpCacheAddressType_Type(Integer32):
    """Custom type snFdpCacheAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("appletalk", 3),
          ("ip", 1),
          ("ipx", 2))
    )


_SnFdpCacheAddressType_Type.__name__ = "Integer32"
_SnFdpCacheAddressType_Object = MibTableColumn
snFdpCacheAddressType = _SnFdpCacheAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 2, 1, 1, 4),
    _SnFdpCacheAddressType_Type()
)
snFdpCacheAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFdpCacheAddressType.setStatus("current")
_SnFdpCacheAddress_Type = OctetString
_SnFdpCacheAddress_Object = MibTableColumn
snFdpCacheAddress = _SnFdpCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 2, 1, 1, 5),
    _SnFdpCacheAddress_Type()
)
snFdpCacheAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFdpCacheAddress.setStatus("current")
_SnFdpCacheVersion_Type = DisplayString
_SnFdpCacheVersion_Object = MibTableColumn
snFdpCacheVersion = _SnFdpCacheVersion_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 2, 1, 1, 6),
    _SnFdpCacheVersion_Type()
)
snFdpCacheVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFdpCacheVersion.setStatus("current")
_SnFdpCacheDevicePort_Type = DisplayString
_SnFdpCacheDevicePort_Object = MibTableColumn
snFdpCacheDevicePort = _SnFdpCacheDevicePort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 2, 1, 1, 7),
    _SnFdpCacheDevicePort_Type()
)
snFdpCacheDevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFdpCacheDevicePort.setStatus("current")
_SnFdpCachePlatform_Type = DisplayString
_SnFdpCachePlatform_Object = MibTableColumn
snFdpCachePlatform = _SnFdpCachePlatform_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 2, 1, 1, 8),
    _SnFdpCachePlatform_Type()
)
snFdpCachePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFdpCachePlatform.setStatus("current")
_SnFdpCacheCapabilities_Type = DisplayString
_SnFdpCacheCapabilities_Object = MibTableColumn
snFdpCacheCapabilities = _SnFdpCacheCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 2, 1, 1, 9),
    _SnFdpCacheCapabilities_Type()
)
snFdpCacheCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFdpCacheCapabilities.setStatus("current")


class _SnFdpCacheVendorId_Type(Integer32):
    """Custom type snFdpCacheVendorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cdp", 2),
          ("fdp", 1))
    )


_SnFdpCacheVendorId_Type.__name__ = "Integer32"
_SnFdpCacheVendorId_Object = MibTableColumn
snFdpCacheVendorId = _SnFdpCacheVendorId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 2, 1, 1, 10),
    _SnFdpCacheVendorId_Type()
)
snFdpCacheVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFdpCacheVendorId.setStatus("current")


class _SnFdpCacheIsAggregateVlan_Type(Integer32):
    """Custom type snFdpCacheIsAggregateVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnFdpCacheIsAggregateVlan_Type.__name__ = "Integer32"
_SnFdpCacheIsAggregateVlan_Object = MibTableColumn
snFdpCacheIsAggregateVlan = _SnFdpCacheIsAggregateVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 2, 1, 1, 11),
    _SnFdpCacheIsAggregateVlan_Type()
)
snFdpCacheIsAggregateVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFdpCacheIsAggregateVlan.setStatus("current")
_SnFdpCacheTagType_Type = Integer32
_SnFdpCacheTagType_Object = MibTableColumn
snFdpCacheTagType = _SnFdpCacheTagType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 2, 1, 1, 12),
    _SnFdpCacheTagType_Type()
)
snFdpCacheTagType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFdpCacheTagType.setStatus("current")
_SnFdpCachePortVlanMask_Type = OctetString
_SnFdpCachePortVlanMask_Object = MibTableColumn
snFdpCachePortVlanMask = _SnFdpCachePortVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 2, 1, 1, 13),
    _SnFdpCachePortVlanMask_Type()
)
snFdpCachePortVlanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFdpCachePortVlanMask.setStatus("current")


class _SnFdpCachePortTagMode_Type(Integer32):
    """Custom type snFdpCachePortTagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dual", 3),
          ("tagged", 2),
          ("untagged", 1))
    )


_SnFdpCachePortTagMode_Type.__name__ = "Integer32"
_SnFdpCachePortTagMode_Object = MibTableColumn
snFdpCachePortTagMode = _SnFdpCachePortTagMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 2, 1, 1, 14),
    _SnFdpCachePortTagMode_Type()
)
snFdpCachePortTagMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFdpCachePortTagMode.setStatus("current")
_SnFdpCacheDefaultTrafficeVlanIdForDualMode_Type = Integer32
_SnFdpCacheDefaultTrafficeVlanIdForDualMode_Object = MibTableColumn
snFdpCacheDefaultTrafficeVlanIdForDualMode = _SnFdpCacheDefaultTrafficeVlanIdForDualMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 2, 1, 1, 15),
    _SnFdpCacheDefaultTrafficeVlanIdForDualMode_Type()
)
snFdpCacheDefaultTrafficeVlanIdForDualMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFdpCacheDefaultTrafficeVlanIdForDualMode.setStatus("current")
_SnFdpGlobal_ObjectIdentity = ObjectIdentity
snFdpGlobal = _SnFdpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 3)
)


class _SnFdpGlobalRun_Type(Integer32):
    """Custom type snFdpGlobalRun based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnFdpGlobalRun_Type.__name__ = "Integer32"
_SnFdpGlobalRun_Object = MibScalar
snFdpGlobalRun = _SnFdpGlobalRun_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 3, 1),
    _SnFdpGlobalRun_Type()
)
snFdpGlobalRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFdpGlobalRun.setStatus("current")


class _SnFdpGlobalMessageInterval_Type(Integer32):
    """Custom type snFdpGlobalMessageInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 900),
    )


_SnFdpGlobalMessageInterval_Type.__name__ = "Integer32"
_SnFdpGlobalMessageInterval_Object = MibScalar
snFdpGlobalMessageInterval = _SnFdpGlobalMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 3, 2),
    _SnFdpGlobalMessageInterval_Type()
)
snFdpGlobalMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFdpGlobalMessageInterval.setStatus("current")


class _SnFdpGlobalHoldTime_Type(Integer32):
    """Custom type snFdpGlobalHoldTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_SnFdpGlobalHoldTime_Type.__name__ = "Integer32"
_SnFdpGlobalHoldTime_Object = MibScalar
snFdpGlobalHoldTime = _SnFdpGlobalHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 3, 3),
    _SnFdpGlobalHoldTime_Type()
)
snFdpGlobalHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFdpGlobalHoldTime.setStatus("current")


class _SnFdpGlobalCdpRun_Type(Integer32):
    """Custom type snFdpGlobalCdpRun based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnFdpGlobalCdpRun_Type.__name__ = "Integer32"
_SnFdpGlobalCdpRun_Object = MibScalar
snFdpGlobalCdpRun = _SnFdpGlobalCdpRun_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 3, 4),
    _SnFdpGlobalCdpRun_Type()
)
snFdpGlobalCdpRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFdpGlobalCdpRun.setStatus("current")
_SnFdpCachedAddr_ObjectIdentity = ObjectIdentity
snFdpCachedAddr = _SnFdpCachedAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 4)
)
_SnFdpCachedAddressTable_Object = MibTable
snFdpCachedAddressTable = _SnFdpCachedAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 4, 1)
)
if mibBuilder.loadTexts:
    snFdpCachedAddressTable.setStatus("current")
_SnFdpCachedAddressEntry_Object = MibTableRow
snFdpCachedAddressEntry = _SnFdpCachedAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 4, 1, 1)
)
snFdpCachedAddressEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snFdpCachedAddrIfIndex"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snFdpCachedAddrDeviceIndex"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snFdpCachedAddrDeviceAddrEntryIndex"),
)
if mibBuilder.loadTexts:
    snFdpCachedAddressEntry.setStatus("current")
_SnFdpCachedAddrIfIndex_Type = InterfaceIndex
_SnFdpCachedAddrIfIndex_Object = MibTableColumn
snFdpCachedAddrIfIndex = _SnFdpCachedAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 4, 1, 1, 1),
    _SnFdpCachedAddrIfIndex_Type()
)
snFdpCachedAddrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snFdpCachedAddrIfIndex.setStatus("current")
_SnFdpCachedAddrDeviceIndex_Type = Integer32
_SnFdpCachedAddrDeviceIndex_Object = MibTableColumn
snFdpCachedAddrDeviceIndex = _SnFdpCachedAddrDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 4, 1, 1, 2),
    _SnFdpCachedAddrDeviceIndex_Type()
)
snFdpCachedAddrDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snFdpCachedAddrDeviceIndex.setStatus("current")
_SnFdpCachedAddrDeviceAddrEntryIndex_Type = Integer32
_SnFdpCachedAddrDeviceAddrEntryIndex_Object = MibTableColumn
snFdpCachedAddrDeviceAddrEntryIndex = _SnFdpCachedAddrDeviceAddrEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 4, 1, 1, 3),
    _SnFdpCachedAddrDeviceAddrEntryIndex_Type()
)
snFdpCachedAddrDeviceAddrEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snFdpCachedAddrDeviceAddrEntryIndex.setStatus("current")


class _SnFdpCachedAddrType_Type(Integer32):
    """Custom type snFdpCachedAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("appletalk", 3),
          ("ip", 1),
          ("ipx", 2))
    )


_SnFdpCachedAddrType_Type.__name__ = "Integer32"
_SnFdpCachedAddrType_Object = MibTableColumn
snFdpCachedAddrType = _SnFdpCachedAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 4, 1, 1, 4),
    _SnFdpCachedAddrType_Type()
)
snFdpCachedAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFdpCachedAddrType.setStatus("current")
_SnFdpCachedAddrValue_Type = OctetString
_SnFdpCachedAddrValue_Object = MibTableColumn
snFdpCachedAddrValue = _SnFdpCachedAddrValue_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 20, 1, 4, 1, 1, 5),
    _SnFdpCachedAddrValue_Type()
)
snFdpCachedAddrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFdpCachedAddrValue.setStatus("current")
_SnVsrp_ObjectIdentity = ObjectIdentity
snVsrp = _SnVsrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 21)
)
_SnArpInfo_ObjectIdentity = ObjectIdentity
snArpInfo = _SnArpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 22)
)
_SnWireless_ObjectIdentity = ObjectIdentity
snWireless = _SnWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 23)
)
_SnMac_ObjectIdentity = ObjectIdentity
snMac = _SnMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24)
)
_SnMacSecurity_ObjectIdentity = ObjectIdentity
snMacSecurity = _SnMacSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1)
)
_SnPortMacSecurity_ObjectIdentity = ObjectIdentity
snPortMacSecurity = _SnPortMacSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1)
)
_SnPortMacSecurityTable_Object = MibTable
snPortMacSecurityTable = _SnPortMacSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 1)
)
if mibBuilder.loadTexts:
    snPortMacSecurityTable.setStatus("current")
_SnPortMacSecurityEntry_Object = MibTableRow
snPortMacSecurityEntry = _SnPortMacSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 1, 1)
)
snPortMacSecurityEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snPortMacSecurityIfIndex"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snPortMacSecurityResource"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snPortMacSecurityQueryIndex"),
)
if mibBuilder.loadTexts:
    snPortMacSecurityEntry.setStatus("current")
_SnPortMacSecurityIfIndex_Type = Unsigned32
_SnPortMacSecurityIfIndex_Object = MibTableColumn
snPortMacSecurityIfIndex = _SnPortMacSecurityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 1, 1, 1),
    _SnPortMacSecurityIfIndex_Type()
)
snPortMacSecurityIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityIfIndex.setStatus("current")


class _SnPortMacSecurityResource_Type(Integer32):
    """Custom type snPortMacSecurityResource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("shared", 2))
    )


_SnPortMacSecurityResource_Type.__name__ = "Integer32"
_SnPortMacSecurityResource_Object = MibTableColumn
snPortMacSecurityResource = _SnPortMacSecurityResource_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 1, 1, 2),
    _SnPortMacSecurityResource_Type()
)
snPortMacSecurityResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityResource.setStatus("current")
_SnPortMacSecurityQueryIndex_Type = Unsigned32
_SnPortMacSecurityQueryIndex_Object = MibTableColumn
snPortMacSecurityQueryIndex = _SnPortMacSecurityQueryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 1, 1, 3),
    _SnPortMacSecurityQueryIndex_Type()
)
snPortMacSecurityQueryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityQueryIndex.setStatus("current")
_SnPortMacSecurityMAC_Type = MacAddress
_SnPortMacSecurityMAC_Object = MibTableColumn
snPortMacSecurityMAC = _SnPortMacSecurityMAC_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 1, 1, 4),
    _SnPortMacSecurityMAC_Type()
)
snPortMacSecurityMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityMAC.setStatus("current")
_SnPortMacSecurityAgeLeft_Type = Unsigned32
_SnPortMacSecurityAgeLeft_Object = MibTableColumn
snPortMacSecurityAgeLeft = _SnPortMacSecurityAgeLeft_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 1, 1, 5),
    _SnPortMacSecurityAgeLeft_Type()
)
snPortMacSecurityAgeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityAgeLeft.setStatus("current")


class _SnPortMacSecurityShutdownStatus_Type(Integer32):
    """Custom type snPortMacSecurityShutdownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_SnPortMacSecurityShutdownStatus_Type.__name__ = "Integer32"
_SnPortMacSecurityShutdownStatus_Object = MibTableColumn
snPortMacSecurityShutdownStatus = _SnPortMacSecurityShutdownStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 1, 1, 6),
    _SnPortMacSecurityShutdownStatus_Type()
)
snPortMacSecurityShutdownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityShutdownStatus.setStatus("current")
_SnPortMacSecurityShutdownTimeLeft_Type = Unsigned32
_SnPortMacSecurityShutdownTimeLeft_Object = MibTableColumn
snPortMacSecurityShutdownTimeLeft = _SnPortMacSecurityShutdownTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 1, 1, 7),
    _SnPortMacSecurityShutdownTimeLeft_Type()
)
snPortMacSecurityShutdownTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityShutdownTimeLeft.setStatus("current")


class _SnPortMacSecurityVlanId_Type(Unsigned32):
    """Custom type snPortMacSecurityVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnPortMacSecurityVlanId_Type.__name__ = "Unsigned32"
_SnPortMacSecurityVlanId_Object = MibTableColumn
snPortMacSecurityVlanId = _SnPortMacSecurityVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 1, 1, 8),
    _SnPortMacSecurityVlanId_Type()
)
snPortMacSecurityVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityVlanId.setStatus("current")
_SnPortMacSecurityModuleStatTable_Object = MibTable
snPortMacSecurityModuleStatTable = _SnPortMacSecurityModuleStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 2)
)
if mibBuilder.loadTexts:
    snPortMacSecurityModuleStatTable.setStatus("current")
_SnPortMacSecurityModuleStatEntry_Object = MibTableRow
snPortMacSecurityModuleStatEntry = _SnPortMacSecurityModuleStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 2, 1)
)
snPortMacSecurityModuleStatEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snPortMacSecurityModuleStatSlotNum"),
)
if mibBuilder.loadTexts:
    snPortMacSecurityModuleStatEntry.setStatus("current")
_SnPortMacSecurityModuleStatSlotNum_Type = Integer32
_SnPortMacSecurityModuleStatSlotNum_Object = MibTableColumn
snPortMacSecurityModuleStatSlotNum = _SnPortMacSecurityModuleStatSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 2, 1, 1),
    _SnPortMacSecurityModuleStatSlotNum_Type()
)
snPortMacSecurityModuleStatSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityModuleStatSlotNum.setStatus("current")
_SnPortMacSecurityModuleStatTotalSecurityPorts_Type = Unsigned32
_SnPortMacSecurityModuleStatTotalSecurityPorts_Object = MibTableColumn
snPortMacSecurityModuleStatTotalSecurityPorts = _SnPortMacSecurityModuleStatTotalSecurityPorts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 2, 1, 2),
    _SnPortMacSecurityModuleStatTotalSecurityPorts_Type()
)
snPortMacSecurityModuleStatTotalSecurityPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityModuleStatTotalSecurityPorts.setStatus("current")
_SnPortMacSecurityModuleStatTotalMACs_Type = Unsigned32
_SnPortMacSecurityModuleStatTotalMACs_Object = MibTableColumn
snPortMacSecurityModuleStatTotalMACs = _SnPortMacSecurityModuleStatTotalMACs_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 2, 1, 3),
    _SnPortMacSecurityModuleStatTotalMACs_Type()
)
snPortMacSecurityModuleStatTotalMACs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityModuleStatTotalMACs.setStatus("current")
_SnPortMacSecurityModuleStatViolationCounts_Type = Unsigned32
_SnPortMacSecurityModuleStatViolationCounts_Object = MibTableColumn
snPortMacSecurityModuleStatViolationCounts = _SnPortMacSecurityModuleStatViolationCounts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 2, 1, 4),
    _SnPortMacSecurityModuleStatViolationCounts_Type()
)
snPortMacSecurityModuleStatViolationCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityModuleStatViolationCounts.setStatus("current")
_SnPortMacSecurityModuleStatTotalShutdownPorts_Type = Unsigned32
_SnPortMacSecurityModuleStatTotalShutdownPorts_Object = MibTableColumn
snPortMacSecurityModuleStatTotalShutdownPorts = _SnPortMacSecurityModuleStatTotalShutdownPorts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 2, 1, 5),
    _SnPortMacSecurityModuleStatTotalShutdownPorts_Type()
)
snPortMacSecurityModuleStatTotalShutdownPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityModuleStatTotalShutdownPorts.setStatus("current")
_SnPortMacSecurityIntfContentTable_Object = MibTable
snPortMacSecurityIntfContentTable = _SnPortMacSecurityIntfContentTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 3)
)
if mibBuilder.loadTexts:
    snPortMacSecurityIntfContentTable.setStatus("current")
_SnPortMacSecurityIntfContentEntry_Object = MibTableRow
snPortMacSecurityIntfContentEntry = _SnPortMacSecurityIntfContentEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 3, 1)
)
snPortMacSecurityIntfContentEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snPortMacSecurityIntfContentIfIndex"),
)
if mibBuilder.loadTexts:
    snPortMacSecurityIntfContentEntry.setStatus("current")
_SnPortMacSecurityIntfContentIfIndex_Type = InterfaceIndex
_SnPortMacSecurityIntfContentIfIndex_Object = MibTableColumn
snPortMacSecurityIntfContentIfIndex = _SnPortMacSecurityIntfContentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 3, 1, 1),
    _SnPortMacSecurityIntfContentIfIndex_Type()
)
snPortMacSecurityIntfContentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snPortMacSecurityIntfContentIfIndex.setStatus("current")


class _SnPortMacSecurityIntfContentSecurity_Type(Integer32):
    """Custom type snPortMacSecurityIntfContentSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SnPortMacSecurityIntfContentSecurity_Type.__name__ = "Integer32"
_SnPortMacSecurityIntfContentSecurity_Object = MibTableColumn
snPortMacSecurityIntfContentSecurity = _SnPortMacSecurityIntfContentSecurity_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 3, 1, 2),
    _SnPortMacSecurityIntfContentSecurity_Type()
)
snPortMacSecurityIntfContentSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortMacSecurityIntfContentSecurity.setStatus("current")


class _SnPortMacSecurityIntfContentViolationType_Type(Integer32):
    """Custom type snPortMacSecurityIntfContentViolationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("restrict", 1),
          ("shutdown", 0))
    )


_SnPortMacSecurityIntfContentViolationType_Type.__name__ = "Integer32"
_SnPortMacSecurityIntfContentViolationType_Object = MibTableColumn
snPortMacSecurityIntfContentViolationType = _SnPortMacSecurityIntfContentViolationType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 3, 1, 3),
    _SnPortMacSecurityIntfContentViolationType_Type()
)
snPortMacSecurityIntfContentViolationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortMacSecurityIntfContentViolationType.setStatus("current")


class _SnPortMacSecurityIntfContentShutdownTime_Type(Unsigned32):
    """Custom type snPortMacSecurityIntfContentShutdownTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SnPortMacSecurityIntfContentShutdownTime_Type.__name__ = "Unsigned32"
_SnPortMacSecurityIntfContentShutdownTime_Object = MibTableColumn
snPortMacSecurityIntfContentShutdownTime = _SnPortMacSecurityIntfContentShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 3, 1, 4),
    _SnPortMacSecurityIntfContentShutdownTime_Type()
)
snPortMacSecurityIntfContentShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortMacSecurityIntfContentShutdownTime.setStatus("current")
_SnPortMacSecurityIntfContentShutdownTimeLeft_Type = Unsigned32
_SnPortMacSecurityIntfContentShutdownTimeLeft_Object = MibTableColumn
snPortMacSecurityIntfContentShutdownTimeLeft = _SnPortMacSecurityIntfContentShutdownTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 3, 1, 5),
    _SnPortMacSecurityIntfContentShutdownTimeLeft_Type()
)
snPortMacSecurityIntfContentShutdownTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityIntfContentShutdownTimeLeft.setStatus("current")


class _SnPortMacSecurityIntfContentAgeOutTime_Type(Unsigned32):
    """Custom type snPortMacSecurityIntfContentAgeOutTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SnPortMacSecurityIntfContentAgeOutTime_Type.__name__ = "Unsigned32"
_SnPortMacSecurityIntfContentAgeOutTime_Object = MibTableColumn
snPortMacSecurityIntfContentAgeOutTime = _SnPortMacSecurityIntfContentAgeOutTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 3, 1, 6),
    _SnPortMacSecurityIntfContentAgeOutTime_Type()
)
snPortMacSecurityIntfContentAgeOutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortMacSecurityIntfContentAgeOutTime.setStatus("current")
_SnPortMacSecurityIntfContentMaxLockedMacAllowed_Type = Unsigned32
_SnPortMacSecurityIntfContentMaxLockedMacAllowed_Object = MibTableColumn
snPortMacSecurityIntfContentMaxLockedMacAllowed = _SnPortMacSecurityIntfContentMaxLockedMacAllowed_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 3, 1, 7),
    _SnPortMacSecurityIntfContentMaxLockedMacAllowed_Type()
)
snPortMacSecurityIntfContentMaxLockedMacAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortMacSecurityIntfContentMaxLockedMacAllowed.setStatus("current")
_SnPortMacSecurityIntfContentTotalMACs_Type = Unsigned32
_SnPortMacSecurityIntfContentTotalMACs_Object = MibTableColumn
snPortMacSecurityIntfContentTotalMACs = _SnPortMacSecurityIntfContentTotalMACs_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 3, 1, 8),
    _SnPortMacSecurityIntfContentTotalMACs_Type()
)
snPortMacSecurityIntfContentTotalMACs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityIntfContentTotalMACs.setStatus("current")
_SnPortMacSecurityIntfContentViolationCounts_Type = Unsigned32
_SnPortMacSecurityIntfContentViolationCounts_Object = MibTableColumn
snPortMacSecurityIntfContentViolationCounts = _SnPortMacSecurityIntfContentViolationCounts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 3, 1, 9),
    _SnPortMacSecurityIntfContentViolationCounts_Type()
)
snPortMacSecurityIntfContentViolationCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityIntfContentViolationCounts.setStatus("current")
_SnPortMacSecurityIntfMacTable_Object = MibTable
snPortMacSecurityIntfMacTable = _SnPortMacSecurityIntfMacTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 4)
)
if mibBuilder.loadTexts:
    snPortMacSecurityIntfMacTable.setStatus("current")
_SnPortMacSecurityIntfMacEntry_Object = MibTableRow
snPortMacSecurityIntfMacEntry = _SnPortMacSecurityIntfMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 4, 1)
)
snPortMacSecurityIntfMacEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snPortMacSecurityIntfMacIfIndex"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snPortMacSecurityIntfMacAddress"),
)
if mibBuilder.loadTexts:
    snPortMacSecurityIntfMacEntry.setStatus("current")
_SnPortMacSecurityIntfMacIfIndex_Type = Integer32
_SnPortMacSecurityIntfMacIfIndex_Object = MibTableColumn
snPortMacSecurityIntfMacIfIndex = _SnPortMacSecurityIntfMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 4, 1, 1),
    _SnPortMacSecurityIntfMacIfIndex_Type()
)
snPortMacSecurityIntfMacIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityIntfMacIfIndex.setStatus("current")
_SnPortMacSecurityIntfMacAddress_Type = MacAddress
_SnPortMacSecurityIntfMacAddress_Object = MibTableColumn
snPortMacSecurityIntfMacAddress = _SnPortMacSecurityIntfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 4, 1, 2),
    _SnPortMacSecurityIntfMacAddress_Type()
)
snPortMacSecurityIntfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityIntfMacAddress.setStatus("current")


class _SnPortMacSecurityIntfMacVlanId_Type(Unsigned32):
    """Custom type snPortMacSecurityIntfMacVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnPortMacSecurityIntfMacVlanId_Type.__name__ = "Unsigned32"
_SnPortMacSecurityIntfMacVlanId_Object = MibTableColumn
snPortMacSecurityIntfMacVlanId = _SnPortMacSecurityIntfMacVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 4, 1, 3),
    _SnPortMacSecurityIntfMacVlanId_Type()
)
snPortMacSecurityIntfMacVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortMacSecurityIntfMacVlanId.setStatus("current")


class _SnPortMacSecurityIntfMacRowStatus_Type(Integer32):
    """Custom type snPortMacSecurityIntfMacRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnPortMacSecurityIntfMacRowStatus_Type.__name__ = "Integer32"
_SnPortMacSecurityIntfMacRowStatus_Object = MibTableColumn
snPortMacSecurityIntfMacRowStatus = _SnPortMacSecurityIntfMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 4, 1, 4),
    _SnPortMacSecurityIntfMacRowStatus_Type()
)
snPortMacSecurityIntfMacRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortMacSecurityIntfMacRowStatus.setStatus("current")
_SnPortMacSecurityAutosaveMacTable_Object = MibTable
snPortMacSecurityAutosaveMacTable = _SnPortMacSecurityAutosaveMacTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 5)
)
if mibBuilder.loadTexts:
    snPortMacSecurityAutosaveMacTable.setStatus("current")
_SnPortMacSecurityAutosaveMacEntry_Object = MibTableRow
snPortMacSecurityAutosaveMacEntry = _SnPortMacSecurityAutosaveMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 5, 1)
)
snPortMacSecurityAutosaveMacEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snPortMacSecurityAutosaveMacIfIndex"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snPortMacSecurityAutosaveMacResource"),
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snPortMacSecurityAutosaveMacQueryIndex"),
)
if mibBuilder.loadTexts:
    snPortMacSecurityAutosaveMacEntry.setStatus("current")
_SnPortMacSecurityAutosaveMacIfIndex_Type = Integer32
_SnPortMacSecurityAutosaveMacIfIndex_Object = MibTableColumn
snPortMacSecurityAutosaveMacIfIndex = _SnPortMacSecurityAutosaveMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 5, 1, 1),
    _SnPortMacSecurityAutosaveMacIfIndex_Type()
)
snPortMacSecurityAutosaveMacIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityAutosaveMacIfIndex.setStatus("current")


class _SnPortMacSecurityAutosaveMacResource_Type(Integer32):
    """Custom type snPortMacSecurityAutosaveMacResource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("shared", 2))
    )


_SnPortMacSecurityAutosaveMacResource_Type.__name__ = "Integer32"
_SnPortMacSecurityAutosaveMacResource_Object = MibTableColumn
snPortMacSecurityAutosaveMacResource = _SnPortMacSecurityAutosaveMacResource_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 5, 1, 2),
    _SnPortMacSecurityAutosaveMacResource_Type()
)
snPortMacSecurityAutosaveMacResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityAutosaveMacResource.setStatus("current")
_SnPortMacSecurityAutosaveMacQueryIndex_Type = Unsigned32
_SnPortMacSecurityAutosaveMacQueryIndex_Object = MibTableColumn
snPortMacSecurityAutosaveMacQueryIndex = _SnPortMacSecurityAutosaveMacQueryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 5, 1, 3),
    _SnPortMacSecurityAutosaveMacQueryIndex_Type()
)
snPortMacSecurityAutosaveMacQueryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityAutosaveMacQueryIndex.setStatus("current")
_SnPortMacSecurityAutosaveMacAddress_Type = MacAddress
_SnPortMacSecurityAutosaveMacAddress_Object = MibTableColumn
snPortMacSecurityAutosaveMacAddress = _SnPortMacSecurityAutosaveMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 1, 5, 1, 4),
    _SnPortMacSecurityAutosaveMacAddress_Type()
)
snPortMacSecurityAutosaveMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPortMacSecurityAutosaveMacAddress.setStatus("current")
_SnPortMacGlobalSecurity_ObjectIdentity = ObjectIdentity
snPortMacGlobalSecurity = _SnPortMacGlobalSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 2)
)


class _SnPortMacGlobalSecurityFeature_Type(Integer32):
    """Custom type snPortMacGlobalSecurityFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SnPortMacGlobalSecurityFeature_Type.__name__ = "Integer32"
_SnPortMacGlobalSecurityFeature_Object = MibScalar
snPortMacGlobalSecurityFeature = _SnPortMacGlobalSecurityFeature_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 2, 1),
    _SnPortMacGlobalSecurityFeature_Type()
)
snPortMacGlobalSecurityFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortMacGlobalSecurityFeature.setStatus("current")


class _SnPortMacGlobalSecurityAgeOutTime_Type(Unsigned32):
    """Custom type snPortMacGlobalSecurityAgeOutTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SnPortMacGlobalSecurityAgeOutTime_Type.__name__ = "Unsigned32"
_SnPortMacGlobalSecurityAgeOutTime_Object = MibScalar
snPortMacGlobalSecurityAgeOutTime = _SnPortMacGlobalSecurityAgeOutTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 2, 2),
    _SnPortMacGlobalSecurityAgeOutTime_Type()
)
snPortMacGlobalSecurityAgeOutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortMacGlobalSecurityAgeOutTime.setStatus("current")
_SnPortMacGlobalSecurityAutosave_Type = Unsigned32
_SnPortMacGlobalSecurityAutosave_Object = MibScalar
snPortMacGlobalSecurityAutosave = _SnPortMacGlobalSecurityAutosave_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 24, 1, 2, 3),
    _SnPortMacGlobalSecurityAutosave_Type()
)
snPortMacGlobalSecurityAutosave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortMacGlobalSecurityAutosave.setStatus("current")
_SnPortMonitor_ObjectIdentity = ObjectIdentity
snPortMonitor = _SnPortMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 25)
)
_SnPortMonitorTable_Object = MibTable
snPortMonitorTable = _SnPortMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 25, 1)
)
if mibBuilder.loadTexts:
    snPortMonitorTable.setStatus("current")
_SnPortMonitorEntry_Object = MibTableRow
snPortMonitorEntry = _SnPortMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 25, 1, 1)
)
snPortMonitorEntry.setIndexNames(
    (0, "FOUNDRY-SN-SWITCH-GROUP-MIB", "snPortMonitorIfIndex"),
)
if mibBuilder.loadTexts:
    snPortMonitorEntry.setStatus("current")
_SnPortMonitorIfIndex_Type = InterfaceIndex
_SnPortMonitorIfIndex_Object = MibTableColumn
snPortMonitorIfIndex = _SnPortMonitorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 25, 1, 1, 1),
    _SnPortMonitorIfIndex_Type()
)
snPortMonitorIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snPortMonitorIfIndex.setStatus("current")
_SnPortMonitorMirrorList_Type = DisplayString
_SnPortMonitorMirrorList_Object = MibTableColumn
snPortMonitorMirrorList = _SnPortMonitorMirrorList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 25, 1, 1, 2),
    _SnPortMonitorMirrorList_Type()
)
snPortMonitorMirrorList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortMonitorMirrorList.setStatus("current")
_SnSSH_ObjectIdentity = ObjectIdentity
snSSH = _SnSSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 26)
)
_SnSSL_ObjectIdentity = ObjectIdentity
snSSL = _SnSSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 27)
)
_SnMacAuth_ObjectIdentity = ObjectIdentity
snMacAuth = _SnMacAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28)
)
_SnMetroRing_ObjectIdentity = ObjectIdentity
snMetroRing = _SnMetroRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29)
)
_SnStacking_ObjectIdentity = ObjectIdentity
snStacking = _SnStacking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31)
)
_FdryMacVlanMIB_ObjectIdentity = ObjectIdentity
fdryMacVlanMIB = _FdryMacVlanMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32)
)
_FdryLinkAggregationGroupMIB_ObjectIdentity = ObjectIdentity
fdryLinkAggregationGroupMIB = _FdryLinkAggregationGroupMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33)
)
_FdryDns2MIB_ObjectIdentity = ObjectIdentity
fdryDns2MIB = _FdryDns2MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 34)
)
_FdryDaiMIB_ObjectIdentity = ObjectIdentity
fdryDaiMIB = _FdryDaiMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35)
)
_FdryDhcpSnoopMIB_ObjectIdentity = ObjectIdentity
fdryDhcpSnoopMIB = _FdryDhcpSnoopMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36)
)
_FdryIpSrcGuardMIB_ObjectIdentity = ObjectIdentity
fdryIpSrcGuardMIB = _FdryIpSrcGuardMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37)
)
_BrcdRouteMap_ObjectIdentity = ObjectIdentity
brcdRouteMap = _BrcdRouteMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 39)
)
_BrcdSPXMIB_ObjectIdentity = ObjectIdentity
brcdSPXMIB = _BrcdSPXMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    **{"PhysAddress": PhysAddress,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "PortMask": PortMask,
       "InterfaceId": InterfaceId,
       "InterfaceId2": InterfaceId2,
       "VlanTagMode": VlanTagMode,
       "FdryVlanIdOrNoneTC": FdryVlanIdOrNoneTC,
       "BrcdVlanIdTC": BrcdVlanIdTC,
       "BrcdVlanIdOrNoneTC": BrcdVlanIdOrNoneTC,
       "PortQosTC": PortQosTC,
       "PortPriorityTC": PortPriorityTC,
       "snSwitch": snSwitch,
       "snSwInfo": snSwInfo,
       "snSwGroupOperMode": snSwGroupOperMode,
       "snSwGroupIpL3SwMode": snSwGroupIpL3SwMode,
       "snSwGroupIpMcastMode": snSwGroupIpMcastMode,
       "snSwGroupDefaultCfgMode": snSwGroupDefaultCfgMode,
       "snSwGroupSwitchAgeTime": snSwGroupSwitchAgeTime,
       "snVLanGroupVlanCurEntry": snVLanGroupVlanCurEntry,
       "snVLanGroupSetAllVLan": snVLanGroupSetAllVLan,
       "snSwPortSetAll": snSwPortSetAll,
       "snFdbTableCurEntry": snFdbTableCurEntry,
       "snFdbTableStationFlush": snFdbTableStationFlush,
       "snPortStpSetAll": snPortStpSetAll,
       "snSwProbePortNum": snSwProbePortNum,
       "snSw8021qTagMode": snSw8021qTagMode,
       "snSwGlobalStpMode": snSwGlobalStpMode,
       "snSwIpMcastQuerierMode": snSwIpMcastQuerierMode,
       "snSwViolatorPortNumber": snSwViolatorPortNumber,
       "snSwViolatorMacAddress": snSwViolatorMacAddress,
       "snVLanGroupVlanMaxEntry": snVLanGroupVlanMaxEntry,
       "snSwEosBufferSize": snSwEosBufferSize,
       "snVLanByPortEntrySize": snVLanByPortEntrySize,
       "snSwPortEntrySize": snSwPortEntrySize,
       "snFdbStationEntrySize": snFdbStationEntrySize,
       "snPortStpEntrySize": snPortStpEntrySize,
       "snSwEnableBridgeNewRootTrap": snSwEnableBridgeNewRootTrap,
       "snSwEnableBridgeTopoChangeTrap": snSwEnableBridgeTopoChangeTrap,
       "snSwEnableLockedAddrViolationTrap": snSwEnableLockedAddrViolationTrap,
       "snSwIpxL3SwMode": snSwIpxL3SwMode,
       "snVLanByIpSubnetMaxSubnets": snVLanByIpSubnetMaxSubnets,
       "snVLanByIpxNetMaxNetworks": snVLanByIpxNetMaxNetworks,
       "snSwProtocolVLanMode": snSwProtocolVLanMode,
       "snMacStationVLanId": snMacStationVLanId,
       "snSwClearCounters": snSwClearCounters,
       "snSw8021qTagType": snSw8021qTagType,
       "snSwBroadcastLimit": snSwBroadcastLimit,
       "snSwMaxMacFilterPerSystem": snSwMaxMacFilterPerSystem,
       "snSwMaxMacFilterPerPort": snSwMaxMacFilterPerPort,
       "snSwDefaultVLanId": snSwDefaultVLanId,
       "snSwGlobalAutoNegotiate": snSwGlobalAutoNegotiate,
       "snSwQosMechanism": snSwQosMechanism,
       "snSwSingleStpMode": snSwSingleStpMode,
       "snSwFastStpMode": snSwFastStpMode,
       "snSwViolatorIfIndex": snSwViolatorIfIndex,
       "snSwSingleStpVLanId": snSwSingleStpVLanId,
       "snSwBroadcastLimit2": snSwBroadcastLimit2,
       "snVLanInfo": snVLanInfo,
       "snVLanByPortTable": snVLanByPortTable,
       "snVLanByPortEntry": snVLanByPortEntry,
       "snVLanByPortVLanIndex": snVLanByPortVLanIndex,
       "snVLanByPortVLanId": snVLanByPortVLanId,
       "snVLanByPortPortMask": snVLanByPortPortMask,
       "snVLanByPortQos": snVLanByPortQos,
       "snVLanByPortStpMode": snVLanByPortStpMode,
       "snVLanByPortStpPriority": snVLanByPortStpPriority,
       "snVLanByPortStpGroupMaxAge": snVLanByPortStpGroupMaxAge,
       "snVLanByPortStpGroupHelloTime": snVLanByPortStpGroupHelloTime,
       "snVLanByPortStpGroupForwardDelay": snVLanByPortStpGroupForwardDelay,
       "snVLanByPortRowStatus": snVLanByPortRowStatus,
       "snVLanByPortOperState": snVLanByPortOperState,
       "snVLanByPortBaseNumPorts": snVLanByPortBaseNumPorts,
       "snVLanByPortBaseType": snVLanByPortBaseType,
       "snVLanByPortStpProtocolSpecification": snVLanByPortStpProtocolSpecification,
       "snVLanByPortStpMaxAge": snVLanByPortStpMaxAge,
       "snVLanByPortStpHelloTime": snVLanByPortStpHelloTime,
       "snVLanByPortStpHoldTime": snVLanByPortStpHoldTime,
       "snVLanByPortStpForwardDelay": snVLanByPortStpForwardDelay,
       "snVLanByPortStpTimeSinceTopologyChange": snVLanByPortStpTimeSinceTopologyChange,
       "snVLanByPortStpTopChanges": snVLanByPortStpTopChanges,
       "snVLanByPortStpRootCost": snVLanByPortStpRootCost,
       "snVLanByPortStpRootPort": snVLanByPortStpRootPort,
       "snVLanByPortStpDesignatedRoot": snVLanByPortStpDesignatedRoot,
       "snVLanByPortBaseBridgeAddress": snVLanByPortBaseBridgeAddress,
       "snVLanByPortVLanName": snVLanByPortVLanName,
       "snVLanByPortRouterIntf": snVLanByPortRouterIntf,
       "snVLanByPortChassisPortMask": snVLanByPortChassisPortMask,
       "snVLanByPortPortList": snVLanByPortPortList,
       "snVLanByProtocolTable": snVLanByProtocolTable,
       "snVLanByProtocolEntry": snVLanByProtocolEntry,
       "snVLanByProtocolVLanId": snVLanByProtocolVLanId,
       "snVLanByProtocolIndex": snVLanByProtocolIndex,
       "snVLanByProtocolDynamic": snVLanByProtocolDynamic,
       "snVLanByProtocolStaticMask": snVLanByProtocolStaticMask,
       "snVLanByProtocolExcludeMask": snVLanByProtocolExcludeMask,
       "snVLanByProtocolRouterIntf": snVLanByProtocolRouterIntf,
       "snVLanByProtocolRowStatus": snVLanByProtocolRowStatus,
       "snVLanByProtocolDynamicMask": snVLanByProtocolDynamicMask,
       "snVLanByProtocolChassisStaticMask": snVLanByProtocolChassisStaticMask,
       "snVLanByProtocolChassisExcludeMask": snVLanByProtocolChassisExcludeMask,
       "snVLanByProtocolChassisDynamicMask": snVLanByProtocolChassisDynamicMask,
       "snVLanByProtocolVLanName": snVLanByProtocolVLanName,
       "snVLanByProtocolStaticPortList": snVLanByProtocolStaticPortList,
       "snVLanByProtocolExcludePortList": snVLanByProtocolExcludePortList,
       "snVLanByProtocolDynamicPortList": snVLanByProtocolDynamicPortList,
       "snVLanByIpSubnetTable": snVLanByIpSubnetTable,
       "snVLanByIpSubnetEntry": snVLanByIpSubnetEntry,
       "snVLanByIpSubnetVLanId": snVLanByIpSubnetVLanId,
       "snVLanByIpSubnetIpAddress": snVLanByIpSubnetIpAddress,
       "snVLanByIpSubnetSubnetMask": snVLanByIpSubnetSubnetMask,
       "snVLanByIpSubnetDynamic": snVLanByIpSubnetDynamic,
       "snVLanByIpSubnetStaticMask": snVLanByIpSubnetStaticMask,
       "snVLanByIpSubnetExcludeMask": snVLanByIpSubnetExcludeMask,
       "snVLanByIpSubnetRouterIntf": snVLanByIpSubnetRouterIntf,
       "snVLanByIpSubnetRowStatus": snVLanByIpSubnetRowStatus,
       "snVLanByIpSubnetDynamicMask": snVLanByIpSubnetDynamicMask,
       "snVLanByIpSubnetChassisStaticMask": snVLanByIpSubnetChassisStaticMask,
       "snVLanByIpSubnetChassisExcludeMask": snVLanByIpSubnetChassisExcludeMask,
       "snVLanByIpSubnetChassisDynamicMask": snVLanByIpSubnetChassisDynamicMask,
       "snVLanByIpSubnetVLanName": snVLanByIpSubnetVLanName,
       "snVLanByIpSubnetStaticPortList": snVLanByIpSubnetStaticPortList,
       "snVLanByIpSubnetExcludePortList": snVLanByIpSubnetExcludePortList,
       "snVLanByIpSubnetDynamicPortList": snVLanByIpSubnetDynamicPortList,
       "snVLanByIpxNetTable": snVLanByIpxNetTable,
       "snVLanByIpxNetEntry": snVLanByIpxNetEntry,
       "snVLanByIpxNetVLanId": snVLanByIpxNetVLanId,
       "snVLanByIpxNetNetworkNum": snVLanByIpxNetNetworkNum,
       "snVLanByIpxNetFrameType": snVLanByIpxNetFrameType,
       "snVLanByIpxNetDynamic": snVLanByIpxNetDynamic,
       "snVLanByIpxNetStaticMask": snVLanByIpxNetStaticMask,
       "snVLanByIpxNetExcludeMask": snVLanByIpxNetExcludeMask,
       "snVLanByIpxNetRouterIntf": snVLanByIpxNetRouterIntf,
       "snVLanByIpxNetRowStatus": snVLanByIpxNetRowStatus,
       "snVLanByIpxNetDynamicMask": snVLanByIpxNetDynamicMask,
       "snVLanByIpxNetChassisStaticMask": snVLanByIpxNetChassisStaticMask,
       "snVLanByIpxNetChassisExcludeMask": snVLanByIpxNetChassisExcludeMask,
       "snVLanByIpxNetChassisDynamicMask": snVLanByIpxNetChassisDynamicMask,
       "snVLanByIpxNetVLanName": snVLanByIpxNetVLanName,
       "snVLanByIpxNetStaticPortList": snVLanByIpxNetStaticPortList,
       "snVLanByIpxNetExcludePortList": snVLanByIpxNetExcludePortList,
       "snVLanByIpxNetDynamicPortList": snVLanByIpxNetDynamicPortList,
       "snVLanByATCableTable": snVLanByATCableTable,
       "snVLanByATCableEntry": snVLanByATCableEntry,
       "snVLanByATCableVLanId": snVLanByATCableVLanId,
       "snVLanByATCableIndex": snVLanByATCableIndex,
       "snVLanByATCableRouterIntf": snVLanByATCableRouterIntf,
       "snVLanByATCableRowStatus": snVLanByATCableRowStatus,
       "snVLanByATCableChassisStaticMask": snVLanByATCableChassisStaticMask,
       "snVLanByATCableVLanName": snVLanByATCableVLanName,
       "snVLanByATCableStaticPortList": snVLanByATCableStaticPortList,
       "snVLanByPortMemberTable": snVLanByPortMemberTable,
       "snVLanByPortMemberEntry": snVLanByPortMemberEntry,
       "snVLanByPortMemberVLanId": snVLanByPortMemberVLanId,
       "snVLanByPortMemberPortId": snVLanByPortMemberPortId,
       "snVLanByPortMemberRowStatus": snVLanByPortMemberRowStatus,
       "snVLanByPortMemberTagMode": snVLanByPortMemberTagMode,
       "snVLanByPortCfgTable": snVLanByPortCfgTable,
       "snVLanByPortCfgEntry": snVLanByPortCfgEntry,
       "snVLanByPortCfgVLanId": snVLanByPortCfgVLanId,
       "snVLanByPortCfgQos": snVLanByPortCfgQos,
       "snVLanByPortCfgStpMode": snVLanByPortCfgStpMode,
       "snVLanByPortCfgStpPriority": snVLanByPortCfgStpPriority,
       "snVLanByPortCfgStpGroupMaxAge": snVLanByPortCfgStpGroupMaxAge,
       "snVLanByPortCfgStpGroupHelloTime": snVLanByPortCfgStpGroupHelloTime,
       "snVLanByPortCfgStpGroupForwardDelay": snVLanByPortCfgStpGroupForwardDelay,
       "snVLanByPortCfgBaseNumPorts": snVLanByPortCfgBaseNumPorts,
       "snVLanByPortCfgBaseType": snVLanByPortCfgBaseType,
       "snVLanByPortCfgStpProtocolSpecification": snVLanByPortCfgStpProtocolSpecification,
       "snVLanByPortCfgStpMaxAge": snVLanByPortCfgStpMaxAge,
       "snVLanByPortCfgStpHelloTime": snVLanByPortCfgStpHelloTime,
       "snVLanByPortCfgStpHoldTime": snVLanByPortCfgStpHoldTime,
       "snVLanByPortCfgStpForwardDelay": snVLanByPortCfgStpForwardDelay,
       "snVLanByPortCfgStpTimeSinceTopologyChange": snVLanByPortCfgStpTimeSinceTopologyChange,
       "snVLanByPortCfgStpTopChanges": snVLanByPortCfgStpTopChanges,
       "snVLanByPortCfgStpRootCost": snVLanByPortCfgStpRootCost,
       "snVLanByPortCfgStpRootPort": snVLanByPortCfgStpRootPort,
       "snVLanByPortCfgStpDesignatedRoot": snVLanByPortCfgStpDesignatedRoot,
       "snVLanByPortCfgBaseBridgeAddress": snVLanByPortCfgBaseBridgeAddress,
       "snVLanByPortCfgVLanName": snVLanByPortCfgVLanName,
       "snVLanByPortCfgRouterIntf": snVLanByPortCfgRouterIntf,
       "snVLanByPortCfgRowStatus": snVLanByPortCfgRowStatus,
       "snVLanByPortCfgStpVersion": snVLanByPortCfgStpVersion,
       "snVLanByPortCfgInOctets": snVLanByPortCfgInOctets,
       "snVLanByPortCfgTransparentHwFlooding": snVLanByPortCfgTransparentHwFlooding,
       "brcdVlanExtStatsTable": brcdVlanExtStatsTable,
       "brcdVlanExtStatsEntry": brcdVlanExtStatsEntry,
       "brcdVlanExtStatsVlanId": brcdVlanExtStatsVlanId,
       "brcdVlanExtStatsIfIndex": brcdVlanExtStatsIfIndex,
       "brcdVlanExtStatsPriorityId": brcdVlanExtStatsPriorityId,
       "brcdVlanExtStatsInSwitchedPkts": brcdVlanExtStatsInSwitchedPkts,
       "brcdVlanExtStatsInRoutedPkts": brcdVlanExtStatsInRoutedPkts,
       "brcdVlanExtStatsInPkts": brcdVlanExtStatsInPkts,
       "brcdVlanExtStatsOutSwitchedPkts": brcdVlanExtStatsOutSwitchedPkts,
       "brcdVlanExtStatsOutRoutedPkts": brcdVlanExtStatsOutRoutedPkts,
       "brcdVlanExtStatsOutPkts": brcdVlanExtStatsOutPkts,
       "brcdVlanExtStatsInSwitchedOctets": brcdVlanExtStatsInSwitchedOctets,
       "brcdVlanExtStatsInRoutedOctets": brcdVlanExtStatsInRoutedOctets,
       "brcdVlanExtStatsInOctets": brcdVlanExtStatsInOctets,
       "brcdVlanExtStatsOutSwitchedOctets": brcdVlanExtStatsOutSwitchedOctets,
       "brcdVlanExtStatsOutRoutedOctets": brcdVlanExtStatsOutRoutedOctets,
       "brcdVlanExtStatsOutOctets": brcdVlanExtStatsOutOctets,
       "snSwPortInfo": snSwPortInfo,
       "snSwPortInfoTable": snSwPortInfoTable,
       "snSwPortInfoEntry": snSwPortInfoEntry,
       "snSwPortInfoPortNum": snSwPortInfoPortNum,
       "snSwPortInfoMonitorMode": snSwPortInfoMonitorMode,
       "snSwPortInfoTagMode": snSwPortInfoTagMode,
       "snSwPortInfoChnMode": snSwPortInfoChnMode,
       "snSwPortInfoSpeed": snSwPortInfoSpeed,
       "snSwPortInfoMediaType": snSwPortInfoMediaType,
       "snSwPortInfoConnectorType": snSwPortInfoConnectorType,
       "snSwPortInfoAdminStatus": snSwPortInfoAdminStatus,
       "snSwPortInfoLinkStatus": snSwPortInfoLinkStatus,
       "snSwPortInfoPortQos": snSwPortInfoPortQos,
       "snSwPortInfoPhysAddress": snSwPortInfoPhysAddress,
       "snSwPortStatsInFrames": snSwPortStatsInFrames,
       "snSwPortStatsOutFrames": snSwPortStatsOutFrames,
       "snSwPortStatsAlignErrors": snSwPortStatsAlignErrors,
       "snSwPortStatsFCSErrors": snSwPortStatsFCSErrors,
       "snSwPortStatsMultiColliFrames": snSwPortStatsMultiColliFrames,
       "snSwPortStatsFrameTooLongs": snSwPortStatsFrameTooLongs,
       "snSwPortStatsTxColliFrames": snSwPortStatsTxColliFrames,
       "snSwPortStatsRxColliFrames": snSwPortStatsRxColliFrames,
       "snSwPortStatsFrameTooShorts": snSwPortStatsFrameTooShorts,
       "snSwPortLockAddressCount": snSwPortLockAddressCount,
       "snSwPortStpPortEnable": snSwPortStpPortEnable,
       "snSwPortDhcpGateListId": snSwPortDhcpGateListId,
       "snSwPortName": snSwPortName,
       "snSwPortStatsInBcastFrames": snSwPortStatsInBcastFrames,
       "snSwPortStatsOutBcastFrames": snSwPortStatsOutBcastFrames,
       "snSwPortStatsInMcastFrames": snSwPortStatsInMcastFrames,
       "snSwPortStatsOutMcastFrames": snSwPortStatsOutMcastFrames,
       "snSwPortStatsInDiscard": snSwPortStatsInDiscard,
       "snSwPortStatsOutDiscard": snSwPortStatsOutDiscard,
       "snSwPortStatsMacStations": snSwPortStatsMacStations,
       "snSwPortCacheGroupId": snSwPortCacheGroupId,
       "snSwPortTransGroupId": snSwPortTransGroupId,
       "snSwPortInfoAutoNegotiate": snSwPortInfoAutoNegotiate,
       "snSwPortInfoFlowControl": snSwPortInfoFlowControl,
       "snSwPortInfoGigType": snSwPortInfoGigType,
       "snSwPortStatsLinkChange": snSwPortStatsLinkChange,
       "snSwPortIfIndex": snSwPortIfIndex,
       "snSwPortDescr": snSwPortDescr,
       "snSwPortInOctets": snSwPortInOctets,
       "snSwPortOutOctets": snSwPortOutOctets,
       "snSwPortStatsInBitsPerSec": snSwPortStatsInBitsPerSec,
       "snSwPortStatsOutBitsPerSec": snSwPortStatsOutBitsPerSec,
       "snSwPortStatsInPktsPerSec": snSwPortStatsInPktsPerSec,
       "snSwPortStatsOutPktsPerSec": snSwPortStatsOutPktsPerSec,
       "snSwPortStatsInUtilization": snSwPortStatsInUtilization,
       "snSwPortStatsOutUtilization": snSwPortStatsOutUtilization,
       "snSwPortFastSpanPortEnable": snSwPortFastSpanPortEnable,
       "snSwPortFastSpanUplinkEnable": snSwPortFastSpanUplinkEnable,
       "snSwPortVlanId": snSwPortVlanId,
       "snSwPortRouteOnly": snSwPortRouteOnly,
       "snSwPortPresent": snSwPortPresent,
       "snSwPortGBICStatus": snSwPortGBICStatus,
       "snSwPortStatsInKiloBitsPerSec": snSwPortStatsInKiloBitsPerSec,
       "snSwPortStatsOutKiloBitsPerSec": snSwPortStatsOutKiloBitsPerSec,
       "snSwPortLoadInterval": snSwPortLoadInterval,
       "snSwPortTagType": snSwPortTagType,
       "snSwPortInLinePowerControl": snSwPortInLinePowerControl,
       "snSwPortInLinePowerWattage": snSwPortInLinePowerWattage,
       "snSwPortInLinePowerClass": snSwPortInLinePowerClass,
       "snSwPortInLinePowerPriority": snSwPortInLinePowerPriority,
       "snSwPortInfoMirrorMode": snSwPortInfoMirrorMode,
       "snSwPortStatsInJumboFrames": snSwPortStatsInJumboFrames,
       "snSwPortStatsOutJumboFrames": snSwPortStatsOutJumboFrames,
       "snSwPortInLinePowerConsumed": snSwPortInLinePowerConsumed,
       "snSwPortInLinePowerPDType": snSwPortInLinePowerPDType,
       "snInterfaceId": snInterfaceId,
       "snEthernetInterface": snEthernetInterface,
       "snPosInterface": snPosInterface,
       "snAtmInterface": snAtmInterface,
       "snVirtualInterface": snVirtualInterface,
       "snLoopbackInterface": snLoopbackInterface,
       "snGreTunnelInterface": snGreTunnelInterface,
       "snSubInterface": snSubInterface,
       "snMplsTunnelInterface": snMplsTunnelInterface,
       "snPvcInterface": snPvcInterface,
       "snMgmtEthernetInterface": snMgmtEthernetInterface,
       "snTrunkInterface": snTrunkInterface,
       "snVirtualMgmtInterface": snVirtualMgmtInterface,
       "sn6to4TunnelInterface": sn6to4TunnelInterface,
       "snInterfaceLookupTable": snInterfaceLookupTable,
       "snInterfaceLookupEntry": snInterfaceLookupEntry,
       "snInterfaceLookupInterfaceId": snInterfaceLookupInterfaceId,
       "snInterfaceLookupIfIndex": snInterfaceLookupIfIndex,
       "snIfIndexLookupTable": snIfIndexLookupTable,
       "snIfIndexLookupEntry": snIfIndexLookupEntry,
       "snIfIndexLookupIfIndex": snIfIndexLookupIfIndex,
       "snIfIndexLookupInterfaceId": snIfIndexLookupInterfaceId,
       "snSwIfInfoTable": snSwIfInfoTable,
       "snSwIfInfoEntry": snSwIfInfoEntry,
       "snSwIfInfoPortNum": snSwIfInfoPortNum,
       "snSwIfInfoMonitorMode": snSwIfInfoMonitorMode,
       "snSwIfInfoMirrorPorts": snSwIfInfoMirrorPorts,
       "snSwIfInfoTagMode": snSwIfInfoTagMode,
       "snSwIfInfoTagType": snSwIfInfoTagType,
       "snSwIfInfoChnMode": snSwIfInfoChnMode,
       "snSwIfInfoSpeed": snSwIfInfoSpeed,
       "snSwIfInfoMediaType": snSwIfInfoMediaType,
       "snSwIfInfoConnectorType": snSwIfInfoConnectorType,
       "snSwIfInfoAdminStatus": snSwIfInfoAdminStatus,
       "snSwIfInfoLinkStatus": snSwIfInfoLinkStatus,
       "snSwIfInfoPortQos": snSwIfInfoPortQos,
       "snSwIfInfoPhysAddress": snSwIfInfoPhysAddress,
       "snSwIfLockAddressCount": snSwIfLockAddressCount,
       "snSwIfStpPortEnable": snSwIfStpPortEnable,
       "snSwIfDhcpGateListId": snSwIfDhcpGateListId,
       "snSwIfName": snSwIfName,
       "snSwIfDescr": snSwIfDescr,
       "snSwIfInfoAutoNegotiate": snSwIfInfoAutoNegotiate,
       "snSwIfInfoFlowControl": snSwIfInfoFlowControl,
       "snSwIfInfoGigType": snSwIfInfoGigType,
       "snSwIfFastSpanPortEnable": snSwIfFastSpanPortEnable,
       "snSwIfFastSpanUplinkEnable": snSwIfFastSpanUplinkEnable,
       "snSwIfVlanId": snSwIfVlanId,
       "snSwIfRouteOnly": snSwIfRouteOnly,
       "snSwIfPresent": snSwIfPresent,
       "snSwIfGBICStatus": snSwIfGBICStatus,
       "snSwIfLoadInterval": snSwIfLoadInterval,
       "snSwIfStatsInFrames": snSwIfStatsInFrames,
       "snSwIfStatsOutFrames": snSwIfStatsOutFrames,
       "snSwIfStatsAlignErrors": snSwIfStatsAlignErrors,
       "snSwIfStatsFCSErrors": snSwIfStatsFCSErrors,
       "snSwIfStatsMultiColliFrames": snSwIfStatsMultiColliFrames,
       "snSwIfStatsTxColliFrames": snSwIfStatsTxColliFrames,
       "snSwIfStatsRxColliFrames": snSwIfStatsRxColliFrames,
       "snSwIfStatsFrameTooLongs": snSwIfStatsFrameTooLongs,
       "snSwIfStatsFrameTooShorts": snSwIfStatsFrameTooShorts,
       "snSwIfStatsInBcastFrames": snSwIfStatsInBcastFrames,
       "snSwIfStatsOutBcastFrames": snSwIfStatsOutBcastFrames,
       "snSwIfStatsInMcastFrames": snSwIfStatsInMcastFrames,
       "snSwIfStatsOutMcastFrames": snSwIfStatsOutMcastFrames,
       "snSwIfStatsInDiscard": snSwIfStatsInDiscard,
       "snSwIfStatsOutDiscard": snSwIfStatsOutDiscard,
       "snSwIfStatsMacStations": snSwIfStatsMacStations,
       "snSwIfStatsLinkChange": snSwIfStatsLinkChange,
       "snSwIfInOctets": snSwIfInOctets,
       "snSwIfOutOctets": snSwIfOutOctets,
       "snSwIfStatsInBitsPerSec": snSwIfStatsInBitsPerSec,
       "snSwIfStatsOutBitsPerSec": snSwIfStatsOutBitsPerSec,
       "snSwIfStatsInPktsPerSec": snSwIfStatsInPktsPerSec,
       "snSwIfStatsOutPktsPerSec": snSwIfStatsOutPktsPerSec,
       "snSwIfStatsInUtilization": snSwIfStatsInUtilization,
       "snSwIfStatsOutUtilization": snSwIfStatsOutUtilization,
       "snSwIfStatsInKiloBitsPerSec": snSwIfStatsInKiloBitsPerSec,
       "snSwIfStatsOutKiloBitsPerSec": snSwIfStatsOutKiloBitsPerSec,
       "snSwIfStatsInJumboFrames": snSwIfStatsInJumboFrames,
       "snSwIfStatsOutJumboFrames": snSwIfStatsOutJumboFrames,
       "snSwIfInfoMirrorMode": snSwIfInfoMirrorMode,
       "snSwIfMacLearningDisable": snSwIfMacLearningDisable,
       "snSwIfInfoL2FowardEnable": snSwIfInfoL2FowardEnable,
       "snSwIfInfoAllowAllVlan": snSwIfInfoAllowAllVlan,
       "snSwIfInfoNativeMacAddress": snSwIfInfoNativeMacAddress,
       "snIfOpticalMonitoringInfoTable": snIfOpticalMonitoringInfoTable,
       "snIfOpticalMonitoringInfoEntry": snIfOpticalMonitoringInfoEntry,
       "snIfOpticalMonitoringTemperature": snIfOpticalMonitoringTemperature,
       "snIfOpticalMonitoringTxPower": snIfOpticalMonitoringTxPower,
       "snIfOpticalMonitoringRxPower": snIfOpticalMonitoringRxPower,
       "snIfOpticalMonitoringTxBiasCurrent": snIfOpticalMonitoringTxBiasCurrent,
       "snInterfaceLookup2Table": snInterfaceLookup2Table,
       "snInterfaceLookup2Entry": snInterfaceLookup2Entry,
       "snInterfaceLookup2InterfaceId": snInterfaceLookup2InterfaceId,
       "snInterfaceLookup2IfIndex": snInterfaceLookup2IfIndex,
       "snIfIndexLookup2Table": snIfIndexLookup2Table,
       "snIfIndexLookup2Entry": snIfIndexLookup2Entry,
       "snIfIndexLookup2IfIndex": snIfIndexLookup2IfIndex,
       "snIfIndexLookup2InterfaceId": snIfIndexLookup2InterfaceId,
       "snIfMediaInfoTable": snIfMediaInfoTable,
       "snIfMediaInfoEntry": snIfMediaInfoEntry,
       "snIfMediaType": snIfMediaType,
       "snIfMediaVendorName": snIfMediaVendorName,
       "snIfMediaVersion": snIfMediaVersion,
       "snIfMediaPartNumber": snIfMediaPartNumber,
       "snIfMediaSerialNumber": snIfMediaSerialNumber,
       "snIfOpticalLaneMonitoringTable": snIfOpticalLaneMonitoringTable,
       "snIfOpticalLaneMonitoringEntry": snIfOpticalLaneMonitoringEntry,
       "snIfOpticalLaneMonitoringLane": snIfOpticalLaneMonitoringLane,
       "snIfOpticalLaneMonitoringTemperature": snIfOpticalLaneMonitoringTemperature,
       "snIfOpticalLaneMonitoringTxPower": snIfOpticalLaneMonitoringTxPower,
       "snIfOpticalLaneMonitoringRxPower": snIfOpticalLaneMonitoringRxPower,
       "snIfOpticalLaneMonitoringTxBiasCurrent": snIfOpticalLaneMonitoringTxBiasCurrent,
       "brcdIfEgressCounterInfoTable": brcdIfEgressCounterInfoTable,
       "brcdIfEgressCounterInfoEntry": brcdIfEgressCounterInfoEntry,
       "brcdIfEgressCounterIfIndex": brcdIfEgressCounterIfIndex,
       "brcdIfEgressCounterQueueId": brcdIfEgressCounterQueueId,
       "brcdIfEgressCounterType": brcdIfEgressCounterType,
       "brcdIfEgressCounterPkts": brcdIfEgressCounterPkts,
       "brcdIfEgressCounterDropPkts": brcdIfEgressCounterDropPkts,
       "snFdbInfo": snFdbInfo,
       "snFdbTable": snFdbTable,
       "snFdbEntry": snFdbEntry,
       "snFdbStationIndex": snFdbStationIndex,
       "snFdbStationAddr": snFdbStationAddr,
       "snFdbStationPort": snFdbStationPort,
       "snFdbVLanId": snFdbVLanId,
       "snFdbStationQos": snFdbStationQos,
       "snFdbStationType": snFdbStationType,
       "snFdbRowStatus": snFdbRowStatus,
       "snFdbStationIf": snFdbStationIf,
       "snPortStpInfo": snPortStpInfo,
       "snPortStpTable": snPortStpTable,
       "snPortStpEntry": snPortStpEntry,
       "snPortStpVLanId": snPortStpVLanId,
       "snPortStpPortNum": snPortStpPortNum,
       "snPortStpPortPriority": snPortStpPortPriority,
       "snPortStpPathCost": snPortStpPathCost,
       "snPortStpOperState": snPortStpOperState,
       "snPortStpPortEnable": snPortStpPortEnable,
       "snPortStpPortForwardTransitions": snPortStpPortForwardTransitions,
       "snPortStpPortState": snPortStpPortState,
       "snPortStpPortDesignatedCost": snPortStpPortDesignatedCost,
       "snPortStpPortDesignatedRoot": snPortStpPortDesignatedRoot,
       "snPortStpPortDesignatedBridge": snPortStpPortDesignatedBridge,
       "snPortStpPortDesignatedPort": snPortStpPortDesignatedPort,
       "snPortStpPortAdminRstp": snPortStpPortAdminRstp,
       "snPortStpPortProtocolMigration": snPortStpPortProtocolMigration,
       "snPortStpPortAdminEdgePort": snPortStpPortAdminEdgePort,
       "snPortStpPortAdminPointToPoint": snPortStpPortAdminPointToPoint,
       "snIfStpTable": snIfStpTable,
       "snIfStpEntry": snIfStpEntry,
       "snIfStpVLanId": snIfStpVLanId,
       "snIfStpPortNum": snIfStpPortNum,
       "snIfStpPortPriority": snIfStpPortPriority,
       "snIfStpCfgPathCost": snIfStpCfgPathCost,
       "snIfStpOperState": snIfStpOperState,
       "snIfStpPortState": snIfStpPortState,
       "snIfStpPortDesignatedCost": snIfStpPortDesignatedCost,
       "snIfStpPortDesignatedRoot": snIfStpPortDesignatedRoot,
       "snIfStpPortDesignatedBridge": snIfStpPortDesignatedBridge,
       "snIfStpPortDesignatedPort": snIfStpPortDesignatedPort,
       "snIfStpPortAdminRstp": snIfStpPortAdminRstp,
       "snIfStpPortProtocolMigration": snIfStpPortProtocolMigration,
       "snIfStpPortAdminEdgePort": snIfStpPortAdminEdgePort,
       "snIfStpPortAdminPointToPoint": snIfStpPortAdminPointToPoint,
       "snIfStpOperPathCost": snIfStpOperPathCost,
       "snIfStpPortRole": snIfStpPortRole,
       "snIfStpBPDUTransmitted": snIfStpBPDUTransmitted,
       "snIfStpBPDUReceived": snIfStpBPDUReceived,
       "snIfRstpConfigBPDUReceived": snIfRstpConfigBPDUReceived,
       "snIfRstpTCNBPDUReceived": snIfRstpTCNBPDUReceived,
       "snIfRstpConfigBPDUTransmitted": snIfRstpConfigBPDUTransmitted,
       "snIfRstpTCNBPDUTransmitted": snIfRstpTCNBPDUTransmitted,
       "snTrunkInfo": snTrunkInfo,
       "snTrunkTable": snTrunkTable,
       "snTrunkEntry": snTrunkEntry,
       "snTrunkIndex": snTrunkIndex,
       "snTrunkPortMask": snTrunkPortMask,
       "snTrunkType": snTrunkType,
       "snMSTrunkTable": snMSTrunkTable,
       "snMSTrunkEntry": snMSTrunkEntry,
       "snMSTrunkPortIndex": snMSTrunkPortIndex,
       "snMSTrunkPortList": snMSTrunkPortList,
       "snMSTrunkType": snMSTrunkType,
       "snMSTrunkRowStatus": snMSTrunkRowStatus,
       "snMSTrunkIfTable": snMSTrunkIfTable,
       "snMSTrunkIfEntry": snMSTrunkIfEntry,
       "snMSTrunkIfIndex": snMSTrunkIfIndex,
       "snMSTrunkIfList": snMSTrunkIfList,
       "snMSTrunkIfType": snMSTrunkIfType,
       "snMSTrunkIfRowStatus": snMSTrunkIfRowStatus,
       "snSwSummary": snSwSummary,
       "snSwSummaryMode": snSwSummaryMode,
       "snDhcpGatewayListInfo": snDhcpGatewayListInfo,
       "snDhcpGatewayListTable": snDhcpGatewayListTable,
       "snDhcpGatewayListEntry": snDhcpGatewayListEntry,
       "snDhcpGatewayListId": snDhcpGatewayListId,
       "snDhcpGatewayListAddrList": snDhcpGatewayListAddrList,
       "snDhcpGatewayListRowStatus": snDhcpGatewayListRowStatus,
       "snDnsInfo": snDnsInfo,
       "snDnsDomainName": snDnsDomainName,
       "snDnsGatewayIpAddrList": snDnsGatewayIpAddrList,
       "snMacFilter": snMacFilter,
       "snMacFilterTable": snMacFilterTable,
       "snMacFilterEntry": snMacFilterEntry,
       "snMacFilterIndex": snMacFilterIndex,
       "snMacFilterAction": snMacFilterAction,
       "snMacFilterSourceMac": snMacFilterSourceMac,
       "snMacFilterSourceMask": snMacFilterSourceMask,
       "snMacFilterDestMac": snMacFilterDestMac,
       "snMacFilterDestMask": snMacFilterDestMask,
       "snMacFilterOperator": snMacFilterOperator,
       "snMacFilterFrameType": snMacFilterFrameType,
       "snMacFilterFrameTypeNum": snMacFilterFrameTypeNum,
       "snMacFilterRowStatus": snMacFilterRowStatus,
       "snMacFilterPortAccessTable": snMacFilterPortAccessTable,
       "snMacFilterPortAccessEntry": snMacFilterPortAccessEntry,
       "snMacFilterPortAccessPortIndex": snMacFilterPortAccessPortIndex,
       "snMacFilterPortAccessFilters": snMacFilterPortAccessFilters,
       "snMacFilterPortAccessRowStatus": snMacFilterPortAccessRowStatus,
       "snMacFilterIfAccessTable": snMacFilterIfAccessTable,
       "snMacFilterIfAccessEntry": snMacFilterIfAccessEntry,
       "snMacFilterIfAccessPortIndex": snMacFilterIfAccessPortIndex,
       "snMacFilterIfAccessFilters": snMacFilterIfAccessFilters,
       "snMacFilterIfAccessRowStatus": snMacFilterIfAccessRowStatus,
       "snNTP": snNTP,
       "snNTPGeneral": snNTPGeneral,
       "snNTPPollInterval": snNTPPollInterval,
       "snNTPTimeZone": snNTPTimeZone,
       "snNTPSummerTimeEnable": snNTPSummerTimeEnable,
       "snNTPSystemClock": snNTPSystemClock,
       "snNTPSync": snNTPSync,
       "snNTPServerTable": snNTPServerTable,
       "snNTPServerEntry": snNTPServerEntry,
       "snNTPServerIp": snNTPServerIp,
       "snNTPServerVersion": snNTPServerVersion,
       "snNTPServerRowStatus": snNTPServerRowStatus,
       "snRadius": snRadius,
       "snRadiusGeneral": snRadiusGeneral,
       "snRadiusSNMPAccess": snRadiusSNMPAccess,
       "snRadiusEnableTelnetAuth": snRadiusEnableTelnetAuth,
       "snRadiusRetransmit": snRadiusRetransmit,
       "snRadiusTimeOut": snRadiusTimeOut,
       "snRadiusDeadTime": snRadiusDeadTime,
       "snRadiusKey": snRadiusKey,
       "snRadiusLoginMethod": snRadiusLoginMethod,
       "snRadiusEnableMethod": snRadiusEnableMethod,
       "snRadiusWebServerMethod": snRadiusWebServerMethod,
       "snRadiusSNMPServerMethod": snRadiusSNMPServerMethod,
       "snRadiusServerTable": snRadiusServerTable,
       "snRadiusServerEntry": snRadiusServerEntry,
       "snRadiusServerIp": snRadiusServerIp,
       "snRadiusServerAuthPort": snRadiusServerAuthPort,
       "snRadiusServerAcctPort": snRadiusServerAcctPort,
       "snRadiusServerRowStatus": snRadiusServerRowStatus,
       "snRadiusServerRowKey": snRadiusServerRowKey,
       "snRadiusServerUsage": snRadiusServerUsage,
       "snTacacs": snTacacs,
       "snTacacsGeneral": snTacacsGeneral,
       "snTacacsRetransmit": snTacacsRetransmit,
       "snTacacsTimeOut": snTacacsTimeOut,
       "snTacacsDeadTime": snTacacsDeadTime,
       "snTacacsKey": snTacacsKey,
       "snTacacsSNMPAccess": snTacacsSNMPAccess,
       "snTacacsServerTable": snTacacsServerTable,
       "snTacacsServerEntry": snTacacsServerEntry,
       "snTacacsServerIp": snTacacsServerIp,
       "snTacacsServerAuthPort": snTacacsServerAuthPort,
       "snTacacsServerRowStatus": snTacacsServerRowStatus,
       "snTacacsServerRowKey": snTacacsServerRowKey,
       "snTacacsServerUsage": snTacacsServerUsage,
       "snQos": snQos,
       "snQosProfileTable": snQosProfileTable,
       "snQosProfileEntry": snQosProfileEntry,
       "snQosProfileIndex": snQosProfileIndex,
       "snQosProfileName": snQosProfileName,
       "snQosProfileRequestedBandwidth": snQosProfileRequestedBandwidth,
       "snQosProfileCalculatedBandwidth": snQosProfileCalculatedBandwidth,
       "snQosBindTable": snQosBindTable,
       "snQosBindEntry": snQosBindEntry,
       "snQosBindIndex": snQosBindIndex,
       "snQosBindPriority": snQosBindPriority,
       "snQosBindProfileIndex": snQosBindProfileIndex,
       "snDosAttack": snDosAttack,
       "snDosAttackGlobal": snDosAttackGlobal,
       "snDosAttackICMPDropCount": snDosAttackICMPDropCount,
       "snDosAttackICMPBlockCount": snDosAttackICMPBlockCount,
       "snDosAttackSYNDropCount": snDosAttackSYNDropCount,
       "snDosAttackSYNBlockCount": snDosAttackSYNBlockCount,
       "snDosAttackPortTable": snDosAttackPortTable,
       "snDosAttackPortEntry": snDosAttackPortEntry,
       "snDosAttackPort": snDosAttackPort,
       "snDosAttackPortICMPDropCount": snDosAttackPortICMPDropCount,
       "snDosAttackPortICMPBlockCount": snDosAttackPortICMPBlockCount,
       "snDosAttackPortSYNDropCount": snDosAttackPortSYNDropCount,
       "snDosAttackPortSYNBlockCount": snDosAttackPortSYNBlockCount,
       "snAAA": snAAA,
       "snAuthentication": snAuthentication,
       "snAuthorization": snAuthorization,
       "snAuthorizationCommandMethods": snAuthorizationCommandMethods,
       "snAuthorizationCommandLevel": snAuthorizationCommandLevel,
       "snAuthorizationExec": snAuthorizationExec,
       "snAccounting": snAccounting,
       "snAccountingCommandMethods": snAccountingCommandMethods,
       "snAccountingCommandLevel": snAccountingCommandLevel,
       "snAccountingExec": snAccountingExec,
       "snAccountingSystem": snAccountingSystem,
       "snCAR": snCAR,
       "snVLanCAR": snVLanCAR,
       "snNetFlow": snNetFlow,
       "snNetFlowGlb": snNetFlowGlb,
       "snNetFlowGblEnable": snNetFlowGblEnable,
       "snNetFlowGblVersion": snNetFlowGblVersion,
       "snNetFlowGblProtocolDisable": snNetFlowGblProtocolDisable,
       "snNetFlowGblActiveTimeout": snNetFlowGblActiveTimeout,
       "snNetFlowGblInactiveTimeout": snNetFlowGblInactiveTimeout,
       "snNetFlowCollectorTable": snNetFlowCollectorTable,
       "snNetFlowCollectorEntry": snNetFlowCollectorEntry,
       "snNetFlowCollectorIndex": snNetFlowCollectorIndex,
       "snNetFlowCollectorIp": snNetFlowCollectorIp,
       "snNetFlowCollectorUdpPort": snNetFlowCollectorUdpPort,
       "snNetFlowCollectorSourceInterface": snNetFlowCollectorSourceInterface,
       "snNetFlowCollectorRowStatus": snNetFlowCollectorRowStatus,
       "snNetFlowAggregationTable": snNetFlowAggregationTable,
       "snNetFlowAggregationEntry": snNetFlowAggregationEntry,
       "snNetFlowAggregationIndex": snNetFlowAggregationIndex,
       "snNetFlowAggregationIp": snNetFlowAggregationIp,
       "snNetFlowAggregationUdpPort": snNetFlowAggregationUdpPort,
       "snNetFlowAggregationSourceInterface": snNetFlowAggregationSourceInterface,
       "snNetFlowAggregationNumberOfCacheEntries": snNetFlowAggregationNumberOfCacheEntries,
       "snNetFlowAggregationActiveTimeout": snNetFlowAggregationActiveTimeout,
       "snNetFlowAggregationInactiveTimeout": snNetFlowAggregationInactiveTimeout,
       "snNetFlowAggregationEnable": snNetFlowAggregationEnable,
       "snNetFlowAggregationRowStatus": snNetFlowAggregationRowStatus,
       "snNetFlowIfTable": snNetFlowIfTable,
       "snNetFlowIfEntry": snNetFlowIfEntry,
       "snNetFlowIfIndex": snNetFlowIfIndex,
       "snNetFlowIfFlowSwitching": snNetFlowIfFlowSwitching,
       "snSFlow": snSFlow,
       "snSFlowGlb": snSFlowGlb,
       "snSflowCollectorTable": snSflowCollectorTable,
       "snSflowCollectorEntry": snSflowCollectorEntry,
       "snSflowCollectorIndex": snSflowCollectorIndex,
       "snSflowCollectorIP": snSflowCollectorIP,
       "snSflowCollectorUDPPort": snSflowCollectorUDPPort,
       "snSflowCollectorRowStatus": snSflowCollectorRowStatus,
       "snFDP": snFDP,
       "snFdpMIBObjects": snFdpMIBObjects,
       "snFdpInterface": snFdpInterface,
       "snFdpInterfaceTable": snFdpInterfaceTable,
       "snFdpInterfaceEntry": snFdpInterfaceEntry,
       "snFdpInterfaceIfIndex": snFdpInterfaceIfIndex,
       "snFdpInterfaceFdpEnable": snFdpInterfaceFdpEnable,
       "snFdpInterfaceCdpEnable": snFdpInterfaceCdpEnable,
       "snFdpCache": snFdpCache,
       "snFdpCacheTable": snFdpCacheTable,
       "snFdpCacheEntry": snFdpCacheEntry,
       "snFdpCacheIfIndex": snFdpCacheIfIndex,
       "snFdpCacheDeviceIndex": snFdpCacheDeviceIndex,
       "snFdpCacheDeviceId": snFdpCacheDeviceId,
       "snFdpCacheAddressType": snFdpCacheAddressType,
       "snFdpCacheAddress": snFdpCacheAddress,
       "snFdpCacheVersion": snFdpCacheVersion,
       "snFdpCacheDevicePort": snFdpCacheDevicePort,
       "snFdpCachePlatform": snFdpCachePlatform,
       "snFdpCacheCapabilities": snFdpCacheCapabilities,
       "snFdpCacheVendorId": snFdpCacheVendorId,
       "snFdpCacheIsAggregateVlan": snFdpCacheIsAggregateVlan,
       "snFdpCacheTagType": snFdpCacheTagType,
       "snFdpCachePortVlanMask": snFdpCachePortVlanMask,
       "snFdpCachePortTagMode": snFdpCachePortTagMode,
       "snFdpCacheDefaultTrafficeVlanIdForDualMode": snFdpCacheDefaultTrafficeVlanIdForDualMode,
       "snFdpGlobal": snFdpGlobal,
       "snFdpGlobalRun": snFdpGlobalRun,
       "snFdpGlobalMessageInterval": snFdpGlobalMessageInterval,
       "snFdpGlobalHoldTime": snFdpGlobalHoldTime,
       "snFdpGlobalCdpRun": snFdpGlobalCdpRun,
       "snFdpCachedAddr": snFdpCachedAddr,
       "snFdpCachedAddressTable": snFdpCachedAddressTable,
       "snFdpCachedAddressEntry": snFdpCachedAddressEntry,
       "snFdpCachedAddrIfIndex": snFdpCachedAddrIfIndex,
       "snFdpCachedAddrDeviceIndex": snFdpCachedAddrDeviceIndex,
       "snFdpCachedAddrDeviceAddrEntryIndex": snFdpCachedAddrDeviceAddrEntryIndex,
       "snFdpCachedAddrType": snFdpCachedAddrType,
       "snFdpCachedAddrValue": snFdpCachedAddrValue,
       "snVsrp": snVsrp,
       "snArpInfo": snArpInfo,
       "snWireless": snWireless,
       "snMac": snMac,
       "snMacSecurity": snMacSecurity,
       "snPortMacSecurity": snPortMacSecurity,
       "snPortMacSecurityTable": snPortMacSecurityTable,
       "snPortMacSecurityEntry": snPortMacSecurityEntry,
       "snPortMacSecurityIfIndex": snPortMacSecurityIfIndex,
       "snPortMacSecurityResource": snPortMacSecurityResource,
       "snPortMacSecurityQueryIndex": snPortMacSecurityQueryIndex,
       "snPortMacSecurityMAC": snPortMacSecurityMAC,
       "snPortMacSecurityAgeLeft": snPortMacSecurityAgeLeft,
       "snPortMacSecurityShutdownStatus": snPortMacSecurityShutdownStatus,
       "snPortMacSecurityShutdownTimeLeft": snPortMacSecurityShutdownTimeLeft,
       "snPortMacSecurityVlanId": snPortMacSecurityVlanId,
       "snPortMacSecurityModuleStatTable": snPortMacSecurityModuleStatTable,
       "snPortMacSecurityModuleStatEntry": snPortMacSecurityModuleStatEntry,
       "snPortMacSecurityModuleStatSlotNum": snPortMacSecurityModuleStatSlotNum,
       "snPortMacSecurityModuleStatTotalSecurityPorts": snPortMacSecurityModuleStatTotalSecurityPorts,
       "snPortMacSecurityModuleStatTotalMACs": snPortMacSecurityModuleStatTotalMACs,
       "snPortMacSecurityModuleStatViolationCounts": snPortMacSecurityModuleStatViolationCounts,
       "snPortMacSecurityModuleStatTotalShutdownPorts": snPortMacSecurityModuleStatTotalShutdownPorts,
       "snPortMacSecurityIntfContentTable": snPortMacSecurityIntfContentTable,
       "snPortMacSecurityIntfContentEntry": snPortMacSecurityIntfContentEntry,
       "snPortMacSecurityIntfContentIfIndex": snPortMacSecurityIntfContentIfIndex,
       "snPortMacSecurityIntfContentSecurity": snPortMacSecurityIntfContentSecurity,
       "snPortMacSecurityIntfContentViolationType": snPortMacSecurityIntfContentViolationType,
       "snPortMacSecurityIntfContentShutdownTime": snPortMacSecurityIntfContentShutdownTime,
       "snPortMacSecurityIntfContentShutdownTimeLeft": snPortMacSecurityIntfContentShutdownTimeLeft,
       "snPortMacSecurityIntfContentAgeOutTime": snPortMacSecurityIntfContentAgeOutTime,
       "snPortMacSecurityIntfContentMaxLockedMacAllowed": snPortMacSecurityIntfContentMaxLockedMacAllowed,
       "snPortMacSecurityIntfContentTotalMACs": snPortMacSecurityIntfContentTotalMACs,
       "snPortMacSecurityIntfContentViolationCounts": snPortMacSecurityIntfContentViolationCounts,
       "snPortMacSecurityIntfMacTable": snPortMacSecurityIntfMacTable,
       "snPortMacSecurityIntfMacEntry": snPortMacSecurityIntfMacEntry,
       "snPortMacSecurityIntfMacIfIndex": snPortMacSecurityIntfMacIfIndex,
       "snPortMacSecurityIntfMacAddress": snPortMacSecurityIntfMacAddress,
       "snPortMacSecurityIntfMacVlanId": snPortMacSecurityIntfMacVlanId,
       "snPortMacSecurityIntfMacRowStatus": snPortMacSecurityIntfMacRowStatus,
       "snPortMacSecurityAutosaveMacTable": snPortMacSecurityAutosaveMacTable,
       "snPortMacSecurityAutosaveMacEntry": snPortMacSecurityAutosaveMacEntry,
       "snPortMacSecurityAutosaveMacIfIndex": snPortMacSecurityAutosaveMacIfIndex,
       "snPortMacSecurityAutosaveMacResource": snPortMacSecurityAutosaveMacResource,
       "snPortMacSecurityAutosaveMacQueryIndex": snPortMacSecurityAutosaveMacQueryIndex,
       "snPortMacSecurityAutosaveMacAddress": snPortMacSecurityAutosaveMacAddress,
       "snPortMacGlobalSecurity": snPortMacGlobalSecurity,
       "snPortMacGlobalSecurityFeature": snPortMacGlobalSecurityFeature,
       "snPortMacGlobalSecurityAgeOutTime": snPortMacGlobalSecurityAgeOutTime,
       "snPortMacGlobalSecurityAutosave": snPortMacGlobalSecurityAutosave,
       "snPortMonitor": snPortMonitor,
       "snPortMonitorTable": snPortMonitorTable,
       "snPortMonitorEntry": snPortMonitorEntry,
       "snPortMonitorIfIndex": snPortMonitorIfIndex,
       "snPortMonitorMirrorList": snPortMonitorMirrorList,
       "snSSH": snSSH,
       "snSSL": snSSL,
       "snMacAuth": snMacAuth,
       "snMetroRing": snMetroRing,
       "snStacking": snStacking,
       "fdryMacVlanMIB": fdryMacVlanMIB,
       "fdryLinkAggregationGroupMIB": fdryLinkAggregationGroupMIB,
       "fdryDns2MIB": fdryDns2MIB,
       "fdryDaiMIB": fdryDaiMIB,
       "fdryDhcpSnoopMIB": fdryDhcpSnoopMIB,
       "fdryIpSrcGuardMIB": fdryIpSrcGuardMIB,
       "brcdRouteMap": brcdRouteMap,
       "brcdSPXMIB": brcdSPXMIB}
)

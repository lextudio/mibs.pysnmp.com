# SNMP MIB module (BLADETYPE2-PHYSICAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLADETYPE2-PHYSICAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:03 2024
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

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

(hpSwitchBladeType2_Mgmt,) = mibBuilder.importSymbols(
    "HP-SWITCH-PL-MIB",
    "hpSwitchBladeType2-Mgmt")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

layer2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Layer2Configs_ObjectIdentity = ObjectIdentity
layer2Configs = _Layer2Configs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1)
)
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1)
)
_VlanMaxEnt_Type = Integer32
_VlanMaxEnt_Object = MibScalar
vlanMaxEnt = _VlanMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1, 1),
    _VlanMaxEnt_Type()
)
vlanMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMaxEnt.setStatus("current")
_VlanCurCfgTable_Object = MibTable
vlanCurCfgTable = _VlanCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vlanCurCfgTable.setStatus("current")
_VlanCurCfgTableEntry_Object = MibTableRow
vlanCurCfgTableEntry = _VlanCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1, 2, 1)
)
vlanCurCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "vlanCurCfgVlanId"),
)
if mibBuilder.loadTexts:
    vlanCurCfgTableEntry.setStatus("current")
_VlanCurCfgVlanId_Type = Integer32
_VlanCurCfgVlanId_Object = MibTableColumn
vlanCurCfgVlanId = _VlanCurCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1, 2, 1, 1),
    _VlanCurCfgVlanId_Type()
)
vlanCurCfgVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgVlanId.setStatus("current")


class _VlanCurCfgVlanName_Type(DisplayString):
    """Custom type vlanCurCfgVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VlanCurCfgVlanName_Type.__name__ = "DisplayString"
_VlanCurCfgVlanName_Object = MibTableColumn
vlanCurCfgVlanName = _VlanCurCfgVlanName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1, 2, 1, 2),
    _VlanCurCfgVlanName_Type()
)
vlanCurCfgVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgVlanName.setStatus("current")
_VlanCurCfgPorts_Type = OctetString
_VlanCurCfgPorts_Object = MibTableColumn
vlanCurCfgPorts = _VlanCurCfgPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1, 2, 1, 3),
    _VlanCurCfgPorts_Type()
)
vlanCurCfgPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgPorts.setStatus("current")


class _VlanCurCfgState_Type(Integer32):
    """Custom type vlanCurCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_VlanCurCfgState_Type.__name__ = "Integer32"
_VlanCurCfgState_Object = MibTableColumn
vlanCurCfgState = _VlanCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1, 2, 1, 4),
    _VlanCurCfgState_Type()
)
vlanCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgState.setStatus("current")
_VlanCurCfgStg_Type = Integer32
_VlanCurCfgStg_Object = MibTableColumn
vlanCurCfgStg = _VlanCurCfgStg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1, 2, 1, 6),
    _VlanCurCfgStg_Type()
)
vlanCurCfgStg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgStg.setStatus("current")
_VlanNewCfgTable_Object = MibTable
vlanNewCfgTable = _VlanNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    vlanNewCfgTable.setStatus("current")
_VlanNewCfgTableEntry_Object = MibTableRow
vlanNewCfgTableEntry = _VlanNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1, 3, 1)
)
vlanNewCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "vlanNewCfgVlanId"),
)
if mibBuilder.loadTexts:
    vlanNewCfgTableEntry.setStatus("current")
_VlanNewCfgVlanId_Type = Integer32
_VlanNewCfgVlanId_Object = MibTableColumn
vlanNewCfgVlanId = _VlanNewCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1, 3, 1, 1),
    _VlanNewCfgVlanId_Type()
)
vlanNewCfgVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNewCfgVlanId.setStatus("current")


class _VlanNewCfgVlanName_Type(DisplayString):
    """Custom type vlanNewCfgVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VlanNewCfgVlanName_Type.__name__ = "DisplayString"
_VlanNewCfgVlanName_Object = MibTableColumn
vlanNewCfgVlanName = _VlanNewCfgVlanName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1, 3, 1, 2),
    _VlanNewCfgVlanName_Type()
)
vlanNewCfgVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgVlanName.setStatus("current")
_VlanNewCfgPorts_Type = OctetString
_VlanNewCfgPorts_Object = MibTableColumn
vlanNewCfgPorts = _VlanNewCfgPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1, 3, 1, 3),
    _VlanNewCfgPorts_Type()
)
vlanNewCfgPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNewCfgPorts.setStatus("current")


class _VlanNewCfgState_Type(Integer32):
    """Custom type vlanNewCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_VlanNewCfgState_Type.__name__ = "Integer32"
_VlanNewCfgState_Object = MibTableColumn
vlanNewCfgState = _VlanNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1, 3, 1, 4),
    _VlanNewCfgState_Type()
)
vlanNewCfgState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgState.setStatus("current")
_VlanNewCfgAddPort_Type = Integer32
_VlanNewCfgAddPort_Object = MibTableColumn
vlanNewCfgAddPort = _VlanNewCfgAddPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1, 3, 1, 5),
    _VlanNewCfgAddPort_Type()
)
vlanNewCfgAddPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgAddPort.setStatus("current")
_VlanNewCfgRemovePort_Type = Integer32
_VlanNewCfgRemovePort_Object = MibTableColumn
vlanNewCfgRemovePort = _VlanNewCfgRemovePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1, 3, 1, 6),
    _VlanNewCfgRemovePort_Type()
)
vlanNewCfgRemovePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgRemovePort.setStatus("current")


class _VlanNewCfgDelete_Type(Integer32):
    """Custom type vlanNewCfgDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_VlanNewCfgDelete_Type.__name__ = "Integer32"
_VlanNewCfgDelete_Object = MibTableColumn
vlanNewCfgDelete = _VlanNewCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1, 3, 1, 7),
    _VlanNewCfgDelete_Type()
)
vlanNewCfgDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgDelete.setStatus("current")
_VlanNewCfgStg_Type = Integer32
_VlanNewCfgStg_Object = MibTableColumn
vlanNewCfgStg = _VlanNewCfgStg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 1, 3, 1, 9),
    _VlanNewCfgStg_Type()
)
vlanNewCfgStg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgStg.setStatus("current")
_Trunkgroup_ObjectIdentity = ObjectIdentity
trunkgroup = _Trunkgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 2)
)
_TrunkGroupTableMaxSize_Type = Integer32
_TrunkGroupTableMaxSize_Object = MibScalar
trunkGroupTableMaxSize = _TrunkGroupTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 2, 1),
    _TrunkGroupTableMaxSize_Type()
)
trunkGroupTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupTableMaxSize.setStatus("current")
_TrunkGroupCurCfgTable_Object = MibTable
trunkGroupCurCfgTable = _TrunkGroupCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    trunkGroupCurCfgTable.setStatus("current")
_TrunkGroupCurCfgTableEntry_Object = MibTableRow
trunkGroupCurCfgTableEntry = _TrunkGroupCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 2, 2, 1)
)
trunkGroupCurCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "trunkGroupCurCfgIndex"),
)
if mibBuilder.loadTexts:
    trunkGroupCurCfgTableEntry.setStatus("current")
_TrunkGroupCurCfgIndex_Type = Integer32
_TrunkGroupCurCfgIndex_Object = MibTableColumn
trunkGroupCurCfgIndex = _TrunkGroupCurCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 2, 2, 1, 1),
    _TrunkGroupCurCfgIndex_Type()
)
trunkGroupCurCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupCurCfgIndex.setStatus("current")
_TrunkGroupCurCfgPorts_Type = OctetString
_TrunkGroupCurCfgPorts_Object = MibTableColumn
trunkGroupCurCfgPorts = _TrunkGroupCurCfgPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 2, 2, 1, 2),
    _TrunkGroupCurCfgPorts_Type()
)
trunkGroupCurCfgPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupCurCfgPorts.setStatus("current")


class _TrunkGroupCurCfgState_Type(Integer32):
    """Custom type trunkGroupCurCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TrunkGroupCurCfgState_Type.__name__ = "Integer32"
_TrunkGroupCurCfgState_Object = MibTableColumn
trunkGroupCurCfgState = _TrunkGroupCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 2, 2, 1, 3),
    _TrunkGroupCurCfgState_Type()
)
trunkGroupCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupCurCfgState.setStatus("current")
_TrunkGroupNewCfgTable_Object = MibTable
trunkGroupNewCfgTable = _TrunkGroupNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    trunkGroupNewCfgTable.setStatus("current")
_TrunkGroupNewCfgTableEntry_Object = MibTableRow
trunkGroupNewCfgTableEntry = _TrunkGroupNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 2, 3, 1)
)
trunkGroupNewCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "trunkGroupNewCfgIndex"),
)
if mibBuilder.loadTexts:
    trunkGroupNewCfgTableEntry.setStatus("current")
_TrunkGroupNewCfgIndex_Type = Integer32
_TrunkGroupNewCfgIndex_Object = MibTableColumn
trunkGroupNewCfgIndex = _TrunkGroupNewCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 2, 3, 1, 1),
    _TrunkGroupNewCfgIndex_Type()
)
trunkGroupNewCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupNewCfgIndex.setStatus("current")
_TrunkGroupNewCfgPorts_Type = OctetString
_TrunkGroupNewCfgPorts_Object = MibTableColumn
trunkGroupNewCfgPorts = _TrunkGroupNewCfgPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 2, 3, 1, 2),
    _TrunkGroupNewCfgPorts_Type()
)
trunkGroupNewCfgPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupNewCfgPorts.setStatus("current")
_TrunkGroupNewCfgAddPort_Type = Integer32
_TrunkGroupNewCfgAddPort_Object = MibTableColumn
trunkGroupNewCfgAddPort = _TrunkGroupNewCfgAddPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 2, 3, 1, 3),
    _TrunkGroupNewCfgAddPort_Type()
)
trunkGroupNewCfgAddPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkGroupNewCfgAddPort.setStatus("current")
_TrunkGroupNewCfgRemovePort_Type = Integer32
_TrunkGroupNewCfgRemovePort_Object = MibTableColumn
trunkGroupNewCfgRemovePort = _TrunkGroupNewCfgRemovePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 2, 3, 1, 4),
    _TrunkGroupNewCfgRemovePort_Type()
)
trunkGroupNewCfgRemovePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkGroupNewCfgRemovePort.setStatus("current")


class _TrunkGroupNewCfgState_Type(Integer32):
    """Custom type trunkGroupNewCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TrunkGroupNewCfgState_Type.__name__ = "Integer32"
_TrunkGroupNewCfgState_Object = MibTableColumn
trunkGroupNewCfgState = _TrunkGroupNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 2, 3, 1, 5),
    _TrunkGroupNewCfgState_Type()
)
trunkGroupNewCfgState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkGroupNewCfgState.setStatus("current")


class _TrunkGroupNewCfgDelete_Type(Integer32):
    """Custom type trunkGroupNewCfgDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_TrunkGroupNewCfgDelete_Type.__name__ = "Integer32"
_TrunkGroupNewCfgDelete_Object = MibTableColumn
trunkGroupNewCfgDelete = _TrunkGroupNewCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 2, 3, 1, 6),
    _TrunkGroupNewCfgDelete_Type()
)
trunkGroupNewCfgDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkGroupNewCfgDelete.setStatus("current")
_StgCfg_ObjectIdentity = ObjectIdentity
stgCfg = _StgCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3)
)
_StgCurCfgTable_Object = MibTable
stgCurCfgTable = _StgCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    stgCurCfgTable.setStatus("current")
_StgCurCfgTableEntry_Object = MibTableRow
stgCurCfgTableEntry = _StgCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 1, 1)
)
stgCurCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "stgCurCfgIndex"),
)
if mibBuilder.loadTexts:
    stgCurCfgTableEntry.setStatus("current")
_StgCurCfgIndex_Type = Integer32
_StgCurCfgIndex_Object = MibTableColumn
stgCurCfgIndex = _StgCurCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 1, 1, 1),
    _StgCurCfgIndex_Type()
)
stgCurCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgIndex.setStatus("current")


class _StgCurCfgState_Type(Integer32):
    """Custom type stgCurCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_StgCurCfgState_Type.__name__ = "Integer32"
_StgCurCfgState_Object = MibTableColumn
stgCurCfgState = _StgCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 1, 1, 2),
    _StgCurCfgState_Type()
)
stgCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgState.setStatus("current")


class _StgCurCfgVlanBmap1_Type(OctetString):
    """Custom type stgCurCfgVlanBmap1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_StgCurCfgVlanBmap1_Type.__name__ = "OctetString"
_StgCurCfgVlanBmap1_Object = MibTableColumn
stgCurCfgVlanBmap1 = _StgCurCfgVlanBmap1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 1, 1, 3),
    _StgCurCfgVlanBmap1_Type()
)
stgCurCfgVlanBmap1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgVlanBmap1.setStatus("obsolete")


class _StgCurCfgVlanBmap2_Type(OctetString):
    """Custom type stgCurCfgVlanBmap2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_StgCurCfgVlanBmap2_Type.__name__ = "OctetString"
_StgCurCfgVlanBmap2_Object = MibTableColumn
stgCurCfgVlanBmap2 = _StgCurCfgVlanBmap2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 1, 1, 4),
    _StgCurCfgVlanBmap2_Type()
)
stgCurCfgVlanBmap2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgVlanBmap2.setStatus("obsolete")


class _StgCurCfgPriority_Type(Integer32):
    """Custom type stgCurCfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StgCurCfgPriority_Type.__name__ = "Integer32"
_StgCurCfgPriority_Object = MibTableColumn
stgCurCfgPriority = _StgCurCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 1, 1, 5),
    _StgCurCfgPriority_Type()
)
stgCurCfgPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgPriority.setStatus("current")


class _StgCurCfgBrgHelloTime_Type(Integer32):
    """Custom type stgCurCfgBrgHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StgCurCfgBrgHelloTime_Type.__name__ = "Integer32"
_StgCurCfgBrgHelloTime_Object = MibTableColumn
stgCurCfgBrgHelloTime = _StgCurCfgBrgHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 1, 1, 6),
    _StgCurCfgBrgHelloTime_Type()
)
stgCurCfgBrgHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgBrgHelloTime.setStatus("current")


class _StgCurCfgBrgForwardDelay_Type(Integer32):
    """Custom type stgCurCfgBrgForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_StgCurCfgBrgForwardDelay_Type.__name__ = "Integer32"
_StgCurCfgBrgForwardDelay_Object = MibTableColumn
stgCurCfgBrgForwardDelay = _StgCurCfgBrgForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 1, 1, 7),
    _StgCurCfgBrgForwardDelay_Type()
)
stgCurCfgBrgForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgBrgForwardDelay.setStatus("current")


class _StgCurCfgBrgMaxAge_Type(Integer32):
    """Custom type stgCurCfgBrgMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_StgCurCfgBrgMaxAge_Type.__name__ = "Integer32"
_StgCurCfgBrgMaxAge_Object = MibTableColumn
stgCurCfgBrgMaxAge = _StgCurCfgBrgMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 1, 1, 8),
    _StgCurCfgBrgMaxAge_Type()
)
stgCurCfgBrgMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgBrgMaxAge.setStatus("current")


class _StgCurCfgAgingTime_Type(Integer32):
    """Custom type stgCurCfgAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StgCurCfgAgingTime_Type.__name__ = "Integer32"
_StgCurCfgAgingTime_Object = MibTableColumn
stgCurCfgAgingTime = _StgCurCfgAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 1, 1, 9),
    _StgCurCfgAgingTime_Type()
)
stgCurCfgAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgAgingTime.setStatus("current")


class _StgCurCfgVlanBmap_Type(OctetString):
    """Custom type stgCurCfgVlanBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_StgCurCfgVlanBmap_Type.__name__ = "OctetString"
_StgCurCfgVlanBmap_Object = MibTableColumn
stgCurCfgVlanBmap = _StgCurCfgVlanBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 1, 1, 10),
    _StgCurCfgVlanBmap_Type()
)
stgCurCfgVlanBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgVlanBmap.setStatus("current")
_StgNewCfgTable_Object = MibTable
stgNewCfgTable = _StgNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    stgNewCfgTable.setStatus("current")
_StgNewCfgTableEntry_Object = MibTableRow
stgNewCfgTableEntry = _StgNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 2, 1)
)
stgNewCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "stgNewCfgIndex"),
)
if mibBuilder.loadTexts:
    stgNewCfgTableEntry.setStatus("current")
_StgNewCfgIndex_Type = Integer32
_StgNewCfgIndex_Object = MibTableColumn
stgNewCfgIndex = _StgNewCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 2, 1, 1),
    _StgNewCfgIndex_Type()
)
stgNewCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgNewCfgIndex.setStatus("current")


class _StgNewCfgState_Type(Integer32):
    """Custom type stgNewCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_StgNewCfgState_Type.__name__ = "Integer32"
_StgNewCfgState_Object = MibTableColumn
stgNewCfgState = _StgNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 2, 1, 2),
    _StgNewCfgState_Type()
)
stgNewCfgState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stgNewCfgState.setStatus("current")


class _StgNewCfgDefaultCfg_Type(Integer32):
    """Custom type stgNewCfgDefaultCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("default-config", 1)
    )


_StgNewCfgDefaultCfg_Type.__name__ = "Integer32"
_StgNewCfgDefaultCfg_Object = MibTableColumn
stgNewCfgDefaultCfg = _StgNewCfgDefaultCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 2, 1, 3),
    _StgNewCfgDefaultCfg_Type()
)
stgNewCfgDefaultCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stgNewCfgDefaultCfg.setStatus("current")
_StgNewCfgAddVlan_Type = Integer32
_StgNewCfgAddVlan_Object = MibTableColumn
stgNewCfgAddVlan = _StgNewCfgAddVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 2, 1, 4),
    _StgNewCfgAddVlan_Type()
)
stgNewCfgAddVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stgNewCfgAddVlan.setStatus("current")
_StgNewCfgRemoveVlan_Type = Integer32
_StgNewCfgRemoveVlan_Object = MibTableColumn
stgNewCfgRemoveVlan = _StgNewCfgRemoveVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 2, 1, 5),
    _StgNewCfgRemoveVlan_Type()
)
stgNewCfgRemoveVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stgNewCfgRemoveVlan.setStatus("current")


class _StgNewCfgVlanBmap1_Type(OctetString):
    """Custom type stgNewCfgVlanBmap1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_StgNewCfgVlanBmap1_Type.__name__ = "OctetString"
_StgNewCfgVlanBmap1_Object = MibTableColumn
stgNewCfgVlanBmap1 = _StgNewCfgVlanBmap1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 2, 1, 6),
    _StgNewCfgVlanBmap1_Type()
)
stgNewCfgVlanBmap1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgNewCfgVlanBmap1.setStatus("obsolete")


class _StgNewCfgVlanBmap2_Type(OctetString):
    """Custom type stgNewCfgVlanBmap2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_StgNewCfgVlanBmap2_Type.__name__ = "OctetString"
_StgNewCfgVlanBmap2_Object = MibTableColumn
stgNewCfgVlanBmap2 = _StgNewCfgVlanBmap2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 2, 1, 7),
    _StgNewCfgVlanBmap2_Type()
)
stgNewCfgVlanBmap2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgNewCfgVlanBmap2.setStatus("obsolete")


class _StgNewCfgPriority_Type(Integer32):
    """Custom type stgNewCfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StgNewCfgPriority_Type.__name__ = "Integer32"
_StgNewCfgPriority_Object = MibTableColumn
stgNewCfgPriority = _StgNewCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 2, 1, 8),
    _StgNewCfgPriority_Type()
)
stgNewCfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stgNewCfgPriority.setStatus("current")


class _StgNewCfgBrgHelloTime_Type(Integer32):
    """Custom type stgNewCfgBrgHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StgNewCfgBrgHelloTime_Type.__name__ = "Integer32"
_StgNewCfgBrgHelloTime_Object = MibTableColumn
stgNewCfgBrgHelloTime = _StgNewCfgBrgHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 2, 1, 9),
    _StgNewCfgBrgHelloTime_Type()
)
stgNewCfgBrgHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stgNewCfgBrgHelloTime.setStatus("current")


class _StgNewCfgBrgForwardDelay_Type(Integer32):
    """Custom type stgNewCfgBrgForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_StgNewCfgBrgForwardDelay_Type.__name__ = "Integer32"
_StgNewCfgBrgForwardDelay_Object = MibTableColumn
stgNewCfgBrgForwardDelay = _StgNewCfgBrgForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 2, 1, 10),
    _StgNewCfgBrgForwardDelay_Type()
)
stgNewCfgBrgForwardDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stgNewCfgBrgForwardDelay.setStatus("current")


class _StgNewCfgBrgMaxAge_Type(Integer32):
    """Custom type stgNewCfgBrgMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_StgNewCfgBrgMaxAge_Type.__name__ = "Integer32"
_StgNewCfgBrgMaxAge_Object = MibTableColumn
stgNewCfgBrgMaxAge = _StgNewCfgBrgMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 2, 1, 11),
    _StgNewCfgBrgMaxAge_Type()
)
stgNewCfgBrgMaxAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stgNewCfgBrgMaxAge.setStatus("current")


class _StgNewCfgAgingTime_Type(Integer32):
    """Custom type stgNewCfgAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StgNewCfgAgingTime_Type.__name__ = "Integer32"
_StgNewCfgAgingTime_Object = MibTableColumn
stgNewCfgAgingTime = _StgNewCfgAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 2, 1, 12),
    _StgNewCfgAgingTime_Type()
)
stgNewCfgAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stgNewCfgAgingTime.setStatus("current")


class _StgNewCfgVlanBmap_Type(OctetString):
    """Custom type stgNewCfgVlanBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_StgNewCfgVlanBmap_Type.__name__ = "OctetString"
_StgNewCfgVlanBmap_Object = MibTableColumn
stgNewCfgVlanBmap = _StgNewCfgVlanBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 2, 1, 13),
    _StgNewCfgVlanBmap_Type()
)
stgNewCfgVlanBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgNewCfgVlanBmap.setStatus("current")
_StgCurCfgPortTable_Object = MibTable
stgCurCfgPortTable = _StgCurCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    stgCurCfgPortTable.setStatus("current")
_StgCurCfgPortTableEntry_Object = MibTableRow
stgCurCfgPortTableEntry = _StgCurCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 3, 1)
)
stgCurCfgPortTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "stgCurCfgStgIndex"),
    (0, "BLADETYPE2-PHYSICAL-MIB", "stgCurCfgPortIndex"),
)
if mibBuilder.loadTexts:
    stgCurCfgPortTableEntry.setStatus("current")
_StgCurCfgStgIndex_Type = Integer32
_StgCurCfgStgIndex_Object = MibTableColumn
stgCurCfgStgIndex = _StgCurCfgStgIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 3, 1, 1),
    _StgCurCfgStgIndex_Type()
)
stgCurCfgStgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgStgIndex.setStatus("current")
_StgCurCfgPortIndex_Type = Integer32
_StgCurCfgPortIndex_Object = MibTableColumn
stgCurCfgPortIndex = _StgCurCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 3, 1, 2),
    _StgCurCfgPortIndex_Type()
)
stgCurCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgPortIndex.setStatus("current")


class _StgCurCfgPortState_Type(Integer32):
    """Custom type stgCurCfgPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_StgCurCfgPortState_Type.__name__ = "Integer32"
_StgCurCfgPortState_Object = MibTableColumn
stgCurCfgPortState = _StgCurCfgPortState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 3, 1, 3),
    _StgCurCfgPortState_Type()
)
stgCurCfgPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgPortState.setStatus("current")


class _StgCurCfgPortPriority_Type(Integer32):
    """Custom type stgCurCfgPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StgCurCfgPortPriority_Type.__name__ = "Integer32"
_StgCurCfgPortPriority_Object = MibTableColumn
stgCurCfgPortPriority = _StgCurCfgPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 3, 1, 4),
    _StgCurCfgPortPriority_Type()
)
stgCurCfgPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgPortPriority.setStatus("current")


class _StgCurCfgPortPathCost_Type(Integer32):
    """Custom type stgCurCfgPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StgCurCfgPortPathCost_Type.__name__ = "Integer32"
_StgCurCfgPortPathCost_Object = MibTableColumn
stgCurCfgPortPathCost = _StgCurCfgPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 3, 1, 5),
    _StgCurCfgPortPathCost_Type()
)
stgCurCfgPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgPortPathCost.setStatus("current")


class _StgCurCfgPortLink_Type(Integer32):
    """Custom type stgCurCfgPortLink based on Integer32"""
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
          ("p2p", 2),
          ("shared", 3))
    )


_StgCurCfgPortLink_Type.__name__ = "Integer32"
_StgCurCfgPortLink_Object = MibTableColumn
stgCurCfgPortLink = _StgCurCfgPortLink_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 3, 1, 6),
    _StgCurCfgPortLink_Type()
)
stgCurCfgPortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgPortLink.setStatus("current")


class _StgCurCfgPortEdge_Type(Integer32):
    """Custom type stgCurCfgPortEdge based on Integer32"""
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


_StgCurCfgPortEdge_Type.__name__ = "Integer32"
_StgCurCfgPortEdge_Object = MibTableColumn
stgCurCfgPortEdge = _StgCurCfgPortEdge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 3, 1, 7),
    _StgCurCfgPortEdge_Type()
)
stgCurCfgPortEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgPortEdge.setStatus("current")


class _StgCurCfgPortFastFwd_Type(Integer32):
    """Custom type stgCurCfgPortFastFwd based on Integer32"""
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


_StgCurCfgPortFastFwd_Type.__name__ = "Integer32"
_StgCurCfgPortFastFwd_Object = MibTableColumn
stgCurCfgPortFastFwd = _StgCurCfgPortFastFwd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 3, 1, 8),
    _StgCurCfgPortFastFwd_Type()
)
stgCurCfgPortFastFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgPortFastFwd.setStatus("current")
_StgNewCfgPortTable_Object = MibTable
stgNewCfgPortTable = _StgNewCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    stgNewCfgPortTable.setStatus("current")
_StgNewCfgPortTableEntry_Object = MibTableRow
stgNewCfgPortTableEntry = _StgNewCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 4, 1)
)
stgNewCfgPortTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "stgNewCfgStgIndex"),
    (0, "BLADETYPE2-PHYSICAL-MIB", "stgNewCfgPortIndex"),
)
if mibBuilder.loadTexts:
    stgNewCfgPortTableEntry.setStatus("current")
_StgNewCfgStgIndex_Type = Integer32
_StgNewCfgStgIndex_Object = MibTableColumn
stgNewCfgStgIndex = _StgNewCfgStgIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 4, 1, 1),
    _StgNewCfgStgIndex_Type()
)
stgNewCfgStgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgNewCfgStgIndex.setStatus("current")
_StgNewCfgPortIndex_Type = Integer32
_StgNewCfgPortIndex_Object = MibTableColumn
stgNewCfgPortIndex = _StgNewCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 4, 1, 2),
    _StgNewCfgPortIndex_Type()
)
stgNewCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgNewCfgPortIndex.setStatus("current")


class _StgNewCfgPortState_Type(Integer32):
    """Custom type stgNewCfgPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_StgNewCfgPortState_Type.__name__ = "Integer32"
_StgNewCfgPortState_Object = MibTableColumn
stgNewCfgPortState = _StgNewCfgPortState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 4, 1, 3),
    _StgNewCfgPortState_Type()
)
stgNewCfgPortState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stgNewCfgPortState.setStatus("current")


class _StgNewCfgPortPriority_Type(Integer32):
    """Custom type stgNewCfgPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StgNewCfgPortPriority_Type.__name__ = "Integer32"
_StgNewCfgPortPriority_Object = MibTableColumn
stgNewCfgPortPriority = _StgNewCfgPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 4, 1, 4),
    _StgNewCfgPortPriority_Type()
)
stgNewCfgPortPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stgNewCfgPortPriority.setStatus("current")


class _StgNewCfgPortPathCost_Type(Integer32):
    """Custom type stgNewCfgPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StgNewCfgPortPathCost_Type.__name__ = "Integer32"
_StgNewCfgPortPathCost_Object = MibTableColumn
stgNewCfgPortPathCost = _StgNewCfgPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 4, 1, 5),
    _StgNewCfgPortPathCost_Type()
)
stgNewCfgPortPathCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stgNewCfgPortPathCost.setStatus("current")


class _StgNewCfgPortLink_Type(Integer32):
    """Custom type stgNewCfgPortLink based on Integer32"""
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
          ("p2p", 2),
          ("shared", 3))
    )


_StgNewCfgPortLink_Type.__name__ = "Integer32"
_StgNewCfgPortLink_Object = MibTableColumn
stgNewCfgPortLink = _StgNewCfgPortLink_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 4, 1, 6),
    _StgNewCfgPortLink_Type()
)
stgNewCfgPortLink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stgNewCfgPortLink.setStatus("current")


class _StgNewCfgPortEdge_Type(Integer32):
    """Custom type stgNewCfgPortEdge based on Integer32"""
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


_StgNewCfgPortEdge_Type.__name__ = "Integer32"
_StgNewCfgPortEdge_Object = MibTableColumn
stgNewCfgPortEdge = _StgNewCfgPortEdge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 4, 1, 7),
    _StgNewCfgPortEdge_Type()
)
stgNewCfgPortEdge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stgNewCfgPortEdge.setStatus("current")


class _StgNewCfgPortFastFwd_Type(Integer32):
    """Custom type stgNewCfgPortFastFwd based on Integer32"""
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


_StgNewCfgPortFastFwd_Type.__name__ = "Integer32"
_StgNewCfgPortFastFwd_Object = MibTableColumn
stgNewCfgPortFastFwd = _StgNewCfgPortFastFwd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 3, 4, 1, 8),
    _StgNewCfgPortFastFwd_Type()
)
stgNewCfgPortFastFwd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stgNewCfgPortFastFwd.setStatus("current")
_Mirroring_ObjectIdentity = ObjectIdentity
mirroring = _Mirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 4)
)
_MirrPortMirr_ObjectIdentity = ObjectIdentity
mirrPortMirr = _MirrPortMirr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 4, 1)
)


class _PmCurCfgPortMirrState_Type(Integer32):
    """Custom type pmCurCfgPortMirrState based on Integer32"""
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


_PmCurCfgPortMirrState_Type.__name__ = "Integer32"
_PmCurCfgPortMirrState_Object = MibScalar
pmCurCfgPortMirrState = _PmCurCfgPortMirrState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 4, 1, 1),
    _PmCurCfgPortMirrState_Type()
)
pmCurCfgPortMirrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgPortMirrState.setStatus("current")


class _PmNewCfgPortMirrState_Type(Integer32):
    """Custom type pmNewCfgPortMirrState based on Integer32"""
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


_PmNewCfgPortMirrState_Type.__name__ = "Integer32"
_PmNewCfgPortMirrState_Object = MibScalar
pmNewCfgPortMirrState = _PmNewCfgPortMirrState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 4, 1, 2),
    _PmNewCfgPortMirrState_Type()
)
pmNewCfgPortMirrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmNewCfgPortMirrState.setStatus("current")
_PmCurCfgPortMonitorTable_Object = MibTable
pmCurCfgPortMonitorTable = _PmCurCfgPortMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    pmCurCfgPortMonitorTable.setStatus("current")
_PmCurCfgPortMonitorEntry_Object = MibTableRow
pmCurCfgPortMonitorEntry = _PmCurCfgPortMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 4, 1, 3, 1)
)
pmCurCfgPortMonitorEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "pmCurCfgPmirrMoniPortIndex"),
    (0, "BLADETYPE2-PHYSICAL-MIB", "pmCurCfgPmirrMirrPortIndex"),
)
if mibBuilder.loadTexts:
    pmCurCfgPortMonitorEntry.setStatus("current")
_PmCurCfgPmirrMoniPortIndex_Type = Integer32
_PmCurCfgPmirrMoniPortIndex_Object = MibTableColumn
pmCurCfgPmirrMoniPortIndex = _PmCurCfgPmirrMoniPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 4, 1, 3, 1, 1),
    _PmCurCfgPmirrMoniPortIndex_Type()
)
pmCurCfgPmirrMoniPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgPmirrMoniPortIndex.setStatus("current")
_PmCurCfgPmirrMirrPortIndex_Type = Integer32
_PmCurCfgPmirrMirrPortIndex_Object = MibTableColumn
pmCurCfgPmirrMirrPortIndex = _PmCurCfgPmirrMirrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 4, 1, 3, 1, 2),
    _PmCurCfgPmirrMirrPortIndex_Type()
)
pmCurCfgPmirrMirrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgPmirrMirrPortIndex.setStatus("current")


class _PmCurCfgPmirrDirection_Type(Integer32):
    """Custom type pmCurCfgPmirrDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("in", 1),
          ("out", 2))
    )


_PmCurCfgPmirrDirection_Type.__name__ = "Integer32"
_PmCurCfgPmirrDirection_Object = MibTableColumn
pmCurCfgPmirrDirection = _PmCurCfgPmirrDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 4, 1, 3, 1, 3),
    _PmCurCfgPmirrDirection_Type()
)
pmCurCfgPmirrDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgPmirrDirection.setStatus("current")
_PmNewCfgPortMonitorTable_Object = MibTable
pmNewCfgPortMonitorTable = _PmNewCfgPortMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    pmNewCfgPortMonitorTable.setStatus("current")
_PmNewCfgPortMonitorEntry_Object = MibTableRow
pmNewCfgPortMonitorEntry = _PmNewCfgPortMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 4, 1, 4, 1)
)
pmNewCfgPortMonitorEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "pmNewCfgPmirrMoniPortIndex"),
    (0, "BLADETYPE2-PHYSICAL-MIB", "pmNewCfgPmirrMirrPortIndex"),
)
if mibBuilder.loadTexts:
    pmNewCfgPortMonitorEntry.setStatus("current")
_PmNewCfgPmirrMoniPortIndex_Type = Integer32
_PmNewCfgPmirrMoniPortIndex_Object = MibTableColumn
pmNewCfgPmirrMoniPortIndex = _PmNewCfgPmirrMoniPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 4, 1, 4, 1, 1),
    _PmNewCfgPmirrMoniPortIndex_Type()
)
pmNewCfgPmirrMoniPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmNewCfgPmirrMoniPortIndex.setStatus("current")
_PmNewCfgPmirrMirrPortIndex_Type = Integer32
_PmNewCfgPmirrMirrPortIndex_Object = MibTableColumn
pmNewCfgPmirrMirrPortIndex = _PmNewCfgPmirrMirrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 4, 1, 4, 1, 2),
    _PmNewCfgPmirrMirrPortIndex_Type()
)
pmNewCfgPmirrMirrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmNewCfgPmirrMirrPortIndex.setStatus("current")


class _PmNewCfgPmirrDirection_Type(Integer32):
    """Custom type pmNewCfgPmirrDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("in", 1),
          ("out", 2))
    )


_PmNewCfgPmirrDirection_Type.__name__ = "Integer32"
_PmNewCfgPmirrDirection_Object = MibTableColumn
pmNewCfgPmirrDirection = _PmNewCfgPmirrDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 4, 1, 4, 1, 3),
    _PmNewCfgPmirrDirection_Type()
)
pmNewCfgPmirrDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmNewCfgPmirrDirection.setStatus("current")


class _PmNewCfgPmirrDelete_Type(Integer32):
    """Custom type pmNewCfgPmirrDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_PmNewCfgPmirrDelete_Type.__name__ = "Integer32"
_PmNewCfgPmirrDelete_Object = MibTableColumn
pmNewCfgPmirrDelete = _PmNewCfgPmirrDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 4, 1, 4, 1, 4),
    _PmNewCfgPmirrDelete_Type()
)
pmNewCfgPmirrDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmNewCfgPmirrDelete.setStatus("current")


class _PmNewCfgPmonDelete_Type(Integer32):
    """Custom type pmNewCfgPmonDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_PmNewCfgPmonDelete_Type.__name__ = "Integer32"
_PmNewCfgPmonDelete_Object = MibTableColumn
pmNewCfgPmonDelete = _PmNewCfgPmonDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 4, 1, 4, 1, 10),
    _PmNewCfgPmonDelete_Type()
)
pmNewCfgPmonDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmNewCfgPmonDelete.setStatus("current")
_MstCfg_ObjectIdentity = ObjectIdentity
mstCfg = _MstCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5)
)
_MstGeneralCfg_ObjectIdentity = ObjectIdentity
mstGeneralCfg = _MstGeneralCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 1)
)


class _MstCurCfgState_Type(Integer32):
    """Custom type mstCurCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_MstCurCfgState_Type.__name__ = "Integer32"
_MstCurCfgState_Object = MibScalar
mstCurCfgState = _MstCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 1, 1),
    _MstCurCfgState_Type()
)
mstCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCurCfgState.setStatus("current")


class _MstNewCfgState_Type(Integer32):
    """Custom type mstNewCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_MstNewCfgState_Type.__name__ = "Integer32"
_MstNewCfgState_Object = MibScalar
mstNewCfgState = _MstNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 1, 2),
    _MstNewCfgState_Type()
)
mstNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstNewCfgState.setStatus("current")


class _MstCurCfgRegionName_Type(DisplayString):
    """Custom type mstCurCfgRegionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MstCurCfgRegionName_Type.__name__ = "DisplayString"
_MstCurCfgRegionName_Object = MibScalar
mstCurCfgRegionName = _MstCurCfgRegionName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 1, 3),
    _MstCurCfgRegionName_Type()
)
mstCurCfgRegionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCurCfgRegionName.setStatus("current")


class _MstNewCfgRegionName_Type(DisplayString):
    """Custom type mstNewCfgRegionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MstNewCfgRegionName_Type.__name__ = "DisplayString"
_MstNewCfgRegionName_Object = MibScalar
mstNewCfgRegionName = _MstNewCfgRegionName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 1, 4),
    _MstNewCfgRegionName_Type()
)
mstNewCfgRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstNewCfgRegionName.setStatus("current")


class _MstCurCfgRegionVersion_Type(Integer32):
    """Custom type mstCurCfgRegionVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MstCurCfgRegionVersion_Type.__name__ = "Integer32"
_MstCurCfgRegionVersion_Object = MibScalar
mstCurCfgRegionVersion = _MstCurCfgRegionVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 1, 5),
    _MstCurCfgRegionVersion_Type()
)
mstCurCfgRegionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCurCfgRegionVersion.setStatus("current")


class _MstNewCfgRegionVersion_Type(Integer32):
    """Custom type mstNewCfgRegionVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MstNewCfgRegionVersion_Type.__name__ = "Integer32"
_MstNewCfgRegionVersion_Object = MibScalar
mstNewCfgRegionVersion = _MstNewCfgRegionVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 1, 6),
    _MstNewCfgRegionVersion_Type()
)
mstNewCfgRegionVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstNewCfgRegionVersion.setStatus("current")


class _MstCurCfgMaxHopCount_Type(Integer32):
    """Custom type mstCurCfgMaxHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_MstCurCfgMaxHopCount_Type.__name__ = "Integer32"
_MstCurCfgMaxHopCount_Object = MibScalar
mstCurCfgMaxHopCount = _MstCurCfgMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 1, 7),
    _MstCurCfgMaxHopCount_Type()
)
mstCurCfgMaxHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCurCfgMaxHopCount.setStatus("current")


class _MstNewCfgMaxHopCount_Type(Integer32):
    """Custom type mstNewCfgMaxHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_MstNewCfgMaxHopCount_Type.__name__ = "Integer32"
_MstNewCfgMaxHopCount_Object = MibScalar
mstNewCfgMaxHopCount = _MstNewCfgMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 1, 8),
    _MstNewCfgMaxHopCount_Type()
)
mstNewCfgMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstNewCfgMaxHopCount.setStatus("current")


class _MstCurCfgStpMode_Type(Integer32):
    """Custom type mstCurCfgStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 1),
          ("rstp", 2))
    )


_MstCurCfgStpMode_Type.__name__ = "Integer32"
_MstCurCfgStpMode_Object = MibScalar
mstCurCfgStpMode = _MstCurCfgStpMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 1, 9),
    _MstCurCfgStpMode_Type()
)
mstCurCfgStpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCurCfgStpMode.setStatus("current")


class _MstNewCfgStpMode_Type(Integer32):
    """Custom type mstNewCfgStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 1),
          ("rstp", 2))
    )


_MstNewCfgStpMode_Type.__name__ = "Integer32"
_MstNewCfgStpMode_Object = MibScalar
mstNewCfgStpMode = _MstNewCfgStpMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 1, 10),
    _MstNewCfgStpMode_Type()
)
mstNewCfgStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstNewCfgStpMode.setStatus("current")
_MstCistCfg_ObjectIdentity = ObjectIdentity
mstCistCfg = _MstCistCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2)
)


class _MstCistDefaultCfg_Type(Integer32):
    """Custom type mstCistDefaultCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("default", 1)
    )


_MstCistDefaultCfg_Type.__name__ = "Integer32"
_MstCistDefaultCfg_Object = MibScalar
mstCistDefaultCfg = _MstCistDefaultCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 1),
    _MstCistDefaultCfg_Type()
)
mstCistDefaultCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstCistDefaultCfg.setStatus("current")
_MstCistBridgeCfg_ObjectIdentity = ObjectIdentity
mstCistBridgeCfg = _MstCistBridgeCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 2)
)


class _MstCistCurCfgBridgePriority_Type(Integer32):
    """Custom type mstCistCurCfgBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MstCistCurCfgBridgePriority_Type.__name__ = "Integer32"
_MstCistCurCfgBridgePriority_Object = MibScalar
mstCistCurCfgBridgePriority = _MstCistCurCfgBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 2, 1),
    _MstCistCurCfgBridgePriority_Type()
)
mstCistCurCfgBridgePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistCurCfgBridgePriority.setStatus("current")


class _MstCistNewCfgBridgePriority_Type(Integer32):
    """Custom type mstCistNewCfgBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MstCistNewCfgBridgePriority_Type.__name__ = "Integer32"
_MstCistNewCfgBridgePriority_Object = MibScalar
mstCistNewCfgBridgePriority = _MstCistNewCfgBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 2, 2),
    _MstCistNewCfgBridgePriority_Type()
)
mstCistNewCfgBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstCistNewCfgBridgePriority.setStatus("current")


class _MstCistCurCfgBridgeMaxAge_Type(Integer32):
    """Custom type mstCistCurCfgBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_MstCistCurCfgBridgeMaxAge_Type.__name__ = "Integer32"
_MstCistCurCfgBridgeMaxAge_Object = MibScalar
mstCistCurCfgBridgeMaxAge = _MstCistCurCfgBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 2, 5),
    _MstCistCurCfgBridgeMaxAge_Type()
)
mstCistCurCfgBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistCurCfgBridgeMaxAge.setStatus("current")


class _MstCistNewCfgBridgeMaxAge_Type(Integer32):
    """Custom type mstCistNewCfgBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_MstCistNewCfgBridgeMaxAge_Type.__name__ = "Integer32"
_MstCistNewCfgBridgeMaxAge_Object = MibScalar
mstCistNewCfgBridgeMaxAge = _MstCistNewCfgBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 2, 6),
    _MstCistNewCfgBridgeMaxAge_Type()
)
mstCistNewCfgBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstCistNewCfgBridgeMaxAge.setStatus("current")


class _MstCistCurCfgBridgeForwardDelay_Type(Integer32):
    """Custom type mstCistCurCfgBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_MstCistCurCfgBridgeForwardDelay_Type.__name__ = "Integer32"
_MstCistCurCfgBridgeForwardDelay_Object = MibScalar
mstCistCurCfgBridgeForwardDelay = _MstCistCurCfgBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 2, 7),
    _MstCistCurCfgBridgeForwardDelay_Type()
)
mstCistCurCfgBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistCurCfgBridgeForwardDelay.setStatus("current")


class _MstCistNewCfgBridgeForwardDelay_Type(Integer32):
    """Custom type mstCistNewCfgBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_MstCistNewCfgBridgeForwardDelay_Type.__name__ = "Integer32"
_MstCistNewCfgBridgeForwardDelay_Object = MibScalar
mstCistNewCfgBridgeForwardDelay = _MstCistNewCfgBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 2, 8),
    _MstCistNewCfgBridgeForwardDelay_Type()
)
mstCistNewCfgBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstCistNewCfgBridgeForwardDelay.setStatus("current")


class _MstCistCurCfgVlanBmap_Type(OctetString):
    """Custom type mstCistCurCfgVlanBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MstCistCurCfgVlanBmap_Type.__name__ = "OctetString"
_MstCistCurCfgVlanBmap_Object = MibScalar
mstCistCurCfgVlanBmap = _MstCistCurCfgVlanBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 2, 9),
    _MstCistCurCfgVlanBmap_Type()
)
mstCistCurCfgVlanBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistCurCfgVlanBmap.setStatus("current")


class _MstCistNewCfgVlanBmap_Type(OctetString):
    """Custom type mstCistNewCfgVlanBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MstCistNewCfgVlanBmap_Type.__name__ = "OctetString"
_MstCistNewCfgVlanBmap_Object = MibScalar
mstCistNewCfgVlanBmap = _MstCistNewCfgVlanBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 2, 10),
    _MstCistNewCfgVlanBmap_Type()
)
mstCistNewCfgVlanBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistNewCfgVlanBmap.setStatus("current")
_MstCistNewCfgAddVlan_Type = Integer32
_MstCistNewCfgAddVlan_Object = MibScalar
mstCistNewCfgAddVlan = _MstCistNewCfgAddVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 2, 11),
    _MstCistNewCfgAddVlan_Type()
)
mstCistNewCfgAddVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstCistNewCfgAddVlan.setStatus("current")
_MstCistCurCfgPortTable_Object = MibTable
mstCistCurCfgPortTable = _MstCistCurCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    mstCistCurCfgPortTable.setStatus("current")
_MstCistCurCfgPortTableEntry_Object = MibTableRow
mstCistCurCfgPortTableEntry = _MstCistCurCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 3, 1)
)
mstCistCurCfgPortTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "mstCistCurCfgPortIndex"),
)
if mibBuilder.loadTexts:
    mstCistCurCfgPortTableEntry.setStatus("current")
_MstCistCurCfgPortIndex_Type = Integer32
_MstCistCurCfgPortIndex_Object = MibTableColumn
mstCistCurCfgPortIndex = _MstCistCurCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 3, 1, 1),
    _MstCistCurCfgPortIndex_Type()
)
mstCistCurCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistCurCfgPortIndex.setStatus("current")


class _MstCistCurCfgPortPriority_Type(Integer32):
    """Custom type mstCistCurCfgPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_MstCistCurCfgPortPriority_Type.__name__ = "Integer32"
_MstCistCurCfgPortPriority_Object = MibTableColumn
mstCistCurCfgPortPriority = _MstCistCurCfgPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 3, 1, 2),
    _MstCistCurCfgPortPriority_Type()
)
mstCistCurCfgPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistCurCfgPortPriority.setStatus("current")


class _MstCistCurCfgPortPathCost_Type(Integer32):
    """Custom type mstCistCurCfgPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_MstCistCurCfgPortPathCost_Type.__name__ = "Integer32"
_MstCistCurCfgPortPathCost_Object = MibTableColumn
mstCistCurCfgPortPathCost = _MstCistCurCfgPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 3, 1, 3),
    _MstCistCurCfgPortPathCost_Type()
)
mstCistCurCfgPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistCurCfgPortPathCost.setStatus("current")


class _MstCistCurCfgPortLinkType_Type(Integer32):
    """Custom type mstCistCurCfgPortLinkType based on Integer32"""
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
          ("p2p", 2),
          ("shared", 3))
    )


_MstCistCurCfgPortLinkType_Type.__name__ = "Integer32"
_MstCistCurCfgPortLinkType_Object = MibTableColumn
mstCistCurCfgPortLinkType = _MstCistCurCfgPortLinkType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 3, 1, 4),
    _MstCistCurCfgPortLinkType_Type()
)
mstCistCurCfgPortLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistCurCfgPortLinkType.setStatus("current")


class _MstCistCurCfgPortEdge_Type(Integer32):
    """Custom type mstCistCurCfgPortEdge based on Integer32"""
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


_MstCistCurCfgPortEdge_Type.__name__ = "Integer32"
_MstCistCurCfgPortEdge_Object = MibTableColumn
mstCistCurCfgPortEdge = _MstCistCurCfgPortEdge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 3, 1, 5),
    _MstCistCurCfgPortEdge_Type()
)
mstCistCurCfgPortEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistCurCfgPortEdge.setStatus("current")


class _MstCistCurCfgPortStpState_Type(Integer32):
    """Custom type mstCistCurCfgPortStpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_MstCistCurCfgPortStpState_Type.__name__ = "Integer32"
_MstCistCurCfgPortStpState_Object = MibTableColumn
mstCistCurCfgPortStpState = _MstCistCurCfgPortStpState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 3, 1, 6),
    _MstCistCurCfgPortStpState_Type()
)
mstCistCurCfgPortStpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistCurCfgPortStpState.setStatus("current")


class _MstCistCurCfgPortHelloTime_Type(Integer32):
    """Custom type mstCistCurCfgPortHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MstCistCurCfgPortHelloTime_Type.__name__ = "Integer32"
_MstCistCurCfgPortHelloTime_Object = MibTableColumn
mstCistCurCfgPortHelloTime = _MstCistCurCfgPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 3, 1, 7),
    _MstCistCurCfgPortHelloTime_Type()
)
mstCistCurCfgPortHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistCurCfgPortHelloTime.setStatus("current")
_MstCistNewCfgPortTable_Object = MibTable
mstCistNewCfgPortTable = _MstCistNewCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    mstCistNewCfgPortTable.setStatus("current")
_MstCistNewCfgPortTableEntry_Object = MibTableRow
mstCistNewCfgPortTableEntry = _MstCistNewCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 4, 1)
)
mstCistNewCfgPortTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "mstCistNewCfgPortIndex"),
)
if mibBuilder.loadTexts:
    mstCistNewCfgPortTableEntry.setStatus("current")
_MstCistNewCfgPortIndex_Type = Integer32
_MstCistNewCfgPortIndex_Object = MibTableColumn
mstCistNewCfgPortIndex = _MstCistNewCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 4, 1, 1),
    _MstCistNewCfgPortIndex_Type()
)
mstCistNewCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistNewCfgPortIndex.setStatus("current")


class _MstCistNewCfgPortPriority_Type(Integer32):
    """Custom type mstCistNewCfgPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_MstCistNewCfgPortPriority_Type.__name__ = "Integer32"
_MstCistNewCfgPortPriority_Object = MibTableColumn
mstCistNewCfgPortPriority = _MstCistNewCfgPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 4, 1, 2),
    _MstCistNewCfgPortPriority_Type()
)
mstCistNewCfgPortPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstCistNewCfgPortPriority.setStatus("current")


class _MstCistNewCfgPortPathCost_Type(Integer32):
    """Custom type mstCistNewCfgPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_MstCistNewCfgPortPathCost_Type.__name__ = "Integer32"
_MstCistNewCfgPortPathCost_Object = MibTableColumn
mstCistNewCfgPortPathCost = _MstCistNewCfgPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 4, 1, 3),
    _MstCistNewCfgPortPathCost_Type()
)
mstCistNewCfgPortPathCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstCistNewCfgPortPathCost.setStatus("current")


class _MstCistNewCfgPortLinkType_Type(Integer32):
    """Custom type mstCistNewCfgPortLinkType based on Integer32"""
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
          ("p2p", 2),
          ("shared", 3))
    )


_MstCistNewCfgPortLinkType_Type.__name__ = "Integer32"
_MstCistNewCfgPortLinkType_Object = MibTableColumn
mstCistNewCfgPortLinkType = _MstCistNewCfgPortLinkType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 4, 1, 4),
    _MstCistNewCfgPortLinkType_Type()
)
mstCistNewCfgPortLinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstCistNewCfgPortLinkType.setStatus("current")


class _MstCistNewCfgPortEdge_Type(Integer32):
    """Custom type mstCistNewCfgPortEdge based on Integer32"""
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


_MstCistNewCfgPortEdge_Type.__name__ = "Integer32"
_MstCistNewCfgPortEdge_Object = MibTableColumn
mstCistNewCfgPortEdge = _MstCistNewCfgPortEdge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 4, 1, 5),
    _MstCistNewCfgPortEdge_Type()
)
mstCistNewCfgPortEdge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstCistNewCfgPortEdge.setStatus("current")


class _MstCistNewCfgPortStpState_Type(Integer32):
    """Custom type mstCistNewCfgPortStpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_MstCistNewCfgPortStpState_Type.__name__ = "Integer32"
_MstCistNewCfgPortStpState_Object = MibTableColumn
mstCistNewCfgPortStpState = _MstCistNewCfgPortStpState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 4, 1, 6),
    _MstCistNewCfgPortStpState_Type()
)
mstCistNewCfgPortStpState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstCistNewCfgPortStpState.setStatus("current")


class _MstCistNewCfgPortHelloTime_Type(Integer32):
    """Custom type mstCistNewCfgPortHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MstCistNewCfgPortHelloTime_Type.__name__ = "Integer32"
_MstCistNewCfgPortHelloTime_Object = MibTableColumn
mstCistNewCfgPortHelloTime = _MstCistNewCfgPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 5, 2, 4, 1, 7),
    _MstCistNewCfgPortHelloTime_Type()
)
mstCistNewCfgPortHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstCistNewCfgPortHelloTime.setStatus("current")
_Lacp_ObjectIdentity = ObjectIdentity
lacp = _Lacp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 6)
)


class _LacpCurSystemPriority_Type(Integer32):
    """Custom type lacpCurSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LacpCurSystemPriority_Type.__name__ = "Integer32"
_LacpCurSystemPriority_Object = MibScalar
lacpCurSystemPriority = _LacpCurSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 6, 1),
    _LacpCurSystemPriority_Type()
)
lacpCurSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpCurSystemPriority.setStatus("current")


class _LacpNewSystemPriority_Type(Integer32):
    """Custom type lacpNewSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LacpNewSystemPriority_Type.__name__ = "Integer32"
_LacpNewSystemPriority_Object = MibScalar
lacpNewSystemPriority = _LacpNewSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 6, 2),
    _LacpNewSystemPriority_Type()
)
lacpNewSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpNewSystemPriority.setStatus("current")


class _LacpCurSystemTimeoutTime_Type(Integer32):
    """Custom type lacpCurSystemTimeoutTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              90)
        )
    )
    namedValues = NamedValues(
        *(("long", 90),
          ("short", 3))
    )


_LacpCurSystemTimeoutTime_Type.__name__ = "Integer32"
_LacpCurSystemTimeoutTime_Object = MibScalar
lacpCurSystemTimeoutTime = _LacpCurSystemTimeoutTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 6, 5),
    _LacpCurSystemTimeoutTime_Type()
)
lacpCurSystemTimeoutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpCurSystemTimeoutTime.setStatus("current")


class _LacpNewSystemTimeoutTime_Type(Integer32):
    """Custom type lacpNewSystemTimeoutTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              90)
        )
    )
    namedValues = NamedValues(
        *(("long", 90),
          ("short", 3))
    )


_LacpNewSystemTimeoutTime_Type.__name__ = "Integer32"
_LacpNewSystemTimeoutTime_Object = MibScalar
lacpNewSystemTimeoutTime = _LacpNewSystemTimeoutTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 6, 6),
    _LacpNewSystemTimeoutTime_Type()
)
lacpNewSystemTimeoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpNewSystemTimeoutTime.setStatus("current")
_LacpCurPortCfgTable_Object = MibTable
lacpCurPortCfgTable = _LacpCurPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 6, 7)
)
if mibBuilder.loadTexts:
    lacpCurPortCfgTable.setStatus("current")
_LacpCurPortCfgTableEntry_Object = MibTableRow
lacpCurPortCfgTableEntry = _LacpCurPortCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 6, 7, 1)
)
lacpCurPortCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "lacpCurPortCfgTableId"),
)
if mibBuilder.loadTexts:
    lacpCurPortCfgTableEntry.setStatus("current")
_LacpCurPortCfgTableId_Type = Integer32
_LacpCurPortCfgTableId_Object = MibTableColumn
lacpCurPortCfgTableId = _LacpCurPortCfgTableId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 6, 7, 1, 1),
    _LacpCurPortCfgTableId_Type()
)
lacpCurPortCfgTableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpCurPortCfgTableId.setStatus("current")


class _LacpCurPortState_Type(Integer32):
    """Custom type lacpCurPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("off", 1),
          ("passive", 3))
    )


_LacpCurPortState_Type.__name__ = "Integer32"
_LacpCurPortState_Object = MibTableColumn
lacpCurPortState = _LacpCurPortState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 6, 7, 1, 2),
    _LacpCurPortState_Type()
)
lacpCurPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpCurPortState.setStatus("current")


class _LacpCurPortActorPortPriority_Type(Integer32):
    """Custom type lacpCurPortActorPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LacpCurPortActorPortPriority_Type.__name__ = "Integer32"
_LacpCurPortActorPortPriority_Object = MibTableColumn
lacpCurPortActorPortPriority = _LacpCurPortActorPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 6, 7, 1, 3),
    _LacpCurPortActorPortPriority_Type()
)
lacpCurPortActorPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpCurPortActorPortPriority.setStatus("current")


class _LacpCurPortActorAdminKey_Type(Integer32):
    """Custom type lacpCurPortActorAdminKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LacpCurPortActorAdminKey_Type.__name__ = "Integer32"
_LacpCurPortActorAdminKey_Object = MibTableColumn
lacpCurPortActorAdminKey = _LacpCurPortActorAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 6, 7, 1, 4),
    _LacpCurPortActorAdminKey_Type()
)
lacpCurPortActorAdminKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpCurPortActorAdminKey.setStatus("current")
_LacpNewPortCfgTable_Object = MibTable
lacpNewPortCfgTable = _LacpNewPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 6, 8)
)
if mibBuilder.loadTexts:
    lacpNewPortCfgTable.setStatus("current")
_LacpNewPortCfgTableEntry_Object = MibTableRow
lacpNewPortCfgTableEntry = _LacpNewPortCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 6, 8, 1)
)
lacpNewPortCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "lacpNewPortCfgTableId"),
)
if mibBuilder.loadTexts:
    lacpNewPortCfgTableEntry.setStatus("current")
_LacpNewPortCfgTableId_Type = Integer32
_LacpNewPortCfgTableId_Object = MibTableColumn
lacpNewPortCfgTableId = _LacpNewPortCfgTableId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 6, 8, 1, 1),
    _LacpNewPortCfgTableId_Type()
)
lacpNewPortCfgTableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpNewPortCfgTableId.setStatus("current")


class _LacpNewPortState_Type(Integer32):
    """Custom type lacpNewPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("off", 1),
          ("passive", 3))
    )


_LacpNewPortState_Type.__name__ = "Integer32"
_LacpNewPortState_Object = MibTableColumn
lacpNewPortState = _LacpNewPortState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 6, 8, 1, 2),
    _LacpNewPortState_Type()
)
lacpNewPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpNewPortState.setStatus("current")


class _LacpNewPortActorPortPriority_Type(Integer32):
    """Custom type lacpNewPortActorPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LacpNewPortActorPortPriority_Type.__name__ = "Integer32"
_LacpNewPortActorPortPriority_Object = MibTableColumn
lacpNewPortActorPortPriority = _LacpNewPortActorPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 6, 8, 1, 3),
    _LacpNewPortActorPortPriority_Type()
)
lacpNewPortActorPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpNewPortActorPortPriority.setStatus("current")


class _LacpNewPortActorAdminKey_Type(Integer32):
    """Custom type lacpNewPortActorAdminKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LacpNewPortActorAdminKey_Type.__name__ = "Integer32"
_LacpNewPortActorAdminKey_Object = MibTableColumn
lacpNewPortActorAdminKey = _LacpNewPortActorAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 6, 8, 1, 4),
    _LacpNewPortActorAdminKey_Type()
)
lacpNewPortActorAdminKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpNewPortActorAdminKey.setStatus("current")
_Thash_ObjectIdentity = ObjectIdentity
thash = _Thash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 7)
)
_ThashL2_ObjectIdentity = ObjectIdentity
thashL2 = _ThashL2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 7, 1)
)


class _L2ThashCurCfgSmacState_Type(Integer32):
    """Custom type l2ThashCurCfgSmacState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_L2ThashCurCfgSmacState_Type.__name__ = "Integer32"
_L2ThashCurCfgSmacState_Object = MibScalar
l2ThashCurCfgSmacState = _L2ThashCurCfgSmacState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 7, 1, 1),
    _L2ThashCurCfgSmacState_Type()
)
l2ThashCurCfgSmacState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2ThashCurCfgSmacState.setStatus("current")


class _L2ThashNewCfgSmacState_Type(Integer32):
    """Custom type l2ThashNewCfgSmacState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_L2ThashNewCfgSmacState_Type.__name__ = "Integer32"
_L2ThashNewCfgSmacState_Object = MibScalar
l2ThashNewCfgSmacState = _L2ThashNewCfgSmacState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 7, 1, 2),
    _L2ThashNewCfgSmacState_Type()
)
l2ThashNewCfgSmacState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2ThashNewCfgSmacState.setStatus("current")


class _L2ThashCurCfgDmacState_Type(Integer32):
    """Custom type l2ThashCurCfgDmacState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_L2ThashCurCfgDmacState_Type.__name__ = "Integer32"
_L2ThashCurCfgDmacState_Object = MibScalar
l2ThashCurCfgDmacState = _L2ThashCurCfgDmacState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 7, 1, 3),
    _L2ThashCurCfgDmacState_Type()
)
l2ThashCurCfgDmacState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2ThashCurCfgDmacState.setStatus("current")


class _L2ThashNewCfgDmacState_Type(Integer32):
    """Custom type l2ThashNewCfgDmacState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_L2ThashNewCfgDmacState_Type.__name__ = "Integer32"
_L2ThashNewCfgDmacState_Object = MibScalar
l2ThashNewCfgDmacState = _L2ThashNewCfgDmacState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 7, 1, 4),
    _L2ThashNewCfgDmacState_Type()
)
l2ThashNewCfgDmacState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2ThashNewCfgDmacState.setStatus("current")


class _L2ThashCurCfgSipState_Type(Integer32):
    """Custom type l2ThashCurCfgSipState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_L2ThashCurCfgSipState_Type.__name__ = "Integer32"
_L2ThashCurCfgSipState_Object = MibScalar
l2ThashCurCfgSipState = _L2ThashCurCfgSipState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 7, 1, 5),
    _L2ThashCurCfgSipState_Type()
)
l2ThashCurCfgSipState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2ThashCurCfgSipState.setStatus("current")


class _L2ThashNewCfgSipState_Type(Integer32):
    """Custom type l2ThashNewCfgSipState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_L2ThashNewCfgSipState_Type.__name__ = "Integer32"
_L2ThashNewCfgSipState_Object = MibScalar
l2ThashNewCfgSipState = _L2ThashNewCfgSipState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 7, 1, 6),
    _L2ThashNewCfgSipState_Type()
)
l2ThashNewCfgSipState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2ThashNewCfgSipState.setStatus("current")


class _L2ThashCurCfgDipState_Type(Integer32):
    """Custom type l2ThashCurCfgDipState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_L2ThashCurCfgDipState_Type.__name__ = "Integer32"
_L2ThashCurCfgDipState_Object = MibScalar
l2ThashCurCfgDipState = _L2ThashCurCfgDipState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 7, 1, 7),
    _L2ThashCurCfgDipState_Type()
)
l2ThashCurCfgDipState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2ThashCurCfgDipState.setStatus("current")


class _L2ThashNewCfgDipState_Type(Integer32):
    """Custom type l2ThashNewCfgDipState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_L2ThashNewCfgDipState_Type.__name__ = "Integer32"
_L2ThashNewCfgDipState_Object = MibScalar
l2ThashNewCfgDipState = _L2ThashNewCfgDipState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 7, 1, 8),
    _L2ThashNewCfgDipState_Type()
)
l2ThashNewCfgDipState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2ThashNewCfgDipState.setStatus("current")
_L2GeneralCfg_ObjectIdentity = ObjectIdentity
l2GeneralCfg = _L2GeneralCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 8)
)


class _UpfastCurCfgState_Type(Integer32):
    """Custom type upfastCurCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UpfastCurCfgState_Type.__name__ = "Integer32"
_UpfastCurCfgState_Object = MibScalar
upfastCurCfgState = _UpfastCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 8, 1),
    _UpfastCurCfgState_Type()
)
upfastCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upfastCurCfgState.setStatus("current")


class _UpfastNewCfgState_Type(Integer32):
    """Custom type upfastNewCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UpfastNewCfgState_Type.__name__ = "Integer32"
_UpfastNewCfgState_Object = MibScalar
upfastNewCfgState = _UpfastNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 8, 2),
    _UpfastNewCfgState_Type()
)
upfastNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upfastNewCfgState.setStatus("current")


class _UpdateCurCfgState_Type(Integer32):
    """Custom type updateCurCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_UpdateCurCfgState_Type.__name__ = "Integer32"
_UpdateCurCfgState_Object = MibScalar
updateCurCfgState = _UpdateCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 8, 3),
    _UpdateCurCfgState_Type()
)
updateCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    updateCurCfgState.setStatus("current")


class _UpdateNewCfgState_Type(Integer32):
    """Custom type updateNewCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_UpdateNewCfgState_Type.__name__ = "Integer32"
_UpdateNewCfgState_Object = MibScalar
updateNewCfgState = _UpdateNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 8, 4),
    _UpdateNewCfgState_Type()
)
updateNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    updateNewCfgState.setStatus("current")
_Ufd_ObjectIdentity = ObjectIdentity
ufd = _Ufd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9)
)
_UfdGeneralCfg_ObjectIdentity = ObjectIdentity
ufdGeneralCfg = _UfdGeneralCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1)
)


class _UfdCurCfgState_Type(Integer32):
    """Custom type ufdCurCfgState based on Integer32"""
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


_UfdCurCfgState_Type.__name__ = "Integer32"
_UfdCurCfgState_Object = MibScalar
ufdCurCfgState = _UfdCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 1),
    _UfdCurCfgState_Type()
)
ufdCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdCurCfgState.setStatus("current")


class _UfdNewCfgState_Type(Integer32):
    """Custom type ufdNewCfgState based on Integer32"""
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


_UfdNewCfgState_Type.__name__ = "Integer32"
_UfdNewCfgState_Object = MibScalar
ufdNewCfgState = _UfdNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 2),
    _UfdNewCfgState_Type()
)
ufdNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdNewCfgState.setStatus("current")
_UfdCurCfgLtMPorts_Type = OctetString
_UfdCurCfgLtMPorts_Object = MibScalar
ufdCurCfgLtMPorts = _UfdCurCfgLtMPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 3),
    _UfdCurCfgLtMPorts_Type()
)
ufdCurCfgLtMPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdCurCfgLtMPorts.setStatus("current")
_UfdNewCfgLtMPorts_Type = OctetString
_UfdNewCfgLtMPorts_Object = MibScalar
ufdNewCfgLtMPorts = _UfdNewCfgLtMPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 4),
    _UfdNewCfgLtMPorts_Type()
)
ufdNewCfgLtMPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdNewCfgLtMPorts.setStatus("current")
_UfdCurCfgLtMTrunks_Type = OctetString
_UfdCurCfgLtMTrunks_Object = MibScalar
ufdCurCfgLtMTrunks = _UfdCurCfgLtMTrunks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 5),
    _UfdCurCfgLtMTrunks_Type()
)
ufdCurCfgLtMTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdCurCfgLtMTrunks.setStatus("current")
_UfdNewCfgLtMTrunks_Type = OctetString
_UfdNewCfgLtMTrunks_Object = MibScalar
ufdNewCfgLtMTrunks = _UfdNewCfgLtMTrunks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 6),
    _UfdNewCfgLtMTrunks_Type()
)
ufdNewCfgLtMTrunks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdNewCfgLtMTrunks.setStatus("current")
_UfdCurCfgLtDPorts_Type = OctetString
_UfdCurCfgLtDPorts_Object = MibScalar
ufdCurCfgLtDPorts = _UfdCurCfgLtDPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 7),
    _UfdCurCfgLtDPorts_Type()
)
ufdCurCfgLtDPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdCurCfgLtDPorts.setStatus("current")
_UfdNewCfgLtDPorts_Type = OctetString
_UfdNewCfgLtDPorts_Object = MibScalar
ufdNewCfgLtDPorts = _UfdNewCfgLtDPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 8),
    _UfdNewCfgLtDPorts_Type()
)
ufdNewCfgLtDPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdNewCfgLtDPorts.setStatus("current")
_UfdCurCfgLtDTrunks_Type = OctetString
_UfdCurCfgLtDTrunks_Object = MibScalar
ufdCurCfgLtDTrunks = _UfdCurCfgLtDTrunks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 9),
    _UfdCurCfgLtDTrunks_Type()
)
ufdCurCfgLtDTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdCurCfgLtDTrunks.setStatus("current")
_UfdNewCfgLtDTrunks_Type = OctetString
_UfdNewCfgLtDTrunks_Object = MibScalar
ufdNewCfgLtDTrunks = _UfdNewCfgLtDTrunks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 10),
    _UfdNewCfgLtDTrunks_Type()
)
ufdNewCfgLtDTrunks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdNewCfgLtDTrunks.setStatus("current")
_UfdNewCfgAddLtMPort_Type = Integer32
_UfdNewCfgAddLtMPort_Object = MibScalar
ufdNewCfgAddLtMPort = _UfdNewCfgAddLtMPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 11),
    _UfdNewCfgAddLtMPort_Type()
)
ufdNewCfgAddLtMPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdNewCfgAddLtMPort.setStatus("current")
_UfdNewCfgRemoveLtMPort_Type = Integer32
_UfdNewCfgRemoveLtMPort_Object = MibScalar
ufdNewCfgRemoveLtMPort = _UfdNewCfgRemoveLtMPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 12),
    _UfdNewCfgRemoveLtMPort_Type()
)
ufdNewCfgRemoveLtMPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdNewCfgRemoveLtMPort.setStatus("current")
_UfdNewCfgAddLtMTrunk_Type = Integer32
_UfdNewCfgAddLtMTrunk_Object = MibScalar
ufdNewCfgAddLtMTrunk = _UfdNewCfgAddLtMTrunk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 13),
    _UfdNewCfgAddLtMTrunk_Type()
)
ufdNewCfgAddLtMTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdNewCfgAddLtMTrunk.setStatus("current")
_UfdNewCfgRemoveLtMTrunk_Type = Integer32
_UfdNewCfgRemoveLtMTrunk_Object = MibScalar
ufdNewCfgRemoveLtMTrunk = _UfdNewCfgRemoveLtMTrunk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 14),
    _UfdNewCfgRemoveLtMTrunk_Type()
)
ufdNewCfgRemoveLtMTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdNewCfgRemoveLtMTrunk.setStatus("current")
_UfdNewCfgAddLtDPort_Type = Integer32
_UfdNewCfgAddLtDPort_Object = MibScalar
ufdNewCfgAddLtDPort = _UfdNewCfgAddLtDPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 15),
    _UfdNewCfgAddLtDPort_Type()
)
ufdNewCfgAddLtDPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdNewCfgAddLtDPort.setStatus("current")
_UfdNewCfgRemoveLtDPort_Type = Integer32
_UfdNewCfgRemoveLtDPort_Object = MibScalar
ufdNewCfgRemoveLtDPort = _UfdNewCfgRemoveLtDPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 16),
    _UfdNewCfgRemoveLtDPort_Type()
)
ufdNewCfgRemoveLtDPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdNewCfgRemoveLtDPort.setStatus("current")
_UfdNewCfgAddLtDTrunk_Type = Integer32
_UfdNewCfgAddLtDTrunk_Object = MibScalar
ufdNewCfgAddLtDTrunk = _UfdNewCfgAddLtDTrunk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 17),
    _UfdNewCfgAddLtDTrunk_Type()
)
ufdNewCfgAddLtDTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdNewCfgAddLtDTrunk.setStatus("current")
_UfdNewCfgRemoveLtDTrunk_Type = Integer32
_UfdNewCfgRemoveLtDTrunk_Object = MibScalar
ufdNewCfgRemoveLtDTrunk = _UfdNewCfgRemoveLtDTrunk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 18),
    _UfdNewCfgRemoveLtDTrunk_Type()
)
ufdNewCfgRemoveLtDTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdNewCfgRemoveLtDTrunk.setStatus("current")


class _UfdCurCfgGlobalState_Type(Integer32):
    """Custom type ufdCurCfgGlobalState based on Integer32"""
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


_UfdCurCfgGlobalState_Type.__name__ = "Integer32"
_UfdCurCfgGlobalState_Object = MibScalar
ufdCurCfgGlobalState = _UfdCurCfgGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 19),
    _UfdCurCfgGlobalState_Type()
)
ufdCurCfgGlobalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdCurCfgGlobalState.setStatus("current")


class _UfdNewCfgGlobalState_Type(Integer32):
    """Custom type ufdNewCfgGlobalState based on Integer32"""
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


_UfdNewCfgGlobalState_Type.__name__ = "Integer32"
_UfdNewCfgGlobalState_Object = MibScalar
ufdNewCfgGlobalState = _UfdNewCfgGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 9, 1, 20),
    _UfdNewCfgGlobalState_Type()
)
ufdNewCfgGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdNewCfgGlobalState.setStatus("current")
_Dot1x_ObjectIdentity = ObjectIdentity
dot1x = _Dot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11)
)


class _Dot1xCurStatus_Type(Integer32):
    """Custom type dot1xCurStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_Dot1xCurStatus_Type.__name__ = "Integer32"
_Dot1xCurStatus_Object = MibScalar
dot1xCurStatus = _Dot1xCurStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 1),
    _Dot1xCurStatus_Type()
)
dot1xCurStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xCurStatus.setStatus("current")


class _Dot1xNewStatus_Type(Integer32):
    """Custom type dot1xNewStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_Dot1xNewStatus_Type.__name__ = "Integer32"
_Dot1xNewStatus_Object = MibScalar
dot1xNewStatus = _Dot1xNewStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 2),
    _Dot1xNewStatus_Type()
)
dot1xNewStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xNewStatus.setStatus("current")
_Dot1xCurCfgPortTable_Object = MibTable
dot1xCurCfgPortTable = _Dot1xCurCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 3)
)
if mibBuilder.loadTexts:
    dot1xCurCfgPortTable.setStatus("current")
_Dot1xCurCfgPortEntry_Object = MibTableRow
dot1xCurCfgPortEntry = _Dot1xCurCfgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 3, 1)
)
dot1xCurCfgPortEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "dot1xCurCfgPortIndex"),
)
if mibBuilder.loadTexts:
    dot1xCurCfgPortEntry.setStatus("current")
_Dot1xCurCfgPortIndex_Type = Integer32
_Dot1xCurCfgPortIndex_Object = MibTableColumn
dot1xCurCfgPortIndex = _Dot1xCurCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 3, 1, 1),
    _Dot1xCurCfgPortIndex_Type()
)
dot1xCurCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xCurCfgPortIndex.setStatus("current")


class _Dot1xCurCfgPortMode_Type(Integer32):
    """Custom type dot1xCurCfgPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("forceAuth", 2),
          ("forceUnauth", 0))
    )


_Dot1xCurCfgPortMode_Type.__name__ = "Integer32"
_Dot1xCurCfgPortMode_Object = MibTableColumn
dot1xCurCfgPortMode = _Dot1xCurCfgPortMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 3, 1, 2),
    _Dot1xCurCfgPortMode_Type()
)
dot1xCurCfgPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xCurCfgPortMode.setStatus("current")


class _Dot1xCurCfgPortQtPeriod_Type(Integer32):
    """Custom type dot1xCurCfgPortQtPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1xCurCfgPortQtPeriod_Type.__name__ = "Integer32"
_Dot1xCurCfgPortQtPeriod_Object = MibTableColumn
dot1xCurCfgPortQtPeriod = _Dot1xCurCfgPortQtPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 3, 1, 3),
    _Dot1xCurCfgPortQtPeriod_Type()
)
dot1xCurCfgPortQtPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xCurCfgPortQtPeriod.setStatus("current")


class _Dot1xCurCfgPortTxPeriod_Type(Integer32):
    """Custom type dot1xCurCfgPortTxPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xCurCfgPortTxPeriod_Type.__name__ = "Integer32"
_Dot1xCurCfgPortTxPeriod_Object = MibTableColumn
dot1xCurCfgPortTxPeriod = _Dot1xCurCfgPortTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 3, 1, 4),
    _Dot1xCurCfgPortTxPeriod_Type()
)
dot1xCurCfgPortTxPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xCurCfgPortTxPeriod.setStatus("current")


class _Dot1xCurCfgPortSupTmout_Type(Integer32):
    """Custom type dot1xCurCfgPortSupTmout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xCurCfgPortSupTmout_Type.__name__ = "Integer32"
_Dot1xCurCfgPortSupTmout_Object = MibTableColumn
dot1xCurCfgPortSupTmout = _Dot1xCurCfgPortSupTmout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 3, 1, 5),
    _Dot1xCurCfgPortSupTmout_Type()
)
dot1xCurCfgPortSupTmout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xCurCfgPortSupTmout.setStatus("current")


class _Dot1xCurCfgPortSrvTmout_Type(Integer32):
    """Custom type dot1xCurCfgPortSrvTmout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xCurCfgPortSrvTmout_Type.__name__ = "Integer32"
_Dot1xCurCfgPortSrvTmout_Object = MibTableColumn
dot1xCurCfgPortSrvTmout = _Dot1xCurCfgPortSrvTmout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 3, 1, 6),
    _Dot1xCurCfgPortSrvTmout_Type()
)
dot1xCurCfgPortSrvTmout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xCurCfgPortSrvTmout.setStatus("current")


class _Dot1xCurCfgPortMaxRq_Type(Integer32):
    """Custom type dot1xCurCfgPortMaxRq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Dot1xCurCfgPortMaxRq_Type.__name__ = "Integer32"
_Dot1xCurCfgPortMaxRq_Object = MibTableColumn
dot1xCurCfgPortMaxRq = _Dot1xCurCfgPortMaxRq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 3, 1, 7),
    _Dot1xCurCfgPortMaxRq_Type()
)
dot1xCurCfgPortMaxRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xCurCfgPortMaxRq.setStatus("current")


class _Dot1xCurCfgPortRaPeriod_Type(Integer32):
    """Custom type dot1xCurCfgPortRaPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_Dot1xCurCfgPortRaPeriod_Type.__name__ = "Integer32"
_Dot1xCurCfgPortRaPeriod_Object = MibTableColumn
dot1xCurCfgPortRaPeriod = _Dot1xCurCfgPortRaPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 3, 1, 8),
    _Dot1xCurCfgPortRaPeriod_Type()
)
dot1xCurCfgPortRaPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xCurCfgPortRaPeriod.setStatus("current")


class _Dot1xCurCfgPortReAuth_Type(Integer32):
    """Custom type dot1xCurCfgPortReAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Dot1xCurCfgPortReAuth_Type.__name__ = "Integer32"
_Dot1xCurCfgPortReAuth_Object = MibTableColumn
dot1xCurCfgPortReAuth = _Dot1xCurCfgPortReAuth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 3, 1, 9),
    _Dot1xCurCfgPortReAuth_Type()
)
dot1xCurCfgPortReAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xCurCfgPortReAuth.setStatus("current")
_Dot1xNewCfgPortTable_Object = MibTable
dot1xNewCfgPortTable = _Dot1xNewCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 4)
)
if mibBuilder.loadTexts:
    dot1xNewCfgPortTable.setStatus("current")
_Dot1xNewCfgPortEntry_Object = MibTableRow
dot1xNewCfgPortEntry = _Dot1xNewCfgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 4, 1)
)
dot1xNewCfgPortEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "dot1xNewCfgPortIndex"),
)
if mibBuilder.loadTexts:
    dot1xNewCfgPortEntry.setStatus("current")
_Dot1xNewCfgPortIndex_Type = Integer32
_Dot1xNewCfgPortIndex_Object = MibTableColumn
dot1xNewCfgPortIndex = _Dot1xNewCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 4, 1, 1),
    _Dot1xNewCfgPortIndex_Type()
)
dot1xNewCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xNewCfgPortIndex.setStatus("current")


class _Dot1xNewCfgPortMode_Type(Integer32):
    """Custom type dot1xNewCfgPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("forceAuth", 2),
          ("forceUnauth", 0))
    )


_Dot1xNewCfgPortMode_Type.__name__ = "Integer32"
_Dot1xNewCfgPortMode_Object = MibTableColumn
dot1xNewCfgPortMode = _Dot1xNewCfgPortMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 4, 1, 2),
    _Dot1xNewCfgPortMode_Type()
)
dot1xNewCfgPortMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xNewCfgPortMode.setStatus("current")


class _Dot1xNewCfgPortQtPeriod_Type(Integer32):
    """Custom type dot1xNewCfgPortQtPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1xNewCfgPortQtPeriod_Type.__name__ = "Integer32"
_Dot1xNewCfgPortQtPeriod_Object = MibTableColumn
dot1xNewCfgPortQtPeriod = _Dot1xNewCfgPortQtPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 4, 1, 3),
    _Dot1xNewCfgPortQtPeriod_Type()
)
dot1xNewCfgPortQtPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xNewCfgPortQtPeriod.setStatus("current")


class _Dot1xNewCfgPortTxPeriod_Type(Integer32):
    """Custom type dot1xNewCfgPortTxPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xNewCfgPortTxPeriod_Type.__name__ = "Integer32"
_Dot1xNewCfgPortTxPeriod_Object = MibTableColumn
dot1xNewCfgPortTxPeriod = _Dot1xNewCfgPortTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 4, 1, 4),
    _Dot1xNewCfgPortTxPeriod_Type()
)
dot1xNewCfgPortTxPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xNewCfgPortTxPeriod.setStatus("current")


class _Dot1xNewCfgPortSupTmout_Type(Integer32):
    """Custom type dot1xNewCfgPortSupTmout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xNewCfgPortSupTmout_Type.__name__ = "Integer32"
_Dot1xNewCfgPortSupTmout_Object = MibTableColumn
dot1xNewCfgPortSupTmout = _Dot1xNewCfgPortSupTmout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 4, 1, 5),
    _Dot1xNewCfgPortSupTmout_Type()
)
dot1xNewCfgPortSupTmout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xNewCfgPortSupTmout.setStatus("current")


class _Dot1xNewCfgPortSrvTmout_Type(Integer32):
    """Custom type dot1xNewCfgPortSrvTmout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xNewCfgPortSrvTmout_Type.__name__ = "Integer32"
_Dot1xNewCfgPortSrvTmout_Object = MibTableColumn
dot1xNewCfgPortSrvTmout = _Dot1xNewCfgPortSrvTmout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 4, 1, 6),
    _Dot1xNewCfgPortSrvTmout_Type()
)
dot1xNewCfgPortSrvTmout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xNewCfgPortSrvTmout.setStatus("current")


class _Dot1xNewCfgPortMaxRq_Type(Integer32):
    """Custom type dot1xNewCfgPortMaxRq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Dot1xNewCfgPortMaxRq_Type.__name__ = "Integer32"
_Dot1xNewCfgPortMaxRq_Object = MibTableColumn
dot1xNewCfgPortMaxRq = _Dot1xNewCfgPortMaxRq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 4, 1, 7),
    _Dot1xNewCfgPortMaxRq_Type()
)
dot1xNewCfgPortMaxRq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xNewCfgPortMaxRq.setStatus("current")


class _Dot1xNewCfgPortRaPeriod_Type(Integer32):
    """Custom type dot1xNewCfgPortRaPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_Dot1xNewCfgPortRaPeriod_Type.__name__ = "Integer32"
_Dot1xNewCfgPortRaPeriod_Object = MibTableColumn
dot1xNewCfgPortRaPeriod = _Dot1xNewCfgPortRaPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 4, 1, 8),
    _Dot1xNewCfgPortRaPeriod_Type()
)
dot1xNewCfgPortRaPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xNewCfgPortRaPeriod.setStatus("current")


class _Dot1xNewCfgPortReAuth_Type(Integer32):
    """Custom type dot1xNewCfgPortReAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Dot1xNewCfgPortReAuth_Type.__name__ = "Integer32"
_Dot1xNewCfgPortReAuth_Object = MibTableColumn
dot1xNewCfgPortReAuth = _Dot1xNewCfgPortReAuth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 4, 1, 9),
    _Dot1xNewCfgPortReAuth_Type()
)
dot1xNewCfgPortReAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xNewCfgPortReAuth.setStatus("current")


class _Dot1xNewCfgPortDefault_Type(Integer32):
    """Custom type dot1xNewCfgPortDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("apply", 1),
          ("other", 0))
    )


_Dot1xNewCfgPortDefault_Type.__name__ = "Integer32"
_Dot1xNewCfgPortDefault_Object = MibTableColumn
dot1xNewCfgPortDefault = _Dot1xNewCfgPortDefault_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 4, 1, 10),
    _Dot1xNewCfgPortDefault_Type()
)
dot1xNewCfgPortDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xNewCfgPortDefault.setStatus("current")


class _Dot1xNewCfgPortApplyGlobal_Type(Integer32):
    """Custom type dot1xNewCfgPortApplyGlobal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("apply", 1),
          ("other", 0))
    )


_Dot1xNewCfgPortApplyGlobal_Type.__name__ = "Integer32"
_Dot1xNewCfgPortApplyGlobal_Object = MibTableColumn
dot1xNewCfgPortApplyGlobal = _Dot1xNewCfgPortApplyGlobal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 4, 1, 11),
    _Dot1xNewCfgPortApplyGlobal_Type()
)
dot1xNewCfgPortApplyGlobal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xNewCfgPortApplyGlobal.setStatus("current")
_Dot1xCurCfgGlobalTable_ObjectIdentity = ObjectIdentity
dot1xCurCfgGlobalTable = _Dot1xCurCfgGlobalTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 5)
)


class _Dot1xCurCfgGlobalMode_Type(Integer32):
    """Custom type dot1xCurCfgGlobalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("forceAuth", 2),
          ("forceUnauth", 0))
    )


_Dot1xCurCfgGlobalMode_Type.__name__ = "Integer32"
_Dot1xCurCfgGlobalMode_Object = MibScalar
dot1xCurCfgGlobalMode = _Dot1xCurCfgGlobalMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 5, 1),
    _Dot1xCurCfgGlobalMode_Type()
)
dot1xCurCfgGlobalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xCurCfgGlobalMode.setStatus("current")


class _Dot1xCurCfgGlobalQtPeriod_Type(Integer32):
    """Custom type dot1xCurCfgGlobalQtPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1xCurCfgGlobalQtPeriod_Type.__name__ = "Integer32"
_Dot1xCurCfgGlobalQtPeriod_Object = MibScalar
dot1xCurCfgGlobalQtPeriod = _Dot1xCurCfgGlobalQtPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 5, 2),
    _Dot1xCurCfgGlobalQtPeriod_Type()
)
dot1xCurCfgGlobalQtPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xCurCfgGlobalQtPeriod.setStatus("current")


class _Dot1xCurCfgGlobalTxPeriod_Type(Integer32):
    """Custom type dot1xCurCfgGlobalTxPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xCurCfgGlobalTxPeriod_Type.__name__ = "Integer32"
_Dot1xCurCfgGlobalTxPeriod_Object = MibScalar
dot1xCurCfgGlobalTxPeriod = _Dot1xCurCfgGlobalTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 5, 3),
    _Dot1xCurCfgGlobalTxPeriod_Type()
)
dot1xCurCfgGlobalTxPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xCurCfgGlobalTxPeriod.setStatus("current")


class _Dot1xCurCfgGlobalSupTmout_Type(Integer32):
    """Custom type dot1xCurCfgGlobalSupTmout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xCurCfgGlobalSupTmout_Type.__name__ = "Integer32"
_Dot1xCurCfgGlobalSupTmout_Object = MibScalar
dot1xCurCfgGlobalSupTmout = _Dot1xCurCfgGlobalSupTmout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 5, 4),
    _Dot1xCurCfgGlobalSupTmout_Type()
)
dot1xCurCfgGlobalSupTmout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xCurCfgGlobalSupTmout.setStatus("current")


class _Dot1xCurCfgGlobalSrvTmout_Type(Integer32):
    """Custom type dot1xCurCfgGlobalSrvTmout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xCurCfgGlobalSrvTmout_Type.__name__ = "Integer32"
_Dot1xCurCfgGlobalSrvTmout_Object = MibScalar
dot1xCurCfgGlobalSrvTmout = _Dot1xCurCfgGlobalSrvTmout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 5, 5),
    _Dot1xCurCfgGlobalSrvTmout_Type()
)
dot1xCurCfgGlobalSrvTmout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xCurCfgGlobalSrvTmout.setStatus("current")


class _Dot1xCurCfgGlobalMaxRq_Type(Integer32):
    """Custom type dot1xCurCfgGlobalMaxRq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Dot1xCurCfgGlobalMaxRq_Type.__name__ = "Integer32"
_Dot1xCurCfgGlobalMaxRq_Object = MibScalar
dot1xCurCfgGlobalMaxRq = _Dot1xCurCfgGlobalMaxRq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 5, 6),
    _Dot1xCurCfgGlobalMaxRq_Type()
)
dot1xCurCfgGlobalMaxRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xCurCfgGlobalMaxRq.setStatus("current")


class _Dot1xCurCfgGlobalRaPeriod_Type(Integer32):
    """Custom type dot1xCurCfgGlobalRaPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_Dot1xCurCfgGlobalRaPeriod_Type.__name__ = "Integer32"
_Dot1xCurCfgGlobalRaPeriod_Object = MibScalar
dot1xCurCfgGlobalRaPeriod = _Dot1xCurCfgGlobalRaPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 5, 7),
    _Dot1xCurCfgGlobalRaPeriod_Type()
)
dot1xCurCfgGlobalRaPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xCurCfgGlobalRaPeriod.setStatus("current")


class _Dot1xCurCfgGlobalReAuth_Type(Integer32):
    """Custom type dot1xCurCfgGlobalReAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Dot1xCurCfgGlobalReAuth_Type.__name__ = "Integer32"
_Dot1xCurCfgGlobalReAuth_Object = MibScalar
dot1xCurCfgGlobalReAuth = _Dot1xCurCfgGlobalReAuth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 5, 8),
    _Dot1xCurCfgGlobalReAuth_Type()
)
dot1xCurCfgGlobalReAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xCurCfgGlobalReAuth.setStatus("current")
_Dot1xNewCfgGlobalTable_ObjectIdentity = ObjectIdentity
dot1xNewCfgGlobalTable = _Dot1xNewCfgGlobalTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 6)
)


class _Dot1xNewCfgGlobalMode_Type(Integer32):
    """Custom type dot1xNewCfgGlobalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("forceAuth", 2),
          ("forceUnauth", 0))
    )


_Dot1xNewCfgGlobalMode_Type.__name__ = "Integer32"
_Dot1xNewCfgGlobalMode_Object = MibScalar
dot1xNewCfgGlobalMode = _Dot1xNewCfgGlobalMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 6, 1),
    _Dot1xNewCfgGlobalMode_Type()
)
dot1xNewCfgGlobalMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xNewCfgGlobalMode.setStatus("current")


class _Dot1xNewCfgGlobalQtPeriod_Type(Integer32):
    """Custom type dot1xNewCfgGlobalQtPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1xNewCfgGlobalQtPeriod_Type.__name__ = "Integer32"
_Dot1xNewCfgGlobalQtPeriod_Object = MibScalar
dot1xNewCfgGlobalQtPeriod = _Dot1xNewCfgGlobalQtPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 6, 2),
    _Dot1xNewCfgGlobalQtPeriod_Type()
)
dot1xNewCfgGlobalQtPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xNewCfgGlobalQtPeriod.setStatus("current")


class _Dot1xNewCfgGlobalTxPeriod_Type(Integer32):
    """Custom type dot1xNewCfgGlobalTxPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xNewCfgGlobalTxPeriod_Type.__name__ = "Integer32"
_Dot1xNewCfgGlobalTxPeriod_Object = MibScalar
dot1xNewCfgGlobalTxPeriod = _Dot1xNewCfgGlobalTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 6, 3),
    _Dot1xNewCfgGlobalTxPeriod_Type()
)
dot1xNewCfgGlobalTxPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xNewCfgGlobalTxPeriod.setStatus("current")


class _Dot1xNewCfgGlobalSupTmout_Type(Integer32):
    """Custom type dot1xNewCfgGlobalSupTmout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xNewCfgGlobalSupTmout_Type.__name__ = "Integer32"
_Dot1xNewCfgGlobalSupTmout_Object = MibScalar
dot1xNewCfgGlobalSupTmout = _Dot1xNewCfgGlobalSupTmout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 6, 4),
    _Dot1xNewCfgGlobalSupTmout_Type()
)
dot1xNewCfgGlobalSupTmout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xNewCfgGlobalSupTmout.setStatus("current")


class _Dot1xNewCfgGlobalSrvTmout_Type(Integer32):
    """Custom type dot1xNewCfgGlobalSrvTmout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xNewCfgGlobalSrvTmout_Type.__name__ = "Integer32"
_Dot1xNewCfgGlobalSrvTmout_Object = MibScalar
dot1xNewCfgGlobalSrvTmout = _Dot1xNewCfgGlobalSrvTmout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 6, 5),
    _Dot1xNewCfgGlobalSrvTmout_Type()
)
dot1xNewCfgGlobalSrvTmout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xNewCfgGlobalSrvTmout.setStatus("current")


class _Dot1xNewCfgGlobalMaxRq_Type(Integer32):
    """Custom type dot1xNewCfgGlobalMaxRq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Dot1xNewCfgGlobalMaxRq_Type.__name__ = "Integer32"
_Dot1xNewCfgGlobalMaxRq_Object = MibScalar
dot1xNewCfgGlobalMaxRq = _Dot1xNewCfgGlobalMaxRq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 6, 6),
    _Dot1xNewCfgGlobalMaxRq_Type()
)
dot1xNewCfgGlobalMaxRq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xNewCfgGlobalMaxRq.setStatus("current")


class _Dot1xNewCfgGlobalRaPeriod_Type(Integer32):
    """Custom type dot1xNewCfgGlobalRaPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_Dot1xNewCfgGlobalRaPeriod_Type.__name__ = "Integer32"
_Dot1xNewCfgGlobalRaPeriod_Object = MibScalar
dot1xNewCfgGlobalRaPeriod = _Dot1xNewCfgGlobalRaPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 6, 7),
    _Dot1xNewCfgGlobalRaPeriod_Type()
)
dot1xNewCfgGlobalRaPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xNewCfgGlobalRaPeriod.setStatus("current")


class _Dot1xNewCfgGlobalReAuth_Type(Integer32):
    """Custom type dot1xNewCfgGlobalReAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Dot1xNewCfgGlobalReAuth_Type.__name__ = "Integer32"
_Dot1xNewCfgGlobalReAuth_Object = MibScalar
dot1xNewCfgGlobalReAuth = _Dot1xNewCfgGlobalReAuth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 11, 6, 8),
    _Dot1xNewCfgGlobalReAuth_Type()
)
dot1xNewCfgGlobalReAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xNewCfgGlobalReAuth.setStatus("current")
_Fdb_ObjectIdentity = ObjectIdentity
fdb = _Fdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 12)
)
_FdbGeneralCfg_ObjectIdentity = ObjectIdentity
fdbGeneralCfg = _FdbGeneralCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 12, 1)
)
_FdbCurCfgAgingTime_Type = Integer32
_FdbCurCfgAgingTime_Object = MibScalar
fdbCurCfgAgingTime = _FdbCurCfgAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 12, 1, 1),
    _FdbCurCfgAgingTime_Type()
)
fdbCurCfgAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbCurCfgAgingTime.setStatus("current")
_FdbNewCfgAgingTime_Type = Integer32
_FdbNewCfgAgingTime_Object = MibScalar
fdbNewCfgAgingTime = _FdbNewCfgAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 12, 1, 2),
    _FdbNewCfgAgingTime_Type()
)
fdbNewCfgAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbNewCfgAgingTime.setStatus("current")
_FdbNewCfgStaticTable_Object = MibTable
fdbNewCfgStaticTable = _FdbNewCfgStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 12, 2)
)
if mibBuilder.loadTexts:
    fdbNewCfgStaticTable.setStatus("current")
_FdbNewCfgStaticEntry_Object = MibTableRow
fdbNewCfgStaticEntry = _FdbNewCfgStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 12, 2, 1)
)
fdbNewCfgStaticEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "fdbNewCfgEntryIndex"),
)
if mibBuilder.loadTexts:
    fdbNewCfgStaticEntry.setStatus("current")
_FdbNewCfgEntryIndex_Type = Integer32
_FdbNewCfgEntryIndex_Object = MibTableColumn
fdbNewCfgEntryIndex = _FdbNewCfgEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 12, 2, 1, 1),
    _FdbNewCfgEntryIndex_Type()
)
fdbNewCfgEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbNewCfgEntryIndex.setStatus("current")
_FdbNewCfgAddVlan_Type = Integer32
_FdbNewCfgAddVlan_Object = MibTableColumn
fdbNewCfgAddVlan = _FdbNewCfgAddVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 12, 2, 1, 2),
    _FdbNewCfgAddVlan_Type()
)
fdbNewCfgAddVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdbNewCfgAddVlan.setStatus("current")
_FdbNewCfgAddPort_Type = Integer32
_FdbNewCfgAddPort_Object = MibTableColumn
fdbNewCfgAddPort = _FdbNewCfgAddPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 12, 2, 1, 3),
    _FdbNewCfgAddPort_Type()
)
fdbNewCfgAddPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdbNewCfgAddPort.setStatus("current")
_FdbNewCfgAddMac_Type = PhysAddress
_FdbNewCfgAddMac_Object = MibTableColumn
fdbNewCfgAddMac = _FdbNewCfgAddMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 12, 2, 1, 4),
    _FdbNewCfgAddMac_Type()
)
fdbNewCfgAddMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdbNewCfgAddMac.setStatus("current")


class _FdbNewCfgDelStaticEntry_Type(Integer32):
    """Custom type fdbNewCfgDelStaticEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_FdbNewCfgDelStaticEntry_Type.__name__ = "Integer32"
_FdbNewCfgDelStaticEntry_Object = MibTableColumn
fdbNewCfgDelStaticEntry = _FdbNewCfgDelStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 12, 2, 1, 5),
    _FdbNewCfgDelStaticEntry_Type()
)
fdbNewCfgDelStaticEntry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdbNewCfgDelStaticEntry.setStatus("current")
_HotlinksCfg_ObjectIdentity = ObjectIdentity
hotlinksCfg = _HotlinksCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14)
)


class _HotlinksCurCfgOnState_Type(Integer32):
    """Custom type hotlinksCurCfgOnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_HotlinksCurCfgOnState_Type.__name__ = "Integer32"
_HotlinksCurCfgOnState_Object = MibScalar
hotlinksCurCfgOnState = _HotlinksCurCfgOnState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 1),
    _HotlinksCurCfgOnState_Type()
)
hotlinksCurCfgOnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksCurCfgOnState.setStatus("current")


class _HotlinksNewCfgOnState_Type(Integer32):
    """Custom type hotlinksNewCfgOnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_HotlinksNewCfgOnState_Type.__name__ = "Integer32"
_HotlinksNewCfgOnState_Object = MibScalar
hotlinksNewCfgOnState = _HotlinksNewCfgOnState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 2),
    _HotlinksNewCfgOnState_Type()
)
hotlinksNewCfgOnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hotlinksNewCfgOnState.setStatus("current")


class _HotlinksCurCfgFdbUpdateState_Type(Integer32):
    """Custom type hotlinksCurCfgFdbUpdateState based on Integer32"""
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


_HotlinksCurCfgFdbUpdateState_Type.__name__ = "Integer32"
_HotlinksCurCfgFdbUpdateState_Object = MibScalar
hotlinksCurCfgFdbUpdateState = _HotlinksCurCfgFdbUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 3),
    _HotlinksCurCfgFdbUpdateState_Type()
)
hotlinksCurCfgFdbUpdateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksCurCfgFdbUpdateState.setStatus("current")


class _HotlinksNewCfgFdbUpdateState_Type(Integer32):
    """Custom type hotlinksNewCfgFdbUpdateState based on Integer32"""
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


_HotlinksNewCfgFdbUpdateState_Type.__name__ = "Integer32"
_HotlinksNewCfgFdbUpdateState_Object = MibScalar
hotlinksNewCfgFdbUpdateState = _HotlinksNewCfgFdbUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 4),
    _HotlinksNewCfgFdbUpdateState_Type()
)
hotlinksNewCfgFdbUpdateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hotlinksNewCfgFdbUpdateState.setStatus("current")
_HotlinksMaxTriggerEntries_Type = Integer32
_HotlinksMaxTriggerEntries_Object = MibScalar
hotlinksMaxTriggerEntries = _HotlinksMaxTriggerEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 5),
    _HotlinksMaxTriggerEntries_Type()
)
hotlinksMaxTriggerEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksMaxTriggerEntries.setStatus("current")
_HotlinksCurCfgTriggerTable_Object = MibTable
hotlinksCurCfgTriggerTable = _HotlinksCurCfgTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 6)
)
if mibBuilder.loadTexts:
    hotlinksCurCfgTriggerTable.setStatus("current")
_HotlinksCurCfgTriggerTableEntry_Object = MibTableRow
hotlinksCurCfgTriggerTableEntry = _HotlinksCurCfgTriggerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 6, 1)
)
hotlinksCurCfgTriggerTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "hotlinksCurCfgTriggerId"),
)
if mibBuilder.loadTexts:
    hotlinksCurCfgTriggerTableEntry.setStatus("current")
_HotlinksCurCfgTriggerId_Type = Integer32
_HotlinksCurCfgTriggerId_Object = MibTableColumn
hotlinksCurCfgTriggerId = _HotlinksCurCfgTriggerId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 6, 1, 1),
    _HotlinksCurCfgTriggerId_Type()
)
hotlinksCurCfgTriggerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksCurCfgTriggerId.setStatus("current")


class _HotlinksCurCfgTriggerState_Type(Integer32):
    """Custom type hotlinksCurCfgTriggerState based on Integer32"""
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


_HotlinksCurCfgTriggerState_Type.__name__ = "Integer32"
_HotlinksCurCfgTriggerState_Object = MibTableColumn
hotlinksCurCfgTriggerState = _HotlinksCurCfgTriggerState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 6, 1, 2),
    _HotlinksCurCfgTriggerState_Type()
)
hotlinksCurCfgTriggerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksCurCfgTriggerState.setStatus("current")


class _HotlinksCurCfgTriggerPreemptState_Type(Integer32):
    """Custom type hotlinksCurCfgTriggerPreemptState based on Integer32"""
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


_HotlinksCurCfgTriggerPreemptState_Type.__name__ = "Integer32"
_HotlinksCurCfgTriggerPreemptState_Object = MibTableColumn
hotlinksCurCfgTriggerPreemptState = _HotlinksCurCfgTriggerPreemptState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 6, 1, 3),
    _HotlinksCurCfgTriggerPreemptState_Type()
)
hotlinksCurCfgTriggerPreemptState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksCurCfgTriggerPreemptState.setStatus("current")
_HotlinksCurCfgTriggerFdelay_Type = Integer32
_HotlinksCurCfgTriggerFdelay_Object = MibTableColumn
hotlinksCurCfgTriggerFdelay = _HotlinksCurCfgTriggerFdelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 6, 1, 4),
    _HotlinksCurCfgTriggerFdelay_Type()
)
hotlinksCurCfgTriggerFdelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksCurCfgTriggerFdelay.setStatus("current")
_HotlinksCurCfgTriggerMasterPort_Type = Integer32
_HotlinksCurCfgTriggerMasterPort_Object = MibTableColumn
hotlinksCurCfgTriggerMasterPort = _HotlinksCurCfgTriggerMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 6, 1, 5),
    _HotlinksCurCfgTriggerMasterPort_Type()
)
hotlinksCurCfgTriggerMasterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksCurCfgTriggerMasterPort.setStatus("current")
_HotlinksCurCfgTriggerMasterTrunk_Type = Integer32
_HotlinksCurCfgTriggerMasterTrunk_Object = MibTableColumn
hotlinksCurCfgTriggerMasterTrunk = _HotlinksCurCfgTriggerMasterTrunk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 6, 1, 6),
    _HotlinksCurCfgTriggerMasterTrunk_Type()
)
hotlinksCurCfgTriggerMasterTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksCurCfgTriggerMasterTrunk.setStatus("current")
_HotlinksCurCfgTriggerBackupPort_Type = Integer32
_HotlinksCurCfgTriggerBackupPort_Object = MibTableColumn
hotlinksCurCfgTriggerBackupPort = _HotlinksCurCfgTriggerBackupPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 6, 1, 7),
    _HotlinksCurCfgTriggerBackupPort_Type()
)
hotlinksCurCfgTriggerBackupPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksCurCfgTriggerBackupPort.setStatus("current")
_HotlinksCurCfgTriggerBackupTrunk_Type = Integer32
_HotlinksCurCfgTriggerBackupTrunk_Object = MibTableColumn
hotlinksCurCfgTriggerBackupTrunk = _HotlinksCurCfgTriggerBackupTrunk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 6, 1, 8),
    _HotlinksCurCfgTriggerBackupTrunk_Type()
)
hotlinksCurCfgTriggerBackupTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksCurCfgTriggerBackupTrunk.setStatus("current")
_HotlinksNewCfgTriggerTable_Object = MibTable
hotlinksNewCfgTriggerTable = _HotlinksNewCfgTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 7)
)
if mibBuilder.loadTexts:
    hotlinksNewCfgTriggerTable.setStatus("current")
_HotlinksNewCfgTriggerTableEntry_Object = MibTableRow
hotlinksNewCfgTriggerTableEntry = _HotlinksNewCfgTriggerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 7, 1)
)
hotlinksNewCfgTriggerTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "hotlinksNewCfgTriggerId"),
)
if mibBuilder.loadTexts:
    hotlinksNewCfgTriggerTableEntry.setStatus("current")
_HotlinksNewCfgTriggerId_Type = Integer32
_HotlinksNewCfgTriggerId_Object = MibTableColumn
hotlinksNewCfgTriggerId = _HotlinksNewCfgTriggerId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 7, 1, 1),
    _HotlinksNewCfgTriggerId_Type()
)
hotlinksNewCfgTriggerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksNewCfgTriggerId.setStatus("current")


class _HotlinksNewCfgTriggerState_Type(Integer32):
    """Custom type hotlinksNewCfgTriggerState based on Integer32"""
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


_HotlinksNewCfgTriggerState_Type.__name__ = "Integer32"
_HotlinksNewCfgTriggerState_Object = MibTableColumn
hotlinksNewCfgTriggerState = _HotlinksNewCfgTriggerState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 7, 1, 2),
    _HotlinksNewCfgTriggerState_Type()
)
hotlinksNewCfgTriggerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hotlinksNewCfgTriggerState.setStatus("current")


class _HotlinksNewCfgTriggerPreemptState_Type(Integer32):
    """Custom type hotlinksNewCfgTriggerPreemptState based on Integer32"""
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


_HotlinksNewCfgTriggerPreemptState_Type.__name__ = "Integer32"
_HotlinksNewCfgTriggerPreemptState_Object = MibTableColumn
hotlinksNewCfgTriggerPreemptState = _HotlinksNewCfgTriggerPreemptState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 7, 1, 3),
    _HotlinksNewCfgTriggerPreemptState_Type()
)
hotlinksNewCfgTriggerPreemptState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hotlinksNewCfgTriggerPreemptState.setStatus("current")
_HotlinksNewCfgTriggerFdelay_Type = Integer32
_HotlinksNewCfgTriggerFdelay_Object = MibTableColumn
hotlinksNewCfgTriggerFdelay = _HotlinksNewCfgTriggerFdelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 7, 1, 4),
    _HotlinksNewCfgTriggerFdelay_Type()
)
hotlinksNewCfgTriggerFdelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hotlinksNewCfgTriggerFdelay.setStatus("current")
_HotlinksNewCfgTriggerMasterPort_Type = Integer32
_HotlinksNewCfgTriggerMasterPort_Object = MibTableColumn
hotlinksNewCfgTriggerMasterPort = _HotlinksNewCfgTriggerMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 7, 1, 5),
    _HotlinksNewCfgTriggerMasterPort_Type()
)
hotlinksNewCfgTriggerMasterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hotlinksNewCfgTriggerMasterPort.setStatus("current")
_HotlinksNewCfgTriggerMasterTrunk_Type = Integer32
_HotlinksNewCfgTriggerMasterTrunk_Object = MibTableColumn
hotlinksNewCfgTriggerMasterTrunk = _HotlinksNewCfgTriggerMasterTrunk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 7, 1, 6),
    _HotlinksNewCfgTriggerMasterTrunk_Type()
)
hotlinksNewCfgTriggerMasterTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hotlinksNewCfgTriggerMasterTrunk.setStatus("current")
_HotlinksNewCfgTriggerBackupPort_Type = Integer32
_HotlinksNewCfgTriggerBackupPort_Object = MibTableColumn
hotlinksNewCfgTriggerBackupPort = _HotlinksNewCfgTriggerBackupPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 7, 1, 7),
    _HotlinksNewCfgTriggerBackupPort_Type()
)
hotlinksNewCfgTriggerBackupPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hotlinksNewCfgTriggerBackupPort.setStatus("current")
_HotlinksNewCfgTriggerBackupTrunk_Type = Integer32
_HotlinksNewCfgTriggerBackupTrunk_Object = MibTableColumn
hotlinksNewCfgTriggerBackupTrunk = _HotlinksNewCfgTriggerBackupTrunk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 1, 14, 7, 1, 8),
    _HotlinksNewCfgTriggerBackupTrunk_Type()
)
hotlinksNewCfgTriggerBackupTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hotlinksNewCfgTriggerBackupTrunk.setStatus("current")
_Layer2Stats_ObjectIdentity = ObjectIdentity
layer2Stats = _Layer2Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2)
)
_FdbStats_ObjectIdentity = ObjectIdentity
fdbStats = _FdbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 1)
)
_FdbStatsCreates_Type = Counter32
_FdbStatsCreates_Object = MibScalar
fdbStatsCreates = _FdbStatsCreates_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 1, 1),
    _FdbStatsCreates_Type()
)
fdbStatsCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsCreates.setStatus("current")
_FdbStatsDeletes_Type = Counter32
_FdbStatsDeletes_Object = MibScalar
fdbStatsDeletes = _FdbStatsDeletes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 1, 2),
    _FdbStatsDeletes_Type()
)
fdbStatsDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsDeletes.setStatus("current")
_FdbStatsCurrent_Type = Gauge32
_FdbStatsCurrent_Object = MibScalar
fdbStatsCurrent = _FdbStatsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 1, 3),
    _FdbStatsCurrent_Type()
)
fdbStatsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsCurrent.setStatus("current")
_FdbStatsHiwat_Type = Integer32
_FdbStatsHiwat_Object = MibScalar
fdbStatsHiwat = _FdbStatsHiwat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 1, 4),
    _FdbStatsHiwat_Type()
)
fdbStatsHiwat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsHiwat.setStatus("current")
_FdbStatsLookups_Type = Counter32
_FdbStatsLookups_Object = MibScalar
fdbStatsLookups = _FdbStatsLookups_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 1, 5),
    _FdbStatsLookups_Type()
)
fdbStatsLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsLookups.setStatus("current")
_FdbStatsLookupFails_Type = Counter32
_FdbStatsLookupFails_Object = MibScalar
fdbStatsLookupFails = _FdbStatsLookupFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 1, 6),
    _FdbStatsLookupFails_Type()
)
fdbStatsLookupFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsLookupFails.setStatus("current")
_FdbStatsFinds_Type = Counter32
_FdbStatsFinds_Object = MibScalar
fdbStatsFinds = _FdbStatsFinds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 1, 7),
    _FdbStatsFinds_Type()
)
fdbStatsFinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsFinds.setStatus("current")
_FdbStatsFindFails_Type = Counter32
_FdbStatsFindFails_Object = MibScalar
fdbStatsFindFails = _FdbStatsFindFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 1, 8),
    _FdbStatsFindFails_Type()
)
fdbStatsFindFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsFindFails.setStatus("current")
_FdbStatsFindOrCreates_Type = Counter32
_FdbStatsFindOrCreates_Object = MibScalar
fdbStatsFindOrCreates = _FdbStatsFindOrCreates_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 1, 9),
    _FdbStatsFindOrCreates_Type()
)
fdbStatsFindOrCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsFindOrCreates.setStatus("current")
_FdbStatsOverflows_Type = Counter32
_FdbStatsOverflows_Object = MibScalar
fdbStatsOverflows = _FdbStatsOverflows_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 1, 10),
    _FdbStatsOverflows_Type()
)
fdbStatsOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsOverflows.setStatus("current")
_StpStats_ObjectIdentity = ObjectIdentity
stpStats = _StpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 2)
)
_StgStatsPortTable_Object = MibTable
stgStatsPortTable = _StgStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    stgStatsPortTable.setStatus("current")
_StgStatsPortTableEntry_Object = MibTableRow
stgStatsPortTableEntry = _StgStatsPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 2, 1, 1)
)
stgStatsPortTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "stgStatsStpIndex"),
    (0, "BLADETYPE2-PHYSICAL-MIB", "stgStatsPortIndex"),
)
if mibBuilder.loadTexts:
    stgStatsPortTableEntry.setStatus("current")
_StgStatsStpIndex_Type = Integer32
_StgStatsStpIndex_Object = MibTableColumn
stgStatsStpIndex = _StgStatsStpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 2, 1, 1, 1),
    _StgStatsStpIndex_Type()
)
stgStatsStpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgStatsStpIndex.setStatus("current")
_StgStatsPortIndex_Type = Integer32
_StgStatsPortIndex_Object = MibTableColumn
stgStatsPortIndex = _StgStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 2, 1, 1, 2),
    _StgStatsPortIndex_Type()
)
stgStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgStatsPortIndex.setStatus("current")
_StgStatsPortRcvCfgBpdus_Type = Counter32
_StgStatsPortRcvCfgBpdus_Object = MibTableColumn
stgStatsPortRcvCfgBpdus = _StgStatsPortRcvCfgBpdus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 2, 1, 1, 3),
    _StgStatsPortRcvCfgBpdus_Type()
)
stgStatsPortRcvCfgBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgStatsPortRcvCfgBpdus.setStatus("current")
_StgStatsPortRcvTcnBpdus_Type = Counter32
_StgStatsPortRcvTcnBpdus_Object = MibTableColumn
stgStatsPortRcvTcnBpdus = _StgStatsPortRcvTcnBpdus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 2, 1, 1, 4),
    _StgStatsPortRcvTcnBpdus_Type()
)
stgStatsPortRcvTcnBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgStatsPortRcvTcnBpdus.setStatus("current")
_StgStatsPortXmtCfgBpdus_Type = Counter32
_StgStatsPortXmtCfgBpdus_Object = MibTableColumn
stgStatsPortXmtCfgBpdus = _StgStatsPortXmtCfgBpdus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 2, 1, 1, 5),
    _StgStatsPortXmtCfgBpdus_Type()
)
stgStatsPortXmtCfgBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgStatsPortXmtCfgBpdus.setStatus("current")
_StgStatsPortXmtTcnBpdus_Type = Counter32
_StgStatsPortXmtTcnBpdus_Object = MibTableColumn
stgStatsPortXmtTcnBpdus = _StgStatsPortXmtTcnBpdus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 2, 1, 1, 6),
    _StgStatsPortXmtTcnBpdus_Type()
)
stgStatsPortXmtTcnBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgStatsPortXmtTcnBpdus.setStatus("current")
_LacpStats_ObjectIdentity = ObjectIdentity
lacpStats = _LacpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 3)
)
_LacpStatsTable_Object = MibTable
lacpStatsTable = _LacpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    lacpStatsTable.setStatus("current")
_LacpStatsTableEntry_Object = MibTableRow
lacpStatsTableEntry = _LacpStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 3, 1, 1)
)
lacpStatsTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "lacpStatsIndex"),
)
if mibBuilder.loadTexts:
    lacpStatsTableEntry.setStatus("current")
_LacpStatsIndex_Type = Integer32
_LacpStatsIndex_Object = MibTableColumn
lacpStatsIndex = _LacpStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 3, 1, 1, 1),
    _LacpStatsIndex_Type()
)
lacpStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpStatsIndex.setStatus("current")
_LacpdusRx_Type = Integer32
_LacpdusRx_Object = MibTableColumn
lacpdusRx = _LacpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 3, 1, 1, 2),
    _LacpdusRx_Type()
)
lacpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpdusRx.setStatus("current")
_MarkerpdusRx_Type = Integer32
_MarkerpdusRx_Object = MibTableColumn
markerpdusRx = _MarkerpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 3, 1, 1, 3),
    _MarkerpdusRx_Type()
)
markerpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    markerpdusRx.setStatus("current")
_MarkerresponsepdusRx_Type = Integer32
_MarkerresponsepdusRx_Object = MibTableColumn
markerresponsepdusRx = _MarkerresponsepdusRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 3, 1, 1, 4),
    _MarkerresponsepdusRx_Type()
)
markerresponsepdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    markerresponsepdusRx.setStatus("current")
_UnknownRx_Type = Integer32
_UnknownRx_Object = MibTableColumn
unknownRx = _UnknownRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 3, 1, 1, 5),
    _UnknownRx_Type()
)
unknownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknownRx.setStatus("current")
_IllegalRx_Type = Integer32
_IllegalRx_Object = MibTableColumn
illegalRx = _IllegalRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 3, 1, 1, 6),
    _IllegalRx_Type()
)
illegalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    illegalRx.setStatus("current")
_LacpdusTx_Type = Integer32
_LacpdusTx_Object = MibTableColumn
lacpdusTx = _LacpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 3, 1, 1, 7),
    _LacpdusTx_Type()
)
lacpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpdusTx.setStatus("current")
_MarkerpdusTx_Type = Integer32
_MarkerpdusTx_Object = MibTableColumn
markerpdusTx = _MarkerpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 3, 1, 1, 8),
    _MarkerpdusTx_Type()
)
markerpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    markerpdusTx.setStatus("current")
_MarkerresponsepdusTx_Type = Integer32
_MarkerresponsepdusTx_Object = MibTableColumn
markerresponsepdusTx = _MarkerresponsepdusTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 3, 1, 1, 9),
    _MarkerresponsepdusTx_Type()
)
markerresponsepdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    markerresponsepdusTx.setStatus("current")
_UfdStats_ObjectIdentity = ObjectIdentity
ufdStats = _UfdStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 4)
)
_UfdNoLtMLinkFailure_Type = Integer32
_UfdNoLtMLinkFailure_Object = MibScalar
ufdNoLtMLinkFailure = _UfdNoLtMLinkFailure_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 4, 1),
    _UfdNoLtMLinkFailure_Type()
)
ufdNoLtMLinkFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdNoLtMLinkFailure.setStatus("current")
_UfdNoLtMLinkBlockingState_Type = Integer32
_UfdNoLtMLinkBlockingState_Object = MibScalar
ufdNoLtMLinkBlockingState = _UfdNoLtMLinkBlockingState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 4, 2),
    _UfdNoLtMLinkBlockingState_Type()
)
ufdNoLtMLinkBlockingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdNoLtMLinkBlockingState.setStatus("current")
_UfdNoLtDAutoDisabled_Type = Integer32
_UfdNoLtDAutoDisabled_Object = MibScalar
ufdNoLtDAutoDisabled = _UfdNoLtDAutoDisabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 4, 3),
    _UfdNoLtDAutoDisabled_Type()
)
ufdNoLtDAutoDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdNoLtDAutoDisabled.setStatus("current")
_HotlinksStats_ObjectIdentity = ObjectIdentity
hotlinksStats = _HotlinksStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 6)
)
_HotlinksStatsTriggerTable_Object = MibTable
hotlinksStatsTriggerTable = _HotlinksStatsTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    hotlinksStatsTriggerTable.setStatus("current")
_HotlinksStatsTriggerTableEntry_Object = MibTableRow
hotlinksStatsTriggerTableEntry = _HotlinksStatsTriggerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 6, 1, 1)
)
hotlinksStatsTriggerTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "hotlinksStatsTriggerId"),
)
if mibBuilder.loadTexts:
    hotlinksStatsTriggerTableEntry.setStatus("current")
_HotlinksStatsTriggerId_Type = Integer32
_HotlinksStatsTriggerId_Object = MibTableColumn
hotlinksStatsTriggerId = _HotlinksStatsTriggerId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 6, 1, 1, 1),
    _HotlinksStatsTriggerId_Type()
)
hotlinksStatsTriggerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksStatsTriggerId.setStatus("current")
_HotlinksStatsTriggerMasterActive_Type = Integer32
_HotlinksStatsTriggerMasterActive_Object = MibTableColumn
hotlinksStatsTriggerMasterActive = _HotlinksStatsTriggerMasterActive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 6, 1, 1, 2),
    _HotlinksStatsTriggerMasterActive_Type()
)
hotlinksStatsTriggerMasterActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksStatsTriggerMasterActive.setStatus("current")
_HotlinksStatsTriggerBackupActive_Type = Integer32
_HotlinksStatsTriggerBackupActive_Object = MibTableColumn
hotlinksStatsTriggerBackupActive = _HotlinksStatsTriggerBackupActive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 6, 1, 1, 3),
    _HotlinksStatsTriggerBackupActive_Type()
)
hotlinksStatsTriggerBackupActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksStatsTriggerBackupActive.setStatus("current")
_HotlinksStatsTriggerFdbUpdate_Type = Integer32
_HotlinksStatsTriggerFdbUpdate_Object = MibTableColumn
hotlinksStatsTriggerFdbUpdate = _HotlinksStatsTriggerFdbUpdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 6, 1, 1, 4),
    _HotlinksStatsTriggerFdbUpdate_Type()
)
hotlinksStatsTriggerFdbUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksStatsTriggerFdbUpdate.setStatus("current")
_HotlinksStatsTriggerFdbFailed_Type = Integer32
_HotlinksStatsTriggerFdbFailed_Object = MibTableColumn
hotlinksStatsTriggerFdbFailed = _HotlinksStatsTriggerFdbFailed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 2, 6, 1, 1, 5),
    _HotlinksStatsTriggerFdbFailed_Type()
)
hotlinksStatsTriggerFdbFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksStatsTriggerFdbFailed.setStatus("current")
_Layer2Info_ObjectIdentity = ObjectIdentity
layer2Info = _Layer2Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3)
)
_CistInfo_ObjectIdentity = ObjectIdentity
cistInfo = _CistInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1)
)
_CistGeneralInfo_ObjectIdentity = ObjectIdentity
cistGeneralInfo = _CistGeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 1)
)
_CistRoot_Type = BridgeId
_CistRoot_Object = MibScalar
cistRoot = _CistRoot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 1, 1),
    _CistRoot_Type()
)
cistRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistRoot.setStatus("current")
_CistRootPathCost_Type = Integer32
_CistRootPathCost_Object = MibScalar
cistRootPathCost = _CistRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 1, 2),
    _CistRootPathCost_Type()
)
cistRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistRootPathCost.setStatus("current")
_CistRootPort_Type = Integer32
_CistRootPort_Object = MibScalar
cistRootPort = _CistRootPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 1, 3),
    _CistRootPort_Type()
)
cistRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistRootPort.setStatus("current")
_CistRootHelloTime_Type = Integer32
_CistRootHelloTime_Object = MibScalar
cistRootHelloTime = _CistRootHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 1, 4),
    _CistRootHelloTime_Type()
)
cistRootHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistRootHelloTime.setStatus("current")
_CistRootMaxAge_Type = Integer32
_CistRootMaxAge_Object = MibScalar
cistRootMaxAge = _CistRootMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 1, 5),
    _CistRootMaxAge_Type()
)
cistRootMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistRootMaxAge.setStatus("current")
_CistRootForwardDelay_Type = Integer32
_CistRootForwardDelay_Object = MibScalar
cistRootForwardDelay = _CistRootForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 1, 6),
    _CistRootForwardDelay_Type()
)
cistRootForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistRootForwardDelay.setStatus("current")
_CistRegionalRoot_Type = BridgeId
_CistRegionalRoot_Object = MibScalar
cistRegionalRoot = _CistRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 1, 7),
    _CistRegionalRoot_Type()
)
cistRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistRegionalRoot.setStatus("current")
_CistRegionalPathCost_Type = Integer32
_CistRegionalPathCost_Object = MibScalar
cistRegionalPathCost = _CistRegionalPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 1, 8),
    _CistRegionalPathCost_Type()
)
cistRegionalPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistRegionalPathCost.setStatus("current")


class _CistBridgePriority_Type(Integer32):
    """Custom type cistBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CistBridgePriority_Type.__name__ = "Integer32"
_CistBridgePriority_Object = MibScalar
cistBridgePriority = _CistBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 1, 9),
    _CistBridgePriority_Type()
)
cistBridgePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistBridgePriority.setStatus("current")


class _CistBridgeMaxAge_Type(Integer32):
    """Custom type cistBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_CistBridgeMaxAge_Type.__name__ = "Integer32"
_CistBridgeMaxAge_Object = MibScalar
cistBridgeMaxAge = _CistBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 1, 10),
    _CistBridgeMaxAge_Type()
)
cistBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistBridgeMaxAge.setStatus("current")


class _CistBridgeForwardDelay_Type(Integer32):
    """Custom type cistBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_CistBridgeForwardDelay_Type.__name__ = "Integer32"
_CistBridgeForwardDelay_Object = MibScalar
cistBridgeForwardDelay = _CistBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 1, 11),
    _CistBridgeForwardDelay_Type()
)
cistBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistBridgeForwardDelay.setStatus("current")


class _CistMaxHopCount_Type(Integer32):
    """Custom type cistMaxHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_CistMaxHopCount_Type.__name__ = "Integer32"
_CistMaxHopCount_Object = MibScalar
cistMaxHopCount = _CistMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 1, 12),
    _CistMaxHopCount_Type()
)
cistMaxHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistMaxHopCount.setStatus("current")


class _MstpDigest_Type(DisplayString):
    """Custom type mstpDigest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MstpDigest_Type.__name__ = "DisplayString"
_MstpDigest_Object = MibScalar
mstpDigest = _MstpDigest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 1, 13),
    _MstpDigest_Type()
)
mstpDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpDigest.setStatus("current")
_CistInfoPortTable_Object = MibTable
cistInfoPortTable = _CistInfoPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cistInfoPortTable.setStatus("current")
_CistInfoPortTableEntry_Object = MibTableRow
cistInfoPortTableEntry = _CistInfoPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 2, 1)
)
cistInfoPortTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "cistInfoPortIndex"),
)
if mibBuilder.loadTexts:
    cistInfoPortTableEntry.setStatus("current")
_CistInfoPortIndex_Type = Integer32
_CistInfoPortIndex_Object = MibTableColumn
cistInfoPortIndex = _CistInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 2, 1, 1),
    _CistInfoPortIndex_Type()
)
cistInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistInfoPortIndex.setStatus("current")
_CistInfoPortPriority_Type = Integer32
_CistInfoPortPriority_Object = MibTableColumn
cistInfoPortPriority = _CistInfoPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 2, 1, 2),
    _CistInfoPortPriority_Type()
)
cistInfoPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistInfoPortPriority.setStatus("current")
_CistInfoPortPathCost_Type = Integer32
_CistInfoPortPathCost_Object = MibTableColumn
cistInfoPortPathCost = _CistInfoPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 2, 1, 3),
    _CistInfoPortPathCost_Type()
)
cistInfoPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistInfoPortPathCost.setStatus("current")


class _CistInfoPortState_Type(Integer32):
    """Custom type cistInfoPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discarding", 2),
          ("forwarding", 5),
          ("learning", 4))
    )


_CistInfoPortState_Type.__name__ = "Integer32"
_CistInfoPortState_Object = MibTableColumn
cistInfoPortState = _CistInfoPortState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 2, 1, 4),
    _CistInfoPortState_Type()
)
cistInfoPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistInfoPortState.setStatus("current")


class _CistInfoPortRole_Type(Integer32):
    """Custom type cistInfoPortRole based on Integer32"""
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
          ("master", 6),
          ("root", 4),
          ("unknown", 7))
    )


_CistInfoPortRole_Type.__name__ = "Integer32"
_CistInfoPortRole_Object = MibTableColumn
cistInfoPortRole = _CistInfoPortRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 2, 1, 5),
    _CistInfoPortRole_Type()
)
cistInfoPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistInfoPortRole.setStatus("current")
_CistInfoPortDesignatedBridge_Type = BridgeId
_CistInfoPortDesignatedBridge_Object = MibTableColumn
cistInfoPortDesignatedBridge = _CistInfoPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 2, 1, 6),
    _CistInfoPortDesignatedBridge_Type()
)
cistInfoPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistInfoPortDesignatedBridge.setStatus("current")


class _CistInfoPortDesignatedPort_Type(OctetString):
    """Custom type cistInfoPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CistInfoPortDesignatedPort_Type.__name__ = "OctetString"
_CistInfoPortDesignatedPort_Object = MibTableColumn
cistInfoPortDesignatedPort = _CistInfoPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 2, 1, 7),
    _CistInfoPortDesignatedPort_Type()
)
cistInfoPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistInfoPortDesignatedPort.setStatus("current")


class _CistInfoPortLinkType_Type(Integer32):
    """Custom type cistInfoPortLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("p2p", 1),
          ("shared", 2),
          ("unknown", 3))
    )


_CistInfoPortLinkType_Type.__name__ = "Integer32"
_CistInfoPortLinkType_Object = MibTableColumn
cistInfoPortLinkType = _CistInfoPortLinkType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 2, 1, 8),
    _CistInfoPortLinkType_Type()
)
cistInfoPortLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistInfoPortLinkType.setStatus("current")


class _CistInfoPortHelloTime_Type(Integer32):
    """Custom type cistInfoPortHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CistInfoPortHelloTime_Type.__name__ = "Integer32"
_CistInfoPortHelloTime_Object = MibTableColumn
cistInfoPortHelloTime = _CistInfoPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 1, 2, 1, 9),
    _CistInfoPortHelloTime_Type()
)
cistInfoPortHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistInfoPortHelloTime.setStatus("current")
_FdbInfo_ObjectIdentity = ObjectIdentity
fdbInfo = _FdbInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 2)
)


class _FdbClear_Type(Integer32):
    """Custom type fdbClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ok", 1))
    )


_FdbClear_Type.__name__ = "Integer32"
_FdbClear_Object = MibScalar
fdbClear = _FdbClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 2, 1),
    _FdbClear_Type()
)
fdbClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbClear.setStatus("current")
_FdbTable_Object = MibTable
fdbTable = _FdbTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    fdbTable.setStatus("current")
_FdbEntry_Object = MibTableRow
fdbEntry = _FdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 2, 2, 1)
)
fdbEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "fdbMacAddr"),
)
if mibBuilder.loadTexts:
    fdbEntry.setStatus("current")
_FdbMacAddr_Type = PhysAddress
_FdbMacAddr_Object = MibTableColumn
fdbMacAddr = _FdbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 2, 2, 1, 1),
    _FdbMacAddr_Type()
)
fdbMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbMacAddr.setStatus("current")
_FdbVlan_Type = Integer32
_FdbVlan_Object = MibTableColumn
fdbVlan = _FdbVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 2, 2, 1, 2),
    _FdbVlan_Type()
)
fdbVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbVlan.setStatus("current")
_FdbSrcPort_Type = Integer32
_FdbSrcPort_Object = MibTableColumn
fdbSrcPort = _FdbSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 2, 2, 1, 3),
    _FdbSrcPort_Type()
)
fdbSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbSrcPort.setStatus("current")


class _FdbState_Type(Integer32):
    """Custom type fdbState based on Integer32"""
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
        *(("ffd", 5),
          ("flood", 4),
          ("forward", 3),
          ("ignore", 2),
          ("other", 10),
          ("trunk", 6),
          ("unknown", 1),
          ("vir", 7),
          ("vpr", 9),
          ("vsr", 8))
    )


_FdbState_Type.__name__ = "Integer32"
_FdbState_Object = MibTableColumn
fdbState = _FdbState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 2, 2, 1, 4),
    _FdbState_Type()
)
fdbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbState.setStatus("current")


class _FdbRefSps_Type(DisplayString):
    """Custom type fdbRefSps based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FdbRefSps_Type.__name__ = "DisplayString"
_FdbRefSps_Object = MibTableColumn
fdbRefSps = _FdbRefSps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 2, 2, 1, 5),
    _FdbRefSps_Type()
)
fdbRefSps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbRefSps.setStatus("current")
_FdbLearnedPort_Type = Integer32
_FdbLearnedPort_Object = MibTableColumn
fdbLearnedPort = _FdbLearnedPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 2, 2, 1, 6),
    _FdbLearnedPort_Type()
)
fdbLearnedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbLearnedPort.setStatus("current")
_FdbSrcTrunk_Type = Integer32
_FdbSrcTrunk_Object = MibTableColumn
fdbSrcTrunk = _FdbSrcTrunk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 2, 2, 1, 7),
    _FdbSrcTrunk_Type()
)
fdbSrcTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbSrcTrunk.setStatus("current")
_StpInfo_ObjectIdentity = ObjectIdentity
stpInfo = _StpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3)
)
_StpInfoTable_Object = MibTable
stpInfoTable = _StpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    stpInfoTable.setStatus("current")
_StpInfoTableEntry_Object = MibTableRow
stpInfoTableEntry = _StpInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1, 1)
)
stpInfoTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "stpInfoIndex"),
)
if mibBuilder.loadTexts:
    stpInfoTableEntry.setStatus("current")
_StpInfoIndex_Type = Integer32
_StpInfoIndex_Object = MibTableColumn
stpInfoIndex = _StpInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1, 1, 1),
    _StpInfoIndex_Type()
)
stpInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoIndex.setStatus("current")


class _StpInfoState_Type(Integer32):
    """Custom type stpInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_StpInfoState_Type.__name__ = "Integer32"
_StpInfoState_Object = MibTableColumn
stpInfoState = _StpInfoState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1, 1, 2),
    _StpInfoState_Type()
)
stpInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoState.setStatus("current")


class _StgInfoVlanBmap_Type(OctetString):
    """Custom type stgInfoVlanBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_StgInfoVlanBmap_Type.__name__ = "OctetString"
_StgInfoVlanBmap_Object = MibTableColumn
stgInfoVlanBmap = _StgInfoVlanBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1, 1, 3),
    _StgInfoVlanBmap_Type()
)
stgInfoVlanBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgInfoVlanBmap.setStatus("current")
_StpInfoTimeSinceTopChange_Type = TimeTicks
_StpInfoTimeSinceTopChange_Object = MibTableColumn
stpInfoTimeSinceTopChange = _StpInfoTimeSinceTopChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1, 1, 4),
    _StpInfoTimeSinceTopChange_Type()
)
stpInfoTimeSinceTopChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoTimeSinceTopChange.setStatus("current")
_StpInfoTopChanges_Type = Counter32
_StpInfoTopChanges_Object = MibTableColumn
stpInfoTopChanges = _StpInfoTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1, 1, 5),
    _StpInfoTopChanges_Type()
)
stpInfoTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoTopChanges.setStatus("current")
_StpInfoDesignatedRoot_Type = BridgeId
_StpInfoDesignatedRoot_Object = MibTableColumn
stpInfoDesignatedRoot = _StpInfoDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1, 1, 6),
    _StpInfoDesignatedRoot_Type()
)
stpInfoDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoDesignatedRoot.setStatus("current")
_StpInfoRootCost_Type = Integer32
_StpInfoRootCost_Object = MibTableColumn
stpInfoRootCost = _StpInfoRootCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1, 1, 7),
    _StpInfoRootCost_Type()
)
stpInfoRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoRootCost.setStatus("current")
_StpInfoRootPort_Type = Integer32
_StpInfoRootPort_Object = MibTableColumn
stpInfoRootPort = _StpInfoRootPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1, 1, 8),
    _StpInfoRootPort_Type()
)
stpInfoRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoRootPort.setStatus("current")
_StpInfoMaxAge_Type = Integer32
_StpInfoMaxAge_Object = MibTableColumn
stpInfoMaxAge = _StpInfoMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1, 1, 9),
    _StpInfoMaxAge_Type()
)
stpInfoMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoMaxAge.setStatus("current")
_StpInfoHelloTime_Type = Integer32
_StpInfoHelloTime_Object = MibTableColumn
stpInfoHelloTime = _StpInfoHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1, 1, 10),
    _StpInfoHelloTime_Type()
)
stpInfoHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoHelloTime.setStatus("current")
_StpInfoForwardDelay_Type = Integer32
_StpInfoForwardDelay_Object = MibTableColumn
stpInfoForwardDelay = _StpInfoForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1, 1, 11),
    _StpInfoForwardDelay_Type()
)
stpInfoForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoForwardDelay.setStatus("current")
_StpInfoHoldTime_Type = Integer32
_StpInfoHoldTime_Object = MibTableColumn
stpInfoHoldTime = _StpInfoHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1, 1, 12),
    _StpInfoHoldTime_Type()
)
stpInfoHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoHoldTime.setStatus("current")


class _StpInfoBrgPriority_Type(Integer32):
    """Custom type stpInfoBrgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StpInfoBrgPriority_Type.__name__ = "Integer32"
_StpInfoBrgPriority_Object = MibTableColumn
stpInfoBrgPriority = _StpInfoBrgPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1, 1, 13),
    _StpInfoBrgPriority_Type()
)
stpInfoBrgPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoBrgPriority.setStatus("current")


class _StpInfoBrgHelloTime_Type(Integer32):
    """Custom type stpInfoBrgHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StpInfoBrgHelloTime_Type.__name__ = "Integer32"
_StpInfoBrgHelloTime_Object = MibTableColumn
stpInfoBrgHelloTime = _StpInfoBrgHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1, 1, 14),
    _StpInfoBrgHelloTime_Type()
)
stpInfoBrgHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoBrgHelloTime.setStatus("current")


class _StpInfoBrgForwardDelay_Type(Integer32):
    """Custom type stpInfoBrgForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_StpInfoBrgForwardDelay_Type.__name__ = "Integer32"
_StpInfoBrgForwardDelay_Object = MibTableColumn
stpInfoBrgForwardDelay = _StpInfoBrgForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1, 1, 15),
    _StpInfoBrgForwardDelay_Type()
)
stpInfoBrgForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoBrgForwardDelay.setStatus("current")


class _StpInfoBrgMaxAge_Type(Integer32):
    """Custom type stpInfoBrgMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_StpInfoBrgMaxAge_Type.__name__ = "Integer32"
_StpInfoBrgMaxAge_Object = MibTableColumn
stpInfoBrgMaxAge = _StpInfoBrgMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1, 1, 16),
    _StpInfoBrgMaxAge_Type()
)
stpInfoBrgMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoBrgMaxAge.setStatus("current")


class _StpInfoAgingTime_Type(Integer32):
    """Custom type stpInfoAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StpInfoAgingTime_Type.__name__ = "Integer32"
_StpInfoAgingTime_Object = MibTableColumn
stpInfoAgingTime = _StpInfoAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 1, 1, 17),
    _StpInfoAgingTime_Type()
)
stpInfoAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoAgingTime.setStatus("current")
_StpInfoPortTable_Object = MibTable
stpInfoPortTable = _StpInfoPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    stpInfoPortTable.setStatus("current")
_StpInfoPortTableEntry_Object = MibTableRow
stpInfoPortTableEntry = _StpInfoPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 2, 1)
)
stpInfoPortTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "stpInfoPortStpIndex"),
    (0, "BLADETYPE2-PHYSICAL-MIB", "stpInfoPortIndex"),
)
if mibBuilder.loadTexts:
    stpInfoPortTableEntry.setStatus("current")
_StpInfoPortStpIndex_Type = Integer32
_StpInfoPortStpIndex_Object = MibTableColumn
stpInfoPortStpIndex = _StpInfoPortStpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 2, 1, 1),
    _StpInfoPortStpIndex_Type()
)
stpInfoPortStpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortStpIndex.setStatus("current")
_StpInfoPortIndex_Type = Integer32
_StpInfoPortIndex_Object = MibTableColumn
stpInfoPortIndex = _StpInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 2, 1, 2),
    _StpInfoPortIndex_Type()
)
stpInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortIndex.setStatus("current")


class _StpInfoPortState_Type(Integer32):
    """Custom type stpInfoPortState based on Integer32"""
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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_StpInfoPortState_Type.__name__ = "Integer32"
_StpInfoPortState_Object = MibTableColumn
stpInfoPortState = _StpInfoPortState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 2, 1, 3),
    _StpInfoPortState_Type()
)
stpInfoPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortState.setStatus("current")
_StpInfoPortDesignatedRoot_Type = BridgeId
_StpInfoPortDesignatedRoot_Object = MibTableColumn
stpInfoPortDesignatedRoot = _StpInfoPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 2, 1, 4),
    _StpInfoPortDesignatedRoot_Type()
)
stpInfoPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortDesignatedRoot.setStatus("current")
_StpInfoPortDesignatedCost_Type = Integer32
_StpInfoPortDesignatedCost_Object = MibTableColumn
stpInfoPortDesignatedCost = _StpInfoPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 2, 1, 5),
    _StpInfoPortDesignatedCost_Type()
)
stpInfoPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortDesignatedCost.setStatus("current")
_StpInfoPortDesignatedBridge_Type = BridgeId
_StpInfoPortDesignatedBridge_Object = MibTableColumn
stpInfoPortDesignatedBridge = _StpInfoPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 2, 1, 6),
    _StpInfoPortDesignatedBridge_Type()
)
stpInfoPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortDesignatedBridge.setStatus("current")


class _StpInfoPortDesignatedPort_Type(OctetString):
    """Custom type stpInfoPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_StpInfoPortDesignatedPort_Type.__name__ = "OctetString"
_StpInfoPortDesignatedPort_Object = MibTableColumn
stpInfoPortDesignatedPort = _StpInfoPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 2, 1, 7),
    _StpInfoPortDesignatedPort_Type()
)
stpInfoPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortDesignatedPort.setStatus("current")
_StpInfoPortForwardTransitions_Type = Counter32
_StpInfoPortForwardTransitions_Object = MibTableColumn
stpInfoPortForwardTransitions = _StpInfoPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 2, 1, 8),
    _StpInfoPortForwardTransitions_Type()
)
stpInfoPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortForwardTransitions.setStatus("current")
_StpInfoPortPathCost_Type = Integer32
_StpInfoPortPathCost_Object = MibTableColumn
stpInfoPortPathCost = _StpInfoPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 3, 2, 1, 9),
    _StpInfoPortPathCost_Type()
)
stpInfoPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortPathCost.setStatus("current")
_LacpInfo_ObjectIdentity = ObjectIdentity
lacpInfo = _LacpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 4)
)
_LacpInfoPortTable_Object = MibTable
lacpInfoPortTable = _LacpInfoPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 4, 1)
)
if mibBuilder.loadTexts:
    lacpInfoPortTable.setStatus("current")
_LacpInfoPortTableEntry_Object = MibTableRow
lacpInfoPortTableEntry = _LacpInfoPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 4, 1, 1)
)
lacpInfoPortTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "lacpInfoPortIndex"),
)
if mibBuilder.loadTexts:
    lacpInfoPortTableEntry.setStatus("current")
_LacpInfoPortIndex_Type = Integer32
_LacpInfoPortIndex_Object = MibTableColumn
lacpInfoPortIndex = _LacpInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 4, 1, 1, 1),
    _LacpInfoPortIndex_Type()
)
lacpInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpInfoPortIndex.setStatus("current")


class _LacpInfoPortSelected_Type(Integer32):
    """Custom type lacpInfoPortSelected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("selected", 1),
          ("standby", 3),
          ("unselected", 2))
    )


_LacpInfoPortSelected_Type.__name__ = "Integer32"
_LacpInfoPortSelected_Object = MibTableColumn
lacpInfoPortSelected = _LacpInfoPortSelected_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 4, 1, 1, 2),
    _LacpInfoPortSelected_Type()
)
lacpInfoPortSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpInfoPortSelected.setStatus("current")


class _LacpInfoPortNtt_Type(Integer32):
    """Custom type lacpInfoPortNtt based on Integer32"""
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


_LacpInfoPortNtt_Type.__name__ = "Integer32"
_LacpInfoPortNtt_Object = MibTableColumn
lacpInfoPortNtt = _LacpInfoPortNtt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 4, 1, 1, 3),
    _LacpInfoPortNtt_Type()
)
lacpInfoPortNtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpInfoPortNtt.setStatus("current")


class _LacpInfoPortReadyN_Type(Integer32):
    """Custom type lacpInfoPortReadyN based on Integer32"""
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


_LacpInfoPortReadyN_Type.__name__ = "Integer32"
_LacpInfoPortReadyN_Object = MibTableColumn
lacpInfoPortReadyN = _LacpInfoPortReadyN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 4, 1, 1, 4),
    _LacpInfoPortReadyN_Type()
)
lacpInfoPortReadyN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpInfoPortReadyN.setStatus("current")


class _LacpInfoPortMoved_Type(Integer32):
    """Custom type lacpInfoPortMoved based on Integer32"""
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


_LacpInfoPortMoved_Type.__name__ = "Integer32"
_LacpInfoPortMoved_Object = MibTableColumn
lacpInfoPortMoved = _LacpInfoPortMoved_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 4, 1, 1, 5),
    _LacpInfoPortMoved_Type()
)
lacpInfoPortMoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpInfoPortMoved.setStatus("current")
_Dot1xInfo_ObjectIdentity = ObjectIdentity
dot1xInfo = _Dot1xInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 5)
)
_Dot1xInfoPortTable_Object = MibTable
dot1xInfoPortTable = _Dot1xInfoPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    dot1xInfoPortTable.setStatus("current")
_Dot1xInfoPortEntry_Object = MibTableRow
dot1xInfoPortEntry = _Dot1xInfoPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 5, 1, 1)
)
dot1xInfoPortEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "dot1xInfoPortIndex"),
)
if mibBuilder.loadTexts:
    dot1xInfoPortEntry.setStatus("current")
_Dot1xInfoPortIndex_Type = Integer32
_Dot1xInfoPortIndex_Object = MibTableColumn
dot1xInfoPortIndex = _Dot1xInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 5, 1, 1, 1),
    _Dot1xInfoPortIndex_Type()
)
dot1xInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInfoPortIndex.setStatus("current")


class _Dot1xInfoPortAuthMode_Type(Integer32):
    """Custom type dot1xInfoPortAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("forceAuth", 2),
          ("forceUnauth", 0))
    )


_Dot1xInfoPortAuthMode_Type.__name__ = "Integer32"
_Dot1xInfoPortAuthMode_Object = MibTableColumn
dot1xInfoPortAuthMode = _Dot1xInfoPortAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 5, 1, 1, 2),
    _Dot1xInfoPortAuthMode_Type()
)
dot1xInfoPortAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInfoPortAuthMode.setStatus("current")


class _Dot1xInfoPortAuthStatus_Type(Integer32):
    """Custom type dot1xInfoPortAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 0),
          ("unauthorized", 1))
    )


_Dot1xInfoPortAuthStatus_Type.__name__ = "Integer32"
_Dot1xInfoPortAuthStatus_Object = MibTableColumn
dot1xInfoPortAuthStatus = _Dot1xInfoPortAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 5, 1, 1, 3),
    _Dot1xInfoPortAuthStatus_Type()
)
dot1xInfoPortAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInfoPortAuthStatus.setStatus("current")


class _Dot1xInfoPortCtrlDir_Type(Integer32):
    """Custom type dot1xInfoPortCtrlDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("both", 0),
          ("in", 1))
    )


_Dot1xInfoPortCtrlDir_Type.__name__ = "Integer32"
_Dot1xInfoPortCtrlDir_Object = MibTableColumn
dot1xInfoPortCtrlDir = _Dot1xInfoPortCtrlDir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 5, 1, 1, 4),
    _Dot1xInfoPortCtrlDir_Type()
)
dot1xInfoPortCtrlDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInfoPortCtrlDir.setStatus("current")


class _Dot1xInfoPortAuthPAEState_Type(Integer32):
    """Custom type dot1xInfoPortAuthPAEState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("aborting", 5),
          ("authenticated", 4),
          ("authenticating", 3),
          ("connecting", 2),
          ("disconnected", 1),
          ("forceauth", 7),
          ("forceunauth", 8),
          ("held", 6),
          ("initialize", 0))
    )


_Dot1xInfoPortAuthPAEState_Type.__name__ = "Integer32"
_Dot1xInfoPortAuthPAEState_Object = MibTableColumn
dot1xInfoPortAuthPAEState = _Dot1xInfoPortAuthPAEState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 5, 1, 1, 5),
    _Dot1xInfoPortAuthPAEState_Type()
)
dot1xInfoPortAuthPAEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInfoPortAuthPAEState.setStatus("current")


class _Dot1xInfoPortBackAuthState_Type(Integer32):
    """Custom type dot1xInfoPortBackAuthState based on Integer32"""
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
        *(("fail", 3),
          ("idle", 5),
          ("initialize", 6),
          ("request", 0),
          ("response", 1),
          ("success", 2),
          ("timeout", 4))
    )


_Dot1xInfoPortBackAuthState_Type.__name__ = "Integer32"
_Dot1xInfoPortBackAuthState_Object = MibTableColumn
dot1xInfoPortBackAuthState = _Dot1xInfoPortBackAuthState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 5, 1, 1, 6),
    _Dot1xInfoPortBackAuthState_Type()
)
dot1xInfoPortBackAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xInfoPortBackAuthState.setStatus("current")
_Dot1xSystemInfo_ObjectIdentity = ObjectIdentity
dot1xSystemInfo = _Dot1xSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 5, 2)
)


class _Dot1xSystemCapability_Type(Integer32):
    """Custom type dot1xSystemCapability based on Integer32"""
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
        *(("authenticator", 0),
          ("authenticatorAndSupplicant", 2),
          ("supplicant", 1),
          ("unknown", 3))
    )


_Dot1xSystemCapability_Type.__name__ = "Integer32"
_Dot1xSystemCapability_Object = MibScalar
dot1xSystemCapability = _Dot1xSystemCapability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 5, 2, 1),
    _Dot1xSystemCapability_Type()
)
dot1xSystemCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xSystemCapability.setStatus("current")


class _Dot1xSystemStatus_Type(Integer32):
    """Custom type dot1xSystemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_Dot1xSystemStatus_Type.__name__ = "Integer32"
_Dot1xSystemStatus_Object = MibScalar
dot1xSystemStatus = _Dot1xSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 5, 2, 2),
    _Dot1xSystemStatus_Type()
)
dot1xSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xSystemStatus.setStatus("current")
_Dot1xSystemProtoVersion_Type = Integer32
_Dot1xSystemProtoVersion_Object = MibScalar
dot1xSystemProtoVersion = _Dot1xSystemProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 5, 2, 3),
    _Dot1xSystemProtoVersion_Type()
)
dot1xSystemProtoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xSystemProtoVersion.setStatus("current")
_Dot1pInfo_ObjectIdentity = ObjectIdentity
dot1pInfo = _Dot1pInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 6)
)
_Dot1pInfoPriorityCOSTable_Object = MibTable
dot1pInfoPriorityCOSTable = _Dot1pInfoPriorityCOSTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 6, 1)
)
if mibBuilder.loadTexts:
    dot1pInfoPriorityCOSTable.setStatus("current")
_Dot1pInfoPriorityCOSEntry_Object = MibTableRow
dot1pInfoPriorityCOSEntry = _Dot1pInfoPriorityCOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 6, 1, 1)
)
dot1pInfoPriorityCOSEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "dot1pInfoPriorityIndex"),
)
if mibBuilder.loadTexts:
    dot1pInfoPriorityCOSEntry.setStatus("current")


class _Dot1pInfoPriorityIndex_Type(Integer32):
    """Custom type dot1pInfoPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1pInfoPriorityIndex_Type.__name__ = "Integer32"
_Dot1pInfoPriorityIndex_Object = MibTableColumn
dot1pInfoPriorityIndex = _Dot1pInfoPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 6, 1, 1, 1),
    _Dot1pInfoPriorityIndex_Type()
)
dot1pInfoPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1pInfoPriorityIndex.setStatus("current")
_Dot1pInfoPriorityCOSQueue_Type = Integer32
_Dot1pInfoPriorityCOSQueue_Object = MibTableColumn
dot1pInfoPriorityCOSQueue = _Dot1pInfoPriorityCOSQueue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 6, 1, 1, 2),
    _Dot1pInfoPriorityCOSQueue_Type()
)
dot1pInfoPriorityCOSQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1pInfoPriorityCOSQueue.setStatus("current")
_Dot1pInfoPriorityCOSWeight_Type = Integer32
_Dot1pInfoPriorityCOSWeight_Object = MibTableColumn
dot1pInfoPriorityCOSWeight = _Dot1pInfoPriorityCOSWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 6, 1, 1, 3),
    _Dot1pInfoPriorityCOSWeight_Type()
)
dot1pInfoPriorityCOSWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1pInfoPriorityCOSWeight.setStatus("current")
_Dot1pInfoPortTable_Object = MibTable
dot1pInfoPortTable = _Dot1pInfoPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 6, 2)
)
if mibBuilder.loadTexts:
    dot1pInfoPortTable.setStatus("current")
_Dot1pInfoPortEntry_Object = MibTableRow
dot1pInfoPortEntry = _Dot1pInfoPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 6, 2, 1)
)
dot1pInfoPortEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "dot1pInfoPortIndex"),
)
if mibBuilder.loadTexts:
    dot1pInfoPortEntry.setStatus("current")
_Dot1pInfoPortIndex_Type = Integer32
_Dot1pInfoPortIndex_Object = MibTableColumn
dot1pInfoPortIndex = _Dot1pInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 6, 2, 1, 1),
    _Dot1pInfoPortIndex_Type()
)
dot1pInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1pInfoPortIndex.setStatus("current")
_Dot1pInfoPortPriority_Type = Integer32
_Dot1pInfoPortPriority_Object = MibTableColumn
dot1pInfoPortPriority = _Dot1pInfoPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 6, 2, 1, 2),
    _Dot1pInfoPortPriority_Type()
)
dot1pInfoPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1pInfoPortPriority.setStatus("current")
_Dot1pInfoPortCOSq_Type = Integer32
_Dot1pInfoPortCOSq_Object = MibTableColumn
dot1pInfoPortCOSq = _Dot1pInfoPortCOSq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 6, 2, 1, 3),
    _Dot1pInfoPortCOSq_Type()
)
dot1pInfoPortCOSq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1pInfoPortCOSq.setStatus("current")
_Dot1pInfoPortWeight_Type = Integer32
_Dot1pInfoPortWeight_Object = MibTableColumn
dot1pInfoPortWeight = _Dot1pInfoPortWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 6, 2, 1, 4),
    _Dot1pInfoPortWeight_Type()
)
dot1pInfoPortWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1pInfoPortWeight.setStatus("current")
_GenInfo_ObjectIdentity = ObjectIdentity
genInfo = _GenInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 7)
)


class _GeneralInfoStpUplinkFast_Type(Integer32):
    """Custom type generalInfoStpUplinkFast based on Integer32"""
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


_GeneralInfoStpUplinkFast_Type.__name__ = "Integer32"
_GeneralInfoStpUplinkFast_Object = MibScalar
generalInfoStpUplinkFast = _GeneralInfoStpUplinkFast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 7, 1),
    _GeneralInfoStpUplinkFast_Type()
)
generalInfoStpUplinkFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalInfoStpUplinkFast.setStatus("current")
_GeneralInfoUplinkFastRate_Type = Integer32
_GeneralInfoUplinkFastRate_Object = MibScalar
generalInfoUplinkFastRate = _GeneralInfoUplinkFastRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 7, 2),
    _GeneralInfoUplinkFastRate_Type()
)
generalInfoUplinkFastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalInfoUplinkFastRate.setStatus("current")
_VlanInfo_ObjectIdentity = ObjectIdentity
vlanInfo = _VlanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 8)
)
_VlanInfoTable_Object = MibTable
vlanInfoTable = _VlanInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 8, 1)
)
if mibBuilder.loadTexts:
    vlanInfoTable.setStatus("current")
_VlanInfoTableEntry_Object = MibTableRow
vlanInfoTableEntry = _VlanInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 8, 1, 1)
)
vlanInfoTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "vlanInfoId"),
)
if mibBuilder.loadTexts:
    vlanInfoTableEntry.setStatus("current")


class _VlanInfoId_Type(Integer32):
    """Custom type vlanInfoId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_VlanInfoId_Type.__name__ = "Integer32"
_VlanInfoId_Object = MibTableColumn
vlanInfoId = _VlanInfoId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 8, 1, 1, 1),
    _VlanInfoId_Type()
)
vlanInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanInfoId.setStatus("current")


class _VlanInfoName_Type(DisplayString):
    """Custom type vlanInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VlanInfoName_Type.__name__ = "DisplayString"
_VlanInfoName_Object = MibTableColumn
vlanInfoName = _VlanInfoName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 8, 1, 1, 2),
    _VlanInfoName_Type()
)
vlanInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanInfoName.setStatus("current")


class _VlanInfoStatus_Type(Integer32):
    """Custom type vlanInfoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_VlanInfoStatus_Type.__name__ = "Integer32"
_VlanInfoStatus_Object = MibTableColumn
vlanInfoStatus = _VlanInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 8, 1, 1, 3),
    _VlanInfoStatus_Type()
)
vlanInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanInfoStatus.setStatus("current")
_VlanInfoPorts_Type = OctetString
_VlanInfoPorts_Object = MibTableColumn
vlanInfoPorts = _VlanInfoPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 8, 1, 1, 4),
    _VlanInfoPorts_Type()
)
vlanInfoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanInfoPorts.setStatus("current")
_TrunkGroupInfo_ObjectIdentity = ObjectIdentity
trunkGroupInfo = _TrunkGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 9)
)
_TrunkGroupInfoTable_Object = MibTable
trunkGroupInfoTable = _TrunkGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 9, 1)
)
if mibBuilder.loadTexts:
    trunkGroupInfoTable.setStatus("current")
_TrunkGroupInfoTableEntry_Object = MibTableRow
trunkGroupInfoTableEntry = _TrunkGroupInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 9, 1, 1)
)
trunkGroupInfoTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "trunkGroupInfoIndex"),
)
if mibBuilder.loadTexts:
    trunkGroupInfoTableEntry.setStatus("current")
_TrunkGroupInfoIndex_Type = Integer32
_TrunkGroupInfoIndex_Object = MibTableColumn
trunkGroupInfoIndex = _TrunkGroupInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 9, 1, 1, 1),
    _TrunkGroupInfoIndex_Type()
)
trunkGroupInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupInfoIndex.setStatus("current")


class _TrunkGroupInfoState_Type(Integer32):
    """Custom type trunkGroupInfoState based on Integer32"""
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


_TrunkGroupInfoState_Type.__name__ = "Integer32"
_TrunkGroupInfoState_Object = MibTableColumn
trunkGroupInfoState = _TrunkGroupInfoState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 9, 1, 1, 2),
    _TrunkGroupInfoState_Type()
)
trunkGroupInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupInfoState.setStatus("current")
_TrunkGroupInfoPorts_Type = OctetString
_TrunkGroupInfoPorts_Object = MibTableColumn
trunkGroupInfoPorts = _TrunkGroupInfoPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 9, 1, 1, 3),
    _TrunkGroupInfoPorts_Type()
)
trunkGroupInfoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupInfoPorts.setStatus("current")
_HotlinksInfo_ObjectIdentity = ObjectIdentity
hotlinksInfo = _HotlinksInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 10)
)


class _HotlinksInfoOnState_Type(Integer32):
    """Custom type hotlinksInfoOnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_HotlinksInfoOnState_Type.__name__ = "Integer32"
_HotlinksInfoOnState_Object = MibScalar
hotlinksInfoOnState = _HotlinksInfoOnState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 10, 1),
    _HotlinksInfoOnState_Type()
)
hotlinksInfoOnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksInfoOnState.setStatus("current")


class _HotlinksInfoFdbUpdateState_Type(Integer32):
    """Custom type hotlinksInfoFdbUpdateState based on Integer32"""
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


_HotlinksInfoFdbUpdateState_Type.__name__ = "Integer32"
_HotlinksInfoFdbUpdateState_Object = MibScalar
hotlinksInfoFdbUpdateState = _HotlinksInfoFdbUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 10, 2),
    _HotlinksInfoFdbUpdateState_Type()
)
hotlinksInfoFdbUpdateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksInfoFdbUpdateState.setStatus("current")
_HotlinksInfoTriggerTable_Object = MibTable
hotlinksInfoTriggerTable = _HotlinksInfoTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 10, 3)
)
if mibBuilder.loadTexts:
    hotlinksInfoTriggerTable.setStatus("current")
_HotlinksInfoTriggerTableEntry_Object = MibTableRow
hotlinksInfoTriggerTableEntry = _HotlinksInfoTriggerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 10, 3, 1)
)
hotlinksInfoTriggerTableEntry.setIndexNames(
    (0, "BLADETYPE2-PHYSICAL-MIB", "hotlinksInfoTriggerId"),
)
if mibBuilder.loadTexts:
    hotlinksInfoTriggerTableEntry.setStatus("current")
_HotlinksInfoTriggerId_Type = Integer32
_HotlinksInfoTriggerId_Object = MibTableColumn
hotlinksInfoTriggerId = _HotlinksInfoTriggerId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 10, 3, 1, 1),
    _HotlinksInfoTriggerId_Type()
)
hotlinksInfoTriggerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksInfoTriggerId.setStatus("current")


class _HotlinksInfoTriggerState_Type(Integer32):
    """Custom type hotlinksInfoTriggerState based on Integer32"""
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


_HotlinksInfoTriggerState_Type.__name__ = "Integer32"
_HotlinksInfoTriggerState_Object = MibTableColumn
hotlinksInfoTriggerState = _HotlinksInfoTriggerState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 10, 3, 1, 2),
    _HotlinksInfoTriggerState_Type()
)
hotlinksInfoTriggerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksInfoTriggerState.setStatus("current")


class _HotlinksInfoTriggerPreemptState_Type(Integer32):
    """Custom type hotlinksInfoTriggerPreemptState based on Integer32"""
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


_HotlinksInfoTriggerPreemptState_Type.__name__ = "Integer32"
_HotlinksInfoTriggerPreemptState_Object = MibTableColumn
hotlinksInfoTriggerPreemptState = _HotlinksInfoTriggerPreemptState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 10, 3, 1, 3),
    _HotlinksInfoTriggerPreemptState_Type()
)
hotlinksInfoTriggerPreemptState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksInfoTriggerPreemptState.setStatus("current")
_HotlinksInfoTriggerFdelay_Type = Integer32
_HotlinksInfoTriggerFdelay_Object = MibTableColumn
hotlinksInfoTriggerFdelay = _HotlinksInfoTriggerFdelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 10, 3, 1, 4),
    _HotlinksInfoTriggerFdelay_Type()
)
hotlinksInfoTriggerFdelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksInfoTriggerFdelay.setStatus("current")
_HotlinksInfoTriggerActive_Type = DisplayString
_HotlinksInfoTriggerActive_Object = MibTableColumn
hotlinksInfoTriggerActive = _HotlinksInfoTriggerActive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 3, 10, 3, 1, 5),
    _HotlinksInfoTriggerActive_Type()
)
hotlinksInfoTriggerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hotlinksInfoTriggerActive.setStatus("current")
_Layer2Oper_ObjectIdentity = ObjectIdentity
layer2Oper = _Layer2Oper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 2, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLADETYPE2-PHYSICAL-MIB",
    **{"layer2": layer2,
       "layer2Configs": layer2Configs,
       "vlan": vlan,
       "vlanMaxEnt": vlanMaxEnt,
       "vlanCurCfgTable": vlanCurCfgTable,
       "vlanCurCfgTableEntry": vlanCurCfgTableEntry,
       "vlanCurCfgVlanId": vlanCurCfgVlanId,
       "vlanCurCfgVlanName": vlanCurCfgVlanName,
       "vlanCurCfgPorts": vlanCurCfgPorts,
       "vlanCurCfgState": vlanCurCfgState,
       "vlanCurCfgStg": vlanCurCfgStg,
       "vlanNewCfgTable": vlanNewCfgTable,
       "vlanNewCfgTableEntry": vlanNewCfgTableEntry,
       "vlanNewCfgVlanId": vlanNewCfgVlanId,
       "vlanNewCfgVlanName": vlanNewCfgVlanName,
       "vlanNewCfgPorts": vlanNewCfgPorts,
       "vlanNewCfgState": vlanNewCfgState,
       "vlanNewCfgAddPort": vlanNewCfgAddPort,
       "vlanNewCfgRemovePort": vlanNewCfgRemovePort,
       "vlanNewCfgDelete": vlanNewCfgDelete,
       "vlanNewCfgStg": vlanNewCfgStg,
       "trunkgroup": trunkgroup,
       "trunkGroupTableMaxSize": trunkGroupTableMaxSize,
       "trunkGroupCurCfgTable": trunkGroupCurCfgTable,
       "trunkGroupCurCfgTableEntry": trunkGroupCurCfgTableEntry,
       "trunkGroupCurCfgIndex": trunkGroupCurCfgIndex,
       "trunkGroupCurCfgPorts": trunkGroupCurCfgPorts,
       "trunkGroupCurCfgState": trunkGroupCurCfgState,
       "trunkGroupNewCfgTable": trunkGroupNewCfgTable,
       "trunkGroupNewCfgTableEntry": trunkGroupNewCfgTableEntry,
       "trunkGroupNewCfgIndex": trunkGroupNewCfgIndex,
       "trunkGroupNewCfgPorts": trunkGroupNewCfgPorts,
       "trunkGroupNewCfgAddPort": trunkGroupNewCfgAddPort,
       "trunkGroupNewCfgRemovePort": trunkGroupNewCfgRemovePort,
       "trunkGroupNewCfgState": trunkGroupNewCfgState,
       "trunkGroupNewCfgDelete": trunkGroupNewCfgDelete,
       "stgCfg": stgCfg,
       "stgCurCfgTable": stgCurCfgTable,
       "stgCurCfgTableEntry": stgCurCfgTableEntry,
       "stgCurCfgIndex": stgCurCfgIndex,
       "stgCurCfgState": stgCurCfgState,
       "stgCurCfgVlanBmap1": stgCurCfgVlanBmap1,
       "stgCurCfgVlanBmap2": stgCurCfgVlanBmap2,
       "stgCurCfgPriority": stgCurCfgPriority,
       "stgCurCfgBrgHelloTime": stgCurCfgBrgHelloTime,
       "stgCurCfgBrgForwardDelay": stgCurCfgBrgForwardDelay,
       "stgCurCfgBrgMaxAge": stgCurCfgBrgMaxAge,
       "stgCurCfgAgingTime": stgCurCfgAgingTime,
       "stgCurCfgVlanBmap": stgCurCfgVlanBmap,
       "stgNewCfgTable": stgNewCfgTable,
       "stgNewCfgTableEntry": stgNewCfgTableEntry,
       "stgNewCfgIndex": stgNewCfgIndex,
       "stgNewCfgState": stgNewCfgState,
       "stgNewCfgDefaultCfg": stgNewCfgDefaultCfg,
       "stgNewCfgAddVlan": stgNewCfgAddVlan,
       "stgNewCfgRemoveVlan": stgNewCfgRemoveVlan,
       "stgNewCfgVlanBmap1": stgNewCfgVlanBmap1,
       "stgNewCfgVlanBmap2": stgNewCfgVlanBmap2,
       "stgNewCfgPriority": stgNewCfgPriority,
       "stgNewCfgBrgHelloTime": stgNewCfgBrgHelloTime,
       "stgNewCfgBrgForwardDelay": stgNewCfgBrgForwardDelay,
       "stgNewCfgBrgMaxAge": stgNewCfgBrgMaxAge,
       "stgNewCfgAgingTime": stgNewCfgAgingTime,
       "stgNewCfgVlanBmap": stgNewCfgVlanBmap,
       "stgCurCfgPortTable": stgCurCfgPortTable,
       "stgCurCfgPortTableEntry": stgCurCfgPortTableEntry,
       "stgCurCfgStgIndex": stgCurCfgStgIndex,
       "stgCurCfgPortIndex": stgCurCfgPortIndex,
       "stgCurCfgPortState": stgCurCfgPortState,
       "stgCurCfgPortPriority": stgCurCfgPortPriority,
       "stgCurCfgPortPathCost": stgCurCfgPortPathCost,
       "stgCurCfgPortLink": stgCurCfgPortLink,
       "stgCurCfgPortEdge": stgCurCfgPortEdge,
       "stgCurCfgPortFastFwd": stgCurCfgPortFastFwd,
       "stgNewCfgPortTable": stgNewCfgPortTable,
       "stgNewCfgPortTableEntry": stgNewCfgPortTableEntry,
       "stgNewCfgStgIndex": stgNewCfgStgIndex,
       "stgNewCfgPortIndex": stgNewCfgPortIndex,
       "stgNewCfgPortState": stgNewCfgPortState,
       "stgNewCfgPortPriority": stgNewCfgPortPriority,
       "stgNewCfgPortPathCost": stgNewCfgPortPathCost,
       "stgNewCfgPortLink": stgNewCfgPortLink,
       "stgNewCfgPortEdge": stgNewCfgPortEdge,
       "stgNewCfgPortFastFwd": stgNewCfgPortFastFwd,
       "mirroring": mirroring,
       "mirrPortMirr": mirrPortMirr,
       "pmCurCfgPortMirrState": pmCurCfgPortMirrState,
       "pmNewCfgPortMirrState": pmNewCfgPortMirrState,
       "pmCurCfgPortMonitorTable": pmCurCfgPortMonitorTable,
       "pmCurCfgPortMonitorEntry": pmCurCfgPortMonitorEntry,
       "pmCurCfgPmirrMoniPortIndex": pmCurCfgPmirrMoniPortIndex,
       "pmCurCfgPmirrMirrPortIndex": pmCurCfgPmirrMirrPortIndex,
       "pmCurCfgPmirrDirection": pmCurCfgPmirrDirection,
       "pmNewCfgPortMonitorTable": pmNewCfgPortMonitorTable,
       "pmNewCfgPortMonitorEntry": pmNewCfgPortMonitorEntry,
       "pmNewCfgPmirrMoniPortIndex": pmNewCfgPmirrMoniPortIndex,
       "pmNewCfgPmirrMirrPortIndex": pmNewCfgPmirrMirrPortIndex,
       "pmNewCfgPmirrDirection": pmNewCfgPmirrDirection,
       "pmNewCfgPmirrDelete": pmNewCfgPmirrDelete,
       "pmNewCfgPmonDelete": pmNewCfgPmonDelete,
       "mstCfg": mstCfg,
       "mstGeneralCfg": mstGeneralCfg,
       "mstCurCfgState": mstCurCfgState,
       "mstNewCfgState": mstNewCfgState,
       "mstCurCfgRegionName": mstCurCfgRegionName,
       "mstNewCfgRegionName": mstNewCfgRegionName,
       "mstCurCfgRegionVersion": mstCurCfgRegionVersion,
       "mstNewCfgRegionVersion": mstNewCfgRegionVersion,
       "mstCurCfgMaxHopCount": mstCurCfgMaxHopCount,
       "mstNewCfgMaxHopCount": mstNewCfgMaxHopCount,
       "mstCurCfgStpMode": mstCurCfgStpMode,
       "mstNewCfgStpMode": mstNewCfgStpMode,
       "mstCistCfg": mstCistCfg,
       "mstCistDefaultCfg": mstCistDefaultCfg,
       "mstCistBridgeCfg": mstCistBridgeCfg,
       "mstCistCurCfgBridgePriority": mstCistCurCfgBridgePriority,
       "mstCistNewCfgBridgePriority": mstCistNewCfgBridgePriority,
       "mstCistCurCfgBridgeMaxAge": mstCistCurCfgBridgeMaxAge,
       "mstCistNewCfgBridgeMaxAge": mstCistNewCfgBridgeMaxAge,
       "mstCistCurCfgBridgeForwardDelay": mstCistCurCfgBridgeForwardDelay,
       "mstCistNewCfgBridgeForwardDelay": mstCistNewCfgBridgeForwardDelay,
       "mstCistCurCfgVlanBmap": mstCistCurCfgVlanBmap,
       "mstCistNewCfgVlanBmap": mstCistNewCfgVlanBmap,
       "mstCistNewCfgAddVlan": mstCistNewCfgAddVlan,
       "mstCistCurCfgPortTable": mstCistCurCfgPortTable,
       "mstCistCurCfgPortTableEntry": mstCistCurCfgPortTableEntry,
       "mstCistCurCfgPortIndex": mstCistCurCfgPortIndex,
       "mstCistCurCfgPortPriority": mstCistCurCfgPortPriority,
       "mstCistCurCfgPortPathCost": mstCistCurCfgPortPathCost,
       "mstCistCurCfgPortLinkType": mstCistCurCfgPortLinkType,
       "mstCistCurCfgPortEdge": mstCistCurCfgPortEdge,
       "mstCistCurCfgPortStpState": mstCistCurCfgPortStpState,
       "mstCistCurCfgPortHelloTime": mstCistCurCfgPortHelloTime,
       "mstCistNewCfgPortTable": mstCistNewCfgPortTable,
       "mstCistNewCfgPortTableEntry": mstCistNewCfgPortTableEntry,
       "mstCistNewCfgPortIndex": mstCistNewCfgPortIndex,
       "mstCistNewCfgPortPriority": mstCistNewCfgPortPriority,
       "mstCistNewCfgPortPathCost": mstCistNewCfgPortPathCost,
       "mstCistNewCfgPortLinkType": mstCistNewCfgPortLinkType,
       "mstCistNewCfgPortEdge": mstCistNewCfgPortEdge,
       "mstCistNewCfgPortStpState": mstCistNewCfgPortStpState,
       "mstCistNewCfgPortHelloTime": mstCistNewCfgPortHelloTime,
       "lacp": lacp,
       "lacpCurSystemPriority": lacpCurSystemPriority,
       "lacpNewSystemPriority": lacpNewSystemPriority,
       "lacpCurSystemTimeoutTime": lacpCurSystemTimeoutTime,
       "lacpNewSystemTimeoutTime": lacpNewSystemTimeoutTime,
       "lacpCurPortCfgTable": lacpCurPortCfgTable,
       "lacpCurPortCfgTableEntry": lacpCurPortCfgTableEntry,
       "lacpCurPortCfgTableId": lacpCurPortCfgTableId,
       "lacpCurPortState": lacpCurPortState,
       "lacpCurPortActorPortPriority": lacpCurPortActorPortPriority,
       "lacpCurPortActorAdminKey": lacpCurPortActorAdminKey,
       "lacpNewPortCfgTable": lacpNewPortCfgTable,
       "lacpNewPortCfgTableEntry": lacpNewPortCfgTableEntry,
       "lacpNewPortCfgTableId": lacpNewPortCfgTableId,
       "lacpNewPortState": lacpNewPortState,
       "lacpNewPortActorPortPriority": lacpNewPortActorPortPriority,
       "lacpNewPortActorAdminKey": lacpNewPortActorAdminKey,
       "thash": thash,
       "thashL2": thashL2,
       "l2ThashCurCfgSmacState": l2ThashCurCfgSmacState,
       "l2ThashNewCfgSmacState": l2ThashNewCfgSmacState,
       "l2ThashCurCfgDmacState": l2ThashCurCfgDmacState,
       "l2ThashNewCfgDmacState": l2ThashNewCfgDmacState,
       "l2ThashCurCfgSipState": l2ThashCurCfgSipState,
       "l2ThashNewCfgSipState": l2ThashNewCfgSipState,
       "l2ThashCurCfgDipState": l2ThashCurCfgDipState,
       "l2ThashNewCfgDipState": l2ThashNewCfgDipState,
       "l2GeneralCfg": l2GeneralCfg,
       "upfastCurCfgState": upfastCurCfgState,
       "upfastNewCfgState": upfastNewCfgState,
       "updateCurCfgState": updateCurCfgState,
       "updateNewCfgState": updateNewCfgState,
       "ufd": ufd,
       "ufdGeneralCfg": ufdGeneralCfg,
       "ufdCurCfgState": ufdCurCfgState,
       "ufdNewCfgState": ufdNewCfgState,
       "ufdCurCfgLtMPorts": ufdCurCfgLtMPorts,
       "ufdNewCfgLtMPorts": ufdNewCfgLtMPorts,
       "ufdCurCfgLtMTrunks": ufdCurCfgLtMTrunks,
       "ufdNewCfgLtMTrunks": ufdNewCfgLtMTrunks,
       "ufdCurCfgLtDPorts": ufdCurCfgLtDPorts,
       "ufdNewCfgLtDPorts": ufdNewCfgLtDPorts,
       "ufdCurCfgLtDTrunks": ufdCurCfgLtDTrunks,
       "ufdNewCfgLtDTrunks": ufdNewCfgLtDTrunks,
       "ufdNewCfgAddLtMPort": ufdNewCfgAddLtMPort,
       "ufdNewCfgRemoveLtMPort": ufdNewCfgRemoveLtMPort,
       "ufdNewCfgAddLtMTrunk": ufdNewCfgAddLtMTrunk,
       "ufdNewCfgRemoveLtMTrunk": ufdNewCfgRemoveLtMTrunk,
       "ufdNewCfgAddLtDPort": ufdNewCfgAddLtDPort,
       "ufdNewCfgRemoveLtDPort": ufdNewCfgRemoveLtDPort,
       "ufdNewCfgAddLtDTrunk": ufdNewCfgAddLtDTrunk,
       "ufdNewCfgRemoveLtDTrunk": ufdNewCfgRemoveLtDTrunk,
       "ufdCurCfgGlobalState": ufdCurCfgGlobalState,
       "ufdNewCfgGlobalState": ufdNewCfgGlobalState,
       "dot1x": dot1x,
       "dot1xCurStatus": dot1xCurStatus,
       "dot1xNewStatus": dot1xNewStatus,
       "dot1xCurCfgPortTable": dot1xCurCfgPortTable,
       "dot1xCurCfgPortEntry": dot1xCurCfgPortEntry,
       "dot1xCurCfgPortIndex": dot1xCurCfgPortIndex,
       "dot1xCurCfgPortMode": dot1xCurCfgPortMode,
       "dot1xCurCfgPortQtPeriod": dot1xCurCfgPortQtPeriod,
       "dot1xCurCfgPortTxPeriod": dot1xCurCfgPortTxPeriod,
       "dot1xCurCfgPortSupTmout": dot1xCurCfgPortSupTmout,
       "dot1xCurCfgPortSrvTmout": dot1xCurCfgPortSrvTmout,
       "dot1xCurCfgPortMaxRq": dot1xCurCfgPortMaxRq,
       "dot1xCurCfgPortRaPeriod": dot1xCurCfgPortRaPeriod,
       "dot1xCurCfgPortReAuth": dot1xCurCfgPortReAuth,
       "dot1xNewCfgPortTable": dot1xNewCfgPortTable,
       "dot1xNewCfgPortEntry": dot1xNewCfgPortEntry,
       "dot1xNewCfgPortIndex": dot1xNewCfgPortIndex,
       "dot1xNewCfgPortMode": dot1xNewCfgPortMode,
       "dot1xNewCfgPortQtPeriod": dot1xNewCfgPortQtPeriod,
       "dot1xNewCfgPortTxPeriod": dot1xNewCfgPortTxPeriod,
       "dot1xNewCfgPortSupTmout": dot1xNewCfgPortSupTmout,
       "dot1xNewCfgPortSrvTmout": dot1xNewCfgPortSrvTmout,
       "dot1xNewCfgPortMaxRq": dot1xNewCfgPortMaxRq,
       "dot1xNewCfgPortRaPeriod": dot1xNewCfgPortRaPeriod,
       "dot1xNewCfgPortReAuth": dot1xNewCfgPortReAuth,
       "dot1xNewCfgPortDefault": dot1xNewCfgPortDefault,
       "dot1xNewCfgPortApplyGlobal": dot1xNewCfgPortApplyGlobal,
       "dot1xCurCfgGlobalTable": dot1xCurCfgGlobalTable,
       "dot1xCurCfgGlobalMode": dot1xCurCfgGlobalMode,
       "dot1xCurCfgGlobalQtPeriod": dot1xCurCfgGlobalQtPeriod,
       "dot1xCurCfgGlobalTxPeriod": dot1xCurCfgGlobalTxPeriod,
       "dot1xCurCfgGlobalSupTmout": dot1xCurCfgGlobalSupTmout,
       "dot1xCurCfgGlobalSrvTmout": dot1xCurCfgGlobalSrvTmout,
       "dot1xCurCfgGlobalMaxRq": dot1xCurCfgGlobalMaxRq,
       "dot1xCurCfgGlobalRaPeriod": dot1xCurCfgGlobalRaPeriod,
       "dot1xCurCfgGlobalReAuth": dot1xCurCfgGlobalReAuth,
       "dot1xNewCfgGlobalTable": dot1xNewCfgGlobalTable,
       "dot1xNewCfgGlobalMode": dot1xNewCfgGlobalMode,
       "dot1xNewCfgGlobalQtPeriod": dot1xNewCfgGlobalQtPeriod,
       "dot1xNewCfgGlobalTxPeriod": dot1xNewCfgGlobalTxPeriod,
       "dot1xNewCfgGlobalSupTmout": dot1xNewCfgGlobalSupTmout,
       "dot1xNewCfgGlobalSrvTmout": dot1xNewCfgGlobalSrvTmout,
       "dot1xNewCfgGlobalMaxRq": dot1xNewCfgGlobalMaxRq,
       "dot1xNewCfgGlobalRaPeriod": dot1xNewCfgGlobalRaPeriod,
       "dot1xNewCfgGlobalReAuth": dot1xNewCfgGlobalReAuth,
       "fdb": fdb,
       "fdbGeneralCfg": fdbGeneralCfg,
       "fdbCurCfgAgingTime": fdbCurCfgAgingTime,
       "fdbNewCfgAgingTime": fdbNewCfgAgingTime,
       "fdbNewCfgStaticTable": fdbNewCfgStaticTable,
       "fdbNewCfgStaticEntry": fdbNewCfgStaticEntry,
       "fdbNewCfgEntryIndex": fdbNewCfgEntryIndex,
       "fdbNewCfgAddVlan": fdbNewCfgAddVlan,
       "fdbNewCfgAddPort": fdbNewCfgAddPort,
       "fdbNewCfgAddMac": fdbNewCfgAddMac,
       "fdbNewCfgDelStaticEntry": fdbNewCfgDelStaticEntry,
       "hotlinksCfg": hotlinksCfg,
       "hotlinksCurCfgOnState": hotlinksCurCfgOnState,
       "hotlinksNewCfgOnState": hotlinksNewCfgOnState,
       "hotlinksCurCfgFdbUpdateState": hotlinksCurCfgFdbUpdateState,
       "hotlinksNewCfgFdbUpdateState": hotlinksNewCfgFdbUpdateState,
       "hotlinksMaxTriggerEntries": hotlinksMaxTriggerEntries,
       "hotlinksCurCfgTriggerTable": hotlinksCurCfgTriggerTable,
       "hotlinksCurCfgTriggerTableEntry": hotlinksCurCfgTriggerTableEntry,
       "hotlinksCurCfgTriggerId": hotlinksCurCfgTriggerId,
       "hotlinksCurCfgTriggerState": hotlinksCurCfgTriggerState,
       "hotlinksCurCfgTriggerPreemptState": hotlinksCurCfgTriggerPreemptState,
       "hotlinksCurCfgTriggerFdelay": hotlinksCurCfgTriggerFdelay,
       "hotlinksCurCfgTriggerMasterPort": hotlinksCurCfgTriggerMasterPort,
       "hotlinksCurCfgTriggerMasterTrunk": hotlinksCurCfgTriggerMasterTrunk,
       "hotlinksCurCfgTriggerBackupPort": hotlinksCurCfgTriggerBackupPort,
       "hotlinksCurCfgTriggerBackupTrunk": hotlinksCurCfgTriggerBackupTrunk,
       "hotlinksNewCfgTriggerTable": hotlinksNewCfgTriggerTable,
       "hotlinksNewCfgTriggerTableEntry": hotlinksNewCfgTriggerTableEntry,
       "hotlinksNewCfgTriggerId": hotlinksNewCfgTriggerId,
       "hotlinksNewCfgTriggerState": hotlinksNewCfgTriggerState,
       "hotlinksNewCfgTriggerPreemptState": hotlinksNewCfgTriggerPreemptState,
       "hotlinksNewCfgTriggerFdelay": hotlinksNewCfgTriggerFdelay,
       "hotlinksNewCfgTriggerMasterPort": hotlinksNewCfgTriggerMasterPort,
       "hotlinksNewCfgTriggerMasterTrunk": hotlinksNewCfgTriggerMasterTrunk,
       "hotlinksNewCfgTriggerBackupPort": hotlinksNewCfgTriggerBackupPort,
       "hotlinksNewCfgTriggerBackupTrunk": hotlinksNewCfgTriggerBackupTrunk,
       "layer2Stats": layer2Stats,
       "fdbStats": fdbStats,
       "fdbStatsCreates": fdbStatsCreates,
       "fdbStatsDeletes": fdbStatsDeletes,
       "fdbStatsCurrent": fdbStatsCurrent,
       "fdbStatsHiwat": fdbStatsHiwat,
       "fdbStatsLookups": fdbStatsLookups,
       "fdbStatsLookupFails": fdbStatsLookupFails,
       "fdbStatsFinds": fdbStatsFinds,
       "fdbStatsFindFails": fdbStatsFindFails,
       "fdbStatsFindOrCreates": fdbStatsFindOrCreates,
       "fdbStatsOverflows": fdbStatsOverflows,
       "stpStats": stpStats,
       "stgStatsPortTable": stgStatsPortTable,
       "stgStatsPortTableEntry": stgStatsPortTableEntry,
       "stgStatsStpIndex": stgStatsStpIndex,
       "stgStatsPortIndex": stgStatsPortIndex,
       "stgStatsPortRcvCfgBpdus": stgStatsPortRcvCfgBpdus,
       "stgStatsPortRcvTcnBpdus": stgStatsPortRcvTcnBpdus,
       "stgStatsPortXmtCfgBpdus": stgStatsPortXmtCfgBpdus,
       "stgStatsPortXmtTcnBpdus": stgStatsPortXmtTcnBpdus,
       "lacpStats": lacpStats,
       "lacpStatsTable": lacpStatsTable,
       "lacpStatsTableEntry": lacpStatsTableEntry,
       "lacpStatsIndex": lacpStatsIndex,
       "lacpdusRx": lacpdusRx,
       "markerpdusRx": markerpdusRx,
       "markerresponsepdusRx": markerresponsepdusRx,
       "unknownRx": unknownRx,
       "illegalRx": illegalRx,
       "lacpdusTx": lacpdusTx,
       "markerpdusTx": markerpdusTx,
       "markerresponsepdusTx": markerresponsepdusTx,
       "ufdStats": ufdStats,
       "ufdNoLtMLinkFailure": ufdNoLtMLinkFailure,
       "ufdNoLtMLinkBlockingState": ufdNoLtMLinkBlockingState,
       "ufdNoLtDAutoDisabled": ufdNoLtDAutoDisabled,
       "hotlinksStats": hotlinksStats,
       "hotlinksStatsTriggerTable": hotlinksStatsTriggerTable,
       "hotlinksStatsTriggerTableEntry": hotlinksStatsTriggerTableEntry,
       "hotlinksStatsTriggerId": hotlinksStatsTriggerId,
       "hotlinksStatsTriggerMasterActive": hotlinksStatsTriggerMasterActive,
       "hotlinksStatsTriggerBackupActive": hotlinksStatsTriggerBackupActive,
       "hotlinksStatsTriggerFdbUpdate": hotlinksStatsTriggerFdbUpdate,
       "hotlinksStatsTriggerFdbFailed": hotlinksStatsTriggerFdbFailed,
       "layer2Info": layer2Info,
       "cistInfo": cistInfo,
       "cistGeneralInfo": cistGeneralInfo,
       "cistRoot": cistRoot,
       "cistRootPathCost": cistRootPathCost,
       "cistRootPort": cistRootPort,
       "cistRootHelloTime": cistRootHelloTime,
       "cistRootMaxAge": cistRootMaxAge,
       "cistRootForwardDelay": cistRootForwardDelay,
       "cistRegionalRoot": cistRegionalRoot,
       "cistRegionalPathCost": cistRegionalPathCost,
       "cistBridgePriority": cistBridgePriority,
       "cistBridgeMaxAge": cistBridgeMaxAge,
       "cistBridgeForwardDelay": cistBridgeForwardDelay,
       "cistMaxHopCount": cistMaxHopCount,
       "mstpDigest": mstpDigest,
       "cistInfoPortTable": cistInfoPortTable,
       "cistInfoPortTableEntry": cistInfoPortTableEntry,
       "cistInfoPortIndex": cistInfoPortIndex,
       "cistInfoPortPriority": cistInfoPortPriority,
       "cistInfoPortPathCost": cistInfoPortPathCost,
       "cistInfoPortState": cistInfoPortState,
       "cistInfoPortRole": cistInfoPortRole,
       "cistInfoPortDesignatedBridge": cistInfoPortDesignatedBridge,
       "cistInfoPortDesignatedPort": cistInfoPortDesignatedPort,
       "cistInfoPortLinkType": cistInfoPortLinkType,
       "cistInfoPortHelloTime": cistInfoPortHelloTime,
       "fdbInfo": fdbInfo,
       "fdbClear": fdbClear,
       "fdbTable": fdbTable,
       "fdbEntry": fdbEntry,
       "fdbMacAddr": fdbMacAddr,
       "fdbVlan": fdbVlan,
       "fdbSrcPort": fdbSrcPort,
       "fdbState": fdbState,
       "fdbRefSps": fdbRefSps,
       "fdbLearnedPort": fdbLearnedPort,
       "fdbSrcTrunk": fdbSrcTrunk,
       "stpInfo": stpInfo,
       "stpInfoTable": stpInfoTable,
       "stpInfoTableEntry": stpInfoTableEntry,
       "stpInfoIndex": stpInfoIndex,
       "stpInfoState": stpInfoState,
       "stgInfoVlanBmap": stgInfoVlanBmap,
       "stpInfoTimeSinceTopChange": stpInfoTimeSinceTopChange,
       "stpInfoTopChanges": stpInfoTopChanges,
       "stpInfoDesignatedRoot": stpInfoDesignatedRoot,
       "stpInfoRootCost": stpInfoRootCost,
       "stpInfoRootPort": stpInfoRootPort,
       "stpInfoMaxAge": stpInfoMaxAge,
       "stpInfoHelloTime": stpInfoHelloTime,
       "stpInfoForwardDelay": stpInfoForwardDelay,
       "stpInfoHoldTime": stpInfoHoldTime,
       "stpInfoBrgPriority": stpInfoBrgPriority,
       "stpInfoBrgHelloTime": stpInfoBrgHelloTime,
       "stpInfoBrgForwardDelay": stpInfoBrgForwardDelay,
       "stpInfoBrgMaxAge": stpInfoBrgMaxAge,
       "stpInfoAgingTime": stpInfoAgingTime,
       "stpInfoPortTable": stpInfoPortTable,
       "stpInfoPortTableEntry": stpInfoPortTableEntry,
       "stpInfoPortStpIndex": stpInfoPortStpIndex,
       "stpInfoPortIndex": stpInfoPortIndex,
       "stpInfoPortState": stpInfoPortState,
       "stpInfoPortDesignatedRoot": stpInfoPortDesignatedRoot,
       "stpInfoPortDesignatedCost": stpInfoPortDesignatedCost,
       "stpInfoPortDesignatedBridge": stpInfoPortDesignatedBridge,
       "stpInfoPortDesignatedPort": stpInfoPortDesignatedPort,
       "stpInfoPortForwardTransitions": stpInfoPortForwardTransitions,
       "stpInfoPortPathCost": stpInfoPortPathCost,
       "lacpInfo": lacpInfo,
       "lacpInfoPortTable": lacpInfoPortTable,
       "lacpInfoPortTableEntry": lacpInfoPortTableEntry,
       "lacpInfoPortIndex": lacpInfoPortIndex,
       "lacpInfoPortSelected": lacpInfoPortSelected,
       "lacpInfoPortNtt": lacpInfoPortNtt,
       "lacpInfoPortReadyN": lacpInfoPortReadyN,
       "lacpInfoPortMoved": lacpInfoPortMoved,
       "dot1xInfo": dot1xInfo,
       "dot1xInfoPortTable": dot1xInfoPortTable,
       "dot1xInfoPortEntry": dot1xInfoPortEntry,
       "dot1xInfoPortIndex": dot1xInfoPortIndex,
       "dot1xInfoPortAuthMode": dot1xInfoPortAuthMode,
       "dot1xInfoPortAuthStatus": dot1xInfoPortAuthStatus,
       "dot1xInfoPortCtrlDir": dot1xInfoPortCtrlDir,
       "dot1xInfoPortAuthPAEState": dot1xInfoPortAuthPAEState,
       "dot1xInfoPortBackAuthState": dot1xInfoPortBackAuthState,
       "dot1xSystemInfo": dot1xSystemInfo,
       "dot1xSystemCapability": dot1xSystemCapability,
       "dot1xSystemStatus": dot1xSystemStatus,
       "dot1xSystemProtoVersion": dot1xSystemProtoVersion,
       "dot1pInfo": dot1pInfo,
       "dot1pInfoPriorityCOSTable": dot1pInfoPriorityCOSTable,
       "dot1pInfoPriorityCOSEntry": dot1pInfoPriorityCOSEntry,
       "dot1pInfoPriorityIndex": dot1pInfoPriorityIndex,
       "dot1pInfoPriorityCOSQueue": dot1pInfoPriorityCOSQueue,
       "dot1pInfoPriorityCOSWeight": dot1pInfoPriorityCOSWeight,
       "dot1pInfoPortTable": dot1pInfoPortTable,
       "dot1pInfoPortEntry": dot1pInfoPortEntry,
       "dot1pInfoPortIndex": dot1pInfoPortIndex,
       "dot1pInfoPortPriority": dot1pInfoPortPriority,
       "dot1pInfoPortCOSq": dot1pInfoPortCOSq,
       "dot1pInfoPortWeight": dot1pInfoPortWeight,
       "genInfo": genInfo,
       "generalInfoStpUplinkFast": generalInfoStpUplinkFast,
       "generalInfoUplinkFastRate": generalInfoUplinkFastRate,
       "vlanInfo": vlanInfo,
       "vlanInfoTable": vlanInfoTable,
       "vlanInfoTableEntry": vlanInfoTableEntry,
       "vlanInfoId": vlanInfoId,
       "vlanInfoName": vlanInfoName,
       "vlanInfoStatus": vlanInfoStatus,
       "vlanInfoPorts": vlanInfoPorts,
       "trunkGroupInfo": trunkGroupInfo,
       "trunkGroupInfoTable": trunkGroupInfoTable,
       "trunkGroupInfoTableEntry": trunkGroupInfoTableEntry,
       "trunkGroupInfoIndex": trunkGroupInfoIndex,
       "trunkGroupInfoState": trunkGroupInfoState,
       "trunkGroupInfoPorts": trunkGroupInfoPorts,
       "hotlinksInfo": hotlinksInfo,
       "hotlinksInfoOnState": hotlinksInfoOnState,
       "hotlinksInfoFdbUpdateState": hotlinksInfoFdbUpdateState,
       "hotlinksInfoTriggerTable": hotlinksInfoTriggerTable,
       "hotlinksInfoTriggerTableEntry": hotlinksInfoTriggerTableEntry,
       "hotlinksInfoTriggerId": hotlinksInfoTriggerId,
       "hotlinksInfoTriggerState": hotlinksInfoTriggerState,
       "hotlinksInfoTriggerPreemptState": hotlinksInfoTriggerPreemptState,
       "hotlinksInfoTriggerFdelay": hotlinksInfoTriggerFdelay,
       "hotlinksInfoTriggerActive": hotlinksInfoTriggerActive,
       "layer2Oper": layer2Oper}
)

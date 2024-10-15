# SNMP MIB module (ALTEON-CS-PHYSICAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTEON-CS-PHYSICAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:53 2024
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

(aws_switch,) = mibBuilder.importSymbols(
    "ALTEON-ROOT-MIB",
    "aws-switch")

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2)
)
layer2.setRevisions(
        ("2009-08-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Layer2Configs_ObjectIdentity = ObjectIdentity
layer2Configs = _Layer2Configs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1)
)
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1)
)
_VlanMaxEnt_Type = Integer32
_VlanMaxEnt_Object = MibScalar
vlanMaxEnt = _VlanMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 1),
    _VlanMaxEnt_Type()
)
vlanMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMaxEnt.setStatus("current")
_VlanCurCfgTable_Object = MibTable
vlanCurCfgTable = _VlanCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vlanCurCfgTable.setStatus("current")
_VlanCurCfgTableEntry_Object = MibTableRow
vlanCurCfgTableEntry = _VlanCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1)
)
vlanCurCfgTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "vlanCurCfgVlanId"),
)
if mibBuilder.loadTexts:
    vlanCurCfgTableEntry.setStatus("current")
_VlanCurCfgVlanId_Type = Integer32
_VlanCurCfgVlanId_Object = MibTableColumn
vlanCurCfgVlanId = _VlanCurCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 2),
    _VlanCurCfgVlanName_Type()
)
vlanCurCfgVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgVlanName.setStatus("current")
_VlanCurCfgPorts_Type = OctetString
_VlanCurCfgPorts_Object = MibTableColumn
vlanCurCfgPorts = _VlanCurCfgPorts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 4),
    _VlanCurCfgState_Type()
)
vlanCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgState.setStatus("current")
_VlanCurCfgBwmContract_Type = Integer32
_VlanCurCfgBwmContract_Object = MibTableColumn
vlanCurCfgBwmContract = _VlanCurCfgBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 5),
    _VlanCurCfgBwmContract_Type()
)
vlanCurCfgBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgBwmContract.setStatus("current")
_VlanCurCfgStg_Type = Integer32
_VlanCurCfgStg_Object = MibTableColumn
vlanCurCfgStg = _VlanCurCfgStg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 6),
    _VlanCurCfgStg_Type()
)
vlanCurCfgStg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgStg.setStatus("current")


class _VlanCurCfgJumbo_Type(Integer32):
    """Custom type vlanCurCfgJumbo based on Integer32"""
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


_VlanCurCfgJumbo_Type.__name__ = "Integer32"
_VlanCurCfgJumbo_Object = MibTableColumn
vlanCurCfgJumbo = _VlanCurCfgJumbo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 7),
    _VlanCurCfgJumbo_Type()
)
vlanCurCfgJumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgJumbo.setStatus("current")


class _VlanCurCfgLearn_Type(Integer32):
    """Custom type vlanCurCfgLearn based on Integer32"""
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


_VlanCurCfgLearn_Type.__name__ = "Integer32"
_VlanCurCfgLearn_Object = MibTableColumn
vlanCurCfgLearn = _VlanCurCfgLearn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 8),
    _VlanCurCfgLearn_Type()
)
vlanCurCfgLearn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgLearn.setStatus("current")


class _VlanCurCfgShared_Type(Integer32):
    """Custom type vlanCurCfgShared based on Integer32"""
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


_VlanCurCfgShared_Type.__name__ = "Integer32"
_VlanCurCfgShared_Object = MibTableColumn
vlanCurCfgShared = _VlanCurCfgShared_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 9),
    _VlanCurCfgShared_Type()
)
vlanCurCfgShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgShared.setStatus("current")


class _VlanCurCfgIpv6LlaGen_Type(Integer32):
    """Custom type vlanCurCfgIpv6LlaGen based on Integer32"""
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


_VlanCurCfgIpv6LlaGen_Type.__name__ = "Integer32"
_VlanCurCfgIpv6LlaGen_Object = MibTableColumn
vlanCurCfgIpv6LlaGen = _VlanCurCfgIpv6LlaGen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 10),
    _VlanCurCfgIpv6LlaGen_Type()
)
vlanCurCfgIpv6LlaGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgIpv6LlaGen.setStatus("current")


class _VlanCurCfgRouterAdv_Type(Integer32):
    """Custom type vlanCurCfgRouterAdv based on Integer32"""
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


_VlanCurCfgRouterAdv_Type.__name__ = "Integer32"
_VlanCurCfgRouterAdv_Object = MibTableColumn
vlanCurCfgRouterAdv = _VlanCurCfgRouterAdv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 11),
    _VlanCurCfgRouterAdv_Type()
)
vlanCurCfgRouterAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgRouterAdv.setStatus("current")


class _VlanCurCfgReTransInt_Type(Unsigned32):
    """Custom type vlanCurCfgReTransInt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VlanCurCfgReTransInt_Type.__name__ = "Unsigned32"
_VlanCurCfgReTransInt_Object = MibTableColumn
vlanCurCfgReTransInt = _VlanCurCfgReTransInt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 12),
    _VlanCurCfgReTransInt_Type()
)
vlanCurCfgReTransInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgReTransInt.setStatus("current")


class _VlanCurCfgMinIntBwAdv_Type(Integer32):
    """Custom type vlanCurCfgMinIntBwAdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1800),
    )


_VlanCurCfgMinIntBwAdv_Type.__name__ = "Integer32"
_VlanCurCfgMinIntBwAdv_Object = MibTableColumn
vlanCurCfgMinIntBwAdv = _VlanCurCfgMinIntBwAdv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 13),
    _VlanCurCfgMinIntBwAdv_Type()
)
vlanCurCfgMinIntBwAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgMinIntBwAdv.setStatus("current")


class _VlanCurCfgMaxIntBwAdv_Type(Integer32):
    """Custom type vlanCurCfgMaxIntBwAdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_VlanCurCfgMaxIntBwAdv_Type.__name__ = "Integer32"
_VlanCurCfgMaxIntBwAdv_Object = MibTableColumn
vlanCurCfgMaxIntBwAdv = _VlanCurCfgMaxIntBwAdv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 14),
    _VlanCurCfgMaxIntBwAdv_Type()
)
vlanCurCfgMaxIntBwAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgMaxIntBwAdv.setStatus("current")


class _VlanCurCfgMtu_Type(Integer32):
    """Custom type vlanCurCfgMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 1500),
    )


_VlanCurCfgMtu_Type.__name__ = "Integer32"
_VlanCurCfgMtu_Object = MibTableColumn
vlanCurCfgMtu = _VlanCurCfgMtu_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 15),
    _VlanCurCfgMtu_Type()
)
vlanCurCfgMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgMtu.setStatus("current")


class _VlanCurCfgCurHopLimit_Type(Integer32):
    """Custom type vlanCurCfgCurHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VlanCurCfgCurHopLimit_Type.__name__ = "Integer32"
_VlanCurCfgCurHopLimit_Object = MibTableColumn
vlanCurCfgCurHopLimit = _VlanCurCfgCurHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 16),
    _VlanCurCfgCurHopLimit_Type()
)
vlanCurCfgCurHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgCurHopLimit.setStatus("current")


class _VlanCurCfgMFlag_Type(Integer32):
    """Custom type vlanCurCfgMFlag based on Integer32"""
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


_VlanCurCfgMFlag_Type.__name__ = "Integer32"
_VlanCurCfgMFlag_Object = MibTableColumn
vlanCurCfgMFlag = _VlanCurCfgMFlag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 17),
    _VlanCurCfgMFlag_Type()
)
vlanCurCfgMFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgMFlag.setStatus("current")


class _VlanCurCfgOFlag_Type(Integer32):
    """Custom type vlanCurCfgOFlag based on Integer32"""
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


_VlanCurCfgOFlag_Type.__name__ = "Integer32"
_VlanCurCfgOFlag_Object = MibTableColumn
vlanCurCfgOFlag = _VlanCurCfgOFlag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 18),
    _VlanCurCfgOFlag_Type()
)
vlanCurCfgOFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgOFlag.setStatus("current")


class _VlanCurCfgRTime_Type(Integer32):
    """Custom type vlanCurCfgRTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_VlanCurCfgRTime_Type.__name__ = "Integer32"
_VlanCurCfgRTime_Object = MibTableColumn
vlanCurCfgRTime = _VlanCurCfgRTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 19),
    _VlanCurCfgRTime_Type()
)
vlanCurCfgRTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgRTime.setStatus("current")


class _VlanCurCfgRlTime_Type(Integer32):
    """Custom type vlanCurCfgRlTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
    )


_VlanCurCfgRlTime_Type.__name__ = "Integer32"
_VlanCurCfgRlTime_Object = MibTableColumn
vlanCurCfgRlTime = _VlanCurCfgRlTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 20),
    _VlanCurCfgRlTime_Type()
)
vlanCurCfgRlTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgRlTime.setStatus("current")


class _VlanCurCfgPlTime_Type(Unsigned32):
    """Custom type vlanCurCfgPlTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VlanCurCfgPlTime_Type.__name__ = "Unsigned32"
_VlanCurCfgPlTime_Object = MibTableColumn
vlanCurCfgPlTime = _VlanCurCfgPlTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 21),
    _VlanCurCfgPlTime_Type()
)
vlanCurCfgPlTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgPlTime.setStatus("current")


class _VlanCurCfgVlTime_Type(Unsigned32):
    """Custom type vlanCurCfgVlTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VlanCurCfgVlTime_Type.__name__ = "Unsigned32"
_VlanCurCfgVlTime_Object = MibTableColumn
vlanCurCfgVlTime = _VlanCurCfgVlTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 22),
    _VlanCurCfgVlTime_Type()
)
vlanCurCfgVlTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgVlTime.setStatus("current")


class _VlanCurCfgOpInfo_Type(Integer32):
    """Custom type vlanCurCfgOpInfo based on Integer32"""
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


_VlanCurCfgOpInfo_Type.__name__ = "Integer32"
_VlanCurCfgOpInfo_Object = MibTableColumn
vlanCurCfgOpInfo = _VlanCurCfgOpInfo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 23),
    _VlanCurCfgOpInfo_Type()
)
vlanCurCfgOpInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgOpInfo.setStatus("current")


class _VlanCurCfgApInfo_Type(Integer32):
    """Custom type vlanCurCfgApInfo based on Integer32"""
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


_VlanCurCfgApInfo_Type.__name__ = "Integer32"
_VlanCurCfgApInfo_Object = MibTableColumn
vlanCurCfgApInfo = _VlanCurCfgApInfo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 2, 1, 24),
    _VlanCurCfgApInfo_Type()
)
vlanCurCfgApInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCurCfgApInfo.setStatus("current")
_VlanNewCfgTable_Object = MibTable
vlanNewCfgTable = _VlanNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    vlanNewCfgTable.setStatus("current")
_VlanNewCfgTableEntry_Object = MibTableRow
vlanNewCfgTableEntry = _VlanNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1)
)
vlanNewCfgTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "vlanNewCfgVlanId"),
)
if mibBuilder.loadTexts:
    vlanNewCfgTableEntry.setStatus("current")
_VlanNewCfgVlanId_Type = Integer32
_VlanNewCfgVlanId_Object = MibTableColumn
vlanNewCfgVlanId = _VlanNewCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 2),
    _VlanNewCfgVlanName_Type()
)
vlanNewCfgVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgVlanName.setStatus("current")
_VlanNewCfgPorts_Type = OctetString
_VlanNewCfgPorts_Object = MibTableColumn
vlanNewCfgPorts = _VlanNewCfgPorts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 4),
    _VlanNewCfgState_Type()
)
vlanNewCfgState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgState.setStatus("current")
_VlanNewCfgAddPort_Type = Integer32
_VlanNewCfgAddPort_Object = MibTableColumn
vlanNewCfgAddPort = _VlanNewCfgAddPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 5),
    _VlanNewCfgAddPort_Type()
)
vlanNewCfgAddPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgAddPort.setStatus("current")
_VlanNewCfgRemovePort_Type = Integer32
_VlanNewCfgRemovePort_Object = MibTableColumn
vlanNewCfgRemovePort = _VlanNewCfgRemovePort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 7),
    _VlanNewCfgDelete_Type()
)
vlanNewCfgDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgDelete.setStatus("current")
_VlanNewCfgBwmContract_Type = Integer32
_VlanNewCfgBwmContract_Object = MibTableColumn
vlanNewCfgBwmContract = _VlanNewCfgBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 8),
    _VlanNewCfgBwmContract_Type()
)
vlanNewCfgBwmContract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgBwmContract.setStatus("current")
_VlanNewCfgStg_Type = Integer32
_VlanNewCfgStg_Object = MibTableColumn
vlanNewCfgStg = _VlanNewCfgStg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 9),
    _VlanNewCfgStg_Type()
)
vlanNewCfgStg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgStg.setStatus("current")


class _VlanNewCfgJumbo_Type(Integer32):
    """Custom type vlanNewCfgJumbo based on Integer32"""
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


_VlanNewCfgJumbo_Type.__name__ = "Integer32"
_VlanNewCfgJumbo_Object = MibTableColumn
vlanNewCfgJumbo = _VlanNewCfgJumbo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 10),
    _VlanNewCfgJumbo_Type()
)
vlanNewCfgJumbo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgJumbo.setStatus("current")


class _VlanNewCfgLearn_Type(Integer32):
    """Custom type vlanNewCfgLearn based on Integer32"""
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


_VlanNewCfgLearn_Type.__name__ = "Integer32"
_VlanNewCfgLearn_Object = MibTableColumn
vlanNewCfgLearn = _VlanNewCfgLearn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 11),
    _VlanNewCfgLearn_Type()
)
vlanNewCfgLearn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgLearn.setStatus("current")


class _VlanNewCfgShared_Type(Integer32):
    """Custom type vlanNewCfgShared based on Integer32"""
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


_VlanNewCfgShared_Type.__name__ = "Integer32"
_VlanNewCfgShared_Object = MibTableColumn
vlanNewCfgShared = _VlanNewCfgShared_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 12),
    _VlanNewCfgShared_Type()
)
vlanNewCfgShared.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgShared.setStatus("current")


class _VlanNewCfgIpv6LlaGen_Type(Integer32):
    """Custom type vlanNewCfgIpv6LlaGen based on Integer32"""
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


_VlanNewCfgIpv6LlaGen_Type.__name__ = "Integer32"
_VlanNewCfgIpv6LlaGen_Object = MibTableColumn
vlanNewCfgIpv6LlaGen = _VlanNewCfgIpv6LlaGen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 13),
    _VlanNewCfgIpv6LlaGen_Type()
)
vlanNewCfgIpv6LlaGen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgIpv6LlaGen.setStatus("current")


class _VlanNewCfgRouterAdv_Type(Integer32):
    """Custom type vlanNewCfgRouterAdv based on Integer32"""
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


_VlanNewCfgRouterAdv_Type.__name__ = "Integer32"
_VlanNewCfgRouterAdv_Object = MibTableColumn
vlanNewCfgRouterAdv = _VlanNewCfgRouterAdv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 14),
    _VlanNewCfgRouterAdv_Type()
)
vlanNewCfgRouterAdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgRouterAdv.setStatus("current")


class _VlanNewCfgReTransInt_Type(Unsigned32):
    """Custom type vlanNewCfgReTransInt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VlanNewCfgReTransInt_Type.__name__ = "Unsigned32"
_VlanNewCfgReTransInt_Object = MibTableColumn
vlanNewCfgReTransInt = _VlanNewCfgReTransInt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 15),
    _VlanNewCfgReTransInt_Type()
)
vlanNewCfgReTransInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgReTransInt.setStatus("current")


class _VlanNewCfgMinIntBwAdv_Type(Integer32):
    """Custom type vlanNewCfgMinIntBwAdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1800),
    )


_VlanNewCfgMinIntBwAdv_Type.__name__ = "Integer32"
_VlanNewCfgMinIntBwAdv_Object = MibTableColumn
vlanNewCfgMinIntBwAdv = _VlanNewCfgMinIntBwAdv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 16),
    _VlanNewCfgMinIntBwAdv_Type()
)
vlanNewCfgMinIntBwAdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgMinIntBwAdv.setStatus("current")


class _VlanNewCfgMaxIntBwAdv_Type(Integer32):
    """Custom type vlanNewCfgMaxIntBwAdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_VlanNewCfgMaxIntBwAdv_Type.__name__ = "Integer32"
_VlanNewCfgMaxIntBwAdv_Object = MibTableColumn
vlanNewCfgMaxIntBwAdv = _VlanNewCfgMaxIntBwAdv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 17),
    _VlanNewCfgMaxIntBwAdv_Type()
)
vlanNewCfgMaxIntBwAdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgMaxIntBwAdv.setStatus("current")


class _VlanNewCfgMtu_Type(Integer32):
    """Custom type vlanNewCfgMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 1500),
    )


_VlanNewCfgMtu_Type.__name__ = "Integer32"
_VlanNewCfgMtu_Object = MibTableColumn
vlanNewCfgMtu = _VlanNewCfgMtu_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 18),
    _VlanNewCfgMtu_Type()
)
vlanNewCfgMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgMtu.setStatus("current")


class _VlanNewCfgCurHopLimit_Type(Integer32):
    """Custom type vlanNewCfgCurHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VlanNewCfgCurHopLimit_Type.__name__ = "Integer32"
_VlanNewCfgCurHopLimit_Object = MibTableColumn
vlanNewCfgCurHopLimit = _VlanNewCfgCurHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 19),
    _VlanNewCfgCurHopLimit_Type()
)
vlanNewCfgCurHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgCurHopLimit.setStatus("current")


class _VlanNewCfgMFlag_Type(Integer32):
    """Custom type vlanNewCfgMFlag based on Integer32"""
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


_VlanNewCfgMFlag_Type.__name__ = "Integer32"
_VlanNewCfgMFlag_Object = MibTableColumn
vlanNewCfgMFlag = _VlanNewCfgMFlag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 20),
    _VlanNewCfgMFlag_Type()
)
vlanNewCfgMFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgMFlag.setStatus("current")


class _VlanNewCfgOFlag_Type(Integer32):
    """Custom type vlanNewCfgOFlag based on Integer32"""
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


_VlanNewCfgOFlag_Type.__name__ = "Integer32"
_VlanNewCfgOFlag_Object = MibTableColumn
vlanNewCfgOFlag = _VlanNewCfgOFlag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 21),
    _VlanNewCfgOFlag_Type()
)
vlanNewCfgOFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgOFlag.setStatus("current")


class _VlanNewCfgRTime_Type(Integer32):
    """Custom type vlanNewCfgRTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_VlanNewCfgRTime_Type.__name__ = "Integer32"
_VlanNewCfgRTime_Object = MibTableColumn
vlanNewCfgRTime = _VlanNewCfgRTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 22),
    _VlanNewCfgRTime_Type()
)
vlanNewCfgRTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgRTime.setStatus("current")


class _VlanNewCfgRlTime_Type(Integer32):
    """Custom type vlanNewCfgRlTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
    )


_VlanNewCfgRlTime_Type.__name__ = "Integer32"
_VlanNewCfgRlTime_Object = MibTableColumn
vlanNewCfgRlTime = _VlanNewCfgRlTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 23),
    _VlanNewCfgRlTime_Type()
)
vlanNewCfgRlTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgRlTime.setStatus("current")


class _VlanNewCfgPlTime_Type(Unsigned32):
    """Custom type vlanNewCfgPlTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VlanNewCfgPlTime_Type.__name__ = "Unsigned32"
_VlanNewCfgPlTime_Object = MibTableColumn
vlanNewCfgPlTime = _VlanNewCfgPlTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 24),
    _VlanNewCfgPlTime_Type()
)
vlanNewCfgPlTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgPlTime.setStatus("current")


class _VlanNewCfgVlTime_Type(Unsigned32):
    """Custom type vlanNewCfgVlTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VlanNewCfgVlTime_Type.__name__ = "Unsigned32"
_VlanNewCfgVlTime_Object = MibTableColumn
vlanNewCfgVlTime = _VlanNewCfgVlTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 25),
    _VlanNewCfgVlTime_Type()
)
vlanNewCfgVlTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgVlTime.setStatus("current")


class _VlanNewCfgOpInfo_Type(Integer32):
    """Custom type vlanNewCfgOpInfo based on Integer32"""
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


_VlanNewCfgOpInfo_Type.__name__ = "Integer32"
_VlanNewCfgOpInfo_Object = MibTableColumn
vlanNewCfgOpInfo = _VlanNewCfgOpInfo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 26),
    _VlanNewCfgOpInfo_Type()
)
vlanNewCfgOpInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgOpInfo.setStatus("current")


class _VlanNewCfgApInfo_Type(Integer32):
    """Custom type vlanNewCfgApInfo based on Integer32"""
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


_VlanNewCfgApInfo_Type.__name__ = "Integer32"
_VlanNewCfgApInfo_Object = MibTableColumn
vlanNewCfgApInfo = _VlanNewCfgApInfo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 3, 1, 27),
    _VlanNewCfgApInfo_Type()
)
vlanNewCfgApInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgApInfo.setStatus("current")
_VlanMaxVlanID_Type = Integer32
_VlanMaxVlanID_Object = MibScalar
vlanMaxVlanID = _VlanMaxVlanID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 1, 4),
    _VlanMaxVlanID_Type()
)
vlanMaxVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMaxVlanID.setStatus("current")
_Trunkgroup_ObjectIdentity = ObjectIdentity
trunkgroup = _Trunkgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2)
)
_TrunkGroupTableMaxSize_Type = Integer32
_TrunkGroupTableMaxSize_Object = MibScalar
trunkGroupTableMaxSize = _TrunkGroupTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2, 1),
    _TrunkGroupTableMaxSize_Type()
)
trunkGroupTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupTableMaxSize.setStatus("current")
_TrunkGroupCurCfgTable_Object = MibTable
trunkGroupCurCfgTable = _TrunkGroupCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    trunkGroupCurCfgTable.setStatus("current")
_TrunkGroupCurCfgTableEntry_Object = MibTableRow
trunkGroupCurCfgTableEntry = _TrunkGroupCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2, 2, 1)
)
trunkGroupCurCfgTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "trunkGroupCurCfgIndex"),
)
if mibBuilder.loadTexts:
    trunkGroupCurCfgTableEntry.setStatus("current")
_TrunkGroupCurCfgIndex_Type = Integer32
_TrunkGroupCurCfgIndex_Object = MibTableColumn
trunkGroupCurCfgIndex = _TrunkGroupCurCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2, 2, 1, 1),
    _TrunkGroupCurCfgIndex_Type()
)
trunkGroupCurCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupCurCfgIndex.setStatus("current")
_TrunkGroupCurCfgPorts_Type = OctetString
_TrunkGroupCurCfgPorts_Object = MibTableColumn
trunkGroupCurCfgPorts = _TrunkGroupCurCfgPorts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2, 2, 1, 3),
    _TrunkGroupCurCfgState_Type()
)
trunkGroupCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupCurCfgState.setStatus("current")
_TrunkGroupCurCfgBwmContract_Type = Integer32
_TrunkGroupCurCfgBwmContract_Object = MibTableColumn
trunkGroupCurCfgBwmContract = _TrunkGroupCurCfgBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2, 2, 1, 4),
    _TrunkGroupCurCfgBwmContract_Type()
)
trunkGroupCurCfgBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupCurCfgBwmContract.setStatus("current")


class _TrunkGroupCurCfgName_Type(DisplayString):
    """Custom type trunkGroupCurCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TrunkGroupCurCfgName_Type.__name__ = "DisplayString"
_TrunkGroupCurCfgName_Object = MibTableColumn
trunkGroupCurCfgName = _TrunkGroupCurCfgName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2, 2, 1, 6),
    _TrunkGroupCurCfgName_Type()
)
trunkGroupCurCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupCurCfgName.setStatus("current")
_TrunkGroupNewCfgTable_Object = MibTable
trunkGroupNewCfgTable = _TrunkGroupNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    trunkGroupNewCfgTable.setStatus("current")
_TrunkGroupNewCfgTableEntry_Object = MibTableRow
trunkGroupNewCfgTableEntry = _TrunkGroupNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2, 3, 1)
)
trunkGroupNewCfgTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "trunkGroupNewCfgIndex"),
)
if mibBuilder.loadTexts:
    trunkGroupNewCfgTableEntry.setStatus("current")
_TrunkGroupNewCfgIndex_Type = Integer32
_TrunkGroupNewCfgIndex_Object = MibTableColumn
trunkGroupNewCfgIndex = _TrunkGroupNewCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2, 3, 1, 1),
    _TrunkGroupNewCfgIndex_Type()
)
trunkGroupNewCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupNewCfgIndex.setStatus("current")
_TrunkGroupNewCfgPorts_Type = OctetString
_TrunkGroupNewCfgPorts_Object = MibTableColumn
trunkGroupNewCfgPorts = _TrunkGroupNewCfgPorts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2, 3, 1, 2),
    _TrunkGroupNewCfgPorts_Type()
)
trunkGroupNewCfgPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupNewCfgPorts.setStatus("current")
_TrunkGroupNewCfgAddPort_Type = Integer32
_TrunkGroupNewCfgAddPort_Object = MibTableColumn
trunkGroupNewCfgAddPort = _TrunkGroupNewCfgAddPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2, 3, 1, 3),
    _TrunkGroupNewCfgAddPort_Type()
)
trunkGroupNewCfgAddPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkGroupNewCfgAddPort.setStatus("current")
_TrunkGroupNewCfgRemovePort_Type = Integer32
_TrunkGroupNewCfgRemovePort_Object = MibTableColumn
trunkGroupNewCfgRemovePort = _TrunkGroupNewCfgRemovePort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2, 3, 1, 6),
    _TrunkGroupNewCfgDelete_Type()
)
trunkGroupNewCfgDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkGroupNewCfgDelete.setStatus("current")
_TrunkGroupNewCfgBwmContract_Type = Integer32
_TrunkGroupNewCfgBwmContract_Object = MibTableColumn
trunkGroupNewCfgBwmContract = _TrunkGroupNewCfgBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2, 3, 1, 7),
    _TrunkGroupNewCfgBwmContract_Type()
)
trunkGroupNewCfgBwmContract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkGroupNewCfgBwmContract.setStatus("current")


class _TrunkGroupNewCfgName_Type(DisplayString):
    """Custom type trunkGroupNewCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TrunkGroupNewCfgName_Type.__name__ = "DisplayString"
_TrunkGroupNewCfgName_Object = MibTableColumn
trunkGroupNewCfgName = _TrunkGroupNewCfgName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 2, 3, 1, 9),
    _TrunkGroupNewCfgName_Type()
)
trunkGroupNewCfgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkGroupNewCfgName.setStatus("current")
_StgCfg_ObjectIdentity = ObjectIdentity
stgCfg = _StgCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3)
)
_StgCurCfgTable_Object = MibTable
stgCurCfgTable = _StgCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    stgCurCfgTable.setStatus("current")
_StgCurCfgTableEntry_Object = MibTableRow
stgCurCfgTableEntry = _StgCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 1, 1)
)
stgCurCfgTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "stgCurCfgIndex"),
)
if mibBuilder.loadTexts:
    stgCurCfgTableEntry.setStatus("current")
_StgCurCfgIndex_Type = Integer32
_StgCurCfgIndex_Object = MibTableColumn
stgCurCfgIndex = _StgCurCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 1, 1, 2),
    _StgCurCfgState_Type()
)
stgCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgState.setStatus("current")


class _StgCurCfgPriority_Type(Integer32):
    """Custom type stgCurCfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StgCurCfgPriority_Type.__name__ = "Integer32"
_StgCurCfgPriority_Object = MibTableColumn
stgCurCfgPriority = _StgCurCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 1, 1, 10),
    _StgCurCfgVlanBmap_Type()
)
stgCurCfgVlanBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgVlanBmap.setStatus("current")
_StgNewCfgTable_Object = MibTable
stgNewCfgTable = _StgNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    stgNewCfgTable.setStatus("current")
_StgNewCfgTableEntry_Object = MibTableRow
stgNewCfgTableEntry = _StgNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 2, 1)
)
stgNewCfgTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "stgNewCfgIndex"),
)
if mibBuilder.loadTexts:
    stgNewCfgTableEntry.setStatus("current")
_StgNewCfgIndex_Type = Integer32
_StgNewCfgIndex_Object = MibTableColumn
stgNewCfgIndex = _StgNewCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 2, 1, 2),
    _StgNewCfgState_Type()
)
stgNewCfgState.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 2, 1, 3),
    _StgNewCfgDefaultCfg_Type()
)
stgNewCfgDefaultCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stgNewCfgDefaultCfg.setStatus("current")
_StgNewCfgAddVlan_Type = Integer32
_StgNewCfgAddVlan_Object = MibTableColumn
stgNewCfgAddVlan = _StgNewCfgAddVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 2, 1, 4),
    _StgNewCfgAddVlan_Type()
)
stgNewCfgAddVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stgNewCfgAddVlan.setStatus("current")
_StgNewCfgRemoveVlan_Type = Integer32
_StgNewCfgRemoveVlan_Object = MibTableColumn
stgNewCfgRemoveVlan = _StgNewCfgRemoveVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 2, 1, 5),
    _StgNewCfgRemoveVlan_Type()
)
stgNewCfgRemoveVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stgNewCfgRemoveVlan.setStatus("current")


class _StgNewCfgPriority_Type(Integer32):
    """Custom type stgNewCfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StgNewCfgPriority_Type.__name__ = "Integer32"
_StgNewCfgPriority_Object = MibTableColumn
stgNewCfgPriority = _StgNewCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 2, 1, 8),
    _StgNewCfgPriority_Type()
)
stgNewCfgPriority.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 2, 1, 9),
    _StgNewCfgBrgHelloTime_Type()
)
stgNewCfgBrgHelloTime.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 2, 1, 10),
    _StgNewCfgBrgForwardDelay_Type()
)
stgNewCfgBrgForwardDelay.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 2, 1, 11),
    _StgNewCfgBrgMaxAge_Type()
)
stgNewCfgBrgMaxAge.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 2, 1, 12),
    _StgNewCfgAgingTime_Type()
)
stgNewCfgAgingTime.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 2, 1, 13),
    _StgNewCfgVlanBmap_Type()
)
stgNewCfgVlanBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgNewCfgVlanBmap.setStatus("current")
_StgCurCfgPortTable_Object = MibTable
stgCurCfgPortTable = _StgCurCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    stgCurCfgPortTable.setStatus("current")
_StgCurCfgPortTableEntry_Object = MibTableRow
stgCurCfgPortTableEntry = _StgCurCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 3, 1)
)
stgCurCfgPortTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "stgCurCfgStgIndex"),
    (0, "ALTEON-CS-PHYSICAL-MIB", "stgCurCfgPortIndex"),
)
if mibBuilder.loadTexts:
    stgCurCfgPortTableEntry.setStatus("current")
_StgCurCfgStgIndex_Type = Integer32
_StgCurCfgStgIndex_Object = MibTableColumn
stgCurCfgStgIndex = _StgCurCfgStgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 3, 1, 1),
    _StgCurCfgStgIndex_Type()
)
stgCurCfgStgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgStgIndex.setStatus("current")
_StgCurCfgPortIndex_Type = Integer32
_StgCurCfgPortIndex_Object = MibTableColumn
stgCurCfgPortIndex = _StgCurCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 3, 1, 4),
    _StgCurCfgPortPriority_Type()
)
stgCurCfgPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgPortPriority.setStatus("current")
_StgCurCfgPortPathCost_Type = Integer32
_StgCurCfgPortPathCost_Object = MibTableColumn
stgCurCfgPortPathCost = _StgCurCfgPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 3, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 3, 1, 7),
    _StgCurCfgPortEdge_Type()
)
stgCurCfgPortEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgCurCfgPortEdge.setStatus("current")
_StgNewCfgPortTable_Object = MibTable
stgNewCfgPortTable = _StgNewCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    stgNewCfgPortTable.setStatus("current")
_StgNewCfgPortTableEntry_Object = MibTableRow
stgNewCfgPortTableEntry = _StgNewCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 4, 1)
)
stgNewCfgPortTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "stgNewCfgStgIndex"),
    (0, "ALTEON-CS-PHYSICAL-MIB", "stgNewCfgPortIndex"),
)
if mibBuilder.loadTexts:
    stgNewCfgPortTableEntry.setStatus("current")
_StgNewCfgStgIndex_Type = Integer32
_StgNewCfgStgIndex_Object = MibTableColumn
stgNewCfgStgIndex = _StgNewCfgStgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 4, 1, 1),
    _StgNewCfgStgIndex_Type()
)
stgNewCfgStgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgNewCfgStgIndex.setStatus("current")
_StgNewCfgPortIndex_Type = Integer32
_StgNewCfgPortIndex_Object = MibTableColumn
stgNewCfgPortIndex = _StgNewCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 4, 1, 4),
    _StgNewCfgPortPriority_Type()
)
stgNewCfgPortPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stgNewCfgPortPriority.setStatus("current")
_StgNewCfgPortPathCost_Type = Integer32
_StgNewCfgPortPathCost_Object = MibTableColumn
stgNewCfgPortPathCost = _StgNewCfgPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 4, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 4, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 3, 4, 1, 7),
    _StgNewCfgPortEdge_Type()
)
stgNewCfgPortEdge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stgNewCfgPortEdge.setStatus("current")
_Mirroring_ObjectIdentity = ObjectIdentity
mirroring = _Mirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4)
)
_MirrPortMirr_ObjectIdentity = ObjectIdentity
mirrPortMirr = _MirrPortMirr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4, 1)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4, 1, 2),
    _PmNewCfgPortMirrState_Type()
)
pmNewCfgPortMirrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmNewCfgPortMirrState.setStatus("current")
_PmCurCfgPortMonitorTable_Object = MibTable
pmCurCfgPortMonitorTable = _PmCurCfgPortMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    pmCurCfgPortMonitorTable.setStatus("current")
_PmCurCfgPortMonitorEntry_Object = MibTableRow
pmCurCfgPortMonitorEntry = _PmCurCfgPortMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4, 1, 3, 1)
)
pmCurCfgPortMonitorEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "pmCurCfgPmirrMoniPortIndex"),
    (0, "ALTEON-CS-PHYSICAL-MIB", "pmCurCfgPmirrMirrPortIndex"),
)
if mibBuilder.loadTexts:
    pmCurCfgPortMonitorEntry.setStatus("current")
_PmCurCfgPmirrMoniPortIndex_Type = Integer32
_PmCurCfgPmirrMoniPortIndex_Object = MibTableColumn
pmCurCfgPmirrMoniPortIndex = _PmCurCfgPmirrMoniPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4, 1, 3, 1, 1),
    _PmCurCfgPmirrMoniPortIndex_Type()
)
pmCurCfgPmirrMoniPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgPmirrMoniPortIndex.setStatus("current")
_PmCurCfgPmirrMirrPortIndex_Type = Integer32
_PmCurCfgPmirrMirrPortIndex_Object = MibTableColumn
pmCurCfgPmirrMirrPortIndex = _PmCurCfgPmirrMirrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4, 1, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4, 1, 3, 1, 3),
    _PmCurCfgPmirrDirection_Type()
)
pmCurCfgPmirrDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgPmirrDirection.setStatus("current")
_PmCurCfgPmirrPortVlansBmap_Type = OctetString
_PmCurCfgPmirrPortVlansBmap_Object = MibTableColumn
pmCurCfgPmirrPortVlansBmap = _PmCurCfgPmirrPortVlansBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4, 1, 3, 1, 6),
    _PmCurCfgPmirrPortVlansBmap_Type()
)
pmCurCfgPmirrPortVlansBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmCurCfgPmirrPortVlansBmap.setStatus("current")
_PmNewCfgPortMonitorTable_Object = MibTable
pmNewCfgPortMonitorTable = _PmNewCfgPortMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    pmNewCfgPortMonitorTable.setStatus("current")
_PmNewCfgPortMonitorEntry_Object = MibTableRow
pmNewCfgPortMonitorEntry = _PmNewCfgPortMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4, 1, 4, 1)
)
pmNewCfgPortMonitorEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "pmNewCfgPmirrMoniPortIndex"),
    (0, "ALTEON-CS-PHYSICAL-MIB", "pmNewCfgPmirrMirrPortIndex"),
)
if mibBuilder.loadTexts:
    pmNewCfgPortMonitorEntry.setStatus("current")
_PmNewCfgPmirrMoniPortIndex_Type = Integer32
_PmNewCfgPmirrMoniPortIndex_Object = MibTableColumn
pmNewCfgPmirrMoniPortIndex = _PmNewCfgPmirrMoniPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4, 1, 4, 1, 1),
    _PmNewCfgPmirrMoniPortIndex_Type()
)
pmNewCfgPmirrMoniPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmNewCfgPmirrMoniPortIndex.setStatus("current")
_PmNewCfgPmirrMirrPortIndex_Type = Integer32
_PmNewCfgPmirrMirrPortIndex_Object = MibTableColumn
pmNewCfgPmirrMirrPortIndex = _PmNewCfgPmirrMirrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4, 1, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4, 1, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4, 1, 4, 1, 4),
    _PmNewCfgPmirrDelete_Type()
)
pmNewCfgPmirrDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmNewCfgPmirrDelete.setStatus("current")
_PmNewCfgAddVlan_Type = Integer32
_PmNewCfgAddVlan_Object = MibTableColumn
pmNewCfgAddVlan = _PmNewCfgAddVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4, 1, 4, 1, 7),
    _PmNewCfgAddVlan_Type()
)
pmNewCfgAddVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmNewCfgAddVlan.setStatus("current")
_PmNewCfgRemoveVlan_Type = Integer32
_PmNewCfgRemoveVlan_Object = MibTableColumn
pmNewCfgRemoveVlan = _PmNewCfgRemoveVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4, 1, 4, 1, 8),
    _PmNewCfgRemoveVlan_Type()
)
pmNewCfgRemoveVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmNewCfgRemoveVlan.setStatus("current")
_PmNewCfgPmirrPortVlansBmap_Type = OctetString
_PmNewCfgPmirrPortVlansBmap_Object = MibTableColumn
pmNewCfgPmirrPortVlansBmap = _PmNewCfgPmirrPortVlansBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 4, 1, 4, 1, 9),
    _PmNewCfgPmirrPortVlansBmap_Type()
)
pmNewCfgPmirrPortVlansBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmNewCfgPmirrPortVlansBmap.setStatus("current")
_Lacp_ObjectIdentity = ObjectIdentity
lacp = _Lacp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5, 6),
    _LacpNewSystemTimeoutTime_Type()
)
lacpNewSystemTimeoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpNewSystemTimeoutTime.setStatus("current")
_LacpCurPortCfgTable_Object = MibTable
lacpCurPortCfgTable = _LacpCurPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5, 7)
)
if mibBuilder.loadTexts:
    lacpCurPortCfgTable.setStatus("current")
_LacpCurPortCfgTableEntry_Object = MibTableRow
lacpCurPortCfgTableEntry = _LacpCurPortCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5, 7, 1)
)
lacpCurPortCfgTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "lacpCurPortCfgTableId"),
)
if mibBuilder.loadTexts:
    lacpCurPortCfgTableEntry.setStatus("current")
_LacpCurPortCfgTableId_Type = Integer32
_LacpCurPortCfgTableId_Object = MibTableColumn
lacpCurPortCfgTableId = _LacpCurPortCfgTableId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5, 7, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5, 7, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5, 7, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5, 7, 1, 4),
    _LacpCurPortActorAdminKey_Type()
)
lacpCurPortActorAdminKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpCurPortActorAdminKey.setStatus("current")
_LacpNewPortCfgTable_Object = MibTable
lacpNewPortCfgTable = _LacpNewPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5, 8)
)
if mibBuilder.loadTexts:
    lacpNewPortCfgTable.setStatus("current")
_LacpNewPortCfgTableEntry_Object = MibTableRow
lacpNewPortCfgTableEntry = _LacpNewPortCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5, 8, 1)
)
lacpNewPortCfgTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "lacpNewPortCfgTableId"),
)
if mibBuilder.loadTexts:
    lacpNewPortCfgTableEntry.setStatus("current")
_LacpNewPortCfgTableId_Type = Integer32
_LacpNewPortCfgTableId_Object = MibTableColumn
lacpNewPortCfgTableId = _LacpNewPortCfgTableId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5, 8, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5, 8, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5, 8, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5, 8, 1, 4),
    _LacpNewPortActorAdminKey_Type()
)
lacpNewPortActorAdminKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpNewPortActorAdminKey.setStatus("current")


class _LacpCurSystemName_Type(DisplayString):
    """Custom type lacpCurSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_LacpCurSystemName_Type.__name__ = "DisplayString"
_LacpCurSystemName_Object = MibScalar
lacpCurSystemName = _LacpCurSystemName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5, 9),
    _LacpCurSystemName_Type()
)
lacpCurSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpCurSystemName.setStatus("current")


class _LacpNewSystemName_Type(DisplayString):
    """Custom type lacpNewSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_LacpNewSystemName_Type.__name__ = "DisplayString"
_LacpNewSystemName_Object = MibScalar
lacpNewSystemName = _LacpNewSystemName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 5, 10),
    _LacpNewSystemName_Type()
)
lacpNewSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpNewSystemName.setStatus("current")
_MstCfg_ObjectIdentity = ObjectIdentity
mstCfg = _MstCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7)
)
_MstGeneralCfg_ObjectIdentity = ObjectIdentity
mstGeneralCfg = _MstGeneralCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 1)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 1, 10),
    _MstNewCfgStpMode_Type()
)
mstNewCfgStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstNewCfgStpMode.setStatus("current")
_MstCistCfg_ObjectIdentity = ObjectIdentity
mstCistCfg = _MstCistCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 1),
    _MstCistDefaultCfg_Type()
)
mstCistDefaultCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstCistDefaultCfg.setStatus("current")
_MstCistBridgeCfg_ObjectIdentity = ObjectIdentity
mstCistBridgeCfg = _MstCistBridgeCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 2)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 2, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 2, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 2, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 2, 8),
    _MstCistNewCfgBridgeForwardDelay_Type()
)
mstCistNewCfgBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstCistNewCfgBridgeForwardDelay.setStatus("current")
_MstCistCurCfgPortTable_Object = MibTable
mstCistCurCfgPortTable = _MstCistCurCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 3)
)
if mibBuilder.loadTexts:
    mstCistCurCfgPortTable.setStatus("current")
_MstCistCurCfgPortTableEntry_Object = MibTableRow
mstCistCurCfgPortTableEntry = _MstCistCurCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 3, 1)
)
mstCistCurCfgPortTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "mstCistCurCfgPortIndex"),
)
if mibBuilder.loadTexts:
    mstCistCurCfgPortTableEntry.setStatus("current")
_MstCistCurCfgPortIndex_Type = Integer32
_MstCistCurCfgPortIndex_Object = MibTableColumn
mstCistCurCfgPortIndex = _MstCistCurCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 3, 1, 2),
    _MstCistCurCfgPortPriority_Type()
)
mstCistCurCfgPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistCurCfgPortPriority.setStatus("current")


class _MstCistCurCfgPortPathCost_Type(Integer32):
    """Custom type mstCistCurCfgPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_MstCistCurCfgPortPathCost_Type.__name__ = "Integer32"
_MstCistCurCfgPortPathCost_Object = MibTableColumn
mstCistCurCfgPortPathCost = _MstCistCurCfgPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 3, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 3, 1, 7),
    _MstCistCurCfgPortHelloTime_Type()
)
mstCistCurCfgPortHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstCistCurCfgPortHelloTime.setStatus("current")
_MstCistNewCfgPortTable_Object = MibTable
mstCistNewCfgPortTable = _MstCistNewCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 4)
)
if mibBuilder.loadTexts:
    mstCistNewCfgPortTable.setStatus("current")
_MstCistNewCfgPortTableEntry_Object = MibTableRow
mstCistNewCfgPortTableEntry = _MstCistNewCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 4, 1)
)
mstCistNewCfgPortTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "mstCistNewCfgPortIndex"),
)
if mibBuilder.loadTexts:
    mstCistNewCfgPortTableEntry.setStatus("current")
_MstCistNewCfgPortIndex_Type = Integer32
_MstCistNewCfgPortIndex_Object = MibTableColumn
mstCistNewCfgPortIndex = _MstCistNewCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 4, 1, 2),
    _MstCistNewCfgPortPriority_Type()
)
mstCistNewCfgPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstCistNewCfgPortPriority.setStatus("current")


class _MstCistNewCfgPortPathCost_Type(Integer32):
    """Custom type mstCistNewCfgPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_MstCistNewCfgPortPathCost_Type.__name__ = "Integer32"
_MstCistNewCfgPortPathCost_Object = MibTableColumn
mstCistNewCfgPortPathCost = _MstCistNewCfgPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 4, 1, 3),
    _MstCistNewCfgPortPathCost_Type()
)
mstCistNewCfgPortPathCost.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 4, 1, 4),
    _MstCistNewCfgPortLinkType_Type()
)
mstCistNewCfgPortLinkType.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 4, 1, 5),
    _MstCistNewCfgPortEdge_Type()
)
mstCistNewCfgPortEdge.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 4, 1, 6),
    _MstCistNewCfgPortStpState_Type()
)
mstCistNewCfgPortStpState.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 7, 2, 4, 1, 7),
    _MstCistNewCfgPortHelloTime_Type()
)
mstCistNewCfgPortHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstCistNewCfgPortHelloTime.setStatus("current")
_PortTeamCfg_ObjectIdentity = ObjectIdentity
portTeamCfg = _PortTeamCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9)
)
_PortTeamTableMaxSize_Type = Integer32
_PortTeamTableMaxSize_Object = MibScalar
portTeamTableMaxSize = _PortTeamTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 1),
    _PortTeamTableMaxSize_Type()
)
portTeamTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTeamTableMaxSize.setStatus("current")
_PortTeamCurCfgTable_Object = MibTable
portTeamCurCfgTable = _PortTeamCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    portTeamCurCfgTable.setStatus("current")
_PortTeamCurCfgTableEntry_Object = MibTableRow
portTeamCurCfgTableEntry = _PortTeamCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 2, 1)
)
portTeamCurCfgTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "portTeamCurCfgIndex"),
)
if mibBuilder.loadTexts:
    portTeamCurCfgTableEntry.setStatus("current")
_PortTeamCurCfgIndex_Type = Integer32
_PortTeamCurCfgIndex_Object = MibTableColumn
portTeamCurCfgIndex = _PortTeamCurCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 2, 1, 1),
    _PortTeamCurCfgIndex_Type()
)
portTeamCurCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTeamCurCfgIndex.setStatus("current")


class _PortTeamCurCfgState_Type(Integer32):
    """Custom type portTeamCurCfgState based on Integer32"""
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


_PortTeamCurCfgState_Type.__name__ = "Integer32"
_PortTeamCurCfgState_Object = MibTableColumn
portTeamCurCfgState = _PortTeamCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 2, 1, 2),
    _PortTeamCurCfgState_Type()
)
portTeamCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTeamCurCfgState.setStatus("current")
_PortTeamCurCfgPorts_Type = OctetString
_PortTeamCurCfgPorts_Object = MibTableColumn
portTeamCurCfgPorts = _PortTeamCurCfgPorts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 2, 1, 3),
    _PortTeamCurCfgPorts_Type()
)
portTeamCurCfgPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTeamCurCfgPorts.setStatus("current")
_PortTeamCurCfgTrunks_Type = OctetString
_PortTeamCurCfgTrunks_Object = MibTableColumn
portTeamCurCfgTrunks = _PortTeamCurCfgTrunks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 2, 1, 4),
    _PortTeamCurCfgTrunks_Type()
)
portTeamCurCfgTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTeamCurCfgTrunks.setStatus("current")


class _PortTeamCurCfgName_Type(DisplayString):
    """Custom type portTeamCurCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PortTeamCurCfgName_Type.__name__ = "DisplayString"
_PortTeamCurCfgName_Object = MibTableColumn
portTeamCurCfgName = _PortTeamCurCfgName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 2, 1, 5),
    _PortTeamCurCfgName_Type()
)
portTeamCurCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTeamCurCfgName.setStatus("current")
_PortTeamNewCfgTable_Object = MibTable
portTeamNewCfgTable = _PortTeamNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 3)
)
if mibBuilder.loadTexts:
    portTeamNewCfgTable.setStatus("current")
_PortTeamNewCfgTableEntry_Object = MibTableRow
portTeamNewCfgTableEntry = _PortTeamNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 3, 1)
)
portTeamNewCfgTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "portTeamNewCfgIndex"),
)
if mibBuilder.loadTexts:
    portTeamNewCfgTableEntry.setStatus("current")
_PortTeamNewCfgIndex_Type = Integer32
_PortTeamNewCfgIndex_Object = MibTableColumn
portTeamNewCfgIndex = _PortTeamNewCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 3, 1, 1),
    _PortTeamNewCfgIndex_Type()
)
portTeamNewCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTeamNewCfgIndex.setStatus("current")


class _PortTeamNewCfgState_Type(Integer32):
    """Custom type portTeamNewCfgState based on Integer32"""
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


_PortTeamNewCfgState_Type.__name__ = "Integer32"
_PortTeamNewCfgState_Object = MibTableColumn
portTeamNewCfgState = _PortTeamNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 3, 1, 2),
    _PortTeamNewCfgState_Type()
)
portTeamNewCfgState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portTeamNewCfgState.setStatus("current")
_PortTeamNewCfgPorts_Type = OctetString
_PortTeamNewCfgPorts_Object = MibTableColumn
portTeamNewCfgPorts = _PortTeamNewCfgPorts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 3, 1, 3),
    _PortTeamNewCfgPorts_Type()
)
portTeamNewCfgPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTeamNewCfgPorts.setStatus("current")
_PortTeamNewCfgAddPort_Type = Integer32
_PortTeamNewCfgAddPort_Object = MibTableColumn
portTeamNewCfgAddPort = _PortTeamNewCfgAddPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 3, 1, 4),
    _PortTeamNewCfgAddPort_Type()
)
portTeamNewCfgAddPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portTeamNewCfgAddPort.setStatus("current")
_PortTeamNewCfgRemovePort_Type = Integer32
_PortTeamNewCfgRemovePort_Object = MibTableColumn
portTeamNewCfgRemovePort = _PortTeamNewCfgRemovePort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 3, 1, 5),
    _PortTeamNewCfgRemovePort_Type()
)
portTeamNewCfgRemovePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portTeamNewCfgRemovePort.setStatus("current")
_PortTeamNewCfgTrunks_Type = OctetString
_PortTeamNewCfgTrunks_Object = MibTableColumn
portTeamNewCfgTrunks = _PortTeamNewCfgTrunks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 3, 1, 6),
    _PortTeamNewCfgTrunks_Type()
)
portTeamNewCfgTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTeamNewCfgTrunks.setStatus("current")
_PortTeamNewCfgAddTrunk_Type = Integer32
_PortTeamNewCfgAddTrunk_Object = MibTableColumn
portTeamNewCfgAddTrunk = _PortTeamNewCfgAddTrunk_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 3, 1, 7),
    _PortTeamNewCfgAddTrunk_Type()
)
portTeamNewCfgAddTrunk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portTeamNewCfgAddTrunk.setStatus("current")
_PortTeamNewCfgRemoveTrunk_Type = Integer32
_PortTeamNewCfgRemoveTrunk_Object = MibTableColumn
portTeamNewCfgRemoveTrunk = _PortTeamNewCfgRemoveTrunk_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 3, 1, 8),
    _PortTeamNewCfgRemoveTrunk_Type()
)
portTeamNewCfgRemoveTrunk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portTeamNewCfgRemoveTrunk.setStatus("current")


class _PortTeamNewCfgDelete_Type(Integer32):
    """Custom type portTeamNewCfgDelete based on Integer32"""
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


_PortTeamNewCfgDelete_Type.__name__ = "Integer32"
_PortTeamNewCfgDelete_Object = MibTableColumn
portTeamNewCfgDelete = _PortTeamNewCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 3, 1, 9),
    _PortTeamNewCfgDelete_Type()
)
portTeamNewCfgDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portTeamNewCfgDelete.setStatus("current")


class _PortTeamNewCfgName_Type(DisplayString):
    """Custom type portTeamNewCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PortTeamNewCfgName_Type.__name__ = "DisplayString"
_PortTeamNewCfgName_Object = MibTableColumn
portTeamNewCfgName = _PortTeamNewCfgName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 9, 3, 1, 10),
    _PortTeamNewCfgName_Type()
)
portTeamNewCfgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portTeamNewCfgName.setStatus("current")
_VadcVlan_ObjectIdentity = ObjectIdentity
vadcVlan = _VadcVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10)
)
_VadcVlanCurCfgTable_Object = MibTable
vadcVlanCurCfgTable = _VadcVlanCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    vadcVlanCurCfgTable.setStatus("current")
_VadcVlanCurCfgTableEntry_Object = MibTableRow
vadcVlanCurCfgTableEntry = _VadcVlanCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1)
)
vadcVlanCurCfgTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "vadcVlanCurCfgVlanId"),
)
if mibBuilder.loadTexts:
    vadcVlanCurCfgTableEntry.setStatus("current")
_VadcVlanCurCfgVlanId_Type = Integer32
_VadcVlanCurCfgVlanId_Object = MibTableColumn
vadcVlanCurCfgVlanId = _VadcVlanCurCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1, 1),
    _VadcVlanCurCfgVlanId_Type()
)
vadcVlanCurCfgVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanCurCfgVlanId.setStatus("current")
_VadcVlanCurCfgBwmCont_Type = Integer32
_VadcVlanCurCfgBwmCont_Object = MibTableColumn
vadcVlanCurCfgBwmCont = _VadcVlanCurCfgBwmCont_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1, 2),
    _VadcVlanCurCfgBwmCont_Type()
)
vadcVlanCurCfgBwmCont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanCurCfgBwmCont.setStatus("current")
_VadcVlanCurCfgNonIp_Type = Integer32
_VadcVlanCurCfgNonIp_Object = MibTableColumn
vadcVlanCurCfgNonIp = _VadcVlanCurCfgNonIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1, 3),
    _VadcVlanCurCfgNonIp_Type()
)
vadcVlanCurCfgNonIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanCurCfgNonIp.setStatus("current")


class _VadcVlanCurCfgIpv6LlaGen_Type(Integer32):
    """Custom type vadcVlanCurCfgIpv6LlaGen based on Integer32"""
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


_VadcVlanCurCfgIpv6LlaGen_Type.__name__ = "Integer32"
_VadcVlanCurCfgIpv6LlaGen_Object = MibTableColumn
vadcVlanCurCfgIpv6LlaGen = _VadcVlanCurCfgIpv6LlaGen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1, 4),
    _VadcVlanCurCfgIpv6LlaGen_Type()
)
vadcVlanCurCfgIpv6LlaGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanCurCfgIpv6LlaGen.setStatus("current")


class _VadcVlanCurCfgRouterAdv_Type(Integer32):
    """Custom type vadcVlanCurCfgRouterAdv based on Integer32"""
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


_VadcVlanCurCfgRouterAdv_Type.__name__ = "Integer32"
_VadcVlanCurCfgRouterAdv_Object = MibTableColumn
vadcVlanCurCfgRouterAdv = _VadcVlanCurCfgRouterAdv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1, 5),
    _VadcVlanCurCfgRouterAdv_Type()
)
vadcVlanCurCfgRouterAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanCurCfgRouterAdv.setStatus("current")


class _VadcVlanCurCfgReTransInt_Type(Unsigned32):
    """Custom type vadcVlanCurCfgReTransInt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VadcVlanCurCfgReTransInt_Type.__name__ = "Unsigned32"
_VadcVlanCurCfgReTransInt_Object = MibTableColumn
vadcVlanCurCfgReTransInt = _VadcVlanCurCfgReTransInt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1, 6),
    _VadcVlanCurCfgReTransInt_Type()
)
vadcVlanCurCfgReTransInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanCurCfgReTransInt.setStatus("current")


class _VadcVlanCurCfgMinIntBwAdv_Type(Integer32):
    """Custom type vadcVlanCurCfgMinIntBwAdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1800),
    )


_VadcVlanCurCfgMinIntBwAdv_Type.__name__ = "Integer32"
_VadcVlanCurCfgMinIntBwAdv_Object = MibTableColumn
vadcVlanCurCfgMinIntBwAdv = _VadcVlanCurCfgMinIntBwAdv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1, 7),
    _VadcVlanCurCfgMinIntBwAdv_Type()
)
vadcVlanCurCfgMinIntBwAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanCurCfgMinIntBwAdv.setStatus("current")


class _VadcVlanCurCfgMaxIntBwAdv_Type(Integer32):
    """Custom type vadcVlanCurCfgMaxIntBwAdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_VadcVlanCurCfgMaxIntBwAdv_Type.__name__ = "Integer32"
_VadcVlanCurCfgMaxIntBwAdv_Object = MibTableColumn
vadcVlanCurCfgMaxIntBwAdv = _VadcVlanCurCfgMaxIntBwAdv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1, 8),
    _VadcVlanCurCfgMaxIntBwAdv_Type()
)
vadcVlanCurCfgMaxIntBwAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanCurCfgMaxIntBwAdv.setStatus("current")


class _VadcVlanCurCfgMtu_Type(Integer32):
    """Custom type vadcVlanCurCfgMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 1500),
    )


_VadcVlanCurCfgMtu_Type.__name__ = "Integer32"
_VadcVlanCurCfgMtu_Object = MibTableColumn
vadcVlanCurCfgMtu = _VadcVlanCurCfgMtu_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1, 9),
    _VadcVlanCurCfgMtu_Type()
)
vadcVlanCurCfgMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanCurCfgMtu.setStatus("current")


class _VadcVlanCurCfgCurHopLimit_Type(Integer32):
    """Custom type vadcVlanCurCfgCurHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VadcVlanCurCfgCurHopLimit_Type.__name__ = "Integer32"
_VadcVlanCurCfgCurHopLimit_Object = MibTableColumn
vadcVlanCurCfgCurHopLimit = _VadcVlanCurCfgCurHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1, 10),
    _VadcVlanCurCfgCurHopLimit_Type()
)
vadcVlanCurCfgCurHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanCurCfgCurHopLimit.setStatus("current")


class _VadcVlanCurCfgMFlag_Type(Integer32):
    """Custom type vadcVlanCurCfgMFlag based on Integer32"""
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


_VadcVlanCurCfgMFlag_Type.__name__ = "Integer32"
_VadcVlanCurCfgMFlag_Object = MibTableColumn
vadcVlanCurCfgMFlag = _VadcVlanCurCfgMFlag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1, 11),
    _VadcVlanCurCfgMFlag_Type()
)
vadcVlanCurCfgMFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanCurCfgMFlag.setStatus("current")


class _VadcVlanCurCfgOFlag_Type(Integer32):
    """Custom type vadcVlanCurCfgOFlag based on Integer32"""
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


_VadcVlanCurCfgOFlag_Type.__name__ = "Integer32"
_VadcVlanCurCfgOFlag_Object = MibTableColumn
vadcVlanCurCfgOFlag = _VadcVlanCurCfgOFlag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1, 12),
    _VadcVlanCurCfgOFlag_Type()
)
vadcVlanCurCfgOFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanCurCfgOFlag.setStatus("current")


class _VadcVlanCurCfgRTime_Type(Integer32):
    """Custom type vadcVlanCurCfgRTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_VadcVlanCurCfgRTime_Type.__name__ = "Integer32"
_VadcVlanCurCfgRTime_Object = MibTableColumn
vadcVlanCurCfgRTime = _VadcVlanCurCfgRTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1, 13),
    _VadcVlanCurCfgRTime_Type()
)
vadcVlanCurCfgRTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanCurCfgRTime.setStatus("current")


class _VadcVlanCurCfgRlTime_Type(Integer32):
    """Custom type vadcVlanCurCfgRlTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
    )


_VadcVlanCurCfgRlTime_Type.__name__ = "Integer32"
_VadcVlanCurCfgRlTime_Object = MibTableColumn
vadcVlanCurCfgRlTime = _VadcVlanCurCfgRlTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1, 14),
    _VadcVlanCurCfgRlTime_Type()
)
vadcVlanCurCfgRlTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanCurCfgRlTime.setStatus("current")


class _VadcVlanCurCfgPlTime_Type(Unsigned32):
    """Custom type vadcVlanCurCfgPlTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VadcVlanCurCfgPlTime_Type.__name__ = "Unsigned32"
_VadcVlanCurCfgPlTime_Object = MibTableColumn
vadcVlanCurCfgPlTime = _VadcVlanCurCfgPlTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1, 15),
    _VadcVlanCurCfgPlTime_Type()
)
vadcVlanCurCfgPlTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanCurCfgPlTime.setStatus("current")


class _VadcVlanCurCfgVlTime_Type(Unsigned32):
    """Custom type vadcVlanCurCfgVlTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VadcVlanCurCfgVlTime_Type.__name__ = "Unsigned32"
_VadcVlanCurCfgVlTime_Object = MibTableColumn
vadcVlanCurCfgVlTime = _VadcVlanCurCfgVlTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1, 16),
    _VadcVlanCurCfgVlTime_Type()
)
vadcVlanCurCfgVlTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanCurCfgVlTime.setStatus("current")


class _VadcVlanCurCfgOpInfo_Type(Integer32):
    """Custom type vadcVlanCurCfgOpInfo based on Integer32"""
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


_VadcVlanCurCfgOpInfo_Type.__name__ = "Integer32"
_VadcVlanCurCfgOpInfo_Object = MibTableColumn
vadcVlanCurCfgOpInfo = _VadcVlanCurCfgOpInfo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1, 17),
    _VadcVlanCurCfgOpInfo_Type()
)
vadcVlanCurCfgOpInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanCurCfgOpInfo.setStatus("current")


class _VadcVlanCurCfgApInfo_Type(Integer32):
    """Custom type vadcVlanCurCfgApInfo based on Integer32"""
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


_VadcVlanCurCfgApInfo_Type.__name__ = "Integer32"
_VadcVlanCurCfgApInfo_Object = MibTableColumn
vadcVlanCurCfgApInfo = _VadcVlanCurCfgApInfo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 1, 1, 18),
    _VadcVlanCurCfgApInfo_Type()
)
vadcVlanCurCfgApInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanCurCfgApInfo.setStatus("current")
_VadcVlanNewCfgTable_Object = MibTable
vadcVlanNewCfgTable = _VadcVlanNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    vadcVlanNewCfgTable.setStatus("current")
_VadcVlanNewCfgTableEntry_Object = MibTableRow
vadcVlanNewCfgTableEntry = _VadcVlanNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1)
)
vadcVlanNewCfgTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "vadcVlanNewCfgVlanId"),
)
if mibBuilder.loadTexts:
    vadcVlanNewCfgTableEntry.setStatus("current")
_VadcVlanNewCfgVlanId_Type = Integer32
_VadcVlanNewCfgVlanId_Object = MibTableColumn
vadcVlanNewCfgVlanId = _VadcVlanNewCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1, 1),
    _VadcVlanNewCfgVlanId_Type()
)
vadcVlanNewCfgVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vadcVlanNewCfgVlanId.setStatus("current")
_VadcVlanNewCfgBwmCont_Type = Integer32
_VadcVlanNewCfgBwmCont_Object = MibTableColumn
vadcVlanNewCfgBwmCont = _VadcVlanNewCfgBwmCont_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1, 2),
    _VadcVlanNewCfgBwmCont_Type()
)
vadcVlanNewCfgBwmCont.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vadcVlanNewCfgBwmCont.setStatus("current")
_VadcVlanNewCfgNonIp_Type = Integer32
_VadcVlanNewCfgNonIp_Object = MibTableColumn
vadcVlanNewCfgNonIp = _VadcVlanNewCfgNonIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1, 3),
    _VadcVlanNewCfgNonIp_Type()
)
vadcVlanNewCfgNonIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vadcVlanNewCfgNonIp.setStatus("current")


class _VadcVlanNewCfgIpv6LlaGen_Type(Integer32):
    """Custom type vadcVlanNewCfgIpv6LlaGen based on Integer32"""
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


_VadcVlanNewCfgIpv6LlaGen_Type.__name__ = "Integer32"
_VadcVlanNewCfgIpv6LlaGen_Object = MibTableColumn
vadcVlanNewCfgIpv6LlaGen = _VadcVlanNewCfgIpv6LlaGen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1, 4),
    _VadcVlanNewCfgIpv6LlaGen_Type()
)
vadcVlanNewCfgIpv6LlaGen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vadcVlanNewCfgIpv6LlaGen.setStatus("current")


class _VadcVlanNewCfgRouterAdv_Type(Integer32):
    """Custom type vadcVlanNewCfgRouterAdv based on Integer32"""
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


_VadcVlanNewCfgRouterAdv_Type.__name__ = "Integer32"
_VadcVlanNewCfgRouterAdv_Object = MibTableColumn
vadcVlanNewCfgRouterAdv = _VadcVlanNewCfgRouterAdv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1, 5),
    _VadcVlanNewCfgRouterAdv_Type()
)
vadcVlanNewCfgRouterAdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vadcVlanNewCfgRouterAdv.setStatus("current")


class _VadcVlanNewCfgReTransInt_Type(Unsigned32):
    """Custom type vadcVlanNewCfgReTransInt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VadcVlanNewCfgReTransInt_Type.__name__ = "Unsigned32"
_VadcVlanNewCfgReTransInt_Object = MibTableColumn
vadcVlanNewCfgReTransInt = _VadcVlanNewCfgReTransInt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1, 6),
    _VadcVlanNewCfgReTransInt_Type()
)
vadcVlanNewCfgReTransInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vadcVlanNewCfgReTransInt.setStatus("current")


class _VadcVlanNewCfgMinIntBwAdv_Type(Integer32):
    """Custom type vadcVlanNewCfgMinIntBwAdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1800),
    )


_VadcVlanNewCfgMinIntBwAdv_Type.__name__ = "Integer32"
_VadcVlanNewCfgMinIntBwAdv_Object = MibTableColumn
vadcVlanNewCfgMinIntBwAdv = _VadcVlanNewCfgMinIntBwAdv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1, 7),
    _VadcVlanNewCfgMinIntBwAdv_Type()
)
vadcVlanNewCfgMinIntBwAdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vadcVlanNewCfgMinIntBwAdv.setStatus("current")


class _VadcVlanNewCfgMaxIntBwAdv_Type(Integer32):
    """Custom type vadcVlanNewCfgMaxIntBwAdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_VadcVlanNewCfgMaxIntBwAdv_Type.__name__ = "Integer32"
_VadcVlanNewCfgMaxIntBwAdv_Object = MibTableColumn
vadcVlanNewCfgMaxIntBwAdv = _VadcVlanNewCfgMaxIntBwAdv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1, 8),
    _VadcVlanNewCfgMaxIntBwAdv_Type()
)
vadcVlanNewCfgMaxIntBwAdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vadcVlanNewCfgMaxIntBwAdv.setStatus("current")


class _VadcVlanNewCfgMtu_Type(Integer32):
    """Custom type vadcVlanNewCfgMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 1500),
    )


_VadcVlanNewCfgMtu_Type.__name__ = "Integer32"
_VadcVlanNewCfgMtu_Object = MibTableColumn
vadcVlanNewCfgMtu = _VadcVlanNewCfgMtu_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1, 9),
    _VadcVlanNewCfgMtu_Type()
)
vadcVlanNewCfgMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vadcVlanNewCfgMtu.setStatus("current")


class _VadcVlanNewCfgCurHopLimit_Type(Integer32):
    """Custom type vadcVlanNewCfgCurHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VadcVlanNewCfgCurHopLimit_Type.__name__ = "Integer32"
_VadcVlanNewCfgCurHopLimit_Object = MibTableColumn
vadcVlanNewCfgCurHopLimit = _VadcVlanNewCfgCurHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1, 10),
    _VadcVlanNewCfgCurHopLimit_Type()
)
vadcVlanNewCfgCurHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vadcVlanNewCfgCurHopLimit.setStatus("current")


class _VadcVlanNewCfgMFlag_Type(Integer32):
    """Custom type vadcVlanNewCfgMFlag based on Integer32"""
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


_VadcVlanNewCfgMFlag_Type.__name__ = "Integer32"
_VadcVlanNewCfgMFlag_Object = MibTableColumn
vadcVlanNewCfgMFlag = _VadcVlanNewCfgMFlag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1, 11),
    _VadcVlanNewCfgMFlag_Type()
)
vadcVlanNewCfgMFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vadcVlanNewCfgMFlag.setStatus("current")


class _VadcVlanNewCfgOFlag_Type(Integer32):
    """Custom type vadcVlanNewCfgOFlag based on Integer32"""
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


_VadcVlanNewCfgOFlag_Type.__name__ = "Integer32"
_VadcVlanNewCfgOFlag_Object = MibTableColumn
vadcVlanNewCfgOFlag = _VadcVlanNewCfgOFlag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1, 12),
    _VadcVlanNewCfgOFlag_Type()
)
vadcVlanNewCfgOFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vadcVlanNewCfgOFlag.setStatus("current")


class _VadcVlanNewCfgRTime_Type(Integer32):
    """Custom type vadcVlanNewCfgRTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_VadcVlanNewCfgRTime_Type.__name__ = "Integer32"
_VadcVlanNewCfgRTime_Object = MibTableColumn
vadcVlanNewCfgRTime = _VadcVlanNewCfgRTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1, 13),
    _VadcVlanNewCfgRTime_Type()
)
vadcVlanNewCfgRTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vadcVlanNewCfgRTime.setStatus("current")


class _VadcVlanNewCfgRlTime_Type(Integer32):
    """Custom type vadcVlanNewCfgRlTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
    )


_VadcVlanNewCfgRlTime_Type.__name__ = "Integer32"
_VadcVlanNewCfgRlTime_Object = MibTableColumn
vadcVlanNewCfgRlTime = _VadcVlanNewCfgRlTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1, 14),
    _VadcVlanNewCfgRlTime_Type()
)
vadcVlanNewCfgRlTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vadcVlanNewCfgRlTime.setStatus("current")


class _VadcVlanNewCfgPlTime_Type(Unsigned32):
    """Custom type vadcVlanNewCfgPlTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VadcVlanNewCfgPlTime_Type.__name__ = "Unsigned32"
_VadcVlanNewCfgPlTime_Object = MibTableColumn
vadcVlanNewCfgPlTime = _VadcVlanNewCfgPlTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1, 15),
    _VadcVlanNewCfgPlTime_Type()
)
vadcVlanNewCfgPlTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vadcVlanNewCfgPlTime.setStatus("current")


class _VadcVlanNewCfgVlTime_Type(Unsigned32):
    """Custom type vadcVlanNewCfgVlTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VadcVlanNewCfgVlTime_Type.__name__ = "Unsigned32"
_VadcVlanNewCfgVlTime_Object = MibTableColumn
vadcVlanNewCfgVlTime = _VadcVlanNewCfgVlTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1, 16),
    _VadcVlanNewCfgVlTime_Type()
)
vadcVlanNewCfgVlTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vadcVlanNewCfgVlTime.setStatus("current")


class _VadcVlanNewCfgOpInfo_Type(Integer32):
    """Custom type vadcVlanNewCfgOpInfo based on Integer32"""
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


_VadcVlanNewCfgOpInfo_Type.__name__ = "Integer32"
_VadcVlanNewCfgOpInfo_Object = MibTableColumn
vadcVlanNewCfgOpInfo = _VadcVlanNewCfgOpInfo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1, 17),
    _VadcVlanNewCfgOpInfo_Type()
)
vadcVlanNewCfgOpInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vadcVlanNewCfgOpInfo.setStatus("current")


class _VadcVlanNewCfgApInfo_Type(Integer32):
    """Custom type vadcVlanNewCfgApInfo based on Integer32"""
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


_VadcVlanNewCfgApInfo_Type.__name__ = "Integer32"
_VadcVlanNewCfgApInfo_Object = MibTableColumn
vadcVlanNewCfgApInfo = _VadcVlanNewCfgApInfo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 1, 10, 2, 1, 18),
    _VadcVlanNewCfgApInfo_Type()
)
vadcVlanNewCfgApInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vadcVlanNewCfgApInfo.setStatus("current")
_Layer2Stats_ObjectIdentity = ObjectIdentity
layer2Stats = _Layer2Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2)
)
_FdbStats_ObjectIdentity = ObjectIdentity
fdbStats = _FdbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 1)
)
_FdbStatsCreates_Type = Counter32
_FdbStatsCreates_Object = MibScalar
fdbStatsCreates = _FdbStatsCreates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 1, 1),
    _FdbStatsCreates_Type()
)
fdbStatsCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsCreates.setStatus("current")
_FdbStatsDeletes_Type = Counter32
_FdbStatsDeletes_Object = MibScalar
fdbStatsDeletes = _FdbStatsDeletes_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 1, 2),
    _FdbStatsDeletes_Type()
)
fdbStatsDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsDeletes.setStatus("current")
_FdbStatsCurrent_Type = Gauge32
_FdbStatsCurrent_Object = MibScalar
fdbStatsCurrent = _FdbStatsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 1, 3),
    _FdbStatsCurrent_Type()
)
fdbStatsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsCurrent.setStatus("current")
_FdbStatsHiwat_Type = Integer32
_FdbStatsHiwat_Object = MibScalar
fdbStatsHiwat = _FdbStatsHiwat_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 1, 4),
    _FdbStatsHiwat_Type()
)
fdbStatsHiwat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsHiwat.setStatus("current")
_FdbStatsLookups_Type = Counter32
_FdbStatsLookups_Object = MibScalar
fdbStatsLookups = _FdbStatsLookups_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 1, 5),
    _FdbStatsLookups_Type()
)
fdbStatsLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsLookups.setStatus("current")
_FdbStatsLookupFails_Type = Counter32
_FdbStatsLookupFails_Object = MibScalar
fdbStatsLookupFails = _FdbStatsLookupFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 1, 6),
    _FdbStatsLookupFails_Type()
)
fdbStatsLookupFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsLookupFails.setStatus("current")
_FdbStatsFinds_Type = Counter32
_FdbStatsFinds_Object = MibScalar
fdbStatsFinds = _FdbStatsFinds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 1, 7),
    _FdbStatsFinds_Type()
)
fdbStatsFinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsFinds.setStatus("current")
_FdbStatsFindFails_Type = Counter32
_FdbStatsFindFails_Object = MibScalar
fdbStatsFindFails = _FdbStatsFindFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 1, 8),
    _FdbStatsFindFails_Type()
)
fdbStatsFindFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsFindFails.setStatus("current")
_FdbStatsFindOrCreates_Type = Counter32
_FdbStatsFindOrCreates_Object = MibScalar
fdbStatsFindOrCreates = _FdbStatsFindOrCreates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 1, 9),
    _FdbStatsFindOrCreates_Type()
)
fdbStatsFindOrCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsFindOrCreates.setStatus("current")
_FdbStatsOverflows_Type = Counter32
_FdbStatsOverflows_Object = MibScalar
fdbStatsOverflows = _FdbStatsOverflows_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 1, 10),
    _FdbStatsOverflows_Type()
)
fdbStatsOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsOverflows.setStatus("current")
_StpStats_ObjectIdentity = ObjectIdentity
stpStats = _StpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 2)
)
_StgStatsPortTable_Object = MibTable
stgStatsPortTable = _StgStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    stgStatsPortTable.setStatus("current")
_StgStatsPortTableEntry_Object = MibTableRow
stgStatsPortTableEntry = _StgStatsPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 2, 1, 1)
)
stgStatsPortTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "stgStatsStpIndex"),
    (0, "ALTEON-CS-PHYSICAL-MIB", "stgStatsPortIndex"),
)
if mibBuilder.loadTexts:
    stgStatsPortTableEntry.setStatus("current")
_StgStatsStpIndex_Type = Integer32
_StgStatsStpIndex_Object = MibTableColumn
stgStatsStpIndex = _StgStatsStpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 2, 1, 1, 1),
    _StgStatsStpIndex_Type()
)
stgStatsStpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgStatsStpIndex.setStatus("current")
_StgStatsPortIndex_Type = Integer32
_StgStatsPortIndex_Object = MibTableColumn
stgStatsPortIndex = _StgStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 2, 1, 1, 2),
    _StgStatsPortIndex_Type()
)
stgStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgStatsPortIndex.setStatus("current")
_StgStatsPortRcvCfgBpdus_Type = Integer32
_StgStatsPortRcvCfgBpdus_Object = MibTableColumn
stgStatsPortRcvCfgBpdus = _StgStatsPortRcvCfgBpdus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 2, 1, 1, 3),
    _StgStatsPortRcvCfgBpdus_Type()
)
stgStatsPortRcvCfgBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgStatsPortRcvCfgBpdus.setStatus("current")
_StgStatsPortRcvTcnBpdus_Type = Integer32
_StgStatsPortRcvTcnBpdus_Object = MibTableColumn
stgStatsPortRcvTcnBpdus = _StgStatsPortRcvTcnBpdus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 2, 1, 1, 4),
    _StgStatsPortRcvTcnBpdus_Type()
)
stgStatsPortRcvTcnBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgStatsPortRcvTcnBpdus.setStatus("current")
_StgStatsPortXmtCfgBpdus_Type = Integer32
_StgStatsPortXmtCfgBpdus_Object = MibTableColumn
stgStatsPortXmtCfgBpdus = _StgStatsPortXmtCfgBpdus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 2, 1, 1, 5),
    _StgStatsPortXmtCfgBpdus_Type()
)
stgStatsPortXmtCfgBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgStatsPortXmtCfgBpdus.setStatus("current")
_StgStatsPortXmtTcnBpdus_Type = Integer32
_StgStatsPortXmtTcnBpdus_Object = MibTableColumn
stgStatsPortXmtTcnBpdus = _StgStatsPortXmtTcnBpdus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 2, 2, 1, 1, 6),
    _StgStatsPortXmtTcnBpdus_Type()
)
stgStatsPortXmtTcnBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stgStatsPortXmtTcnBpdus.setStatus("current")
_Layer2Info_ObjectIdentity = ObjectIdentity
layer2Info = _Layer2Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3)
)
_FdbInfo_ObjectIdentity = ObjectIdentity
fdbInfo = _FdbInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 1)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 1, 1),
    _FdbClear_Type()
)
fdbClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbClear.setStatus("current")
_FdbTable_Object = MibTable
fdbTable = _FdbTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    fdbTable.setStatus("current")
_FdbEntry_Object = MibTableRow
fdbEntry = _FdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 1, 2, 1)
)
fdbEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "fdbMacAddr"),
)
if mibBuilder.loadTexts:
    fdbEntry.setStatus("current")
_FdbMacAddr_Type = PhysAddress
_FdbMacAddr_Object = MibTableColumn
fdbMacAddr = _FdbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 1, 2, 1, 1),
    _FdbMacAddr_Type()
)
fdbMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbMacAddr.setStatus("current")
_FdbVlan_Type = Integer32
_FdbVlan_Object = MibTableColumn
fdbVlan = _FdbVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 1, 2, 1, 2),
    _FdbVlan_Type()
)
fdbVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbVlan.setStatus("current")
_FdbSrcPort_Type = Integer32
_FdbSrcPort_Object = MibTableColumn
fdbSrcPort = _FdbSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 1, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 1, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 1, 2, 1, 5),
    _FdbRefSps_Type()
)
fdbRefSps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbRefSps.setStatus("current")
_FdbLearnedPort_Type = Integer32
_FdbLearnedPort_Object = MibTableColumn
fdbLearnedPort = _FdbLearnedPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 1, 2, 1, 6),
    _FdbLearnedPort_Type()
)
fdbLearnedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbLearnedPort.setStatus("current")
_FdbSrcTrunk_Type = Integer32
_FdbSrcTrunk_Object = MibTableColumn
fdbSrcTrunk = _FdbSrcTrunk_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 1, 2, 1, 7),
    _FdbSrcTrunk_Type()
)
fdbSrcTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbSrcTrunk.setStatus("current")
_StpInfo_ObjectIdentity = ObjectIdentity
stpInfo = _StpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2)
)
_StpInfoTable_Object = MibTable
stpInfoTable = _StpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    stpInfoTable.setStatus("current")
_StpInfoTableEntry_Object = MibTableRow
stpInfoTableEntry = _StpInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 1, 1)
)
stpInfoTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "stpInfoIndex"),
)
if mibBuilder.loadTexts:
    stpInfoTableEntry.setStatus("current")
_StpInfoIndex_Type = Integer32
_StpInfoIndex_Object = MibTableColumn
stpInfoIndex = _StpInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 1, 1, 1),
    _StpInfoIndex_Type()
)
stpInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoIndex.setStatus("current")
_StpInfoTimeSinceTopChange_Type = TimeTicks
_StpInfoTimeSinceTopChange_Object = MibTableColumn
stpInfoTimeSinceTopChange = _StpInfoTimeSinceTopChange_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 1, 1, 2),
    _StpInfoTimeSinceTopChange_Type()
)
stpInfoTimeSinceTopChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoTimeSinceTopChange.setStatus("current")
_StpInfoTopChanges_Type = Counter32
_StpInfoTopChanges_Object = MibTableColumn
stpInfoTopChanges = _StpInfoTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 1, 1, 3),
    _StpInfoTopChanges_Type()
)
stpInfoTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoTopChanges.setStatus("current")
_StpInfoDesignatedRoot_Type = BridgeId
_StpInfoDesignatedRoot_Object = MibTableColumn
stpInfoDesignatedRoot = _StpInfoDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 1, 1, 4),
    _StpInfoDesignatedRoot_Type()
)
stpInfoDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoDesignatedRoot.setStatus("current")
_StpInfoRootCost_Type = Integer32
_StpInfoRootCost_Object = MibTableColumn
stpInfoRootCost = _StpInfoRootCost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 1, 1, 5),
    _StpInfoRootCost_Type()
)
stpInfoRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoRootCost.setStatus("current")
_StpInfoRootPort_Type = Integer32
_StpInfoRootPort_Object = MibTableColumn
stpInfoRootPort = _StpInfoRootPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 1, 1, 6),
    _StpInfoRootPort_Type()
)
stpInfoRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoRootPort.setStatus("current")
_StpInfoMaxAge_Type = Integer32
_StpInfoMaxAge_Object = MibTableColumn
stpInfoMaxAge = _StpInfoMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 1, 1, 7),
    _StpInfoMaxAge_Type()
)
stpInfoMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoMaxAge.setStatus("current")
_StpInfoHelloTime_Type = Integer32
_StpInfoHelloTime_Object = MibTableColumn
stpInfoHelloTime = _StpInfoHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 1, 1, 8),
    _StpInfoHelloTime_Type()
)
stpInfoHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoHelloTime.setStatus("current")
_StpInfoForwardDelay_Type = Integer32
_StpInfoForwardDelay_Object = MibTableColumn
stpInfoForwardDelay = _StpInfoForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 1, 1, 9),
    _StpInfoForwardDelay_Type()
)
stpInfoForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoForwardDelay.setStatus("current")
_StpInfoHoldTime_Type = Integer32
_StpInfoHoldTime_Object = MibTableColumn
stpInfoHoldTime = _StpInfoHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 1, 1, 10),
    _StpInfoHoldTime_Type()
)
stpInfoHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoHoldTime.setStatus("current")
_StpInfoPortTable_Object = MibTable
stpInfoPortTable = _StpInfoPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    stpInfoPortTable.setStatus("current")
_StpInfoPortTableEntry_Object = MibTableRow
stpInfoPortTableEntry = _StpInfoPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 2, 1)
)
stpInfoPortTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "stpInfoPortStpIndex"),
    (0, "ALTEON-CS-PHYSICAL-MIB", "stpInfoPortIndex"),
)
if mibBuilder.loadTexts:
    stpInfoPortTableEntry.setStatus("current")
_StpInfoPortStpIndex_Type = Integer32
_StpInfoPortStpIndex_Object = MibTableColumn
stpInfoPortStpIndex = _StpInfoPortStpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 2, 1, 1),
    _StpInfoPortStpIndex_Type()
)
stpInfoPortStpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortStpIndex.setStatus("current")
_StpInfoPortIndex_Type = Integer32
_StpInfoPortIndex_Object = MibTableColumn
stpInfoPortIndex = _StpInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 2, 1, 2),
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
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("discarding", 7),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_StpInfoPortState_Type.__name__ = "Integer32"
_StpInfoPortState_Object = MibTableColumn
stpInfoPortState = _StpInfoPortState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 2, 1, 3),
    _StpInfoPortState_Type()
)
stpInfoPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortState.setStatus("current")
_StpInfoPortDesignatedRoot_Type = BridgeId
_StpInfoPortDesignatedRoot_Object = MibTableColumn
stpInfoPortDesignatedRoot = _StpInfoPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 2, 1, 4),
    _StpInfoPortDesignatedRoot_Type()
)
stpInfoPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortDesignatedRoot.setStatus("current")
_StpInfoPortDesignatedCost_Type = Integer32
_StpInfoPortDesignatedCost_Object = MibTableColumn
stpInfoPortDesignatedCost = _StpInfoPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 2, 1, 5),
    _StpInfoPortDesignatedCost_Type()
)
stpInfoPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortDesignatedCost.setStatus("current")
_StpInfoPortDesignatedBridge_Type = BridgeId
_StpInfoPortDesignatedBridge_Object = MibTableColumn
stpInfoPortDesignatedBridge = _StpInfoPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 2, 1, 7),
    _StpInfoPortDesignatedPort_Type()
)
stpInfoPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortDesignatedPort.setStatus("current")
_StpInfoPortForwardTransitions_Type = Counter32
_StpInfoPortForwardTransitions_Object = MibTableColumn
stpInfoPortForwardTransitions = _StpInfoPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 2, 1, 8),
    _StpInfoPortForwardTransitions_Type()
)
stpInfoPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortForwardTransitions.setStatus("current")
_StpInfoPortPathCost_Type = Integer32
_StpInfoPortPathCost_Object = MibTableColumn
stpInfoPortPathCost = _StpInfoPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 2, 1, 9),
    _StpInfoPortPathCost_Type()
)
stpInfoPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortPathCost.setStatus("current")


class _StpInfoPortRole_Type(Integer32):
    """Custom type stpInfoPortRole based on Integer32"""
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


_StpInfoPortRole_Type.__name__ = "Integer32"
_StpInfoPortRole_Object = MibTableColumn
stpInfoPortRole = _StpInfoPortRole_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 2, 1, 10),
    _StpInfoPortRole_Type()
)
stpInfoPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortRole.setStatus("current")


class _StpInfoPortLinkType_Type(Integer32):
    """Custom type stpInfoPortLinkType based on Integer32"""
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


_StpInfoPortLinkType_Type.__name__ = "Integer32"
_StpInfoPortLinkType_Object = MibTableColumn
stpInfoPortLinkType = _StpInfoPortLinkType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 2, 1, 11),
    _StpInfoPortLinkType_Type()
)
stpInfoPortLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortLinkType.setStatus("current")


class _StpInfoPortEdge_Type(Integer32):
    """Custom type stpInfoPortEdge based on Integer32"""
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


_StpInfoPortEdge_Type.__name__ = "Integer32"
_StpInfoPortEdge_Object = MibTableColumn
stpInfoPortEdge = _StpInfoPortEdge_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 2, 2, 1, 12),
    _StpInfoPortEdge_Type()
)
stpInfoPortEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInfoPortEdge.setStatus("current")
_LacpInfo_ObjectIdentity = ObjectIdentity
lacpInfo = _LacpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 3)
)
_LacpInfoPortTable_Object = MibTable
lacpInfoPortTable = _LacpInfoPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    lacpInfoPortTable.setStatus("current")
_LacpInfoPortTableEntry_Object = MibTableRow
lacpInfoPortTableEntry = _LacpInfoPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 3, 1, 1)
)
lacpInfoPortTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "lacpInfoPortIndex"),
)
if mibBuilder.loadTexts:
    lacpInfoPortTableEntry.setStatus("current")
_LacpInfoPortIndex_Type = Integer32
_LacpInfoPortIndex_Object = MibTableColumn
lacpInfoPortIndex = _LacpInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 3, 1, 1, 5),
    _LacpInfoPortMoved_Type()
)
lacpInfoPortMoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpInfoPortMoved.setStatus("current")
_CistInfo_ObjectIdentity = ObjectIdentity
cistInfo = _CistInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4)
)
_CistGeneralInfo_ObjectIdentity = ObjectIdentity
cistGeneralInfo = _CistGeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 1)
)
_CistRoot_Type = BridgeId
_CistRoot_Object = MibScalar
cistRoot = _CistRoot_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 1, 1),
    _CistRoot_Type()
)
cistRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistRoot.setStatus("current")
_CistRootPathCost_Type = Integer32
_CistRootPathCost_Object = MibScalar
cistRootPathCost = _CistRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 1, 2),
    _CistRootPathCost_Type()
)
cistRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistRootPathCost.setStatus("current")
_CistRootPort_Type = Integer32
_CistRootPort_Object = MibScalar
cistRootPort = _CistRootPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 1, 3),
    _CistRootPort_Type()
)
cistRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistRootPort.setStatus("current")
_CistBridgeHelloTime_Type = Integer32
_CistBridgeHelloTime_Object = MibScalar
cistBridgeHelloTime = _CistBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 1, 4),
    _CistBridgeHelloTime_Type()
)
cistBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistBridgeHelloTime.setStatus("current")
_CistBridgeMaxAge_Type = Integer32
_CistBridgeMaxAge_Object = MibScalar
cistBridgeMaxAge = _CistBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 1, 5),
    _CistBridgeMaxAge_Type()
)
cistBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistBridgeMaxAge.setStatus("current")
_CistBridgeForwardDelay_Type = Integer32
_CistBridgeForwardDelay_Object = MibScalar
cistBridgeForwardDelay = _CistBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 1, 6),
    _CistBridgeForwardDelay_Type()
)
cistBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistBridgeForwardDelay.setStatus("current")
_CistRegionalRoot_Type = BridgeId
_CistRegionalRoot_Object = MibScalar
cistRegionalRoot = _CistRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 1, 7),
    _CistRegionalRoot_Type()
)
cistRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistRegionalRoot.setStatus("current")
_CistRegionalPathCost_Type = Integer32
_CistRegionalPathCost_Object = MibScalar
cistRegionalPathCost = _CistRegionalPathCost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 1, 8),
    _CistRegionalPathCost_Type()
)
cistRegionalPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistRegionalPathCost.setStatus("current")
_CistInfoPortTable_Object = MibTable
cistInfoPortTable = _CistInfoPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 2)
)
if mibBuilder.loadTexts:
    cistInfoPortTable.setStatus("current")
_CistInfoPortTableEntry_Object = MibTableRow
cistInfoPortTableEntry = _CistInfoPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 2, 1)
)
cistInfoPortTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "cistInfoPortIndex"),
)
if mibBuilder.loadTexts:
    cistInfoPortTableEntry.setStatus("current")
_CistInfoPortIndex_Type = Integer32
_CistInfoPortIndex_Object = MibTableColumn
cistInfoPortIndex = _CistInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 2, 1, 1),
    _CistInfoPortIndex_Type()
)
cistInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistInfoPortIndex.setStatus("current")
_CistInfoPortPriority_Type = Integer32
_CistInfoPortPriority_Object = MibTableColumn
cistInfoPortPriority = _CistInfoPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 2, 1, 2),
    _CistInfoPortPriority_Type()
)
cistInfoPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistInfoPortPriority.setStatus("current")
_CistInfoPortPathCost_Type = Integer32
_CistInfoPortPathCost_Object = MibTableColumn
cistInfoPortPathCost = _CistInfoPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 2, 1, 5),
    _CistInfoPortRole_Type()
)
cistInfoPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistInfoPortRole.setStatus("current")
_CistInfoPortDesignatedBridge_Type = BridgeId
_CistInfoPortDesignatedBridge_Object = MibTableColumn
cistInfoPortDesignatedBridge = _CistInfoPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 4, 2, 1, 8),
    _CistInfoPortLinkType_Type()
)
cistInfoPortLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cistInfoPortLinkType.setStatus("current")
_VlanInfo_ObjectIdentity = ObjectIdentity
vlanInfo = _VlanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 5)
)
_VlanInfoTable_Object = MibTable
vlanInfoTable = _VlanInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    vlanInfoTable.setStatus("current")
_VlanInfoTableEntry_Object = MibTableRow
vlanInfoTableEntry = _VlanInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 5, 1, 1)
)
vlanInfoTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "vlanInfoId"),
)
if mibBuilder.loadTexts:
    vlanInfoTableEntry.setStatus("current")


class _VlanInfoId_Type(Integer32):
    """Custom type vlanInfoId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4090),
    )


_VlanInfoId_Type.__name__ = "Integer32"
_VlanInfoId_Object = MibTableColumn
vlanInfoId = _VlanInfoId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 5, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 5, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 5, 1, 1, 3),
    _VlanInfoStatus_Type()
)
vlanInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanInfoStatus.setStatus("current")


class _VlanInfoJumbo_Type(Integer32):
    """Custom type vlanInfoJumbo based on Integer32"""
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


_VlanInfoJumbo_Type.__name__ = "Integer32"
_VlanInfoJumbo_Object = MibTableColumn
vlanInfoJumbo = _VlanInfoJumbo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 5, 1, 1, 4),
    _VlanInfoJumbo_Type()
)
vlanInfoJumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanInfoJumbo.setStatus("current")
_VlanInfoBwmContract_Type = Integer32
_VlanInfoBwmContract_Object = MibTableColumn
vlanInfoBwmContract = _VlanInfoBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 5, 1, 1, 5),
    _VlanInfoBwmContract_Type()
)
vlanInfoBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanInfoBwmContract.setStatus("current")


class _VlanInfoLearn_Type(Integer32):
    """Custom type vlanInfoLearn based on Integer32"""
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


_VlanInfoLearn_Type.__name__ = "Integer32"
_VlanInfoLearn_Object = MibTableColumn
vlanInfoLearn = _VlanInfoLearn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 5, 1, 1, 6),
    _VlanInfoLearn_Type()
)
vlanInfoLearn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanInfoLearn.setStatus("current")
_VlanInfoPorts_Type = OctetString
_VlanInfoPorts_Object = MibTableColumn
vlanInfoPorts = _VlanInfoPorts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 5, 1, 1, 7),
    _VlanInfoPorts_Type()
)
vlanInfoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanInfoPorts.setStatus("current")
_VlanInfoTableVADC_Object = MibTable
vlanInfoTableVADC = _VlanInfoTableVADC_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 5, 2)
)
if mibBuilder.loadTexts:
    vlanInfoTableVADC.setStatus("current")
_VlanInfoTableVADCEntry_Object = MibTableRow
vlanInfoTableVADCEntry = _VlanInfoTableVADCEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 5, 2, 1)
)
vlanInfoTableVADCEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "vlanInfoIdx"),
)
if mibBuilder.loadTexts:
    vlanInfoTableVADCEntry.setStatus("current")


class _VlanInfoIdx_Type(Integer32):
    """Custom type vlanInfoIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4090),
    )


_VlanInfoIdx_Type.__name__ = "Integer32"
_VlanInfoIdx_Object = MibTableColumn
vlanInfoIdx = _VlanInfoIdx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 5, 2, 1, 1),
    _VlanInfoIdx_Type()
)
vlanInfoIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanInfoIdx.setStatus("current")


class _VlanInfoVADC_Type(DisplayString):
    """Custom type vlanInfoVADC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VlanInfoVADC_Type.__name__ = "DisplayString"
_VlanInfoVADC_Object = MibTableColumn
vlanInfoVADC = _VlanInfoVADC_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 5, 2, 1, 2),
    _VlanInfoVADC_Type()
)
vlanInfoVADC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanInfoVADC.setStatus("current")
_PortTeamInfo_ObjectIdentity = ObjectIdentity
portTeamInfo = _PortTeamInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 6)
)
_PortTeamInfoTable_Object = MibTable
portTeamInfoTable = _PortTeamInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 6, 1)
)
if mibBuilder.loadTexts:
    portTeamInfoTable.setStatus("current")
_PortTeamInfoTableEntry_Object = MibTableRow
portTeamInfoTableEntry = _PortTeamInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 6, 1, 1)
)
portTeamInfoTableEntry.setIndexNames(
    (0, "ALTEON-CS-PHYSICAL-MIB", "portTeamInfoIndex"),
)
if mibBuilder.loadTexts:
    portTeamInfoTableEntry.setStatus("current")
_PortTeamInfoIndex_Type = Integer32
_PortTeamInfoIndex_Object = MibTableColumn
portTeamInfoIndex = _PortTeamInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 6, 1, 1, 1),
    _PortTeamInfoIndex_Type()
)
portTeamInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTeamInfoIndex.setStatus("current")


class _PortTeamInfoState_Type(Integer32):
    """Custom type portTeamInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("off", 1),
          ("passive", 2))
    )


_PortTeamInfoState_Type.__name__ = "Integer32"
_PortTeamInfoState_Object = MibTableColumn
portTeamInfoState = _PortTeamInfoState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 6, 1, 1, 2),
    _PortTeamInfoState_Type()
)
portTeamInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTeamInfoState.setStatus("current")
_PortTeamInfoPorts_Type = OctetString
_PortTeamInfoPorts_Object = MibTableColumn
portTeamInfoPorts = _PortTeamInfoPorts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 6, 1, 1, 3),
    _PortTeamInfoPorts_Type()
)
portTeamInfoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTeamInfoPorts.setStatus("current")
_PortTeamInfoPortsState_Type = OctetString
_PortTeamInfoPortsState_Object = MibTableColumn
portTeamInfoPortsState = _PortTeamInfoPortsState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 6, 1, 1, 4),
    _PortTeamInfoPortsState_Type()
)
portTeamInfoPortsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTeamInfoPortsState.setStatus("current")
_PortTeamInfoTrunks_Type = OctetString
_PortTeamInfoTrunks_Object = MibTableColumn
portTeamInfoTrunks = _PortTeamInfoTrunks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 6, 1, 1, 5),
    _PortTeamInfoTrunks_Type()
)
portTeamInfoTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTeamInfoTrunks.setStatus("current")
_PortTeamInfoTrunksState_Type = OctetString
_PortTeamInfoTrunksState_Object = MibTableColumn
portTeamInfoTrunksState = _PortTeamInfoTrunksState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 6, 1, 1, 6),
    _PortTeamInfoTrunksState_Type()
)
portTeamInfoTrunksState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTeamInfoTrunksState.setStatus("current")
_PortTeamInfoMaster_Type = DisplayString
_PortTeamInfoMaster_Object = MibTableColumn
portTeamInfoMaster = _PortTeamInfoMaster_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 3, 6, 1, 1, 7),
    _PortTeamInfoMaster_Type()
)
portTeamInfoMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTeamInfoMaster.setStatus("current")
_Layer2Oper_ObjectIdentity = ObjectIdentity
layer2Oper = _Layer2Oper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 2, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTEON-CS-PHYSICAL-MIB",
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
       "vlanCurCfgBwmContract": vlanCurCfgBwmContract,
       "vlanCurCfgStg": vlanCurCfgStg,
       "vlanCurCfgJumbo": vlanCurCfgJumbo,
       "vlanCurCfgLearn": vlanCurCfgLearn,
       "vlanCurCfgShared": vlanCurCfgShared,
       "vlanCurCfgIpv6LlaGen": vlanCurCfgIpv6LlaGen,
       "vlanCurCfgRouterAdv": vlanCurCfgRouterAdv,
       "vlanCurCfgReTransInt": vlanCurCfgReTransInt,
       "vlanCurCfgMinIntBwAdv": vlanCurCfgMinIntBwAdv,
       "vlanCurCfgMaxIntBwAdv": vlanCurCfgMaxIntBwAdv,
       "vlanCurCfgMtu": vlanCurCfgMtu,
       "vlanCurCfgCurHopLimit": vlanCurCfgCurHopLimit,
       "vlanCurCfgMFlag": vlanCurCfgMFlag,
       "vlanCurCfgOFlag": vlanCurCfgOFlag,
       "vlanCurCfgRTime": vlanCurCfgRTime,
       "vlanCurCfgRlTime": vlanCurCfgRlTime,
       "vlanCurCfgPlTime": vlanCurCfgPlTime,
       "vlanCurCfgVlTime": vlanCurCfgVlTime,
       "vlanCurCfgOpInfo": vlanCurCfgOpInfo,
       "vlanCurCfgApInfo": vlanCurCfgApInfo,
       "vlanNewCfgTable": vlanNewCfgTable,
       "vlanNewCfgTableEntry": vlanNewCfgTableEntry,
       "vlanNewCfgVlanId": vlanNewCfgVlanId,
       "vlanNewCfgVlanName": vlanNewCfgVlanName,
       "vlanNewCfgPorts": vlanNewCfgPorts,
       "vlanNewCfgState": vlanNewCfgState,
       "vlanNewCfgAddPort": vlanNewCfgAddPort,
       "vlanNewCfgRemovePort": vlanNewCfgRemovePort,
       "vlanNewCfgDelete": vlanNewCfgDelete,
       "vlanNewCfgBwmContract": vlanNewCfgBwmContract,
       "vlanNewCfgStg": vlanNewCfgStg,
       "vlanNewCfgJumbo": vlanNewCfgJumbo,
       "vlanNewCfgLearn": vlanNewCfgLearn,
       "vlanNewCfgShared": vlanNewCfgShared,
       "vlanNewCfgIpv6LlaGen": vlanNewCfgIpv6LlaGen,
       "vlanNewCfgRouterAdv": vlanNewCfgRouterAdv,
       "vlanNewCfgReTransInt": vlanNewCfgReTransInt,
       "vlanNewCfgMinIntBwAdv": vlanNewCfgMinIntBwAdv,
       "vlanNewCfgMaxIntBwAdv": vlanNewCfgMaxIntBwAdv,
       "vlanNewCfgMtu": vlanNewCfgMtu,
       "vlanNewCfgCurHopLimit": vlanNewCfgCurHopLimit,
       "vlanNewCfgMFlag": vlanNewCfgMFlag,
       "vlanNewCfgOFlag": vlanNewCfgOFlag,
       "vlanNewCfgRTime": vlanNewCfgRTime,
       "vlanNewCfgRlTime": vlanNewCfgRlTime,
       "vlanNewCfgPlTime": vlanNewCfgPlTime,
       "vlanNewCfgVlTime": vlanNewCfgVlTime,
       "vlanNewCfgOpInfo": vlanNewCfgOpInfo,
       "vlanNewCfgApInfo": vlanNewCfgApInfo,
       "vlanMaxVlanID": vlanMaxVlanID,
       "trunkgroup": trunkgroup,
       "trunkGroupTableMaxSize": trunkGroupTableMaxSize,
       "trunkGroupCurCfgTable": trunkGroupCurCfgTable,
       "trunkGroupCurCfgTableEntry": trunkGroupCurCfgTableEntry,
       "trunkGroupCurCfgIndex": trunkGroupCurCfgIndex,
       "trunkGroupCurCfgPorts": trunkGroupCurCfgPorts,
       "trunkGroupCurCfgState": trunkGroupCurCfgState,
       "trunkGroupCurCfgBwmContract": trunkGroupCurCfgBwmContract,
       "trunkGroupCurCfgName": trunkGroupCurCfgName,
       "trunkGroupNewCfgTable": trunkGroupNewCfgTable,
       "trunkGroupNewCfgTableEntry": trunkGroupNewCfgTableEntry,
       "trunkGroupNewCfgIndex": trunkGroupNewCfgIndex,
       "trunkGroupNewCfgPorts": trunkGroupNewCfgPorts,
       "trunkGroupNewCfgAddPort": trunkGroupNewCfgAddPort,
       "trunkGroupNewCfgRemovePort": trunkGroupNewCfgRemovePort,
       "trunkGroupNewCfgState": trunkGroupNewCfgState,
       "trunkGroupNewCfgDelete": trunkGroupNewCfgDelete,
       "trunkGroupNewCfgBwmContract": trunkGroupNewCfgBwmContract,
       "trunkGroupNewCfgName": trunkGroupNewCfgName,
       "stgCfg": stgCfg,
       "stgCurCfgTable": stgCurCfgTable,
       "stgCurCfgTableEntry": stgCurCfgTableEntry,
       "stgCurCfgIndex": stgCurCfgIndex,
       "stgCurCfgState": stgCurCfgState,
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
       "stgNewCfgPortTable": stgNewCfgPortTable,
       "stgNewCfgPortTableEntry": stgNewCfgPortTableEntry,
       "stgNewCfgStgIndex": stgNewCfgStgIndex,
       "stgNewCfgPortIndex": stgNewCfgPortIndex,
       "stgNewCfgPortState": stgNewCfgPortState,
       "stgNewCfgPortPriority": stgNewCfgPortPriority,
       "stgNewCfgPortPathCost": stgNewCfgPortPathCost,
       "stgNewCfgPortLink": stgNewCfgPortLink,
       "stgNewCfgPortEdge": stgNewCfgPortEdge,
       "mirroring": mirroring,
       "mirrPortMirr": mirrPortMirr,
       "pmCurCfgPortMirrState": pmCurCfgPortMirrState,
       "pmNewCfgPortMirrState": pmNewCfgPortMirrState,
       "pmCurCfgPortMonitorTable": pmCurCfgPortMonitorTable,
       "pmCurCfgPortMonitorEntry": pmCurCfgPortMonitorEntry,
       "pmCurCfgPmirrMoniPortIndex": pmCurCfgPmirrMoniPortIndex,
       "pmCurCfgPmirrMirrPortIndex": pmCurCfgPmirrMirrPortIndex,
       "pmCurCfgPmirrDirection": pmCurCfgPmirrDirection,
       "pmCurCfgPmirrPortVlansBmap": pmCurCfgPmirrPortVlansBmap,
       "pmNewCfgPortMonitorTable": pmNewCfgPortMonitorTable,
       "pmNewCfgPortMonitorEntry": pmNewCfgPortMonitorEntry,
       "pmNewCfgPmirrMoniPortIndex": pmNewCfgPmirrMoniPortIndex,
       "pmNewCfgPmirrMirrPortIndex": pmNewCfgPmirrMirrPortIndex,
       "pmNewCfgPmirrDirection": pmNewCfgPmirrDirection,
       "pmNewCfgPmirrDelete": pmNewCfgPmirrDelete,
       "pmNewCfgAddVlan": pmNewCfgAddVlan,
       "pmNewCfgRemoveVlan": pmNewCfgRemoveVlan,
       "pmNewCfgPmirrPortVlansBmap": pmNewCfgPmirrPortVlansBmap,
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
       "lacpCurSystemName": lacpCurSystemName,
       "lacpNewSystemName": lacpNewSystemName,
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
       "portTeamCfg": portTeamCfg,
       "portTeamTableMaxSize": portTeamTableMaxSize,
       "portTeamCurCfgTable": portTeamCurCfgTable,
       "portTeamCurCfgTableEntry": portTeamCurCfgTableEntry,
       "portTeamCurCfgIndex": portTeamCurCfgIndex,
       "portTeamCurCfgState": portTeamCurCfgState,
       "portTeamCurCfgPorts": portTeamCurCfgPorts,
       "portTeamCurCfgTrunks": portTeamCurCfgTrunks,
       "portTeamCurCfgName": portTeamCurCfgName,
       "portTeamNewCfgTable": portTeamNewCfgTable,
       "portTeamNewCfgTableEntry": portTeamNewCfgTableEntry,
       "portTeamNewCfgIndex": portTeamNewCfgIndex,
       "portTeamNewCfgState": portTeamNewCfgState,
       "portTeamNewCfgPorts": portTeamNewCfgPorts,
       "portTeamNewCfgAddPort": portTeamNewCfgAddPort,
       "portTeamNewCfgRemovePort": portTeamNewCfgRemovePort,
       "portTeamNewCfgTrunks": portTeamNewCfgTrunks,
       "portTeamNewCfgAddTrunk": portTeamNewCfgAddTrunk,
       "portTeamNewCfgRemoveTrunk": portTeamNewCfgRemoveTrunk,
       "portTeamNewCfgDelete": portTeamNewCfgDelete,
       "portTeamNewCfgName": portTeamNewCfgName,
       "vadcVlan": vadcVlan,
       "vadcVlanCurCfgTable": vadcVlanCurCfgTable,
       "vadcVlanCurCfgTableEntry": vadcVlanCurCfgTableEntry,
       "vadcVlanCurCfgVlanId": vadcVlanCurCfgVlanId,
       "vadcVlanCurCfgBwmCont": vadcVlanCurCfgBwmCont,
       "vadcVlanCurCfgNonIp": vadcVlanCurCfgNonIp,
       "vadcVlanCurCfgIpv6LlaGen": vadcVlanCurCfgIpv6LlaGen,
       "vadcVlanCurCfgRouterAdv": vadcVlanCurCfgRouterAdv,
       "vadcVlanCurCfgReTransInt": vadcVlanCurCfgReTransInt,
       "vadcVlanCurCfgMinIntBwAdv": vadcVlanCurCfgMinIntBwAdv,
       "vadcVlanCurCfgMaxIntBwAdv": vadcVlanCurCfgMaxIntBwAdv,
       "vadcVlanCurCfgMtu": vadcVlanCurCfgMtu,
       "vadcVlanCurCfgCurHopLimit": vadcVlanCurCfgCurHopLimit,
       "vadcVlanCurCfgMFlag": vadcVlanCurCfgMFlag,
       "vadcVlanCurCfgOFlag": vadcVlanCurCfgOFlag,
       "vadcVlanCurCfgRTime": vadcVlanCurCfgRTime,
       "vadcVlanCurCfgRlTime": vadcVlanCurCfgRlTime,
       "vadcVlanCurCfgPlTime": vadcVlanCurCfgPlTime,
       "vadcVlanCurCfgVlTime": vadcVlanCurCfgVlTime,
       "vadcVlanCurCfgOpInfo": vadcVlanCurCfgOpInfo,
       "vadcVlanCurCfgApInfo": vadcVlanCurCfgApInfo,
       "vadcVlanNewCfgTable": vadcVlanNewCfgTable,
       "vadcVlanNewCfgTableEntry": vadcVlanNewCfgTableEntry,
       "vadcVlanNewCfgVlanId": vadcVlanNewCfgVlanId,
       "vadcVlanNewCfgBwmCont": vadcVlanNewCfgBwmCont,
       "vadcVlanNewCfgNonIp": vadcVlanNewCfgNonIp,
       "vadcVlanNewCfgIpv6LlaGen": vadcVlanNewCfgIpv6LlaGen,
       "vadcVlanNewCfgRouterAdv": vadcVlanNewCfgRouterAdv,
       "vadcVlanNewCfgReTransInt": vadcVlanNewCfgReTransInt,
       "vadcVlanNewCfgMinIntBwAdv": vadcVlanNewCfgMinIntBwAdv,
       "vadcVlanNewCfgMaxIntBwAdv": vadcVlanNewCfgMaxIntBwAdv,
       "vadcVlanNewCfgMtu": vadcVlanNewCfgMtu,
       "vadcVlanNewCfgCurHopLimit": vadcVlanNewCfgCurHopLimit,
       "vadcVlanNewCfgMFlag": vadcVlanNewCfgMFlag,
       "vadcVlanNewCfgOFlag": vadcVlanNewCfgOFlag,
       "vadcVlanNewCfgRTime": vadcVlanNewCfgRTime,
       "vadcVlanNewCfgRlTime": vadcVlanNewCfgRlTime,
       "vadcVlanNewCfgPlTime": vadcVlanNewCfgPlTime,
       "vadcVlanNewCfgVlTime": vadcVlanNewCfgVlTime,
       "vadcVlanNewCfgOpInfo": vadcVlanNewCfgOpInfo,
       "vadcVlanNewCfgApInfo": vadcVlanNewCfgApInfo,
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
       "layer2Info": layer2Info,
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
       "stpInfoTimeSinceTopChange": stpInfoTimeSinceTopChange,
       "stpInfoTopChanges": stpInfoTopChanges,
       "stpInfoDesignatedRoot": stpInfoDesignatedRoot,
       "stpInfoRootCost": stpInfoRootCost,
       "stpInfoRootPort": stpInfoRootPort,
       "stpInfoMaxAge": stpInfoMaxAge,
       "stpInfoHelloTime": stpInfoHelloTime,
       "stpInfoForwardDelay": stpInfoForwardDelay,
       "stpInfoHoldTime": stpInfoHoldTime,
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
       "stpInfoPortRole": stpInfoPortRole,
       "stpInfoPortLinkType": stpInfoPortLinkType,
       "stpInfoPortEdge": stpInfoPortEdge,
       "lacpInfo": lacpInfo,
       "lacpInfoPortTable": lacpInfoPortTable,
       "lacpInfoPortTableEntry": lacpInfoPortTableEntry,
       "lacpInfoPortIndex": lacpInfoPortIndex,
       "lacpInfoPortSelected": lacpInfoPortSelected,
       "lacpInfoPortNtt": lacpInfoPortNtt,
       "lacpInfoPortReadyN": lacpInfoPortReadyN,
       "lacpInfoPortMoved": lacpInfoPortMoved,
       "cistInfo": cistInfo,
       "cistGeneralInfo": cistGeneralInfo,
       "cistRoot": cistRoot,
       "cistRootPathCost": cistRootPathCost,
       "cistRootPort": cistRootPort,
       "cistBridgeHelloTime": cistBridgeHelloTime,
       "cistBridgeMaxAge": cistBridgeMaxAge,
       "cistBridgeForwardDelay": cistBridgeForwardDelay,
       "cistRegionalRoot": cistRegionalRoot,
       "cistRegionalPathCost": cistRegionalPathCost,
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
       "vlanInfo": vlanInfo,
       "vlanInfoTable": vlanInfoTable,
       "vlanInfoTableEntry": vlanInfoTableEntry,
       "vlanInfoId": vlanInfoId,
       "vlanInfoName": vlanInfoName,
       "vlanInfoStatus": vlanInfoStatus,
       "vlanInfoJumbo": vlanInfoJumbo,
       "vlanInfoBwmContract": vlanInfoBwmContract,
       "vlanInfoLearn": vlanInfoLearn,
       "vlanInfoPorts": vlanInfoPorts,
       "vlanInfoTableVADC": vlanInfoTableVADC,
       "vlanInfoTableVADCEntry": vlanInfoTableVADCEntry,
       "vlanInfoIdx": vlanInfoIdx,
       "vlanInfoVADC": vlanInfoVADC,
       "portTeamInfo": portTeamInfo,
       "portTeamInfoTable": portTeamInfoTable,
       "portTeamInfoTableEntry": portTeamInfoTableEntry,
       "portTeamInfoIndex": portTeamInfoIndex,
       "portTeamInfoState": portTeamInfoState,
       "portTeamInfoPorts": portTeamInfoPorts,
       "portTeamInfoPortsState": portTeamInfoPortsState,
       "portTeamInfoTrunks": portTeamInfoTrunks,
       "portTeamInfoTrunksState": portTeamInfoTrunksState,
       "portTeamInfoMaster": portTeamInfoMaster,
       "layer2Oper": layer2Oper}
)

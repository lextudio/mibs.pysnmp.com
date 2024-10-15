# SNMP MIB module (ADMIN-ALTEON-AC-vADC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADMIN-ALTEON-AC-vADC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:48 2024
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

(virt_admin,) = mibBuilder.importSymbols(
    "ALTEON-ROOT-MIB",
    "virt-admin")

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

adminvADC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1)
)
adminvADC.setRevisions(
        ("2010-06-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdminvADCConfigs_ObjectIdentity = ObjectIdentity
adminvADCConfigs = _AdminvADCConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1)
)
_VADCConfig_ObjectIdentity = ObjectIdentity
vADCConfig = _VADCConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1)
)
_VADCMaxVADCId_Type = Integer32
_VADCMaxVADCId_Object = MibScalar
vADCMaxVADCId = _VADCMaxVADCId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 1),
    _VADCMaxVADCId_Type()
)
vADCMaxVADCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCMaxVADCId.setStatus("current")
_VADCMaxCU_Type = Integer32
_VADCMaxCU_Object = MibScalar
vADCMaxCU = _VADCMaxCU_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 2),
    _VADCMaxCU_Type()
)
vADCMaxCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCMaxCU.setStatus("current")
_VADCCurCfgTable_Object = MibTable
vADCCurCfgTable = _VADCCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    vADCCurCfgTable.setStatus("current")
_VADCCurCfgTableEntry_Object = MibTableRow
vADCCurCfgTableEntry = _VADCCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 3, 1)
)
vADCCurCfgTableEntry.setIndexNames(
    (0, "ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgVADCId"),
)
if mibBuilder.loadTexts:
    vADCCurCfgTableEntry.setStatus("current")
_VADCCurCfgVADCId_Type = Integer32
_VADCCurCfgVADCId_Object = MibTableColumn
vADCCurCfgVADCId = _VADCCurCfgVADCId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 3, 1, 1),
    _VADCCurCfgVADCId_Type()
)
vADCCurCfgVADCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgVADCId.setStatus("current")
_VADCCurCfgVlanId_Type = OctetString
_VADCCurCfgVlanId_Object = MibTableColumn
vADCCurCfgVlanId = _VADCCurCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 3, 1, 2),
    _VADCCurCfgVlanId_Type()
)
vADCCurCfgVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgVlanId.setStatus("current")


class _VADCCurCfgName_Type(DisplayString):
    """Custom type vADCCurCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VADCCurCfgName_Type.__name__ = "DisplayString"
_VADCCurCfgName_Object = MibTableColumn
vADCCurCfgName = _VADCCurCfgName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 3, 1, 3),
    _VADCCurCfgName_Type()
)
vADCCurCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgName.setStatus("current")
_VADCCurCfgCU_Type = Integer32
_VADCCurCfgCU_Object = MibTableColumn
vADCCurCfgCU = _VADCCurCfgCU_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 3, 1, 4),
    _VADCCurCfgCU_Type()
)
vADCCurCfgCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgCU.setStatus("current")


class _VADCCurCfgLimit_Type(Integer32):
    """Custom type vADCCurCfgLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_VADCCurCfgLimit_Type.__name__ = "Integer32"
_VADCCurCfgLimit_Object = MibTableColumn
vADCCurCfgLimit = _VADCCurCfgLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 3, 1, 5),
    _VADCCurCfgLimit_Type()
)
vADCCurCfgLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgLimit.setStatus("current")


class _VADCCurCfgState_Type(Integer32):
    """Custom type vADCCurCfgState based on Integer32"""
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


_VADCCurCfgState_Type.__name__ = "Integer32"
_VADCCurCfgState_Object = MibTableColumn
vADCCurCfgState = _VADCCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 3, 1, 6),
    _VADCCurCfgState_Type()
)
vADCCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgState.setStatus("current")


class _VADCCurCfgFeatGlobal_Type(Integer32):
    """Custom type vADCCurCfgFeatGlobal based on Integer32"""
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


_VADCCurCfgFeatGlobal_Type.__name__ = "Integer32"
_VADCCurCfgFeatGlobal_Object = MibTableColumn
vADCCurCfgFeatGlobal = _VADCCurCfgFeatGlobal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 3, 1, 7),
    _VADCCurCfgFeatGlobal_Type()
)
vADCCurCfgFeatGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgFeatGlobal.setStatus("current")


class _VADCCurCfgFeatBWM_Type(Integer32):
    """Custom type vADCCurCfgFeatBWM based on Integer32"""
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


_VADCCurCfgFeatBWM_Type.__name__ = "Integer32"
_VADCCurCfgFeatBWM_Object = MibTableColumn
vADCCurCfgFeatBWM = _VADCCurCfgFeatBWM_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 3, 1, 8),
    _VADCCurCfgFeatBWM_Type()
)
vADCCurCfgFeatBWM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgFeatBWM.setStatus("current")


class _VADCCurCfgFeatITM_Type(Integer32):
    """Custom type vADCCurCfgFeatITM based on Integer32"""
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


_VADCCurCfgFeatITM_Type.__name__ = "Integer32"
_VADCCurCfgFeatITM_Object = MibTableColumn
vADCCurCfgFeatITM = _VADCCurCfgFeatITM_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 3, 1, 9),
    _VADCCurCfgFeatITM_Type()
)
vADCCurCfgFeatITM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgFeatITM.setStatus("current")


class _VADCCurCfgFeatADOS_Type(Integer32):
    """Custom type vADCCurCfgFeatADOS based on Integer32"""
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


_VADCCurCfgFeatADOS_Type.__name__ = "Integer32"
_VADCCurCfgFeatADOS_Object = MibTableColumn
vADCCurCfgFeatADOS = _VADCCurCfgFeatADOS_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 3, 1, 10),
    _VADCCurCfgFeatADOS_Type()
)
vADCCurCfgFeatADOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgFeatADOS.setStatus("current")


class _VADCCurCfgFeatLLB_Type(Integer32):
    """Custom type vADCCurCfgFeatLLB based on Integer32"""
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


_VADCCurCfgFeatLLB_Type.__name__ = "Integer32"
_VADCCurCfgFeatLLB_Object = MibTableColumn
vADCCurCfgFeatLLB = _VADCCurCfgFeatLLB_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 3, 1, 11),
    _VADCCurCfgFeatLLB_Type()
)
vADCCurCfgFeatLLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgFeatLLB.setStatus("current")


class _VADCCurCfgSslLimit_Type(Integer32):
    """Custom type vADCCurCfgSslLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_VADCCurCfgSslLimit_Type.__name__ = "Integer32"
_VADCCurCfgSslLimit_Object = MibTableColumn
vADCCurCfgSslLimit = _VADCCurCfgSslLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 3, 1, 12),
    _VADCCurCfgSslLimit_Type()
)
vADCCurCfgSslLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSslLimit.setStatus("current")


class _VADCCurCfgCompLimit_Type(Integer32):
    """Custom type vADCCurCfgCompLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7500),
    )


_VADCCurCfgCompLimit_Type.__name__ = "Integer32"
_VADCCurCfgCompLimit_Object = MibTableColumn
vADCCurCfgCompLimit = _VADCCurCfgCompLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 3, 1, 13),
    _VADCCurCfgCompLimit_Type()
)
vADCCurCfgCompLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgCompLimit.setStatus("current")


class _VADCCurResetImageVersion_Type(DisplayString):
    """Custom type vADCCurResetImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VADCCurResetImageVersion_Type.__name__ = "DisplayString"
_VADCCurResetImageVersion_Object = MibTableColumn
vADCCurResetImageVersion = _VADCCurResetImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 3, 1, 14),
    _VADCCurResetImageVersion_Type()
)
vADCCurResetImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurResetImageVersion.setStatus("current")


class _VADCCurSyncPeerSwitch_Type(Integer32):
    """Custom type vADCCurSyncPeerSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_VADCCurSyncPeerSwitch_Type.__name__ = "Integer32"
_VADCCurSyncPeerSwitch_Object = MibTableColumn
vADCCurSyncPeerSwitch = _VADCCurSyncPeerSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 3, 1, 15),
    _VADCCurSyncPeerSwitch_Type()
)
vADCCurSyncPeerSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurSyncPeerSwitch.setStatus("current")
_VADCNewCfgTable_Object = MibTable
vADCNewCfgTable = _VADCNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    vADCNewCfgTable.setStatus("current")
_VADCNewCfgTableEntry_Object = MibTableRow
vADCNewCfgTableEntry = _VADCNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1)
)
vADCNewCfgTableEntry.setIndexNames(
    (0, "ADMIN-ALTEON-AC-vADC-MIB", "vADCNewCfgVADCId"),
)
if mibBuilder.loadTexts:
    vADCNewCfgTableEntry.setStatus("current")
_VADCNewCfgVADCId_Type = Integer32
_VADCNewCfgVADCId_Object = MibTableColumn
vADCNewCfgVADCId = _VADCNewCfgVADCId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1, 1),
    _VADCNewCfgVADCId_Type()
)
vADCNewCfgVADCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCNewCfgVADCId.setStatus("current")
_VADCNewCfgVlanId_Type = OctetString
_VADCNewCfgVlanId_Object = MibTableColumn
vADCNewCfgVlanId = _VADCNewCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1, 2),
    _VADCNewCfgVlanId_Type()
)
vADCNewCfgVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCNewCfgVlanId.setStatus("current")


class _VADCNewCfgAddVlan_Type(Integer32):
    """Custom type vADCNewCfgAddVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4090),
    )


_VADCNewCfgAddVlan_Type.__name__ = "Integer32"
_VADCNewCfgAddVlan_Object = MibTableColumn
vADCNewCfgAddVlan = _VADCNewCfgAddVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1, 3),
    _VADCNewCfgAddVlan_Type()
)
vADCNewCfgAddVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgAddVlan.setStatus("current")


class _VADCNewCfgRemoveVlan_Type(Integer32):
    """Custom type vADCNewCfgRemoveVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4090),
    )


_VADCNewCfgRemoveVlan_Type.__name__ = "Integer32"
_VADCNewCfgRemoveVlan_Object = MibTableColumn
vADCNewCfgRemoveVlan = _VADCNewCfgRemoveVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1, 4),
    _VADCNewCfgRemoveVlan_Type()
)
vADCNewCfgRemoveVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgRemoveVlan.setStatus("current")


class _VADCNewCfgName_Type(DisplayString):
    """Custom type vADCNewCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VADCNewCfgName_Type.__name__ = "DisplayString"
_VADCNewCfgName_Object = MibTableColumn
vADCNewCfgName = _VADCNewCfgName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1, 5),
    _VADCNewCfgName_Type()
)
vADCNewCfgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgName.setStatus("current")
_VADCNewCfgCU_Type = Integer32
_VADCNewCfgCU_Object = MibTableColumn
vADCNewCfgCU = _VADCNewCfgCU_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1, 6),
    _VADCNewCfgCU_Type()
)
vADCNewCfgCU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgCU.setStatus("current")


class _VADCNewCfgLimit_Type(Integer32):
    """Custom type vADCNewCfgLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_VADCNewCfgLimit_Type.__name__ = "Integer32"
_VADCNewCfgLimit_Object = MibTableColumn
vADCNewCfgLimit = _VADCNewCfgLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1, 7),
    _VADCNewCfgLimit_Type()
)
vADCNewCfgLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgLimit.setStatus("current")


class _VADCNewCfgState_Type(Integer32):
    """Custom type vADCNewCfgState based on Integer32"""
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


_VADCNewCfgState_Type.__name__ = "Integer32"
_VADCNewCfgState_Object = MibTableColumn
vADCNewCfgState = _VADCNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1, 8),
    _VADCNewCfgState_Type()
)
vADCNewCfgState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgState.setStatus("current")


class _VADCNewCfgDelete_Type(Integer32):
    """Custom type vADCNewCfgDelete based on Integer32"""
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


_VADCNewCfgDelete_Type.__name__ = "Integer32"
_VADCNewCfgDelete_Object = MibTableColumn
vADCNewCfgDelete = _VADCNewCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1, 9),
    _VADCNewCfgDelete_Type()
)
vADCNewCfgDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgDelete.setStatus("current")


class _VADCNewCfgFeatGlobal_Type(Integer32):
    """Custom type vADCNewCfgFeatGlobal based on Integer32"""
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


_VADCNewCfgFeatGlobal_Type.__name__ = "Integer32"
_VADCNewCfgFeatGlobal_Object = MibTableColumn
vADCNewCfgFeatGlobal = _VADCNewCfgFeatGlobal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1, 10),
    _VADCNewCfgFeatGlobal_Type()
)
vADCNewCfgFeatGlobal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgFeatGlobal.setStatus("current")


class _VADCNewCfgFeatBWM_Type(Integer32):
    """Custom type vADCNewCfgFeatBWM based on Integer32"""
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


_VADCNewCfgFeatBWM_Type.__name__ = "Integer32"
_VADCNewCfgFeatBWM_Object = MibTableColumn
vADCNewCfgFeatBWM = _VADCNewCfgFeatBWM_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1, 11),
    _VADCNewCfgFeatBWM_Type()
)
vADCNewCfgFeatBWM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgFeatBWM.setStatus("current")


class _VADCNewCfgFeatITM_Type(Integer32):
    """Custom type vADCNewCfgFeatITM based on Integer32"""
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


_VADCNewCfgFeatITM_Type.__name__ = "Integer32"
_VADCNewCfgFeatITM_Object = MibTableColumn
vADCNewCfgFeatITM = _VADCNewCfgFeatITM_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1, 12),
    _VADCNewCfgFeatITM_Type()
)
vADCNewCfgFeatITM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgFeatITM.setStatus("current")


class _VADCNewCfgFeatADOS_Type(Integer32):
    """Custom type vADCNewCfgFeatADOS based on Integer32"""
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


_VADCNewCfgFeatADOS_Type.__name__ = "Integer32"
_VADCNewCfgFeatADOS_Object = MibTableColumn
vADCNewCfgFeatADOS = _VADCNewCfgFeatADOS_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1, 13),
    _VADCNewCfgFeatADOS_Type()
)
vADCNewCfgFeatADOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgFeatADOS.setStatus("current")


class _VADCNewCfgFeatLLB_Type(Integer32):
    """Custom type vADCNewCfgFeatLLB based on Integer32"""
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


_VADCNewCfgFeatLLB_Type.__name__ = "Integer32"
_VADCNewCfgFeatLLB_Object = MibTableColumn
vADCNewCfgFeatLLB = _VADCNewCfgFeatLLB_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1, 14),
    _VADCNewCfgFeatLLB_Type()
)
vADCNewCfgFeatLLB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgFeatLLB.setStatus("current")


class _VADCNewCfgSslLimit_Type(Integer32):
    """Custom type vADCNewCfgSslLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_VADCNewCfgSslLimit_Type.__name__ = "Integer32"
_VADCNewCfgSslLimit_Object = MibTableColumn
vADCNewCfgSslLimit = _VADCNewCfgSslLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1, 15),
    _VADCNewCfgSslLimit_Type()
)
vADCNewCfgSslLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSslLimit.setStatus("current")


class _VADCNewCfgCompLimit_Type(Integer32):
    """Custom type vADCNewCfgCompLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7500),
    )


_VADCNewCfgCompLimit_Type.__name__ = "Integer32"
_VADCNewCfgCompLimit_Object = MibTableColumn
vADCNewCfgCompLimit = _VADCNewCfgCompLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1, 16),
    _VADCNewCfgCompLimit_Type()
)
vADCNewCfgCompLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgCompLimit.setStatus("current")


class _VADCNewResetImageVersion_Type(DisplayString):
    """Custom type vADCNewResetImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VADCNewResetImageVersion_Type.__name__ = "DisplayString"
_VADCNewResetImageVersion_Object = MibTableColumn
vADCNewResetImageVersion = _VADCNewResetImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1, 17),
    _VADCNewResetImageVersion_Type()
)
vADCNewResetImageVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCNewResetImageVersion.setStatus("current")


class _VADCNewSyncPeerSwitch_Type(Integer32):
    """Custom type vADCNewSyncPeerSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_VADCNewSyncPeerSwitch_Type.__name__ = "Integer32"
_VADCNewSyncPeerSwitch_Object = MibTableColumn
vADCNewSyncPeerSwitch = _VADCNewSyncPeerSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 4, 1, 18),
    _VADCNewSyncPeerSwitch_Type()
)
vADCNewSyncPeerSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCNewSyncPeerSwitch.setStatus("current")
_VADCCurCfgSysTable_Object = MibTable
vADCCurCfgSysTable = _VADCCurCfgSysTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    vADCCurCfgSysTable.setStatus("current")
_VADCCurCfgSysTableEntry_Object = MibTableRow
vADCCurCfgSysTableEntry = _VADCCurCfgSysTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1)
)
vADCCurCfgSysTableEntry.setIndexNames(
    (0, "ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgSysVADCId"),
)
if mibBuilder.loadTexts:
    vADCCurCfgSysTableEntry.setStatus("current")
_VADCCurCfgSysMmgmtAddr_Type = IpAddress
_VADCCurCfgSysMmgmtAddr_Object = MibTableColumn
vADCCurCfgSysMmgmtAddr = _VADCCurCfgSysMmgmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 1),
    _VADCCurCfgSysMmgmtAddr_Type()
)
vADCCurCfgSysMmgmtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysMmgmtAddr.setStatus("current")
_VADCCurCfgSysMmgmtMask_Type = IpAddress
_VADCCurCfgSysMmgmtMask_Object = MibTableColumn
vADCCurCfgSysMmgmtMask = _VADCCurCfgSysMmgmtMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 2),
    _VADCCurCfgSysMmgmtMask_Type()
)
vADCCurCfgSysMmgmtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysMmgmtMask.setStatus("current")
_VADCCurCfgSysMmgmtGw_Type = IpAddress
_VADCCurCfgSysMmgmtGw_Object = MibTableColumn
vADCCurCfgSysMmgmtGw = _VADCCurCfgSysMmgmtGw_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 3),
    _VADCCurCfgSysMmgmtGw_Type()
)
vADCCurCfgSysMmgmtGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysMmgmtGw.setStatus("current")


class _VADCCurCfgSysMmgmtState_Type(Integer32):
    """Custom type vADCCurCfgSysMmgmtState based on Integer32"""
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


_VADCCurCfgSysMmgmtState_Type.__name__ = "Integer32"
_VADCCurCfgSysMmgmtState_Object = MibTableColumn
vADCCurCfgSysMmgmtState = _VADCCurCfgSysMmgmtState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 4),
    _VADCCurCfgSysMmgmtState_Type()
)
vADCCurCfgSysMmgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysMmgmtState.setStatus("current")
_VADCCurCfgSysPeerAddr_Type = IpAddress
_VADCCurCfgSysPeerAddr_Object = MibTableColumn
vADCCurCfgSysPeerAddr = _VADCCurCfgSysPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 5),
    _VADCCurCfgSysPeerAddr_Type()
)
vADCCurCfgSysPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysPeerAddr.setStatus("current")
_VADCCurCfgSysPeerMask_Type = IpAddress
_VADCCurCfgSysPeerMask_Object = MibTableColumn
vADCCurCfgSysPeerMask = _VADCCurCfgSysPeerMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 6),
    _VADCCurCfgSysPeerMask_Type()
)
vADCCurCfgSysPeerMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysPeerMask.setStatus("current")
_VADCCurCfgSysPeerGw_Type = IpAddress
_VADCCurCfgSysPeerGw_Object = MibTableColumn
vADCCurCfgSysPeerGw = _VADCCurCfgSysPeerGw_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 7),
    _VADCCurCfgSysPeerGw_Type()
)
vADCCurCfgSysPeerGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysPeerGw.setStatus("current")


class _VADCCurCfgSysHttpsState_Type(Integer32):
    """Custom type vADCCurCfgSysHttpsState based on Integer32"""
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


_VADCCurCfgSysHttpsState_Type.__name__ = "Integer32"
_VADCCurCfgSysHttpsState_Object = MibTableColumn
vADCCurCfgSysHttpsState = _VADCCurCfgSysHttpsState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 8),
    _VADCCurCfgSysHttpsState_Type()
)
vADCCurCfgSysHttpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysHttpsState.setStatus("current")


class _VADCCurCfgSysSshState_Type(Integer32):
    """Custom type vADCCurCfgSysSshState based on Integer32"""
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


_VADCCurCfgSysSshState_Type.__name__ = "Integer32"
_VADCCurCfgSysSshState_Object = MibTableColumn
vADCCurCfgSysSshState = _VADCCurCfgSysSshState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 9),
    _VADCCurCfgSysSshState_Type()
)
vADCCurCfgSysSshState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysSshState.setStatus("current")


class _VADCCurCfgSysHttpState_Type(Integer32):
    """Custom type vADCCurCfgSysHttpState based on Integer32"""
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


_VADCCurCfgSysHttpState_Type.__name__ = "Integer32"
_VADCCurCfgSysHttpState_Object = MibTableColumn
vADCCurCfgSysHttpState = _VADCCurCfgSysHttpState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 10),
    _VADCCurCfgSysHttpState_Type()
)
vADCCurCfgSysHttpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysHttpState.setStatus("current")


class _VADCCurCfgSysSnmpState_Type(Integer32):
    """Custom type vADCCurCfgSysSnmpState based on Integer32"""
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


_VADCCurCfgSysSnmpState_Type.__name__ = "Integer32"
_VADCCurCfgSysSnmpState_Object = MibTableColumn
vADCCurCfgSysSnmpState = _VADCCurCfgSysSnmpState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 11),
    _VADCCurCfgSysSnmpState_Type()
)
vADCCurCfgSysSnmpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysSnmpState.setStatus("current")


class _VADCCurCfgSysSyslogState_Type(Integer32):
    """Custom type vADCCurCfgSysSyslogState based on Integer32"""
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


_VADCCurCfgSysSyslogState_Type.__name__ = "Integer32"
_VADCCurCfgSysSyslogState_Object = MibTableColumn
vADCCurCfgSysSyslogState = _VADCCurCfgSysSyslogState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 12),
    _VADCCurCfgSysSyslogState_Type()
)
vADCCurCfgSysSyslogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysSyslogState.setStatus("current")


class _VADCCurCfgSysRadiusState_Type(Integer32):
    """Custom type vADCCurCfgSysRadiusState based on Integer32"""
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


_VADCCurCfgSysRadiusState_Type.__name__ = "Integer32"
_VADCCurCfgSysRadiusState_Object = MibTableColumn
vADCCurCfgSysRadiusState = _VADCCurCfgSysRadiusState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 13),
    _VADCCurCfgSysRadiusState_Type()
)
vADCCurCfgSysRadiusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysRadiusState.setStatus("current")


class _VADCCurCfgSysTacacsState_Type(Integer32):
    """Custom type vADCCurCfgSysTacacsState based on Integer32"""
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


_VADCCurCfgSysTacacsState_Type.__name__ = "Integer32"
_VADCCurCfgSysTacacsState_Object = MibTableColumn
vADCCurCfgSysTacacsState = _VADCCurCfgSysTacacsState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 14),
    _VADCCurCfgSysTacacsState_Type()
)
vADCCurCfgSysTacacsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysTacacsState.setStatus("current")


class _VADCCurCfgSysIdleState_Type(Integer32):
    """Custom type vADCCurCfgSysIdleState based on Integer32"""
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


_VADCCurCfgSysIdleState_Type.__name__ = "Integer32"
_VADCCurCfgSysIdleState_Object = MibTableColumn
vADCCurCfgSysIdleState = _VADCCurCfgSysIdleState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 15),
    _VADCCurCfgSysIdleState_Type()
)
vADCCurCfgSysIdleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysIdleState.setStatus("current")


class _VADCCurCfgSysSmtpState_Type(Integer32):
    """Custom type vADCCurCfgSysSmtpState based on Integer32"""
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


_VADCCurCfgSysSmtpState_Type.__name__ = "Integer32"
_VADCCurCfgSysSmtpState_Object = MibTableColumn
vADCCurCfgSysSmtpState = _VADCCurCfgSysSmtpState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 16),
    _VADCCurCfgSysSmtpState_Type()
)
vADCCurCfgSysSmtpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysSmtpState.setStatus("current")


class _VADCCurCfgSyslogDelegation_Type(Integer32):
    """Custom type vADCCurCfgSyslogDelegation based on Integer32"""
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


_VADCCurCfgSyslogDelegation_Type.__name__ = "Integer32"
_VADCCurCfgSyslogDelegation_Object = MibTableColumn
vADCCurCfgSyslogDelegation = _VADCCurCfgSyslogDelegation_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 17),
    _VADCCurCfgSyslogDelegation_Type()
)
vADCCurCfgSyslogDelegation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSyslogDelegation.setStatus("current")


class _VADCCurCfgRadiusDelegation_Type(Integer32):
    """Custom type vADCCurCfgRadiusDelegation based on Integer32"""
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


_VADCCurCfgRadiusDelegation_Type.__name__ = "Integer32"
_VADCCurCfgRadiusDelegation_Object = MibTableColumn
vADCCurCfgRadiusDelegation = _VADCCurCfgRadiusDelegation_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 18),
    _VADCCurCfgRadiusDelegation_Type()
)
vADCCurCfgRadiusDelegation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgRadiusDelegation.setStatus("current")


class _VADCCurCfgTacacsDelegation_Type(Integer32):
    """Custom type vADCCurCfgTacacsDelegation based on Integer32"""
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


_VADCCurCfgTacacsDelegation_Type.__name__ = "Integer32"
_VADCCurCfgTacacsDelegation_Object = MibTableColumn
vADCCurCfgTacacsDelegation = _VADCCurCfgTacacsDelegation_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 19),
    _VADCCurCfgTacacsDelegation_Type()
)
vADCCurCfgTacacsDelegation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgTacacsDelegation.setStatus("current")


class _VADCCurCfgSmtpDelegation_Type(Integer32):
    """Custom type vADCCurCfgSmtpDelegation based on Integer32"""
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


_VADCCurCfgSmtpDelegation_Type.__name__ = "Integer32"
_VADCCurCfgSmtpDelegation_Object = MibTableColumn
vADCCurCfgSmtpDelegation = _VADCCurCfgSmtpDelegation_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 20),
    _VADCCurCfgSmtpDelegation_Type()
)
vADCCurCfgSmtpDelegation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSmtpDelegation.setStatus("current")


class _VADCCurCfgSysMmgmtIpv6Addr_Type(DisplayString):
    """Custom type vADCCurCfgSysMmgmtIpv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VADCCurCfgSysMmgmtIpv6Addr_Type.__name__ = "DisplayString"
_VADCCurCfgSysMmgmtIpv6Addr_Object = MibTableColumn
vADCCurCfgSysMmgmtIpv6Addr = _VADCCurCfgSysMmgmtIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 21),
    _VADCCurCfgSysMmgmtIpv6Addr_Type()
)
vADCCurCfgSysMmgmtIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysMmgmtIpv6Addr.setStatus("current")


class _VADCCurCfgSysMmgmtIpv6PrefixLen_Type(Integer32):
    """Custom type vADCCurCfgSysMmgmtIpv6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_VADCCurCfgSysMmgmtIpv6PrefixLen_Type.__name__ = "Integer32"
_VADCCurCfgSysMmgmtIpv6PrefixLen_Object = MibTableColumn
vADCCurCfgSysMmgmtIpv6PrefixLen = _VADCCurCfgSysMmgmtIpv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 22),
    _VADCCurCfgSysMmgmtIpv6PrefixLen_Type()
)
vADCCurCfgSysMmgmtIpv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysMmgmtIpv6PrefixLen.setStatus("current")


class _VADCCurCfgSysMmgmtIpv6Gateway_Type(DisplayString):
    """Custom type vADCCurCfgSysMmgmtIpv6Gateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VADCCurCfgSysMmgmtIpv6Gateway_Type.__name__ = "DisplayString"
_VADCCurCfgSysMmgmtIpv6Gateway_Object = MibTableColumn
vADCCurCfgSysMmgmtIpv6Gateway = _VADCCurCfgSysMmgmtIpv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 23),
    _VADCCurCfgSysMmgmtIpv6Gateway_Type()
)
vADCCurCfgSysMmgmtIpv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysMmgmtIpv6Gateway.setStatus("current")


class _VADCCurCfgSysPeerIpv6Addr_Type(DisplayString):
    """Custom type vADCCurCfgSysPeerIpv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VADCCurCfgSysPeerIpv6Addr_Type.__name__ = "DisplayString"
_VADCCurCfgSysPeerIpv6Addr_Object = MibTableColumn
vADCCurCfgSysPeerIpv6Addr = _VADCCurCfgSysPeerIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 24),
    _VADCCurCfgSysPeerIpv6Addr_Type()
)
vADCCurCfgSysPeerIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysPeerIpv6Addr.setStatus("current")


class _VADCCurCfgSysPeerIpv6PrefixLen_Type(Integer32):
    """Custom type vADCCurCfgSysPeerIpv6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_VADCCurCfgSysPeerIpv6PrefixLen_Type.__name__ = "Integer32"
_VADCCurCfgSysPeerIpv6PrefixLen_Object = MibTableColumn
vADCCurCfgSysPeerIpv6PrefixLen = _VADCCurCfgSysPeerIpv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 25),
    _VADCCurCfgSysPeerIpv6PrefixLen_Type()
)
vADCCurCfgSysPeerIpv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysPeerIpv6PrefixLen.setStatus("current")


class _VADCCurCfgSysPeerIpv6Gateway_Type(DisplayString):
    """Custom type vADCCurCfgSysPeerIpv6Gateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VADCCurCfgSysPeerIpv6Gateway_Type.__name__ = "DisplayString"
_VADCCurCfgSysPeerIpv6Gateway_Object = MibTableColumn
vADCCurCfgSysPeerIpv6Gateway = _VADCCurCfgSysPeerIpv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 26),
    _VADCCurCfgSysPeerIpv6Gateway_Type()
)
vADCCurCfgSysPeerIpv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysPeerIpv6Gateway.setStatus("current")


class _VADCCurCfgSysTnetState_Type(Integer32):
    """Custom type vADCCurCfgSysTnetState based on Integer32"""
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


_VADCCurCfgSysTnetState_Type.__name__ = "Integer32"
_VADCCurCfgSysTnetState_Object = MibTableColumn
vADCCurCfgSysTnetState = _VADCCurCfgSysTnetState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 27),
    _VADCCurCfgSysTnetState_Type()
)
vADCCurCfgSysTnetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysTnetState.setStatus("current")


class _VADCCurCfgSysHaId_Type(Integer32):
    """Custom type vADCCurCfgSysHaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_VADCCurCfgSysHaId_Type.__name__ = "Integer32"
_VADCCurCfgSysHaId_Object = MibTableColumn
vADCCurCfgSysHaId = _VADCCurCfgSysHaId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 28),
    _VADCCurCfgSysHaId_Type()
)
vADCCurCfgSysHaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysHaId.setStatus("current")


class _VADCCurCfgSysPeerId_Type(Integer32):
    """Custom type vADCCurCfgSysPeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_VADCCurCfgSysPeerId_Type.__name__ = "Integer32"
_VADCCurCfgSysPeerId_Object = MibTableColumn
vADCCurCfgSysPeerId = _VADCCurCfgSysPeerId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 29),
    _VADCCurCfgSysPeerId_Type()
)
vADCCurCfgSysPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysPeerId.setStatus("current")
_VADCCurCfgSysVADCId_Type = Integer32
_VADCCurCfgSysVADCId_Object = MibTableColumn
vADCCurCfgSysVADCId = _VADCCurCfgSysVADCId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 30),
    _VADCCurCfgSysVADCId_Type()
)
vADCCurCfgSysVADCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysVADCId.setStatus("current")


class _VADCCurCfgIdleDelegation_Type(Integer32):
    """Custom type vADCCurCfgIdleDelegation based on Integer32"""
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


_VADCCurCfgIdleDelegation_Type.__name__ = "Integer32"
_VADCCurCfgIdleDelegation_Object = MibTableColumn
vADCCurCfgIdleDelegation = _VADCCurCfgIdleDelegation_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 31),
    _VADCCurCfgIdleDelegation_Type()
)
vADCCurCfgIdleDelegation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgIdleDelegation.setStatus("current")


class _VADCCurCfgSysMmgmtDelegation_Type(Integer32):
    """Custom type vADCCurCfgSysMmgmtDelegation based on Integer32"""
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


_VADCCurCfgSysMmgmtDelegation_Type.__name__ = "Integer32"
_VADCCurCfgSysMmgmtDelegation_Object = MibTableColumn
vADCCurCfgSysMmgmtDelegation = _VADCCurCfgSysMmgmtDelegation_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 32),
    _VADCCurCfgSysMmgmtDelegation_Type()
)
vADCCurCfgSysMmgmtDelegation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysMmgmtDelegation.setStatus("current")


class _VADCCurCfgSysPeerName_Type(DisplayString):
    """Custom type vADCCurCfgSysPeerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VADCCurCfgSysPeerName_Type.__name__ = "DisplayString"
_VADCCurCfgSysPeerName_Object = MibTableColumn
vADCCurCfgSysPeerName = _VADCCurCfgSysPeerName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 5, 1, 33),
    _VADCCurCfgSysPeerName_Type()
)
vADCCurCfgSysPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgSysPeerName.setStatus("current")
_VADCNewCfgSysTable_Object = MibTable
vADCNewCfgSysTable = _VADCNewCfgSysTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    vADCNewCfgSysTable.setStatus("current")
_VADCNewCfgSysTableEntry_Object = MibTableRow
vADCNewCfgSysTableEntry = _VADCNewCfgSysTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1)
)
vADCNewCfgSysTableEntry.setIndexNames(
    (0, "ADMIN-ALTEON-AC-vADC-MIB", "vADCNewCfgSysVADCId"),
)
if mibBuilder.loadTexts:
    vADCNewCfgSysTableEntry.setStatus("current")
_VADCNewCfgSysMmgmtAddr_Type = IpAddress
_VADCNewCfgSysMmgmtAddr_Object = MibTableColumn
vADCNewCfgSysMmgmtAddr = _VADCNewCfgSysMmgmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 1),
    _VADCNewCfgSysMmgmtAddr_Type()
)
vADCNewCfgSysMmgmtAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysMmgmtAddr.setStatus("current")
_VADCNewCfgSysMmgmtMask_Type = IpAddress
_VADCNewCfgSysMmgmtMask_Object = MibTableColumn
vADCNewCfgSysMmgmtMask = _VADCNewCfgSysMmgmtMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 2),
    _VADCNewCfgSysMmgmtMask_Type()
)
vADCNewCfgSysMmgmtMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysMmgmtMask.setStatus("current")
_VADCNewCfgSysMmgmtGw_Type = IpAddress
_VADCNewCfgSysMmgmtGw_Object = MibTableColumn
vADCNewCfgSysMmgmtGw = _VADCNewCfgSysMmgmtGw_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 3),
    _VADCNewCfgSysMmgmtGw_Type()
)
vADCNewCfgSysMmgmtGw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysMmgmtGw.setStatus("current")


class _VADCNewCfgSysMmgmtState_Type(Integer32):
    """Custom type vADCNewCfgSysMmgmtState based on Integer32"""
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


_VADCNewCfgSysMmgmtState_Type.__name__ = "Integer32"
_VADCNewCfgSysMmgmtState_Object = MibTableColumn
vADCNewCfgSysMmgmtState = _VADCNewCfgSysMmgmtState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 4),
    _VADCNewCfgSysMmgmtState_Type()
)
vADCNewCfgSysMmgmtState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysMmgmtState.setStatus("current")
_VADCNewCfgSysPeerAddr_Type = IpAddress
_VADCNewCfgSysPeerAddr_Object = MibTableColumn
vADCNewCfgSysPeerAddr = _VADCNewCfgSysPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 5),
    _VADCNewCfgSysPeerAddr_Type()
)
vADCNewCfgSysPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysPeerAddr.setStatus("current")
_VADCNewCfgSysPeerMask_Type = IpAddress
_VADCNewCfgSysPeerMask_Object = MibTableColumn
vADCNewCfgSysPeerMask = _VADCNewCfgSysPeerMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 6),
    _VADCNewCfgSysPeerMask_Type()
)
vADCNewCfgSysPeerMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysPeerMask.setStatus("current")
_VADCNewCfgSysPeerGw_Type = IpAddress
_VADCNewCfgSysPeerGw_Object = MibTableColumn
vADCNewCfgSysPeerGw = _VADCNewCfgSysPeerGw_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 7),
    _VADCNewCfgSysPeerGw_Type()
)
vADCNewCfgSysPeerGw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysPeerGw.setStatus("current")


class _VADCNewCfgSysHttpsState_Type(Integer32):
    """Custom type vADCNewCfgSysHttpsState based on Integer32"""
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


_VADCNewCfgSysHttpsState_Type.__name__ = "Integer32"
_VADCNewCfgSysHttpsState_Object = MibTableColumn
vADCNewCfgSysHttpsState = _VADCNewCfgSysHttpsState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 8),
    _VADCNewCfgSysHttpsState_Type()
)
vADCNewCfgSysHttpsState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysHttpsState.setStatus("current")


class _VADCNewCfgSysSshState_Type(Integer32):
    """Custom type vADCNewCfgSysSshState based on Integer32"""
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


_VADCNewCfgSysSshState_Type.__name__ = "Integer32"
_VADCNewCfgSysSshState_Object = MibTableColumn
vADCNewCfgSysSshState = _VADCNewCfgSysSshState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 9),
    _VADCNewCfgSysSshState_Type()
)
vADCNewCfgSysSshState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysSshState.setStatus("current")


class _VADCNewCfgSysHttpState_Type(Integer32):
    """Custom type vADCNewCfgSysHttpState based on Integer32"""
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


_VADCNewCfgSysHttpState_Type.__name__ = "Integer32"
_VADCNewCfgSysHttpState_Object = MibTableColumn
vADCNewCfgSysHttpState = _VADCNewCfgSysHttpState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 10),
    _VADCNewCfgSysHttpState_Type()
)
vADCNewCfgSysHttpState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysHttpState.setStatus("current")


class _VADCNewCfgSysSnmpState_Type(Integer32):
    """Custom type vADCNewCfgSysSnmpState based on Integer32"""
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


_VADCNewCfgSysSnmpState_Type.__name__ = "Integer32"
_VADCNewCfgSysSnmpState_Object = MibTableColumn
vADCNewCfgSysSnmpState = _VADCNewCfgSysSnmpState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 11),
    _VADCNewCfgSysSnmpState_Type()
)
vADCNewCfgSysSnmpState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysSnmpState.setStatus("current")


class _VADCNewCfgSysSyslogState_Type(Integer32):
    """Custom type vADCNewCfgSysSyslogState based on Integer32"""
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


_VADCNewCfgSysSyslogState_Type.__name__ = "Integer32"
_VADCNewCfgSysSyslogState_Object = MibTableColumn
vADCNewCfgSysSyslogState = _VADCNewCfgSysSyslogState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 12),
    _VADCNewCfgSysSyslogState_Type()
)
vADCNewCfgSysSyslogState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysSyslogState.setStatus("current")


class _VADCNewCfgSysRadiusState_Type(Integer32):
    """Custom type vADCNewCfgSysRadiusState based on Integer32"""
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


_VADCNewCfgSysRadiusState_Type.__name__ = "Integer32"
_VADCNewCfgSysRadiusState_Object = MibTableColumn
vADCNewCfgSysRadiusState = _VADCNewCfgSysRadiusState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 13),
    _VADCNewCfgSysRadiusState_Type()
)
vADCNewCfgSysRadiusState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysRadiusState.setStatus("current")


class _VADCNewCfgSysTacacsState_Type(Integer32):
    """Custom type vADCNewCfgSysTacacsState based on Integer32"""
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


_VADCNewCfgSysTacacsState_Type.__name__ = "Integer32"
_VADCNewCfgSysTacacsState_Object = MibTableColumn
vADCNewCfgSysTacacsState = _VADCNewCfgSysTacacsState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 14),
    _VADCNewCfgSysTacacsState_Type()
)
vADCNewCfgSysTacacsState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysTacacsState.setStatus("current")


class _VADCNewCfgSysIdleState_Type(Integer32):
    """Custom type vADCNewCfgSysIdleState based on Integer32"""
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


_VADCNewCfgSysIdleState_Type.__name__ = "Integer32"
_VADCNewCfgSysIdleState_Object = MibTableColumn
vADCNewCfgSysIdleState = _VADCNewCfgSysIdleState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 15),
    _VADCNewCfgSysIdleState_Type()
)
vADCNewCfgSysIdleState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysIdleState.setStatus("current")


class _VADCNewCfgSysSmtpState_Type(Integer32):
    """Custom type vADCNewCfgSysSmtpState based on Integer32"""
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


_VADCNewCfgSysSmtpState_Type.__name__ = "Integer32"
_VADCNewCfgSysSmtpState_Object = MibTableColumn
vADCNewCfgSysSmtpState = _VADCNewCfgSysSmtpState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 16),
    _VADCNewCfgSysSmtpState_Type()
)
vADCNewCfgSysSmtpState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysSmtpState.setStatus("current")


class _VADCNewCfgSyslogDelegation_Type(Integer32):
    """Custom type vADCNewCfgSyslogDelegation based on Integer32"""
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


_VADCNewCfgSyslogDelegation_Type.__name__ = "Integer32"
_VADCNewCfgSyslogDelegation_Object = MibTableColumn
vADCNewCfgSyslogDelegation = _VADCNewCfgSyslogDelegation_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 17),
    _VADCNewCfgSyslogDelegation_Type()
)
vADCNewCfgSyslogDelegation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSyslogDelegation.setStatus("current")


class _VADCNewCfgRadiusDelegation_Type(Integer32):
    """Custom type vADCNewCfgRadiusDelegation based on Integer32"""
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


_VADCNewCfgRadiusDelegation_Type.__name__ = "Integer32"
_VADCNewCfgRadiusDelegation_Object = MibTableColumn
vADCNewCfgRadiusDelegation = _VADCNewCfgRadiusDelegation_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 18),
    _VADCNewCfgRadiusDelegation_Type()
)
vADCNewCfgRadiusDelegation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgRadiusDelegation.setStatus("current")


class _VADCNewCfgTacacsDelegation_Type(Integer32):
    """Custom type vADCNewCfgTacacsDelegation based on Integer32"""
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


_VADCNewCfgTacacsDelegation_Type.__name__ = "Integer32"
_VADCNewCfgTacacsDelegation_Object = MibTableColumn
vADCNewCfgTacacsDelegation = _VADCNewCfgTacacsDelegation_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 19),
    _VADCNewCfgTacacsDelegation_Type()
)
vADCNewCfgTacacsDelegation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgTacacsDelegation.setStatus("current")


class _VADCNewCfgSmtpDelegation_Type(Integer32):
    """Custom type vADCNewCfgSmtpDelegation based on Integer32"""
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


_VADCNewCfgSmtpDelegation_Type.__name__ = "Integer32"
_VADCNewCfgSmtpDelegation_Object = MibTableColumn
vADCNewCfgSmtpDelegation = _VADCNewCfgSmtpDelegation_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 20),
    _VADCNewCfgSmtpDelegation_Type()
)
vADCNewCfgSmtpDelegation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSmtpDelegation.setStatus("current")


class _VADCNewCfgSysMmgmtIpv6Addr_Type(DisplayString):
    """Custom type vADCNewCfgSysMmgmtIpv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VADCNewCfgSysMmgmtIpv6Addr_Type.__name__ = "DisplayString"
_VADCNewCfgSysMmgmtIpv6Addr_Object = MibTableColumn
vADCNewCfgSysMmgmtIpv6Addr = _VADCNewCfgSysMmgmtIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 21),
    _VADCNewCfgSysMmgmtIpv6Addr_Type()
)
vADCNewCfgSysMmgmtIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysMmgmtIpv6Addr.setStatus("current")


class _VADCNewCfgSysMmgmtIpv6PrefixLen_Type(Integer32):
    """Custom type vADCNewCfgSysMmgmtIpv6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_VADCNewCfgSysMmgmtIpv6PrefixLen_Type.__name__ = "Integer32"
_VADCNewCfgSysMmgmtIpv6PrefixLen_Object = MibTableColumn
vADCNewCfgSysMmgmtIpv6PrefixLen = _VADCNewCfgSysMmgmtIpv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 22),
    _VADCNewCfgSysMmgmtIpv6PrefixLen_Type()
)
vADCNewCfgSysMmgmtIpv6PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysMmgmtIpv6PrefixLen.setStatus("current")


class _VADCNewCfgSysMmgmtIpv6Gateway_Type(DisplayString):
    """Custom type vADCNewCfgSysMmgmtIpv6Gateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VADCNewCfgSysMmgmtIpv6Gateway_Type.__name__ = "DisplayString"
_VADCNewCfgSysMmgmtIpv6Gateway_Object = MibTableColumn
vADCNewCfgSysMmgmtIpv6Gateway = _VADCNewCfgSysMmgmtIpv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 23),
    _VADCNewCfgSysMmgmtIpv6Gateway_Type()
)
vADCNewCfgSysMmgmtIpv6Gateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysMmgmtIpv6Gateway.setStatus("current")


class _VADCNewCfgSysPeerIpv6Addr_Type(DisplayString):
    """Custom type vADCNewCfgSysPeerIpv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VADCNewCfgSysPeerIpv6Addr_Type.__name__ = "DisplayString"
_VADCNewCfgSysPeerIpv6Addr_Object = MibTableColumn
vADCNewCfgSysPeerIpv6Addr = _VADCNewCfgSysPeerIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 24),
    _VADCNewCfgSysPeerIpv6Addr_Type()
)
vADCNewCfgSysPeerIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysPeerIpv6Addr.setStatus("current")


class _VADCNewCfgSysPeerIpv6PrefixLen_Type(Integer32):
    """Custom type vADCNewCfgSysPeerIpv6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_VADCNewCfgSysPeerIpv6PrefixLen_Type.__name__ = "Integer32"
_VADCNewCfgSysPeerIpv6PrefixLen_Object = MibTableColumn
vADCNewCfgSysPeerIpv6PrefixLen = _VADCNewCfgSysPeerIpv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 25),
    _VADCNewCfgSysPeerIpv6PrefixLen_Type()
)
vADCNewCfgSysPeerIpv6PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysPeerIpv6PrefixLen.setStatus("current")


class _VADCNewCfgSysPeerIpv6Gateway_Type(DisplayString):
    """Custom type vADCNewCfgSysPeerIpv6Gateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VADCNewCfgSysPeerIpv6Gateway_Type.__name__ = "DisplayString"
_VADCNewCfgSysPeerIpv6Gateway_Object = MibTableColumn
vADCNewCfgSysPeerIpv6Gateway = _VADCNewCfgSysPeerIpv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 26),
    _VADCNewCfgSysPeerIpv6Gateway_Type()
)
vADCNewCfgSysPeerIpv6Gateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysPeerIpv6Gateway.setStatus("current")


class _VADCNewCfgSysTnetState_Type(Integer32):
    """Custom type vADCNewCfgSysTnetState based on Integer32"""
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


_VADCNewCfgSysTnetState_Type.__name__ = "Integer32"
_VADCNewCfgSysTnetState_Object = MibTableColumn
vADCNewCfgSysTnetState = _VADCNewCfgSysTnetState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 27),
    _VADCNewCfgSysTnetState_Type()
)
vADCNewCfgSysTnetState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysTnetState.setStatus("current")


class _VADCNewCfgSysHaId_Type(Integer32):
    """Custom type vADCNewCfgSysHaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_VADCNewCfgSysHaId_Type.__name__ = "Integer32"
_VADCNewCfgSysHaId_Object = MibTableColumn
vADCNewCfgSysHaId = _VADCNewCfgSysHaId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 28),
    _VADCNewCfgSysHaId_Type()
)
vADCNewCfgSysHaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysHaId.setStatus("current")


class _VADCNewCfgSysPeerId_Type(Integer32):
    """Custom type vADCNewCfgSysPeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_VADCNewCfgSysPeerId_Type.__name__ = "Integer32"
_VADCNewCfgSysPeerId_Object = MibTableColumn
vADCNewCfgSysPeerId = _VADCNewCfgSysPeerId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 29),
    _VADCNewCfgSysPeerId_Type()
)
vADCNewCfgSysPeerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysPeerId.setStatus("current")
_VADCNewCfgSysVADCId_Type = Integer32
_VADCNewCfgSysVADCId_Object = MibTableColumn
vADCNewCfgSysVADCId = _VADCNewCfgSysVADCId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 30),
    _VADCNewCfgSysVADCId_Type()
)
vADCNewCfgSysVADCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCNewCfgSysVADCId.setStatus("current")


class _VADCNewCfgIdleDelegation_Type(Integer32):
    """Custom type vADCNewCfgIdleDelegation based on Integer32"""
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


_VADCNewCfgIdleDelegation_Type.__name__ = "Integer32"
_VADCNewCfgIdleDelegation_Object = MibTableColumn
vADCNewCfgIdleDelegation = _VADCNewCfgIdleDelegation_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 31),
    _VADCNewCfgIdleDelegation_Type()
)
vADCNewCfgIdleDelegation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgIdleDelegation.setStatus("current")


class _VADCNewCfgSysMmgmtDelegation_Type(Integer32):
    """Custom type vADCNewCfgSysMmgmtDelegation based on Integer32"""
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


_VADCNewCfgSysMmgmtDelegation_Type.__name__ = "Integer32"
_VADCNewCfgSysMmgmtDelegation_Object = MibTableColumn
vADCNewCfgSysMmgmtDelegation = _VADCNewCfgSysMmgmtDelegation_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 32),
    _VADCNewCfgSysMmgmtDelegation_Type()
)
vADCNewCfgSysMmgmtDelegation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysMmgmtDelegation.setStatus("current")


class _VADCNewCfgSysPeerName_Type(DisplayString):
    """Custom type vADCNewCfgSysPeerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VADCNewCfgSysPeerName_Type.__name__ = "DisplayString"
_VADCNewCfgSysPeerName_Object = MibTableColumn
vADCNewCfgSysPeerName = _VADCNewCfgSysPeerName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 6, 1, 33),
    _VADCNewCfgSysPeerName_Type()
)
vADCNewCfgSysPeerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgSysPeerName.setStatus("current")
_VADCCurCfgNetTable_Object = MibTable
vADCCurCfgNetTable = _VADCCurCfgNetTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    vADCCurCfgNetTable.setStatus("current")
_VADCCurCfgNetTableEntry_Object = MibTableRow
vADCCurCfgNetTableEntry = _VADCCurCfgNetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 7, 1)
)
vADCCurCfgNetTableEntry.setIndexNames(
    (0, "ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgNetVADCId"),
    (0, "ADMIN-ALTEON-AC-vADC-MIB", "vADCCurCfgNetId"),
)
if mibBuilder.loadTexts:
    vADCCurCfgNetTableEntry.setStatus("current")


class _VADCCurCfgNetId_Type(Integer32):
    """Custom type vADCCurCfgNetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VADCCurCfgNetId_Type.__name__ = "Integer32"
_VADCCurCfgNetId_Object = MibTableColumn
vADCCurCfgNetId = _VADCCurCfgNetId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 7, 1, 1),
    _VADCCurCfgNetId_Type()
)
vADCCurCfgNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgNetId.setStatus("current")


class _VADCCurCfgNetVlanId_Type(Integer32):
    """Custom type vADCCurCfgNetVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_VADCCurCfgNetVlanId_Type.__name__ = "Integer32"
_VADCCurCfgNetVlanId_Object = MibTableColumn
vADCCurCfgNetVlanId = _VADCCurCfgNetVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 7, 1, 2),
    _VADCCurCfgNetVlanId_Type()
)
vADCCurCfgNetVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgNetVlanId.setStatus("current")


class _VADCCurCfgNetIPver_Type(Integer32):
    """Custom type vADCCurCfgNetIPver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 4),
          ("ipv6", 6))
    )


_VADCCurCfgNetIPver_Type.__name__ = "Integer32"
_VADCCurCfgNetIPver_Object = MibTableColumn
vADCCurCfgNetIPver = _VADCCurCfgNetIPver_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 7, 1, 3),
    _VADCCurCfgNetIPver_Type()
)
vADCCurCfgNetIPver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgNetIPver.setStatus("current")
_VADCCurCfgNetIPBegin_Type = IpAddress
_VADCCurCfgNetIPBegin_Object = MibTableColumn
vADCCurCfgNetIPBegin = _VADCCurCfgNetIPBegin_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 7, 1, 4),
    _VADCCurCfgNetIPBegin_Type()
)
vADCCurCfgNetIPBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgNetIPBegin.setStatus("current")
_VADCCurCfgNetMask_Type = IpAddress
_VADCCurCfgNetMask_Object = MibTableColumn
vADCCurCfgNetMask = _VADCCurCfgNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 7, 1, 5),
    _VADCCurCfgNetMask_Type()
)
vADCCurCfgNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgNetMask.setStatus("current")
_VADCCurCfgNetIPEnd_Type = IpAddress
_VADCCurCfgNetIPEnd_Object = MibTableColumn
vADCCurCfgNetIPEnd = _VADCCurCfgNetIPEnd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 7, 1, 6),
    _VADCCurCfgNetIPEnd_Type()
)
vADCCurCfgNetIPEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgNetIPEnd.setStatus("current")


class _VADCCurCfgNetIPv6Begin_Type(DisplayString):
    """Custom type vADCCurCfgNetIPv6Begin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VADCCurCfgNetIPv6Begin_Type.__name__ = "DisplayString"
_VADCCurCfgNetIPv6Begin_Object = MibTableColumn
vADCCurCfgNetIPv6Begin = _VADCCurCfgNetIPv6Begin_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 7, 1, 7),
    _VADCCurCfgNetIPv6Begin_Type()
)
vADCCurCfgNetIPv6Begin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgNetIPv6Begin.setStatus("current")


class _VADCCurCfgNetPrefix_Type(Integer32):
    """Custom type vADCCurCfgNetPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_VADCCurCfgNetPrefix_Type.__name__ = "Integer32"
_VADCCurCfgNetPrefix_Object = MibTableColumn
vADCCurCfgNetPrefix = _VADCCurCfgNetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 7, 1, 8),
    _VADCCurCfgNetPrefix_Type()
)
vADCCurCfgNetPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgNetPrefix.setStatus("current")


class _VADCCurCfgNetIPv6End_Type(DisplayString):
    """Custom type vADCCurCfgNetIPv6End based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VADCCurCfgNetIPv6End_Type.__name__ = "DisplayString"
_VADCCurCfgNetIPv6End_Object = MibTableColumn
vADCCurCfgNetIPv6End = _VADCCurCfgNetIPv6End_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 7, 1, 9),
    _VADCCurCfgNetIPv6End_Type()
)
vADCCurCfgNetIPv6End.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgNetIPv6End.setStatus("current")
_VADCCurCfgNetVADCId_Type = Integer32
_VADCCurCfgNetVADCId_Object = MibTableColumn
vADCCurCfgNetVADCId = _VADCCurCfgNetVADCId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 7, 1, 10),
    _VADCCurCfgNetVADCId_Type()
)
vADCCurCfgNetVADCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCCurCfgNetVADCId.setStatus("current")
_VADCNewCfgNetTable_Object = MibTable
vADCNewCfgNetTable = _VADCNewCfgNetTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    vADCNewCfgNetTable.setStatus("current")
_VADCNewCfgNetTableEntry_Object = MibTableRow
vADCNewCfgNetTableEntry = _VADCNewCfgNetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 8, 1)
)
vADCNewCfgNetTableEntry.setIndexNames(
    (0, "ADMIN-ALTEON-AC-vADC-MIB", "vADCNewCfgNetVADCId"),
    (0, "ADMIN-ALTEON-AC-vADC-MIB", "vADCNewCfgNetId"),
)
if mibBuilder.loadTexts:
    vADCNewCfgNetTableEntry.setStatus("current")


class _VADCNewCfgNetId_Type(Integer32):
    """Custom type vADCNewCfgNetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VADCNewCfgNetId_Type.__name__ = "Integer32"
_VADCNewCfgNetId_Object = MibTableColumn
vADCNewCfgNetId = _VADCNewCfgNetId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 8, 1, 1),
    _VADCNewCfgNetId_Type()
)
vADCNewCfgNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCNewCfgNetId.setStatus("current")


class _VADCNewCfgNetVlanId_Type(Integer32):
    """Custom type vADCNewCfgNetVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_VADCNewCfgNetVlanId_Type.__name__ = "Integer32"
_VADCNewCfgNetVlanId_Object = MibTableColumn
vADCNewCfgNetVlanId = _VADCNewCfgNetVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 8, 1, 2),
    _VADCNewCfgNetVlanId_Type()
)
vADCNewCfgNetVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgNetVlanId.setStatus("current")


class _VADCNewCfgNetIPver_Type(Integer32):
    """Custom type vADCNewCfgNetIPver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 4),
          ("ipv6", 6))
    )


_VADCNewCfgNetIPver_Type.__name__ = "Integer32"
_VADCNewCfgNetIPver_Object = MibTableColumn
vADCNewCfgNetIPver = _VADCNewCfgNetIPver_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 8, 1, 3),
    _VADCNewCfgNetIPver_Type()
)
vADCNewCfgNetIPver.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgNetIPver.setStatus("current")
_VADCNewCfgNetIPBegin_Type = IpAddress
_VADCNewCfgNetIPBegin_Object = MibTableColumn
vADCNewCfgNetIPBegin = _VADCNewCfgNetIPBegin_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 8, 1, 4),
    _VADCNewCfgNetIPBegin_Type()
)
vADCNewCfgNetIPBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgNetIPBegin.setStatus("current")
_VADCNewCfgNetMask_Type = IpAddress
_VADCNewCfgNetMask_Object = MibTableColumn
vADCNewCfgNetMask = _VADCNewCfgNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 8, 1, 5),
    _VADCNewCfgNetMask_Type()
)
vADCNewCfgNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgNetMask.setStatus("current")
_VADCNewCfgNetIPEnd_Type = IpAddress
_VADCNewCfgNetIPEnd_Object = MibTableColumn
vADCNewCfgNetIPEnd = _VADCNewCfgNetIPEnd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 8, 1, 6),
    _VADCNewCfgNetIPEnd_Type()
)
vADCNewCfgNetIPEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgNetIPEnd.setStatus("current")


class _VADCNewCfgNetRemId_Type(Integer32):
    """Custom type vADCNewCfgNetRemId based on Integer32"""
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


_VADCNewCfgNetRemId_Type.__name__ = "Integer32"
_VADCNewCfgNetRemId_Object = MibTableColumn
vADCNewCfgNetRemId = _VADCNewCfgNetRemId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 8, 1, 7),
    _VADCNewCfgNetRemId_Type()
)
vADCNewCfgNetRemId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgNetRemId.setStatus("current")


class _VADCNewCfgNetIPv6Begin_Type(DisplayString):
    """Custom type vADCNewCfgNetIPv6Begin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VADCNewCfgNetIPv6Begin_Type.__name__ = "DisplayString"
_VADCNewCfgNetIPv6Begin_Object = MibTableColumn
vADCNewCfgNetIPv6Begin = _VADCNewCfgNetIPv6Begin_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 8, 1, 8),
    _VADCNewCfgNetIPv6Begin_Type()
)
vADCNewCfgNetIPv6Begin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgNetIPv6Begin.setStatus("current")


class _VADCNewCfgNetPrefix_Type(Integer32):
    """Custom type vADCNewCfgNetPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_VADCNewCfgNetPrefix_Type.__name__ = "Integer32"
_VADCNewCfgNetPrefix_Object = MibTableColumn
vADCNewCfgNetPrefix = _VADCNewCfgNetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 8, 1, 9),
    _VADCNewCfgNetPrefix_Type()
)
vADCNewCfgNetPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgNetPrefix.setStatus("current")


class _VADCNewCfgNetIPv6End_Type(DisplayString):
    """Custom type vADCNewCfgNetIPv6End based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VADCNewCfgNetIPv6End_Type.__name__ = "DisplayString"
_VADCNewCfgNetIPv6End_Object = MibTableColumn
vADCNewCfgNetIPv6End = _VADCNewCfgNetIPv6End_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 8, 1, 10),
    _VADCNewCfgNetIPv6End_Type()
)
vADCNewCfgNetIPv6End.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCNewCfgNetIPv6End.setStatus("current")
_VADCNewCfgNetVADCId_Type = Integer32
_VADCNewCfgNetVADCId_Object = MibTableColumn
vADCNewCfgNetVADCId = _VADCNewCfgNetVADCId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 8, 1, 11),
    _VADCNewCfgNetVADCId_Type()
)
vADCNewCfgNetVADCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCNewCfgNetVADCId.setStatus("current")
_VADCAccessUser_ObjectIdentity = ObjectIdentity
vADCAccessUser = _VADCAccessUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9)
)
_VADCAccessUid_ObjectIdentity = ObjectIdentity
vADCAccessUid = _VADCAccessUid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1)
)
_VADCUserCurCfgTable_Object = MibTable
vADCUserCurCfgTable = _VADCUserCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    vADCUserCurCfgTable.setStatus("current")
_VADCUserCurCfgTableEntry_Object = MibTableRow
vADCUserCurCfgTableEntry = _VADCUserCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 1, 1)
)
vADCUserCurCfgTableEntry.setIndexNames(
    (0, "ADMIN-ALTEON-AC-vADC-MIB", "vADCUserCurCfgVADCId"),
    (0, "ADMIN-ALTEON-AC-vADC-MIB", "vADCUserCurCfgUId"),
)
if mibBuilder.loadTexts:
    vADCUserCurCfgTableEntry.setStatus("current")
_VADCUserCurCfgVADCId_Type = Integer32
_VADCUserCurCfgVADCId_Object = MibTableColumn
vADCUserCurCfgVADCId = _VADCUserCurCfgVADCId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 1, 1, 1),
    _VADCUserCurCfgVADCId_Type()
)
vADCUserCurCfgVADCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCUserCurCfgVADCId.setStatus("current")
_VADCUserCurCfgUId_Type = Integer32
_VADCUserCurCfgUId_Object = MibTableColumn
vADCUserCurCfgUId = _VADCUserCurCfgUId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 1, 1, 2),
    _VADCUserCurCfgUId_Type()
)
vADCUserCurCfgUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCUserCurCfgUId.setStatus("current")


class _VADCUserCurCos_Type(Integer32):
    """Custom type vADCUserCurCos based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("admin", 10),
          ("crtadmin", 4),
          ("l3Oper", 1),
          ("l3admin", 7),
          ("l4admin", 9),
          ("l4oper", 5),
          ("oper", 6),
          ("slbadmin", 8),
          ("slboper", 2),
          ("slbview", 3),
          ("user", 0))
    )


_VADCUserCurCos_Type.__name__ = "Integer32"
_VADCUserCurCos_Object = MibTableColumn
vADCUserCurCos = _VADCUserCurCos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 1, 1, 3),
    _VADCUserCurCos_Type()
)
vADCUserCurCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCUserCurCos.setStatus("current")


class _VADCUserCurCfgName_Type(DisplayString):
    """Custom type vADCUserCurCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VADCUserCurCfgName_Type.__name__ = "DisplayString"
_VADCUserCurCfgName_Object = MibTableColumn
vADCUserCurCfgName = _VADCUserCurCfgName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 1, 1, 4),
    _VADCUserCurCfgName_Type()
)
vADCUserCurCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCUserCurCfgName.setStatus("current")


class _VADCUserCurCfgAdminPswd_Type(DisplayString):
    """Custom type vADCUserCurCfgAdminPswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VADCUserCurCfgAdminPswd_Type.__name__ = "DisplayString"
_VADCUserCurCfgAdminPswd_Object = MibTableColumn
vADCUserCurCfgAdminPswd = _VADCUserCurCfgAdminPswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 1, 1, 5),
    _VADCUserCurCfgAdminPswd_Type()
)
vADCUserCurCfgAdminPswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCUserCurCfgAdminPswd.setStatus("current")


class _VADCUserCurCfgPswd_Type(DisplayString):
    """Custom type vADCUserCurCfgPswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VADCUserCurCfgPswd_Type.__name__ = "DisplayString"
_VADCUserCurCfgPswd_Object = MibTableColumn
vADCUserCurCfgPswd = _VADCUserCurCfgPswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 1, 1, 6),
    _VADCUserCurCfgPswd_Type()
)
vADCUserCurCfgPswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCUserCurCfgPswd.setStatus("current")


class _VADCUserCurCfgConfPswd_Type(DisplayString):
    """Custom type vADCUserCurCfgConfPswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VADCUserCurCfgConfPswd_Type.__name__ = "DisplayString"
_VADCUserCurCfgConfPswd_Object = MibTableColumn
vADCUserCurCfgConfPswd = _VADCUserCurCfgConfPswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 1, 1, 7),
    _VADCUserCurCfgConfPswd_Type()
)
vADCUserCurCfgConfPswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCUserCurCfgConfPswd.setStatus("current")


class _VADCUserCurCfgBackdoor_Type(Integer32):
    """Custom type vADCUserCurCfgBackdoor based on Integer32"""
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


_VADCUserCurCfgBackdoor_Type.__name__ = "Integer32"
_VADCUserCurCfgBackdoor_Object = MibTableColumn
vADCUserCurCfgBackdoor = _VADCUserCurCfgBackdoor_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 1, 1, 8),
    _VADCUserCurCfgBackdoor_Type()
)
vADCUserCurCfgBackdoor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCUserCurCfgBackdoor.setStatus("current")


class _VADCUserCurCfgCrtMng_Type(Integer32):
    """Custom type vADCUserCurCfgCrtMng based on Integer32"""
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


_VADCUserCurCfgCrtMng_Type.__name__ = "Integer32"
_VADCUserCurCfgCrtMng_Object = MibTableColumn
vADCUserCurCfgCrtMng = _VADCUserCurCfgCrtMng_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 1, 1, 9),
    _VADCUserCurCfgCrtMng_Type()
)
vADCUserCurCfgCrtMng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCUserCurCfgCrtMng.setStatus("current")


class _VADCUserCurCfgState_Type(Integer32):
    """Custom type vADCUserCurCfgState based on Integer32"""
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


_VADCUserCurCfgState_Type.__name__ = "Integer32"
_VADCUserCurCfgState_Object = MibTableColumn
vADCUserCurCfgState = _VADCUserCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 1, 1, 10),
    _VADCUserCurCfgState_Type()
)
vADCUserCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCUserCurCfgState.setStatus("current")
_VADCUserNewCfgTable_Object = MibTable
vADCUserNewCfgTable = _VADCUserNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    vADCUserNewCfgTable.setStatus("current")
_VADCUserNewCfgTableEntry_Object = MibTableRow
vADCUserNewCfgTableEntry = _VADCUserNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 2, 1)
)
vADCUserNewCfgTableEntry.setIndexNames(
    (0, "ADMIN-ALTEON-AC-vADC-MIB", "vADCUserNewCfgVADCId"),
    (0, "ADMIN-ALTEON-AC-vADC-MIB", "vADCUserNewCfgUId"),
)
if mibBuilder.loadTexts:
    vADCUserNewCfgTableEntry.setStatus("current")
_VADCUserNewCfgVADCId_Type = Integer32
_VADCUserNewCfgVADCId_Object = MibTableColumn
vADCUserNewCfgVADCId = _VADCUserNewCfgVADCId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 2, 1, 1),
    _VADCUserNewCfgVADCId_Type()
)
vADCUserNewCfgVADCId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCUserNewCfgVADCId.setStatus("current")
_VADCUserNewCfgUId_Type = Integer32
_VADCUserNewCfgUId_Object = MibTableColumn
vADCUserNewCfgUId = _VADCUserNewCfgUId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 2, 1, 2),
    _VADCUserNewCfgUId_Type()
)
vADCUserNewCfgUId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCUserNewCfgUId.setStatus("current")


class _VADCUserNewCos_Type(Integer32):
    """Custom type vADCUserNewCos based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("admin", 10),
          ("crtadmin", 4),
          ("l3admin", 7),
          ("l3oper", 1),
          ("l4admin", 9),
          ("l4oper", 5),
          ("oper", 6),
          ("slbadmin", 8),
          ("slboper", 2),
          ("slbview", 3),
          ("user", 0))
    )


_VADCUserNewCos_Type.__name__ = "Integer32"
_VADCUserNewCos_Object = MibTableColumn
vADCUserNewCos = _VADCUserNewCos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 2, 1, 3),
    _VADCUserNewCos_Type()
)
vADCUserNewCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCUserNewCos.setStatus("current")


class _VADCUserNewCfgName_Type(DisplayString):
    """Custom type vADCUserNewCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VADCUserNewCfgName_Type.__name__ = "DisplayString"
_VADCUserNewCfgName_Object = MibTableColumn
vADCUserNewCfgName = _VADCUserNewCfgName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 2, 1, 4),
    _VADCUserNewCfgName_Type()
)
vADCUserNewCfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCUserNewCfgName.setStatus("current")


class _VADCUserNewCfgAdminPswd_Type(DisplayString):
    """Custom type vADCUserNewCfgAdminPswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VADCUserNewCfgAdminPswd_Type.__name__ = "DisplayString"
_VADCUserNewCfgAdminPswd_Object = MibTableColumn
vADCUserNewCfgAdminPswd = _VADCUserNewCfgAdminPswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 2, 1, 5),
    _VADCUserNewCfgAdminPswd_Type()
)
vADCUserNewCfgAdminPswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCUserNewCfgAdminPswd.setStatus("current")


class _VADCUserNewCfgPswd_Type(DisplayString):
    """Custom type vADCUserNewCfgPswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VADCUserNewCfgPswd_Type.__name__ = "DisplayString"
_VADCUserNewCfgPswd_Object = MibTableColumn
vADCUserNewCfgPswd = _VADCUserNewCfgPswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 2, 1, 6),
    _VADCUserNewCfgPswd_Type()
)
vADCUserNewCfgPswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCUserNewCfgPswd.setStatus("current")


class _VADCUserNewCfgConfPswd_Type(DisplayString):
    """Custom type vADCUserNewCfgConfPswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VADCUserNewCfgConfPswd_Type.__name__ = "DisplayString"
_VADCUserNewCfgConfPswd_Object = MibTableColumn
vADCUserNewCfgConfPswd = _VADCUserNewCfgConfPswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 2, 1, 7),
    _VADCUserNewCfgConfPswd_Type()
)
vADCUserNewCfgConfPswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCUserNewCfgConfPswd.setStatus("current")


class _VADCUserNewCfgBackdoor_Type(Integer32):
    """Custom type vADCUserNewCfgBackdoor based on Integer32"""
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


_VADCUserNewCfgBackdoor_Type.__name__ = "Integer32"
_VADCUserNewCfgBackdoor_Object = MibTableColumn
vADCUserNewCfgBackdoor = _VADCUserNewCfgBackdoor_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 2, 1, 8),
    _VADCUserNewCfgBackdoor_Type()
)
vADCUserNewCfgBackdoor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCUserNewCfgBackdoor.setStatus("current")


class _VADCUserNewCfgCrtMng_Type(Integer32):
    """Custom type vADCUserNewCfgCrtMng based on Integer32"""
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


_VADCUserNewCfgCrtMng_Type.__name__ = "Integer32"
_VADCUserNewCfgCrtMng_Object = MibTableColumn
vADCUserNewCfgCrtMng = _VADCUserNewCfgCrtMng_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 2, 1, 9),
    _VADCUserNewCfgCrtMng_Type()
)
vADCUserNewCfgCrtMng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCUserNewCfgCrtMng.setStatus("current")


class _VADCUserNewCfgState_Type(Integer32):
    """Custom type vADCUserNewCfgState based on Integer32"""
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


_VADCUserNewCfgState_Type.__name__ = "Integer32"
_VADCUserNewCfgState_Object = MibTableColumn
vADCUserNewCfgState = _VADCUserNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 2, 1, 10),
    _VADCUserNewCfgState_Type()
)
vADCUserNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCUserNewCfgState.setStatus("current")


class _VADCUserNewCfgDelete_Type(Integer32):
    """Custom type vADCUserNewCfgDelete based on Integer32"""
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


_VADCUserNewCfgDelete_Type.__name__ = "Integer32"
_VADCUserNewCfgDelete_Object = MibTableColumn
vADCUserNewCfgDelete = _VADCUserNewCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 1, 2, 1, 11),
    _VADCUserNewCfgDelete_Type()
)
vADCUserNewCfgDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCUserNewCfgDelete.setStatus("current")
_VADCUsersPswdTable_Object = MibTable
vADCUsersPswdTable = _VADCUsersPswdTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 2)
)
if mibBuilder.loadTexts:
    vADCUsersPswdTable.setStatus("current")
_VADCUsersPswdTableEntry_Object = MibTableRow
vADCUsersPswdTableEntry = _VADCUsersPswdTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 2, 1)
)
vADCUsersPswdTableEntry.setIndexNames(
    (0, "ADMIN-ALTEON-AC-vADC-MIB", "vADCUsersVADCId"),
)
if mibBuilder.loadTexts:
    vADCUsersPswdTableEntry.setStatus("current")
_VADCUsersVADCId_Type = Integer32
_VADCUsersVADCId_Object = MibTableColumn
vADCUsersVADCId = _VADCUsersVADCId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 2, 1, 1),
    _VADCUsersVADCId_Type()
)
vADCUsersVADCId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCUsersVADCId.setStatus("current")


class _VADCAccessUsrPasswd_Type(DisplayString):
    """Custom type vADCAccessUsrPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VADCAccessUsrPasswd_Type.__name__ = "DisplayString"
_VADCAccessUsrPasswd_Object = MibTableColumn
vADCAccessUsrPasswd = _VADCAccessUsrPasswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 2, 1, 2),
    _VADCAccessUsrPasswd_Type()
)
vADCAccessUsrPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCAccessUsrPasswd.setStatus("current")


class _VADCAccessSlbOperPasswd_Type(DisplayString):
    """Custom type vADCAccessSlbOperPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VADCAccessSlbOperPasswd_Type.__name__ = "DisplayString"
_VADCAccessSlbOperPasswd_Object = MibTableColumn
vADCAccessSlbOperPasswd = _VADCAccessSlbOperPasswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 2, 1, 3),
    _VADCAccessSlbOperPasswd_Type()
)
vADCAccessSlbOperPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCAccessSlbOperPasswd.setStatus("current")


class _VADCAccessL4OperPasswd_Type(DisplayString):
    """Custom type vADCAccessL4OperPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VADCAccessL4OperPasswd_Type.__name__ = "DisplayString"
_VADCAccessL4OperPasswd_Object = MibTableColumn
vADCAccessL4OperPasswd = _VADCAccessL4OperPasswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 2, 1, 4),
    _VADCAccessL4OperPasswd_Type()
)
vADCAccessL4OperPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCAccessL4OperPasswd.setStatus("current")


class _VADCAccessOperPasswd_Type(DisplayString):
    """Custom type vADCAccessOperPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VADCAccessOperPasswd_Type.__name__ = "DisplayString"
_VADCAccessOperPasswd_Object = MibTableColumn
vADCAccessOperPasswd = _VADCAccessOperPasswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 2, 1, 5),
    _VADCAccessOperPasswd_Type()
)
vADCAccessOperPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCAccessOperPasswd.setStatus("current")


class _VADCAccessSlbAdminPasswd_Type(DisplayString):
    """Custom type vADCAccessSlbAdminPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VADCAccessSlbAdminPasswd_Type.__name__ = "DisplayString"
_VADCAccessSlbAdminPasswd_Object = MibTableColumn
vADCAccessSlbAdminPasswd = _VADCAccessSlbAdminPasswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 2, 1, 6),
    _VADCAccessSlbAdminPasswd_Type()
)
vADCAccessSlbAdminPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCAccessSlbAdminPasswd.setStatus("current")


class _VADCAccessL4AdminPasswd_Type(DisplayString):
    """Custom type vADCAccessL4AdminPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VADCAccessL4AdminPasswd_Type.__name__ = "DisplayString"
_VADCAccessL4AdminPasswd_Object = MibTableColumn
vADCAccessL4AdminPasswd = _VADCAccessL4AdminPasswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 2, 1, 7),
    _VADCAccessL4AdminPasswd_Type()
)
vADCAccessL4AdminPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCAccessL4AdminPasswd.setStatus("current")


class _VADCAccessAdminPasswd_Type(DisplayString):
    """Custom type vADCAccessAdminPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VADCAccessAdminPasswd_Type.__name__ = "DisplayString"
_VADCAccessAdminPasswd_Object = MibTableColumn
vADCAccessAdminPasswd = _VADCAccessAdminPasswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 2, 1, 8),
    _VADCAccessAdminPasswd_Type()
)
vADCAccessAdminPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCAccessAdminPasswd.setStatus("current")


class _VADCAccessAdminNewPasswd_Type(DisplayString):
    """Custom type vADCAccessAdminNewPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VADCAccessAdminNewPasswd_Type.__name__ = "DisplayString"
_VADCAccessAdminNewPasswd_Object = MibTableColumn
vADCAccessAdminNewPasswd = _VADCAccessAdminNewPasswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 2, 1, 9),
    _VADCAccessAdminNewPasswd_Type()
)
vADCAccessAdminNewPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCAccessAdminNewPasswd.setStatus("current")


class _VADCAccessAdminConfNewPasswd_Type(DisplayString):
    """Custom type vADCAccessAdminConfNewPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VADCAccessAdminConfNewPasswd_Type.__name__ = "DisplayString"
_VADCAccessAdminConfNewPasswd_Object = MibTableColumn
vADCAccessAdminConfNewPasswd = _VADCAccessAdminConfNewPasswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 1, 1, 9, 2, 1, 10),
    _VADCAccessAdminConfNewPasswd_Type()
)
vADCAccessAdminConfNewPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vADCAccessAdminConfNewPasswd.setStatus("current")
_AdminvADCInfo_ObjectIdentity = ObjectIdentity
adminvADCInfo = _AdminvADCInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 2)
)
_VADCInfo_ObjectIdentity = ObjectIdentity
vADCInfo = _VADCInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 2, 1)
)


class _VADCInfoAvailableCU_Type(Integer32):
    """Custom type vADCInfoAvailableCU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_VADCInfoAvailableCU_Type.__name__ = "Integer32"
_VADCInfoAvailableCU_Object = MibScalar
vADCInfoAvailableCU = _VADCInfoAvailableCU_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 2, 1, 1),
    _VADCInfoAvailableCU_Type()
)
vADCInfoAvailableCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCInfoAvailableCU.setStatus("current")


class _VADCInfoAvailableThruput_Type(Integer32):
    """Custom type vADCInfoAvailableThruput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_VADCInfoAvailableThruput_Type.__name__ = "Integer32"
_VADCInfoAvailableThruput_Object = MibScalar
vADCInfoAvailableThruput = _VADCInfoAvailableThruput_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 2, 1, 2),
    _VADCInfoAvailableThruput_Type()
)
vADCInfoAvailableThruput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCInfoAvailableThruput.setStatus("current")
_VADCInfoTable_Object = MibTable
vADCInfoTable = _VADCInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    vADCInfoTable.setStatus("current")
_VADCInfoTableEntry_Object = MibTableRow
vADCInfoTableEntry = _VADCInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 2, 1, 3, 1)
)
vADCInfoTableEntry.setIndexNames(
    (0, "ADMIN-ALTEON-AC-vADC-MIB", "vADCInfoId"),
)
if mibBuilder.loadTexts:
    vADCInfoTableEntry.setStatus("current")


class _VADCInfoId_Type(Integer32):
    """Custom type vADCInfoId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_VADCInfoId_Type.__name__ = "Integer32"
_VADCInfoId_Object = MibTableColumn
vADCInfoId = _VADCInfoId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 2, 1, 3, 1, 1),
    _VADCInfoId_Type()
)
vADCInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCInfoId.setStatus("current")


class _VADCInfoName_Type(DisplayString):
    """Custom type vADCInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_VADCInfoName_Type.__name__ = "DisplayString"
_VADCInfoName_Object = MibTableColumn
vADCInfoName = _VADCInfoName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 2, 1, 3, 1, 2),
    _VADCInfoName_Type()
)
vADCInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCInfoName.setStatus("current")


class _VADCInfoStatus_Type(Integer32):
    """Custom type vADCInfoStatus based on Integer32"""
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
        *(("disabled", 0),
          ("down", 3),
          ("init", 1),
          ("querying", 6),
          ("restarting", 5),
          ("running", 2),
          ("stopping", 4))
    )


_VADCInfoStatus_Type.__name__ = "Integer32"
_VADCInfoStatus_Object = MibTableColumn
vADCInfoStatus = _VADCInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 2, 1, 3, 1, 3),
    _VADCInfoStatus_Type()
)
vADCInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCInfoStatus.setStatus("current")


class _VADCInfoVRRPStatus_Type(Integer32):
    """Custom type vADCInfoVRRPStatus based on Integer32"""
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
        *(("active", 6),
          ("backup", 3),
          ("holdoff", 4),
          ("init", 1),
          ("master", 2),
          ("off", 5),
          ("standby", 7))
    )


_VADCInfoVRRPStatus_Type.__name__ = "Integer32"
_VADCInfoVRRPStatus_Object = MibTableColumn
vADCInfoVRRPStatus = _VADCInfoVRRPStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 2, 1, 3, 1, 4),
    _VADCInfoVRRPStatus_Type()
)
vADCInfoVRRPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCInfoVRRPStatus.setStatus("current")


class _VADCInfoCU_Type(Integer32):
    """Custom type vADCInfoCU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_VADCInfoCU_Type.__name__ = "Integer32"
_VADCInfoCU_Object = MibTableColumn
vADCInfoCU = _VADCInfoCU_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 2, 1, 3, 1, 5),
    _VADCInfoCU_Type()
)
vADCInfoCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCInfoCU.setStatus("current")


class _VADCInfoThroughput_Type(Integer32):
    """Custom type vADCInfoThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_VADCInfoThroughput_Type.__name__ = "Integer32"
_VADCInfoThroughput_Object = MibTableColumn
vADCInfoThroughput = _VADCInfoThroughput_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 2, 1, 3, 1, 6),
    _VADCInfoThroughput_Type()
)
vADCInfoThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCInfoThroughput.setStatus("current")


class _VADCInfoLimit_Type(Integer32):
    """Custom type vADCInfoLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_VADCInfoLimit_Type.__name__ = "Integer32"
_VADCInfoLimit_Object = MibTableColumn
vADCInfoLimit = _VADCInfoLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 2, 1, 3, 1, 7),
    _VADCInfoLimit_Type()
)
vADCInfoLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCInfoLimit.setStatus("current")


class _VADCInfoSPcpu_Type(Integer32):
    """Custom type vADCInfoSPcpu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VADCInfoSPcpu_Type.__name__ = "Integer32"
_VADCInfoSPcpu_Object = MibTableColumn
vADCInfoSPcpu = _VADCInfoSPcpu_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 2, 1, 3, 1, 8),
    _VADCInfoSPcpu_Type()
)
vADCInfoSPcpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCInfoSPcpu.setStatus("current")


class _VADCInfoMPcpu_Type(Integer32):
    """Custom type vADCInfoMPcpu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VADCInfoMPcpu_Type.__name__ = "Integer32"
_VADCInfoMPcpu_Object = MibTableColumn
vADCInfoMPcpu = _VADCInfoMPcpu_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 2, 1, 3, 1, 9),
    _VADCInfoMPcpu_Type()
)
vADCInfoMPcpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCInfoMPcpu.setStatus("current")
_VADCInfoCUMbit_Type = Integer32
_VADCInfoCUMbit_Object = MibTableColumn
vADCInfoCUMbit = _VADCInfoCUMbit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 2, 1, 3, 1, 10),
    _VADCInfoCUMbit_Type()
)
vADCInfoCUMbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCInfoCUMbit.setStatus("current")
_VADCInfoUpTime_Type = DisplayString
_VADCInfoUpTime_Object = MibTableColumn
vADCInfoUpTime = _VADCInfoUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 2, 1, 3, 1, 11),
    _VADCInfoUpTime_Type()
)
vADCInfoUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCInfoUpTime.setStatus("current")
_VADCInfoConfigChangeTime_Type = TimeTicks
_VADCInfoConfigChangeTime_Object = MibScalar
vADCInfoConfigChangeTime = _VADCInfoConfigChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 2, 1, 4),
    _VADCInfoConfigChangeTime_Type()
)
vADCInfoConfigChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCInfoConfigChangeTime.setStatus("current")
_AdminvADCBoot_ObjectIdentity = ObjectIdentity
adminvADCBoot = _AdminvADCBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 3)
)
_VADCBoot_ObjectIdentity = ObjectIdentity
vADCBoot = _VADCBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 3, 1)
)
_VADCBootTable_Object = MibTable
vADCBootTable = _VADCBootTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    vADCBootTable.setStatus("current")
_VADCBootTableEntry_Object = MibTableRow
vADCBootTableEntry = _VADCBootTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 3, 1, 1, 1)
)
vADCBootTableEntry.setIndexNames(
    (0, "ADMIN-ALTEON-AC-vADC-MIB", "vADCBootVADCId"),
)
if mibBuilder.loadTexts:
    vADCBootTableEntry.setStatus("current")


class _VADCBootVADCId_Type(Integer32):
    """Custom type vADCBootVADCId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_VADCBootVADCId_Type.__name__ = "Integer32"
_VADCBootVADCId_Object = MibTableColumn
vADCBootVADCId = _VADCBootVADCId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 3, 1, 1, 1, 1),
    _VADCBootVADCId_Type()
)
vADCBootVADCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCBootVADCId.setStatus("current")


class _VADCBootAction_Type(Integer32):
    """Custom type vADCBootAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("reset", 2))
    )


_VADCBootAction_Type.__name__ = "Integer32"
_VADCBootAction_Object = MibTableColumn
vADCBootAction = _VADCBootAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 3, 1, 1, 1, 2),
    _VADCBootAction_Type()
)
vADCBootAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vADCBootAction.setStatus("current")
_AdminvADCStats_ObjectIdentity = ObjectIdentity
adminvADCStats = _AdminvADCStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 4)
)
_VADCStat_ObjectIdentity = ObjectIdentity
vADCStat = _VADCStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 4, 1)
)
_VADCStatsAccelResourceTable_Object = MibTable
vADCStatsAccelResourceTable = _VADCStatsAccelResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    vADCStatsAccelResourceTable.setStatus("current")
_VADCStatsAccelResourceTableEntry_Object = MibTableRow
vADCStatsAccelResourceTableEntry = _VADCStatsAccelResourceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 4, 1, 1, 1)
)
vADCStatsAccelResourceTableEntry.setIndexNames(
    (0, "ADMIN-ALTEON-AC-vADC-MIB", "vADCIndex"),
)
if mibBuilder.loadTexts:
    vADCStatsAccelResourceTableEntry.setStatus("current")
_VADCIndex_Type = Integer32
_VADCIndex_Object = MibTableColumn
vADCIndex = _VADCIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 4, 1, 1, 1, 1),
    _VADCIndex_Type()
)
vADCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCIndex.setStatus("current")
_VADCName_Type = DisplayString
_VADCName_Object = MibTableColumn
vADCName = _VADCName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 4, 1, 1, 1, 2),
    _VADCName_Type()
)
vADCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCName.setStatus("current")
_VADCStatsCompLimit_Type = Integer32
_VADCStatsCompLimit_Object = MibTableColumn
vADCStatsCompLimit = _VADCStatsCompLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 4, 1, 1, 1, 3),
    _VADCStatsCompLimit_Type()
)
vADCStatsCompLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCStatsCompLimit.setStatus("current")
_VADCStatsCompUtil_Type = Integer32
_VADCStatsCompUtil_Object = MibTableColumn
vADCStatsCompUtil = _VADCStatsCompUtil_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 4, 1, 1, 1, 4),
    _VADCStatsCompUtil_Type()
)
vADCStatsCompUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCStatsCompUtil.setStatus("current")
_VADCStatsSSLLimit_Type = Integer32
_VADCStatsSSLLimit_Object = MibTableColumn
vADCStatsSSLLimit = _VADCStatsSSLLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 4, 1, 1, 1, 5),
    _VADCStatsSSLLimit_Type()
)
vADCStatsSSLLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCStatsSSLLimit.setStatus("current")
_VADCStatsSSLUtil_Type = Integer32
_VADCStatsSSLUtil_Object = MibTableColumn
vADCStatsSSLUtil = _VADCStatsSSLUtil_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 4, 1, 1, 1, 6),
    _VADCStatsSSLUtil_Type()
)
vADCStatsSSLUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCStatsSSLUtil.setStatus("current")
_VADCMemStatsTable_Object = MibTable
vADCMemStatsTable = _VADCMemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    vADCMemStatsTable.setStatus("current")
_VADCMemStatsTableEntry_Object = MibTableRow
vADCMemStatsTableEntry = _VADCMemStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 4, 1, 2, 1)
)
vADCMemStatsTableEntry.setIndexNames(
    (0, "ADMIN-ALTEON-AC-vADC-MIB", "vADCMemStatsIndex"),
)
if mibBuilder.loadTexts:
    vADCMemStatsTableEntry.setStatus("current")
_VADCMemStatsIndex_Type = Integer32
_VADCMemStatsIndex_Object = MibTableColumn
vADCMemStatsIndex = _VADCMemStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 4, 1, 2, 1, 1),
    _VADCMemStatsIndex_Type()
)
vADCMemStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCMemStatsIndex.setStatus("current")
_VADCMemStatsName_Type = DisplayString
_VADCMemStatsName_Object = MibTableColumn
vADCMemStatsName = _VADCMemStatsName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 4, 1, 2, 1, 2),
    _VADCMemStatsName_Type()
)
vADCMemStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCMemStatsName.setStatus("current")
_VADCMemStatsCurrentMemory_Type = Integer32
_VADCMemStatsCurrentMemory_Object = MibTableColumn
vADCMemStatsCurrentMemory = _VADCMemStatsCurrentMemory_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 4, 1, 2, 1, 3),
    _VADCMemStatsCurrentMemory_Type()
)
vADCMemStatsCurrentMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCMemStatsCurrentMemory.setStatus("current")
_VADCMemStatsHiWaterMark_Type = Integer32
_VADCMemStatsHiWaterMark_Object = MibTableColumn
vADCMemStatsHiWaterMark = _VADCMemStatsHiWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 6, 1, 4, 1, 2, 1, 4),
    _VADCMemStatsHiWaterMark_Type()
)
vADCMemStatsHiWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vADCMemStatsHiWaterMark.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADMIN-ALTEON-AC-vADC-MIB",
    **{"adminvADC": adminvADC,
       "adminvADCConfigs": adminvADCConfigs,
       "vADCConfig": vADCConfig,
       "vADCMaxVADCId": vADCMaxVADCId,
       "vADCMaxCU": vADCMaxCU,
       "vADCCurCfgTable": vADCCurCfgTable,
       "vADCCurCfgTableEntry": vADCCurCfgTableEntry,
       "vADCCurCfgVADCId": vADCCurCfgVADCId,
       "vADCCurCfgVlanId": vADCCurCfgVlanId,
       "vADCCurCfgName": vADCCurCfgName,
       "vADCCurCfgCU": vADCCurCfgCU,
       "vADCCurCfgLimit": vADCCurCfgLimit,
       "vADCCurCfgState": vADCCurCfgState,
       "vADCCurCfgFeatGlobal": vADCCurCfgFeatGlobal,
       "vADCCurCfgFeatBWM": vADCCurCfgFeatBWM,
       "vADCCurCfgFeatITM": vADCCurCfgFeatITM,
       "vADCCurCfgFeatADOS": vADCCurCfgFeatADOS,
       "vADCCurCfgFeatLLB": vADCCurCfgFeatLLB,
       "vADCCurCfgSslLimit": vADCCurCfgSslLimit,
       "vADCCurCfgCompLimit": vADCCurCfgCompLimit,
       "vADCCurResetImageVersion": vADCCurResetImageVersion,
       "vADCCurSyncPeerSwitch": vADCCurSyncPeerSwitch,
       "vADCNewCfgTable": vADCNewCfgTable,
       "vADCNewCfgTableEntry": vADCNewCfgTableEntry,
       "vADCNewCfgVADCId": vADCNewCfgVADCId,
       "vADCNewCfgVlanId": vADCNewCfgVlanId,
       "vADCNewCfgAddVlan": vADCNewCfgAddVlan,
       "vADCNewCfgRemoveVlan": vADCNewCfgRemoveVlan,
       "vADCNewCfgName": vADCNewCfgName,
       "vADCNewCfgCU": vADCNewCfgCU,
       "vADCNewCfgLimit": vADCNewCfgLimit,
       "vADCNewCfgState": vADCNewCfgState,
       "vADCNewCfgDelete": vADCNewCfgDelete,
       "vADCNewCfgFeatGlobal": vADCNewCfgFeatGlobal,
       "vADCNewCfgFeatBWM": vADCNewCfgFeatBWM,
       "vADCNewCfgFeatITM": vADCNewCfgFeatITM,
       "vADCNewCfgFeatADOS": vADCNewCfgFeatADOS,
       "vADCNewCfgFeatLLB": vADCNewCfgFeatLLB,
       "vADCNewCfgSslLimit": vADCNewCfgSslLimit,
       "vADCNewCfgCompLimit": vADCNewCfgCompLimit,
       "vADCNewResetImageVersion": vADCNewResetImageVersion,
       "vADCNewSyncPeerSwitch": vADCNewSyncPeerSwitch,
       "vADCCurCfgSysTable": vADCCurCfgSysTable,
       "vADCCurCfgSysTableEntry": vADCCurCfgSysTableEntry,
       "vADCCurCfgSysMmgmtAddr": vADCCurCfgSysMmgmtAddr,
       "vADCCurCfgSysMmgmtMask": vADCCurCfgSysMmgmtMask,
       "vADCCurCfgSysMmgmtGw": vADCCurCfgSysMmgmtGw,
       "vADCCurCfgSysMmgmtState": vADCCurCfgSysMmgmtState,
       "vADCCurCfgSysPeerAddr": vADCCurCfgSysPeerAddr,
       "vADCCurCfgSysPeerMask": vADCCurCfgSysPeerMask,
       "vADCCurCfgSysPeerGw": vADCCurCfgSysPeerGw,
       "vADCCurCfgSysHttpsState": vADCCurCfgSysHttpsState,
       "vADCCurCfgSysSshState": vADCCurCfgSysSshState,
       "vADCCurCfgSysHttpState": vADCCurCfgSysHttpState,
       "vADCCurCfgSysSnmpState": vADCCurCfgSysSnmpState,
       "vADCCurCfgSysSyslogState": vADCCurCfgSysSyslogState,
       "vADCCurCfgSysRadiusState": vADCCurCfgSysRadiusState,
       "vADCCurCfgSysTacacsState": vADCCurCfgSysTacacsState,
       "vADCCurCfgSysIdleState": vADCCurCfgSysIdleState,
       "vADCCurCfgSysSmtpState": vADCCurCfgSysSmtpState,
       "vADCCurCfgSyslogDelegation": vADCCurCfgSyslogDelegation,
       "vADCCurCfgRadiusDelegation": vADCCurCfgRadiusDelegation,
       "vADCCurCfgTacacsDelegation": vADCCurCfgTacacsDelegation,
       "vADCCurCfgSmtpDelegation": vADCCurCfgSmtpDelegation,
       "vADCCurCfgSysMmgmtIpv6Addr": vADCCurCfgSysMmgmtIpv6Addr,
       "vADCCurCfgSysMmgmtIpv6PrefixLen": vADCCurCfgSysMmgmtIpv6PrefixLen,
       "vADCCurCfgSysMmgmtIpv6Gateway": vADCCurCfgSysMmgmtIpv6Gateway,
       "vADCCurCfgSysPeerIpv6Addr": vADCCurCfgSysPeerIpv6Addr,
       "vADCCurCfgSysPeerIpv6PrefixLen": vADCCurCfgSysPeerIpv6PrefixLen,
       "vADCCurCfgSysPeerIpv6Gateway": vADCCurCfgSysPeerIpv6Gateway,
       "vADCCurCfgSysTnetState": vADCCurCfgSysTnetState,
       "vADCCurCfgSysHaId": vADCCurCfgSysHaId,
       "vADCCurCfgSysPeerId": vADCCurCfgSysPeerId,
       "vADCCurCfgSysVADCId": vADCCurCfgSysVADCId,
       "vADCCurCfgIdleDelegation": vADCCurCfgIdleDelegation,
       "vADCCurCfgSysMmgmtDelegation": vADCCurCfgSysMmgmtDelegation,
       "vADCCurCfgSysPeerName": vADCCurCfgSysPeerName,
       "vADCNewCfgSysTable": vADCNewCfgSysTable,
       "vADCNewCfgSysTableEntry": vADCNewCfgSysTableEntry,
       "vADCNewCfgSysMmgmtAddr": vADCNewCfgSysMmgmtAddr,
       "vADCNewCfgSysMmgmtMask": vADCNewCfgSysMmgmtMask,
       "vADCNewCfgSysMmgmtGw": vADCNewCfgSysMmgmtGw,
       "vADCNewCfgSysMmgmtState": vADCNewCfgSysMmgmtState,
       "vADCNewCfgSysPeerAddr": vADCNewCfgSysPeerAddr,
       "vADCNewCfgSysPeerMask": vADCNewCfgSysPeerMask,
       "vADCNewCfgSysPeerGw": vADCNewCfgSysPeerGw,
       "vADCNewCfgSysHttpsState": vADCNewCfgSysHttpsState,
       "vADCNewCfgSysSshState": vADCNewCfgSysSshState,
       "vADCNewCfgSysHttpState": vADCNewCfgSysHttpState,
       "vADCNewCfgSysSnmpState": vADCNewCfgSysSnmpState,
       "vADCNewCfgSysSyslogState": vADCNewCfgSysSyslogState,
       "vADCNewCfgSysRadiusState": vADCNewCfgSysRadiusState,
       "vADCNewCfgSysTacacsState": vADCNewCfgSysTacacsState,
       "vADCNewCfgSysIdleState": vADCNewCfgSysIdleState,
       "vADCNewCfgSysSmtpState": vADCNewCfgSysSmtpState,
       "vADCNewCfgSyslogDelegation": vADCNewCfgSyslogDelegation,
       "vADCNewCfgRadiusDelegation": vADCNewCfgRadiusDelegation,
       "vADCNewCfgTacacsDelegation": vADCNewCfgTacacsDelegation,
       "vADCNewCfgSmtpDelegation": vADCNewCfgSmtpDelegation,
       "vADCNewCfgSysMmgmtIpv6Addr": vADCNewCfgSysMmgmtIpv6Addr,
       "vADCNewCfgSysMmgmtIpv6PrefixLen": vADCNewCfgSysMmgmtIpv6PrefixLen,
       "vADCNewCfgSysMmgmtIpv6Gateway": vADCNewCfgSysMmgmtIpv6Gateway,
       "vADCNewCfgSysPeerIpv6Addr": vADCNewCfgSysPeerIpv6Addr,
       "vADCNewCfgSysPeerIpv6PrefixLen": vADCNewCfgSysPeerIpv6PrefixLen,
       "vADCNewCfgSysPeerIpv6Gateway": vADCNewCfgSysPeerIpv6Gateway,
       "vADCNewCfgSysTnetState": vADCNewCfgSysTnetState,
       "vADCNewCfgSysHaId": vADCNewCfgSysHaId,
       "vADCNewCfgSysPeerId": vADCNewCfgSysPeerId,
       "vADCNewCfgSysVADCId": vADCNewCfgSysVADCId,
       "vADCNewCfgIdleDelegation": vADCNewCfgIdleDelegation,
       "vADCNewCfgSysMmgmtDelegation": vADCNewCfgSysMmgmtDelegation,
       "vADCNewCfgSysPeerName": vADCNewCfgSysPeerName,
       "vADCCurCfgNetTable": vADCCurCfgNetTable,
       "vADCCurCfgNetTableEntry": vADCCurCfgNetTableEntry,
       "vADCCurCfgNetId": vADCCurCfgNetId,
       "vADCCurCfgNetVlanId": vADCCurCfgNetVlanId,
       "vADCCurCfgNetIPver": vADCCurCfgNetIPver,
       "vADCCurCfgNetIPBegin": vADCCurCfgNetIPBegin,
       "vADCCurCfgNetMask": vADCCurCfgNetMask,
       "vADCCurCfgNetIPEnd": vADCCurCfgNetIPEnd,
       "vADCCurCfgNetIPv6Begin": vADCCurCfgNetIPv6Begin,
       "vADCCurCfgNetPrefix": vADCCurCfgNetPrefix,
       "vADCCurCfgNetIPv6End": vADCCurCfgNetIPv6End,
       "vADCCurCfgNetVADCId": vADCCurCfgNetVADCId,
       "vADCNewCfgNetTable": vADCNewCfgNetTable,
       "vADCNewCfgNetTableEntry": vADCNewCfgNetTableEntry,
       "vADCNewCfgNetId": vADCNewCfgNetId,
       "vADCNewCfgNetVlanId": vADCNewCfgNetVlanId,
       "vADCNewCfgNetIPver": vADCNewCfgNetIPver,
       "vADCNewCfgNetIPBegin": vADCNewCfgNetIPBegin,
       "vADCNewCfgNetMask": vADCNewCfgNetMask,
       "vADCNewCfgNetIPEnd": vADCNewCfgNetIPEnd,
       "vADCNewCfgNetRemId": vADCNewCfgNetRemId,
       "vADCNewCfgNetIPv6Begin": vADCNewCfgNetIPv6Begin,
       "vADCNewCfgNetPrefix": vADCNewCfgNetPrefix,
       "vADCNewCfgNetIPv6End": vADCNewCfgNetIPv6End,
       "vADCNewCfgNetVADCId": vADCNewCfgNetVADCId,
       "vADCAccessUser": vADCAccessUser,
       "vADCAccessUid": vADCAccessUid,
       "vADCUserCurCfgTable": vADCUserCurCfgTable,
       "vADCUserCurCfgTableEntry": vADCUserCurCfgTableEntry,
       "vADCUserCurCfgVADCId": vADCUserCurCfgVADCId,
       "vADCUserCurCfgUId": vADCUserCurCfgUId,
       "vADCUserCurCos": vADCUserCurCos,
       "vADCUserCurCfgName": vADCUserCurCfgName,
       "vADCUserCurCfgAdminPswd": vADCUserCurCfgAdminPswd,
       "vADCUserCurCfgPswd": vADCUserCurCfgPswd,
       "vADCUserCurCfgConfPswd": vADCUserCurCfgConfPswd,
       "vADCUserCurCfgBackdoor": vADCUserCurCfgBackdoor,
       "vADCUserCurCfgCrtMng": vADCUserCurCfgCrtMng,
       "vADCUserCurCfgState": vADCUserCurCfgState,
       "vADCUserNewCfgTable": vADCUserNewCfgTable,
       "vADCUserNewCfgTableEntry": vADCUserNewCfgTableEntry,
       "vADCUserNewCfgVADCId": vADCUserNewCfgVADCId,
       "vADCUserNewCfgUId": vADCUserNewCfgUId,
       "vADCUserNewCos": vADCUserNewCos,
       "vADCUserNewCfgName": vADCUserNewCfgName,
       "vADCUserNewCfgAdminPswd": vADCUserNewCfgAdminPswd,
       "vADCUserNewCfgPswd": vADCUserNewCfgPswd,
       "vADCUserNewCfgConfPswd": vADCUserNewCfgConfPswd,
       "vADCUserNewCfgBackdoor": vADCUserNewCfgBackdoor,
       "vADCUserNewCfgCrtMng": vADCUserNewCfgCrtMng,
       "vADCUserNewCfgState": vADCUserNewCfgState,
       "vADCUserNewCfgDelete": vADCUserNewCfgDelete,
       "vADCUsersPswdTable": vADCUsersPswdTable,
       "vADCUsersPswdTableEntry": vADCUsersPswdTableEntry,
       "vADCUsersVADCId": vADCUsersVADCId,
       "vADCAccessUsrPasswd": vADCAccessUsrPasswd,
       "vADCAccessSlbOperPasswd": vADCAccessSlbOperPasswd,
       "vADCAccessL4OperPasswd": vADCAccessL4OperPasswd,
       "vADCAccessOperPasswd": vADCAccessOperPasswd,
       "vADCAccessSlbAdminPasswd": vADCAccessSlbAdminPasswd,
       "vADCAccessL4AdminPasswd": vADCAccessL4AdminPasswd,
       "vADCAccessAdminPasswd": vADCAccessAdminPasswd,
       "vADCAccessAdminNewPasswd": vADCAccessAdminNewPasswd,
       "vADCAccessAdminConfNewPasswd": vADCAccessAdminConfNewPasswd,
       "adminvADCInfo": adminvADCInfo,
       "vADCInfo": vADCInfo,
       "vADCInfoAvailableCU": vADCInfoAvailableCU,
       "vADCInfoAvailableThruput": vADCInfoAvailableThruput,
       "vADCInfoTable": vADCInfoTable,
       "vADCInfoTableEntry": vADCInfoTableEntry,
       "vADCInfoId": vADCInfoId,
       "vADCInfoName": vADCInfoName,
       "vADCInfoStatus": vADCInfoStatus,
       "vADCInfoVRRPStatus": vADCInfoVRRPStatus,
       "vADCInfoCU": vADCInfoCU,
       "vADCInfoThroughput": vADCInfoThroughput,
       "vADCInfoLimit": vADCInfoLimit,
       "vADCInfoSPcpu": vADCInfoSPcpu,
       "vADCInfoMPcpu": vADCInfoMPcpu,
       "vADCInfoCUMbit": vADCInfoCUMbit,
       "vADCInfoUpTime": vADCInfoUpTime,
       "vADCInfoConfigChangeTime": vADCInfoConfigChangeTime,
       "adminvADCBoot": adminvADCBoot,
       "vADCBoot": vADCBoot,
       "vADCBootTable": vADCBootTable,
       "vADCBootTableEntry": vADCBootTableEntry,
       "vADCBootVADCId": vADCBootVADCId,
       "vADCBootAction": vADCBootAction,
       "adminvADCStats": adminvADCStats,
       "vADCStat": vADCStat,
       "vADCStatsAccelResourceTable": vADCStatsAccelResourceTable,
       "vADCStatsAccelResourceTableEntry": vADCStatsAccelResourceTableEntry,
       "vADCIndex": vADCIndex,
       "vADCName": vADCName,
       "vADCStatsCompLimit": vADCStatsCompLimit,
       "vADCStatsCompUtil": vADCStatsCompUtil,
       "vADCStatsSSLLimit": vADCStatsSSLLimit,
       "vADCStatsSSLUtil": vADCStatsSSLUtil,
       "vADCMemStatsTable": vADCMemStatsTable,
       "vADCMemStatsTableEntry": vADCMemStatsTableEntry,
       "vADCMemStatsIndex": vADCMemStatsIndex,
       "vADCMemStatsName": vADCMemStatsName,
       "vADCMemStatsCurrentMemory": vADCMemStatsCurrentMemory,
       "vADCMemStatsHiWaterMark": vADCMemStatsHiWaterMark}
)

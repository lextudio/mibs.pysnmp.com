# SNMP MIB module (BLADETYPE2-NETWORK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLADETYPE2-NETWORK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:02 2024
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

layer3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Layer3Configs_ObjectIdentity = ObjectIdentity
layer3Configs = _Layer3Configs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1)
)
_IpInterfaceCfg_ObjectIdentity = ObjectIdentity
ipInterfaceCfg = _IpInterfaceCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1)
)
_IpInterfaceTableMax_Type = Integer32
_IpInterfaceTableMax_Object = MibScalar
ipInterfaceTableMax = _IpInterfaceTableMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 1),
    _IpInterfaceTableMax_Type()
)
ipInterfaceTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceTableMax.setStatus("current")
_IpCurCfgIntfTable_Object = MibTable
ipCurCfgIntfTable = _IpCurCfgIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipCurCfgIntfTable.setStatus("current")
_IpCurCfgIntfEntry_Object = MibTableRow
ipCurCfgIntfEntry = _IpCurCfgIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 2, 1)
)
ipCurCfgIntfEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipCurCfgIntfIndex"),
)
if mibBuilder.loadTexts:
    ipCurCfgIntfEntry.setStatus("current")
_IpCurCfgIntfIndex_Type = Integer32
_IpCurCfgIntfIndex_Object = MibTableColumn
ipCurCfgIntfIndex = _IpCurCfgIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 2, 1, 1),
    _IpCurCfgIntfIndex_Type()
)
ipCurCfgIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfIndex.setStatus("current")
_IpCurCfgIntfAddr_Type = IpAddress
_IpCurCfgIntfAddr_Object = MibTableColumn
ipCurCfgIntfAddr = _IpCurCfgIntfAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 2, 1, 2),
    _IpCurCfgIntfAddr_Type()
)
ipCurCfgIntfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfAddr.setStatus("current")
_IpCurCfgIntfMask_Type = IpAddress
_IpCurCfgIntfMask_Object = MibTableColumn
ipCurCfgIntfMask = _IpCurCfgIntfMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 2, 1, 3),
    _IpCurCfgIntfMask_Type()
)
ipCurCfgIntfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfMask.setStatus("current")
_IpCurCfgIntfBroadcast_Type = IpAddress
_IpCurCfgIntfBroadcast_Object = MibTableColumn
ipCurCfgIntfBroadcast = _IpCurCfgIntfBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 2, 1, 4),
    _IpCurCfgIntfBroadcast_Type()
)
ipCurCfgIntfBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfBroadcast.setStatus("current")


class _IpCurCfgIntfVlan_Type(Integer32):
    """Custom type ipCurCfgIntfVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_IpCurCfgIntfVlan_Type.__name__ = "Integer32"
_IpCurCfgIntfVlan_Object = MibTableColumn
ipCurCfgIntfVlan = _IpCurCfgIntfVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 2, 1, 5),
    _IpCurCfgIntfVlan_Type()
)
ipCurCfgIntfVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfVlan.setStatus("current")


class _IpCurCfgIntfState_Type(Integer32):
    """Custom type ipCurCfgIntfState based on Integer32"""
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


_IpCurCfgIntfState_Type.__name__ = "Integer32"
_IpCurCfgIntfState_Object = MibTableColumn
ipCurCfgIntfState = _IpCurCfgIntfState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 2, 1, 6),
    _IpCurCfgIntfState_Type()
)
ipCurCfgIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfState.setStatus("current")


class _IpCurCfgIntfBootpRelay_Type(Integer32):
    """Custom type ipCurCfgIntfBootpRelay based on Integer32"""
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


_IpCurCfgIntfBootpRelay_Type.__name__ = "Integer32"
_IpCurCfgIntfBootpRelay_Object = MibTableColumn
ipCurCfgIntfBootpRelay = _IpCurCfgIntfBootpRelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 2, 1, 7),
    _IpCurCfgIntfBootpRelay_Type()
)
ipCurCfgIntfBootpRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfBootpRelay.setStatus("current")
_IpNewCfgIntfTable_Object = MibTable
ipNewCfgIntfTable = _IpNewCfgIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ipNewCfgIntfTable.setStatus("current")
_IpNewCfgIntfEntry_Object = MibTableRow
ipNewCfgIntfEntry = _IpNewCfgIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 3, 1)
)
ipNewCfgIntfEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipNewCfgIntfIndex"),
)
if mibBuilder.loadTexts:
    ipNewCfgIntfEntry.setStatus("current")
_IpNewCfgIntfIndex_Type = Integer32
_IpNewCfgIntfIndex_Object = MibTableColumn
ipNewCfgIntfIndex = _IpNewCfgIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 3, 1, 1),
    _IpNewCfgIntfIndex_Type()
)
ipNewCfgIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgIntfIndex.setStatus("current")
_IpNewCfgIntfAddr_Type = IpAddress
_IpNewCfgIntfAddr_Object = MibTableColumn
ipNewCfgIntfAddr = _IpNewCfgIntfAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 3, 1, 2),
    _IpNewCfgIntfAddr_Type()
)
ipNewCfgIntfAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgIntfAddr.setStatus("current")
_IpNewCfgIntfMask_Type = IpAddress
_IpNewCfgIntfMask_Object = MibTableColumn
ipNewCfgIntfMask = _IpNewCfgIntfMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 3, 1, 3),
    _IpNewCfgIntfMask_Type()
)
ipNewCfgIntfMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgIntfMask.setStatus("current")
_IpNewCfgIntfBroadcast_Type = IpAddress
_IpNewCfgIntfBroadcast_Object = MibTableColumn
ipNewCfgIntfBroadcast = _IpNewCfgIntfBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 3, 1, 4),
    _IpNewCfgIntfBroadcast_Type()
)
ipNewCfgIntfBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgIntfBroadcast.setStatus("current")


class _IpNewCfgIntfVlan_Type(Integer32):
    """Custom type ipNewCfgIntfVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_IpNewCfgIntfVlan_Type.__name__ = "Integer32"
_IpNewCfgIntfVlan_Object = MibTableColumn
ipNewCfgIntfVlan = _IpNewCfgIntfVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 3, 1, 5),
    _IpNewCfgIntfVlan_Type()
)
ipNewCfgIntfVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgIntfVlan.setStatus("current")


class _IpNewCfgIntfState_Type(Integer32):
    """Custom type ipNewCfgIntfState based on Integer32"""
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


_IpNewCfgIntfState_Type.__name__ = "Integer32"
_IpNewCfgIntfState_Object = MibTableColumn
ipNewCfgIntfState = _IpNewCfgIntfState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 3, 1, 6),
    _IpNewCfgIntfState_Type()
)
ipNewCfgIntfState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgIntfState.setStatus("current")


class _IpNewCfgIntfDelete_Type(Integer32):
    """Custom type ipNewCfgIntfDelete based on Integer32"""
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


_IpNewCfgIntfDelete_Type.__name__ = "Integer32"
_IpNewCfgIntfDelete_Object = MibTableColumn
ipNewCfgIntfDelete = _IpNewCfgIntfDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 3, 1, 7),
    _IpNewCfgIntfDelete_Type()
)
ipNewCfgIntfDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgIntfDelete.setStatus("current")


class _IpNewCfgIntfBootpRelay_Type(Integer32):
    """Custom type ipNewCfgIntfBootpRelay based on Integer32"""
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


_IpNewCfgIntfBootpRelay_Type.__name__ = "Integer32"
_IpNewCfgIntfBootpRelay_Object = MibTableColumn
ipNewCfgIntfBootpRelay = _IpNewCfgIntfBootpRelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 1, 3, 1, 8),
    _IpNewCfgIntfBootpRelay_Type()
)
ipNewCfgIntfBootpRelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgIntfBootpRelay.setStatus("current")
_IpGatewayCfg_ObjectIdentity = ObjectIdentity
ipGatewayCfg = _IpGatewayCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2)
)
_IpGatewayTableMax_Type = Integer32
_IpGatewayTableMax_Object = MibScalar
ipGatewayTableMax = _IpGatewayTableMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2, 3),
    _IpGatewayTableMax_Type()
)
ipGatewayTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGatewayTableMax.setStatus("current")
_IpCurCfgGwTable_Object = MibTable
ipCurCfgGwTable = _IpCurCfgGwTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ipCurCfgGwTable.setStatus("current")
_IpCurCfgGwEntry_Object = MibTableRow
ipCurCfgGwEntry = _IpCurCfgGwEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2, 4, 1)
)
ipCurCfgGwEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipCurCfgGwIndex"),
)
if mibBuilder.loadTexts:
    ipCurCfgGwEntry.setStatus("current")
_IpCurCfgGwIndex_Type = Integer32
_IpCurCfgGwIndex_Object = MibTableColumn
ipCurCfgGwIndex = _IpCurCfgGwIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2, 4, 1, 1),
    _IpCurCfgGwIndex_Type()
)
ipCurCfgGwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwIndex.setStatus("current")
_IpCurCfgGwAddr_Type = IpAddress
_IpCurCfgGwAddr_Object = MibTableColumn
ipCurCfgGwAddr = _IpCurCfgGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2, 4, 1, 2),
    _IpCurCfgGwAddr_Type()
)
ipCurCfgGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwAddr.setStatus("current")


class _IpCurCfgGwInterval_Type(Integer32):
    """Custom type ipCurCfgGwInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_IpCurCfgGwInterval_Type.__name__ = "Integer32"
_IpCurCfgGwInterval_Object = MibTableColumn
ipCurCfgGwInterval = _IpCurCfgGwInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2, 4, 1, 3),
    _IpCurCfgGwInterval_Type()
)
ipCurCfgGwInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwInterval.setStatus("current")


class _IpCurCfgGwRetry_Type(Integer32):
    """Custom type ipCurCfgGwRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_IpCurCfgGwRetry_Type.__name__ = "Integer32"
_IpCurCfgGwRetry_Object = MibTableColumn
ipCurCfgGwRetry = _IpCurCfgGwRetry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2, 4, 1, 4),
    _IpCurCfgGwRetry_Type()
)
ipCurCfgGwRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwRetry.setStatus("current")


class _IpCurCfgGwState_Type(Integer32):
    """Custom type ipCurCfgGwState based on Integer32"""
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


_IpCurCfgGwState_Type.__name__ = "Integer32"
_IpCurCfgGwState_Object = MibTableColumn
ipCurCfgGwState = _IpCurCfgGwState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2, 4, 1, 5),
    _IpCurCfgGwState_Type()
)
ipCurCfgGwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwState.setStatus("current")


class _IpCurCfgGwArp_Type(Integer32):
    """Custom type ipCurCfgGwArp based on Integer32"""
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


_IpCurCfgGwArp_Type.__name__ = "Integer32"
_IpCurCfgGwArp_Object = MibTableColumn
ipCurCfgGwArp = _IpCurCfgGwArp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2, 4, 1, 6),
    _IpCurCfgGwArp_Type()
)
ipCurCfgGwArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwArp.setStatus("current")
_IpNewCfgGwTable_Object = MibTable
ipNewCfgGwTable = _IpNewCfgGwTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ipNewCfgGwTable.setStatus("current")
_IpNewCfgGwEntry_Object = MibTableRow
ipNewCfgGwEntry = _IpNewCfgGwEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2, 5, 1)
)
ipNewCfgGwEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipNewCfgGwIndex"),
)
if mibBuilder.loadTexts:
    ipNewCfgGwEntry.setStatus("current")
_IpNewCfgGwIndex_Type = Integer32
_IpNewCfgGwIndex_Object = MibTableColumn
ipNewCfgGwIndex = _IpNewCfgGwIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2, 5, 1, 1),
    _IpNewCfgGwIndex_Type()
)
ipNewCfgGwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgGwIndex.setStatus("current")
_IpNewCfgGwAddr_Type = IpAddress
_IpNewCfgGwAddr_Object = MibTableColumn
ipNewCfgGwAddr = _IpNewCfgGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2, 5, 1, 2),
    _IpNewCfgGwAddr_Type()
)
ipNewCfgGwAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgGwAddr.setStatus("current")


class _IpNewCfgGwInterval_Type(Integer32):
    """Custom type ipNewCfgGwInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_IpNewCfgGwInterval_Type.__name__ = "Integer32"
_IpNewCfgGwInterval_Object = MibTableColumn
ipNewCfgGwInterval = _IpNewCfgGwInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2, 5, 1, 3),
    _IpNewCfgGwInterval_Type()
)
ipNewCfgGwInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgGwInterval.setStatus("current")


class _IpNewCfgGwRetry_Type(Integer32):
    """Custom type ipNewCfgGwRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_IpNewCfgGwRetry_Type.__name__ = "Integer32"
_IpNewCfgGwRetry_Object = MibTableColumn
ipNewCfgGwRetry = _IpNewCfgGwRetry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2, 5, 1, 4),
    _IpNewCfgGwRetry_Type()
)
ipNewCfgGwRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgGwRetry.setStatus("current")


class _IpNewCfgGwState_Type(Integer32):
    """Custom type ipNewCfgGwState based on Integer32"""
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


_IpNewCfgGwState_Type.__name__ = "Integer32"
_IpNewCfgGwState_Object = MibTableColumn
ipNewCfgGwState = _IpNewCfgGwState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2, 5, 1, 5),
    _IpNewCfgGwState_Type()
)
ipNewCfgGwState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgGwState.setStatus("current")


class _IpNewCfgGwDelete_Type(Integer32):
    """Custom type ipNewCfgGwDelete based on Integer32"""
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


_IpNewCfgGwDelete_Type.__name__ = "Integer32"
_IpNewCfgGwDelete_Object = MibTableColumn
ipNewCfgGwDelete = _IpNewCfgGwDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2, 5, 1, 6),
    _IpNewCfgGwDelete_Type()
)
ipNewCfgGwDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgGwDelete.setStatus("current")


class _IpNewCfgGwArp_Type(Integer32):
    """Custom type ipNewCfgGwArp based on Integer32"""
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


_IpNewCfgGwArp_Type.__name__ = "Integer32"
_IpNewCfgGwArp_Object = MibTableColumn
ipNewCfgGwArp = _IpNewCfgGwArp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 2, 5, 1, 7),
    _IpNewCfgGwArp_Type()
)
ipNewCfgGwArp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgGwArp.setStatus("current")
_IpStaticRouteCfg_ObjectIdentity = ObjectIdentity
ipStaticRouteCfg = _IpStaticRouteCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 3)
)
_IpStaticRouteTableMaxSize_Type = Integer32
_IpStaticRouteTableMaxSize_Object = MibScalar
ipStaticRouteTableMaxSize = _IpStaticRouteTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 3, 1),
    _IpStaticRouteTableMaxSize_Type()
)
ipStaticRouteTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStaticRouteTableMaxSize.setStatus("current")
_IpCurCfgStaticRouteTable_Object = MibTable
ipCurCfgStaticRouteTable = _IpCurCfgStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteTable.setStatus("current")
_IpCurCfgStaticRouteEntry_Object = MibTableRow
ipCurCfgStaticRouteEntry = _IpCurCfgStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 3, 2, 1)
)
ipCurCfgStaticRouteEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipCurCfgStaticRouteIndx"),
)
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteEntry.setStatus("current")
_IpCurCfgStaticRouteIndx_Type = Integer32
_IpCurCfgStaticRouteIndx_Object = MibTableColumn
ipCurCfgStaticRouteIndx = _IpCurCfgStaticRouteIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 3, 2, 1, 1),
    _IpCurCfgStaticRouteIndx_Type()
)
ipCurCfgStaticRouteIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteIndx.setStatus("current")
_IpCurCfgStaticRouteDestIp_Type = IpAddress
_IpCurCfgStaticRouteDestIp_Object = MibTableColumn
ipCurCfgStaticRouteDestIp = _IpCurCfgStaticRouteDestIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 3, 2, 1, 2),
    _IpCurCfgStaticRouteDestIp_Type()
)
ipCurCfgStaticRouteDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteDestIp.setStatus("current")
_IpCurCfgStaticRouteMask_Type = IpAddress
_IpCurCfgStaticRouteMask_Object = MibTableColumn
ipCurCfgStaticRouteMask = _IpCurCfgStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 3, 2, 1, 3),
    _IpCurCfgStaticRouteMask_Type()
)
ipCurCfgStaticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteMask.setStatus("current")
_IpCurCfgStaticRouteGateway_Type = IpAddress
_IpCurCfgStaticRouteGateway_Object = MibTableColumn
ipCurCfgStaticRouteGateway = _IpCurCfgStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 3, 2, 1, 4),
    _IpCurCfgStaticRouteGateway_Type()
)
ipCurCfgStaticRouteGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteGateway.setStatus("current")
_IpCurCfgStaticRouteInterface_Type = Integer32
_IpCurCfgStaticRouteInterface_Object = MibTableColumn
ipCurCfgStaticRouteInterface = _IpCurCfgStaticRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 3, 2, 1, 5),
    _IpCurCfgStaticRouteInterface_Type()
)
ipCurCfgStaticRouteInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteInterface.setStatus("current")
_IpNewCfgStaticRouteTable_Object = MibTable
ipNewCfgStaticRouteTable = _IpNewCfgStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteTable.setStatus("current")
_IpNewCfgStaticRouteEntry_Object = MibTableRow
ipNewCfgStaticRouteEntry = _IpNewCfgStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 3, 3, 1)
)
ipNewCfgStaticRouteEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipNewCfgStaticRouteIndx"),
)
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteEntry.setStatus("current")
_IpNewCfgStaticRouteIndx_Type = Integer32
_IpNewCfgStaticRouteIndx_Object = MibTableColumn
ipNewCfgStaticRouteIndx = _IpNewCfgStaticRouteIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 3, 3, 1, 1),
    _IpNewCfgStaticRouteIndx_Type()
)
ipNewCfgStaticRouteIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteIndx.setStatus("current")
_IpNewCfgStaticRouteDestIp_Type = IpAddress
_IpNewCfgStaticRouteDestIp_Object = MibTableColumn
ipNewCfgStaticRouteDestIp = _IpNewCfgStaticRouteDestIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 3, 3, 1, 2),
    _IpNewCfgStaticRouteDestIp_Type()
)
ipNewCfgStaticRouteDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteDestIp.setStatus("current")
_IpNewCfgStaticRouteMask_Type = IpAddress
_IpNewCfgStaticRouteMask_Object = MibTableColumn
ipNewCfgStaticRouteMask = _IpNewCfgStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 3, 3, 1, 3),
    _IpNewCfgStaticRouteMask_Type()
)
ipNewCfgStaticRouteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteMask.setStatus("current")
_IpNewCfgStaticRouteGateway_Type = IpAddress
_IpNewCfgStaticRouteGateway_Object = MibTableColumn
ipNewCfgStaticRouteGateway = _IpNewCfgStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 3, 3, 1, 4),
    _IpNewCfgStaticRouteGateway_Type()
)
ipNewCfgStaticRouteGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteGateway.setStatus("current")


class _IpNewCfgStaticRouteAction_Type(Integer32):
    """Custom type ipNewCfgStaticRouteAction based on Integer32"""
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


_IpNewCfgStaticRouteAction_Type.__name__ = "Integer32"
_IpNewCfgStaticRouteAction_Object = MibTableColumn
ipNewCfgStaticRouteAction = _IpNewCfgStaticRouteAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 3, 3, 1, 5),
    _IpNewCfgStaticRouteAction_Type()
)
ipNewCfgStaticRouteAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteAction.setStatus("current")
_IpNewCfgStaticRouteInterface_Type = Integer32
_IpNewCfgStaticRouteInterface_Object = MibTableColumn
ipNewCfgStaticRouteInterface = _IpNewCfgStaticRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 3, 3, 1, 6),
    _IpNewCfgStaticRouteInterface_Type()
)
ipNewCfgStaticRouteInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteInterface.setStatus("current")
_IpForwardCfg_ObjectIdentity = ObjectIdentity
ipForwardCfg = _IpForwardCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 4)
)
_IpFwdGeneralCfg_ObjectIdentity = ObjectIdentity
ipFwdGeneralCfg = _IpFwdGeneralCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 4, 1)
)


class _IpFwdCurCfgState_Type(Integer32):
    """Custom type ipFwdCurCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_IpFwdCurCfgState_Type.__name__ = "Integer32"
_IpFwdCurCfgState_Object = MibScalar
ipFwdCurCfgState = _IpFwdCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 4, 1, 1),
    _IpFwdCurCfgState_Type()
)
ipFwdCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgState.setStatus("current")


class _IpFwdNewCfgState_Type(Integer32):
    """Custom type ipFwdNewCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_IpFwdNewCfgState_Type.__name__ = "Integer32"
_IpFwdNewCfgState_Object = MibScalar
ipFwdNewCfgState = _IpFwdNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 4, 1, 2),
    _IpFwdNewCfgState_Type()
)
ipFwdNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFwdNewCfgState.setStatus("current")


class _IpFwdCurCfgDirectedBcast_Type(Integer32):
    """Custom type ipFwdCurCfgDirectedBcast based on Integer32"""
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


_IpFwdCurCfgDirectedBcast_Type.__name__ = "Integer32"
_IpFwdCurCfgDirectedBcast_Object = MibScalar
ipFwdCurCfgDirectedBcast = _IpFwdCurCfgDirectedBcast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 4, 1, 3),
    _IpFwdCurCfgDirectedBcast_Type()
)
ipFwdCurCfgDirectedBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgDirectedBcast.setStatus("current")


class _IpFwdNewCfgDirectedBcast_Type(Integer32):
    """Custom type ipFwdNewCfgDirectedBcast based on Integer32"""
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


_IpFwdNewCfgDirectedBcast_Type.__name__ = "Integer32"
_IpFwdNewCfgDirectedBcast_Object = MibScalar
ipFwdNewCfgDirectedBcast = _IpFwdNewCfgDirectedBcast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 4, 1, 4),
    _IpFwdNewCfgDirectedBcast_Type()
)
ipFwdNewCfgDirectedBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFwdNewCfgDirectedBcast.setStatus("current")
_RipCfg_ObjectIdentity = ObjectIdentity
ripCfg = _RipCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 5)
)


class _RipCurCfgSupply_Type(Integer32):
    """Custom type ripCurCfgSupply based on Integer32"""
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


_RipCurCfgSupply_Type.__name__ = "Integer32"
_RipCurCfgSupply_Object = MibScalar
ripCurCfgSupply = _RipCurCfgSupply_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 5, 1),
    _RipCurCfgSupply_Type()
)
ripCurCfgSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgSupply.setStatus("current")


class _RipNewCfgSupply_Type(Integer32):
    """Custom type ripNewCfgSupply based on Integer32"""
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


_RipNewCfgSupply_Type.__name__ = "Integer32"
_RipNewCfgSupply_Object = MibScalar
ripNewCfgSupply = _RipNewCfgSupply_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 5, 2),
    _RipNewCfgSupply_Type()
)
ripNewCfgSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgSupply.setStatus("current")


class _RipCurCfgListen_Type(Integer32):
    """Custom type ripCurCfgListen based on Integer32"""
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


_RipCurCfgListen_Type.__name__ = "Integer32"
_RipCurCfgListen_Object = MibScalar
ripCurCfgListen = _RipCurCfgListen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 5, 3),
    _RipCurCfgListen_Type()
)
ripCurCfgListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgListen.setStatus("current")


class _RipNewCfgListen_Type(Integer32):
    """Custom type ripNewCfgListen based on Integer32"""
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


_RipNewCfgListen_Type.__name__ = "Integer32"
_RipNewCfgListen_Object = MibScalar
ripNewCfgListen = _RipNewCfgListen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 5, 4),
    _RipNewCfgListen_Type()
)
ripNewCfgListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgListen.setStatus("current")


class _RipCurCfgDefListen_Type(Integer32):
    """Custom type ripCurCfgDefListen based on Integer32"""
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


_RipCurCfgDefListen_Type.__name__ = "Integer32"
_RipCurCfgDefListen_Object = MibScalar
ripCurCfgDefListen = _RipCurCfgDefListen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 5, 5),
    _RipCurCfgDefListen_Type()
)
ripCurCfgDefListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgDefListen.setStatus("current")


class _RipNewCfgDefListen_Type(Integer32):
    """Custom type ripNewCfgDefListen based on Integer32"""
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


_RipNewCfgDefListen_Type.__name__ = "Integer32"
_RipNewCfgDefListen_Object = MibScalar
ripNewCfgDefListen = _RipNewCfgDefListen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 5, 6),
    _RipNewCfgDefListen_Type()
)
ripNewCfgDefListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgDefListen.setStatus("current")


class _RipCurCfgStaticSupply_Type(Integer32):
    """Custom type ripCurCfgStaticSupply based on Integer32"""
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


_RipCurCfgStaticSupply_Type.__name__ = "Integer32"
_RipCurCfgStaticSupply_Object = MibScalar
ripCurCfgStaticSupply = _RipCurCfgStaticSupply_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 5, 7),
    _RipCurCfgStaticSupply_Type()
)
ripCurCfgStaticSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgStaticSupply.setStatus("current")


class _RipNewCfgStaticSupply_Type(Integer32):
    """Custom type ripNewCfgStaticSupply based on Integer32"""
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


_RipNewCfgStaticSupply_Type.__name__ = "Integer32"
_RipNewCfgStaticSupply_Object = MibScalar
ripNewCfgStaticSupply = _RipNewCfgStaticSupply_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 5, 8),
    _RipNewCfgStaticSupply_Type()
)
ripNewCfgStaticSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgStaticSupply.setStatus("current")


class _RipCurCfgUpdatePeriod_Type(Integer32):
    """Custom type ripCurCfgUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_RipCurCfgUpdatePeriod_Type.__name__ = "Integer32"
_RipCurCfgUpdatePeriod_Object = MibScalar
ripCurCfgUpdatePeriod = _RipCurCfgUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 5, 9),
    _RipCurCfgUpdatePeriod_Type()
)
ripCurCfgUpdatePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgUpdatePeriod.setStatus("current")


class _RipNewCfgUpdatePeriod_Type(Integer32):
    """Custom type ripNewCfgUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_RipNewCfgUpdatePeriod_Type.__name__ = "Integer32"
_RipNewCfgUpdatePeriod_Object = MibScalar
ripNewCfgUpdatePeriod = _RipNewCfgUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 5, 10),
    _RipNewCfgUpdatePeriod_Type()
)
ripNewCfgUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgUpdatePeriod.setStatus("current")


class _RipCurCfgState_Type(Integer32):
    """Custom type ripCurCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_RipCurCfgState_Type.__name__ = "Integer32"
_RipCurCfgState_Object = MibScalar
ripCurCfgState = _RipCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 5, 11),
    _RipCurCfgState_Type()
)
ripCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgState.setStatus("current")


class _RipNewCfgState_Type(Integer32):
    """Custom type ripNewCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_RipNewCfgState_Type.__name__ = "Integer32"
_RipNewCfgState_Object = MibScalar
ripNewCfgState = _RipNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 5, 12),
    _RipNewCfgState_Type()
)
ripNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgState.setStatus("current")


class _RipCurCfgPoisonReverse_Type(Integer32):
    """Custom type ripCurCfgPoisonReverse based on Integer32"""
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


_RipCurCfgPoisonReverse_Type.__name__ = "Integer32"
_RipCurCfgPoisonReverse_Object = MibScalar
ripCurCfgPoisonReverse = _RipCurCfgPoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 5, 13),
    _RipCurCfgPoisonReverse_Type()
)
ripCurCfgPoisonReverse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgPoisonReverse.setStatus("current")


class _RipNewCfgPoisonReverse_Type(Integer32):
    """Custom type ripNewCfgPoisonReverse based on Integer32"""
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


_RipNewCfgPoisonReverse_Type.__name__ = "Integer32"
_RipNewCfgPoisonReverse_Object = MibScalar
ripNewCfgPoisonReverse = _RipNewCfgPoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 5, 14),
    _RipNewCfgPoisonReverse_Type()
)
ripNewCfgPoisonReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgPoisonReverse.setStatus("current")


class _RipCurCfgSplitHorizon_Type(Integer32):
    """Custom type ripCurCfgSplitHorizon based on Integer32"""
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


_RipCurCfgSplitHorizon_Type.__name__ = "Integer32"
_RipCurCfgSplitHorizon_Object = MibScalar
ripCurCfgSplitHorizon = _RipCurCfgSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 5, 15),
    _RipCurCfgSplitHorizon_Type()
)
ripCurCfgSplitHorizon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgSplitHorizon.setStatus("current")


class _RipNewCfgSplitHorizon_Type(Integer32):
    """Custom type ripNewCfgSplitHorizon based on Integer32"""
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


_RipNewCfgSplitHorizon_Type.__name__ = "Integer32"
_RipNewCfgSplitHorizon_Object = MibScalar
ripNewCfgSplitHorizon = _RipNewCfgSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 5, 16),
    _RipNewCfgSplitHorizon_Type()
)
ripNewCfgSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgSplitHorizon.setStatus("current")
_VrrpCfg_ObjectIdentity = ObjectIdentity
vrrpCfg = _VrrpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6)
)
_VrrpGeneral_ObjectIdentity = ObjectIdentity
vrrpGeneral = _VrrpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1)
)


class _VrrpCurCfgGenState_Type(Integer32):
    """Custom type vrrpCurCfgGenState based on Integer32"""
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


_VrrpCurCfgGenState_Type.__name__ = "Integer32"
_VrrpCurCfgGenState_Object = MibScalar
vrrpCurCfgGenState = _VrrpCurCfgGenState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1, 1),
    _VrrpCurCfgGenState_Type()
)
vrrpCurCfgGenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenState.setStatus("current")


class _VrrpNewCfgGenState_Type(Integer32):
    """Custom type vrrpNewCfgGenState based on Integer32"""
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


_VrrpNewCfgGenState_Type.__name__ = "Integer32"
_VrrpNewCfgGenState_Object = MibScalar
vrrpNewCfgGenState = _VrrpNewCfgGenState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1, 2),
    _VrrpNewCfgGenState_Type()
)
vrrpNewCfgGenState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenState.setStatus("current")


class _VrrpCurCfgGenTckVirtRtrInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckVirtRtrInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckVirtRtrInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckVirtRtrInc_Object = MibScalar
vrrpCurCfgGenTckVirtRtrInc = _VrrpCurCfgGenTckVirtRtrInc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1, 3),
    _VrrpCurCfgGenTckVirtRtrInc_Type()
)
vrrpCurCfgGenTckVirtRtrInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckVirtRtrInc.setStatus("current")


class _VrrpNewCfgGenTckVirtRtrInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckVirtRtrInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckVirtRtrInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckVirtRtrInc_Object = MibScalar
vrrpNewCfgGenTckVirtRtrInc = _VrrpNewCfgGenTckVirtRtrInc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1, 4),
    _VrrpNewCfgGenTckVirtRtrInc_Type()
)
vrrpNewCfgGenTckVirtRtrInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckVirtRtrInc.setStatus("current")


class _VrrpCurCfgGenTckIpIntfInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckIpIntfInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckIpIntfInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckIpIntfInc_Object = MibScalar
vrrpCurCfgGenTckIpIntfInc = _VrrpCurCfgGenTckIpIntfInc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1, 5),
    _VrrpCurCfgGenTckIpIntfInc_Type()
)
vrrpCurCfgGenTckIpIntfInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckIpIntfInc.setStatus("current")


class _VrrpNewCfgGenTckIpIntfInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckIpIntfInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckIpIntfInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckIpIntfInc_Object = MibScalar
vrrpNewCfgGenTckIpIntfInc = _VrrpNewCfgGenTckIpIntfInc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1, 6),
    _VrrpNewCfgGenTckIpIntfInc_Type()
)
vrrpNewCfgGenTckIpIntfInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckIpIntfInc.setStatus("current")


class _VrrpCurCfgGenTckVlanPortInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckVlanPortInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckVlanPortInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckVlanPortInc_Object = MibScalar
vrrpCurCfgGenTckVlanPortInc = _VrrpCurCfgGenTckVlanPortInc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1, 7),
    _VrrpCurCfgGenTckVlanPortInc_Type()
)
vrrpCurCfgGenTckVlanPortInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckVlanPortInc.setStatus("current")


class _VrrpNewCfgGenTckVlanPortInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckVlanPortInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckVlanPortInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckVlanPortInc_Object = MibScalar
vrrpNewCfgGenTckVlanPortInc = _VrrpNewCfgGenTckVlanPortInc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1, 8),
    _VrrpNewCfgGenTckVlanPortInc_Type()
)
vrrpNewCfgGenTckVlanPortInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckVlanPortInc.setStatus("current")


class _VrrpCurCfgGenTckL4PortInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckL4PortInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckL4PortInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckL4PortInc_Object = MibScalar
vrrpCurCfgGenTckL4PortInc = _VrrpCurCfgGenTckL4PortInc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1, 9),
    _VrrpCurCfgGenTckL4PortInc_Type()
)
vrrpCurCfgGenTckL4PortInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckL4PortInc.setStatus("current")


class _VrrpNewCfgGenTckL4PortInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckL4PortInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckL4PortInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckL4PortInc_Object = MibScalar
vrrpNewCfgGenTckL4PortInc = _VrrpNewCfgGenTckL4PortInc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1, 10),
    _VrrpNewCfgGenTckL4PortInc_Type()
)
vrrpNewCfgGenTckL4PortInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckL4PortInc.setStatus("current")


class _VrrpCurCfgGenTckRServerInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckRServerInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckRServerInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckRServerInc_Object = MibScalar
vrrpCurCfgGenTckRServerInc = _VrrpCurCfgGenTckRServerInc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1, 11),
    _VrrpCurCfgGenTckRServerInc_Type()
)
vrrpCurCfgGenTckRServerInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckRServerInc.setStatus("current")


class _VrrpNewCfgGenTckRServerInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckRServerInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckRServerInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckRServerInc_Object = MibScalar
vrrpNewCfgGenTckRServerInc = _VrrpNewCfgGenTckRServerInc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1, 12),
    _VrrpNewCfgGenTckRServerInc_Type()
)
vrrpNewCfgGenTckRServerInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckRServerInc.setStatus("current")


class _VrrpCurCfgGenTckHsrpInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckHsrpInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckHsrpInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckHsrpInc_Object = MibScalar
vrrpCurCfgGenTckHsrpInc = _VrrpCurCfgGenTckHsrpInc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1, 13),
    _VrrpCurCfgGenTckHsrpInc_Type()
)
vrrpCurCfgGenTckHsrpInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckHsrpInc.setStatus("current")


class _VrrpNewCfgGenTckHsrpInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckHsrpInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckHsrpInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckHsrpInc_Object = MibScalar
vrrpNewCfgGenTckHsrpInc = _VrrpNewCfgGenTckHsrpInc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1, 14),
    _VrrpNewCfgGenTckHsrpInc_Type()
)
vrrpNewCfgGenTckHsrpInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckHsrpInc.setStatus("current")


class _VrrpCurCfgGenHotstandby_Type(Integer32):
    """Custom type vrrpCurCfgGenHotstandby based on Integer32"""
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


_VrrpCurCfgGenHotstandby_Type.__name__ = "Integer32"
_VrrpCurCfgGenHotstandby_Object = MibScalar
vrrpCurCfgGenHotstandby = _VrrpCurCfgGenHotstandby_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1, 15),
    _VrrpCurCfgGenHotstandby_Type()
)
vrrpCurCfgGenHotstandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenHotstandby.setStatus("current")


class _VrrpNewCfgGenHotstandby_Type(Integer32):
    """Custom type vrrpNewCfgGenHotstandby based on Integer32"""
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


_VrrpNewCfgGenHotstandby_Type.__name__ = "Integer32"
_VrrpNewCfgGenHotstandby_Object = MibScalar
vrrpNewCfgGenHotstandby = _VrrpNewCfgGenHotstandby_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1, 16),
    _VrrpNewCfgGenHotstandby_Type()
)
vrrpNewCfgGenHotstandby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenHotstandby.setStatus("current")


class _VrrpCurCfgGenTckHsrvInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckHsrvInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckHsrvInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckHsrvInc_Object = MibScalar
vrrpCurCfgGenTckHsrvInc = _VrrpCurCfgGenTckHsrvInc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1, 17),
    _VrrpCurCfgGenTckHsrvInc_Type()
)
vrrpCurCfgGenTckHsrvInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckHsrvInc.setStatus("current")


class _VrrpNewCfgGenTckHsrvInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckHsrvInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckHsrvInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckHsrvInc_Object = MibScalar
vrrpNewCfgGenTckHsrvInc = _VrrpNewCfgGenTckHsrvInc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 1, 18),
    _VrrpNewCfgGenTckHsrvInc_Type()
)
vrrpNewCfgGenTckHsrvInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckHsrvInc.setStatus("current")
_VrrpVirtRtrTableMaxSize_Type = Integer32
_VrrpVirtRtrTableMaxSize_Object = MibScalar
vrrpVirtRtrTableMaxSize = _VrrpVirtRtrTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 2),
    _VrrpVirtRtrTableMaxSize_Type()
)
vrrpVirtRtrTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpVirtRtrTableMaxSize.setStatus("current")
_VrrpCurCfgVirtRtrTable_Object = MibTable
vrrpCurCfgVirtRtrTable = _VrrpCurCfgVirtRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 3)
)
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTable.setStatus("current")
_VrrpCurCfgVirtRtrTableEntry_Object = MibTableRow
vrrpCurCfgVirtRtrTableEntry = _VrrpCurCfgVirtRtrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 3, 1)
)
vrrpCurCfgVirtRtrTableEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "vrrpCurCfgVirtRtrIndx"),
)
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTableEntry.setStatus("current")
_VrrpCurCfgVirtRtrIndx_Type = Integer32
_VrrpCurCfgVirtRtrIndx_Object = MibTableColumn
vrrpCurCfgVirtRtrIndx = _VrrpCurCfgVirtRtrIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 3, 1, 1),
    _VrrpCurCfgVirtRtrIndx_Type()
)
vrrpCurCfgVirtRtrIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrIndx.setStatus("current")


class _VrrpCurCfgVirtRtrID_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpCurCfgVirtRtrID_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrID_Object = MibTableColumn
vrrpCurCfgVirtRtrID = _VrrpCurCfgVirtRtrID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 3, 1, 2),
    _VrrpCurCfgVirtRtrID_Type()
)
vrrpCurCfgVirtRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrID.setStatus("current")
_VrrpCurCfgVirtRtrAddr_Type = IpAddress
_VrrpCurCfgVirtRtrAddr_Object = MibTableColumn
vrrpCurCfgVirtRtrAddr = _VrrpCurCfgVirtRtrAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 3, 1, 3),
    _VrrpCurCfgVirtRtrAddr_Type()
)
vrrpCurCfgVirtRtrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrAddr.setStatus("current")
_VrrpCurCfgVirtRtrIfIndex_Type = Integer32
_VrrpCurCfgVirtRtrIfIndex_Object = MibTableColumn
vrrpCurCfgVirtRtrIfIndex = _VrrpCurCfgVirtRtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 3, 1, 4),
    _VrrpCurCfgVirtRtrIfIndex_Type()
)
vrrpCurCfgVirtRtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrIfIndex.setStatus("current")


class _VrrpCurCfgVirtRtrInterval_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpCurCfgVirtRtrInterval_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrInterval_Object = MibTableColumn
vrrpCurCfgVirtRtrInterval = _VrrpCurCfgVirtRtrInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 3, 1, 5),
    _VrrpCurCfgVirtRtrInterval_Type()
)
vrrpCurCfgVirtRtrInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrInterval.setStatus("current")


class _VrrpCurCfgVirtRtrPriority_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VrrpCurCfgVirtRtrPriority_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrPriority_Object = MibTableColumn
vrrpCurCfgVirtRtrPriority = _VrrpCurCfgVirtRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 3, 1, 6),
    _VrrpCurCfgVirtRtrPriority_Type()
)
vrrpCurCfgVirtRtrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrPriority.setStatus("current")


class _VrrpCurCfgVirtRtrPreempt_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrPreempt based on Integer32"""
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


_VrrpCurCfgVirtRtrPreempt_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrPreempt_Object = MibTableColumn
vrrpCurCfgVirtRtrPreempt = _VrrpCurCfgVirtRtrPreempt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 3, 1, 7),
    _VrrpCurCfgVirtRtrPreempt_Type()
)
vrrpCurCfgVirtRtrPreempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrPreempt.setStatus("current")


class _VrrpCurCfgVirtRtrState_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrState based on Integer32"""
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


_VrrpCurCfgVirtRtrState_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrState_Object = MibTableColumn
vrrpCurCfgVirtRtrState = _VrrpCurCfgVirtRtrState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 3, 1, 8),
    _VrrpCurCfgVirtRtrState_Type()
)
vrrpCurCfgVirtRtrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrState.setStatus("current")


class _VrrpCurCfgVirtRtrSharing_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrSharing based on Integer32"""
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


_VrrpCurCfgVirtRtrSharing_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrSharing_Object = MibTableColumn
vrrpCurCfgVirtRtrSharing = _VrrpCurCfgVirtRtrSharing_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 3, 1, 9),
    _VrrpCurCfgVirtRtrSharing_Type()
)
vrrpCurCfgVirtRtrSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrSharing.setStatus("current")


class _VrrpCurCfgVirtRtrTckVirtRtr_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrTckVirtRtr based on Integer32"""
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


_VrrpCurCfgVirtRtrTckVirtRtr_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrTckVirtRtr_Object = MibTableColumn
vrrpCurCfgVirtRtrTckVirtRtr = _VrrpCurCfgVirtRtrTckVirtRtr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 3, 1, 10),
    _VrrpCurCfgVirtRtrTckVirtRtr_Type()
)
vrrpCurCfgVirtRtrTckVirtRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckVirtRtr.setStatus("current")


class _VrrpCurCfgVirtRtrTckIpIntf_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrTckIpIntf based on Integer32"""
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


_VrrpCurCfgVirtRtrTckIpIntf_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrTckIpIntf_Object = MibTableColumn
vrrpCurCfgVirtRtrTckIpIntf = _VrrpCurCfgVirtRtrTckIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 3, 1, 11),
    _VrrpCurCfgVirtRtrTckIpIntf_Type()
)
vrrpCurCfgVirtRtrTckIpIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckIpIntf.setStatus("current")


class _VrrpCurCfgVirtRtrTckVlanPort_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrTckVlanPort based on Integer32"""
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


_VrrpCurCfgVirtRtrTckVlanPort_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrTckVlanPort_Object = MibTableColumn
vrrpCurCfgVirtRtrTckVlanPort = _VrrpCurCfgVirtRtrTckVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 3, 1, 12),
    _VrrpCurCfgVirtRtrTckVlanPort_Type()
)
vrrpCurCfgVirtRtrTckVlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckVlanPort.setStatus("current")


class _VrrpCurCfgVirtRtrTckL4Port_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrTckL4Port based on Integer32"""
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


_VrrpCurCfgVirtRtrTckL4Port_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrTckL4Port_Object = MibTableColumn
vrrpCurCfgVirtRtrTckL4Port = _VrrpCurCfgVirtRtrTckL4Port_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 3, 1, 13),
    _VrrpCurCfgVirtRtrTckL4Port_Type()
)
vrrpCurCfgVirtRtrTckL4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckL4Port.setStatus("current")


class _VrrpCurCfgVirtRtrTckRServer_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrTckRServer based on Integer32"""
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


_VrrpCurCfgVirtRtrTckRServer_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrTckRServer_Object = MibTableColumn
vrrpCurCfgVirtRtrTckRServer = _VrrpCurCfgVirtRtrTckRServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 3, 1, 14),
    _VrrpCurCfgVirtRtrTckRServer_Type()
)
vrrpCurCfgVirtRtrTckRServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckRServer.setStatus("current")


class _VrrpCurCfgVirtRtrTckHsrp_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrTckHsrp based on Integer32"""
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


_VrrpCurCfgVirtRtrTckHsrp_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrTckHsrp_Object = MibTableColumn
vrrpCurCfgVirtRtrTckHsrp = _VrrpCurCfgVirtRtrTckHsrp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 3, 1, 15),
    _VrrpCurCfgVirtRtrTckHsrp_Type()
)
vrrpCurCfgVirtRtrTckHsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckHsrp.setStatus("current")


class _VrrpCurCfgVirtRtrTckHsrv_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrTckHsrv based on Integer32"""
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


_VrrpCurCfgVirtRtrTckHsrv_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrTckHsrv_Object = MibTableColumn
vrrpCurCfgVirtRtrTckHsrv = _VrrpCurCfgVirtRtrTckHsrv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 3, 1, 16),
    _VrrpCurCfgVirtRtrTckHsrv_Type()
)
vrrpCurCfgVirtRtrTckHsrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckHsrv.setStatus("current")
_VrrpNewCfgVirtRtrTable_Object = MibTable
vrrpNewCfgVirtRtrTable = _VrrpNewCfgVirtRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4)
)
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTable.setStatus("current")
_VrrpNewCfgVirtRtrTableEntry_Object = MibTableRow
vrrpNewCfgVirtRtrTableEntry = _VrrpNewCfgVirtRtrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4, 1)
)
vrrpNewCfgVirtRtrTableEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "vrrpNewCfgVirtRtrIndx"),
)
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTableEntry.setStatus("current")
_VrrpNewCfgVirtRtrIndx_Type = Integer32
_VrrpNewCfgVirtRtrIndx_Object = MibTableColumn
vrrpNewCfgVirtRtrIndx = _VrrpNewCfgVirtRtrIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4, 1, 1),
    _VrrpNewCfgVirtRtrIndx_Type()
)
vrrpNewCfgVirtRtrIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrIndx.setStatus("current")


class _VrrpNewCfgVirtRtrID_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpNewCfgVirtRtrID_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrID_Object = MibTableColumn
vrrpNewCfgVirtRtrID = _VrrpNewCfgVirtRtrID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4, 1, 2),
    _VrrpNewCfgVirtRtrID_Type()
)
vrrpNewCfgVirtRtrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrID.setStatus("current")
_VrrpNewCfgVirtRtrAddr_Type = IpAddress
_VrrpNewCfgVirtRtrAddr_Object = MibTableColumn
vrrpNewCfgVirtRtrAddr = _VrrpNewCfgVirtRtrAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4, 1, 3),
    _VrrpNewCfgVirtRtrAddr_Type()
)
vrrpNewCfgVirtRtrAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrAddr.setStatus("current")
_VrrpNewCfgVirtRtrIfIndex_Type = Integer32
_VrrpNewCfgVirtRtrIfIndex_Object = MibTableColumn
vrrpNewCfgVirtRtrIfIndex = _VrrpNewCfgVirtRtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4, 1, 4),
    _VrrpNewCfgVirtRtrIfIndex_Type()
)
vrrpNewCfgVirtRtrIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrIfIndex.setStatus("current")


class _VrrpNewCfgVirtRtrInterval_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpNewCfgVirtRtrInterval_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrInterval_Object = MibTableColumn
vrrpNewCfgVirtRtrInterval = _VrrpNewCfgVirtRtrInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4, 1, 5),
    _VrrpNewCfgVirtRtrInterval_Type()
)
vrrpNewCfgVirtRtrInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrInterval.setStatus("current")


class _VrrpNewCfgVirtRtrPriority_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VrrpNewCfgVirtRtrPriority_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrPriority_Object = MibTableColumn
vrrpNewCfgVirtRtrPriority = _VrrpNewCfgVirtRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4, 1, 6),
    _VrrpNewCfgVirtRtrPriority_Type()
)
vrrpNewCfgVirtRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrPriority.setStatus("current")


class _VrrpNewCfgVirtRtrPreempt_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrPreempt based on Integer32"""
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


_VrrpNewCfgVirtRtrPreempt_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrPreempt_Object = MibTableColumn
vrrpNewCfgVirtRtrPreempt = _VrrpNewCfgVirtRtrPreempt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4, 1, 7),
    _VrrpNewCfgVirtRtrPreempt_Type()
)
vrrpNewCfgVirtRtrPreempt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrPreempt.setStatus("current")


class _VrrpNewCfgVirtRtrState_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrState based on Integer32"""
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


_VrrpNewCfgVirtRtrState_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrState_Object = MibTableColumn
vrrpNewCfgVirtRtrState = _VrrpNewCfgVirtRtrState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4, 1, 8),
    _VrrpNewCfgVirtRtrState_Type()
)
vrrpNewCfgVirtRtrState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrState.setStatus("current")


class _VrrpNewCfgVirtRtrDelete_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrDelete based on Integer32"""
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


_VrrpNewCfgVirtRtrDelete_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrDelete_Object = MibTableColumn
vrrpNewCfgVirtRtrDelete = _VrrpNewCfgVirtRtrDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4, 1, 9),
    _VrrpNewCfgVirtRtrDelete_Type()
)
vrrpNewCfgVirtRtrDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrDelete.setStatus("current")


class _VrrpNewCfgVirtRtrSharing_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrSharing based on Integer32"""
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


_VrrpNewCfgVirtRtrSharing_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrSharing_Object = MibTableColumn
vrrpNewCfgVirtRtrSharing = _VrrpNewCfgVirtRtrSharing_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4, 1, 10),
    _VrrpNewCfgVirtRtrSharing_Type()
)
vrrpNewCfgVirtRtrSharing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrSharing.setStatus("current")


class _VrrpNewCfgVirtRtrTckVirtRtr_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrTckVirtRtr based on Integer32"""
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


_VrrpNewCfgVirtRtrTckVirtRtr_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrTckVirtRtr_Object = MibTableColumn
vrrpNewCfgVirtRtrTckVirtRtr = _VrrpNewCfgVirtRtrTckVirtRtr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4, 1, 11),
    _VrrpNewCfgVirtRtrTckVirtRtr_Type()
)
vrrpNewCfgVirtRtrTckVirtRtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckVirtRtr.setStatus("current")


class _VrrpNewCfgVirtRtrTckIpIntf_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrTckIpIntf based on Integer32"""
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


_VrrpNewCfgVirtRtrTckIpIntf_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrTckIpIntf_Object = MibTableColumn
vrrpNewCfgVirtRtrTckIpIntf = _VrrpNewCfgVirtRtrTckIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4, 1, 12),
    _VrrpNewCfgVirtRtrTckIpIntf_Type()
)
vrrpNewCfgVirtRtrTckIpIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckIpIntf.setStatus("current")


class _VrrpNewCfgVirtRtrTckVlanPort_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrTckVlanPort based on Integer32"""
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


_VrrpNewCfgVirtRtrTckVlanPort_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrTckVlanPort_Object = MibTableColumn
vrrpNewCfgVirtRtrTckVlanPort = _VrrpNewCfgVirtRtrTckVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4, 1, 13),
    _VrrpNewCfgVirtRtrTckVlanPort_Type()
)
vrrpNewCfgVirtRtrTckVlanPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckVlanPort.setStatus("current")


class _VrrpNewCfgVirtRtrTckL4Port_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrTckL4Port based on Integer32"""
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


_VrrpNewCfgVirtRtrTckL4Port_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrTckL4Port_Object = MibTableColumn
vrrpNewCfgVirtRtrTckL4Port = _VrrpNewCfgVirtRtrTckL4Port_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4, 1, 14),
    _VrrpNewCfgVirtRtrTckL4Port_Type()
)
vrrpNewCfgVirtRtrTckL4Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckL4Port.setStatus("current")


class _VrrpNewCfgVirtRtrTckRServer_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrTckRServer based on Integer32"""
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


_VrrpNewCfgVirtRtrTckRServer_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrTckRServer_Object = MibTableColumn
vrrpNewCfgVirtRtrTckRServer = _VrrpNewCfgVirtRtrTckRServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4, 1, 15),
    _VrrpNewCfgVirtRtrTckRServer_Type()
)
vrrpNewCfgVirtRtrTckRServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckRServer.setStatus("current")


class _VrrpNewCfgVirtRtrTckHsrp_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrTckHsrp based on Integer32"""
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


_VrrpNewCfgVirtRtrTckHsrp_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrTckHsrp_Object = MibTableColumn
vrrpNewCfgVirtRtrTckHsrp = _VrrpNewCfgVirtRtrTckHsrp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4, 1, 16),
    _VrrpNewCfgVirtRtrTckHsrp_Type()
)
vrrpNewCfgVirtRtrTckHsrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckHsrp.setStatus("current")


class _VrrpNewCfgVirtRtrTckHsrv_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrTckHsrv based on Integer32"""
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


_VrrpNewCfgVirtRtrTckHsrv_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrTckHsrv_Object = MibTableColumn
vrrpNewCfgVirtRtrTckHsrv = _VrrpNewCfgVirtRtrTckHsrv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 4, 1, 17),
    _VrrpNewCfgVirtRtrTckHsrv_Type()
)
vrrpNewCfgVirtRtrTckHsrv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckHsrv.setStatus("current")
_VrrpIfTableMaxSize_Type = Integer32
_VrrpIfTableMaxSize_Object = MibScalar
vrrpIfTableMaxSize = _VrrpIfTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 5),
    _VrrpIfTableMaxSize_Type()
)
vrrpIfTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpIfTableMaxSize.setStatus("current")
_VrrpCurCfgIfTable_Object = MibTable
vrrpCurCfgIfTable = _VrrpCurCfgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 6)
)
if mibBuilder.loadTexts:
    vrrpCurCfgIfTable.setStatus("current")
_VrrpCurCfgIfTableEntry_Object = MibTableRow
vrrpCurCfgIfTableEntry = _VrrpCurCfgIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 6, 1)
)
vrrpCurCfgIfTableEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "vrrpCurCfgIfIndx"),
)
if mibBuilder.loadTexts:
    vrrpCurCfgIfTableEntry.setStatus("current")
_VrrpCurCfgIfIndx_Type = Integer32
_VrrpCurCfgIfIndx_Object = MibTableColumn
vrrpCurCfgIfIndx = _VrrpCurCfgIfIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 6, 1, 1),
    _VrrpCurCfgIfIndx_Type()
)
vrrpCurCfgIfIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgIfIndx.setStatus("current")


class _VrrpCurCfgIfAuthType_Type(Integer32):
    """Custom type vrrpCurCfgIfAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("simple-text-password", 2))
    )


_VrrpCurCfgIfAuthType_Type.__name__ = "Integer32"
_VrrpCurCfgIfAuthType_Object = MibTableColumn
vrrpCurCfgIfAuthType = _VrrpCurCfgIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 6, 1, 2),
    _VrrpCurCfgIfAuthType_Type()
)
vrrpCurCfgIfAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgIfAuthType.setStatus("current")


class _VrrpCurCfgIfPasswd_Type(DisplayString):
    """Custom type vrrpCurCfgIfPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_VrrpCurCfgIfPasswd_Type.__name__ = "DisplayString"
_VrrpCurCfgIfPasswd_Object = MibTableColumn
vrrpCurCfgIfPasswd = _VrrpCurCfgIfPasswd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 6, 1, 3),
    _VrrpCurCfgIfPasswd_Type()
)
vrrpCurCfgIfPasswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgIfPasswd.setStatus("current")
_VrrpNewCfgIfTable_Object = MibTable
vrrpNewCfgIfTable = _VrrpNewCfgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 7)
)
if mibBuilder.loadTexts:
    vrrpNewCfgIfTable.setStatus("current")
_VrrpNewCfgIfTableEntry_Object = MibTableRow
vrrpNewCfgIfTableEntry = _VrrpNewCfgIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 7, 1)
)
vrrpNewCfgIfTableEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "vrrpNewCfgIfIndx"),
)
if mibBuilder.loadTexts:
    vrrpNewCfgIfTableEntry.setStatus("current")
_VrrpNewCfgIfIndx_Type = Integer32
_VrrpNewCfgIfIndx_Object = MibTableColumn
vrrpNewCfgIfIndx = _VrrpNewCfgIfIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 7, 1, 1),
    _VrrpNewCfgIfIndx_Type()
)
vrrpNewCfgIfIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpNewCfgIfIndx.setStatus("current")


class _VrrpNewCfgIfAuthType_Type(Integer32):
    """Custom type vrrpNewCfgIfAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("simple-text-password", 2))
    )


_VrrpNewCfgIfAuthType_Type.__name__ = "Integer32"
_VrrpNewCfgIfAuthType_Object = MibTableColumn
vrrpNewCfgIfAuthType = _VrrpNewCfgIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 7, 1, 2),
    _VrrpNewCfgIfAuthType_Type()
)
vrrpNewCfgIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgIfAuthType.setStatus("current")


class _VrrpNewCfgIfPasswd_Type(DisplayString):
    """Custom type vrrpNewCfgIfPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_VrrpNewCfgIfPasswd_Type.__name__ = "DisplayString"
_VrrpNewCfgIfPasswd_Object = MibTableColumn
vrrpNewCfgIfPasswd = _VrrpNewCfgIfPasswd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 7, 1, 3),
    _VrrpNewCfgIfPasswd_Type()
)
vrrpNewCfgIfPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgIfPasswd.setStatus("current")


class _VrrpNewCfgIfDelete_Type(Integer32):
    """Custom type vrrpNewCfgIfDelete based on Integer32"""
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


_VrrpNewCfgIfDelete_Type.__name__ = "Integer32"
_VrrpNewCfgIfDelete_Object = MibTableColumn
vrrpNewCfgIfDelete = _VrrpNewCfgIfDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 7, 1, 4),
    _VrrpNewCfgIfDelete_Type()
)
vrrpNewCfgIfDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgIfDelete.setStatus("current")
_VrrpVirtRtrGrpTableMaxSize_Type = Integer32
_VrrpVirtRtrGrpTableMaxSize_Object = MibScalar
vrrpVirtRtrGrpTableMaxSize = _VrrpVirtRtrGrpTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 8),
    _VrrpVirtRtrGrpTableMaxSize_Type()
)
vrrpVirtRtrGrpTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpVirtRtrGrpTableMaxSize.setStatus("current")
_VrrpCurCfgVirtRtrGrpTable_Object = MibTable
vrrpCurCfgVirtRtrGrpTable = _VrrpCurCfgVirtRtrGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 9)
)
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTable.setStatus("current")
_VrrpCurCfgVirtRtrGrpTableEntry_Object = MibTableRow
vrrpCurCfgVirtRtrGrpTableEntry = _VrrpCurCfgVirtRtrGrpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 9, 1)
)
vrrpCurCfgVirtRtrGrpTableEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "vrrpCurCfgVirtRtrGrpIndx"),
)
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTableEntry.setStatus("current")
_VrrpCurCfgVirtRtrGrpIndx_Type = Integer32
_VrrpCurCfgVirtRtrGrpIndx_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpIndx = _VrrpCurCfgVirtRtrGrpIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 9, 1, 1),
    _VrrpCurCfgVirtRtrGrpIndx_Type()
)
vrrpCurCfgVirtRtrGrpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpIndx.setStatus("current")


class _VrrpCurCfgVirtRtrGrpID_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpCurCfgVirtRtrGrpID_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpID_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpID = _VrrpCurCfgVirtRtrGrpID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 9, 1, 2),
    _VrrpCurCfgVirtRtrGrpID_Type()
)
vrrpCurCfgVirtRtrGrpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpID.setStatus("current")
_VrrpCurCfgVirtRtrGrpIfIndex_Type = Integer32
_VrrpCurCfgVirtRtrGrpIfIndex_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpIfIndex = _VrrpCurCfgVirtRtrGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 9, 1, 3),
    _VrrpCurCfgVirtRtrGrpIfIndex_Type()
)
vrrpCurCfgVirtRtrGrpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpIfIndex.setStatus("current")


class _VrrpCurCfgVirtRtrGrpInterval_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpCurCfgVirtRtrGrpInterval_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpInterval_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpInterval = _VrrpCurCfgVirtRtrGrpInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 9, 1, 4),
    _VrrpCurCfgVirtRtrGrpInterval_Type()
)
vrrpCurCfgVirtRtrGrpInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpInterval.setStatus("current")


class _VrrpCurCfgVirtRtrGrpPriority_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VrrpCurCfgVirtRtrGrpPriority_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpPriority_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpPriority = _VrrpCurCfgVirtRtrGrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 9, 1, 5),
    _VrrpCurCfgVirtRtrGrpPriority_Type()
)
vrrpCurCfgVirtRtrGrpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpPriority.setStatus("current")


class _VrrpCurCfgVirtRtrGrpPreempt_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpPreempt based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpPreempt_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpPreempt_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpPreempt = _VrrpCurCfgVirtRtrGrpPreempt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 9, 1, 6),
    _VrrpCurCfgVirtRtrGrpPreempt_Type()
)
vrrpCurCfgVirtRtrGrpPreempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpPreempt.setStatus("current")


class _VrrpCurCfgVirtRtrGrpState_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpState based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpState_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpState_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpState = _VrrpCurCfgVirtRtrGrpState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 9, 1, 7),
    _VrrpCurCfgVirtRtrGrpState_Type()
)
vrrpCurCfgVirtRtrGrpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpState.setStatus("current")


class _VrrpCurCfgVirtRtrGrpSharing_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpSharing based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpSharing_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpSharing_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpSharing = _VrrpCurCfgVirtRtrGrpSharing_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 9, 1, 8),
    _VrrpCurCfgVirtRtrGrpSharing_Type()
)
vrrpCurCfgVirtRtrGrpSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpSharing.setStatus("current")


class _VrrpCurCfgVirtRtrGrpTckVirtRtr_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpTckVirtRtr based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpTckVirtRtr_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpTckVirtRtr_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpTckVirtRtr = _VrrpCurCfgVirtRtrGrpTckVirtRtr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 9, 1, 9),
    _VrrpCurCfgVirtRtrGrpTckVirtRtr_Type()
)
vrrpCurCfgVirtRtrGrpTckVirtRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckVirtRtr.setStatus("current")


class _VrrpCurCfgVirtRtrGrpTckIpIntf_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpTckIpIntf based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpTckIpIntf_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpTckIpIntf_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpTckIpIntf = _VrrpCurCfgVirtRtrGrpTckIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 9, 1, 10),
    _VrrpCurCfgVirtRtrGrpTckIpIntf_Type()
)
vrrpCurCfgVirtRtrGrpTckIpIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckIpIntf.setStatus("current")


class _VrrpCurCfgVirtRtrGrpTckVlanPort_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpTckVlanPort based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpTckVlanPort_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpTckVlanPort_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpTckVlanPort = _VrrpCurCfgVirtRtrGrpTckVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 9, 1, 11),
    _VrrpCurCfgVirtRtrGrpTckVlanPort_Type()
)
vrrpCurCfgVirtRtrGrpTckVlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckVlanPort.setStatus("current")


class _VrrpCurCfgVirtRtrGrpTckL4Port_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpTckL4Port based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpTckL4Port_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpTckL4Port_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpTckL4Port = _VrrpCurCfgVirtRtrGrpTckL4Port_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 9, 1, 12),
    _VrrpCurCfgVirtRtrGrpTckL4Port_Type()
)
vrrpCurCfgVirtRtrGrpTckL4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckL4Port.setStatus("current")


class _VrrpCurCfgVirtRtrGrpTckRServer_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpTckRServer based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpTckRServer_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpTckRServer_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpTckRServer = _VrrpCurCfgVirtRtrGrpTckRServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 9, 1, 13),
    _VrrpCurCfgVirtRtrGrpTckRServer_Type()
)
vrrpCurCfgVirtRtrGrpTckRServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckRServer.setStatus("current")


class _VrrpCurCfgVirtRtrGrpTckHsrp_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpTckHsrp based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpTckHsrp_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpTckHsrp_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpTckHsrp = _VrrpCurCfgVirtRtrGrpTckHsrp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 9, 1, 14),
    _VrrpCurCfgVirtRtrGrpTckHsrp_Type()
)
vrrpCurCfgVirtRtrGrpTckHsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckHsrp.setStatus("current")


class _VrrpCurCfgVirtRtrGrpTckHsrv_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpTckHsrv based on Integer32"""
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


_VrrpCurCfgVirtRtrGrpTckHsrv_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpTckHsrv_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpTckHsrv = _VrrpCurCfgVirtRtrGrpTckHsrv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 9, 1, 15),
    _VrrpCurCfgVirtRtrGrpTckHsrv_Type()
)
vrrpCurCfgVirtRtrGrpTckHsrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckHsrv.setStatus("current")
_VrrpNewCfgVirtRtrGrpTable_Object = MibTable
vrrpNewCfgVirtRtrGrpTable = _VrrpNewCfgVirtRtrGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 10)
)
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTable.setStatus("current")
_VrrpNewCfgVirtRtrGrpTableEntry_Object = MibTableRow
vrrpNewCfgVirtRtrGrpTableEntry = _VrrpNewCfgVirtRtrGrpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 10, 1)
)
vrrpNewCfgVirtRtrGrpTableEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "vrrpNewCfgVirtRtrGrpIndx"),
)
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTableEntry.setStatus("current")
_VrrpNewCfgVirtRtrGrpIndx_Type = Integer32
_VrrpNewCfgVirtRtrGrpIndx_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpIndx = _VrrpNewCfgVirtRtrGrpIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 10, 1, 1),
    _VrrpNewCfgVirtRtrGrpIndx_Type()
)
vrrpNewCfgVirtRtrGrpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpIndx.setStatus("current")


class _VrrpNewCfgVirtRtrGrpID_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpNewCfgVirtRtrGrpID_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpID_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpID = _VrrpNewCfgVirtRtrGrpID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 10, 1, 2),
    _VrrpNewCfgVirtRtrGrpID_Type()
)
vrrpNewCfgVirtRtrGrpID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpID.setStatus("current")
_VrrpNewCfgVirtRtrGrpIfIndex_Type = Integer32
_VrrpNewCfgVirtRtrGrpIfIndex_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpIfIndex = _VrrpNewCfgVirtRtrGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 10, 1, 3),
    _VrrpNewCfgVirtRtrGrpIfIndex_Type()
)
vrrpNewCfgVirtRtrGrpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpIfIndex.setStatus("current")


class _VrrpNewCfgVirtRtrGrpInterval_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpNewCfgVirtRtrGrpInterval_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpInterval_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpInterval = _VrrpNewCfgVirtRtrGrpInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 10, 1, 4),
    _VrrpNewCfgVirtRtrGrpInterval_Type()
)
vrrpNewCfgVirtRtrGrpInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpInterval.setStatus("current")


class _VrrpNewCfgVirtRtrGrpPriority_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VrrpNewCfgVirtRtrGrpPriority_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpPriority_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpPriority = _VrrpNewCfgVirtRtrGrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 10, 1, 5),
    _VrrpNewCfgVirtRtrGrpPriority_Type()
)
vrrpNewCfgVirtRtrGrpPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpPriority.setStatus("current")


class _VrrpNewCfgVirtRtrGrpPreempt_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpPreempt based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpPreempt_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpPreempt_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpPreempt = _VrrpNewCfgVirtRtrGrpPreempt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 10, 1, 6),
    _VrrpNewCfgVirtRtrGrpPreempt_Type()
)
vrrpNewCfgVirtRtrGrpPreempt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpPreempt.setStatus("current")


class _VrrpNewCfgVirtRtrGrpState_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpState based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpState_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpState_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpState = _VrrpNewCfgVirtRtrGrpState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 10, 1, 7),
    _VrrpNewCfgVirtRtrGrpState_Type()
)
vrrpNewCfgVirtRtrGrpState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpState.setStatus("current")


class _VrrpNewCfgVirtRtrGrpDelete_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpDelete based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpDelete_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpDelete_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpDelete = _VrrpNewCfgVirtRtrGrpDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 10, 1, 8),
    _VrrpNewCfgVirtRtrGrpDelete_Type()
)
vrrpNewCfgVirtRtrGrpDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpDelete.setStatus("current")


class _VrrpNewCfgVirtRtrGrpSharing_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpSharing based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpSharing_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpSharing_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpSharing = _VrrpNewCfgVirtRtrGrpSharing_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 10, 1, 9),
    _VrrpNewCfgVirtRtrGrpSharing_Type()
)
vrrpNewCfgVirtRtrGrpSharing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpSharing.setStatus("current")


class _VrrpNewCfgVirtRtrGrpTckVirtRtr_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpTckVirtRtr based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpTckVirtRtr_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpTckVirtRtr_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpTckVirtRtr = _VrrpNewCfgVirtRtrGrpTckVirtRtr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 10, 1, 10),
    _VrrpNewCfgVirtRtrGrpTckVirtRtr_Type()
)
vrrpNewCfgVirtRtrGrpTckVirtRtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckVirtRtr.setStatus("current")


class _VrrpNewCfgVirtRtrGrpTckIpIntf_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpTckIpIntf based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpTckIpIntf_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpTckIpIntf_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpTckIpIntf = _VrrpNewCfgVirtRtrGrpTckIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 10, 1, 11),
    _VrrpNewCfgVirtRtrGrpTckIpIntf_Type()
)
vrrpNewCfgVirtRtrGrpTckIpIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckIpIntf.setStatus("current")


class _VrrpNewCfgVirtRtrGrpTckVlanPort_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpTckVlanPort based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpTckVlanPort_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpTckVlanPort_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpTckVlanPort = _VrrpNewCfgVirtRtrGrpTckVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 10, 1, 12),
    _VrrpNewCfgVirtRtrGrpTckVlanPort_Type()
)
vrrpNewCfgVirtRtrGrpTckVlanPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckVlanPort.setStatus("current")


class _VrrpNewCfgVirtRtrGrpTckL4Port_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpTckL4Port based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpTckL4Port_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpTckL4Port_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpTckL4Port = _VrrpNewCfgVirtRtrGrpTckL4Port_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 10, 1, 13),
    _VrrpNewCfgVirtRtrGrpTckL4Port_Type()
)
vrrpNewCfgVirtRtrGrpTckL4Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckL4Port.setStatus("current")


class _VrrpNewCfgVirtRtrGrpTckRServer_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpTckRServer based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpTckRServer_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpTckRServer_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpTckRServer = _VrrpNewCfgVirtRtrGrpTckRServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 10, 1, 14),
    _VrrpNewCfgVirtRtrGrpTckRServer_Type()
)
vrrpNewCfgVirtRtrGrpTckRServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckRServer.setStatus("current")


class _VrrpNewCfgVirtRtrGrpTckHsrp_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpTckHsrp based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpTckHsrp_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpTckHsrp_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpTckHsrp = _VrrpNewCfgVirtRtrGrpTckHsrp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 10, 1, 15),
    _VrrpNewCfgVirtRtrGrpTckHsrp_Type()
)
vrrpNewCfgVirtRtrGrpTckHsrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckHsrp.setStatus("current")


class _VrrpNewCfgVirtRtrGrpTckHsrv_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpTckHsrv based on Integer32"""
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


_VrrpNewCfgVirtRtrGrpTckHsrv_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpTckHsrv_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpTckHsrv = _VrrpNewCfgVirtRtrGrpTckHsrv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 6, 10, 1, 16),
    _VrrpNewCfgVirtRtrGrpTckHsrv_Type()
)
vrrpNewCfgVirtRtrGrpTckHsrv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckHsrv.setStatus("current")
_ArpCfg_ObjectIdentity = ObjectIdentity
arpCfg = _ArpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7)
)


class _ArpCurCfgReARPPeriod_Type(Integer32):
    """Custom type arpCurCfgReARPPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 120),
    )


_ArpCurCfgReARPPeriod_Type.__name__ = "Integer32"
_ArpCurCfgReARPPeriod_Object = MibScalar
arpCurCfgReARPPeriod = _ArpCurCfgReARPPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7, 1),
    _ArpCurCfgReARPPeriod_Type()
)
arpCurCfgReARPPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpCurCfgReARPPeriod.setStatus("current")


class _ArpNewCfgReARPPeriod_Type(Integer32):
    """Custom type arpNewCfgReARPPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 120),
    )


_ArpNewCfgReARPPeriod_Type.__name__ = "Integer32"
_ArpNewCfgReARPPeriod_Object = MibScalar
arpNewCfgReARPPeriod = _ArpNewCfgReARPPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7, 2),
    _ArpNewCfgReARPPeriod_Type()
)
arpNewCfgReARPPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpNewCfgReARPPeriod.setStatus("current")


class _IpStaticArpTableMaxSize_Type(Integer32):
    """Custom type ipStaticArpTableMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_IpStaticArpTableMaxSize_Type.__name__ = "Integer32"
_IpStaticArpTableMaxSize_Object = MibScalar
ipStaticArpTableMaxSize = _IpStaticArpTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7, 3),
    _IpStaticArpTableMaxSize_Type()
)
ipStaticArpTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStaticArpTableMaxSize.setStatus("current")
_IpCurCfgStaticArpTable_Object = MibTable
ipCurCfgStaticArpTable = _IpCurCfgStaticArpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7, 4)
)
if mibBuilder.loadTexts:
    ipCurCfgStaticArpTable.setStatus("current")
_IpCurCfgStaticArpEntry_Object = MibTableRow
ipCurCfgStaticArpEntry = _IpCurCfgStaticArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7, 4, 1)
)
ipCurCfgStaticArpEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipCurCfgStaticArpIndx"),
)
if mibBuilder.loadTexts:
    ipCurCfgStaticArpEntry.setStatus("current")
_IpCurCfgStaticArpIndx_Type = Integer32
_IpCurCfgStaticArpIndx_Object = MibTableColumn
ipCurCfgStaticArpIndx = _IpCurCfgStaticArpIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7, 4, 1, 1),
    _IpCurCfgStaticArpIndx_Type()
)
ipCurCfgStaticArpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticArpIndx.setStatus("current")
_IpCurCfgStaticArpIp_Type = IpAddress
_IpCurCfgStaticArpIp_Object = MibTableColumn
ipCurCfgStaticArpIp = _IpCurCfgStaticArpIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7, 4, 1, 2),
    _IpCurCfgStaticArpIp_Type()
)
ipCurCfgStaticArpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticArpIp.setStatus("current")
_IpCurCfgStaticArpMAC_Type = PhysAddress
_IpCurCfgStaticArpMAC_Object = MibTableColumn
ipCurCfgStaticArpMAC = _IpCurCfgStaticArpMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7, 4, 1, 3),
    _IpCurCfgStaticArpMAC_Type()
)
ipCurCfgStaticArpMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticArpMAC.setStatus("current")


class _IpCurCfgStaticArpVlan_Type(Integer32):
    """Custom type ipCurCfgStaticArpVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4090),
    )


_IpCurCfgStaticArpVlan_Type.__name__ = "Integer32"
_IpCurCfgStaticArpVlan_Object = MibTableColumn
ipCurCfgStaticArpVlan = _IpCurCfgStaticArpVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7, 4, 1, 4),
    _IpCurCfgStaticArpVlan_Type()
)
ipCurCfgStaticArpVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticArpVlan.setStatus("current")
_IpCurCfgStaticArpPort_Type = Integer32
_IpCurCfgStaticArpPort_Object = MibTableColumn
ipCurCfgStaticArpPort = _IpCurCfgStaticArpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7, 4, 1, 5),
    _IpCurCfgStaticArpPort_Type()
)
ipCurCfgStaticArpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticArpPort.setStatus("current")
_IpNewCfgStaticArpTable_Object = MibTable
ipNewCfgStaticArpTable = _IpNewCfgStaticArpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7, 5)
)
if mibBuilder.loadTexts:
    ipNewCfgStaticArpTable.setStatus("current")
_IpNewCfgStaticArpEntry_Object = MibTableRow
ipNewCfgStaticArpEntry = _IpNewCfgStaticArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7, 5, 1)
)
ipNewCfgStaticArpEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipNewCfgStaticArpIndx"),
)
if mibBuilder.loadTexts:
    ipNewCfgStaticArpEntry.setStatus("current")
_IpNewCfgStaticArpIndx_Type = Integer32
_IpNewCfgStaticArpIndx_Object = MibTableColumn
ipNewCfgStaticArpIndx = _IpNewCfgStaticArpIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7, 5, 1, 1),
    _IpNewCfgStaticArpIndx_Type()
)
ipNewCfgStaticArpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgStaticArpIndx.setStatus("current")
_IpNewCfgStaticArpIp_Type = IpAddress
_IpNewCfgStaticArpIp_Object = MibTableColumn
ipNewCfgStaticArpIp = _IpNewCfgStaticArpIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7, 5, 1, 2),
    _IpNewCfgStaticArpIp_Type()
)
ipNewCfgStaticArpIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticArpIp.setStatus("current")
_IpNewCfgStaticArpMAC_Type = PhysAddress
_IpNewCfgStaticArpMAC_Object = MibTableColumn
ipNewCfgStaticArpMAC = _IpNewCfgStaticArpMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7, 5, 1, 3),
    _IpNewCfgStaticArpMAC_Type()
)
ipNewCfgStaticArpMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticArpMAC.setStatus("current")


class _IpNewCfgStaticArpVlan_Type(Integer32):
    """Custom type ipNewCfgStaticArpVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4090),
    )


_IpNewCfgStaticArpVlan_Type.__name__ = "Integer32"
_IpNewCfgStaticArpVlan_Object = MibTableColumn
ipNewCfgStaticArpVlan = _IpNewCfgStaticArpVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7, 5, 1, 4),
    _IpNewCfgStaticArpVlan_Type()
)
ipNewCfgStaticArpVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticArpVlan.setStatus("current")
_IpNewCfgStaticArpPort_Type = Integer32
_IpNewCfgStaticArpPort_Object = MibTableColumn
ipNewCfgStaticArpPort = _IpNewCfgStaticArpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7, 5, 1, 5),
    _IpNewCfgStaticArpPort_Type()
)
ipNewCfgStaticArpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticArpPort.setStatus("current")


class _IpNewCfgStaticArpAction_Type(Integer32):
    """Custom type ipNewCfgStaticArpAction based on Integer32"""
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


_IpNewCfgStaticArpAction_Type.__name__ = "Integer32"
_IpNewCfgStaticArpAction_Object = MibTableColumn
ipNewCfgStaticArpAction = _IpNewCfgStaticArpAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 7, 5, 1, 6),
    _IpNewCfgStaticArpAction_Type()
)
ipNewCfgStaticArpAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticArpAction.setStatus("current")
_IpBootpCfg_ObjectIdentity = ObjectIdentity
ipBootpCfg = _IpBootpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 8)
)
_IpCurCfgBootpAddr_Type = IpAddress
_IpCurCfgBootpAddr_Object = MibScalar
ipCurCfgBootpAddr = _IpCurCfgBootpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 8, 1),
    _IpCurCfgBootpAddr_Type()
)
ipCurCfgBootpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgBootpAddr.setStatus("current")
_IpNewCfgBootpAddr_Type = IpAddress
_IpNewCfgBootpAddr_Object = MibScalar
ipNewCfgBootpAddr = _IpNewCfgBootpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 8, 2),
    _IpNewCfgBootpAddr_Type()
)
ipNewCfgBootpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgBootpAddr.setStatus("current")
_IpCurCfgBootpAddr2_Type = IpAddress
_IpCurCfgBootpAddr2_Object = MibScalar
ipCurCfgBootpAddr2 = _IpCurCfgBootpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 8, 3),
    _IpCurCfgBootpAddr2_Type()
)
ipCurCfgBootpAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgBootpAddr2.setStatus("current")
_IpNewCfgBootpAddr2_Type = IpAddress
_IpNewCfgBootpAddr2_Object = MibScalar
ipNewCfgBootpAddr2 = _IpNewCfgBootpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 8, 4),
    _IpNewCfgBootpAddr2_Type()
)
ipNewCfgBootpAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgBootpAddr2.setStatus("current")


class _IpCurCfgBootpState_Type(Integer32):
    """Custom type ipCurCfgBootpState based on Integer32"""
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


_IpCurCfgBootpState_Type.__name__ = "Integer32"
_IpCurCfgBootpState_Object = MibScalar
ipCurCfgBootpState = _IpCurCfgBootpState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 8, 5),
    _IpCurCfgBootpState_Type()
)
ipCurCfgBootpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgBootpState.setStatus("current")


class _IpNewCfgBootpState_Type(Integer32):
    """Custom type ipNewCfgBootpState based on Integer32"""
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


_IpNewCfgBootpState_Type.__name__ = "Integer32"
_IpNewCfgBootpState_Object = MibScalar
ipNewCfgBootpState = _IpNewCfgBootpState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 8, 6),
    _IpNewCfgBootpState_Type()
)
ipNewCfgBootpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgBootpState.setStatus("current")


class _IpCurCfgDhcpOpt82State_Type(Integer32):
    """Custom type ipCurCfgDhcpOpt82State based on Integer32"""
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


_IpCurCfgDhcpOpt82State_Type.__name__ = "Integer32"
_IpCurCfgDhcpOpt82State_Object = MibScalar
ipCurCfgDhcpOpt82State = _IpCurCfgDhcpOpt82State_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 8, 7),
    _IpCurCfgDhcpOpt82State_Type()
)
ipCurCfgDhcpOpt82State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgDhcpOpt82State.setStatus("current")


class _IpNewCfgDhcpOpt82State_Type(Integer32):
    """Custom type ipNewCfgDhcpOpt82State based on Integer32"""
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


_IpNewCfgDhcpOpt82State_Type.__name__ = "Integer32"
_IpNewCfgDhcpOpt82State_Object = MibScalar
ipNewCfgDhcpOpt82State = _IpNewCfgDhcpOpt82State_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 8, 8),
    _IpNewCfgDhcpOpt82State_Type()
)
ipNewCfgDhcpOpt82State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgDhcpOpt82State.setStatus("current")
_DnsCfg_ObjectIdentity = ObjectIdentity
dnsCfg = _DnsCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 9)
)
_DnsCurCfgPrimaryIpAddr_Type = IpAddress
_DnsCurCfgPrimaryIpAddr_Object = MibScalar
dnsCurCfgPrimaryIpAddr = _DnsCurCfgPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 9, 1),
    _DnsCurCfgPrimaryIpAddr_Type()
)
dnsCurCfgPrimaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurCfgPrimaryIpAddr.setStatus("current")
_DnsNewCfgPrimaryIpAddr_Type = IpAddress
_DnsNewCfgPrimaryIpAddr_Object = MibScalar
dnsNewCfgPrimaryIpAddr = _DnsNewCfgPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 9, 2),
    _DnsNewCfgPrimaryIpAddr_Type()
)
dnsNewCfgPrimaryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsNewCfgPrimaryIpAddr.setStatus("current")
_DnsCurCfgSecondaryIpAddr_Type = IpAddress
_DnsCurCfgSecondaryIpAddr_Object = MibScalar
dnsCurCfgSecondaryIpAddr = _DnsCurCfgSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 9, 3),
    _DnsCurCfgSecondaryIpAddr_Type()
)
dnsCurCfgSecondaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurCfgSecondaryIpAddr.setStatus("current")
_DnsNewCfgSecondaryIpAddr_Type = IpAddress
_DnsNewCfgSecondaryIpAddr_Object = MibScalar
dnsNewCfgSecondaryIpAddr = _DnsNewCfgSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 9, 4),
    _DnsNewCfgSecondaryIpAddr_Type()
)
dnsNewCfgSecondaryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsNewCfgSecondaryIpAddr.setStatus("current")


class _DnsCurCfgDomainName_Type(DisplayString):
    """Custom type dnsCurCfgDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 191),
    )


_DnsCurCfgDomainName_Type.__name__ = "DisplayString"
_DnsCurCfgDomainName_Object = MibScalar
dnsCurCfgDomainName = _DnsCurCfgDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 9, 5),
    _DnsCurCfgDomainName_Type()
)
dnsCurCfgDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurCfgDomainName.setStatus("current")


class _DnsNewCfgDomainName_Type(DisplayString):
    """Custom type dnsNewCfgDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 191),
    )


_DnsNewCfgDomainName_Type.__name__ = "DisplayString"
_DnsNewCfgDomainName_Object = MibScalar
dnsNewCfgDomainName = _DnsNewCfgDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 9, 6),
    _DnsNewCfgDomainName_Type()
)
dnsNewCfgDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsNewCfgDomainName.setStatus("current")
_IpNwfCfg_ObjectIdentity = ObjectIdentity
ipNwfCfg = _IpNwfCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 10)
)
_IpNwfTableMax_Type = Integer32
_IpNwfTableMax_Object = MibScalar
ipNwfTableMax = _IpNwfTableMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 10, 1),
    _IpNwfTableMax_Type()
)
ipNwfTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNwfTableMax.setStatus("current")
_IpCurCfgNwfTable_Object = MibTable
ipCurCfgNwfTable = _IpCurCfgNwfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 10, 2)
)
if mibBuilder.loadTexts:
    ipCurCfgNwfTable.setStatus("current")
_IpCurCfgNwfEntry_Object = MibTableRow
ipCurCfgNwfEntry = _IpCurCfgNwfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 10, 2, 1)
)
ipCurCfgNwfEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipCurCfgNwfIndex"),
)
if mibBuilder.loadTexts:
    ipCurCfgNwfEntry.setStatus("current")
_IpCurCfgNwfIndex_Type = Integer32
_IpCurCfgNwfIndex_Object = MibTableColumn
ipCurCfgNwfIndex = _IpCurCfgNwfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 10, 2, 1, 1),
    _IpCurCfgNwfIndex_Type()
)
ipCurCfgNwfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgNwfIndex.setStatus("current")
_IpCurCfgNwfAddr_Type = IpAddress
_IpCurCfgNwfAddr_Object = MibTableColumn
ipCurCfgNwfAddr = _IpCurCfgNwfAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 10, 2, 1, 2),
    _IpCurCfgNwfAddr_Type()
)
ipCurCfgNwfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgNwfAddr.setStatus("current")
_IpCurCfgNwfMask_Type = IpAddress
_IpCurCfgNwfMask_Object = MibTableColumn
ipCurCfgNwfMask = _IpCurCfgNwfMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 10, 2, 1, 3),
    _IpCurCfgNwfMask_Type()
)
ipCurCfgNwfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgNwfMask.setStatus("current")


class _IpCurCfgNwfState_Type(Integer32):
    """Custom type ipCurCfgNwfState based on Integer32"""
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


_IpCurCfgNwfState_Type.__name__ = "Integer32"
_IpCurCfgNwfState_Object = MibTableColumn
ipCurCfgNwfState = _IpCurCfgNwfState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 10, 2, 1, 4),
    _IpCurCfgNwfState_Type()
)
ipCurCfgNwfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgNwfState.setStatus("current")
_IpNewCfgNwfTable_Object = MibTable
ipNewCfgNwfTable = _IpNewCfgNwfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 10, 3)
)
if mibBuilder.loadTexts:
    ipNewCfgNwfTable.setStatus("current")
_IpNewCfgNwfEntry_Object = MibTableRow
ipNewCfgNwfEntry = _IpNewCfgNwfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 10, 3, 1)
)
ipNewCfgNwfEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipNewCfgNwfIndex"),
)
if mibBuilder.loadTexts:
    ipNewCfgNwfEntry.setStatus("current")
_IpNewCfgNwfIndex_Type = Integer32
_IpNewCfgNwfIndex_Object = MibTableColumn
ipNewCfgNwfIndex = _IpNewCfgNwfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 10, 3, 1, 1),
    _IpNewCfgNwfIndex_Type()
)
ipNewCfgNwfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgNwfIndex.setStatus("current")
_IpNewCfgNwfAddr_Type = IpAddress
_IpNewCfgNwfAddr_Object = MibTableColumn
ipNewCfgNwfAddr = _IpNewCfgNwfAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 10, 3, 1, 2),
    _IpNewCfgNwfAddr_Type()
)
ipNewCfgNwfAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgNwfAddr.setStatus("current")
_IpNewCfgNwfMask_Type = IpAddress
_IpNewCfgNwfMask_Object = MibTableColumn
ipNewCfgNwfMask = _IpNewCfgNwfMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 10, 3, 1, 3),
    _IpNewCfgNwfMask_Type()
)
ipNewCfgNwfMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgNwfMask.setStatus("current")


class _IpNewCfgNwfState_Type(Integer32):
    """Custom type ipNewCfgNwfState based on Integer32"""
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


_IpNewCfgNwfState_Type.__name__ = "Integer32"
_IpNewCfgNwfState_Object = MibTableColumn
ipNewCfgNwfState = _IpNewCfgNwfState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 10, 3, 1, 4),
    _IpNewCfgNwfState_Type()
)
ipNewCfgNwfState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgNwfState.setStatus("current")


class _IpNewCfgNwfDelete_Type(Integer32):
    """Custom type ipNewCfgNwfDelete based on Integer32"""
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


_IpNewCfgNwfDelete_Type.__name__ = "Integer32"
_IpNewCfgNwfDelete_Object = MibTableColumn
ipNewCfgNwfDelete = _IpNewCfgNwfDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 10, 3, 1, 5),
    _IpNewCfgNwfDelete_Type()
)
ipNewCfgNwfDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgNwfDelete.setStatus("current")
_IpRmapCfg_ObjectIdentity = ObjectIdentity
ipRmapCfg = _IpRmapCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11)
)
_IpRmapTableMax_Type = Integer32
_IpRmapTableMax_Object = MibScalar
ipRmapTableMax = _IpRmapTableMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 1),
    _IpRmapTableMax_Type()
)
ipRmapTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRmapTableMax.setStatus("current")
_IpCurCfgRmapTable_Object = MibTable
ipCurCfgRmapTable = _IpCurCfgRmapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 2)
)
if mibBuilder.loadTexts:
    ipCurCfgRmapTable.setStatus("current")
_IpCurCfgRmapEntry_Object = MibTableRow
ipCurCfgRmapEntry = _IpCurCfgRmapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 2, 1)
)
ipCurCfgRmapEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipCurCfgRmapIndex"),
)
if mibBuilder.loadTexts:
    ipCurCfgRmapEntry.setStatus("current")
_IpCurCfgRmapIndex_Type = Integer32
_IpCurCfgRmapIndex_Object = MibTableColumn
ipCurCfgRmapIndex = _IpCurCfgRmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 2, 1, 1),
    _IpCurCfgRmapIndex_Type()
)
ipCurCfgRmapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgRmapIndex.setStatus("current")


class _IpCurCfgRmapLp_Type(Unsigned32):
    """Custom type ipCurCfgRmapLp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IpCurCfgRmapLp_Type.__name__ = "Unsigned32"
_IpCurCfgRmapLp_Object = MibTableColumn
ipCurCfgRmapLp = _IpCurCfgRmapLp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 2, 1, 2),
    _IpCurCfgRmapLp_Type()
)
ipCurCfgRmapLp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgRmapLp.setStatus("current")


class _IpCurCfgRmapMetric_Type(Unsigned32):
    """Custom type ipCurCfgRmapMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IpCurCfgRmapMetric_Type.__name__ = "Unsigned32"
_IpCurCfgRmapMetric_Object = MibTableColumn
ipCurCfgRmapMetric = _IpCurCfgRmapMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 2, 1, 3),
    _IpCurCfgRmapMetric_Type()
)
ipCurCfgRmapMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgRmapMetric.setStatus("current")


class _IpCurCfgRmapPrec_Type(Integer32):
    """Custom type ipCurCfgRmapPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpCurCfgRmapPrec_Type.__name__ = "Integer32"
_IpCurCfgRmapPrec_Object = MibTableColumn
ipCurCfgRmapPrec = _IpCurCfgRmapPrec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 2, 1, 4),
    _IpCurCfgRmapPrec_Type()
)
ipCurCfgRmapPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgRmapPrec.setStatus("current")


class _IpCurCfgRmapWeight_Type(Integer32):
    """Custom type ipCurCfgRmapWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpCurCfgRmapWeight_Type.__name__ = "Integer32"
_IpCurCfgRmapWeight_Object = MibTableColumn
ipCurCfgRmapWeight = _IpCurCfgRmapWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 2, 1, 5),
    _IpCurCfgRmapWeight_Type()
)
ipCurCfgRmapWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgRmapWeight.setStatus("current")


class _IpCurCfgRmapState_Type(Integer32):
    """Custom type ipCurCfgRmapState based on Integer32"""
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


_IpCurCfgRmapState_Type.__name__ = "Integer32"
_IpCurCfgRmapState_Object = MibTableColumn
ipCurCfgRmapState = _IpCurCfgRmapState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 2, 1, 6),
    _IpCurCfgRmapState_Type()
)
ipCurCfgRmapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgRmapState.setStatus("current")


class _IpCurCfgRmapAp_Type(DisplayString):
    """Custom type ipCurCfgRmapAp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_IpCurCfgRmapAp_Type.__name__ = "DisplayString"
_IpCurCfgRmapAp_Object = MibTableColumn
ipCurCfgRmapAp = _IpCurCfgRmapAp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 2, 1, 7),
    _IpCurCfgRmapAp_Type()
)
ipCurCfgRmapAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgRmapAp.setStatus("current")


class _IpCurCfgRmapMetricType_Type(Integer32):
    """Custom type ipCurCfgRmapMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("type1", 2),
          ("type2", 3))
    )


_IpCurCfgRmapMetricType_Type.__name__ = "Integer32"
_IpCurCfgRmapMetricType_Object = MibTableColumn
ipCurCfgRmapMetricType = _IpCurCfgRmapMetricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 2, 1, 8),
    _IpCurCfgRmapMetricType_Type()
)
ipCurCfgRmapMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgRmapMetricType.setStatus("current")
_IpNewCfgRmapTable_Object = MibTable
ipNewCfgRmapTable = _IpNewCfgRmapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 3)
)
if mibBuilder.loadTexts:
    ipNewCfgRmapTable.setStatus("current")
_IpNewCfgRmapEntry_Object = MibTableRow
ipNewCfgRmapEntry = _IpNewCfgRmapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 3, 1)
)
ipNewCfgRmapEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipNewCfgRmapIndex"),
)
if mibBuilder.loadTexts:
    ipNewCfgRmapEntry.setStatus("current")
_IpNewCfgRmapIndex_Type = Integer32
_IpNewCfgRmapIndex_Object = MibTableColumn
ipNewCfgRmapIndex = _IpNewCfgRmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 3, 1, 1),
    _IpNewCfgRmapIndex_Type()
)
ipNewCfgRmapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgRmapIndex.setStatus("current")


class _IpNewCfgRmapLp_Type(Unsigned32):
    """Custom type ipNewCfgRmapLp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IpNewCfgRmapLp_Type.__name__ = "Unsigned32"
_IpNewCfgRmapLp_Object = MibTableColumn
ipNewCfgRmapLp = _IpNewCfgRmapLp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 3, 1, 2),
    _IpNewCfgRmapLp_Type()
)
ipNewCfgRmapLp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgRmapLp.setStatus("current")


class _IpNewCfgRmapMetric_Type(Unsigned32):
    """Custom type ipNewCfgRmapMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IpNewCfgRmapMetric_Type.__name__ = "Unsigned32"
_IpNewCfgRmapMetric_Object = MibTableColumn
ipNewCfgRmapMetric = _IpNewCfgRmapMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 3, 1, 3),
    _IpNewCfgRmapMetric_Type()
)
ipNewCfgRmapMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgRmapMetric.setStatus("current")


class _IpNewCfgRmapPrec_Type(Integer32):
    """Custom type ipNewCfgRmapPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpNewCfgRmapPrec_Type.__name__ = "Integer32"
_IpNewCfgRmapPrec_Object = MibTableColumn
ipNewCfgRmapPrec = _IpNewCfgRmapPrec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 3, 1, 4),
    _IpNewCfgRmapPrec_Type()
)
ipNewCfgRmapPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgRmapPrec.setStatus("current")


class _IpNewCfgRmapWeight_Type(Integer32):
    """Custom type ipNewCfgRmapWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpNewCfgRmapWeight_Type.__name__ = "Integer32"
_IpNewCfgRmapWeight_Object = MibTableColumn
ipNewCfgRmapWeight = _IpNewCfgRmapWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 3, 1, 5),
    _IpNewCfgRmapWeight_Type()
)
ipNewCfgRmapWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgRmapWeight.setStatus("current")


class _IpNewCfgRmapState_Type(Integer32):
    """Custom type ipNewCfgRmapState based on Integer32"""
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


_IpNewCfgRmapState_Type.__name__ = "Integer32"
_IpNewCfgRmapState_Object = MibTableColumn
ipNewCfgRmapState = _IpNewCfgRmapState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 3, 1, 6),
    _IpNewCfgRmapState_Type()
)
ipNewCfgRmapState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgRmapState.setStatus("current")


class _IpNewCfgRmapAp_Type(DisplayString):
    """Custom type ipNewCfgRmapAp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_IpNewCfgRmapAp_Type.__name__ = "DisplayString"
_IpNewCfgRmapAp_Object = MibTableColumn
ipNewCfgRmapAp = _IpNewCfgRmapAp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 3, 1, 7),
    _IpNewCfgRmapAp_Type()
)
ipNewCfgRmapAp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgRmapAp.setStatus("current")


class _IpNewCfgRmapMetricType_Type(Integer32):
    """Custom type ipNewCfgRmapMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("type1", 2),
          ("type2", 3))
    )


_IpNewCfgRmapMetricType_Type.__name__ = "Integer32"
_IpNewCfgRmapMetricType_Object = MibTableColumn
ipNewCfgRmapMetricType = _IpNewCfgRmapMetricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 3, 1, 8),
    _IpNewCfgRmapMetricType_Type()
)
ipNewCfgRmapMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgRmapMetricType.setStatus("current")


class _IpNewCfgRmapDelete_Type(Integer32):
    """Custom type ipNewCfgRmapDelete based on Integer32"""
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


_IpNewCfgRmapDelete_Type.__name__ = "Integer32"
_IpNewCfgRmapDelete_Object = MibTableColumn
ipNewCfgRmapDelete = _IpNewCfgRmapDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 3, 1, 9),
    _IpNewCfgRmapDelete_Type()
)
ipNewCfgRmapDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgRmapDelete.setStatus("current")
_IpAlistTableMax_Type = Integer32
_IpAlistTableMax_Object = MibScalar
ipAlistTableMax = _IpAlistTableMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 4),
    _IpAlistTableMax_Type()
)
ipAlistTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAlistTableMax.setStatus("current")
_IpCurCfgAlistTable_Object = MibTable
ipCurCfgAlistTable = _IpCurCfgAlistTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 5)
)
if mibBuilder.loadTexts:
    ipCurCfgAlistTable.setStatus("current")
_IpCurCfgAlistEntry_Object = MibTableRow
ipCurCfgAlistEntry = _IpCurCfgAlistEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 5, 1)
)
ipCurCfgAlistEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipCurCfgAlistRmapIndex"),
    (0, "BLADETYPE2-NETWORK-MIB", "ipCurCfgAlistIndex"),
)
if mibBuilder.loadTexts:
    ipCurCfgAlistEntry.setStatus("current")
_IpCurCfgAlistRmapIndex_Type = Integer32
_IpCurCfgAlistRmapIndex_Object = MibTableColumn
ipCurCfgAlistRmapIndex = _IpCurCfgAlistRmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 5, 1, 1),
    _IpCurCfgAlistRmapIndex_Type()
)
ipCurCfgAlistRmapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgAlistRmapIndex.setStatus("current")
_IpCurCfgAlistIndex_Type = Integer32
_IpCurCfgAlistIndex_Object = MibTableColumn
ipCurCfgAlistIndex = _IpCurCfgAlistIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 5, 1, 2),
    _IpCurCfgAlistIndex_Type()
)
ipCurCfgAlistIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgAlistIndex.setStatus("current")


class _IpCurCfgAlistNwf_Type(Integer32):
    """Custom type ipCurCfgAlistNwf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpCurCfgAlistNwf_Type.__name__ = "Integer32"
_IpCurCfgAlistNwf_Object = MibTableColumn
ipCurCfgAlistNwf = _IpCurCfgAlistNwf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 5, 1, 3),
    _IpCurCfgAlistNwf_Type()
)
ipCurCfgAlistNwf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgAlistNwf.setStatus("current")


class _IpCurCfgAlistMetric_Type(Unsigned32):
    """Custom type ipCurCfgAlistMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IpCurCfgAlistMetric_Type.__name__ = "Unsigned32"
_IpCurCfgAlistMetric_Object = MibTableColumn
ipCurCfgAlistMetric = _IpCurCfgAlistMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 5, 1, 4),
    _IpCurCfgAlistMetric_Type()
)
ipCurCfgAlistMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgAlistMetric.setStatus("current")


class _IpCurCfgAlistAction_Type(Integer32):
    """Custom type ipCurCfgAlistAction based on Integer32"""
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


_IpCurCfgAlistAction_Type.__name__ = "Integer32"
_IpCurCfgAlistAction_Object = MibTableColumn
ipCurCfgAlistAction = _IpCurCfgAlistAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 5, 1, 5),
    _IpCurCfgAlistAction_Type()
)
ipCurCfgAlistAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgAlistAction.setStatus("current")


class _IpCurCfgAlistState_Type(Integer32):
    """Custom type ipCurCfgAlistState based on Integer32"""
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


_IpCurCfgAlistState_Type.__name__ = "Integer32"
_IpCurCfgAlistState_Object = MibTableColumn
ipCurCfgAlistState = _IpCurCfgAlistState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 5, 1, 6),
    _IpCurCfgAlistState_Type()
)
ipCurCfgAlistState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgAlistState.setStatus("current")
_IpNewCfgAlistTable_Object = MibTable
ipNewCfgAlistTable = _IpNewCfgAlistTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 6)
)
if mibBuilder.loadTexts:
    ipNewCfgAlistTable.setStatus("current")
_IpNewCfgAlistEntry_Object = MibTableRow
ipNewCfgAlistEntry = _IpNewCfgAlistEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 6, 1)
)
ipNewCfgAlistEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipNewCfgAlistRmapIndex"),
    (0, "BLADETYPE2-NETWORK-MIB", "ipNewCfgAlistIndex"),
)
if mibBuilder.loadTexts:
    ipNewCfgAlistEntry.setStatus("current")
_IpNewCfgAlistRmapIndex_Type = Integer32
_IpNewCfgAlistRmapIndex_Object = MibTableColumn
ipNewCfgAlistRmapIndex = _IpNewCfgAlistRmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 6, 1, 1),
    _IpNewCfgAlistRmapIndex_Type()
)
ipNewCfgAlistRmapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgAlistRmapIndex.setStatus("current")
_IpNewCfgAlistIndex_Type = Integer32
_IpNewCfgAlistIndex_Object = MibTableColumn
ipNewCfgAlistIndex = _IpNewCfgAlistIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 6, 1, 2),
    _IpNewCfgAlistIndex_Type()
)
ipNewCfgAlistIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgAlistIndex.setStatus("current")


class _IpNewCfgAlistNwf_Type(Integer32):
    """Custom type ipNewCfgAlistNwf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpNewCfgAlistNwf_Type.__name__ = "Integer32"
_IpNewCfgAlistNwf_Object = MibTableColumn
ipNewCfgAlistNwf = _IpNewCfgAlistNwf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 6, 1, 3),
    _IpNewCfgAlistNwf_Type()
)
ipNewCfgAlistNwf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgAlistNwf.setStatus("current")


class _IpNewCfgAlistMetric_Type(Unsigned32):
    """Custom type ipNewCfgAlistMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IpNewCfgAlistMetric_Type.__name__ = "Unsigned32"
_IpNewCfgAlistMetric_Object = MibTableColumn
ipNewCfgAlistMetric = _IpNewCfgAlistMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 6, 1, 4),
    _IpNewCfgAlistMetric_Type()
)
ipNewCfgAlistMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgAlistMetric.setStatus("current")


class _IpNewCfgAlistAction_Type(Integer32):
    """Custom type ipNewCfgAlistAction based on Integer32"""
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


_IpNewCfgAlistAction_Type.__name__ = "Integer32"
_IpNewCfgAlistAction_Object = MibTableColumn
ipNewCfgAlistAction = _IpNewCfgAlistAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 6, 1, 5),
    _IpNewCfgAlistAction_Type()
)
ipNewCfgAlistAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgAlistAction.setStatus("current")


class _IpNewCfgAlistState_Type(Integer32):
    """Custom type ipNewCfgAlistState based on Integer32"""
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


_IpNewCfgAlistState_Type.__name__ = "Integer32"
_IpNewCfgAlistState_Object = MibTableColumn
ipNewCfgAlistState = _IpNewCfgAlistState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 6, 1, 6),
    _IpNewCfgAlistState_Type()
)
ipNewCfgAlistState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgAlistState.setStatus("current")


class _IpNewCfgAlistDelete_Type(Integer32):
    """Custom type ipNewCfgAlistDelete based on Integer32"""
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


_IpNewCfgAlistDelete_Type.__name__ = "Integer32"
_IpNewCfgAlistDelete_Object = MibTableColumn
ipNewCfgAlistDelete = _IpNewCfgAlistDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 6, 1, 7),
    _IpNewCfgAlistDelete_Type()
)
ipNewCfgAlistDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgAlistDelete.setStatus("current")
_IpAspathTableMax_Type = Integer32
_IpAspathTableMax_Object = MibScalar
ipAspathTableMax = _IpAspathTableMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 7),
    _IpAspathTableMax_Type()
)
ipAspathTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAspathTableMax.setStatus("current")
_IpCurCfgAspathTable_Object = MibTable
ipCurCfgAspathTable = _IpCurCfgAspathTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 8)
)
if mibBuilder.loadTexts:
    ipCurCfgAspathTable.setStatus("current")
_IpCurCfgAspathEntry_Object = MibTableRow
ipCurCfgAspathEntry = _IpCurCfgAspathEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 8, 1)
)
ipCurCfgAspathEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipCurCfgAspathRmapIndex"),
    (0, "BLADETYPE2-NETWORK-MIB", "ipCurCfgAlistIndex"),
)
if mibBuilder.loadTexts:
    ipCurCfgAspathEntry.setStatus("current")
_IpCurCfgAspathRmapIndex_Type = Integer32
_IpCurCfgAspathRmapIndex_Object = MibTableColumn
ipCurCfgAspathRmapIndex = _IpCurCfgAspathRmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 8, 1, 1),
    _IpCurCfgAspathRmapIndex_Type()
)
ipCurCfgAspathRmapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgAspathRmapIndex.setStatus("current")
_IpCurCfgAspathIndex_Type = Integer32
_IpCurCfgAspathIndex_Object = MibTableColumn
ipCurCfgAspathIndex = _IpCurCfgAspathIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 8, 1, 2),
    _IpCurCfgAspathIndex_Type()
)
ipCurCfgAspathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgAspathIndex.setStatus("current")


class _IpCurCfgAspathAS_Type(Integer32):
    """Custom type ipCurCfgAspathAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpCurCfgAspathAS_Type.__name__ = "Integer32"
_IpCurCfgAspathAS_Object = MibTableColumn
ipCurCfgAspathAS = _IpCurCfgAspathAS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 8, 1, 3),
    _IpCurCfgAspathAS_Type()
)
ipCurCfgAspathAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgAspathAS.setStatus("current")


class _IpCurCfgAspathAction_Type(Integer32):
    """Custom type ipCurCfgAspathAction based on Integer32"""
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


_IpCurCfgAspathAction_Type.__name__ = "Integer32"
_IpCurCfgAspathAction_Object = MibTableColumn
ipCurCfgAspathAction = _IpCurCfgAspathAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 8, 1, 4),
    _IpCurCfgAspathAction_Type()
)
ipCurCfgAspathAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgAspathAction.setStatus("current")


class _IpCurCfgAspathState_Type(Integer32):
    """Custom type ipCurCfgAspathState based on Integer32"""
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


_IpCurCfgAspathState_Type.__name__ = "Integer32"
_IpCurCfgAspathState_Object = MibTableColumn
ipCurCfgAspathState = _IpCurCfgAspathState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 8, 1, 5),
    _IpCurCfgAspathState_Type()
)
ipCurCfgAspathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgAspathState.setStatus("current")
_IpNewCfgAspathTable_Object = MibTable
ipNewCfgAspathTable = _IpNewCfgAspathTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 9)
)
if mibBuilder.loadTexts:
    ipNewCfgAspathTable.setStatus("current")
_IpNewCfgAspathEntry_Object = MibTableRow
ipNewCfgAspathEntry = _IpNewCfgAspathEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 9, 1)
)
ipNewCfgAspathEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipNewCfgAspathRmapIndex"),
    (0, "BLADETYPE2-NETWORK-MIB", "ipNewCfgAspathIndex"),
)
if mibBuilder.loadTexts:
    ipNewCfgAspathEntry.setStatus("current")
_IpNewCfgAspathRmapIndex_Type = Integer32
_IpNewCfgAspathRmapIndex_Object = MibTableColumn
ipNewCfgAspathRmapIndex = _IpNewCfgAspathRmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 9, 1, 1),
    _IpNewCfgAspathRmapIndex_Type()
)
ipNewCfgAspathRmapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgAspathRmapIndex.setStatus("current")
_IpNewCfgAspathIndex_Type = Integer32
_IpNewCfgAspathIndex_Object = MibTableColumn
ipNewCfgAspathIndex = _IpNewCfgAspathIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 9, 1, 2),
    _IpNewCfgAspathIndex_Type()
)
ipNewCfgAspathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgAspathIndex.setStatus("current")


class _IpNewCfgAspathAS_Type(Integer32):
    """Custom type ipNewCfgAspathAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpNewCfgAspathAS_Type.__name__ = "Integer32"
_IpNewCfgAspathAS_Object = MibTableColumn
ipNewCfgAspathAS = _IpNewCfgAspathAS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 9, 1, 3),
    _IpNewCfgAspathAS_Type()
)
ipNewCfgAspathAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgAspathAS.setStatus("current")


class _IpNewCfgAspathAction_Type(Integer32):
    """Custom type ipNewCfgAspathAction based on Integer32"""
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


_IpNewCfgAspathAction_Type.__name__ = "Integer32"
_IpNewCfgAspathAction_Object = MibTableColumn
ipNewCfgAspathAction = _IpNewCfgAspathAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 9, 1, 4),
    _IpNewCfgAspathAction_Type()
)
ipNewCfgAspathAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgAspathAction.setStatus("current")


class _IpNewCfgAspathState_Type(Integer32):
    """Custom type ipNewCfgAspathState based on Integer32"""
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


_IpNewCfgAspathState_Type.__name__ = "Integer32"
_IpNewCfgAspathState_Object = MibTableColumn
ipNewCfgAspathState = _IpNewCfgAspathState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 9, 1, 5),
    _IpNewCfgAspathState_Type()
)
ipNewCfgAspathState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgAspathState.setStatus("current")


class _IpNewCfgAspathDelete_Type(Integer32):
    """Custom type ipNewCfgAspathDelete based on Integer32"""
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


_IpNewCfgAspathDelete_Type.__name__ = "Integer32"
_IpNewCfgAspathDelete_Object = MibTableColumn
ipNewCfgAspathDelete = _IpNewCfgAspathDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 11, 9, 1, 6),
    _IpNewCfgAspathDelete_Type()
)
ipNewCfgAspathDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgAspathDelete.setStatus("current")
_OspfCfg_ObjectIdentity = ObjectIdentity
ospfCfg = _OspfCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13)
)
_OspfGeneral_ObjectIdentity = ObjectIdentity
ospfGeneral = _OspfGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 1)
)


class _OspfCurCfgDefaultRouteMetric_Type(Integer32):
    """Custom type ospfCurCfgDefaultRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OspfCurCfgDefaultRouteMetric_Type.__name__ = "Integer32"
_OspfCurCfgDefaultRouteMetric_Object = MibScalar
ospfCurCfgDefaultRouteMetric = _OspfCurCfgDefaultRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 1, 1),
    _OspfCurCfgDefaultRouteMetric_Type()
)
ospfCurCfgDefaultRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgDefaultRouteMetric.setStatus("current")


class _OspfNewCfgDefaultRouteMetric_Type(Integer32):
    """Custom type ospfNewCfgDefaultRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OspfNewCfgDefaultRouteMetric_Type.__name__ = "Integer32"
_OspfNewCfgDefaultRouteMetric_Object = MibScalar
ospfNewCfgDefaultRouteMetric = _OspfNewCfgDefaultRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 1, 2),
    _OspfNewCfgDefaultRouteMetric_Type()
)
ospfNewCfgDefaultRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgDefaultRouteMetric.setStatus("current")


class _OspfCurCfgDefaultRouteMetricType_Type(Integer32):
    """Custom type ospfCurCfgDefaultRouteMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("type1", 2),
          ("type2", 3))
    )


_OspfCurCfgDefaultRouteMetricType_Type.__name__ = "Integer32"
_OspfCurCfgDefaultRouteMetricType_Object = MibScalar
ospfCurCfgDefaultRouteMetricType = _OspfCurCfgDefaultRouteMetricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 1, 3),
    _OspfCurCfgDefaultRouteMetricType_Type()
)
ospfCurCfgDefaultRouteMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgDefaultRouteMetricType.setStatus("current")


class _OspfNewCfgDefaultRouteMetricType_Type(Integer32):
    """Custom type ospfNewCfgDefaultRouteMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("type1", 2),
          ("type2", 3))
    )


_OspfNewCfgDefaultRouteMetricType_Type.__name__ = "Integer32"
_OspfNewCfgDefaultRouteMetricType_Object = MibScalar
ospfNewCfgDefaultRouteMetricType = _OspfNewCfgDefaultRouteMetricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 1, 4),
    _OspfNewCfgDefaultRouteMetricType_Type()
)
ospfNewCfgDefaultRouteMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgDefaultRouteMetricType.setStatus("current")
_OspfIntfTableMaxSize_Type = Integer32
_OspfIntfTableMaxSize_Object = MibScalar
ospfIntfTableMaxSize = _OspfIntfTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 1, 5),
    _OspfIntfTableMaxSize_Type()
)
ospfIntfTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTableMaxSize.setStatus("current")
_OspfAreaTableMaxSize_Type = Integer32
_OspfAreaTableMaxSize_Object = MibScalar
ospfAreaTableMaxSize = _OspfAreaTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 1, 6),
    _OspfAreaTableMaxSize_Type()
)
ospfAreaTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTableMaxSize.setStatus("current")
_OspfRangeTableMaxSize_Type = Integer32
_OspfRangeTableMaxSize_Object = MibScalar
ospfRangeTableMaxSize = _OspfRangeTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 1, 7),
    _OspfRangeTableMaxSize_Type()
)
ospfRangeTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRangeTableMaxSize.setStatus("current")
_OspfVirtIntfTableMaxSize_Type = Integer32
_OspfVirtIntfTableMaxSize_Object = MibScalar
ospfVirtIntfTableMaxSize = _OspfVirtIntfTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 1, 8),
    _OspfVirtIntfTableMaxSize_Type()
)
ospfVirtIntfTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtIntfTableMaxSize.setStatus("current")
_OspfHostTableMaxSize_Type = Integer32
_OspfHostTableMaxSize_Object = MibScalar
ospfHostTableMaxSize = _OspfHostTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 1, 9),
    _OspfHostTableMaxSize_Type()
)
ospfHostTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfHostTableMaxSize.setStatus("current")


class _OspfCurCfgState_Type(Integer32):
    """Custom type ospfCurCfgState based on Integer32"""
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


_OspfCurCfgState_Type.__name__ = "Integer32"
_OspfCurCfgState_Object = MibScalar
ospfCurCfgState = _OspfCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 1, 10),
    _OspfCurCfgState_Type()
)
ospfCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgState.setStatus("current")


class _OspfNewCfgState_Type(Integer32):
    """Custom type ospfNewCfgState based on Integer32"""
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


_OspfNewCfgState_Type.__name__ = "Integer32"
_OspfNewCfgState_Object = MibScalar
ospfNewCfgState = _OspfNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 1, 11),
    _OspfNewCfgState_Type()
)
ospfNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgState.setStatus("current")
_OspfCurCfgAreaTable_Object = MibTable
ospfCurCfgAreaTable = _OspfCurCfgAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 2)
)
if mibBuilder.loadTexts:
    ospfCurCfgAreaTable.setStatus("current")
_OspfCurCfgAreaEntry_Object = MibTableRow
ospfCurCfgAreaEntry = _OspfCurCfgAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 2, 1)
)
ospfCurCfgAreaEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfCurCfgAreaIndex"),
)
if mibBuilder.loadTexts:
    ospfCurCfgAreaEntry.setStatus("current")
_OspfCurCfgAreaIndex_Type = Integer32
_OspfCurCfgAreaIndex_Object = MibTableColumn
ospfCurCfgAreaIndex = _OspfCurCfgAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 2, 1, 1),
    _OspfCurCfgAreaIndex_Type()
)
ospfCurCfgAreaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgAreaIndex.setStatus("current")
_OspfCurCfgAreaId_Type = IpAddress
_OspfCurCfgAreaId_Object = MibTableColumn
ospfCurCfgAreaId = _OspfCurCfgAreaId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 2, 1, 2),
    _OspfCurCfgAreaId_Type()
)
ospfCurCfgAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgAreaId.setStatus("current")


class _OspfCurCfgAreaSpfInterval_Type(Integer32):
    """Custom type ospfCurCfgAreaSpfInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OspfCurCfgAreaSpfInterval_Type.__name__ = "Integer32"
_OspfCurCfgAreaSpfInterval_Object = MibTableColumn
ospfCurCfgAreaSpfInterval = _OspfCurCfgAreaSpfInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 2, 1, 3),
    _OspfCurCfgAreaSpfInterval_Type()
)
ospfCurCfgAreaSpfInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgAreaSpfInterval.setStatus("current")


class _OspfCurCfgAreaAuthType_Type(Integer32):
    """Custom type ospfCurCfgAreaAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("none", 1),
          ("password", 2))
    )


_OspfCurCfgAreaAuthType_Type.__name__ = "Integer32"
_OspfCurCfgAreaAuthType_Object = MibTableColumn
ospfCurCfgAreaAuthType = _OspfCurCfgAreaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 2, 1, 4),
    _OspfCurCfgAreaAuthType_Type()
)
ospfCurCfgAreaAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgAreaAuthType.setStatus("current")


class _OspfCurCfgAreaType_Type(Integer32):
    """Custom type ospfCurCfgAreaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nssa", 2),
          ("stub", 1),
          ("transit", 0))
    )


_OspfCurCfgAreaType_Type.__name__ = "Integer32"
_OspfCurCfgAreaType_Object = MibTableColumn
ospfCurCfgAreaType = _OspfCurCfgAreaType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 2, 1, 5),
    _OspfCurCfgAreaType_Type()
)
ospfCurCfgAreaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgAreaType.setStatus("current")


class _OspfCurCfgAreaMetric_Type(Integer32):
    """Custom type ospfCurCfgAreaMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfCurCfgAreaMetric_Type.__name__ = "Integer32"
_OspfCurCfgAreaMetric_Object = MibTableColumn
ospfCurCfgAreaMetric = _OspfCurCfgAreaMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 2, 1, 6),
    _OspfCurCfgAreaMetric_Type()
)
ospfCurCfgAreaMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgAreaMetric.setStatus("current")


class _OspfCurCfgAreaStatus_Type(Integer32):
    """Custom type ospfCurCfgAreaStatus based on Integer32"""
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


_OspfCurCfgAreaStatus_Type.__name__ = "Integer32"
_OspfCurCfgAreaStatus_Object = MibTableColumn
ospfCurCfgAreaStatus = _OspfCurCfgAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 2, 1, 7),
    _OspfCurCfgAreaStatus_Type()
)
ospfCurCfgAreaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgAreaStatus.setStatus("current")
_OspfNewCfgAreaTable_Object = MibTable
ospfNewCfgAreaTable = _OspfNewCfgAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 3)
)
if mibBuilder.loadTexts:
    ospfNewCfgAreaTable.setStatus("current")
_OspfNewCfgAreaEntry_Object = MibTableRow
ospfNewCfgAreaEntry = _OspfNewCfgAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 3, 1)
)
ospfNewCfgAreaEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfNewCfgAreaIndex"),
)
if mibBuilder.loadTexts:
    ospfNewCfgAreaEntry.setStatus("current")
_OspfNewCfgAreaIndex_Type = Integer32
_OspfNewCfgAreaIndex_Object = MibTableColumn
ospfNewCfgAreaIndex = _OspfNewCfgAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 3, 1, 1),
    _OspfNewCfgAreaIndex_Type()
)
ospfNewCfgAreaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgAreaIndex.setStatus("current")
_OspfNewCfgAreaId_Type = IpAddress
_OspfNewCfgAreaId_Object = MibTableColumn
ospfNewCfgAreaId = _OspfNewCfgAreaId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 3, 1, 2),
    _OspfNewCfgAreaId_Type()
)
ospfNewCfgAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgAreaId.setStatus("current")


class _OspfNewCfgAreaSpfInterval_Type(Integer32):
    """Custom type ospfNewCfgAreaSpfInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OspfNewCfgAreaSpfInterval_Type.__name__ = "Integer32"
_OspfNewCfgAreaSpfInterval_Object = MibTableColumn
ospfNewCfgAreaSpfInterval = _OspfNewCfgAreaSpfInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 3, 1, 3),
    _OspfNewCfgAreaSpfInterval_Type()
)
ospfNewCfgAreaSpfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgAreaSpfInterval.setStatus("current")


class _OspfNewCfgAreaAuthType_Type(Integer32):
    """Custom type ospfNewCfgAreaAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("none", 1),
          ("password", 2))
    )


_OspfNewCfgAreaAuthType_Type.__name__ = "Integer32"
_OspfNewCfgAreaAuthType_Object = MibTableColumn
ospfNewCfgAreaAuthType = _OspfNewCfgAreaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 3, 1, 4),
    _OspfNewCfgAreaAuthType_Type()
)
ospfNewCfgAreaAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgAreaAuthType.setStatus("current")


class _OspfNewCfgAreaType_Type(Integer32):
    """Custom type ospfNewCfgAreaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nssa", 2),
          ("stub", 1),
          ("transit", 0))
    )


_OspfNewCfgAreaType_Type.__name__ = "Integer32"
_OspfNewCfgAreaType_Object = MibTableColumn
ospfNewCfgAreaType = _OspfNewCfgAreaType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 3, 1, 5),
    _OspfNewCfgAreaType_Type()
)
ospfNewCfgAreaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgAreaType.setStatus("current")


class _OspfNewCfgAreaMetric_Type(Integer32):
    """Custom type ospfNewCfgAreaMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfNewCfgAreaMetric_Type.__name__ = "Integer32"
_OspfNewCfgAreaMetric_Object = MibTableColumn
ospfNewCfgAreaMetric = _OspfNewCfgAreaMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 3, 1, 6),
    _OspfNewCfgAreaMetric_Type()
)
ospfNewCfgAreaMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgAreaMetric.setStatus("current")


class _OspfNewCfgAreaStatus_Type(Integer32):
    """Custom type ospfNewCfgAreaStatus based on Integer32"""
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


_OspfNewCfgAreaStatus_Type.__name__ = "Integer32"
_OspfNewCfgAreaStatus_Object = MibTableColumn
ospfNewCfgAreaStatus = _OspfNewCfgAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 3, 1, 7),
    _OspfNewCfgAreaStatus_Type()
)
ospfNewCfgAreaStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgAreaStatus.setStatus("current")


class _OspfNewCfgAreaDelete_Type(Integer32):
    """Custom type ospfNewCfgAreaDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_OspfNewCfgAreaDelete_Type.__name__ = "Integer32"
_OspfNewCfgAreaDelete_Object = MibTableColumn
ospfNewCfgAreaDelete = _OspfNewCfgAreaDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 3, 1, 8),
    _OspfNewCfgAreaDelete_Type()
)
ospfNewCfgAreaDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgAreaDelete.setStatus("current")
_OspfRouteRedistribution_ObjectIdentity = ObjectIdentity
ospfRouteRedistribution = _OspfRouteRedistribution_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4)
)
_OspfRedistributeStatic_ObjectIdentity = ObjectIdentity
ospfRedistributeStatic = _OspfRedistributeStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 1)
)


class _OspfCurCfgStaticMetric_Type(Integer32):
    """Custom type ospfCurCfgStaticMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OspfCurCfgStaticMetric_Type.__name__ = "Integer32"
_OspfCurCfgStaticMetric_Object = MibScalar
ospfCurCfgStaticMetric = _OspfCurCfgStaticMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 1, 1),
    _OspfCurCfgStaticMetric_Type()
)
ospfCurCfgStaticMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgStaticMetric.setStatus("current")


class _OspfNewCfgStaticMetric_Type(Integer32):
    """Custom type ospfNewCfgStaticMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OspfNewCfgStaticMetric_Type.__name__ = "Integer32"
_OspfNewCfgStaticMetric_Object = MibScalar
ospfNewCfgStaticMetric = _OspfNewCfgStaticMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 1, 2),
    _OspfNewCfgStaticMetric_Type()
)
ospfNewCfgStaticMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgStaticMetric.setStatus("current")


class _OspfCurCfgStaticMetricType_Type(Integer32):
    """Custom type ospfCurCfgStaticMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("type1", 2),
          ("type2", 3))
    )


_OspfCurCfgStaticMetricType_Type.__name__ = "Integer32"
_OspfCurCfgStaticMetricType_Object = MibScalar
ospfCurCfgStaticMetricType = _OspfCurCfgStaticMetricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 1, 3),
    _OspfCurCfgStaticMetricType_Type()
)
ospfCurCfgStaticMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgStaticMetricType.setStatus("current")


class _OspfNewCfgStaticMetricType_Type(Integer32):
    """Custom type ospfNewCfgStaticMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("type1", 2),
          ("type2", 3))
    )


_OspfNewCfgStaticMetricType_Type.__name__ = "Integer32"
_OspfNewCfgStaticMetricType_Object = MibScalar
ospfNewCfgStaticMetricType = _OspfNewCfgStaticMetricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 1, 4),
    _OspfNewCfgStaticMetricType_Type()
)
ospfNewCfgStaticMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgStaticMetricType.setStatus("current")
_OspfCurCfgStaticOutRmapList_Type = OctetString
_OspfCurCfgStaticOutRmapList_Object = MibScalar
ospfCurCfgStaticOutRmapList = _OspfCurCfgStaticOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 1, 5),
    _OspfCurCfgStaticOutRmapList_Type()
)
ospfCurCfgStaticOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgStaticOutRmapList.setStatus("current")
_OspfNewCfgStaticOutRmapList_Type = OctetString
_OspfNewCfgStaticOutRmapList_Object = MibScalar
ospfNewCfgStaticOutRmapList = _OspfNewCfgStaticOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 1, 6),
    _OspfNewCfgStaticOutRmapList_Type()
)
ospfNewCfgStaticOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgStaticOutRmapList.setStatus("current")
_OspfNewCfgStaticAddOutRmap_Type = Integer32
_OspfNewCfgStaticAddOutRmap_Object = MibScalar
ospfNewCfgStaticAddOutRmap = _OspfNewCfgStaticAddOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 1, 7),
    _OspfNewCfgStaticAddOutRmap_Type()
)
ospfNewCfgStaticAddOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgStaticAddOutRmap.setStatus("current")
_OspfNewCfgStaticRemoveOutRmap_Type = Integer32
_OspfNewCfgStaticRemoveOutRmap_Object = MibScalar
ospfNewCfgStaticRemoveOutRmap = _OspfNewCfgStaticRemoveOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 1, 8),
    _OspfNewCfgStaticRemoveOutRmap_Type()
)
ospfNewCfgStaticRemoveOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgStaticRemoveOutRmap.setStatus("current")
_OspfRedistributeFixed_ObjectIdentity = ObjectIdentity
ospfRedistributeFixed = _OspfRedistributeFixed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 4)
)


class _OspfCurCfgFixedMetric_Type(Integer32):
    """Custom type ospfCurCfgFixedMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OspfCurCfgFixedMetric_Type.__name__ = "Integer32"
_OspfCurCfgFixedMetric_Object = MibScalar
ospfCurCfgFixedMetric = _OspfCurCfgFixedMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 4, 1),
    _OspfCurCfgFixedMetric_Type()
)
ospfCurCfgFixedMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgFixedMetric.setStatus("current")


class _OspfNewCfgFixedMetric_Type(Integer32):
    """Custom type ospfNewCfgFixedMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OspfNewCfgFixedMetric_Type.__name__ = "Integer32"
_OspfNewCfgFixedMetric_Object = MibScalar
ospfNewCfgFixedMetric = _OspfNewCfgFixedMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 4, 2),
    _OspfNewCfgFixedMetric_Type()
)
ospfNewCfgFixedMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgFixedMetric.setStatus("current")


class _OspfCurCfgFixedMetricType_Type(Integer32):
    """Custom type ospfCurCfgFixedMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("type1", 2),
          ("type2", 3))
    )


_OspfCurCfgFixedMetricType_Type.__name__ = "Integer32"
_OspfCurCfgFixedMetricType_Object = MibScalar
ospfCurCfgFixedMetricType = _OspfCurCfgFixedMetricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 4, 3),
    _OspfCurCfgFixedMetricType_Type()
)
ospfCurCfgFixedMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgFixedMetricType.setStatus("current")


class _OspfNewCfgFixedMetricType_Type(Integer32):
    """Custom type ospfNewCfgFixedMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("type1", 2),
          ("type2", 3))
    )


_OspfNewCfgFixedMetricType_Type.__name__ = "Integer32"
_OspfNewCfgFixedMetricType_Object = MibScalar
ospfNewCfgFixedMetricType = _OspfNewCfgFixedMetricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 4, 4),
    _OspfNewCfgFixedMetricType_Type()
)
ospfNewCfgFixedMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgFixedMetricType.setStatus("current")
_OspfCurCfgFixedOutRmapList_Type = OctetString
_OspfCurCfgFixedOutRmapList_Object = MibScalar
ospfCurCfgFixedOutRmapList = _OspfCurCfgFixedOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 4, 5),
    _OspfCurCfgFixedOutRmapList_Type()
)
ospfCurCfgFixedOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgFixedOutRmapList.setStatus("current")
_OspfNewCfgFixedOutRmapList_Type = OctetString
_OspfNewCfgFixedOutRmapList_Object = MibScalar
ospfNewCfgFixedOutRmapList = _OspfNewCfgFixedOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 4, 6),
    _OspfNewCfgFixedOutRmapList_Type()
)
ospfNewCfgFixedOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgFixedOutRmapList.setStatus("current")
_OspfNewCfgFixedAddOutRmap_Type = Integer32
_OspfNewCfgFixedAddOutRmap_Object = MibScalar
ospfNewCfgFixedAddOutRmap = _OspfNewCfgFixedAddOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 4, 7),
    _OspfNewCfgFixedAddOutRmap_Type()
)
ospfNewCfgFixedAddOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgFixedAddOutRmap.setStatus("current")
_OspfNewCfgFixedRemoveOutRmap_Type = Integer32
_OspfNewCfgFixedRemoveOutRmap_Object = MibScalar
ospfNewCfgFixedRemoveOutRmap = _OspfNewCfgFixedRemoveOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 4, 8),
    _OspfNewCfgFixedRemoveOutRmap_Type()
)
ospfNewCfgFixedRemoveOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgFixedRemoveOutRmap.setStatus("current")
_OspfRedistributeRip_ObjectIdentity = ObjectIdentity
ospfRedistributeRip = _OspfRedistributeRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 5)
)


class _OspfCurCfgRipMetric_Type(Integer32):
    """Custom type ospfCurCfgRipMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OspfCurCfgRipMetric_Type.__name__ = "Integer32"
_OspfCurCfgRipMetric_Object = MibScalar
ospfCurCfgRipMetric = _OspfCurCfgRipMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 5, 1),
    _OspfCurCfgRipMetric_Type()
)
ospfCurCfgRipMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgRipMetric.setStatus("current")


class _OspfNewCfgRipMetric_Type(Integer32):
    """Custom type ospfNewCfgRipMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OspfNewCfgRipMetric_Type.__name__ = "Integer32"
_OspfNewCfgRipMetric_Object = MibScalar
ospfNewCfgRipMetric = _OspfNewCfgRipMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 5, 2),
    _OspfNewCfgRipMetric_Type()
)
ospfNewCfgRipMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgRipMetric.setStatus("current")


class _OspfCurCfgRipMetricType_Type(Integer32):
    """Custom type ospfCurCfgRipMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("type1", 2),
          ("type2", 3))
    )


_OspfCurCfgRipMetricType_Type.__name__ = "Integer32"
_OspfCurCfgRipMetricType_Object = MibScalar
ospfCurCfgRipMetricType = _OspfCurCfgRipMetricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 5, 3),
    _OspfCurCfgRipMetricType_Type()
)
ospfCurCfgRipMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgRipMetricType.setStatus("current")


class _OspfNewCfgRipMetricType_Type(Integer32):
    """Custom type ospfNewCfgRipMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("type1", 2),
          ("type2", 3))
    )


_OspfNewCfgRipMetricType_Type.__name__ = "Integer32"
_OspfNewCfgRipMetricType_Object = MibScalar
ospfNewCfgRipMetricType = _OspfNewCfgRipMetricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 5, 4),
    _OspfNewCfgRipMetricType_Type()
)
ospfNewCfgRipMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgRipMetricType.setStatus("current")
_OspfCurCfgRipOutRmapList_Type = OctetString
_OspfCurCfgRipOutRmapList_Object = MibScalar
ospfCurCfgRipOutRmapList = _OspfCurCfgRipOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 5, 5),
    _OspfCurCfgRipOutRmapList_Type()
)
ospfCurCfgRipOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgRipOutRmapList.setStatus("current")
_OspfNewCfgRipOutRmapList_Type = OctetString
_OspfNewCfgRipOutRmapList_Object = MibScalar
ospfNewCfgRipOutRmapList = _OspfNewCfgRipOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 5, 6),
    _OspfNewCfgRipOutRmapList_Type()
)
ospfNewCfgRipOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgRipOutRmapList.setStatus("current")
_OspfNewCfgRipAddOutRmap_Type = Integer32
_OspfNewCfgRipAddOutRmap_Object = MibScalar
ospfNewCfgRipAddOutRmap = _OspfNewCfgRipAddOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 5, 7),
    _OspfNewCfgRipAddOutRmap_Type()
)
ospfNewCfgRipAddOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgRipAddOutRmap.setStatus("current")
_OspfNewCfgRipRemoveOutRmap_Type = Integer32
_OspfNewCfgRipRemoveOutRmap_Object = MibScalar
ospfNewCfgRipRemoveOutRmap = _OspfNewCfgRipRemoveOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 4, 5, 8),
    _OspfNewCfgRipRemoveOutRmap_Type()
)
ospfNewCfgRipRemoveOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgRipRemoveOutRmap.setStatus("current")
_OspfCurCfgMdkeyTable_Object = MibTable
ospfCurCfgMdkeyTable = _OspfCurCfgMdkeyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 5)
)
if mibBuilder.loadTexts:
    ospfCurCfgMdkeyTable.setStatus("current")
_OspfCurCfgMdkeyEntry_Object = MibTableRow
ospfCurCfgMdkeyEntry = _OspfCurCfgMdkeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 5, 1)
)
ospfCurCfgMdkeyEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfCurCfgMdkeyIndex"),
)
if mibBuilder.loadTexts:
    ospfCurCfgMdkeyEntry.setStatus("current")
_OspfCurCfgMdkeyIndex_Type = Integer32
_OspfCurCfgMdkeyIndex_Object = MibTableColumn
ospfCurCfgMdkeyIndex = _OspfCurCfgMdkeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 5, 1, 1),
    _OspfCurCfgMdkeyIndex_Type()
)
ospfCurCfgMdkeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgMdkeyIndex.setStatus("current")


class _OspfCurCfgMdkeyKey_Type(DisplayString):
    """Custom type ospfCurCfgMdkeyKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OspfCurCfgMdkeyKey_Type.__name__ = "DisplayString"
_OspfCurCfgMdkeyKey_Object = MibTableColumn
ospfCurCfgMdkeyKey = _OspfCurCfgMdkeyKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 5, 1, 2),
    _OspfCurCfgMdkeyKey_Type()
)
ospfCurCfgMdkeyKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgMdkeyKey.setStatus("current")
_OspfNewCfgMdkeyTable_Object = MibTable
ospfNewCfgMdkeyTable = _OspfNewCfgMdkeyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 6)
)
if mibBuilder.loadTexts:
    ospfNewCfgMdkeyTable.setStatus("current")
_OspfNewCfgMdkeyEntry_Object = MibTableRow
ospfNewCfgMdkeyEntry = _OspfNewCfgMdkeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 6, 1)
)
ospfNewCfgMdkeyEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfNewCfgMdkeyIndex"),
)
if mibBuilder.loadTexts:
    ospfNewCfgMdkeyEntry.setStatus("current")
_OspfNewCfgMdkeyIndex_Type = Integer32
_OspfNewCfgMdkeyIndex_Object = MibTableColumn
ospfNewCfgMdkeyIndex = _OspfNewCfgMdkeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 6, 1, 1),
    _OspfNewCfgMdkeyIndex_Type()
)
ospfNewCfgMdkeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgMdkeyIndex.setStatus("current")


class _OspfNewCfgMdkeyKey_Type(DisplayString):
    """Custom type ospfNewCfgMdkeyKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OspfNewCfgMdkeyKey_Type.__name__ = "DisplayString"
_OspfNewCfgMdkeyKey_Object = MibTableColumn
ospfNewCfgMdkeyKey = _OspfNewCfgMdkeyKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 6, 1, 2),
    _OspfNewCfgMdkeyKey_Type()
)
ospfNewCfgMdkeyKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgMdkeyKey.setStatus("current")


class _OspfNewCfgMdkeyDelete_Type(Integer32):
    """Custom type ospfNewCfgMdkeyDelete based on Integer32"""
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


_OspfNewCfgMdkeyDelete_Type.__name__ = "Integer32"
_OspfNewCfgMdkeyDelete_Object = MibTableColumn
ospfNewCfgMdkeyDelete = _OspfNewCfgMdkeyDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 6, 1, 3),
    _OspfNewCfgMdkeyDelete_Type()
)
ospfNewCfgMdkeyDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgMdkeyDelete.setStatus("current")
_OspfCurCfgIntfTable_Object = MibTable
ospfCurCfgIntfTable = _OspfCurCfgIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 7)
)
if mibBuilder.loadTexts:
    ospfCurCfgIntfTable.setStatus("current")
_OspfCurCfgIntfEntry_Object = MibTableRow
ospfCurCfgIntfEntry = _OspfCurCfgIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 7, 1)
)
ospfCurCfgIntfEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfCurCfgIntfIndex"),
)
if mibBuilder.loadTexts:
    ospfCurCfgIntfEntry.setStatus("current")
_OspfCurCfgIntfIndex_Type = Integer32
_OspfCurCfgIntfIndex_Object = MibTableColumn
ospfCurCfgIntfIndex = _OspfCurCfgIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 7, 1, 1),
    _OspfCurCfgIntfIndex_Type()
)
ospfCurCfgIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfIndex.setStatus("current")
_OspfCurCfgIntfId_Type = IpAddress
_OspfCurCfgIntfId_Object = MibTableColumn
ospfCurCfgIntfId = _OspfCurCfgIntfId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 7, 1, 2),
    _OspfCurCfgIntfId_Type()
)
ospfCurCfgIntfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfId.setStatus("current")


class _OspfCurCfgIntfArea_Type(Integer32):
    """Custom type ospfCurCfgIntfArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_OspfCurCfgIntfArea_Type.__name__ = "Integer32"
_OspfCurCfgIntfArea_Object = MibTableColumn
ospfCurCfgIntfArea = _OspfCurCfgIntfArea_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 7, 1, 3),
    _OspfCurCfgIntfArea_Type()
)
ospfCurCfgIntfArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfArea.setStatus("current")


class _OspfCurCfgIntfMdkey_Type(Integer32):
    """Custom type ospfCurCfgIntfMdkey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OspfCurCfgIntfMdkey_Type.__name__ = "Integer32"
_OspfCurCfgIntfMdkey_Object = MibTableColumn
ospfCurCfgIntfMdkey = _OspfCurCfgIntfMdkey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 7, 1, 4),
    _OspfCurCfgIntfMdkey_Type()
)
ospfCurCfgIntfMdkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfMdkey.setStatus("current")


class _OspfCurCfgIntfCost_Type(Integer32):
    """Custom type ospfCurCfgIntfCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfCurCfgIntfCost_Type.__name__ = "Integer32"
_OspfCurCfgIntfCost_Object = MibTableColumn
ospfCurCfgIntfCost = _OspfCurCfgIntfCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 7, 1, 5),
    _OspfCurCfgIntfCost_Type()
)
ospfCurCfgIntfCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfCost.setStatus("current")


class _OspfCurCfgIntfPrio_Type(Integer32):
    """Custom type ospfCurCfgIntfPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OspfCurCfgIntfPrio_Type.__name__ = "Integer32"
_OspfCurCfgIntfPrio_Object = MibTableColumn
ospfCurCfgIntfPrio = _OspfCurCfgIntfPrio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 7, 1, 6),
    _OspfCurCfgIntfPrio_Type()
)
ospfCurCfgIntfPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfPrio.setStatus("current")


class _OspfCurCfgIntfHello_Type(Integer32):
    """Custom type ospfCurCfgIntfHello based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfCurCfgIntfHello_Type.__name__ = "Integer32"
_OspfCurCfgIntfHello_Object = MibTableColumn
ospfCurCfgIntfHello = _OspfCurCfgIntfHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 7, 1, 7),
    _OspfCurCfgIntfHello_Type()
)
ospfCurCfgIntfHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfHello.setStatus("current")


class _OspfCurCfgIntfDead_Type(Integer32):
    """Custom type ospfCurCfgIntfDead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfCurCfgIntfDead_Type.__name__ = "Integer32"
_OspfCurCfgIntfDead_Object = MibTableColumn
ospfCurCfgIntfDead = _OspfCurCfgIntfDead_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 7, 1, 8),
    _OspfCurCfgIntfDead_Type()
)
ospfCurCfgIntfDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfDead.setStatus("current")


class _OspfCurCfgIntfTrans_Type(Integer32):
    """Custom type ospfCurCfgIntfTrans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_OspfCurCfgIntfTrans_Type.__name__ = "Integer32"
_OspfCurCfgIntfTrans_Object = MibTableColumn
ospfCurCfgIntfTrans = _OspfCurCfgIntfTrans_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 7, 1, 9),
    _OspfCurCfgIntfTrans_Type()
)
ospfCurCfgIntfTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfTrans.setStatus("current")


class _OspfCurCfgIntfRetra_Type(Integer32):
    """Custom type ospfCurCfgIntfRetra based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_OspfCurCfgIntfRetra_Type.__name__ = "Integer32"
_OspfCurCfgIntfRetra_Object = MibTableColumn
ospfCurCfgIntfRetra = _OspfCurCfgIntfRetra_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 7, 1, 10),
    _OspfCurCfgIntfRetra_Type()
)
ospfCurCfgIntfRetra.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfRetra.setStatus("current")


class _OspfCurCfgIntfAuthKey_Type(DisplayString):
    """Custom type ospfCurCfgIntfAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OspfCurCfgIntfAuthKey_Type.__name__ = "DisplayString"
_OspfCurCfgIntfAuthKey_Object = MibTableColumn
ospfCurCfgIntfAuthKey = _OspfCurCfgIntfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 7, 1, 11),
    _OspfCurCfgIntfAuthKey_Type()
)
ospfCurCfgIntfAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfAuthKey.setStatus("current")


class _OspfCurCfgIntfStatus_Type(Integer32):
    """Custom type ospfCurCfgIntfStatus based on Integer32"""
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


_OspfCurCfgIntfStatus_Type.__name__ = "Integer32"
_OspfCurCfgIntfStatus_Object = MibTableColumn
ospfCurCfgIntfStatus = _OspfCurCfgIntfStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 7, 1, 12),
    _OspfCurCfgIntfStatus_Type()
)
ospfCurCfgIntfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfStatus.setStatus("current")
_OspfNewCfgIntfTable_Object = MibTable
ospfNewCfgIntfTable = _OspfNewCfgIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 8)
)
if mibBuilder.loadTexts:
    ospfNewCfgIntfTable.setStatus("current")
_OspfNewCfgIntfEntry_Object = MibTableRow
ospfNewCfgIntfEntry = _OspfNewCfgIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 8, 1)
)
ospfNewCfgIntfEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfNewCfgIntfIndex"),
)
if mibBuilder.loadTexts:
    ospfNewCfgIntfEntry.setStatus("current")
_OspfNewCfgIntfIndex_Type = Integer32
_OspfNewCfgIntfIndex_Object = MibTableColumn
ospfNewCfgIntfIndex = _OspfNewCfgIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 8, 1, 1),
    _OspfNewCfgIntfIndex_Type()
)
ospfNewCfgIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgIntfIndex.setStatus("current")
_OspfNewCfgIntfId_Type = IpAddress
_OspfNewCfgIntfId_Object = MibTableColumn
ospfNewCfgIntfId = _OspfNewCfgIntfId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 8, 1, 2),
    _OspfNewCfgIntfId_Type()
)
ospfNewCfgIntfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgIntfId.setStatus("current")


class _OspfNewCfgIntfArea_Type(Integer32):
    """Custom type ospfNewCfgIntfArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_OspfNewCfgIntfArea_Type.__name__ = "Integer32"
_OspfNewCfgIntfArea_Object = MibTableColumn
ospfNewCfgIntfArea = _OspfNewCfgIntfArea_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 8, 1, 3),
    _OspfNewCfgIntfArea_Type()
)
ospfNewCfgIntfArea.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfArea.setStatus("current")


class _OspfNewCfgIntfMdkey_Type(Integer32):
    """Custom type ospfNewCfgIntfMdkey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OspfNewCfgIntfMdkey_Type.__name__ = "Integer32"
_OspfNewCfgIntfMdkey_Object = MibTableColumn
ospfNewCfgIntfMdkey = _OspfNewCfgIntfMdkey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 8, 1, 4),
    _OspfNewCfgIntfMdkey_Type()
)
ospfNewCfgIntfMdkey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfMdkey.setStatus("current")


class _OspfNewCfgIntfCost_Type(Integer32):
    """Custom type ospfNewCfgIntfCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfNewCfgIntfCost_Type.__name__ = "Integer32"
_OspfNewCfgIntfCost_Object = MibTableColumn
ospfNewCfgIntfCost = _OspfNewCfgIntfCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 8, 1, 5),
    _OspfNewCfgIntfCost_Type()
)
ospfNewCfgIntfCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfCost.setStatus("current")


class _OspfNewCfgIntfPrio_Type(Integer32):
    """Custom type ospfNewCfgIntfPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OspfNewCfgIntfPrio_Type.__name__ = "Integer32"
_OspfNewCfgIntfPrio_Object = MibTableColumn
ospfNewCfgIntfPrio = _OspfNewCfgIntfPrio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 8, 1, 6),
    _OspfNewCfgIntfPrio_Type()
)
ospfNewCfgIntfPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfPrio.setStatus("current")


class _OspfNewCfgIntfHello_Type(Integer32):
    """Custom type ospfNewCfgIntfHello based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfNewCfgIntfHello_Type.__name__ = "Integer32"
_OspfNewCfgIntfHello_Object = MibTableColumn
ospfNewCfgIntfHello = _OspfNewCfgIntfHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 8, 1, 7),
    _OspfNewCfgIntfHello_Type()
)
ospfNewCfgIntfHello.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfHello.setStatus("current")


class _OspfNewCfgIntfDead_Type(Integer32):
    """Custom type ospfNewCfgIntfDead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfNewCfgIntfDead_Type.__name__ = "Integer32"
_OspfNewCfgIntfDead_Object = MibTableColumn
ospfNewCfgIntfDead = _OspfNewCfgIntfDead_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 8, 1, 8),
    _OspfNewCfgIntfDead_Type()
)
ospfNewCfgIntfDead.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfDead.setStatus("current")


class _OspfNewCfgIntfTrans_Type(Integer32):
    """Custom type ospfNewCfgIntfTrans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_OspfNewCfgIntfTrans_Type.__name__ = "Integer32"
_OspfNewCfgIntfTrans_Object = MibTableColumn
ospfNewCfgIntfTrans = _OspfNewCfgIntfTrans_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 8, 1, 9),
    _OspfNewCfgIntfTrans_Type()
)
ospfNewCfgIntfTrans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfTrans.setStatus("current")


class _OspfNewCfgIntfRetra_Type(Integer32):
    """Custom type ospfNewCfgIntfRetra based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_OspfNewCfgIntfRetra_Type.__name__ = "Integer32"
_OspfNewCfgIntfRetra_Object = MibTableColumn
ospfNewCfgIntfRetra = _OspfNewCfgIntfRetra_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 8, 1, 10),
    _OspfNewCfgIntfRetra_Type()
)
ospfNewCfgIntfRetra.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfRetra.setStatus("current")


class _OspfNewCfgIntfAuthKey_Type(DisplayString):
    """Custom type ospfNewCfgIntfAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OspfNewCfgIntfAuthKey_Type.__name__ = "DisplayString"
_OspfNewCfgIntfAuthKey_Object = MibTableColumn
ospfNewCfgIntfAuthKey = _OspfNewCfgIntfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 8, 1, 11),
    _OspfNewCfgIntfAuthKey_Type()
)
ospfNewCfgIntfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfAuthKey.setStatus("current")


class _OspfNewCfgIntfStatus_Type(Integer32):
    """Custom type ospfNewCfgIntfStatus based on Integer32"""
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


_OspfNewCfgIntfStatus_Type.__name__ = "Integer32"
_OspfNewCfgIntfStatus_Object = MibTableColumn
ospfNewCfgIntfStatus = _OspfNewCfgIntfStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 8, 1, 12),
    _OspfNewCfgIntfStatus_Type()
)
ospfNewCfgIntfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfStatus.setStatus("current")


class _OspfNewCfgIntfDelete_Type(Integer32):
    """Custom type ospfNewCfgIntfDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("other", 0))
    )


_OspfNewCfgIntfDelete_Type.__name__ = "Integer32"
_OspfNewCfgIntfDelete_Object = MibTableColumn
ospfNewCfgIntfDelete = _OspfNewCfgIntfDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 8, 1, 13),
    _OspfNewCfgIntfDelete_Type()
)
ospfNewCfgIntfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgIntfDelete.setStatus("current")
_OspfCurCfgVirtIntfTable_Object = MibTable
ospfCurCfgVirtIntfTable = _OspfCurCfgVirtIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 9)
)
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfTable.setStatus("current")
_OspfCurCfgVirtIntfEntry_Object = MibTableRow
ospfCurCfgVirtIntfEntry = _OspfCurCfgVirtIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 9, 1)
)
ospfCurCfgVirtIntfEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfCurCfgVirtIntfIndex"),
)
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfEntry.setStatus("current")
_OspfCurCfgVirtIntfIndex_Type = Integer32
_OspfCurCfgVirtIntfIndex_Object = MibTableColumn
ospfCurCfgVirtIntfIndex = _OspfCurCfgVirtIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 9, 1, 1),
    _OspfCurCfgVirtIntfIndex_Type()
)
ospfCurCfgVirtIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfIndex.setStatus("current")


class _OspfCurCfgVirtIntfAreaId_Type(Integer32):
    """Custom type ospfCurCfgVirtIntfAreaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_OspfCurCfgVirtIntfAreaId_Type.__name__ = "Integer32"
_OspfCurCfgVirtIntfAreaId_Object = MibTableColumn
ospfCurCfgVirtIntfAreaId = _OspfCurCfgVirtIntfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 9, 1, 2),
    _OspfCurCfgVirtIntfAreaId_Type()
)
ospfCurCfgVirtIntfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfAreaId.setStatus("current")
_OspfCurCfgVirtIntfNbr_Type = IpAddress
_OspfCurCfgVirtIntfNbr_Object = MibTableColumn
ospfCurCfgVirtIntfNbr = _OspfCurCfgVirtIntfNbr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 9, 1, 3),
    _OspfCurCfgVirtIntfNbr_Type()
)
ospfCurCfgVirtIntfNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfNbr.setStatus("current")


class _OspfCurCfgVirtIntfMdkey_Type(Integer32):
    """Custom type ospfCurCfgVirtIntfMdkey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OspfCurCfgVirtIntfMdkey_Type.__name__ = "Integer32"
_OspfCurCfgVirtIntfMdkey_Object = MibTableColumn
ospfCurCfgVirtIntfMdkey = _OspfCurCfgVirtIntfMdkey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 9, 1, 4),
    _OspfCurCfgVirtIntfMdkey_Type()
)
ospfCurCfgVirtIntfMdkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfMdkey.setStatus("current")


class _OspfCurCfgVirtIntfHello_Type(Integer32):
    """Custom type ospfCurCfgVirtIntfHello based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfCurCfgVirtIntfHello_Type.__name__ = "Integer32"
_OspfCurCfgVirtIntfHello_Object = MibTableColumn
ospfCurCfgVirtIntfHello = _OspfCurCfgVirtIntfHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 9, 1, 5),
    _OspfCurCfgVirtIntfHello_Type()
)
ospfCurCfgVirtIntfHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfHello.setStatus("current")


class _OspfCurCfgVirtIntfDead_Type(Integer32):
    """Custom type ospfCurCfgVirtIntfDead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfCurCfgVirtIntfDead_Type.__name__ = "Integer32"
_OspfCurCfgVirtIntfDead_Object = MibTableColumn
ospfCurCfgVirtIntfDead = _OspfCurCfgVirtIntfDead_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 9, 1, 6),
    _OspfCurCfgVirtIntfDead_Type()
)
ospfCurCfgVirtIntfDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfDead.setStatus("current")


class _OspfCurCfgVirtIntfTrans_Type(Integer32):
    """Custom type ospfCurCfgVirtIntfTrans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_OspfCurCfgVirtIntfTrans_Type.__name__ = "Integer32"
_OspfCurCfgVirtIntfTrans_Object = MibTableColumn
ospfCurCfgVirtIntfTrans = _OspfCurCfgVirtIntfTrans_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 9, 1, 7),
    _OspfCurCfgVirtIntfTrans_Type()
)
ospfCurCfgVirtIntfTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfTrans.setStatus("current")


class _OspfCurCfgVirtIntfRetra_Type(Integer32):
    """Custom type ospfCurCfgVirtIntfRetra based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_OspfCurCfgVirtIntfRetra_Type.__name__ = "Integer32"
_OspfCurCfgVirtIntfRetra_Object = MibTableColumn
ospfCurCfgVirtIntfRetra = _OspfCurCfgVirtIntfRetra_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 9, 1, 8),
    _OspfCurCfgVirtIntfRetra_Type()
)
ospfCurCfgVirtIntfRetra.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfRetra.setStatus("current")


class _OspfCurCfgVirtIntfAuthKey_Type(DisplayString):
    """Custom type ospfCurCfgVirtIntfAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OspfCurCfgVirtIntfAuthKey_Type.__name__ = "DisplayString"
_OspfCurCfgVirtIntfAuthKey_Object = MibTableColumn
ospfCurCfgVirtIntfAuthKey = _OspfCurCfgVirtIntfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 9, 1, 9),
    _OspfCurCfgVirtIntfAuthKey_Type()
)
ospfCurCfgVirtIntfAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfAuthKey.setStatus("current")


class _OspfCurCfgVirtIntfStatus_Type(Integer32):
    """Custom type ospfCurCfgVirtIntfStatus based on Integer32"""
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


_OspfCurCfgVirtIntfStatus_Type.__name__ = "Integer32"
_OspfCurCfgVirtIntfStatus_Object = MibTableColumn
ospfCurCfgVirtIntfStatus = _OspfCurCfgVirtIntfStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 9, 1, 10),
    _OspfCurCfgVirtIntfStatus_Type()
)
ospfCurCfgVirtIntfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfStatus.setStatus("current")
_OspfNewCfgVirtIntfTable_Object = MibTable
ospfNewCfgVirtIntfTable = _OspfNewCfgVirtIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 10)
)
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfTable.setStatus("current")
_OspfNewCfgVirtIntfEntry_Object = MibTableRow
ospfNewCfgVirtIntfEntry = _OspfNewCfgVirtIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 10, 1)
)
ospfNewCfgVirtIntfEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfNewCfgVirtIntfIndex"),
)
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfEntry.setStatus("current")
_OspfNewCfgVirtIntfIndex_Type = Integer32
_OspfNewCfgVirtIntfIndex_Object = MibTableColumn
ospfNewCfgVirtIntfIndex = _OspfNewCfgVirtIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 10, 1, 1),
    _OspfNewCfgVirtIntfIndex_Type()
)
ospfNewCfgVirtIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfIndex.setStatus("current")


class _OspfNewCfgVirtIntfAreaId_Type(Integer32):
    """Custom type ospfNewCfgVirtIntfAreaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_OspfNewCfgVirtIntfAreaId_Type.__name__ = "Integer32"
_OspfNewCfgVirtIntfAreaId_Object = MibTableColumn
ospfNewCfgVirtIntfAreaId = _OspfNewCfgVirtIntfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 10, 1, 2),
    _OspfNewCfgVirtIntfAreaId_Type()
)
ospfNewCfgVirtIntfAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfAreaId.setStatus("current")
_OspfNewCfgVirtIntfNbr_Type = IpAddress
_OspfNewCfgVirtIntfNbr_Object = MibTableColumn
ospfNewCfgVirtIntfNbr = _OspfNewCfgVirtIntfNbr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 10, 1, 3),
    _OspfNewCfgVirtIntfNbr_Type()
)
ospfNewCfgVirtIntfNbr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfNbr.setStatus("current")


class _OspfNewCfgVirtIntfMdkey_Type(Integer32):
    """Custom type ospfNewCfgVirtIntfMdkey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OspfNewCfgVirtIntfMdkey_Type.__name__ = "Integer32"
_OspfNewCfgVirtIntfMdkey_Object = MibTableColumn
ospfNewCfgVirtIntfMdkey = _OspfNewCfgVirtIntfMdkey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 10, 1, 4),
    _OspfNewCfgVirtIntfMdkey_Type()
)
ospfNewCfgVirtIntfMdkey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfMdkey.setStatus("current")


class _OspfNewCfgVirtIntfHello_Type(Integer32):
    """Custom type ospfNewCfgVirtIntfHello based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfNewCfgVirtIntfHello_Type.__name__ = "Integer32"
_OspfNewCfgVirtIntfHello_Object = MibTableColumn
ospfNewCfgVirtIntfHello = _OspfNewCfgVirtIntfHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 10, 1, 5),
    _OspfNewCfgVirtIntfHello_Type()
)
ospfNewCfgVirtIntfHello.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfHello.setStatus("current")


class _OspfNewCfgVirtIntfDead_Type(Integer32):
    """Custom type ospfNewCfgVirtIntfDead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfNewCfgVirtIntfDead_Type.__name__ = "Integer32"
_OspfNewCfgVirtIntfDead_Object = MibTableColumn
ospfNewCfgVirtIntfDead = _OspfNewCfgVirtIntfDead_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 10, 1, 6),
    _OspfNewCfgVirtIntfDead_Type()
)
ospfNewCfgVirtIntfDead.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfDead.setStatus("current")


class _OspfNewCfgVirtIntfTrans_Type(Integer32):
    """Custom type ospfNewCfgVirtIntfTrans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_OspfNewCfgVirtIntfTrans_Type.__name__ = "Integer32"
_OspfNewCfgVirtIntfTrans_Object = MibTableColumn
ospfNewCfgVirtIntfTrans = _OspfNewCfgVirtIntfTrans_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 10, 1, 7),
    _OspfNewCfgVirtIntfTrans_Type()
)
ospfNewCfgVirtIntfTrans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfTrans.setStatus("current")


class _OspfNewCfgVirtIntfRetra_Type(Integer32):
    """Custom type ospfNewCfgVirtIntfRetra based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_OspfNewCfgVirtIntfRetra_Type.__name__ = "Integer32"
_OspfNewCfgVirtIntfRetra_Object = MibTableColumn
ospfNewCfgVirtIntfRetra = _OspfNewCfgVirtIntfRetra_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 10, 1, 8),
    _OspfNewCfgVirtIntfRetra_Type()
)
ospfNewCfgVirtIntfRetra.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfRetra.setStatus("current")


class _OspfNewCfgVirtIntfAuthKey_Type(DisplayString):
    """Custom type ospfNewCfgVirtIntfAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OspfNewCfgVirtIntfAuthKey_Type.__name__ = "DisplayString"
_OspfNewCfgVirtIntfAuthKey_Object = MibTableColumn
ospfNewCfgVirtIntfAuthKey = _OspfNewCfgVirtIntfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 10, 1, 9),
    _OspfNewCfgVirtIntfAuthKey_Type()
)
ospfNewCfgVirtIntfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfAuthKey.setStatus("current")


class _OspfNewCfgVirtIntfStatus_Type(Integer32):
    """Custom type ospfNewCfgVirtIntfStatus based on Integer32"""
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


_OspfNewCfgVirtIntfStatus_Type.__name__ = "Integer32"
_OspfNewCfgVirtIntfStatus_Object = MibTableColumn
ospfNewCfgVirtIntfStatus = _OspfNewCfgVirtIntfStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 10, 1, 10),
    _OspfNewCfgVirtIntfStatus_Type()
)
ospfNewCfgVirtIntfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfStatus.setStatus("current")


class _OspfNewCfgVirtIntfDelete_Type(Integer32):
    """Custom type ospfNewCfgVirtIntfDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("other", 0))
    )


_OspfNewCfgVirtIntfDelete_Type.__name__ = "Integer32"
_OspfNewCfgVirtIntfDelete_Object = MibTableColumn
ospfNewCfgVirtIntfDelete = _OspfNewCfgVirtIntfDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 10, 1, 11),
    _OspfNewCfgVirtIntfDelete_Type()
)
ospfNewCfgVirtIntfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfDelete.setStatus("current")
_OspfMdkeyTableMaxSize_Type = Integer32
_OspfMdkeyTableMaxSize_Object = MibScalar
ospfMdkeyTableMaxSize = _OspfMdkeyTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 11),
    _OspfMdkeyTableMaxSize_Type()
)
ospfMdkeyTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfMdkeyTableMaxSize.setStatus("current")
_OspfCurCfgHostTable_Object = MibTable
ospfCurCfgHostTable = _OspfCurCfgHostTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 12)
)
if mibBuilder.loadTexts:
    ospfCurCfgHostTable.setStatus("current")
_OspfCurCfgHostEntry_Object = MibTableRow
ospfCurCfgHostEntry = _OspfCurCfgHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 12, 1)
)
ospfCurCfgHostEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfCurCfgHostIndex"),
    (0, "BLADETYPE2-NETWORK-MIB", "ospfCurCfgHostIpAddr"),
)
if mibBuilder.loadTexts:
    ospfCurCfgHostEntry.setStatus("current")
_OspfCurCfgHostIndex_Type = Integer32
_OspfCurCfgHostIndex_Object = MibTableColumn
ospfCurCfgHostIndex = _OspfCurCfgHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 12, 1, 1),
    _OspfCurCfgHostIndex_Type()
)
ospfCurCfgHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgHostIndex.setStatus("current")
_OspfCurCfgHostIpAddr_Type = IpAddress
_OspfCurCfgHostIpAddr_Object = MibTableColumn
ospfCurCfgHostIpAddr = _OspfCurCfgHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 12, 1, 2),
    _OspfCurCfgHostIpAddr_Type()
)
ospfCurCfgHostIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgHostIpAddr.setStatus("current")
_OspfCurCfgHostAreaIndex_Type = Integer32
_OspfCurCfgHostAreaIndex_Object = MibTableColumn
ospfCurCfgHostAreaIndex = _OspfCurCfgHostAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 12, 1, 3),
    _OspfCurCfgHostAreaIndex_Type()
)
ospfCurCfgHostAreaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgHostAreaIndex.setStatus("current")


class _OspfCurCfgHostCost_Type(Integer32):
    """Custom type ospfCurCfgHostCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfCurCfgHostCost_Type.__name__ = "Integer32"
_OspfCurCfgHostCost_Object = MibTableColumn
ospfCurCfgHostCost = _OspfCurCfgHostCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 12, 1, 4),
    _OspfCurCfgHostCost_Type()
)
ospfCurCfgHostCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgHostCost.setStatus("current")


class _OspfCurCfgHostState_Type(Integer32):
    """Custom type ospfCurCfgHostState based on Integer32"""
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


_OspfCurCfgHostState_Type.__name__ = "Integer32"
_OspfCurCfgHostState_Object = MibTableColumn
ospfCurCfgHostState = _OspfCurCfgHostState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 12, 1, 5),
    _OspfCurCfgHostState_Type()
)
ospfCurCfgHostState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgHostState.setStatus("current")
_OspfNewCfgHostTable_Object = MibTable
ospfNewCfgHostTable = _OspfNewCfgHostTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 13)
)
if mibBuilder.loadTexts:
    ospfNewCfgHostTable.setStatus("current")
_OspfNewCfgHostEntry_Object = MibTableRow
ospfNewCfgHostEntry = _OspfNewCfgHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 13, 1)
)
ospfNewCfgHostEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfNewCfgHostIndex"),
    (0, "BLADETYPE2-NETWORK-MIB", "ospfNewCfgHostIpAddr"),
)
if mibBuilder.loadTexts:
    ospfNewCfgHostEntry.setStatus("current")
_OspfNewCfgHostIndex_Type = Integer32
_OspfNewCfgHostIndex_Object = MibTableColumn
ospfNewCfgHostIndex = _OspfNewCfgHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 13, 1, 1),
    _OspfNewCfgHostIndex_Type()
)
ospfNewCfgHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgHostIndex.setStatus("current")
_OspfNewCfgHostIpAddr_Type = IpAddress
_OspfNewCfgHostIpAddr_Object = MibTableColumn
ospfNewCfgHostIpAddr = _OspfNewCfgHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 13, 1, 2),
    _OspfNewCfgHostIpAddr_Type()
)
ospfNewCfgHostIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgHostIpAddr.setStatus("current")
_OspfNewCfgHostAreaIndex_Type = Integer32
_OspfNewCfgHostAreaIndex_Object = MibTableColumn
ospfNewCfgHostAreaIndex = _OspfNewCfgHostAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 13, 1, 3),
    _OspfNewCfgHostAreaIndex_Type()
)
ospfNewCfgHostAreaIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgHostAreaIndex.setStatus("current")


class _OspfNewCfgHostCost_Type(Integer32):
    """Custom type ospfNewCfgHostCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfNewCfgHostCost_Type.__name__ = "Integer32"
_OspfNewCfgHostCost_Object = MibTableColumn
ospfNewCfgHostCost = _OspfNewCfgHostCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 13, 1, 4),
    _OspfNewCfgHostCost_Type()
)
ospfNewCfgHostCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgHostCost.setStatus("current")


class _OspfNewCfgHostState_Type(Integer32):
    """Custom type ospfNewCfgHostState based on Integer32"""
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


_OspfNewCfgHostState_Type.__name__ = "Integer32"
_OspfNewCfgHostState_Object = MibTableColumn
ospfNewCfgHostState = _OspfNewCfgHostState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 13, 1, 5),
    _OspfNewCfgHostState_Type()
)
ospfNewCfgHostState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgHostState.setStatus("current")


class _OspfNewCfgHostDelete_Type(Integer32):
    """Custom type ospfNewCfgHostDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_OspfNewCfgHostDelete_Type.__name__ = "Integer32"
_OspfNewCfgHostDelete_Object = MibTableColumn
ospfNewCfgHostDelete = _OspfNewCfgHostDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 13, 1, 6),
    _OspfNewCfgHostDelete_Type()
)
ospfNewCfgHostDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgHostDelete.setStatus("current")
_OspfCurCfgRangeTable_Object = MibTable
ospfCurCfgRangeTable = _OspfCurCfgRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 14)
)
if mibBuilder.loadTexts:
    ospfCurCfgRangeTable.setStatus("current")
_OspfCurCfgRangeEntry_Object = MibTableRow
ospfCurCfgRangeEntry = _OspfCurCfgRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 14, 1)
)
ospfCurCfgRangeEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfCurCfgRangeIndex"),
)
if mibBuilder.loadTexts:
    ospfCurCfgRangeEntry.setStatus("current")
_OspfCurCfgRangeIndex_Type = Integer32
_OspfCurCfgRangeIndex_Object = MibTableColumn
ospfCurCfgRangeIndex = _OspfCurCfgRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 14, 1, 1),
    _OspfCurCfgRangeIndex_Type()
)
ospfCurCfgRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgRangeIndex.setStatus("current")
_OspfCurCfgRangeAddr_Type = IpAddress
_OspfCurCfgRangeAddr_Object = MibTableColumn
ospfCurCfgRangeAddr = _OspfCurCfgRangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 14, 1, 2),
    _OspfCurCfgRangeAddr_Type()
)
ospfCurCfgRangeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgRangeAddr.setStatus("current")
_OspfCurCfgRangeMask_Type = IpAddress
_OspfCurCfgRangeMask_Object = MibTableColumn
ospfCurCfgRangeMask = _OspfCurCfgRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 14, 1, 3),
    _OspfCurCfgRangeMask_Type()
)
ospfCurCfgRangeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgRangeMask.setStatus("current")
_OspfCurCfgRangeAreaIndex_Type = Integer32
_OspfCurCfgRangeAreaIndex_Object = MibTableColumn
ospfCurCfgRangeAreaIndex = _OspfCurCfgRangeAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 14, 1, 4),
    _OspfCurCfgRangeAreaIndex_Type()
)
ospfCurCfgRangeAreaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgRangeAreaIndex.setStatus("current")


class _OspfCurCfgRangeHideState_Type(Integer32):
    """Custom type ospfCurCfgRangeHideState based on Integer32"""
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


_OspfCurCfgRangeHideState_Type.__name__ = "Integer32"
_OspfCurCfgRangeHideState_Object = MibTableColumn
ospfCurCfgRangeHideState = _OspfCurCfgRangeHideState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 14, 1, 5),
    _OspfCurCfgRangeHideState_Type()
)
ospfCurCfgRangeHideState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgRangeHideState.setStatus("current")


class _OspfCurCfgRangeState_Type(Integer32):
    """Custom type ospfCurCfgRangeState based on Integer32"""
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


_OspfCurCfgRangeState_Type.__name__ = "Integer32"
_OspfCurCfgRangeState_Object = MibTableColumn
ospfCurCfgRangeState = _OspfCurCfgRangeState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 14, 1, 6),
    _OspfCurCfgRangeState_Type()
)
ospfCurCfgRangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgRangeState.setStatus("current")
_OspfNewCfgRangeTable_Object = MibTable
ospfNewCfgRangeTable = _OspfNewCfgRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 15)
)
if mibBuilder.loadTexts:
    ospfNewCfgRangeTable.setStatus("current")
_OspfNewCfgRangeEntry_Object = MibTableRow
ospfNewCfgRangeEntry = _OspfNewCfgRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 15, 1)
)
ospfNewCfgRangeEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfNewCfgRangeIndex"),
)
if mibBuilder.loadTexts:
    ospfNewCfgRangeEntry.setStatus("current")
_OspfNewCfgRangeIndex_Type = Integer32
_OspfNewCfgRangeIndex_Object = MibTableColumn
ospfNewCfgRangeIndex = _OspfNewCfgRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 15, 1, 1),
    _OspfNewCfgRangeIndex_Type()
)
ospfNewCfgRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgRangeIndex.setStatus("current")
_OspfNewCfgRangeAddr_Type = IpAddress
_OspfNewCfgRangeAddr_Object = MibTableColumn
ospfNewCfgRangeAddr = _OspfNewCfgRangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 15, 1, 2),
    _OspfNewCfgRangeAddr_Type()
)
ospfNewCfgRangeAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgRangeAddr.setStatus("current")
_OspfNewCfgRangeMask_Type = IpAddress
_OspfNewCfgRangeMask_Object = MibTableColumn
ospfNewCfgRangeMask = _OspfNewCfgRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 15, 1, 3),
    _OspfNewCfgRangeMask_Type()
)
ospfNewCfgRangeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgRangeMask.setStatus("current")
_OspfNewCfgRangeAreaIndex_Type = Integer32
_OspfNewCfgRangeAreaIndex_Object = MibTableColumn
ospfNewCfgRangeAreaIndex = _OspfNewCfgRangeAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 15, 1, 4),
    _OspfNewCfgRangeAreaIndex_Type()
)
ospfNewCfgRangeAreaIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgRangeAreaIndex.setStatus("current")


class _OspfNewCfgRangeHideState_Type(Integer32):
    """Custom type ospfNewCfgRangeHideState based on Integer32"""
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


_OspfNewCfgRangeHideState_Type.__name__ = "Integer32"
_OspfNewCfgRangeHideState_Object = MibTableColumn
ospfNewCfgRangeHideState = _OspfNewCfgRangeHideState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 15, 1, 5),
    _OspfNewCfgRangeHideState_Type()
)
ospfNewCfgRangeHideState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgRangeHideState.setStatus("current")


class _OspfNewCfgRangeState_Type(Integer32):
    """Custom type ospfNewCfgRangeState based on Integer32"""
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


_OspfNewCfgRangeState_Type.__name__ = "Integer32"
_OspfNewCfgRangeState_Object = MibTableColumn
ospfNewCfgRangeState = _OspfNewCfgRangeState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 15, 1, 6),
    _OspfNewCfgRangeState_Type()
)
ospfNewCfgRangeState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgRangeState.setStatus("current")


class _OspfNewCfgRangeDelete_Type(Integer32):
    """Custom type ospfNewCfgRangeDelete based on Integer32"""
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


_OspfNewCfgRangeDelete_Type.__name__ = "Integer32"
_OspfNewCfgRangeDelete_Object = MibTableColumn
ospfNewCfgRangeDelete = _OspfNewCfgRangeDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 13, 15, 1, 7),
    _OspfNewCfgRangeDelete_Type()
)
ospfNewCfgRangeDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgRangeDelete.setStatus("current")
_IpGeneralCfg_ObjectIdentity = ObjectIdentity
ipGeneralCfg = _IpGeneralCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 14)
)
_IpCurCfgRouterID_Type = IpAddress
_IpCurCfgRouterID_Object = MibScalar
ipCurCfgRouterID = _IpCurCfgRouterID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 14, 1),
    _IpCurCfgRouterID_Type()
)
ipCurCfgRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgRouterID.setStatus("current")
_IpNewCfgRouterID_Type = IpAddress
_IpNewCfgRouterID_Object = MibScalar
ipNewCfgRouterID = _IpNewCfgRouterID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 14, 2),
    _IpNewCfgRouterID_Type()
)
ipNewCfgRouterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgRouterID.setStatus("current")
_IgmpCfg_ObjectIdentity = ObjectIdentity
igmpCfg = _IgmpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15)
)


class _IgmpCurCfgOnOff_Type(Integer32):
    """Custom type igmpCurCfgOnOff based on Integer32"""
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


_IgmpCurCfgOnOff_Type.__name__ = "Integer32"
_IgmpCurCfgOnOff_Object = MibScalar
igmpCurCfgOnOff = _IgmpCurCfgOnOff_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 1),
    _IgmpCurCfgOnOff_Type()
)
igmpCurCfgOnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCurCfgOnOff.setStatus("current")


class _IgmpNewCfgOnOff_Type(Integer32):
    """Custom type igmpNewCfgOnOff based on Integer32"""
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


_IgmpNewCfgOnOff_Type.__name__ = "Integer32"
_IgmpNewCfgOnOff_Object = MibScalar
igmpNewCfgOnOff = _IgmpNewCfgOnOff_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 2),
    _IgmpNewCfgOnOff_Type()
)
igmpNewCfgOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpNewCfgOnOff.setStatus("current")
_IgmpSnoopCfgGen_ObjectIdentity = ObjectIdentity
igmpSnoopCfgGen = _IgmpSnoopCfgGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3)
)
_IgmpSnoopCfg_ObjectIdentity = ObjectIdentity
igmpSnoopCfg = _IgmpSnoopCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1)
)
_IgmpSnoopCurCfgTimeout_Type = Integer32
_IgmpSnoopCurCfgTimeout_Object = MibScalar
igmpSnoopCurCfgTimeout = _IgmpSnoopCurCfgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 1),
    _IgmpSnoopCurCfgTimeout_Type()
)
igmpSnoopCurCfgTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopCurCfgTimeout.setStatus("current")
_IgmpSnoopNewCfgTimeout_Type = Integer32
_IgmpSnoopNewCfgTimeout_Object = MibScalar
igmpSnoopNewCfgTimeout = _IgmpSnoopNewCfgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 2),
    _IgmpSnoopNewCfgTimeout_Type()
)
igmpSnoopNewCfgTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopNewCfgTimeout.setStatus("current")
_IgmpSnoopCurCfgMrto_Type = Integer32
_IgmpSnoopCurCfgMrto_Object = MibScalar
igmpSnoopCurCfgMrto = _IgmpSnoopCurCfgMrto_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 3),
    _IgmpSnoopCurCfgMrto_Type()
)
igmpSnoopCurCfgMrto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopCurCfgMrto.setStatus("current")
_IgmpSnoopNewCfgMrto_Type = Integer32
_IgmpSnoopNewCfgMrto_Object = MibScalar
igmpSnoopNewCfgMrto = _IgmpSnoopNewCfgMrto_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 4),
    _IgmpSnoopNewCfgMrto_Type()
)
igmpSnoopNewCfgMrto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopNewCfgMrto.setStatus("current")
_IgmpSnoopNewCfgVlanFastlvAdd_Type = Integer32
_IgmpSnoopNewCfgVlanFastlvAdd_Object = MibScalar
igmpSnoopNewCfgVlanFastlvAdd = _IgmpSnoopNewCfgVlanFastlvAdd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 12),
    _IgmpSnoopNewCfgVlanFastlvAdd_Type()
)
igmpSnoopNewCfgVlanFastlvAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopNewCfgVlanFastlvAdd.setStatus("current")
_IgmpSnoopNewCfgVlanFastlvRem_Type = Integer32
_IgmpSnoopNewCfgVlanFastlvRem_Object = MibScalar
igmpSnoopNewCfgVlanFastlvRem = _IgmpSnoopNewCfgVlanFastlvRem_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 13),
    _IgmpSnoopNewCfgVlanFastlvRem_Type()
)
igmpSnoopNewCfgVlanFastlvRem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopNewCfgVlanFastlvRem.setStatus("current")
_IgmpSnoopCurCfgVlanFastlvBmap_Type = OctetString
_IgmpSnoopCurCfgVlanFastlvBmap_Object = MibScalar
igmpSnoopCurCfgVlanFastlvBmap = _IgmpSnoopCurCfgVlanFastlvBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 14),
    _IgmpSnoopCurCfgVlanFastlvBmap_Type()
)
igmpSnoopCurCfgVlanFastlvBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopCurCfgVlanFastlvBmap.setStatus("current")
_IgmpSnoopNewCfgVlanFastlvBmap_Type = OctetString
_IgmpSnoopNewCfgVlanFastlvBmap_Object = MibScalar
igmpSnoopNewCfgVlanFastlvBmap = _IgmpSnoopNewCfgVlanFastlvBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 15),
    _IgmpSnoopNewCfgVlanFastlvBmap_Type()
)
igmpSnoopNewCfgVlanFastlvBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopNewCfgVlanFastlvBmap.setStatus("current")
_IgmpSnoopCurCfgRobust_Type = Integer32
_IgmpSnoopCurCfgRobust_Object = MibScalar
igmpSnoopCurCfgRobust = _IgmpSnoopCurCfgRobust_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 16),
    _IgmpSnoopCurCfgRobust_Type()
)
igmpSnoopCurCfgRobust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopCurCfgRobust.setStatus("current")
_IgmpSnoopNewCfgRobust_Type = Integer32
_IgmpSnoopNewCfgRobust_Object = MibScalar
igmpSnoopNewCfgRobust = _IgmpSnoopNewCfgRobust_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 17),
    _IgmpSnoopNewCfgRobust_Type()
)
igmpSnoopNewCfgRobust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopNewCfgRobust.setStatus("current")
_IgmpSnoopNewCfgVlanAdd_Type = Integer32
_IgmpSnoopNewCfgVlanAdd_Object = MibScalar
igmpSnoopNewCfgVlanAdd = _IgmpSnoopNewCfgVlanAdd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 18),
    _IgmpSnoopNewCfgVlanAdd_Type()
)
igmpSnoopNewCfgVlanAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopNewCfgVlanAdd.setStatus("current")
_IgmpSnoopNewCfgVlanRem_Type = Integer32
_IgmpSnoopNewCfgVlanRem_Object = MibScalar
igmpSnoopNewCfgVlanRem = _IgmpSnoopNewCfgVlanRem_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 19),
    _IgmpSnoopNewCfgVlanRem_Type()
)
igmpSnoopNewCfgVlanRem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopNewCfgVlanRem.setStatus("current")


class _IgmpSnoopNewCfgVlanClear_Type(Integer32):
    """Custom type igmpSnoopNewCfgVlanClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ok", 2))
    )


_IgmpSnoopNewCfgVlanClear_Type.__name__ = "Integer32"
_IgmpSnoopNewCfgVlanClear_Object = MibScalar
igmpSnoopNewCfgVlanClear = _IgmpSnoopNewCfgVlanClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 20),
    _IgmpSnoopNewCfgVlanClear_Type()
)
igmpSnoopNewCfgVlanClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopNewCfgVlanClear.setStatus("current")
_IgmpSnoopCurCfgVlanBmap_Type = OctetString
_IgmpSnoopCurCfgVlanBmap_Object = MibScalar
igmpSnoopCurCfgVlanBmap = _IgmpSnoopCurCfgVlanBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 21),
    _IgmpSnoopCurCfgVlanBmap_Type()
)
igmpSnoopCurCfgVlanBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopCurCfgVlanBmap.setStatus("current")
_IgmpSnoopNewCfgVlanBmap_Type = OctetString
_IgmpSnoopNewCfgVlanBmap_Object = MibScalar
igmpSnoopNewCfgVlanBmap = _IgmpSnoopNewCfgVlanBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 22),
    _IgmpSnoopNewCfgVlanBmap_Type()
)
igmpSnoopNewCfgVlanBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopNewCfgVlanBmap.setStatus("current")
_IgmpSnoopCurCfgQInterval_Type = Integer32
_IgmpSnoopCurCfgQInterval_Object = MibScalar
igmpSnoopCurCfgQInterval = _IgmpSnoopCurCfgQInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 23),
    _IgmpSnoopCurCfgQInterval_Type()
)
igmpSnoopCurCfgQInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopCurCfgQInterval.setStatus("current")
_IgmpSnoopNewCfgQInterval_Type = Integer32
_IgmpSnoopNewCfgQInterval_Object = MibScalar
igmpSnoopNewCfgQInterval = _IgmpSnoopNewCfgQInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 24),
    _IgmpSnoopNewCfgQInterval_Type()
)
igmpSnoopNewCfgQInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopNewCfgQInterval.setStatus("current")
_IgmpSnoopCurCfgSrcIp_Type = IpAddress
_IgmpSnoopCurCfgSrcIp_Object = MibScalar
igmpSnoopCurCfgSrcIp = _IgmpSnoopCurCfgSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 25),
    _IgmpSnoopCurCfgSrcIp_Type()
)
igmpSnoopCurCfgSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopCurCfgSrcIp.setStatus("current")
_IgmpSnoopNewCfgSrcIp_Type = IpAddress
_IgmpSnoopNewCfgSrcIp_Object = MibScalar
igmpSnoopNewCfgSrcIp = _IgmpSnoopNewCfgSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 26),
    _IgmpSnoopNewCfgSrcIp_Type()
)
igmpSnoopNewCfgSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopNewCfgSrcIp.setStatus("current")


class _IgmpSnoopCurCfgAggrEnaDis_Type(Integer32):
    """Custom type igmpSnoopCurCfgAggrEnaDis based on Integer32"""
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


_IgmpSnoopCurCfgAggrEnaDis_Type.__name__ = "Integer32"
_IgmpSnoopCurCfgAggrEnaDis_Object = MibScalar
igmpSnoopCurCfgAggrEnaDis = _IgmpSnoopCurCfgAggrEnaDis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 27),
    _IgmpSnoopCurCfgAggrEnaDis_Type()
)
igmpSnoopCurCfgAggrEnaDis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopCurCfgAggrEnaDis.setStatus("current")


class _IgmpSnoopNewCfgAggrEnaDis_Type(Integer32):
    """Custom type igmpSnoopNewCfgAggrEnaDis based on Integer32"""
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


_IgmpSnoopNewCfgAggrEnaDis_Type.__name__ = "Integer32"
_IgmpSnoopNewCfgAggrEnaDis_Object = MibScalar
igmpSnoopNewCfgAggrEnaDis = _IgmpSnoopNewCfgAggrEnaDis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 3, 1, 28),
    _IgmpSnoopNewCfgAggrEnaDis_Type()
)
igmpSnoopNewCfgAggrEnaDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopNewCfgAggrEnaDis.setStatus("current")
_IgmpStaticMrtrCfg_ObjectIdentity = ObjectIdentity
igmpStaticMrtrCfg = _IgmpStaticMrtrCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 4)
)
_IgmpStaticMrtrCurCfgTable_Object = MibTable
igmpStaticMrtrCurCfgTable = _IgmpStaticMrtrCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 4, 1)
)
if mibBuilder.loadTexts:
    igmpStaticMrtrCurCfgTable.setStatus("current")
_IgmpStaticMrtrCurCfgTableEntry_Object = MibTableRow
igmpStaticMrtrCurCfgTableEntry = _IgmpStaticMrtrCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 4, 1, 1)
)
igmpStaticMrtrCurCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "igmpStaticMrtrCurCfgIndx"),
)
if mibBuilder.loadTexts:
    igmpStaticMrtrCurCfgTableEntry.setStatus("current")
_IgmpStaticMrtrCurCfgIndx_Type = Integer32
_IgmpStaticMrtrCurCfgIndx_Object = MibTableColumn
igmpStaticMrtrCurCfgIndx = _IgmpStaticMrtrCurCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 4, 1, 1, 1),
    _IgmpStaticMrtrCurCfgIndx_Type()
)
igmpStaticMrtrCurCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpStaticMrtrCurCfgIndx.setStatus("current")
_IgmpStaticMrtrCurCfgPortId_Type = Integer32
_IgmpStaticMrtrCurCfgPortId_Object = MibTableColumn
igmpStaticMrtrCurCfgPortId = _IgmpStaticMrtrCurCfgPortId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 4, 1, 1, 2),
    _IgmpStaticMrtrCurCfgPortId_Type()
)
igmpStaticMrtrCurCfgPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpStaticMrtrCurCfgPortId.setStatus("current")
_IgmpStaticMrtrCurCfgVlanId_Type = Integer32
_IgmpStaticMrtrCurCfgVlanId_Object = MibTableColumn
igmpStaticMrtrCurCfgVlanId = _IgmpStaticMrtrCurCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 4, 1, 1, 3),
    _IgmpStaticMrtrCurCfgVlanId_Type()
)
igmpStaticMrtrCurCfgVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpStaticMrtrCurCfgVlanId.setStatus("current")


class _IgmpStaticMrtrCurCfgVersion_Type(Integer32):
    """Custom type igmpStaticMrtrCurCfgVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_IgmpStaticMrtrCurCfgVersion_Type.__name__ = "Integer32"
_IgmpStaticMrtrCurCfgVersion_Object = MibTableColumn
igmpStaticMrtrCurCfgVersion = _IgmpStaticMrtrCurCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 4, 1, 1, 4),
    _IgmpStaticMrtrCurCfgVersion_Type()
)
igmpStaticMrtrCurCfgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpStaticMrtrCurCfgVersion.setStatus("current")
_IgmpStaticMrtrNewCfgTable_Object = MibTable
igmpStaticMrtrNewCfgTable = _IgmpStaticMrtrNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 4, 2)
)
if mibBuilder.loadTexts:
    igmpStaticMrtrNewCfgTable.setStatus("current")
_IgmpStaticMrtrNewCfgTableEntry_Object = MibTableRow
igmpStaticMrtrNewCfgTableEntry = _IgmpStaticMrtrNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 4, 2, 1)
)
igmpStaticMrtrNewCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "igmpStaticMrtrNewCfgIndx"),
)
if mibBuilder.loadTexts:
    igmpStaticMrtrNewCfgTableEntry.setStatus("current")
_IgmpStaticMrtrNewCfgIndx_Type = Integer32
_IgmpStaticMrtrNewCfgIndx_Object = MibTableColumn
igmpStaticMrtrNewCfgIndx = _IgmpStaticMrtrNewCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 4, 2, 1, 1),
    _IgmpStaticMrtrNewCfgIndx_Type()
)
igmpStaticMrtrNewCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpStaticMrtrNewCfgIndx.setStatus("current")
_IgmpStaticMrtrNewCfgPortId_Type = Integer32
_IgmpStaticMrtrNewCfgPortId_Object = MibTableColumn
igmpStaticMrtrNewCfgPortId = _IgmpStaticMrtrNewCfgPortId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 4, 2, 1, 2),
    _IgmpStaticMrtrNewCfgPortId_Type()
)
igmpStaticMrtrNewCfgPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpStaticMrtrNewCfgPortId.setStatus("current")
_IgmpStaticMrtrNewCfgVlanId_Type = Integer32
_IgmpStaticMrtrNewCfgVlanId_Object = MibTableColumn
igmpStaticMrtrNewCfgVlanId = _IgmpStaticMrtrNewCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 4, 2, 1, 3),
    _IgmpStaticMrtrNewCfgVlanId_Type()
)
igmpStaticMrtrNewCfgVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpStaticMrtrNewCfgVlanId.setStatus("current")


class _IgmpStaticMrtrNewCfgVersion_Type(Integer32):
    """Custom type igmpStaticMrtrNewCfgVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_IgmpStaticMrtrNewCfgVersion_Type.__name__ = "Integer32"
_IgmpStaticMrtrNewCfgVersion_Object = MibTableColumn
igmpStaticMrtrNewCfgVersion = _IgmpStaticMrtrNewCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 4, 2, 1, 4),
    _IgmpStaticMrtrNewCfgVersion_Type()
)
igmpStaticMrtrNewCfgVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpStaticMrtrNewCfgVersion.setStatus("current")


class _IgmpStaticMrtrNewCfgDelete_Type(Integer32):
    """Custom type igmpStaticMrtrNewCfgDelete based on Integer32"""
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


_IgmpStaticMrtrNewCfgDelete_Type.__name__ = "Integer32"
_IgmpStaticMrtrNewCfgDelete_Object = MibTableColumn
igmpStaticMrtrNewCfgDelete = _IgmpStaticMrtrNewCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 4, 2, 1, 5),
    _IgmpStaticMrtrNewCfgDelete_Type()
)
igmpStaticMrtrNewCfgDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpStaticMrtrNewCfgDelete.setStatus("current")
_IgmpFilterCfg_ObjectIdentity = ObjectIdentity
igmpFilterCfg = _IgmpFilterCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5)
)
_IgmpFltCurCfgTable_Object = MibTable
igmpFltCurCfgTable = _IgmpFltCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 1)
)
if mibBuilder.loadTexts:
    igmpFltCurCfgTable.setStatus("current")
_IgmpFltCurCfgTableEntry_Object = MibTableRow
igmpFltCurCfgTableEntry = _IgmpFltCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 1, 1)
)
igmpFltCurCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "igmpFltCurCfgIndx"),
)
if mibBuilder.loadTexts:
    igmpFltCurCfgTableEntry.setStatus("current")
_IgmpFltCurCfgIndx_Type = Integer32
_IgmpFltCurCfgIndx_Object = MibTableColumn
igmpFltCurCfgIndx = _IgmpFltCurCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 1, 1, 1),
    _IgmpFltCurCfgIndx_Type()
)
igmpFltCurCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFltCurCfgIndx.setStatus("current")
_IgmpFltCurCfgMcastIp1_Type = IpAddress
_IgmpFltCurCfgMcastIp1_Object = MibTableColumn
igmpFltCurCfgMcastIp1 = _IgmpFltCurCfgMcastIp1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 1, 1, 2),
    _IgmpFltCurCfgMcastIp1_Type()
)
igmpFltCurCfgMcastIp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFltCurCfgMcastIp1.setStatus("current")
_IgmpFltCurCfgMcastIp2_Type = IpAddress
_IgmpFltCurCfgMcastIp2_Object = MibTableColumn
igmpFltCurCfgMcastIp2 = _IgmpFltCurCfgMcastIp2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 1, 1, 3),
    _IgmpFltCurCfgMcastIp2_Type()
)
igmpFltCurCfgMcastIp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFltCurCfgMcastIp2.setStatus("current")


class _IgmpFltCurCfgAction_Type(Integer32):
    """Custom type igmpFltCurCfgAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_IgmpFltCurCfgAction_Type.__name__ = "Integer32"
_IgmpFltCurCfgAction_Object = MibTableColumn
igmpFltCurCfgAction = _IgmpFltCurCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 1, 1, 4),
    _IgmpFltCurCfgAction_Type()
)
igmpFltCurCfgAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFltCurCfgAction.setStatus("current")


class _IgmpFltCurCfgState_Type(Integer32):
    """Custom type igmpFltCurCfgState based on Integer32"""
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


_IgmpFltCurCfgState_Type.__name__ = "Integer32"
_IgmpFltCurCfgState_Object = MibTableColumn
igmpFltCurCfgState = _IgmpFltCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 1, 1, 5),
    _IgmpFltCurCfgState_Type()
)
igmpFltCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFltCurCfgState.setStatus("current")
_IgmpFltNewCfgTable_Object = MibTable
igmpFltNewCfgTable = _IgmpFltNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 2)
)
if mibBuilder.loadTexts:
    igmpFltNewCfgTable.setStatus("current")
_IgmpFltNewCfgTableEntry_Object = MibTableRow
igmpFltNewCfgTableEntry = _IgmpFltNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 2, 1)
)
igmpFltNewCfgTableEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "igmpFltNewCfgIndx"),
)
if mibBuilder.loadTexts:
    igmpFltNewCfgTableEntry.setStatus("current")
_IgmpFltNewCfgIndx_Type = Integer32
_IgmpFltNewCfgIndx_Object = MibTableColumn
igmpFltNewCfgIndx = _IgmpFltNewCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 2, 1, 1),
    _IgmpFltNewCfgIndx_Type()
)
igmpFltNewCfgIndx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFltNewCfgIndx.setStatus("current")
_IgmpFltNewCfgMcastIp1_Type = IpAddress
_IgmpFltNewCfgMcastIp1_Object = MibTableColumn
igmpFltNewCfgMcastIp1 = _IgmpFltNewCfgMcastIp1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 2, 1, 2),
    _IgmpFltNewCfgMcastIp1_Type()
)
igmpFltNewCfgMcastIp1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFltNewCfgMcastIp1.setStatus("current")
_IgmpFltNewCfgMcastIp2_Type = IpAddress
_IgmpFltNewCfgMcastIp2_Object = MibTableColumn
igmpFltNewCfgMcastIp2 = _IgmpFltNewCfgMcastIp2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 2, 1, 3),
    _IgmpFltNewCfgMcastIp2_Type()
)
igmpFltNewCfgMcastIp2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFltNewCfgMcastIp2.setStatus("current")


class _IgmpFltNewCfgAction_Type(Integer32):
    """Custom type igmpFltNewCfgAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_IgmpFltNewCfgAction_Type.__name__ = "Integer32"
_IgmpFltNewCfgAction_Object = MibTableColumn
igmpFltNewCfgAction = _IgmpFltNewCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 2, 1, 4),
    _IgmpFltNewCfgAction_Type()
)
igmpFltNewCfgAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFltNewCfgAction.setStatus("current")


class _IgmpFltNewCfgState_Type(Integer32):
    """Custom type igmpFltNewCfgState based on Integer32"""
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


_IgmpFltNewCfgState_Type.__name__ = "Integer32"
_IgmpFltNewCfgState_Object = MibTableColumn
igmpFltNewCfgState = _IgmpFltNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 2, 1, 5),
    _IgmpFltNewCfgState_Type()
)
igmpFltNewCfgState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFltNewCfgState.setStatus("current")


class _IgmpFltNewCfgDelete_Type(Integer32):
    """Custom type igmpFltNewCfgDelete based on Integer32"""
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


_IgmpFltNewCfgDelete_Type.__name__ = "Integer32"
_IgmpFltNewCfgDelete_Object = MibTableColumn
igmpFltNewCfgDelete = _IgmpFltNewCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 2, 1, 6),
    _IgmpFltNewCfgDelete_Type()
)
igmpFltNewCfgDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFltNewCfgDelete.setStatus("current")
_IgmpFltCurCfgPortTable_Object = MibTable
igmpFltCurCfgPortTable = _IgmpFltCurCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 3)
)
if mibBuilder.loadTexts:
    igmpFltCurCfgPortTable.setStatus("current")
_IgmpFltCurCfgPortTableEntry_Object = MibTableRow
igmpFltCurCfgPortTableEntry = _IgmpFltCurCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 3, 1)
)
igmpFltCurCfgPortTableEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "igmpFltCurCfgPortIndx"),
)
if mibBuilder.loadTexts:
    igmpFltCurCfgPortTableEntry.setStatus("current")
_IgmpFltCurCfgPortIndx_Type = Integer32
_IgmpFltCurCfgPortIndx_Object = MibTableColumn
igmpFltCurCfgPortIndx = _IgmpFltCurCfgPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 3, 1, 1),
    _IgmpFltCurCfgPortIndx_Type()
)
igmpFltCurCfgPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFltCurCfgPortIndx.setStatus("current")


class _IgmpFltCurCfgPortState_Type(Integer32):
    """Custom type igmpFltCurCfgPortState based on Integer32"""
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


_IgmpFltCurCfgPortState_Type.__name__ = "Integer32"
_IgmpFltCurCfgPortState_Object = MibTableColumn
igmpFltCurCfgPortState = _IgmpFltCurCfgPortState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 3, 1, 2),
    _IgmpFltCurCfgPortState_Type()
)
igmpFltCurCfgPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFltCurCfgPortState.setStatus("current")


class _IgmpFltCurCfgPortFiltBmap_Type(OctetString):
    """Custom type igmpFltCurCfgPortFiltBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_IgmpFltCurCfgPortFiltBmap_Type.__name__ = "OctetString"
_IgmpFltCurCfgPortFiltBmap_Object = MibTableColumn
igmpFltCurCfgPortFiltBmap = _IgmpFltCurCfgPortFiltBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 3, 1, 3),
    _IgmpFltCurCfgPortFiltBmap_Type()
)
igmpFltCurCfgPortFiltBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFltCurCfgPortFiltBmap.setStatus("current")
_IgmpFltNewCfgPortTable_Object = MibTable
igmpFltNewCfgPortTable = _IgmpFltNewCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 4)
)
if mibBuilder.loadTexts:
    igmpFltNewCfgPortTable.setStatus("current")
_IgmpFltNewCfgPortTableEntry_Object = MibTableRow
igmpFltNewCfgPortTableEntry = _IgmpFltNewCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 4, 1)
)
igmpFltNewCfgPortTableEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "igmpFltNewCfgPortIndx"),
)
if mibBuilder.loadTexts:
    igmpFltNewCfgPortTableEntry.setStatus("current")
_IgmpFltNewCfgPortIndx_Type = Integer32
_IgmpFltNewCfgPortIndx_Object = MibTableColumn
igmpFltNewCfgPortIndx = _IgmpFltNewCfgPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 4, 1, 1),
    _IgmpFltNewCfgPortIndx_Type()
)
igmpFltNewCfgPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFltNewCfgPortIndx.setStatus("current")


class _IgmpFltNewCfgPortState_Type(Integer32):
    """Custom type igmpFltNewCfgPortState based on Integer32"""
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


_IgmpFltNewCfgPortState_Type.__name__ = "Integer32"
_IgmpFltNewCfgPortState_Object = MibTableColumn
igmpFltNewCfgPortState = _IgmpFltNewCfgPortState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 4, 1, 2),
    _IgmpFltNewCfgPortState_Type()
)
igmpFltNewCfgPortState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFltNewCfgPortState.setStatus("current")


class _IgmpFltNewCfgPortFiltBmap_Type(OctetString):
    """Custom type igmpFltNewCfgPortFiltBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_IgmpFltNewCfgPortFiltBmap_Type.__name__ = "OctetString"
_IgmpFltNewCfgPortFiltBmap_Object = MibTableColumn
igmpFltNewCfgPortFiltBmap = _IgmpFltNewCfgPortFiltBmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 4, 1, 3),
    _IgmpFltNewCfgPortFiltBmap_Type()
)
igmpFltNewCfgPortFiltBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFltNewCfgPortFiltBmap.setStatus("current")
_IgmpFltNewCfgPortAddFiltRule_Type = Integer32
_IgmpFltNewCfgPortAddFiltRule_Object = MibTableColumn
igmpFltNewCfgPortAddFiltRule = _IgmpFltNewCfgPortAddFiltRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 4, 1, 4),
    _IgmpFltNewCfgPortAddFiltRule_Type()
)
igmpFltNewCfgPortAddFiltRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFltNewCfgPortAddFiltRule.setStatus("current")
_IgmpFltNewCfgPortRemFiltRule_Type = Integer32
_IgmpFltNewCfgPortRemFiltRule_Object = MibTableColumn
igmpFltNewCfgPortRemFiltRule = _IgmpFltNewCfgPortRemFiltRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 4, 1, 5),
    _IgmpFltNewCfgPortRemFiltRule_Type()
)
igmpFltNewCfgPortRemFiltRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFltNewCfgPortRemFiltRule.setStatus("current")


class _IgmpFltCurCfgEnaDis_Type(Integer32):
    """Custom type igmpFltCurCfgEnaDis based on Integer32"""
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


_IgmpFltCurCfgEnaDis_Type.__name__ = "Integer32"
_IgmpFltCurCfgEnaDis_Object = MibScalar
igmpFltCurCfgEnaDis = _IgmpFltCurCfgEnaDis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 5),
    _IgmpFltCurCfgEnaDis_Type()
)
igmpFltCurCfgEnaDis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFltCurCfgEnaDis.setStatus("current")


class _IgmpFltNewCfgEnaDis_Type(Integer32):
    """Custom type igmpFltNewCfgEnaDis based on Integer32"""
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


_IgmpFltNewCfgEnaDis_Type.__name__ = "Integer32"
_IgmpFltNewCfgEnaDis_Object = MibScalar
igmpFltNewCfgEnaDis = _IgmpFltNewCfgEnaDis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 15, 5, 6),
    _IgmpFltNewCfgEnaDis_Type()
)
igmpFltNewCfgEnaDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpFltNewCfgEnaDis.setStatus("current")
_Rip2Cfg_ObjectIdentity = ObjectIdentity
rip2Cfg = _Rip2Cfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18)
)
_RipCurCfgIntfTable_Object = MibTable
ripCurCfgIntfTable = _RipCurCfgIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 1)
)
if mibBuilder.loadTexts:
    ripCurCfgIntfTable.setStatus("current")
_RipCurCfgIntfEntry_Object = MibTableRow
ripCurCfgIntfEntry = _RipCurCfgIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 1, 1)
)
ripCurCfgIntfEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ripCurCfgIntfIndex"),
)
if mibBuilder.loadTexts:
    ripCurCfgIntfEntry.setStatus("current")
_RipCurCfgIntfIndex_Type = Integer32
_RipCurCfgIntfIndex_Object = MibTableColumn
ripCurCfgIntfIndex = _RipCurCfgIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 1, 1, 1),
    _RipCurCfgIntfIndex_Type()
)
ripCurCfgIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfIndex.setStatus("current")


class _RipCurCfgIntfVersion_Type(Integer32):
    """Custom type ripCurCfgIntfVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ripVersion1", 1),
          ("ripVersion2", 2))
    )


_RipCurCfgIntfVersion_Type.__name__ = "Integer32"
_RipCurCfgIntfVersion_Object = MibTableColumn
ripCurCfgIntfVersion = _RipCurCfgIntfVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 1, 1, 2),
    _RipCurCfgIntfVersion_Type()
)
ripCurCfgIntfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfVersion.setStatus("current")


class _RipCurCfgIntfSupply_Type(Integer32):
    """Custom type ripCurCfgIntfSupply based on Integer32"""
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


_RipCurCfgIntfSupply_Type.__name__ = "Integer32"
_RipCurCfgIntfSupply_Object = MibTableColumn
ripCurCfgIntfSupply = _RipCurCfgIntfSupply_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 1, 1, 3),
    _RipCurCfgIntfSupply_Type()
)
ripCurCfgIntfSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfSupply.setStatus("current")


class _RipCurCfgIntfListen_Type(Integer32):
    """Custom type ripCurCfgIntfListen based on Integer32"""
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


_RipCurCfgIntfListen_Type.__name__ = "Integer32"
_RipCurCfgIntfListen_Object = MibTableColumn
ripCurCfgIntfListen = _RipCurCfgIntfListen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 1, 1, 4),
    _RipCurCfgIntfListen_Type()
)
ripCurCfgIntfListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfListen.setStatus("current")


class _RipCurCfgIntfDefault_Type(Integer32):
    """Custom type ripCurCfgIntfDefault based on Integer32"""
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
        *(("both", 1),
          ("listen", 2),
          ("none", 4),
          ("supply", 3))
    )


_RipCurCfgIntfDefault_Type.__name__ = "Integer32"
_RipCurCfgIntfDefault_Object = MibTableColumn
ripCurCfgIntfDefault = _RipCurCfgIntfDefault_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 1, 1, 5),
    _RipCurCfgIntfDefault_Type()
)
ripCurCfgIntfDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfDefault.setStatus("current")


class _RipCurCfgIntfTrigUpdate_Type(Integer32):
    """Custom type ripCurCfgIntfTrigUpdate based on Integer32"""
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


_RipCurCfgIntfTrigUpdate_Type.__name__ = "Integer32"
_RipCurCfgIntfTrigUpdate_Object = MibTableColumn
ripCurCfgIntfTrigUpdate = _RipCurCfgIntfTrigUpdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 1, 1, 6),
    _RipCurCfgIntfTrigUpdate_Type()
)
ripCurCfgIntfTrigUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfTrigUpdate.setStatus("current")


class _RipCurCfgIntfMcastUpdate_Type(Integer32):
    """Custom type ripCurCfgIntfMcastUpdate based on Integer32"""
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


_RipCurCfgIntfMcastUpdate_Type.__name__ = "Integer32"
_RipCurCfgIntfMcastUpdate_Object = MibTableColumn
ripCurCfgIntfMcastUpdate = _RipCurCfgIntfMcastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 1, 1, 7),
    _RipCurCfgIntfMcastUpdate_Type()
)
ripCurCfgIntfMcastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfMcastUpdate.setStatus("current")


class _RipCurCfgIntfPoisonReverse_Type(Integer32):
    """Custom type ripCurCfgIntfPoisonReverse based on Integer32"""
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


_RipCurCfgIntfPoisonReverse_Type.__name__ = "Integer32"
_RipCurCfgIntfPoisonReverse_Object = MibTableColumn
ripCurCfgIntfPoisonReverse = _RipCurCfgIntfPoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 1, 1, 8),
    _RipCurCfgIntfPoisonReverse_Type()
)
ripCurCfgIntfPoisonReverse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfPoisonReverse.setStatus("current")


class _RipCurCfgIntfState_Type(Integer32):
    """Custom type ripCurCfgIntfState based on Integer32"""
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


_RipCurCfgIntfState_Type.__name__ = "Integer32"
_RipCurCfgIntfState_Object = MibTableColumn
ripCurCfgIntfState = _RipCurCfgIntfState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 1, 1, 9),
    _RipCurCfgIntfState_Type()
)
ripCurCfgIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfState.setStatus("current")


class _RipCurCfgIntfMetric_Type(Integer32):
    """Custom type ripCurCfgIntfMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RipCurCfgIntfMetric_Type.__name__ = "Integer32"
_RipCurCfgIntfMetric_Object = MibTableColumn
ripCurCfgIntfMetric = _RipCurCfgIntfMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 1, 1, 10),
    _RipCurCfgIntfMetric_Type()
)
ripCurCfgIntfMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfMetric.setStatus("current")


class _RipCurCfgIntfAuth_Type(Integer32):
    """Custom type ripCurCfgIntfAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("password", 2))
    )


_RipCurCfgIntfAuth_Type.__name__ = "Integer32"
_RipCurCfgIntfAuth_Object = MibTableColumn
ripCurCfgIntfAuth = _RipCurCfgIntfAuth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 1, 1, 11),
    _RipCurCfgIntfAuth_Type()
)
ripCurCfgIntfAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfAuth.setStatus("current")


class _RipCurCfgIntfKey_Type(DisplayString):
    """Custom type ripCurCfgIntfKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RipCurCfgIntfKey_Type.__name__ = "DisplayString"
_RipCurCfgIntfKey_Object = MibTableColumn
ripCurCfgIntfKey = _RipCurCfgIntfKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 1, 1, 12),
    _RipCurCfgIntfKey_Type()
)
ripCurCfgIntfKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfKey.setStatus("current")


class _RipCurCfgIntfSplitHorizon_Type(Integer32):
    """Custom type ripCurCfgIntfSplitHorizon based on Integer32"""
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


_RipCurCfgIntfSplitHorizon_Type.__name__ = "Integer32"
_RipCurCfgIntfSplitHorizon_Object = MibTableColumn
ripCurCfgIntfSplitHorizon = _RipCurCfgIntfSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 1, 1, 13),
    _RipCurCfgIntfSplitHorizon_Type()
)
ripCurCfgIntfSplitHorizon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfSplitHorizon.setStatus("current")
_RipNewCfgIntfTable_Object = MibTable
ripNewCfgIntfTable = _RipNewCfgIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 2)
)
if mibBuilder.loadTexts:
    ripNewCfgIntfTable.setStatus("current")
_RipNewCfgIntfEntry_Object = MibTableRow
ripNewCfgIntfEntry = _RipNewCfgIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 2, 1)
)
ripNewCfgIntfEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ripNewCfgIntfIndex"),
)
if mibBuilder.loadTexts:
    ripNewCfgIntfEntry.setStatus("current")
_RipNewCfgIntfIndex_Type = Integer32
_RipNewCfgIntfIndex_Object = MibTableColumn
ripNewCfgIntfIndex = _RipNewCfgIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 2, 1, 1),
    _RipNewCfgIntfIndex_Type()
)
ripNewCfgIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripNewCfgIntfIndex.setStatus("current")


class _RipNewCfgIntfVersion_Type(Integer32):
    """Custom type ripNewCfgIntfVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ripVersion1", 1),
          ("ripVersion2", 2))
    )


_RipNewCfgIntfVersion_Type.__name__ = "Integer32"
_RipNewCfgIntfVersion_Object = MibTableColumn
ripNewCfgIntfVersion = _RipNewCfgIntfVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 2, 1, 2),
    _RipNewCfgIntfVersion_Type()
)
ripNewCfgIntfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgIntfVersion.setStatus("current")


class _RipNewCfgIntfSupply_Type(Integer32):
    """Custom type ripNewCfgIntfSupply based on Integer32"""
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


_RipNewCfgIntfSupply_Type.__name__ = "Integer32"
_RipNewCfgIntfSupply_Object = MibTableColumn
ripNewCfgIntfSupply = _RipNewCfgIntfSupply_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 2, 1, 3),
    _RipNewCfgIntfSupply_Type()
)
ripNewCfgIntfSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgIntfSupply.setStatus("current")


class _RipNewCfgIntfListen_Type(Integer32):
    """Custom type ripNewCfgIntfListen based on Integer32"""
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


_RipNewCfgIntfListen_Type.__name__ = "Integer32"
_RipNewCfgIntfListen_Object = MibTableColumn
ripNewCfgIntfListen = _RipNewCfgIntfListen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 2, 1, 4),
    _RipNewCfgIntfListen_Type()
)
ripNewCfgIntfListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgIntfListen.setStatus("current")


class _RipNewCfgIntfDefault_Type(Integer32):
    """Custom type ripNewCfgIntfDefault based on Integer32"""
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
        *(("both", 1),
          ("listen", 2),
          ("none", 4),
          ("supply", 3))
    )


_RipNewCfgIntfDefault_Type.__name__ = "Integer32"
_RipNewCfgIntfDefault_Object = MibTableColumn
ripNewCfgIntfDefault = _RipNewCfgIntfDefault_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 2, 1, 5),
    _RipNewCfgIntfDefault_Type()
)
ripNewCfgIntfDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripNewCfgIntfDefault.setStatus("current")


class _RipNewCfgIntfTrigUpdate_Type(Integer32):
    """Custom type ripNewCfgIntfTrigUpdate based on Integer32"""
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


_RipNewCfgIntfTrigUpdate_Type.__name__ = "Integer32"
_RipNewCfgIntfTrigUpdate_Object = MibTableColumn
ripNewCfgIntfTrigUpdate = _RipNewCfgIntfTrigUpdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 2, 1, 6),
    _RipNewCfgIntfTrigUpdate_Type()
)
ripNewCfgIntfTrigUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgIntfTrigUpdate.setStatus("current")


class _RipNewCfgIntfMcastUpdate_Type(Integer32):
    """Custom type ripNewCfgIntfMcastUpdate based on Integer32"""
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


_RipNewCfgIntfMcastUpdate_Type.__name__ = "Integer32"
_RipNewCfgIntfMcastUpdate_Object = MibTableColumn
ripNewCfgIntfMcastUpdate = _RipNewCfgIntfMcastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 2, 1, 7),
    _RipNewCfgIntfMcastUpdate_Type()
)
ripNewCfgIntfMcastUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgIntfMcastUpdate.setStatus("current")


class _RipNewCfgIntfPoisonReverse_Type(Integer32):
    """Custom type ripNewCfgIntfPoisonReverse based on Integer32"""
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


_RipNewCfgIntfPoisonReverse_Type.__name__ = "Integer32"
_RipNewCfgIntfPoisonReverse_Object = MibTableColumn
ripNewCfgIntfPoisonReverse = _RipNewCfgIntfPoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 2, 1, 8),
    _RipNewCfgIntfPoisonReverse_Type()
)
ripNewCfgIntfPoisonReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgIntfPoisonReverse.setStatus("current")


class _RipNewCfgIntfState_Type(Integer32):
    """Custom type ripNewCfgIntfState based on Integer32"""
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


_RipNewCfgIntfState_Type.__name__ = "Integer32"
_RipNewCfgIntfState_Object = MibTableColumn
ripNewCfgIntfState = _RipNewCfgIntfState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 2, 1, 9),
    _RipNewCfgIntfState_Type()
)
ripNewCfgIntfState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripNewCfgIntfState.setStatus("current")


class _RipNewCfgIntfMetric_Type(Integer32):
    """Custom type ripNewCfgIntfMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RipNewCfgIntfMetric_Type.__name__ = "Integer32"
_RipNewCfgIntfMetric_Object = MibTableColumn
ripNewCfgIntfMetric = _RipNewCfgIntfMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 2, 1, 10),
    _RipNewCfgIntfMetric_Type()
)
ripNewCfgIntfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgIntfMetric.setStatus("current")


class _RipNewCfgIntfAuth_Type(Integer32):
    """Custom type ripNewCfgIntfAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("password", 2))
    )


_RipNewCfgIntfAuth_Type.__name__ = "Integer32"
_RipNewCfgIntfAuth_Object = MibTableColumn
ripNewCfgIntfAuth = _RipNewCfgIntfAuth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 2, 1, 11),
    _RipNewCfgIntfAuth_Type()
)
ripNewCfgIntfAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgIntfAuth.setStatus("current")


class _RipNewCfgIntfKey_Type(DisplayString):
    """Custom type ripNewCfgIntfKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RipNewCfgIntfKey_Type.__name__ = "DisplayString"
_RipNewCfgIntfKey_Object = MibTableColumn
ripNewCfgIntfKey = _RipNewCfgIntfKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 2, 1, 12),
    _RipNewCfgIntfKey_Type()
)
ripNewCfgIntfKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripNewCfgIntfKey.setStatus("current")


class _RipNewCfgIntfSplitHorizon_Type(Integer32):
    """Custom type ripNewCfgIntfSplitHorizon based on Integer32"""
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


_RipNewCfgIntfSplitHorizon_Type.__name__ = "Integer32"
_RipNewCfgIntfSplitHorizon_Object = MibTableColumn
ripNewCfgIntfSplitHorizon = _RipNewCfgIntfSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 2, 1, 13),
    _RipNewCfgIntfSplitHorizon_Type()
)
ripNewCfgIntfSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgIntfSplitHorizon.setStatus("current")
_RipGeneral_ObjectIdentity = ObjectIdentity
ripGeneral = _RipGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 3)
)


class _Rip2CurCfgState_Type(Integer32):
    """Custom type rip2CurCfgState based on Integer32"""
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


_Rip2CurCfgState_Type.__name__ = "Integer32"
_Rip2CurCfgState_Object = MibScalar
rip2CurCfgState = _Rip2CurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 3, 1),
    _Rip2CurCfgState_Type()
)
rip2CurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2CurCfgState.setStatus("current")


class _Rip2NewCfgState_Type(Integer32):
    """Custom type rip2NewCfgState based on Integer32"""
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


_Rip2NewCfgState_Type.__name__ = "Integer32"
_Rip2NewCfgState_Object = MibScalar
rip2NewCfgState = _Rip2NewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 3, 2),
    _Rip2NewCfgState_Type()
)
rip2NewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2NewCfgState.setStatus("current")


class _Rip2CurCfgUpdatePeriod_Type(Integer32):
    """Custom type rip2CurCfgUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Rip2CurCfgUpdatePeriod_Type.__name__ = "Integer32"
_Rip2CurCfgUpdatePeriod_Object = MibScalar
rip2CurCfgUpdatePeriod = _Rip2CurCfgUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 3, 3),
    _Rip2CurCfgUpdatePeriod_Type()
)
rip2CurCfgUpdatePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2CurCfgUpdatePeriod.setStatus("current")


class _Rip2NewCfgUpdatePeriod_Type(Integer32):
    """Custom type rip2NewCfgUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Rip2NewCfgUpdatePeriod_Type.__name__ = "Integer32"
_Rip2NewCfgUpdatePeriod_Object = MibScalar
rip2NewCfgUpdatePeriod = _Rip2NewCfgUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 3, 4),
    _Rip2NewCfgUpdatePeriod_Type()
)
rip2NewCfgUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2NewCfgUpdatePeriod.setStatus("current")
_RipRouteRedistribution_ObjectIdentity = ObjectIdentity
ripRouteRedistribution = _RipRouteRedistribution_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4)
)
_RipRedistributeStatic_ObjectIdentity = ObjectIdentity
ripRedistributeStatic = _RipRedistributeStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 1)
)


class _RipCurCfgStaticMetric_Type(Integer32):
    """Custom type ripCurCfgStaticMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RipCurCfgStaticMetric_Type.__name__ = "Integer32"
_RipCurCfgStaticMetric_Object = MibScalar
ripCurCfgStaticMetric = _RipCurCfgStaticMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 1, 1),
    _RipCurCfgStaticMetric_Type()
)
ripCurCfgStaticMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgStaticMetric.setStatus("current")


class _RipNewCfgStaticMetric_Type(Integer32):
    """Custom type ripNewCfgStaticMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RipNewCfgStaticMetric_Type.__name__ = "Integer32"
_RipNewCfgStaticMetric_Object = MibScalar
ripNewCfgStaticMetric = _RipNewCfgStaticMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 1, 2),
    _RipNewCfgStaticMetric_Type()
)
ripNewCfgStaticMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgStaticMetric.setStatus("current")
_RipCurCfgStaticOutRmapList_Type = OctetString
_RipCurCfgStaticOutRmapList_Object = MibScalar
ripCurCfgStaticOutRmapList = _RipCurCfgStaticOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 1, 5),
    _RipCurCfgStaticOutRmapList_Type()
)
ripCurCfgStaticOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgStaticOutRmapList.setStatus("current")
_RipNewCfgStaticOutRmapList_Type = OctetString
_RipNewCfgStaticOutRmapList_Object = MibScalar
ripNewCfgStaticOutRmapList = _RipNewCfgStaticOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 1, 6),
    _RipNewCfgStaticOutRmapList_Type()
)
ripNewCfgStaticOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripNewCfgStaticOutRmapList.setStatus("current")
_RipNewCfgStaticAddOutRmap_Type = Integer32
_RipNewCfgStaticAddOutRmap_Object = MibScalar
ripNewCfgStaticAddOutRmap = _RipNewCfgStaticAddOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 1, 7),
    _RipNewCfgStaticAddOutRmap_Type()
)
ripNewCfgStaticAddOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgStaticAddOutRmap.setStatus("current")
_RipNewCfgStaticRemoveOutRmap_Type = Integer32
_RipNewCfgStaticRemoveOutRmap_Object = MibScalar
ripNewCfgStaticRemoveOutRmap = _RipNewCfgStaticRemoveOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 1, 8),
    _RipNewCfgStaticRemoveOutRmap_Type()
)
ripNewCfgStaticRemoveOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgStaticRemoveOutRmap.setStatus("current")
_RipRedistributeFixed_ObjectIdentity = ObjectIdentity
ripRedistributeFixed = _RipRedistributeFixed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 4)
)


class _RipCurCfgFixedMetric_Type(Integer32):
    """Custom type ripCurCfgFixedMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RipCurCfgFixedMetric_Type.__name__ = "Integer32"
_RipCurCfgFixedMetric_Object = MibScalar
ripCurCfgFixedMetric = _RipCurCfgFixedMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 4, 1),
    _RipCurCfgFixedMetric_Type()
)
ripCurCfgFixedMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgFixedMetric.setStatus("current")


class _RipNewCfgFixedMetric_Type(Integer32):
    """Custom type ripNewCfgFixedMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RipNewCfgFixedMetric_Type.__name__ = "Integer32"
_RipNewCfgFixedMetric_Object = MibScalar
ripNewCfgFixedMetric = _RipNewCfgFixedMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 4, 2),
    _RipNewCfgFixedMetric_Type()
)
ripNewCfgFixedMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgFixedMetric.setStatus("current")
_RipCurCfgFixedOutRmapList_Type = OctetString
_RipCurCfgFixedOutRmapList_Object = MibScalar
ripCurCfgFixedOutRmapList = _RipCurCfgFixedOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 4, 5),
    _RipCurCfgFixedOutRmapList_Type()
)
ripCurCfgFixedOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgFixedOutRmapList.setStatus("current")
_RipNewCfgFixedOutRmapList_Type = OctetString
_RipNewCfgFixedOutRmapList_Object = MibScalar
ripNewCfgFixedOutRmapList = _RipNewCfgFixedOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 4, 6),
    _RipNewCfgFixedOutRmapList_Type()
)
ripNewCfgFixedOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripNewCfgFixedOutRmapList.setStatus("current")
_RipNewCfgFixedAddOutRmap_Type = Integer32
_RipNewCfgFixedAddOutRmap_Object = MibScalar
ripNewCfgFixedAddOutRmap = _RipNewCfgFixedAddOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 4, 7),
    _RipNewCfgFixedAddOutRmap_Type()
)
ripNewCfgFixedAddOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgFixedAddOutRmap.setStatus("current")
_RipNewCfgFixedRemoveOutRmap_Type = Integer32
_RipNewCfgFixedRemoveOutRmap_Object = MibScalar
ripNewCfgFixedRemoveOutRmap = _RipNewCfgFixedRemoveOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 4, 8),
    _RipNewCfgFixedRemoveOutRmap_Type()
)
ripNewCfgFixedRemoveOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgFixedRemoveOutRmap.setStatus("current")
_RipRedistributeOspf_ObjectIdentity = ObjectIdentity
ripRedistributeOspf = _RipRedistributeOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 5)
)


class _RipCurCfgOspfMetric_Type(Integer32):
    """Custom type ripCurCfgOspfMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RipCurCfgOspfMetric_Type.__name__ = "Integer32"
_RipCurCfgOspfMetric_Object = MibScalar
ripCurCfgOspfMetric = _RipCurCfgOspfMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 5, 1),
    _RipCurCfgOspfMetric_Type()
)
ripCurCfgOspfMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgOspfMetric.setStatus("current")


class _RipNewCfgOspfMetric_Type(Integer32):
    """Custom type ripNewCfgOspfMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RipNewCfgOspfMetric_Type.__name__ = "Integer32"
_RipNewCfgOspfMetric_Object = MibScalar
ripNewCfgOspfMetric = _RipNewCfgOspfMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 5, 2),
    _RipNewCfgOspfMetric_Type()
)
ripNewCfgOspfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgOspfMetric.setStatus("current")
_RipCurCfgOspfOutRmapList_Type = OctetString
_RipCurCfgOspfOutRmapList_Object = MibScalar
ripCurCfgOspfOutRmapList = _RipCurCfgOspfOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 5, 5),
    _RipCurCfgOspfOutRmapList_Type()
)
ripCurCfgOspfOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgOspfOutRmapList.setStatus("current")
_RipNewCfgOspfOutRmapList_Type = OctetString
_RipNewCfgOspfOutRmapList_Object = MibScalar
ripNewCfgOspfOutRmapList = _RipNewCfgOspfOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 5, 6),
    _RipNewCfgOspfOutRmapList_Type()
)
ripNewCfgOspfOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripNewCfgOspfOutRmapList.setStatus("current")
_RipNewCfgOspfAddOutRmap_Type = Integer32
_RipNewCfgOspfAddOutRmap_Object = MibScalar
ripNewCfgOspfAddOutRmap = _RipNewCfgOspfAddOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 5, 7),
    _RipNewCfgOspfAddOutRmap_Type()
)
ripNewCfgOspfAddOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgOspfAddOutRmap.setStatus("current")
_RipNewCfgOspfRemoveOutRmap_Type = Integer32
_RipNewCfgOspfRemoveOutRmap_Object = MibScalar
ripNewCfgOspfRemoveOutRmap = _RipNewCfgOspfRemoveOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 5, 8),
    _RipNewCfgOspfRemoveOutRmap_Type()
)
ripNewCfgOspfRemoveOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgOspfRemoveOutRmap.setStatus("current")
_RipRedistributeEospf_ObjectIdentity = ObjectIdentity
ripRedistributeEospf = _RipRedistributeEospf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 6)
)


class _RipCurCfgEospfMetric_Type(Integer32):
    """Custom type ripCurCfgEospfMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RipCurCfgEospfMetric_Type.__name__ = "Integer32"
_RipCurCfgEospfMetric_Object = MibScalar
ripCurCfgEospfMetric = _RipCurCfgEospfMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 6, 1),
    _RipCurCfgEospfMetric_Type()
)
ripCurCfgEospfMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgEospfMetric.setStatus("current")


class _RipNewCfgEospfMetric_Type(Integer32):
    """Custom type ripNewCfgEospfMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RipNewCfgEospfMetric_Type.__name__ = "Integer32"
_RipNewCfgEospfMetric_Object = MibScalar
ripNewCfgEospfMetric = _RipNewCfgEospfMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 6, 2),
    _RipNewCfgEospfMetric_Type()
)
ripNewCfgEospfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgEospfMetric.setStatus("current")
_RipCurCfgEospfOutRmapList_Type = OctetString
_RipCurCfgEospfOutRmapList_Object = MibScalar
ripCurCfgEospfOutRmapList = _RipCurCfgEospfOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 6, 5),
    _RipCurCfgEospfOutRmapList_Type()
)
ripCurCfgEospfOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgEospfOutRmapList.setStatus("current")
_RipNewCfgEospfOutRmapList_Type = OctetString
_RipNewCfgEospfOutRmapList_Object = MibScalar
ripNewCfgEospfOutRmapList = _RipNewCfgEospfOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 6, 6),
    _RipNewCfgEospfOutRmapList_Type()
)
ripNewCfgEospfOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripNewCfgEospfOutRmapList.setStatus("current")
_RipNewCfgEospfAddOutRmap_Type = Integer32
_RipNewCfgEospfAddOutRmap_Object = MibScalar
ripNewCfgEospfAddOutRmap = _RipNewCfgEospfAddOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 6, 7),
    _RipNewCfgEospfAddOutRmap_Type()
)
ripNewCfgEospfAddOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgEospfAddOutRmap.setStatus("current")
_RipNewCfgEospfRemoveOutRmap_Type = Integer32
_RipNewCfgEospfRemoveOutRmap_Object = MibScalar
ripNewCfgEospfRemoveOutRmap = _RipNewCfgEospfRemoveOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 1, 18, 4, 6, 8),
    _RipNewCfgEospfRemoveOutRmap_Type()
)
ripNewCfgEospfRemoveOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgEospfRemoveOutRmap.setStatus("current")
_Layer3Stats_ObjectIdentity = ObjectIdentity
layer3Stats = _Layer3Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2)
)
_RipStats_ObjectIdentity = ObjectIdentity
ripStats = _RipStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 1)
)
_RipStatInPkts_Type = Counter32
_RipStatInPkts_Object = MibScalar
ripStatInPkts = _RipStatInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 1, 1),
    _RipStatInPkts_Type()
)
ripStatInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInPkts.setStatus("current")
_RipStatOutPkts_Type = Counter32
_RipStatOutPkts_Object = MibScalar
ripStatOutPkts = _RipStatOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 1, 2),
    _RipStatOutPkts_Type()
)
ripStatOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatOutPkts.setStatus("current")
_RipStatInErrorPkts_Type = Counter32
_RipStatInErrorPkts_Object = MibScalar
ripStatInErrorPkts = _RipStatInErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 1, 3),
    _RipStatInErrorPkts_Type()
)
ripStatInErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInErrorPkts.setStatus("current")
_RipStatRoutesAgedOut_Type = Counter32
_RipStatRoutesAgedOut_Object = MibScalar
ripStatRoutesAgedOut = _RipStatRoutesAgedOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 1, 4),
    _RipStatRoutesAgedOut_Type()
)
ripStatRoutesAgedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatRoutesAgedOut.setStatus("current")
_ArpStats_ObjectIdentity = ObjectIdentity
arpStats = _ArpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 2)
)
_ArpStatEntries_Type = Gauge32
_ArpStatEntries_Object = MibScalar
arpStatEntries = _ArpStatEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 2, 1),
    _ArpStatEntries_Type()
)
arpStatEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpStatEntries.setStatus("current")
_ArpStatHighWater_Type = Gauge32
_ArpStatHighWater_Object = MibScalar
arpStatHighWater = _ArpStatHighWater_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 2, 2),
    _ArpStatHighWater_Type()
)
arpStatHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpStatHighWater.setStatus("current")
_ArpStatMaxEntries_Type = Gauge32
_ArpStatMaxEntries_Object = MibScalar
arpStatMaxEntries = _ArpStatMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 2, 3),
    _ArpStatMaxEntries_Type()
)
arpStatMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpStatMaxEntries.setStatus("current")
_RouteStats_ObjectIdentity = ObjectIdentity
routeStats = _RouteStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 3)
)
_RouteStatEntries_Type = Gauge32
_RouteStatEntries_Object = MibScalar
routeStatEntries = _RouteStatEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 3, 1),
    _RouteStatEntries_Type()
)
routeStatEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatEntries.setStatus("current")
_RouteStatHighWater_Type = Gauge32
_RouteStatHighWater_Object = MibScalar
routeStatHighWater = _RouteStatHighWater_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 3, 2),
    _RouteStatHighWater_Type()
)
routeStatHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatHighWater.setStatus("current")
_RouteStatMaxEntries_Type = Gauge32
_RouteStatMaxEntries_Object = MibScalar
routeStatMaxEntries = _RouteStatMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 3, 3),
    _RouteStatMaxEntries_Type()
)
routeStatMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatMaxEntries.setStatus("current")
_VrrpStats_ObjectIdentity = ObjectIdentity
vrrpStats = _VrrpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 4)
)
_VrrpStatInAdvers_Type = Counter32
_VrrpStatInAdvers_Object = MibScalar
vrrpStatInAdvers = _VrrpStatInAdvers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 4, 1),
    _VrrpStatInAdvers_Type()
)
vrrpStatInAdvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatInAdvers.setStatus("current")
_VrrpStatOutAdvers_Type = Counter32
_VrrpStatOutAdvers_Object = MibScalar
vrrpStatOutAdvers = _VrrpStatOutAdvers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 4, 2),
    _VrrpStatOutAdvers_Type()
)
vrrpStatOutAdvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatOutAdvers.setStatus("current")
_VrrpStatOutBadAdvers_Type = Counter32
_VrrpStatOutBadAdvers_Object = MibScalar
vrrpStatOutBadAdvers = _VrrpStatOutBadAdvers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 4, 3),
    _VrrpStatOutBadAdvers_Type()
)
vrrpStatOutBadAdvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatOutBadAdvers.setStatus("current")
_VrrpStatBadVersion_Type = Counter32
_VrrpStatBadVersion_Object = MibScalar
vrrpStatBadVersion = _VrrpStatBadVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 4, 4),
    _VrrpStatBadVersion_Type()
)
vrrpStatBadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatBadVersion.setStatus("current")
_VrrpStatBadAddress_Type = Counter32
_VrrpStatBadAddress_Object = MibScalar
vrrpStatBadAddress = _VrrpStatBadAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 4, 5),
    _VrrpStatBadAddress_Type()
)
vrrpStatBadAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatBadAddress.setStatus("current")
_VrrpStatBadPassword_Type = Counter32
_VrrpStatBadPassword_Object = MibScalar
vrrpStatBadPassword = _VrrpStatBadPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 4, 6),
    _VrrpStatBadPassword_Type()
)
vrrpStatBadPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatBadPassword.setStatus("current")
_VrrpStatBadVrid_Type = Counter32
_VrrpStatBadVrid_Object = MibScalar
vrrpStatBadVrid = _VrrpStatBadVrid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 4, 7),
    _VrrpStatBadVrid_Type()
)
vrrpStatBadVrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatBadVrid.setStatus("current")
_VrrpStatBadData_Type = Counter32
_VrrpStatBadData_Object = MibScalar
vrrpStatBadData = _VrrpStatBadData_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 4, 8),
    _VrrpStatBadData_Type()
)
vrrpStatBadData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatBadData.setStatus("current")
_VrrpStatBadInterval_Type = Counter32
_VrrpStatBadInterval_Object = MibScalar
vrrpStatBadInterval = _VrrpStatBadInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 4, 9),
    _VrrpStatBadInterval_Type()
)
vrrpStatBadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatBadInterval.setStatus("current")
_OspfStats_ObjectIdentity = ObjectIdentity
ospfStats = _OspfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5)
)
_OspfGeneralStats_ObjectIdentity = ObjectIdentity
ospfGeneralStats = _OspfGeneralStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1)
)
_OspfCumRxTxStats_ObjectIdentity = ObjectIdentity
ospfCumRxTxStats = _OspfCumRxTxStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 1)
)
_OspfCumRxPkts_Type = Counter32
_OspfCumRxPkts_Object = MibScalar
ospfCumRxPkts = _OspfCumRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 1, 1),
    _OspfCumRxPkts_Type()
)
ospfCumRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumRxPkts.setStatus("current")
_OspfCumTxPkts_Type = Counter32
_OspfCumTxPkts_Object = MibScalar
ospfCumTxPkts = _OspfCumTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 1, 2),
    _OspfCumTxPkts_Type()
)
ospfCumTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumTxPkts.setStatus("current")
_OspfCumRxHello_Type = Counter32
_OspfCumRxHello_Object = MibScalar
ospfCumRxHello = _OspfCumRxHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 1, 3),
    _OspfCumRxHello_Type()
)
ospfCumRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumRxHello.setStatus("current")
_OspfCumTxHello_Type = Counter32
_OspfCumTxHello_Object = MibScalar
ospfCumTxHello = _OspfCumTxHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 1, 4),
    _OspfCumTxHello_Type()
)
ospfCumTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumTxHello.setStatus("current")
_OspfCumRxDatabase_Type = Counter32
_OspfCumRxDatabase_Object = MibScalar
ospfCumRxDatabase = _OspfCumRxDatabase_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 1, 5),
    _OspfCumRxDatabase_Type()
)
ospfCumRxDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumRxDatabase.setStatus("current")
_OspfCumTxDatabase_Type = Counter32
_OspfCumTxDatabase_Object = MibScalar
ospfCumTxDatabase = _OspfCumTxDatabase_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 1, 6),
    _OspfCumTxDatabase_Type()
)
ospfCumTxDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumTxDatabase.setStatus("current")
_OspfCumRxlsReqs_Type = Counter32
_OspfCumRxlsReqs_Object = MibScalar
ospfCumRxlsReqs = _OspfCumRxlsReqs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 1, 7),
    _OspfCumRxlsReqs_Type()
)
ospfCumRxlsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumRxlsReqs.setStatus("current")
_OspfCumTxlsReqs_Type = Counter32
_OspfCumTxlsReqs_Object = MibScalar
ospfCumTxlsReqs = _OspfCumTxlsReqs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 1, 8),
    _OspfCumTxlsReqs_Type()
)
ospfCumTxlsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumTxlsReqs.setStatus("current")
_OspfCumRxlsAcks_Type = Counter32
_OspfCumRxlsAcks_Object = MibScalar
ospfCumRxlsAcks = _OspfCumRxlsAcks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 1, 9),
    _OspfCumRxlsAcks_Type()
)
ospfCumRxlsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumRxlsAcks.setStatus("current")
_OspfCumTxlsAcks_Type = Counter32
_OspfCumTxlsAcks_Object = MibScalar
ospfCumTxlsAcks = _OspfCumTxlsAcks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 1, 10),
    _OspfCumTxlsAcks_Type()
)
ospfCumTxlsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumTxlsAcks.setStatus("current")
_OspfCumRxlsUpdates_Type = Counter32
_OspfCumRxlsUpdates_Object = MibScalar
ospfCumRxlsUpdates = _OspfCumRxlsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 1, 11),
    _OspfCumRxlsUpdates_Type()
)
ospfCumRxlsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumRxlsUpdates.setStatus("current")
_OspfCumTxlsUpdates_Type = Counter32
_OspfCumTxlsUpdates_Object = MibScalar
ospfCumTxlsUpdates = _OspfCumTxlsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 1, 12),
    _OspfCumTxlsUpdates_Type()
)
ospfCumTxlsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumTxlsUpdates.setStatus("current")
_OspfCumNbrChangeStats_ObjectIdentity = ObjectIdentity
ospfCumNbrChangeStats = _OspfCumNbrChangeStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 2)
)
_OspfCumNbrhello_Type = Counter32
_OspfCumNbrhello_Object = MibScalar
ospfCumNbrhello = _OspfCumNbrhello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 2, 1),
    _OspfCumNbrhello_Type()
)
ospfCumNbrhello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrhello.setStatus("current")
_OspfCumNbrStart_Type = Counter32
_OspfCumNbrStart_Object = MibScalar
ospfCumNbrStart = _OspfCumNbrStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 2, 2),
    _OspfCumNbrStart_Type()
)
ospfCumNbrStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrStart.setStatus("current")
_OspfCumNbrAdjointOk_Type = Counter32
_OspfCumNbrAdjointOk_Object = MibScalar
ospfCumNbrAdjointOk = _OspfCumNbrAdjointOk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 2, 3),
    _OspfCumNbrAdjointOk_Type()
)
ospfCumNbrAdjointOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrAdjointOk.setStatus("current")
_OspfCumNbrNegotiationDone_Type = Counter32
_OspfCumNbrNegotiationDone_Object = MibScalar
ospfCumNbrNegotiationDone = _OspfCumNbrNegotiationDone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 2, 4),
    _OspfCumNbrNegotiationDone_Type()
)
ospfCumNbrNegotiationDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrNegotiationDone.setStatus("current")
_OspfCumNbrExchangeDone_Type = Counter32
_OspfCumNbrExchangeDone_Object = MibScalar
ospfCumNbrExchangeDone = _OspfCumNbrExchangeDone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 2, 5),
    _OspfCumNbrExchangeDone_Type()
)
ospfCumNbrExchangeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrExchangeDone.setStatus("current")
_OspfCumNbrBadRequests_Type = Counter32
_OspfCumNbrBadRequests_Object = MibScalar
ospfCumNbrBadRequests = _OspfCumNbrBadRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 2, 6),
    _OspfCumNbrBadRequests_Type()
)
ospfCumNbrBadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrBadRequests.setStatus("current")
_OspfCumNbrBadSequence_Type = Counter32
_OspfCumNbrBadSequence_Object = MibScalar
ospfCumNbrBadSequence = _OspfCumNbrBadSequence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 2, 7),
    _OspfCumNbrBadSequence_Type()
)
ospfCumNbrBadSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrBadSequence.setStatus("current")
_OspfCumNbrLoadingDone_Type = Counter32
_OspfCumNbrLoadingDone_Object = MibScalar
ospfCumNbrLoadingDone = _OspfCumNbrLoadingDone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 2, 8),
    _OspfCumNbrLoadingDone_Type()
)
ospfCumNbrLoadingDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrLoadingDone.setStatus("current")
_OspfCumNbrN1way_Type = Counter32
_OspfCumNbrN1way_Object = MibScalar
ospfCumNbrN1way = _OspfCumNbrN1way_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 2, 9),
    _OspfCumNbrN1way_Type()
)
ospfCumNbrN1way.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrN1way.setStatus("current")
_OspfCumNbrRstAd_Type = Counter32
_OspfCumNbrRstAd_Object = MibScalar
ospfCumNbrRstAd = _OspfCumNbrRstAd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 2, 10),
    _OspfCumNbrRstAd_Type()
)
ospfCumNbrRstAd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrRstAd.setStatus("current")
_OspfCumNbrDown_Type = Counter32
_OspfCumNbrDown_Object = MibScalar
ospfCumNbrDown = _OspfCumNbrDown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 2, 11),
    _OspfCumNbrDown_Type()
)
ospfCumNbrDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrDown.setStatus("current")
_OspfCumNbrN2way_Type = Counter32
_OspfCumNbrN2way_Object = MibScalar
ospfCumNbrN2way = _OspfCumNbrN2way_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 2, 12),
    _OspfCumNbrN2way_Type()
)
ospfCumNbrN2way.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrN2way.setStatus("current")
_OspfCumIntfChangeStats_ObjectIdentity = ObjectIdentity
ospfCumIntfChangeStats = _OspfCumIntfChangeStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 3)
)
_OspfCumIntfHello_Type = Counter32
_OspfCumIntfHello_Object = MibScalar
ospfCumIntfHello = _OspfCumIntfHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 3, 1),
    _OspfCumIntfHello_Type()
)
ospfCumIntfHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfHello.setStatus("current")
_OspfCumIntfDown_Type = Counter32
_OspfCumIntfDown_Object = MibScalar
ospfCumIntfDown = _OspfCumIntfDown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 3, 2),
    _OspfCumIntfDown_Type()
)
ospfCumIntfDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfDown.setStatus("current")
_OspfCumIntfLoop_Type = Counter32
_OspfCumIntfLoop_Object = MibScalar
ospfCumIntfLoop = _OspfCumIntfLoop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 3, 3),
    _OspfCumIntfLoop_Type()
)
ospfCumIntfLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfLoop.setStatus("current")
_OspfCumIntfUnloop_Type = Counter32
_OspfCumIntfUnloop_Object = MibScalar
ospfCumIntfUnloop = _OspfCumIntfUnloop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 3, 4),
    _OspfCumIntfUnloop_Type()
)
ospfCumIntfUnloop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfUnloop.setStatus("current")
_OspfCumIntfWaitTimer_Type = Counter32
_OspfCumIntfWaitTimer_Object = MibScalar
ospfCumIntfWaitTimer = _OspfCumIntfWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 3, 5),
    _OspfCumIntfWaitTimer_Type()
)
ospfCumIntfWaitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfWaitTimer.setStatus("current")
_OspfCumIntfBackup_Type = Counter32
_OspfCumIntfBackup_Object = MibScalar
ospfCumIntfBackup = _OspfCumIntfBackup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 3, 6),
    _OspfCumIntfBackup_Type()
)
ospfCumIntfBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfBackup.setStatus("current")
_OspfCumIntfNbrChange_Type = Counter32
_OspfCumIntfNbrChange_Object = MibScalar
ospfCumIntfNbrChange = _OspfCumIntfNbrChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 3, 7),
    _OspfCumIntfNbrChange_Type()
)
ospfCumIntfNbrChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfNbrChange.setStatus("current")
_OspfTimersKickOffStats_ObjectIdentity = ObjectIdentity
ospfTimersKickOffStats = _OspfTimersKickOffStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 4)
)
_OspfTmrsKckOffHello_Type = Counter32
_OspfTmrsKckOffHello_Object = MibScalar
ospfTmrsKckOffHello = _OspfTmrsKckOffHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 4, 1),
    _OspfTmrsKckOffHello_Type()
)
ospfTmrsKckOffHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffHello.setStatus("current")
_OspfTmrsKckOffRetransmit_Type = Counter32
_OspfTmrsKckOffRetransmit_Object = MibScalar
ospfTmrsKckOffRetransmit = _OspfTmrsKckOffRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 4, 2),
    _OspfTmrsKckOffRetransmit_Type()
)
ospfTmrsKckOffRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffRetransmit.setStatus("current")
_OspfTmrsKckOffLsaLock_Type = Counter32
_OspfTmrsKckOffLsaLock_Object = MibScalar
ospfTmrsKckOffLsaLock = _OspfTmrsKckOffLsaLock_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 4, 3),
    _OspfTmrsKckOffLsaLock_Type()
)
ospfTmrsKckOffLsaLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffLsaLock.setStatus("current")
_OspfTmrsKckOffLsaAck_Type = Counter32
_OspfTmrsKckOffLsaAck_Object = MibScalar
ospfTmrsKckOffLsaAck = _OspfTmrsKckOffLsaAck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 4, 4),
    _OspfTmrsKckOffLsaAck_Type()
)
ospfTmrsKckOffLsaAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffLsaAck.setStatus("current")
_OspfTmrsKckOffDbage_Type = Counter32
_OspfTmrsKckOffDbage_Object = MibScalar
ospfTmrsKckOffDbage = _OspfTmrsKckOffDbage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 4, 5),
    _OspfTmrsKckOffDbage_Type()
)
ospfTmrsKckOffDbage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffDbage.setStatus("current")
_OspfTmrsKckOffSummary_Type = Counter32
_OspfTmrsKckOffSummary_Object = MibScalar
ospfTmrsKckOffSummary = _OspfTmrsKckOffSummary_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 4, 6),
    _OspfTmrsKckOffSummary_Type()
)
ospfTmrsKckOffSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffSummary.setStatus("current")
_OspfTmrsKckOffAseExport_Type = Counter32
_OspfTmrsKckOffAseExport_Object = MibScalar
ospfTmrsKckOffAseExport = _OspfTmrsKckOffAseExport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 1, 4, 7),
    _OspfTmrsKckOffAseExport_Type()
)
ospfTmrsKckOffAseExport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffAseExport.setStatus("current")
_OspfArea_ObjectIdentity = ObjectIdentity
ospfArea = _OspfArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2)
)
_OspfAreaRxTxStats_Object = MibTable
ospfAreaRxTxStats = _OspfAreaRxTxStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    ospfAreaRxTxStats.setStatus("current")
_OspfAreaRxTxStatsEntry_Object = MibTableRow
ospfAreaRxTxStatsEntry = _OspfAreaRxTxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 1, 1)
)
ospfAreaRxTxStatsEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfAreaRxTxIndex"),
)
if mibBuilder.loadTexts:
    ospfAreaRxTxStatsEntry.setStatus("current")
_OspfAreaRxTxIndex_Type = Integer32
_OspfAreaRxTxIndex_Object = MibTableColumn
ospfAreaRxTxIndex = _OspfAreaRxTxIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 1, 1, 1),
    _OspfAreaRxTxIndex_Type()
)
ospfAreaRxTxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxTxIndex.setStatus("current")
_OspfAreaRxPkts_Type = Counter32
_OspfAreaRxPkts_Object = MibTableColumn
ospfAreaRxPkts = _OspfAreaRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 1, 1, 2),
    _OspfAreaRxPkts_Type()
)
ospfAreaRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxPkts.setStatus("current")
_OspfAreaTxPkts_Type = Counter32
_OspfAreaTxPkts_Object = MibTableColumn
ospfAreaTxPkts = _OspfAreaTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 1, 1, 3),
    _OspfAreaTxPkts_Type()
)
ospfAreaTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTxPkts.setStatus("current")
_OspfAreaRxHello_Type = Counter32
_OspfAreaRxHello_Object = MibTableColumn
ospfAreaRxHello = _OspfAreaRxHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 1, 1, 4),
    _OspfAreaRxHello_Type()
)
ospfAreaRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxHello.setStatus("current")
_OspfAreaTxHello_Type = Counter32
_OspfAreaTxHello_Object = MibTableColumn
ospfAreaTxHello = _OspfAreaTxHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 1, 1, 5),
    _OspfAreaTxHello_Type()
)
ospfAreaTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTxHello.setStatus("current")
_OspfAreaRxDatabase_Type = Counter32
_OspfAreaRxDatabase_Object = MibTableColumn
ospfAreaRxDatabase = _OspfAreaRxDatabase_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 1, 1, 6),
    _OspfAreaRxDatabase_Type()
)
ospfAreaRxDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxDatabase.setStatus("current")
_OspfAreaTxDatabase_Type = Counter32
_OspfAreaTxDatabase_Object = MibTableColumn
ospfAreaTxDatabase = _OspfAreaTxDatabase_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 1, 1, 7),
    _OspfAreaTxDatabase_Type()
)
ospfAreaTxDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTxDatabase.setStatus("current")
_OspfAreaRxlsReqs_Type = Counter32
_OspfAreaRxlsReqs_Object = MibTableColumn
ospfAreaRxlsReqs = _OspfAreaRxlsReqs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 1, 1, 8),
    _OspfAreaRxlsReqs_Type()
)
ospfAreaRxlsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxlsReqs.setStatus("current")
_OspfAreaTxlsReqs_Type = Counter32
_OspfAreaTxlsReqs_Object = MibTableColumn
ospfAreaTxlsReqs = _OspfAreaTxlsReqs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 1, 1, 9),
    _OspfAreaTxlsReqs_Type()
)
ospfAreaTxlsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTxlsReqs.setStatus("current")
_OspfAreaRxlsAcks_Type = Counter32
_OspfAreaRxlsAcks_Object = MibTableColumn
ospfAreaRxlsAcks = _OspfAreaRxlsAcks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 1, 1, 10),
    _OspfAreaRxlsAcks_Type()
)
ospfAreaRxlsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxlsAcks.setStatus("current")
_OspfAreaTxlsAcks_Type = Counter32
_OspfAreaTxlsAcks_Object = MibTableColumn
ospfAreaTxlsAcks = _OspfAreaTxlsAcks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 1, 1, 11),
    _OspfAreaTxlsAcks_Type()
)
ospfAreaTxlsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTxlsAcks.setStatus("current")
_OspfAreaRxlsUpdates_Type = Counter32
_OspfAreaRxlsUpdates_Object = MibTableColumn
ospfAreaRxlsUpdates = _OspfAreaRxlsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 1, 1, 12),
    _OspfAreaRxlsUpdates_Type()
)
ospfAreaRxlsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxlsUpdates.setStatus("current")
_OspfAreaTxlsUpdates_Type = Counter32
_OspfAreaTxlsUpdates_Object = MibTableColumn
ospfAreaTxlsUpdates = _OspfAreaTxlsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 1, 1, 13),
    _OspfAreaTxlsUpdates_Type()
)
ospfAreaTxlsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTxlsUpdates.setStatus("current")
_OspfAreaNbrChangeStats_Object = MibTable
ospfAreaNbrChangeStats = _OspfAreaNbrChangeStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 2)
)
if mibBuilder.loadTexts:
    ospfAreaNbrChangeStats.setStatus("current")
_OspfAreaNbrChangeStatsEntry_Object = MibTableRow
ospfAreaNbrChangeStatsEntry = _OspfAreaNbrChangeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 2, 1)
)
ospfAreaNbrChangeStatsEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfAreaNbrIndex"),
)
if mibBuilder.loadTexts:
    ospfAreaNbrChangeStatsEntry.setStatus("current")
_OspfAreaNbrIndex_Type = Integer32
_OspfAreaNbrIndex_Object = MibTableColumn
ospfAreaNbrIndex = _OspfAreaNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 2, 1, 1),
    _OspfAreaNbrIndex_Type()
)
ospfAreaNbrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrIndex.setStatus("current")
_OspfAreaNbrhello_Type = Counter32
_OspfAreaNbrhello_Object = MibTableColumn
ospfAreaNbrhello = _OspfAreaNbrhello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 2, 1, 2),
    _OspfAreaNbrhello_Type()
)
ospfAreaNbrhello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrhello.setStatus("current")
_OspfAreaNbrStart_Type = Counter32
_OspfAreaNbrStart_Object = MibTableColumn
ospfAreaNbrStart = _OspfAreaNbrStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 2, 1, 3),
    _OspfAreaNbrStart_Type()
)
ospfAreaNbrStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrStart.setStatus("current")
_OspfAreaNbrAdjointOk_Type = Counter32
_OspfAreaNbrAdjointOk_Object = MibTableColumn
ospfAreaNbrAdjointOk = _OspfAreaNbrAdjointOk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 2, 1, 4),
    _OspfAreaNbrAdjointOk_Type()
)
ospfAreaNbrAdjointOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrAdjointOk.setStatus("current")
_OspfAreaNbrNegotiationDone_Type = Counter32
_OspfAreaNbrNegotiationDone_Object = MibTableColumn
ospfAreaNbrNegotiationDone = _OspfAreaNbrNegotiationDone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 2, 1, 5),
    _OspfAreaNbrNegotiationDone_Type()
)
ospfAreaNbrNegotiationDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrNegotiationDone.setStatus("current")
_OspfAreaNbrExchangeDone_Type = Counter32
_OspfAreaNbrExchangeDone_Object = MibTableColumn
ospfAreaNbrExchangeDone = _OspfAreaNbrExchangeDone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 2, 1, 6),
    _OspfAreaNbrExchangeDone_Type()
)
ospfAreaNbrExchangeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrExchangeDone.setStatus("current")
_OspfAreaNbrBadRequests_Type = Counter32
_OspfAreaNbrBadRequests_Object = MibTableColumn
ospfAreaNbrBadRequests = _OspfAreaNbrBadRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 2, 1, 7),
    _OspfAreaNbrBadRequests_Type()
)
ospfAreaNbrBadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrBadRequests.setStatus("current")
_OspfAreaNbrBadSequence_Type = Counter32
_OspfAreaNbrBadSequence_Object = MibTableColumn
ospfAreaNbrBadSequence = _OspfAreaNbrBadSequence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 2, 1, 8),
    _OspfAreaNbrBadSequence_Type()
)
ospfAreaNbrBadSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrBadSequence.setStatus("current")
_OspfAreaNbrLoadingDone_Type = Counter32
_OspfAreaNbrLoadingDone_Object = MibTableColumn
ospfAreaNbrLoadingDone = _OspfAreaNbrLoadingDone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 2, 1, 9),
    _OspfAreaNbrLoadingDone_Type()
)
ospfAreaNbrLoadingDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrLoadingDone.setStatus("current")
_OspfAreaNbrN1way_Type = Counter32
_OspfAreaNbrN1way_Object = MibTableColumn
ospfAreaNbrN1way = _OspfAreaNbrN1way_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 2, 1, 10),
    _OspfAreaNbrN1way_Type()
)
ospfAreaNbrN1way.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrN1way.setStatus("current")
_OspfAreaNbrRstAd_Type = Counter32
_OspfAreaNbrRstAd_Object = MibTableColumn
ospfAreaNbrRstAd = _OspfAreaNbrRstAd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 2, 1, 11),
    _OspfAreaNbrRstAd_Type()
)
ospfAreaNbrRstAd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrRstAd.setStatus("current")
_OspfAreaNbrDown_Type = Counter32
_OspfAreaNbrDown_Object = MibTableColumn
ospfAreaNbrDown = _OspfAreaNbrDown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 2, 1, 12),
    _OspfAreaNbrDown_Type()
)
ospfAreaNbrDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrDown.setStatus("current")
_OspfAreaNbrN2way_Type = Counter32
_OspfAreaNbrN2way_Object = MibTableColumn
ospfAreaNbrN2way = _OspfAreaNbrN2way_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 2, 1, 13),
    _OspfAreaNbrN2way_Type()
)
ospfAreaNbrN2way.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrN2way.setStatus("current")
_OspfAreaChangeStats_Object = MibTable
ospfAreaChangeStats = _OspfAreaChangeStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 3)
)
if mibBuilder.loadTexts:
    ospfAreaChangeStats.setStatus("current")
_OspfAreaChangeStatsEntry_Object = MibTableRow
ospfAreaChangeStatsEntry = _OspfAreaChangeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 3, 1)
)
ospfAreaChangeStatsEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfAreaIntfIndex"),
)
if mibBuilder.loadTexts:
    ospfAreaChangeStatsEntry.setStatus("current")
_OspfAreaIntfIndex_Type = Integer32
_OspfAreaIntfIndex_Object = MibTableColumn
ospfAreaIntfIndex = _OspfAreaIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 3, 1, 1),
    _OspfAreaIntfIndex_Type()
)
ospfAreaIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfIndex.setStatus("current")
_OspfAreaIntfHello_Type = Counter32
_OspfAreaIntfHello_Object = MibTableColumn
ospfAreaIntfHello = _OspfAreaIntfHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 3, 1, 2),
    _OspfAreaIntfHello_Type()
)
ospfAreaIntfHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfHello.setStatus("current")
_OspfAreaIntfDown_Type = Counter32
_OspfAreaIntfDown_Object = MibTableColumn
ospfAreaIntfDown = _OspfAreaIntfDown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 3, 1, 3),
    _OspfAreaIntfDown_Type()
)
ospfAreaIntfDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfDown.setStatus("current")
_OspfAreaIntfLoop_Type = Counter32
_OspfAreaIntfLoop_Object = MibTableColumn
ospfAreaIntfLoop = _OspfAreaIntfLoop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 3, 1, 4),
    _OspfAreaIntfLoop_Type()
)
ospfAreaIntfLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfLoop.setStatus("current")
_OspfAreaIntfUnloop_Type = Counter32
_OspfAreaIntfUnloop_Object = MibTableColumn
ospfAreaIntfUnloop = _OspfAreaIntfUnloop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 3, 1, 5),
    _OspfAreaIntfUnloop_Type()
)
ospfAreaIntfUnloop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfUnloop.setStatus("current")
_OspfAreaIntfWaitTimer_Type = Counter32
_OspfAreaIntfWaitTimer_Object = MibTableColumn
ospfAreaIntfWaitTimer = _OspfAreaIntfWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 3, 1, 6),
    _OspfAreaIntfWaitTimer_Type()
)
ospfAreaIntfWaitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfWaitTimer.setStatus("current")
_OspfAreaIntfBackup_Type = Counter32
_OspfAreaIntfBackup_Object = MibTableColumn
ospfAreaIntfBackup = _OspfAreaIntfBackup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 3, 1, 7),
    _OspfAreaIntfBackup_Type()
)
ospfAreaIntfBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfBackup.setStatus("current")
_OspfAreaIntfNbrChange_Type = Counter32
_OspfAreaIntfNbrChange_Object = MibTableColumn
ospfAreaIntfNbrChange = _OspfAreaIntfNbrChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 3, 1, 8),
    _OspfAreaIntfNbrChange_Type()
)
ospfAreaIntfNbrChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfNbrChange.setStatus("current")
_OspfAreaErrorStats_Object = MibTable
ospfAreaErrorStats = _OspfAreaErrorStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 4)
)
if mibBuilder.loadTexts:
    ospfAreaErrorStats.setStatus("current")
_OspfAreaErrorStatsEntry_Object = MibTableRow
ospfAreaErrorStatsEntry = _OspfAreaErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 4, 1)
)
ospfAreaErrorStatsEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfAreaErrIndex"),
)
if mibBuilder.loadTexts:
    ospfAreaErrorStatsEntry.setStatus("current")
_OspfAreaErrIndex_Type = Integer32
_OspfAreaErrIndex_Object = MibTableColumn
ospfAreaErrIndex = _OspfAreaErrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 4, 1, 1),
    _OspfAreaErrIndex_Type()
)
ospfAreaErrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaErrIndex.setStatus("current")
_OspfAreaErrAuthFailure_Type = Counter32
_OspfAreaErrAuthFailure_Object = MibTableColumn
ospfAreaErrAuthFailure = _OspfAreaErrAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 4, 1, 2),
    _OspfAreaErrAuthFailure_Type()
)
ospfAreaErrAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaErrAuthFailure.setStatus("current")
_OspfAreaErrNetmaskMismatch_Type = Counter32
_OspfAreaErrNetmaskMismatch_Object = MibTableColumn
ospfAreaErrNetmaskMismatch = _OspfAreaErrNetmaskMismatch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 4, 1, 3),
    _OspfAreaErrNetmaskMismatch_Type()
)
ospfAreaErrNetmaskMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaErrNetmaskMismatch.setStatus("current")
_OspfAreaErrHelloMismatch_Type = Counter32
_OspfAreaErrHelloMismatch_Object = MibTableColumn
ospfAreaErrHelloMismatch = _OspfAreaErrHelloMismatch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 4, 1, 4),
    _OspfAreaErrHelloMismatch_Type()
)
ospfAreaErrHelloMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaErrHelloMismatch.setStatus("current")
_OspfAreaErrDeadMismatch_Type = Counter32
_OspfAreaErrDeadMismatch_Object = MibTableColumn
ospfAreaErrDeadMismatch = _OspfAreaErrDeadMismatch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 4, 1, 5),
    _OspfAreaErrDeadMismatch_Type()
)
ospfAreaErrDeadMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaErrDeadMismatch.setStatus("current")
_OspfAreaErrOptionsMismatch_Type = Counter32
_OspfAreaErrOptionsMismatch_Object = MibTableColumn
ospfAreaErrOptionsMismatch = _OspfAreaErrOptionsMismatch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 4, 1, 6),
    _OspfAreaErrOptionsMismatch_Type()
)
ospfAreaErrOptionsMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaErrOptionsMismatch.setStatus("current")
_OspfAreaErrUnknownNbr_Type = Counter32
_OspfAreaErrUnknownNbr_Object = MibTableColumn
ospfAreaErrUnknownNbr = _OspfAreaErrUnknownNbr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 2, 4, 1, 7),
    _OspfAreaErrUnknownNbr_Type()
)
ospfAreaErrUnknownNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaErrUnknownNbr.setStatus("current")
_OspfInterface_ObjectIdentity = ObjectIdentity
ospfInterface = _OspfInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3)
)
_OspfIntfRxTxStats_Object = MibTable
ospfIntfRxTxStats = _OspfIntfRxTxStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    ospfIntfRxTxStats.setStatus("current")
_OspfIntfRxTxStatsEntry_Object = MibTableRow
ospfIntfRxTxStatsEntry = _OspfIntfRxTxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 1, 1)
)
ospfIntfRxTxStatsEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfIntfRxTxIndex"),
)
if mibBuilder.loadTexts:
    ospfIntfRxTxStatsEntry.setStatus("current")
_OspfIntfRxTxIndex_Type = Integer32
_OspfIntfRxTxIndex_Object = MibTableColumn
ospfIntfRxTxIndex = _OspfIntfRxTxIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 1, 1, 1),
    _OspfIntfRxTxIndex_Type()
)
ospfIntfRxTxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxTxIndex.setStatus("current")
_OspfIntfRxPkts_Type = Counter32
_OspfIntfRxPkts_Object = MibTableColumn
ospfIntfRxPkts = _OspfIntfRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 1, 1, 2),
    _OspfIntfRxPkts_Type()
)
ospfIntfRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxPkts.setStatus("current")
_OspfIntfTxPkts_Type = Counter32
_OspfIntfTxPkts_Object = MibTableColumn
ospfIntfTxPkts = _OspfIntfTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 1, 1, 3),
    _OspfIntfTxPkts_Type()
)
ospfIntfTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTxPkts.setStatus("current")
_OspfIntfRxHello_Type = Counter32
_OspfIntfRxHello_Object = MibTableColumn
ospfIntfRxHello = _OspfIntfRxHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 1, 1, 4),
    _OspfIntfRxHello_Type()
)
ospfIntfRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxHello.setStatus("current")
_OspfIntfTxHello_Type = Counter32
_OspfIntfTxHello_Object = MibTableColumn
ospfIntfTxHello = _OspfIntfTxHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 1, 1, 5),
    _OspfIntfTxHello_Type()
)
ospfIntfTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTxHello.setStatus("current")
_OspfIntfRxDatabase_Type = Counter32
_OspfIntfRxDatabase_Object = MibTableColumn
ospfIntfRxDatabase = _OspfIntfRxDatabase_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 1, 1, 6),
    _OspfIntfRxDatabase_Type()
)
ospfIntfRxDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxDatabase.setStatus("current")
_OspfIntfTxDatabase_Type = Counter32
_OspfIntfTxDatabase_Object = MibTableColumn
ospfIntfTxDatabase = _OspfIntfTxDatabase_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 1, 1, 7),
    _OspfIntfTxDatabase_Type()
)
ospfIntfTxDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTxDatabase.setStatus("current")
_OspfIntfRxlsReqs_Type = Counter32
_OspfIntfRxlsReqs_Object = MibTableColumn
ospfIntfRxlsReqs = _OspfIntfRxlsReqs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 1, 1, 8),
    _OspfIntfRxlsReqs_Type()
)
ospfIntfRxlsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxlsReqs.setStatus("current")
_OspfIntfTxlsReqs_Type = Counter32
_OspfIntfTxlsReqs_Object = MibTableColumn
ospfIntfTxlsReqs = _OspfIntfTxlsReqs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 1, 1, 9),
    _OspfIntfTxlsReqs_Type()
)
ospfIntfTxlsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTxlsReqs.setStatus("current")
_OspfIntfRxlsAcks_Type = Counter32
_OspfIntfRxlsAcks_Object = MibTableColumn
ospfIntfRxlsAcks = _OspfIntfRxlsAcks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 1, 1, 10),
    _OspfIntfRxlsAcks_Type()
)
ospfIntfRxlsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxlsAcks.setStatus("current")
_OspfIntfTxlsAcks_Type = Counter32
_OspfIntfTxlsAcks_Object = MibTableColumn
ospfIntfTxlsAcks = _OspfIntfTxlsAcks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 1, 1, 11),
    _OspfIntfTxlsAcks_Type()
)
ospfIntfTxlsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTxlsAcks.setStatus("current")
_OspfIntfRxlsUpdates_Type = Counter32
_OspfIntfRxlsUpdates_Object = MibTableColumn
ospfIntfRxlsUpdates = _OspfIntfRxlsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 1, 1, 12),
    _OspfIntfRxlsUpdates_Type()
)
ospfIntfRxlsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxlsUpdates.setStatus("current")
_OspfIntfTxlsUpdates_Type = Counter32
_OspfIntfTxlsUpdates_Object = MibTableColumn
ospfIntfTxlsUpdates = _OspfIntfTxlsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 1, 1, 13),
    _OspfIntfTxlsUpdates_Type()
)
ospfIntfTxlsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTxlsUpdates.setStatus("current")
_OspfIntfNbrChangeStats_Object = MibTable
ospfIntfNbrChangeStats = _OspfIntfNbrChangeStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 2)
)
if mibBuilder.loadTexts:
    ospfIntfNbrChangeStats.setStatus("current")
_OspfIntfNbrChangeStatsEntry_Object = MibTableRow
ospfIntfNbrChangeStatsEntry = _OspfIntfNbrChangeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 2, 1)
)
ospfIntfNbrChangeStatsEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfIntfNbrIndex"),
)
if mibBuilder.loadTexts:
    ospfIntfNbrChangeStatsEntry.setStatus("current")
_OspfIntfNbrIndex_Type = Integer32
_OspfIntfNbrIndex_Object = MibTableColumn
ospfIntfNbrIndex = _OspfIntfNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 2, 1, 1),
    _OspfIntfNbrIndex_Type()
)
ospfIntfNbrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrIndex.setStatus("current")
_OspfIntfNbrhello_Type = Counter32
_OspfIntfNbrhello_Object = MibTableColumn
ospfIntfNbrhello = _OspfIntfNbrhello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 2, 1, 2),
    _OspfIntfNbrhello_Type()
)
ospfIntfNbrhello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrhello.setStatus("current")
_OspfIntfNbrStart_Type = Counter32
_OspfIntfNbrStart_Object = MibTableColumn
ospfIntfNbrStart = _OspfIntfNbrStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 2, 1, 3),
    _OspfIntfNbrStart_Type()
)
ospfIntfNbrStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrStart.setStatus("current")
_OspfIntfNbrAdjointOk_Type = Counter32
_OspfIntfNbrAdjointOk_Object = MibTableColumn
ospfIntfNbrAdjointOk = _OspfIntfNbrAdjointOk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 2, 1, 4),
    _OspfIntfNbrAdjointOk_Type()
)
ospfIntfNbrAdjointOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrAdjointOk.setStatus("current")
_OspfIntfNbrNegotiationDone_Type = Counter32
_OspfIntfNbrNegotiationDone_Object = MibTableColumn
ospfIntfNbrNegotiationDone = _OspfIntfNbrNegotiationDone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 2, 1, 5),
    _OspfIntfNbrNegotiationDone_Type()
)
ospfIntfNbrNegotiationDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrNegotiationDone.setStatus("current")
_OspfIntfNbrExchangeDone_Type = Counter32
_OspfIntfNbrExchangeDone_Object = MibTableColumn
ospfIntfNbrExchangeDone = _OspfIntfNbrExchangeDone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 2, 1, 6),
    _OspfIntfNbrExchangeDone_Type()
)
ospfIntfNbrExchangeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrExchangeDone.setStatus("current")
_OspfIntfNbrBadRequests_Type = Counter32
_OspfIntfNbrBadRequests_Object = MibTableColumn
ospfIntfNbrBadRequests = _OspfIntfNbrBadRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 2, 1, 7),
    _OspfIntfNbrBadRequests_Type()
)
ospfIntfNbrBadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrBadRequests.setStatus("current")
_OspfIntfNbrBadSequence_Type = Counter32
_OspfIntfNbrBadSequence_Object = MibTableColumn
ospfIntfNbrBadSequence = _OspfIntfNbrBadSequence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 2, 1, 8),
    _OspfIntfNbrBadSequence_Type()
)
ospfIntfNbrBadSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrBadSequence.setStatus("current")
_OspfIntfNbrLoadingDone_Type = Counter32
_OspfIntfNbrLoadingDone_Object = MibTableColumn
ospfIntfNbrLoadingDone = _OspfIntfNbrLoadingDone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 2, 1, 9),
    _OspfIntfNbrLoadingDone_Type()
)
ospfIntfNbrLoadingDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrLoadingDone.setStatus("current")
_OspfIntfNbrN1way_Type = Counter32
_OspfIntfNbrN1way_Object = MibTableColumn
ospfIntfNbrN1way = _OspfIntfNbrN1way_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 2, 1, 10),
    _OspfIntfNbrN1way_Type()
)
ospfIntfNbrN1way.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrN1way.setStatus("current")
_OspfIntfNbrRstAd_Type = Counter32
_OspfIntfNbrRstAd_Object = MibTableColumn
ospfIntfNbrRstAd = _OspfIntfNbrRstAd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 2, 1, 11),
    _OspfIntfNbrRstAd_Type()
)
ospfIntfNbrRstAd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrRstAd.setStatus("current")
_OspfIntfNbrDown_Type = Counter32
_OspfIntfNbrDown_Object = MibTableColumn
ospfIntfNbrDown = _OspfIntfNbrDown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 2, 1, 12),
    _OspfIntfNbrDown_Type()
)
ospfIntfNbrDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrDown.setStatus("current")
_OspfIntfNbrN2way_Type = Counter32
_OspfIntfNbrN2way_Object = MibTableColumn
ospfIntfNbrN2way = _OspfIntfNbrN2way_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 2, 1, 13),
    _OspfIntfNbrN2way_Type()
)
ospfIntfNbrN2way.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrN2way.setStatus("current")
_OspfIntfChangeStats_Object = MibTable
ospfIntfChangeStats = _OspfIntfChangeStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 3)
)
if mibBuilder.loadTexts:
    ospfIntfChangeStats.setStatus("current")
_OspfIntfChangeStatsEntry_Object = MibTableRow
ospfIntfChangeStatsEntry = _OspfIntfChangeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 3, 1)
)
ospfIntfChangeStatsEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfIntfIndex"),
)
if mibBuilder.loadTexts:
    ospfIntfChangeStatsEntry.setStatus("current")
_OspfIntfIndex_Type = Integer32
_OspfIntfIndex_Object = MibTableColumn
ospfIntfIndex = _OspfIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 3, 1, 1),
    _OspfIntfIndex_Type()
)
ospfIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfIndex.setStatus("current")
_OspfIntfHello_Type = Counter32
_OspfIntfHello_Object = MibTableColumn
ospfIntfHello = _OspfIntfHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 3, 1, 2),
    _OspfIntfHello_Type()
)
ospfIntfHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfHello.setStatus("current")
_OspfIntfDown_Type = Counter32
_OspfIntfDown_Object = MibTableColumn
ospfIntfDown = _OspfIntfDown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 3, 1, 3),
    _OspfIntfDown_Type()
)
ospfIntfDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfDown.setStatus("current")
_OspfIntfLoop_Type = Counter32
_OspfIntfLoop_Object = MibTableColumn
ospfIntfLoop = _OspfIntfLoop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 3, 1, 4),
    _OspfIntfLoop_Type()
)
ospfIntfLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfLoop.setStatus("current")
_OspfIntfUnloop_Type = Counter32
_OspfIntfUnloop_Object = MibTableColumn
ospfIntfUnloop = _OspfIntfUnloop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 3, 1, 5),
    _OspfIntfUnloop_Type()
)
ospfIntfUnloop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfUnloop.setStatus("current")
_OspfIntfWaitTimer_Type = Counter32
_OspfIntfWaitTimer_Object = MibTableColumn
ospfIntfWaitTimer = _OspfIntfWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 3, 1, 6),
    _OspfIntfWaitTimer_Type()
)
ospfIntfWaitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfWaitTimer.setStatus("current")
_OspfIntfBackup_Type = Counter32
_OspfIntfBackup_Object = MibTableColumn
ospfIntfBackup = _OspfIntfBackup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 3, 1, 7),
    _OspfIntfBackup_Type()
)
ospfIntfBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfBackup.setStatus("current")
_OspfIntfNbrChange_Type = Counter32
_OspfIntfNbrChange_Object = MibTableColumn
ospfIntfNbrChange = _OspfIntfNbrChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 3, 1, 8),
    _OspfIntfNbrChange_Type()
)
ospfIntfNbrChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrChange.setStatus("current")
_OspfIntfErrorStats_Object = MibTable
ospfIntfErrorStats = _OspfIntfErrorStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 4)
)
if mibBuilder.loadTexts:
    ospfIntfErrorStats.setStatus("current")
_OspfIntfErrorStatsEntry_Object = MibTableRow
ospfIntfErrorStatsEntry = _OspfIntfErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 4, 1)
)
ospfIntfErrorStatsEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfIntfErrIndex"),
)
if mibBuilder.loadTexts:
    ospfIntfErrorStatsEntry.setStatus("current")
_OspfIntfErrIndex_Type = Integer32
_OspfIntfErrIndex_Object = MibTableColumn
ospfIntfErrIndex = _OspfIntfErrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 4, 1, 1),
    _OspfIntfErrIndex_Type()
)
ospfIntfErrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfErrIndex.setStatus("current")
_OspfIntfErrAuthFailure_Type = Counter32
_OspfIntfErrAuthFailure_Object = MibTableColumn
ospfIntfErrAuthFailure = _OspfIntfErrAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 4, 1, 2),
    _OspfIntfErrAuthFailure_Type()
)
ospfIntfErrAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfErrAuthFailure.setStatus("current")
_OspfIntfErrNetmaskMismatch_Type = Counter32
_OspfIntfErrNetmaskMismatch_Object = MibTableColumn
ospfIntfErrNetmaskMismatch = _OspfIntfErrNetmaskMismatch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 4, 1, 3),
    _OspfIntfErrNetmaskMismatch_Type()
)
ospfIntfErrNetmaskMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfErrNetmaskMismatch.setStatus("current")
_OspfIntfErrHelloMismatch_Type = Counter32
_OspfIntfErrHelloMismatch_Object = MibTableColumn
ospfIntfErrHelloMismatch = _OspfIntfErrHelloMismatch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 4, 1, 4),
    _OspfIntfErrHelloMismatch_Type()
)
ospfIntfErrHelloMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfErrHelloMismatch.setStatus("current")
_OspfIntfErrDeadMismatch_Type = Counter32
_OspfIntfErrDeadMismatch_Object = MibTableColumn
ospfIntfErrDeadMismatch = _OspfIntfErrDeadMismatch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 4, 1, 5),
    _OspfIntfErrDeadMismatch_Type()
)
ospfIntfErrDeadMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfErrDeadMismatch.setStatus("current")
_OspfIntfErrOptionsMismatch_Type = Counter32
_OspfIntfErrOptionsMismatch_Object = MibTableColumn
ospfIntfErrOptionsMismatch = _OspfIntfErrOptionsMismatch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 4, 1, 6),
    _OspfIntfErrOptionsMismatch_Type()
)
ospfIntfErrOptionsMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfErrOptionsMismatch.setStatus("current")
_OspfIntfErrUnknownNbr_Type = Counter32
_OspfIntfErrUnknownNbr_Object = MibTableColumn
ospfIntfErrUnknownNbr = _OspfIntfErrUnknownNbr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 5, 3, 4, 1, 7),
    _OspfIntfErrUnknownNbr_Type()
)
ospfIntfErrUnknownNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfErrUnknownNbr.setStatus("current")
_ClearStats_ObjectIdentity = ObjectIdentity
clearStats = _ClearStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 6)
)


class _IpClearStats_Type(Integer32):
    """Custom type ipClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ok", 2))
    )


_IpClearStats_Type.__name__ = "Integer32"
_IpClearStats_Object = MibScalar
ipClearStats = _IpClearStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 6, 1),
    _IpClearStats_Type()
)
ipClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipClearStats.setStatus("current")
_IfStatsTable_Object = MibTable
ifStatsTable = _IfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 6, 2)
)
if mibBuilder.loadTexts:
    ifStatsTable.setStatus("current")
_IfStatsEntry_Object = MibTableRow
ifStatsEntry = _IfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 6, 2, 1)
)
ifStatsEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ifStatsIndex"),
)
if mibBuilder.loadTexts:
    ifStatsEntry.setStatus("current")
_IfStatsIndex_Type = Integer32
_IfStatsIndex_Object = MibTableColumn
ifStatsIndex = _IfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 6, 2, 1, 1),
    _IfStatsIndex_Type()
)
ifStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStatsIndex.setStatus("current")


class _IfClearStats_Type(Integer32):
    """Custom type ifClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ok", 2))
    )


_IfClearStats_Type.__name__ = "Integer32"
_IfClearStats_Object = MibTableColumn
ifClearStats = _IfClearStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 6, 2, 1, 2),
    _IfClearStats_Type()
)
ifClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifClearStats.setStatus("current")
_IgmpStats_ObjectIdentity = ObjectIdentity
igmpStats = _IgmpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 7)
)
_IgmpSnoopStats_Object = MibTable
igmpSnoopStats = _IgmpSnoopStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 7, 1)
)
if mibBuilder.loadTexts:
    igmpSnoopStats.setStatus("current")
_IgmpSnoopStatsEntry_Object = MibTableRow
igmpSnoopStatsEntry = _IgmpSnoopStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 7, 1, 1)
)
igmpSnoopStatsEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "igmpSnoopVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopStatsEntry.setStatus("current")
_IgmpSnoopVlanIndex_Type = Integer32
_IgmpSnoopVlanIndex_Object = MibTableColumn
igmpSnoopVlanIndex = _IgmpSnoopVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 7, 1, 1, 1),
    _IgmpSnoopVlanIndex_Type()
)
igmpSnoopVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopVlanIndex.setStatus("current")
_RxIgmpValidPkts_Type = Counter32
_RxIgmpValidPkts_Object = MibTableColumn
rxIgmpValidPkts = _RxIgmpValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 7, 1, 1, 2),
    _RxIgmpValidPkts_Type()
)
rxIgmpValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxIgmpValidPkts.setStatus("current")
_RxIgmpInvalidPkts_Type = Counter32
_RxIgmpInvalidPkts_Object = MibTableColumn
rxIgmpInvalidPkts = _RxIgmpInvalidPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 7, 1, 1, 3),
    _RxIgmpInvalidPkts_Type()
)
rxIgmpInvalidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxIgmpInvalidPkts.setStatus("current")
_RxIgmpGenQueries_Type = Counter32
_RxIgmpGenQueries_Object = MibTableColumn
rxIgmpGenQueries = _RxIgmpGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 7, 1, 1, 4),
    _RxIgmpGenQueries_Type()
)
rxIgmpGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxIgmpGenQueries.setStatus("current")
_RxIgmpGrpSpecificQueries_Type = Counter32
_RxIgmpGrpSpecificQueries_Object = MibTableColumn
rxIgmpGrpSpecificQueries = _RxIgmpGrpSpecificQueries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 7, 1, 1, 5),
    _RxIgmpGrpSpecificQueries_Type()
)
rxIgmpGrpSpecificQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxIgmpGrpSpecificQueries.setStatus("current")
_RxIgmpLeaves_Type = Counter32
_RxIgmpLeaves_Object = MibTableColumn
rxIgmpLeaves = _RxIgmpLeaves_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 7, 1, 1, 6),
    _RxIgmpLeaves_Type()
)
rxIgmpLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxIgmpLeaves.setStatus("current")
_RxIgmpReports_Type = Counter32
_RxIgmpReports_Object = MibTableColumn
rxIgmpReports = _RxIgmpReports_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 7, 1, 1, 7),
    _RxIgmpReports_Type()
)
rxIgmpReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxIgmpReports.setStatus("current")
_TxIgmpGrpSpecificQueries_Type = Counter32
_TxIgmpGrpSpecificQueries_Object = MibTableColumn
txIgmpGrpSpecificQueries = _TxIgmpGrpSpecificQueries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 7, 1, 1, 8),
    _TxIgmpGrpSpecificQueries_Type()
)
txIgmpGrpSpecificQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txIgmpGrpSpecificQueries.setStatus("current")
_TxIgmpReports_Type = Counter32
_TxIgmpReports_Object = MibTableColumn
txIgmpReports = _TxIgmpReports_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 7, 1, 1, 9),
    _TxIgmpReports_Type()
)
txIgmpReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txIgmpReports.setStatus("current")
_TxIgmpLeaves_Type = Counter32
_TxIgmpLeaves_Object = MibTableColumn
txIgmpLeaves = _TxIgmpLeaves_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 7, 1, 1, 10),
    _TxIgmpLeaves_Type()
)
txIgmpLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txIgmpLeaves.setStatus("current")


class _IgmpClearVlanStats_Type(Integer32):
    """Custom type igmpClearVlanStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ok", 2))
    )


_IgmpClearVlanStats_Type.__name__ = "Integer32"
_IgmpClearVlanStats_Object = MibTableColumn
igmpClearVlanStats = _IgmpClearVlanStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 7, 1, 1, 11),
    _IgmpClearVlanStats_Type()
)
igmpClearVlanStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpClearVlanStats.setStatus("current")


class _IgmpClearAllStats_Type(Integer32):
    """Custom type igmpClearAllStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ok", 2))
    )


_IgmpClearAllStats_Type.__name__ = "Integer32"
_IgmpClearAllStats_Object = MibScalar
igmpClearAllStats = _IgmpClearAllStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 7, 2),
    _IgmpClearAllStats_Type()
)
igmpClearAllStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpClearAllStats.setStatus("current")
_Rip2Stats_ObjectIdentity = ObjectIdentity
rip2Stats = _Rip2Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 13)
)
_RipStatInPackets_Type = Counter32
_RipStatInPackets_Object = MibScalar
ripStatInPackets = _RipStatInPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 13, 1),
    _RipStatInPackets_Type()
)
ripStatInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInPackets.setStatus("current")
_RipStatOutPackets_Type = Counter32
_RipStatOutPackets_Object = MibScalar
ripStatOutPackets = _RipStatOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 13, 2),
    _RipStatOutPackets_Type()
)
ripStatOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatOutPackets.setStatus("current")
_RipStatInRequestPkts_Type = Counter32
_RipStatInRequestPkts_Object = MibScalar
ripStatInRequestPkts = _RipStatInRequestPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 13, 3),
    _RipStatInRequestPkts_Type()
)
ripStatInRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInRequestPkts.setStatus("current")
_RipStatInResponsePkts_Type = Counter32
_RipStatInResponsePkts_Object = MibScalar
ripStatInResponsePkts = _RipStatInResponsePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 13, 4),
    _RipStatInResponsePkts_Type()
)
ripStatInResponsePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInResponsePkts.setStatus("current")
_RipStatOutRequestPkts_Type = Counter32
_RipStatOutRequestPkts_Object = MibScalar
ripStatOutRequestPkts = _RipStatOutRequestPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 13, 5),
    _RipStatOutRequestPkts_Type()
)
ripStatOutRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatOutRequestPkts.setStatus("current")
_RipStatOutResponsePkts_Type = Counter32
_RipStatOutResponsePkts_Object = MibScalar
ripStatOutResponsePkts = _RipStatOutResponsePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 13, 6),
    _RipStatOutResponsePkts_Type()
)
ripStatOutResponsePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatOutResponsePkts.setStatus("current")
_RipStatRouteTimeout_Type = Counter32
_RipStatRouteTimeout_Object = MibScalar
ripStatRouteTimeout = _RipStatRouteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 13, 7),
    _RipStatRouteTimeout_Type()
)
ripStatRouteTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatRouteTimeout.setStatus("current")
_RipStatInBadSizePkts_Type = Counter32
_RipStatInBadSizePkts_Object = MibScalar
ripStatInBadSizePkts = _RipStatInBadSizePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 13, 8),
    _RipStatInBadSizePkts_Type()
)
ripStatInBadSizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInBadSizePkts.setStatus("current")
_RipStatInBadVersion_Type = Counter32
_RipStatInBadVersion_Object = MibScalar
ripStatInBadVersion = _RipStatInBadVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 13, 9),
    _RipStatInBadVersion_Type()
)
ripStatInBadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInBadVersion.setStatus("current")
_RipStatInBadZeros_Type = Counter32
_RipStatInBadZeros_Object = MibScalar
ripStatInBadZeros = _RipStatInBadZeros_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 13, 10),
    _RipStatInBadZeros_Type()
)
ripStatInBadZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInBadZeros.setStatus("current")
_RipStatInBadSourcePort_Type = Counter32
_RipStatInBadSourcePort_Object = MibScalar
ripStatInBadSourcePort = _RipStatInBadSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 13, 11),
    _RipStatInBadSourcePort_Type()
)
ripStatInBadSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInBadSourcePort.setStatus("current")
_RipStatInBadSourceIP_Type = Counter32
_RipStatInBadSourceIP_Object = MibScalar
ripStatInBadSourceIP = _RipStatInBadSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 13, 12),
    _RipStatInBadSourceIP_Type()
)
ripStatInBadSourceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInBadSourceIP.setStatus("current")
_RipStatInSelfRcvPkts_Type = Counter32
_RipStatInSelfRcvPkts_Object = MibScalar
ripStatInSelfRcvPkts = _RipStatInSelfRcvPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 13, 13),
    _RipStatInSelfRcvPkts_Type()
)
ripStatInSelfRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInSelfRcvPkts.setStatus("current")
_DnsStats_ObjectIdentity = ObjectIdentity
dnsStats = _DnsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 14)
)
_DnsStatInGoodDnsRequests_Type = Counter32
_DnsStatInGoodDnsRequests_Object = MibScalar
dnsStatInGoodDnsRequests = _DnsStatInGoodDnsRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 14, 1),
    _DnsStatInGoodDnsRequests_Type()
)
dnsStatInGoodDnsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsStatInGoodDnsRequests.setStatus("current")
_DnsStatOutDnsRequests_Type = Counter32
_DnsStatOutDnsRequests_Object = MibScalar
dnsStatOutDnsRequests = _DnsStatOutDnsRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 14, 2),
    _DnsStatOutDnsRequests_Type()
)
dnsStatOutDnsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsStatOutDnsRequests.setStatus("current")
_DnsStatInBadDnsRequests_Type = Counter32
_DnsStatInBadDnsRequests_Object = MibScalar
dnsStatInBadDnsRequests = _DnsStatInBadDnsRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 14, 3),
    _DnsStatInBadDnsRequests_Type()
)
dnsStatInBadDnsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsStatInBadDnsRequests.setStatus("current")
_Geal3Stats_ObjectIdentity = ObjectIdentity
geal3Stats = _Geal3Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 15)
)
_MaxL3TableSize_Type = Integer32
_MaxL3TableSize_Object = MibScalar
maxL3TableSize = _MaxL3TableSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 15, 1),
    _MaxL3TableSize_Type()
)
maxL3TableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxL3TableSize.setStatus("current")
_NoL3EntriesUsed_Type = Integer32
_NoL3EntriesUsed_Object = MibScalar
noL3EntriesUsed = _NoL3EntriesUsed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 15, 2),
    _NoL3EntriesUsed_Type()
)
noL3EntriesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noL3EntriesUsed.setStatus("current")
_MaxLpmTableSize_Type = Integer32
_MaxLpmTableSize_Object = MibScalar
maxLpmTableSize = _MaxLpmTableSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 15, 3),
    _MaxLpmTableSize_Type()
)
maxLpmTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxLpmTableSize.setStatus("current")
_NoLpmEntriesUsed_Type = Integer32
_NoLpmEntriesUsed_Object = MibScalar
noLpmEntriesUsed = _NoLpmEntriesUsed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 15, 4),
    _NoLpmEntriesUsed_Type()
)
noLpmEntriesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noLpmEntriesUsed.setStatus("current")
_MaxBlockInLpmTable_Type = Integer32
_MaxBlockInLpmTable_Object = MibScalar
maxBlockInLpmTable = _MaxBlockInLpmTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 15, 5),
    _MaxBlockInLpmTable_Type()
)
maxBlockInLpmTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxBlockInLpmTable.setStatus("current")
_NoBlocksUsedInLpmTable_Type = Integer32
_NoBlocksUsedInLpmTable_Object = MibScalar
noBlocksUsedInLpmTable = _NoBlocksUsedInLpmTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 2, 15, 6),
    _NoBlocksUsedInLpmTable_Type()
)
noBlocksUsedInLpmTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noBlocksUsedInLpmTable.setStatus("current")
_Layer3Info_ObjectIdentity = ObjectIdentity
layer3Info = _Layer3Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3)
)
_IpRoutingInfo_ObjectIdentity = ObjectIdentity
ipRoutingInfo = _IpRoutingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 1)
)
_IpRouteInfoTable_Object = MibTable
ipRouteInfoTable = _IpRouteInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ipRouteInfoTable.setStatus("current")
_IpRouteInfoEntry_Object = MibTableRow
ipRouteInfoEntry = _IpRouteInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 1, 1, 1)
)
ipRouteInfoEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipRouteInfoIndx"),
)
if mibBuilder.loadTexts:
    ipRouteInfoEntry.setStatus("current")
_IpRouteInfoIndx_Type = Integer32
_IpRouteInfoIndx_Object = MibTableColumn
ipRouteInfoIndx = _IpRouteInfoIndx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 1, 1, 1, 1),
    _IpRouteInfoIndx_Type()
)
ipRouteInfoIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoIndx.setStatus("current")
_IpRouteInfoDestIp_Type = IpAddress
_IpRouteInfoDestIp_Object = MibTableColumn
ipRouteInfoDestIp = _IpRouteInfoDestIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 1, 1, 1, 2),
    _IpRouteInfoDestIp_Type()
)
ipRouteInfoDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoDestIp.setStatus("current")
_IpRouteInfoMask_Type = IpAddress
_IpRouteInfoMask_Object = MibTableColumn
ipRouteInfoMask = _IpRouteInfoMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 1, 1, 1, 3),
    _IpRouteInfoMask_Type()
)
ipRouteInfoMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoMask.setStatus("current")
_IpRouteInfoGateway_Type = IpAddress
_IpRouteInfoGateway_Object = MibTableColumn
ipRouteInfoGateway = _IpRouteInfoGateway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 1, 1, 1, 4),
    _IpRouteInfoGateway_Type()
)
ipRouteInfoGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoGateway.setStatus("current")


class _IpRouteInfoTag_Type(Integer32):
    """Custom type ipRouteInfoTag based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("addr", 3),
          ("bgp", 9),
          ("broadcast", 5),
          ("fixed", 1),
          ("martian", 6),
          ("multicast", 7),
          ("none", 11),
          ("ospf", 10),
          ("rip", 4),
          ("static", 2),
          ("vip", 8))
    )


_IpRouteInfoTag_Type.__name__ = "Integer32"
_IpRouteInfoTag_Object = MibTableColumn
ipRouteInfoTag = _IpRouteInfoTag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 1, 1, 1, 5),
    _IpRouteInfoTag_Type()
)
ipRouteInfoTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoTag.setStatus("current")


class _IpRouteInfoType_Type(Integer32):
    """Custom type ipRouteInfoType based on Integer32"""
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
        *(("broadcast", 4),
          ("direct", 2),
          ("indirect", 1),
          ("local", 3),
          ("martian", 5),
          ("multicast", 6),
          ("other", 7))
    )


_IpRouteInfoType_Type.__name__ = "Integer32"
_IpRouteInfoType_Object = MibTableColumn
ipRouteInfoType = _IpRouteInfoType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 1, 1, 1, 6),
    _IpRouteInfoType_Type()
)
ipRouteInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoType.setStatus("current")
_IpRouteInfoInterface_Type = Integer32
_IpRouteInfoInterface_Object = MibTableColumn
ipRouteInfoInterface = _IpRouteInfoInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 1, 1, 1, 7),
    _IpRouteInfoInterface_Type()
)
ipRouteInfoInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoInterface.setStatus("current")
_IpRouteInfoMetric_Type = Integer32
_IpRouteInfoMetric_Object = MibTableColumn
ipRouteInfoMetric = _IpRouteInfoMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 1, 1, 1, 8),
    _IpRouteInfoMetric_Type()
)
ipRouteInfoMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoMetric.setStatus("current")


class _RouteTableClear_Type(Integer32):
    """Custom type routeTableClear based on Integer32"""
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


_RouteTableClear_Type.__name__ = "Integer32"
_RouteTableClear_Object = MibScalar
routeTableClear = _RouteTableClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 1, 2),
    _RouteTableClear_Type()
)
routeTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeTableClear.setStatus("current")
_ArpInfo_ObjectIdentity = ObjectIdentity
arpInfo = _ArpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 2)
)
_ArpInfoTable_Object = MibTable
arpInfoTable = _ArpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    arpInfoTable.setStatus("current")
_ArpInfoEntry_Object = MibTableRow
arpInfoEntry = _ArpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 2, 1, 1)
)
arpInfoEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "arpInfoDestIp"),
)
if mibBuilder.loadTexts:
    arpInfoEntry.setStatus("current")
_ArpInfoDestIp_Type = IpAddress
_ArpInfoDestIp_Object = MibTableColumn
arpInfoDestIp = _ArpInfoDestIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 2, 1, 1, 1),
    _ArpInfoDestIp_Type()
)
arpInfoDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoDestIp.setStatus("current")
_ArpInfoMacAddr_Type = PhysAddress
_ArpInfoMacAddr_Object = MibTableColumn
arpInfoMacAddr = _ArpInfoMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 2, 1, 1, 2),
    _ArpInfoMacAddr_Type()
)
arpInfoMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoMacAddr.setStatus("current")
_ArpInfoVLAN_Type = Integer32
_ArpInfoVLAN_Object = MibTableColumn
arpInfoVLAN = _ArpInfoVLAN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 2, 1, 1, 3),
    _ArpInfoVLAN_Type()
)
arpInfoVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoVLAN.setStatus("current")
_ArpInfoSrcPort_Type = Integer32
_ArpInfoSrcPort_Object = MibTableColumn
arpInfoSrcPort = _ArpInfoSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 2, 1, 1, 4),
    _ArpInfoSrcPort_Type()
)
arpInfoSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoSrcPort.setStatus("current")
_ArpInfoRefPorts_Type = Integer32
_ArpInfoRefPorts_Object = MibTableColumn
arpInfoRefPorts = _ArpInfoRefPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 2, 1, 1, 5),
    _ArpInfoRefPorts_Type()
)
arpInfoRefPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoRefPorts.setStatus("current")


class _ArpInfoFlag_Type(Integer32):
    """Custom type arpInfoFlag based on Integer32"""
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
        *(("clear", 1),
          ("indirect", 4),
          ("permanent", 3),
          ("unresolved", 2))
    )


_ArpInfoFlag_Type.__name__ = "Integer32"
_ArpInfoFlag_Object = MibTableColumn
arpInfoFlag = _ArpInfoFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 2, 1, 1, 6),
    _ArpInfoFlag_Type()
)
arpInfoFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoFlag.setStatus("current")


class _ArpCacheClear_Type(Integer32):
    """Custom type arpCacheClear based on Integer32"""
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


_ArpCacheClear_Type.__name__ = "Integer32"
_ArpCacheClear_Object = MibScalar
arpCacheClear = _ArpCacheClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 2, 2),
    _ArpCacheClear_Type()
)
arpCacheClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpCacheClear.setStatus("current")
_VrrpInfo_ObjectIdentity = ObjectIdentity
vrrpInfo = _VrrpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 3)
)
_VrrpInfoVirtRtrTable_Object = MibTable
vrrpInfoVirtRtrTable = _VrrpInfoVirtRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrTable.setStatus("current")
_VrrpInfoVirtRtrTableEntry_Object = MibTableRow
vrrpInfoVirtRtrTableEntry = _VrrpInfoVirtRtrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 3, 1, 1)
)
vrrpInfoVirtRtrTableEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "vrrpInfoVirtRtrIndex"),
)
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrTableEntry.setStatus("current")
_VrrpInfoVirtRtrIndex_Type = Integer32
_VrrpInfoVirtRtrIndex_Object = MibTableColumn
vrrpInfoVirtRtrIndex = _VrrpInfoVirtRtrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 3, 1, 1, 1),
    _VrrpInfoVirtRtrIndex_Type()
)
vrrpInfoVirtRtrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrIndex.setStatus("current")


class _VrrpInfoVirtRtrConfig_Type(Integer32):
    """Custom type vrrpInfoVirtRtrConfig based on Integer32"""
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


_VrrpInfoVirtRtrConfig_Type.__name__ = "Integer32"
_VrrpInfoVirtRtrConfig_Object = MibTableColumn
vrrpInfoVirtRtrConfig = _VrrpInfoVirtRtrConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 3, 1, 1, 2),
    _VrrpInfoVirtRtrConfig_Type()
)
vrrpInfoVirtRtrConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrConfig.setStatus("current")


class _VrrpInfoVirtRtrID_Type(Integer32):
    """Custom type vrrpInfoVirtRtrID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpInfoVirtRtrID_Type.__name__ = "Integer32"
_VrrpInfoVirtRtrID_Object = MibTableColumn
vrrpInfoVirtRtrID = _VrrpInfoVirtRtrID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 3, 1, 1, 3),
    _VrrpInfoVirtRtrID_Type()
)
vrrpInfoVirtRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrID.setStatus("current")
_VrrpInfoVirtRtrAddr_Type = IpAddress
_VrrpInfoVirtRtrAddr_Object = MibTableColumn
vrrpInfoVirtRtrAddr = _VrrpInfoVirtRtrAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 3, 1, 1, 4),
    _VrrpInfoVirtRtrAddr_Type()
)
vrrpInfoVirtRtrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrAddr.setStatus("current")
_VrrpInfoVirtRtrIfIndex_Type = Integer32
_VrrpInfoVirtRtrIfIndex_Object = MibTableColumn
vrrpInfoVirtRtrIfIndex = _VrrpInfoVirtRtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 3, 1, 1, 5),
    _VrrpInfoVirtRtrIfIndex_Type()
)
vrrpInfoVirtRtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrIfIndex.setStatus("current")


class _VrrpInfoVirtRtrPriority_Type(Integer32):
    """Custom type vrrpInfoVirtRtrPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VrrpInfoVirtRtrPriority_Type.__name__ = "Integer32"
_VrrpInfoVirtRtrPriority_Object = MibTableColumn
vrrpInfoVirtRtrPriority = _VrrpInfoVirtRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 3, 1, 1, 6),
    _VrrpInfoVirtRtrPriority_Type()
)
vrrpInfoVirtRtrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrPriority.setStatus("current")


class _VrrpInfoVirtRtrState_Type(Integer32):
    """Custom type vrrpInfoVirtRtrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 3),
          ("init", 1),
          ("master", 2))
    )


_VrrpInfoVirtRtrState_Type.__name__ = "Integer32"
_VrrpInfoVirtRtrState_Object = MibTableColumn
vrrpInfoVirtRtrState = _VrrpInfoVirtRtrState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 3, 1, 1, 7),
    _VrrpInfoVirtRtrState_Type()
)
vrrpInfoVirtRtrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrState.setStatus("current")


class _VrrpInfoVirtRtrOwnership_Type(Integer32):
    """Custom type vrrpInfoVirtRtrOwnership based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("owner", 1),
          ("renter", 2))
    )


_VrrpInfoVirtRtrOwnership_Type.__name__ = "Integer32"
_VrrpInfoVirtRtrOwnership_Object = MibTableColumn
vrrpInfoVirtRtrOwnership = _VrrpInfoVirtRtrOwnership_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 3, 1, 1, 8),
    _VrrpInfoVirtRtrOwnership_Type()
)
vrrpInfoVirtRtrOwnership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrOwnership.setStatus("current")


class _VrrpInfoVirtRtrServer_Type(Integer32):
    """Custom type vrrpInfoVirtRtrServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_VrrpInfoVirtRtrServer_Type.__name__ = "Integer32"
_VrrpInfoVirtRtrServer_Object = MibTableColumn
vrrpInfoVirtRtrServer = _VrrpInfoVirtRtrServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 3, 1, 1, 9),
    _VrrpInfoVirtRtrServer_Type()
)
vrrpInfoVirtRtrServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrServer.setStatus("current")


class _VrrpInfoVirtRtrProxy_Type(Integer32):
    """Custom type vrrpInfoVirtRtrProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_VrrpInfoVirtRtrProxy_Type.__name__ = "Integer32"
_VrrpInfoVirtRtrProxy_Object = MibTableColumn
vrrpInfoVirtRtrProxy = _VrrpInfoVirtRtrProxy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 3, 1, 1, 10),
    _VrrpInfoVirtRtrProxy_Type()
)
vrrpInfoVirtRtrProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrProxy.setStatus("current")
_OspfInfo_ObjectIdentity = ObjectIdentity
ospfInfo = _OspfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4)
)
_OspfGeneralInfo_ObjectIdentity = ObjectIdentity
ospfGeneralInfo = _OspfGeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1)
)


class _OspfVersion_Type(Integer32):
    """Custom type ospfVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ospfVersion1", 1),
          ("ospfVersion2", 2))
    )


_OspfVersion_Type.__name__ = "Integer32"
_OspfVersion_Object = MibScalar
ospfVersion = _OspfVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 1),
    _OspfVersion_Type()
)
ospfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVersion.setStatus("current")
_OspfRouterID_Type = IpAddress
_OspfRouterID_Object = MibScalar
ospfRouterID = _OspfRouterID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 2),
    _OspfRouterID_Type()
)
ospfRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRouterID.setStatus("current")
_OspfStartTime_Type = Integer32
_OspfStartTime_Object = MibScalar
ospfStartTime = _OspfStartTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 3),
    _OspfStartTime_Type()
)
ospfStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStartTime.setStatus("current")
_OspfProcessUptime_Type = Counter32
_OspfProcessUptime_Object = MibScalar
ospfProcessUptime = _OspfProcessUptime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 4),
    _OspfProcessUptime_Type()
)
ospfProcessUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessUptime.setStatus("current")
_OspfLsTypesSupported_Type = Integer32
_OspfLsTypesSupported_Object = MibScalar
ospfLsTypesSupported = _OspfLsTypesSupported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 5),
    _OspfLsTypesSupported_Type()
)
ospfLsTypesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsTypesSupported.setStatus("current")


class _OspfAreaBorderRouter_Type(Integer32):
    """Custom type ospfAreaBorderRouter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_OspfAreaBorderRouter_Type.__name__ = "Integer32"
_OspfAreaBorderRouter_Object = MibScalar
ospfAreaBorderRouter = _OspfAreaBorderRouter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 6),
    _OspfAreaBorderRouter_Type()
)
ospfAreaBorderRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaBorderRouter.setStatus("current")


class _OspfAreaBoundaryRouter_Type(Integer32):
    """Custom type ospfAreaBoundaryRouter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_OspfAreaBoundaryRouter_Type.__name__ = "Integer32"
_OspfAreaBoundaryRouter_Object = MibScalar
ospfAreaBoundaryRouter = _OspfAreaBoundaryRouter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 7),
    _OspfAreaBoundaryRouter_Type()
)
ospfAreaBoundaryRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaBoundaryRouter.setStatus("current")
_OspfExternalLsa_Type = Integer32
_OspfExternalLsa_Object = MibScalar
ospfExternalLsa = _OspfExternalLsa_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 8),
    _OspfExternalLsa_Type()
)
ospfExternalLsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExternalLsa.setStatus("current")
_OspfIntfCountForRouter_Type = Integer32
_OspfIntfCountForRouter_Object = MibScalar
ospfIntfCountForRouter = _OspfIntfCountForRouter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 9),
    _OspfIntfCountForRouter_Type()
)
ospfIntfCountForRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfCountForRouter.setStatus("current")
_OspfVlinkCountForRouter_Type = Integer32
_OspfVlinkCountForRouter_Object = MibScalar
ospfVlinkCountForRouter = _OspfVlinkCountForRouter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 10),
    _OspfVlinkCountForRouter_Type()
)
ospfVlinkCountForRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVlinkCountForRouter.setStatus("current")
_OspfNewLsaReceived_Type = Integer32
_OspfNewLsaReceived_Object = MibScalar
ospfNewLsaReceived = _OspfNewLsaReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 11),
    _OspfNewLsaReceived_Type()
)
ospfNewLsaReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewLsaReceived.setStatus("current")
_OspfTotalLsaOriginated_Type = Integer32
_OspfTotalLsaOriginated_Object = MibScalar
ospfTotalLsaOriginated = _OspfTotalLsaOriginated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 12),
    _OspfTotalLsaOriginated_Type()
)
ospfTotalLsaOriginated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTotalLsaOriginated.setStatus("current")
_OspfTotalNumberOfLsdbEntries_Type = Integer32
_OspfTotalNumberOfLsdbEntries_Object = MibScalar
ospfTotalNumberOfLsdbEntries = _OspfTotalNumberOfLsdbEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 13),
    _OspfTotalNumberOfLsdbEntries_Type()
)
ospfTotalNumberOfLsdbEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTotalNumberOfLsdbEntries.setStatus("current")
_OspfTotalNeighbours_Type = Integer32
_OspfTotalNeighbours_Object = MibScalar
ospfTotalNeighbours = _OspfTotalNeighbours_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 14),
    _OspfTotalNeighbours_Type()
)
ospfTotalNeighbours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTotalNeighbours.setStatus("current")
_OspfNbrInInitState_Type = Integer32
_OspfNbrInInitState_Object = MibScalar
ospfNbrInInitState = _OspfNbrInInitState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 15),
    _OspfNbrInInitState_Type()
)
ospfNbrInInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrInInitState.setStatus("current")
_OspfNbrInExchState_Type = Integer32
_OspfNbrInExchState_Object = MibScalar
ospfNbrInExchState = _OspfNbrInExchState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 16),
    _OspfNbrInExchState_Type()
)
ospfNbrInExchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrInExchState.setStatus("current")
_OspfNbrInFullState_Type = Integer32
_OspfNbrInFullState_Object = MibScalar
ospfNbrInFullState = _OspfNbrInFullState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 17),
    _OspfNbrInFullState_Type()
)
ospfNbrInFullState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrInFullState.setStatus("current")
_OspfTotalAreas_Type = Integer32
_OspfTotalAreas_Object = MibScalar
ospfTotalAreas = _OspfTotalAreas_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 18),
    _OspfTotalAreas_Type()
)
ospfTotalAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTotalAreas.setStatus("current")
_OspfTotalTransitAreas_Type = Integer32
_OspfTotalTransitAreas_Object = MibScalar
ospfTotalTransitAreas = _OspfTotalTransitAreas_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 19),
    _OspfTotalTransitAreas_Type()
)
ospfTotalTransitAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTotalTransitAreas.setStatus("current")
_OspfTotalNssaAreas_Type = Integer32
_OspfTotalNssaAreas_Object = MibScalar
ospfTotalNssaAreas = _OspfTotalNssaAreas_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 1, 20),
    _OspfTotalNssaAreas_Type()
)
ospfTotalNssaAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTotalNssaAreas.setStatus("current")
_OspfAreaInfoTable_Object = MibTable
ospfAreaInfoTable = _OspfAreaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 2)
)
if mibBuilder.loadTexts:
    ospfAreaInfoTable.setStatus("current")
_OspfAreaInfoEntry_Object = MibTableRow
ospfAreaInfoEntry = _OspfAreaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 2, 1)
)
ospfAreaInfoEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfAreaInfoIndex"),
)
if mibBuilder.loadTexts:
    ospfAreaInfoEntry.setStatus("current")
_OspfAreaInfoIndex_Type = Integer32
_OspfAreaInfoIndex_Object = MibTableColumn
ospfAreaInfoIndex = _OspfAreaInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 2, 1, 1),
    _OspfAreaInfoIndex_Type()
)
ospfAreaInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaInfoIndex.setStatus("current")
_OspfAreaInfoId_Type = IpAddress
_OspfAreaInfoId_Object = MibTableColumn
ospfAreaInfoId = _OspfAreaInfoId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 2, 1, 2),
    _OspfAreaInfoId_Type()
)
ospfAreaInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaInfoId.setStatus("current")


class _OspfAreaInfoStatus_Type(Integer32):
    """Custom type ospfAreaInfoStatus based on Integer32"""
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


_OspfAreaInfoStatus_Type.__name__ = "Integer32"
_OspfAreaInfoStatus_Object = MibTableColumn
ospfAreaInfoStatus = _OspfAreaInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 2, 1, 3),
    _OspfAreaInfoStatus_Type()
)
ospfAreaInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaInfoStatus.setStatus("current")
_OspfTotalNumberOfInterfaces_Type = Integer32
_OspfTotalNumberOfInterfaces_Object = MibTableColumn
ospfTotalNumberOfInterfaces = _OspfTotalNumberOfInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 2, 1, 4),
    _OspfTotalNumberOfInterfaces_Type()
)
ospfTotalNumberOfInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTotalNumberOfInterfaces.setStatus("current")
_OspfNumberOfInterfacesUp_Type = Integer32
_OspfNumberOfInterfacesUp_Object = MibTableColumn
ospfNumberOfInterfacesUp = _OspfNumberOfInterfacesUp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 2, 1, 5),
    _OspfNumberOfInterfacesUp_Type()
)
ospfNumberOfInterfacesUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNumberOfInterfacesUp.setStatus("current")


class _OspfAreaInfoAuthType_Type(Integer32):
    """Custom type ospfAreaInfoAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("none", 1),
          ("password", 2))
    )


_OspfAreaInfoAuthType_Type.__name__ = "Integer32"
_OspfAreaInfoAuthType_Object = MibTableColumn
ospfAreaInfoAuthType = _OspfAreaInfoAuthType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 2, 1, 6),
    _OspfAreaInfoAuthType_Type()
)
ospfAreaInfoAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaInfoAuthType.setStatus("current")
_OspfAreaInfoSPF_Type = Integer32
_OspfAreaInfoSPF_Object = MibTableColumn
ospfAreaInfoSPF = _OspfAreaInfoSPF_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 2, 1, 7),
    _OspfAreaInfoSPF_Type()
)
ospfAreaInfoSPF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaInfoSPF.setStatus("current")
_OspfNumberOfLsdbEntries_Type = Integer32
_OspfNumberOfLsdbEntries_Object = MibTableColumn
ospfNumberOfLsdbEntries = _OspfNumberOfLsdbEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 2, 1, 8),
    _OspfNumberOfLsdbEntries_Type()
)
ospfNumberOfLsdbEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNumberOfLsdbEntries.setStatus("current")
_OspfAreaInfoAreaBorderRouter_Type = Integer32
_OspfAreaInfoAreaBorderRouter_Object = MibTableColumn
ospfAreaInfoAreaBorderRouter = _OspfAreaInfoAreaBorderRouter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 2, 1, 9),
    _OspfAreaInfoAreaBorderRouter_Type()
)
ospfAreaInfoAreaBorderRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaInfoAreaBorderRouter.setStatus("current")
_OspfAreaInfoASBoundaryRouter_Type = Integer32
_OspfAreaInfoASBoundaryRouter_Object = MibTableColumn
ospfAreaInfoASBoundaryRouter = _OspfAreaInfoASBoundaryRouter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 2, 1, 10),
    _OspfAreaInfoASBoundaryRouter_Type()
)
ospfAreaInfoASBoundaryRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaInfoASBoundaryRouter.setStatus("current")
_OspfAreaInfoTotalNeighbours_Type = Integer32
_OspfAreaInfoTotalNeighbours_Object = MibTableColumn
ospfAreaInfoTotalNeighbours = _OspfAreaInfoTotalNeighbours_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 2, 1, 11),
    _OspfAreaInfoTotalNeighbours_Type()
)
ospfAreaInfoTotalNeighbours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaInfoTotalNeighbours.setStatus("current")
_OspfIntfInfoTable_Object = MibTable
ospfIntfInfoTable = _OspfIntfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3)
)
if mibBuilder.loadTexts:
    ospfIntfInfoTable.setStatus("current")
_OspfIntfInfoEntry_Object = MibTableRow
ospfIntfInfoEntry = _OspfIntfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1)
)
ospfIntfInfoEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfIfInfoIndex"),
)
if mibBuilder.loadTexts:
    ospfIntfInfoEntry.setStatus("current")
_OspfIfInfoIndex_Type = Integer32
_OspfIfInfoIndex_Object = MibTableColumn
ospfIfInfoIndex = _OspfIfInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 1),
    _OspfIfInfoIndex_Type()
)
ospfIfInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoIndex.setStatus("current")
_OspfIfInfoIpAddress_Type = IpAddress
_OspfIfInfoIpAddress_Object = MibTableColumn
ospfIfInfoIpAddress = _OspfIfInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 2),
    _OspfIfInfoIpAddress_Type()
)
ospfIfInfoIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoIpAddress.setStatus("current")


class _OspfIfInfoArea_Type(Integer32):
    """Custom type ospfIfInfoArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_OspfIfInfoArea_Type.__name__ = "Integer32"
_OspfIfInfoArea_Object = MibTableColumn
ospfIfInfoArea = _OspfIfInfoArea_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 3),
    _OspfIfInfoArea_Type()
)
ospfIfInfoArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoArea.setStatus("current")


class _OspfIfInfoAdminStatus_Type(Integer32):
    """Custom type ospfIfInfoAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_OspfIfInfoAdminStatus_Type.__name__ = "Integer32"
_OspfIfInfoAdminStatus_Object = MibTableColumn
ospfIfInfoAdminStatus = _OspfIfInfoAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 4),
    _OspfIfInfoAdminStatus_Type()
)
ospfIfInfoAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoAdminStatus.setStatus("current")
_OspfIfInfoRouterID_Type = IpAddress
_OspfIfInfoRouterID_Object = MibTableColumn
ospfIfInfoRouterID = _OspfIfInfoRouterID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 5),
    _OspfIfInfoRouterID_Type()
)
ospfIfInfoRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoRouterID.setStatus("current")


class _OspfIfInfoState_Type(Integer32):
    """Custom type ospfIfInfoState based on Integer32"""
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
        *(("backupdr", 5),
          ("down", 0),
          ("dr", 4),
          ("drother", 6),
          ("loopback", 1),
          ("ptop", 3),
          ("waiting", 2))
    )


_OspfIfInfoState_Type.__name__ = "Integer32"
_OspfIfInfoState_Object = MibTableColumn
ospfIfInfoState = _OspfIfInfoState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 6),
    _OspfIfInfoState_Type()
)
ospfIfInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoState.setStatus("current")


class _OspfIfInfoPriority_Type(Integer32):
    """Custom type ospfIfInfoPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OspfIfInfoPriority_Type.__name__ = "Integer32"
_OspfIfInfoPriority_Object = MibTableColumn
ospfIfInfoPriority = _OspfIfInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 7),
    _OspfIfInfoPriority_Type()
)
ospfIfInfoPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoPriority.setStatus("current")
_OspfIfInfoDesignatedRouterID_Type = IpAddress
_OspfIfInfoDesignatedRouterID_Object = MibTableColumn
ospfIfInfoDesignatedRouterID = _OspfIfInfoDesignatedRouterID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 8),
    _OspfIfInfoDesignatedRouterID_Type()
)
ospfIfInfoDesignatedRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoDesignatedRouterID.setStatus("current")
_OspfIfInfoDesignatedRouterIpAddress_Type = IpAddress
_OspfIfInfoDesignatedRouterIpAddress_Object = MibTableColumn
ospfIfInfoDesignatedRouterIpAddress = _OspfIfInfoDesignatedRouterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 9),
    _OspfIfInfoDesignatedRouterIpAddress_Type()
)
ospfIfInfoDesignatedRouterIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoDesignatedRouterIpAddress.setStatus("current")
_OspfIfInfoBackupDesignatedRouterID_Type = IpAddress
_OspfIfInfoBackupDesignatedRouterID_Object = MibTableColumn
ospfIfInfoBackupDesignatedRouterID = _OspfIfInfoBackupDesignatedRouterID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 10),
    _OspfIfInfoBackupDesignatedRouterID_Type()
)
ospfIfInfoBackupDesignatedRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoBackupDesignatedRouterID.setStatus("current")
_OspfIfInfoBackupDesignatedRouterIpAddress_Type = IpAddress
_OspfIfInfoBackupDesignatedRouterIpAddress_Object = MibTableColumn
ospfIfInfoBackupDesignatedRouterIpAddress = _OspfIfInfoBackupDesignatedRouterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 11),
    _OspfIfInfoBackupDesignatedRouterIpAddress_Type()
)
ospfIfInfoBackupDesignatedRouterIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoBackupDesignatedRouterIpAddress.setStatus("current")


class _OspfIfInfoHello_Type(Integer32):
    """Custom type ospfIfInfoHello based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfIfInfoHello_Type.__name__ = "Integer32"
_OspfIfInfoHello_Object = MibTableColumn
ospfIfInfoHello = _OspfIfInfoHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 12),
    _OspfIfInfoHello_Type()
)
ospfIfInfoHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoHello.setStatus("current")


class _OspfIfInfoDead_Type(Integer32):
    """Custom type ospfIfInfoDead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfIfInfoDead_Type.__name__ = "Integer32"
_OspfIfInfoDead_Object = MibTableColumn
ospfIfInfoDead = _OspfIfInfoDead_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 13),
    _OspfIfInfoDead_Type()
)
ospfIfInfoDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoDead.setStatus("current")
_OspfIfInfoWait_Type = Integer32
_OspfIfInfoWait_Object = MibTableColumn
ospfIfInfoWait = _OspfIfInfoWait_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 14),
    _OspfIfInfoWait_Type()
)
ospfIfInfoWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoWait.setStatus("current")


class _OspfIfInfoRetransmit_Type(Integer32):
    """Custom type ospfIfInfoRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_OspfIfInfoRetransmit_Type.__name__ = "Integer32"
_OspfIfInfoRetransmit_Object = MibTableColumn
ospfIfInfoRetransmit = _OspfIfInfoRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 15),
    _OspfIfInfoRetransmit_Type()
)
ospfIfInfoRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoRetransmit.setStatus("current")


class _OspfIfInfoTransitDelay_Type(Integer32):
    """Custom type ospfIfInfoTransitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_OspfIfInfoTransitDelay_Type.__name__ = "Integer32"
_OspfIfInfoTransitDelay_Object = MibTableColumn
ospfIfInfoTransitDelay = _OspfIfInfoTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 16),
    _OspfIfInfoTransitDelay_Type()
)
ospfIfInfoTransitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoTransitDelay.setStatus("current")
_OspfIfInfoTotalNeighbours_Type = Integer32
_OspfIfInfoTotalNeighbours_Object = MibTableColumn
ospfIfInfoTotalNeighbours = _OspfIfInfoTotalNeighbours_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 17),
    _OspfIfInfoTotalNeighbours_Type()
)
ospfIfInfoTotalNeighbours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoTotalNeighbours.setStatus("current")
_OspfIfInfoEvents_Type = Integer32
_OspfIfInfoEvents_Object = MibTableColumn
ospfIfInfoEvents = _OspfIfInfoEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 18),
    _OspfIfInfoEvents_Type()
)
ospfIfInfoEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoEvents.setStatus("current")


class _OspfIfInfoAuthType_Type(Integer32):
    """Custom type ospfIfInfoAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("password", 1))
    )


_OspfIfInfoAuthType_Type.__name__ = "Integer32"
_OspfIfInfoAuthType_Object = MibTableColumn
ospfIfInfoAuthType = _OspfIfInfoAuthType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 3, 1, 19),
    _OspfIfInfoAuthType_Type()
)
ospfIfInfoAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoAuthType.setStatus("current")
_OspfIfNbrTable_Object = MibTable
ospfIfNbrTable = _OspfIfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 5)
)
if mibBuilder.loadTexts:
    ospfIfNbrTable.setStatus("current")
_OspfIfNbrEntry_Object = MibTableRow
ospfIfNbrEntry = _OspfIfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 5, 1)
)
ospfIfNbrEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ospfIfNbrIntfIndex"),
    (0, "BLADETYPE2-NETWORK-MIB", "ospfIfNbrIpAddr"),
)
if mibBuilder.loadTexts:
    ospfIfNbrEntry.setStatus("current")
_OspfIfNbrIntfIndex_Type = Integer32
_OspfIfNbrIntfIndex_Object = MibTableColumn
ospfIfNbrIntfIndex = _OspfIfNbrIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 5, 1, 1),
    _OspfIfNbrIntfIndex_Type()
)
ospfIfNbrIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfNbrIntfIndex.setStatus("current")
_OspfIfNbrIpAddr_Type = IpAddress
_OspfIfNbrIpAddr_Object = MibTableColumn
ospfIfNbrIpAddr = _OspfIfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 5, 1, 2),
    _OspfIfNbrIpAddr_Type()
)
ospfIfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfNbrIpAddr.setStatus("current")
_OspfIfNbrPriority_Type = Integer32
_OspfIfNbrPriority_Object = MibTableColumn
ospfIfNbrPriority = _OspfIfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 5, 1, 3),
    _OspfIfNbrPriority_Type()
)
ospfIfNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfNbrPriority.setStatus("current")


class _OspfIfNbrState_Type(Integer32):
    """Custom type ospfIfNbrState based on Integer32"""
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
        *(("attempt", 2),
          ("down", 1),
          ("exStart", 5),
          ("exchange", 6),
          ("full", 8),
          ("init", 3),
          ("loading", 7),
          ("twoway", 4))
    )


_OspfIfNbrState_Type.__name__ = "Integer32"
_OspfIfNbrState_Object = MibTableColumn
ospfIfNbrState = _OspfIfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 5, 1, 4),
    _OspfIfNbrState_Type()
)
ospfIfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfNbrState.setStatus("current")
_OspfIfNbrDesignatedRtr_Type = IpAddress
_OspfIfNbrDesignatedRtr_Object = MibTableColumn
ospfIfNbrDesignatedRtr = _OspfIfNbrDesignatedRtr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 5, 1, 5),
    _OspfIfNbrDesignatedRtr_Type()
)
ospfIfNbrDesignatedRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfNbrDesignatedRtr.setStatus("current")
_OspfIfNbrBackupDesignatedRtr_Type = IpAddress
_OspfIfNbrBackupDesignatedRtr_Object = MibTableColumn
ospfIfNbrBackupDesignatedRtr = _OspfIfNbrBackupDesignatedRtr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 5, 1, 6),
    _OspfIfNbrBackupDesignatedRtr_Type()
)
ospfIfNbrBackupDesignatedRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfNbrBackupDesignatedRtr.setStatus("current")
_OspfIfNbrIpAddress_Type = IpAddress
_OspfIfNbrIpAddress_Object = MibTableColumn
ospfIfNbrIpAddress = _OspfIfNbrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 4, 5, 1, 7),
    _OspfIfNbrIpAddress_Type()
)
ospfIfNbrIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfNbrIpAddress.setStatus("current")
_IgmpInfo_ObjectIdentity = ObjectIdentity
igmpInfo = _IgmpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 5)
)
_IgmpInfoTable_Object = MibTable
igmpInfoTable = _IgmpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 5, 1)
)
if mibBuilder.loadTexts:
    igmpInfoTable.setStatus("current")
_IgmpInfoEntry_Object = MibTableRow
igmpInfoEntry = _IgmpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 5, 1, 1)
)
igmpInfoEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "igmpInfoIndex"),
)
if mibBuilder.loadTexts:
    igmpInfoEntry.setStatus("current")
_IgmpInfoIndex_Type = Integer32
_IgmpInfoIndex_Object = MibTableColumn
igmpInfoIndex = _IgmpInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 5, 1, 1, 1),
    _IgmpInfoIndex_Type()
)
igmpInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInfoIndex.setStatus("current")
_IgmpInfoGroupId_Type = IpAddress
_IgmpInfoGroupId_Object = MibTableColumn
igmpInfoGroupId = _IgmpInfoGroupId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 5, 1, 1, 2),
    _IgmpInfoGroupId_Type()
)
igmpInfoGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInfoGroupId.setStatus("current")
_IgmpInfoVlanId_Type = Integer32
_IgmpInfoVlanId_Object = MibTableColumn
igmpInfoVlanId = _IgmpInfoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 5, 1, 1, 3),
    _IgmpInfoVlanId_Type()
)
igmpInfoVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInfoVlanId.setStatus("current")


class _IgmpInfoVersion_Type(Integer32):
    """Custom type igmpInfoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 3),
          ("v2", 2),
          ("v3", 1))
    )


_IgmpInfoVersion_Type.__name__ = "Integer32"
_IgmpInfoVersion_Object = MibTableColumn
igmpInfoVersion = _IgmpInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 5, 1, 1, 5),
    _IgmpInfoVersion_Type()
)
igmpInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInfoVersion.setStatus("current")
_IgmpInfoPortNum_Type = Integer32
_IgmpInfoPortNum_Object = MibTableColumn
igmpInfoPortNum = _IgmpInfoPortNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 5, 1, 1, 6),
    _IgmpInfoPortNum_Type()
)
igmpInfoPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInfoPortNum.setStatus("current")
_IgmpInfoExpires_Type = DisplayString
_IgmpInfoExpires_Object = MibTableColumn
igmpInfoExpires = _IgmpInfoExpires_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 5, 1, 1, 7),
    _IgmpInfoExpires_Type()
)
igmpInfoExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInfoExpires.setStatus("current")
_IgmpMrtrInfoTable_Object = MibTable
igmpMrtrInfoTable = _IgmpMrtrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 5, 2)
)
if mibBuilder.loadTexts:
    igmpMrtrInfoTable.setStatus("current")
_IgmpMrtrInfoEntry_Object = MibTableRow
igmpMrtrInfoEntry = _IgmpMrtrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 5, 2, 1)
)
igmpMrtrInfoEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "igmpMrtrInfoIndex"),
)
if mibBuilder.loadTexts:
    igmpMrtrInfoEntry.setStatus("current")
_IgmpMrtrInfoIndex_Type = Integer32
_IgmpMrtrInfoIndex_Object = MibTableColumn
igmpMrtrInfoIndex = _IgmpMrtrInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 5, 2, 1, 1),
    _IgmpMrtrInfoIndex_Type()
)
igmpMrtrInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpMrtrInfoIndex.setStatus("current")
_IgmpMrtrInfoVlanId_Type = Integer32
_IgmpMrtrInfoVlanId_Object = MibTableColumn
igmpMrtrInfoVlanId = _IgmpMrtrInfoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 5, 2, 1, 2),
    _IgmpMrtrInfoVlanId_Type()
)
igmpMrtrInfoVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpMrtrInfoVlanId.setStatus("current")
_IgmpMrtrInfoPortId_Type = Integer32
_IgmpMrtrInfoPortId_Object = MibTableColumn
igmpMrtrInfoPortId = _IgmpMrtrInfoPortId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 5, 2, 1, 3),
    _IgmpMrtrInfoPortId_Type()
)
igmpMrtrInfoPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpMrtrInfoPortId.setStatus("current")
_IgmpMrtrInfoVersion_Type = Integer32
_IgmpMrtrInfoVersion_Object = MibTableColumn
igmpMrtrInfoVersion = _IgmpMrtrInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 5, 2, 1, 4),
    _IgmpMrtrInfoVersion_Type()
)
igmpMrtrInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpMrtrInfoVersion.setStatus("current")
_IgmpMrtrInfoExpires_Type = DisplayString
_IgmpMrtrInfoExpires_Object = MibTableColumn
igmpMrtrInfoExpires = _IgmpMrtrInfoExpires_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 5, 2, 1, 5),
    _IgmpMrtrInfoExpires_Type()
)
igmpMrtrInfoExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpMrtrInfoExpires.setStatus("current")
_IgmpMrtrInfoMrt_Type = Integer32
_IgmpMrtrInfoMrt_Object = MibTableColumn
igmpMrtrInfoMrt = _IgmpMrtrInfoMrt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 5, 2, 1, 6),
    _IgmpMrtrInfoMrt_Type()
)
igmpMrtrInfoMrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpMrtrInfoMrt.setStatus("current")
_Rip2Info_ObjectIdentity = ObjectIdentity
rip2Info = _Rip2Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7)
)
_Rip2GeneralInfo_ObjectIdentity = ObjectIdentity
rip2GeneralInfo = _Rip2GeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7, 1)
)


class _RipInfoState_Type(Integer32):
    """Custom type ripInfoState based on Integer32"""
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


_RipInfoState_Type.__name__ = "Integer32"
_RipInfoState_Object = MibScalar
ripInfoState = _RipInfoState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7, 1, 1),
    _RipInfoState_Type()
)
ripInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoState.setStatus("current")


class _RipInfoUpdatePeriod_Type(Integer32):
    """Custom type ripInfoUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_RipInfoUpdatePeriod_Type.__name__ = "Integer32"
_RipInfoUpdatePeriod_Object = MibScalar
ripInfoUpdatePeriod = _RipInfoUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7, 1, 2),
    _RipInfoUpdatePeriod_Type()
)
ripInfoUpdatePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoUpdatePeriod.setStatus("current")
_Rip2InfoIntfTable_Object = MibTable
rip2InfoIntfTable = _Rip2InfoIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7, 2)
)
if mibBuilder.loadTexts:
    rip2InfoIntfTable.setStatus("current")
_RipInfoIntfEntry_Object = MibTableRow
ripInfoIntfEntry = _RipInfoIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7, 2, 1)
)
ripInfoIntfEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ripInfoIntfIndex"),
)
if mibBuilder.loadTexts:
    ripInfoIntfEntry.setStatus("current")
_RipInfoIntfIndex_Type = Integer32
_RipInfoIntfIndex_Object = MibTableColumn
ripInfoIntfIndex = _RipInfoIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7, 2, 1, 1),
    _RipInfoIntfIndex_Type()
)
ripInfoIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoIntfIndex.setStatus("current")


class _RipInfoIntfVersion_Type(Integer32):
    """Custom type ripInfoIntfVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ripVersion1", 1),
          ("ripVersion2", 2))
    )


_RipInfoIntfVersion_Type.__name__ = "Integer32"
_RipInfoIntfVersion_Object = MibTableColumn
ripInfoIntfVersion = _RipInfoIntfVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7, 2, 1, 2),
    _RipInfoIntfVersion_Type()
)
ripInfoIntfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoIntfVersion.setStatus("current")
_RipInfoIntfAddress_Type = IpAddress
_RipInfoIntfAddress_Object = MibTableColumn
ripInfoIntfAddress = _RipInfoIntfAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7, 2, 1, 3),
    _RipInfoIntfAddress_Type()
)
ripInfoIntfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoIntfAddress.setStatus("current")


class _RipInfoIntfState_Type(Integer32):
    """Custom type ripInfoIntfState based on Integer32"""
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


_RipInfoIntfState_Type.__name__ = "Integer32"
_RipInfoIntfState_Object = MibTableColumn
ripInfoIntfState = _RipInfoIntfState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7, 2, 1, 4),
    _RipInfoIntfState_Type()
)
ripInfoIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoIntfState.setStatus("current")


class _RipInfoIntfListen_Type(Integer32):
    """Custom type ripInfoIntfListen based on Integer32"""
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


_RipInfoIntfListen_Type.__name__ = "Integer32"
_RipInfoIntfListen_Object = MibTableColumn
ripInfoIntfListen = _RipInfoIntfListen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7, 2, 1, 5),
    _RipInfoIntfListen_Type()
)
ripInfoIntfListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoIntfListen.setStatus("current")


class _RipInfoIntfTrigUpdate_Type(Integer32):
    """Custom type ripInfoIntfTrigUpdate based on Integer32"""
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


_RipInfoIntfTrigUpdate_Type.__name__ = "Integer32"
_RipInfoIntfTrigUpdate_Object = MibTableColumn
ripInfoIntfTrigUpdate = _RipInfoIntfTrigUpdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7, 2, 1, 6),
    _RipInfoIntfTrigUpdate_Type()
)
ripInfoIntfTrigUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoIntfTrigUpdate.setStatus("current")


class _RipInfoIntfMcastUpdate_Type(Integer32):
    """Custom type ripInfoIntfMcastUpdate based on Integer32"""
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


_RipInfoIntfMcastUpdate_Type.__name__ = "Integer32"
_RipInfoIntfMcastUpdate_Object = MibTableColumn
ripInfoIntfMcastUpdate = _RipInfoIntfMcastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7, 2, 1, 7),
    _RipInfoIntfMcastUpdate_Type()
)
ripInfoIntfMcastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoIntfMcastUpdate.setStatus("current")


class _RipInfoIntfPoisonReverse_Type(Integer32):
    """Custom type ripInfoIntfPoisonReverse based on Integer32"""
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


_RipInfoIntfPoisonReverse_Type.__name__ = "Integer32"
_RipInfoIntfPoisonReverse_Object = MibTableColumn
ripInfoIntfPoisonReverse = _RipInfoIntfPoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7, 2, 1, 8),
    _RipInfoIntfPoisonReverse_Type()
)
ripInfoIntfPoisonReverse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoIntfPoisonReverse.setStatus("current")


class _RipInfoIntfSupply_Type(Integer32):
    """Custom type ripInfoIntfSupply based on Integer32"""
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


_RipInfoIntfSupply_Type.__name__ = "Integer32"
_RipInfoIntfSupply_Object = MibTableColumn
ripInfoIntfSupply = _RipInfoIntfSupply_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7, 2, 1, 9),
    _RipInfoIntfSupply_Type()
)
ripInfoIntfSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoIntfSupply.setStatus("current")


class _RipInfoIntfMetric_Type(Integer32):
    """Custom type ripInfoIntfMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RipInfoIntfMetric_Type.__name__ = "Integer32"
_RipInfoIntfMetric_Object = MibTableColumn
ripInfoIntfMetric = _RipInfoIntfMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7, 2, 1, 10),
    _RipInfoIntfMetric_Type()
)
ripInfoIntfMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoIntfMetric.setStatus("current")


class _RipInfoIntfAuth_Type(Integer32):
    """Custom type ripInfoIntfAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("password", 2))
    )


_RipInfoIntfAuth_Type.__name__ = "Integer32"
_RipInfoIntfAuth_Object = MibTableColumn
ripInfoIntfAuth = _RipInfoIntfAuth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7, 2, 1, 11),
    _RipInfoIntfAuth_Type()
)
ripInfoIntfAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoIntfAuth.setStatus("current")


class _RipInfoIntfKey_Type(DisplayString):
    """Custom type ripInfoIntfKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RipInfoIntfKey_Type.__name__ = "DisplayString"
_RipInfoIntfKey_Object = MibTableColumn
ripInfoIntfKey = _RipInfoIntfKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7, 2, 1, 12),
    _RipInfoIntfKey_Type()
)
ripInfoIntfKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoIntfKey.setStatus("current")


class _RipInfoIntfDefault_Type(Integer32):
    """Custom type ripInfoIntfDefault based on Integer32"""
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
        *(("both", 1),
          ("listen", 2),
          ("none", 4),
          ("supply", 3))
    )


_RipInfoIntfDefault_Type.__name__ = "Integer32"
_RipInfoIntfDefault_Object = MibTableColumn
ripInfoIntfDefault = _RipInfoIntfDefault_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 7, 2, 1, 13),
    _RipInfoIntfDefault_Type()
)
ripInfoIntfDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoIntfDefault.setStatus("current")
_IpInfo_ObjectIdentity = ObjectIdentity
ipInfo = _IpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8)
)
_IpInfoRouterID_Type = IpAddress
_IpInfoRouterID_Object = MibScalar
ipInfoRouterID = _IpInfoRouterID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 1),
    _IpInfoRouterID_Type()
)
ipInfoRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInfoRouterID.setStatus("current")
_IpIntfInfoTable_Object = MibTable
ipIntfInfoTable = _IpIntfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 2)
)
if mibBuilder.loadTexts:
    ipIntfInfoTable.setStatus("current")
_IntfInfoEntry_Object = MibTableRow
intfInfoEntry = _IntfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 2, 1)
)
intfInfoEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "intfInfoIndex"),
)
if mibBuilder.loadTexts:
    intfInfoEntry.setStatus("current")
_IntfInfoIndex_Type = Integer32
_IntfInfoIndex_Object = MibTableColumn
intfInfoIndex = _IntfInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 2, 1, 1),
    _IntfInfoIndex_Type()
)
intfInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfInfoIndex.setStatus("current")
_IntfInfoAddr_Type = DisplayString
_IntfInfoAddr_Object = MibTableColumn
intfInfoAddr = _IntfInfoAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 2, 1, 2),
    _IntfInfoAddr_Type()
)
intfInfoAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfInfoAddr.setStatus("current")
_IntfInfoNetMask_Type = DisplayString
_IntfInfoNetMask_Object = MibTableColumn
intfInfoNetMask = _IntfInfoNetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 2, 1, 3),
    _IntfInfoNetMask_Type()
)
intfInfoNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfInfoNetMask.setStatus("current")
_IntfInfoBcastAddr_Type = DisplayString
_IntfInfoBcastAddr_Object = MibTableColumn
intfInfoBcastAddr = _IntfInfoBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 2, 1, 4),
    _IntfInfoBcastAddr_Type()
)
intfInfoBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfInfoBcastAddr.setStatus("current")
_IntfInfoVlan_Type = Integer32
_IntfInfoVlan_Object = MibTableColumn
intfInfoVlan = _IntfInfoVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 2, 1, 5),
    _IntfInfoVlan_Type()
)
intfInfoVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfInfoVlan.setStatus("current")


class _IntfInfoStatus_Type(Integer32):
    """Custom type intfInfoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("down", 2),
          ("up", 1))
    )


_IntfInfoStatus_Type.__name__ = "Integer32"
_IntfInfoStatus_Object = MibTableColumn
intfInfoStatus = _IntfInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 2, 1, 6),
    _IntfInfoStatus_Type()
)
intfInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfInfoStatus.setStatus("current")
_GatewayInfoTable_Object = MibTable
gatewayInfoTable = _GatewayInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 3)
)
if mibBuilder.loadTexts:
    gatewayInfoTable.setStatus("current")
_GatewayInfoEntry_Object = MibTableRow
gatewayInfoEntry = _GatewayInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 3, 1)
)
gatewayInfoEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "gatewayInfoIndex"),
)
if mibBuilder.loadTexts:
    gatewayInfoEntry.setStatus("current")
_GatewayInfoIndex_Type = Integer32
_GatewayInfoIndex_Object = MibTableColumn
gatewayInfoIndex = _GatewayInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 3, 1, 1),
    _GatewayInfoIndex_Type()
)
gatewayInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayInfoIndex.setStatus("current")
_GatewayInfoAddr_Type = IpAddress
_GatewayInfoAddr_Object = MibTableColumn
gatewayInfoAddr = _GatewayInfoAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 3, 1, 2),
    _GatewayInfoAddr_Type()
)
gatewayInfoAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayInfoAddr.setStatus("current")


class _GatewayInfoStatus_Type(Integer32):
    """Custom type gatewayInfoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("up", 1))
    )


_GatewayInfoStatus_Type.__name__ = "Integer32"
_GatewayInfoStatus_Object = MibTableColumn
gatewayInfoStatus = _GatewayInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 3, 1, 4),
    _GatewayInfoStatus_Type()
)
gatewayInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayInfoStatus.setStatus("current")


class _IpInfoBootpRelayState_Type(Integer32):
    """Custom type ipInfoBootpRelayState based on Integer32"""
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


_IpInfoBootpRelayState_Type.__name__ = "Integer32"
_IpInfoBootpRelayState_Object = MibScalar
ipInfoBootpRelayState = _IpInfoBootpRelayState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 4),
    _IpInfoBootpRelayState_Type()
)
ipInfoBootpRelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInfoBootpRelayState.setStatus("current")
_IpInfoBootpRelayAddr_Type = IpAddress
_IpInfoBootpRelayAddr_Object = MibScalar
ipInfoBootpRelayAddr = _IpInfoBootpRelayAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 5),
    _IpInfoBootpRelayAddr_Type()
)
ipInfoBootpRelayAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInfoBootpRelayAddr.setStatus("current")
_IpInfoBootpRelayAddr2_Type = IpAddress
_IpInfoBootpRelayAddr2_Object = MibScalar
ipInfoBootpRelayAddr2 = _IpInfoBootpRelayAddr2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 6),
    _IpInfoBootpRelayAddr2_Type()
)
ipInfoBootpRelayAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInfoBootpRelayAddr2.setStatus("current")


class _IpInfoFwdState_Type(Integer32):
    """Custom type ipInfoFwdState based on Integer32"""
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


_IpInfoFwdState_Type.__name__ = "Integer32"
_IpInfoFwdState_Object = MibScalar
ipInfoFwdState = _IpInfoFwdState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 7),
    _IpInfoFwdState_Type()
)
ipInfoFwdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInfoFwdState.setStatus("current")


class _IpInfoFwdDirectedBcast_Type(Integer32):
    """Custom type ipInfoFwdDirectedBcast based on Integer32"""
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


_IpInfoFwdDirectedBcast_Type.__name__ = "Integer32"
_IpInfoFwdDirectedBcast_Object = MibScalar
ipInfoFwdDirectedBcast = _IpInfoFwdDirectedBcast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 8),
    _IpInfoFwdDirectedBcast_Type()
)
ipInfoFwdDirectedBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInfoFwdDirectedBcast.setStatus("current")
_IpInfoNwfTable_Object = MibTable
ipInfoNwfTable = _IpInfoNwfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 9)
)
if mibBuilder.loadTexts:
    ipInfoNwfTable.setStatus("current")
_IpInfoNwfEntry_Object = MibTableRow
ipInfoNwfEntry = _IpInfoNwfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 9, 1)
)
ipInfoNwfEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipInfoNwfIndex"),
)
if mibBuilder.loadTexts:
    ipInfoNwfEntry.setStatus("current")
_IpInfoNwfIndex_Type = Integer32
_IpInfoNwfIndex_Object = MibTableColumn
ipInfoNwfIndex = _IpInfoNwfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 9, 1, 1),
    _IpInfoNwfIndex_Type()
)
ipInfoNwfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInfoNwfIndex.setStatus("current")
_IpInfoNwfAddr_Type = IpAddress
_IpInfoNwfAddr_Object = MibTableColumn
ipInfoNwfAddr = _IpInfoNwfAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 9, 1, 2),
    _IpInfoNwfAddr_Type()
)
ipInfoNwfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInfoNwfAddr.setStatus("current")
_IpInfoNwfMask_Type = IpAddress
_IpInfoNwfMask_Object = MibTableColumn
ipInfoNwfMask = _IpInfoNwfMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 9, 1, 3),
    _IpInfoNwfMask_Type()
)
ipInfoNwfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInfoNwfMask.setStatus("current")


class _IpInfoNwfState_Type(Integer32):
    """Custom type ipInfoNwfState based on Integer32"""
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


_IpInfoNwfState_Type.__name__ = "Integer32"
_IpInfoNwfState_Object = MibTableColumn
ipInfoNwfState = _IpInfoNwfState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 9, 1, 4),
    _IpInfoNwfState_Type()
)
ipInfoNwfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInfoNwfState.setStatus("current")
_IpInfoRmapTable_Object = MibTable
ipInfoRmapTable = _IpInfoRmapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 10)
)
if mibBuilder.loadTexts:
    ipInfoRmapTable.setStatus("current")
_IpInfoRmapEntry_Object = MibTableRow
ipInfoRmapEntry = _IpInfoRmapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 10, 1)
)
ipInfoRmapEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipInfoRmapIndex"),
)
if mibBuilder.loadTexts:
    ipInfoRmapEntry.setStatus("current")
_IpInfoRmapIndex_Type = Integer32
_IpInfoRmapIndex_Object = MibTableColumn
ipInfoRmapIndex = _IpInfoRmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 10, 1, 1),
    _IpInfoRmapIndex_Type()
)
ipInfoRmapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInfoRmapIndex.setStatus("current")


class _IpInfoRmapLp_Type(Unsigned32):
    """Custom type ipInfoRmapLp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IpInfoRmapLp_Type.__name__ = "Unsigned32"
_IpInfoRmapLp_Object = MibTableColumn
ipInfoRmapLp = _IpInfoRmapLp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 10, 1, 2),
    _IpInfoRmapLp_Type()
)
ipInfoRmapLp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInfoRmapLp.setStatus("current")


class _IpInfoRmapMetric_Type(Unsigned32):
    """Custom type ipInfoRmapMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IpInfoRmapMetric_Type.__name__ = "Unsigned32"
_IpInfoRmapMetric_Object = MibTableColumn
ipInfoRmapMetric = _IpInfoRmapMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 10, 1, 3),
    _IpInfoRmapMetric_Type()
)
ipInfoRmapMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInfoRmapMetric.setStatus("current")


class _IpInfoRmapPrec_Type(Integer32):
    """Custom type ipInfoRmapPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpInfoRmapPrec_Type.__name__ = "Integer32"
_IpInfoRmapPrec_Object = MibTableColumn
ipInfoRmapPrec = _IpInfoRmapPrec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 10, 1, 4),
    _IpInfoRmapPrec_Type()
)
ipInfoRmapPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInfoRmapPrec.setStatus("current")


class _IpInfoRmapWeight_Type(Integer32):
    """Custom type ipInfoRmapWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpInfoRmapWeight_Type.__name__ = "Integer32"
_IpInfoRmapWeight_Object = MibTableColumn
ipInfoRmapWeight = _IpInfoRmapWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 10, 1, 5),
    _IpInfoRmapWeight_Type()
)
ipInfoRmapWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInfoRmapWeight.setStatus("current")


class _IpInfoRmapState_Type(Integer32):
    """Custom type ipInfoRmapState based on Integer32"""
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


_IpInfoRmapState_Type.__name__ = "Integer32"
_IpInfoRmapState_Object = MibTableColumn
ipInfoRmapState = _IpInfoRmapState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 10, 1, 6),
    _IpInfoRmapState_Type()
)
ipInfoRmapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInfoRmapState.setStatus("current")


class _IpInfoRmapAp_Type(DisplayString):
    """Custom type ipInfoRmapAp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_IpInfoRmapAp_Type.__name__ = "DisplayString"
_IpInfoRmapAp_Object = MibTableColumn
ipInfoRmapAp = _IpInfoRmapAp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 10, 1, 7),
    _IpInfoRmapAp_Type()
)
ipInfoRmapAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInfoRmapAp.setStatus("current")


class _IpInfoRmapMetricType_Type(Integer32):
    """Custom type ipInfoRmapMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("type1", 2),
          ("type2", 3))
    )


_IpInfoRmapMetricType_Type.__name__ = "Integer32"
_IpInfoRmapMetricType_Object = MibTableColumn
ipInfoRmapMetricType = _IpInfoRmapMetricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 10, 1, 8),
    _IpInfoRmapMetricType_Type()
)
ipInfoRmapMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInfoRmapMetricType.setStatus("current")
_IpOspfInfo_ObjectIdentity = ObjectIdentity
ipOspfInfo = _IpOspfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11)
)


class _IpOspfInfoState_Type(Integer32):
    """Custom type ipOspfInfoState based on Integer32"""
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


_IpOspfInfoState_Type.__name__ = "Integer32"
_IpOspfInfoState_Object = MibScalar
ipOspfInfoState = _IpOspfInfoState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 1),
    _IpOspfInfoState_Type()
)
ipOspfInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfInfoState.setStatus("current")


class _IpOspfInfoDefaultRouteMetric_Type(Integer32):
    """Custom type ipOspfInfoDefaultRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_IpOspfInfoDefaultRouteMetric_Type.__name__ = "Integer32"
_IpOspfInfoDefaultRouteMetric_Object = MibScalar
ipOspfInfoDefaultRouteMetric = _IpOspfInfoDefaultRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 2),
    _IpOspfInfoDefaultRouteMetric_Type()
)
ipOspfInfoDefaultRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfInfoDefaultRouteMetric.setStatus("current")


class _IpOspfInfoDefaultRouteMetricType_Type(Integer32):
    """Custom type ipOspfInfoDefaultRouteMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("type1", 2),
          ("type2", 3))
    )


_IpOspfInfoDefaultRouteMetricType_Type.__name__ = "Integer32"
_IpOspfInfoDefaultRouteMetricType_Object = MibScalar
ipOspfInfoDefaultRouteMetricType = _IpOspfInfoDefaultRouteMetricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 3),
    _IpOspfInfoDefaultRouteMetricType_Type()
)
ipOspfInfoDefaultRouteMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfInfoDefaultRouteMetricType.setStatus("current")
_IpOspfInfoRouterID_Type = IpAddress
_IpOspfInfoRouterID_Object = MibScalar
ipOspfInfoRouterID = _IpOspfInfoRouterID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 4),
    _IpOspfInfoRouterID_Type()
)
ipOspfInfoRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfInfoRouterID.setStatus("current")


class _IpOspfInfoLsdbLimit_Type(Integer32):
    """Custom type ipOspfInfoLsdbLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_IpOspfInfoLsdbLimit_Type.__name__ = "Integer32"
_IpOspfInfoLsdbLimit_Object = MibScalar
ipOspfInfoLsdbLimit = _IpOspfInfoLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 5),
    _IpOspfInfoLsdbLimit_Type()
)
ipOspfInfoLsdbLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfInfoLsdbLimit.setStatus("current")
_IpOspfAreaInfoTable_Object = MibTable
ipOspfAreaInfoTable = _IpOspfAreaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 6)
)
if mibBuilder.loadTexts:
    ipOspfAreaInfoTable.setStatus("current")
_IpOspfAreaInfoEntry_Object = MibTableRow
ipOspfAreaInfoEntry = _IpOspfAreaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 6, 1)
)
ipOspfAreaInfoEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipOspfAreaInfoIndex"),
    (0, "BLADETYPE2-NETWORK-MIB", "ipOspfAreaInfoId"),
)
if mibBuilder.loadTexts:
    ipOspfAreaInfoEntry.setStatus("current")
_IpOspfAreaInfoIndex_Type = Integer32
_IpOspfAreaInfoIndex_Object = MibTableColumn
ipOspfAreaInfoIndex = _IpOspfAreaInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 6, 1, 1),
    _IpOspfAreaInfoIndex_Type()
)
ipOspfAreaInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfAreaInfoIndex.setStatus("current")
_IpOspfAreaInfoId_Type = IpAddress
_IpOspfAreaInfoId_Object = MibTableColumn
ipOspfAreaInfoId = _IpOspfAreaInfoId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 6, 1, 2),
    _IpOspfAreaInfoId_Type()
)
ipOspfAreaInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfAreaInfoId.setStatus("current")


class _IpOspfAreaInfoSpfInterval_Type(Integer32):
    """Custom type ipOspfAreaInfoSpfInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpOspfAreaInfoSpfInterval_Type.__name__ = "Integer32"
_IpOspfAreaInfoSpfInterval_Object = MibTableColumn
ipOspfAreaInfoSpfInterval = _IpOspfAreaInfoSpfInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 6, 1, 3),
    _IpOspfAreaInfoSpfInterval_Type()
)
ipOspfAreaInfoSpfInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfAreaInfoSpfInterval.setStatus("current")


class _IpOspfAreaInfoAuthType_Type(Integer32):
    """Custom type ipOspfAreaInfoAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("none", 1),
          ("password", 2))
    )


_IpOspfAreaInfoAuthType_Type.__name__ = "Integer32"
_IpOspfAreaInfoAuthType_Object = MibTableColumn
ipOspfAreaInfoAuthType = _IpOspfAreaInfoAuthType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 6, 1, 4),
    _IpOspfAreaInfoAuthType_Type()
)
ipOspfAreaInfoAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfAreaInfoAuthType.setStatus("current")


class _IpOspfAreaInfoType_Type(Integer32):
    """Custom type ipOspfAreaInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nssa", 2),
          ("stub", 1),
          ("transit", 0))
    )


_IpOspfAreaInfoType_Type.__name__ = "Integer32"
_IpOspfAreaInfoType_Object = MibTableColumn
ipOspfAreaInfoType = _IpOspfAreaInfoType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 6, 1, 5),
    _IpOspfAreaInfoType_Type()
)
ipOspfAreaInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfAreaInfoType.setStatus("current")


class _IpOspfAreaInfoMetric_Type(Integer32):
    """Custom type ipOspfAreaInfoMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpOspfAreaInfoMetric_Type.__name__ = "Integer32"
_IpOspfAreaInfoMetric_Object = MibTableColumn
ipOspfAreaInfoMetric = _IpOspfAreaInfoMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 6, 1, 6),
    _IpOspfAreaInfoMetric_Type()
)
ipOspfAreaInfoMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfAreaInfoMetric.setStatus("current")


class _IpOspfAreaInfoStatus_Type(Integer32):
    """Custom type ipOspfAreaInfoStatus based on Integer32"""
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


_IpOspfAreaInfoStatus_Type.__name__ = "Integer32"
_IpOspfAreaInfoStatus_Object = MibTableColumn
ipOspfAreaInfoStatus = _IpOspfAreaInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 6, 1, 7),
    _IpOspfAreaInfoStatus_Type()
)
ipOspfAreaInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfAreaInfoStatus.setStatus("current")
_IpOspfRangeInfoTable_Object = MibTable
ipOspfRangeInfoTable = _IpOspfRangeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 7)
)
if mibBuilder.loadTexts:
    ipOspfRangeInfoTable.setStatus("current")
_IpOspfRangeInfoEntry_Object = MibTableRow
ipOspfRangeInfoEntry = _IpOspfRangeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 7, 1)
)
ipOspfRangeInfoEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipOspfRangeInfoIndex"),
)
if mibBuilder.loadTexts:
    ipOspfRangeInfoEntry.setStatus("current")
_IpOspfRangeInfoIndex_Type = Integer32
_IpOspfRangeInfoIndex_Object = MibTableColumn
ipOspfRangeInfoIndex = _IpOspfRangeInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 7, 1, 1),
    _IpOspfRangeInfoIndex_Type()
)
ipOspfRangeInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfRangeInfoIndex.setStatus("current")
_IpOspfRangeInfoAddr_Type = IpAddress
_IpOspfRangeInfoAddr_Object = MibTableColumn
ipOspfRangeInfoAddr = _IpOspfRangeInfoAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 7, 1, 2),
    _IpOspfRangeInfoAddr_Type()
)
ipOspfRangeInfoAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfRangeInfoAddr.setStatus("current")
_IpOspfRangeInfoMask_Type = IpAddress
_IpOspfRangeInfoMask_Object = MibTableColumn
ipOspfRangeInfoMask = _IpOspfRangeInfoMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 7, 1, 3),
    _IpOspfRangeInfoMask_Type()
)
ipOspfRangeInfoMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfRangeInfoMask.setStatus("current")
_IpOspfRangeInfoAreaIndex_Type = Integer32
_IpOspfRangeInfoAreaIndex_Object = MibTableColumn
ipOspfRangeInfoAreaIndex = _IpOspfRangeInfoAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 7, 1, 4),
    _IpOspfRangeInfoAreaIndex_Type()
)
ipOspfRangeInfoAreaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfRangeInfoAreaIndex.setStatus("current")


class _IpOspfRangeInfoHideState_Type(Integer32):
    """Custom type ipOspfRangeInfoHideState based on Integer32"""
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


_IpOspfRangeInfoHideState_Type.__name__ = "Integer32"
_IpOspfRangeInfoHideState_Object = MibTableColumn
ipOspfRangeInfoHideState = _IpOspfRangeInfoHideState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 7, 1, 5),
    _IpOspfRangeInfoHideState_Type()
)
ipOspfRangeInfoHideState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfRangeInfoHideState.setStatus("current")


class _IpOspfRangeInfoState_Type(Integer32):
    """Custom type ipOspfRangeInfoState based on Integer32"""
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


_IpOspfRangeInfoState_Type.__name__ = "Integer32"
_IpOspfRangeInfoState_Object = MibTableColumn
ipOspfRangeInfoState = _IpOspfRangeInfoState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 7, 1, 6),
    _IpOspfRangeInfoState_Type()
)
ipOspfRangeInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfRangeInfoState.setStatus("current")
_IpOspfIntfInfoTable_Object = MibTable
ipOspfIntfInfoTable = _IpOspfIntfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 8)
)
if mibBuilder.loadTexts:
    ipOspfIntfInfoTable.setStatus("current")
_IpOspfIntfInfoEntry_Object = MibTableRow
ipOspfIntfInfoEntry = _IpOspfIntfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 8, 1)
)
ipOspfIntfInfoEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipOspfIntfInfoIndex"),
)
if mibBuilder.loadTexts:
    ipOspfIntfInfoEntry.setStatus("current")
_IpOspfIntfInfoIndex_Type = Integer32
_IpOspfIntfInfoIndex_Object = MibTableColumn
ipOspfIntfInfoIndex = _IpOspfIntfInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 8, 1, 1),
    _IpOspfIntfInfoIndex_Type()
)
ipOspfIntfInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfIntfInfoIndex.setStatus("current")
_IpOspfIntfInfoId_Type = IpAddress
_IpOspfIntfInfoId_Object = MibTableColumn
ipOspfIntfInfoId = _IpOspfIntfInfoId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 8, 1, 2),
    _IpOspfIntfInfoId_Type()
)
ipOspfIntfInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfIntfInfoId.setStatus("current")


class _IpOspfIntfInfoArea_Type(Integer32):
    """Custom type ipOspfIntfInfoArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_IpOspfIntfInfoArea_Type.__name__ = "Integer32"
_IpOspfIntfInfoArea_Object = MibTableColumn
ipOspfIntfInfoArea = _IpOspfIntfInfoArea_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 8, 1, 3),
    _IpOspfIntfInfoArea_Type()
)
ipOspfIntfInfoArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfIntfInfoArea.setStatus("current")


class _IpOspfIntfInfoMdkey_Type(Integer32):
    """Custom type ipOspfIntfInfoMdkey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpOspfIntfInfoMdkey_Type.__name__ = "Integer32"
_IpOspfIntfInfoMdkey_Object = MibTableColumn
ipOspfIntfInfoMdkey = _IpOspfIntfInfoMdkey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 8, 1, 4),
    _IpOspfIntfInfoMdkey_Type()
)
ipOspfIntfInfoMdkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfIntfInfoMdkey.setStatus("current")


class _IpOspfIntfInfoCost_Type(Integer32):
    """Custom type ipOspfIntfInfoCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpOspfIntfInfoCost_Type.__name__ = "Integer32"
_IpOspfIntfInfoCost_Object = MibTableColumn
ipOspfIntfInfoCost = _IpOspfIntfInfoCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 8, 1, 5),
    _IpOspfIntfInfoCost_Type()
)
ipOspfIntfInfoCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfIntfInfoCost.setStatus("current")


class _IpOspfIntfInfoPrio_Type(Integer32):
    """Custom type ipOspfIntfInfoPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpOspfIntfInfoPrio_Type.__name__ = "Integer32"
_IpOspfIntfInfoPrio_Object = MibTableColumn
ipOspfIntfInfoPrio = _IpOspfIntfInfoPrio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 8, 1, 6),
    _IpOspfIntfInfoPrio_Type()
)
ipOspfIntfInfoPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfIntfInfoPrio.setStatus("current")


class _IpOspfIntfInfoHello_Type(Integer32):
    """Custom type ipOspfIntfInfoHello based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpOspfIntfInfoHello_Type.__name__ = "Integer32"
_IpOspfIntfInfoHello_Object = MibTableColumn
ipOspfIntfInfoHello = _IpOspfIntfInfoHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 8, 1, 7),
    _IpOspfIntfInfoHello_Type()
)
ipOspfIntfInfoHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfIntfInfoHello.setStatus("current")


class _IpOspfIntfInfoDead_Type(Integer32):
    """Custom type ipOspfIntfInfoDead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpOspfIntfInfoDead_Type.__name__ = "Integer32"
_IpOspfIntfInfoDead_Object = MibTableColumn
ipOspfIntfInfoDead = _IpOspfIntfInfoDead_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 8, 1, 8),
    _IpOspfIntfInfoDead_Type()
)
ipOspfIntfInfoDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfIntfInfoDead.setStatus("current")


class _IpOspfIntfInfoTrans_Type(Integer32):
    """Custom type ipOspfIntfInfoTrans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_IpOspfIntfInfoTrans_Type.__name__ = "Integer32"
_IpOspfIntfInfoTrans_Object = MibTableColumn
ipOspfIntfInfoTrans = _IpOspfIntfInfoTrans_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 8, 1, 9),
    _IpOspfIntfInfoTrans_Type()
)
ipOspfIntfInfoTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfIntfInfoTrans.setStatus("current")


class _IpOspfIntfInfoRetra_Type(Integer32):
    """Custom type ipOspfIntfInfoRetra based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_IpOspfIntfInfoRetra_Type.__name__ = "Integer32"
_IpOspfIntfInfoRetra_Object = MibTableColumn
ipOspfIntfInfoRetra = _IpOspfIntfInfoRetra_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 8, 1, 10),
    _IpOspfIntfInfoRetra_Type()
)
ipOspfIntfInfoRetra.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfIntfInfoRetra.setStatus("current")


class _IpOspfIntfInfoAuthKey_Type(DisplayString):
    """Custom type ipOspfIntfInfoAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IpOspfIntfInfoAuthKey_Type.__name__ = "DisplayString"
_IpOspfIntfInfoAuthKey_Object = MibTableColumn
ipOspfIntfInfoAuthKey = _IpOspfIntfInfoAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 8, 1, 11),
    _IpOspfIntfInfoAuthKey_Type()
)
ipOspfIntfInfoAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfIntfInfoAuthKey.setStatus("current")


class _IpOspfIntfInfoStatus_Type(Integer32):
    """Custom type ipOspfIntfInfoStatus based on Integer32"""
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


_IpOspfIntfInfoStatus_Type.__name__ = "Integer32"
_IpOspfIntfInfoStatus_Object = MibTableColumn
ipOspfIntfInfoStatus = _IpOspfIntfInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 8, 1, 12),
    _IpOspfIntfInfoStatus_Type()
)
ipOspfIntfInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfIntfInfoStatus.setStatus("current")
_IpOspfVirtIntfInfoTable_Object = MibTable
ipOspfVirtIntfInfoTable = _IpOspfVirtIntfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 9)
)
if mibBuilder.loadTexts:
    ipOspfVirtIntfInfoTable.setStatus("current")
_IpOspfVirtIntfInfoEntry_Object = MibTableRow
ipOspfVirtIntfInfoEntry = _IpOspfVirtIntfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 9, 1)
)
ipOspfVirtIntfInfoEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipOspfVirtIntfInfoIndex"),
)
if mibBuilder.loadTexts:
    ipOspfVirtIntfInfoEntry.setStatus("current")
_IpOspfVirtIntfInfoIndex_Type = Integer32
_IpOspfVirtIntfInfoIndex_Object = MibTableColumn
ipOspfVirtIntfInfoIndex = _IpOspfVirtIntfInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 9, 1, 1),
    _IpOspfVirtIntfInfoIndex_Type()
)
ipOspfVirtIntfInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfVirtIntfInfoIndex.setStatus("current")


class _IpOspfVirtIntfInfoAreaId_Type(Integer32):
    """Custom type ipOspfVirtIntfInfoAreaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_IpOspfVirtIntfInfoAreaId_Type.__name__ = "Integer32"
_IpOspfVirtIntfInfoAreaId_Object = MibTableColumn
ipOspfVirtIntfInfoAreaId = _IpOspfVirtIntfInfoAreaId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 9, 1, 2),
    _IpOspfVirtIntfInfoAreaId_Type()
)
ipOspfVirtIntfInfoAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfVirtIntfInfoAreaId.setStatus("current")
_IpOspfVirtIntfInfoNbr_Type = IpAddress
_IpOspfVirtIntfInfoNbr_Object = MibTableColumn
ipOspfVirtIntfInfoNbr = _IpOspfVirtIntfInfoNbr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 9, 1, 3),
    _IpOspfVirtIntfInfoNbr_Type()
)
ipOspfVirtIntfInfoNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfVirtIntfInfoNbr.setStatus("current")


class _IpOspfVirtIntfInfoMdkey_Type(Integer32):
    """Custom type ipOspfVirtIntfInfoMdkey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpOspfVirtIntfInfoMdkey_Type.__name__ = "Integer32"
_IpOspfVirtIntfInfoMdkey_Object = MibTableColumn
ipOspfVirtIntfInfoMdkey = _IpOspfVirtIntfInfoMdkey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 9, 1, 4),
    _IpOspfVirtIntfInfoMdkey_Type()
)
ipOspfVirtIntfInfoMdkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfVirtIntfInfoMdkey.setStatus("current")


class _IpOspfVirtIntfInfoHello_Type(Integer32):
    """Custom type ipOspfVirtIntfInfoHello based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpOspfVirtIntfInfoHello_Type.__name__ = "Integer32"
_IpOspfVirtIntfInfoHello_Object = MibTableColumn
ipOspfVirtIntfInfoHello = _IpOspfVirtIntfInfoHello_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 9, 1, 5),
    _IpOspfVirtIntfInfoHello_Type()
)
ipOspfVirtIntfInfoHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfVirtIntfInfoHello.setStatus("current")


class _IpOspfVirtIntfInfoDead_Type(Integer32):
    """Custom type ipOspfVirtIntfInfoDead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpOspfVirtIntfInfoDead_Type.__name__ = "Integer32"
_IpOspfVirtIntfInfoDead_Object = MibTableColumn
ipOspfVirtIntfInfoDead = _IpOspfVirtIntfInfoDead_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 9, 1, 6),
    _IpOspfVirtIntfInfoDead_Type()
)
ipOspfVirtIntfInfoDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfVirtIntfInfoDead.setStatus("current")


class _IpOspfVirtIntfInfoTrans_Type(Integer32):
    """Custom type ipOspfVirtIntfInfoTrans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_IpOspfVirtIntfInfoTrans_Type.__name__ = "Integer32"
_IpOspfVirtIntfInfoTrans_Object = MibTableColumn
ipOspfVirtIntfInfoTrans = _IpOspfVirtIntfInfoTrans_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 9, 1, 7),
    _IpOspfVirtIntfInfoTrans_Type()
)
ipOspfVirtIntfInfoTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfVirtIntfInfoTrans.setStatus("current")


class _IpOspfVirtIntfInfoRetra_Type(Integer32):
    """Custom type ipOspfVirtIntfInfoRetra based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_IpOspfVirtIntfInfoRetra_Type.__name__ = "Integer32"
_IpOspfVirtIntfInfoRetra_Object = MibTableColumn
ipOspfVirtIntfInfoRetra = _IpOspfVirtIntfInfoRetra_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 9, 1, 8),
    _IpOspfVirtIntfInfoRetra_Type()
)
ipOspfVirtIntfInfoRetra.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfVirtIntfInfoRetra.setStatus("current")


class _IpOspfVirtIntfInfoAuthKey_Type(DisplayString):
    """Custom type ipOspfVirtIntfInfoAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IpOspfVirtIntfInfoAuthKey_Type.__name__ = "DisplayString"
_IpOspfVirtIntfInfoAuthKey_Object = MibTableColumn
ipOspfVirtIntfInfoAuthKey = _IpOspfVirtIntfInfoAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 9, 1, 9),
    _IpOspfVirtIntfInfoAuthKey_Type()
)
ipOspfVirtIntfInfoAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfVirtIntfInfoAuthKey.setStatus("current")


class _IpOspfVirtIntfInfoStatus_Type(Integer32):
    """Custom type ipOspfVirtIntfInfoStatus based on Integer32"""
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


_IpOspfVirtIntfInfoStatus_Type.__name__ = "Integer32"
_IpOspfVirtIntfInfoStatus_Object = MibTableColumn
ipOspfVirtIntfInfoStatus = _IpOspfVirtIntfInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 9, 1, 10),
    _IpOspfVirtIntfInfoStatus_Type()
)
ipOspfVirtIntfInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfVirtIntfInfoStatus.setStatus("current")
_IpOspfHostInfoTable_Object = MibTable
ipOspfHostInfoTable = _IpOspfHostInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 10)
)
if mibBuilder.loadTexts:
    ipOspfHostInfoTable.setStatus("current")
_IpOspfHostInfoEntry_Object = MibTableRow
ipOspfHostInfoEntry = _IpOspfHostInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 10, 1)
)
ipOspfHostInfoEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipOspfHostInfoIndex"),
    (0, "BLADETYPE2-NETWORK-MIB", "ipOspfHostInfoIpAddr"),
)
if mibBuilder.loadTexts:
    ipOspfHostInfoEntry.setStatus("current")
_IpOspfHostInfoIndex_Type = Integer32
_IpOspfHostInfoIndex_Object = MibTableColumn
ipOspfHostInfoIndex = _IpOspfHostInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 10, 1, 1),
    _IpOspfHostInfoIndex_Type()
)
ipOspfHostInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfHostInfoIndex.setStatus("current")
_IpOspfHostInfoIpAddr_Type = IpAddress
_IpOspfHostInfoIpAddr_Object = MibTableColumn
ipOspfHostInfoIpAddr = _IpOspfHostInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 10, 1, 2),
    _IpOspfHostInfoIpAddr_Type()
)
ipOspfHostInfoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfHostInfoIpAddr.setStatus("current")
_IpOspfHostInfoAreaIndex_Type = Integer32
_IpOspfHostInfoAreaIndex_Object = MibTableColumn
ipOspfHostInfoAreaIndex = _IpOspfHostInfoAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 10, 1, 3),
    _IpOspfHostInfoAreaIndex_Type()
)
ipOspfHostInfoAreaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfHostInfoAreaIndex.setStatus("current")
_IpOspfHostInfoCost_Type = Integer32
_IpOspfHostInfoCost_Object = MibTableColumn
ipOspfHostInfoCost = _IpOspfHostInfoCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 10, 1, 4),
    _IpOspfHostInfoCost_Type()
)
ipOspfHostInfoCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfHostInfoCost.setStatus("current")


class _IpOspfHostInfoState_Type(Integer32):
    """Custom type ipOspfHostInfoState based on Integer32"""
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


_IpOspfHostInfoState_Type.__name__ = "Integer32"
_IpOspfHostInfoState_Object = MibTableColumn
ipOspfHostInfoState = _IpOspfHostInfoState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 10, 1, 5),
    _IpOspfHostInfoState_Type()
)
ipOspfHostInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfHostInfoState.setStatus("current")
_IpOspfRedistributeInfo_ObjectIdentity = ObjectIdentity
ipOspfRedistributeInfo = _IpOspfRedistributeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 11)
)
_IpOspfRedistributeStaticInfo_ObjectIdentity = ObjectIdentity
ipOspfRedistributeStaticInfo = _IpOspfRedistributeStaticInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 11, 1)
)


class _IpOspfRedistributeStaticInfoMetric_Type(Integer32):
    """Custom type ipOspfRedistributeStaticInfoMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_IpOspfRedistributeStaticInfoMetric_Type.__name__ = "Integer32"
_IpOspfRedistributeStaticInfoMetric_Object = MibScalar
ipOspfRedistributeStaticInfoMetric = _IpOspfRedistributeStaticInfoMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 11, 1, 1),
    _IpOspfRedistributeStaticInfoMetric_Type()
)
ipOspfRedistributeStaticInfoMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfRedistributeStaticInfoMetric.setStatus("current")


class _IpOspfRedistributeStaticInfoMetricType_Type(Integer32):
    """Custom type ipOspfRedistributeStaticInfoMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("type1", 2),
          ("type2", 3))
    )


_IpOspfRedistributeStaticInfoMetricType_Type.__name__ = "Integer32"
_IpOspfRedistributeStaticInfoMetricType_Object = MibScalar
ipOspfRedistributeStaticInfoMetricType = _IpOspfRedistributeStaticInfoMetricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 11, 1, 2),
    _IpOspfRedistributeStaticInfoMetricType_Type()
)
ipOspfRedistributeStaticInfoMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfRedistributeStaticInfoMetricType.setStatus("current")
_IpOspfRedistributeStaticInfoOutRmapList_Type = OctetString
_IpOspfRedistributeStaticInfoOutRmapList_Object = MibScalar
ipOspfRedistributeStaticInfoOutRmapList = _IpOspfRedistributeStaticInfoOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 11, 1, 3),
    _IpOspfRedistributeStaticInfoOutRmapList_Type()
)
ipOspfRedistributeStaticInfoOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfRedistributeStaticInfoOutRmapList.setStatus("current")
_IpOspfRedistributeFixedInfo_ObjectIdentity = ObjectIdentity
ipOspfRedistributeFixedInfo = _IpOspfRedistributeFixedInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 11, 2)
)


class _IpOspfRedistributeFixedInfoMetric_Type(Integer32):
    """Custom type ipOspfRedistributeFixedInfoMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_IpOspfRedistributeFixedInfoMetric_Type.__name__ = "Integer32"
_IpOspfRedistributeFixedInfoMetric_Object = MibScalar
ipOspfRedistributeFixedInfoMetric = _IpOspfRedistributeFixedInfoMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 11, 2, 1),
    _IpOspfRedistributeFixedInfoMetric_Type()
)
ipOspfRedistributeFixedInfoMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfRedistributeFixedInfoMetric.setStatus("current")


class _IpOspfRedistributeFixedInfoMetricType_Type(Integer32):
    """Custom type ipOspfRedistributeFixedInfoMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("type1", 2),
          ("type2", 3))
    )


_IpOspfRedistributeFixedInfoMetricType_Type.__name__ = "Integer32"
_IpOspfRedistributeFixedInfoMetricType_Object = MibScalar
ipOspfRedistributeFixedInfoMetricType = _IpOspfRedistributeFixedInfoMetricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 11, 2, 2),
    _IpOspfRedistributeFixedInfoMetricType_Type()
)
ipOspfRedistributeFixedInfoMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfRedistributeFixedInfoMetricType.setStatus("current")
_IpOspfRedistributeFixedInfoOutRmapList_Type = OctetString
_IpOspfRedistributeFixedInfoOutRmapList_Object = MibScalar
ipOspfRedistributeFixedInfoOutRmapList = _IpOspfRedistributeFixedInfoOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 11, 2, 3),
    _IpOspfRedistributeFixedInfoOutRmapList_Type()
)
ipOspfRedistributeFixedInfoOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfRedistributeFixedInfoOutRmapList.setStatus("current")
_IpOspfRedistributeRipInfo_ObjectIdentity = ObjectIdentity
ipOspfRedistributeRipInfo = _IpOspfRedistributeRipInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 11, 3)
)


class _IpOspfRedistributeRipInfoMetric_Type(Integer32):
    """Custom type ipOspfRedistributeRipInfoMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_IpOspfRedistributeRipInfoMetric_Type.__name__ = "Integer32"
_IpOspfRedistributeRipInfoMetric_Object = MibScalar
ipOspfRedistributeRipInfoMetric = _IpOspfRedistributeRipInfoMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 11, 3, 1),
    _IpOspfRedistributeRipInfoMetric_Type()
)
ipOspfRedistributeRipInfoMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfRedistributeRipInfoMetric.setStatus("current")


class _IpOspfRedistributeRipInfoMetricType_Type(Integer32):
    """Custom type ipOspfRedistributeRipInfoMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("type1", 2),
          ("type2", 3))
    )


_IpOspfRedistributeRipInfoMetricType_Type.__name__ = "Integer32"
_IpOspfRedistributeRipInfoMetricType_Object = MibScalar
ipOspfRedistributeRipInfoMetricType = _IpOspfRedistributeRipInfoMetricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 11, 3, 2),
    _IpOspfRedistributeRipInfoMetricType_Type()
)
ipOspfRedistributeRipInfoMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfRedistributeRipInfoMetricType.setStatus("current")
_IpOspfRedistributeRipInfoOutRmapList_Type = OctetString
_IpOspfRedistributeRipInfoOutRmapList_Object = MibScalar
ipOspfRedistributeRipInfoOutRmapList = _IpOspfRedistributeRipInfoOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 11, 3, 3),
    _IpOspfRedistributeRipInfoOutRmapList_Type()
)
ipOspfRedistributeRipInfoOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfRedistributeRipInfoOutRmapList.setStatus("current")
_IpOspfMd5keyInfoTable_Object = MibTable
ipOspfMd5keyInfoTable = _IpOspfMd5keyInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 12)
)
if mibBuilder.loadTexts:
    ipOspfMd5keyInfoTable.setStatus("current")
_IpOspfMd5keyInfoEntry_Object = MibTableRow
ipOspfMd5keyInfoEntry = _IpOspfMd5keyInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 12, 1)
)
ipOspfMd5keyInfoEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "ipOspfMd5keyInfoIndex"),
)
if mibBuilder.loadTexts:
    ipOspfMd5keyInfoEntry.setStatus("current")
_IpOspfMd5keyInfoIndex_Type = Integer32
_IpOspfMd5keyInfoIndex_Object = MibTableColumn
ipOspfMd5keyInfoIndex = _IpOspfMd5keyInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 12, 1, 1),
    _IpOspfMd5keyInfoIndex_Type()
)
ipOspfMd5keyInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfMd5keyInfoIndex.setStatus("current")


class _IpOspfMd5keyInfoKey_Type(DisplayString):
    """Custom type ipOspfMd5keyInfoKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_IpOspfMd5keyInfoKey_Type.__name__ = "DisplayString"
_IpOspfMd5keyInfoKey_Object = MibTableColumn
ipOspfMd5keyInfoKey = _IpOspfMd5keyInfoKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 3, 8, 11, 12, 1, 2),
    _IpOspfMd5keyInfoKey_Type()
)
ipOspfMd5keyInfoKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOspfMd5keyInfoKey.setStatus("current")
_Layer3Oper_ObjectIdentity = ObjectIdentity
layer3Oper = _Layer3Oper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 4)
)
_VrrpOper_ObjectIdentity = ObjectIdentity
vrrpOper = _VrrpOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 4, 1)
)
_VrrpOperVirtRtrTable_Object = MibTable
vrrpOperVirtRtrTable = _VrrpOperVirtRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    vrrpOperVirtRtrTable.setStatus("current")
_VrrpOperVirtRtrEntry_Object = MibTableRow
vrrpOperVirtRtrEntry = _VrrpOperVirtRtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 4, 1, 1, 1)
)
vrrpOperVirtRtrEntry.setIndexNames(
    (0, "BLADETYPE2-NETWORK-MIB", "vrrpOperVirtRtrIndex"),
)
if mibBuilder.loadTexts:
    vrrpOperVirtRtrEntry.setStatus("current")
_VrrpOperVirtRtrIndex_Type = Integer32
_VrrpOperVirtRtrIndex_Object = MibTableColumn
vrrpOperVirtRtrIndex = _VrrpOperVirtRtrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 4, 1, 1, 1, 1),
    _VrrpOperVirtRtrIndex_Type()
)
vrrpOperVirtRtrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperVirtRtrIndex.setStatus("current")


class _VrrpOperVirtRtrBackup_Type(Integer32):
    """Custom type vrrpOperVirtRtrBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("ok", 1))
    )


_VrrpOperVirtRtrBackup_Type.__name__ = "Integer32"
_VrrpOperVirtRtrBackup_Object = MibTableColumn
vrrpOperVirtRtrBackup = _VrrpOperVirtRtrBackup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 4, 1, 1, 1, 2),
    _VrrpOperVirtRtrBackup_Type()
)
vrrpOperVirtRtrBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpOperVirtRtrBackup.setStatus("current")


class _VrrpOperVirtRtrGroupBackup_Type(Integer32):
    """Custom type vrrpOperVirtRtrGroupBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("ok", 1))
    )


_VrrpOperVirtRtrGroupBackup_Type.__name__ = "Integer32"
_VrrpOperVirtRtrGroupBackup_Object = MibScalar
vrrpOperVirtRtrGroupBackup = _VrrpOperVirtRtrGroupBackup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 3, 4, 1, 2),
    _VrrpOperVirtRtrGroupBackup_Type()
)
vrrpOperVirtRtrGroupBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpOperVirtRtrGroupBackup.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLADETYPE2-NETWORK-MIB",
    **{"layer3": layer3,
       "layer3Configs": layer3Configs,
       "ipInterfaceCfg": ipInterfaceCfg,
       "ipInterfaceTableMax": ipInterfaceTableMax,
       "ipCurCfgIntfTable": ipCurCfgIntfTable,
       "ipCurCfgIntfEntry": ipCurCfgIntfEntry,
       "ipCurCfgIntfIndex": ipCurCfgIntfIndex,
       "ipCurCfgIntfAddr": ipCurCfgIntfAddr,
       "ipCurCfgIntfMask": ipCurCfgIntfMask,
       "ipCurCfgIntfBroadcast": ipCurCfgIntfBroadcast,
       "ipCurCfgIntfVlan": ipCurCfgIntfVlan,
       "ipCurCfgIntfState": ipCurCfgIntfState,
       "ipCurCfgIntfBootpRelay": ipCurCfgIntfBootpRelay,
       "ipNewCfgIntfTable": ipNewCfgIntfTable,
       "ipNewCfgIntfEntry": ipNewCfgIntfEntry,
       "ipNewCfgIntfIndex": ipNewCfgIntfIndex,
       "ipNewCfgIntfAddr": ipNewCfgIntfAddr,
       "ipNewCfgIntfMask": ipNewCfgIntfMask,
       "ipNewCfgIntfBroadcast": ipNewCfgIntfBroadcast,
       "ipNewCfgIntfVlan": ipNewCfgIntfVlan,
       "ipNewCfgIntfState": ipNewCfgIntfState,
       "ipNewCfgIntfDelete": ipNewCfgIntfDelete,
       "ipNewCfgIntfBootpRelay": ipNewCfgIntfBootpRelay,
       "ipGatewayCfg": ipGatewayCfg,
       "ipGatewayTableMax": ipGatewayTableMax,
       "ipCurCfgGwTable": ipCurCfgGwTable,
       "ipCurCfgGwEntry": ipCurCfgGwEntry,
       "ipCurCfgGwIndex": ipCurCfgGwIndex,
       "ipCurCfgGwAddr": ipCurCfgGwAddr,
       "ipCurCfgGwInterval": ipCurCfgGwInterval,
       "ipCurCfgGwRetry": ipCurCfgGwRetry,
       "ipCurCfgGwState": ipCurCfgGwState,
       "ipCurCfgGwArp": ipCurCfgGwArp,
       "ipNewCfgGwTable": ipNewCfgGwTable,
       "ipNewCfgGwEntry": ipNewCfgGwEntry,
       "ipNewCfgGwIndex": ipNewCfgGwIndex,
       "ipNewCfgGwAddr": ipNewCfgGwAddr,
       "ipNewCfgGwInterval": ipNewCfgGwInterval,
       "ipNewCfgGwRetry": ipNewCfgGwRetry,
       "ipNewCfgGwState": ipNewCfgGwState,
       "ipNewCfgGwDelete": ipNewCfgGwDelete,
       "ipNewCfgGwArp": ipNewCfgGwArp,
       "ipStaticRouteCfg": ipStaticRouteCfg,
       "ipStaticRouteTableMaxSize": ipStaticRouteTableMaxSize,
       "ipCurCfgStaticRouteTable": ipCurCfgStaticRouteTable,
       "ipCurCfgStaticRouteEntry": ipCurCfgStaticRouteEntry,
       "ipCurCfgStaticRouteIndx": ipCurCfgStaticRouteIndx,
       "ipCurCfgStaticRouteDestIp": ipCurCfgStaticRouteDestIp,
       "ipCurCfgStaticRouteMask": ipCurCfgStaticRouteMask,
       "ipCurCfgStaticRouteGateway": ipCurCfgStaticRouteGateway,
       "ipCurCfgStaticRouteInterface": ipCurCfgStaticRouteInterface,
       "ipNewCfgStaticRouteTable": ipNewCfgStaticRouteTable,
       "ipNewCfgStaticRouteEntry": ipNewCfgStaticRouteEntry,
       "ipNewCfgStaticRouteIndx": ipNewCfgStaticRouteIndx,
       "ipNewCfgStaticRouteDestIp": ipNewCfgStaticRouteDestIp,
       "ipNewCfgStaticRouteMask": ipNewCfgStaticRouteMask,
       "ipNewCfgStaticRouteGateway": ipNewCfgStaticRouteGateway,
       "ipNewCfgStaticRouteAction": ipNewCfgStaticRouteAction,
       "ipNewCfgStaticRouteInterface": ipNewCfgStaticRouteInterface,
       "ipForwardCfg": ipForwardCfg,
       "ipFwdGeneralCfg": ipFwdGeneralCfg,
       "ipFwdCurCfgState": ipFwdCurCfgState,
       "ipFwdNewCfgState": ipFwdNewCfgState,
       "ipFwdCurCfgDirectedBcast": ipFwdCurCfgDirectedBcast,
       "ipFwdNewCfgDirectedBcast": ipFwdNewCfgDirectedBcast,
       "ripCfg": ripCfg,
       "ripCurCfgSupply": ripCurCfgSupply,
       "ripNewCfgSupply": ripNewCfgSupply,
       "ripCurCfgListen": ripCurCfgListen,
       "ripNewCfgListen": ripNewCfgListen,
       "ripCurCfgDefListen": ripCurCfgDefListen,
       "ripNewCfgDefListen": ripNewCfgDefListen,
       "ripCurCfgStaticSupply": ripCurCfgStaticSupply,
       "ripNewCfgStaticSupply": ripNewCfgStaticSupply,
       "ripCurCfgUpdatePeriod": ripCurCfgUpdatePeriod,
       "ripNewCfgUpdatePeriod": ripNewCfgUpdatePeriod,
       "ripCurCfgState": ripCurCfgState,
       "ripNewCfgState": ripNewCfgState,
       "ripCurCfgPoisonReverse": ripCurCfgPoisonReverse,
       "ripNewCfgPoisonReverse": ripNewCfgPoisonReverse,
       "ripCurCfgSplitHorizon": ripCurCfgSplitHorizon,
       "ripNewCfgSplitHorizon": ripNewCfgSplitHorizon,
       "vrrpCfg": vrrpCfg,
       "vrrpGeneral": vrrpGeneral,
       "vrrpCurCfgGenState": vrrpCurCfgGenState,
       "vrrpNewCfgGenState": vrrpNewCfgGenState,
       "vrrpCurCfgGenTckVirtRtrInc": vrrpCurCfgGenTckVirtRtrInc,
       "vrrpNewCfgGenTckVirtRtrInc": vrrpNewCfgGenTckVirtRtrInc,
       "vrrpCurCfgGenTckIpIntfInc": vrrpCurCfgGenTckIpIntfInc,
       "vrrpNewCfgGenTckIpIntfInc": vrrpNewCfgGenTckIpIntfInc,
       "vrrpCurCfgGenTckVlanPortInc": vrrpCurCfgGenTckVlanPortInc,
       "vrrpNewCfgGenTckVlanPortInc": vrrpNewCfgGenTckVlanPortInc,
       "vrrpCurCfgGenTckL4PortInc": vrrpCurCfgGenTckL4PortInc,
       "vrrpNewCfgGenTckL4PortInc": vrrpNewCfgGenTckL4PortInc,
       "vrrpCurCfgGenTckRServerInc": vrrpCurCfgGenTckRServerInc,
       "vrrpNewCfgGenTckRServerInc": vrrpNewCfgGenTckRServerInc,
       "vrrpCurCfgGenTckHsrpInc": vrrpCurCfgGenTckHsrpInc,
       "vrrpNewCfgGenTckHsrpInc": vrrpNewCfgGenTckHsrpInc,
       "vrrpCurCfgGenHotstandby": vrrpCurCfgGenHotstandby,
       "vrrpNewCfgGenHotstandby": vrrpNewCfgGenHotstandby,
       "vrrpCurCfgGenTckHsrvInc": vrrpCurCfgGenTckHsrvInc,
       "vrrpNewCfgGenTckHsrvInc": vrrpNewCfgGenTckHsrvInc,
       "vrrpVirtRtrTableMaxSize": vrrpVirtRtrTableMaxSize,
       "vrrpCurCfgVirtRtrTable": vrrpCurCfgVirtRtrTable,
       "vrrpCurCfgVirtRtrTableEntry": vrrpCurCfgVirtRtrTableEntry,
       "vrrpCurCfgVirtRtrIndx": vrrpCurCfgVirtRtrIndx,
       "vrrpCurCfgVirtRtrID": vrrpCurCfgVirtRtrID,
       "vrrpCurCfgVirtRtrAddr": vrrpCurCfgVirtRtrAddr,
       "vrrpCurCfgVirtRtrIfIndex": vrrpCurCfgVirtRtrIfIndex,
       "vrrpCurCfgVirtRtrInterval": vrrpCurCfgVirtRtrInterval,
       "vrrpCurCfgVirtRtrPriority": vrrpCurCfgVirtRtrPriority,
       "vrrpCurCfgVirtRtrPreempt": vrrpCurCfgVirtRtrPreempt,
       "vrrpCurCfgVirtRtrState": vrrpCurCfgVirtRtrState,
       "vrrpCurCfgVirtRtrSharing": vrrpCurCfgVirtRtrSharing,
       "vrrpCurCfgVirtRtrTckVirtRtr": vrrpCurCfgVirtRtrTckVirtRtr,
       "vrrpCurCfgVirtRtrTckIpIntf": vrrpCurCfgVirtRtrTckIpIntf,
       "vrrpCurCfgVirtRtrTckVlanPort": vrrpCurCfgVirtRtrTckVlanPort,
       "vrrpCurCfgVirtRtrTckL4Port": vrrpCurCfgVirtRtrTckL4Port,
       "vrrpCurCfgVirtRtrTckRServer": vrrpCurCfgVirtRtrTckRServer,
       "vrrpCurCfgVirtRtrTckHsrp": vrrpCurCfgVirtRtrTckHsrp,
       "vrrpCurCfgVirtRtrTckHsrv": vrrpCurCfgVirtRtrTckHsrv,
       "vrrpNewCfgVirtRtrTable": vrrpNewCfgVirtRtrTable,
       "vrrpNewCfgVirtRtrTableEntry": vrrpNewCfgVirtRtrTableEntry,
       "vrrpNewCfgVirtRtrIndx": vrrpNewCfgVirtRtrIndx,
       "vrrpNewCfgVirtRtrID": vrrpNewCfgVirtRtrID,
       "vrrpNewCfgVirtRtrAddr": vrrpNewCfgVirtRtrAddr,
       "vrrpNewCfgVirtRtrIfIndex": vrrpNewCfgVirtRtrIfIndex,
       "vrrpNewCfgVirtRtrInterval": vrrpNewCfgVirtRtrInterval,
       "vrrpNewCfgVirtRtrPriority": vrrpNewCfgVirtRtrPriority,
       "vrrpNewCfgVirtRtrPreempt": vrrpNewCfgVirtRtrPreempt,
       "vrrpNewCfgVirtRtrState": vrrpNewCfgVirtRtrState,
       "vrrpNewCfgVirtRtrDelete": vrrpNewCfgVirtRtrDelete,
       "vrrpNewCfgVirtRtrSharing": vrrpNewCfgVirtRtrSharing,
       "vrrpNewCfgVirtRtrTckVirtRtr": vrrpNewCfgVirtRtrTckVirtRtr,
       "vrrpNewCfgVirtRtrTckIpIntf": vrrpNewCfgVirtRtrTckIpIntf,
       "vrrpNewCfgVirtRtrTckVlanPort": vrrpNewCfgVirtRtrTckVlanPort,
       "vrrpNewCfgVirtRtrTckL4Port": vrrpNewCfgVirtRtrTckL4Port,
       "vrrpNewCfgVirtRtrTckRServer": vrrpNewCfgVirtRtrTckRServer,
       "vrrpNewCfgVirtRtrTckHsrp": vrrpNewCfgVirtRtrTckHsrp,
       "vrrpNewCfgVirtRtrTckHsrv": vrrpNewCfgVirtRtrTckHsrv,
       "vrrpIfTableMaxSize": vrrpIfTableMaxSize,
       "vrrpCurCfgIfTable": vrrpCurCfgIfTable,
       "vrrpCurCfgIfTableEntry": vrrpCurCfgIfTableEntry,
       "vrrpCurCfgIfIndx": vrrpCurCfgIfIndx,
       "vrrpCurCfgIfAuthType": vrrpCurCfgIfAuthType,
       "vrrpCurCfgIfPasswd": vrrpCurCfgIfPasswd,
       "vrrpNewCfgIfTable": vrrpNewCfgIfTable,
       "vrrpNewCfgIfTableEntry": vrrpNewCfgIfTableEntry,
       "vrrpNewCfgIfIndx": vrrpNewCfgIfIndx,
       "vrrpNewCfgIfAuthType": vrrpNewCfgIfAuthType,
       "vrrpNewCfgIfPasswd": vrrpNewCfgIfPasswd,
       "vrrpNewCfgIfDelete": vrrpNewCfgIfDelete,
       "vrrpVirtRtrGrpTableMaxSize": vrrpVirtRtrGrpTableMaxSize,
       "vrrpCurCfgVirtRtrGrpTable": vrrpCurCfgVirtRtrGrpTable,
       "vrrpCurCfgVirtRtrGrpTableEntry": vrrpCurCfgVirtRtrGrpTableEntry,
       "vrrpCurCfgVirtRtrGrpIndx": vrrpCurCfgVirtRtrGrpIndx,
       "vrrpCurCfgVirtRtrGrpID": vrrpCurCfgVirtRtrGrpID,
       "vrrpCurCfgVirtRtrGrpIfIndex": vrrpCurCfgVirtRtrGrpIfIndex,
       "vrrpCurCfgVirtRtrGrpInterval": vrrpCurCfgVirtRtrGrpInterval,
       "vrrpCurCfgVirtRtrGrpPriority": vrrpCurCfgVirtRtrGrpPriority,
       "vrrpCurCfgVirtRtrGrpPreempt": vrrpCurCfgVirtRtrGrpPreempt,
       "vrrpCurCfgVirtRtrGrpState": vrrpCurCfgVirtRtrGrpState,
       "vrrpCurCfgVirtRtrGrpSharing": vrrpCurCfgVirtRtrGrpSharing,
       "vrrpCurCfgVirtRtrGrpTckVirtRtr": vrrpCurCfgVirtRtrGrpTckVirtRtr,
       "vrrpCurCfgVirtRtrGrpTckIpIntf": vrrpCurCfgVirtRtrGrpTckIpIntf,
       "vrrpCurCfgVirtRtrGrpTckVlanPort": vrrpCurCfgVirtRtrGrpTckVlanPort,
       "vrrpCurCfgVirtRtrGrpTckL4Port": vrrpCurCfgVirtRtrGrpTckL4Port,
       "vrrpCurCfgVirtRtrGrpTckRServer": vrrpCurCfgVirtRtrGrpTckRServer,
       "vrrpCurCfgVirtRtrGrpTckHsrp": vrrpCurCfgVirtRtrGrpTckHsrp,
       "vrrpCurCfgVirtRtrGrpTckHsrv": vrrpCurCfgVirtRtrGrpTckHsrv,
       "vrrpNewCfgVirtRtrGrpTable": vrrpNewCfgVirtRtrGrpTable,
       "vrrpNewCfgVirtRtrGrpTableEntry": vrrpNewCfgVirtRtrGrpTableEntry,
       "vrrpNewCfgVirtRtrGrpIndx": vrrpNewCfgVirtRtrGrpIndx,
       "vrrpNewCfgVirtRtrGrpID": vrrpNewCfgVirtRtrGrpID,
       "vrrpNewCfgVirtRtrGrpIfIndex": vrrpNewCfgVirtRtrGrpIfIndex,
       "vrrpNewCfgVirtRtrGrpInterval": vrrpNewCfgVirtRtrGrpInterval,
       "vrrpNewCfgVirtRtrGrpPriority": vrrpNewCfgVirtRtrGrpPriority,
       "vrrpNewCfgVirtRtrGrpPreempt": vrrpNewCfgVirtRtrGrpPreempt,
       "vrrpNewCfgVirtRtrGrpState": vrrpNewCfgVirtRtrGrpState,
       "vrrpNewCfgVirtRtrGrpDelete": vrrpNewCfgVirtRtrGrpDelete,
       "vrrpNewCfgVirtRtrGrpSharing": vrrpNewCfgVirtRtrGrpSharing,
       "vrrpNewCfgVirtRtrGrpTckVirtRtr": vrrpNewCfgVirtRtrGrpTckVirtRtr,
       "vrrpNewCfgVirtRtrGrpTckIpIntf": vrrpNewCfgVirtRtrGrpTckIpIntf,
       "vrrpNewCfgVirtRtrGrpTckVlanPort": vrrpNewCfgVirtRtrGrpTckVlanPort,
       "vrrpNewCfgVirtRtrGrpTckL4Port": vrrpNewCfgVirtRtrGrpTckL4Port,
       "vrrpNewCfgVirtRtrGrpTckRServer": vrrpNewCfgVirtRtrGrpTckRServer,
       "vrrpNewCfgVirtRtrGrpTckHsrp": vrrpNewCfgVirtRtrGrpTckHsrp,
       "vrrpNewCfgVirtRtrGrpTckHsrv": vrrpNewCfgVirtRtrGrpTckHsrv,
       "arpCfg": arpCfg,
       "arpCurCfgReARPPeriod": arpCurCfgReARPPeriod,
       "arpNewCfgReARPPeriod": arpNewCfgReARPPeriod,
       "ipStaticArpTableMaxSize": ipStaticArpTableMaxSize,
       "ipCurCfgStaticArpTable": ipCurCfgStaticArpTable,
       "ipCurCfgStaticArpEntry": ipCurCfgStaticArpEntry,
       "ipCurCfgStaticArpIndx": ipCurCfgStaticArpIndx,
       "ipCurCfgStaticArpIp": ipCurCfgStaticArpIp,
       "ipCurCfgStaticArpMAC": ipCurCfgStaticArpMAC,
       "ipCurCfgStaticArpVlan": ipCurCfgStaticArpVlan,
       "ipCurCfgStaticArpPort": ipCurCfgStaticArpPort,
       "ipNewCfgStaticArpTable": ipNewCfgStaticArpTable,
       "ipNewCfgStaticArpEntry": ipNewCfgStaticArpEntry,
       "ipNewCfgStaticArpIndx": ipNewCfgStaticArpIndx,
       "ipNewCfgStaticArpIp": ipNewCfgStaticArpIp,
       "ipNewCfgStaticArpMAC": ipNewCfgStaticArpMAC,
       "ipNewCfgStaticArpVlan": ipNewCfgStaticArpVlan,
       "ipNewCfgStaticArpPort": ipNewCfgStaticArpPort,
       "ipNewCfgStaticArpAction": ipNewCfgStaticArpAction,
       "ipBootpCfg": ipBootpCfg,
       "ipCurCfgBootpAddr": ipCurCfgBootpAddr,
       "ipNewCfgBootpAddr": ipNewCfgBootpAddr,
       "ipCurCfgBootpAddr2": ipCurCfgBootpAddr2,
       "ipNewCfgBootpAddr2": ipNewCfgBootpAddr2,
       "ipCurCfgBootpState": ipCurCfgBootpState,
       "ipNewCfgBootpState": ipNewCfgBootpState,
       "ipCurCfgDhcpOpt82State": ipCurCfgDhcpOpt82State,
       "ipNewCfgDhcpOpt82State": ipNewCfgDhcpOpt82State,
       "dnsCfg": dnsCfg,
       "dnsCurCfgPrimaryIpAddr": dnsCurCfgPrimaryIpAddr,
       "dnsNewCfgPrimaryIpAddr": dnsNewCfgPrimaryIpAddr,
       "dnsCurCfgSecondaryIpAddr": dnsCurCfgSecondaryIpAddr,
       "dnsNewCfgSecondaryIpAddr": dnsNewCfgSecondaryIpAddr,
       "dnsCurCfgDomainName": dnsCurCfgDomainName,
       "dnsNewCfgDomainName": dnsNewCfgDomainName,
       "ipNwfCfg": ipNwfCfg,
       "ipNwfTableMax": ipNwfTableMax,
       "ipCurCfgNwfTable": ipCurCfgNwfTable,
       "ipCurCfgNwfEntry": ipCurCfgNwfEntry,
       "ipCurCfgNwfIndex": ipCurCfgNwfIndex,
       "ipCurCfgNwfAddr": ipCurCfgNwfAddr,
       "ipCurCfgNwfMask": ipCurCfgNwfMask,
       "ipCurCfgNwfState": ipCurCfgNwfState,
       "ipNewCfgNwfTable": ipNewCfgNwfTable,
       "ipNewCfgNwfEntry": ipNewCfgNwfEntry,
       "ipNewCfgNwfIndex": ipNewCfgNwfIndex,
       "ipNewCfgNwfAddr": ipNewCfgNwfAddr,
       "ipNewCfgNwfMask": ipNewCfgNwfMask,
       "ipNewCfgNwfState": ipNewCfgNwfState,
       "ipNewCfgNwfDelete": ipNewCfgNwfDelete,
       "ipRmapCfg": ipRmapCfg,
       "ipRmapTableMax": ipRmapTableMax,
       "ipCurCfgRmapTable": ipCurCfgRmapTable,
       "ipCurCfgRmapEntry": ipCurCfgRmapEntry,
       "ipCurCfgRmapIndex": ipCurCfgRmapIndex,
       "ipCurCfgRmapLp": ipCurCfgRmapLp,
       "ipCurCfgRmapMetric": ipCurCfgRmapMetric,
       "ipCurCfgRmapPrec": ipCurCfgRmapPrec,
       "ipCurCfgRmapWeight": ipCurCfgRmapWeight,
       "ipCurCfgRmapState": ipCurCfgRmapState,
       "ipCurCfgRmapAp": ipCurCfgRmapAp,
       "ipCurCfgRmapMetricType": ipCurCfgRmapMetricType,
       "ipNewCfgRmapTable": ipNewCfgRmapTable,
       "ipNewCfgRmapEntry": ipNewCfgRmapEntry,
       "ipNewCfgRmapIndex": ipNewCfgRmapIndex,
       "ipNewCfgRmapLp": ipNewCfgRmapLp,
       "ipNewCfgRmapMetric": ipNewCfgRmapMetric,
       "ipNewCfgRmapPrec": ipNewCfgRmapPrec,
       "ipNewCfgRmapWeight": ipNewCfgRmapWeight,
       "ipNewCfgRmapState": ipNewCfgRmapState,
       "ipNewCfgRmapAp": ipNewCfgRmapAp,
       "ipNewCfgRmapMetricType": ipNewCfgRmapMetricType,
       "ipNewCfgRmapDelete": ipNewCfgRmapDelete,
       "ipAlistTableMax": ipAlistTableMax,
       "ipCurCfgAlistTable": ipCurCfgAlistTable,
       "ipCurCfgAlistEntry": ipCurCfgAlistEntry,
       "ipCurCfgAlistRmapIndex": ipCurCfgAlistRmapIndex,
       "ipCurCfgAlistIndex": ipCurCfgAlistIndex,
       "ipCurCfgAlistNwf": ipCurCfgAlistNwf,
       "ipCurCfgAlistMetric": ipCurCfgAlistMetric,
       "ipCurCfgAlistAction": ipCurCfgAlistAction,
       "ipCurCfgAlistState": ipCurCfgAlistState,
       "ipNewCfgAlistTable": ipNewCfgAlistTable,
       "ipNewCfgAlistEntry": ipNewCfgAlistEntry,
       "ipNewCfgAlistRmapIndex": ipNewCfgAlistRmapIndex,
       "ipNewCfgAlistIndex": ipNewCfgAlistIndex,
       "ipNewCfgAlistNwf": ipNewCfgAlistNwf,
       "ipNewCfgAlistMetric": ipNewCfgAlistMetric,
       "ipNewCfgAlistAction": ipNewCfgAlistAction,
       "ipNewCfgAlistState": ipNewCfgAlistState,
       "ipNewCfgAlistDelete": ipNewCfgAlistDelete,
       "ipAspathTableMax": ipAspathTableMax,
       "ipCurCfgAspathTable": ipCurCfgAspathTable,
       "ipCurCfgAspathEntry": ipCurCfgAspathEntry,
       "ipCurCfgAspathRmapIndex": ipCurCfgAspathRmapIndex,
       "ipCurCfgAspathIndex": ipCurCfgAspathIndex,
       "ipCurCfgAspathAS": ipCurCfgAspathAS,
       "ipCurCfgAspathAction": ipCurCfgAspathAction,
       "ipCurCfgAspathState": ipCurCfgAspathState,
       "ipNewCfgAspathTable": ipNewCfgAspathTable,
       "ipNewCfgAspathEntry": ipNewCfgAspathEntry,
       "ipNewCfgAspathRmapIndex": ipNewCfgAspathRmapIndex,
       "ipNewCfgAspathIndex": ipNewCfgAspathIndex,
       "ipNewCfgAspathAS": ipNewCfgAspathAS,
       "ipNewCfgAspathAction": ipNewCfgAspathAction,
       "ipNewCfgAspathState": ipNewCfgAspathState,
       "ipNewCfgAspathDelete": ipNewCfgAspathDelete,
       "ospfCfg": ospfCfg,
       "ospfGeneral": ospfGeneral,
       "ospfCurCfgDefaultRouteMetric": ospfCurCfgDefaultRouteMetric,
       "ospfNewCfgDefaultRouteMetric": ospfNewCfgDefaultRouteMetric,
       "ospfCurCfgDefaultRouteMetricType": ospfCurCfgDefaultRouteMetricType,
       "ospfNewCfgDefaultRouteMetricType": ospfNewCfgDefaultRouteMetricType,
       "ospfIntfTableMaxSize": ospfIntfTableMaxSize,
       "ospfAreaTableMaxSize": ospfAreaTableMaxSize,
       "ospfRangeTableMaxSize": ospfRangeTableMaxSize,
       "ospfVirtIntfTableMaxSize": ospfVirtIntfTableMaxSize,
       "ospfHostTableMaxSize": ospfHostTableMaxSize,
       "ospfCurCfgState": ospfCurCfgState,
       "ospfNewCfgState": ospfNewCfgState,
       "ospfCurCfgAreaTable": ospfCurCfgAreaTable,
       "ospfCurCfgAreaEntry": ospfCurCfgAreaEntry,
       "ospfCurCfgAreaIndex": ospfCurCfgAreaIndex,
       "ospfCurCfgAreaId": ospfCurCfgAreaId,
       "ospfCurCfgAreaSpfInterval": ospfCurCfgAreaSpfInterval,
       "ospfCurCfgAreaAuthType": ospfCurCfgAreaAuthType,
       "ospfCurCfgAreaType": ospfCurCfgAreaType,
       "ospfCurCfgAreaMetric": ospfCurCfgAreaMetric,
       "ospfCurCfgAreaStatus": ospfCurCfgAreaStatus,
       "ospfNewCfgAreaTable": ospfNewCfgAreaTable,
       "ospfNewCfgAreaEntry": ospfNewCfgAreaEntry,
       "ospfNewCfgAreaIndex": ospfNewCfgAreaIndex,
       "ospfNewCfgAreaId": ospfNewCfgAreaId,
       "ospfNewCfgAreaSpfInterval": ospfNewCfgAreaSpfInterval,
       "ospfNewCfgAreaAuthType": ospfNewCfgAreaAuthType,
       "ospfNewCfgAreaType": ospfNewCfgAreaType,
       "ospfNewCfgAreaMetric": ospfNewCfgAreaMetric,
       "ospfNewCfgAreaStatus": ospfNewCfgAreaStatus,
       "ospfNewCfgAreaDelete": ospfNewCfgAreaDelete,
       "ospfRouteRedistribution": ospfRouteRedistribution,
       "ospfRedistributeStatic": ospfRedistributeStatic,
       "ospfCurCfgStaticMetric": ospfCurCfgStaticMetric,
       "ospfNewCfgStaticMetric": ospfNewCfgStaticMetric,
       "ospfCurCfgStaticMetricType": ospfCurCfgStaticMetricType,
       "ospfNewCfgStaticMetricType": ospfNewCfgStaticMetricType,
       "ospfCurCfgStaticOutRmapList": ospfCurCfgStaticOutRmapList,
       "ospfNewCfgStaticOutRmapList": ospfNewCfgStaticOutRmapList,
       "ospfNewCfgStaticAddOutRmap": ospfNewCfgStaticAddOutRmap,
       "ospfNewCfgStaticRemoveOutRmap": ospfNewCfgStaticRemoveOutRmap,
       "ospfRedistributeFixed": ospfRedistributeFixed,
       "ospfCurCfgFixedMetric": ospfCurCfgFixedMetric,
       "ospfNewCfgFixedMetric": ospfNewCfgFixedMetric,
       "ospfCurCfgFixedMetricType": ospfCurCfgFixedMetricType,
       "ospfNewCfgFixedMetricType": ospfNewCfgFixedMetricType,
       "ospfCurCfgFixedOutRmapList": ospfCurCfgFixedOutRmapList,
       "ospfNewCfgFixedOutRmapList": ospfNewCfgFixedOutRmapList,
       "ospfNewCfgFixedAddOutRmap": ospfNewCfgFixedAddOutRmap,
       "ospfNewCfgFixedRemoveOutRmap": ospfNewCfgFixedRemoveOutRmap,
       "ospfRedistributeRip": ospfRedistributeRip,
       "ospfCurCfgRipMetric": ospfCurCfgRipMetric,
       "ospfNewCfgRipMetric": ospfNewCfgRipMetric,
       "ospfCurCfgRipMetricType": ospfCurCfgRipMetricType,
       "ospfNewCfgRipMetricType": ospfNewCfgRipMetricType,
       "ospfCurCfgRipOutRmapList": ospfCurCfgRipOutRmapList,
       "ospfNewCfgRipOutRmapList": ospfNewCfgRipOutRmapList,
       "ospfNewCfgRipAddOutRmap": ospfNewCfgRipAddOutRmap,
       "ospfNewCfgRipRemoveOutRmap": ospfNewCfgRipRemoveOutRmap,
       "ospfCurCfgMdkeyTable": ospfCurCfgMdkeyTable,
       "ospfCurCfgMdkeyEntry": ospfCurCfgMdkeyEntry,
       "ospfCurCfgMdkeyIndex": ospfCurCfgMdkeyIndex,
       "ospfCurCfgMdkeyKey": ospfCurCfgMdkeyKey,
       "ospfNewCfgMdkeyTable": ospfNewCfgMdkeyTable,
       "ospfNewCfgMdkeyEntry": ospfNewCfgMdkeyEntry,
       "ospfNewCfgMdkeyIndex": ospfNewCfgMdkeyIndex,
       "ospfNewCfgMdkeyKey": ospfNewCfgMdkeyKey,
       "ospfNewCfgMdkeyDelete": ospfNewCfgMdkeyDelete,
       "ospfCurCfgIntfTable": ospfCurCfgIntfTable,
       "ospfCurCfgIntfEntry": ospfCurCfgIntfEntry,
       "ospfCurCfgIntfIndex": ospfCurCfgIntfIndex,
       "ospfCurCfgIntfId": ospfCurCfgIntfId,
       "ospfCurCfgIntfArea": ospfCurCfgIntfArea,
       "ospfCurCfgIntfMdkey": ospfCurCfgIntfMdkey,
       "ospfCurCfgIntfCost": ospfCurCfgIntfCost,
       "ospfCurCfgIntfPrio": ospfCurCfgIntfPrio,
       "ospfCurCfgIntfHello": ospfCurCfgIntfHello,
       "ospfCurCfgIntfDead": ospfCurCfgIntfDead,
       "ospfCurCfgIntfTrans": ospfCurCfgIntfTrans,
       "ospfCurCfgIntfRetra": ospfCurCfgIntfRetra,
       "ospfCurCfgIntfAuthKey": ospfCurCfgIntfAuthKey,
       "ospfCurCfgIntfStatus": ospfCurCfgIntfStatus,
       "ospfNewCfgIntfTable": ospfNewCfgIntfTable,
       "ospfNewCfgIntfEntry": ospfNewCfgIntfEntry,
       "ospfNewCfgIntfIndex": ospfNewCfgIntfIndex,
       "ospfNewCfgIntfId": ospfNewCfgIntfId,
       "ospfNewCfgIntfArea": ospfNewCfgIntfArea,
       "ospfNewCfgIntfMdkey": ospfNewCfgIntfMdkey,
       "ospfNewCfgIntfCost": ospfNewCfgIntfCost,
       "ospfNewCfgIntfPrio": ospfNewCfgIntfPrio,
       "ospfNewCfgIntfHello": ospfNewCfgIntfHello,
       "ospfNewCfgIntfDead": ospfNewCfgIntfDead,
       "ospfNewCfgIntfTrans": ospfNewCfgIntfTrans,
       "ospfNewCfgIntfRetra": ospfNewCfgIntfRetra,
       "ospfNewCfgIntfAuthKey": ospfNewCfgIntfAuthKey,
       "ospfNewCfgIntfStatus": ospfNewCfgIntfStatus,
       "ospfNewCfgIntfDelete": ospfNewCfgIntfDelete,
       "ospfCurCfgVirtIntfTable": ospfCurCfgVirtIntfTable,
       "ospfCurCfgVirtIntfEntry": ospfCurCfgVirtIntfEntry,
       "ospfCurCfgVirtIntfIndex": ospfCurCfgVirtIntfIndex,
       "ospfCurCfgVirtIntfAreaId": ospfCurCfgVirtIntfAreaId,
       "ospfCurCfgVirtIntfNbr": ospfCurCfgVirtIntfNbr,
       "ospfCurCfgVirtIntfMdkey": ospfCurCfgVirtIntfMdkey,
       "ospfCurCfgVirtIntfHello": ospfCurCfgVirtIntfHello,
       "ospfCurCfgVirtIntfDead": ospfCurCfgVirtIntfDead,
       "ospfCurCfgVirtIntfTrans": ospfCurCfgVirtIntfTrans,
       "ospfCurCfgVirtIntfRetra": ospfCurCfgVirtIntfRetra,
       "ospfCurCfgVirtIntfAuthKey": ospfCurCfgVirtIntfAuthKey,
       "ospfCurCfgVirtIntfStatus": ospfCurCfgVirtIntfStatus,
       "ospfNewCfgVirtIntfTable": ospfNewCfgVirtIntfTable,
       "ospfNewCfgVirtIntfEntry": ospfNewCfgVirtIntfEntry,
       "ospfNewCfgVirtIntfIndex": ospfNewCfgVirtIntfIndex,
       "ospfNewCfgVirtIntfAreaId": ospfNewCfgVirtIntfAreaId,
       "ospfNewCfgVirtIntfNbr": ospfNewCfgVirtIntfNbr,
       "ospfNewCfgVirtIntfMdkey": ospfNewCfgVirtIntfMdkey,
       "ospfNewCfgVirtIntfHello": ospfNewCfgVirtIntfHello,
       "ospfNewCfgVirtIntfDead": ospfNewCfgVirtIntfDead,
       "ospfNewCfgVirtIntfTrans": ospfNewCfgVirtIntfTrans,
       "ospfNewCfgVirtIntfRetra": ospfNewCfgVirtIntfRetra,
       "ospfNewCfgVirtIntfAuthKey": ospfNewCfgVirtIntfAuthKey,
       "ospfNewCfgVirtIntfStatus": ospfNewCfgVirtIntfStatus,
       "ospfNewCfgVirtIntfDelete": ospfNewCfgVirtIntfDelete,
       "ospfMdkeyTableMaxSize": ospfMdkeyTableMaxSize,
       "ospfCurCfgHostTable": ospfCurCfgHostTable,
       "ospfCurCfgHostEntry": ospfCurCfgHostEntry,
       "ospfCurCfgHostIndex": ospfCurCfgHostIndex,
       "ospfCurCfgHostIpAddr": ospfCurCfgHostIpAddr,
       "ospfCurCfgHostAreaIndex": ospfCurCfgHostAreaIndex,
       "ospfCurCfgHostCost": ospfCurCfgHostCost,
       "ospfCurCfgHostState": ospfCurCfgHostState,
       "ospfNewCfgHostTable": ospfNewCfgHostTable,
       "ospfNewCfgHostEntry": ospfNewCfgHostEntry,
       "ospfNewCfgHostIndex": ospfNewCfgHostIndex,
       "ospfNewCfgHostIpAddr": ospfNewCfgHostIpAddr,
       "ospfNewCfgHostAreaIndex": ospfNewCfgHostAreaIndex,
       "ospfNewCfgHostCost": ospfNewCfgHostCost,
       "ospfNewCfgHostState": ospfNewCfgHostState,
       "ospfNewCfgHostDelete": ospfNewCfgHostDelete,
       "ospfCurCfgRangeTable": ospfCurCfgRangeTable,
       "ospfCurCfgRangeEntry": ospfCurCfgRangeEntry,
       "ospfCurCfgRangeIndex": ospfCurCfgRangeIndex,
       "ospfCurCfgRangeAddr": ospfCurCfgRangeAddr,
       "ospfCurCfgRangeMask": ospfCurCfgRangeMask,
       "ospfCurCfgRangeAreaIndex": ospfCurCfgRangeAreaIndex,
       "ospfCurCfgRangeHideState": ospfCurCfgRangeHideState,
       "ospfCurCfgRangeState": ospfCurCfgRangeState,
       "ospfNewCfgRangeTable": ospfNewCfgRangeTable,
       "ospfNewCfgRangeEntry": ospfNewCfgRangeEntry,
       "ospfNewCfgRangeIndex": ospfNewCfgRangeIndex,
       "ospfNewCfgRangeAddr": ospfNewCfgRangeAddr,
       "ospfNewCfgRangeMask": ospfNewCfgRangeMask,
       "ospfNewCfgRangeAreaIndex": ospfNewCfgRangeAreaIndex,
       "ospfNewCfgRangeHideState": ospfNewCfgRangeHideState,
       "ospfNewCfgRangeState": ospfNewCfgRangeState,
       "ospfNewCfgRangeDelete": ospfNewCfgRangeDelete,
       "ipGeneralCfg": ipGeneralCfg,
       "ipCurCfgRouterID": ipCurCfgRouterID,
       "ipNewCfgRouterID": ipNewCfgRouterID,
       "igmpCfg": igmpCfg,
       "igmpCurCfgOnOff": igmpCurCfgOnOff,
       "igmpNewCfgOnOff": igmpNewCfgOnOff,
       "igmpSnoopCfgGen": igmpSnoopCfgGen,
       "igmpSnoopCfg": igmpSnoopCfg,
       "igmpSnoopCurCfgTimeout": igmpSnoopCurCfgTimeout,
       "igmpSnoopNewCfgTimeout": igmpSnoopNewCfgTimeout,
       "igmpSnoopCurCfgMrto": igmpSnoopCurCfgMrto,
       "igmpSnoopNewCfgMrto": igmpSnoopNewCfgMrto,
       "igmpSnoopNewCfgVlanFastlvAdd": igmpSnoopNewCfgVlanFastlvAdd,
       "igmpSnoopNewCfgVlanFastlvRem": igmpSnoopNewCfgVlanFastlvRem,
       "igmpSnoopCurCfgVlanFastlvBmap": igmpSnoopCurCfgVlanFastlvBmap,
       "igmpSnoopNewCfgVlanFastlvBmap": igmpSnoopNewCfgVlanFastlvBmap,
       "igmpSnoopCurCfgRobust": igmpSnoopCurCfgRobust,
       "igmpSnoopNewCfgRobust": igmpSnoopNewCfgRobust,
       "igmpSnoopNewCfgVlanAdd": igmpSnoopNewCfgVlanAdd,
       "igmpSnoopNewCfgVlanRem": igmpSnoopNewCfgVlanRem,
       "igmpSnoopNewCfgVlanClear": igmpSnoopNewCfgVlanClear,
       "igmpSnoopCurCfgVlanBmap": igmpSnoopCurCfgVlanBmap,
       "igmpSnoopNewCfgVlanBmap": igmpSnoopNewCfgVlanBmap,
       "igmpSnoopCurCfgQInterval": igmpSnoopCurCfgQInterval,
       "igmpSnoopNewCfgQInterval": igmpSnoopNewCfgQInterval,
       "igmpSnoopCurCfgSrcIp": igmpSnoopCurCfgSrcIp,
       "igmpSnoopNewCfgSrcIp": igmpSnoopNewCfgSrcIp,
       "igmpSnoopCurCfgAggrEnaDis": igmpSnoopCurCfgAggrEnaDis,
       "igmpSnoopNewCfgAggrEnaDis": igmpSnoopNewCfgAggrEnaDis,
       "igmpStaticMrtrCfg": igmpStaticMrtrCfg,
       "igmpStaticMrtrCurCfgTable": igmpStaticMrtrCurCfgTable,
       "igmpStaticMrtrCurCfgTableEntry": igmpStaticMrtrCurCfgTableEntry,
       "igmpStaticMrtrCurCfgIndx": igmpStaticMrtrCurCfgIndx,
       "igmpStaticMrtrCurCfgPortId": igmpStaticMrtrCurCfgPortId,
       "igmpStaticMrtrCurCfgVlanId": igmpStaticMrtrCurCfgVlanId,
       "igmpStaticMrtrCurCfgVersion": igmpStaticMrtrCurCfgVersion,
       "igmpStaticMrtrNewCfgTable": igmpStaticMrtrNewCfgTable,
       "igmpStaticMrtrNewCfgTableEntry": igmpStaticMrtrNewCfgTableEntry,
       "igmpStaticMrtrNewCfgIndx": igmpStaticMrtrNewCfgIndx,
       "igmpStaticMrtrNewCfgPortId": igmpStaticMrtrNewCfgPortId,
       "igmpStaticMrtrNewCfgVlanId": igmpStaticMrtrNewCfgVlanId,
       "igmpStaticMrtrNewCfgVersion": igmpStaticMrtrNewCfgVersion,
       "igmpStaticMrtrNewCfgDelete": igmpStaticMrtrNewCfgDelete,
       "igmpFilterCfg": igmpFilterCfg,
       "igmpFltCurCfgTable": igmpFltCurCfgTable,
       "igmpFltCurCfgTableEntry": igmpFltCurCfgTableEntry,
       "igmpFltCurCfgIndx": igmpFltCurCfgIndx,
       "igmpFltCurCfgMcastIp1": igmpFltCurCfgMcastIp1,
       "igmpFltCurCfgMcastIp2": igmpFltCurCfgMcastIp2,
       "igmpFltCurCfgAction": igmpFltCurCfgAction,
       "igmpFltCurCfgState": igmpFltCurCfgState,
       "igmpFltNewCfgTable": igmpFltNewCfgTable,
       "igmpFltNewCfgTableEntry": igmpFltNewCfgTableEntry,
       "igmpFltNewCfgIndx": igmpFltNewCfgIndx,
       "igmpFltNewCfgMcastIp1": igmpFltNewCfgMcastIp1,
       "igmpFltNewCfgMcastIp2": igmpFltNewCfgMcastIp2,
       "igmpFltNewCfgAction": igmpFltNewCfgAction,
       "igmpFltNewCfgState": igmpFltNewCfgState,
       "igmpFltNewCfgDelete": igmpFltNewCfgDelete,
       "igmpFltCurCfgPortTable": igmpFltCurCfgPortTable,
       "igmpFltCurCfgPortTableEntry": igmpFltCurCfgPortTableEntry,
       "igmpFltCurCfgPortIndx": igmpFltCurCfgPortIndx,
       "igmpFltCurCfgPortState": igmpFltCurCfgPortState,
       "igmpFltCurCfgPortFiltBmap": igmpFltCurCfgPortFiltBmap,
       "igmpFltNewCfgPortTable": igmpFltNewCfgPortTable,
       "igmpFltNewCfgPortTableEntry": igmpFltNewCfgPortTableEntry,
       "igmpFltNewCfgPortIndx": igmpFltNewCfgPortIndx,
       "igmpFltNewCfgPortState": igmpFltNewCfgPortState,
       "igmpFltNewCfgPortFiltBmap": igmpFltNewCfgPortFiltBmap,
       "igmpFltNewCfgPortAddFiltRule": igmpFltNewCfgPortAddFiltRule,
       "igmpFltNewCfgPortRemFiltRule": igmpFltNewCfgPortRemFiltRule,
       "igmpFltCurCfgEnaDis": igmpFltCurCfgEnaDis,
       "igmpFltNewCfgEnaDis": igmpFltNewCfgEnaDis,
       "rip2Cfg": rip2Cfg,
       "ripCurCfgIntfTable": ripCurCfgIntfTable,
       "ripCurCfgIntfEntry": ripCurCfgIntfEntry,
       "ripCurCfgIntfIndex": ripCurCfgIntfIndex,
       "ripCurCfgIntfVersion": ripCurCfgIntfVersion,
       "ripCurCfgIntfSupply": ripCurCfgIntfSupply,
       "ripCurCfgIntfListen": ripCurCfgIntfListen,
       "ripCurCfgIntfDefault": ripCurCfgIntfDefault,
       "ripCurCfgIntfTrigUpdate": ripCurCfgIntfTrigUpdate,
       "ripCurCfgIntfMcastUpdate": ripCurCfgIntfMcastUpdate,
       "ripCurCfgIntfPoisonReverse": ripCurCfgIntfPoisonReverse,
       "ripCurCfgIntfState": ripCurCfgIntfState,
       "ripCurCfgIntfMetric": ripCurCfgIntfMetric,
       "ripCurCfgIntfAuth": ripCurCfgIntfAuth,
       "ripCurCfgIntfKey": ripCurCfgIntfKey,
       "ripCurCfgIntfSplitHorizon": ripCurCfgIntfSplitHorizon,
       "ripNewCfgIntfTable": ripNewCfgIntfTable,
       "ripNewCfgIntfEntry": ripNewCfgIntfEntry,
       "ripNewCfgIntfIndex": ripNewCfgIntfIndex,
       "ripNewCfgIntfVersion": ripNewCfgIntfVersion,
       "ripNewCfgIntfSupply": ripNewCfgIntfSupply,
       "ripNewCfgIntfListen": ripNewCfgIntfListen,
       "ripNewCfgIntfDefault": ripNewCfgIntfDefault,
       "ripNewCfgIntfTrigUpdate": ripNewCfgIntfTrigUpdate,
       "ripNewCfgIntfMcastUpdate": ripNewCfgIntfMcastUpdate,
       "ripNewCfgIntfPoisonReverse": ripNewCfgIntfPoisonReverse,
       "ripNewCfgIntfState": ripNewCfgIntfState,
       "ripNewCfgIntfMetric": ripNewCfgIntfMetric,
       "ripNewCfgIntfAuth": ripNewCfgIntfAuth,
       "ripNewCfgIntfKey": ripNewCfgIntfKey,
       "ripNewCfgIntfSplitHorizon": ripNewCfgIntfSplitHorizon,
       "ripGeneral": ripGeneral,
       "rip2CurCfgState": rip2CurCfgState,
       "rip2NewCfgState": rip2NewCfgState,
       "rip2CurCfgUpdatePeriod": rip2CurCfgUpdatePeriod,
       "rip2NewCfgUpdatePeriod": rip2NewCfgUpdatePeriod,
       "ripRouteRedistribution": ripRouteRedistribution,
       "ripRedistributeStatic": ripRedistributeStatic,
       "ripCurCfgStaticMetric": ripCurCfgStaticMetric,
       "ripNewCfgStaticMetric": ripNewCfgStaticMetric,
       "ripCurCfgStaticOutRmapList": ripCurCfgStaticOutRmapList,
       "ripNewCfgStaticOutRmapList": ripNewCfgStaticOutRmapList,
       "ripNewCfgStaticAddOutRmap": ripNewCfgStaticAddOutRmap,
       "ripNewCfgStaticRemoveOutRmap": ripNewCfgStaticRemoveOutRmap,
       "ripRedistributeFixed": ripRedistributeFixed,
       "ripCurCfgFixedMetric": ripCurCfgFixedMetric,
       "ripNewCfgFixedMetric": ripNewCfgFixedMetric,
       "ripCurCfgFixedOutRmapList": ripCurCfgFixedOutRmapList,
       "ripNewCfgFixedOutRmapList": ripNewCfgFixedOutRmapList,
       "ripNewCfgFixedAddOutRmap": ripNewCfgFixedAddOutRmap,
       "ripNewCfgFixedRemoveOutRmap": ripNewCfgFixedRemoveOutRmap,
       "ripRedistributeOspf": ripRedistributeOspf,
       "ripCurCfgOspfMetric": ripCurCfgOspfMetric,
       "ripNewCfgOspfMetric": ripNewCfgOspfMetric,
       "ripCurCfgOspfOutRmapList": ripCurCfgOspfOutRmapList,
       "ripNewCfgOspfOutRmapList": ripNewCfgOspfOutRmapList,
       "ripNewCfgOspfAddOutRmap": ripNewCfgOspfAddOutRmap,
       "ripNewCfgOspfRemoveOutRmap": ripNewCfgOspfRemoveOutRmap,
       "ripRedistributeEospf": ripRedistributeEospf,
       "ripCurCfgEospfMetric": ripCurCfgEospfMetric,
       "ripNewCfgEospfMetric": ripNewCfgEospfMetric,
       "ripCurCfgEospfOutRmapList": ripCurCfgEospfOutRmapList,
       "ripNewCfgEospfOutRmapList": ripNewCfgEospfOutRmapList,
       "ripNewCfgEospfAddOutRmap": ripNewCfgEospfAddOutRmap,
       "ripNewCfgEospfRemoveOutRmap": ripNewCfgEospfRemoveOutRmap,
       "layer3Stats": layer3Stats,
       "ripStats": ripStats,
       "ripStatInPkts": ripStatInPkts,
       "ripStatOutPkts": ripStatOutPkts,
       "ripStatInErrorPkts": ripStatInErrorPkts,
       "ripStatRoutesAgedOut": ripStatRoutesAgedOut,
       "arpStats": arpStats,
       "arpStatEntries": arpStatEntries,
       "arpStatHighWater": arpStatHighWater,
       "arpStatMaxEntries": arpStatMaxEntries,
       "routeStats": routeStats,
       "routeStatEntries": routeStatEntries,
       "routeStatHighWater": routeStatHighWater,
       "routeStatMaxEntries": routeStatMaxEntries,
       "vrrpStats": vrrpStats,
       "vrrpStatInAdvers": vrrpStatInAdvers,
       "vrrpStatOutAdvers": vrrpStatOutAdvers,
       "vrrpStatOutBadAdvers": vrrpStatOutBadAdvers,
       "vrrpStatBadVersion": vrrpStatBadVersion,
       "vrrpStatBadAddress": vrrpStatBadAddress,
       "vrrpStatBadPassword": vrrpStatBadPassword,
       "vrrpStatBadVrid": vrrpStatBadVrid,
       "vrrpStatBadData": vrrpStatBadData,
       "vrrpStatBadInterval": vrrpStatBadInterval,
       "ospfStats": ospfStats,
       "ospfGeneralStats": ospfGeneralStats,
       "ospfCumRxTxStats": ospfCumRxTxStats,
       "ospfCumRxPkts": ospfCumRxPkts,
       "ospfCumTxPkts": ospfCumTxPkts,
       "ospfCumRxHello": ospfCumRxHello,
       "ospfCumTxHello": ospfCumTxHello,
       "ospfCumRxDatabase": ospfCumRxDatabase,
       "ospfCumTxDatabase": ospfCumTxDatabase,
       "ospfCumRxlsReqs": ospfCumRxlsReqs,
       "ospfCumTxlsReqs": ospfCumTxlsReqs,
       "ospfCumRxlsAcks": ospfCumRxlsAcks,
       "ospfCumTxlsAcks": ospfCumTxlsAcks,
       "ospfCumRxlsUpdates": ospfCumRxlsUpdates,
       "ospfCumTxlsUpdates": ospfCumTxlsUpdates,
       "ospfCumNbrChangeStats": ospfCumNbrChangeStats,
       "ospfCumNbrhello": ospfCumNbrhello,
       "ospfCumNbrStart": ospfCumNbrStart,
       "ospfCumNbrAdjointOk": ospfCumNbrAdjointOk,
       "ospfCumNbrNegotiationDone": ospfCumNbrNegotiationDone,
       "ospfCumNbrExchangeDone": ospfCumNbrExchangeDone,
       "ospfCumNbrBadRequests": ospfCumNbrBadRequests,
       "ospfCumNbrBadSequence": ospfCumNbrBadSequence,
       "ospfCumNbrLoadingDone": ospfCumNbrLoadingDone,
       "ospfCumNbrN1way": ospfCumNbrN1way,
       "ospfCumNbrRstAd": ospfCumNbrRstAd,
       "ospfCumNbrDown": ospfCumNbrDown,
       "ospfCumNbrN2way": ospfCumNbrN2way,
       "ospfCumIntfChangeStats": ospfCumIntfChangeStats,
       "ospfCumIntfHello": ospfCumIntfHello,
       "ospfCumIntfDown": ospfCumIntfDown,
       "ospfCumIntfLoop": ospfCumIntfLoop,
       "ospfCumIntfUnloop": ospfCumIntfUnloop,
       "ospfCumIntfWaitTimer": ospfCumIntfWaitTimer,
       "ospfCumIntfBackup": ospfCumIntfBackup,
       "ospfCumIntfNbrChange": ospfCumIntfNbrChange,
       "ospfTimersKickOffStats": ospfTimersKickOffStats,
       "ospfTmrsKckOffHello": ospfTmrsKckOffHello,
       "ospfTmrsKckOffRetransmit": ospfTmrsKckOffRetransmit,
       "ospfTmrsKckOffLsaLock": ospfTmrsKckOffLsaLock,
       "ospfTmrsKckOffLsaAck": ospfTmrsKckOffLsaAck,
       "ospfTmrsKckOffDbage": ospfTmrsKckOffDbage,
       "ospfTmrsKckOffSummary": ospfTmrsKckOffSummary,
       "ospfTmrsKckOffAseExport": ospfTmrsKckOffAseExport,
       "ospfArea": ospfArea,
       "ospfAreaRxTxStats": ospfAreaRxTxStats,
       "ospfAreaRxTxStatsEntry": ospfAreaRxTxStatsEntry,
       "ospfAreaRxTxIndex": ospfAreaRxTxIndex,
       "ospfAreaRxPkts": ospfAreaRxPkts,
       "ospfAreaTxPkts": ospfAreaTxPkts,
       "ospfAreaRxHello": ospfAreaRxHello,
       "ospfAreaTxHello": ospfAreaTxHello,
       "ospfAreaRxDatabase": ospfAreaRxDatabase,
       "ospfAreaTxDatabase": ospfAreaTxDatabase,
       "ospfAreaRxlsReqs": ospfAreaRxlsReqs,
       "ospfAreaTxlsReqs": ospfAreaTxlsReqs,
       "ospfAreaRxlsAcks": ospfAreaRxlsAcks,
       "ospfAreaTxlsAcks": ospfAreaTxlsAcks,
       "ospfAreaRxlsUpdates": ospfAreaRxlsUpdates,
       "ospfAreaTxlsUpdates": ospfAreaTxlsUpdates,
       "ospfAreaNbrChangeStats": ospfAreaNbrChangeStats,
       "ospfAreaNbrChangeStatsEntry": ospfAreaNbrChangeStatsEntry,
       "ospfAreaNbrIndex": ospfAreaNbrIndex,
       "ospfAreaNbrhello": ospfAreaNbrhello,
       "ospfAreaNbrStart": ospfAreaNbrStart,
       "ospfAreaNbrAdjointOk": ospfAreaNbrAdjointOk,
       "ospfAreaNbrNegotiationDone": ospfAreaNbrNegotiationDone,
       "ospfAreaNbrExchangeDone": ospfAreaNbrExchangeDone,
       "ospfAreaNbrBadRequests": ospfAreaNbrBadRequests,
       "ospfAreaNbrBadSequence": ospfAreaNbrBadSequence,
       "ospfAreaNbrLoadingDone": ospfAreaNbrLoadingDone,
       "ospfAreaNbrN1way": ospfAreaNbrN1way,
       "ospfAreaNbrRstAd": ospfAreaNbrRstAd,
       "ospfAreaNbrDown": ospfAreaNbrDown,
       "ospfAreaNbrN2way": ospfAreaNbrN2way,
       "ospfAreaChangeStats": ospfAreaChangeStats,
       "ospfAreaChangeStatsEntry": ospfAreaChangeStatsEntry,
       "ospfAreaIntfIndex": ospfAreaIntfIndex,
       "ospfAreaIntfHello": ospfAreaIntfHello,
       "ospfAreaIntfDown": ospfAreaIntfDown,
       "ospfAreaIntfLoop": ospfAreaIntfLoop,
       "ospfAreaIntfUnloop": ospfAreaIntfUnloop,
       "ospfAreaIntfWaitTimer": ospfAreaIntfWaitTimer,
       "ospfAreaIntfBackup": ospfAreaIntfBackup,
       "ospfAreaIntfNbrChange": ospfAreaIntfNbrChange,
       "ospfAreaErrorStats": ospfAreaErrorStats,
       "ospfAreaErrorStatsEntry": ospfAreaErrorStatsEntry,
       "ospfAreaErrIndex": ospfAreaErrIndex,
       "ospfAreaErrAuthFailure": ospfAreaErrAuthFailure,
       "ospfAreaErrNetmaskMismatch": ospfAreaErrNetmaskMismatch,
       "ospfAreaErrHelloMismatch": ospfAreaErrHelloMismatch,
       "ospfAreaErrDeadMismatch": ospfAreaErrDeadMismatch,
       "ospfAreaErrOptionsMismatch": ospfAreaErrOptionsMismatch,
       "ospfAreaErrUnknownNbr": ospfAreaErrUnknownNbr,
       "ospfInterface": ospfInterface,
       "ospfIntfRxTxStats": ospfIntfRxTxStats,
       "ospfIntfRxTxStatsEntry": ospfIntfRxTxStatsEntry,
       "ospfIntfRxTxIndex": ospfIntfRxTxIndex,
       "ospfIntfRxPkts": ospfIntfRxPkts,
       "ospfIntfTxPkts": ospfIntfTxPkts,
       "ospfIntfRxHello": ospfIntfRxHello,
       "ospfIntfTxHello": ospfIntfTxHello,
       "ospfIntfRxDatabase": ospfIntfRxDatabase,
       "ospfIntfTxDatabase": ospfIntfTxDatabase,
       "ospfIntfRxlsReqs": ospfIntfRxlsReqs,
       "ospfIntfTxlsReqs": ospfIntfTxlsReqs,
       "ospfIntfRxlsAcks": ospfIntfRxlsAcks,
       "ospfIntfTxlsAcks": ospfIntfTxlsAcks,
       "ospfIntfRxlsUpdates": ospfIntfRxlsUpdates,
       "ospfIntfTxlsUpdates": ospfIntfTxlsUpdates,
       "ospfIntfNbrChangeStats": ospfIntfNbrChangeStats,
       "ospfIntfNbrChangeStatsEntry": ospfIntfNbrChangeStatsEntry,
       "ospfIntfNbrIndex": ospfIntfNbrIndex,
       "ospfIntfNbrhello": ospfIntfNbrhello,
       "ospfIntfNbrStart": ospfIntfNbrStart,
       "ospfIntfNbrAdjointOk": ospfIntfNbrAdjointOk,
       "ospfIntfNbrNegotiationDone": ospfIntfNbrNegotiationDone,
       "ospfIntfNbrExchangeDone": ospfIntfNbrExchangeDone,
       "ospfIntfNbrBadRequests": ospfIntfNbrBadRequests,
       "ospfIntfNbrBadSequence": ospfIntfNbrBadSequence,
       "ospfIntfNbrLoadingDone": ospfIntfNbrLoadingDone,
       "ospfIntfNbrN1way": ospfIntfNbrN1way,
       "ospfIntfNbrRstAd": ospfIntfNbrRstAd,
       "ospfIntfNbrDown": ospfIntfNbrDown,
       "ospfIntfNbrN2way": ospfIntfNbrN2way,
       "ospfIntfChangeStats": ospfIntfChangeStats,
       "ospfIntfChangeStatsEntry": ospfIntfChangeStatsEntry,
       "ospfIntfIndex": ospfIntfIndex,
       "ospfIntfHello": ospfIntfHello,
       "ospfIntfDown": ospfIntfDown,
       "ospfIntfLoop": ospfIntfLoop,
       "ospfIntfUnloop": ospfIntfUnloop,
       "ospfIntfWaitTimer": ospfIntfWaitTimer,
       "ospfIntfBackup": ospfIntfBackup,
       "ospfIntfNbrChange": ospfIntfNbrChange,
       "ospfIntfErrorStats": ospfIntfErrorStats,
       "ospfIntfErrorStatsEntry": ospfIntfErrorStatsEntry,
       "ospfIntfErrIndex": ospfIntfErrIndex,
       "ospfIntfErrAuthFailure": ospfIntfErrAuthFailure,
       "ospfIntfErrNetmaskMismatch": ospfIntfErrNetmaskMismatch,
       "ospfIntfErrHelloMismatch": ospfIntfErrHelloMismatch,
       "ospfIntfErrDeadMismatch": ospfIntfErrDeadMismatch,
       "ospfIntfErrOptionsMismatch": ospfIntfErrOptionsMismatch,
       "ospfIntfErrUnknownNbr": ospfIntfErrUnknownNbr,
       "clearStats": clearStats,
       "ipClearStats": ipClearStats,
       "ifStatsTable": ifStatsTable,
       "ifStatsEntry": ifStatsEntry,
       "ifStatsIndex": ifStatsIndex,
       "ifClearStats": ifClearStats,
       "igmpStats": igmpStats,
       "igmpSnoopStats": igmpSnoopStats,
       "igmpSnoopStatsEntry": igmpSnoopStatsEntry,
       "igmpSnoopVlanIndex": igmpSnoopVlanIndex,
       "rxIgmpValidPkts": rxIgmpValidPkts,
       "rxIgmpInvalidPkts": rxIgmpInvalidPkts,
       "rxIgmpGenQueries": rxIgmpGenQueries,
       "rxIgmpGrpSpecificQueries": rxIgmpGrpSpecificQueries,
       "rxIgmpLeaves": rxIgmpLeaves,
       "rxIgmpReports": rxIgmpReports,
       "txIgmpGrpSpecificQueries": txIgmpGrpSpecificQueries,
       "txIgmpReports": txIgmpReports,
       "txIgmpLeaves": txIgmpLeaves,
       "igmpClearVlanStats": igmpClearVlanStats,
       "igmpClearAllStats": igmpClearAllStats,
       "rip2Stats": rip2Stats,
       "ripStatInPackets": ripStatInPackets,
       "ripStatOutPackets": ripStatOutPackets,
       "ripStatInRequestPkts": ripStatInRequestPkts,
       "ripStatInResponsePkts": ripStatInResponsePkts,
       "ripStatOutRequestPkts": ripStatOutRequestPkts,
       "ripStatOutResponsePkts": ripStatOutResponsePkts,
       "ripStatRouteTimeout": ripStatRouteTimeout,
       "ripStatInBadSizePkts": ripStatInBadSizePkts,
       "ripStatInBadVersion": ripStatInBadVersion,
       "ripStatInBadZeros": ripStatInBadZeros,
       "ripStatInBadSourcePort": ripStatInBadSourcePort,
       "ripStatInBadSourceIP": ripStatInBadSourceIP,
       "ripStatInSelfRcvPkts": ripStatInSelfRcvPkts,
       "dnsStats": dnsStats,
       "dnsStatInGoodDnsRequests": dnsStatInGoodDnsRequests,
       "dnsStatOutDnsRequests": dnsStatOutDnsRequests,
       "dnsStatInBadDnsRequests": dnsStatInBadDnsRequests,
       "geal3Stats": geal3Stats,
       "maxL3TableSize": maxL3TableSize,
       "noL3EntriesUsed": noL3EntriesUsed,
       "maxLpmTableSize": maxLpmTableSize,
       "noLpmEntriesUsed": noLpmEntriesUsed,
       "maxBlockInLpmTable": maxBlockInLpmTable,
       "noBlocksUsedInLpmTable": noBlocksUsedInLpmTable,
       "layer3Info": layer3Info,
       "ipRoutingInfo": ipRoutingInfo,
       "ipRouteInfoTable": ipRouteInfoTable,
       "ipRouteInfoEntry": ipRouteInfoEntry,
       "ipRouteInfoIndx": ipRouteInfoIndx,
       "ipRouteInfoDestIp": ipRouteInfoDestIp,
       "ipRouteInfoMask": ipRouteInfoMask,
       "ipRouteInfoGateway": ipRouteInfoGateway,
       "ipRouteInfoTag": ipRouteInfoTag,
       "ipRouteInfoType": ipRouteInfoType,
       "ipRouteInfoInterface": ipRouteInfoInterface,
       "ipRouteInfoMetric": ipRouteInfoMetric,
       "routeTableClear": routeTableClear,
       "arpInfo": arpInfo,
       "arpInfoTable": arpInfoTable,
       "arpInfoEntry": arpInfoEntry,
       "arpInfoDestIp": arpInfoDestIp,
       "arpInfoMacAddr": arpInfoMacAddr,
       "arpInfoVLAN": arpInfoVLAN,
       "arpInfoSrcPort": arpInfoSrcPort,
       "arpInfoRefPorts": arpInfoRefPorts,
       "arpInfoFlag": arpInfoFlag,
       "arpCacheClear": arpCacheClear,
       "vrrpInfo": vrrpInfo,
       "vrrpInfoVirtRtrTable": vrrpInfoVirtRtrTable,
       "vrrpInfoVirtRtrTableEntry": vrrpInfoVirtRtrTableEntry,
       "vrrpInfoVirtRtrIndex": vrrpInfoVirtRtrIndex,
       "vrrpInfoVirtRtrConfig": vrrpInfoVirtRtrConfig,
       "vrrpInfoVirtRtrID": vrrpInfoVirtRtrID,
       "vrrpInfoVirtRtrAddr": vrrpInfoVirtRtrAddr,
       "vrrpInfoVirtRtrIfIndex": vrrpInfoVirtRtrIfIndex,
       "vrrpInfoVirtRtrPriority": vrrpInfoVirtRtrPriority,
       "vrrpInfoVirtRtrState": vrrpInfoVirtRtrState,
       "vrrpInfoVirtRtrOwnership": vrrpInfoVirtRtrOwnership,
       "vrrpInfoVirtRtrServer": vrrpInfoVirtRtrServer,
       "vrrpInfoVirtRtrProxy": vrrpInfoVirtRtrProxy,
       "ospfInfo": ospfInfo,
       "ospfGeneralInfo": ospfGeneralInfo,
       "ospfVersion": ospfVersion,
       "ospfRouterID": ospfRouterID,
       "ospfStartTime": ospfStartTime,
       "ospfProcessUptime": ospfProcessUptime,
       "ospfLsTypesSupported": ospfLsTypesSupported,
       "ospfAreaBorderRouter": ospfAreaBorderRouter,
       "ospfAreaBoundaryRouter": ospfAreaBoundaryRouter,
       "ospfExternalLsa": ospfExternalLsa,
       "ospfIntfCountForRouter": ospfIntfCountForRouter,
       "ospfVlinkCountForRouter": ospfVlinkCountForRouter,
       "ospfNewLsaReceived": ospfNewLsaReceived,
       "ospfTotalLsaOriginated": ospfTotalLsaOriginated,
       "ospfTotalNumberOfLsdbEntries": ospfTotalNumberOfLsdbEntries,
       "ospfTotalNeighbours": ospfTotalNeighbours,
       "ospfNbrInInitState": ospfNbrInInitState,
       "ospfNbrInExchState": ospfNbrInExchState,
       "ospfNbrInFullState": ospfNbrInFullState,
       "ospfTotalAreas": ospfTotalAreas,
       "ospfTotalTransitAreas": ospfTotalTransitAreas,
       "ospfTotalNssaAreas": ospfTotalNssaAreas,
       "ospfAreaInfoTable": ospfAreaInfoTable,
       "ospfAreaInfoEntry": ospfAreaInfoEntry,
       "ospfAreaInfoIndex": ospfAreaInfoIndex,
       "ospfAreaInfoId": ospfAreaInfoId,
       "ospfAreaInfoStatus": ospfAreaInfoStatus,
       "ospfTotalNumberOfInterfaces": ospfTotalNumberOfInterfaces,
       "ospfNumberOfInterfacesUp": ospfNumberOfInterfacesUp,
       "ospfAreaInfoAuthType": ospfAreaInfoAuthType,
       "ospfAreaInfoSPF": ospfAreaInfoSPF,
       "ospfNumberOfLsdbEntries": ospfNumberOfLsdbEntries,
       "ospfAreaInfoAreaBorderRouter": ospfAreaInfoAreaBorderRouter,
       "ospfAreaInfoASBoundaryRouter": ospfAreaInfoASBoundaryRouter,
       "ospfAreaInfoTotalNeighbours": ospfAreaInfoTotalNeighbours,
       "ospfIntfInfoTable": ospfIntfInfoTable,
       "ospfIntfInfoEntry": ospfIntfInfoEntry,
       "ospfIfInfoIndex": ospfIfInfoIndex,
       "ospfIfInfoIpAddress": ospfIfInfoIpAddress,
       "ospfIfInfoArea": ospfIfInfoArea,
       "ospfIfInfoAdminStatus": ospfIfInfoAdminStatus,
       "ospfIfInfoRouterID": ospfIfInfoRouterID,
       "ospfIfInfoState": ospfIfInfoState,
       "ospfIfInfoPriority": ospfIfInfoPriority,
       "ospfIfInfoDesignatedRouterID": ospfIfInfoDesignatedRouterID,
       "ospfIfInfoDesignatedRouterIpAddress": ospfIfInfoDesignatedRouterIpAddress,
       "ospfIfInfoBackupDesignatedRouterID": ospfIfInfoBackupDesignatedRouterID,
       "ospfIfInfoBackupDesignatedRouterIpAddress": ospfIfInfoBackupDesignatedRouterIpAddress,
       "ospfIfInfoHello": ospfIfInfoHello,
       "ospfIfInfoDead": ospfIfInfoDead,
       "ospfIfInfoWait": ospfIfInfoWait,
       "ospfIfInfoRetransmit": ospfIfInfoRetransmit,
       "ospfIfInfoTransitDelay": ospfIfInfoTransitDelay,
       "ospfIfInfoTotalNeighbours": ospfIfInfoTotalNeighbours,
       "ospfIfInfoEvents": ospfIfInfoEvents,
       "ospfIfInfoAuthType": ospfIfInfoAuthType,
       "ospfIfNbrTable": ospfIfNbrTable,
       "ospfIfNbrEntry": ospfIfNbrEntry,
       "ospfIfNbrIntfIndex": ospfIfNbrIntfIndex,
       "ospfIfNbrIpAddr": ospfIfNbrIpAddr,
       "ospfIfNbrPriority": ospfIfNbrPriority,
       "ospfIfNbrState": ospfIfNbrState,
       "ospfIfNbrDesignatedRtr": ospfIfNbrDesignatedRtr,
       "ospfIfNbrBackupDesignatedRtr": ospfIfNbrBackupDesignatedRtr,
       "ospfIfNbrIpAddress": ospfIfNbrIpAddress,
       "igmpInfo": igmpInfo,
       "igmpInfoTable": igmpInfoTable,
       "igmpInfoEntry": igmpInfoEntry,
       "igmpInfoIndex": igmpInfoIndex,
       "igmpInfoGroupId": igmpInfoGroupId,
       "igmpInfoVlanId": igmpInfoVlanId,
       "igmpInfoVersion": igmpInfoVersion,
       "igmpInfoPortNum": igmpInfoPortNum,
       "igmpInfoExpires": igmpInfoExpires,
       "igmpMrtrInfoTable": igmpMrtrInfoTable,
       "igmpMrtrInfoEntry": igmpMrtrInfoEntry,
       "igmpMrtrInfoIndex": igmpMrtrInfoIndex,
       "igmpMrtrInfoVlanId": igmpMrtrInfoVlanId,
       "igmpMrtrInfoPortId": igmpMrtrInfoPortId,
       "igmpMrtrInfoVersion": igmpMrtrInfoVersion,
       "igmpMrtrInfoExpires": igmpMrtrInfoExpires,
       "igmpMrtrInfoMrt": igmpMrtrInfoMrt,
       "rip2Info": rip2Info,
       "rip2GeneralInfo": rip2GeneralInfo,
       "ripInfoState": ripInfoState,
       "ripInfoUpdatePeriod": ripInfoUpdatePeriod,
       "rip2InfoIntfTable": rip2InfoIntfTable,
       "ripInfoIntfEntry": ripInfoIntfEntry,
       "ripInfoIntfIndex": ripInfoIntfIndex,
       "ripInfoIntfVersion": ripInfoIntfVersion,
       "ripInfoIntfAddress": ripInfoIntfAddress,
       "ripInfoIntfState": ripInfoIntfState,
       "ripInfoIntfListen": ripInfoIntfListen,
       "ripInfoIntfTrigUpdate": ripInfoIntfTrigUpdate,
       "ripInfoIntfMcastUpdate": ripInfoIntfMcastUpdate,
       "ripInfoIntfPoisonReverse": ripInfoIntfPoisonReverse,
       "ripInfoIntfSupply": ripInfoIntfSupply,
       "ripInfoIntfMetric": ripInfoIntfMetric,
       "ripInfoIntfAuth": ripInfoIntfAuth,
       "ripInfoIntfKey": ripInfoIntfKey,
       "ripInfoIntfDefault": ripInfoIntfDefault,
       "ipInfo": ipInfo,
       "ipInfoRouterID": ipInfoRouterID,
       "ipIntfInfoTable": ipIntfInfoTable,
       "intfInfoEntry": intfInfoEntry,
       "intfInfoIndex": intfInfoIndex,
       "intfInfoAddr": intfInfoAddr,
       "intfInfoNetMask": intfInfoNetMask,
       "intfInfoBcastAddr": intfInfoBcastAddr,
       "intfInfoVlan": intfInfoVlan,
       "intfInfoStatus": intfInfoStatus,
       "gatewayInfoTable": gatewayInfoTable,
       "gatewayInfoEntry": gatewayInfoEntry,
       "gatewayInfoIndex": gatewayInfoIndex,
       "gatewayInfoAddr": gatewayInfoAddr,
       "gatewayInfoStatus": gatewayInfoStatus,
       "ipInfoBootpRelayState": ipInfoBootpRelayState,
       "ipInfoBootpRelayAddr": ipInfoBootpRelayAddr,
       "ipInfoBootpRelayAddr2": ipInfoBootpRelayAddr2,
       "ipInfoFwdState": ipInfoFwdState,
       "ipInfoFwdDirectedBcast": ipInfoFwdDirectedBcast,
       "ipInfoNwfTable": ipInfoNwfTable,
       "ipInfoNwfEntry": ipInfoNwfEntry,
       "ipInfoNwfIndex": ipInfoNwfIndex,
       "ipInfoNwfAddr": ipInfoNwfAddr,
       "ipInfoNwfMask": ipInfoNwfMask,
       "ipInfoNwfState": ipInfoNwfState,
       "ipInfoRmapTable": ipInfoRmapTable,
       "ipInfoRmapEntry": ipInfoRmapEntry,
       "ipInfoRmapIndex": ipInfoRmapIndex,
       "ipInfoRmapLp": ipInfoRmapLp,
       "ipInfoRmapMetric": ipInfoRmapMetric,
       "ipInfoRmapPrec": ipInfoRmapPrec,
       "ipInfoRmapWeight": ipInfoRmapWeight,
       "ipInfoRmapState": ipInfoRmapState,
       "ipInfoRmapAp": ipInfoRmapAp,
       "ipInfoRmapMetricType": ipInfoRmapMetricType,
       "ipOspfInfo": ipOspfInfo,
       "ipOspfInfoState": ipOspfInfoState,
       "ipOspfInfoDefaultRouteMetric": ipOspfInfoDefaultRouteMetric,
       "ipOspfInfoDefaultRouteMetricType": ipOspfInfoDefaultRouteMetricType,
       "ipOspfInfoRouterID": ipOspfInfoRouterID,
       "ipOspfInfoLsdbLimit": ipOspfInfoLsdbLimit,
       "ipOspfAreaInfoTable": ipOspfAreaInfoTable,
       "ipOspfAreaInfoEntry": ipOspfAreaInfoEntry,
       "ipOspfAreaInfoIndex": ipOspfAreaInfoIndex,
       "ipOspfAreaInfoId": ipOspfAreaInfoId,
       "ipOspfAreaInfoSpfInterval": ipOspfAreaInfoSpfInterval,
       "ipOspfAreaInfoAuthType": ipOspfAreaInfoAuthType,
       "ipOspfAreaInfoType": ipOspfAreaInfoType,
       "ipOspfAreaInfoMetric": ipOspfAreaInfoMetric,
       "ipOspfAreaInfoStatus": ipOspfAreaInfoStatus,
       "ipOspfRangeInfoTable": ipOspfRangeInfoTable,
       "ipOspfRangeInfoEntry": ipOspfRangeInfoEntry,
       "ipOspfRangeInfoIndex": ipOspfRangeInfoIndex,
       "ipOspfRangeInfoAddr": ipOspfRangeInfoAddr,
       "ipOspfRangeInfoMask": ipOspfRangeInfoMask,
       "ipOspfRangeInfoAreaIndex": ipOspfRangeInfoAreaIndex,
       "ipOspfRangeInfoHideState": ipOspfRangeInfoHideState,
       "ipOspfRangeInfoState": ipOspfRangeInfoState,
       "ipOspfIntfInfoTable": ipOspfIntfInfoTable,
       "ipOspfIntfInfoEntry": ipOspfIntfInfoEntry,
       "ipOspfIntfInfoIndex": ipOspfIntfInfoIndex,
       "ipOspfIntfInfoId": ipOspfIntfInfoId,
       "ipOspfIntfInfoArea": ipOspfIntfInfoArea,
       "ipOspfIntfInfoMdkey": ipOspfIntfInfoMdkey,
       "ipOspfIntfInfoCost": ipOspfIntfInfoCost,
       "ipOspfIntfInfoPrio": ipOspfIntfInfoPrio,
       "ipOspfIntfInfoHello": ipOspfIntfInfoHello,
       "ipOspfIntfInfoDead": ipOspfIntfInfoDead,
       "ipOspfIntfInfoTrans": ipOspfIntfInfoTrans,
       "ipOspfIntfInfoRetra": ipOspfIntfInfoRetra,
       "ipOspfIntfInfoAuthKey": ipOspfIntfInfoAuthKey,
       "ipOspfIntfInfoStatus": ipOspfIntfInfoStatus,
       "ipOspfVirtIntfInfoTable": ipOspfVirtIntfInfoTable,
       "ipOspfVirtIntfInfoEntry": ipOspfVirtIntfInfoEntry,
       "ipOspfVirtIntfInfoIndex": ipOspfVirtIntfInfoIndex,
       "ipOspfVirtIntfInfoAreaId": ipOspfVirtIntfInfoAreaId,
       "ipOspfVirtIntfInfoNbr": ipOspfVirtIntfInfoNbr,
       "ipOspfVirtIntfInfoMdkey": ipOspfVirtIntfInfoMdkey,
       "ipOspfVirtIntfInfoHello": ipOspfVirtIntfInfoHello,
       "ipOspfVirtIntfInfoDead": ipOspfVirtIntfInfoDead,
       "ipOspfVirtIntfInfoTrans": ipOspfVirtIntfInfoTrans,
       "ipOspfVirtIntfInfoRetra": ipOspfVirtIntfInfoRetra,
       "ipOspfVirtIntfInfoAuthKey": ipOspfVirtIntfInfoAuthKey,
       "ipOspfVirtIntfInfoStatus": ipOspfVirtIntfInfoStatus,
       "ipOspfHostInfoTable": ipOspfHostInfoTable,
       "ipOspfHostInfoEntry": ipOspfHostInfoEntry,
       "ipOspfHostInfoIndex": ipOspfHostInfoIndex,
       "ipOspfHostInfoIpAddr": ipOspfHostInfoIpAddr,
       "ipOspfHostInfoAreaIndex": ipOspfHostInfoAreaIndex,
       "ipOspfHostInfoCost": ipOspfHostInfoCost,
       "ipOspfHostInfoState": ipOspfHostInfoState,
       "ipOspfRedistributeInfo": ipOspfRedistributeInfo,
       "ipOspfRedistributeStaticInfo": ipOspfRedistributeStaticInfo,
       "ipOspfRedistributeStaticInfoMetric": ipOspfRedistributeStaticInfoMetric,
       "ipOspfRedistributeStaticInfoMetricType": ipOspfRedistributeStaticInfoMetricType,
       "ipOspfRedistributeStaticInfoOutRmapList": ipOspfRedistributeStaticInfoOutRmapList,
       "ipOspfRedistributeFixedInfo": ipOspfRedistributeFixedInfo,
       "ipOspfRedistributeFixedInfoMetric": ipOspfRedistributeFixedInfoMetric,
       "ipOspfRedistributeFixedInfoMetricType": ipOspfRedistributeFixedInfoMetricType,
       "ipOspfRedistributeFixedInfoOutRmapList": ipOspfRedistributeFixedInfoOutRmapList,
       "ipOspfRedistributeRipInfo": ipOspfRedistributeRipInfo,
       "ipOspfRedistributeRipInfoMetric": ipOspfRedistributeRipInfoMetric,
       "ipOspfRedistributeRipInfoMetricType": ipOspfRedistributeRipInfoMetricType,
       "ipOspfRedistributeRipInfoOutRmapList": ipOspfRedistributeRipInfoOutRmapList,
       "ipOspfMd5keyInfoTable": ipOspfMd5keyInfoTable,
       "ipOspfMd5keyInfoEntry": ipOspfMd5keyInfoEntry,
       "ipOspfMd5keyInfoIndex": ipOspfMd5keyInfoIndex,
       "ipOspfMd5keyInfoKey": ipOspfMd5keyInfoKey,
       "layer3Oper": layer3Oper,
       "vrrpOper": vrrpOper,
       "vrrpOperVirtRtrTable": vrrpOperVirtRtrTable,
       "vrrpOperVirtRtrEntry": vrrpOperVirtRtrEntry,
       "vrrpOperVirtRtrIndex": vrrpOperVirtRtrIndex,
       "vrrpOperVirtRtrBackup": vrrpOperVirtRtrBackup,
       "vrrpOperVirtRtrGroupBackup": vrrpOperVirtRtrGroupBackup}
)

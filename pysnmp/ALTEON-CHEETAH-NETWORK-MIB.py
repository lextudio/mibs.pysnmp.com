# SNMP MIB module (ALTEON-CHEETAH-NETWORK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTEON-CHEETAH-NETWORK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:51 2024
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3)
)
layer3.setRevisions(
        ("2009-08-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Layer3Configs_ObjectIdentity = ObjectIdentity
layer3Configs = _Layer3Configs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1)
)
_IpInterfaceCfg_ObjectIdentity = ObjectIdentity
ipInterfaceCfg = _IpInterfaceCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1)
)
_IpInterfaceTableMax_Type = Integer32
_IpInterfaceTableMax_Object = MibScalar
ipInterfaceTableMax = _IpInterfaceTableMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 1),
    _IpInterfaceTableMax_Type()
)
ipInterfaceTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceTableMax.setStatus("current")
_IpCurCfgIntfTable_Object = MibTable
ipCurCfgIntfTable = _IpCurCfgIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipCurCfgIntfTable.setStatus("current")
_IpCurCfgIntfEntry_Object = MibTableRow
ipCurCfgIntfEntry = _IpCurCfgIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 2, 1)
)
ipCurCfgIntfEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgIntfIndex"),
)
if mibBuilder.loadTexts:
    ipCurCfgIntfEntry.setStatus("current")
_IpCurCfgIntfIndex_Type = Integer32
_IpCurCfgIntfIndex_Object = MibTableColumn
ipCurCfgIntfIndex = _IpCurCfgIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 2, 1, 1),
    _IpCurCfgIntfIndex_Type()
)
ipCurCfgIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfIndex.setStatus("current")
_IpCurCfgIntfAddr_Type = IpAddress
_IpCurCfgIntfAddr_Object = MibTableColumn
ipCurCfgIntfAddr = _IpCurCfgIntfAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 2, 1, 2),
    _IpCurCfgIntfAddr_Type()
)
ipCurCfgIntfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfAddr.setStatus("current")
_IpCurCfgIntfMask_Type = IpAddress
_IpCurCfgIntfMask_Object = MibTableColumn
ipCurCfgIntfMask = _IpCurCfgIntfMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 2, 1, 3),
    _IpCurCfgIntfMask_Type()
)
ipCurCfgIntfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfMask.setStatus("current")
_IpCurCfgIntfBroadcast_Type = IpAddress
_IpCurCfgIntfBroadcast_Object = MibTableColumn
ipCurCfgIntfBroadcast = _IpCurCfgIntfBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 2, 1, 4),
    _IpCurCfgIntfBroadcast_Type()
)
ipCurCfgIntfBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfBroadcast.setStatus("obsolete")
_IpCurCfgIntfVlan_Type = Integer32
_IpCurCfgIntfVlan_Object = MibTableColumn
ipCurCfgIntfVlan = _IpCurCfgIntfVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 2, 1, 7),
    _IpCurCfgIntfBootpRelay_Type()
)
ipCurCfgIntfBootpRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfBootpRelay.setStatus("current")


class _IpCurCfgIntfIpVer_Type(Integer32):
    """Custom type ipCurCfgIntfIpVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_IpCurCfgIntfIpVer_Type.__name__ = "Integer32"
_IpCurCfgIntfIpVer_Object = MibTableColumn
ipCurCfgIntfIpVer = _IpCurCfgIntfIpVer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 2, 1, 9),
    _IpCurCfgIntfIpVer_Type()
)
ipCurCfgIntfIpVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfIpVer.setStatus("current")


class _IpCurCfgIntfIpv6Addr_Type(DisplayString):
    """Custom type ipCurCfgIntfIpv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_IpCurCfgIntfIpv6Addr_Type.__name__ = "DisplayString"
_IpCurCfgIntfIpv6Addr_Object = MibTableColumn
ipCurCfgIntfIpv6Addr = _IpCurCfgIntfIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 2, 1, 10),
    _IpCurCfgIntfIpv6Addr_Type()
)
ipCurCfgIntfIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfIpv6Addr.setStatus("current")


class _IpCurCfgIntfPrefixLen_Type(Integer32):
    """Custom type ipCurCfgIntfPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_IpCurCfgIntfPrefixLen_Type.__name__ = "Integer32"
_IpCurCfgIntfPrefixLen_Object = MibTableColumn
ipCurCfgIntfPrefixLen = _IpCurCfgIntfPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 2, 1, 11),
    _IpCurCfgIntfPrefixLen_Type()
)
ipCurCfgIntfPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfPrefixLen.setStatus("current")


class _IpCurCfgIntfRouteAdv_Type(Integer32):
    """Custom type ipCurCfgIntfRouteAdv based on Integer32"""
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


_IpCurCfgIntfRouteAdv_Type.__name__ = "Integer32"
_IpCurCfgIntfRouteAdv_Object = MibTableColumn
ipCurCfgIntfRouteAdv = _IpCurCfgIntfRouteAdv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 2, 1, 12),
    _IpCurCfgIntfRouteAdv_Type()
)
ipCurCfgIntfRouteAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfRouteAdv.setStatus("current")
_IpNewCfgIntfTable_Object = MibTable
ipNewCfgIntfTable = _IpNewCfgIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ipNewCfgIntfTable.setStatus("current")
_IpNewCfgIntfEntry_Object = MibTableRow
ipNewCfgIntfEntry = _IpNewCfgIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 3, 1)
)
ipNewCfgIntfEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipNewCfgIntfIndex"),
)
if mibBuilder.loadTexts:
    ipNewCfgIntfEntry.setStatus("current")
_IpNewCfgIntfIndex_Type = Integer32
_IpNewCfgIntfIndex_Object = MibTableColumn
ipNewCfgIntfIndex = _IpNewCfgIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 3, 1, 1),
    _IpNewCfgIntfIndex_Type()
)
ipNewCfgIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgIntfIndex.setStatus("current")
_IpNewCfgIntfAddr_Type = IpAddress
_IpNewCfgIntfAddr_Object = MibTableColumn
ipNewCfgIntfAddr = _IpNewCfgIntfAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 3, 1, 2),
    _IpNewCfgIntfAddr_Type()
)
ipNewCfgIntfAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgIntfAddr.setStatus("current")
_IpNewCfgIntfMask_Type = IpAddress
_IpNewCfgIntfMask_Object = MibTableColumn
ipNewCfgIntfMask = _IpNewCfgIntfMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 3, 1, 3),
    _IpNewCfgIntfMask_Type()
)
ipNewCfgIntfMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgIntfMask.setStatus("current")
_IpNewCfgIntfBroadcast_Type = IpAddress
_IpNewCfgIntfBroadcast_Object = MibTableColumn
ipNewCfgIntfBroadcast = _IpNewCfgIntfBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 3, 1, 4),
    _IpNewCfgIntfBroadcast_Type()
)
ipNewCfgIntfBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgIntfBroadcast.setStatus("obsolete")
_IpNewCfgIntfVlan_Type = Integer32
_IpNewCfgIntfVlan_Object = MibTableColumn
ipNewCfgIntfVlan = _IpNewCfgIntfVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 3, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 3, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 3, 1, 8),
    _IpNewCfgIntfBootpRelay_Type()
)
ipNewCfgIntfBootpRelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgIntfBootpRelay.setStatus("current")


class _IpNewCfgIntfIpVer_Type(Integer32):
    """Custom type ipNewCfgIntfIpVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_IpNewCfgIntfIpVer_Type.__name__ = "Integer32"
_IpNewCfgIntfIpVer_Object = MibTableColumn
ipNewCfgIntfIpVer = _IpNewCfgIntfIpVer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 3, 1, 10),
    _IpNewCfgIntfIpVer_Type()
)
ipNewCfgIntfIpVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgIntfIpVer.setStatus("current")


class _IpNewCfgIntfIpv6Addr_Type(DisplayString):
    """Custom type ipNewCfgIntfIpv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_IpNewCfgIntfIpv6Addr_Type.__name__ = "DisplayString"
_IpNewCfgIntfIpv6Addr_Object = MibTableColumn
ipNewCfgIntfIpv6Addr = _IpNewCfgIntfIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 3, 1, 11),
    _IpNewCfgIntfIpv6Addr_Type()
)
ipNewCfgIntfIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgIntfIpv6Addr.setStatus("current")


class _IpNewCfgIntfPrefixLen_Type(Integer32):
    """Custom type ipNewCfgIntfPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_IpNewCfgIntfPrefixLen_Type.__name__ = "Integer32"
_IpNewCfgIntfPrefixLen_Object = MibTableColumn
ipNewCfgIntfPrefixLen = _IpNewCfgIntfPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 3, 1, 12),
    _IpNewCfgIntfPrefixLen_Type()
)
ipNewCfgIntfPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgIntfPrefixLen.setStatus("current")


class _IpNewCfgIntfRouteAdv_Type(Integer32):
    """Custom type ipNewCfgIntfRouteAdv based on Integer32"""
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


_IpNewCfgIntfRouteAdv_Type.__name__ = "Integer32"
_IpNewCfgIntfRouteAdv_Object = MibTableColumn
ipNewCfgIntfRouteAdv = _IpNewCfgIntfRouteAdv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 1, 3, 1, 13),
    _IpNewCfgIntfRouteAdv_Type()
)
ipNewCfgIntfRouteAdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgIntfRouteAdv.setStatus("current")
_IpGatewayCfg_ObjectIdentity = ObjectIdentity
ipGatewayCfg = _IpGatewayCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2)
)


class _IpCurCfgGwMetric_Type(Integer32):
    """Custom type ipCurCfgGwMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("roundrobin", 2),
          ("strict", 1))
    )


_IpCurCfgGwMetric_Type.__name__ = "Integer32"
_IpCurCfgGwMetric_Object = MibScalar
ipCurCfgGwMetric = _IpCurCfgGwMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 1),
    _IpCurCfgGwMetric_Type()
)
ipCurCfgGwMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwMetric.setStatus("current")


class _IpNewCfgGwMetric_Type(Integer32):
    """Custom type ipNewCfgGwMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("roundrobin", 2),
          ("strict", 1))
    )


_IpNewCfgGwMetric_Type.__name__ = "Integer32"
_IpNewCfgGwMetric_Object = MibScalar
ipNewCfgGwMetric = _IpNewCfgGwMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 2),
    _IpNewCfgGwMetric_Type()
)
ipNewCfgGwMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgGwMetric.setStatus("current")
_IpGatewayTableMax_Type = Integer32
_IpGatewayTableMax_Object = MibScalar
ipGatewayTableMax = _IpGatewayTableMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 3),
    _IpGatewayTableMax_Type()
)
ipGatewayTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGatewayTableMax.setStatus("current")
_IpCurCfgGwTable_Object = MibTable
ipCurCfgGwTable = _IpCurCfgGwTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ipCurCfgGwTable.setStatus("current")
_IpCurCfgGwEntry_Object = MibTableRow
ipCurCfgGwEntry = _IpCurCfgGwEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 4, 1)
)
ipCurCfgGwEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgGwIndex"),
)
if mibBuilder.loadTexts:
    ipCurCfgGwEntry.setStatus("current")
_IpCurCfgGwIndex_Type = Integer32
_IpCurCfgGwIndex_Object = MibTableColumn
ipCurCfgGwIndex = _IpCurCfgGwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 4, 1, 1),
    _IpCurCfgGwIndex_Type()
)
ipCurCfgGwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwIndex.setStatus("current")
_IpCurCfgGwAddr_Type = IpAddress
_IpCurCfgGwAddr_Object = MibTableColumn
ipCurCfgGwAddr = _IpCurCfgGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 4, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 4, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 4, 1, 6),
    _IpCurCfgGwArp_Type()
)
ipCurCfgGwArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwArp.setStatus("current")
_IpCurCfgGwVlan_Type = Integer32
_IpCurCfgGwVlan_Object = MibTableColumn
ipCurCfgGwVlan = _IpCurCfgGwVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 4, 1, 7),
    _IpCurCfgGwVlan_Type()
)
ipCurCfgGwVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwVlan.setStatus("current")


class _IpCurCfgGwPriority_Type(Integer32):
    """Custom type ipCurCfgGwPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_IpCurCfgGwPriority_Type.__name__ = "Integer32"
_IpCurCfgGwPriority_Object = MibTableColumn
ipCurCfgGwPriority = _IpCurCfgGwPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 4, 1, 8),
    _IpCurCfgGwPriority_Type()
)
ipCurCfgGwPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwPriority.setStatus("current")


class _IpCurCfgGwIpVer_Type(Integer32):
    """Custom type ipCurCfgGwIpVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_IpCurCfgGwIpVer_Type.__name__ = "Integer32"
_IpCurCfgGwIpVer_Object = MibTableColumn
ipCurCfgGwIpVer = _IpCurCfgGwIpVer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 4, 1, 9),
    _IpCurCfgGwIpVer_Type()
)
ipCurCfgGwIpVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwIpVer.setStatus("current")


class _IpCurCfgGwIpv6Addr_Type(DisplayString):
    """Custom type ipCurCfgGwIpv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_IpCurCfgGwIpv6Addr_Type.__name__ = "DisplayString"
_IpCurCfgGwIpv6Addr_Object = MibTableColumn
ipCurCfgGwIpv6Addr = _IpCurCfgGwIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 4, 1, 10),
    _IpCurCfgGwIpv6Addr_Type()
)
ipCurCfgGwIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwIpv6Addr.setStatus("current")
_IpNewCfgGwTable_Object = MibTable
ipNewCfgGwTable = _IpNewCfgGwTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ipNewCfgGwTable.setStatus("current")
_IpNewCfgGwEntry_Object = MibTableRow
ipNewCfgGwEntry = _IpNewCfgGwEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 5, 1)
)
ipNewCfgGwEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipNewCfgGwIndex"),
)
if mibBuilder.loadTexts:
    ipNewCfgGwEntry.setStatus("current")
_IpNewCfgGwIndex_Type = Integer32
_IpNewCfgGwIndex_Object = MibTableColumn
ipNewCfgGwIndex = _IpNewCfgGwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 5, 1, 1),
    _IpNewCfgGwIndex_Type()
)
ipNewCfgGwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgGwIndex.setStatus("current")
_IpNewCfgGwAddr_Type = IpAddress
_IpNewCfgGwAddr_Object = MibTableColumn
ipNewCfgGwAddr = _IpNewCfgGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 5, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 5, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 5, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 5, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 5, 1, 7),
    _IpNewCfgGwArp_Type()
)
ipNewCfgGwArp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgGwArp.setStatus("current")
_IpNewCfgGwVlan_Type = Integer32
_IpNewCfgGwVlan_Object = MibTableColumn
ipNewCfgGwVlan = _IpNewCfgGwVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 5, 1, 8),
    _IpNewCfgGwVlan_Type()
)
ipNewCfgGwVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgGwVlan.setStatus("current")


class _IpNewCfgGwPriority_Type(Integer32):
    """Custom type ipNewCfgGwPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_IpNewCfgGwPriority_Type.__name__ = "Integer32"
_IpNewCfgGwPriority_Object = MibTableColumn
ipNewCfgGwPriority = _IpNewCfgGwPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 5, 1, 9),
    _IpNewCfgGwPriority_Type()
)
ipNewCfgGwPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgGwPriority.setStatus("current")


class _IpNewCfgGwIpVer_Type(Integer32):
    """Custom type ipNewCfgGwIpVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_IpNewCfgGwIpVer_Type.__name__ = "Integer32"
_IpNewCfgGwIpVer_Object = MibTableColumn
ipNewCfgGwIpVer = _IpNewCfgGwIpVer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 5, 1, 10),
    _IpNewCfgGwIpVer_Type()
)
ipNewCfgGwIpVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgGwIpVer.setStatus("current")


class _IpNewCfgGwIpv6Addr_Type(DisplayString):
    """Custom type ipNewCfgGwIpv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_IpNewCfgGwIpv6Addr_Type.__name__ = "DisplayString"
_IpNewCfgGwIpv6Addr_Object = MibTableColumn
ipNewCfgGwIpv6Addr = _IpNewCfgGwIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 2, 5, 1, 11),
    _IpNewCfgGwIpv6Addr_Type()
)
ipNewCfgGwIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgGwIpv6Addr.setStatus("current")
_IpStaticRouteCfg_ObjectIdentity = ObjectIdentity
ipStaticRouteCfg = _IpStaticRouteCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3)
)
_IpStaticRouteTableMaxSize_Type = Integer32
_IpStaticRouteTableMaxSize_Object = MibScalar
ipStaticRouteTableMaxSize = _IpStaticRouteTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 1),
    _IpStaticRouteTableMaxSize_Type()
)
ipStaticRouteTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStaticRouteTableMaxSize.setStatus("current")
_IpCurCfgStaticRouteTable_Object = MibTable
ipCurCfgStaticRouteTable = _IpCurCfgStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteTable.setStatus("current")
_IpCurCfgStaticRouteEntry_Object = MibTableRow
ipCurCfgStaticRouteEntry = _IpCurCfgStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 2, 1)
)
ipCurCfgStaticRouteEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgStaticRouteIndx"),
)
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteEntry.setStatus("current")
_IpCurCfgStaticRouteIndx_Type = Integer32
_IpCurCfgStaticRouteIndx_Object = MibTableColumn
ipCurCfgStaticRouteIndx = _IpCurCfgStaticRouteIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 2, 1, 1),
    _IpCurCfgStaticRouteIndx_Type()
)
ipCurCfgStaticRouteIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteIndx.setStatus("current")
_IpCurCfgStaticRouteDestIp_Type = IpAddress
_IpCurCfgStaticRouteDestIp_Object = MibTableColumn
ipCurCfgStaticRouteDestIp = _IpCurCfgStaticRouteDestIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 2, 1, 2),
    _IpCurCfgStaticRouteDestIp_Type()
)
ipCurCfgStaticRouteDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteDestIp.setStatus("current")
_IpCurCfgStaticRouteMask_Type = IpAddress
_IpCurCfgStaticRouteMask_Object = MibTableColumn
ipCurCfgStaticRouteMask = _IpCurCfgStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 2, 1, 3),
    _IpCurCfgStaticRouteMask_Type()
)
ipCurCfgStaticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteMask.setStatus("current")
_IpCurCfgStaticRouteGateway_Type = IpAddress
_IpCurCfgStaticRouteGateway_Object = MibTableColumn
ipCurCfgStaticRouteGateway = _IpCurCfgStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 2, 1, 4),
    _IpCurCfgStaticRouteGateway_Type()
)
ipCurCfgStaticRouteGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteGateway.setStatus("current")
_IpCurCfgStaticRouteInterface_Type = Integer32
_IpCurCfgStaticRouteInterface_Object = MibTableColumn
ipCurCfgStaticRouteInterface = _IpCurCfgStaticRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 2, 1, 5),
    _IpCurCfgStaticRouteInterface_Type()
)
ipCurCfgStaticRouteInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteInterface.setStatus("current")
_IpNewCfgStaticRouteTable_Object = MibTable
ipNewCfgStaticRouteTable = _IpNewCfgStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteTable.setStatus("current")
_IpNewCfgStaticRouteEntry_Object = MibTableRow
ipNewCfgStaticRouteEntry = _IpNewCfgStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 3, 1)
)
ipNewCfgStaticRouteEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipNewCfgStaticRouteIndx"),
)
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteEntry.setStatus("current")
_IpNewCfgStaticRouteIndx_Type = Integer32
_IpNewCfgStaticRouteIndx_Object = MibTableColumn
ipNewCfgStaticRouteIndx = _IpNewCfgStaticRouteIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 3, 1, 1),
    _IpNewCfgStaticRouteIndx_Type()
)
ipNewCfgStaticRouteIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteIndx.setStatus("current")
_IpNewCfgStaticRouteDestIp_Type = IpAddress
_IpNewCfgStaticRouteDestIp_Object = MibTableColumn
ipNewCfgStaticRouteDestIp = _IpNewCfgStaticRouteDestIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 3, 1, 2),
    _IpNewCfgStaticRouteDestIp_Type()
)
ipNewCfgStaticRouteDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteDestIp.setStatus("current")
_IpNewCfgStaticRouteMask_Type = IpAddress
_IpNewCfgStaticRouteMask_Object = MibTableColumn
ipNewCfgStaticRouteMask = _IpNewCfgStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 3, 1, 3),
    _IpNewCfgStaticRouteMask_Type()
)
ipNewCfgStaticRouteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteMask.setStatus("current")
_IpNewCfgStaticRouteGateway_Type = IpAddress
_IpNewCfgStaticRouteGateway_Object = MibTableColumn
ipNewCfgStaticRouteGateway = _IpNewCfgStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 3, 1, 5),
    _IpNewCfgStaticRouteAction_Type()
)
ipNewCfgStaticRouteAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteAction.setStatus("current")
_IpNewCfgStaticRouteInterface_Type = Integer32
_IpNewCfgStaticRouteInterface_Object = MibTableColumn
ipNewCfgStaticRouteInterface = _IpNewCfgStaticRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 3, 1, 6),
    _IpNewCfgStaticRouteInterface_Type()
)
ipNewCfgStaticRouteInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteInterface.setStatus("current")
_Ipv6CurCfgStaticRouteTable_Object = MibTable
ipv6CurCfgStaticRouteTable = _Ipv6CurCfgStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 4)
)
if mibBuilder.loadTexts:
    ipv6CurCfgStaticRouteTable.setStatus("current")
_Ipv6CurCfgStaticRouteEntry_Object = MibTableRow
ipv6CurCfgStaticRouteEntry = _Ipv6CurCfgStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 4, 1)
)
ipv6CurCfgStaticRouteEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipv6CurCfgStaticRouteIndx"),
)
if mibBuilder.loadTexts:
    ipv6CurCfgStaticRouteEntry.setStatus("current")
_Ipv6CurCfgStaticRouteIndx_Type = Integer32
_Ipv6CurCfgStaticRouteIndx_Object = MibTableColumn
ipv6CurCfgStaticRouteIndx = _Ipv6CurCfgStaticRouteIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 4, 1, 1),
    _Ipv6CurCfgStaticRouteIndx_Type()
)
ipv6CurCfgStaticRouteIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6CurCfgStaticRouteIndx.setStatus("current")


class _Ipv6CurCfgStaticRouteDestIp_Type(DisplayString):
    """Custom type ipv6CurCfgStaticRouteDestIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Ipv6CurCfgStaticRouteDestIp_Type.__name__ = "DisplayString"
_Ipv6CurCfgStaticRouteDestIp_Object = MibTableColumn
ipv6CurCfgStaticRouteDestIp = _Ipv6CurCfgStaticRouteDestIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 4, 1, 2),
    _Ipv6CurCfgStaticRouteDestIp_Type()
)
ipv6CurCfgStaticRouteDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6CurCfgStaticRouteDestIp.setStatus("current")


class _Ipv6CurCfgStaticRouteMask_Type(Integer32):
    """Custom type ipv6CurCfgStaticRouteMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Ipv6CurCfgStaticRouteMask_Type.__name__ = "Integer32"
_Ipv6CurCfgStaticRouteMask_Object = MibTableColumn
ipv6CurCfgStaticRouteMask = _Ipv6CurCfgStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 4, 1, 3),
    _Ipv6CurCfgStaticRouteMask_Type()
)
ipv6CurCfgStaticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6CurCfgStaticRouteMask.setStatus("current")


class _Ipv6CurCfgStaticRouteGateway_Type(DisplayString):
    """Custom type ipv6CurCfgStaticRouteGateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Ipv6CurCfgStaticRouteGateway_Type.__name__ = "DisplayString"
_Ipv6CurCfgStaticRouteGateway_Object = MibTableColumn
ipv6CurCfgStaticRouteGateway = _Ipv6CurCfgStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 4, 1, 4),
    _Ipv6CurCfgStaticRouteGateway_Type()
)
ipv6CurCfgStaticRouteGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6CurCfgStaticRouteGateway.setStatus("current")


class _Ipv6CurCfgStaticRouteInterface_Type(Integer32):
    """Custom type ipv6CurCfgStaticRouteInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Ipv6CurCfgStaticRouteInterface_Type.__name__ = "Integer32"
_Ipv6CurCfgStaticRouteInterface_Object = MibTableColumn
ipv6CurCfgStaticRouteInterface = _Ipv6CurCfgStaticRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 4, 1, 5),
    _Ipv6CurCfgStaticRouteInterface_Type()
)
ipv6CurCfgStaticRouteInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6CurCfgStaticRouteInterface.setStatus("current")
_Ipv6NewCfgStaticRouteTable_Object = MibTable
ipv6NewCfgStaticRouteTable = _Ipv6NewCfgStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 5)
)
if mibBuilder.loadTexts:
    ipv6NewCfgStaticRouteTable.setStatus("current")
_Ipv6NewCfgStaticRouteEntry_Object = MibTableRow
ipv6NewCfgStaticRouteEntry = _Ipv6NewCfgStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 5, 1)
)
ipv6NewCfgStaticRouteEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipv6NewCfgStaticRouteIndx"),
)
if mibBuilder.loadTexts:
    ipv6NewCfgStaticRouteEntry.setStatus("current")
_Ipv6NewCfgStaticRouteIndx_Type = Integer32
_Ipv6NewCfgStaticRouteIndx_Object = MibTableColumn
ipv6NewCfgStaticRouteIndx = _Ipv6NewCfgStaticRouteIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 5, 1, 1),
    _Ipv6NewCfgStaticRouteIndx_Type()
)
ipv6NewCfgStaticRouteIndx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6NewCfgStaticRouteIndx.setStatus("current")


class _Ipv6NewCfgStaticRouteDestIp_Type(DisplayString):
    """Custom type ipv6NewCfgStaticRouteDestIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Ipv6NewCfgStaticRouteDestIp_Type.__name__ = "DisplayString"
_Ipv6NewCfgStaticRouteDestIp_Object = MibTableColumn
ipv6NewCfgStaticRouteDestIp = _Ipv6NewCfgStaticRouteDestIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 5, 1, 2),
    _Ipv6NewCfgStaticRouteDestIp_Type()
)
ipv6NewCfgStaticRouteDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6NewCfgStaticRouteDestIp.setStatus("current")


class _Ipv6NewCfgStaticRouteMask_Type(Integer32):
    """Custom type ipv6NewCfgStaticRouteMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Ipv6NewCfgStaticRouteMask_Type.__name__ = "Integer32"
_Ipv6NewCfgStaticRouteMask_Object = MibTableColumn
ipv6NewCfgStaticRouteMask = _Ipv6NewCfgStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 5, 1, 3),
    _Ipv6NewCfgStaticRouteMask_Type()
)
ipv6NewCfgStaticRouteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6NewCfgStaticRouteMask.setStatus("current")


class _Ipv6NewCfgStaticRouteGateway_Type(DisplayString):
    """Custom type ipv6NewCfgStaticRouteGateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Ipv6NewCfgStaticRouteGateway_Type.__name__ = "DisplayString"
_Ipv6NewCfgStaticRouteGateway_Object = MibTableColumn
ipv6NewCfgStaticRouteGateway = _Ipv6NewCfgStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 5, 1, 4),
    _Ipv6NewCfgStaticRouteGateway_Type()
)
ipv6NewCfgStaticRouteGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6NewCfgStaticRouteGateway.setStatus("current")


class _Ipv6NewCfgStaticRouteAction_Type(Integer32):
    """Custom type ipv6NewCfgStaticRouteAction based on Integer32"""
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


_Ipv6NewCfgStaticRouteAction_Type.__name__ = "Integer32"
_Ipv6NewCfgStaticRouteAction_Object = MibTableColumn
ipv6NewCfgStaticRouteAction = _Ipv6NewCfgStaticRouteAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 5, 1, 5),
    _Ipv6NewCfgStaticRouteAction_Type()
)
ipv6NewCfgStaticRouteAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6NewCfgStaticRouteAction.setStatus("current")


class _Ipv6NewCfgStaticRouteInterface_Type(Integer32):
    """Custom type ipv6NewCfgStaticRouteInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Ipv6NewCfgStaticRouteInterface_Type.__name__ = "Integer32"
_Ipv6NewCfgStaticRouteInterface_Object = MibTableColumn
ipv6NewCfgStaticRouteInterface = _Ipv6NewCfgStaticRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 3, 5, 1, 6),
    _Ipv6NewCfgStaticRouteInterface_Type()
)
ipv6NewCfgStaticRouteInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6NewCfgStaticRouteInterface.setStatus("current")
_IpForwardCfg_ObjectIdentity = ObjectIdentity
ipForwardCfg = _IpForwardCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4)
)
_IpFwdGeneralCfg_ObjectIdentity = ObjectIdentity
ipFwdGeneralCfg = _IpFwdGeneralCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 1)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 1, 4),
    _IpFwdNewCfgDirectedBcast_Type()
)
ipFwdNewCfgDirectedBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFwdNewCfgDirectedBcast.setStatus("current")


class _IpFwdCurCfgNoICMPRedirect_Type(Integer32):
    """Custom type ipFwdCurCfgNoICMPRedirect based on Integer32"""
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


_IpFwdCurCfgNoICMPRedirect_Type.__name__ = "Integer32"
_IpFwdCurCfgNoICMPRedirect_Object = MibScalar
ipFwdCurCfgNoICMPRedirect = _IpFwdCurCfgNoICMPRedirect_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 1, 5),
    _IpFwdCurCfgNoICMPRedirect_Type()
)
ipFwdCurCfgNoICMPRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgNoICMPRedirect.setStatus("current")


class _IpFwdNewCfgNoICMPRedirect_Type(Integer32):
    """Custom type ipFwdNewCfgNoICMPRedirect based on Integer32"""
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


_IpFwdNewCfgNoICMPRedirect_Type.__name__ = "Integer32"
_IpFwdNewCfgNoICMPRedirect_Object = MibScalar
ipFwdNewCfgNoICMPRedirect = _IpFwdNewCfgNoICMPRedirect_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 1, 6),
    _IpFwdNewCfgNoICMPRedirect_Type()
)
ipFwdNewCfgNoICMPRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFwdNewCfgNoICMPRedirect.setStatus("current")


class _IpFwdCurCfgRtCache_Type(Integer32):
    """Custom type ipFwdCurCfgRtCache based on Integer32"""
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


_IpFwdCurCfgRtCache_Type.__name__ = "Integer32"
_IpFwdCurCfgRtCache_Object = MibScalar
ipFwdCurCfgRtCache = _IpFwdCurCfgRtCache_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 1, 7),
    _IpFwdCurCfgRtCache_Type()
)
ipFwdCurCfgRtCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgRtCache.setStatus("current")


class _IpFwdNewCfgRtCache_Type(Integer32):
    """Custom type ipFwdNewCfgRtCache based on Integer32"""
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


_IpFwdNewCfgRtCache_Type.__name__ = "Integer32"
_IpFwdNewCfgRtCache_Object = MibScalar
ipFwdNewCfgRtCache = _IpFwdNewCfgRtCache_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 1, 8),
    _IpFwdNewCfgRtCache_Type()
)
ipFwdNewCfgRtCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFwdNewCfgRtCache.setStatus("current")
_IpFwdPortTableMaxSize_Type = Integer32
_IpFwdPortTableMaxSize_Object = MibScalar
ipFwdPortTableMaxSize = _IpFwdPortTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 2),
    _IpFwdPortTableMaxSize_Type()
)
ipFwdPortTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdPortTableMaxSize.setStatus("current")
_IpFwdCurCfgPortTable_Object = MibTable
ipFwdCurCfgPortTable = _IpFwdCurCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ipFwdCurCfgPortTable.setStatus("current")
_IpFwdCurCfgPortEntry_Object = MibTableRow
ipFwdCurCfgPortEntry = _IpFwdCurCfgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 3, 1)
)
ipFwdCurCfgPortEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipFwdCurCfgPortIndex"),
)
if mibBuilder.loadTexts:
    ipFwdCurCfgPortEntry.setStatus("current")
_IpFwdCurCfgPortIndex_Type = Integer32
_IpFwdCurCfgPortIndex_Object = MibTableColumn
ipFwdCurCfgPortIndex = _IpFwdCurCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 3, 1, 1),
    _IpFwdCurCfgPortIndex_Type()
)
ipFwdCurCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgPortIndex.setStatus("current")


class _IpFwdCurCfgPortState_Type(Integer32):
    """Custom type ipFwdCurCfgPortState based on Integer32"""
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


_IpFwdCurCfgPortState_Type.__name__ = "Integer32"
_IpFwdCurCfgPortState_Object = MibTableColumn
ipFwdCurCfgPortState = _IpFwdCurCfgPortState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 3, 1, 2),
    _IpFwdCurCfgPortState_Type()
)
ipFwdCurCfgPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgPortState.setStatus("current")
_IpFwdNewCfgPortTable_Object = MibTable
ipFwdNewCfgPortTable = _IpFwdNewCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    ipFwdNewCfgPortTable.setStatus("current")
_IpFwdNewCfgPortEntry_Object = MibTableRow
ipFwdNewCfgPortEntry = _IpFwdNewCfgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 4, 1)
)
ipFwdNewCfgPortEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipFwdNewCfgPortIndex"),
)
if mibBuilder.loadTexts:
    ipFwdNewCfgPortEntry.setStatus("current")
_IpFwdNewCfgPortIndex_Type = Integer32
_IpFwdNewCfgPortIndex_Object = MibTableColumn
ipFwdNewCfgPortIndex = _IpFwdNewCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 4, 1, 1),
    _IpFwdNewCfgPortIndex_Type()
)
ipFwdNewCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdNewCfgPortIndex.setStatus("current")


class _IpFwdNewCfgPortState_Type(Integer32):
    """Custom type ipFwdNewCfgPortState based on Integer32"""
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


_IpFwdNewCfgPortState_Type.__name__ = "Integer32"
_IpFwdNewCfgPortState_Object = MibTableColumn
ipFwdNewCfgPortState = _IpFwdNewCfgPortState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 4, 1, 2),
    _IpFwdNewCfgPortState_Type()
)
ipFwdNewCfgPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFwdNewCfgPortState.setStatus("current")
_IpFwdLocalTableMaxSize_Type = Integer32
_IpFwdLocalTableMaxSize_Object = MibScalar
ipFwdLocalTableMaxSize = _IpFwdLocalTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 5),
    _IpFwdLocalTableMaxSize_Type()
)
ipFwdLocalTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdLocalTableMaxSize.setStatus("current")
_IpFwdCurCfgLocalTable_Object = MibTable
ipFwdCurCfgLocalTable = _IpFwdCurCfgLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 6)
)
if mibBuilder.loadTexts:
    ipFwdCurCfgLocalTable.setStatus("current")
_IpFwdCurCfgLocalEntry_Object = MibTableRow
ipFwdCurCfgLocalEntry = _IpFwdCurCfgLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 6, 1)
)
ipFwdCurCfgLocalEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipFwdCurCfgLocalIndex"),
)
if mibBuilder.loadTexts:
    ipFwdCurCfgLocalEntry.setStatus("current")
_IpFwdCurCfgLocalIndex_Type = Integer32
_IpFwdCurCfgLocalIndex_Object = MibTableColumn
ipFwdCurCfgLocalIndex = _IpFwdCurCfgLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 6, 1, 1),
    _IpFwdCurCfgLocalIndex_Type()
)
ipFwdCurCfgLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgLocalIndex.setStatus("current")
_IpFwdCurCfgLocalSubnet_Type = IpAddress
_IpFwdCurCfgLocalSubnet_Object = MibTableColumn
ipFwdCurCfgLocalSubnet = _IpFwdCurCfgLocalSubnet_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 6, 1, 2),
    _IpFwdCurCfgLocalSubnet_Type()
)
ipFwdCurCfgLocalSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgLocalSubnet.setStatus("current")
_IpFwdCurCfgLocalMask_Type = IpAddress
_IpFwdCurCfgLocalMask_Object = MibTableColumn
ipFwdCurCfgLocalMask = _IpFwdCurCfgLocalMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 6, 1, 3),
    _IpFwdCurCfgLocalMask_Type()
)
ipFwdCurCfgLocalMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgLocalMask.setStatus("current")
_IpFwdNewCfgLocalTable_Object = MibTable
ipFwdNewCfgLocalTable = _IpFwdNewCfgLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 7)
)
if mibBuilder.loadTexts:
    ipFwdNewCfgLocalTable.setStatus("current")
_IpFwdNewCfgLocalEntry_Object = MibTableRow
ipFwdNewCfgLocalEntry = _IpFwdNewCfgLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 7, 1)
)
ipFwdNewCfgLocalEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipFwdNewCfgLocalIndex"),
)
if mibBuilder.loadTexts:
    ipFwdNewCfgLocalEntry.setStatus("current")
_IpFwdNewCfgLocalIndex_Type = Integer32
_IpFwdNewCfgLocalIndex_Object = MibTableColumn
ipFwdNewCfgLocalIndex = _IpFwdNewCfgLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 7, 1, 1),
    _IpFwdNewCfgLocalIndex_Type()
)
ipFwdNewCfgLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdNewCfgLocalIndex.setStatus("current")
_IpFwdNewCfgLocalSubnet_Type = IpAddress
_IpFwdNewCfgLocalSubnet_Object = MibTableColumn
ipFwdNewCfgLocalSubnet = _IpFwdNewCfgLocalSubnet_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 7, 1, 2),
    _IpFwdNewCfgLocalSubnet_Type()
)
ipFwdNewCfgLocalSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFwdNewCfgLocalSubnet.setStatus("current")
_IpFwdNewCfgLocalMask_Type = IpAddress
_IpFwdNewCfgLocalMask_Object = MibTableColumn
ipFwdNewCfgLocalMask = _IpFwdNewCfgLocalMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 7, 1, 3),
    _IpFwdNewCfgLocalMask_Type()
)
ipFwdNewCfgLocalMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFwdNewCfgLocalMask.setStatus("current")


class _IpFwdNewCfgLocalDelete_Type(Integer32):
    """Custom type ipFwdNewCfgLocalDelete based on Integer32"""
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


_IpFwdNewCfgLocalDelete_Type.__name__ = "Integer32"
_IpFwdNewCfgLocalDelete_Object = MibTableColumn
ipFwdNewCfgLocalDelete = _IpFwdNewCfgLocalDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 4, 7, 1, 4),
    _IpFwdNewCfgLocalDelete_Type()
)
ipFwdNewCfgLocalDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFwdNewCfgLocalDelete.setStatus("current")
_VrrpCfg_ObjectIdentity = ObjectIdentity
vrrpCfg = _VrrpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6)
)
_VrrpGeneral_ObjectIdentity = ObjectIdentity
vrrpGeneral = _VrrpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 18),
    _VrrpNewCfgGenTckHsrvInc_Type()
)
vrrpNewCfgGenTckHsrvInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckHsrvInc.setStatus("current")


class _VrrpCurCfgGenHoldoff_Type(Integer32):
    """Custom type vrrpCurCfgGenHoldoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrrpCurCfgGenHoldoff_Type.__name__ = "Integer32"
_VrrpCurCfgGenHoldoff_Object = MibScalar
vrrpCurCfgGenHoldoff = _VrrpCurCfgGenHoldoff_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 19),
    _VrrpCurCfgGenHoldoff_Type()
)
vrrpCurCfgGenHoldoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenHoldoff.setStatus("current")


class _VrrpNewCfgGenHoldoff_Type(Integer32):
    """Custom type vrrpNewCfgGenHoldoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrrpNewCfgGenHoldoff_Type.__name__ = "Integer32"
_VrrpNewCfgGenHoldoff_Object = MibScalar
vrrpNewCfgGenHoldoff = _VrrpNewCfgGenHoldoff_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 1, 20),
    _VrrpNewCfgGenHoldoff_Type()
)
vrrpNewCfgGenHoldoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenHoldoff.setStatus("current")
_VrrpVirtRtrTableMaxSize_Type = Integer32
_VrrpVirtRtrTableMaxSize_Object = MibScalar
vrrpVirtRtrTableMaxSize = _VrrpVirtRtrTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 2),
    _VrrpVirtRtrTableMaxSize_Type()
)
vrrpVirtRtrTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpVirtRtrTableMaxSize.setStatus("current")
_VrrpCurCfgVirtRtrTable_Object = MibTable
vrrpCurCfgVirtRtrTable = _VrrpCurCfgVirtRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3)
)
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTable.setStatus("current")
_VrrpCurCfgVirtRtrTableEntry_Object = MibTableRow
vrrpCurCfgVirtRtrTableEntry = _VrrpCurCfgVirtRtrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1)
)
vrrpCurCfgVirtRtrTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrIndx"),
)
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTableEntry.setStatus("current")
_VrrpCurCfgVirtRtrIndx_Type = Integer32
_VrrpCurCfgVirtRtrIndx_Object = MibTableColumn
vrrpCurCfgVirtRtrIndx = _VrrpCurCfgVirtRtrIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 1),
    _VrrpCurCfgVirtRtrIndx_Type()
)
vrrpCurCfgVirtRtrIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrIndx.setStatus("current")


class _VrrpCurCfgVirtRtrID_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VrrpCurCfgVirtRtrID_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrID_Object = MibTableColumn
vrrpCurCfgVirtRtrID = _VrrpCurCfgVirtRtrID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 2),
    _VrrpCurCfgVirtRtrID_Type()
)
vrrpCurCfgVirtRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrID.setStatus("current")
_VrrpCurCfgVirtRtrAddr_Type = IpAddress
_VrrpCurCfgVirtRtrAddr_Object = MibTableColumn
vrrpCurCfgVirtRtrAddr = _VrrpCurCfgVirtRtrAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 3),
    _VrrpCurCfgVirtRtrAddr_Type()
)
vrrpCurCfgVirtRtrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrAddr.setStatus("current")
_VrrpCurCfgVirtRtrIfIndex_Type = Integer32
_VrrpCurCfgVirtRtrIfIndex_Object = MibTableColumn
vrrpCurCfgVirtRtrIfIndex = _VrrpCurCfgVirtRtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 16),
    _VrrpCurCfgVirtRtrTckHsrv_Type()
)
vrrpCurCfgVirtRtrTckHsrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckHsrv.setStatus("current")


class _VrrpCurCfgVirtRtrVersion_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v4", 1),
          ("v6", 2))
    )


_VrrpCurCfgVirtRtrVersion_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrVersion_Object = MibTableColumn
vrrpCurCfgVirtRtrVersion = _VrrpCurCfgVirtRtrVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 17),
    _VrrpCurCfgVirtRtrVersion_Type()
)
vrrpCurCfgVirtRtrVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVersion.setStatus("current")


class _VrrpCurCfgVirtRtrIpv6Addr_Type(DisplayString):
    """Custom type vrrpCurCfgVirtRtrIpv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VrrpCurCfgVirtRtrIpv6Addr_Type.__name__ = "DisplayString"
_VrrpCurCfgVirtRtrIpv6Addr_Object = MibTableColumn
vrrpCurCfgVirtRtrIpv6Addr = _VrrpCurCfgVirtRtrIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 18),
    _VrrpCurCfgVirtRtrIpv6Addr_Type()
)
vrrpCurCfgVirtRtrIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrIpv6Addr.setStatus("current")


class _VrrpCurCfgVirtRtrIpv6Interval_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrIpv6Interval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1045),
    )


_VrrpCurCfgVirtRtrIpv6Interval_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrIpv6Interval_Object = MibTableColumn
vrrpCurCfgVirtRtrIpv6Interval = _VrrpCurCfgVirtRtrIpv6Interval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 3, 1, 19),
    _VrrpCurCfgVirtRtrIpv6Interval_Type()
)
vrrpCurCfgVirtRtrIpv6Interval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrIpv6Interval.setStatus("current")
_VrrpNewCfgVirtRtrTable_Object = MibTable
vrrpNewCfgVirtRtrTable = _VrrpNewCfgVirtRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4)
)
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTable.setStatus("current")
_VrrpNewCfgVirtRtrTableEntry_Object = MibTableRow
vrrpNewCfgVirtRtrTableEntry = _VrrpNewCfgVirtRtrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1)
)
vrrpNewCfgVirtRtrTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "vrrpNewCfgVirtRtrIndx"),
)
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTableEntry.setStatus("current")
_VrrpNewCfgVirtRtrIndx_Type = Integer32
_VrrpNewCfgVirtRtrIndx_Object = MibTableColumn
vrrpNewCfgVirtRtrIndx = _VrrpNewCfgVirtRtrIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 1),
    _VrrpNewCfgVirtRtrIndx_Type()
)
vrrpNewCfgVirtRtrIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrIndx.setStatus("current")


class _VrrpNewCfgVirtRtrID_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VrrpNewCfgVirtRtrID_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrID_Object = MibTableColumn
vrrpNewCfgVirtRtrID = _VrrpNewCfgVirtRtrID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 2),
    _VrrpNewCfgVirtRtrID_Type()
)
vrrpNewCfgVirtRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrID.setStatus("current")
_VrrpNewCfgVirtRtrAddr_Type = IpAddress
_VrrpNewCfgVirtRtrAddr_Object = MibTableColumn
vrrpNewCfgVirtRtrAddr = _VrrpNewCfgVirtRtrAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 3),
    _VrrpNewCfgVirtRtrAddr_Type()
)
vrrpNewCfgVirtRtrAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrAddr.setStatus("current")
_VrrpNewCfgVirtRtrIfIndex_Type = Integer32
_VrrpNewCfgVirtRtrIfIndex_Object = MibTableColumn
vrrpNewCfgVirtRtrIfIndex = _VrrpNewCfgVirtRtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 17),
    _VrrpNewCfgVirtRtrTckHsrv_Type()
)
vrrpNewCfgVirtRtrTckHsrv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckHsrv.setStatus("current")


class _VrrpNewCfgVirtRtrVersion_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v4", 1),
          ("v6", 2))
    )


_VrrpNewCfgVirtRtrVersion_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrVersion_Object = MibTableColumn
vrrpNewCfgVirtRtrVersion = _VrrpNewCfgVirtRtrVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 18),
    _VrrpNewCfgVirtRtrVersion_Type()
)
vrrpNewCfgVirtRtrVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVersion.setStatus("current")


class _VrrpNewCfgVirtRtrIpv6Addr_Type(DisplayString):
    """Custom type vrrpNewCfgVirtRtrIpv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VrrpNewCfgVirtRtrIpv6Addr_Type.__name__ = "DisplayString"
_VrrpNewCfgVirtRtrIpv6Addr_Object = MibTableColumn
vrrpNewCfgVirtRtrIpv6Addr = _VrrpNewCfgVirtRtrIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 19),
    _VrrpNewCfgVirtRtrIpv6Addr_Type()
)
vrrpNewCfgVirtRtrIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrIpv6Addr.setStatus("current")


class _VrrpNewCfgVirtRtrIpv6Interval_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrIpv6Interval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_VrrpNewCfgVirtRtrIpv6Interval_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrIpv6Interval_Object = MibTableColumn
vrrpNewCfgVirtRtrIpv6Interval = _VrrpNewCfgVirtRtrIpv6Interval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 4, 1, 20),
    _VrrpNewCfgVirtRtrIpv6Interval_Type()
)
vrrpNewCfgVirtRtrIpv6Interval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrIpv6Interval.setStatus("current")
_VrrpIfTableMaxSize_Type = Integer32
_VrrpIfTableMaxSize_Object = MibScalar
vrrpIfTableMaxSize = _VrrpIfTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 5),
    _VrrpIfTableMaxSize_Type()
)
vrrpIfTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpIfTableMaxSize.setStatus("current")
_VrrpCurCfgIfTable_Object = MibTable
vrrpCurCfgIfTable = _VrrpCurCfgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 6)
)
if mibBuilder.loadTexts:
    vrrpCurCfgIfTable.setStatus("current")
_VrrpCurCfgIfTableEntry_Object = MibTableRow
vrrpCurCfgIfTableEntry = _VrrpCurCfgIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 6, 1)
)
vrrpCurCfgIfTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgIfIndx"),
)
if mibBuilder.loadTexts:
    vrrpCurCfgIfTableEntry.setStatus("current")
_VrrpCurCfgIfIndx_Type = Integer32
_VrrpCurCfgIfIndx_Object = MibTableColumn
vrrpCurCfgIfIndx = _VrrpCurCfgIfIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 6, 1, 3),
    _VrrpCurCfgIfPasswd_Type()
)
vrrpCurCfgIfPasswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgIfPasswd.setStatus("current")
_VrrpCurCfgIfIpAddr_Type = IpAddress
_VrrpCurCfgIfIpAddr_Object = MibTableColumn
vrrpCurCfgIfIpAddr = _VrrpCurCfgIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 6, 1, 4),
    _VrrpCurCfgIfIpAddr_Type()
)
vrrpCurCfgIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgIfIpAddr.setStatus("current")
_VrrpNewCfgIfTable_Object = MibTable
vrrpNewCfgIfTable = _VrrpNewCfgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 7)
)
if mibBuilder.loadTexts:
    vrrpNewCfgIfTable.setStatus("current")
_VrrpNewCfgIfTableEntry_Object = MibTableRow
vrrpNewCfgIfTableEntry = _VrrpNewCfgIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 7, 1)
)
vrrpNewCfgIfTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "vrrpNewCfgIfIndx"),
)
if mibBuilder.loadTexts:
    vrrpNewCfgIfTableEntry.setStatus("current")
_VrrpNewCfgIfIndx_Type = Integer32
_VrrpNewCfgIfIndx_Object = MibTableColumn
vrrpNewCfgIfIndx = _VrrpNewCfgIfIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 7, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 7, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 7, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 7, 1, 4),
    _VrrpNewCfgIfDelete_Type()
)
vrrpNewCfgIfDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgIfDelete.setStatus("current")
_VrrpVirtRtrGrpTableMaxSize_Type = Integer32
_VrrpVirtRtrGrpTableMaxSize_Object = MibScalar
vrrpVirtRtrGrpTableMaxSize = _VrrpVirtRtrGrpTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 8),
    _VrrpVirtRtrGrpTableMaxSize_Type()
)
vrrpVirtRtrGrpTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpVirtRtrGrpTableMaxSize.setStatus("current")
_VrrpCurCfgVirtRtrGrpTable_Object = MibTable
vrrpCurCfgVirtRtrGrpTable = _VrrpCurCfgVirtRtrGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9)
)
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTable.setStatus("current")
_VrrpCurCfgVirtRtrGrpTableEntry_Object = MibTableRow
vrrpCurCfgVirtRtrGrpTableEntry = _VrrpCurCfgVirtRtrGrpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9, 1)
)
vrrpCurCfgVirtRtrGrpTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrGrpIndx"),
)
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTableEntry.setStatus("current")
_VrrpCurCfgVirtRtrGrpIndx_Type = Integer32
_VrrpCurCfgVirtRtrGrpIndx_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpIndx = _VrrpCurCfgVirtRtrGrpIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9, 1, 1),
    _VrrpCurCfgVirtRtrGrpIndx_Type()
)
vrrpCurCfgVirtRtrGrpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpIndx.setStatus("current")


class _VrrpCurCfgVirtRtrGrpID_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VrrpCurCfgVirtRtrGrpID_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpID_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpID = _VrrpCurCfgVirtRtrGrpID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9, 1, 2),
    _VrrpCurCfgVirtRtrGrpID_Type()
)
vrrpCurCfgVirtRtrGrpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpID.setStatus("current")
_VrrpCurCfgVirtRtrGrpIfIndex_Type = Integer32
_VrrpCurCfgVirtRtrGrpIfIndex_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpIfIndex = _VrrpCurCfgVirtRtrGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9, 1, 15),
    _VrrpCurCfgVirtRtrGrpTckHsrv_Type()
)
vrrpCurCfgVirtRtrGrpTckHsrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckHsrv.setStatus("current")


class _VrrpCurCfgVirtRtrGrpVersion_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v4", 1),
          ("v6", 2))
    )


_VrrpCurCfgVirtRtrGrpVersion_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpVersion_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpVersion = _VrrpCurCfgVirtRtrGrpVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9, 1, 16),
    _VrrpCurCfgVirtRtrGrpVersion_Type()
)
vrrpCurCfgVirtRtrGrpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpVersion.setStatus("current")


class _VrrpCurCfgVirtRtrGrpIpv6Interval_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpIpv6Interval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_VrrpCurCfgVirtRtrGrpIpv6Interval_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpIpv6Interval_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpIpv6Interval = _VrrpCurCfgVirtRtrGrpIpv6Interval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 9, 1, 17),
    _VrrpCurCfgVirtRtrGrpIpv6Interval_Type()
)
vrrpCurCfgVirtRtrGrpIpv6Interval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpIpv6Interval.setStatus("current")
_VrrpNewCfgVirtRtrGrpTable_Object = MibTable
vrrpNewCfgVirtRtrGrpTable = _VrrpNewCfgVirtRtrGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10)
)
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTable.setStatus("current")
_VrrpNewCfgVirtRtrGrpTableEntry_Object = MibTableRow
vrrpNewCfgVirtRtrGrpTableEntry = _VrrpNewCfgVirtRtrGrpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1)
)
vrrpNewCfgVirtRtrGrpTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "vrrpNewCfgVirtRtrGrpIndx"),
)
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTableEntry.setStatus("current")
_VrrpNewCfgVirtRtrGrpIndx_Type = Integer32
_VrrpNewCfgVirtRtrGrpIndx_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpIndx = _VrrpNewCfgVirtRtrGrpIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1, 1),
    _VrrpNewCfgVirtRtrGrpIndx_Type()
)
vrrpNewCfgVirtRtrGrpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpIndx.setStatus("current")


class _VrrpNewCfgVirtRtrGrpID_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VrrpNewCfgVirtRtrGrpID_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpID_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpID = _VrrpNewCfgVirtRtrGrpID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1, 2),
    _VrrpNewCfgVirtRtrGrpID_Type()
)
vrrpNewCfgVirtRtrGrpID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpID.setStatus("current")
_VrrpNewCfgVirtRtrGrpIfIndex_Type = Integer32
_VrrpNewCfgVirtRtrGrpIfIndex_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpIfIndex = _VrrpNewCfgVirtRtrGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1, 16),
    _VrrpNewCfgVirtRtrGrpTckHsrv_Type()
)
vrrpNewCfgVirtRtrGrpTckHsrv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckHsrv.setStatus("current")


class _VrrpNewCfgVirtRtrGrpVersion_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v4", 1),
          ("v6", 2))
    )


_VrrpNewCfgVirtRtrGrpVersion_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpVersion_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpVersion = _VrrpNewCfgVirtRtrGrpVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1, 17),
    _VrrpNewCfgVirtRtrGrpVersion_Type()
)
vrrpNewCfgVirtRtrGrpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpVersion.setStatus("current")


class _VrrpNewCfgVirtRtrGrpIpv6Interval_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpIpv6Interval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_VrrpNewCfgVirtRtrGrpIpv6Interval_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpIpv6Interval_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpIpv6Interval = _VrrpNewCfgVirtRtrGrpIpv6Interval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 10, 1, 18),
    _VrrpNewCfgVirtRtrGrpIpv6Interval_Type()
)
vrrpNewCfgVirtRtrGrpIpv6Interval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpIpv6Interval.setStatus("current")
_VrrpVirtRtrVrGrpTableMaxSize_Type = Integer32
_VrrpVirtRtrVrGrpTableMaxSize_Object = MibScalar
vrrpVirtRtrVrGrpTableMaxSize = _VrrpVirtRtrVrGrpTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 11),
    _VrrpVirtRtrVrGrpTableMaxSize_Type()
)
vrrpVirtRtrVrGrpTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpVirtRtrVrGrpTableMaxSize.setStatus("current")
_VrrpCurCfgVirtRtrVrGrpTable_Object = MibTable
vrrpCurCfgVirtRtrVrGrpTable = _VrrpCurCfgVirtRtrVrGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 12)
)
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVrGrpTable.setStatus("current")
_VrrpCurCfgVirtRtrVrGrpTableEntry_Object = MibTableRow
vrrpCurCfgVirtRtrVrGrpTableEntry = _VrrpCurCfgVirtRtrVrGrpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 12, 1)
)
vrrpCurCfgVirtRtrVrGrpTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "vrrpCurCfgVirtRtrVrGrpIndx"),
)
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVrGrpTableEntry.setStatus("current")
_VrrpCurCfgVirtRtrVrGrpIndx_Type = Integer32
_VrrpCurCfgVirtRtrVrGrpIndx_Object = MibTableColumn
vrrpCurCfgVirtRtrVrGrpIndx = _VrrpCurCfgVirtRtrVrGrpIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 12, 1, 1),
    _VrrpCurCfgVirtRtrVrGrpIndx_Type()
)
vrrpCurCfgVirtRtrVrGrpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVrGrpIndx.setStatus("current")


class _VrrpCurCfgVirtRtrVrGrpName_Type(DisplayString):
    """Custom type vrrpCurCfgVirtRtrVrGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VrrpCurCfgVirtRtrVrGrpName_Type.__name__ = "DisplayString"
_VrrpCurCfgVirtRtrVrGrpName_Object = MibTableColumn
vrrpCurCfgVirtRtrVrGrpName = _VrrpCurCfgVirtRtrVrGrpName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 12, 1, 2),
    _VrrpCurCfgVirtRtrVrGrpName_Type()
)
vrrpCurCfgVirtRtrVrGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVrGrpName.setStatus("current")


class _VrrpCurCfgVirtRtrVrGrpState_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrVrGrpState based on Integer32"""
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


_VrrpCurCfgVirtRtrVrGrpState_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrVrGrpState_Object = MibTableColumn
vrrpCurCfgVirtRtrVrGrpState = _VrrpCurCfgVirtRtrVrGrpState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 12, 1, 3),
    _VrrpCurCfgVirtRtrVrGrpState_Type()
)
vrrpCurCfgVirtRtrVrGrpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVrGrpState.setStatus("current")
_VrrpCurCfgVirtRtrVrGrpBmap_Type = OctetString
_VrrpCurCfgVirtRtrVrGrpBmap_Object = MibTableColumn
vrrpCurCfgVirtRtrVrGrpBmap = _VrrpCurCfgVirtRtrVrGrpBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 12, 1, 4),
    _VrrpCurCfgVirtRtrVrGrpBmap_Type()
)
vrrpCurCfgVirtRtrVrGrpBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVrGrpBmap.setStatus("current")


class _VrrpCurCfgVirtRtrVrGrpPriority_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrVrGrpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VrrpCurCfgVirtRtrVrGrpPriority_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrVrGrpPriority_Object = MibTableColumn
vrrpCurCfgVirtRtrVrGrpPriority = _VrrpCurCfgVirtRtrVrGrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 12, 1, 5),
    _VrrpCurCfgVirtRtrVrGrpPriority_Type()
)
vrrpCurCfgVirtRtrVrGrpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVrGrpPriority.setStatus("current")


class _VrrpCurCfgVirtRtrVrGrpTckIpIntf_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrVrGrpTckIpIntf based on Integer32"""
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


_VrrpCurCfgVirtRtrVrGrpTckIpIntf_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrVrGrpTckIpIntf_Object = MibTableColumn
vrrpCurCfgVirtRtrVrGrpTckIpIntf = _VrrpCurCfgVirtRtrVrGrpTckIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 12, 1, 6),
    _VrrpCurCfgVirtRtrVrGrpTckIpIntf_Type()
)
vrrpCurCfgVirtRtrVrGrpTckIpIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVrGrpTckIpIntf.setStatus("current")


class _VrrpCurCfgVirtRtrVrGrpTckVlanPort_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrVrGrpTckVlanPort based on Integer32"""
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


_VrrpCurCfgVirtRtrVrGrpTckVlanPort_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrVrGrpTckVlanPort_Object = MibTableColumn
vrrpCurCfgVirtRtrVrGrpTckVlanPort = _VrrpCurCfgVirtRtrVrGrpTckVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 12, 1, 7),
    _VrrpCurCfgVirtRtrVrGrpTckVlanPort_Type()
)
vrrpCurCfgVirtRtrVrGrpTckVlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVrGrpTckVlanPort.setStatus("current")


class _VrrpCurCfgVirtRtrVrGrpTckL4Port_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrVrGrpTckL4Port based on Integer32"""
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


_VrrpCurCfgVirtRtrVrGrpTckL4Port_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrVrGrpTckL4Port_Object = MibTableColumn
vrrpCurCfgVirtRtrVrGrpTckL4Port = _VrrpCurCfgVirtRtrVrGrpTckL4Port_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 12, 1, 8),
    _VrrpCurCfgVirtRtrVrGrpTckL4Port_Type()
)
vrrpCurCfgVirtRtrVrGrpTckL4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVrGrpTckL4Port.setStatus("current")


class _VrrpCurCfgVirtRtrVrGrpTckRServer_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrVrGrpTckRServer based on Integer32"""
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


_VrrpCurCfgVirtRtrVrGrpTckRServer_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrVrGrpTckRServer_Object = MibTableColumn
vrrpCurCfgVirtRtrVrGrpTckRServer = _VrrpCurCfgVirtRtrVrGrpTckRServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 12, 1, 9),
    _VrrpCurCfgVirtRtrVrGrpTckRServer_Type()
)
vrrpCurCfgVirtRtrVrGrpTckRServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVrGrpTckRServer.setStatus("current")


class _VrrpCurCfgVirtRtrVrGrpTckHsrp_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrVrGrpTckHsrp based on Integer32"""
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


_VrrpCurCfgVirtRtrVrGrpTckHsrp_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrVrGrpTckHsrp_Object = MibTableColumn
vrrpCurCfgVirtRtrVrGrpTckHsrp = _VrrpCurCfgVirtRtrVrGrpTckHsrp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 12, 1, 10),
    _VrrpCurCfgVirtRtrVrGrpTckHsrp_Type()
)
vrrpCurCfgVirtRtrVrGrpTckHsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVrGrpTckHsrp.setStatus("current")


class _VrrpCurCfgVirtRtrVrGrpTckHsrv_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrVrGrpTckHsrv based on Integer32"""
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


_VrrpCurCfgVirtRtrVrGrpTckHsrv_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrVrGrpTckHsrv_Object = MibTableColumn
vrrpCurCfgVirtRtrVrGrpTckHsrv = _VrrpCurCfgVirtRtrVrGrpTckHsrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 12, 1, 11),
    _VrrpCurCfgVirtRtrVrGrpTckHsrv_Type()
)
vrrpCurCfgVirtRtrVrGrpTckHsrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVrGrpTckHsrv.setStatus("current")


class _VrrpCurCfgVirtRtrVrGrpTckVirtRtrNo_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrVrGrpTckVirtRtrNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_VrrpCurCfgVirtRtrVrGrpTckVirtRtrNo_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrVrGrpTckVirtRtrNo_Object = MibTableColumn
vrrpCurCfgVirtRtrVrGrpTckVirtRtrNo = _VrrpCurCfgVirtRtrVrGrpTckVirtRtrNo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 12, 1, 12),
    _VrrpCurCfgVirtRtrVrGrpTckVirtRtrNo_Type()
)
vrrpCurCfgVirtRtrVrGrpTckVirtRtrNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVrGrpTckVirtRtrNo.setStatus("current")


class _VrrpCurCfgVirtRtrVrGrpAdd_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrVrGrpAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_VrrpCurCfgVirtRtrVrGrpAdd_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrVrGrpAdd_Object = MibTableColumn
vrrpCurCfgVirtRtrVrGrpAdd = _VrrpCurCfgVirtRtrVrGrpAdd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 12, 1, 13),
    _VrrpCurCfgVirtRtrVrGrpAdd_Type()
)
vrrpCurCfgVirtRtrVrGrpAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVrGrpAdd.setStatus("current")


class _VrrpCurCfgVirtRtrVrGrpAdverInterval_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrVrGrpAdverInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpCurCfgVirtRtrVrGrpAdverInterval_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrVrGrpAdverInterval_Object = MibTableColumn
vrrpCurCfgVirtRtrVrGrpAdverInterval = _VrrpCurCfgVirtRtrVrGrpAdverInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 12, 1, 14),
    _VrrpCurCfgVirtRtrVrGrpAdverInterval_Type()
)
vrrpCurCfgVirtRtrVrGrpAdverInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVrGrpAdverInterval.setStatus("current")


class _VrrpCurCfgVirtRtrVrGrpPreemption_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrVrGrpPreemption based on Integer32"""
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


_VrrpCurCfgVirtRtrVrGrpPreemption_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrVrGrpPreemption_Object = MibTableColumn
vrrpCurCfgVirtRtrVrGrpPreemption = _VrrpCurCfgVirtRtrVrGrpPreemption_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 12, 1, 15),
    _VrrpCurCfgVirtRtrVrGrpPreemption_Type()
)
vrrpCurCfgVirtRtrVrGrpPreemption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVrGrpPreemption.setStatus("current")


class _VrrpCurCfgVirtRtrVrGrpSharing_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrVrGrpSharing based on Integer32"""
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


_VrrpCurCfgVirtRtrVrGrpSharing_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrVrGrpSharing_Object = MibTableColumn
vrrpCurCfgVirtRtrVrGrpSharing = _VrrpCurCfgVirtRtrVrGrpSharing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 12, 1, 16),
    _VrrpCurCfgVirtRtrVrGrpSharing_Type()
)
vrrpCurCfgVirtRtrVrGrpSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrVrGrpSharing.setStatus("current")
_VrrpNewCfgVirtRtrVrGrpTable_Object = MibTable
vrrpNewCfgVirtRtrVrGrpTable = _VrrpNewCfgVirtRtrVrGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13)
)
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpTable.setStatus("current")
_VrrpNewCfgVirtRtrVrGrpTableEntry_Object = MibTableRow
vrrpNewCfgVirtRtrVrGrpTableEntry = _VrrpNewCfgVirtRtrVrGrpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1)
)
vrrpNewCfgVirtRtrVrGrpTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "vrrpNewCfgVirtRtrVrGrpIndx"),
)
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpTableEntry.setStatus("current")
_VrrpNewCfgVirtRtrVrGrpIndx_Type = Integer32
_VrrpNewCfgVirtRtrVrGrpIndx_Object = MibTableColumn
vrrpNewCfgVirtRtrVrGrpIndx = _VrrpNewCfgVirtRtrVrGrpIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1, 1),
    _VrrpNewCfgVirtRtrVrGrpIndx_Type()
)
vrrpNewCfgVirtRtrVrGrpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpIndx.setStatus("current")


class _VrrpNewCfgVirtRtrVrGrpName_Type(DisplayString):
    """Custom type vrrpNewCfgVirtRtrVrGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VrrpNewCfgVirtRtrVrGrpName_Type.__name__ = "DisplayString"
_VrrpNewCfgVirtRtrVrGrpName_Object = MibTableColumn
vrrpNewCfgVirtRtrVrGrpName = _VrrpNewCfgVirtRtrVrGrpName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1, 2),
    _VrrpNewCfgVirtRtrVrGrpName_Type()
)
vrrpNewCfgVirtRtrVrGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpName.setStatus("current")


class _VrrpNewCfgVirtRtrVrGrpAdd_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrVrGrpAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VrrpNewCfgVirtRtrVrGrpAdd_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrVrGrpAdd_Object = MibTableColumn
vrrpNewCfgVirtRtrVrGrpAdd = _VrrpNewCfgVirtRtrVrGrpAdd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1, 3),
    _VrrpNewCfgVirtRtrVrGrpAdd_Type()
)
vrrpNewCfgVirtRtrVrGrpAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpAdd.setStatus("current")


class _VrrpNewCfgVirtRtrVrGrpRem_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrVrGrpRem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VrrpNewCfgVirtRtrVrGrpRem_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrVrGrpRem_Object = MibTableColumn
vrrpNewCfgVirtRtrVrGrpRem = _VrrpNewCfgVirtRtrVrGrpRem_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1, 4),
    _VrrpNewCfgVirtRtrVrGrpRem_Type()
)
vrrpNewCfgVirtRtrVrGrpRem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpRem.setStatus("current")


class _VrrpNewCfgVirtRtrVrGrpState_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrVrGrpState based on Integer32"""
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


_VrrpNewCfgVirtRtrVrGrpState_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrVrGrpState_Object = MibTableColumn
vrrpNewCfgVirtRtrVrGrpState = _VrrpNewCfgVirtRtrVrGrpState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1, 5),
    _VrrpNewCfgVirtRtrVrGrpState_Type()
)
vrrpNewCfgVirtRtrVrGrpState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpState.setStatus("current")


class _VrrpNewCfgVirtRtrVrGrpDelete_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrVrGrpDelete based on Integer32"""
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


_VrrpNewCfgVirtRtrVrGrpDelete_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrVrGrpDelete_Object = MibTableColumn
vrrpNewCfgVirtRtrVrGrpDelete = _VrrpNewCfgVirtRtrVrGrpDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1, 6),
    _VrrpNewCfgVirtRtrVrGrpDelete_Type()
)
vrrpNewCfgVirtRtrVrGrpDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpDelete.setStatus("current")
_VrrpNewCfgVirtRtrVrGrpBmap_Type = OctetString
_VrrpNewCfgVirtRtrVrGrpBmap_Object = MibTableColumn
vrrpNewCfgVirtRtrVrGrpBmap = _VrrpNewCfgVirtRtrVrGrpBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1, 7),
    _VrrpNewCfgVirtRtrVrGrpBmap_Type()
)
vrrpNewCfgVirtRtrVrGrpBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpBmap.setStatus("current")


class _VrrpNewCfgVirtRtrVrGrpPriority_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrVrGrpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VrrpNewCfgVirtRtrVrGrpPriority_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrVrGrpPriority_Object = MibTableColumn
vrrpNewCfgVirtRtrVrGrpPriority = _VrrpNewCfgVirtRtrVrGrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1, 8),
    _VrrpNewCfgVirtRtrVrGrpPriority_Type()
)
vrrpNewCfgVirtRtrVrGrpPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpPriority.setStatus("current")


class _VrrpNewCfgVirtRtrVrGrpTckIpIntf_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrVrGrpTckIpIntf based on Integer32"""
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


_VrrpNewCfgVirtRtrVrGrpTckIpIntf_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrVrGrpTckIpIntf_Object = MibTableColumn
vrrpNewCfgVirtRtrVrGrpTckIpIntf = _VrrpNewCfgVirtRtrVrGrpTckIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1, 9),
    _VrrpNewCfgVirtRtrVrGrpTckIpIntf_Type()
)
vrrpNewCfgVirtRtrVrGrpTckIpIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpTckIpIntf.setStatus("current")


class _VrrpNewCfgVirtRtrVrGrpTckVlanPort_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrVrGrpTckVlanPort based on Integer32"""
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


_VrrpNewCfgVirtRtrVrGrpTckVlanPort_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrVrGrpTckVlanPort_Object = MibTableColumn
vrrpNewCfgVirtRtrVrGrpTckVlanPort = _VrrpNewCfgVirtRtrVrGrpTckVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1, 10),
    _VrrpNewCfgVirtRtrVrGrpTckVlanPort_Type()
)
vrrpNewCfgVirtRtrVrGrpTckVlanPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpTckVlanPort.setStatus("current")


class _VrrpNewCfgVirtRtrVrGrpTckL4Port_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrVrGrpTckL4Port based on Integer32"""
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


_VrrpNewCfgVirtRtrVrGrpTckL4Port_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrVrGrpTckL4Port_Object = MibTableColumn
vrrpNewCfgVirtRtrVrGrpTckL4Port = _VrrpNewCfgVirtRtrVrGrpTckL4Port_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1, 11),
    _VrrpNewCfgVirtRtrVrGrpTckL4Port_Type()
)
vrrpNewCfgVirtRtrVrGrpTckL4Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpTckL4Port.setStatus("current")


class _VrrpNewCfgVirtRtrVrGrpTckRServer_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrVrGrpTckRServer based on Integer32"""
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


_VrrpNewCfgVirtRtrVrGrpTckRServer_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrVrGrpTckRServer_Object = MibTableColumn
vrrpNewCfgVirtRtrVrGrpTckRServer = _VrrpNewCfgVirtRtrVrGrpTckRServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1, 12),
    _VrrpNewCfgVirtRtrVrGrpTckRServer_Type()
)
vrrpNewCfgVirtRtrVrGrpTckRServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpTckRServer.setStatus("current")


class _VrrpNewCfgVirtRtrVrGrpTckHsrp_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrVrGrpTckHsrp based on Integer32"""
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


_VrrpNewCfgVirtRtrVrGrpTckHsrp_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrVrGrpTckHsrp_Object = MibTableColumn
vrrpNewCfgVirtRtrVrGrpTckHsrp = _VrrpNewCfgVirtRtrVrGrpTckHsrp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1, 13),
    _VrrpNewCfgVirtRtrVrGrpTckHsrp_Type()
)
vrrpNewCfgVirtRtrVrGrpTckHsrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpTckHsrp.setStatus("current")


class _VrrpNewCfgVirtRtrVrGrpTckHsrv_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrVrGrpTckHsrv based on Integer32"""
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


_VrrpNewCfgVirtRtrVrGrpTckHsrv_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrVrGrpTckHsrv_Object = MibTableColumn
vrrpNewCfgVirtRtrVrGrpTckHsrv = _VrrpNewCfgVirtRtrVrGrpTckHsrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1, 14),
    _VrrpNewCfgVirtRtrVrGrpTckHsrv_Type()
)
vrrpNewCfgVirtRtrVrGrpTckHsrv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpTckHsrv.setStatus("current")


class _VrrpNewCfgVirtRtrVrGrpTckVirtRtrNo_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrVrGrpTckVirtRtrNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_VrrpNewCfgVirtRtrVrGrpTckVirtRtrNo_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrVrGrpTckVirtRtrNo_Object = MibTableColumn
vrrpNewCfgVirtRtrVrGrpTckVirtRtrNo = _VrrpNewCfgVirtRtrVrGrpTckVirtRtrNo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1, 15),
    _VrrpNewCfgVirtRtrVrGrpTckVirtRtrNo_Type()
)
vrrpNewCfgVirtRtrVrGrpTckVirtRtrNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpTckVirtRtrNo.setStatus("current")


class _VrrpNewCfgVirtRtrVrGrpAdverInterval_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrVrGrpAdverInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpNewCfgVirtRtrVrGrpAdverInterval_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrVrGrpAdverInterval_Object = MibTableColumn
vrrpNewCfgVirtRtrVrGrpAdverInterval = _VrrpNewCfgVirtRtrVrGrpAdverInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1, 16),
    _VrrpNewCfgVirtRtrVrGrpAdverInterval_Type()
)
vrrpNewCfgVirtRtrVrGrpAdverInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpAdverInterval.setStatus("current")


class _VrrpNewCfgVirtRtrVrGrpPreemption_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrVrGrpPreemption based on Integer32"""
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


_VrrpNewCfgVirtRtrVrGrpPreemption_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrVrGrpPreemption_Object = MibTableColumn
vrrpNewCfgVirtRtrVrGrpPreemption = _VrrpNewCfgVirtRtrVrGrpPreemption_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1, 17),
    _VrrpNewCfgVirtRtrVrGrpPreemption_Type()
)
vrrpNewCfgVirtRtrVrGrpPreemption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpPreemption.setStatus("current")


class _VrrpNewCfgVirtRtrVrGrpSharing_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrVrGrpSharing based on Integer32"""
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


_VrrpNewCfgVirtRtrVrGrpSharing_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrVrGrpSharing_Object = MibTableColumn
vrrpNewCfgVirtRtrVrGrpSharing = _VrrpNewCfgVirtRtrVrGrpSharing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 6, 13, 1, 18),
    _VrrpNewCfgVirtRtrVrGrpSharing_Type()
)
vrrpNewCfgVirtRtrVrGrpSharing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrVrGrpSharing.setStatus("current")
_ArpCfg_ObjectIdentity = ObjectIdentity
arpCfg = _ArpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 7)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 7, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 7, 2),
    _ArpNewCfgReARPPeriod_Type()
)
arpNewCfgReARPPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpNewCfgReARPPeriod.setStatus("current")
_IpBootpCfg_ObjectIdentity = ObjectIdentity
ipBootpCfg = _IpBootpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 8)
)
_IpCurCfgBootpAddr_Type = IpAddress
_IpCurCfgBootpAddr_Object = MibScalar
ipCurCfgBootpAddr = _IpCurCfgBootpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 8, 1),
    _IpCurCfgBootpAddr_Type()
)
ipCurCfgBootpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgBootpAddr.setStatus("current")
_IpNewCfgBootpAddr_Type = IpAddress
_IpNewCfgBootpAddr_Object = MibScalar
ipNewCfgBootpAddr = _IpNewCfgBootpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 8, 2),
    _IpNewCfgBootpAddr_Type()
)
ipNewCfgBootpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgBootpAddr.setStatus("current")
_IpCurCfgBootpAddr2_Type = IpAddress
_IpCurCfgBootpAddr2_Object = MibScalar
ipCurCfgBootpAddr2 = _IpCurCfgBootpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 8, 3),
    _IpCurCfgBootpAddr2_Type()
)
ipCurCfgBootpAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgBootpAddr2.setStatus("current")
_IpNewCfgBootpAddr2_Type = IpAddress
_IpNewCfgBootpAddr2_Object = MibScalar
ipNewCfgBootpAddr2 = _IpNewCfgBootpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 8, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 8, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 8, 6),
    _IpNewCfgBootpState_Type()
)
ipNewCfgBootpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgBootpState.setStatus("current")
_DnsCfg_ObjectIdentity = ObjectIdentity
dnsCfg = _DnsCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 9)
)
_DnsCurCfgPrimaryIpAddr_Type = IpAddress
_DnsCurCfgPrimaryIpAddr_Object = MibScalar
dnsCurCfgPrimaryIpAddr = _DnsCurCfgPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 9, 1),
    _DnsCurCfgPrimaryIpAddr_Type()
)
dnsCurCfgPrimaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurCfgPrimaryIpAddr.setStatus("current")
_DnsNewCfgPrimaryIpAddr_Type = IpAddress
_DnsNewCfgPrimaryIpAddr_Object = MibScalar
dnsNewCfgPrimaryIpAddr = _DnsNewCfgPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 9, 2),
    _DnsNewCfgPrimaryIpAddr_Type()
)
dnsNewCfgPrimaryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsNewCfgPrimaryIpAddr.setStatus("current")
_DnsCurCfgSecondaryIpAddr_Type = IpAddress
_DnsCurCfgSecondaryIpAddr_Object = MibScalar
dnsCurCfgSecondaryIpAddr = _DnsCurCfgSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 9, 3),
    _DnsCurCfgSecondaryIpAddr_Type()
)
dnsCurCfgSecondaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurCfgSecondaryIpAddr.setStatus("current")
_DnsNewCfgSecondaryIpAddr_Type = IpAddress
_DnsNewCfgSecondaryIpAddr_Object = MibScalar
dnsNewCfgSecondaryIpAddr = _DnsNewCfgSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 9, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 9, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 9, 6),
    _DnsNewCfgDomainName_Type()
)
dnsNewCfgDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsNewCfgDomainName.setStatus("current")


class _DnsCurCfgPrimaryIpv6Addr_Type(DisplayString):
    """Custom type dnsCurCfgPrimaryIpv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DnsCurCfgPrimaryIpv6Addr_Type.__name__ = "DisplayString"
_DnsCurCfgPrimaryIpv6Addr_Object = MibScalar
dnsCurCfgPrimaryIpv6Addr = _DnsCurCfgPrimaryIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 9, 7),
    _DnsCurCfgPrimaryIpv6Addr_Type()
)
dnsCurCfgPrimaryIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurCfgPrimaryIpv6Addr.setStatus("current")


class _DnsNewCfgPrimaryIpv6Addr_Type(DisplayString):
    """Custom type dnsNewCfgPrimaryIpv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DnsNewCfgPrimaryIpv6Addr_Type.__name__ = "DisplayString"
_DnsNewCfgPrimaryIpv6Addr_Object = MibScalar
dnsNewCfgPrimaryIpv6Addr = _DnsNewCfgPrimaryIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 9, 8),
    _DnsNewCfgPrimaryIpv6Addr_Type()
)
dnsNewCfgPrimaryIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsNewCfgPrimaryIpv6Addr.setStatus("current")


class _DnsCurCfgSecondaryIpv6Addr_Type(DisplayString):
    """Custom type dnsCurCfgSecondaryIpv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DnsCurCfgSecondaryIpv6Addr_Type.__name__ = "DisplayString"
_DnsCurCfgSecondaryIpv6Addr_Object = MibScalar
dnsCurCfgSecondaryIpv6Addr = _DnsCurCfgSecondaryIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 9, 9),
    _DnsCurCfgSecondaryIpv6Addr_Type()
)
dnsCurCfgSecondaryIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurCfgSecondaryIpv6Addr.setStatus("current")


class _DnsNewCfgSecondaryIpv6Addr_Type(DisplayString):
    """Custom type dnsNewCfgSecondaryIpv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DnsNewCfgSecondaryIpv6Addr_Type.__name__ = "DisplayString"
_DnsNewCfgSecondaryIpv6Addr_Object = MibScalar
dnsNewCfgSecondaryIpv6Addr = _DnsNewCfgSecondaryIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 9, 10),
    _DnsNewCfgSecondaryIpv6Addr_Type()
)
dnsNewCfgSecondaryIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsNewCfgSecondaryIpv6Addr.setStatus("current")
_IpNwfCfg_ObjectIdentity = ObjectIdentity
ipNwfCfg = _IpNwfCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 10)
)
_IpNwfTableMax_Type = Integer32
_IpNwfTableMax_Object = MibScalar
ipNwfTableMax = _IpNwfTableMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 10, 1),
    _IpNwfTableMax_Type()
)
ipNwfTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNwfTableMax.setStatus("current")
_IpCurCfgNwfTable_Object = MibTable
ipCurCfgNwfTable = _IpCurCfgNwfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 10, 2)
)
if mibBuilder.loadTexts:
    ipCurCfgNwfTable.setStatus("current")
_IpCurCfgNwfEntry_Object = MibTableRow
ipCurCfgNwfEntry = _IpCurCfgNwfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 10, 2, 1)
)
ipCurCfgNwfEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgNwfIndex"),
)
if mibBuilder.loadTexts:
    ipCurCfgNwfEntry.setStatus("current")
_IpCurCfgNwfIndex_Type = Integer32
_IpCurCfgNwfIndex_Object = MibTableColumn
ipCurCfgNwfIndex = _IpCurCfgNwfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 10, 2, 1, 1),
    _IpCurCfgNwfIndex_Type()
)
ipCurCfgNwfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgNwfIndex.setStatus("current")
_IpCurCfgNwfAddr_Type = IpAddress
_IpCurCfgNwfAddr_Object = MibTableColumn
ipCurCfgNwfAddr = _IpCurCfgNwfAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 10, 2, 1, 2),
    _IpCurCfgNwfAddr_Type()
)
ipCurCfgNwfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgNwfAddr.setStatus("current")
_IpCurCfgNwfMask_Type = IpAddress
_IpCurCfgNwfMask_Object = MibTableColumn
ipCurCfgNwfMask = _IpCurCfgNwfMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 10, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 10, 2, 1, 4),
    _IpCurCfgNwfState_Type()
)
ipCurCfgNwfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgNwfState.setStatus("current")
_IpNewCfgNwfTable_Object = MibTable
ipNewCfgNwfTable = _IpNewCfgNwfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 10, 3)
)
if mibBuilder.loadTexts:
    ipNewCfgNwfTable.setStatus("current")
_IpNewCfgNwfEntry_Object = MibTableRow
ipNewCfgNwfEntry = _IpNewCfgNwfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 10, 3, 1)
)
ipNewCfgNwfEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipNewCfgNwfIndex"),
)
if mibBuilder.loadTexts:
    ipNewCfgNwfEntry.setStatus("current")
_IpNewCfgNwfIndex_Type = Integer32
_IpNewCfgNwfIndex_Object = MibTableColumn
ipNewCfgNwfIndex = _IpNewCfgNwfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 10, 3, 1, 1),
    _IpNewCfgNwfIndex_Type()
)
ipNewCfgNwfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgNwfIndex.setStatus("current")
_IpNewCfgNwfAddr_Type = IpAddress
_IpNewCfgNwfAddr_Object = MibTableColumn
ipNewCfgNwfAddr = _IpNewCfgNwfAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 10, 3, 1, 2),
    _IpNewCfgNwfAddr_Type()
)
ipNewCfgNwfAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgNwfAddr.setStatus("current")
_IpNewCfgNwfMask_Type = IpAddress
_IpNewCfgNwfMask_Object = MibTableColumn
ipNewCfgNwfMask = _IpNewCfgNwfMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 10, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 10, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 10, 3, 1, 5),
    _IpNewCfgNwfDelete_Type()
)
ipNewCfgNwfDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgNwfDelete.setStatus("current")
_IpRmapCfg_ObjectIdentity = ObjectIdentity
ipRmapCfg = _IpRmapCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11)
)
_IpRmapTableMax_Type = Integer32
_IpRmapTableMax_Object = MibScalar
ipRmapTableMax = _IpRmapTableMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 1),
    _IpRmapTableMax_Type()
)
ipRmapTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRmapTableMax.setStatus("current")
_IpCurCfgRmapTable_Object = MibTable
ipCurCfgRmapTable = _IpCurCfgRmapTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 2)
)
if mibBuilder.loadTexts:
    ipCurCfgRmapTable.setStatus("current")
_IpCurCfgRmapEntry_Object = MibTableRow
ipCurCfgRmapEntry = _IpCurCfgRmapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 2, 1)
)
ipCurCfgRmapEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgRmapIndex"),
)
if mibBuilder.loadTexts:
    ipCurCfgRmapEntry.setStatus("current")
_IpCurCfgRmapIndex_Type = Integer32
_IpCurCfgRmapIndex_Object = MibTableColumn
ipCurCfgRmapIndex = _IpCurCfgRmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 2, 1, 8),
    _IpCurCfgRmapMetricType_Type()
)
ipCurCfgRmapMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgRmapMetricType.setStatus("current")
_IpNewCfgRmapTable_Object = MibTable
ipNewCfgRmapTable = _IpNewCfgRmapTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 3)
)
if mibBuilder.loadTexts:
    ipNewCfgRmapTable.setStatus("current")
_IpNewCfgRmapEntry_Object = MibTableRow
ipNewCfgRmapEntry = _IpNewCfgRmapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 3, 1)
)
ipNewCfgRmapEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipNewCfgRmapIndex"),
)
if mibBuilder.loadTexts:
    ipNewCfgRmapEntry.setStatus("current")
_IpNewCfgRmapIndex_Type = Integer32
_IpNewCfgRmapIndex_Object = MibTableColumn
ipNewCfgRmapIndex = _IpNewCfgRmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 3, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 3, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 3, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 3, 1, 9),
    _IpNewCfgRmapDelete_Type()
)
ipNewCfgRmapDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgRmapDelete.setStatus("current")
_IpAlistTableMax_Type = Integer32
_IpAlistTableMax_Object = MibScalar
ipAlistTableMax = _IpAlistTableMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 4),
    _IpAlistTableMax_Type()
)
ipAlistTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAlistTableMax.setStatus("current")
_IpCurCfgAlistTable_Object = MibTable
ipCurCfgAlistTable = _IpCurCfgAlistTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 5)
)
if mibBuilder.loadTexts:
    ipCurCfgAlistTable.setStatus("current")
_IpCurCfgAlistEntry_Object = MibTableRow
ipCurCfgAlistEntry = _IpCurCfgAlistEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 5, 1)
)
ipCurCfgAlistEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgAlistRmapIndex"),
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgAlistIndex"),
)
if mibBuilder.loadTexts:
    ipCurCfgAlistEntry.setStatus("current")
_IpCurCfgAlistRmapIndex_Type = Integer32
_IpCurCfgAlistRmapIndex_Object = MibTableColumn
ipCurCfgAlistRmapIndex = _IpCurCfgAlistRmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 5, 1, 1),
    _IpCurCfgAlistRmapIndex_Type()
)
ipCurCfgAlistRmapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgAlistRmapIndex.setStatus("current")
_IpCurCfgAlistIndex_Type = Integer32
_IpCurCfgAlistIndex_Object = MibTableColumn
ipCurCfgAlistIndex = _IpCurCfgAlistIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 5, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 5, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 5, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 5, 1, 6),
    _IpCurCfgAlistState_Type()
)
ipCurCfgAlistState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgAlistState.setStatus("current")
_IpNewCfgAlistTable_Object = MibTable
ipNewCfgAlistTable = _IpNewCfgAlistTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 6)
)
if mibBuilder.loadTexts:
    ipNewCfgAlistTable.setStatus("current")
_IpNewCfgAlistEntry_Object = MibTableRow
ipNewCfgAlistEntry = _IpNewCfgAlistEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 6, 1)
)
ipNewCfgAlistEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipNewCfgAlistRmapIndex"),
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipNewCfgAlistIndex"),
)
if mibBuilder.loadTexts:
    ipNewCfgAlistEntry.setStatus("current")
_IpNewCfgAlistRmapIndex_Type = Integer32
_IpNewCfgAlistRmapIndex_Object = MibTableColumn
ipNewCfgAlistRmapIndex = _IpNewCfgAlistRmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 6, 1, 1),
    _IpNewCfgAlistRmapIndex_Type()
)
ipNewCfgAlistRmapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgAlistRmapIndex.setStatus("current")
_IpNewCfgAlistIndex_Type = Integer32
_IpNewCfgAlistIndex_Object = MibTableColumn
ipNewCfgAlistIndex = _IpNewCfgAlistIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 6, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 6, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 6, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 6, 1, 7),
    _IpNewCfgAlistDelete_Type()
)
ipNewCfgAlistDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgAlistDelete.setStatus("current")
_IpAspathTableMax_Type = Integer32
_IpAspathTableMax_Object = MibScalar
ipAspathTableMax = _IpAspathTableMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 7),
    _IpAspathTableMax_Type()
)
ipAspathTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAspathTableMax.setStatus("current")
_IpCurCfgAspathTable_Object = MibTable
ipCurCfgAspathTable = _IpCurCfgAspathTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 8)
)
if mibBuilder.loadTexts:
    ipCurCfgAspathTable.setStatus("current")
_IpCurCfgAspathEntry_Object = MibTableRow
ipCurCfgAspathEntry = _IpCurCfgAspathEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 8, 1)
)
ipCurCfgAspathEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgAspathRmapIndex"),
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgAlistIndex"),
)
if mibBuilder.loadTexts:
    ipCurCfgAspathEntry.setStatus("current")
_IpCurCfgAspathRmapIndex_Type = Integer32
_IpCurCfgAspathRmapIndex_Object = MibTableColumn
ipCurCfgAspathRmapIndex = _IpCurCfgAspathRmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 8, 1, 1),
    _IpCurCfgAspathRmapIndex_Type()
)
ipCurCfgAspathRmapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgAspathRmapIndex.setStatus("current")
_IpCurCfgAspathIndex_Type = Integer32
_IpCurCfgAspathIndex_Object = MibTableColumn
ipCurCfgAspathIndex = _IpCurCfgAspathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 8, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 8, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 8, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 8, 1, 5),
    _IpCurCfgAspathState_Type()
)
ipCurCfgAspathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgAspathState.setStatus("current")
_IpNewCfgAspathTable_Object = MibTable
ipNewCfgAspathTable = _IpNewCfgAspathTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 9)
)
if mibBuilder.loadTexts:
    ipNewCfgAspathTable.setStatus("current")
_IpNewCfgAspathEntry_Object = MibTableRow
ipNewCfgAspathEntry = _IpNewCfgAspathEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 9, 1)
)
ipNewCfgAspathEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipNewCfgAspathRmapIndex"),
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipNewCfgAspathIndex"),
)
if mibBuilder.loadTexts:
    ipNewCfgAspathEntry.setStatus("current")
_IpNewCfgAspathRmapIndex_Type = Integer32
_IpNewCfgAspathRmapIndex_Object = MibTableColumn
ipNewCfgAspathRmapIndex = _IpNewCfgAspathRmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 9, 1, 1),
    _IpNewCfgAspathRmapIndex_Type()
)
ipNewCfgAspathRmapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgAspathRmapIndex.setStatus("current")
_IpNewCfgAspathIndex_Type = Integer32
_IpNewCfgAspathIndex_Object = MibTableColumn
ipNewCfgAspathIndex = _IpNewCfgAspathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 9, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 9, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 9, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 9, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 11, 9, 1, 6),
    _IpNewCfgAspathDelete_Type()
)
ipNewCfgAspathDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgAspathDelete.setStatus("current")
_BgpCfg_ObjectIdentity = ObjectIdentity
bgpCfg = _BgpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12)
)
_BgpGeneral_ObjectIdentity = ObjectIdentity
bgpGeneral = _BgpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 1)
)


class _BgpCurCfgState_Type(Integer32):
    """Custom type bgpCurCfgState based on Integer32"""
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


_BgpCurCfgState_Type.__name__ = "Integer32"
_BgpCurCfgState_Object = MibScalar
bgpCurCfgState = _BgpCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 1, 1),
    _BgpCurCfgState_Type()
)
bgpCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgState.setStatus("current")


class _BgpNewCfgState_Type(Integer32):
    """Custom type bgpNewCfgState based on Integer32"""
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


_BgpNewCfgState_Type.__name__ = "Integer32"
_BgpNewCfgState_Object = MibScalar
bgpNewCfgState = _BgpNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 1, 2),
    _BgpNewCfgState_Type()
)
bgpNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bgpNewCfgState.setStatus("current")


class _BgpCurCfgLocalPref_Type(Unsigned32):
    """Custom type bgpCurCfgLocalPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_BgpCurCfgLocalPref_Type.__name__ = "Unsigned32"
_BgpCurCfgLocalPref_Object = MibScalar
bgpCurCfgLocalPref = _BgpCurCfgLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 1, 3),
    _BgpCurCfgLocalPref_Type()
)
bgpCurCfgLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgLocalPref.setStatus("current")


class _BgpNewCfgLocalPref_Type(Unsigned32):
    """Custom type bgpNewCfgLocalPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_BgpNewCfgLocalPref_Type.__name__ = "Unsigned32"
_BgpNewCfgLocalPref_Object = MibScalar
bgpNewCfgLocalPref = _BgpNewCfgLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 1, 4),
    _BgpNewCfgLocalPref_Type()
)
bgpNewCfgLocalPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bgpNewCfgLocalPref.setStatus("current")


class _BgpCurCfgMaxASPath_Type(Unsigned32):
    """Custom type bgpCurCfgMaxASPath based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_BgpCurCfgMaxASPath_Type.__name__ = "Unsigned32"
_BgpCurCfgMaxASPath_Object = MibScalar
bgpCurCfgMaxASPath = _BgpCurCfgMaxASPath_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 1, 5),
    _BgpCurCfgMaxASPath_Type()
)
bgpCurCfgMaxASPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgMaxASPath.setStatus("current")


class _BgpNewCfgMaxASPath_Type(Unsigned32):
    """Custom type bgpNewCfgMaxASPath based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_BgpNewCfgMaxASPath_Type.__name__ = "Unsigned32"
_BgpNewCfgMaxASPath_Object = MibScalar
bgpNewCfgMaxASPath = _BgpNewCfgMaxASPath_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 1, 6),
    _BgpNewCfgMaxASPath_Type()
)
bgpNewCfgMaxASPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bgpNewCfgMaxASPath.setStatus("current")


class _BgpCurCfgASNumber_Type(Unsigned32):
    """Custom type bgpCurCfgASNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BgpCurCfgASNumber_Type.__name__ = "Unsigned32"
_BgpCurCfgASNumber_Object = MibScalar
bgpCurCfgASNumber = _BgpCurCfgASNumber_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 1, 7),
    _BgpCurCfgASNumber_Type()
)
bgpCurCfgASNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgASNumber.setStatus("current")


class _BgpNewCfgASNumber_Type(Unsigned32):
    """Custom type bgpNewCfgASNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BgpNewCfgASNumber_Type.__name__ = "Unsigned32"
_BgpNewCfgASNumber_Object = MibScalar
bgpNewCfgASNumber = _BgpNewCfgASNumber_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 1, 8),
    _BgpNewCfgASNumber_Type()
)
bgpNewCfgASNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bgpNewCfgASNumber.setStatus("current")
_BgpPeerTableMax_Type = Integer32
_BgpPeerTableMax_Object = MibScalar
bgpPeerTableMax = _BgpPeerTableMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 2),
    _BgpPeerTableMax_Type()
)
bgpPeerTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerTableMax.setStatus("current")
_BgpCurCfgPeerTable_Object = MibTable
bgpCurCfgPeerTable = _BgpCurCfgPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3)
)
if mibBuilder.loadTexts:
    bgpCurCfgPeerTable.setStatus("current")
_BgpCurCfgPeerEntry_Object = MibTableRow
bgpCurCfgPeerEntry = _BgpCurCfgPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1)
)
bgpCurCfgPeerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "bgpCurCfgPeerIndex"),
)
if mibBuilder.loadTexts:
    bgpCurCfgPeerEntry.setStatus("current")
_BgpCurCfgPeerIndex_Type = Integer32
_BgpCurCfgPeerIndex_Object = MibTableColumn
bgpCurCfgPeerIndex = _BgpCurCfgPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 1),
    _BgpCurCfgPeerIndex_Type()
)
bgpCurCfgPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerIndex.setStatus("current")
_BgpCurCfgPeerRemoteAddr_Type = IpAddress
_BgpCurCfgPeerRemoteAddr_Object = MibTableColumn
bgpCurCfgPeerRemoteAddr = _BgpCurCfgPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 2),
    _BgpCurCfgPeerRemoteAddr_Type()
)
bgpCurCfgPeerRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerRemoteAddr.setStatus("current")


class _BgpCurCfgPeerRemoteAs_Type(Integer32):
    """Custom type bgpCurCfgPeerRemoteAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BgpCurCfgPeerRemoteAs_Type.__name__ = "Integer32"
_BgpCurCfgPeerRemoteAs_Object = MibTableColumn
bgpCurCfgPeerRemoteAs = _BgpCurCfgPeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 3),
    _BgpCurCfgPeerRemoteAs_Type()
)
bgpCurCfgPeerRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerRemoteAs.setStatus("current")


class _BgpCurCfgPeerTtl_Type(Integer32):
    """Custom type bgpCurCfgPeerTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BgpCurCfgPeerTtl_Type.__name__ = "Integer32"
_BgpCurCfgPeerTtl_Object = MibTableColumn
bgpCurCfgPeerTtl = _BgpCurCfgPeerTtl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 4),
    _BgpCurCfgPeerTtl_Type()
)
bgpCurCfgPeerTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerTtl.setStatus("current")


class _BgpCurCfgPeerState_Type(Integer32):
    """Custom type bgpCurCfgPeerState based on Integer32"""
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


_BgpCurCfgPeerState_Type.__name__ = "Integer32"
_BgpCurCfgPeerState_Object = MibTableColumn
bgpCurCfgPeerState = _BgpCurCfgPeerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 5),
    _BgpCurCfgPeerState_Type()
)
bgpCurCfgPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerState.setStatus("current")


class _BgpCurCfgPeerMetric_Type(Unsigned32):
    """Custom type bgpCurCfgPeerMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_BgpCurCfgPeerMetric_Type.__name__ = "Unsigned32"
_BgpCurCfgPeerMetric_Object = MibTableColumn
bgpCurCfgPeerMetric = _BgpCurCfgPeerMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 10),
    _BgpCurCfgPeerMetric_Type()
)
bgpCurCfgPeerMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerMetric.setStatus("current")


class _BgpCurCfgPeerDefaultAction_Type(Integer32):
    """Custom type bgpCurCfgPeerDefaultAction based on Integer32"""
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
        *(("import", 2),
          ("none", 1),
          ("originate", 3),
          ("redistribute", 4))
    )


_BgpCurCfgPeerDefaultAction_Type.__name__ = "Integer32"
_BgpCurCfgPeerDefaultAction_Object = MibTableColumn
bgpCurCfgPeerDefaultAction = _BgpCurCfgPeerDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 11),
    _BgpCurCfgPeerDefaultAction_Type()
)
bgpCurCfgPeerDefaultAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerDefaultAction.setStatus("current")


class _BgpCurCfgPeerOspfState_Type(Integer32):
    """Custom type bgpCurCfgPeerOspfState based on Integer32"""
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


_BgpCurCfgPeerOspfState_Type.__name__ = "Integer32"
_BgpCurCfgPeerOspfState_Object = MibTableColumn
bgpCurCfgPeerOspfState = _BgpCurCfgPeerOspfState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 12),
    _BgpCurCfgPeerOspfState_Type()
)
bgpCurCfgPeerOspfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerOspfState.setStatus("current")


class _BgpCurCfgPeerFixedState_Type(Integer32):
    """Custom type bgpCurCfgPeerFixedState based on Integer32"""
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


_BgpCurCfgPeerFixedState_Type.__name__ = "Integer32"
_BgpCurCfgPeerFixedState_Object = MibTableColumn
bgpCurCfgPeerFixedState = _BgpCurCfgPeerFixedState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 13),
    _BgpCurCfgPeerFixedState_Type()
)
bgpCurCfgPeerFixedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerFixedState.setStatus("current")


class _BgpCurCfgPeerStaticState_Type(Integer32):
    """Custom type bgpCurCfgPeerStaticState based on Integer32"""
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


_BgpCurCfgPeerStaticState_Type.__name__ = "Integer32"
_BgpCurCfgPeerStaticState_Object = MibTableColumn
bgpCurCfgPeerStaticState = _BgpCurCfgPeerStaticState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 14),
    _BgpCurCfgPeerStaticState_Type()
)
bgpCurCfgPeerStaticState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerStaticState.setStatus("current")


class _BgpCurCfgPeerVipState_Type(Integer32):
    """Custom type bgpCurCfgPeerVipState based on Integer32"""
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


_BgpCurCfgPeerVipState_Type.__name__ = "Integer32"
_BgpCurCfgPeerVipState_Object = MibTableColumn
bgpCurCfgPeerVipState = _BgpCurCfgPeerVipState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 15),
    _BgpCurCfgPeerVipState_Type()
)
bgpCurCfgPeerVipState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerVipState.setStatus("current")
_BgpCurCfgPeerInRmapList_Type = OctetString
_BgpCurCfgPeerInRmapList_Object = MibTableColumn
bgpCurCfgPeerInRmapList = _BgpCurCfgPeerInRmapList_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 16),
    _BgpCurCfgPeerInRmapList_Type()
)
bgpCurCfgPeerInRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerInRmapList.setStatus("current")
_BgpCurCfgPeerOutRmapList_Type = OctetString
_BgpCurCfgPeerOutRmapList_Object = MibTableColumn
bgpCurCfgPeerOutRmapList = _BgpCurCfgPeerOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 17),
    _BgpCurCfgPeerOutRmapList_Type()
)
bgpCurCfgPeerOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerOutRmapList.setStatus("current")


class _BgpCurCfgPeerHoldTime_Type(Integer32):
    """Custom type bgpCurCfgPeerHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BgpCurCfgPeerHoldTime_Type.__name__ = "Integer32"
_BgpCurCfgPeerHoldTime_Object = MibTableColumn
bgpCurCfgPeerHoldTime = _BgpCurCfgPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 18),
    _BgpCurCfgPeerHoldTime_Type()
)
bgpCurCfgPeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerHoldTime.setStatus("current")


class _BgpCurCfgPeerKeepAlive_Type(Integer32):
    """Custom type bgpCurCfgPeerKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 21845),
    )


_BgpCurCfgPeerKeepAlive_Type.__name__ = "Integer32"
_BgpCurCfgPeerKeepAlive_Object = MibTableColumn
bgpCurCfgPeerKeepAlive = _BgpCurCfgPeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 19),
    _BgpCurCfgPeerKeepAlive_Type()
)
bgpCurCfgPeerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerKeepAlive.setStatus("current")


class _BgpCurCfgPeerMinTime_Type(Integer32):
    """Custom type bgpCurCfgPeerMinTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BgpCurCfgPeerMinTime_Type.__name__ = "Integer32"
_BgpCurCfgPeerMinTime_Object = MibTableColumn
bgpCurCfgPeerMinTime = _BgpCurCfgPeerMinTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 20),
    _BgpCurCfgPeerMinTime_Type()
)
bgpCurCfgPeerMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerMinTime.setStatus("current")


class _BgpCurCfgPeerConRetry_Type(Integer32):
    """Custom type bgpCurCfgPeerConRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BgpCurCfgPeerConRetry_Type.__name__ = "Integer32"
_BgpCurCfgPeerConRetry_Object = MibTableColumn
bgpCurCfgPeerConRetry = _BgpCurCfgPeerConRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 21),
    _BgpCurCfgPeerConRetry_Type()
)
bgpCurCfgPeerConRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerConRetry.setStatus("current")


class _BgpCurCfgPeerMinAS_Type(Integer32):
    """Custom type bgpCurCfgPeerMinAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 65535),
    )


_BgpCurCfgPeerMinAS_Type.__name__ = "Integer32"
_BgpCurCfgPeerMinAS_Object = MibTableColumn
bgpCurCfgPeerMinAS = _BgpCurCfgPeerMinAS_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 22),
    _BgpCurCfgPeerMinAS_Type()
)
bgpCurCfgPeerMinAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerMinAS.setStatus("current")


class _BgpCurCfgPeerRipState_Type(Integer32):
    """Custom type bgpCurCfgPeerRipState based on Integer32"""
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


_BgpCurCfgPeerRipState_Type.__name__ = "Integer32"
_BgpCurCfgPeerRipState_Object = MibTableColumn
bgpCurCfgPeerRipState = _BgpCurCfgPeerRipState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 3, 1, 23),
    _BgpCurCfgPeerRipState_Type()
)
bgpCurCfgPeerRipState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgPeerRipState.setStatus("current")
_BgpNewCfgPeerTable_Object = MibTable
bgpNewCfgPeerTable = _BgpNewCfgPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4)
)
if mibBuilder.loadTexts:
    bgpNewCfgPeerTable.setStatus("current")
_BgpNewCfgPeerEntry_Object = MibTableRow
bgpNewCfgPeerEntry = _BgpNewCfgPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1)
)
bgpNewCfgPeerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "bgpNewCfgPeerIndex"),
)
if mibBuilder.loadTexts:
    bgpNewCfgPeerEntry.setStatus("current")
_BgpNewCfgPeerIndex_Type = Integer32
_BgpNewCfgPeerIndex_Object = MibTableColumn
bgpNewCfgPeerIndex = _BgpNewCfgPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 1),
    _BgpNewCfgPeerIndex_Type()
)
bgpNewCfgPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNewCfgPeerIndex.setStatus("current")
_BgpNewCfgPeerRemoteAddr_Type = IpAddress
_BgpNewCfgPeerRemoteAddr_Object = MibTableColumn
bgpNewCfgPeerRemoteAddr = _BgpNewCfgPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 2),
    _BgpNewCfgPeerRemoteAddr_Type()
)
bgpNewCfgPeerRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerRemoteAddr.setStatus("current")


class _BgpNewCfgPeerRemoteAs_Type(Integer32):
    """Custom type bgpNewCfgPeerRemoteAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BgpNewCfgPeerRemoteAs_Type.__name__ = "Integer32"
_BgpNewCfgPeerRemoteAs_Object = MibTableColumn
bgpNewCfgPeerRemoteAs = _BgpNewCfgPeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 3),
    _BgpNewCfgPeerRemoteAs_Type()
)
bgpNewCfgPeerRemoteAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerRemoteAs.setStatus("current")


class _BgpNewCfgPeerTtl_Type(Integer32):
    """Custom type bgpNewCfgPeerTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BgpNewCfgPeerTtl_Type.__name__ = "Integer32"
_BgpNewCfgPeerTtl_Object = MibTableColumn
bgpNewCfgPeerTtl = _BgpNewCfgPeerTtl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 4),
    _BgpNewCfgPeerTtl_Type()
)
bgpNewCfgPeerTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerTtl.setStatus("current")


class _BgpNewCfgPeerState_Type(Integer32):
    """Custom type bgpNewCfgPeerState based on Integer32"""
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


_BgpNewCfgPeerState_Type.__name__ = "Integer32"
_BgpNewCfgPeerState_Object = MibTableColumn
bgpNewCfgPeerState = _BgpNewCfgPeerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 5),
    _BgpNewCfgPeerState_Type()
)
bgpNewCfgPeerState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerState.setStatus("current")


class _BgpNewCfgPeerDelete_Type(Integer32):
    """Custom type bgpNewCfgPeerDelete based on Integer32"""
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


_BgpNewCfgPeerDelete_Type.__name__ = "Integer32"
_BgpNewCfgPeerDelete_Object = MibTableColumn
bgpNewCfgPeerDelete = _BgpNewCfgPeerDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 6),
    _BgpNewCfgPeerDelete_Type()
)
bgpNewCfgPeerDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerDelete.setStatus("current")


class _BgpNewCfgPeerMetric_Type(Unsigned32):
    """Custom type bgpNewCfgPeerMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_BgpNewCfgPeerMetric_Type.__name__ = "Unsigned32"
_BgpNewCfgPeerMetric_Object = MibTableColumn
bgpNewCfgPeerMetric = _BgpNewCfgPeerMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 10),
    _BgpNewCfgPeerMetric_Type()
)
bgpNewCfgPeerMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerMetric.setStatus("current")


class _BgpNewCfgPeerDefaultAction_Type(Integer32):
    """Custom type bgpNewCfgPeerDefaultAction based on Integer32"""
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
        *(("import", 2),
          ("none", 1),
          ("originate", 3),
          ("redistribute", 4))
    )


_BgpNewCfgPeerDefaultAction_Type.__name__ = "Integer32"
_BgpNewCfgPeerDefaultAction_Object = MibTableColumn
bgpNewCfgPeerDefaultAction = _BgpNewCfgPeerDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 11),
    _BgpNewCfgPeerDefaultAction_Type()
)
bgpNewCfgPeerDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerDefaultAction.setStatus("current")


class _BgpNewCfgPeerOspfState_Type(Integer32):
    """Custom type bgpNewCfgPeerOspfState based on Integer32"""
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


_BgpNewCfgPeerOspfState_Type.__name__ = "Integer32"
_BgpNewCfgPeerOspfState_Object = MibTableColumn
bgpNewCfgPeerOspfState = _BgpNewCfgPeerOspfState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 12),
    _BgpNewCfgPeerOspfState_Type()
)
bgpNewCfgPeerOspfState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerOspfState.setStatus("current")


class _BgpNewCfgPeerFixedState_Type(Integer32):
    """Custom type bgpNewCfgPeerFixedState based on Integer32"""
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


_BgpNewCfgPeerFixedState_Type.__name__ = "Integer32"
_BgpNewCfgPeerFixedState_Object = MibTableColumn
bgpNewCfgPeerFixedState = _BgpNewCfgPeerFixedState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 13),
    _BgpNewCfgPeerFixedState_Type()
)
bgpNewCfgPeerFixedState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerFixedState.setStatus("current")


class _BgpNewCfgPeerStaticState_Type(Integer32):
    """Custom type bgpNewCfgPeerStaticState based on Integer32"""
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


_BgpNewCfgPeerStaticState_Type.__name__ = "Integer32"
_BgpNewCfgPeerStaticState_Object = MibTableColumn
bgpNewCfgPeerStaticState = _BgpNewCfgPeerStaticState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 14),
    _BgpNewCfgPeerStaticState_Type()
)
bgpNewCfgPeerStaticState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerStaticState.setStatus("current")


class _BgpNewCfgPeerVipState_Type(Integer32):
    """Custom type bgpNewCfgPeerVipState based on Integer32"""
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


_BgpNewCfgPeerVipState_Type.__name__ = "Integer32"
_BgpNewCfgPeerVipState_Object = MibTableColumn
bgpNewCfgPeerVipState = _BgpNewCfgPeerVipState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 15),
    _BgpNewCfgPeerVipState_Type()
)
bgpNewCfgPeerVipState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerVipState.setStatus("current")
_BgpNewCfgPeerInRmapList_Type = OctetString
_BgpNewCfgPeerInRmapList_Object = MibTableColumn
bgpNewCfgPeerInRmapList = _BgpNewCfgPeerInRmapList_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 16),
    _BgpNewCfgPeerInRmapList_Type()
)
bgpNewCfgPeerInRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNewCfgPeerInRmapList.setStatus("current")
_BgpNewCfgPeerOutRmapList_Type = OctetString
_BgpNewCfgPeerOutRmapList_Object = MibTableColumn
bgpNewCfgPeerOutRmapList = _BgpNewCfgPeerOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 17),
    _BgpNewCfgPeerOutRmapList_Type()
)
bgpNewCfgPeerOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNewCfgPeerOutRmapList.setStatus("current")
_BgpNewCfgPeerAddInRmap_Type = Integer32
_BgpNewCfgPeerAddInRmap_Object = MibTableColumn
bgpNewCfgPeerAddInRmap = _BgpNewCfgPeerAddInRmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 18),
    _BgpNewCfgPeerAddInRmap_Type()
)
bgpNewCfgPeerAddInRmap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerAddInRmap.setStatus("current")
_BgpNewCfgPeerAddOutRmap_Type = Integer32
_BgpNewCfgPeerAddOutRmap_Object = MibTableColumn
bgpNewCfgPeerAddOutRmap = _BgpNewCfgPeerAddOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 19),
    _BgpNewCfgPeerAddOutRmap_Type()
)
bgpNewCfgPeerAddOutRmap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerAddOutRmap.setStatus("current")
_BgpNewCfgPeerRemoveInRmap_Type = Integer32
_BgpNewCfgPeerRemoveInRmap_Object = MibTableColumn
bgpNewCfgPeerRemoveInRmap = _BgpNewCfgPeerRemoveInRmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 20),
    _BgpNewCfgPeerRemoveInRmap_Type()
)
bgpNewCfgPeerRemoveInRmap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerRemoveInRmap.setStatus("current")
_BgpNewCfgPeerRemoveOutRmap_Type = Integer32
_BgpNewCfgPeerRemoveOutRmap_Object = MibTableColumn
bgpNewCfgPeerRemoveOutRmap = _BgpNewCfgPeerRemoveOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 21),
    _BgpNewCfgPeerRemoveOutRmap_Type()
)
bgpNewCfgPeerRemoveOutRmap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerRemoveOutRmap.setStatus("current")


class _BgpNewCfgPeerHoldTime_Type(Integer32):
    """Custom type bgpNewCfgPeerHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BgpNewCfgPeerHoldTime_Type.__name__ = "Integer32"
_BgpNewCfgPeerHoldTime_Object = MibTableColumn
bgpNewCfgPeerHoldTime = _BgpNewCfgPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 22),
    _BgpNewCfgPeerHoldTime_Type()
)
bgpNewCfgPeerHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerHoldTime.setStatus("current")


class _BgpNewCfgPeerKeepAlive_Type(Integer32):
    """Custom type bgpNewCfgPeerKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 21845),
    )


_BgpNewCfgPeerKeepAlive_Type.__name__ = "Integer32"
_BgpNewCfgPeerKeepAlive_Object = MibTableColumn
bgpNewCfgPeerKeepAlive = _BgpNewCfgPeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 23),
    _BgpNewCfgPeerKeepAlive_Type()
)
bgpNewCfgPeerKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerKeepAlive.setStatus("current")


class _BgpNewCfgPeerMinTime_Type(Integer32):
    """Custom type bgpNewCfgPeerMinTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BgpNewCfgPeerMinTime_Type.__name__ = "Integer32"
_BgpNewCfgPeerMinTime_Object = MibTableColumn
bgpNewCfgPeerMinTime = _BgpNewCfgPeerMinTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 24),
    _BgpNewCfgPeerMinTime_Type()
)
bgpNewCfgPeerMinTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerMinTime.setStatus("current")


class _BgpNewCfgPeerConRetry_Type(Integer32):
    """Custom type bgpNewCfgPeerConRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BgpNewCfgPeerConRetry_Type.__name__ = "Integer32"
_BgpNewCfgPeerConRetry_Object = MibTableColumn
bgpNewCfgPeerConRetry = _BgpNewCfgPeerConRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 25),
    _BgpNewCfgPeerConRetry_Type()
)
bgpNewCfgPeerConRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerConRetry.setStatus("current")


class _BgpNewCfgPeerMinAS_Type(Integer32):
    """Custom type bgpNewCfgPeerMinAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 65535),
    )


_BgpNewCfgPeerMinAS_Type.__name__ = "Integer32"
_BgpNewCfgPeerMinAS_Object = MibTableColumn
bgpNewCfgPeerMinAS = _BgpNewCfgPeerMinAS_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 26),
    _BgpNewCfgPeerMinAS_Type()
)
bgpNewCfgPeerMinAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerMinAS.setStatus("current")


class _BgpNewCfgPeerRipState_Type(Integer32):
    """Custom type bgpNewCfgPeerRipState based on Integer32"""
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


_BgpNewCfgPeerRipState_Type.__name__ = "Integer32"
_BgpNewCfgPeerRipState_Object = MibTableColumn
bgpNewCfgPeerRipState = _BgpNewCfgPeerRipState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 4, 1, 27),
    _BgpNewCfgPeerRipState_Type()
)
bgpNewCfgPeerRipState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgPeerRipState.setStatus("current")
_BgpAggrTableMax_Type = Integer32
_BgpAggrTableMax_Object = MibScalar
bgpAggrTableMax = _BgpAggrTableMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 5),
    _BgpAggrTableMax_Type()
)
bgpAggrTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAggrTableMax.setStatus("current")
_BgpCurCfgAggrTable_Object = MibTable
bgpCurCfgAggrTable = _BgpCurCfgAggrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 6)
)
if mibBuilder.loadTexts:
    bgpCurCfgAggrTable.setStatus("current")
_BgpCurCfgAggrEntry_Object = MibTableRow
bgpCurCfgAggrEntry = _BgpCurCfgAggrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 6, 1)
)
bgpCurCfgAggrEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "bgpCurCfgAggrIndex"),
)
if mibBuilder.loadTexts:
    bgpCurCfgAggrEntry.setStatus("current")
_BgpCurCfgAggrIndex_Type = Integer32
_BgpCurCfgAggrIndex_Object = MibTableColumn
bgpCurCfgAggrIndex = _BgpCurCfgAggrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 6, 1, 1),
    _BgpCurCfgAggrIndex_Type()
)
bgpCurCfgAggrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgAggrIndex.setStatus("current")
_BgpCurCfgAggrAddr_Type = IpAddress
_BgpCurCfgAggrAddr_Object = MibTableColumn
bgpCurCfgAggrAddr = _BgpCurCfgAggrAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 6, 1, 2),
    _BgpCurCfgAggrAddr_Type()
)
bgpCurCfgAggrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgAggrAddr.setStatus("current")
_BgpCurCfgAggrMask_Type = IpAddress
_BgpCurCfgAggrMask_Object = MibTableColumn
bgpCurCfgAggrMask = _BgpCurCfgAggrMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 6, 1, 3),
    _BgpCurCfgAggrMask_Type()
)
bgpCurCfgAggrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgAggrMask.setStatus("current")


class _BgpCurCfgAggrState_Type(Integer32):
    """Custom type bgpCurCfgAggrState based on Integer32"""
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


_BgpCurCfgAggrState_Type.__name__ = "Integer32"
_BgpCurCfgAggrState_Object = MibTableColumn
bgpCurCfgAggrState = _BgpCurCfgAggrState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 6, 1, 4),
    _BgpCurCfgAggrState_Type()
)
bgpCurCfgAggrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpCurCfgAggrState.setStatus("current")
_BgpNewCfgAggrTable_Object = MibTable
bgpNewCfgAggrTable = _BgpNewCfgAggrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 7)
)
if mibBuilder.loadTexts:
    bgpNewCfgAggrTable.setStatus("current")
_BgpNewCfgAggrEntry_Object = MibTableRow
bgpNewCfgAggrEntry = _BgpNewCfgAggrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 7, 1)
)
bgpNewCfgAggrEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "bgpNewCfgAggrIndex"),
)
if mibBuilder.loadTexts:
    bgpNewCfgAggrEntry.setStatus("current")
_BgpNewCfgAggrIndex_Type = Integer32
_BgpNewCfgAggrIndex_Object = MibTableColumn
bgpNewCfgAggrIndex = _BgpNewCfgAggrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 7, 1, 1),
    _BgpNewCfgAggrIndex_Type()
)
bgpNewCfgAggrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNewCfgAggrIndex.setStatus("current")
_BgpNewCfgAggrAddr_Type = IpAddress
_BgpNewCfgAggrAddr_Object = MibTableColumn
bgpNewCfgAggrAddr = _BgpNewCfgAggrAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 7, 1, 2),
    _BgpNewCfgAggrAddr_Type()
)
bgpNewCfgAggrAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgAggrAddr.setStatus("current")
_BgpNewCfgAggrMask_Type = IpAddress
_BgpNewCfgAggrMask_Object = MibTableColumn
bgpNewCfgAggrMask = _BgpNewCfgAggrMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 7, 1, 3),
    _BgpNewCfgAggrMask_Type()
)
bgpNewCfgAggrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgAggrMask.setStatus("current")


class _BgpNewCfgAggrState_Type(Integer32):
    """Custom type bgpNewCfgAggrState based on Integer32"""
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


_BgpNewCfgAggrState_Type.__name__ = "Integer32"
_BgpNewCfgAggrState_Object = MibTableColumn
bgpNewCfgAggrState = _BgpNewCfgAggrState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 7, 1, 4),
    _BgpNewCfgAggrState_Type()
)
bgpNewCfgAggrState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgAggrState.setStatus("current")


class _BgpNewCfgAggrDelete_Type(Integer32):
    """Custom type bgpNewCfgAggrDelete based on Integer32"""
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


_BgpNewCfgAggrDelete_Type.__name__ = "Integer32"
_BgpNewCfgAggrDelete_Object = MibTableColumn
bgpNewCfgAggrDelete = _BgpNewCfgAggrDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 12, 7, 1, 5),
    _BgpNewCfgAggrDelete_Type()
)
bgpNewCfgAggrDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNewCfgAggrDelete.setStatus("current")
_OspfCfg_ObjectIdentity = ObjectIdentity
ospfCfg = _OspfCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13)
)
_OspfGeneral_ObjectIdentity = ObjectIdentity
ospfGeneral = _OspfGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 1)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 1, 4),
    _OspfNewCfgDefaultRouteMetricType_Type()
)
ospfNewCfgDefaultRouteMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgDefaultRouteMetricType.setStatus("current")
_OspfIntfTableMaxSize_Type = Integer32
_OspfIntfTableMaxSize_Object = MibScalar
ospfIntfTableMaxSize = _OspfIntfTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 1, 5),
    _OspfIntfTableMaxSize_Type()
)
ospfIntfTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTableMaxSize.setStatus("current")
_OspfAreaTableMaxSize_Type = Integer32
_OspfAreaTableMaxSize_Object = MibScalar
ospfAreaTableMaxSize = _OspfAreaTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 1, 6),
    _OspfAreaTableMaxSize_Type()
)
ospfAreaTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTableMaxSize.setStatus("current")
_OspfRangeTableMaxSize_Type = Integer32
_OspfRangeTableMaxSize_Object = MibScalar
ospfRangeTableMaxSize = _OspfRangeTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 1, 7),
    _OspfRangeTableMaxSize_Type()
)
ospfRangeTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRangeTableMaxSize.setStatus("current")
_OspfVirtIntfTableMaxSize_Type = Integer32
_OspfVirtIntfTableMaxSize_Object = MibScalar
ospfVirtIntfTableMaxSize = _OspfVirtIntfTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 1, 8),
    _OspfVirtIntfTableMaxSize_Type()
)
ospfVirtIntfTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtIntfTableMaxSize.setStatus("current")
_OspfHostTableMaxSize_Type = Integer32
_OspfHostTableMaxSize_Object = MibScalar
ospfHostTableMaxSize = _OspfHostTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 1, 11),
    _OspfNewCfgState_Type()
)
ospfNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgState.setStatus("current")


class _OspfCurCfgLsdb_Type(Integer32):
    """Custom type ospfCurCfgLsdb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_OspfCurCfgLsdb_Type.__name__ = "Integer32"
_OspfCurCfgLsdb_Object = MibScalar
ospfCurCfgLsdb = _OspfCurCfgLsdb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 1, 12),
    _OspfCurCfgLsdb_Type()
)
ospfCurCfgLsdb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgLsdb.setStatus("current")


class _OspfNewCfgLsdb_Type(Integer32):
    """Custom type ospfNewCfgLsdb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_OspfNewCfgLsdb_Type.__name__ = "Integer32"
_OspfNewCfgLsdb_Object = MibScalar
ospfNewCfgLsdb = _OspfNewCfgLsdb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 1, 13),
    _OspfNewCfgLsdb_Type()
)
ospfNewCfgLsdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgLsdb.setStatus("current")
_OspfCurCfgAreaTable_Object = MibTable
ospfCurCfgAreaTable = _OspfCurCfgAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 2)
)
if mibBuilder.loadTexts:
    ospfCurCfgAreaTable.setStatus("current")
_OspfCurCfgAreaEntry_Object = MibTableRow
ospfCurCfgAreaEntry = _OspfCurCfgAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 2, 1)
)
ospfCurCfgAreaEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfCurCfgAreaIndex"),
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfCurCfgAreaId"),
)
if mibBuilder.loadTexts:
    ospfCurCfgAreaEntry.setStatus("current")
_OspfCurCfgAreaIndex_Type = Integer32
_OspfCurCfgAreaIndex_Object = MibTableColumn
ospfCurCfgAreaIndex = _OspfCurCfgAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 2, 1, 1),
    _OspfCurCfgAreaIndex_Type()
)
ospfCurCfgAreaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgAreaIndex.setStatus("current")
_OspfCurCfgAreaId_Type = IpAddress
_OspfCurCfgAreaId_Object = MibTableColumn
ospfCurCfgAreaId = _OspfCurCfgAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 2, 1, 4),
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
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nssa", 3),
          ("stub", 2),
          ("transit", 1))
    )


_OspfCurCfgAreaType_Type.__name__ = "Integer32"
_OspfCurCfgAreaType_Object = MibTableColumn
ospfCurCfgAreaType = _OspfCurCfgAreaType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 2, 1, 6),
    _OspfCurCfgAreaMetric_Type()
)
ospfCurCfgAreaMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgAreaMetric.setStatus("current")


class _OspfCurCfgAreaState_Type(Integer32):
    """Custom type ospfCurCfgAreaState based on Integer32"""
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


_OspfCurCfgAreaState_Type.__name__ = "Integer32"
_OspfCurCfgAreaState_Object = MibTableColumn
ospfCurCfgAreaState = _OspfCurCfgAreaState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 2, 1, 7),
    _OspfCurCfgAreaState_Type()
)
ospfCurCfgAreaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgAreaState.setStatus("current")
_OspfNewCfgAreaTable_Object = MibTable
ospfNewCfgAreaTable = _OspfNewCfgAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 3)
)
if mibBuilder.loadTexts:
    ospfNewCfgAreaTable.setStatus("current")
_OspfNewCfgAreaEntry_Object = MibTableRow
ospfNewCfgAreaEntry = _OspfNewCfgAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 3, 1)
)
ospfNewCfgAreaEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfNewCfgAreaIndex"),
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfNewCfgAreaId"),
)
if mibBuilder.loadTexts:
    ospfNewCfgAreaEntry.setStatus("current")
_OspfNewCfgAreaIndex_Type = Integer32
_OspfNewCfgAreaIndex_Object = MibTableColumn
ospfNewCfgAreaIndex = _OspfNewCfgAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 3, 1, 1),
    _OspfNewCfgAreaIndex_Type()
)
ospfNewCfgAreaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgAreaIndex.setStatus("current")
_OspfNewCfgAreaId_Type = IpAddress
_OspfNewCfgAreaId_Object = MibTableColumn
ospfNewCfgAreaId = _OspfNewCfgAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 3, 1, 2),
    _OspfNewCfgAreaId_Type()
)
ospfNewCfgAreaId.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 3, 1, 3),
    _OspfNewCfgAreaSpfInterval_Type()
)
ospfNewCfgAreaSpfInterval.setMaxAccess("read-create")
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 3, 1, 4),
    _OspfNewCfgAreaAuthType_Type()
)
ospfNewCfgAreaAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgAreaAuthType.setStatus("current")


class _OspfNewCfgAreaType_Type(Integer32):
    """Custom type ospfNewCfgAreaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nssa", 3),
          ("stub", 2),
          ("transit", 1))
    )


_OspfNewCfgAreaType_Type.__name__ = "Integer32"
_OspfNewCfgAreaType_Object = MibTableColumn
ospfNewCfgAreaType = _OspfNewCfgAreaType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 3, 1, 5),
    _OspfNewCfgAreaType_Type()
)
ospfNewCfgAreaType.setMaxAccess("read-create")
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 3, 1, 6),
    _OspfNewCfgAreaMetric_Type()
)
ospfNewCfgAreaMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgAreaMetric.setStatus("current")


class _OspfNewCfgAreaState_Type(Integer32):
    """Custom type ospfNewCfgAreaState based on Integer32"""
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


_OspfNewCfgAreaState_Type.__name__ = "Integer32"
_OspfNewCfgAreaState_Object = MibTableColumn
ospfNewCfgAreaState = _OspfNewCfgAreaState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 3, 1, 7),
    _OspfNewCfgAreaState_Type()
)
ospfNewCfgAreaState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgAreaState.setStatus("current")


class _OspfNewCfgAreaDelete_Type(Integer32):
    """Custom type ospfNewCfgAreaDelete based on Integer32"""
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


_OspfNewCfgAreaDelete_Type.__name__ = "Integer32"
_OspfNewCfgAreaDelete_Object = MibTableColumn
ospfNewCfgAreaDelete = _OspfNewCfgAreaDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 3, 1, 8),
    _OspfNewCfgAreaDelete_Type()
)
ospfNewCfgAreaDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgAreaDelete.setStatus("current")
_OspfRouteRedistribution_ObjectIdentity = ObjectIdentity
ospfRouteRedistribution = _OspfRouteRedistribution_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4)
)
_OspfRedistributeStatic_ObjectIdentity = ObjectIdentity
ospfRedistributeStatic = _OspfRedistributeStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 1)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 1, 4),
    _OspfNewCfgStaticMetricType_Type()
)
ospfNewCfgStaticMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgStaticMetricType.setStatus("current")
_OspfCurCfgStaticOutRmapList_Type = OctetString
_OspfCurCfgStaticOutRmapList_Object = MibScalar
ospfCurCfgStaticOutRmapList = _OspfCurCfgStaticOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 1, 5),
    _OspfCurCfgStaticOutRmapList_Type()
)
ospfCurCfgStaticOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgStaticOutRmapList.setStatus("current")
_OspfNewCfgStaticOutRmapList_Type = OctetString
_OspfNewCfgStaticOutRmapList_Object = MibScalar
ospfNewCfgStaticOutRmapList = _OspfNewCfgStaticOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 1, 6),
    _OspfNewCfgStaticOutRmapList_Type()
)
ospfNewCfgStaticOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgStaticOutRmapList.setStatus("current")
_OspfNewCfgStaticAddOutRmap_Type = Integer32
_OspfNewCfgStaticAddOutRmap_Object = MibScalar
ospfNewCfgStaticAddOutRmap = _OspfNewCfgStaticAddOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 1, 7),
    _OspfNewCfgStaticAddOutRmap_Type()
)
ospfNewCfgStaticAddOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgStaticAddOutRmap.setStatus("current")
_OspfNewCfgStaticRemoveOutRmap_Type = Integer32
_OspfNewCfgStaticRemoveOutRmap_Object = MibScalar
ospfNewCfgStaticRemoveOutRmap = _OspfNewCfgStaticRemoveOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 1, 8),
    _OspfNewCfgStaticRemoveOutRmap_Type()
)
ospfNewCfgStaticRemoveOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgStaticRemoveOutRmap.setStatus("current")
_OspfRedistributeEbgp_ObjectIdentity = ObjectIdentity
ospfRedistributeEbgp = _OspfRedistributeEbgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 2)
)


class _OspfCurCfgEbgpMetric_Type(Integer32):
    """Custom type ospfCurCfgEbgpMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OspfCurCfgEbgpMetric_Type.__name__ = "Integer32"
_OspfCurCfgEbgpMetric_Object = MibScalar
ospfCurCfgEbgpMetric = _OspfCurCfgEbgpMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 2, 1),
    _OspfCurCfgEbgpMetric_Type()
)
ospfCurCfgEbgpMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgEbgpMetric.setStatus("current")


class _OspfNewCfgEbgpMetric_Type(Integer32):
    """Custom type ospfNewCfgEbgpMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OspfNewCfgEbgpMetric_Type.__name__ = "Integer32"
_OspfNewCfgEbgpMetric_Object = MibScalar
ospfNewCfgEbgpMetric = _OspfNewCfgEbgpMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 2, 2),
    _OspfNewCfgEbgpMetric_Type()
)
ospfNewCfgEbgpMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgEbgpMetric.setStatus("current")


class _OspfCurCfgEbgpMetricType_Type(Integer32):
    """Custom type ospfCurCfgEbgpMetricType based on Integer32"""
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


_OspfCurCfgEbgpMetricType_Type.__name__ = "Integer32"
_OspfCurCfgEbgpMetricType_Object = MibScalar
ospfCurCfgEbgpMetricType = _OspfCurCfgEbgpMetricType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 2, 3),
    _OspfCurCfgEbgpMetricType_Type()
)
ospfCurCfgEbgpMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgEbgpMetricType.setStatus("current")


class _OspfNewCfgEbgpMetricType_Type(Integer32):
    """Custom type ospfNewCfgEbgpMetricType based on Integer32"""
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


_OspfNewCfgEbgpMetricType_Type.__name__ = "Integer32"
_OspfNewCfgEbgpMetricType_Object = MibScalar
ospfNewCfgEbgpMetricType = _OspfNewCfgEbgpMetricType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 2, 4),
    _OspfNewCfgEbgpMetricType_Type()
)
ospfNewCfgEbgpMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgEbgpMetricType.setStatus("current")
_OspfCurCfgEbgpOutRmapList_Type = OctetString
_OspfCurCfgEbgpOutRmapList_Object = MibScalar
ospfCurCfgEbgpOutRmapList = _OspfCurCfgEbgpOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 2, 5),
    _OspfCurCfgEbgpOutRmapList_Type()
)
ospfCurCfgEbgpOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgEbgpOutRmapList.setStatus("current")
_OspfNewCfgEbgpOutRmapList_Type = OctetString
_OspfNewCfgEbgpOutRmapList_Object = MibScalar
ospfNewCfgEbgpOutRmapList = _OspfNewCfgEbgpOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 2, 6),
    _OspfNewCfgEbgpOutRmapList_Type()
)
ospfNewCfgEbgpOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgEbgpOutRmapList.setStatus("current")
_OspfNewCfgEbgpAddOutRmap_Type = Integer32
_OspfNewCfgEbgpAddOutRmap_Object = MibScalar
ospfNewCfgEbgpAddOutRmap = _OspfNewCfgEbgpAddOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 2, 7),
    _OspfNewCfgEbgpAddOutRmap_Type()
)
ospfNewCfgEbgpAddOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgEbgpAddOutRmap.setStatus("current")
_OspfNewCfgEbgpRemoveOutRmap_Type = Integer32
_OspfNewCfgEbgpRemoveOutRmap_Object = MibScalar
ospfNewCfgEbgpRemoveOutRmap = _OspfNewCfgEbgpRemoveOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 2, 8),
    _OspfNewCfgEbgpRemoveOutRmap_Type()
)
ospfNewCfgEbgpRemoveOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgEbgpRemoveOutRmap.setStatus("current")
_OspfRedistributeIbgp_ObjectIdentity = ObjectIdentity
ospfRedistributeIbgp = _OspfRedistributeIbgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 3)
)


class _OspfCurCfgIbgpMetric_Type(Integer32):
    """Custom type ospfCurCfgIbgpMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OspfCurCfgIbgpMetric_Type.__name__ = "Integer32"
_OspfCurCfgIbgpMetric_Object = MibScalar
ospfCurCfgIbgpMetric = _OspfCurCfgIbgpMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 3, 1),
    _OspfCurCfgIbgpMetric_Type()
)
ospfCurCfgIbgpMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIbgpMetric.setStatus("current")


class _OspfNewCfgIbgpMetric_Type(Integer32):
    """Custom type ospfNewCfgIbgpMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OspfNewCfgIbgpMetric_Type.__name__ = "Integer32"
_OspfNewCfgIbgpMetric_Object = MibScalar
ospfNewCfgIbgpMetric = _OspfNewCfgIbgpMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 3, 2),
    _OspfNewCfgIbgpMetric_Type()
)
ospfNewCfgIbgpMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgIbgpMetric.setStatus("current")


class _OspfCurCfgIbgpMetricType_Type(Integer32):
    """Custom type ospfCurCfgIbgpMetricType based on Integer32"""
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


_OspfCurCfgIbgpMetricType_Type.__name__ = "Integer32"
_OspfCurCfgIbgpMetricType_Object = MibScalar
ospfCurCfgIbgpMetricType = _OspfCurCfgIbgpMetricType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 3, 3),
    _OspfCurCfgIbgpMetricType_Type()
)
ospfCurCfgIbgpMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIbgpMetricType.setStatus("current")


class _OspfNewCfgIbgpMetricType_Type(Integer32):
    """Custom type ospfNewCfgIbgpMetricType based on Integer32"""
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


_OspfNewCfgIbgpMetricType_Type.__name__ = "Integer32"
_OspfNewCfgIbgpMetricType_Object = MibScalar
ospfNewCfgIbgpMetricType = _OspfNewCfgIbgpMetricType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 3, 4),
    _OspfNewCfgIbgpMetricType_Type()
)
ospfNewCfgIbgpMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgIbgpMetricType.setStatus("current")
_OspfCurCfgIbgpOutRmapList_Type = OctetString
_OspfCurCfgIbgpOutRmapList_Object = MibScalar
ospfCurCfgIbgpOutRmapList = _OspfCurCfgIbgpOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 3, 5),
    _OspfCurCfgIbgpOutRmapList_Type()
)
ospfCurCfgIbgpOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIbgpOutRmapList.setStatus("current")
_OspfNewCfgIbgpOutRmapList_Type = OctetString
_OspfNewCfgIbgpOutRmapList_Object = MibScalar
ospfNewCfgIbgpOutRmapList = _OspfNewCfgIbgpOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 3, 6),
    _OspfNewCfgIbgpOutRmapList_Type()
)
ospfNewCfgIbgpOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgIbgpOutRmapList.setStatus("current")
_OspfNewCfgIbgpAddOutRmap_Type = Integer32
_OspfNewCfgIbgpAddOutRmap_Object = MibScalar
ospfNewCfgIbgpAddOutRmap = _OspfNewCfgIbgpAddOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 3, 7),
    _OspfNewCfgIbgpAddOutRmap_Type()
)
ospfNewCfgIbgpAddOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgIbgpAddOutRmap.setStatus("current")
_OspfNewCfgIbgpRemoveOutRmap_Type = Integer32
_OspfNewCfgIbgpRemoveOutRmap_Object = MibScalar
ospfNewCfgIbgpRemoveOutRmap = _OspfNewCfgIbgpRemoveOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 3, 8),
    _OspfNewCfgIbgpRemoveOutRmap_Type()
)
ospfNewCfgIbgpRemoveOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgIbgpRemoveOutRmap.setStatus("current")
_OspfRedistributeFixed_ObjectIdentity = ObjectIdentity
ospfRedistributeFixed = _OspfRedistributeFixed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 4)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 4, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 4, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 4, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 4, 4),
    _OspfNewCfgFixedMetricType_Type()
)
ospfNewCfgFixedMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgFixedMetricType.setStatus("current")
_OspfCurCfgFixedOutRmapList_Type = OctetString
_OspfCurCfgFixedOutRmapList_Object = MibScalar
ospfCurCfgFixedOutRmapList = _OspfCurCfgFixedOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 4, 5),
    _OspfCurCfgFixedOutRmapList_Type()
)
ospfCurCfgFixedOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgFixedOutRmapList.setStatus("current")
_OspfNewCfgFixedOutRmapList_Type = OctetString
_OspfNewCfgFixedOutRmapList_Object = MibScalar
ospfNewCfgFixedOutRmapList = _OspfNewCfgFixedOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 4, 6),
    _OspfNewCfgFixedOutRmapList_Type()
)
ospfNewCfgFixedOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgFixedOutRmapList.setStatus("current")
_OspfNewCfgFixedAddOutRmap_Type = Integer32
_OspfNewCfgFixedAddOutRmap_Object = MibScalar
ospfNewCfgFixedAddOutRmap = _OspfNewCfgFixedAddOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 4, 7),
    _OspfNewCfgFixedAddOutRmap_Type()
)
ospfNewCfgFixedAddOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgFixedAddOutRmap.setStatus("current")
_OspfNewCfgFixedRemoveOutRmap_Type = Integer32
_OspfNewCfgFixedRemoveOutRmap_Object = MibScalar
ospfNewCfgFixedRemoveOutRmap = _OspfNewCfgFixedRemoveOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 4, 8),
    _OspfNewCfgFixedRemoveOutRmap_Type()
)
ospfNewCfgFixedRemoveOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgFixedRemoveOutRmap.setStatus("current")
_OspfRedistributeRip_ObjectIdentity = ObjectIdentity
ospfRedistributeRip = _OspfRedistributeRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 5)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 5, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 5, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 5, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 5, 4),
    _OspfNewCfgRipMetricType_Type()
)
ospfNewCfgRipMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgRipMetricType.setStatus("current")
_OspfCurCfgRipOutRmapList_Type = OctetString
_OspfCurCfgRipOutRmapList_Object = MibScalar
ospfCurCfgRipOutRmapList = _OspfCurCfgRipOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 5, 5),
    _OspfCurCfgRipOutRmapList_Type()
)
ospfCurCfgRipOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgRipOutRmapList.setStatus("current")
_OspfNewCfgRipOutRmapList_Type = OctetString
_OspfNewCfgRipOutRmapList_Object = MibScalar
ospfNewCfgRipOutRmapList = _OspfNewCfgRipOutRmapList_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 5, 6),
    _OspfNewCfgRipOutRmapList_Type()
)
ospfNewCfgRipOutRmapList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgRipOutRmapList.setStatus("current")
_OspfNewCfgRipAddOutRmap_Type = Integer32
_OspfNewCfgRipAddOutRmap_Object = MibScalar
ospfNewCfgRipAddOutRmap = _OspfNewCfgRipAddOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 5, 7),
    _OspfNewCfgRipAddOutRmap_Type()
)
ospfNewCfgRipAddOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgRipAddOutRmap.setStatus("current")
_OspfNewCfgRipRemoveOutRmap_Type = Integer32
_OspfNewCfgRipRemoveOutRmap_Object = MibScalar
ospfNewCfgRipRemoveOutRmap = _OspfNewCfgRipRemoveOutRmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 4, 5, 8),
    _OspfNewCfgRipRemoveOutRmap_Type()
)
ospfNewCfgRipRemoveOutRmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgRipRemoveOutRmap.setStatus("current")
_OspfCurCfgMdkeyTable_Object = MibTable
ospfCurCfgMdkeyTable = _OspfCurCfgMdkeyTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 5)
)
if mibBuilder.loadTexts:
    ospfCurCfgMdkeyTable.setStatus("current")
_OspfCurCfgMdkeyEntry_Object = MibTableRow
ospfCurCfgMdkeyEntry = _OspfCurCfgMdkeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 5, 1)
)
ospfCurCfgMdkeyEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfCurCfgMdkeyIndex"),
)
if mibBuilder.loadTexts:
    ospfCurCfgMdkeyEntry.setStatus("current")
_OspfCurCfgMdkeyIndex_Type = Integer32
_OspfCurCfgMdkeyIndex_Object = MibTableColumn
ospfCurCfgMdkeyIndex = _OspfCurCfgMdkeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 5, 1, 2),
    _OspfCurCfgMdkeyKey_Type()
)
ospfCurCfgMdkeyKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgMdkeyKey.setStatus("current")
_OspfNewCfgMdkeyTable_Object = MibTable
ospfNewCfgMdkeyTable = _OspfNewCfgMdkeyTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 6)
)
if mibBuilder.loadTexts:
    ospfNewCfgMdkeyTable.setStatus("current")
_OspfNewCfgMdkeyEntry_Object = MibTableRow
ospfNewCfgMdkeyEntry = _OspfNewCfgMdkeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 6, 1)
)
ospfNewCfgMdkeyEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfNewCfgMdkeyIndex"),
)
if mibBuilder.loadTexts:
    ospfNewCfgMdkeyEntry.setStatus("current")
_OspfNewCfgMdkeyIndex_Type = Integer32
_OspfNewCfgMdkeyIndex_Object = MibTableColumn
ospfNewCfgMdkeyIndex = _OspfNewCfgMdkeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 6, 1, 3),
    _OspfNewCfgMdkeyDelete_Type()
)
ospfNewCfgMdkeyDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgMdkeyDelete.setStatus("current")
_OspfCurCfgIntfTable_Object = MibTable
ospfCurCfgIntfTable = _OspfCurCfgIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 7)
)
if mibBuilder.loadTexts:
    ospfCurCfgIntfTable.setStatus("current")
_OspfCurCfgIntfEntry_Object = MibTableRow
ospfCurCfgIntfEntry = _OspfCurCfgIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 7, 1)
)
ospfCurCfgIntfEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfCurCfgIntfIndex"),
)
if mibBuilder.loadTexts:
    ospfCurCfgIntfEntry.setStatus("current")
_OspfCurCfgIntfIndex_Type = Integer32
_OspfCurCfgIntfIndex_Object = MibTableColumn
ospfCurCfgIntfIndex = _OspfCurCfgIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 7, 1, 1),
    _OspfCurCfgIntfIndex_Type()
)
ospfCurCfgIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfIndex.setStatus("current")
_OspfCurCfgIntfId_Type = IpAddress
_OspfCurCfgIntfId_Object = MibTableColumn
ospfCurCfgIntfId = _OspfCurCfgIntfId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 7, 1, 2),
    _OspfCurCfgIntfId_Type()
)
ospfCurCfgIntfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfId.setStatus("current")


class _OspfCurCfgIntfMdkey_Type(Integer32):
    """Custom type ospfCurCfgIntfMdkey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OspfCurCfgIntfMdkey_Type.__name__ = "Integer32"
_OspfCurCfgIntfMdkey_Object = MibTableColumn
ospfCurCfgIntfMdkey = _OspfCurCfgIntfMdkey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 7, 1, 3),
    _OspfCurCfgIntfMdkey_Type()
)
ospfCurCfgIntfMdkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfMdkey.setStatus("current")


class _OspfCurCfgIntfAreaId_Type(Integer32):
    """Custom type ospfCurCfgIntfAreaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_OspfCurCfgIntfAreaId_Type.__name__ = "Integer32"
_OspfCurCfgIntfAreaId_Object = MibTableColumn
ospfCurCfgIntfAreaId = _OspfCurCfgIntfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 7, 1, 4),
    _OspfCurCfgIntfAreaId_Type()
)
ospfCurCfgIntfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfAreaId.setStatus("current")


class _OspfCurCfgIntfPriority_Type(Integer32):
    """Custom type ospfCurCfgIntfPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfCurCfgIntfPriority_Type.__name__ = "Integer32"
_OspfCurCfgIntfPriority_Object = MibTableColumn
ospfCurCfgIntfPriority = _OspfCurCfgIntfPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 7, 1, 5),
    _OspfCurCfgIntfPriority_Type()
)
ospfCurCfgIntfPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfPriority.setStatus("current")


class _OspfCurCfgIntfCost_Type(Integer32):
    """Custom type ospfCurCfgIntfCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfCurCfgIntfCost_Type.__name__ = "Integer32"
_OspfCurCfgIntfCost_Object = MibTableColumn
ospfCurCfgIntfCost = _OspfCurCfgIntfCost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 7, 1, 6),
    _OspfCurCfgIntfCost_Type()
)
ospfCurCfgIntfCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfCost.setStatus("current")


class _OspfCurCfgIntfHello_Type(Integer32):
    """Custom type ospfCurCfgIntfHello based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfCurCfgIntfHello_Type.__name__ = "Integer32"
_OspfCurCfgIntfHello_Object = MibTableColumn
ospfCurCfgIntfHello = _OspfCurCfgIntfHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 7, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 7, 1, 8),
    _OspfCurCfgIntfDead_Type()
)
ospfCurCfgIntfDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfDead.setStatus("current")


class _OspfCurCfgIntfTransit_Type(Integer32):
    """Custom type ospfCurCfgIntfTransit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_OspfCurCfgIntfTransit_Type.__name__ = "Integer32"
_OspfCurCfgIntfTransit_Object = MibTableColumn
ospfCurCfgIntfTransit = _OspfCurCfgIntfTransit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 7, 1, 9),
    _OspfCurCfgIntfTransit_Type()
)
ospfCurCfgIntfTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfTransit.setStatus("current")


class _OspfCurCfgIntfRetrans_Type(Integer32):
    """Custom type ospfCurCfgIntfRetrans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_OspfCurCfgIntfRetrans_Type.__name__ = "Integer32"
_OspfCurCfgIntfRetrans_Object = MibTableColumn
ospfCurCfgIntfRetrans = _OspfCurCfgIntfRetrans_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 7, 1, 10),
    _OspfCurCfgIntfRetrans_Type()
)
ospfCurCfgIntfRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfRetrans.setStatus("current")


class _OspfCurCfgIntfKey_Type(DisplayString):
    """Custom type ospfCurCfgIntfKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OspfCurCfgIntfKey_Type.__name__ = "DisplayString"
_OspfCurCfgIntfKey_Object = MibTableColumn
ospfCurCfgIntfKey = _OspfCurCfgIntfKey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 7, 1, 11),
    _OspfCurCfgIntfKey_Type()
)
ospfCurCfgIntfKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfKey.setStatus("current")


class _OspfCurCfgIntfState_Type(Integer32):
    """Custom type ospfCurCfgIntfState based on Integer32"""
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


_OspfCurCfgIntfState_Type.__name__ = "Integer32"
_OspfCurCfgIntfState_Object = MibTableColumn
ospfCurCfgIntfState = _OspfCurCfgIntfState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 7, 1, 12),
    _OspfCurCfgIntfState_Type()
)
ospfCurCfgIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgIntfState.setStatus("current")
_OspfNewCfgIntfTable_Object = MibTable
ospfNewCfgIntfTable = _OspfNewCfgIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 8)
)
if mibBuilder.loadTexts:
    ospfNewCfgIntfTable.setStatus("current")
_OspfNewCfgIntfEntry_Object = MibTableRow
ospfNewCfgIntfEntry = _OspfNewCfgIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 8, 1)
)
ospfNewCfgIntfEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfNewCfgIntfIndex"),
)
if mibBuilder.loadTexts:
    ospfNewCfgIntfEntry.setStatus("current")
_OspfNewCfgIntfIndex_Type = Integer32
_OspfNewCfgIntfIndex_Object = MibTableColumn
ospfNewCfgIntfIndex = _OspfNewCfgIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 8, 1, 1),
    _OspfNewCfgIntfIndex_Type()
)
ospfNewCfgIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgIntfIndex.setStatus("current")
_OspfNewCfgIntfId_Type = IpAddress
_OspfNewCfgIntfId_Object = MibTableColumn
ospfNewCfgIntfId = _OspfNewCfgIntfId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 8, 1, 2),
    _OspfNewCfgIntfId_Type()
)
ospfNewCfgIntfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgIntfId.setStatus("current")


class _OspfNewCfgIntfMdkey_Type(Integer32):
    """Custom type ospfNewCfgIntfMdkey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OspfNewCfgIntfMdkey_Type.__name__ = "Integer32"
_OspfNewCfgIntfMdkey_Object = MibTableColumn
ospfNewCfgIntfMdkey = _OspfNewCfgIntfMdkey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 8, 1, 3),
    _OspfNewCfgIntfMdkey_Type()
)
ospfNewCfgIntfMdkey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfMdkey.setStatus("current")


class _OspfNewCfgIntfAreaId_Type(Integer32):
    """Custom type ospfNewCfgIntfAreaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_OspfNewCfgIntfAreaId_Type.__name__ = "Integer32"
_OspfNewCfgIntfAreaId_Object = MibTableColumn
ospfNewCfgIntfAreaId = _OspfNewCfgIntfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 8, 1, 4),
    _OspfNewCfgIntfAreaId_Type()
)
ospfNewCfgIntfAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfAreaId.setStatus("current")


class _OspfNewCfgIntfPriority_Type(Integer32):
    """Custom type ospfNewCfgIntfPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfNewCfgIntfPriority_Type.__name__ = "Integer32"
_OspfNewCfgIntfPriority_Object = MibTableColumn
ospfNewCfgIntfPriority = _OspfNewCfgIntfPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 8, 1, 5),
    _OspfNewCfgIntfPriority_Type()
)
ospfNewCfgIntfPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfPriority.setStatus("current")


class _OspfNewCfgIntfCost_Type(Integer32):
    """Custom type ospfNewCfgIntfCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfNewCfgIntfCost_Type.__name__ = "Integer32"
_OspfNewCfgIntfCost_Object = MibTableColumn
ospfNewCfgIntfCost = _OspfNewCfgIntfCost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 8, 1, 6),
    _OspfNewCfgIntfCost_Type()
)
ospfNewCfgIntfCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfCost.setStatus("current")


class _OspfNewCfgIntfHello_Type(Integer32):
    """Custom type ospfNewCfgIntfHello based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfNewCfgIntfHello_Type.__name__ = "Integer32"
_OspfNewCfgIntfHello_Object = MibTableColumn
ospfNewCfgIntfHello = _OspfNewCfgIntfHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 8, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 8, 1, 8),
    _OspfNewCfgIntfDead_Type()
)
ospfNewCfgIntfDead.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfDead.setStatus("current")


class _OspfNewCfgIntfTransit_Type(Integer32):
    """Custom type ospfNewCfgIntfTransit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_OspfNewCfgIntfTransit_Type.__name__ = "Integer32"
_OspfNewCfgIntfTransit_Object = MibTableColumn
ospfNewCfgIntfTransit = _OspfNewCfgIntfTransit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 8, 1, 9),
    _OspfNewCfgIntfTransit_Type()
)
ospfNewCfgIntfTransit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfTransit.setStatus("current")


class _OspfNewCfgIntfRetrans_Type(Integer32):
    """Custom type ospfNewCfgIntfRetrans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_OspfNewCfgIntfRetrans_Type.__name__ = "Integer32"
_OspfNewCfgIntfRetrans_Object = MibTableColumn
ospfNewCfgIntfRetrans = _OspfNewCfgIntfRetrans_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 8, 1, 10),
    _OspfNewCfgIntfRetrans_Type()
)
ospfNewCfgIntfRetrans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfRetrans.setStatus("current")


class _OspfNewCfgIntfKey_Type(DisplayString):
    """Custom type ospfNewCfgIntfKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OspfNewCfgIntfKey_Type.__name__ = "DisplayString"
_OspfNewCfgIntfKey_Object = MibTableColumn
ospfNewCfgIntfKey = _OspfNewCfgIntfKey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 8, 1, 11),
    _OspfNewCfgIntfKey_Type()
)
ospfNewCfgIntfKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfKey.setStatus("current")


class _OspfNewCfgIntfState_Type(Integer32):
    """Custom type ospfNewCfgIntfState based on Integer32"""
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


_OspfNewCfgIntfState_Type.__name__ = "Integer32"
_OspfNewCfgIntfState_Object = MibTableColumn
ospfNewCfgIntfState = _OspfNewCfgIntfState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 8, 1, 12),
    _OspfNewCfgIntfState_Type()
)
ospfNewCfgIntfState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfState.setStatus("current")


class _OspfNewCfgIntfDelete_Type(Integer32):
    """Custom type ospfNewCfgIntfDelete based on Integer32"""
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


_OspfNewCfgIntfDelete_Type.__name__ = "Integer32"
_OspfNewCfgIntfDelete_Object = MibTableColumn
ospfNewCfgIntfDelete = _OspfNewCfgIntfDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 8, 1, 13),
    _OspfNewCfgIntfDelete_Type()
)
ospfNewCfgIntfDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgIntfDelete.setStatus("current")
_OspfCurCfgVirtIntfTable_Object = MibTable
ospfCurCfgVirtIntfTable = _OspfCurCfgVirtIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 9)
)
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfTable.setStatus("current")
_OspfCurCfgVirtIntfEntry_Object = MibTableRow
ospfCurCfgVirtIntfEntry = _OspfCurCfgVirtIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 9, 1)
)
ospfCurCfgVirtIntfEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfCurCfgVirtIntfIndex"),
)
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfEntry.setStatus("current")
_OspfCurCfgVirtIntfIndex_Type = Integer32
_OspfCurCfgVirtIntfIndex_Object = MibTableColumn
ospfCurCfgVirtIntfIndex = _OspfCurCfgVirtIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 9, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 9, 1, 2),
    _OspfCurCfgVirtIntfAreaId_Type()
)
ospfCurCfgVirtIntfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfAreaId.setStatus("current")
_OspfCurCfgVirtIntfNbr_Type = IpAddress
_OspfCurCfgVirtIntfNbr_Object = MibTableColumn
ospfCurCfgVirtIntfNbr = _OspfCurCfgVirtIntfNbr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 9, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 9, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 9, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 9, 1, 6),
    _OspfCurCfgVirtIntfDead_Type()
)
ospfCurCfgVirtIntfDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfDead.setStatus("current")


class _OspfCurCfgVirtIntfTransit_Type(Integer32):
    """Custom type ospfCurCfgVirtIntfTransit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_OspfCurCfgVirtIntfTransit_Type.__name__ = "Integer32"
_OspfCurCfgVirtIntfTransit_Object = MibTableColumn
ospfCurCfgVirtIntfTransit = _OspfCurCfgVirtIntfTransit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 9, 1, 7),
    _OspfCurCfgVirtIntfTransit_Type()
)
ospfCurCfgVirtIntfTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfTransit.setStatus("current")


class _OspfCurCfgVirtIntfRetrans_Type(Integer32):
    """Custom type ospfCurCfgVirtIntfRetrans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_OspfCurCfgVirtIntfRetrans_Type.__name__ = "Integer32"
_OspfCurCfgVirtIntfRetrans_Object = MibTableColumn
ospfCurCfgVirtIntfRetrans = _OspfCurCfgVirtIntfRetrans_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 9, 1, 8),
    _OspfCurCfgVirtIntfRetrans_Type()
)
ospfCurCfgVirtIntfRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfRetrans.setStatus("current")


class _OspfCurCfgVirtIntfKey_Type(DisplayString):
    """Custom type ospfCurCfgVirtIntfKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OspfCurCfgVirtIntfKey_Type.__name__ = "DisplayString"
_OspfCurCfgVirtIntfKey_Object = MibTableColumn
ospfCurCfgVirtIntfKey = _OspfCurCfgVirtIntfKey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 9, 1, 9),
    _OspfCurCfgVirtIntfKey_Type()
)
ospfCurCfgVirtIntfKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfKey.setStatus("current")


class _OspfCurCfgVirtIntfState_Type(Integer32):
    """Custom type ospfCurCfgVirtIntfState based on Integer32"""
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


_OspfCurCfgVirtIntfState_Type.__name__ = "Integer32"
_OspfCurCfgVirtIntfState_Object = MibTableColumn
ospfCurCfgVirtIntfState = _OspfCurCfgVirtIntfState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 9, 1, 10),
    _OspfCurCfgVirtIntfState_Type()
)
ospfCurCfgVirtIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgVirtIntfState.setStatus("current")
_OspfNewCfgVirtIntfTable_Object = MibTable
ospfNewCfgVirtIntfTable = _OspfNewCfgVirtIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 10)
)
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfTable.setStatus("current")
_OspfNewCfgVirtIntfEntry_Object = MibTableRow
ospfNewCfgVirtIntfEntry = _OspfNewCfgVirtIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 10, 1)
)
ospfNewCfgVirtIntfEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfNewCfgVirtIntfIndex"),
)
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfEntry.setStatus("current")
_OspfNewCfgVirtIntfIndex_Type = Integer32
_OspfNewCfgVirtIntfIndex_Object = MibTableColumn
ospfNewCfgVirtIntfIndex = _OspfNewCfgVirtIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 10, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 10, 1, 2),
    _OspfNewCfgVirtIntfAreaId_Type()
)
ospfNewCfgVirtIntfAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfAreaId.setStatus("current")
_OspfNewCfgVirtIntfNbr_Type = IpAddress
_OspfNewCfgVirtIntfNbr_Object = MibTableColumn
ospfNewCfgVirtIntfNbr = _OspfNewCfgVirtIntfNbr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 10, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 10, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 10, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 10, 1, 6),
    _OspfNewCfgVirtIntfDead_Type()
)
ospfNewCfgVirtIntfDead.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfDead.setStatus("current")


class _OspfNewCfgVirtIntfTransit_Type(Integer32):
    """Custom type ospfNewCfgVirtIntfTransit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_OspfNewCfgVirtIntfTransit_Type.__name__ = "Integer32"
_OspfNewCfgVirtIntfTransit_Object = MibTableColumn
ospfNewCfgVirtIntfTransit = _OspfNewCfgVirtIntfTransit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 10, 1, 7),
    _OspfNewCfgVirtIntfTransit_Type()
)
ospfNewCfgVirtIntfTransit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfTransit.setStatus("current")


class _OspfNewCfgVirtIntfRetrans_Type(Integer32):
    """Custom type ospfNewCfgVirtIntfRetrans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_OspfNewCfgVirtIntfRetrans_Type.__name__ = "Integer32"
_OspfNewCfgVirtIntfRetrans_Object = MibTableColumn
ospfNewCfgVirtIntfRetrans = _OspfNewCfgVirtIntfRetrans_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 10, 1, 8),
    _OspfNewCfgVirtIntfRetrans_Type()
)
ospfNewCfgVirtIntfRetrans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfRetrans.setStatus("current")


class _OspfNewCfgVirtIntfKey_Type(DisplayString):
    """Custom type ospfNewCfgVirtIntfKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OspfNewCfgVirtIntfKey_Type.__name__ = "DisplayString"
_OspfNewCfgVirtIntfKey_Object = MibTableColumn
ospfNewCfgVirtIntfKey = _OspfNewCfgVirtIntfKey_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 10, 1, 9),
    _OspfNewCfgVirtIntfKey_Type()
)
ospfNewCfgVirtIntfKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfKey.setStatus("current")


class _OspfNewCfgVirtIntfState_Type(Integer32):
    """Custom type ospfNewCfgVirtIntfState based on Integer32"""
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


_OspfNewCfgVirtIntfState_Type.__name__ = "Integer32"
_OspfNewCfgVirtIntfState_Object = MibTableColumn
ospfNewCfgVirtIntfState = _OspfNewCfgVirtIntfState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 10, 1, 10),
    _OspfNewCfgVirtIntfState_Type()
)
ospfNewCfgVirtIntfState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfState.setStatus("current")


class _OspfNewCfgVirtIntfDelete_Type(Integer32):
    """Custom type ospfNewCfgVirtIntfDelete based on Integer32"""
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


_OspfNewCfgVirtIntfDelete_Type.__name__ = "Integer32"
_OspfNewCfgVirtIntfDelete_Object = MibTableColumn
ospfNewCfgVirtIntfDelete = _OspfNewCfgVirtIntfDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 10, 1, 11),
    _OspfNewCfgVirtIntfDelete_Type()
)
ospfNewCfgVirtIntfDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVirtIntfDelete.setStatus("current")
_OspfMdkeyTableMaxSize_Type = Integer32
_OspfMdkeyTableMaxSize_Object = MibScalar
ospfMdkeyTableMaxSize = _OspfMdkeyTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 11),
    _OspfMdkeyTableMaxSize_Type()
)
ospfMdkeyTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfMdkeyTableMaxSize.setStatus("current")
_OspfCurCfgHostTable_Object = MibTable
ospfCurCfgHostTable = _OspfCurCfgHostTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 12)
)
if mibBuilder.loadTexts:
    ospfCurCfgHostTable.setStatus("current")
_OspfCurCfgHostEntry_Object = MibTableRow
ospfCurCfgHostEntry = _OspfCurCfgHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 12, 1)
)
ospfCurCfgHostEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfCurCfgHostIndex"),
)
if mibBuilder.loadTexts:
    ospfCurCfgHostEntry.setStatus("current")
_OspfCurCfgHostIndex_Type = Integer32
_OspfCurCfgHostIndex_Object = MibTableColumn
ospfCurCfgHostIndex = _OspfCurCfgHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 12, 1, 1),
    _OspfCurCfgHostIndex_Type()
)
ospfCurCfgHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgHostIndex.setStatus("current")
_OspfCurCfgHostIpAddr_Type = IpAddress
_OspfCurCfgHostIpAddr_Object = MibTableColumn
ospfCurCfgHostIpAddr = _OspfCurCfgHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 12, 1, 2),
    _OspfCurCfgHostIpAddr_Type()
)
ospfCurCfgHostIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgHostIpAddr.setStatus("current")
_OspfCurCfgHostAreaIndex_Type = Integer32
_OspfCurCfgHostAreaIndex_Object = MibTableColumn
ospfCurCfgHostAreaIndex = _OspfCurCfgHostAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 12, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 12, 1, 4),
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
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_OspfCurCfgHostState_Type.__name__ = "Integer32"
_OspfCurCfgHostState_Object = MibTableColumn
ospfCurCfgHostState = _OspfCurCfgHostState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 12, 1, 5),
    _OspfCurCfgHostState_Type()
)
ospfCurCfgHostState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgHostState.setStatus("current")
_OspfNewCfgHostTable_Object = MibTable
ospfNewCfgHostTable = _OspfNewCfgHostTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 13)
)
if mibBuilder.loadTexts:
    ospfNewCfgHostTable.setStatus("current")
_OspfNewCfgHostEntry_Object = MibTableRow
ospfNewCfgHostEntry = _OspfNewCfgHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 13, 1)
)
ospfNewCfgHostEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfNewCfgHostIndex"),
)
if mibBuilder.loadTexts:
    ospfNewCfgHostEntry.setStatus("current")
_OspfNewCfgHostIndex_Type = Integer32
_OspfNewCfgHostIndex_Object = MibTableColumn
ospfNewCfgHostIndex = _OspfNewCfgHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 13, 1, 1),
    _OspfNewCfgHostIndex_Type()
)
ospfNewCfgHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgHostIndex.setStatus("current")
_OspfNewCfgHostIpAddr_Type = IpAddress
_OspfNewCfgHostIpAddr_Object = MibTableColumn
ospfNewCfgHostIpAddr = _OspfNewCfgHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 13, 1, 2),
    _OspfNewCfgHostIpAddr_Type()
)
ospfNewCfgHostIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgHostIpAddr.setStatus("current")
_OspfNewCfgHostAreaIndex_Type = Integer32
_OspfNewCfgHostAreaIndex_Object = MibTableColumn
ospfNewCfgHostAreaIndex = _OspfNewCfgHostAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 13, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 13, 1, 4),
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
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_OspfNewCfgHostState_Type.__name__ = "Integer32"
_OspfNewCfgHostState_Object = MibTableColumn
ospfNewCfgHostState = _OspfNewCfgHostState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 13, 1, 5),
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
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_OspfNewCfgHostDelete_Type.__name__ = "Integer32"
_OspfNewCfgHostDelete_Object = MibTableColumn
ospfNewCfgHostDelete = _OspfNewCfgHostDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 13, 1, 6),
    _OspfNewCfgHostDelete_Type()
)
ospfNewCfgHostDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgHostDelete.setStatus("current")
_OspfCurCfgRangeTable_Object = MibTable
ospfCurCfgRangeTable = _OspfCurCfgRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 14)
)
if mibBuilder.loadTexts:
    ospfCurCfgRangeTable.setStatus("current")
_OspfCurCfgRangeEntry_Object = MibTableRow
ospfCurCfgRangeEntry = _OspfCurCfgRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 14, 1)
)
ospfCurCfgRangeEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfCurCfgRangeIndex"),
)
if mibBuilder.loadTexts:
    ospfCurCfgRangeEntry.setStatus("current")
_OspfCurCfgRangeIndex_Type = Integer32
_OspfCurCfgRangeIndex_Object = MibTableColumn
ospfCurCfgRangeIndex = _OspfCurCfgRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 14, 1, 1),
    _OspfCurCfgRangeIndex_Type()
)
ospfCurCfgRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgRangeIndex.setStatus("current")
_OspfCurCfgRangeAddr_Type = IpAddress
_OspfCurCfgRangeAddr_Object = MibTableColumn
ospfCurCfgRangeAddr = _OspfCurCfgRangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 14, 1, 2),
    _OspfCurCfgRangeAddr_Type()
)
ospfCurCfgRangeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgRangeAddr.setStatus("current")
_OspfCurCfgRangeMask_Type = IpAddress
_OspfCurCfgRangeMask_Object = MibTableColumn
ospfCurCfgRangeMask = _OspfCurCfgRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 14, 1, 3),
    _OspfCurCfgRangeMask_Type()
)
ospfCurCfgRangeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgRangeMask.setStatus("current")
_OspfCurCfgRangeAreaIndex_Type = Integer32
_OspfCurCfgRangeAreaIndex_Object = MibTableColumn
ospfCurCfgRangeAreaIndex = _OspfCurCfgRangeAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 14, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 14, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 14, 1, 6),
    _OspfCurCfgRangeState_Type()
)
ospfCurCfgRangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgRangeState.setStatus("current")
_OspfNewCfgRangeTable_Object = MibTable
ospfNewCfgRangeTable = _OspfNewCfgRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 15)
)
if mibBuilder.loadTexts:
    ospfNewCfgRangeTable.setStatus("current")
_OspfNewCfgRangeEntry_Object = MibTableRow
ospfNewCfgRangeEntry = _OspfNewCfgRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 15, 1)
)
ospfNewCfgRangeEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfNewCfgRangeIndex"),
)
if mibBuilder.loadTexts:
    ospfNewCfgRangeEntry.setStatus("current")
_OspfNewCfgRangeIndex_Type = Integer32
_OspfNewCfgRangeIndex_Object = MibTableColumn
ospfNewCfgRangeIndex = _OspfNewCfgRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 15, 1, 1),
    _OspfNewCfgRangeIndex_Type()
)
ospfNewCfgRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgRangeIndex.setStatus("current")
_OspfNewCfgRangeAddr_Type = IpAddress
_OspfNewCfgRangeAddr_Object = MibTableColumn
ospfNewCfgRangeAddr = _OspfNewCfgRangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 15, 1, 2),
    _OspfNewCfgRangeAddr_Type()
)
ospfNewCfgRangeAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgRangeAddr.setStatus("current")
_OspfNewCfgRangeMask_Type = IpAddress
_OspfNewCfgRangeMask_Object = MibTableColumn
ospfNewCfgRangeMask = _OspfNewCfgRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 15, 1, 3),
    _OspfNewCfgRangeMask_Type()
)
ospfNewCfgRangeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgRangeMask.setStatus("current")
_OspfNewCfgRangeAreaIndex_Type = Integer32
_OspfNewCfgRangeAreaIndex_Object = MibTableColumn
ospfNewCfgRangeAreaIndex = _OspfNewCfgRangeAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 15, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 15, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 15, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 15, 1, 7),
    _OspfNewCfgRangeDelete_Type()
)
ospfNewCfgRangeDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgRangeDelete.setStatus("current")
_OspfNewCfgVisionAreaTable_Object = MibTable
ospfNewCfgVisionAreaTable = _OspfNewCfgVisionAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 16)
)
if mibBuilder.loadTexts:
    ospfNewCfgVisionAreaTable.setStatus("current")
_OspfNewCfgVisionAreaEntry_Object = MibTableRow
ospfNewCfgVisionAreaEntry = _OspfNewCfgVisionAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 16, 1)
)
ospfNewCfgVisionAreaEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfNewCfgVisionAreaIndex"),
)
if mibBuilder.loadTexts:
    ospfNewCfgVisionAreaEntry.setStatus("current")
_OspfNewCfgVisionAreaIndex_Type = Integer32
_OspfNewCfgVisionAreaIndex_Object = MibTableColumn
ospfNewCfgVisionAreaIndex = _OspfNewCfgVisionAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 16, 1, 1),
    _OspfNewCfgVisionAreaIndex_Type()
)
ospfNewCfgVisionAreaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgVisionAreaIndex.setStatus("current")
_OspfNewCfgVisionAreaId_Type = IpAddress
_OspfNewCfgVisionAreaId_Object = MibTableColumn
ospfNewCfgVisionAreaId = _OspfNewCfgVisionAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 16, 1, 2),
    _OspfNewCfgVisionAreaId_Type()
)
ospfNewCfgVisionAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgVisionAreaId.setStatus("current")


class _OspfNewCfgVisionAreaSpfInterval_Type(Integer32):
    """Custom type ospfNewCfgVisionAreaSpfInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OspfNewCfgVisionAreaSpfInterval_Type.__name__ = "Integer32"
_OspfNewCfgVisionAreaSpfInterval_Object = MibTableColumn
ospfNewCfgVisionAreaSpfInterval = _OspfNewCfgVisionAreaSpfInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 16, 1, 3),
    _OspfNewCfgVisionAreaSpfInterval_Type()
)
ospfNewCfgVisionAreaSpfInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVisionAreaSpfInterval.setStatus("current")


class _OspfNewCfgVisionAreaAuthType_Type(Integer32):
    """Custom type ospfNewCfgVisionAreaAuthType based on Integer32"""
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


_OspfNewCfgVisionAreaAuthType_Type.__name__ = "Integer32"
_OspfNewCfgVisionAreaAuthType_Object = MibTableColumn
ospfNewCfgVisionAreaAuthType = _OspfNewCfgVisionAreaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 16, 1, 4),
    _OspfNewCfgVisionAreaAuthType_Type()
)
ospfNewCfgVisionAreaAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVisionAreaAuthType.setStatus("current")


class _OspfNewCfgVisionAreaType_Type(Integer32):
    """Custom type ospfNewCfgVisionAreaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nssa", 3),
          ("stub", 2),
          ("transit", 1))
    )


_OspfNewCfgVisionAreaType_Type.__name__ = "Integer32"
_OspfNewCfgVisionAreaType_Object = MibTableColumn
ospfNewCfgVisionAreaType = _OspfNewCfgVisionAreaType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 16, 1, 5),
    _OspfNewCfgVisionAreaType_Type()
)
ospfNewCfgVisionAreaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVisionAreaType.setStatus("current")


class _OspfNewCfgVisionAreaMetric_Type(Integer32):
    """Custom type ospfNewCfgVisionAreaMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfNewCfgVisionAreaMetric_Type.__name__ = "Integer32"
_OspfNewCfgVisionAreaMetric_Object = MibTableColumn
ospfNewCfgVisionAreaMetric = _OspfNewCfgVisionAreaMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 16, 1, 6),
    _OspfNewCfgVisionAreaMetric_Type()
)
ospfNewCfgVisionAreaMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVisionAreaMetric.setStatus("current")


class _OspfNewCfgVisionAreaState_Type(Integer32):
    """Custom type ospfNewCfgVisionAreaState based on Integer32"""
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


_OspfNewCfgVisionAreaState_Type.__name__ = "Integer32"
_OspfNewCfgVisionAreaState_Object = MibTableColumn
ospfNewCfgVisionAreaState = _OspfNewCfgVisionAreaState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 16, 1, 7),
    _OspfNewCfgVisionAreaState_Type()
)
ospfNewCfgVisionAreaState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVisionAreaState.setStatus("current")


class _OspfNewCfgVisionAreaDelete_Type(Integer32):
    """Custom type ospfNewCfgVisionAreaDelete based on Integer32"""
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


_OspfNewCfgVisionAreaDelete_Type.__name__ = "Integer32"
_OspfNewCfgVisionAreaDelete_Object = MibTableColumn
ospfNewCfgVisionAreaDelete = _OspfNewCfgVisionAreaDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 13, 16, 1, 8),
    _OspfNewCfgVisionAreaDelete_Type()
)
ospfNewCfgVisionAreaDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNewCfgVisionAreaDelete.setStatus("current")
_IpGeneralCfg_ObjectIdentity = ObjectIdentity
ipGeneralCfg = _IpGeneralCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 14)
)
_IpCurCfgRouterID_Type = IpAddress
_IpCurCfgRouterID_Object = MibScalar
ipCurCfgRouterID = _IpCurCfgRouterID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 14, 1),
    _IpCurCfgRouterID_Type()
)
ipCurCfgRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgRouterID.setStatus("current")
_IpNewCfgRouterID_Type = IpAddress
_IpNewCfgRouterID_Object = MibScalar
ipNewCfgRouterID = _IpNewCfgRouterID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 14, 2),
    _IpNewCfgRouterID_Type()
)
ipNewCfgRouterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgRouterID.setStatus("current")


class _IpCurCfgASNumber_Type(Integer32):
    """Custom type ipCurCfgASNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpCurCfgASNumber_Type.__name__ = "Integer32"
_IpCurCfgASNumber_Object = MibScalar
ipCurCfgASNumber = _IpCurCfgASNumber_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 14, 3),
    _IpCurCfgASNumber_Type()
)
ipCurCfgASNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgASNumber.setStatus("current")


class _IpNewCfgASNumber_Type(Integer32):
    """Custom type ipNewCfgASNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpNewCfgASNumber_Type.__name__ = "Integer32"
_IpNewCfgASNumber_Object = MibScalar
ipNewCfgASNumber = _IpNewCfgASNumber_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 14, 4),
    _IpNewCfgASNumber_Type()
)
ipNewCfgASNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgASNumber.setStatus("current")
_IpStaticArpCfg_ObjectIdentity = ObjectIdentity
ipStaticArpCfg = _IpStaticArpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 15)
)
_IpStaticArpTableMaxSize_Type = Integer32
_IpStaticArpTableMaxSize_Object = MibScalar
ipStaticArpTableMaxSize = _IpStaticArpTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 15, 1),
    _IpStaticArpTableMaxSize_Type()
)
ipStaticArpTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStaticArpTableMaxSize.setStatus("current")
_IpCurCfgStaticArpTable_Object = MibTable
ipCurCfgStaticArpTable = _IpCurCfgStaticArpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 15, 2)
)
if mibBuilder.loadTexts:
    ipCurCfgStaticArpTable.setStatus("current")
_IpCurCfgStaticArpEntry_Object = MibTableRow
ipCurCfgStaticArpEntry = _IpCurCfgStaticArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 15, 2, 1)
)
ipCurCfgStaticArpEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipCurCfgStaticArpIndx"),
)
if mibBuilder.loadTexts:
    ipCurCfgStaticArpEntry.setStatus("current")
_IpCurCfgStaticArpIndx_Type = Integer32
_IpCurCfgStaticArpIndx_Object = MibTableColumn
ipCurCfgStaticArpIndx = _IpCurCfgStaticArpIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 15, 2, 1, 1),
    _IpCurCfgStaticArpIndx_Type()
)
ipCurCfgStaticArpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticArpIndx.setStatus("current")
_IpCurCfgStaticArpIp_Type = IpAddress
_IpCurCfgStaticArpIp_Object = MibTableColumn
ipCurCfgStaticArpIp = _IpCurCfgStaticArpIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 15, 2, 1, 2),
    _IpCurCfgStaticArpIp_Type()
)
ipCurCfgStaticArpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticArpIp.setStatus("current")
_IpCurCfgStaticArpMAC_Type = PhysAddress
_IpCurCfgStaticArpMAC_Object = MibTableColumn
ipCurCfgStaticArpMAC = _IpCurCfgStaticArpMAC_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 15, 2, 1, 3),
    _IpCurCfgStaticArpMAC_Type()
)
ipCurCfgStaticArpMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticArpMAC.setStatus("current")
_IpCurCfgStaticArpVlan_Type = Integer32
_IpCurCfgStaticArpVlan_Object = MibTableColumn
ipCurCfgStaticArpVlan = _IpCurCfgStaticArpVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 15, 2, 1, 4),
    _IpCurCfgStaticArpVlan_Type()
)
ipCurCfgStaticArpVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticArpVlan.setStatus("current")
_IpCurCfgStaticArpPort_Type = Integer32
_IpCurCfgStaticArpPort_Object = MibTableColumn
ipCurCfgStaticArpPort = _IpCurCfgStaticArpPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 15, 2, 1, 5),
    _IpCurCfgStaticArpPort_Type()
)
ipCurCfgStaticArpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticArpPort.setStatus("current")
_IpNewCfgStaticArpTable_Object = MibTable
ipNewCfgStaticArpTable = _IpNewCfgStaticArpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 15, 3)
)
if mibBuilder.loadTexts:
    ipNewCfgStaticArpTable.setStatus("current")
_IpNewCfgStaticArpEntry_Object = MibTableRow
ipNewCfgStaticArpEntry = _IpNewCfgStaticArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 15, 3, 1)
)
ipNewCfgStaticArpEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipNewCfgStaticArpIndx"),
)
if mibBuilder.loadTexts:
    ipNewCfgStaticArpEntry.setStatus("current")
_IpNewCfgStaticArpIndx_Type = Integer32
_IpNewCfgStaticArpIndx_Object = MibTableColumn
ipNewCfgStaticArpIndx = _IpNewCfgStaticArpIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 15, 3, 1, 1),
    _IpNewCfgStaticArpIndx_Type()
)
ipNewCfgStaticArpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgStaticArpIndx.setStatus("current")
_IpNewCfgStaticArpIp_Type = IpAddress
_IpNewCfgStaticArpIp_Object = MibTableColumn
ipNewCfgStaticArpIp = _IpNewCfgStaticArpIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 15, 3, 1, 2),
    _IpNewCfgStaticArpIp_Type()
)
ipNewCfgStaticArpIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticArpIp.setStatus("current")
_IpNewCfgStaticArpMAC_Type = PhysAddress
_IpNewCfgStaticArpMAC_Object = MibTableColumn
ipNewCfgStaticArpMAC = _IpNewCfgStaticArpMAC_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 15, 3, 1, 3),
    _IpNewCfgStaticArpMAC_Type()
)
ipNewCfgStaticArpMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticArpMAC.setStatus("current")
_IpNewCfgStaticArpVlan_Type = Integer32
_IpNewCfgStaticArpVlan_Object = MibTableColumn
ipNewCfgStaticArpVlan = _IpNewCfgStaticArpVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 15, 3, 1, 4),
    _IpNewCfgStaticArpVlan_Type()
)
ipNewCfgStaticArpVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticArpVlan.setStatus("current")
_IpNewCfgStaticArpPort_Type = Integer32
_IpNewCfgStaticArpPort_Object = MibTableColumn
ipNewCfgStaticArpPort = _IpNewCfgStaticArpPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 15, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 15, 3, 1, 6),
    _IpNewCfgStaticArpAction_Type()
)
ipNewCfgStaticArpAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticArpAction.setStatus("current")
_IpStaticArpTableNextAvailableIndex_Type = Integer32
_IpStaticArpTableNextAvailableIndex_Object = MibScalar
ipStaticArpTableNextAvailableIndex = _IpStaticArpTableNextAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 15, 4),
    _IpStaticArpTableNextAvailableIndex_Type()
)
ipStaticArpTableNextAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStaticArpTableNextAvailableIndex.setStatus("current")
_Rip2Cfg_ObjectIdentity = ObjectIdentity
rip2Cfg = _Rip2Cfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18)
)
_RipCurCfgIntfTable_Object = MibTable
ripCurCfgIntfTable = _RipCurCfgIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 1)
)
if mibBuilder.loadTexts:
    ripCurCfgIntfTable.setStatus("current")
_RipCurCfgIntfEntry_Object = MibTableRow
ripCurCfgIntfEntry = _RipCurCfgIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 1, 1)
)
ripCurCfgIntfEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ripCurCfgIntfIndex"),
)
if mibBuilder.loadTexts:
    ripCurCfgIntfEntry.setStatus("current")
_RipCurCfgIntfIndex_Type = Integer32
_RipCurCfgIntfIndex_Object = MibTableColumn
ripCurCfgIntfIndex = _RipCurCfgIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 1, 1, 1),
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
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("ripVersion1", 1),
          ("ripVersion2", 2))
    )


_RipCurCfgIntfVersion_Type.__name__ = "Integer32"
_RipCurCfgIntfVersion_Object = MibTableColumn
ripCurCfgIntfVersion = _RipCurCfgIntfVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 1, 1, 2),
    _RipCurCfgIntfVersion_Type()
)
ripCurCfgIntfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfVersion.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 1, 1, 3),
    _RipCurCfgIntfState_Type()
)
ripCurCfgIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfState.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 1, 1, 4),
    _RipCurCfgIntfListen_Type()
)
ripCurCfgIntfListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfListen.setStatus("current")


class _RipCurCfgIntfDefListen_Type(Integer32):
    """Custom type ripCurCfgIntfDefListen based on Integer32"""
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


_RipCurCfgIntfDefListen_Type.__name__ = "Integer32"
_RipCurCfgIntfDefListen_Object = MibTableColumn
ripCurCfgIntfDefListen = _RipCurCfgIntfDefListen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 1, 1, 5),
    _RipCurCfgIntfDefListen_Type()
)
ripCurCfgIntfDefListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfDefListen.setStatus("obsolete")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 1, 1, 8),
    _RipCurCfgIntfPoisonReverse_Type()
)
ripCurCfgIntfPoisonReverse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfPoisonReverse.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 1, 1, 9),
    _RipCurCfgIntfSupply_Type()
)
ripCurCfgIntfSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfSupply.setStatus("current")


class _RipCurCfgIntfMetric_Type(Integer32):
    """Custom type ripCurCfgIntfMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RipCurCfgIntfMetric_Type.__name__ = "Integer32"
_RipCurCfgIntfMetric_Object = MibTableColumn
ripCurCfgIntfMetric = _RipCurCfgIntfMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 1, 1, 12),
    _RipCurCfgIntfKey_Type()
)
ripCurCfgIntfKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfKey.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 1, 1, 13),
    _RipCurCfgIntfDefault_Type()
)
ripCurCfgIntfDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgIntfDefault.setStatus("current")
_RipNewCfgIntfTable_Object = MibTable
ripNewCfgIntfTable = _RipNewCfgIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 2)
)
if mibBuilder.loadTexts:
    ripNewCfgIntfTable.setStatus("current")
_RipNewCfgIntfEntry_Object = MibTableRow
ripNewCfgIntfEntry = _RipNewCfgIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 2, 1)
)
ripNewCfgIntfEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ripNewCfgIntfIndex"),
)
if mibBuilder.loadTexts:
    ripNewCfgIntfEntry.setStatus("current")
_RipNewCfgIntfIndex_Type = Integer32
_RipNewCfgIntfIndex_Object = MibTableColumn
ripNewCfgIntfIndex = _RipNewCfgIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 2, 1, 1),
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
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("ripVersion1", 1),
          ("ripVersion2", 2))
    )


_RipNewCfgIntfVersion_Type.__name__ = "Integer32"
_RipNewCfgIntfVersion_Object = MibTableColumn
ripNewCfgIntfVersion = _RipNewCfgIntfVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 2, 1, 2),
    _RipNewCfgIntfVersion_Type()
)
ripNewCfgIntfVersion.setMaxAccess("read-create")
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 2, 1, 3),
    _RipNewCfgIntfSupply_Type()
)
ripNewCfgIntfSupply.setMaxAccess("read-create")
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 2, 1, 4),
    _RipNewCfgIntfListen_Type()
)
ripNewCfgIntfListen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripNewCfgIntfListen.setStatus("current")


class _RipNewCfgIntfDefListen_Type(Integer32):
    """Custom type ripNewCfgIntfDefListen based on Integer32"""
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


_RipNewCfgIntfDefListen_Type.__name__ = "Integer32"
_RipNewCfgIntfDefListen_Object = MibTableColumn
ripNewCfgIntfDefListen = _RipNewCfgIntfDefListen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 2, 1, 5),
    _RipNewCfgIntfDefListen_Type()
)
ripNewCfgIntfDefListen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripNewCfgIntfDefListen.setStatus("obsolete")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 2, 1, 6),
    _RipNewCfgIntfTrigUpdate_Type()
)
ripNewCfgIntfTrigUpdate.setMaxAccess("read-create")
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 2, 1, 7),
    _RipNewCfgIntfMcastUpdate_Type()
)
ripNewCfgIntfMcastUpdate.setMaxAccess("read-create")
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 2, 1, 8),
    _RipNewCfgIntfPoisonReverse_Type()
)
ripNewCfgIntfPoisonReverse.setMaxAccess("read-create")
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 2, 1, 9),
    _RipNewCfgIntfState_Type()
)
ripNewCfgIntfState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripNewCfgIntfState.setStatus("current")


class _RipNewCfgIntfMetric_Type(Integer32):
    """Custom type ripNewCfgIntfMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RipNewCfgIntfMetric_Type.__name__ = "Integer32"
_RipNewCfgIntfMetric_Object = MibTableColumn
ripNewCfgIntfMetric = _RipNewCfgIntfMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 2, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 2, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 2, 1, 12),
    _RipNewCfgIntfKey_Type()
)
ripNewCfgIntfKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripNewCfgIntfKey.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 2, 1, 13),
    _RipNewCfgIntfDefault_Type()
)
ripNewCfgIntfDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripNewCfgIntfDefault.setStatus("current")
_RipGeneral_ObjectIdentity = ObjectIdentity
ripGeneral = _RipGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 3)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 3, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 3, 4),
    _Rip2NewCfgUpdatePeriod_Type()
)
rip2NewCfgUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2NewCfgUpdatePeriod.setStatus("current")


class _Rip2CurCfgVip_Type(Integer32):
    """Custom type rip2CurCfgVip based on Integer32"""
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


_Rip2CurCfgVip_Type.__name__ = "Integer32"
_Rip2CurCfgVip_Object = MibScalar
rip2CurCfgVip = _Rip2CurCfgVip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 3, 5),
    _Rip2CurCfgVip_Type()
)
rip2CurCfgVip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2CurCfgVip.setStatus("current")


class _Rip2NewCfgVip_Type(Integer32):
    """Custom type rip2NewCfgVip based on Integer32"""
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


_Rip2NewCfgVip_Type.__name__ = "Integer32"
_Rip2NewCfgVip_Object = MibScalar
rip2NewCfgVip = _Rip2NewCfgVip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 3, 6),
    _Rip2NewCfgVip_Type()
)
rip2NewCfgVip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2NewCfgVip.setStatus("current")


class _Rip2CurCfgStaticSupply_Type(Integer32):
    """Custom type rip2CurCfgStaticSupply based on Integer32"""
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


_Rip2CurCfgStaticSupply_Type.__name__ = "Integer32"
_Rip2CurCfgStaticSupply_Object = MibScalar
rip2CurCfgStaticSupply = _Rip2CurCfgStaticSupply_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 3, 7),
    _Rip2CurCfgStaticSupply_Type()
)
rip2CurCfgStaticSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2CurCfgStaticSupply.setStatus("current")


class _Rip2NewCfgStaticSupply_Type(Integer32):
    """Custom type rip2NewCfgStaticSupply based on Integer32"""
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


_Rip2NewCfgStaticSupply_Type.__name__ = "Integer32"
_Rip2NewCfgStaticSupply_Object = MibScalar
rip2NewCfgStaticSupply = _Rip2NewCfgStaticSupply_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 1, 18, 3, 8),
    _Rip2NewCfgStaticSupply_Type()
)
rip2NewCfgStaticSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2NewCfgStaticSupply.setStatus("current")
_Layer3Stats_ObjectIdentity = ObjectIdentity
layer3Stats = _Layer3Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2)
)
_ArpStats_ObjectIdentity = ObjectIdentity
arpStats = _ArpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 2)
)
_ArpStatEntries_Type = Gauge32
_ArpStatEntries_Object = MibScalar
arpStatEntries = _ArpStatEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 2, 1),
    _ArpStatEntries_Type()
)
arpStatEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpStatEntries.setStatus("current")
_ArpStatHighWater_Type = Gauge32
_ArpStatHighWater_Object = MibScalar
arpStatHighWater = _ArpStatHighWater_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 2, 2),
    _ArpStatHighWater_Type()
)
arpStatHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpStatHighWater.setStatus("current")
_ArpStatMaxEntries_Type = Gauge32
_ArpStatMaxEntries_Object = MibScalar
arpStatMaxEntries = _ArpStatMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 2, 3),
    _ArpStatMaxEntries_Type()
)
arpStatMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpStatMaxEntries.setStatus("current")
_RouteStats_ObjectIdentity = ObjectIdentity
routeStats = _RouteStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 3)
)
_RouteStatEntries_Type = Gauge32
_RouteStatEntries_Object = MibScalar
routeStatEntries = _RouteStatEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 3, 1),
    _RouteStatEntries_Type()
)
routeStatEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatEntries.setStatus("current")
_RouteStatHighWater_Type = Gauge32
_RouteStatHighWater_Object = MibScalar
routeStatHighWater = _RouteStatHighWater_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 3, 2),
    _RouteStatHighWater_Type()
)
routeStatHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatHighWater.setStatus("current")
_RouteStatMaxEntries_Type = Gauge32
_RouteStatMaxEntries_Object = MibScalar
routeStatMaxEntries = _RouteStatMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 3, 3),
    _RouteStatMaxEntries_Type()
)
routeStatMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatMaxEntries.setStatus("current")
_DnsStats_ObjectIdentity = ObjectIdentity
dnsStats = _DnsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 4)
)
_DnsStatInGoodDnsRequests_Type = Counter32
_DnsStatInGoodDnsRequests_Object = MibScalar
dnsStatInGoodDnsRequests = _DnsStatInGoodDnsRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 4, 1),
    _DnsStatInGoodDnsRequests_Type()
)
dnsStatInGoodDnsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsStatInGoodDnsRequests.setStatus("current")
_DnsStatInBadDnsRequests_Type = Counter32
_DnsStatInBadDnsRequests_Object = MibScalar
dnsStatInBadDnsRequests = _DnsStatInBadDnsRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 4, 2),
    _DnsStatInBadDnsRequests_Type()
)
dnsStatInBadDnsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsStatInBadDnsRequests.setStatus("current")
_DnsStatOutDnsRequests_Type = Counter32
_DnsStatOutDnsRequests_Object = MibScalar
dnsStatOutDnsRequests = _DnsStatOutDnsRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 4, 3),
    _DnsStatOutDnsRequests_Type()
)
dnsStatOutDnsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsStatOutDnsRequests.setStatus("current")
_VrrpStats_ObjectIdentity = ObjectIdentity
vrrpStats = _VrrpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 5)
)
_VrrpStatInAdvers_Type = Counter32
_VrrpStatInAdvers_Object = MibScalar
vrrpStatInAdvers = _VrrpStatInAdvers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 5, 1),
    _VrrpStatInAdvers_Type()
)
vrrpStatInAdvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatInAdvers.setStatus("current")
_VrrpStatOutAdvers_Type = Counter32
_VrrpStatOutAdvers_Object = MibScalar
vrrpStatOutAdvers = _VrrpStatOutAdvers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 5, 2),
    _VrrpStatOutAdvers_Type()
)
vrrpStatOutAdvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatOutAdvers.setStatus("current")
_VrrpStatOutBadAdvers_Type = Counter32
_VrrpStatOutBadAdvers_Object = MibScalar
vrrpStatOutBadAdvers = _VrrpStatOutBadAdvers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 5, 3),
    _VrrpStatOutBadAdvers_Type()
)
vrrpStatOutBadAdvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatOutBadAdvers.setStatus("current")
_OspfStats_ObjectIdentity = ObjectIdentity
ospfStats = _OspfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6)
)
_OspfGeneralStats_ObjectIdentity = ObjectIdentity
ospfGeneralStats = _OspfGeneralStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1)
)
_OspfCumRxTxStats_ObjectIdentity = ObjectIdentity
ospfCumRxTxStats = _OspfCumRxTxStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 1)
)
_OspfCumRxPkts_Type = Counter32
_OspfCumRxPkts_Object = MibScalar
ospfCumRxPkts = _OspfCumRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 1, 1),
    _OspfCumRxPkts_Type()
)
ospfCumRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumRxPkts.setStatus("current")
_OspfCumTxPkts_Type = Counter32
_OspfCumTxPkts_Object = MibScalar
ospfCumTxPkts = _OspfCumTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 1, 2),
    _OspfCumTxPkts_Type()
)
ospfCumTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumTxPkts.setStatus("current")
_OspfCumRxHello_Type = Counter32
_OspfCumRxHello_Object = MibScalar
ospfCumRxHello = _OspfCumRxHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 1, 3),
    _OspfCumRxHello_Type()
)
ospfCumRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumRxHello.setStatus("current")
_OspfCumTxHello_Type = Counter32
_OspfCumTxHello_Object = MibScalar
ospfCumTxHello = _OspfCumTxHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 1, 4),
    _OspfCumTxHello_Type()
)
ospfCumTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumTxHello.setStatus("current")
_OspfCumRxDatabase_Type = Counter32
_OspfCumRxDatabase_Object = MibScalar
ospfCumRxDatabase = _OspfCumRxDatabase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 1, 5),
    _OspfCumRxDatabase_Type()
)
ospfCumRxDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumRxDatabase.setStatus("current")
_OspfCumTxDatabase_Type = Counter32
_OspfCumTxDatabase_Object = MibScalar
ospfCumTxDatabase = _OspfCumTxDatabase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 1, 6),
    _OspfCumTxDatabase_Type()
)
ospfCumTxDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumTxDatabase.setStatus("current")
_OspfCumRxlsReqs_Type = Counter32
_OspfCumRxlsReqs_Object = MibScalar
ospfCumRxlsReqs = _OspfCumRxlsReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 1, 7),
    _OspfCumRxlsReqs_Type()
)
ospfCumRxlsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumRxlsReqs.setStatus("current")
_OspfCumTxlsReqs_Type = Counter32
_OspfCumTxlsReqs_Object = MibScalar
ospfCumTxlsReqs = _OspfCumTxlsReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 1, 8),
    _OspfCumTxlsReqs_Type()
)
ospfCumTxlsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumTxlsReqs.setStatus("current")
_OspfCumRxlsAcks_Type = Counter32
_OspfCumRxlsAcks_Object = MibScalar
ospfCumRxlsAcks = _OspfCumRxlsAcks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 1, 9),
    _OspfCumRxlsAcks_Type()
)
ospfCumRxlsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumRxlsAcks.setStatus("current")
_OspfCumTxlsAcks_Type = Counter32
_OspfCumTxlsAcks_Object = MibScalar
ospfCumTxlsAcks = _OspfCumTxlsAcks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 1, 10),
    _OspfCumTxlsAcks_Type()
)
ospfCumTxlsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumTxlsAcks.setStatus("current")
_OspfCumRxlsUpdates_Type = Counter32
_OspfCumRxlsUpdates_Object = MibScalar
ospfCumRxlsUpdates = _OspfCumRxlsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 1, 11),
    _OspfCumRxlsUpdates_Type()
)
ospfCumRxlsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumRxlsUpdates.setStatus("current")
_OspfCumTxlsUpdates_Type = Counter32
_OspfCumTxlsUpdates_Object = MibScalar
ospfCumTxlsUpdates = _OspfCumTxlsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 1, 12),
    _OspfCumTxlsUpdates_Type()
)
ospfCumTxlsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumTxlsUpdates.setStatus("current")
_OspfCumNbrChangeStats_ObjectIdentity = ObjectIdentity
ospfCumNbrChangeStats = _OspfCumNbrChangeStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 2)
)
_OspfCumNbrhello_Type = Counter32
_OspfCumNbrhello_Object = MibScalar
ospfCumNbrhello = _OspfCumNbrhello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 2, 1),
    _OspfCumNbrhello_Type()
)
ospfCumNbrhello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrhello.setStatus("current")
_OspfCumNbrStart_Type = Counter32
_OspfCumNbrStart_Object = MibScalar
ospfCumNbrStart = _OspfCumNbrStart_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 2, 2),
    _OspfCumNbrStart_Type()
)
ospfCumNbrStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrStart.setStatus("current")
_OspfCumNbrAdjointOk_Type = Counter32
_OspfCumNbrAdjointOk_Object = MibScalar
ospfCumNbrAdjointOk = _OspfCumNbrAdjointOk_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 2, 3),
    _OspfCumNbrAdjointOk_Type()
)
ospfCumNbrAdjointOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrAdjointOk.setStatus("current")
_OspfCumNbrNegotiationDone_Type = Counter32
_OspfCumNbrNegotiationDone_Object = MibScalar
ospfCumNbrNegotiationDone = _OspfCumNbrNegotiationDone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 2, 4),
    _OspfCumNbrNegotiationDone_Type()
)
ospfCumNbrNegotiationDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrNegotiationDone.setStatus("current")
_OspfCumNbrExchangeDone_Type = Counter32
_OspfCumNbrExchangeDone_Object = MibScalar
ospfCumNbrExchangeDone = _OspfCumNbrExchangeDone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 2, 5),
    _OspfCumNbrExchangeDone_Type()
)
ospfCumNbrExchangeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrExchangeDone.setStatus("current")
_OspfCumNbrBadRequests_Type = Counter32
_OspfCumNbrBadRequests_Object = MibScalar
ospfCumNbrBadRequests = _OspfCumNbrBadRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 2, 6),
    _OspfCumNbrBadRequests_Type()
)
ospfCumNbrBadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrBadRequests.setStatus("current")
_OspfCumNbrBadSequence_Type = Counter32
_OspfCumNbrBadSequence_Object = MibScalar
ospfCumNbrBadSequence = _OspfCumNbrBadSequence_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 2, 7),
    _OspfCumNbrBadSequence_Type()
)
ospfCumNbrBadSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrBadSequence.setStatus("current")
_OspfCumNbrLoadingDone_Type = Counter32
_OspfCumNbrLoadingDone_Object = MibScalar
ospfCumNbrLoadingDone = _OspfCumNbrLoadingDone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 2, 8),
    _OspfCumNbrLoadingDone_Type()
)
ospfCumNbrLoadingDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrLoadingDone.setStatus("current")
_OspfCumNbrN1way_Type = Counter32
_OspfCumNbrN1way_Object = MibScalar
ospfCumNbrN1way = _OspfCumNbrN1way_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 2, 9),
    _OspfCumNbrN1way_Type()
)
ospfCumNbrN1way.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrN1way.setStatus("current")
_OspfCumNbrRstAd_Type = Counter32
_OspfCumNbrRstAd_Object = MibScalar
ospfCumNbrRstAd = _OspfCumNbrRstAd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 2, 10),
    _OspfCumNbrRstAd_Type()
)
ospfCumNbrRstAd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrRstAd.setStatus("current")
_OspfCumNbrDown_Type = Counter32
_OspfCumNbrDown_Object = MibScalar
ospfCumNbrDown = _OspfCumNbrDown_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 2, 11),
    _OspfCumNbrDown_Type()
)
ospfCumNbrDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrDown.setStatus("current")
_OspfCumNbrN2way_Type = Counter32
_OspfCumNbrN2way_Object = MibScalar
ospfCumNbrN2way = _OspfCumNbrN2way_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 2, 12),
    _OspfCumNbrN2way_Type()
)
ospfCumNbrN2way.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrN2way.setStatus("current")
_OspfCumIntfChangeStats_ObjectIdentity = ObjectIdentity
ospfCumIntfChangeStats = _OspfCumIntfChangeStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 3)
)
_OspfCumIntfHello_Type = Counter32
_OspfCumIntfHello_Object = MibScalar
ospfCumIntfHello = _OspfCumIntfHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 3, 1),
    _OspfCumIntfHello_Type()
)
ospfCumIntfHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfHello.setStatus("current")
_OspfCumIntfDown_Type = Counter32
_OspfCumIntfDown_Object = MibScalar
ospfCumIntfDown = _OspfCumIntfDown_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 3, 2),
    _OspfCumIntfDown_Type()
)
ospfCumIntfDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfDown.setStatus("current")
_OspfCumIntfLoop_Type = Counter32
_OspfCumIntfLoop_Object = MibScalar
ospfCumIntfLoop = _OspfCumIntfLoop_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 3, 3),
    _OspfCumIntfLoop_Type()
)
ospfCumIntfLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfLoop.setStatus("current")
_OspfCumIntfUnloop_Type = Counter32
_OspfCumIntfUnloop_Object = MibScalar
ospfCumIntfUnloop = _OspfCumIntfUnloop_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 3, 4),
    _OspfCumIntfUnloop_Type()
)
ospfCumIntfUnloop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfUnloop.setStatus("current")
_OspfCumIntfWaitTimer_Type = Counter32
_OspfCumIntfWaitTimer_Object = MibScalar
ospfCumIntfWaitTimer = _OspfCumIntfWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 3, 5),
    _OspfCumIntfWaitTimer_Type()
)
ospfCumIntfWaitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfWaitTimer.setStatus("current")
_OspfCumIntfBackup_Type = Counter32
_OspfCumIntfBackup_Object = MibScalar
ospfCumIntfBackup = _OspfCumIntfBackup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 3, 6),
    _OspfCumIntfBackup_Type()
)
ospfCumIntfBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfBackup.setStatus("current")
_OspfCumIntfNbrChange_Type = Counter32
_OspfCumIntfNbrChange_Object = MibScalar
ospfCumIntfNbrChange = _OspfCumIntfNbrChange_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 3, 7),
    _OspfCumIntfNbrChange_Type()
)
ospfCumIntfNbrChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfNbrChange.setStatus("current")
_OspfTimersKickOffStats_ObjectIdentity = ObjectIdentity
ospfTimersKickOffStats = _OspfTimersKickOffStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 4)
)
_OspfTmrsKckOffHello_Type = Counter32
_OspfTmrsKckOffHello_Object = MibScalar
ospfTmrsKckOffHello = _OspfTmrsKckOffHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 4, 1),
    _OspfTmrsKckOffHello_Type()
)
ospfTmrsKckOffHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffHello.setStatus("current")
_OspfTmrsKckOffRetransmit_Type = Counter32
_OspfTmrsKckOffRetransmit_Object = MibScalar
ospfTmrsKckOffRetransmit = _OspfTmrsKckOffRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 4, 2),
    _OspfTmrsKckOffRetransmit_Type()
)
ospfTmrsKckOffRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffRetransmit.setStatus("current")
_OspfTmrsKckOffLsaLock_Type = Counter32
_OspfTmrsKckOffLsaLock_Object = MibScalar
ospfTmrsKckOffLsaLock = _OspfTmrsKckOffLsaLock_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 4, 3),
    _OspfTmrsKckOffLsaLock_Type()
)
ospfTmrsKckOffLsaLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffLsaLock.setStatus("current")
_OspfTmrsKckOffLsaAck_Type = Counter32
_OspfTmrsKckOffLsaAck_Object = MibScalar
ospfTmrsKckOffLsaAck = _OspfTmrsKckOffLsaAck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 4, 4),
    _OspfTmrsKckOffLsaAck_Type()
)
ospfTmrsKckOffLsaAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffLsaAck.setStatus("current")
_OspfTmrsKckOffDbage_Type = Counter32
_OspfTmrsKckOffDbage_Object = MibScalar
ospfTmrsKckOffDbage = _OspfTmrsKckOffDbage_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 4, 5),
    _OspfTmrsKckOffDbage_Type()
)
ospfTmrsKckOffDbage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffDbage.setStatus("current")
_OspfTmrsKckOffSummary_Type = Counter32
_OspfTmrsKckOffSummary_Object = MibScalar
ospfTmrsKckOffSummary = _OspfTmrsKckOffSummary_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 4, 6),
    _OspfTmrsKckOffSummary_Type()
)
ospfTmrsKckOffSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffSummary.setStatus("current")
_OspfTmrsKckOffAseExport_Type = Counter32
_OspfTmrsKckOffAseExport_Object = MibScalar
ospfTmrsKckOffAseExport = _OspfTmrsKckOffAseExport_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 1, 4, 7),
    _OspfTmrsKckOffAseExport_Type()
)
ospfTmrsKckOffAseExport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffAseExport.setStatus("current")
_OspfArea_ObjectIdentity = ObjectIdentity
ospfArea = _OspfArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2)
)
_OspfAreaRxTxStats_Object = MibTable
ospfAreaRxTxStats = _OspfAreaRxTxStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    ospfAreaRxTxStats.setStatus("current")
_OspfAreaRxTxStatsEntry_Object = MibTableRow
ospfAreaRxTxStatsEntry = _OspfAreaRxTxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 1, 1)
)
ospfAreaRxTxStatsEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfAreaRxTxIndex"),
)
if mibBuilder.loadTexts:
    ospfAreaRxTxStatsEntry.setStatus("current")
_OspfAreaRxTxIndex_Type = Integer32
_OspfAreaRxTxIndex_Object = MibTableColumn
ospfAreaRxTxIndex = _OspfAreaRxTxIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 1, 1, 1),
    _OspfAreaRxTxIndex_Type()
)
ospfAreaRxTxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxTxIndex.setStatus("current")
_OspfAreaRxPkts_Type = Counter32
_OspfAreaRxPkts_Object = MibTableColumn
ospfAreaRxPkts = _OspfAreaRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 1, 1, 2),
    _OspfAreaRxPkts_Type()
)
ospfAreaRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxPkts.setStatus("current")
_OspfAreaTxPkts_Type = Counter32
_OspfAreaTxPkts_Object = MibTableColumn
ospfAreaTxPkts = _OspfAreaTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 1, 1, 3),
    _OspfAreaTxPkts_Type()
)
ospfAreaTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTxPkts.setStatus("current")
_OspfAreaRxHello_Type = Counter32
_OspfAreaRxHello_Object = MibTableColumn
ospfAreaRxHello = _OspfAreaRxHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 1, 1, 4),
    _OspfAreaRxHello_Type()
)
ospfAreaRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxHello.setStatus("current")
_OspfAreaTxHello_Type = Counter32
_OspfAreaTxHello_Object = MibTableColumn
ospfAreaTxHello = _OspfAreaTxHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 1, 1, 5),
    _OspfAreaTxHello_Type()
)
ospfAreaTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTxHello.setStatus("current")
_OspfAreaRxDatabase_Type = Counter32
_OspfAreaRxDatabase_Object = MibTableColumn
ospfAreaRxDatabase = _OspfAreaRxDatabase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 1, 1, 6),
    _OspfAreaRxDatabase_Type()
)
ospfAreaRxDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxDatabase.setStatus("current")
_OspfAreaTxDatabase_Type = Counter32
_OspfAreaTxDatabase_Object = MibTableColumn
ospfAreaTxDatabase = _OspfAreaTxDatabase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 1, 1, 7),
    _OspfAreaTxDatabase_Type()
)
ospfAreaTxDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTxDatabase.setStatus("current")
_OspfAreaRxlsReqs_Type = Counter32
_OspfAreaRxlsReqs_Object = MibTableColumn
ospfAreaRxlsReqs = _OspfAreaRxlsReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 1, 1, 8),
    _OspfAreaRxlsReqs_Type()
)
ospfAreaRxlsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxlsReqs.setStatus("current")
_OspfAreaTxlsReqs_Type = Counter32
_OspfAreaTxlsReqs_Object = MibTableColumn
ospfAreaTxlsReqs = _OspfAreaTxlsReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 1, 1, 9),
    _OspfAreaTxlsReqs_Type()
)
ospfAreaTxlsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTxlsReqs.setStatus("current")
_OspfAreaRxlsAcks_Type = Counter32
_OspfAreaRxlsAcks_Object = MibTableColumn
ospfAreaRxlsAcks = _OspfAreaRxlsAcks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 1, 1, 10),
    _OspfAreaRxlsAcks_Type()
)
ospfAreaRxlsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxlsAcks.setStatus("current")
_OspfAreaTxlsAcks_Type = Counter32
_OspfAreaTxlsAcks_Object = MibTableColumn
ospfAreaTxlsAcks = _OspfAreaTxlsAcks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 1, 1, 11),
    _OspfAreaTxlsAcks_Type()
)
ospfAreaTxlsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTxlsAcks.setStatus("current")
_OspfAreaRxlsUpdates_Type = Counter32
_OspfAreaRxlsUpdates_Object = MibTableColumn
ospfAreaRxlsUpdates = _OspfAreaRxlsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 1, 1, 12),
    _OspfAreaRxlsUpdates_Type()
)
ospfAreaRxlsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxlsUpdates.setStatus("current")
_OspfAreaTxlsUpdates_Type = Counter32
_OspfAreaTxlsUpdates_Object = MibTableColumn
ospfAreaTxlsUpdates = _OspfAreaTxlsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 1, 1, 13),
    _OspfAreaTxlsUpdates_Type()
)
ospfAreaTxlsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTxlsUpdates.setStatus("current")
_OspfAreaNbrChangeStats_Object = MibTable
ospfAreaNbrChangeStats = _OspfAreaNbrChangeStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 2)
)
if mibBuilder.loadTexts:
    ospfAreaNbrChangeStats.setStatus("current")
_OspfAreaNbrChangeStatsEntry_Object = MibTableRow
ospfAreaNbrChangeStatsEntry = _OspfAreaNbrChangeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 2, 1)
)
ospfAreaNbrChangeStatsEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfAreaNbrIndex"),
)
if mibBuilder.loadTexts:
    ospfAreaNbrChangeStatsEntry.setStatus("current")
_OspfAreaNbrIndex_Type = Integer32
_OspfAreaNbrIndex_Object = MibTableColumn
ospfAreaNbrIndex = _OspfAreaNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 2, 1, 1),
    _OspfAreaNbrIndex_Type()
)
ospfAreaNbrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrIndex.setStatus("current")
_OspfAreaNbrhello_Type = Counter32
_OspfAreaNbrhello_Object = MibTableColumn
ospfAreaNbrhello = _OspfAreaNbrhello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 2, 1, 2),
    _OspfAreaNbrhello_Type()
)
ospfAreaNbrhello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrhello.setStatus("current")
_OspfAreaNbrStart_Type = Counter32
_OspfAreaNbrStart_Object = MibTableColumn
ospfAreaNbrStart = _OspfAreaNbrStart_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 2, 1, 3),
    _OspfAreaNbrStart_Type()
)
ospfAreaNbrStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrStart.setStatus("current")
_OspfAreaNbrAdjointOk_Type = Counter32
_OspfAreaNbrAdjointOk_Object = MibTableColumn
ospfAreaNbrAdjointOk = _OspfAreaNbrAdjointOk_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 2, 1, 4),
    _OspfAreaNbrAdjointOk_Type()
)
ospfAreaNbrAdjointOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrAdjointOk.setStatus("current")
_OspfAreaNbrNegotiationDone_Type = Counter32
_OspfAreaNbrNegotiationDone_Object = MibTableColumn
ospfAreaNbrNegotiationDone = _OspfAreaNbrNegotiationDone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 2, 1, 5),
    _OspfAreaNbrNegotiationDone_Type()
)
ospfAreaNbrNegotiationDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrNegotiationDone.setStatus("current")
_OspfAreaNbrExchangeDone_Type = Counter32
_OspfAreaNbrExchangeDone_Object = MibTableColumn
ospfAreaNbrExchangeDone = _OspfAreaNbrExchangeDone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 2, 1, 6),
    _OspfAreaNbrExchangeDone_Type()
)
ospfAreaNbrExchangeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrExchangeDone.setStatus("current")
_OspfAreaNbrBadRequests_Type = Counter32
_OspfAreaNbrBadRequests_Object = MibTableColumn
ospfAreaNbrBadRequests = _OspfAreaNbrBadRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 2, 1, 7),
    _OspfAreaNbrBadRequests_Type()
)
ospfAreaNbrBadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrBadRequests.setStatus("current")
_OspfAreaNbrBadSequence_Type = Counter32
_OspfAreaNbrBadSequence_Object = MibTableColumn
ospfAreaNbrBadSequence = _OspfAreaNbrBadSequence_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 2, 1, 8),
    _OspfAreaNbrBadSequence_Type()
)
ospfAreaNbrBadSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrBadSequence.setStatus("current")
_OspfAreaNbrLoadingDone_Type = Counter32
_OspfAreaNbrLoadingDone_Object = MibTableColumn
ospfAreaNbrLoadingDone = _OspfAreaNbrLoadingDone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 2, 1, 9),
    _OspfAreaNbrLoadingDone_Type()
)
ospfAreaNbrLoadingDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrLoadingDone.setStatus("current")
_OspfAreaNbrN1way_Type = Counter32
_OspfAreaNbrN1way_Object = MibTableColumn
ospfAreaNbrN1way = _OspfAreaNbrN1way_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 2, 1, 10),
    _OspfAreaNbrN1way_Type()
)
ospfAreaNbrN1way.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrN1way.setStatus("current")
_OspfAreaNbrRstAd_Type = Counter32
_OspfAreaNbrRstAd_Object = MibTableColumn
ospfAreaNbrRstAd = _OspfAreaNbrRstAd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 2, 1, 11),
    _OspfAreaNbrRstAd_Type()
)
ospfAreaNbrRstAd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrRstAd.setStatus("current")
_OspfAreaNbrDown_Type = Counter32
_OspfAreaNbrDown_Object = MibTableColumn
ospfAreaNbrDown = _OspfAreaNbrDown_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 2, 1, 12),
    _OspfAreaNbrDown_Type()
)
ospfAreaNbrDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrDown.setStatus("current")
_OspfAreaNbrN2way_Type = Counter32
_OspfAreaNbrN2way_Object = MibTableColumn
ospfAreaNbrN2way = _OspfAreaNbrN2way_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 2, 1, 13),
    _OspfAreaNbrN2way_Type()
)
ospfAreaNbrN2way.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrN2way.setStatus("current")
_OspfAreaChangeStats_Object = MibTable
ospfAreaChangeStats = _OspfAreaChangeStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 3)
)
if mibBuilder.loadTexts:
    ospfAreaChangeStats.setStatus("current")
_OspfAreaChangeStatsEntry_Object = MibTableRow
ospfAreaChangeStatsEntry = _OspfAreaChangeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 3, 1)
)
ospfAreaChangeStatsEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfAreaIntfIndex"),
)
if mibBuilder.loadTexts:
    ospfAreaChangeStatsEntry.setStatus("current")
_OspfAreaIntfIndex_Type = Integer32
_OspfAreaIntfIndex_Object = MibTableColumn
ospfAreaIntfIndex = _OspfAreaIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 3, 1, 1),
    _OspfAreaIntfIndex_Type()
)
ospfAreaIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfIndex.setStatus("current")
_OspfAreaIntfHello_Type = Counter32
_OspfAreaIntfHello_Object = MibTableColumn
ospfAreaIntfHello = _OspfAreaIntfHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 3, 1, 2),
    _OspfAreaIntfHello_Type()
)
ospfAreaIntfHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfHello.setStatus("current")
_OspfAreaIntfDown_Type = Counter32
_OspfAreaIntfDown_Object = MibTableColumn
ospfAreaIntfDown = _OspfAreaIntfDown_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 3, 1, 3),
    _OspfAreaIntfDown_Type()
)
ospfAreaIntfDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfDown.setStatus("current")
_OspfAreaIntfLoop_Type = Counter32
_OspfAreaIntfLoop_Object = MibTableColumn
ospfAreaIntfLoop = _OspfAreaIntfLoop_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 3, 1, 4),
    _OspfAreaIntfLoop_Type()
)
ospfAreaIntfLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfLoop.setStatus("current")
_OspfAreaIntfUnloop_Type = Counter32
_OspfAreaIntfUnloop_Object = MibTableColumn
ospfAreaIntfUnloop = _OspfAreaIntfUnloop_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 3, 1, 5),
    _OspfAreaIntfUnloop_Type()
)
ospfAreaIntfUnloop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfUnloop.setStatus("current")
_OspfAreaIntfWaitTimer_Type = Counter32
_OspfAreaIntfWaitTimer_Object = MibTableColumn
ospfAreaIntfWaitTimer = _OspfAreaIntfWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 3, 1, 6),
    _OspfAreaIntfWaitTimer_Type()
)
ospfAreaIntfWaitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfWaitTimer.setStatus("current")
_OspfAreaIntfBackup_Type = Counter32
_OspfAreaIntfBackup_Object = MibTableColumn
ospfAreaIntfBackup = _OspfAreaIntfBackup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 3, 1, 7),
    _OspfAreaIntfBackup_Type()
)
ospfAreaIntfBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfBackup.setStatus("current")
_OspfAreaIntfNbrChange_Type = Counter32
_OspfAreaIntfNbrChange_Object = MibTableColumn
ospfAreaIntfNbrChange = _OspfAreaIntfNbrChange_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 3, 1, 8),
    _OspfAreaIntfNbrChange_Type()
)
ospfAreaIntfNbrChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfNbrChange.setStatus("current")
_OspfAreaErrorStats_Object = MibTable
ospfAreaErrorStats = _OspfAreaErrorStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 4)
)
if mibBuilder.loadTexts:
    ospfAreaErrorStats.setStatus("current")
_OspfAreaErrorStatsEntry_Object = MibTableRow
ospfAreaErrorStatsEntry = _OspfAreaErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 4, 1)
)
ospfAreaErrorStatsEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfAreaErrIndex"),
)
if mibBuilder.loadTexts:
    ospfAreaErrorStatsEntry.setStatus("current")
_OspfAreaErrIndex_Type = Integer32
_OspfAreaErrIndex_Object = MibTableColumn
ospfAreaErrIndex = _OspfAreaErrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 4, 1, 1),
    _OspfAreaErrIndex_Type()
)
ospfAreaErrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaErrIndex.setStatus("current")
_OspfAreaErrAuthFailure_Type = Counter32
_OspfAreaErrAuthFailure_Object = MibTableColumn
ospfAreaErrAuthFailure = _OspfAreaErrAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 4, 1, 2),
    _OspfAreaErrAuthFailure_Type()
)
ospfAreaErrAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaErrAuthFailure.setStatus("current")
_OspfAreaErrNetmaskMismatch_Type = Counter32
_OspfAreaErrNetmaskMismatch_Object = MibTableColumn
ospfAreaErrNetmaskMismatch = _OspfAreaErrNetmaskMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 4, 1, 3),
    _OspfAreaErrNetmaskMismatch_Type()
)
ospfAreaErrNetmaskMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaErrNetmaskMismatch.setStatus("current")
_OspfAreaErrHelloMismatch_Type = Counter32
_OspfAreaErrHelloMismatch_Object = MibTableColumn
ospfAreaErrHelloMismatch = _OspfAreaErrHelloMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 4, 1, 4),
    _OspfAreaErrHelloMismatch_Type()
)
ospfAreaErrHelloMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaErrHelloMismatch.setStatus("current")
_OspfAreaErrDeadMismatch_Type = Counter32
_OspfAreaErrDeadMismatch_Object = MibTableColumn
ospfAreaErrDeadMismatch = _OspfAreaErrDeadMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 4, 1, 5),
    _OspfAreaErrDeadMismatch_Type()
)
ospfAreaErrDeadMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaErrDeadMismatch.setStatus("current")
_OspfAreaErrOptionsMismatch_Type = Counter32
_OspfAreaErrOptionsMismatch_Object = MibTableColumn
ospfAreaErrOptionsMismatch = _OspfAreaErrOptionsMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 4, 1, 6),
    _OspfAreaErrOptionsMismatch_Type()
)
ospfAreaErrOptionsMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaErrOptionsMismatch.setStatus("current")
_OspfAreaErrUnknownNbr_Type = Counter32
_OspfAreaErrUnknownNbr_Object = MibTableColumn
ospfAreaErrUnknownNbr = _OspfAreaErrUnknownNbr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 2, 4, 1, 7),
    _OspfAreaErrUnknownNbr_Type()
)
ospfAreaErrUnknownNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaErrUnknownNbr.setStatus("current")
_OspfInterface_ObjectIdentity = ObjectIdentity
ospfInterface = _OspfInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3)
)
_OspfIntfRxTxStats_Object = MibTable
ospfIntfRxTxStats = _OspfIntfRxTxStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    ospfIntfRxTxStats.setStatus("current")
_OspfIntfRxTxStatsEntry_Object = MibTableRow
ospfIntfRxTxStatsEntry = _OspfIntfRxTxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 1, 1)
)
ospfIntfRxTxStatsEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfIntfRxTxIndex"),
)
if mibBuilder.loadTexts:
    ospfIntfRxTxStatsEntry.setStatus("current")
_OspfIntfRxTxIndex_Type = Integer32
_OspfIntfRxTxIndex_Object = MibTableColumn
ospfIntfRxTxIndex = _OspfIntfRxTxIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 1, 1, 1),
    _OspfIntfRxTxIndex_Type()
)
ospfIntfRxTxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxTxIndex.setStatus("current")
_OspfIntfRxPkts_Type = Counter32
_OspfIntfRxPkts_Object = MibTableColumn
ospfIntfRxPkts = _OspfIntfRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 1, 1, 2),
    _OspfIntfRxPkts_Type()
)
ospfIntfRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxPkts.setStatus("current")
_OspfIntfTxPkts_Type = Counter32
_OspfIntfTxPkts_Object = MibTableColumn
ospfIntfTxPkts = _OspfIntfTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 1, 1, 3),
    _OspfIntfTxPkts_Type()
)
ospfIntfTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTxPkts.setStatus("current")
_OspfIntfRxHello_Type = Counter32
_OspfIntfRxHello_Object = MibTableColumn
ospfIntfRxHello = _OspfIntfRxHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 1, 1, 4),
    _OspfIntfRxHello_Type()
)
ospfIntfRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxHello.setStatus("current")
_OspfIntfTxHello_Type = Counter32
_OspfIntfTxHello_Object = MibTableColumn
ospfIntfTxHello = _OspfIntfTxHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 1, 1, 5),
    _OspfIntfTxHello_Type()
)
ospfIntfTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTxHello.setStatus("current")
_OspfIntfRxDatabase_Type = Counter32
_OspfIntfRxDatabase_Object = MibTableColumn
ospfIntfRxDatabase = _OspfIntfRxDatabase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 1, 1, 6),
    _OspfIntfRxDatabase_Type()
)
ospfIntfRxDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxDatabase.setStatus("current")
_OspfIntfTxDatabase_Type = Counter32
_OspfIntfTxDatabase_Object = MibTableColumn
ospfIntfTxDatabase = _OspfIntfTxDatabase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 1, 1, 7),
    _OspfIntfTxDatabase_Type()
)
ospfIntfTxDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTxDatabase.setStatus("current")
_OspfIntfRxlsReqs_Type = Counter32
_OspfIntfRxlsReqs_Object = MibTableColumn
ospfIntfRxlsReqs = _OspfIntfRxlsReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 1, 1, 8),
    _OspfIntfRxlsReqs_Type()
)
ospfIntfRxlsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxlsReqs.setStatus("current")
_OspfIntfTxlsReqs_Type = Counter32
_OspfIntfTxlsReqs_Object = MibTableColumn
ospfIntfTxlsReqs = _OspfIntfTxlsReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 1, 1, 9),
    _OspfIntfTxlsReqs_Type()
)
ospfIntfTxlsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTxlsReqs.setStatus("current")
_OspfIntfRxlsAcks_Type = Counter32
_OspfIntfRxlsAcks_Object = MibTableColumn
ospfIntfRxlsAcks = _OspfIntfRxlsAcks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 1, 1, 10),
    _OspfIntfRxlsAcks_Type()
)
ospfIntfRxlsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxlsAcks.setStatus("current")
_OspfIntfTxlsAcks_Type = Counter32
_OspfIntfTxlsAcks_Object = MibTableColumn
ospfIntfTxlsAcks = _OspfIntfTxlsAcks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 1, 1, 11),
    _OspfIntfTxlsAcks_Type()
)
ospfIntfTxlsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTxlsAcks.setStatus("current")
_OspfIntfRxlsUpdates_Type = Counter32
_OspfIntfRxlsUpdates_Object = MibTableColumn
ospfIntfRxlsUpdates = _OspfIntfRxlsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 1, 1, 12),
    _OspfIntfRxlsUpdates_Type()
)
ospfIntfRxlsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxlsUpdates.setStatus("current")
_OspfIntfTxlsUpdates_Type = Counter32
_OspfIntfTxlsUpdates_Object = MibTableColumn
ospfIntfTxlsUpdates = _OspfIntfTxlsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 1, 1, 13),
    _OspfIntfTxlsUpdates_Type()
)
ospfIntfTxlsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTxlsUpdates.setStatus("current")
_OspfIntfNbrChangeStats_Object = MibTable
ospfIntfNbrChangeStats = _OspfIntfNbrChangeStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 2)
)
if mibBuilder.loadTexts:
    ospfIntfNbrChangeStats.setStatus("current")
_OspfIntfNbrChangeStatsEntry_Object = MibTableRow
ospfIntfNbrChangeStatsEntry = _OspfIntfNbrChangeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 2, 1)
)
ospfIntfNbrChangeStatsEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfIntfNbrIndex"),
)
if mibBuilder.loadTexts:
    ospfIntfNbrChangeStatsEntry.setStatus("current")
_OspfIntfNbrIndex_Type = Integer32
_OspfIntfNbrIndex_Object = MibTableColumn
ospfIntfNbrIndex = _OspfIntfNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 2, 1, 1),
    _OspfIntfNbrIndex_Type()
)
ospfIntfNbrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrIndex.setStatus("current")
_OspfIntfNbrhello_Type = Counter32
_OspfIntfNbrhello_Object = MibTableColumn
ospfIntfNbrhello = _OspfIntfNbrhello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 2, 1, 2),
    _OspfIntfNbrhello_Type()
)
ospfIntfNbrhello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrhello.setStatus("current")
_OspfIntfNbrStart_Type = Counter32
_OspfIntfNbrStart_Object = MibTableColumn
ospfIntfNbrStart = _OspfIntfNbrStart_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 2, 1, 3),
    _OspfIntfNbrStart_Type()
)
ospfIntfNbrStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrStart.setStatus("current")
_OspfIntfNbrAdjointOk_Type = Counter32
_OspfIntfNbrAdjointOk_Object = MibTableColumn
ospfIntfNbrAdjointOk = _OspfIntfNbrAdjointOk_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 2, 1, 4),
    _OspfIntfNbrAdjointOk_Type()
)
ospfIntfNbrAdjointOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrAdjointOk.setStatus("current")
_OspfIntfNbrNegotiationDone_Type = Counter32
_OspfIntfNbrNegotiationDone_Object = MibTableColumn
ospfIntfNbrNegotiationDone = _OspfIntfNbrNegotiationDone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 2, 1, 5),
    _OspfIntfNbrNegotiationDone_Type()
)
ospfIntfNbrNegotiationDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrNegotiationDone.setStatus("current")
_OspfIntfNbrExchangeDone_Type = Counter32
_OspfIntfNbrExchangeDone_Object = MibTableColumn
ospfIntfNbrExchangeDone = _OspfIntfNbrExchangeDone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 2, 1, 6),
    _OspfIntfNbrExchangeDone_Type()
)
ospfIntfNbrExchangeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrExchangeDone.setStatus("current")
_OspfIntfNbrBadRequests_Type = Counter32
_OspfIntfNbrBadRequests_Object = MibTableColumn
ospfIntfNbrBadRequests = _OspfIntfNbrBadRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 2, 1, 7),
    _OspfIntfNbrBadRequests_Type()
)
ospfIntfNbrBadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrBadRequests.setStatus("current")
_OspfIntfNbrBadSequence_Type = Counter32
_OspfIntfNbrBadSequence_Object = MibTableColumn
ospfIntfNbrBadSequence = _OspfIntfNbrBadSequence_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 2, 1, 8),
    _OspfIntfNbrBadSequence_Type()
)
ospfIntfNbrBadSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrBadSequence.setStatus("current")
_OspfIntfNbrLoadingDone_Type = Counter32
_OspfIntfNbrLoadingDone_Object = MibTableColumn
ospfIntfNbrLoadingDone = _OspfIntfNbrLoadingDone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 2, 1, 9),
    _OspfIntfNbrLoadingDone_Type()
)
ospfIntfNbrLoadingDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrLoadingDone.setStatus("current")
_OspfIntfNbrN1way_Type = Counter32
_OspfIntfNbrN1way_Object = MibTableColumn
ospfIntfNbrN1way = _OspfIntfNbrN1way_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 2, 1, 10),
    _OspfIntfNbrN1way_Type()
)
ospfIntfNbrN1way.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrN1way.setStatus("current")
_OspfIntfNbrRstAd_Type = Counter32
_OspfIntfNbrRstAd_Object = MibTableColumn
ospfIntfNbrRstAd = _OspfIntfNbrRstAd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 2, 1, 11),
    _OspfIntfNbrRstAd_Type()
)
ospfIntfNbrRstAd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrRstAd.setStatus("current")
_OspfIntfNbrDown_Type = Counter32
_OspfIntfNbrDown_Object = MibTableColumn
ospfIntfNbrDown = _OspfIntfNbrDown_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 2, 1, 12),
    _OspfIntfNbrDown_Type()
)
ospfIntfNbrDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrDown.setStatus("current")
_OspfIntfNbrN2way_Type = Counter32
_OspfIntfNbrN2way_Object = MibTableColumn
ospfIntfNbrN2way = _OspfIntfNbrN2way_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 2, 1, 13),
    _OspfIntfNbrN2way_Type()
)
ospfIntfNbrN2way.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrN2way.setStatus("current")
_OspfIntfChangeStats_Object = MibTable
ospfIntfChangeStats = _OspfIntfChangeStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 3)
)
if mibBuilder.loadTexts:
    ospfIntfChangeStats.setStatus("current")
_OspfIntfChangeStatsEntry_Object = MibTableRow
ospfIntfChangeStatsEntry = _OspfIntfChangeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 3, 1)
)
ospfIntfChangeStatsEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfIntfIndex"),
)
if mibBuilder.loadTexts:
    ospfIntfChangeStatsEntry.setStatus("current")
_OspfIntfIndex_Type = Integer32
_OspfIntfIndex_Object = MibTableColumn
ospfIntfIndex = _OspfIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 3, 1, 1),
    _OspfIntfIndex_Type()
)
ospfIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfIndex.setStatus("current")
_OspfIntfHello_Type = Counter32
_OspfIntfHello_Object = MibTableColumn
ospfIntfHello = _OspfIntfHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 3, 1, 2),
    _OspfIntfHello_Type()
)
ospfIntfHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfHello.setStatus("current")
_OspfIntfDown_Type = Counter32
_OspfIntfDown_Object = MibTableColumn
ospfIntfDown = _OspfIntfDown_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 3, 1, 3),
    _OspfIntfDown_Type()
)
ospfIntfDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfDown.setStatus("current")
_OspfIntfLoop_Type = Counter32
_OspfIntfLoop_Object = MibTableColumn
ospfIntfLoop = _OspfIntfLoop_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 3, 1, 4),
    _OspfIntfLoop_Type()
)
ospfIntfLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfLoop.setStatus("current")
_OspfIntfUnloop_Type = Counter32
_OspfIntfUnloop_Object = MibTableColumn
ospfIntfUnloop = _OspfIntfUnloop_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 3, 1, 5),
    _OspfIntfUnloop_Type()
)
ospfIntfUnloop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfUnloop.setStatus("current")
_OspfIntfWaitTimer_Type = Counter32
_OspfIntfWaitTimer_Object = MibTableColumn
ospfIntfWaitTimer = _OspfIntfWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 3, 1, 6),
    _OspfIntfWaitTimer_Type()
)
ospfIntfWaitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfWaitTimer.setStatus("current")
_OspfIntfBackup_Type = Counter32
_OspfIntfBackup_Object = MibTableColumn
ospfIntfBackup = _OspfIntfBackup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 3, 1, 7),
    _OspfIntfBackup_Type()
)
ospfIntfBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfBackup.setStatus("current")
_OspfIntfNbrChange_Type = Counter32
_OspfIntfNbrChange_Object = MibTableColumn
ospfIntfNbrChange = _OspfIntfNbrChange_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 3, 1, 8),
    _OspfIntfNbrChange_Type()
)
ospfIntfNbrChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrChange.setStatus("current")
_OspfIntfErrorStats_Object = MibTable
ospfIntfErrorStats = _OspfIntfErrorStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 4)
)
if mibBuilder.loadTexts:
    ospfIntfErrorStats.setStatus("current")
_OspfIntfErrorStatsEntry_Object = MibTableRow
ospfIntfErrorStatsEntry = _OspfIntfErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 4, 1)
)
ospfIntfErrorStatsEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfIntfErrIndex"),
)
if mibBuilder.loadTexts:
    ospfIntfErrorStatsEntry.setStatus("current")
_OspfIntfErrIndex_Type = Integer32
_OspfIntfErrIndex_Object = MibTableColumn
ospfIntfErrIndex = _OspfIntfErrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 4, 1, 1),
    _OspfIntfErrIndex_Type()
)
ospfIntfErrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfErrIndex.setStatus("current")
_OspfIntfErrAuthFailure_Type = Counter32
_OspfIntfErrAuthFailure_Object = MibTableColumn
ospfIntfErrAuthFailure = _OspfIntfErrAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 4, 1, 2),
    _OspfIntfErrAuthFailure_Type()
)
ospfIntfErrAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfErrAuthFailure.setStatus("current")
_OspfIntfErrNetmaskMismatch_Type = Counter32
_OspfIntfErrNetmaskMismatch_Object = MibTableColumn
ospfIntfErrNetmaskMismatch = _OspfIntfErrNetmaskMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 4, 1, 3),
    _OspfIntfErrNetmaskMismatch_Type()
)
ospfIntfErrNetmaskMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfErrNetmaskMismatch.setStatus("current")
_OspfIntfErrHelloMismatch_Type = Counter32
_OspfIntfErrHelloMismatch_Object = MibTableColumn
ospfIntfErrHelloMismatch = _OspfIntfErrHelloMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 4, 1, 4),
    _OspfIntfErrHelloMismatch_Type()
)
ospfIntfErrHelloMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfErrHelloMismatch.setStatus("current")
_OspfIntfErrDeadMismatch_Type = Counter32
_OspfIntfErrDeadMismatch_Object = MibTableColumn
ospfIntfErrDeadMismatch = _OspfIntfErrDeadMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 4, 1, 5),
    _OspfIntfErrDeadMismatch_Type()
)
ospfIntfErrDeadMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfErrDeadMismatch.setStatus("current")
_OspfIntfErrOptionsMismatch_Type = Counter32
_OspfIntfErrOptionsMismatch_Object = MibTableColumn
ospfIntfErrOptionsMismatch = _OspfIntfErrOptionsMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 4, 1, 6),
    _OspfIntfErrOptionsMismatch_Type()
)
ospfIntfErrOptionsMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfErrOptionsMismatch.setStatus("current")
_OspfIntfErrUnknownNbr_Type = Counter32
_OspfIntfErrUnknownNbr_Object = MibTableColumn
ospfIntfErrUnknownNbr = _OspfIntfErrUnknownNbr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 6, 3, 4, 1, 7),
    _OspfIntfErrUnknownNbr_Type()
)
ospfIntfErrUnknownNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfErrUnknownNbr.setStatus("current")
_ClearStats_ObjectIdentity = ObjectIdentity
clearStats = _ClearStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 7)
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
        *(("clear", 2),
          ("ok", 1))
    )


_IpClearStats_Type.__name__ = "Integer32"
_IpClearStats_Object = MibScalar
ipClearStats = _IpClearStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 7, 1),
    _IpClearStats_Type()
)
ipClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipClearStats.setStatus("current")
_IfStatsTable_Object = MibTable
ifStatsTable = _IfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 7, 2)
)
if mibBuilder.loadTexts:
    ifStatsTable.setStatus("current")
_IfStatsEntry_Object = MibTableRow
ifStatsEntry = _IfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 7, 2, 1)
)
ifStatsEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ifStatsIndex"),
)
if mibBuilder.loadTexts:
    ifStatsEntry.setStatus("current")
_IfStatsIndex_Type = Integer32
_IfStatsIndex_Object = MibTableColumn
ifStatsIndex = _IfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 7, 2, 1, 1),
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
        *(("clear", 2),
          ("ok", 1))
    )


_IfClearStats_Type.__name__ = "Integer32"
_IfClearStats_Object = MibTableColumn
ifClearStats = _IfClearStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 7, 2, 1, 2),
    _IfClearStats_Type()
)
ifClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifClearStats.setStatus("current")
_Ip6Stats_ObjectIdentity = ObjectIdentity
ip6Stats = _Ip6Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 10)
)
_Ip6InReceives_Type = Counter32
_Ip6InReceives_Object = MibScalar
ip6InReceives = _Ip6InReceives_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 10, 1),
    _Ip6InReceives_Type()
)
ip6InReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6InReceives.setStatus("current")
_Ip6ForwDatagrams_Type = Counter32
_Ip6ForwDatagrams_Object = MibScalar
ip6ForwDatagrams = _Ip6ForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 10, 2),
    _Ip6ForwDatagrams_Type()
)
ip6ForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6ForwDatagrams.setStatus("current")
_Ip6InDelivers_Type = Counter32
_Ip6InDelivers_Object = MibScalar
ip6InDelivers = _Ip6InDelivers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 10, 3),
    _Ip6InDelivers_Type()
)
ip6InDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6InDelivers.setStatus("current")
_Ip6InDiscards_Type = Counter32
_Ip6InDiscards_Object = MibScalar
ip6InDiscards = _Ip6InDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 10, 4),
    _Ip6InDiscards_Type()
)
ip6InDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6InDiscards.setStatus("current")
_Ip6InUnknownProtos_Type = Counter32
_Ip6InUnknownProtos_Object = MibScalar
ip6InUnknownProtos = _Ip6InUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 10, 5),
    _Ip6InUnknownProtos_Type()
)
ip6InUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6InUnknownProtos.setStatus("current")
_Ip6InAddrErrors_Type = Counter32
_Ip6InAddrErrors_Object = MibScalar
ip6InAddrErrors = _Ip6InAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 10, 6),
    _Ip6InAddrErrors_Type()
)
ip6InAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6InAddrErrors.setStatus("current")
_Ip6OutRequests_Type = Counter32
_Ip6OutRequests_Object = MibScalar
ip6OutRequests = _Ip6OutRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 10, 7),
    _Ip6OutRequests_Type()
)
ip6OutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6OutRequests.setStatus("current")
_Ip6OutNoRoutes_Type = Counter32
_Ip6OutNoRoutes_Object = MibScalar
ip6OutNoRoutes = _Ip6OutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 10, 8),
    _Ip6OutNoRoutes_Type()
)
ip6OutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6OutNoRoutes.setStatus("current")
_Ip6ReasmOKs_Type = Counter32
_Ip6ReasmOKs_Object = MibScalar
ip6ReasmOKs = _Ip6ReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 10, 9),
    _Ip6ReasmOKs_Type()
)
ip6ReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6ReasmOKs.setStatus("current")
_Ip6ReasmFails_Type = Counter32
_Ip6ReasmFails_Object = MibScalar
ip6ReasmFails = _Ip6ReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 10, 10),
    _Ip6ReasmFails_Type()
)
ip6ReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6ReasmFails.setStatus("current")
_Ip6icmpInMsgs_Type = Counter32
_Ip6icmpInMsgs_Object = MibScalar
ip6icmpInMsgs = _Ip6icmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 10, 11),
    _Ip6icmpInMsgs_Type()
)
ip6icmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6icmpInMsgs.setStatus("current")
_Ip6icmpOutMsgs_Type = Counter32
_Ip6icmpOutMsgs_Object = MibScalar
ip6icmpOutMsgs = _Ip6icmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 10, 12),
    _Ip6icmpOutMsgs_Type()
)
ip6icmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6icmpOutMsgs.setStatus("current")
_Ip6icmpInErrors_Type = Counter32
_Ip6icmpInErrors_Object = MibScalar
ip6icmpInErrors = _Ip6icmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 10, 13),
    _Ip6icmpInErrors_Type()
)
ip6icmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6icmpInErrors.setStatus("current")
_Ip6icmpOutErrors_Type = Counter32
_Ip6icmpOutErrors_Object = MibScalar
ip6icmpOutErrors = _Ip6icmpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 10, 14),
    _Ip6icmpOutErrors_Type()
)
ip6icmpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6icmpOutErrors.setStatus("current")
_Icmp6Stats_ObjectIdentity = ObjectIdentity
icmp6Stats = _Icmp6Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11)
)
_Icmp6StatsTable_Object = MibTable
icmp6StatsTable = _Icmp6StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1)
)
if mibBuilder.loadTexts:
    icmp6StatsTable.setStatus("current")
_Icmp6StatsEntry_Object = MibTableRow
icmp6StatsEntry = _Icmp6StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1)
)
icmp6StatsEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "icmp6StatsIndx"),
)
if mibBuilder.loadTexts:
    icmp6StatsEntry.setStatus("current")
_Icmp6StatsIndx_Type = Integer32
_Icmp6StatsIndx_Object = MibTableColumn
icmp6StatsIndx = _Icmp6StatsIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 1),
    _Icmp6StatsIndx_Type()
)
icmp6StatsIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6StatsIndx.setStatus("current")
_Icmp6IntfIndex_Type = Integer32
_Icmp6IntfIndex_Object = MibTableColumn
icmp6IntfIndex = _Icmp6IntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 2),
    _Icmp6IntfIndex_Type()
)
icmp6IntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6IntfIndex.setStatus("current")
_Icmp6InMsgs_Type = Counter32
_Icmp6InMsgs_Object = MibTableColumn
icmp6InMsgs = _Icmp6InMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 3),
    _Icmp6InMsgs_Type()
)
icmp6InMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6InMsgs.setStatus("current")
_Icmp6InErrors_Type = Counter32
_Icmp6InErrors_Object = MibTableColumn
icmp6InErrors = _Icmp6InErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 4),
    _Icmp6InErrors_Type()
)
icmp6InErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6InErrors.setStatus("current")
_Icmp6InEchos_Type = Counter32
_Icmp6InEchos_Object = MibTableColumn
icmp6InEchos = _Icmp6InEchos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 5),
    _Icmp6InEchos_Type()
)
icmp6InEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6InEchos.setStatus("current")
_Icmp6InEchoReps_Type = Counter32
_Icmp6InEchoReps_Object = MibTableColumn
icmp6InEchoReps = _Icmp6InEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 6),
    _Icmp6InEchoReps_Type()
)
icmp6InEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6InEchoReps.setStatus("current")
_Icmp6InNSs_Type = Counter32
_Icmp6InNSs_Object = MibTableColumn
icmp6InNSs = _Icmp6InNSs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 7),
    _Icmp6InNSs_Type()
)
icmp6InNSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6InNSs.setStatus("current")
_Icmp6InNAs_Type = Counter32
_Icmp6InNAs_Object = MibTableColumn
icmp6InNAs = _Icmp6InNAs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 8),
    _Icmp6InNAs_Type()
)
icmp6InNAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6InNAs.setStatus("current")
_Icmp6InRSs_Type = Counter32
_Icmp6InRSs_Object = MibTableColumn
icmp6InRSs = _Icmp6InRSs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 9),
    _Icmp6InRSs_Type()
)
icmp6InRSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6InRSs.setStatus("current")
_Icmp6InRAs_Type = Counter32
_Icmp6InRAs_Object = MibTableColumn
icmp6InRAs = _Icmp6InRAs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 10),
    _Icmp6InRAs_Type()
)
icmp6InRAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6InRAs.setStatus("current")
_Icmp6InDestUnreachs_Type = Counter32
_Icmp6InDestUnreachs_Object = MibTableColumn
icmp6InDestUnreachs = _Icmp6InDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 11),
    _Icmp6InDestUnreachs_Type()
)
icmp6InDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6InDestUnreachs.setStatus("current")
_Icmp6InTimeExcds_Type = Counter32
_Icmp6InTimeExcds_Object = MibTableColumn
icmp6InTimeExcds = _Icmp6InTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 12),
    _Icmp6InTimeExcds_Type()
)
icmp6InTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6InTimeExcds.setStatus("current")
_Icmp6InTooBigs_Type = Counter32
_Icmp6InTooBigs_Object = MibTableColumn
icmp6InTooBigs = _Icmp6InTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 13),
    _Icmp6InTooBigs_Type()
)
icmp6InTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6InTooBigs.setStatus("current")
_Icmp6InParmProbs_Type = Counter32
_Icmp6InParmProbs_Object = MibTableColumn
icmp6InParmProbs = _Icmp6InParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 14),
    _Icmp6InParmProbs_Type()
)
icmp6InParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6InParmProbs.setStatus("current")
_Icmp6InRedirects_Type = Counter32
_Icmp6InRedirects_Object = MibTableColumn
icmp6InRedirects = _Icmp6InRedirects_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 15),
    _Icmp6InRedirects_Type()
)
icmp6InRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6InRedirects.setStatus("current")
_Icmp6OutMsgs_Type = Counter32
_Icmp6OutMsgs_Object = MibTableColumn
icmp6OutMsgs = _Icmp6OutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 16),
    _Icmp6OutMsgs_Type()
)
icmp6OutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6OutMsgs.setStatus("current")
_Icmp6OutErrors_Type = Counter32
_Icmp6OutErrors_Object = MibTableColumn
icmp6OutErrors = _Icmp6OutErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 17),
    _Icmp6OutErrors_Type()
)
icmp6OutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6OutErrors.setStatus("current")
_Icmp6OutEchos_Type = Counter32
_Icmp6OutEchos_Object = MibTableColumn
icmp6OutEchos = _Icmp6OutEchos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 18),
    _Icmp6OutEchos_Type()
)
icmp6OutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6OutEchos.setStatus("current")
_Icmp6OutEchoReps_Type = Counter32
_Icmp6OutEchoReps_Object = MibTableColumn
icmp6OutEchoReps = _Icmp6OutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 19),
    _Icmp6OutEchoReps_Type()
)
icmp6OutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6OutEchoReps.setStatus("current")
_Icmp6OutNSs_Type = Counter32
_Icmp6OutNSs_Object = MibTableColumn
icmp6OutNSs = _Icmp6OutNSs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 20),
    _Icmp6OutNSs_Type()
)
icmp6OutNSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6OutNSs.setStatus("current")
_Icmp6OutNAs_Type = Counter32
_Icmp6OutNAs_Object = MibTableColumn
icmp6OutNAs = _Icmp6OutNAs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 21),
    _Icmp6OutNAs_Type()
)
icmp6OutNAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6OutNAs.setStatus("current")
_Icmp6OutRSs_Type = Counter32
_Icmp6OutRSs_Object = MibTableColumn
icmp6OutRSs = _Icmp6OutRSs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 22),
    _Icmp6OutRSs_Type()
)
icmp6OutRSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6OutRSs.setStatus("current")
_Icmp6OutRAs_Type = Counter32
_Icmp6OutRAs_Object = MibTableColumn
icmp6OutRAs = _Icmp6OutRAs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 23),
    _Icmp6OutRAs_Type()
)
icmp6OutRAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6OutRAs.setStatus("current")
_Icmp6OutRedirects_Type = Counter32
_Icmp6OutRedirects_Object = MibTableColumn
icmp6OutRedirects = _Icmp6OutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 11, 1, 1, 24),
    _Icmp6OutRedirects_Type()
)
icmp6OutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmp6OutRedirects.setStatus("current")
_Ip6gwStats_ObjectIdentity = ObjectIdentity
ip6gwStats = _Ip6gwStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 12)
)
_Ip6GwStatsTable_Object = MibTable
ip6GwStatsTable = _Ip6GwStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 12, 1)
)
if mibBuilder.loadTexts:
    ip6GwStatsTable.setStatus("current")
_Ip6GwStatsEntry_Object = MibTableRow
ip6GwStatsEntry = _Ip6GwStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 12, 1, 1)
)
ip6GwStatsEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ip6GwStatsIndex"),
)
if mibBuilder.loadTexts:
    ip6GwStatsEntry.setStatus("current")
_Ip6GwStatsIndex_Type = Integer32
_Ip6GwStatsIndex_Object = MibTableColumn
ip6GwStatsIndex = _Ip6GwStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 12, 1, 1, 1),
    _Ip6GwStatsIndex_Type()
)
ip6GwStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6GwStatsIndex.setStatus("current")
_Ip6GwIndex_Type = Integer32
_Ip6GwIndex_Object = MibTableColumn
ip6GwIndex = _Ip6GwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 12, 1, 1, 2),
    _Ip6GwIndex_Type()
)
ip6GwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6GwIndex.setStatus("current")
_Ip6GwEchoreq_Type = Counter32
_Ip6GwEchoreq_Object = MibTableColumn
ip6GwEchoreq = _Ip6GwEchoreq_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 12, 1, 1, 3),
    _Ip6GwEchoreq_Type()
)
ip6GwEchoreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6GwEchoreq.setStatus("current")
_Ip6GwEchoresp_Type = Counter32
_Ip6GwEchoresp_Object = MibTableColumn
ip6GwEchoresp = _Ip6GwEchoresp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 12, 1, 1, 4),
    _Ip6GwEchoresp_Type()
)
ip6GwEchoresp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6GwEchoresp.setStatus("current")
_Ip6GwFails_Type = Counter32
_Ip6GwFails_Object = MibTableColumn
ip6GwFails = _Ip6GwFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 12, 1, 1, 5),
    _Ip6GwFails_Type()
)
ip6GwFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6GwFails.setStatus("current")
_Ip6GwMaster_Type = Integer32
_Ip6GwMaster_Object = MibTableColumn
ip6GwMaster = _Ip6GwMaster_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 12, 1, 1, 6),
    _Ip6GwMaster_Type()
)
ip6GwMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6GwMaster.setStatus("current")
_Ip6IfIndex_Type = Integer32
_Ip6IfIndex_Object = MibTableColumn
ip6IfIndex = _Ip6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 12, 1, 1, 7),
    _Ip6IfIndex_Type()
)
ip6IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6IfIndex.setStatus("current")
_Ip6GwRetry_Type = Counter32
_Ip6GwRetry_Object = MibTableColumn
ip6GwRetry = _Ip6GwRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 12, 1, 1, 8),
    _Ip6GwRetry_Type()
)
ip6GwRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip6GwRetry.setStatus("current")
_Rip2Stats_ObjectIdentity = ObjectIdentity
rip2Stats = _Rip2Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 13)
)
_RipStatInPackets_Type = Counter32
_RipStatInPackets_Object = MibScalar
ripStatInPackets = _RipStatInPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 13, 1),
    _RipStatInPackets_Type()
)
ripStatInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInPackets.setStatus("current")
_RipStatOutPackets_Type = Counter32
_RipStatOutPackets_Object = MibScalar
ripStatOutPackets = _RipStatOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 13, 2),
    _RipStatOutPackets_Type()
)
ripStatOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatOutPackets.setStatus("current")
_RipStatInRequestPkts_Type = Counter32
_RipStatInRequestPkts_Object = MibScalar
ripStatInRequestPkts = _RipStatInRequestPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 13, 3),
    _RipStatInRequestPkts_Type()
)
ripStatInRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInRequestPkts.setStatus("current")
_RipStatInResponsePkts_Type = Counter32
_RipStatInResponsePkts_Object = MibScalar
ripStatInResponsePkts = _RipStatInResponsePkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 13, 4),
    _RipStatInResponsePkts_Type()
)
ripStatInResponsePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInResponsePkts.setStatus("current")
_RipStatOutRequestPkts_Type = Counter32
_RipStatOutRequestPkts_Object = MibScalar
ripStatOutRequestPkts = _RipStatOutRequestPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 13, 5),
    _RipStatOutRequestPkts_Type()
)
ripStatOutRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatOutRequestPkts.setStatus("current")
_RipStatOutResponsePkts_Type = Counter32
_RipStatOutResponsePkts_Object = MibScalar
ripStatOutResponsePkts = _RipStatOutResponsePkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 13, 6),
    _RipStatOutResponsePkts_Type()
)
ripStatOutResponsePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatOutResponsePkts.setStatus("current")
_RipStatRouteTimeout_Type = Counter32
_RipStatRouteTimeout_Object = MibScalar
ripStatRouteTimeout = _RipStatRouteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 13, 7),
    _RipStatRouteTimeout_Type()
)
ripStatRouteTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatRouteTimeout.setStatus("current")
_RipStatInBadSizePkts_Type = Counter32
_RipStatInBadSizePkts_Object = MibScalar
ripStatInBadSizePkts = _RipStatInBadSizePkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 13, 8),
    _RipStatInBadSizePkts_Type()
)
ripStatInBadSizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInBadSizePkts.setStatus("current")
_RipStatInBadVersion_Type = Counter32
_RipStatInBadVersion_Object = MibScalar
ripStatInBadVersion = _RipStatInBadVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 13, 9),
    _RipStatInBadVersion_Type()
)
ripStatInBadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInBadVersion.setStatus("current")
_RipStatInBadZeros_Type = Counter32
_RipStatInBadZeros_Object = MibScalar
ripStatInBadZeros = _RipStatInBadZeros_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 13, 10),
    _RipStatInBadZeros_Type()
)
ripStatInBadZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInBadZeros.setStatus("current")
_RipStatInBadSourcePort_Type = Counter32
_RipStatInBadSourcePort_Object = MibScalar
ripStatInBadSourcePort = _RipStatInBadSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 13, 11),
    _RipStatInBadSourcePort_Type()
)
ripStatInBadSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInBadSourcePort.setStatus("current")
_RipStatInBadSourceIP_Type = Counter32
_RipStatInBadSourceIP_Object = MibScalar
ripStatInBadSourceIP = _RipStatInBadSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 13, 12),
    _RipStatInBadSourceIP_Type()
)
ripStatInBadSourceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInBadSourceIP.setStatus("current")
_RipStatInSelfRcvPkts_Type = Counter32
_RipStatInSelfRcvPkts_Object = MibScalar
ripStatInSelfRcvPkts = _RipStatInSelfRcvPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 13, 13),
    _RipStatInSelfRcvPkts_Type()
)
ripStatInSelfRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInSelfRcvPkts.setStatus("current")
_TcpStats_ObjectIdentity = ObjectIdentity
tcpStats = _TcpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 14)
)
_TcpStatCurConn_Type = Counter32
_TcpStatCurConn_Object = MibScalar
tcpStatCurConn = _TcpStatCurConn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 14, 1),
    _TcpStatCurConn_Type()
)
tcpStatCurConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpStatCurConn.setStatus("current")
_TcpStatCurInConn_Type = Counter32
_TcpStatCurInConn_Object = MibScalar
tcpStatCurInConn = _TcpStatCurInConn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 14, 2),
    _TcpStatCurInConn_Type()
)
tcpStatCurInConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpStatCurInConn.setStatus("current")
_TcpStatCurOutConn_Type = Counter32
_TcpStatCurOutConn_Object = MibScalar
tcpStatCurOutConn = _TcpStatCurOutConn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 2, 14, 3),
    _TcpStatCurOutConn_Type()
)
tcpStatCurOutConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpStatCurOutConn.setStatus("current")
_Layer3Info_ObjectIdentity = ObjectIdentity
layer3Info = _Layer3Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3)
)
_IpRoutingInfo_ObjectIdentity = ObjectIdentity
ipRoutingInfo = _IpRoutingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 1)
)
_IpRouteInfoTable_Object = MibTable
ipRouteInfoTable = _IpRouteInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ipRouteInfoTable.setStatus("current")
_IpRouteInfoEntry_Object = MibTableRow
ipRouteInfoEntry = _IpRouteInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 1, 1, 1)
)
ipRouteInfoEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipRouteInfoIndx"),
)
if mibBuilder.loadTexts:
    ipRouteInfoEntry.setStatus("current")
_IpRouteInfoIndx_Type = Integer32
_IpRouteInfoIndx_Object = MibTableColumn
ipRouteInfoIndx = _IpRouteInfoIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 1, 1, 1, 1),
    _IpRouteInfoIndx_Type()
)
ipRouteInfoIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoIndx.setStatus("current")
_IpRouteInfoDestIp_Type = IpAddress
_IpRouteInfoDestIp_Object = MibTableColumn
ipRouteInfoDestIp = _IpRouteInfoDestIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 1, 1, 1, 2),
    _IpRouteInfoDestIp_Type()
)
ipRouteInfoDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoDestIp.setStatus("current")
_IpRouteInfoMask_Type = IpAddress
_IpRouteInfoMask_Object = MibTableColumn
ipRouteInfoMask = _IpRouteInfoMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 1, 1, 1, 3),
    _IpRouteInfoMask_Type()
)
ipRouteInfoMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoMask.setStatus("current")
_IpRouteInfoGateway_Type = IpAddress
_IpRouteInfoGateway_Object = MibTableColumn
ipRouteInfoGateway = _IpRouteInfoGateway_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 1, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 1, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 1, 1, 1, 6),
    _IpRouteInfoType_Type()
)
ipRouteInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoType.setStatus("current")
_IpRouteInfoInterface_Type = Integer32
_IpRouteInfoInterface_Object = MibTableColumn
ipRouteInfoInterface = _IpRouteInfoInterface_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 1, 1, 1, 7),
    _IpRouteInfoInterface_Type()
)
ipRouteInfoInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoInterface.setStatus("current")
_IpRouteInfoGateway1_Type = IpAddress
_IpRouteInfoGateway1_Object = MibTableColumn
ipRouteInfoGateway1 = _IpRouteInfoGateway1_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 1, 1, 1, 8),
    _IpRouteInfoGateway1_Type()
)
ipRouteInfoGateway1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoGateway1.setStatus("current")
_IpRouteInfoGateway2_Type = IpAddress
_IpRouteInfoGateway2_Object = MibTableColumn
ipRouteInfoGateway2 = _IpRouteInfoGateway2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 1, 1, 1, 9),
    _IpRouteInfoGateway2_Type()
)
ipRouteInfoGateway2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoGateway2.setStatus("current")
_IpRouteInfoMetric_Type = Integer32
_IpRouteInfoMetric_Object = MibTableColumn
ipRouteInfoMetric = _IpRouteInfoMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 1, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 1, 2),
    _RouteTableClear_Type()
)
routeTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeTableClear.setStatus("current")
_ArpInfo_ObjectIdentity = ObjectIdentity
arpInfo = _ArpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 2)
)
_ArpInfoTable_Object = MibTable
arpInfoTable = _ArpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    arpInfoTable.setStatus("current")
_ArpInfoEntry_Object = MibTableRow
arpInfoEntry = _ArpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 2, 1, 1)
)
arpInfoEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "arpInfoDestIp"),
)
if mibBuilder.loadTexts:
    arpInfoEntry.setStatus("current")
_ArpInfoDestIp_Type = IpAddress
_ArpInfoDestIp_Object = MibTableColumn
arpInfoDestIp = _ArpInfoDestIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 2, 1, 1, 1),
    _ArpInfoDestIp_Type()
)
arpInfoDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoDestIp.setStatus("current")
_ArpInfoMacAddr_Type = PhysAddress
_ArpInfoMacAddr_Object = MibTableColumn
arpInfoMacAddr = _ArpInfoMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 2, 1, 1, 2),
    _ArpInfoMacAddr_Type()
)
arpInfoMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoMacAddr.setStatus("current")
_ArpInfoVLAN_Type = Integer32
_ArpInfoVLAN_Object = MibTableColumn
arpInfoVLAN = _ArpInfoVLAN_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 2, 1, 1, 3),
    _ArpInfoVLAN_Type()
)
arpInfoVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoVLAN.setStatus("current")
_ArpInfoSrcPort_Type = Integer32
_ArpInfoSrcPort_Object = MibTableColumn
arpInfoSrcPort = _ArpInfoSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 2, 1, 1, 4),
    _ArpInfoSrcPort_Type()
)
arpInfoSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoSrcPort.setStatus("current")
_ArpInfoRefPorts_Type = Integer32
_ArpInfoRefPorts_Object = MibTableColumn
arpInfoRefPorts = _ArpInfoRefPorts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 2, 1, 1, 5),
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
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("indirect", 4),
          ("layer4", 5),
          ("permanent", 3),
          ("unresolved", 2))
    )


_ArpInfoFlag_Type.__name__ = "Integer32"
_ArpInfoFlag_Object = MibTableColumn
arpInfoFlag = _ArpInfoFlag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 2, 2),
    _ArpCacheClear_Type()
)
arpCacheClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpCacheClear.setStatus("current")
_VrrpInfo_ObjectIdentity = ObjectIdentity
vrrpInfo = _VrrpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 3)
)
_VrrpInfoVirtRtrTable_Object = MibTable
vrrpInfoVirtRtrTable = _VrrpInfoVirtRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrTable.setStatus("current")
_VrrpInfoVirtRtrTableEntry_Object = MibTableRow
vrrpInfoVirtRtrTableEntry = _VrrpInfoVirtRtrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 3, 1, 1)
)
vrrpInfoVirtRtrTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "vrrpInfoVirtRtrIndex"),
)
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrTableEntry.setStatus("current")
_VrrpInfoVirtRtrIndex_Type = Integer32
_VrrpInfoVirtRtrIndex_Object = MibTableColumn
vrrpInfoVirtRtrIndex = _VrrpInfoVirtRtrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 3, 1, 1, 1),
    _VrrpInfoVirtRtrIndex_Type()
)
vrrpInfoVirtRtrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrIndex.setStatus("current")


class _VrrpInfoVirtRtrState_Type(Integer32):
    """Custom type vrrpInfoVirtRtrState based on Integer32"""
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
        *(("backup", 3),
          ("holdoff", 4),
          ("init", 1),
          ("master", 2))
    )


_VrrpInfoVirtRtrState_Type.__name__ = "Integer32"
_VrrpInfoVirtRtrState_Object = MibTableColumn
vrrpInfoVirtRtrState = _VrrpInfoVirtRtrState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 3, 1, 1, 5),
    _VrrpInfoVirtRtrProxy_Type()
)
vrrpInfoVirtRtrProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrProxy.setStatus("current")
_VrrpInfoVirtRtrPriority_Type = Integer32
_VrrpInfoVirtRtrPriority_Object = MibTableColumn
vrrpInfoVirtRtrPriority = _VrrpInfoVirtRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 3, 1, 1, 6),
    _VrrpInfoVirtRtrPriority_Type()
)
vrrpInfoVirtRtrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrPriority.setStatus("current")
_Ospfinfo_ObjectIdentity = ObjectIdentity
ospfinfo = _Ospfinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4)
)
_OspfGeneralInfo_ObjectIdentity = ObjectIdentity
ospfGeneralInfo = _OspfGeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 1)
)
_OspfStartTime_Type = Integer32
_OspfStartTime_Object = MibScalar
ospfStartTime = _OspfStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 1, 1),
    _OspfStartTime_Type()
)
ospfStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStartTime.setStatus("current")
_OspfProcessUptime_Type = Counter32
_OspfProcessUptime_Object = MibScalar
ospfProcessUptime = _OspfProcessUptime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 1, 2),
    _OspfProcessUptime_Type()
)
ospfProcessUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessUptime.setStatus("current")
_OspfLsTypesSupported_Type = Integer32
_OspfLsTypesSupported_Object = MibScalar
ospfLsTypesSupported = _OspfLsTypesSupported_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 1, 3),
    _OspfLsTypesSupported_Type()
)
ospfLsTypesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsTypesSupported.setStatus("current")
_OspfIntfCountForRouter_Type = Integer32
_OspfIntfCountForRouter_Object = MibScalar
ospfIntfCountForRouter = _OspfIntfCountForRouter_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 1, 4),
    _OspfIntfCountForRouter_Type()
)
ospfIntfCountForRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfCountForRouter.setStatus("current")
_OspfVlinkCountForRouter_Type = Integer32
_OspfVlinkCountForRouter_Object = MibScalar
ospfVlinkCountForRouter = _OspfVlinkCountForRouter_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 1, 5),
    _OspfVlinkCountForRouter_Type()
)
ospfVlinkCountForRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVlinkCountForRouter.setStatus("current")
_OspfTotalNeighbours_Type = Integer32
_OspfTotalNeighbours_Object = MibScalar
ospfTotalNeighbours = _OspfTotalNeighbours_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 1, 6),
    _OspfTotalNeighbours_Type()
)
ospfTotalNeighbours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTotalNeighbours.setStatus("current")
_OspfNbrInInitState_Type = Integer32
_OspfNbrInInitState_Object = MibScalar
ospfNbrInInitState = _OspfNbrInInitState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 1, 7),
    _OspfNbrInInitState_Type()
)
ospfNbrInInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrInInitState.setStatus("current")
_OspfNbrInExchState_Type = Integer32
_OspfNbrInExchState_Object = MibScalar
ospfNbrInExchState = _OspfNbrInExchState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 1, 8),
    _OspfNbrInExchState_Type()
)
ospfNbrInExchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrInExchState.setStatus("current")
_OspfNbrInFullState_Type = Integer32
_OspfNbrInFullState_Object = MibScalar
ospfNbrInFullState = _OspfNbrInFullState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 1, 9),
    _OspfNbrInFullState_Type()
)
ospfNbrInFullState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrInFullState.setStatus("current")
_OspfTotalAreas_Type = Integer32
_OspfTotalAreas_Object = MibScalar
ospfTotalAreas = _OspfTotalAreas_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 1, 10),
    _OspfTotalAreas_Type()
)
ospfTotalAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTotalAreas.setStatus("current")
_OspfTotalTransitAreas_Type = Integer32
_OspfTotalTransitAreas_Object = MibScalar
ospfTotalTransitAreas = _OspfTotalTransitAreas_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 1, 11),
    _OspfTotalTransitAreas_Type()
)
ospfTotalTransitAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTotalTransitAreas.setStatus("current")
_OspfTotalNssaAreas_Type = Integer32
_OspfTotalNssaAreas_Object = MibScalar
ospfTotalNssaAreas = _OspfTotalNssaAreas_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 1, 12),
    _OspfTotalNssaAreas_Type()
)
ospfTotalNssaAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTotalNssaAreas.setStatus("current")
_OspfAreaInfoTable_Object = MibTable
ospfAreaInfoTable = _OspfAreaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 2)
)
if mibBuilder.loadTexts:
    ospfAreaInfoTable.setStatus("current")
_OspfAreaInfoEntry_Object = MibTableRow
ospfAreaInfoEntry = _OspfAreaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 2, 1)
)
ospfAreaInfoEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfAreaInfoIndex"),
)
if mibBuilder.loadTexts:
    ospfAreaInfoEntry.setStatus("current")
_OspfAreaInfoIndex_Type = Integer32
_OspfAreaInfoIndex_Object = MibTableColumn
ospfAreaInfoIndex = _OspfAreaInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 2, 1, 1),
    _OspfAreaInfoIndex_Type()
)
ospfAreaInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaInfoIndex.setStatus("current")
_OspfTotalNumberOfInterfaces_Type = Integer32
_OspfTotalNumberOfInterfaces_Object = MibTableColumn
ospfTotalNumberOfInterfaces = _OspfTotalNumberOfInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 2, 1, 2),
    _OspfTotalNumberOfInterfaces_Type()
)
ospfTotalNumberOfInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTotalNumberOfInterfaces.setStatus("current")
_OspfNumberOfInterfacesUp_Type = Integer32
_OspfNumberOfInterfacesUp_Object = MibTableColumn
ospfNumberOfInterfacesUp = _OspfNumberOfInterfacesUp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 2, 1, 3),
    _OspfNumberOfInterfacesUp_Type()
)
ospfNumberOfInterfacesUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNumberOfInterfacesUp.setStatus("current")
_OspfNumberOfLsdbEntries_Type = Integer32
_OspfNumberOfLsdbEntries_Object = MibTableColumn
ospfNumberOfLsdbEntries = _OspfNumberOfLsdbEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 2, 1, 4),
    _OspfNumberOfLsdbEntries_Type()
)
ospfNumberOfLsdbEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNumberOfLsdbEntries.setStatus("current")
_OspfAreaInfoId_Type = IpAddress
_OspfAreaInfoId_Object = MibTableColumn
ospfAreaInfoId = _OspfAreaInfoId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 2, 1, 5),
    _OspfAreaInfoId_Type()
)
ospfAreaInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaInfoId.setStatus("current")
_OspfIntfInfoTable_Object = MibTable
ospfIntfInfoTable = _OspfIntfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 3)
)
if mibBuilder.loadTexts:
    ospfIntfInfoTable.setStatus("current")
_OspfIntfInfoEntry_Object = MibTableRow
ospfIntfInfoEntry = _OspfIntfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 3, 1)
)
ospfIntfInfoEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfIfInfoIndex"),
)
if mibBuilder.loadTexts:
    ospfIntfInfoEntry.setStatus("current")
_OspfIfInfoIndex_Type = Integer32
_OspfIfInfoIndex_Object = MibTableColumn
ospfIfInfoIndex = _OspfIfInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 3, 1, 1),
    _OspfIfInfoIndex_Type()
)
ospfIfInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoIndex.setStatus("current")
_OspfIfDesignatedRouterIP_Type = IpAddress
_OspfIfDesignatedRouterIP_Object = MibTableColumn
ospfIfDesignatedRouterIP = _OspfIfDesignatedRouterIP_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 3, 1, 2),
    _OspfIfDesignatedRouterIP_Type()
)
ospfIfDesignatedRouterIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfDesignatedRouterIP.setStatus("current")
_OspfIfBackupDesignatedRouterIP_Type = IpAddress
_OspfIfBackupDesignatedRouterIP_Object = MibTableColumn
ospfIfBackupDesignatedRouterIP = _OspfIfBackupDesignatedRouterIP_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 3, 1, 3),
    _OspfIfBackupDesignatedRouterIP_Type()
)
ospfIfBackupDesignatedRouterIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfBackupDesignatedRouterIP.setStatus("current")
_OspfIfWaitInterval_Type = Integer32
_OspfIfWaitInterval_Object = MibTableColumn
ospfIfWaitInterval = _OspfIfWaitInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 3, 1, 4),
    _OspfIfWaitInterval_Type()
)
ospfIfWaitInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfWaitInterval.setStatus("current")
_OspfIfTotalNeighbours_Type = Integer32
_OspfIfTotalNeighbours_Object = MibTableColumn
ospfIfTotalNeighbours = _OspfIfTotalNeighbours_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 3, 1, 5),
    _OspfIfTotalNeighbours_Type()
)
ospfIfTotalNeighbours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfTotalNeighbours.setStatus("current")
_OspfIfInfoIpAddress_Type = IpAddress
_OspfIfInfoIpAddress_Object = MibTableColumn
ospfIfInfoIpAddress = _OspfIfInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 3, 1, 6),
    _OspfIfInfoIpAddress_Type()
)
ospfIfInfoIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoIpAddress.setStatus("current")
_OspfIfNbrTable_Object = MibTable
ospfIfNbrTable = _OspfIfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 5)
)
if mibBuilder.loadTexts:
    ospfIfNbrTable.setStatus("current")
_OspfIfNbrEntry_Object = MibTableRow
ospfIfNbrEntry = _OspfIfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 5, 1)
)
ospfIfNbrEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfIfNbrIntfIndex"),
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ospfIfNbrIpAddr"),
)
if mibBuilder.loadTexts:
    ospfIfNbrEntry.setStatus("current")
_OspfIfNbrIntfIndex_Type = Integer32
_OspfIfNbrIntfIndex_Object = MibTableColumn
ospfIfNbrIntfIndex = _OspfIfNbrIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 5, 1, 1),
    _OspfIfNbrIntfIndex_Type()
)
ospfIfNbrIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfNbrIntfIndex.setStatus("current")
_OspfIfNbrIpAddr_Type = IpAddress
_OspfIfNbrIpAddr_Object = MibTableColumn
ospfIfNbrIpAddr = _OspfIfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 5, 1, 2),
    _OspfIfNbrIpAddr_Type()
)
ospfIfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfNbrIpAddr.setStatus("current")
_OspfIfNbrPriority_Type = Integer32
_OspfIfNbrPriority_Object = MibTableColumn
ospfIfNbrPriority = _OspfIfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 5, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 5, 1, 4),
    _OspfIfNbrState_Type()
)
ospfIfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfNbrState.setStatus("current")
_OspfIfNbrDesignatedRtr_Type = IpAddress
_OspfIfNbrDesignatedRtr_Object = MibTableColumn
ospfIfNbrDesignatedRtr = _OspfIfNbrDesignatedRtr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 5, 1, 5),
    _OspfIfNbrDesignatedRtr_Type()
)
ospfIfNbrDesignatedRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfNbrDesignatedRtr.setStatus("current")
_OspfIfNbrBackupDesignatedRtr_Type = IpAddress
_OspfIfNbrBackupDesignatedRtr_Object = MibTableColumn
ospfIfNbrBackupDesignatedRtr = _OspfIfNbrBackupDesignatedRtr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 5, 1, 6),
    _OspfIfNbrBackupDesignatedRtr_Type()
)
ospfIfNbrBackupDesignatedRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfNbrBackupDesignatedRtr.setStatus("current")
_OspfIfNbrIpAddress_Type = IpAddress
_OspfIfNbrIpAddress_Object = MibTableColumn
ospfIfNbrIpAddress = _OspfIfNbrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 4, 5, 1, 7),
    _OspfIfNbrIpAddress_Type()
)
ospfIfNbrIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfNbrIpAddress.setStatus("current")
_GatewayInfo_ObjectIdentity = ObjectIdentity
gatewayInfo = _GatewayInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 5)
)
_GatewayInfoTable_Object = MibTable
gatewayInfoTable = _GatewayInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 5, 1)
)
if mibBuilder.loadTexts:
    gatewayInfoTable.setStatus("current")
_GatewayInfoEntry_Object = MibTableRow
gatewayInfoEntry = _GatewayInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 5, 1, 1)
)
gatewayInfoEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "gatewayInfoIndex"),
)
if mibBuilder.loadTexts:
    gatewayInfoEntry.setStatus("current")
_GatewayInfoIndex_Type = Integer32
_GatewayInfoIndex_Object = MibTableColumn
gatewayInfoIndex = _GatewayInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 5, 1, 1, 1),
    _GatewayInfoIndex_Type()
)
gatewayInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayInfoIndex.setStatus("current")
_GatewayInfoAddr_Type = IpAddress
_GatewayInfoAddr_Object = MibTableColumn
gatewayInfoAddr = _GatewayInfoAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 5, 1, 1, 2),
    _GatewayInfoAddr_Type()
)
gatewayInfoAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayInfoAddr.setStatus("current")
_GatewayInfoVlan_Type = Integer32
_GatewayInfoVlan_Object = MibTableColumn
gatewayInfoVlan = _GatewayInfoVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 5, 1, 1, 3),
    _GatewayInfoVlan_Type()
)
gatewayInfoVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayInfoVlan.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 5, 1, 1, 4),
    _GatewayInfoStatus_Type()
)
gatewayInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayInfoStatus.setStatus("current")
_GatewayInfoAddr6_Type = DisplayString
_GatewayInfoAddr6_Object = MibTableColumn
gatewayInfoAddr6 = _GatewayInfoAddr6_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 5, 1, 1, 5),
    _GatewayInfoAddr6_Type()
)
gatewayInfoAddr6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayInfoAddr6.setStatus("current")
_NbrcacheInfo_ObjectIdentity = ObjectIdentity
nbrcacheInfo = _NbrcacheInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 7)
)
_NbrcacheInfoTable_Object = MibTable
nbrcacheInfoTable = _NbrcacheInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 7, 1)
)
if mibBuilder.loadTexts:
    nbrcacheInfoTable.setStatus("current")
_NbrcacheInfoEntry_Object = MibTableRow
nbrcacheInfoEntry = _NbrcacheInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 7, 1, 1)
)
nbrcacheInfoEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "nbrcacheInfoIndex"),
)
if mibBuilder.loadTexts:
    nbrcacheInfoEntry.setStatus("current")
_NbrcacheInfoIndex_Type = Integer32
_NbrcacheInfoIndex_Object = MibTableColumn
nbrcacheInfoIndex = _NbrcacheInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 7, 1, 1, 1),
    _NbrcacheInfoIndex_Type()
)
nbrcacheInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrcacheInfoIndex.setStatus("current")
_NbrcacheInfoDestIp_Type = DisplayString
_NbrcacheInfoDestIp_Object = MibTableColumn
nbrcacheInfoDestIp = _NbrcacheInfoDestIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 7, 1, 1, 2),
    _NbrcacheInfoDestIp_Type()
)
nbrcacheInfoDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrcacheInfoDestIp.setStatus("current")


class _NbrcacheInfoState_Type(Integer32):
    """Custom type nbrcacheInfoState based on Integer32"""
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
        *(("delay", 4),
          ("incmp", 8),
          ("inval", 6),
          ("probe", 5),
          ("reach", 2),
          ("stale", 3),
          ("undef", 1),
          ("unknown", 7))
    )


_NbrcacheInfoState_Type.__name__ = "Integer32"
_NbrcacheInfoState_Object = MibTableColumn
nbrcacheInfoState = _NbrcacheInfoState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 7, 1, 1, 3),
    _NbrcacheInfoState_Type()
)
nbrcacheInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrcacheInfoState.setStatus("current")


class _NbrcacheInfoType_Type(Integer32):
    """Custom type nbrcacheInfoType based on Integer32"""
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
        *(("dynamic", 4),
          ("invalid", 3),
          ("local", 6),
          ("other", 2),
          ("static", 5),
          ("undef", 1))
    )


_NbrcacheInfoType_Type.__name__ = "Integer32"
_NbrcacheInfoType_Object = MibTableColumn
nbrcacheInfoType = _NbrcacheInfoType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 7, 1, 1, 4),
    _NbrcacheInfoType_Type()
)
nbrcacheInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrcacheInfoType.setStatus("current")
_NbrcacheInfoMacAddr_Type = PhysAddress
_NbrcacheInfoMacAddr_Object = MibTableColumn
nbrcacheInfoMacAddr = _NbrcacheInfoMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 7, 1, 1, 5),
    _NbrcacheInfoMacAddr_Type()
)
nbrcacheInfoMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrcacheInfoMacAddr.setStatus("current")
_NbrcacheInfoVlanId_Type = Integer32
_NbrcacheInfoVlanId_Object = MibTableColumn
nbrcacheInfoVlanId = _NbrcacheInfoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 7, 1, 1, 6),
    _NbrcacheInfoVlanId_Type()
)
nbrcacheInfoVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrcacheInfoVlanId.setStatus("current")
_NbrcacheInfoPortNum_Type = Integer32
_NbrcacheInfoPortNum_Object = MibTableColumn
nbrcacheInfoPortNum = _NbrcacheInfoPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 7, 1, 1, 7),
    _NbrcacheInfoPortNum_Type()
)
nbrcacheInfoPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrcacheInfoPortNum.setStatus("current")


class _NbrcacheClear_Type(Integer32):
    """Custom type nbrcacheClear based on Integer32"""
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


_NbrcacheClear_Type.__name__ = "Integer32"
_NbrcacheClear_Object = MibScalar
nbrcacheClear = _NbrcacheClear_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 7, 2),
    _NbrcacheClear_Type()
)
nbrcacheClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbrcacheClear.setStatus("current")
_NbrcacheInfoTotDynamicEntries_Type = Integer32
_NbrcacheInfoTotDynamicEntries_Object = MibScalar
nbrcacheInfoTotDynamicEntries = _NbrcacheInfoTotDynamicEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 7, 3),
    _NbrcacheInfoTotDynamicEntries_Type()
)
nbrcacheInfoTotDynamicEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrcacheInfoTotDynamicEntries.setStatus("current")
_NbrcacheInfoTotLocalEntries_Type = Integer32
_NbrcacheInfoTotLocalEntries_Object = MibScalar
nbrcacheInfoTotLocalEntries = _NbrcacheInfoTotLocalEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 7, 4),
    _NbrcacheInfoTotLocalEntries_Type()
)
nbrcacheInfoTotLocalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrcacheInfoTotLocalEntries.setStatus("current")
_NbrcacheInfoTotOtherEntries_Type = Integer32
_NbrcacheInfoTotOtherEntries_Object = MibScalar
nbrcacheInfoTotOtherEntries = _NbrcacheInfoTotOtherEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 7, 5),
    _NbrcacheInfoTotOtherEntries_Type()
)
nbrcacheInfoTotOtherEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbrcacheInfoTotOtherEntries.setStatus("current")
_IpRoute6Info_ObjectIdentity = ObjectIdentity
ipRoute6Info = _IpRoute6Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 8)
)
_IpRoute6InfoTable_Object = MibTable
ipRoute6InfoTable = _IpRoute6InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 8, 1)
)
if mibBuilder.loadTexts:
    ipRoute6InfoTable.setStatus("current")
_IpRoute6InfoEntry_Object = MibTableRow
ipRoute6InfoEntry = _IpRoute6InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 8, 1, 1)
)
ipRoute6InfoEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ipRoute6InfoIndx"),
)
if mibBuilder.loadTexts:
    ipRoute6InfoEntry.setStatus("current")
_IpRoute6InfoIndx_Type = Integer32
_IpRoute6InfoIndx_Object = MibTableColumn
ipRoute6InfoIndx = _IpRoute6InfoIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 8, 1, 1, 1),
    _IpRoute6InfoIndx_Type()
)
ipRoute6InfoIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoute6InfoIndx.setStatus("current")
_IpRoute6InfoDestIp6_Type = DisplayString
_IpRoute6InfoDestIp6_Object = MibTableColumn
ipRoute6InfoDestIp6 = _IpRoute6InfoDestIp6_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 8, 1, 1, 2),
    _IpRoute6InfoDestIp6_Type()
)
ipRoute6InfoDestIp6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoute6InfoDestIp6.setStatus("current")
_IpRoute6InfoInterface_Type = Integer32
_IpRoute6InfoInterface_Object = MibTableColumn
ipRoute6InfoInterface = _IpRoute6InfoInterface_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 8, 1, 1, 3),
    _IpRoute6InfoInterface_Type()
)
ipRoute6InfoInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoute6InfoInterface.setStatus("current")
_IpRoute6InfoNextHop_Type = DisplayString
_IpRoute6InfoNextHop_Object = MibTableColumn
ipRoute6InfoNextHop = _IpRoute6InfoNextHop_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 8, 1, 1, 4),
    _IpRoute6InfoNextHop_Type()
)
ipRoute6InfoNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoute6InfoNextHop.setStatus("current")


class _IpRoute6InfoProto_Type(Integer32):
    """Custom type ipRoute6InfoProto based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 6),
          ("bgpa", 13),
          ("igmp", 14),
          ("isis", 1),
          ("local", 5),
          ("natpt", 16),
          ("ospf", 3),
          ("ospfa", 11),
          ("ospfe", 9),
          ("ospfe2", 10),
          ("ospfi", 8),
          ("rip", 2),
          ("ripa", 12),
          ("static", 4),
          ("stlow", 7),
          ("unknown", 15))
    )


_IpRoute6InfoProto_Type.__name__ = "Integer32"
_IpRoute6InfoProto_Object = MibTableColumn
ipRoute6InfoProto = _IpRoute6InfoProto_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 8, 1, 1, 5),
    _IpRoute6InfoProto_Type()
)
ipRoute6InfoProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoute6InfoProto.setStatus("current")
_IpIntfInfo_ObjectIdentity = ObjectIdentity
ipIntfInfo = _IpIntfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 9)
)
_IpIntfInfoTable_Object = MibTable
ipIntfInfoTable = _IpIntfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 9, 1)
)
if mibBuilder.loadTexts:
    ipIntfInfoTable.setStatus("current")
_IntfInfoEntry_Object = MibTableRow
intfInfoEntry = _IntfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 9, 1, 1)
)
intfInfoEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "intfInfoIndex"),
)
if mibBuilder.loadTexts:
    intfInfoEntry.setStatus("current")
_IntfInfoIndex_Type = Integer32
_IntfInfoIndex_Object = MibTableColumn
intfInfoIndex = _IntfInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 9, 1, 1, 1),
    _IntfInfoIndex_Type()
)
intfInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfInfoIndex.setStatus("current")


class _IntfInfoIpver_Type(Integer32):
    """Custom type intfInfoIpver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_IntfInfoIpver_Type.__name__ = "Integer32"
_IntfInfoIpver_Object = MibTableColumn
intfInfoIpver = _IntfInfoIpver_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 9, 1, 1, 2),
    _IntfInfoIpver_Type()
)
intfInfoIpver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfInfoIpver.setStatus("current")
_IntfInfoAddr_Type = DisplayString
_IntfInfoAddr_Object = MibTableColumn
intfInfoAddr = _IntfInfoAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 9, 1, 1, 3),
    _IntfInfoAddr_Type()
)
intfInfoAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfInfoAddr.setStatus("current")
_IntfInfoNetMask_Type = DisplayString
_IntfInfoNetMask_Object = MibTableColumn
intfInfoNetMask = _IntfInfoNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 9, 1, 1, 4),
    _IntfInfoNetMask_Type()
)
intfInfoNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfInfoNetMask.setStatus("current")
_IntfInfoBcastAddr_Type = DisplayString
_IntfInfoBcastAddr_Object = MibTableColumn
intfInfoBcastAddr = _IntfInfoBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 9, 1, 1, 5),
    _IntfInfoBcastAddr_Type()
)
intfInfoBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfInfoBcastAddr.setStatus("current")
_IntfInfoVlan_Type = Integer32
_IntfInfoVlan_Object = MibTableColumn
intfInfoVlan = _IntfInfoVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 9, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 9, 1, 1, 7),
    _IntfInfoStatus_Type()
)
intfInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfInfoStatus.setStatus("current")
_IntfInfoLinkLocalAddr_Type = DisplayString
_IntfInfoLinkLocalAddr_Object = MibTableColumn
intfInfoLinkLocalAddr = _IntfInfoLinkLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 9, 1, 1, 8),
    _IntfInfoLinkLocalAddr_Type()
)
intfInfoLinkLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfInfoLinkLocalAddr.setStatus("current")
_Rip2Info_ObjectIdentity = ObjectIdentity
rip2Info = _Rip2Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10)
)
_Rip2GeneralInfo_ObjectIdentity = ObjectIdentity
rip2GeneralInfo = _Rip2GeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 1)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 1, 2),
    _RipInfoUpdatePeriod_Type()
)
ripInfoUpdatePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoUpdatePeriod.setStatus("current")


class _RipInfoVip_Type(Integer32):
    """Custom type ripInfoVip based on Integer32"""
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


_RipInfoVip_Type.__name__ = "Integer32"
_RipInfoVip_Object = MibScalar
ripInfoVip = _RipInfoVip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 1, 3),
    _RipInfoVip_Type()
)
ripInfoVip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoVip.setStatus("current")


class _RipInfoStaticSupply_Type(Integer32):
    """Custom type ripInfoStaticSupply based on Integer32"""
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


_RipInfoStaticSupply_Type.__name__ = "Integer32"
_RipInfoStaticSupply_Object = MibScalar
ripInfoStaticSupply = _RipInfoStaticSupply_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 1, 4),
    _RipInfoStaticSupply_Type()
)
ripInfoStaticSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoStaticSupply.setStatus("current")
_Rip2InfoIntfTable_Object = MibTable
rip2InfoIntfTable = _Rip2InfoIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 2)
)
if mibBuilder.loadTexts:
    rip2InfoIntfTable.setStatus("current")
_RipInfoIntfEntry_Object = MibTableRow
ripInfoIntfEntry = _RipInfoIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 2, 1)
)
ripInfoIntfEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "ripInfoIntfIndex"),
)
if mibBuilder.loadTexts:
    ripInfoIntfEntry.setStatus("current")
_RipInfoIntfIndex_Type = Integer32
_RipInfoIntfIndex_Object = MibTableColumn
ripInfoIntfIndex = _RipInfoIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 2, 1, 2),
    _RipInfoIntfVersion_Type()
)
ripInfoIntfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoIntfVersion.setStatus("current")
_RipInfoIntfAddress_Type = IpAddress
_RipInfoIntfAddress_Object = MibTableColumn
ripInfoIntfAddress = _RipInfoIntfAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 2, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 2, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 2, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 2, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 2, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 10, 2, 1, 13),
    _RipInfoIntfDefault_Type()
)
ripInfoIntfDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInfoIntfDefault.setStatus("current")
_Rip2RoutesInfo_ObjectIdentity = ObjectIdentity
rip2RoutesInfo = _Rip2RoutesInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 11)
)
_Rip2RoutesInfoTable_Object = MibTable
rip2RoutesInfoTable = _Rip2RoutesInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 11, 1)
)
if mibBuilder.loadTexts:
    rip2RoutesInfoTable.setStatus("current")
_Rip2RoutesInfoEntry_Object = MibTableRow
rip2RoutesInfoEntry = _Rip2RoutesInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 11, 1, 1)
)
rip2RoutesInfoEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "rip2RoutesInfoDestIndex"),
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "rip2RoutesInfoNxtHopIndex"),
)
if mibBuilder.loadTexts:
    rip2RoutesInfoEntry.setStatus("current")
_Rip2RoutesInfoDestIndex_Type = Integer32
_Rip2RoutesInfoDestIndex_Object = MibTableColumn
rip2RoutesInfoDestIndex = _Rip2RoutesInfoDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 11, 1, 1, 1),
    _Rip2RoutesInfoDestIndex_Type()
)
rip2RoutesInfoDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2RoutesInfoDestIndex.setStatus("current")
_Rip2RoutesInfoNxtHopIndex_Type = Integer32
_Rip2RoutesInfoNxtHopIndex_Object = MibTableColumn
rip2RoutesInfoNxtHopIndex = _Rip2RoutesInfoNxtHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 11, 1, 1, 2),
    _Rip2RoutesInfoNxtHopIndex_Type()
)
rip2RoutesInfoNxtHopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2RoutesInfoNxtHopIndex.setStatus("current")
_Rip2RoutesInfoDestination_Type = DisplayString
_Rip2RoutesInfoDestination_Object = MibTableColumn
rip2RoutesInfoDestination = _Rip2RoutesInfoDestination_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 11, 1, 1, 3),
    _Rip2RoutesInfoDestination_Type()
)
rip2RoutesInfoDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2RoutesInfoDestination.setStatus("current")
_Rip2RoutesInfoIpAddress_Type = IpAddress
_Rip2RoutesInfoIpAddress_Object = MibTableColumn
rip2RoutesInfoIpAddress = _Rip2RoutesInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 11, 1, 1, 4),
    _Rip2RoutesInfoIpAddress_Type()
)
rip2RoutesInfoIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2RoutesInfoIpAddress.setStatus("current")


class _Rip2RoutesInfoMetric_Type(Integer32):
    """Custom type rip2RoutesInfoMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Rip2RoutesInfoMetric_Type.__name__ = "Integer32"
_Rip2RoutesInfoMetric_Object = MibTableColumn
rip2RoutesInfoMetric = _Rip2RoutesInfoMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 11, 1, 1, 5),
    _Rip2RoutesInfoMetric_Type()
)
rip2RoutesInfoMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2RoutesInfoMetric.setStatus("current")
_AllowedNwInfo_ObjectIdentity = ObjectIdentity
allowedNwInfo = _AllowedNwInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 12)
)
_AllowedNwInfoTable_Object = MibTable
allowedNwInfoTable = _AllowedNwInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 12, 1)
)
if mibBuilder.loadTexts:
    allowedNwInfoTable.setStatus("current")
_AllowedNwInfoEntry_Object = MibTableRow
allowedNwInfoEntry = _AllowedNwInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 12, 1, 1)
)
allowedNwInfoEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "allowedNwInfoIndex"),
)
if mibBuilder.loadTexts:
    allowedNwInfoEntry.setStatus("current")
_AllowedNwInfoIndex_Type = Integer32
_AllowedNwInfoIndex_Object = MibTableColumn
allowedNwInfoIndex = _AllowedNwInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 12, 1, 1, 1),
    _AllowedNwInfoIndex_Type()
)
allowedNwInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allowedNwInfoIndex.setStatus("current")


class _AllowedNwInfoIpver_Type(Integer32):
    """Custom type allowedNwInfoIpver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AllowedNwInfoIpver_Type.__name__ = "Integer32"
_AllowedNwInfoIpver_Object = MibTableColumn
allowedNwInfoIpver = _AllowedNwInfoIpver_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 12, 1, 1, 2),
    _AllowedNwInfoIpver_Type()
)
allowedNwInfoIpver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allowedNwInfoIpver.setStatus("current")
_AllowedNwInfoVlan_Type = Integer32
_AllowedNwInfoVlan_Object = MibTableColumn
allowedNwInfoVlan = _AllowedNwInfoVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 12, 1, 1, 3),
    _AllowedNwInfoVlan_Type()
)
allowedNwInfoVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allowedNwInfoVlan.setStatus("current")
_AllowedNwInfoBeginIpAddr_Type = DisplayString
_AllowedNwInfoBeginIpAddr_Object = MibTableColumn
allowedNwInfoBeginIpAddr = _AllowedNwInfoBeginIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 12, 1, 1, 4),
    _AllowedNwInfoBeginIpAddr_Type()
)
allowedNwInfoBeginIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allowedNwInfoBeginIpAddr.setStatus("current")
_AllowedNwInfoEndIpAddr_Type = DisplayString
_AllowedNwInfoEndIpAddr_Object = MibTableColumn
allowedNwInfoEndIpAddr = _AllowedNwInfoEndIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 12, 1, 1, 5),
    _AllowedNwInfoEndIpAddr_Type()
)
allowedNwInfoEndIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allowedNwInfoEndIpAddr.setStatus("current")
_AllowedNwInfoNetMask_Type = DisplayString
_AllowedNwInfoNetMask_Object = MibTableColumn
allowedNwInfoNetMask = _AllowedNwInfoNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 12, 1, 1, 6),
    _AllowedNwInfoNetMask_Type()
)
allowedNwInfoNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allowedNwInfoNetMask.setStatus("current")
_AllowedNwInfoIp6Prefix_Type = Integer32
_AllowedNwInfoIp6Prefix_Object = MibTableColumn
allowedNwInfoIp6Prefix = _AllowedNwInfoIp6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 3, 12, 1, 1, 7),
    _AllowedNwInfoIp6Prefix_Type()
)
allowedNwInfoIp6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allowedNwInfoIp6Prefix.setStatus("current")
_Layer3Oper_ObjectIdentity = ObjectIdentity
layer3Oper = _Layer3Oper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4)
)
_VrrpOper_ObjectIdentity = ObjectIdentity
vrrpOper = _VrrpOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4, 1)
)
_VrrpOperVirtRtrTable_Object = MibTable
vrrpOperVirtRtrTable = _VrrpOperVirtRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    vrrpOperVirtRtrTable.setStatus("current")
_VrrpOperVirtRtrEntry_Object = MibTableRow
vrrpOperVirtRtrEntry = _VrrpOperVirtRtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4, 1, 1, 1)
)
vrrpOperVirtRtrEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-NETWORK-MIB", "vrrpOperVirtRtrIndex"),
)
if mibBuilder.loadTexts:
    vrrpOperVirtRtrEntry.setStatus("current")
_VrrpOperVirtRtrIndex_Type = Integer32
_VrrpOperVirtRtrIndex_Object = MibTableColumn
vrrpOperVirtRtrIndex = _VrrpOperVirtRtrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4, 1, 2),
    _VrrpOperVirtRtrGroupBackup_Type()
)
vrrpOperVirtRtrGroupBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpOperVirtRtrGroupBackup.setStatus("current")
_IpOper_ObjectIdentity = ObjectIdentity
ipOper = _IpOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4, 2)
)
_BgpOper_ObjectIdentity = ObjectIdentity
bgpOper = _BgpOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4, 2, 1)
)
_BgpOperStart_ObjectIdentity = ObjectIdentity
bgpOperStart = _BgpOperStart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4, 2, 1, 1)
)


class _BgpOperStartPeerNum_Type(Integer32):
    """Custom type bgpOperStartPeerNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BgpOperStartPeerNum_Type.__name__ = "Integer32"
_BgpOperStartPeerNum_Object = MibScalar
bgpOperStartPeerNum = _BgpOperStartPeerNum_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4, 2, 1, 1, 1),
    _BgpOperStartPeerNum_Type()
)
bgpOperStartPeerNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bgpOperStartPeerNum.setStatus("current")


class _BgpOperStartSess_Type(Integer32):
    """Custom type bgpOperStartSess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("start", 2))
    )


_BgpOperStartSess_Type.__name__ = "Integer32"
_BgpOperStartSess_Object = MibScalar
bgpOperStartSess = _BgpOperStartSess_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4, 2, 1, 1, 2),
    _BgpOperStartSess_Type()
)
bgpOperStartSess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bgpOperStartSess.setStatus("current")
_BgpOperStop_ObjectIdentity = ObjectIdentity
bgpOperStop = _BgpOperStop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4, 2, 1, 2)
)


class _BgpOperStopPeerNum_Type(Integer32):
    """Custom type bgpOperStopPeerNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BgpOperStopPeerNum_Type.__name__ = "Integer32"
_BgpOperStopPeerNum_Object = MibScalar
bgpOperStopPeerNum = _BgpOperStopPeerNum_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4, 2, 1, 2, 1),
    _BgpOperStopPeerNum_Type()
)
bgpOperStopPeerNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bgpOperStopPeerNum.setStatus("current")


class _BgpOperStopSess_Type(Integer32):
    """Custom type bgpOperStopSess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("stop", 2))
    )


_BgpOperStopSess_Type.__name__ = "Integer32"
_BgpOperStopSess_Object = MibScalar
bgpOperStopSess = _BgpOperStopSess_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4, 2, 1, 2, 2),
    _BgpOperStopSess_Type()
)
bgpOperStopSess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bgpOperStopSess.setStatus("current")
_GarpOper_ObjectIdentity = ObjectIdentity
garpOper = _GarpOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4, 2, 2)
)
_GarpOperIpAddr_Type = IpAddress
_GarpOperIpAddr_Object = MibScalar
garpOperIpAddr = _GarpOperIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4, 2, 2, 1),
    _GarpOperIpAddr_Type()
)
garpOperIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    garpOperIpAddr.setStatus("current")


class _GarpOperVlanNumber_Type(Integer32):
    """Custom type garpOperVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4090),
    )


_GarpOperVlanNumber_Type.__name__ = "Integer32"
_GarpOperVlanNumber_Object = MibScalar
garpOperVlanNumber = _GarpOperVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4, 2, 2, 2),
    _GarpOperVlanNumber_Type()
)
garpOperVlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    garpOperVlanNumber.setStatus("current")


class _GarpOperSend_Type(Integer32):
    """Custom type garpOperSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("ok", 1),
          ("send", 2))
    )


_GarpOperSend_Type.__name__ = "Integer32"
_GarpOperSend_Object = MibScalar
garpOperSend = _GarpOperSend_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 3, 4, 2, 2, 3),
    _GarpOperSend_Type()
)
garpOperSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    garpOperSend.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTEON-CHEETAH-NETWORK-MIB",
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
       "ipCurCfgIntfIpVer": ipCurCfgIntfIpVer,
       "ipCurCfgIntfIpv6Addr": ipCurCfgIntfIpv6Addr,
       "ipCurCfgIntfPrefixLen": ipCurCfgIntfPrefixLen,
       "ipCurCfgIntfRouteAdv": ipCurCfgIntfRouteAdv,
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
       "ipNewCfgIntfIpVer": ipNewCfgIntfIpVer,
       "ipNewCfgIntfIpv6Addr": ipNewCfgIntfIpv6Addr,
       "ipNewCfgIntfPrefixLen": ipNewCfgIntfPrefixLen,
       "ipNewCfgIntfRouteAdv": ipNewCfgIntfRouteAdv,
       "ipGatewayCfg": ipGatewayCfg,
       "ipCurCfgGwMetric": ipCurCfgGwMetric,
       "ipNewCfgGwMetric": ipNewCfgGwMetric,
       "ipGatewayTableMax": ipGatewayTableMax,
       "ipCurCfgGwTable": ipCurCfgGwTable,
       "ipCurCfgGwEntry": ipCurCfgGwEntry,
       "ipCurCfgGwIndex": ipCurCfgGwIndex,
       "ipCurCfgGwAddr": ipCurCfgGwAddr,
       "ipCurCfgGwInterval": ipCurCfgGwInterval,
       "ipCurCfgGwRetry": ipCurCfgGwRetry,
       "ipCurCfgGwState": ipCurCfgGwState,
       "ipCurCfgGwArp": ipCurCfgGwArp,
       "ipCurCfgGwVlan": ipCurCfgGwVlan,
       "ipCurCfgGwPriority": ipCurCfgGwPriority,
       "ipCurCfgGwIpVer": ipCurCfgGwIpVer,
       "ipCurCfgGwIpv6Addr": ipCurCfgGwIpv6Addr,
       "ipNewCfgGwTable": ipNewCfgGwTable,
       "ipNewCfgGwEntry": ipNewCfgGwEntry,
       "ipNewCfgGwIndex": ipNewCfgGwIndex,
       "ipNewCfgGwAddr": ipNewCfgGwAddr,
       "ipNewCfgGwInterval": ipNewCfgGwInterval,
       "ipNewCfgGwRetry": ipNewCfgGwRetry,
       "ipNewCfgGwState": ipNewCfgGwState,
       "ipNewCfgGwDelete": ipNewCfgGwDelete,
       "ipNewCfgGwArp": ipNewCfgGwArp,
       "ipNewCfgGwVlan": ipNewCfgGwVlan,
       "ipNewCfgGwPriority": ipNewCfgGwPriority,
       "ipNewCfgGwIpVer": ipNewCfgGwIpVer,
       "ipNewCfgGwIpv6Addr": ipNewCfgGwIpv6Addr,
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
       "ipv6CurCfgStaticRouteTable": ipv6CurCfgStaticRouteTable,
       "ipv6CurCfgStaticRouteEntry": ipv6CurCfgStaticRouteEntry,
       "ipv6CurCfgStaticRouteIndx": ipv6CurCfgStaticRouteIndx,
       "ipv6CurCfgStaticRouteDestIp": ipv6CurCfgStaticRouteDestIp,
       "ipv6CurCfgStaticRouteMask": ipv6CurCfgStaticRouteMask,
       "ipv6CurCfgStaticRouteGateway": ipv6CurCfgStaticRouteGateway,
       "ipv6CurCfgStaticRouteInterface": ipv6CurCfgStaticRouteInterface,
       "ipv6NewCfgStaticRouteTable": ipv6NewCfgStaticRouteTable,
       "ipv6NewCfgStaticRouteEntry": ipv6NewCfgStaticRouteEntry,
       "ipv6NewCfgStaticRouteIndx": ipv6NewCfgStaticRouteIndx,
       "ipv6NewCfgStaticRouteDestIp": ipv6NewCfgStaticRouteDestIp,
       "ipv6NewCfgStaticRouteMask": ipv6NewCfgStaticRouteMask,
       "ipv6NewCfgStaticRouteGateway": ipv6NewCfgStaticRouteGateway,
       "ipv6NewCfgStaticRouteAction": ipv6NewCfgStaticRouteAction,
       "ipv6NewCfgStaticRouteInterface": ipv6NewCfgStaticRouteInterface,
       "ipForwardCfg": ipForwardCfg,
       "ipFwdGeneralCfg": ipFwdGeneralCfg,
       "ipFwdCurCfgState": ipFwdCurCfgState,
       "ipFwdNewCfgState": ipFwdNewCfgState,
       "ipFwdCurCfgDirectedBcast": ipFwdCurCfgDirectedBcast,
       "ipFwdNewCfgDirectedBcast": ipFwdNewCfgDirectedBcast,
       "ipFwdCurCfgNoICMPRedirect": ipFwdCurCfgNoICMPRedirect,
       "ipFwdNewCfgNoICMPRedirect": ipFwdNewCfgNoICMPRedirect,
       "ipFwdCurCfgRtCache": ipFwdCurCfgRtCache,
       "ipFwdNewCfgRtCache": ipFwdNewCfgRtCache,
       "ipFwdPortTableMaxSize": ipFwdPortTableMaxSize,
       "ipFwdCurCfgPortTable": ipFwdCurCfgPortTable,
       "ipFwdCurCfgPortEntry": ipFwdCurCfgPortEntry,
       "ipFwdCurCfgPortIndex": ipFwdCurCfgPortIndex,
       "ipFwdCurCfgPortState": ipFwdCurCfgPortState,
       "ipFwdNewCfgPortTable": ipFwdNewCfgPortTable,
       "ipFwdNewCfgPortEntry": ipFwdNewCfgPortEntry,
       "ipFwdNewCfgPortIndex": ipFwdNewCfgPortIndex,
       "ipFwdNewCfgPortState": ipFwdNewCfgPortState,
       "ipFwdLocalTableMaxSize": ipFwdLocalTableMaxSize,
       "ipFwdCurCfgLocalTable": ipFwdCurCfgLocalTable,
       "ipFwdCurCfgLocalEntry": ipFwdCurCfgLocalEntry,
       "ipFwdCurCfgLocalIndex": ipFwdCurCfgLocalIndex,
       "ipFwdCurCfgLocalSubnet": ipFwdCurCfgLocalSubnet,
       "ipFwdCurCfgLocalMask": ipFwdCurCfgLocalMask,
       "ipFwdNewCfgLocalTable": ipFwdNewCfgLocalTable,
       "ipFwdNewCfgLocalEntry": ipFwdNewCfgLocalEntry,
       "ipFwdNewCfgLocalIndex": ipFwdNewCfgLocalIndex,
       "ipFwdNewCfgLocalSubnet": ipFwdNewCfgLocalSubnet,
       "ipFwdNewCfgLocalMask": ipFwdNewCfgLocalMask,
       "ipFwdNewCfgLocalDelete": ipFwdNewCfgLocalDelete,
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
       "vrrpCurCfgGenHoldoff": vrrpCurCfgGenHoldoff,
       "vrrpNewCfgGenHoldoff": vrrpNewCfgGenHoldoff,
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
       "vrrpCurCfgVirtRtrVersion": vrrpCurCfgVirtRtrVersion,
       "vrrpCurCfgVirtRtrIpv6Addr": vrrpCurCfgVirtRtrIpv6Addr,
       "vrrpCurCfgVirtRtrIpv6Interval": vrrpCurCfgVirtRtrIpv6Interval,
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
       "vrrpNewCfgVirtRtrVersion": vrrpNewCfgVirtRtrVersion,
       "vrrpNewCfgVirtRtrIpv6Addr": vrrpNewCfgVirtRtrIpv6Addr,
       "vrrpNewCfgVirtRtrIpv6Interval": vrrpNewCfgVirtRtrIpv6Interval,
       "vrrpIfTableMaxSize": vrrpIfTableMaxSize,
       "vrrpCurCfgIfTable": vrrpCurCfgIfTable,
       "vrrpCurCfgIfTableEntry": vrrpCurCfgIfTableEntry,
       "vrrpCurCfgIfIndx": vrrpCurCfgIfIndx,
       "vrrpCurCfgIfAuthType": vrrpCurCfgIfAuthType,
       "vrrpCurCfgIfPasswd": vrrpCurCfgIfPasswd,
       "vrrpCurCfgIfIpAddr": vrrpCurCfgIfIpAddr,
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
       "vrrpCurCfgVirtRtrGrpVersion": vrrpCurCfgVirtRtrGrpVersion,
       "vrrpCurCfgVirtRtrGrpIpv6Interval": vrrpCurCfgVirtRtrGrpIpv6Interval,
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
       "vrrpNewCfgVirtRtrGrpVersion": vrrpNewCfgVirtRtrGrpVersion,
       "vrrpNewCfgVirtRtrGrpIpv6Interval": vrrpNewCfgVirtRtrGrpIpv6Interval,
       "vrrpVirtRtrVrGrpTableMaxSize": vrrpVirtRtrVrGrpTableMaxSize,
       "vrrpCurCfgVirtRtrVrGrpTable": vrrpCurCfgVirtRtrVrGrpTable,
       "vrrpCurCfgVirtRtrVrGrpTableEntry": vrrpCurCfgVirtRtrVrGrpTableEntry,
       "vrrpCurCfgVirtRtrVrGrpIndx": vrrpCurCfgVirtRtrVrGrpIndx,
       "vrrpCurCfgVirtRtrVrGrpName": vrrpCurCfgVirtRtrVrGrpName,
       "vrrpCurCfgVirtRtrVrGrpState": vrrpCurCfgVirtRtrVrGrpState,
       "vrrpCurCfgVirtRtrVrGrpBmap": vrrpCurCfgVirtRtrVrGrpBmap,
       "vrrpCurCfgVirtRtrVrGrpPriority": vrrpCurCfgVirtRtrVrGrpPriority,
       "vrrpCurCfgVirtRtrVrGrpTckIpIntf": vrrpCurCfgVirtRtrVrGrpTckIpIntf,
       "vrrpCurCfgVirtRtrVrGrpTckVlanPort": vrrpCurCfgVirtRtrVrGrpTckVlanPort,
       "vrrpCurCfgVirtRtrVrGrpTckL4Port": vrrpCurCfgVirtRtrVrGrpTckL4Port,
       "vrrpCurCfgVirtRtrVrGrpTckRServer": vrrpCurCfgVirtRtrVrGrpTckRServer,
       "vrrpCurCfgVirtRtrVrGrpTckHsrp": vrrpCurCfgVirtRtrVrGrpTckHsrp,
       "vrrpCurCfgVirtRtrVrGrpTckHsrv": vrrpCurCfgVirtRtrVrGrpTckHsrv,
       "vrrpCurCfgVirtRtrVrGrpTckVirtRtrNo": vrrpCurCfgVirtRtrVrGrpTckVirtRtrNo,
       "vrrpCurCfgVirtRtrVrGrpAdd": vrrpCurCfgVirtRtrVrGrpAdd,
       "vrrpCurCfgVirtRtrVrGrpAdverInterval": vrrpCurCfgVirtRtrVrGrpAdverInterval,
       "vrrpCurCfgVirtRtrVrGrpPreemption": vrrpCurCfgVirtRtrVrGrpPreemption,
       "vrrpCurCfgVirtRtrVrGrpSharing": vrrpCurCfgVirtRtrVrGrpSharing,
       "vrrpNewCfgVirtRtrVrGrpTable": vrrpNewCfgVirtRtrVrGrpTable,
       "vrrpNewCfgVirtRtrVrGrpTableEntry": vrrpNewCfgVirtRtrVrGrpTableEntry,
       "vrrpNewCfgVirtRtrVrGrpIndx": vrrpNewCfgVirtRtrVrGrpIndx,
       "vrrpNewCfgVirtRtrVrGrpName": vrrpNewCfgVirtRtrVrGrpName,
       "vrrpNewCfgVirtRtrVrGrpAdd": vrrpNewCfgVirtRtrVrGrpAdd,
       "vrrpNewCfgVirtRtrVrGrpRem": vrrpNewCfgVirtRtrVrGrpRem,
       "vrrpNewCfgVirtRtrVrGrpState": vrrpNewCfgVirtRtrVrGrpState,
       "vrrpNewCfgVirtRtrVrGrpDelete": vrrpNewCfgVirtRtrVrGrpDelete,
       "vrrpNewCfgVirtRtrVrGrpBmap": vrrpNewCfgVirtRtrVrGrpBmap,
       "vrrpNewCfgVirtRtrVrGrpPriority": vrrpNewCfgVirtRtrVrGrpPriority,
       "vrrpNewCfgVirtRtrVrGrpTckIpIntf": vrrpNewCfgVirtRtrVrGrpTckIpIntf,
       "vrrpNewCfgVirtRtrVrGrpTckVlanPort": vrrpNewCfgVirtRtrVrGrpTckVlanPort,
       "vrrpNewCfgVirtRtrVrGrpTckL4Port": vrrpNewCfgVirtRtrVrGrpTckL4Port,
       "vrrpNewCfgVirtRtrVrGrpTckRServer": vrrpNewCfgVirtRtrVrGrpTckRServer,
       "vrrpNewCfgVirtRtrVrGrpTckHsrp": vrrpNewCfgVirtRtrVrGrpTckHsrp,
       "vrrpNewCfgVirtRtrVrGrpTckHsrv": vrrpNewCfgVirtRtrVrGrpTckHsrv,
       "vrrpNewCfgVirtRtrVrGrpTckVirtRtrNo": vrrpNewCfgVirtRtrVrGrpTckVirtRtrNo,
       "vrrpNewCfgVirtRtrVrGrpAdverInterval": vrrpNewCfgVirtRtrVrGrpAdverInterval,
       "vrrpNewCfgVirtRtrVrGrpPreemption": vrrpNewCfgVirtRtrVrGrpPreemption,
       "vrrpNewCfgVirtRtrVrGrpSharing": vrrpNewCfgVirtRtrVrGrpSharing,
       "arpCfg": arpCfg,
       "arpCurCfgReARPPeriod": arpCurCfgReARPPeriod,
       "arpNewCfgReARPPeriod": arpNewCfgReARPPeriod,
       "ipBootpCfg": ipBootpCfg,
       "ipCurCfgBootpAddr": ipCurCfgBootpAddr,
       "ipNewCfgBootpAddr": ipNewCfgBootpAddr,
       "ipCurCfgBootpAddr2": ipCurCfgBootpAddr2,
       "ipNewCfgBootpAddr2": ipNewCfgBootpAddr2,
       "ipCurCfgBootpState": ipCurCfgBootpState,
       "ipNewCfgBootpState": ipNewCfgBootpState,
       "dnsCfg": dnsCfg,
       "dnsCurCfgPrimaryIpAddr": dnsCurCfgPrimaryIpAddr,
       "dnsNewCfgPrimaryIpAddr": dnsNewCfgPrimaryIpAddr,
       "dnsCurCfgSecondaryIpAddr": dnsCurCfgSecondaryIpAddr,
       "dnsNewCfgSecondaryIpAddr": dnsNewCfgSecondaryIpAddr,
       "dnsCurCfgDomainName": dnsCurCfgDomainName,
       "dnsNewCfgDomainName": dnsNewCfgDomainName,
       "dnsCurCfgPrimaryIpv6Addr": dnsCurCfgPrimaryIpv6Addr,
       "dnsNewCfgPrimaryIpv6Addr": dnsNewCfgPrimaryIpv6Addr,
       "dnsCurCfgSecondaryIpv6Addr": dnsCurCfgSecondaryIpv6Addr,
       "dnsNewCfgSecondaryIpv6Addr": dnsNewCfgSecondaryIpv6Addr,
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
       "bgpCfg": bgpCfg,
       "bgpGeneral": bgpGeneral,
       "bgpCurCfgState": bgpCurCfgState,
       "bgpNewCfgState": bgpNewCfgState,
       "bgpCurCfgLocalPref": bgpCurCfgLocalPref,
       "bgpNewCfgLocalPref": bgpNewCfgLocalPref,
       "bgpCurCfgMaxASPath": bgpCurCfgMaxASPath,
       "bgpNewCfgMaxASPath": bgpNewCfgMaxASPath,
       "bgpCurCfgASNumber": bgpCurCfgASNumber,
       "bgpNewCfgASNumber": bgpNewCfgASNumber,
       "bgpPeerTableMax": bgpPeerTableMax,
       "bgpCurCfgPeerTable": bgpCurCfgPeerTable,
       "bgpCurCfgPeerEntry": bgpCurCfgPeerEntry,
       "bgpCurCfgPeerIndex": bgpCurCfgPeerIndex,
       "bgpCurCfgPeerRemoteAddr": bgpCurCfgPeerRemoteAddr,
       "bgpCurCfgPeerRemoteAs": bgpCurCfgPeerRemoteAs,
       "bgpCurCfgPeerTtl": bgpCurCfgPeerTtl,
       "bgpCurCfgPeerState": bgpCurCfgPeerState,
       "bgpCurCfgPeerMetric": bgpCurCfgPeerMetric,
       "bgpCurCfgPeerDefaultAction": bgpCurCfgPeerDefaultAction,
       "bgpCurCfgPeerOspfState": bgpCurCfgPeerOspfState,
       "bgpCurCfgPeerFixedState": bgpCurCfgPeerFixedState,
       "bgpCurCfgPeerStaticState": bgpCurCfgPeerStaticState,
       "bgpCurCfgPeerVipState": bgpCurCfgPeerVipState,
       "bgpCurCfgPeerInRmapList": bgpCurCfgPeerInRmapList,
       "bgpCurCfgPeerOutRmapList": bgpCurCfgPeerOutRmapList,
       "bgpCurCfgPeerHoldTime": bgpCurCfgPeerHoldTime,
       "bgpCurCfgPeerKeepAlive": bgpCurCfgPeerKeepAlive,
       "bgpCurCfgPeerMinTime": bgpCurCfgPeerMinTime,
       "bgpCurCfgPeerConRetry": bgpCurCfgPeerConRetry,
       "bgpCurCfgPeerMinAS": bgpCurCfgPeerMinAS,
       "bgpCurCfgPeerRipState": bgpCurCfgPeerRipState,
       "bgpNewCfgPeerTable": bgpNewCfgPeerTable,
       "bgpNewCfgPeerEntry": bgpNewCfgPeerEntry,
       "bgpNewCfgPeerIndex": bgpNewCfgPeerIndex,
       "bgpNewCfgPeerRemoteAddr": bgpNewCfgPeerRemoteAddr,
       "bgpNewCfgPeerRemoteAs": bgpNewCfgPeerRemoteAs,
       "bgpNewCfgPeerTtl": bgpNewCfgPeerTtl,
       "bgpNewCfgPeerState": bgpNewCfgPeerState,
       "bgpNewCfgPeerDelete": bgpNewCfgPeerDelete,
       "bgpNewCfgPeerMetric": bgpNewCfgPeerMetric,
       "bgpNewCfgPeerDefaultAction": bgpNewCfgPeerDefaultAction,
       "bgpNewCfgPeerOspfState": bgpNewCfgPeerOspfState,
       "bgpNewCfgPeerFixedState": bgpNewCfgPeerFixedState,
       "bgpNewCfgPeerStaticState": bgpNewCfgPeerStaticState,
       "bgpNewCfgPeerVipState": bgpNewCfgPeerVipState,
       "bgpNewCfgPeerInRmapList": bgpNewCfgPeerInRmapList,
       "bgpNewCfgPeerOutRmapList": bgpNewCfgPeerOutRmapList,
       "bgpNewCfgPeerAddInRmap": bgpNewCfgPeerAddInRmap,
       "bgpNewCfgPeerAddOutRmap": bgpNewCfgPeerAddOutRmap,
       "bgpNewCfgPeerRemoveInRmap": bgpNewCfgPeerRemoveInRmap,
       "bgpNewCfgPeerRemoveOutRmap": bgpNewCfgPeerRemoveOutRmap,
       "bgpNewCfgPeerHoldTime": bgpNewCfgPeerHoldTime,
       "bgpNewCfgPeerKeepAlive": bgpNewCfgPeerKeepAlive,
       "bgpNewCfgPeerMinTime": bgpNewCfgPeerMinTime,
       "bgpNewCfgPeerConRetry": bgpNewCfgPeerConRetry,
       "bgpNewCfgPeerMinAS": bgpNewCfgPeerMinAS,
       "bgpNewCfgPeerRipState": bgpNewCfgPeerRipState,
       "bgpAggrTableMax": bgpAggrTableMax,
       "bgpCurCfgAggrTable": bgpCurCfgAggrTable,
       "bgpCurCfgAggrEntry": bgpCurCfgAggrEntry,
       "bgpCurCfgAggrIndex": bgpCurCfgAggrIndex,
       "bgpCurCfgAggrAddr": bgpCurCfgAggrAddr,
       "bgpCurCfgAggrMask": bgpCurCfgAggrMask,
       "bgpCurCfgAggrState": bgpCurCfgAggrState,
       "bgpNewCfgAggrTable": bgpNewCfgAggrTable,
       "bgpNewCfgAggrEntry": bgpNewCfgAggrEntry,
       "bgpNewCfgAggrIndex": bgpNewCfgAggrIndex,
       "bgpNewCfgAggrAddr": bgpNewCfgAggrAddr,
       "bgpNewCfgAggrMask": bgpNewCfgAggrMask,
       "bgpNewCfgAggrState": bgpNewCfgAggrState,
       "bgpNewCfgAggrDelete": bgpNewCfgAggrDelete,
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
       "ospfCurCfgLsdb": ospfCurCfgLsdb,
       "ospfNewCfgLsdb": ospfNewCfgLsdb,
       "ospfCurCfgAreaTable": ospfCurCfgAreaTable,
       "ospfCurCfgAreaEntry": ospfCurCfgAreaEntry,
       "ospfCurCfgAreaIndex": ospfCurCfgAreaIndex,
       "ospfCurCfgAreaId": ospfCurCfgAreaId,
       "ospfCurCfgAreaSpfInterval": ospfCurCfgAreaSpfInterval,
       "ospfCurCfgAreaAuthType": ospfCurCfgAreaAuthType,
       "ospfCurCfgAreaType": ospfCurCfgAreaType,
       "ospfCurCfgAreaMetric": ospfCurCfgAreaMetric,
       "ospfCurCfgAreaState": ospfCurCfgAreaState,
       "ospfNewCfgAreaTable": ospfNewCfgAreaTable,
       "ospfNewCfgAreaEntry": ospfNewCfgAreaEntry,
       "ospfNewCfgAreaIndex": ospfNewCfgAreaIndex,
       "ospfNewCfgAreaId": ospfNewCfgAreaId,
       "ospfNewCfgAreaSpfInterval": ospfNewCfgAreaSpfInterval,
       "ospfNewCfgAreaAuthType": ospfNewCfgAreaAuthType,
       "ospfNewCfgAreaType": ospfNewCfgAreaType,
       "ospfNewCfgAreaMetric": ospfNewCfgAreaMetric,
       "ospfNewCfgAreaState": ospfNewCfgAreaState,
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
       "ospfRedistributeEbgp": ospfRedistributeEbgp,
       "ospfCurCfgEbgpMetric": ospfCurCfgEbgpMetric,
       "ospfNewCfgEbgpMetric": ospfNewCfgEbgpMetric,
       "ospfCurCfgEbgpMetricType": ospfCurCfgEbgpMetricType,
       "ospfNewCfgEbgpMetricType": ospfNewCfgEbgpMetricType,
       "ospfCurCfgEbgpOutRmapList": ospfCurCfgEbgpOutRmapList,
       "ospfNewCfgEbgpOutRmapList": ospfNewCfgEbgpOutRmapList,
       "ospfNewCfgEbgpAddOutRmap": ospfNewCfgEbgpAddOutRmap,
       "ospfNewCfgEbgpRemoveOutRmap": ospfNewCfgEbgpRemoveOutRmap,
       "ospfRedistributeIbgp": ospfRedistributeIbgp,
       "ospfCurCfgIbgpMetric": ospfCurCfgIbgpMetric,
       "ospfNewCfgIbgpMetric": ospfNewCfgIbgpMetric,
       "ospfCurCfgIbgpMetricType": ospfCurCfgIbgpMetricType,
       "ospfNewCfgIbgpMetricType": ospfNewCfgIbgpMetricType,
       "ospfCurCfgIbgpOutRmapList": ospfCurCfgIbgpOutRmapList,
       "ospfNewCfgIbgpOutRmapList": ospfNewCfgIbgpOutRmapList,
       "ospfNewCfgIbgpAddOutRmap": ospfNewCfgIbgpAddOutRmap,
       "ospfNewCfgIbgpRemoveOutRmap": ospfNewCfgIbgpRemoveOutRmap,
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
       "ospfCurCfgIntfMdkey": ospfCurCfgIntfMdkey,
       "ospfCurCfgIntfAreaId": ospfCurCfgIntfAreaId,
       "ospfCurCfgIntfPriority": ospfCurCfgIntfPriority,
       "ospfCurCfgIntfCost": ospfCurCfgIntfCost,
       "ospfCurCfgIntfHello": ospfCurCfgIntfHello,
       "ospfCurCfgIntfDead": ospfCurCfgIntfDead,
       "ospfCurCfgIntfTransit": ospfCurCfgIntfTransit,
       "ospfCurCfgIntfRetrans": ospfCurCfgIntfRetrans,
       "ospfCurCfgIntfKey": ospfCurCfgIntfKey,
       "ospfCurCfgIntfState": ospfCurCfgIntfState,
       "ospfNewCfgIntfTable": ospfNewCfgIntfTable,
       "ospfNewCfgIntfEntry": ospfNewCfgIntfEntry,
       "ospfNewCfgIntfIndex": ospfNewCfgIntfIndex,
       "ospfNewCfgIntfId": ospfNewCfgIntfId,
       "ospfNewCfgIntfMdkey": ospfNewCfgIntfMdkey,
       "ospfNewCfgIntfAreaId": ospfNewCfgIntfAreaId,
       "ospfNewCfgIntfPriority": ospfNewCfgIntfPriority,
       "ospfNewCfgIntfCost": ospfNewCfgIntfCost,
       "ospfNewCfgIntfHello": ospfNewCfgIntfHello,
       "ospfNewCfgIntfDead": ospfNewCfgIntfDead,
       "ospfNewCfgIntfTransit": ospfNewCfgIntfTransit,
       "ospfNewCfgIntfRetrans": ospfNewCfgIntfRetrans,
       "ospfNewCfgIntfKey": ospfNewCfgIntfKey,
       "ospfNewCfgIntfState": ospfNewCfgIntfState,
       "ospfNewCfgIntfDelete": ospfNewCfgIntfDelete,
       "ospfCurCfgVirtIntfTable": ospfCurCfgVirtIntfTable,
       "ospfCurCfgVirtIntfEntry": ospfCurCfgVirtIntfEntry,
       "ospfCurCfgVirtIntfIndex": ospfCurCfgVirtIntfIndex,
       "ospfCurCfgVirtIntfAreaId": ospfCurCfgVirtIntfAreaId,
       "ospfCurCfgVirtIntfNbr": ospfCurCfgVirtIntfNbr,
       "ospfCurCfgVirtIntfMdkey": ospfCurCfgVirtIntfMdkey,
       "ospfCurCfgVirtIntfHello": ospfCurCfgVirtIntfHello,
       "ospfCurCfgVirtIntfDead": ospfCurCfgVirtIntfDead,
       "ospfCurCfgVirtIntfTransit": ospfCurCfgVirtIntfTransit,
       "ospfCurCfgVirtIntfRetrans": ospfCurCfgVirtIntfRetrans,
       "ospfCurCfgVirtIntfKey": ospfCurCfgVirtIntfKey,
       "ospfCurCfgVirtIntfState": ospfCurCfgVirtIntfState,
       "ospfNewCfgVirtIntfTable": ospfNewCfgVirtIntfTable,
       "ospfNewCfgVirtIntfEntry": ospfNewCfgVirtIntfEntry,
       "ospfNewCfgVirtIntfIndex": ospfNewCfgVirtIntfIndex,
       "ospfNewCfgVirtIntfAreaId": ospfNewCfgVirtIntfAreaId,
       "ospfNewCfgVirtIntfNbr": ospfNewCfgVirtIntfNbr,
       "ospfNewCfgVirtIntfMdkey": ospfNewCfgVirtIntfMdkey,
       "ospfNewCfgVirtIntfHello": ospfNewCfgVirtIntfHello,
       "ospfNewCfgVirtIntfDead": ospfNewCfgVirtIntfDead,
       "ospfNewCfgVirtIntfTransit": ospfNewCfgVirtIntfTransit,
       "ospfNewCfgVirtIntfRetrans": ospfNewCfgVirtIntfRetrans,
       "ospfNewCfgVirtIntfKey": ospfNewCfgVirtIntfKey,
       "ospfNewCfgVirtIntfState": ospfNewCfgVirtIntfState,
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
       "ospfNewCfgVisionAreaTable": ospfNewCfgVisionAreaTable,
       "ospfNewCfgVisionAreaEntry": ospfNewCfgVisionAreaEntry,
       "ospfNewCfgVisionAreaIndex": ospfNewCfgVisionAreaIndex,
       "ospfNewCfgVisionAreaId": ospfNewCfgVisionAreaId,
       "ospfNewCfgVisionAreaSpfInterval": ospfNewCfgVisionAreaSpfInterval,
       "ospfNewCfgVisionAreaAuthType": ospfNewCfgVisionAreaAuthType,
       "ospfNewCfgVisionAreaType": ospfNewCfgVisionAreaType,
       "ospfNewCfgVisionAreaMetric": ospfNewCfgVisionAreaMetric,
       "ospfNewCfgVisionAreaState": ospfNewCfgVisionAreaState,
       "ospfNewCfgVisionAreaDelete": ospfNewCfgVisionAreaDelete,
       "ipGeneralCfg": ipGeneralCfg,
       "ipCurCfgRouterID": ipCurCfgRouterID,
       "ipNewCfgRouterID": ipNewCfgRouterID,
       "ipCurCfgASNumber": ipCurCfgASNumber,
       "ipNewCfgASNumber": ipNewCfgASNumber,
       "ipStaticArpCfg": ipStaticArpCfg,
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
       "ipStaticArpTableNextAvailableIndex": ipStaticArpTableNextAvailableIndex,
       "rip2Cfg": rip2Cfg,
       "ripCurCfgIntfTable": ripCurCfgIntfTable,
       "ripCurCfgIntfEntry": ripCurCfgIntfEntry,
       "ripCurCfgIntfIndex": ripCurCfgIntfIndex,
       "ripCurCfgIntfVersion": ripCurCfgIntfVersion,
       "ripCurCfgIntfState": ripCurCfgIntfState,
       "ripCurCfgIntfListen": ripCurCfgIntfListen,
       "ripCurCfgIntfDefListen": ripCurCfgIntfDefListen,
       "ripCurCfgIntfTrigUpdate": ripCurCfgIntfTrigUpdate,
       "ripCurCfgIntfMcastUpdate": ripCurCfgIntfMcastUpdate,
       "ripCurCfgIntfPoisonReverse": ripCurCfgIntfPoisonReverse,
       "ripCurCfgIntfSupply": ripCurCfgIntfSupply,
       "ripCurCfgIntfMetric": ripCurCfgIntfMetric,
       "ripCurCfgIntfAuth": ripCurCfgIntfAuth,
       "ripCurCfgIntfKey": ripCurCfgIntfKey,
       "ripCurCfgIntfDefault": ripCurCfgIntfDefault,
       "ripNewCfgIntfTable": ripNewCfgIntfTable,
       "ripNewCfgIntfEntry": ripNewCfgIntfEntry,
       "ripNewCfgIntfIndex": ripNewCfgIntfIndex,
       "ripNewCfgIntfVersion": ripNewCfgIntfVersion,
       "ripNewCfgIntfSupply": ripNewCfgIntfSupply,
       "ripNewCfgIntfListen": ripNewCfgIntfListen,
       "ripNewCfgIntfDefListen": ripNewCfgIntfDefListen,
       "ripNewCfgIntfTrigUpdate": ripNewCfgIntfTrigUpdate,
       "ripNewCfgIntfMcastUpdate": ripNewCfgIntfMcastUpdate,
       "ripNewCfgIntfPoisonReverse": ripNewCfgIntfPoisonReverse,
       "ripNewCfgIntfState": ripNewCfgIntfState,
       "ripNewCfgIntfMetric": ripNewCfgIntfMetric,
       "ripNewCfgIntfAuth": ripNewCfgIntfAuth,
       "ripNewCfgIntfKey": ripNewCfgIntfKey,
       "ripNewCfgIntfDefault": ripNewCfgIntfDefault,
       "ripGeneral": ripGeneral,
       "rip2CurCfgState": rip2CurCfgState,
       "rip2NewCfgState": rip2NewCfgState,
       "rip2CurCfgUpdatePeriod": rip2CurCfgUpdatePeriod,
       "rip2NewCfgUpdatePeriod": rip2NewCfgUpdatePeriod,
       "rip2CurCfgVip": rip2CurCfgVip,
       "rip2NewCfgVip": rip2NewCfgVip,
       "rip2CurCfgStaticSupply": rip2CurCfgStaticSupply,
       "rip2NewCfgStaticSupply": rip2NewCfgStaticSupply,
       "layer3Stats": layer3Stats,
       "arpStats": arpStats,
       "arpStatEntries": arpStatEntries,
       "arpStatHighWater": arpStatHighWater,
       "arpStatMaxEntries": arpStatMaxEntries,
       "routeStats": routeStats,
       "routeStatEntries": routeStatEntries,
       "routeStatHighWater": routeStatHighWater,
       "routeStatMaxEntries": routeStatMaxEntries,
       "dnsStats": dnsStats,
       "dnsStatInGoodDnsRequests": dnsStatInGoodDnsRequests,
       "dnsStatInBadDnsRequests": dnsStatInBadDnsRequests,
       "dnsStatOutDnsRequests": dnsStatOutDnsRequests,
       "vrrpStats": vrrpStats,
       "vrrpStatInAdvers": vrrpStatInAdvers,
       "vrrpStatOutAdvers": vrrpStatOutAdvers,
       "vrrpStatOutBadAdvers": vrrpStatOutBadAdvers,
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
       "ip6Stats": ip6Stats,
       "ip6InReceives": ip6InReceives,
       "ip6ForwDatagrams": ip6ForwDatagrams,
       "ip6InDelivers": ip6InDelivers,
       "ip6InDiscards": ip6InDiscards,
       "ip6InUnknownProtos": ip6InUnknownProtos,
       "ip6InAddrErrors": ip6InAddrErrors,
       "ip6OutRequests": ip6OutRequests,
       "ip6OutNoRoutes": ip6OutNoRoutes,
       "ip6ReasmOKs": ip6ReasmOKs,
       "ip6ReasmFails": ip6ReasmFails,
       "ip6icmpInMsgs": ip6icmpInMsgs,
       "ip6icmpOutMsgs": ip6icmpOutMsgs,
       "ip6icmpInErrors": ip6icmpInErrors,
       "ip6icmpOutErrors": ip6icmpOutErrors,
       "icmp6Stats": icmp6Stats,
       "icmp6StatsTable": icmp6StatsTable,
       "icmp6StatsEntry": icmp6StatsEntry,
       "icmp6StatsIndx": icmp6StatsIndx,
       "icmp6IntfIndex": icmp6IntfIndex,
       "icmp6InMsgs": icmp6InMsgs,
       "icmp6InErrors": icmp6InErrors,
       "icmp6InEchos": icmp6InEchos,
       "icmp6InEchoReps": icmp6InEchoReps,
       "icmp6InNSs": icmp6InNSs,
       "icmp6InNAs": icmp6InNAs,
       "icmp6InRSs": icmp6InRSs,
       "icmp6InRAs": icmp6InRAs,
       "icmp6InDestUnreachs": icmp6InDestUnreachs,
       "icmp6InTimeExcds": icmp6InTimeExcds,
       "icmp6InTooBigs": icmp6InTooBigs,
       "icmp6InParmProbs": icmp6InParmProbs,
       "icmp6InRedirects": icmp6InRedirects,
       "icmp6OutMsgs": icmp6OutMsgs,
       "icmp6OutErrors": icmp6OutErrors,
       "icmp6OutEchos": icmp6OutEchos,
       "icmp6OutEchoReps": icmp6OutEchoReps,
       "icmp6OutNSs": icmp6OutNSs,
       "icmp6OutNAs": icmp6OutNAs,
       "icmp6OutRSs": icmp6OutRSs,
       "icmp6OutRAs": icmp6OutRAs,
       "icmp6OutRedirects": icmp6OutRedirects,
       "ip6gwStats": ip6gwStats,
       "ip6GwStatsTable": ip6GwStatsTable,
       "ip6GwStatsEntry": ip6GwStatsEntry,
       "ip6GwStatsIndex": ip6GwStatsIndex,
       "ip6GwIndex": ip6GwIndex,
       "ip6GwEchoreq": ip6GwEchoreq,
       "ip6GwEchoresp": ip6GwEchoresp,
       "ip6GwFails": ip6GwFails,
       "ip6GwMaster": ip6GwMaster,
       "ip6IfIndex": ip6IfIndex,
       "ip6GwRetry": ip6GwRetry,
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
       "tcpStats": tcpStats,
       "tcpStatCurConn": tcpStatCurConn,
       "tcpStatCurInConn": tcpStatCurInConn,
       "tcpStatCurOutConn": tcpStatCurOutConn,
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
       "ipRouteInfoGateway1": ipRouteInfoGateway1,
       "ipRouteInfoGateway2": ipRouteInfoGateway2,
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
       "vrrpInfoVirtRtrState": vrrpInfoVirtRtrState,
       "vrrpInfoVirtRtrOwnership": vrrpInfoVirtRtrOwnership,
       "vrrpInfoVirtRtrServer": vrrpInfoVirtRtrServer,
       "vrrpInfoVirtRtrProxy": vrrpInfoVirtRtrProxy,
       "vrrpInfoVirtRtrPriority": vrrpInfoVirtRtrPriority,
       "ospfinfo": ospfinfo,
       "ospfGeneralInfo": ospfGeneralInfo,
       "ospfStartTime": ospfStartTime,
       "ospfProcessUptime": ospfProcessUptime,
       "ospfLsTypesSupported": ospfLsTypesSupported,
       "ospfIntfCountForRouter": ospfIntfCountForRouter,
       "ospfVlinkCountForRouter": ospfVlinkCountForRouter,
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
       "ospfTotalNumberOfInterfaces": ospfTotalNumberOfInterfaces,
       "ospfNumberOfInterfacesUp": ospfNumberOfInterfacesUp,
       "ospfNumberOfLsdbEntries": ospfNumberOfLsdbEntries,
       "ospfAreaInfoId": ospfAreaInfoId,
       "ospfIntfInfoTable": ospfIntfInfoTable,
       "ospfIntfInfoEntry": ospfIntfInfoEntry,
       "ospfIfInfoIndex": ospfIfInfoIndex,
       "ospfIfDesignatedRouterIP": ospfIfDesignatedRouterIP,
       "ospfIfBackupDesignatedRouterIP": ospfIfBackupDesignatedRouterIP,
       "ospfIfWaitInterval": ospfIfWaitInterval,
       "ospfIfTotalNeighbours": ospfIfTotalNeighbours,
       "ospfIfInfoIpAddress": ospfIfInfoIpAddress,
       "ospfIfNbrTable": ospfIfNbrTable,
       "ospfIfNbrEntry": ospfIfNbrEntry,
       "ospfIfNbrIntfIndex": ospfIfNbrIntfIndex,
       "ospfIfNbrIpAddr": ospfIfNbrIpAddr,
       "ospfIfNbrPriority": ospfIfNbrPriority,
       "ospfIfNbrState": ospfIfNbrState,
       "ospfIfNbrDesignatedRtr": ospfIfNbrDesignatedRtr,
       "ospfIfNbrBackupDesignatedRtr": ospfIfNbrBackupDesignatedRtr,
       "ospfIfNbrIpAddress": ospfIfNbrIpAddress,
       "gatewayInfo": gatewayInfo,
       "gatewayInfoTable": gatewayInfoTable,
       "gatewayInfoEntry": gatewayInfoEntry,
       "gatewayInfoIndex": gatewayInfoIndex,
       "gatewayInfoAddr": gatewayInfoAddr,
       "gatewayInfoVlan": gatewayInfoVlan,
       "gatewayInfoStatus": gatewayInfoStatus,
       "gatewayInfoAddr6": gatewayInfoAddr6,
       "nbrcacheInfo": nbrcacheInfo,
       "nbrcacheInfoTable": nbrcacheInfoTable,
       "nbrcacheInfoEntry": nbrcacheInfoEntry,
       "nbrcacheInfoIndex": nbrcacheInfoIndex,
       "nbrcacheInfoDestIp": nbrcacheInfoDestIp,
       "nbrcacheInfoState": nbrcacheInfoState,
       "nbrcacheInfoType": nbrcacheInfoType,
       "nbrcacheInfoMacAddr": nbrcacheInfoMacAddr,
       "nbrcacheInfoVlanId": nbrcacheInfoVlanId,
       "nbrcacheInfoPortNum": nbrcacheInfoPortNum,
       "nbrcacheClear": nbrcacheClear,
       "nbrcacheInfoTotDynamicEntries": nbrcacheInfoTotDynamicEntries,
       "nbrcacheInfoTotLocalEntries": nbrcacheInfoTotLocalEntries,
       "nbrcacheInfoTotOtherEntries": nbrcacheInfoTotOtherEntries,
       "ipRoute6Info": ipRoute6Info,
       "ipRoute6InfoTable": ipRoute6InfoTable,
       "ipRoute6InfoEntry": ipRoute6InfoEntry,
       "ipRoute6InfoIndx": ipRoute6InfoIndx,
       "ipRoute6InfoDestIp6": ipRoute6InfoDestIp6,
       "ipRoute6InfoInterface": ipRoute6InfoInterface,
       "ipRoute6InfoNextHop": ipRoute6InfoNextHop,
       "ipRoute6InfoProto": ipRoute6InfoProto,
       "ipIntfInfo": ipIntfInfo,
       "ipIntfInfoTable": ipIntfInfoTable,
       "intfInfoEntry": intfInfoEntry,
       "intfInfoIndex": intfInfoIndex,
       "intfInfoIpver": intfInfoIpver,
       "intfInfoAddr": intfInfoAddr,
       "intfInfoNetMask": intfInfoNetMask,
       "intfInfoBcastAddr": intfInfoBcastAddr,
       "intfInfoVlan": intfInfoVlan,
       "intfInfoStatus": intfInfoStatus,
       "intfInfoLinkLocalAddr": intfInfoLinkLocalAddr,
       "rip2Info": rip2Info,
       "rip2GeneralInfo": rip2GeneralInfo,
       "ripInfoState": ripInfoState,
       "ripInfoUpdatePeriod": ripInfoUpdatePeriod,
       "ripInfoVip": ripInfoVip,
       "ripInfoStaticSupply": ripInfoStaticSupply,
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
       "rip2RoutesInfo": rip2RoutesInfo,
       "rip2RoutesInfoTable": rip2RoutesInfoTable,
       "rip2RoutesInfoEntry": rip2RoutesInfoEntry,
       "rip2RoutesInfoDestIndex": rip2RoutesInfoDestIndex,
       "rip2RoutesInfoNxtHopIndex": rip2RoutesInfoNxtHopIndex,
       "rip2RoutesInfoDestination": rip2RoutesInfoDestination,
       "rip2RoutesInfoIpAddress": rip2RoutesInfoIpAddress,
       "rip2RoutesInfoMetric": rip2RoutesInfoMetric,
       "allowedNwInfo": allowedNwInfo,
       "allowedNwInfoTable": allowedNwInfoTable,
       "allowedNwInfoEntry": allowedNwInfoEntry,
       "allowedNwInfoIndex": allowedNwInfoIndex,
       "allowedNwInfoIpver": allowedNwInfoIpver,
       "allowedNwInfoVlan": allowedNwInfoVlan,
       "allowedNwInfoBeginIpAddr": allowedNwInfoBeginIpAddr,
       "allowedNwInfoEndIpAddr": allowedNwInfoEndIpAddr,
       "allowedNwInfoNetMask": allowedNwInfoNetMask,
       "allowedNwInfoIp6Prefix": allowedNwInfoIp6Prefix,
       "layer3Oper": layer3Oper,
       "vrrpOper": vrrpOper,
       "vrrpOperVirtRtrTable": vrrpOperVirtRtrTable,
       "vrrpOperVirtRtrEntry": vrrpOperVirtRtrEntry,
       "vrrpOperVirtRtrIndex": vrrpOperVirtRtrIndex,
       "vrrpOperVirtRtrBackup": vrrpOperVirtRtrBackup,
       "vrrpOperVirtRtrGroupBackup": vrrpOperVirtRtrGroupBackup,
       "ipOper": ipOper,
       "bgpOper": bgpOper,
       "bgpOperStart": bgpOperStart,
       "bgpOperStartPeerNum": bgpOperStartPeerNum,
       "bgpOperStartSess": bgpOperStartSess,
       "bgpOperStop": bgpOperStop,
       "bgpOperStopPeerNum": bgpOperStopPeerNum,
       "bgpOperStopSess": bgpOperStopSess,
       "garpOper": garpOper,
       "garpOperIpAddr": garpOperIpAddr,
       "garpOperVlanNumber": garpOperVlanNumber,
       "garpOperSend": garpOperSend}
)

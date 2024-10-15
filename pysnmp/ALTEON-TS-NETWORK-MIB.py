# SNMP MIB module (ALTEON-TS-NETWORK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTEON-TS-NETWORK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:02 2024
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

(switch,) = mibBuilder.importSymbols(
    "ALTEON-ROOT-MIB",
    "switch")

(information,
 operCmds,
 stats) = mibBuilder.importSymbols(
    "ALTEON-TIGON-SWITCH-MIB",
    "information",
    "operCmds",
    "stats")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Iprouting_ObjectIdentity = ObjectIdentity
iprouting = _Iprouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3)
)
_IpInterfaceTableMax_Type = Integer32
_IpInterfaceTableMax_Object = MibScalar
ipInterfaceTableMax = _IpInterfaceTableMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 1),
    _IpInterfaceTableMax_Type()
)
ipInterfaceTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceTableMax.setStatus("mandatory")
_IpCurCfgIntfTable_Object = MibTable
ipCurCfgIntfTable = _IpCurCfgIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ipCurCfgIntfTable.setStatus("mandatory")
_IpCurCfgIntfEntry_Object = MibTableRow
ipCurCfgIntfEntry = _IpCurCfgIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 2, 1)
)
ipCurCfgIntfEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ipCurCfgIntfIndex"),
)
if mibBuilder.loadTexts:
    ipCurCfgIntfEntry.setStatus("mandatory")
_IpCurCfgIntfIndex_Type = Integer32
_IpCurCfgIntfIndex_Object = MibTableColumn
ipCurCfgIntfIndex = _IpCurCfgIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 2, 1, 1),
    _IpCurCfgIntfIndex_Type()
)
ipCurCfgIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfIndex.setStatus("mandatory")
_IpCurCfgIntfAddr_Type = IpAddress
_IpCurCfgIntfAddr_Object = MibTableColumn
ipCurCfgIntfAddr = _IpCurCfgIntfAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 2, 1, 2),
    _IpCurCfgIntfAddr_Type()
)
ipCurCfgIntfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfAddr.setStatus("mandatory")
_IpCurCfgIntfMask_Type = IpAddress
_IpCurCfgIntfMask_Object = MibTableColumn
ipCurCfgIntfMask = _IpCurCfgIntfMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 2, 1, 3),
    _IpCurCfgIntfMask_Type()
)
ipCurCfgIntfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfMask.setStatus("mandatory")
_IpCurCfgIntfBroadcast_Type = IpAddress
_IpCurCfgIntfBroadcast_Object = MibTableColumn
ipCurCfgIntfBroadcast = _IpCurCfgIntfBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 2, 1, 4),
    _IpCurCfgIntfBroadcast_Type()
)
ipCurCfgIntfBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfBroadcast.setStatus("mandatory")


class _IpCurCfgIntfVlan_Type(Integer32):
    """Custom type ipCurCfgIntfVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IpCurCfgIntfVlan_Type.__name__ = "Integer32"
_IpCurCfgIntfVlan_Object = MibTableColumn
ipCurCfgIntfVlan = _IpCurCfgIntfVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 2, 1, 5),
    _IpCurCfgIntfVlan_Type()
)
ipCurCfgIntfVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfVlan.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 2, 1, 6),
    _IpCurCfgIntfState_Type()
)
ipCurCfgIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 2, 1, 7),
    _IpCurCfgIntfBootpRelay_Type()
)
ipCurCfgIntfBootpRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgIntfBootpRelay.setStatus("mandatory")
_IpNewCfgIntfTable_Object = MibTable
ipNewCfgIntfTable = _IpNewCfgIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ipNewCfgIntfTable.setStatus("mandatory")
_IpNewCfgIntfEntry_Object = MibTableRow
ipNewCfgIntfEntry = _IpNewCfgIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3, 1)
)
ipNewCfgIntfEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ipNewCfgIntfIndex"),
)
if mibBuilder.loadTexts:
    ipNewCfgIntfEntry.setStatus("mandatory")
_IpNewCfgIntfIndex_Type = Integer32
_IpNewCfgIntfIndex_Object = MibTableColumn
ipNewCfgIntfIndex = _IpNewCfgIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3, 1, 1),
    _IpNewCfgIntfIndex_Type()
)
ipNewCfgIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgIntfIndex.setStatus("mandatory")
_IpNewCfgIntfAddr_Type = IpAddress
_IpNewCfgIntfAddr_Object = MibTableColumn
ipNewCfgIntfAddr = _IpNewCfgIntfAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3, 1, 2),
    _IpNewCfgIntfAddr_Type()
)
ipNewCfgIntfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgIntfAddr.setStatus("mandatory")
_IpNewCfgIntfMask_Type = IpAddress
_IpNewCfgIntfMask_Object = MibTableColumn
ipNewCfgIntfMask = _IpNewCfgIntfMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3, 1, 3),
    _IpNewCfgIntfMask_Type()
)
ipNewCfgIntfMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgIntfMask.setStatus("mandatory")
_IpNewCfgIntfBroadcast_Type = IpAddress
_IpNewCfgIntfBroadcast_Object = MibTableColumn
ipNewCfgIntfBroadcast = _IpNewCfgIntfBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3, 1, 4),
    _IpNewCfgIntfBroadcast_Type()
)
ipNewCfgIntfBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgIntfBroadcast.setStatus("mandatory")


class _IpNewCfgIntfVlan_Type(Integer32):
    """Custom type ipNewCfgIntfVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IpNewCfgIntfVlan_Type.__name__ = "Integer32"
_IpNewCfgIntfVlan_Object = MibTableColumn
ipNewCfgIntfVlan = _IpNewCfgIntfVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3, 1, 5),
    _IpNewCfgIntfVlan_Type()
)
ipNewCfgIntfVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgIntfVlan.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3, 1, 6),
    _IpNewCfgIntfState_Type()
)
ipNewCfgIntfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgIntfState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3, 1, 7),
    _IpNewCfgIntfDelete_Type()
)
ipNewCfgIntfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgIntfDelete.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 3, 1, 8),
    _IpNewCfgIntfBootpRelay_Type()
)
ipNewCfgIntfBootpRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgIntfBootpRelay.setStatus("mandatory")
_IpGatewayTableMax_Type = Integer32
_IpGatewayTableMax_Object = MibScalar
ipGatewayTableMax = _IpGatewayTableMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 4),
    _IpGatewayTableMax_Type()
)
ipGatewayTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGatewayTableMax.setStatus("mandatory")
_IpCurCfgGwTable_Object = MibTable
ipCurCfgGwTable = _IpCurCfgGwTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 5)
)
if mibBuilder.loadTexts:
    ipCurCfgGwTable.setStatus("mandatory")
_IpCurCfgGwEntry_Object = MibTableRow
ipCurCfgGwEntry = _IpCurCfgGwEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 5, 1)
)
ipCurCfgGwEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ipCurCfgGwIndex"),
)
if mibBuilder.loadTexts:
    ipCurCfgGwEntry.setStatus("mandatory")
_IpCurCfgGwIndex_Type = Integer32
_IpCurCfgGwIndex_Object = MibTableColumn
ipCurCfgGwIndex = _IpCurCfgGwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 5, 1, 1),
    _IpCurCfgGwIndex_Type()
)
ipCurCfgGwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwIndex.setStatus("mandatory")
_IpCurCfgGwAddr_Type = IpAddress
_IpCurCfgGwAddr_Object = MibTableColumn
ipCurCfgGwAddr = _IpCurCfgGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 5, 1, 2),
    _IpCurCfgGwAddr_Type()
)
ipCurCfgGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwAddr.setStatus("mandatory")


class _IpCurCfgGwInterval_Type(Integer32):
    """Custom type ipCurCfgGwInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_IpCurCfgGwInterval_Type.__name__ = "Integer32"
_IpCurCfgGwInterval_Object = MibTableColumn
ipCurCfgGwInterval = _IpCurCfgGwInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 5, 1, 3),
    _IpCurCfgGwInterval_Type()
)
ipCurCfgGwInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwInterval.setStatus("mandatory")


class _IpCurCfgGwRetry_Type(Integer32):
    """Custom type ipCurCfgGwRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_IpCurCfgGwRetry_Type.__name__ = "Integer32"
_IpCurCfgGwRetry_Object = MibTableColumn
ipCurCfgGwRetry = _IpCurCfgGwRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 5, 1, 4),
    _IpCurCfgGwRetry_Type()
)
ipCurCfgGwRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwRetry.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 5, 1, 5),
    _IpCurCfgGwState_Type()
)
ipCurCfgGwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 5, 1, 6),
    _IpCurCfgGwArp_Type()
)
ipCurCfgGwArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwArp.setStatus("mandatory")


class _IpCurCfgGwVlan_Type(Integer32):
    """Custom type ipCurCfgGwVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_IpCurCfgGwVlan_Type.__name__ = "Integer32"
_IpCurCfgGwVlan_Object = MibTableColumn
ipCurCfgGwVlan = _IpCurCfgGwVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 5, 1, 7),
    _IpCurCfgGwVlan_Type()
)
ipCurCfgGwVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwVlan.setStatus("mandatory")
_IpNewCfgGwTable_Object = MibTable
ipNewCfgGwTable = _IpNewCfgGwTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6)
)
if mibBuilder.loadTexts:
    ipNewCfgGwTable.setStatus("mandatory")
_IpNewCfgGwEntry_Object = MibTableRow
ipNewCfgGwEntry = _IpNewCfgGwEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6, 1)
)
ipNewCfgGwEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ipNewCfgGwIndex"),
)
if mibBuilder.loadTexts:
    ipNewCfgGwEntry.setStatus("mandatory")
_IpNewCfgGwIndex_Type = Integer32
_IpNewCfgGwIndex_Object = MibTableColumn
ipNewCfgGwIndex = _IpNewCfgGwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6, 1, 1),
    _IpNewCfgGwIndex_Type()
)
ipNewCfgGwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgGwIndex.setStatus("mandatory")
_IpNewCfgGwAddr_Type = IpAddress
_IpNewCfgGwAddr_Object = MibTableColumn
ipNewCfgGwAddr = _IpNewCfgGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6, 1, 2),
    _IpNewCfgGwAddr_Type()
)
ipNewCfgGwAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgGwAddr.setStatus("mandatory")


class _IpNewCfgGwInterval_Type(Integer32):
    """Custom type ipNewCfgGwInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_IpNewCfgGwInterval_Type.__name__ = "Integer32"
_IpNewCfgGwInterval_Object = MibTableColumn
ipNewCfgGwInterval = _IpNewCfgGwInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6, 1, 3),
    _IpNewCfgGwInterval_Type()
)
ipNewCfgGwInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgGwInterval.setStatus("mandatory")


class _IpNewCfgGwRetry_Type(Integer32):
    """Custom type ipNewCfgGwRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_IpNewCfgGwRetry_Type.__name__ = "Integer32"
_IpNewCfgGwRetry_Object = MibTableColumn
ipNewCfgGwRetry = _IpNewCfgGwRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6, 1, 4),
    _IpNewCfgGwRetry_Type()
)
ipNewCfgGwRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgGwRetry.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6, 1, 5),
    _IpNewCfgGwState_Type()
)
ipNewCfgGwState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgGwState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6, 1, 6),
    _IpNewCfgGwDelete_Type()
)
ipNewCfgGwDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgGwDelete.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6, 1, 7),
    _IpNewCfgGwArp_Type()
)
ipNewCfgGwArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgGwArp.setStatus("mandatory")


class _IpNewCfgGwVlan_Type(Integer32):
    """Custom type ipNewCfgGwVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_IpNewCfgGwVlan_Type.__name__ = "Integer32"
_IpNewCfgGwVlan_Object = MibTableColumn
ipNewCfgGwVlan = _IpNewCfgGwVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 6, 1, 8),
    _IpNewCfgGwVlan_Type()
)
ipNewCfgGwVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgGwVlan.setStatus("mandatory")
_IpCurCfgStaticRouteTable_Object = MibTable
ipCurCfgStaticRouteTable = _IpCurCfgStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 7)
)
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteTable.setStatus("mandatory")
_IpCurCfgStaticRouteEntry_Object = MibTableRow
ipCurCfgStaticRouteEntry = _IpCurCfgStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 7, 1)
)
ipCurCfgStaticRouteEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ipCurCfgStaticRouteIndx"),
)
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteEntry.setStatus("mandatory")
_IpCurCfgStaticRouteIndx_Type = Integer32
_IpCurCfgStaticRouteIndx_Object = MibTableColumn
ipCurCfgStaticRouteIndx = _IpCurCfgStaticRouteIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 7, 1, 1),
    _IpCurCfgStaticRouteIndx_Type()
)
ipCurCfgStaticRouteIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteIndx.setStatus("mandatory")
_IpCurCfgStaticRouteDestIp_Type = IpAddress
_IpCurCfgStaticRouteDestIp_Object = MibTableColumn
ipCurCfgStaticRouteDestIp = _IpCurCfgStaticRouteDestIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 7, 1, 2),
    _IpCurCfgStaticRouteDestIp_Type()
)
ipCurCfgStaticRouteDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteDestIp.setStatus("mandatory")
_IpCurCfgStaticRouteMask_Type = IpAddress
_IpCurCfgStaticRouteMask_Object = MibTableColumn
ipCurCfgStaticRouteMask = _IpCurCfgStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 7, 1, 3),
    _IpCurCfgStaticRouteMask_Type()
)
ipCurCfgStaticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteMask.setStatus("mandatory")
_IpCurCfgStaticRouteGateway_Type = IpAddress
_IpCurCfgStaticRouteGateway_Object = MibTableColumn
ipCurCfgStaticRouteGateway = _IpCurCfgStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 7, 1, 4),
    _IpCurCfgStaticRouteGateway_Type()
)
ipCurCfgStaticRouteGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteGateway.setStatus("mandatory")
_IpCurCfgStaticRouteInterface_Type = Integer32
_IpCurCfgStaticRouteInterface_Object = MibTableColumn
ipCurCfgStaticRouteInterface = _IpCurCfgStaticRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 7, 1, 5),
    _IpCurCfgStaticRouteInterface_Type()
)
ipCurCfgStaticRouteInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticRouteInterface.setStatus("mandatory")
_IpNewCfgStaticRouteTable_Object = MibTable
ipNewCfgStaticRouteTable = _IpNewCfgStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 8)
)
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteTable.setStatus("mandatory")
_IpNewCfgStaticRouteEntry_Object = MibTableRow
ipNewCfgStaticRouteEntry = _IpNewCfgStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 8, 1)
)
ipNewCfgStaticRouteEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ipNewCfgStaticRouteIndx"),
)
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteEntry.setStatus("mandatory")
_IpNewCfgStaticRouteIndx_Type = Integer32
_IpNewCfgStaticRouteIndx_Object = MibTableColumn
ipNewCfgStaticRouteIndx = _IpNewCfgStaticRouteIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 8, 1, 1),
    _IpNewCfgStaticRouteIndx_Type()
)
ipNewCfgStaticRouteIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteIndx.setStatus("mandatory")
_IpNewCfgStaticRouteDestIp_Type = IpAddress
_IpNewCfgStaticRouteDestIp_Object = MibTableColumn
ipNewCfgStaticRouteDestIp = _IpNewCfgStaticRouteDestIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 8, 1, 2),
    _IpNewCfgStaticRouteDestIp_Type()
)
ipNewCfgStaticRouteDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteDestIp.setStatus("mandatory")
_IpNewCfgStaticRouteMask_Type = IpAddress
_IpNewCfgStaticRouteMask_Object = MibTableColumn
ipNewCfgStaticRouteMask = _IpNewCfgStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 8, 1, 3),
    _IpNewCfgStaticRouteMask_Type()
)
ipNewCfgStaticRouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteMask.setStatus("mandatory")
_IpNewCfgStaticRouteGateway_Type = IpAddress
_IpNewCfgStaticRouteGateway_Object = MibTableColumn
ipNewCfgStaticRouteGateway = _IpNewCfgStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 8, 1, 4),
    _IpNewCfgStaticRouteGateway_Type()
)
ipNewCfgStaticRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteGateway.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 8, 1, 5),
    _IpNewCfgStaticRouteAction_Type()
)
ipNewCfgStaticRouteAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteAction.setStatus("mandatory")
_IpNewCfgStaticRouteInterface_Type = Integer32
_IpNewCfgStaticRouteInterface_Object = MibTableColumn
ipNewCfgStaticRouteInterface = _IpNewCfgStaticRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 8, 1, 6),
    _IpNewCfgStaticRouteInterface_Type()
)
ipNewCfgStaticRouteInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgStaticRouteInterface.setStatus("mandatory")
_IpForward_ObjectIdentity = ObjectIdentity
ipForward = _IpForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9)
)
_RipConfig_ObjectIdentity = ObjectIdentity
ripConfig = _RipConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 1),
    _RipCurCfgSupply_Type()
)
ripCurCfgSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgSupply.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 2),
    _RipNewCfgSupply_Type()
)
ripNewCfgSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgSupply.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 3),
    _RipCurCfgListen_Type()
)
ripCurCfgListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgListen.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 4),
    _RipNewCfgListen_Type()
)
ripNewCfgListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgListen.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 5),
    _RipCurCfgDefListen_Type()
)
ripCurCfgDefListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgDefListen.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 6),
    _RipNewCfgDefListen_Type()
)
ripNewCfgDefListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgDefListen.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 7),
    _RipCurCfgStaticSupply_Type()
)
ripCurCfgStaticSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgStaticSupply.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 8),
    _RipNewCfgStaticSupply_Type()
)
ripNewCfgStaticSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgStaticSupply.setStatus("mandatory")


class _RipCurCfgUpdatePeriod_Type(Integer32):
    """Custom type ripCurCfgUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_RipCurCfgUpdatePeriod_Type.__name__ = "Integer32"
_RipCurCfgUpdatePeriod_Object = MibScalar
ripCurCfgUpdatePeriod = _RipCurCfgUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 9),
    _RipCurCfgUpdatePeriod_Type()
)
ripCurCfgUpdatePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgUpdatePeriod.setStatus("mandatory")


class _RipNewCfgUpdatePeriod_Type(Integer32):
    """Custom type ripNewCfgUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_RipNewCfgUpdatePeriod_Type.__name__ = "Integer32"
_RipNewCfgUpdatePeriod_Object = MibScalar
ripNewCfgUpdatePeriod = _RipNewCfgUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 10),
    _RipNewCfgUpdatePeriod_Type()
)
ripNewCfgUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgUpdatePeriod.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 11),
    _RipCurCfgState_Type()
)
ripCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 12),
    _RipNewCfgState_Type()
)
ripNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 13),
    _RipCurCfgPoisonReverse_Type()
)
ripCurCfgPoisonReverse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgPoisonReverse.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 14),
    _RipNewCfgPoisonReverse_Type()
)
ripNewCfgPoisonReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgPoisonReverse.setStatus("mandatory")


class _RipCurCfgVip_Type(Integer32):
    """Custom type ripCurCfgVip based on Integer32"""
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


_RipCurCfgVip_Type.__name__ = "Integer32"
_RipCurCfgVip_Object = MibScalar
ripCurCfgVip = _RipCurCfgVip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 15),
    _RipCurCfgVip_Type()
)
ripCurCfgVip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCurCfgVip.setStatus("mandatory")


class _RipNewCfgVip_Type(Integer32):
    """Custom type ripNewCfgVip based on Integer32"""
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


_RipNewCfgVip_Type.__name__ = "Integer32"
_RipNewCfgVip_Object = MibScalar
ripNewCfgVip = _RipNewCfgVip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 1, 16),
    _RipNewCfgVip_Type()
)
ripNewCfgVip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNewCfgVip.setStatus("mandatory")
_IpFwdCurCfgPortTable_Object = MibTable
ipFwdCurCfgPortTable = _IpFwdCurCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 2)
)
if mibBuilder.loadTexts:
    ipFwdCurCfgPortTable.setStatus("mandatory")
_IpFwdCurCfgPortEntry_Object = MibTableRow
ipFwdCurCfgPortEntry = _IpFwdCurCfgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 2, 1)
)
ipFwdCurCfgPortEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ipFwdCurCfgPortIndex"),
)
if mibBuilder.loadTexts:
    ipFwdCurCfgPortEntry.setStatus("mandatory")
_IpFwdCurCfgPortIndex_Type = Integer32
_IpFwdCurCfgPortIndex_Object = MibTableColumn
ipFwdCurCfgPortIndex = _IpFwdCurCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 2, 1, 1),
    _IpFwdCurCfgPortIndex_Type()
)
ipFwdCurCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgPortIndex.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 2, 1, 2),
    _IpFwdCurCfgPortState_Type()
)
ipFwdCurCfgPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgPortState.setStatus("mandatory")
_IpFwdNewCfgPortTable_Object = MibTable
ipFwdNewCfgPortTable = _IpFwdNewCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 3)
)
if mibBuilder.loadTexts:
    ipFwdNewCfgPortTable.setStatus("mandatory")
_IpFwdNewCfgPortEntry_Object = MibTableRow
ipFwdNewCfgPortEntry = _IpFwdNewCfgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 3, 1)
)
ipFwdNewCfgPortEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ipFwdNewCfgPortIndex"),
)
if mibBuilder.loadTexts:
    ipFwdNewCfgPortEntry.setStatus("mandatory")
_IpFwdNewCfgPortIndex_Type = Integer32
_IpFwdNewCfgPortIndex_Object = MibTableColumn
ipFwdNewCfgPortIndex = _IpFwdNewCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 3, 1, 1),
    _IpFwdNewCfgPortIndex_Type()
)
ipFwdNewCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdNewCfgPortIndex.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 3, 1, 2),
    _IpFwdNewCfgPortState_Type()
)
ipFwdNewCfgPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFwdNewCfgPortState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 8),
    _IpFwdCurCfgState_Type()
)
ipFwdCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 9),
    _IpFwdNewCfgState_Type()
)
ipFwdNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFwdNewCfgState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 10),
    _IpFwdCurCfgDirectedBcast_Type()
)
ipFwdCurCfgDirectedBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgDirectedBcast.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 11),
    _IpFwdNewCfgDirectedBcast_Type()
)
ipFwdNewCfgDirectedBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFwdNewCfgDirectedBcast.setStatus("mandatory")
_IpFwdPortTableMaxSize_Type = Integer32
_IpFwdPortTableMaxSize_Object = MibScalar
ipFwdPortTableMaxSize = _IpFwdPortTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 12),
    _IpFwdPortTableMaxSize_Type()
)
ipFwdPortTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdPortTableMaxSize.setStatus("mandatory")
_IpFwdLocalTableMaxSize_Type = Integer32
_IpFwdLocalTableMaxSize_Object = MibScalar
ipFwdLocalTableMaxSize = _IpFwdLocalTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 13),
    _IpFwdLocalTableMaxSize_Type()
)
ipFwdLocalTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdLocalTableMaxSize.setStatus("mandatory")
_IpFwdCurCfgLocalTable_Object = MibTable
ipFwdCurCfgLocalTable = _IpFwdCurCfgLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 14)
)
if mibBuilder.loadTexts:
    ipFwdCurCfgLocalTable.setStatus("mandatory")
_IpFwdCurCfgLocalEntry_Object = MibTableRow
ipFwdCurCfgLocalEntry = _IpFwdCurCfgLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 14, 1)
)
ipFwdCurCfgLocalEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ipFwdCurCfgLocalIndex"),
)
if mibBuilder.loadTexts:
    ipFwdCurCfgLocalEntry.setStatus("mandatory")
_IpFwdCurCfgLocalIndex_Type = Integer32
_IpFwdCurCfgLocalIndex_Object = MibTableColumn
ipFwdCurCfgLocalIndex = _IpFwdCurCfgLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 14, 1, 1),
    _IpFwdCurCfgLocalIndex_Type()
)
ipFwdCurCfgLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgLocalIndex.setStatus("mandatory")
_IpFwdCurCfgLocalSubnet_Type = IpAddress
_IpFwdCurCfgLocalSubnet_Object = MibTableColumn
ipFwdCurCfgLocalSubnet = _IpFwdCurCfgLocalSubnet_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 14, 1, 2),
    _IpFwdCurCfgLocalSubnet_Type()
)
ipFwdCurCfgLocalSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgLocalSubnet.setStatus("mandatory")
_IpFwdCurCfgLocalMask_Type = IpAddress
_IpFwdCurCfgLocalMask_Object = MibTableColumn
ipFwdCurCfgLocalMask = _IpFwdCurCfgLocalMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 14, 1, 3),
    _IpFwdCurCfgLocalMask_Type()
)
ipFwdCurCfgLocalMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdCurCfgLocalMask.setStatus("mandatory")
_IpFwdNewCfgLocalTable_Object = MibTable
ipFwdNewCfgLocalTable = _IpFwdNewCfgLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 15)
)
if mibBuilder.loadTexts:
    ipFwdNewCfgLocalTable.setStatus("mandatory")
_IpFwdNewCfgLocalEntry_Object = MibTableRow
ipFwdNewCfgLocalEntry = _IpFwdNewCfgLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 15, 1)
)
ipFwdNewCfgLocalEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ipFwdNewCfgLocalIndex"),
)
if mibBuilder.loadTexts:
    ipFwdNewCfgLocalEntry.setStatus("mandatory")
_IpFwdNewCfgLocalIndex_Type = Integer32
_IpFwdNewCfgLocalIndex_Object = MibTableColumn
ipFwdNewCfgLocalIndex = _IpFwdNewCfgLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 15, 1, 1),
    _IpFwdNewCfgLocalIndex_Type()
)
ipFwdNewCfgLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwdNewCfgLocalIndex.setStatus("mandatory")
_IpFwdNewCfgLocalSubnet_Type = IpAddress
_IpFwdNewCfgLocalSubnet_Object = MibTableColumn
ipFwdNewCfgLocalSubnet = _IpFwdNewCfgLocalSubnet_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 15, 1, 2),
    _IpFwdNewCfgLocalSubnet_Type()
)
ipFwdNewCfgLocalSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFwdNewCfgLocalSubnet.setStatus("mandatory")
_IpFwdNewCfgLocalMask_Type = IpAddress
_IpFwdNewCfgLocalMask_Object = MibTableColumn
ipFwdNewCfgLocalMask = _IpFwdNewCfgLocalMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 15, 1, 3),
    _IpFwdNewCfgLocalMask_Type()
)
ipFwdNewCfgLocalMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFwdNewCfgLocalMask.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 9, 15, 1, 4),
    _IpFwdNewCfgLocalDelete_Type()
)
ipFwdNewCfgLocalDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFwdNewCfgLocalDelete.setStatus("mandatory")


class _ArpCurCfgReARPPeriod_Type(Integer32):
    """Custom type arpCurCfgReARPPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 120),
    )


_ArpCurCfgReARPPeriod_Type.__name__ = "Integer32"
_ArpCurCfgReARPPeriod_Object = MibScalar
arpCurCfgReARPPeriod = _ArpCurCfgReARPPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 10),
    _ArpCurCfgReARPPeriod_Type()
)
arpCurCfgReARPPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpCurCfgReARPPeriod.setStatus("mandatory")


class _ArpNewCfgReARPPeriod_Type(Integer32):
    """Custom type arpNewCfgReARPPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 120),
    )


_ArpNewCfgReARPPeriod_Type.__name__ = "Integer32"
_ArpNewCfgReARPPeriod_Object = MibScalar
arpNewCfgReARPPeriod = _ArpNewCfgReARPPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 11),
    _ArpNewCfgReARPPeriod_Type()
)
arpNewCfgReARPPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpNewCfgReARPPeriod.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 12),
    _IpCurCfgGwMetric_Type()
)
ipCurCfgGwMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgGwMetric.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 13),
    _IpNewCfgGwMetric_Type()
)
ipNewCfgGwMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgGwMetric.setStatus("mandatory")
_IpCurCfgBootpAddr_Type = IpAddress
_IpCurCfgBootpAddr_Object = MibScalar
ipCurCfgBootpAddr = _IpCurCfgBootpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 14),
    _IpCurCfgBootpAddr_Type()
)
ipCurCfgBootpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgBootpAddr.setStatus("mandatory")
_IpNewCfgBootpAddr_Type = IpAddress
_IpNewCfgBootpAddr_Object = MibScalar
ipNewCfgBootpAddr = _IpNewCfgBootpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 15),
    _IpNewCfgBootpAddr_Type()
)
ipNewCfgBootpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgBootpAddr.setStatus("mandatory")
_IpCurCfgBootpAddr2_Type = IpAddress
_IpCurCfgBootpAddr2_Object = MibScalar
ipCurCfgBootpAddr2 = _IpCurCfgBootpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 16),
    _IpCurCfgBootpAddr2_Type()
)
ipCurCfgBootpAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgBootpAddr2.setStatus("mandatory")
_IpNewCfgBootpAddr2_Type = IpAddress
_IpNewCfgBootpAddr2_Object = MibScalar
ipNewCfgBootpAddr2 = _IpNewCfgBootpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 17),
    _IpNewCfgBootpAddr2_Type()
)
ipNewCfgBootpAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgBootpAddr2.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 18),
    _IpCurCfgBootpState_Type()
)
ipCurCfgBootpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgBootpState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 19),
    _IpNewCfgBootpState_Type()
)
ipNewCfgBootpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewCfgBootpState.setStatus("mandatory")
_IpStaticRouteTableMaxSize_Type = Integer32
_IpStaticRouteTableMaxSize_Object = MibScalar
ipStaticRouteTableMaxSize = _IpStaticRouteTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 20),
    _IpStaticRouteTableMaxSize_Type()
)
ipStaticRouteTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStaticRouteTableMaxSize.setStatus("mandatory")
_OspfCfg_ObjectIdentity = ObjectIdentity
ospfCfg = _OspfCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21)
)
_OspfGeneral_ObjectIdentity = ObjectIdentity
ospfGeneral = _OspfGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 1)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 1, 1),
    _OspfCurCfgDefaultRouteMetric_Type()
)
ospfCurCfgDefaultRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgDefaultRouteMetric.setStatus("mandatory")


class _OspfNewCfgDefaultRouteMetric_Type(Integer32):
    """Custom type ospfNewCfgDefaultRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_OspfNewCfgDefaultRouteMetric_Type.__name__ = "Integer32"
_OspfNewCfgDefaultRouteMetric_Object = MibScalar
ospfNewCfgDefaultRouteMetric = _OspfNewCfgDefaultRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 1, 2),
    _OspfNewCfgDefaultRouteMetric_Type()
)
ospfNewCfgDefaultRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgDefaultRouteMetric.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 1, 3),
    _OspfCurCfgDefaultRouteMetricType_Type()
)
ospfCurCfgDefaultRouteMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgDefaultRouteMetricType.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 1, 4),
    _OspfNewCfgDefaultRouteMetricType_Type()
)
ospfNewCfgDefaultRouteMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgDefaultRouteMetricType.setStatus("mandatory")
_OspfIntfTableMaxSize_Type = Integer32
_OspfIntfTableMaxSize_Object = MibScalar
ospfIntfTableMaxSize = _OspfIntfTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 1, 5),
    _OspfIntfTableMaxSize_Type()
)
ospfIntfTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTableMaxSize.setStatus("mandatory")
_OspfAreaTableMaxSize_Type = Integer32
_OspfAreaTableMaxSize_Object = MibScalar
ospfAreaTableMaxSize = _OspfAreaTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 1, 6),
    _OspfAreaTableMaxSize_Type()
)
ospfAreaTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTableMaxSize.setStatus("mandatory")
_OspfRangeTableMaxSize_Type = Integer32
_OspfRangeTableMaxSize_Object = MibScalar
ospfRangeTableMaxSize = _OspfRangeTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 1, 7),
    _OspfRangeTableMaxSize_Type()
)
ospfRangeTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRangeTableMaxSize.setStatus("mandatory")
_OspfVirtIntfTableMaxSize_Type = Integer32
_OspfVirtIntfTableMaxSize_Object = MibScalar
ospfVirtIntfTableMaxSize = _OspfVirtIntfTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 1, 8),
    _OspfVirtIntfTableMaxSize_Type()
)
ospfVirtIntfTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtIntfTableMaxSize.setStatus("mandatory")
_OspfHostTableMaxSize_Type = Integer32
_OspfHostTableMaxSize_Object = MibScalar
ospfHostTableMaxSize = _OspfHostTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 1, 9),
    _OspfHostTableMaxSize_Type()
)
ospfHostTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfHostTableMaxSize.setStatus("mandatory")
_OspfCurCfgAreaTable_Object = MibTable
ospfCurCfgAreaTable = _OspfCurCfgAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 2)
)
if mibBuilder.loadTexts:
    ospfCurCfgAreaTable.setStatus("mandatory")
_OspfCurCfgAreaEntry_Object = MibTableRow
ospfCurCfgAreaEntry = _OspfCurCfgAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 2, 1)
)
ospfCurCfgAreaEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ospfCurCfgAreaIndex"),
    (0, "ALTEON-TS-NETWORK-MIB", "ospfCurCfgAreaId"),
)
if mibBuilder.loadTexts:
    ospfCurCfgAreaEntry.setStatus("mandatory")


class _OspfCurCfgAreaIndex_Type(Integer32):
    """Custom type ospfCurCfgAreaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_OspfCurCfgAreaIndex_Type.__name__ = "Integer32"
_OspfCurCfgAreaIndex_Object = MibTableColumn
ospfCurCfgAreaIndex = _OspfCurCfgAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 2, 1, 1),
    _OspfCurCfgAreaIndex_Type()
)
ospfCurCfgAreaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgAreaIndex.setStatus("mandatory")
_OspfCurCfgAreaId_Type = IpAddress
_OspfCurCfgAreaId_Object = MibTableColumn
ospfCurCfgAreaId = _OspfCurCfgAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 2, 1, 2),
    _OspfCurCfgAreaId_Type()
)
ospfCurCfgAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgAreaId.setStatus("mandatory")


class _OspfCurCfgAreaSpfInterval_Type(Integer32):
    """Custom type ospfCurCfgAreaSpfInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OspfCurCfgAreaSpfInterval_Type.__name__ = "Integer32"
_OspfCurCfgAreaSpfInterval_Object = MibTableColumn
ospfCurCfgAreaSpfInterval = _OspfCurCfgAreaSpfInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 2, 1, 3),
    _OspfCurCfgAreaSpfInterval_Type()
)
ospfCurCfgAreaSpfInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgAreaSpfInterval.setStatus("mandatory")


class _OspfCurCfgAreaAuthType_Type(Integer32):
    """Custom type ospfCurCfgAreaAuthType based on Integer32"""
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


_OspfCurCfgAreaAuthType_Type.__name__ = "Integer32"
_OspfCurCfgAreaAuthType_Object = MibTableColumn
ospfCurCfgAreaAuthType = _OspfCurCfgAreaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 2, 1, 4),
    _OspfCurCfgAreaAuthType_Type()
)
ospfCurCfgAreaAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCurCfgAreaAuthType.setStatus("mandatory")
_OspfNewCfgAreaTable_Object = MibTable
ospfNewCfgAreaTable = _OspfNewCfgAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 3)
)
if mibBuilder.loadTexts:
    ospfNewCfgAreaTable.setStatus("mandatory")
_OspfNewCfgAreaEntry_Object = MibTableRow
ospfNewCfgAreaEntry = _OspfNewCfgAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 3, 1)
)
ospfNewCfgAreaEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ospfNewCfgAreaIndex"),
    (0, "ALTEON-TS-NETWORK-MIB", "ospfNewCfgAreaId"),
)
if mibBuilder.loadTexts:
    ospfNewCfgAreaEntry.setStatus("mandatory")


class _OspfNewCfgAreaIndex_Type(Integer32):
    """Custom type ospfNewCfgAreaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_OspfNewCfgAreaIndex_Type.__name__ = "Integer32"
_OspfNewCfgAreaIndex_Object = MibTableColumn
ospfNewCfgAreaIndex = _OspfNewCfgAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 3, 1, 1),
    _OspfNewCfgAreaIndex_Type()
)
ospfNewCfgAreaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgAreaIndex.setStatus("mandatory")
_OspfNewCfgAreaId_Type = IpAddress
_OspfNewCfgAreaId_Object = MibTableColumn
ospfNewCfgAreaId = _OspfNewCfgAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 3, 1, 2),
    _OspfNewCfgAreaId_Type()
)
ospfNewCfgAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNewCfgAreaId.setStatus("mandatory")


class _OspfNewCfgAreaSpfInterval_Type(Integer32):
    """Custom type ospfNewCfgAreaSpfInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OspfNewCfgAreaSpfInterval_Type.__name__ = "Integer32"
_OspfNewCfgAreaSpfInterval_Object = MibTableColumn
ospfNewCfgAreaSpfInterval = _OspfNewCfgAreaSpfInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 3, 1, 3),
    _OspfNewCfgAreaSpfInterval_Type()
)
ospfNewCfgAreaSpfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgAreaSpfInterval.setStatus("mandatory")


class _OspfNewCfgAreaAuthType_Type(Integer32):
    """Custom type ospfNewCfgAreaAuthType based on Integer32"""
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


_OspfNewCfgAreaAuthType_Type.__name__ = "Integer32"
_OspfNewCfgAreaAuthType_Object = MibTableColumn
ospfNewCfgAreaAuthType = _OspfNewCfgAreaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 3, 21, 3, 1, 4),
    _OspfNewCfgAreaAuthType_Type()
)
ospfNewCfgAreaAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNewCfgAreaAuthType.setStatus("mandatory")
_RipStats_ObjectIdentity = ObjectIdentity
ripStats = _RipStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 1)
)
_RipStatInPkts_Type = Counter32
_RipStatInPkts_Object = MibScalar
ripStatInPkts = _RipStatInPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 1, 1),
    _RipStatInPkts_Type()
)
ripStatInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInPkts.setStatus("mandatory")
_RipStatOutPkts_Type = Counter32
_RipStatOutPkts_Object = MibScalar
ripStatOutPkts = _RipStatOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 1, 2),
    _RipStatOutPkts_Type()
)
ripStatOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatOutPkts.setStatus("mandatory")
_RipStatInErrorPkts_Type = Counter32
_RipStatInErrorPkts_Object = MibScalar
ripStatInErrorPkts = _RipStatInErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 1, 3),
    _RipStatInErrorPkts_Type()
)
ripStatInErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatInErrorPkts.setStatus("mandatory")
_RipStatRoutesAgedOut_Type = Counter32
_RipStatRoutesAgedOut_Object = MibScalar
ripStatRoutesAgedOut = _RipStatRoutesAgedOut_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 1, 4),
    _RipStatRoutesAgedOut_Type()
)
ripStatRoutesAgedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatRoutesAgedOut.setStatus("mandatory")
_ArpStats_ObjectIdentity = ObjectIdentity
arpStats = _ArpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 3)
)
_ArpStatEntries_Type = Gauge32
_ArpStatEntries_Object = MibScalar
arpStatEntries = _ArpStatEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 3, 1),
    _ArpStatEntries_Type()
)
arpStatEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpStatEntries.setStatus("mandatory")
_ArpStatHighWater_Type = Gauge32
_ArpStatHighWater_Object = MibScalar
arpStatHighWater = _ArpStatHighWater_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 3, 2),
    _ArpStatHighWater_Type()
)
arpStatHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpStatHighWater.setStatus("mandatory")
_ArpStatMaxEntries_Type = Gauge32
_ArpStatMaxEntries_Object = MibScalar
arpStatMaxEntries = _ArpStatMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 3, 3),
    _ArpStatMaxEntries_Type()
)
arpStatMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpStatMaxEntries.setStatus("mandatory")
_RouteStats_ObjectIdentity = ObjectIdentity
routeStats = _RouteStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 4)
)
_RouteStatEntries_Type = Gauge32
_RouteStatEntries_Object = MibScalar
routeStatEntries = _RouteStatEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 4, 1),
    _RouteStatEntries_Type()
)
routeStatEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatEntries.setStatus("mandatory")
_RouteStatHighWater_Type = Gauge32
_RouteStatHighWater_Object = MibScalar
routeStatHighWater = _RouteStatHighWater_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 4, 2),
    _RouteStatHighWater_Type()
)
routeStatHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatHighWater.setStatus("mandatory")
_RouteStatMaxEntries_Type = Gauge32
_RouteStatMaxEntries_Object = MibScalar
routeStatMaxEntries = _RouteStatMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 4, 3),
    _RouteStatMaxEntries_Type()
)
routeStatMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeStatMaxEntries.setStatus("mandatory")
_DnsStats_ObjectIdentity = ObjectIdentity
dnsStats = _DnsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 5)
)
_DnsStatInGoodDnsRequests_Type = Counter32
_DnsStatInGoodDnsRequests_Object = MibScalar
dnsStatInGoodDnsRequests = _DnsStatInGoodDnsRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 5, 1),
    _DnsStatInGoodDnsRequests_Type()
)
dnsStatInGoodDnsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsStatInGoodDnsRequests.setStatus("mandatory")
_DnsStatInBadDnsRequests_Type = Counter32
_DnsStatInBadDnsRequests_Object = MibScalar
dnsStatInBadDnsRequests = _DnsStatInBadDnsRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 5, 2),
    _DnsStatInBadDnsRequests_Type()
)
dnsStatInBadDnsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsStatInBadDnsRequests.setStatus("mandatory")
_VrrpStats_ObjectIdentity = ObjectIdentity
vrrpStats = _VrrpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 9)
)
_VrrpStatInAdvers_Type = Counter32
_VrrpStatInAdvers_Object = MibScalar
vrrpStatInAdvers = _VrrpStatInAdvers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 9, 1),
    _VrrpStatInAdvers_Type()
)
vrrpStatInAdvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatInAdvers.setStatus("mandatory")
_VrrpStatOutAdvers_Type = Counter32
_VrrpStatOutAdvers_Object = MibScalar
vrrpStatOutAdvers = _VrrpStatOutAdvers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 9, 2),
    _VrrpStatOutAdvers_Type()
)
vrrpStatOutAdvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatOutAdvers.setStatus("mandatory")
_VrrpStatOutBadAdvers_Type = Counter32
_VrrpStatOutBadAdvers_Object = MibScalar
vrrpStatOutBadAdvers = _VrrpStatOutBadAdvers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 9, 3),
    _VrrpStatOutBadAdvers_Type()
)
vrrpStatOutBadAdvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatOutBadAdvers.setStatus("mandatory")
_OspfStats_ObjectIdentity = ObjectIdentity
ospfStats = _OspfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22)
)
_OspfGeneralStats_ObjectIdentity = ObjectIdentity
ospfGeneralStats = _OspfGeneralStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1)
)
_OspfCumRxTxStats_ObjectIdentity = ObjectIdentity
ospfCumRxTxStats = _OspfCumRxTxStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 1)
)
_OspfCumRxPkts_Type = Counter32
_OspfCumRxPkts_Object = MibScalar
ospfCumRxPkts = _OspfCumRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 1, 1),
    _OspfCumRxPkts_Type()
)
ospfCumRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumRxPkts.setStatus("mandatory")
_OspfCumTxPkts_Type = Counter32
_OspfCumTxPkts_Object = MibScalar
ospfCumTxPkts = _OspfCumTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 1, 2),
    _OspfCumTxPkts_Type()
)
ospfCumTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumTxPkts.setStatus("mandatory")
_OspfCumRxHello_Type = Counter32
_OspfCumRxHello_Object = MibScalar
ospfCumRxHello = _OspfCumRxHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 1, 3),
    _OspfCumRxHello_Type()
)
ospfCumRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumRxHello.setStatus("mandatory")
_OspfCumTxHello_Type = Counter32
_OspfCumTxHello_Object = MibScalar
ospfCumTxHello = _OspfCumTxHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 1, 4),
    _OspfCumTxHello_Type()
)
ospfCumTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumTxHello.setStatus("mandatory")
_OspfCumRxDatabase_Type = Counter32
_OspfCumRxDatabase_Object = MibScalar
ospfCumRxDatabase = _OspfCumRxDatabase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 1, 5),
    _OspfCumRxDatabase_Type()
)
ospfCumRxDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumRxDatabase.setStatus("mandatory")
_OspfCumTxDatabase_Type = Counter32
_OspfCumTxDatabase_Object = MibScalar
ospfCumTxDatabase = _OspfCumTxDatabase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 1, 6),
    _OspfCumTxDatabase_Type()
)
ospfCumTxDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumTxDatabase.setStatus("mandatory")
_OspfCumRxlsReqs_Type = Counter32
_OspfCumRxlsReqs_Object = MibScalar
ospfCumRxlsReqs = _OspfCumRxlsReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 1, 7),
    _OspfCumRxlsReqs_Type()
)
ospfCumRxlsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumRxlsReqs.setStatus("mandatory")
_OspfCumTxlsReqs_Type = Counter32
_OspfCumTxlsReqs_Object = MibScalar
ospfCumTxlsReqs = _OspfCumTxlsReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 1, 8),
    _OspfCumTxlsReqs_Type()
)
ospfCumTxlsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumTxlsReqs.setStatus("mandatory")
_OspfCumRxlsAcks_Type = Counter32
_OspfCumRxlsAcks_Object = MibScalar
ospfCumRxlsAcks = _OspfCumRxlsAcks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 1, 9),
    _OspfCumRxlsAcks_Type()
)
ospfCumRxlsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumRxlsAcks.setStatus("mandatory")
_OspfCumTxlsAcks_Type = Counter32
_OspfCumTxlsAcks_Object = MibScalar
ospfCumTxlsAcks = _OspfCumTxlsAcks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 1, 10),
    _OspfCumTxlsAcks_Type()
)
ospfCumTxlsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumTxlsAcks.setStatus("mandatory")
_OspfCumRxlsUpdates_Type = Counter32
_OspfCumRxlsUpdates_Object = MibScalar
ospfCumRxlsUpdates = _OspfCumRxlsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 1, 11),
    _OspfCumRxlsUpdates_Type()
)
ospfCumRxlsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumRxlsUpdates.setStatus("mandatory")
_OspfCumTxlsUpdates_Type = Counter32
_OspfCumTxlsUpdates_Object = MibScalar
ospfCumTxlsUpdates = _OspfCumTxlsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 1, 12),
    _OspfCumTxlsUpdates_Type()
)
ospfCumTxlsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumTxlsUpdates.setStatus("mandatory")
_OspfCumNbrChangeStats_ObjectIdentity = ObjectIdentity
ospfCumNbrChangeStats = _OspfCumNbrChangeStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 2)
)
_OspfCumNbrhello_Type = Counter32
_OspfCumNbrhello_Object = MibScalar
ospfCumNbrhello = _OspfCumNbrhello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 2, 1),
    _OspfCumNbrhello_Type()
)
ospfCumNbrhello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrhello.setStatus("mandatory")
_OspfCumNbrStart_Type = Counter32
_OspfCumNbrStart_Object = MibScalar
ospfCumNbrStart = _OspfCumNbrStart_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 2, 2),
    _OspfCumNbrStart_Type()
)
ospfCumNbrStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrStart.setStatus("mandatory")
_OspfCumNbrAdjointOk_Type = Counter32
_OspfCumNbrAdjointOk_Object = MibScalar
ospfCumNbrAdjointOk = _OspfCumNbrAdjointOk_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 2, 3),
    _OspfCumNbrAdjointOk_Type()
)
ospfCumNbrAdjointOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrAdjointOk.setStatus("mandatory")
_OspfCumNbrNegotiationDone_Type = Counter32
_OspfCumNbrNegotiationDone_Object = MibScalar
ospfCumNbrNegotiationDone = _OspfCumNbrNegotiationDone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 2, 4),
    _OspfCumNbrNegotiationDone_Type()
)
ospfCumNbrNegotiationDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrNegotiationDone.setStatus("mandatory")
_OspfCumNbrExchangeDone_Type = Counter32
_OspfCumNbrExchangeDone_Object = MibScalar
ospfCumNbrExchangeDone = _OspfCumNbrExchangeDone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 2, 5),
    _OspfCumNbrExchangeDone_Type()
)
ospfCumNbrExchangeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrExchangeDone.setStatus("mandatory")
_OspfCumNbrBadRequests_Type = Counter32
_OspfCumNbrBadRequests_Object = MibScalar
ospfCumNbrBadRequests = _OspfCumNbrBadRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 2, 6),
    _OspfCumNbrBadRequests_Type()
)
ospfCumNbrBadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrBadRequests.setStatus("mandatory")
_OspfCumNbrBadSequence_Type = Counter32
_OspfCumNbrBadSequence_Object = MibScalar
ospfCumNbrBadSequence = _OspfCumNbrBadSequence_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 2, 7),
    _OspfCumNbrBadSequence_Type()
)
ospfCumNbrBadSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrBadSequence.setStatus("mandatory")
_OspfCumNbrLoadingDone_Type = Counter32
_OspfCumNbrLoadingDone_Object = MibScalar
ospfCumNbrLoadingDone = _OspfCumNbrLoadingDone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 2, 8),
    _OspfCumNbrLoadingDone_Type()
)
ospfCumNbrLoadingDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrLoadingDone.setStatus("mandatory")
_OspfCumNbrN1way_Type = Counter32
_OspfCumNbrN1way_Object = MibScalar
ospfCumNbrN1way = _OspfCumNbrN1way_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 2, 9),
    _OspfCumNbrN1way_Type()
)
ospfCumNbrN1way.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrN1way.setStatus("mandatory")
_OspfCumNbrRstAd_Type = Counter32
_OspfCumNbrRstAd_Object = MibScalar
ospfCumNbrRstAd = _OspfCumNbrRstAd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 2, 10),
    _OspfCumNbrRstAd_Type()
)
ospfCumNbrRstAd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrRstAd.setStatus("mandatory")
_OspfCumNbrDown_Type = Counter32
_OspfCumNbrDown_Object = MibScalar
ospfCumNbrDown = _OspfCumNbrDown_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 2, 11),
    _OspfCumNbrDown_Type()
)
ospfCumNbrDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumNbrDown.setStatus("mandatory")
_OspfCumIntfChangeStats_ObjectIdentity = ObjectIdentity
ospfCumIntfChangeStats = _OspfCumIntfChangeStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 3)
)
_OspfCumIntfHello_Type = Counter32
_OspfCumIntfHello_Object = MibScalar
ospfCumIntfHello = _OspfCumIntfHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 3, 1),
    _OspfCumIntfHello_Type()
)
ospfCumIntfHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfHello.setStatus("mandatory")
_OspfCumIntfDown_Type = Counter32
_OspfCumIntfDown_Object = MibScalar
ospfCumIntfDown = _OspfCumIntfDown_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 3, 2),
    _OspfCumIntfDown_Type()
)
ospfCumIntfDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfDown.setStatus("mandatory")
_OspfCumIntfLoop_Type = Counter32
_OspfCumIntfLoop_Object = MibScalar
ospfCumIntfLoop = _OspfCumIntfLoop_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 3, 3),
    _OspfCumIntfLoop_Type()
)
ospfCumIntfLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfLoop.setStatus("mandatory")
_OspfCumIntfUnloop_Type = Counter32
_OspfCumIntfUnloop_Object = MibScalar
ospfCumIntfUnloop = _OspfCumIntfUnloop_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 3, 4),
    _OspfCumIntfUnloop_Type()
)
ospfCumIntfUnloop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfUnloop.setStatus("mandatory")
_OspfCumIntfWaitTimer_Type = Counter32
_OspfCumIntfWaitTimer_Object = MibScalar
ospfCumIntfWaitTimer = _OspfCumIntfWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 3, 5),
    _OspfCumIntfWaitTimer_Type()
)
ospfCumIntfWaitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfWaitTimer.setStatus("mandatory")
_OspfCumIntfBackup_Type = Counter32
_OspfCumIntfBackup_Object = MibScalar
ospfCumIntfBackup = _OspfCumIntfBackup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 3, 6),
    _OspfCumIntfBackup_Type()
)
ospfCumIntfBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfBackup.setStatus("mandatory")
_OspfCumIntfNbrChange_Type = Counter32
_OspfCumIntfNbrChange_Object = MibScalar
ospfCumIntfNbrChange = _OspfCumIntfNbrChange_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 3, 7),
    _OspfCumIntfNbrChange_Type()
)
ospfCumIntfNbrChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCumIntfNbrChange.setStatus("mandatory")
_OspfTimersKickOffStats_ObjectIdentity = ObjectIdentity
ospfTimersKickOffStats = _OspfTimersKickOffStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 4)
)
_OspfTmrsKckOffHello_Type = Counter32
_OspfTmrsKckOffHello_Object = MibScalar
ospfTmrsKckOffHello = _OspfTmrsKckOffHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 4, 1),
    _OspfTmrsKckOffHello_Type()
)
ospfTmrsKckOffHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffHello.setStatus("mandatory")
_OspfTmrsKckOffRetransmit_Type = Counter32
_OspfTmrsKckOffRetransmit_Object = MibScalar
ospfTmrsKckOffRetransmit = _OspfTmrsKckOffRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 4, 2),
    _OspfTmrsKckOffRetransmit_Type()
)
ospfTmrsKckOffRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffRetransmit.setStatus("mandatory")
_OspfTmrsKckOffLsaLock_Type = Counter32
_OspfTmrsKckOffLsaLock_Object = MibScalar
ospfTmrsKckOffLsaLock = _OspfTmrsKckOffLsaLock_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 4, 3),
    _OspfTmrsKckOffLsaLock_Type()
)
ospfTmrsKckOffLsaLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffLsaLock.setStatus("mandatory")
_OspfTmrsKckOffLsaAck_Type = Counter32
_OspfTmrsKckOffLsaAck_Object = MibScalar
ospfTmrsKckOffLsaAck = _OspfTmrsKckOffLsaAck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 4, 4),
    _OspfTmrsKckOffLsaAck_Type()
)
ospfTmrsKckOffLsaAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffLsaAck.setStatus("mandatory")
_OspfTmrsKckOffDbage_Type = Counter32
_OspfTmrsKckOffDbage_Object = MibScalar
ospfTmrsKckOffDbage = _OspfTmrsKckOffDbage_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 4, 5),
    _OspfTmrsKckOffDbage_Type()
)
ospfTmrsKckOffDbage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffDbage.setStatus("mandatory")
_OspfTmrsKckOffSummary_Type = Counter32
_OspfTmrsKckOffSummary_Object = MibScalar
ospfTmrsKckOffSummary = _OspfTmrsKckOffSummary_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 4, 6),
    _OspfTmrsKckOffSummary_Type()
)
ospfTmrsKckOffSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffSummary.setStatus("mandatory")
_OspfTmrsKckOffAseExport_Type = Counter32
_OspfTmrsKckOffAseExport_Object = MibScalar
ospfTmrsKckOffAseExport = _OspfTmrsKckOffAseExport_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 1, 4, 7),
    _OspfTmrsKckOffAseExport_Type()
)
ospfTmrsKckOffAseExport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTmrsKckOffAseExport.setStatus("mandatory")
_OspfArea_ObjectIdentity = ObjectIdentity
ospfArea = _OspfArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2)
)
_OspfAreaRxTxStats_Object = MibTable
ospfAreaRxTxStats = _OspfAreaRxTxStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 1)
)
if mibBuilder.loadTexts:
    ospfAreaRxTxStats.setStatus("mandatory")
_OspfAreaRxTxStatsEntry_Object = MibTableRow
ospfAreaRxTxStatsEntry = _OspfAreaRxTxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 1, 1)
)
ospfAreaRxTxStatsEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ospfAreaRxTxIndex"),
)
if mibBuilder.loadTexts:
    ospfAreaRxTxStatsEntry.setStatus("mandatory")
_OspfAreaRxTxIndex_Type = Integer32
_OspfAreaRxTxIndex_Object = MibTableColumn
ospfAreaRxTxIndex = _OspfAreaRxTxIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 1, 1, 1),
    _OspfAreaRxTxIndex_Type()
)
ospfAreaRxTxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxTxIndex.setStatus("mandatory")
_OspfAreaRxPkts_Type = Counter32
_OspfAreaRxPkts_Object = MibTableColumn
ospfAreaRxPkts = _OspfAreaRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 1, 1, 2),
    _OspfAreaRxPkts_Type()
)
ospfAreaRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxPkts.setStatus("mandatory")
_OspfAreaTxPkts_Type = Counter32
_OspfAreaTxPkts_Object = MibTableColumn
ospfAreaTxPkts = _OspfAreaTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 1, 1, 3),
    _OspfAreaTxPkts_Type()
)
ospfAreaTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTxPkts.setStatus("mandatory")
_OspfAreaRxHello_Type = Counter32
_OspfAreaRxHello_Object = MibTableColumn
ospfAreaRxHello = _OspfAreaRxHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 1, 1, 4),
    _OspfAreaRxHello_Type()
)
ospfAreaRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxHello.setStatus("mandatory")
_OspfAreaTxHello_Type = Counter32
_OspfAreaTxHello_Object = MibTableColumn
ospfAreaTxHello = _OspfAreaTxHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 1, 1, 5),
    _OspfAreaTxHello_Type()
)
ospfAreaTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTxHello.setStatus("mandatory")
_OspfAreaRxDatabase_Type = Counter32
_OspfAreaRxDatabase_Object = MibTableColumn
ospfAreaRxDatabase = _OspfAreaRxDatabase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 1, 1, 6),
    _OspfAreaRxDatabase_Type()
)
ospfAreaRxDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxDatabase.setStatus("mandatory")
_OspfAreaTxDatabase_Type = Counter32
_OspfAreaTxDatabase_Object = MibTableColumn
ospfAreaTxDatabase = _OspfAreaTxDatabase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 1, 1, 7),
    _OspfAreaTxDatabase_Type()
)
ospfAreaTxDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTxDatabase.setStatus("mandatory")
_OspfAreaRxlsReqs_Type = Counter32
_OspfAreaRxlsReqs_Object = MibTableColumn
ospfAreaRxlsReqs = _OspfAreaRxlsReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 1, 1, 8),
    _OspfAreaRxlsReqs_Type()
)
ospfAreaRxlsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxlsReqs.setStatus("mandatory")
_OspfAreaTxlsReqs_Type = Counter32
_OspfAreaTxlsReqs_Object = MibTableColumn
ospfAreaTxlsReqs = _OspfAreaTxlsReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 1, 1, 9),
    _OspfAreaTxlsReqs_Type()
)
ospfAreaTxlsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTxlsReqs.setStatus("mandatory")
_OspfAreaRxlsAcks_Type = Counter32
_OspfAreaRxlsAcks_Object = MibTableColumn
ospfAreaRxlsAcks = _OspfAreaRxlsAcks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 1, 1, 10),
    _OspfAreaRxlsAcks_Type()
)
ospfAreaRxlsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxlsAcks.setStatus("mandatory")
_OspfAreaTxlsAcks_Type = Counter32
_OspfAreaTxlsAcks_Object = MibTableColumn
ospfAreaTxlsAcks = _OspfAreaTxlsAcks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 1, 1, 11),
    _OspfAreaTxlsAcks_Type()
)
ospfAreaTxlsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTxlsAcks.setStatus("mandatory")
_OspfAreaRxlsUpdates_Type = Counter32
_OspfAreaRxlsUpdates_Object = MibTableColumn
ospfAreaRxlsUpdates = _OspfAreaRxlsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 1, 1, 12),
    _OspfAreaRxlsUpdates_Type()
)
ospfAreaRxlsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRxlsUpdates.setStatus("mandatory")
_OspfAreaTxlsUpdates_Type = Counter32
_OspfAreaTxlsUpdates_Object = MibTableColumn
ospfAreaTxlsUpdates = _OspfAreaTxlsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 1, 1, 13),
    _OspfAreaTxlsUpdates_Type()
)
ospfAreaTxlsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaTxlsUpdates.setStatus("mandatory")
_OspfAreaNbrChangeStats_Object = MibTable
ospfAreaNbrChangeStats = _OspfAreaNbrChangeStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 2)
)
if mibBuilder.loadTexts:
    ospfAreaNbrChangeStats.setStatus("mandatory")
_OspfAreaNbrChangeStatsEntry_Object = MibTableRow
ospfAreaNbrChangeStatsEntry = _OspfAreaNbrChangeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 2, 1)
)
ospfAreaNbrChangeStatsEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ospfAreaNbrIndex"),
)
if mibBuilder.loadTexts:
    ospfAreaNbrChangeStatsEntry.setStatus("mandatory")
_OspfAreaNbrIndex_Type = Integer32
_OspfAreaNbrIndex_Object = MibTableColumn
ospfAreaNbrIndex = _OspfAreaNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 2, 1, 1),
    _OspfAreaNbrIndex_Type()
)
ospfAreaNbrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrIndex.setStatus("mandatory")
_OspfAreaNbrhello_Type = Counter32
_OspfAreaNbrhello_Object = MibTableColumn
ospfAreaNbrhello = _OspfAreaNbrhello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 2, 1, 2),
    _OspfAreaNbrhello_Type()
)
ospfAreaNbrhello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrhello.setStatus("mandatory")
_OspfAreaNbrStart_Type = Counter32
_OspfAreaNbrStart_Object = MibTableColumn
ospfAreaNbrStart = _OspfAreaNbrStart_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 2, 1, 3),
    _OspfAreaNbrStart_Type()
)
ospfAreaNbrStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrStart.setStatus("mandatory")
_OspfAreaNbrAdjointOk_Type = Counter32
_OspfAreaNbrAdjointOk_Object = MibTableColumn
ospfAreaNbrAdjointOk = _OspfAreaNbrAdjointOk_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 2, 1, 4),
    _OspfAreaNbrAdjointOk_Type()
)
ospfAreaNbrAdjointOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrAdjointOk.setStatus("mandatory")
_OspfAreaNbrNegotiationDone_Type = Counter32
_OspfAreaNbrNegotiationDone_Object = MibTableColumn
ospfAreaNbrNegotiationDone = _OspfAreaNbrNegotiationDone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 2, 1, 5),
    _OspfAreaNbrNegotiationDone_Type()
)
ospfAreaNbrNegotiationDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrNegotiationDone.setStatus("mandatory")
_OspfAreaNbrExchangeDone_Type = Counter32
_OspfAreaNbrExchangeDone_Object = MibTableColumn
ospfAreaNbrExchangeDone = _OspfAreaNbrExchangeDone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 2, 1, 6),
    _OspfAreaNbrExchangeDone_Type()
)
ospfAreaNbrExchangeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrExchangeDone.setStatus("mandatory")
_OspfAreaNbrBadRequests_Type = Counter32
_OspfAreaNbrBadRequests_Object = MibTableColumn
ospfAreaNbrBadRequests = _OspfAreaNbrBadRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 2, 1, 7),
    _OspfAreaNbrBadRequests_Type()
)
ospfAreaNbrBadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrBadRequests.setStatus("mandatory")
_OspfAreaNbrBadSequence_Type = Counter32
_OspfAreaNbrBadSequence_Object = MibTableColumn
ospfAreaNbrBadSequence = _OspfAreaNbrBadSequence_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 2, 1, 8),
    _OspfAreaNbrBadSequence_Type()
)
ospfAreaNbrBadSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrBadSequence.setStatus("mandatory")
_OspfAreaNbrLoadingDone_Type = Counter32
_OspfAreaNbrLoadingDone_Object = MibTableColumn
ospfAreaNbrLoadingDone = _OspfAreaNbrLoadingDone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 2, 1, 9),
    _OspfAreaNbrLoadingDone_Type()
)
ospfAreaNbrLoadingDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrLoadingDone.setStatus("mandatory")
_OspfAreaNbrN1way_Type = Counter32
_OspfAreaNbrN1way_Object = MibTableColumn
ospfAreaNbrN1way = _OspfAreaNbrN1way_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 2, 1, 10),
    _OspfAreaNbrN1way_Type()
)
ospfAreaNbrN1way.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrN1way.setStatus("mandatory")
_OspfAreaNbrRstAd_Type = Counter32
_OspfAreaNbrRstAd_Object = MibTableColumn
ospfAreaNbrRstAd = _OspfAreaNbrRstAd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 2, 1, 11),
    _OspfAreaNbrRstAd_Type()
)
ospfAreaNbrRstAd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrRstAd.setStatus("mandatory")
_OspfAreaNbrDown_Type = Counter32
_OspfAreaNbrDown_Object = MibTableColumn
ospfAreaNbrDown = _OspfAreaNbrDown_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 2, 1, 12),
    _OspfAreaNbrDown_Type()
)
ospfAreaNbrDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNbrDown.setStatus("mandatory")
_OspfAreaChangeStats_Object = MibTable
ospfAreaChangeStats = _OspfAreaChangeStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 3)
)
if mibBuilder.loadTexts:
    ospfAreaChangeStats.setStatus("mandatory")
_OspfAreaChangeStatsEntry_Object = MibTableRow
ospfAreaChangeStatsEntry = _OspfAreaChangeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 3, 1)
)
ospfAreaChangeStatsEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ospfAreaIntfIndex"),
)
if mibBuilder.loadTexts:
    ospfAreaChangeStatsEntry.setStatus("mandatory")
_OspfAreaIntfIndex_Type = Integer32
_OspfAreaIntfIndex_Object = MibTableColumn
ospfAreaIntfIndex = _OspfAreaIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 3, 1, 1),
    _OspfAreaIntfIndex_Type()
)
ospfAreaIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfIndex.setStatus("mandatory")
_OspfAreaIntfHello_Type = Counter32
_OspfAreaIntfHello_Object = MibTableColumn
ospfAreaIntfHello = _OspfAreaIntfHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 3, 1, 2),
    _OspfAreaIntfHello_Type()
)
ospfAreaIntfHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfHello.setStatus("mandatory")
_OspfAreaIntfDown_Type = Counter32
_OspfAreaIntfDown_Object = MibTableColumn
ospfAreaIntfDown = _OspfAreaIntfDown_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 3, 1, 3),
    _OspfAreaIntfDown_Type()
)
ospfAreaIntfDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfDown.setStatus("mandatory")
_OspfAreaIntfLoop_Type = Counter32
_OspfAreaIntfLoop_Object = MibTableColumn
ospfAreaIntfLoop = _OspfAreaIntfLoop_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 3, 1, 4),
    _OspfAreaIntfLoop_Type()
)
ospfAreaIntfLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfLoop.setStatus("mandatory")
_OspfAreaIntfUnloop_Type = Counter32
_OspfAreaIntfUnloop_Object = MibTableColumn
ospfAreaIntfUnloop = _OspfAreaIntfUnloop_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 3, 1, 5),
    _OspfAreaIntfUnloop_Type()
)
ospfAreaIntfUnloop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfUnloop.setStatus("mandatory")
_OspfAreaIntfWaitTimer_Type = Counter32
_OspfAreaIntfWaitTimer_Object = MibTableColumn
ospfAreaIntfWaitTimer = _OspfAreaIntfWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 3, 1, 6),
    _OspfAreaIntfWaitTimer_Type()
)
ospfAreaIntfWaitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfWaitTimer.setStatus("mandatory")
_OspfAreaIntfBackup_Type = Counter32
_OspfAreaIntfBackup_Object = MibTableColumn
ospfAreaIntfBackup = _OspfAreaIntfBackup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 3, 1, 7),
    _OspfAreaIntfBackup_Type()
)
ospfAreaIntfBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfBackup.setStatus("mandatory")
_OspfAreaIntfNbrChange_Type = Counter32
_OspfAreaIntfNbrChange_Object = MibTableColumn
ospfAreaIntfNbrChange = _OspfAreaIntfNbrChange_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 2, 3, 1, 8),
    _OspfAreaIntfNbrChange_Type()
)
ospfAreaIntfNbrChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIntfNbrChange.setStatus("mandatory")
_OspfInterface_ObjectIdentity = ObjectIdentity
ospfInterface = _OspfInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3)
)
_OspfIntfRxTxStats_Object = MibTable
ospfIntfRxTxStats = _OspfIntfRxTxStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 1)
)
if mibBuilder.loadTexts:
    ospfIntfRxTxStats.setStatus("mandatory")
_OspfIntfRxTxStatsEntry_Object = MibTableRow
ospfIntfRxTxStatsEntry = _OspfIntfRxTxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 1, 1)
)
ospfIntfRxTxStatsEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ospfIntfRxTxIndex"),
)
if mibBuilder.loadTexts:
    ospfIntfRxTxStatsEntry.setStatus("mandatory")
_OspfIntfRxTxIndex_Type = Integer32
_OspfIntfRxTxIndex_Object = MibTableColumn
ospfIntfRxTxIndex = _OspfIntfRxTxIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 1, 1, 1),
    _OspfIntfRxTxIndex_Type()
)
ospfIntfRxTxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxTxIndex.setStatus("mandatory")
_OspfIntfRxPkts_Type = Counter32
_OspfIntfRxPkts_Object = MibTableColumn
ospfIntfRxPkts = _OspfIntfRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 1, 1, 2),
    _OspfIntfRxPkts_Type()
)
ospfIntfRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxPkts.setStatus("mandatory")
_OspfIntfTxPkts_Type = Counter32
_OspfIntfTxPkts_Object = MibTableColumn
ospfIntfTxPkts = _OspfIntfTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 1, 1, 3),
    _OspfIntfTxPkts_Type()
)
ospfIntfTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTxPkts.setStatus("mandatory")
_OspfIntfRxHello_Type = Counter32
_OspfIntfRxHello_Object = MibTableColumn
ospfIntfRxHello = _OspfIntfRxHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 1, 1, 4),
    _OspfIntfRxHello_Type()
)
ospfIntfRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxHello.setStatus("mandatory")
_OspfIntfTxHello_Type = Counter32
_OspfIntfTxHello_Object = MibTableColumn
ospfIntfTxHello = _OspfIntfTxHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 1, 1, 5),
    _OspfIntfTxHello_Type()
)
ospfIntfTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTxHello.setStatus("mandatory")
_OspfIntfRxDatabase_Type = Counter32
_OspfIntfRxDatabase_Object = MibTableColumn
ospfIntfRxDatabase = _OspfIntfRxDatabase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 1, 1, 6),
    _OspfIntfRxDatabase_Type()
)
ospfIntfRxDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxDatabase.setStatus("mandatory")
_OspfIntfTxDatabase_Type = Counter32
_OspfIntfTxDatabase_Object = MibTableColumn
ospfIntfTxDatabase = _OspfIntfTxDatabase_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 1, 1, 7),
    _OspfIntfTxDatabase_Type()
)
ospfIntfTxDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTxDatabase.setStatus("mandatory")
_OspfIntfRxlsReqs_Type = Counter32
_OspfIntfRxlsReqs_Object = MibTableColumn
ospfIntfRxlsReqs = _OspfIntfRxlsReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 1, 1, 8),
    _OspfIntfRxlsReqs_Type()
)
ospfIntfRxlsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxlsReqs.setStatus("mandatory")
_OspfIntfTxlsReqs_Type = Counter32
_OspfIntfTxlsReqs_Object = MibTableColumn
ospfIntfTxlsReqs = _OspfIntfTxlsReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 1, 1, 9),
    _OspfIntfTxlsReqs_Type()
)
ospfIntfTxlsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTxlsReqs.setStatus("mandatory")
_OspfIntfRxlsAcks_Type = Counter32
_OspfIntfRxlsAcks_Object = MibTableColumn
ospfIntfRxlsAcks = _OspfIntfRxlsAcks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 1, 1, 10),
    _OspfIntfRxlsAcks_Type()
)
ospfIntfRxlsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxlsAcks.setStatus("mandatory")
_OspfIntfTxlsAcks_Type = Counter32
_OspfIntfTxlsAcks_Object = MibTableColumn
ospfIntfTxlsAcks = _OspfIntfTxlsAcks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 1, 1, 11),
    _OspfIntfTxlsAcks_Type()
)
ospfIntfTxlsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTxlsAcks.setStatus("mandatory")
_OspfIntfRxlsUpdates_Type = Counter32
_OspfIntfRxlsUpdates_Object = MibTableColumn
ospfIntfRxlsUpdates = _OspfIntfRxlsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 1, 1, 12),
    _OspfIntfRxlsUpdates_Type()
)
ospfIntfRxlsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfRxlsUpdates.setStatus("mandatory")
_OspfIntfTxlsUpdates_Type = Counter32
_OspfIntfTxlsUpdates_Object = MibTableColumn
ospfIntfTxlsUpdates = _OspfIntfTxlsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 1, 1, 13),
    _OspfIntfTxlsUpdates_Type()
)
ospfIntfTxlsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfTxlsUpdates.setStatus("mandatory")
_OspfIntfNbrChangeStats_Object = MibTable
ospfIntfNbrChangeStats = _OspfIntfNbrChangeStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 2)
)
if mibBuilder.loadTexts:
    ospfIntfNbrChangeStats.setStatus("mandatory")
_OspfIntfNbrChangeStatsEntry_Object = MibTableRow
ospfIntfNbrChangeStatsEntry = _OspfIntfNbrChangeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 2, 1)
)
ospfIntfNbrChangeStatsEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ospfIntfNbrIndex"),
)
if mibBuilder.loadTexts:
    ospfIntfNbrChangeStatsEntry.setStatus("mandatory")
_OspfIntfNbrIndex_Type = Integer32
_OspfIntfNbrIndex_Object = MibTableColumn
ospfIntfNbrIndex = _OspfIntfNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 2, 1, 1),
    _OspfIntfNbrIndex_Type()
)
ospfIntfNbrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrIndex.setStatus("mandatory")
_OspfIntfNbrhello_Type = Counter32
_OspfIntfNbrhello_Object = MibTableColumn
ospfIntfNbrhello = _OspfIntfNbrhello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 2, 1, 2),
    _OspfIntfNbrhello_Type()
)
ospfIntfNbrhello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrhello.setStatus("mandatory")
_OspfIntfNbrStart_Type = Counter32
_OspfIntfNbrStart_Object = MibTableColumn
ospfIntfNbrStart = _OspfIntfNbrStart_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 2, 1, 3),
    _OspfIntfNbrStart_Type()
)
ospfIntfNbrStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrStart.setStatus("mandatory")
_OspfIntfNbrAdjointOk_Type = Counter32
_OspfIntfNbrAdjointOk_Object = MibTableColumn
ospfIntfNbrAdjointOk = _OspfIntfNbrAdjointOk_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 2, 1, 4),
    _OspfIntfNbrAdjointOk_Type()
)
ospfIntfNbrAdjointOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrAdjointOk.setStatus("mandatory")
_OspfIntfNbrNegotiationDone_Type = Counter32
_OspfIntfNbrNegotiationDone_Object = MibTableColumn
ospfIntfNbrNegotiationDone = _OspfIntfNbrNegotiationDone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 2, 1, 5),
    _OspfIntfNbrNegotiationDone_Type()
)
ospfIntfNbrNegotiationDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrNegotiationDone.setStatus("mandatory")
_OspfIntfNbrExchangeDone_Type = Counter32
_OspfIntfNbrExchangeDone_Object = MibTableColumn
ospfIntfNbrExchangeDone = _OspfIntfNbrExchangeDone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 2, 1, 6),
    _OspfIntfNbrExchangeDone_Type()
)
ospfIntfNbrExchangeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrExchangeDone.setStatus("mandatory")
_OspfIntfNbrBadRequests_Type = Counter32
_OspfIntfNbrBadRequests_Object = MibTableColumn
ospfIntfNbrBadRequests = _OspfIntfNbrBadRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 2, 1, 7),
    _OspfIntfNbrBadRequests_Type()
)
ospfIntfNbrBadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrBadRequests.setStatus("mandatory")
_OspfIntfNbrBadSequence_Type = Counter32
_OspfIntfNbrBadSequence_Object = MibTableColumn
ospfIntfNbrBadSequence = _OspfIntfNbrBadSequence_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 2, 1, 8),
    _OspfIntfNbrBadSequence_Type()
)
ospfIntfNbrBadSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrBadSequence.setStatus("mandatory")
_OspfIntfNbrLoadingDone_Type = Counter32
_OspfIntfNbrLoadingDone_Object = MibTableColumn
ospfIntfNbrLoadingDone = _OspfIntfNbrLoadingDone_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 2, 1, 9),
    _OspfIntfNbrLoadingDone_Type()
)
ospfIntfNbrLoadingDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrLoadingDone.setStatus("mandatory")
_OspfIntfNbrN1way_Type = Counter32
_OspfIntfNbrN1way_Object = MibTableColumn
ospfIntfNbrN1way = _OspfIntfNbrN1way_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 2, 1, 10),
    _OspfIntfNbrN1way_Type()
)
ospfIntfNbrN1way.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrN1way.setStatus("mandatory")
_OspfIntfNbrRstAd_Type = Counter32
_OspfIntfNbrRstAd_Object = MibTableColumn
ospfIntfNbrRstAd = _OspfIntfNbrRstAd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 2, 1, 11),
    _OspfIntfNbrRstAd_Type()
)
ospfIntfNbrRstAd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrRstAd.setStatus("mandatory")
_OspfIntfNbrDown_Type = Counter32
_OspfIntfNbrDown_Object = MibTableColumn
ospfIntfNbrDown = _OspfIntfNbrDown_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 2, 1, 12),
    _OspfIntfNbrDown_Type()
)
ospfIntfNbrDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrDown.setStatus("mandatory")
_OspfIntfChangeStats_Object = MibTable
ospfIntfChangeStats = _OspfIntfChangeStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 3)
)
if mibBuilder.loadTexts:
    ospfIntfChangeStats.setStatus("mandatory")
_OspfIntfChangeStatsEntry_Object = MibTableRow
ospfIntfChangeStatsEntry = _OspfIntfChangeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 3, 1)
)
ospfIntfChangeStatsEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ospfIntfIndex"),
)
if mibBuilder.loadTexts:
    ospfIntfChangeStatsEntry.setStatus("mandatory")
_OspfIntfIndex_Type = Integer32
_OspfIntfIndex_Object = MibTableColumn
ospfIntfIndex = _OspfIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 3, 1, 1),
    _OspfIntfIndex_Type()
)
ospfIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfIndex.setStatus("mandatory")
_OspfIntfHello_Type = Counter32
_OspfIntfHello_Object = MibTableColumn
ospfIntfHello = _OspfIntfHello_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 3, 1, 2),
    _OspfIntfHello_Type()
)
ospfIntfHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfHello.setStatus("mandatory")
_OspfIntfDown_Type = Counter32
_OspfIntfDown_Object = MibTableColumn
ospfIntfDown = _OspfIntfDown_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 3, 1, 3),
    _OspfIntfDown_Type()
)
ospfIntfDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfDown.setStatus("mandatory")
_OspfIntfLoop_Type = Counter32
_OspfIntfLoop_Object = MibTableColumn
ospfIntfLoop = _OspfIntfLoop_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 3, 1, 4),
    _OspfIntfLoop_Type()
)
ospfIntfLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfLoop.setStatus("mandatory")
_OspfIntfUnloop_Type = Counter32
_OspfIntfUnloop_Object = MibTableColumn
ospfIntfUnloop = _OspfIntfUnloop_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 3, 1, 5),
    _OspfIntfUnloop_Type()
)
ospfIntfUnloop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfUnloop.setStatus("mandatory")
_OspfIntfWaitTimer_Type = Counter32
_OspfIntfWaitTimer_Object = MibTableColumn
ospfIntfWaitTimer = _OspfIntfWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 3, 1, 6),
    _OspfIntfWaitTimer_Type()
)
ospfIntfWaitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfWaitTimer.setStatus("mandatory")
_OspfIntfBackup_Type = Counter32
_OspfIntfBackup_Object = MibTableColumn
ospfIntfBackup = _OspfIntfBackup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 3, 1, 7),
    _OspfIntfBackup_Type()
)
ospfIntfBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfBackup.setStatus("mandatory")
_OspfIntfNbrChange_Type = Counter32
_OspfIntfNbrChange_Object = MibTableColumn
ospfIntfNbrChange = _OspfIntfNbrChange_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 22, 3, 3, 1, 8),
    _OspfIntfNbrChange_Type()
)
ospfIntfNbrChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfNbrChange.setStatus("mandatory")
_Ip_info_ObjectIdentity = ObjectIdentity
ip_info = _Ip_info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3)
)
_IpRouteInfoTable_Object = MibTable
ipRouteInfoTable = _IpRouteInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 1)
)
if mibBuilder.loadTexts:
    ipRouteInfoTable.setStatus("mandatory")
_IpRouteInfoEntry_Object = MibTableRow
ipRouteInfoEntry = _IpRouteInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 1, 1)
)
ipRouteInfoEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ipRouteInfoIndx"),
)
if mibBuilder.loadTexts:
    ipRouteInfoEntry.setStatus("mandatory")
_IpRouteInfoIndx_Type = Integer32
_IpRouteInfoIndx_Object = MibTableColumn
ipRouteInfoIndx = _IpRouteInfoIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 1, 1, 1),
    _IpRouteInfoIndx_Type()
)
ipRouteInfoIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoIndx.setStatus("mandatory")
_IpRouteInfoDestIp_Type = IpAddress
_IpRouteInfoDestIp_Object = MibTableColumn
ipRouteInfoDestIp = _IpRouteInfoDestIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 1, 1, 2),
    _IpRouteInfoDestIp_Type()
)
ipRouteInfoDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoDestIp.setStatus("mandatory")
_IpRouteInfoMask_Type = IpAddress
_IpRouteInfoMask_Object = MibTableColumn
ipRouteInfoMask = _IpRouteInfoMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 1, 1, 3),
    _IpRouteInfoMask_Type()
)
ipRouteInfoMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoMask.setStatus("mandatory")
_IpRouteInfoGateway_Type = IpAddress
_IpRouteInfoGateway_Object = MibTableColumn
ipRouteInfoGateway = _IpRouteInfoGateway_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 1, 1, 4),
    _IpRouteInfoGateway_Type()
)
ipRouteInfoGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoGateway.setStatus("mandatory")


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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("addr", 5),
          ("bgp", 11),
          ("broadcast", 7),
          ("fixed", 1),
          ("icmp", 2),
          ("martian", 8),
          ("multicast", 9),
          ("none", 12),
          ("ospf", 13),
          ("rip", 6),
          ("snmp", 4),
          ("static", 3),
          ("vip", 10))
    )


_IpRouteInfoTag_Type.__name__ = "Integer32"
_IpRouteInfoTag_Object = MibTableColumn
ipRouteInfoTag = _IpRouteInfoTag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 1, 1, 5),
    _IpRouteInfoTag_Type()
)
ipRouteInfoTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoTag.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 1, 1, 6),
    _IpRouteInfoType_Type()
)
ipRouteInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoType.setStatus("mandatory")
_IpRouteInfoInterface_Type = Integer32
_IpRouteInfoInterface_Object = MibTableColumn
ipRouteInfoInterface = _IpRouteInfoInterface_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 1, 1, 7),
    _IpRouteInfoInterface_Type()
)
ipRouteInfoInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoInterface.setStatus("mandatory")
_ArpInfoTable_Object = MibTable
arpInfoTable = _ArpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 2)
)
if mibBuilder.loadTexts:
    arpInfoTable.setStatus("mandatory")
_ArpInfoEntry_Object = MibTableRow
arpInfoEntry = _ArpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 2, 1)
)
arpInfoEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "arpInfoDestIp"),
)
if mibBuilder.loadTexts:
    arpInfoEntry.setStatus("mandatory")
_ArpInfoDestIp_Type = IpAddress
_ArpInfoDestIp_Object = MibTableColumn
arpInfoDestIp = _ArpInfoDestIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 2, 1, 1),
    _ArpInfoDestIp_Type()
)
arpInfoDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoDestIp.setStatus("mandatory")
_ArpInfoMacAddr_Type = PhysAddress
_ArpInfoMacAddr_Object = MibTableColumn
arpInfoMacAddr = _ArpInfoMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 2, 1, 2),
    _ArpInfoMacAddr_Type()
)
arpInfoMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoMacAddr.setStatus("mandatory")
_ArpInfoVLAN_Type = Integer32
_ArpInfoVLAN_Object = MibTableColumn
arpInfoVLAN = _ArpInfoVLAN_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 2, 1, 3),
    _ArpInfoVLAN_Type()
)
arpInfoVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoVLAN.setStatus("mandatory")
_ArpInfoSrcPort_Type = Integer32
_ArpInfoSrcPort_Object = MibTableColumn
arpInfoSrcPort = _ArpInfoSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 2, 1, 4),
    _ArpInfoSrcPort_Type()
)
arpInfoSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoSrcPort.setStatus("mandatory")
_ArpInfoRefPorts_Type = Integer32
_ArpInfoRefPorts_Object = MibTableColumn
arpInfoRefPorts = _ArpInfoRefPorts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 2, 1, 5),
    _ArpInfoRefPorts_Type()
)
arpInfoRefPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoRefPorts.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 3, 2, 1, 6),
    _ArpInfoFlag_Type()
)
arpInfoFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInfoFlag.setStatus("mandatory")
_Vrrp_info_ObjectIdentity = ObjectIdentity
vrrp_info = _Vrrp_info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 4)
)
_VrrpInfoVirtRtrTable_Object = MibTable
vrrpInfoVirtRtrTable = _VrrpInfoVirtRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 4, 1)
)
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrTable.setStatus("mandatory")
_VrrpInfoVirtRtrTableEntry_Object = MibTableRow
vrrpInfoVirtRtrTableEntry = _VrrpInfoVirtRtrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 4, 1, 1)
)
vrrpInfoVirtRtrTableEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "vrrpInfoVirtRtrIndex"),
)
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrTableEntry.setStatus("mandatory")
_VrrpInfoVirtRtrIndex_Type = Integer32
_VrrpInfoVirtRtrIndex_Object = MibTableColumn
vrrpInfoVirtRtrIndex = _VrrpInfoVirtRtrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 4, 1, 1, 1),
    _VrrpInfoVirtRtrIndex_Type()
)
vrrpInfoVirtRtrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrIndex.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 4, 1, 1, 2),
    _VrrpInfoVirtRtrState_Type()
)
vrrpInfoVirtRtrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 4, 1, 1, 3),
    _VrrpInfoVirtRtrOwnership_Type()
)
vrrpInfoVirtRtrOwnership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrOwnership.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 4, 1, 1, 4),
    _VrrpInfoVirtRtrServer_Type()
)
vrrpInfoVirtRtrServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrServer.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 4, 1, 1, 5),
    _VrrpInfoVirtRtrProxy_Type()
)
vrrpInfoVirtRtrProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInfoVirtRtrProxy.setStatus("mandatory")
_Ospfinfo_ObjectIdentity = ObjectIdentity
ospfinfo = _Ospfinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5)
)
_OspfGeneralInfo_ObjectIdentity = ObjectIdentity
ospfGeneralInfo = _OspfGeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 1)
)
_OspfStartTime_Type = Integer32
_OspfStartTime_Object = MibScalar
ospfStartTime = _OspfStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 1, 1),
    _OspfStartTime_Type()
)
ospfStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStartTime.setStatus("mandatory")
_OspfProcessUptime_Type = Counter32
_OspfProcessUptime_Object = MibScalar
ospfProcessUptime = _OspfProcessUptime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 1, 2),
    _OspfProcessUptime_Type()
)
ospfProcessUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessUptime.setStatus("mandatory")
_OspfLsTypesSupported_Type = Integer32
_OspfLsTypesSupported_Object = MibScalar
ospfLsTypesSupported = _OspfLsTypesSupported_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 1, 3),
    _OspfLsTypesSupported_Type()
)
ospfLsTypesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsTypesSupported.setStatus("mandatory")
_OspfIntfCountForRouter_Type = Integer32
_OspfIntfCountForRouter_Object = MibScalar
ospfIntfCountForRouter = _OspfIntfCountForRouter_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 1, 4),
    _OspfIntfCountForRouter_Type()
)
ospfIntfCountForRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIntfCountForRouter.setStatus("mandatory")
_OspfVlinkCountForRouter_Type = Integer32
_OspfVlinkCountForRouter_Object = MibScalar
ospfVlinkCountForRouter = _OspfVlinkCountForRouter_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 1, 5),
    _OspfVlinkCountForRouter_Type()
)
ospfVlinkCountForRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVlinkCountForRouter.setStatus("mandatory")
_OspfTotalNeighbours_Type = Integer32
_OspfTotalNeighbours_Object = MibScalar
ospfTotalNeighbours = _OspfTotalNeighbours_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 1, 6),
    _OspfTotalNeighbours_Type()
)
ospfTotalNeighbours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTotalNeighbours.setStatus("mandatory")
_OspfNbrInInitState_Type = Integer32
_OspfNbrInInitState_Object = MibScalar
ospfNbrInInitState = _OspfNbrInInitState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 1, 7),
    _OspfNbrInInitState_Type()
)
ospfNbrInInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrInInitState.setStatus("mandatory")
_OspfNbrInExchState_Type = Integer32
_OspfNbrInExchState_Object = MibScalar
ospfNbrInExchState = _OspfNbrInExchState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 1, 8),
    _OspfNbrInExchState_Type()
)
ospfNbrInExchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrInExchState.setStatus("mandatory")
_OspfNbrInFullState_Type = Integer32
_OspfNbrInFullState_Object = MibScalar
ospfNbrInFullState = _OspfNbrInFullState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 1, 9),
    _OspfNbrInFullState_Type()
)
ospfNbrInFullState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrInFullState.setStatus("mandatory")
_OspfTotalAreas_Type = Integer32
_OspfTotalAreas_Object = MibScalar
ospfTotalAreas = _OspfTotalAreas_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 1, 10),
    _OspfTotalAreas_Type()
)
ospfTotalAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTotalAreas.setStatus("mandatory")
_OspfTotalTransitAreas_Type = Integer32
_OspfTotalTransitAreas_Object = MibScalar
ospfTotalTransitAreas = _OspfTotalTransitAreas_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 1, 11),
    _OspfTotalTransitAreas_Type()
)
ospfTotalTransitAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTotalTransitAreas.setStatus("mandatory")
_OspfTotalNssaAreas_Type = Integer32
_OspfTotalNssaAreas_Object = MibScalar
ospfTotalNssaAreas = _OspfTotalNssaAreas_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 1, 12),
    _OspfTotalNssaAreas_Type()
)
ospfTotalNssaAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTotalNssaAreas.setStatus("mandatory")
_OspfAreaInfoTable_Object = MibTable
ospfAreaInfoTable = _OspfAreaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 2)
)
if mibBuilder.loadTexts:
    ospfAreaInfoTable.setStatus("mandatory")
_OspfAreaInfoEntry_Object = MibTableRow
ospfAreaInfoEntry = _OspfAreaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 2, 1)
)
ospfAreaInfoEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ospfAreaInfoIndex"),
)
if mibBuilder.loadTexts:
    ospfAreaInfoEntry.setStatus("mandatory")
_OspfAreaInfoIndex_Type = Integer32
_OspfAreaInfoIndex_Object = MibTableColumn
ospfAreaInfoIndex = _OspfAreaInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 2, 1, 1),
    _OspfAreaInfoIndex_Type()
)
ospfAreaInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaInfoIndex.setStatus("mandatory")
_OspfTotalNumberOfInterfaces_Type = Integer32
_OspfTotalNumberOfInterfaces_Object = MibTableColumn
ospfTotalNumberOfInterfaces = _OspfTotalNumberOfInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 2, 1, 2),
    _OspfTotalNumberOfInterfaces_Type()
)
ospfTotalNumberOfInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfTotalNumberOfInterfaces.setStatus("mandatory")
_OspfNumberOfInterfacesUp_Type = Integer32
_OspfNumberOfInterfacesUp_Object = MibTableColumn
ospfNumberOfInterfacesUp = _OspfNumberOfInterfacesUp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 2, 1, 3),
    _OspfNumberOfInterfacesUp_Type()
)
ospfNumberOfInterfacesUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNumberOfInterfacesUp.setStatus("mandatory")
_OspfNumberOfLsdbEntries_Type = Integer32
_OspfNumberOfLsdbEntries_Object = MibTableColumn
ospfNumberOfLsdbEntries = _OspfNumberOfLsdbEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 2, 1, 4),
    _OspfNumberOfLsdbEntries_Type()
)
ospfNumberOfLsdbEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNumberOfLsdbEntries.setStatus("mandatory")
_OspfAreaInfoId_Type = IpAddress
_OspfAreaInfoId_Object = MibTableColumn
ospfAreaInfoId = _OspfAreaInfoId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 2, 1, 5),
    _OspfAreaInfoId_Type()
)
ospfAreaInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaInfoId.setStatus("mandatory")
_OspfIntfInfoTable_Object = MibTable
ospfIntfInfoTable = _OspfIntfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 3)
)
if mibBuilder.loadTexts:
    ospfIntfInfoTable.setStatus("mandatory")
_OspfIntfInfoEntry_Object = MibTableRow
ospfIntfInfoEntry = _OspfIntfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 3, 1)
)
ospfIntfInfoEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "ospfIfInfoIndex"),
)
if mibBuilder.loadTexts:
    ospfIntfInfoEntry.setStatus("mandatory")
_OspfIfInfoIndex_Type = Integer32
_OspfIfInfoIndex_Object = MibTableColumn
ospfIfInfoIndex = _OspfIfInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 3, 1, 1),
    _OspfIfInfoIndex_Type()
)
ospfIfInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoIndex.setStatus("mandatory")
_OspfIfDesignatedRouterIP_Type = IpAddress
_OspfIfDesignatedRouterIP_Object = MibTableColumn
ospfIfDesignatedRouterIP = _OspfIfDesignatedRouterIP_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 3, 1, 2),
    _OspfIfDesignatedRouterIP_Type()
)
ospfIfDesignatedRouterIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfDesignatedRouterIP.setStatus("mandatory")
_OspfIfBackupDesignatedRouterIP_Type = IpAddress
_OspfIfBackupDesignatedRouterIP_Object = MibTableColumn
ospfIfBackupDesignatedRouterIP = _OspfIfBackupDesignatedRouterIP_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 3, 1, 3),
    _OspfIfBackupDesignatedRouterIP_Type()
)
ospfIfBackupDesignatedRouterIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfBackupDesignatedRouterIP.setStatus("mandatory")
_OspfIfWaitInterval_Type = Integer32
_OspfIfWaitInterval_Object = MibTableColumn
ospfIfWaitInterval = _OspfIfWaitInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 3, 1, 4),
    _OspfIfWaitInterval_Type()
)
ospfIfWaitInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfWaitInterval.setStatus("mandatory")
_OspfIfTotalNeighbours_Type = Integer32
_OspfIfTotalNeighbours_Object = MibTableColumn
ospfIfTotalNeighbours = _OspfIfTotalNeighbours_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 3, 1, 5),
    _OspfIfTotalNeighbours_Type()
)
ospfIfTotalNeighbours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfTotalNeighbours.setStatus("mandatory")
_OspfIfInfoIpAddress_Type = IpAddress
_OspfIfInfoIpAddress_Object = MibTableColumn
ospfIfInfoIpAddress = _OspfIfInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 3, 1, 6),
    _OspfIfInfoIpAddress_Type()
)
ospfIfInfoIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfInfoIpAddress.setStatus("mandatory")
_OspfRouterLSAInfoTable_Object = MibTable
ospfRouterLSAInfoTable = _OspfRouterLSAInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 4)
)
if mibBuilder.loadTexts:
    ospfRouterLSAInfoTable.setStatus("mandatory")
_OspfRouterLSAInfoEntry_Object = MibTableRow
ospfRouterLSAInfoEntry = _OspfRouterLSAInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 4, 1)
)
ospfRouterLSAInfoEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "routerLSAAreaIndex"),
    (0, "ALTEON-TS-NETWORK-MIB", "routerLSALinkIndex"),
    (0, "ALTEON-TS-NETWORK-MIB", "routerLSAId"),
)
if mibBuilder.loadTexts:
    ospfRouterLSAInfoEntry.setStatus("mandatory")
_RouterLSAAreaIndex_Type = Integer32
_RouterLSAAreaIndex_Object = MibTableColumn
routerLSAAreaIndex = _RouterLSAAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 4, 1, 1),
    _RouterLSAAreaIndex_Type()
)
routerLSAAreaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerLSAAreaIndex.setStatus("mandatory")
_RouterLSALinkIndex_Type = Integer32
_RouterLSALinkIndex_Object = MibTableColumn
routerLSALinkIndex = _RouterLSALinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 4, 1, 2),
    _RouterLSALinkIndex_Type()
)
routerLSALinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerLSALinkIndex.setStatus("mandatory")
_RouterLSAId_Type = IpAddress
_RouterLSAId_Object = MibTableColumn
routerLSAId = _RouterLSAId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 4, 1, 3),
    _RouterLSAId_Type()
)
routerLSAId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerLSAId.setStatus("mandatory")
_RouterLSALinkID_Type = IpAddress
_RouterLSALinkID_Object = MibTableColumn
routerLSALinkID = _RouterLSALinkID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 4, 1, 4),
    _RouterLSALinkID_Type()
)
routerLSALinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerLSALinkID.setStatus("mandatory")
_RouterLSALinkData_Type = IpAddress
_RouterLSALinkData_Object = MibTableColumn
routerLSALinkData = _RouterLSALinkData_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 4, 1, 5),
    _RouterLSALinkData_Type()
)
routerLSALinkData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerLSALinkData.setStatus("mandatory")
_RouterLSALinkIfIndex_Type = Integer32
_RouterLSALinkIfIndex_Object = MibTableColumn
routerLSALinkIfIndex = _RouterLSALinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 4, 1, 6),
    _RouterLSALinkIfIndex_Type()
)
routerLSALinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerLSALinkIfIndex.setStatus("mandatory")
_RouterLSANoOfTOSMetrics_Type = Integer32
_RouterLSANoOfTOSMetrics_Object = MibTableColumn
routerLSANoOfTOSMetrics = _RouterLSANoOfTOSMetrics_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 4, 1, 7),
    _RouterLSANoOfTOSMetrics_Type()
)
routerLSANoOfTOSMetrics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerLSANoOfTOSMetrics.setStatus("mandatory")
_RouterLSANoOfTOSZeroMetrics_Type = Integer32
_RouterLSANoOfTOSZeroMetrics_Object = MibTableColumn
routerLSANoOfTOSZeroMetrics = _RouterLSANoOfTOSZeroMetrics_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 5, 4, 1, 8),
    _RouterLSANoOfTOSZeroMetrics_Type()
)
routerLSANoOfTOSZeroMetrics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerLSANoOfTOSZeroMetrics.setStatus("mandatory")
_VrrpOper_ObjectIdentity = ObjectIdentity
vrrpOper = _VrrpOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 5)
)
_VrrpOperVirtRtrTable_Object = MibTable
vrrpOperVirtRtrTable = _VrrpOperVirtRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 5, 1)
)
if mibBuilder.loadTexts:
    vrrpOperVirtRtrTable.setStatus("mandatory")
_VrrpOperVirtRtrEntry_Object = MibTableRow
vrrpOperVirtRtrEntry = _VrrpOperVirtRtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 5, 1, 1)
)
vrrpOperVirtRtrEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "vrrpOperVirtRtrIndex"),
)
if mibBuilder.loadTexts:
    vrrpOperVirtRtrEntry.setStatus("mandatory")
_VrrpOperVirtRtrIndex_Type = Integer32
_VrrpOperVirtRtrIndex_Object = MibTableColumn
vrrpOperVirtRtrIndex = _VrrpOperVirtRtrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 5, 1, 1, 1),
    _VrrpOperVirtRtrIndex_Type()
)
vrrpOperVirtRtrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperVirtRtrIndex.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 5, 1, 1, 2),
    _VrrpOperVirtRtrBackup_Type()
)
vrrpOperVirtRtrBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpOperVirtRtrBackup.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 5, 2),
    _VrrpOperVirtRtrGroupBackup_Type()
)
vrrpOperVirtRtrGroupBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpOperVirtRtrGroupBackup.setStatus("mandatory")
_Vrrp_ObjectIdentity = ObjectIdentity
vrrp = _Vrrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15)
)
_VrrpGeneral_ObjectIdentity = ObjectIdentity
vrrpGeneral = _VrrpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1)
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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 1),
    _VrrpCurCfgGenState_Type()
)
vrrpCurCfgGenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 2),
    _VrrpNewCfgGenState_Type()
)
vrrpNewCfgGenState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenState.setStatus("mandatory")


class _VrrpCurCfgGenTckVirtRtrInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckVirtRtrInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckVirtRtrInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckVirtRtrInc_Object = MibScalar
vrrpCurCfgGenTckVirtRtrInc = _VrrpCurCfgGenTckVirtRtrInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 3),
    _VrrpCurCfgGenTckVirtRtrInc_Type()
)
vrrpCurCfgGenTckVirtRtrInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckVirtRtrInc.setStatus("mandatory")


class _VrrpNewCfgGenTckVirtRtrInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckVirtRtrInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckVirtRtrInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckVirtRtrInc_Object = MibScalar
vrrpNewCfgGenTckVirtRtrInc = _VrrpNewCfgGenTckVirtRtrInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 4),
    _VrrpNewCfgGenTckVirtRtrInc_Type()
)
vrrpNewCfgGenTckVirtRtrInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckVirtRtrInc.setStatus("mandatory")


class _VrrpCurCfgGenTckIpIntfInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckIpIntfInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckIpIntfInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckIpIntfInc_Object = MibScalar
vrrpCurCfgGenTckIpIntfInc = _VrrpCurCfgGenTckIpIntfInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 5),
    _VrrpCurCfgGenTckIpIntfInc_Type()
)
vrrpCurCfgGenTckIpIntfInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckIpIntfInc.setStatus("mandatory")


class _VrrpNewCfgGenTckIpIntfInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckIpIntfInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckIpIntfInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckIpIntfInc_Object = MibScalar
vrrpNewCfgGenTckIpIntfInc = _VrrpNewCfgGenTckIpIntfInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 6),
    _VrrpNewCfgGenTckIpIntfInc_Type()
)
vrrpNewCfgGenTckIpIntfInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckIpIntfInc.setStatus("mandatory")


class _VrrpCurCfgGenTckVlanPortInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckVlanPortInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckVlanPortInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckVlanPortInc_Object = MibScalar
vrrpCurCfgGenTckVlanPortInc = _VrrpCurCfgGenTckVlanPortInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 7),
    _VrrpCurCfgGenTckVlanPortInc_Type()
)
vrrpCurCfgGenTckVlanPortInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckVlanPortInc.setStatus("mandatory")


class _VrrpNewCfgGenTckVlanPortInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckVlanPortInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckVlanPortInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckVlanPortInc_Object = MibScalar
vrrpNewCfgGenTckVlanPortInc = _VrrpNewCfgGenTckVlanPortInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 8),
    _VrrpNewCfgGenTckVlanPortInc_Type()
)
vrrpNewCfgGenTckVlanPortInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckVlanPortInc.setStatus("mandatory")


class _VrrpCurCfgGenTckL4PortInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckL4PortInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckL4PortInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckL4PortInc_Object = MibScalar
vrrpCurCfgGenTckL4PortInc = _VrrpCurCfgGenTckL4PortInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 9),
    _VrrpCurCfgGenTckL4PortInc_Type()
)
vrrpCurCfgGenTckL4PortInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckL4PortInc.setStatus("mandatory")


class _VrrpNewCfgGenTckL4PortInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckL4PortInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckL4PortInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckL4PortInc_Object = MibScalar
vrrpNewCfgGenTckL4PortInc = _VrrpNewCfgGenTckL4PortInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 10),
    _VrrpNewCfgGenTckL4PortInc_Type()
)
vrrpNewCfgGenTckL4PortInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckL4PortInc.setStatus("mandatory")


class _VrrpCurCfgGenTckRServerInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckRServerInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckRServerInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckRServerInc_Object = MibScalar
vrrpCurCfgGenTckRServerInc = _VrrpCurCfgGenTckRServerInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 11),
    _VrrpCurCfgGenTckRServerInc_Type()
)
vrrpCurCfgGenTckRServerInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckRServerInc.setStatus("mandatory")


class _VrrpNewCfgGenTckRServerInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckRServerInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckRServerInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckRServerInc_Object = MibScalar
vrrpNewCfgGenTckRServerInc = _VrrpNewCfgGenTckRServerInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 12),
    _VrrpNewCfgGenTckRServerInc_Type()
)
vrrpNewCfgGenTckRServerInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckRServerInc.setStatus("mandatory")


class _VrrpCurCfgGenTckHsrpInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckHsrpInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckHsrpInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckHsrpInc_Object = MibScalar
vrrpCurCfgGenTckHsrpInc = _VrrpCurCfgGenTckHsrpInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 13),
    _VrrpCurCfgGenTckHsrpInc_Type()
)
vrrpCurCfgGenTckHsrpInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckHsrpInc.setStatus("mandatory")


class _VrrpNewCfgGenTckHsrpInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckHsrpInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckHsrpInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckHsrpInc_Object = MibScalar
vrrpNewCfgGenTckHsrpInc = _VrrpNewCfgGenTckHsrpInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 14),
    _VrrpNewCfgGenTckHsrpInc_Type()
)
vrrpNewCfgGenTckHsrpInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckHsrpInc.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 15),
    _VrrpCurCfgGenHotstandby_Type()
)
vrrpCurCfgGenHotstandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenHotstandby.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 16),
    _VrrpNewCfgGenHotstandby_Type()
)
vrrpNewCfgGenHotstandby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenHotstandby.setStatus("mandatory")


class _VrrpCurCfgGenTckHsrvInc_Type(Integer32):
    """Custom type vrrpCurCfgGenTckHsrvInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpCurCfgGenTckHsrvInc_Type.__name__ = "Integer32"
_VrrpCurCfgGenTckHsrvInc_Object = MibScalar
vrrpCurCfgGenTckHsrvInc = _VrrpCurCfgGenTckHsrvInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 17),
    _VrrpCurCfgGenTckHsrvInc_Type()
)
vrrpCurCfgGenTckHsrvInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgGenTckHsrvInc.setStatus("mandatory")


class _VrrpNewCfgGenTckHsrvInc_Type(Integer32):
    """Custom type vrrpNewCfgGenTckHsrvInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_VrrpNewCfgGenTckHsrvInc_Type.__name__ = "Integer32"
_VrrpNewCfgGenTckHsrvInc_Object = MibScalar
vrrpNewCfgGenTckHsrvInc = _VrrpNewCfgGenTckHsrvInc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 1, 18),
    _VrrpNewCfgGenTckHsrvInc_Type()
)
vrrpNewCfgGenTckHsrvInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgGenTckHsrvInc.setStatus("mandatory")
_VrrpCurCfgVirtRtrTable_Object = MibTable
vrrpCurCfgVirtRtrTable = _VrrpCurCfgVirtRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2)
)
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTable.setStatus("mandatory")
_VrrpCurCfgVirtRtrTableEntry_Object = MibTableRow
vrrpCurCfgVirtRtrTableEntry = _VrrpCurCfgVirtRtrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1)
)
vrrpCurCfgVirtRtrTableEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "vrrpCurCfgVirtRtrIndx"),
)
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTableEntry.setStatus("mandatory")
_VrrpCurCfgVirtRtrIndx_Type = Integer32
_VrrpCurCfgVirtRtrIndx_Object = MibTableColumn
vrrpCurCfgVirtRtrIndx = _VrrpCurCfgVirtRtrIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 1),
    _VrrpCurCfgVirtRtrIndx_Type()
)
vrrpCurCfgVirtRtrIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrIndx.setStatus("mandatory")


class _VrrpCurCfgVirtRtrID_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpCurCfgVirtRtrID_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrID_Object = MibTableColumn
vrrpCurCfgVirtRtrID = _VrrpCurCfgVirtRtrID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 2),
    _VrrpCurCfgVirtRtrID_Type()
)
vrrpCurCfgVirtRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrID.setStatus("mandatory")
_VrrpCurCfgVirtRtrAddr_Type = IpAddress
_VrrpCurCfgVirtRtrAddr_Object = MibTableColumn
vrrpCurCfgVirtRtrAddr = _VrrpCurCfgVirtRtrAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 3),
    _VrrpCurCfgVirtRtrAddr_Type()
)
vrrpCurCfgVirtRtrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrAddr.setStatus("mandatory")
_VrrpCurCfgVirtRtrIfIndex_Type = Integer32
_VrrpCurCfgVirtRtrIfIndex_Object = MibTableColumn
vrrpCurCfgVirtRtrIfIndex = _VrrpCurCfgVirtRtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 4),
    _VrrpCurCfgVirtRtrIfIndex_Type()
)
vrrpCurCfgVirtRtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrIfIndex.setStatus("mandatory")


class _VrrpCurCfgVirtRtrInterval_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpCurCfgVirtRtrInterval_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrInterval_Object = MibTableColumn
vrrpCurCfgVirtRtrInterval = _VrrpCurCfgVirtRtrInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 5),
    _VrrpCurCfgVirtRtrInterval_Type()
)
vrrpCurCfgVirtRtrInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrInterval.setStatus("mandatory")


class _VrrpCurCfgVirtRtrPriority_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VrrpCurCfgVirtRtrPriority_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrPriority_Object = MibTableColumn
vrrpCurCfgVirtRtrPriority = _VrrpCurCfgVirtRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 6),
    _VrrpCurCfgVirtRtrPriority_Type()
)
vrrpCurCfgVirtRtrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrPriority.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 7),
    _VrrpCurCfgVirtRtrPreempt_Type()
)
vrrpCurCfgVirtRtrPreempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrPreempt.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 8),
    _VrrpCurCfgVirtRtrState_Type()
)
vrrpCurCfgVirtRtrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 9),
    _VrrpCurCfgVirtRtrSharing_Type()
)
vrrpCurCfgVirtRtrSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrSharing.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 10),
    _VrrpCurCfgVirtRtrTckVirtRtr_Type()
)
vrrpCurCfgVirtRtrTckVirtRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckVirtRtr.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 11),
    _VrrpCurCfgVirtRtrTckIpIntf_Type()
)
vrrpCurCfgVirtRtrTckIpIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckIpIntf.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 12),
    _VrrpCurCfgVirtRtrTckVlanPort_Type()
)
vrrpCurCfgVirtRtrTckVlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckVlanPort.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 13),
    _VrrpCurCfgVirtRtrTckL4Port_Type()
)
vrrpCurCfgVirtRtrTckL4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckL4Port.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 14),
    _VrrpCurCfgVirtRtrTckRServer_Type()
)
vrrpCurCfgVirtRtrTckRServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckRServer.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 15),
    _VrrpCurCfgVirtRtrTckHsrp_Type()
)
vrrpCurCfgVirtRtrTckHsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckHsrp.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 2, 1, 16),
    _VrrpCurCfgVirtRtrTckHsrv_Type()
)
vrrpCurCfgVirtRtrTckHsrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrTckHsrv.setStatus("mandatory")
_VrrpNewCfgVirtRtrTable_Object = MibTable
vrrpNewCfgVirtRtrTable = _VrrpNewCfgVirtRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3)
)
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTable.setStatus("mandatory")
_VrrpNewCfgVirtRtrTableEntry_Object = MibTableRow
vrrpNewCfgVirtRtrTableEntry = _VrrpNewCfgVirtRtrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1)
)
vrrpNewCfgVirtRtrTableEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "vrrpNewCfgVirtRtrIndx"),
)
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTableEntry.setStatus("mandatory")
_VrrpNewCfgVirtRtrIndx_Type = Integer32
_VrrpNewCfgVirtRtrIndx_Object = MibTableColumn
vrrpNewCfgVirtRtrIndx = _VrrpNewCfgVirtRtrIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 1),
    _VrrpNewCfgVirtRtrIndx_Type()
)
vrrpNewCfgVirtRtrIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrIndx.setStatus("mandatory")


class _VrrpNewCfgVirtRtrID_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpNewCfgVirtRtrID_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrID_Object = MibTableColumn
vrrpNewCfgVirtRtrID = _VrrpNewCfgVirtRtrID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 2),
    _VrrpNewCfgVirtRtrID_Type()
)
vrrpNewCfgVirtRtrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrID.setStatus("mandatory")
_VrrpNewCfgVirtRtrAddr_Type = IpAddress
_VrrpNewCfgVirtRtrAddr_Object = MibTableColumn
vrrpNewCfgVirtRtrAddr = _VrrpNewCfgVirtRtrAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 3),
    _VrrpNewCfgVirtRtrAddr_Type()
)
vrrpNewCfgVirtRtrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrAddr.setStatus("mandatory")
_VrrpNewCfgVirtRtrIfIndex_Type = Integer32
_VrrpNewCfgVirtRtrIfIndex_Object = MibTableColumn
vrrpNewCfgVirtRtrIfIndex = _VrrpNewCfgVirtRtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 4),
    _VrrpNewCfgVirtRtrIfIndex_Type()
)
vrrpNewCfgVirtRtrIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrIfIndex.setStatus("mandatory")


class _VrrpNewCfgVirtRtrInterval_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpNewCfgVirtRtrInterval_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrInterval_Object = MibTableColumn
vrrpNewCfgVirtRtrInterval = _VrrpNewCfgVirtRtrInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 5),
    _VrrpNewCfgVirtRtrInterval_Type()
)
vrrpNewCfgVirtRtrInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrInterval.setStatus("mandatory")


class _VrrpNewCfgVirtRtrPriority_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VrrpNewCfgVirtRtrPriority_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrPriority_Object = MibTableColumn
vrrpNewCfgVirtRtrPriority = _VrrpNewCfgVirtRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 6),
    _VrrpNewCfgVirtRtrPriority_Type()
)
vrrpNewCfgVirtRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrPriority.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 7),
    _VrrpNewCfgVirtRtrPreempt_Type()
)
vrrpNewCfgVirtRtrPreempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrPreempt.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 8),
    _VrrpNewCfgVirtRtrState_Type()
)
vrrpNewCfgVirtRtrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 9),
    _VrrpNewCfgVirtRtrDelete_Type()
)
vrrpNewCfgVirtRtrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrDelete.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 10),
    _VrrpNewCfgVirtRtrSharing_Type()
)
vrrpNewCfgVirtRtrSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrSharing.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 11),
    _VrrpNewCfgVirtRtrTckVirtRtr_Type()
)
vrrpNewCfgVirtRtrTckVirtRtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckVirtRtr.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 12),
    _VrrpNewCfgVirtRtrTckIpIntf_Type()
)
vrrpNewCfgVirtRtrTckIpIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckIpIntf.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 13),
    _VrrpNewCfgVirtRtrTckVlanPort_Type()
)
vrrpNewCfgVirtRtrTckVlanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckVlanPort.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 14),
    _VrrpNewCfgVirtRtrTckL4Port_Type()
)
vrrpNewCfgVirtRtrTckL4Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckL4Port.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 15),
    _VrrpNewCfgVirtRtrTckRServer_Type()
)
vrrpNewCfgVirtRtrTckRServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckRServer.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 16),
    _VrrpNewCfgVirtRtrTckHsrp_Type()
)
vrrpNewCfgVirtRtrTckHsrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckHsrp.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 3, 1, 17),
    _VrrpNewCfgVirtRtrTckHsrv_Type()
)
vrrpNewCfgVirtRtrTckHsrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrTckHsrv.setStatus("mandatory")
_VrrpCurCfgIfTable_Object = MibTable
vrrpCurCfgIfTable = _VrrpCurCfgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 4)
)
if mibBuilder.loadTexts:
    vrrpCurCfgIfTable.setStatus("mandatory")
_VrrpCurCfgIfTableEntry_Object = MibTableRow
vrrpCurCfgIfTableEntry = _VrrpCurCfgIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 4, 1)
)
vrrpCurCfgIfTableEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "vrrpCurCfgIfIndx"),
)
if mibBuilder.loadTexts:
    vrrpCurCfgIfTableEntry.setStatus("mandatory")
_VrrpCurCfgIfIndx_Type = Integer32
_VrrpCurCfgIfIndx_Object = MibTableColumn
vrrpCurCfgIfIndx = _VrrpCurCfgIfIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 4, 1, 1),
    _VrrpCurCfgIfIndx_Type()
)
vrrpCurCfgIfIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgIfIndx.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 4, 1, 2),
    _VrrpCurCfgIfAuthType_Type()
)
vrrpCurCfgIfAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgIfAuthType.setStatus("mandatory")


class _VrrpCurCfgIfPasswd_Type(DisplayString):
    """Custom type vrrpCurCfgIfPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_VrrpCurCfgIfPasswd_Type.__name__ = "DisplayString"
_VrrpCurCfgIfPasswd_Object = MibTableColumn
vrrpCurCfgIfPasswd = _VrrpCurCfgIfPasswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 4, 1, 3),
    _VrrpCurCfgIfPasswd_Type()
)
vrrpCurCfgIfPasswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgIfPasswd.setStatus("mandatory")
_VrrpNewCfgIfTable_Object = MibTable
vrrpNewCfgIfTable = _VrrpNewCfgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 5)
)
if mibBuilder.loadTexts:
    vrrpNewCfgIfTable.setStatus("mandatory")
_VrrpNewCfgIfTableEntry_Object = MibTableRow
vrrpNewCfgIfTableEntry = _VrrpNewCfgIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 5, 1)
)
vrrpNewCfgIfTableEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "vrrpNewCfgIfIndx"),
)
if mibBuilder.loadTexts:
    vrrpNewCfgIfTableEntry.setStatus("mandatory")
_VrrpNewCfgIfIndx_Type = Integer32
_VrrpNewCfgIfIndx_Object = MibTableColumn
vrrpNewCfgIfIndx = _VrrpNewCfgIfIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 5, 1, 1),
    _VrrpNewCfgIfIndx_Type()
)
vrrpNewCfgIfIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpNewCfgIfIndx.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 5, 1, 2),
    _VrrpNewCfgIfAuthType_Type()
)
vrrpNewCfgIfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgIfAuthType.setStatus("mandatory")


class _VrrpNewCfgIfPasswd_Type(DisplayString):
    """Custom type vrrpNewCfgIfPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_VrrpNewCfgIfPasswd_Type.__name__ = "DisplayString"
_VrrpNewCfgIfPasswd_Object = MibTableColumn
vrrpNewCfgIfPasswd = _VrrpNewCfgIfPasswd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 5, 1, 3),
    _VrrpNewCfgIfPasswd_Type()
)
vrrpNewCfgIfPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgIfPasswd.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 5, 1, 4),
    _VrrpNewCfgIfDelete_Type()
)
vrrpNewCfgIfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgIfDelete.setStatus("mandatory")
_VrrpCurCfgVirtRtrGrpTable_Object = MibTable
vrrpCurCfgVirtRtrGrpTable = _VrrpCurCfgVirtRtrGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6)
)
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTable.setStatus("mandatory")
_VrrpCurCfgVirtRtrGrpTableEntry_Object = MibTableRow
vrrpCurCfgVirtRtrGrpTableEntry = _VrrpCurCfgVirtRtrGrpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1)
)
vrrpCurCfgVirtRtrGrpTableEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "vrrpCurCfgVirtRtrGrpIndx"),
)
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTableEntry.setStatus("mandatory")
_VrrpCurCfgVirtRtrGrpIndx_Type = Integer32
_VrrpCurCfgVirtRtrGrpIndx_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpIndx = _VrrpCurCfgVirtRtrGrpIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 1),
    _VrrpCurCfgVirtRtrGrpIndx_Type()
)
vrrpCurCfgVirtRtrGrpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpIndx.setStatus("mandatory")


class _VrrpCurCfgVirtRtrGrpID_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpCurCfgVirtRtrGrpID_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpID_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpID = _VrrpCurCfgVirtRtrGrpID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 2),
    _VrrpCurCfgVirtRtrGrpID_Type()
)
vrrpCurCfgVirtRtrGrpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpID.setStatus("mandatory")
_VrrpCurCfgVirtRtrGrpIfIndex_Type = Integer32
_VrrpCurCfgVirtRtrGrpIfIndex_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpIfIndex = _VrrpCurCfgVirtRtrGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 3),
    _VrrpCurCfgVirtRtrGrpIfIndex_Type()
)
vrrpCurCfgVirtRtrGrpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpIfIndex.setStatus("mandatory")


class _VrrpCurCfgVirtRtrGrpInterval_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpCurCfgVirtRtrGrpInterval_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpInterval_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpInterval = _VrrpCurCfgVirtRtrGrpInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 4),
    _VrrpCurCfgVirtRtrGrpInterval_Type()
)
vrrpCurCfgVirtRtrGrpInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpInterval.setStatus("mandatory")


class _VrrpCurCfgVirtRtrGrpPriority_Type(Integer32):
    """Custom type vrrpCurCfgVirtRtrGrpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VrrpCurCfgVirtRtrGrpPriority_Type.__name__ = "Integer32"
_VrrpCurCfgVirtRtrGrpPriority_Object = MibTableColumn
vrrpCurCfgVirtRtrGrpPriority = _VrrpCurCfgVirtRtrGrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 5),
    _VrrpCurCfgVirtRtrGrpPriority_Type()
)
vrrpCurCfgVirtRtrGrpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpPriority.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 6),
    _VrrpCurCfgVirtRtrGrpPreempt_Type()
)
vrrpCurCfgVirtRtrGrpPreempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpPreempt.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 7),
    _VrrpCurCfgVirtRtrGrpState_Type()
)
vrrpCurCfgVirtRtrGrpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 8),
    _VrrpCurCfgVirtRtrGrpSharing_Type()
)
vrrpCurCfgVirtRtrGrpSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpSharing.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 9),
    _VrrpCurCfgVirtRtrGrpTckVirtRtr_Type()
)
vrrpCurCfgVirtRtrGrpTckVirtRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckVirtRtr.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 10),
    _VrrpCurCfgVirtRtrGrpTckIpIntf_Type()
)
vrrpCurCfgVirtRtrGrpTckIpIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckIpIntf.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 11),
    _VrrpCurCfgVirtRtrGrpTckVlanPort_Type()
)
vrrpCurCfgVirtRtrGrpTckVlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckVlanPort.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 12),
    _VrrpCurCfgVirtRtrGrpTckL4Port_Type()
)
vrrpCurCfgVirtRtrGrpTckL4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckL4Port.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 13),
    _VrrpCurCfgVirtRtrGrpTckRServer_Type()
)
vrrpCurCfgVirtRtrGrpTckRServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckRServer.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 14),
    _VrrpCurCfgVirtRtrGrpTckHsrp_Type()
)
vrrpCurCfgVirtRtrGrpTckHsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckHsrp.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 6, 1, 15),
    _VrrpCurCfgVirtRtrGrpTckHsrv_Type()
)
vrrpCurCfgVirtRtrGrpTckHsrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpCurCfgVirtRtrGrpTckHsrv.setStatus("mandatory")
_VrrpNewCfgVirtRtrGrpTable_Object = MibTable
vrrpNewCfgVirtRtrGrpTable = _VrrpNewCfgVirtRtrGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7)
)
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTable.setStatus("mandatory")
_VrrpNewCfgVirtRtrGrpTableEntry_Object = MibTableRow
vrrpNewCfgVirtRtrGrpTableEntry = _VrrpNewCfgVirtRtrGrpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1)
)
vrrpNewCfgVirtRtrGrpTableEntry.setIndexNames(
    (0, "ALTEON-TS-NETWORK-MIB", "vrrpNewCfgVirtRtrGrpIndx"),
)
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTableEntry.setStatus("mandatory")
_VrrpNewCfgVirtRtrGrpIndx_Type = Integer32
_VrrpNewCfgVirtRtrGrpIndx_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpIndx = _VrrpNewCfgVirtRtrGrpIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 1),
    _VrrpNewCfgVirtRtrGrpIndx_Type()
)
vrrpNewCfgVirtRtrGrpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpIndx.setStatus("mandatory")


class _VrrpNewCfgVirtRtrGrpID_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpNewCfgVirtRtrGrpID_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpID_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpID = _VrrpNewCfgVirtRtrGrpID_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 2),
    _VrrpNewCfgVirtRtrGrpID_Type()
)
vrrpNewCfgVirtRtrGrpID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpID.setStatus("mandatory")
_VrrpNewCfgVirtRtrGrpIfIndex_Type = Integer32
_VrrpNewCfgVirtRtrGrpIfIndex_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpIfIndex = _VrrpNewCfgVirtRtrGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 3),
    _VrrpNewCfgVirtRtrGrpIfIndex_Type()
)
vrrpNewCfgVirtRtrGrpIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpIfIndex.setStatus("mandatory")


class _VrrpNewCfgVirtRtrGrpInterval_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpNewCfgVirtRtrGrpInterval_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpInterval_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpInterval = _VrrpNewCfgVirtRtrGrpInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 4),
    _VrrpNewCfgVirtRtrGrpInterval_Type()
)
vrrpNewCfgVirtRtrGrpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpInterval.setStatus("mandatory")


class _VrrpNewCfgVirtRtrGrpPriority_Type(Integer32):
    """Custom type vrrpNewCfgVirtRtrGrpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VrrpNewCfgVirtRtrGrpPriority_Type.__name__ = "Integer32"
_VrrpNewCfgVirtRtrGrpPriority_Object = MibTableColumn
vrrpNewCfgVirtRtrGrpPriority = _VrrpNewCfgVirtRtrGrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 5),
    _VrrpNewCfgVirtRtrGrpPriority_Type()
)
vrrpNewCfgVirtRtrGrpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpPriority.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 6),
    _VrrpNewCfgVirtRtrGrpPreempt_Type()
)
vrrpNewCfgVirtRtrGrpPreempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpPreempt.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 7),
    _VrrpNewCfgVirtRtrGrpState_Type()
)
vrrpNewCfgVirtRtrGrpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 8),
    _VrrpNewCfgVirtRtrGrpDelete_Type()
)
vrrpNewCfgVirtRtrGrpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpDelete.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 9),
    _VrrpNewCfgVirtRtrGrpSharing_Type()
)
vrrpNewCfgVirtRtrGrpSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpSharing.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 10),
    _VrrpNewCfgVirtRtrGrpTckVirtRtr_Type()
)
vrrpNewCfgVirtRtrGrpTckVirtRtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckVirtRtr.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 11),
    _VrrpNewCfgVirtRtrGrpTckIpIntf_Type()
)
vrrpNewCfgVirtRtrGrpTckIpIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckIpIntf.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 12),
    _VrrpNewCfgVirtRtrGrpTckVlanPort_Type()
)
vrrpNewCfgVirtRtrGrpTckVlanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckVlanPort.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 13),
    _VrrpNewCfgVirtRtrGrpTckL4Port_Type()
)
vrrpNewCfgVirtRtrGrpTckL4Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckL4Port.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 14),
    _VrrpNewCfgVirtRtrGrpTckRServer_Type()
)
vrrpNewCfgVirtRtrGrpTckRServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckRServer.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 15),
    _VrrpNewCfgVirtRtrGrpTckHsrp_Type()
)
vrrpNewCfgVirtRtrGrpTckHsrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckHsrp.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 7, 1, 16),
    _VrrpNewCfgVirtRtrGrpTckHsrv_Type()
)
vrrpNewCfgVirtRtrGrpTckHsrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNewCfgVirtRtrGrpTckHsrv.setStatus("mandatory")
_VrrpVirtRtrTableMaxSize_Type = Integer32
_VrrpVirtRtrTableMaxSize_Object = MibScalar
vrrpVirtRtrTableMaxSize = _VrrpVirtRtrTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 8),
    _VrrpVirtRtrTableMaxSize_Type()
)
vrrpVirtRtrTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpVirtRtrTableMaxSize.setStatus("mandatory")
_VrrpIfTableMaxSize_Type = Integer32
_VrrpIfTableMaxSize_Object = MibScalar
vrrpIfTableMaxSize = _VrrpIfTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 9),
    _VrrpIfTableMaxSize_Type()
)
vrrpIfTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpIfTableMaxSize.setStatus("mandatory")
_VrrpVirtRtrGrpTableMaxSize_Type = Integer32
_VrrpVirtRtrGrpTableMaxSize_Object = MibScalar
vrrpVirtRtrGrpTableMaxSize = _VrrpVirtRtrGrpTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 15, 10),
    _VrrpVirtRtrGrpTableMaxSize_Type()
)
vrrpVirtRtrGrpTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpVirtRtrGrpTableMaxSize.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTEON-TS-NETWORK-MIB",
    **{"iprouting": iprouting,
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
       "ipForward": ipForward,
       "ripConfig": ripConfig,
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
       "ripCurCfgVip": ripCurCfgVip,
       "ripNewCfgVip": ripNewCfgVip,
       "ipFwdCurCfgPortTable": ipFwdCurCfgPortTable,
       "ipFwdCurCfgPortEntry": ipFwdCurCfgPortEntry,
       "ipFwdCurCfgPortIndex": ipFwdCurCfgPortIndex,
       "ipFwdCurCfgPortState": ipFwdCurCfgPortState,
       "ipFwdNewCfgPortTable": ipFwdNewCfgPortTable,
       "ipFwdNewCfgPortEntry": ipFwdNewCfgPortEntry,
       "ipFwdNewCfgPortIndex": ipFwdNewCfgPortIndex,
       "ipFwdNewCfgPortState": ipFwdNewCfgPortState,
       "ipFwdCurCfgState": ipFwdCurCfgState,
       "ipFwdNewCfgState": ipFwdNewCfgState,
       "ipFwdCurCfgDirectedBcast": ipFwdCurCfgDirectedBcast,
       "ipFwdNewCfgDirectedBcast": ipFwdNewCfgDirectedBcast,
       "ipFwdPortTableMaxSize": ipFwdPortTableMaxSize,
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
       "arpCurCfgReARPPeriod": arpCurCfgReARPPeriod,
       "arpNewCfgReARPPeriod": arpNewCfgReARPPeriod,
       "ipCurCfgGwMetric": ipCurCfgGwMetric,
       "ipNewCfgGwMetric": ipNewCfgGwMetric,
       "ipCurCfgBootpAddr": ipCurCfgBootpAddr,
       "ipNewCfgBootpAddr": ipNewCfgBootpAddr,
       "ipCurCfgBootpAddr2": ipCurCfgBootpAddr2,
       "ipNewCfgBootpAddr2": ipNewCfgBootpAddr2,
       "ipCurCfgBootpState": ipCurCfgBootpState,
       "ipNewCfgBootpState": ipNewCfgBootpState,
       "ipStaticRouteTableMaxSize": ipStaticRouteTableMaxSize,
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
       "ospfCurCfgAreaTable": ospfCurCfgAreaTable,
       "ospfCurCfgAreaEntry": ospfCurCfgAreaEntry,
       "ospfCurCfgAreaIndex": ospfCurCfgAreaIndex,
       "ospfCurCfgAreaId": ospfCurCfgAreaId,
       "ospfCurCfgAreaSpfInterval": ospfCurCfgAreaSpfInterval,
       "ospfCurCfgAreaAuthType": ospfCurCfgAreaAuthType,
       "ospfNewCfgAreaTable": ospfNewCfgAreaTable,
       "ospfNewCfgAreaEntry": ospfNewCfgAreaEntry,
       "ospfNewCfgAreaIndex": ospfNewCfgAreaIndex,
       "ospfNewCfgAreaId": ospfNewCfgAreaId,
       "ospfNewCfgAreaSpfInterval": ospfNewCfgAreaSpfInterval,
       "ospfNewCfgAreaAuthType": ospfNewCfgAreaAuthType,
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
       "dnsStats": dnsStats,
       "dnsStatInGoodDnsRequests": dnsStatInGoodDnsRequests,
       "dnsStatInBadDnsRequests": dnsStatInBadDnsRequests,
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
       "ip-info": ip_info,
       "ipRouteInfoTable": ipRouteInfoTable,
       "ipRouteInfoEntry": ipRouteInfoEntry,
       "ipRouteInfoIndx": ipRouteInfoIndx,
       "ipRouteInfoDestIp": ipRouteInfoDestIp,
       "ipRouteInfoMask": ipRouteInfoMask,
       "ipRouteInfoGateway": ipRouteInfoGateway,
       "ipRouteInfoTag": ipRouteInfoTag,
       "ipRouteInfoType": ipRouteInfoType,
       "ipRouteInfoInterface": ipRouteInfoInterface,
       "arpInfoTable": arpInfoTable,
       "arpInfoEntry": arpInfoEntry,
       "arpInfoDestIp": arpInfoDestIp,
       "arpInfoMacAddr": arpInfoMacAddr,
       "arpInfoVLAN": arpInfoVLAN,
       "arpInfoSrcPort": arpInfoSrcPort,
       "arpInfoRefPorts": arpInfoRefPorts,
       "arpInfoFlag": arpInfoFlag,
       "vrrp-info": vrrp_info,
       "vrrpInfoVirtRtrTable": vrrpInfoVirtRtrTable,
       "vrrpInfoVirtRtrTableEntry": vrrpInfoVirtRtrTableEntry,
       "vrrpInfoVirtRtrIndex": vrrpInfoVirtRtrIndex,
       "vrrpInfoVirtRtrState": vrrpInfoVirtRtrState,
       "vrrpInfoVirtRtrOwnership": vrrpInfoVirtRtrOwnership,
       "vrrpInfoVirtRtrServer": vrrpInfoVirtRtrServer,
       "vrrpInfoVirtRtrProxy": vrrpInfoVirtRtrProxy,
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
       "ospfRouterLSAInfoTable": ospfRouterLSAInfoTable,
       "ospfRouterLSAInfoEntry": ospfRouterLSAInfoEntry,
       "routerLSAAreaIndex": routerLSAAreaIndex,
       "routerLSALinkIndex": routerLSALinkIndex,
       "routerLSAId": routerLSAId,
       "routerLSALinkID": routerLSALinkID,
       "routerLSALinkData": routerLSALinkData,
       "routerLSALinkIfIndex": routerLSALinkIfIndex,
       "routerLSANoOfTOSMetrics": routerLSANoOfTOSMetrics,
       "routerLSANoOfTOSZeroMetrics": routerLSANoOfTOSZeroMetrics,
       "vrrpOper": vrrpOper,
       "vrrpOperVirtRtrTable": vrrpOperVirtRtrTable,
       "vrrpOperVirtRtrEntry": vrrpOperVirtRtrEntry,
       "vrrpOperVirtRtrIndex": vrrpOperVirtRtrIndex,
       "vrrpOperVirtRtrBackup": vrrpOperVirtRtrBackup,
       "vrrpOperVirtRtrGroupBackup": vrrpOperVirtRtrGroupBackup,
       "vrrp": vrrp,
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
       "vrrpVirtRtrTableMaxSize": vrrpVirtRtrTableMaxSize,
       "vrrpIfTableMaxSize": vrrpIfTableMaxSize,
       "vrrpVirtRtrGrpTableMaxSize": vrrpVirtRtrGrpTableMaxSize}
)

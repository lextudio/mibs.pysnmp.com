# SNMP MIB module (MRD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MRD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:33 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xylanMrouted,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanMrouted")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MrdMIB_ObjectIdentity = ObjectIdentity
mrdMIB = _MrdMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1)
)
_MrdMIBObjects_ObjectIdentity = ObjectIdentity
mrdMIBObjects = _MrdMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1)
)
_MrdGeneralGroup_ObjectIdentity = ObjectIdentity
mrdGeneralGroup = _MrdGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 1)
)
_MrdVersion_Type = DisplayString
_MrdVersion_Object = MibScalar
mrdVersion = _MrdVersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 1, 1),
    _MrdVersion_Type()
)
mrdVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdVersion.setStatus("mandatory")
_MrdCachedRouteResTime_Type = Integer32
_MrdCachedRouteResTime_Object = MibScalar
mrdCachedRouteResTime = _MrdCachedRouteResTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 1, 2),
    _MrdCachedRouteResTime_Type()
)
mrdCachedRouteResTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdCachedRouteResTime.setStatus("mandatory")


class _MrdPruneFlag_Type(Integer32):
    """Custom type mrdPruneFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-pruningrouter", 2),
          ("pruningrouter", 1))
    )


_MrdPruneFlag_Type.__name__ = "Integer32"
_MrdPruneFlag_Object = MibScalar
mrdPruneFlag = _MrdPruneFlag_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 1, 3),
    _MrdPruneFlag_Type()
)
mrdPruneFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdPruneFlag.setStatus("mandatory")


class _MrdConfigUpdate_Type(Integer32):
    """Custom type mrdConfigUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configUpdate", 1),
          ("noConfigUpdate", 2))
    )


_MrdConfigUpdate_Type.__name__ = "Integer32"
_MrdConfigUpdate_Object = MibScalar
mrdConfigUpdate = _MrdConfigUpdate_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 1, 4),
    _MrdConfigUpdate_Type()
)
mrdConfigUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdConfigUpdate.setStatus("mandatory")


class _MrdEnableDisable_Type(Integer32):
    """Custom type mrdEnableDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doDisable", 2),
          ("doEnable", 1))
    )


_MrdEnableDisable_Type.__name__ = "Integer32"
_MrdEnableDisable_Object = MibScalar
mrdEnableDisable = _MrdEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 1, 5),
    _MrdEnableDisable_Type()
)
mrdEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdEnableDisable.setStatus("mandatory")
_MrdIntfBoundaryTable_Object = MibTable
mrdIntfBoundaryTable = _MrdIntfBoundaryTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mrdIntfBoundaryTable.setStatus("mandatory")
_MrdIntfBoundaryEntry_Object = MibTableRow
mrdIntfBoundaryEntry = _MrdIntfBoundaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 2, 1)
)
mrdIntfBoundaryEntry.setIndexNames(
    (0, "MRD-MIB", "mrdIntfPhyIntAddr"),
    (0, "MRD-MIB", "mrdIntfScopedAddress"),
)
if mibBuilder.loadTexts:
    mrdIntfBoundaryEntry.setStatus("mandatory")
_MrdIntfPhyIntAddr_Type = IpAddress
_MrdIntfPhyIntAddr_Object = MibTableColumn
mrdIntfPhyIntAddr = _MrdIntfPhyIntAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 2, 1, 1),
    _MrdIntfPhyIntAddr_Type()
)
mrdIntfPhyIntAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdIntfPhyIntAddr.setStatus("mandatory")
_MrdIntfScopedAddress_Type = IpAddress
_MrdIntfScopedAddress_Object = MibTableColumn
mrdIntfScopedAddress = _MrdIntfScopedAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 2, 1, 2),
    _MrdIntfScopedAddress_Type()
)
mrdIntfScopedAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdIntfScopedAddress.setStatus("mandatory")
_MrdIntfBoundMaskLength_Type = Integer32
_MrdIntfBoundMaskLength_Object = MibTableColumn
mrdIntfBoundMaskLength = _MrdIntfBoundMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 2, 1, 3),
    _MrdIntfBoundMaskLength_Type()
)
mrdIntfBoundMaskLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdIntfBoundMaskLength.setStatus("mandatory")


class _MrdIntfAdminState_Type(Integer32):
    """Custom type mrdIntfAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("normal", 2))
    )


_MrdIntfAdminState_Type.__name__ = "Integer32"
_MrdIntfAdminState_Object = MibTableColumn
mrdIntfAdminState = _MrdIntfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 2, 1, 4),
    _MrdIntfAdminState_Type()
)
mrdIntfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdIntfAdminState.setStatus("mandatory")
_MrdTunBoundaryTable_Object = MibTable
mrdTunBoundaryTable = _MrdTunBoundaryTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mrdTunBoundaryTable.setStatus("mandatory")
_MrdTunBoundaryEntry_Object = MibTableRow
mrdTunBoundaryEntry = _MrdTunBoundaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 3, 1)
)
mrdTunBoundaryEntry.setIndexNames(
    (0, "MRD-MIB", "mrdTunLocalAddress"),
    (0, "MRD-MIB", "mrdTunRemoteAddress"),
    (0, "MRD-MIB", "mrdTunScopedAddress"),
)
if mibBuilder.loadTexts:
    mrdTunBoundaryEntry.setStatus("mandatory")
_MrdTunLocalAddress_Type = IpAddress
_MrdTunLocalAddress_Object = MibTableColumn
mrdTunLocalAddress = _MrdTunLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 3, 1, 1),
    _MrdTunLocalAddress_Type()
)
mrdTunLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdTunLocalAddress.setStatus("mandatory")
_MrdTunRemoteAddress_Type = IpAddress
_MrdTunRemoteAddress_Object = MibTableColumn
mrdTunRemoteAddress = _MrdTunRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 3, 1, 2),
    _MrdTunRemoteAddress_Type()
)
mrdTunRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdTunRemoteAddress.setStatus("mandatory")
_MrdTunScopedAddress_Type = IpAddress
_MrdTunScopedAddress_Object = MibTableColumn
mrdTunScopedAddress = _MrdTunScopedAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 3, 1, 3),
    _MrdTunScopedAddress_Type()
)
mrdTunScopedAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdTunScopedAddress.setStatus("mandatory")
_MrdTunBoundMaskLength_Type = Integer32
_MrdTunBoundMaskLength_Object = MibTableColumn
mrdTunBoundMaskLength = _MrdTunBoundMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 3, 1, 4),
    _MrdTunBoundMaskLength_Type()
)
mrdTunBoundMaskLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdTunBoundMaskLength.setStatus("mandatory")


class _MrdTunAdminState_Type(Integer32):
    """Custom type mrdTunAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("normal", 2))
    )


_MrdTunAdminState_Type.__name__ = "Integer32"
_MrdTunAdminState_Object = MibTableColumn
mrdTunAdminState = _MrdTunAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 3, 1, 5),
    _MrdTunAdminState_Type()
)
mrdTunAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdTunAdminState.setStatus("mandatory")
_MrdAltNetTable_Object = MibTable
mrdAltNetTable = _MrdAltNetTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    mrdAltNetTable.setStatus("mandatory")
_MrdAltNetEntry_Object = MibTableRow
mrdAltNetEntry = _MrdAltNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 4, 1)
)
mrdAltNetEntry.setIndexNames(
    (0, "MRD-MIB", "mrdAltNetAddr"),
    (0, "MRD-MIB", "mrdNetworkAddress"),
)
if mibBuilder.loadTexts:
    mrdAltNetEntry.setStatus("mandatory")
_MrdAltNetAddr_Type = IpAddress
_MrdAltNetAddr_Object = MibTableColumn
mrdAltNetAddr = _MrdAltNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 4, 1, 1),
    _MrdAltNetAddr_Type()
)
mrdAltNetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdAltNetAddr.setStatus("mandatory")
_MrdNetworkAddress_Type = IpAddress
_MrdNetworkAddress_Object = MibTableColumn
mrdNetworkAddress = _MrdNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 4, 1, 2),
    _MrdNetworkAddress_Type()
)
mrdNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdNetworkAddress.setStatus("mandatory")
_MrdANetMaskLength_Type = Integer32
_MrdANetMaskLength_Object = MibTableColumn
mrdANetMaskLength = _MrdANetMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 4, 1, 3),
    _MrdANetMaskLength_Type()
)
mrdANetMaskLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdANetMaskLength.setStatus("mandatory")


class _MrdANetAdminState_Type(Integer32):
    """Custom type mrdANetAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("normal", 2))
    )


_MrdANetAdminState_Type.__name__ = "Integer32"
_MrdANetAdminState_Object = MibTableColumn
mrdANetAdminState = _MrdANetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 4, 1, 4),
    _MrdANetAdminState_Type()
)
mrdANetAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdANetAdminState.setStatus("mandatory")
_MrdInterfaceTable_Object = MibTable
mrdInterfaceTable = _MrdInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    mrdInterfaceTable.setStatus("mandatory")
_MrdInterfaceEntry_Object = MibTableRow
mrdInterfaceEntry = _MrdInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 5, 1)
)
mrdInterfaceEntry.setIndexNames(
    (0, "MRD-MIB", "mrdIFAddress"),
)
if mibBuilder.loadTexts:
    mrdInterfaceEntry.setStatus("mandatory")
_MrdIFAddress_Type = IpAddress
_MrdIFAddress_Object = MibTableColumn
mrdIFAddress = _MrdIFAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 5, 1, 1),
    _MrdIFAddress_Type()
)
mrdIFAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdIFAddress.setStatus("mandatory")


class _MrdIFEnabledFlag_Type(Integer32):
    """Custom type mrdIFEnabledFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MrdIFEnabledFlag_Type.__name__ = "Integer32"
_MrdIFEnabledFlag_Object = MibTableColumn
mrdIFEnabledFlag = _MrdIFEnabledFlag_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 5, 1, 2),
    _MrdIFEnabledFlag_Type()
)
mrdIFEnabledFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdIFEnabledFlag.setStatus("mandatory")


class _MrdIFMetric_Type(Integer32):
    """Custom type mrdIFMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_MrdIFMetric_Type.__name__ = "Integer32"
_MrdIFMetric_Object = MibTableColumn
mrdIFMetric = _MrdIFMetric_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 5, 1, 3),
    _MrdIFMetric_Type()
)
mrdIFMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdIFMetric.setStatus("mandatory")


class _MrdIFThreshold_Type(Integer32):
    """Custom type mrdIFThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_MrdIFThreshold_Type.__name__ = "Integer32"
_MrdIFThreshold_Object = MibTableColumn
mrdIFThreshold = _MrdIFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 5, 1, 4),
    _MrdIFThreshold_Type()
)
mrdIFThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdIFThreshold.setStatus("mandatory")
_MrdIFRateLimit_Type = Integer32
_MrdIFRateLimit_Object = MibTableColumn
mrdIFRateLimit = _MrdIFRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 5, 1, 5),
    _MrdIFRateLimit_Type()
)
mrdIFRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdIFRateLimit.setStatus("mandatory")


class _MrdIFBoundary_Type(Integer32):
    """Custom type mrdIFBoundary based on Integer32"""
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


_MrdIFBoundary_Type.__name__ = "Integer32"
_MrdIFBoundary_Object = MibTableColumn
mrdIFBoundary = _MrdIFBoundary_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 5, 1, 6),
    _MrdIFBoundary_Type()
)
mrdIFBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdIFBoundary.setStatus("mandatory")


class _MrdIFAlternateNetwork_Type(Integer32):
    """Custom type mrdIFAlternateNetwork based on Integer32"""
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


_MrdIFAlternateNetwork_Type.__name__ = "Integer32"
_MrdIFAlternateNetwork_Object = MibTableColumn
mrdIFAlternateNetwork = _MrdIFAlternateNetwork_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 5, 1, 7),
    _MrdIFAlternateNetwork_Type()
)
mrdIFAlternateNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdIFAlternateNetwork.setStatus("mandatory")


class _MrdIFAdminState_Type(Integer32):
    """Custom type mrdIFAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("normal", 2))
    )


_MrdIFAdminState_Type.__name__ = "Integer32"
_MrdIFAdminState_Object = MibTableColumn
mrdIFAdminState = _MrdIFAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 5, 1, 8),
    _MrdIFAdminState_Type()
)
mrdIFAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdIFAdminState.setStatus("mandatory")
_MrdTunnelTable_Object = MibTable
mrdTunnelTable = _MrdTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    mrdTunnelTable.setStatus("mandatory")
_MrdTunnelEntry_Object = MibTableRow
mrdTunnelEntry = _MrdTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 6, 1)
)
mrdTunnelEntry.setIndexNames(
    (0, "MRD-MIB", "mrdLocalAddress"),
    (0, "MRD-MIB", "mrdRemoteAddress"),
)
if mibBuilder.loadTexts:
    mrdTunnelEntry.setStatus("mandatory")
_MrdLocalAddress_Type = IpAddress
_MrdLocalAddress_Object = MibTableColumn
mrdLocalAddress = _MrdLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 6, 1, 1),
    _MrdLocalAddress_Type()
)
mrdLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdLocalAddress.setStatus("mandatory")
_MrdRemoteAddress_Type = IpAddress
_MrdRemoteAddress_Object = MibTableColumn
mrdRemoteAddress = _MrdRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 6, 1, 2),
    _MrdRemoteAddress_Type()
)
mrdRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdRemoteAddress.setStatus("mandatory")


class _MrdTunnelMetric_Type(Integer32):
    """Custom type mrdTunnelMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_MrdTunnelMetric_Type.__name__ = "Integer32"
_MrdTunnelMetric_Object = MibTableColumn
mrdTunnelMetric = _MrdTunnelMetric_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 6, 1, 3),
    _MrdTunnelMetric_Type()
)
mrdTunnelMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdTunnelMetric.setStatus("mandatory")


class _MrdTunnelThreshold_Type(Integer32):
    """Custom type mrdTunnelThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_MrdTunnelThreshold_Type.__name__ = "Integer32"
_MrdTunnelThreshold_Object = MibTableColumn
mrdTunnelThreshold = _MrdTunnelThreshold_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 6, 1, 4),
    _MrdTunnelThreshold_Type()
)
mrdTunnelThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdTunnelThreshold.setStatus("mandatory")
_MrdTunnelRateLimit_Type = Integer32
_MrdTunnelRateLimit_Object = MibTableColumn
mrdTunnelRateLimit = _MrdTunnelRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 6, 1, 5),
    _MrdTunnelRateLimit_Type()
)
mrdTunnelRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdTunnelRateLimit.setStatus("mandatory")


class _MrdTunnelBoundary_Type(Integer32):
    """Custom type mrdTunnelBoundary based on Integer32"""
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


_MrdTunnelBoundary_Type.__name__ = "Integer32"
_MrdTunnelBoundary_Object = MibTableColumn
mrdTunnelBoundary = _MrdTunnelBoundary_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 6, 1, 6),
    _MrdTunnelBoundary_Type()
)
mrdTunnelBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdTunnelBoundary.setStatus("mandatory")


class _MrdTunnelAdminState_Type(Integer32):
    """Custom type mrdTunnelAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("normal", 2))
    )


_MrdTunnelAdminState_Type.__name__ = "Integer32"
_MrdTunnelAdminState_Object = MibTableColumn
mrdTunnelAdminState = _MrdTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 6, 1, 7),
    _MrdTunnelAdminState_Type()
)
mrdTunnelAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrdTunnelAdminState.setStatus("mandatory")
_MrdGroupTable_Object = MibTable
mrdGroupTable = _MrdGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7)
)
if mibBuilder.loadTexts:
    mrdGroupTable.setStatus("mandatory")
_MrdGroupEntry_Object = MibTableRow
mrdGroupEntry = _MrdGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7, 1)
)
mrdGroupEntry.setIndexNames(
    (0, "MRD-MIB", "mrdGroupID"),
    (0, "MRD-MIB", "mrdGroupVlanMask"),
    (0, "MRD-MIB", "mrdGroupSrcIP"),
)
if mibBuilder.loadTexts:
    mrdGroupEntry.setStatus("mandatory")
_MrdGroupID_Type = Integer32
_MrdGroupID_Object = MibTableColumn
mrdGroupID = _MrdGroupID_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7, 1, 1),
    _MrdGroupID_Type()
)
mrdGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupID.setStatus("mandatory")
_MrdGroupVlanMask_Type = Integer32
_MrdGroupVlanMask_Object = MibTableColumn
mrdGroupVlanMask = _MrdGroupVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7, 1, 2),
    _MrdGroupVlanMask_Type()
)
mrdGroupVlanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupVlanMask.setStatus("mandatory")
_MrdGroupSrcIP_Type = IpAddress
_MrdGroupSrcIP_Object = MibTableColumn
mrdGroupSrcIP = _MrdGroupSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7, 1, 3),
    _MrdGroupSrcIP_Type()
)
mrdGroupSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupSrcIP.setStatus("mandatory")
_MrdGroupSrcIPNet_Type = IpAddress
_MrdGroupSrcIPNet_Object = MibScalar
mrdGroupSrcIPNet = _MrdGroupSrcIPNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7, 1, 4),
    _MrdGroupSrcIPNet_Type()
)
mrdGroupSrcIPNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupSrcIPNet.setStatus("mandatory")
_MrdGroupSrcNetMask_Type = IpAddress
_MrdGroupSrcNetMask_Object = MibTableColumn
mrdGroupSrcNetMask = _MrdGroupSrcNetMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7, 1, 5),
    _MrdGroupSrcNetMask_Type()
)
mrdGroupSrcNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupSrcNetMask.setStatus("mandatory")
_MrdGroupMetric_Type = Integer32
_MrdGroupMetric_Object = MibTableColumn
mrdGroupMetric = _MrdGroupMetric_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7, 1, 6),
    _MrdGroupMetric_Type()
)
mrdGroupMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupMetric.setStatus("mandatory")
_MrdGroupThreshold_Type = Integer32
_MrdGroupThreshold_Object = MibTableColumn
mrdGroupThreshold = _MrdGroupThreshold_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7, 1, 7),
    _MrdGroupThreshold_Type()
)
mrdGroupThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupThreshold.setStatus("mandatory")
_MrdGroupRate_Type = Integer32
_MrdGroupRate_Object = MibTableColumn
mrdGroupRate = _MrdGroupRate_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7, 1, 8),
    _MrdGroupRate_Type()
)
mrdGroupRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupRate.setStatus("mandatory")
_MrdGroupPacketsIn_Type = Integer32
_MrdGroupPacketsIn_Object = MibTableColumn
mrdGroupPacketsIn = _MrdGroupPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7, 1, 9),
    _MrdGroupPacketsIn_Type()
)
mrdGroupPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupPacketsIn.setStatus("mandatory")
_MrdGroupPacketsOut_Type = Integer32
_MrdGroupPacketsOut_Object = MibTableColumn
mrdGroupPacketsOut = _MrdGroupPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7, 1, 10),
    _MrdGroupPacketsOut_Type()
)
mrdGroupPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupPacketsOut.setStatus("mandatory")


class _MrdGroupOneWayFlg_Type(Integer32):
    """Custom type mrdGroupOneWayFlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isNotOneWay", 2),
          ("isOneWay", 1))
    )


_MrdGroupOneWayFlg_Type.__name__ = "Integer32"
_MrdGroupOneWayFlg_Object = MibTableColumn
mrdGroupOneWayFlg = _MrdGroupOneWayFlg_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7, 1, 11),
    _MrdGroupOneWayFlg_Type()
)
mrdGroupOneWayFlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupOneWayFlg.setStatus("mandatory")


class _MrdGroupDownFlg_Type(Integer32):
    """Custom type mrdGroupDownFlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isDown", 1),
          ("isNotDown", 2))
    )


_MrdGroupDownFlg_Type.__name__ = "Integer32"
_MrdGroupDownFlg_Object = MibTableColumn
mrdGroupDownFlg = _MrdGroupDownFlg_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7, 1, 12),
    _MrdGroupDownFlg_Type()
)
mrdGroupDownFlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupDownFlg.setStatus("mandatory")


class _MrdGroupDisabledFlg_Type(Integer32):
    """Custom type mrdGroupDisabledFlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isDisabled", 1),
          ("isNotDisabled", 2))
    )


_MrdGroupDisabledFlg_Type.__name__ = "Integer32"
_MrdGroupDisabledFlg_Object = MibTableColumn
mrdGroupDisabledFlg = _MrdGroupDisabledFlg_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7, 1, 13),
    _MrdGroupDisabledFlg_Type()
)
mrdGroupDisabledFlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupDisabledFlg.setStatus("mandatory")


class _MrdGroupQuerierFlg_Type(Integer32):
    """Custom type mrdGroupQuerierFlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isNotQuerier", 2),
          ("isQuerier", 1))
    )


_MrdGroupQuerierFlg_Type.__name__ = "Integer32"
_MrdGroupQuerierFlg_Object = MibTableColumn
mrdGroupQuerierFlg = _MrdGroupQuerierFlg_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7, 1, 14),
    _MrdGroupQuerierFlg_Type()
)
mrdGroupQuerierFlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupQuerierFlg.setStatus("mandatory")


class _MrdGroupSrcRteFlg_Type(Integer32):
    """Custom type mrdGroupSrcRteFlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isNotSourceRouted", 2),
          ("isSourceRouted", 1))
    )


_MrdGroupSrcRteFlg_Type.__name__ = "Integer32"
_MrdGroupSrcRteFlg_Object = MibTableColumn
mrdGroupSrcRteFlg = _MrdGroupSrcRteFlg_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7, 1, 15),
    _MrdGroupSrcRteFlg_Type()
)
mrdGroupSrcRteFlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupSrcRteFlg.setStatus("mandatory")


class _MrdGroupLeafFlg_Type(Integer32):
    """Custom type mrdGroupLeafFlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isLeaf", 1),
          ("isNotLeaf", 2))
    )


_MrdGroupLeafFlg_Type.__name__ = "Integer32"
_MrdGroupLeafFlg_Object = MibTableColumn
mrdGroupLeafFlg = _MrdGroupLeafFlg_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7, 1, 16),
    _MrdGroupLeafFlg_Type()
)
mrdGroupLeafFlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupLeafFlg.setStatus("mandatory")


class _MrdGroupIgmpv1Flg_Type(Integer32):
    """Custom type mrdGroupIgmpv1Flg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isIgmpV1", 1),
          ("isNotIgmpV1", 2))
    )


_MrdGroupIgmpv1Flg_Type.__name__ = "Integer32"
_MrdGroupIgmpv1Flg_Object = MibTableColumn
mrdGroupIgmpv1Flg = _MrdGroupIgmpv1Flg_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 7, 1, 17),
    _MrdGroupIgmpv1Flg_Type()
)
mrdGroupIgmpv1Flg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupIgmpv1Flg.setStatus("mandatory")
_MrdTunnelListTable_Object = MibTable
mrdTunnelListTable = _MrdTunnelListTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 8)
)
if mibBuilder.loadTexts:
    mrdTunnelListTable.setStatus("mandatory")
_MrdTunnelListEntry_Object = MibTableRow
mrdTunnelListEntry = _MrdTunnelListEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 8, 1)
)
mrdTunnelListEntry.setIndexNames(
    (0, "MRD-MIB", "mrdTunnelListGrpID"),
    (0, "MRD-MIB", "mrdTunnelListVlanMask"),
    (0, "MRD-MIB", "mrdTunnelListSrcIP"),
    (0, "MRD-MIB", "mrdTunnelListDstIP"),
)
if mibBuilder.loadTexts:
    mrdTunnelListEntry.setStatus("mandatory")
_MrdTunnelListGrpID_Type = Integer32
_MrdTunnelListGrpID_Object = MibTableColumn
mrdTunnelListGrpID = _MrdTunnelListGrpID_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 8, 1, 1),
    _MrdTunnelListGrpID_Type()
)
mrdTunnelListGrpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdTunnelListGrpID.setStatus("mandatory")
_MrdTunnelListVlanMask_Type = Integer32
_MrdTunnelListVlanMask_Object = MibTableColumn
mrdTunnelListVlanMask = _MrdTunnelListVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 8, 1, 2),
    _MrdTunnelListVlanMask_Type()
)
mrdTunnelListVlanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdTunnelListVlanMask.setStatus("mandatory")
_MrdTunnelListSrcIP_Type = IpAddress
_MrdTunnelListSrcIP_Object = MibTableColumn
mrdTunnelListSrcIP = _MrdTunnelListSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 8, 1, 3),
    _MrdTunnelListSrcIP_Type()
)
mrdTunnelListSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdTunnelListSrcIP.setStatus("mandatory")
_MrdTunnelListDstIP_Type = IpAddress
_MrdTunnelListDstIP_Object = MibTableColumn
mrdTunnelListDstIP = _MrdTunnelListDstIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 8, 1, 4),
    _MrdTunnelListDstIP_Type()
)
mrdTunnelListDstIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdTunnelListDstIP.setStatus("mandatory")
_MrdTunnelListMetric_Type = Integer32
_MrdTunnelListMetric_Object = MibTableColumn
mrdTunnelListMetric = _MrdTunnelListMetric_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 8, 1, 5),
    _MrdTunnelListMetric_Type()
)
mrdTunnelListMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdTunnelListMetric.setStatus("mandatory")
_MrdTunnelListThreshold_Type = Integer32
_MrdTunnelListThreshold_Object = MibTableColumn
mrdTunnelListThreshold = _MrdTunnelListThreshold_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 8, 1, 6),
    _MrdTunnelListThreshold_Type()
)
mrdTunnelListThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdTunnelListThreshold.setStatus("mandatory")
_MrdTunnelListRate_Type = Integer32
_MrdTunnelListRate_Object = MibTableColumn
mrdTunnelListRate = _MrdTunnelListRate_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 8, 1, 7),
    _MrdTunnelListRate_Type()
)
mrdTunnelListRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdTunnelListRate.setStatus("mandatory")
_MrdTunnelListPacketsIn_Type = Integer32
_MrdTunnelListPacketsIn_Object = MibTableColumn
mrdTunnelListPacketsIn = _MrdTunnelListPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 8, 1, 8),
    _MrdTunnelListPacketsIn_Type()
)
mrdTunnelListPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdTunnelListPacketsIn.setStatus("mandatory")
_MrdTunnelListPacketsOut_Type = Integer32
_MrdTunnelListPacketsOut_Object = MibTableColumn
mrdTunnelListPacketsOut = _MrdTunnelListPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 8, 1, 9),
    _MrdTunnelListPacketsOut_Type()
)
mrdTunnelListPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdTunnelListPacketsOut.setStatus("mandatory")


class _MrdTunnelListOneWayFlg_Type(Integer32):
    """Custom type mrdTunnelListOneWayFlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isNotOneWay", 2),
          ("isOneWay", 1))
    )


_MrdTunnelListOneWayFlg_Type.__name__ = "Integer32"
_MrdTunnelListOneWayFlg_Object = MibTableColumn
mrdTunnelListOneWayFlg = _MrdTunnelListOneWayFlg_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 8, 1, 10),
    _MrdTunnelListOneWayFlg_Type()
)
mrdTunnelListOneWayFlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdTunnelListOneWayFlg.setStatus("mandatory")


class _MrdTunnelListDownFlg_Type(Integer32):
    """Custom type mrdTunnelListDownFlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isDown", 1),
          ("isNotDown", 2))
    )


_MrdTunnelListDownFlg_Type.__name__ = "Integer32"
_MrdTunnelListDownFlg_Object = MibTableColumn
mrdTunnelListDownFlg = _MrdTunnelListDownFlg_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 8, 1, 11),
    _MrdTunnelListDownFlg_Type()
)
mrdTunnelListDownFlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdTunnelListDownFlg.setStatus("mandatory")


class _MrdTunnelListDisabledFlg_Type(Integer32):
    """Custom type mrdTunnelListDisabledFlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isDisabled", 1),
          ("isNotDisabled", 2))
    )


_MrdTunnelListDisabledFlg_Type.__name__ = "Integer32"
_MrdTunnelListDisabledFlg_Object = MibTableColumn
mrdTunnelListDisabledFlg = _MrdTunnelListDisabledFlg_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 8, 1, 12),
    _MrdTunnelListDisabledFlg_Type()
)
mrdTunnelListDisabledFlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdTunnelListDisabledFlg.setStatus("mandatory")


class _MrdTunnelListQuerierFlg_Type(Integer32):
    """Custom type mrdTunnelListQuerierFlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isNotQuerier", 2),
          ("isQuerier", 1))
    )


_MrdTunnelListQuerierFlg_Type.__name__ = "Integer32"
_MrdTunnelListQuerierFlg_Object = MibTableColumn
mrdTunnelListQuerierFlg = _MrdTunnelListQuerierFlg_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 8, 1, 13),
    _MrdTunnelListQuerierFlg_Type()
)
mrdTunnelListQuerierFlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdTunnelListQuerierFlg.setStatus("mandatory")


class _MrdTunnelListSrcRteFlg_Type(Integer32):
    """Custom type mrdTunnelListSrcRteFlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isNotSourceRouted", 2),
          ("isSourceRouted", 1))
    )


_MrdTunnelListSrcRteFlg_Type.__name__ = "Integer32"
_MrdTunnelListSrcRteFlg_Object = MibTableColumn
mrdTunnelListSrcRteFlg = _MrdTunnelListSrcRteFlg_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 8, 1, 14),
    _MrdTunnelListSrcRteFlg_Type()
)
mrdTunnelListSrcRteFlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdTunnelListSrcRteFlg.setStatus("mandatory")


class _MrdTunnelListLeafFlg_Type(Integer32):
    """Custom type mrdTunnelListLeafFlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isLeaf", 1),
          ("isNotLeaf", 2))
    )


_MrdTunnelListLeafFlg_Type.__name__ = "Integer32"
_MrdTunnelListLeafFlg_Object = MibTableColumn
mrdTunnelListLeafFlg = _MrdTunnelListLeafFlg_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 8, 1, 15),
    _MrdTunnelListLeafFlg_Type()
)
mrdTunnelListLeafFlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdTunnelListLeafFlg.setStatus("mandatory")


class _MrdTunnelListIgmpv1Flg_Type(Integer32):
    """Custom type mrdTunnelListIgmpv1Flg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isIgmpV1", 1),
          ("isNotIgmpV1", 2))
    )


_MrdTunnelListIgmpv1Flg_Type.__name__ = "Integer32"
_MrdTunnelListIgmpv1Flg_Object = MibTableColumn
mrdTunnelListIgmpv1Flg = _MrdTunnelListIgmpv1Flg_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 8, 1, 16),
    _MrdTunnelListIgmpv1Flg_Type()
)
mrdTunnelListIgmpv1Flg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdTunnelListIgmpv1Flg.setStatus("mandatory")
_MrdPeerTable_Object = MibTable
mrdPeerTable = _MrdPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 9)
)
if mibBuilder.loadTexts:
    mrdPeerTable.setStatus("mandatory")
_MrdPeerEntry_Object = MibTableRow
mrdPeerEntry = _MrdPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 9, 1)
)
mrdPeerEntry.setIndexNames(
    (0, "MRD-MIB", "mrdPeerGrpID"),
    (0, "MRD-MIB", "mrdPeerVlanMask"),
    (0, "MRD-MIB", "mrdPeerSrcIP"),
    (0, "MRD-MIB", "mrdPeerPeerIP"),
)
if mibBuilder.loadTexts:
    mrdPeerEntry.setStatus("mandatory")
_MrdPeerGrpID_Type = Integer32
_MrdPeerGrpID_Object = MibTableColumn
mrdPeerGrpID = _MrdPeerGrpID_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 9, 1, 1),
    _MrdPeerGrpID_Type()
)
mrdPeerGrpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdPeerGrpID.setStatus("mandatory")
_MrdPeerVlanMask_Type = Integer32
_MrdPeerVlanMask_Object = MibTableColumn
mrdPeerVlanMask = _MrdPeerVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 9, 1, 2),
    _MrdPeerVlanMask_Type()
)
mrdPeerVlanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdPeerVlanMask.setStatus("mandatory")
_MrdPeerSrcIP_Type = IpAddress
_MrdPeerSrcIP_Object = MibTableColumn
mrdPeerSrcIP = _MrdPeerSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 9, 1, 3),
    _MrdPeerSrcIP_Type()
)
mrdPeerSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdPeerSrcIP.setStatus("mandatory")
_MrdPeerPeerIP_Type = IpAddress
_MrdPeerPeerIP_Object = MibTableColumn
mrdPeerPeerIP = _MrdPeerPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 9, 1, 4),
    _MrdPeerPeerIP_Type()
)
mrdPeerPeerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdPeerPeerIP.setStatus("mandatory")
_MrdPeerMajorLevel_Type = Integer32
_MrdPeerMajorLevel_Object = MibTableColumn
mrdPeerMajorLevel = _MrdPeerMajorLevel_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 9, 1, 5),
    _MrdPeerMajorLevel_Type()
)
mrdPeerMajorLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdPeerMajorLevel.setStatus("mandatory")
_MrdPeerMinorLevel_Type = Integer32
_MrdPeerMinorLevel_Object = MibTableColumn
mrdPeerMinorLevel = _MrdPeerMinorLevel_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 9, 1, 6),
    _MrdPeerMinorLevel_Type()
)
mrdPeerMinorLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdPeerMinorLevel.setStatus("mandatory")
_MrdPeerTimer_Type = Integer32
_MrdPeerTimer_Object = MibTableColumn
mrdPeerTimer = _MrdPeerTimer_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 9, 1, 7),
    _MrdPeerTimer_Type()
)
mrdPeerTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdPeerTimer.setStatus("mandatory")
_MrdPeerFlags_Type = Integer32
_MrdPeerFlags_Object = MibTableColumn
mrdPeerFlags = _MrdPeerFlags_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 9, 1, 8),
    _MrdPeerFlags_Type()
)
mrdPeerFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdPeerFlags.setStatus("mandatory")


class _MrdPeerLeafFlag_Type(Integer32):
    """Custom type mrdPeerLeafFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isALeaf", 1),
          ("isNotALeaf", 2))
    )


_MrdPeerLeafFlag_Type.__name__ = "Integer32"
_MrdPeerLeafFlag_Object = MibTableColumn
mrdPeerLeafFlag = _MrdPeerLeafFlag_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 9, 1, 9),
    _MrdPeerLeafFlag_Type()
)
mrdPeerLeafFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdPeerLeafFlag.setStatus("mandatory")


class _MrdPeerPruneFlag_Type(Integer32):
    """Custom type mrdPeerPruneFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isAPruningRouter", 1),
          ("isNotAPruningRouter", 2))
    )


_MrdPeerPruneFlag_Type.__name__ = "Integer32"
_MrdPeerPruneFlag_Object = MibTableColumn
mrdPeerPruneFlag = _MrdPeerPruneFlag_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 9, 1, 10),
    _MrdPeerPruneFlag_Type()
)
mrdPeerPruneFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdPeerPruneFlag.setStatus("mandatory")


class _MrdPeerGenIdFlag_Type(Integer32):
    """Custom type mrdPeerGenIdFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isIncludingGenID", 1),
          ("isNotIncludingGenID", 2))
    )


_MrdPeerGenIdFlag_Type.__name__ = "Integer32"
_MrdPeerGenIdFlag_Object = MibTableColumn
mrdPeerGenIdFlag = _MrdPeerGenIdFlag_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 9, 1, 11),
    _MrdPeerGenIdFlag_Type()
)
mrdPeerGenIdFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdPeerGenIdFlag.setStatus("mandatory")


class _MrdPeerMtraceFlag_Type(Integer32):
    """Custom type mrdPeerMtraceFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isNotSupportingMtrace", 2),
          ("isSupportingMtrace", 1))
    )


_MrdPeerMtraceFlag_Type.__name__ = "Integer32"
_MrdPeerMtraceFlag_Object = MibTableColumn
mrdPeerMtraceFlag = _MrdPeerMtraceFlag_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 9, 1, 12),
    _MrdPeerMtraceFlag_Type()
)
mrdPeerMtraceFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdPeerMtraceFlag.setStatus("mandatory")
_MrdAltNetList_Object = MibTable
mrdAltNetList = _MrdAltNetList_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    mrdAltNetList.setStatus("mandatory")
_MrdAltNetListEntry_Object = MibTableRow
mrdAltNetListEntry = _MrdAltNetListEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 10, 1)
)
mrdAltNetListEntry.setIndexNames(
    (0, "MRD-MIB", "mrdAltNetListGrpID"),
    (0, "MRD-MIB", "mrdAltNetListVlanMask"),
    (0, "MRD-MIB", "mrdAltNetListSrcIP"),
    (0, "MRD-MIB", "mrdAltNetListAltNetIP"),
)
if mibBuilder.loadTexts:
    mrdAltNetListEntry.setStatus("mandatory")
_MrdAltNetListGrpID_Type = Integer32
_MrdAltNetListGrpID_Object = MibTableColumn
mrdAltNetListGrpID = _MrdAltNetListGrpID_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 10, 1, 1),
    _MrdAltNetListGrpID_Type()
)
mrdAltNetListGrpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdAltNetListGrpID.setStatus("mandatory")
_MrdAltNetListVlanMask_Type = Integer32
_MrdAltNetListVlanMask_Object = MibTableColumn
mrdAltNetListVlanMask = _MrdAltNetListVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 10, 1, 2),
    _MrdAltNetListVlanMask_Type()
)
mrdAltNetListVlanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdAltNetListVlanMask.setStatus("mandatory")
_MrdAltNetListSrcIP_Type = IpAddress
_MrdAltNetListSrcIP_Object = MibTableColumn
mrdAltNetListSrcIP = _MrdAltNetListSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 10, 1, 3),
    _MrdAltNetListSrcIP_Type()
)
mrdAltNetListSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdAltNetListSrcIP.setStatus("mandatory")
_MrdAltNetListAltNetIP_Type = IpAddress
_MrdAltNetListAltNetIP_Object = MibTableColumn
mrdAltNetListAltNetIP = _MrdAltNetListAltNetIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 10, 1, 4),
    _MrdAltNetListAltNetIP_Type()
)
mrdAltNetListAltNetIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdAltNetListAltNetIP.setStatus("mandatory")
_MrdAltNetListAltNetNetMask_Type = IpAddress
_MrdAltNetListAltNetNetMask_Object = MibTableColumn
mrdAltNetListAltNetNetMask = _MrdAltNetListAltNetNetMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 10, 1, 5),
    _MrdAltNetListAltNetNetMask_Type()
)
mrdAltNetListAltNetNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdAltNetListAltNetNetMask.setStatus("mandatory")
_MrdBoundaryList_Object = MibTable
mrdBoundaryList = _MrdBoundaryList_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 11)
)
if mibBuilder.loadTexts:
    mrdBoundaryList.setStatus("mandatory")
_MrdBoundaryListEntry_Object = MibTableRow
mrdBoundaryListEntry = _MrdBoundaryListEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 11, 1)
)
mrdBoundaryListEntry.setIndexNames(
    (0, "MRD-MIB", "mrdBoundaryListGrpID"),
    (0, "MRD-MIB", "mrdBoundaryListVlanMask"),
    (0, "MRD-MIB", "mrdBoundaryListSrcIP"),
    (0, "MRD-MIB", "mrdBoundaryListBoundaryIP"),
)
if mibBuilder.loadTexts:
    mrdBoundaryListEntry.setStatus("mandatory")
_MrdBoundaryListGrpID_Type = Integer32
_MrdBoundaryListGrpID_Object = MibTableColumn
mrdBoundaryListGrpID = _MrdBoundaryListGrpID_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 11, 1, 1),
    _MrdBoundaryListGrpID_Type()
)
mrdBoundaryListGrpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdBoundaryListGrpID.setStatus("mandatory")
_MrdBoundaryListVlanMask_Type = Integer32
_MrdBoundaryListVlanMask_Object = MibTableColumn
mrdBoundaryListVlanMask = _MrdBoundaryListVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 11, 1, 2),
    _MrdBoundaryListVlanMask_Type()
)
mrdBoundaryListVlanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdBoundaryListVlanMask.setStatus("mandatory")
_MrdBoundaryListSrcIP_Type = IpAddress
_MrdBoundaryListSrcIP_Object = MibTableColumn
mrdBoundaryListSrcIP = _MrdBoundaryListSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 11, 1, 3),
    _MrdBoundaryListSrcIP_Type()
)
mrdBoundaryListSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdBoundaryListSrcIP.setStatus("mandatory")
_MrdBoundaryListBoundaryIP_Type = IpAddress
_MrdBoundaryListBoundaryIP_Object = MibTableColumn
mrdBoundaryListBoundaryIP = _MrdBoundaryListBoundaryIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 11, 1, 4),
    _MrdBoundaryListBoundaryIP_Type()
)
mrdBoundaryListBoundaryIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdBoundaryListBoundaryIP.setStatus("mandatory")
_MrdBoundaryListBoundaryNetMask_Type = IpAddress
_MrdBoundaryListBoundaryNetMask_Object = MibTableColumn
mrdBoundaryListBoundaryNetMask = _MrdBoundaryListBoundaryNetMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 11, 1, 5),
    _MrdBoundaryListBoundaryNetMask_Type()
)
mrdBoundaryListBoundaryNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdBoundaryListBoundaryNetMask.setStatus("mandatory")
_MrdGroupMemTable_Object = MibTable
mrdGroupMemTable = _MrdGroupMemTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 12)
)
if mibBuilder.loadTexts:
    mrdGroupMemTable.setStatus("mandatory")
_MrdGroupMemEntry_Object = MibTableRow
mrdGroupMemEntry = _MrdGroupMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 12, 1)
)
mrdGroupMemEntry.setIndexNames(
    (0, "MRD-MIB", "mrdGroupMemGrpID"),
    (0, "MRD-MIB", "mrdGroupMemVlanMask"),
    (0, "MRD-MIB", "mrdGroupMemSrcIP"),
    (0, "MRD-MIB", "mrdGroupMemIP"),
)
if mibBuilder.loadTexts:
    mrdGroupMemEntry.setStatus("mandatory")
_MrdGroupMemGrpID_Type = Integer32
_MrdGroupMemGrpID_Object = MibTableColumn
mrdGroupMemGrpID = _MrdGroupMemGrpID_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 12, 1, 1),
    _MrdGroupMemGrpID_Type()
)
mrdGroupMemGrpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupMemGrpID.setStatus("mandatory")
_MrdGroupMemVlanMask_Type = Integer32
_MrdGroupMemVlanMask_Object = MibTableColumn
mrdGroupMemVlanMask = _MrdGroupMemVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 12, 1, 2),
    _MrdGroupMemVlanMask_Type()
)
mrdGroupMemVlanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupMemVlanMask.setStatus("mandatory")
_MrdGroupMemSrcIP_Type = IpAddress
_MrdGroupMemSrcIP_Object = MibTableColumn
mrdGroupMemSrcIP = _MrdGroupMemSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 12, 1, 3),
    _MrdGroupMemSrcIP_Type()
)
mrdGroupMemSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupMemSrcIP.setStatus("mandatory")
_MrdGroupMemIP_Type = IpAddress
_MrdGroupMemIP_Object = MibTableColumn
mrdGroupMemIP = _MrdGroupMemIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 12, 1, 4),
    _MrdGroupMemIP_Type()
)
mrdGroupMemIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupMemIP.setStatus("mandatory")
_MrdGroupMemTimer_Type = Integer32
_MrdGroupMemTimer_Object = MibTableColumn
mrdGroupMemTimer = _MrdGroupMemTimer_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 12, 1, 5),
    _MrdGroupMemTimer_Type()
)
mrdGroupMemTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdGroupMemTimer.setStatus("mandatory")
_MrdForwardingTable_Object = MibTable
mrdForwardingTable = _MrdForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 13)
)
if mibBuilder.loadTexts:
    mrdForwardingTable.setStatus("mandatory")
_MrdForwardingEntry_Object = MibTableRow
mrdForwardingEntry = _MrdForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 13, 1)
)
mrdForwardingEntry.setIndexNames(
    (0, "MRD-MIB", "mrdForwardingSrcIP"),
    (0, "MRD-MIB", "mrdForwardingDstIP"),
    (0, "MRD-MIB", "mrdForwardingGrpID"),
    (0, "MRD-MIB", "mrdForwardingVlanMask"),
)
if mibBuilder.loadTexts:
    mrdForwardingEntry.setStatus("mandatory")
_MrdForwardingSrcIP_Type = IpAddress
_MrdForwardingSrcIP_Object = MibTableColumn
mrdForwardingSrcIP = _MrdForwardingSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 13, 1, 1),
    _MrdForwardingSrcIP_Type()
)
mrdForwardingSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdForwardingSrcIP.setStatus("mandatory")
_MrdForwardingDstIP_Type = IpAddress
_MrdForwardingDstIP_Object = MibTableColumn
mrdForwardingDstIP = _MrdForwardingDstIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 13, 1, 2),
    _MrdForwardingDstIP_Type()
)
mrdForwardingDstIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdForwardingDstIP.setStatus("mandatory")
_MrdForwardingGrpID_Type = Integer32
_MrdForwardingGrpID_Object = MibTableColumn
mrdForwardingGrpID = _MrdForwardingGrpID_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 13, 1, 3),
    _MrdForwardingGrpID_Type()
)
mrdForwardingGrpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdForwardingGrpID.setStatus("mandatory")
_MrdForwardingVlanMask_Type = Integer32
_MrdForwardingVlanMask_Object = MibTableColumn
mrdForwardingVlanMask = _MrdForwardingVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 13, 1, 4),
    _MrdForwardingVlanMask_Type()
)
mrdForwardingVlanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdForwardingVlanMask.setStatus("mandatory")
_MrdForwardingSrcGrpID_Type = Integer32
_MrdForwardingSrcGrpID_Object = MibTableColumn
mrdForwardingSrcGrpID = _MrdForwardingSrcGrpID_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 13, 1, 5),
    _MrdForwardingSrcGrpID_Type()
)
mrdForwardingSrcGrpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdForwardingSrcGrpID.setStatus("mandatory")
_MrdForwardingSrcVlanMask_Type = Integer32
_MrdForwardingSrcVlanMask_Object = MibTableColumn
mrdForwardingSrcVlanMask = _MrdForwardingSrcVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 13, 1, 6),
    _MrdForwardingSrcVlanMask_Type()
)
mrdForwardingSrcVlanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdForwardingSrcVlanMask.setStatus("mandatory")
_MrdPruneTable_Object = MibTable
mrdPruneTable = _MrdPruneTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 14)
)
if mibBuilder.loadTexts:
    mrdPruneTable.setStatus("mandatory")
_MrdPruneEntry_Object = MibTableRow
mrdPruneEntry = _MrdPruneEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 14, 1)
)
mrdPruneEntry.setIndexNames(
    (0, "MRD-MIB", "mrdPruneDstGroup"),
    (0, "MRD-MIB", "mrdPrunePruningRouter"),
)
if mibBuilder.loadTexts:
    mrdPruneEntry.setStatus("mandatory")
_MrdPruneDstGroup_Type = IpAddress
_MrdPruneDstGroup_Object = MibTableColumn
mrdPruneDstGroup = _MrdPruneDstGroup_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 14, 1, 1),
    _MrdPruneDstGroup_Type()
)
mrdPruneDstGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdPruneDstGroup.setStatus("mandatory")
_MrdPrunePruningRouter_Type = IpAddress
_MrdPrunePruningRouter_Object = MibTableColumn
mrdPrunePruningRouter = _MrdPrunePruningRouter_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 14, 1, 2),
    _MrdPrunePruningRouter_Type()
)
mrdPrunePruningRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdPrunePruningRouter.setStatus("mandatory")
_MrdPruneGrpID_Type = Integer32
_MrdPruneGrpID_Object = MibTableColumn
mrdPruneGrpID = _MrdPruneGrpID_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 14, 1, 3),
    _MrdPruneGrpID_Type()
)
mrdPruneGrpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdPruneGrpID.setStatus("mandatory")
_MrdPruneVlanMask_Type = Integer32
_MrdPruneVlanMask_Object = MibTableColumn
mrdPruneVlanMask = _MrdPruneVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 14, 1, 4),
    _MrdPruneVlanMask_Type()
)
mrdPruneVlanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdPruneVlanMask.setStatus("mandatory")
_MrdPruneTimer_Type = Integer32
_MrdPruneTimer_Object = MibTableColumn
mrdPruneTimer = _MrdPruneTimer_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 14, 1, 5),
    _MrdPruneTimer_Type()
)
mrdPruneTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdPruneTimer.setStatus("mandatory")
_MrdRouteTable_Object = MibTable
mrdRouteTable = _MrdRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 15)
)
if mibBuilder.loadTexts:
    mrdRouteTable.setStatus("mandatory")
_MrdRouteEntry_Object = MibTableRow
mrdRouteEntry = _MrdRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 15, 1)
)
mrdRouteEntry.setIndexNames(
    (0, "MRD-MIB", "mrdRouteOriginIP"),
    (0, "MRD-MIB", "mrdRouteGatewayIP"),
    (0, "MRD-MIB", "mrdRouteGrpID"),
    (0, "MRD-MIB", "mrdRouteVlanMask"),
    (0, "MRD-MIB", "mrdRouteTunFlag"),
)
if mibBuilder.loadTexts:
    mrdRouteEntry.setStatus("mandatory")
_MrdRouteOriginIP_Type = IpAddress
_MrdRouteOriginIP_Object = MibTableColumn
mrdRouteOriginIP = _MrdRouteOriginIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 15, 1, 1),
    _MrdRouteOriginIP_Type()
)
mrdRouteOriginIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdRouteOriginIP.setStatus("mandatory")
_MrdRouteOriginMask_Type = IpAddress
_MrdRouteOriginMask_Object = MibTableColumn
mrdRouteOriginMask = _MrdRouteOriginMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 15, 1, 2),
    _MrdRouteOriginMask_Type()
)
mrdRouteOriginMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdRouteOriginMask.setStatus("mandatory")
_MrdRouteGatewayIP_Type = IpAddress
_MrdRouteGatewayIP_Object = MibTableColumn
mrdRouteGatewayIP = _MrdRouteGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 15, 1, 3),
    _MrdRouteGatewayIP_Type()
)
mrdRouteGatewayIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdRouteGatewayIP.setStatus("mandatory")
_MrdRouteGrpID_Type = Integer32
_MrdRouteGrpID_Object = MibTableColumn
mrdRouteGrpID = _MrdRouteGrpID_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 15, 1, 4),
    _MrdRouteGrpID_Type()
)
mrdRouteGrpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdRouteGrpID.setStatus("mandatory")
_MrdRouteVlanMask_Type = Integer32
_MrdRouteVlanMask_Object = MibTableColumn
mrdRouteVlanMask = _MrdRouteVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 15, 1, 5),
    _MrdRouteVlanMask_Type()
)
mrdRouteVlanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdRouteVlanMask.setStatus("mandatory")


class _MrdRouteLeafFlag_Type(Integer32):
    """Custom type mrdRouteLeafFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isLeaf", 1),
          ("isNotLeaf", 2))
    )


_MrdRouteLeafFlag_Type.__name__ = "Integer32"
_MrdRouteLeafFlag_Object = MibTableColumn
mrdRouteLeafFlag = _MrdRouteLeafFlag_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 15, 1, 6),
    _MrdRouteLeafFlag_Type()
)
mrdRouteLeafFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdRouteLeafFlag.setStatus("mandatory")


class _MrdRouteTunFlag_Type(Integer32):
    """Custom type mrdRouteTunFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isNotTunnel", 2),
          ("isTunnel", 1))
    )


_MrdRouteTunFlag_Type.__name__ = "Integer32"
_MrdRouteTunFlag_Object = MibTableColumn
mrdRouteTunFlag = _MrdRouteTunFlag_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 15, 1, 7),
    _MrdRouteTunFlag_Type()
)
mrdRouteTunFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdRouteTunFlag.setStatus("mandatory")
_MrdRouteSrcGrpID_Type = Integer32
_MrdRouteSrcGrpID_Object = MibTableColumn
mrdRouteSrcGrpID = _MrdRouteSrcGrpID_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 15, 1, 8),
    _MrdRouteSrcGrpID_Type()
)
mrdRouteSrcGrpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdRouteSrcGrpID.setStatus("mandatory")
_MrdRouteSrcVlanMask_Type = Integer32
_MrdRouteSrcVlanMask_Object = MibTableColumn
mrdRouteSrcVlanMask = _MrdRouteSrcVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 15, 1, 9),
    _MrdRouteSrcVlanMask_Type()
)
mrdRouteSrcVlanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdRouteSrcVlanMask.setStatus("mandatory")
_MrdRouteMetric_Type = Integer32
_MrdRouteMetric_Object = MibTableColumn
mrdRouteMetric = _MrdRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 15, 1, 10),
    _MrdRouteMetric_Type()
)
mrdRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdRouteMetric.setStatus("mandatory")
_MrdRouteTimer_Type = Integer32
_MrdRouteTimer_Object = MibTableColumn
mrdRouteTimer = _MrdRouteTimer_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3, 1, 1, 15, 1, 11),
    _MrdRouteTimer_Type()
)
mrdRouteTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrdRouteTimer.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MRD-MIB",
    **{"DisplayString": DisplayString,
       "mrdMIB": mrdMIB,
       "mrdMIBObjects": mrdMIBObjects,
       "mrdGeneralGroup": mrdGeneralGroup,
       "mrdVersion": mrdVersion,
       "mrdCachedRouteResTime": mrdCachedRouteResTime,
       "mrdPruneFlag": mrdPruneFlag,
       "mrdConfigUpdate": mrdConfigUpdate,
       "mrdEnableDisable": mrdEnableDisable,
       "mrdIntfBoundaryTable": mrdIntfBoundaryTable,
       "mrdIntfBoundaryEntry": mrdIntfBoundaryEntry,
       "mrdIntfPhyIntAddr": mrdIntfPhyIntAddr,
       "mrdIntfScopedAddress": mrdIntfScopedAddress,
       "mrdIntfBoundMaskLength": mrdIntfBoundMaskLength,
       "mrdIntfAdminState": mrdIntfAdminState,
       "mrdTunBoundaryTable": mrdTunBoundaryTable,
       "mrdTunBoundaryEntry": mrdTunBoundaryEntry,
       "mrdTunLocalAddress": mrdTunLocalAddress,
       "mrdTunRemoteAddress": mrdTunRemoteAddress,
       "mrdTunScopedAddress": mrdTunScopedAddress,
       "mrdTunBoundMaskLength": mrdTunBoundMaskLength,
       "mrdTunAdminState": mrdTunAdminState,
       "mrdAltNetTable": mrdAltNetTable,
       "mrdAltNetEntry": mrdAltNetEntry,
       "mrdAltNetAddr": mrdAltNetAddr,
       "mrdNetworkAddress": mrdNetworkAddress,
       "mrdANetMaskLength": mrdANetMaskLength,
       "mrdANetAdminState": mrdANetAdminState,
       "mrdInterfaceTable": mrdInterfaceTable,
       "mrdInterfaceEntry": mrdInterfaceEntry,
       "mrdIFAddress": mrdIFAddress,
       "mrdIFEnabledFlag": mrdIFEnabledFlag,
       "mrdIFMetric": mrdIFMetric,
       "mrdIFThreshold": mrdIFThreshold,
       "mrdIFRateLimit": mrdIFRateLimit,
       "mrdIFBoundary": mrdIFBoundary,
       "mrdIFAlternateNetwork": mrdIFAlternateNetwork,
       "mrdIFAdminState": mrdIFAdminState,
       "mrdTunnelTable": mrdTunnelTable,
       "mrdTunnelEntry": mrdTunnelEntry,
       "mrdLocalAddress": mrdLocalAddress,
       "mrdRemoteAddress": mrdRemoteAddress,
       "mrdTunnelMetric": mrdTunnelMetric,
       "mrdTunnelThreshold": mrdTunnelThreshold,
       "mrdTunnelRateLimit": mrdTunnelRateLimit,
       "mrdTunnelBoundary": mrdTunnelBoundary,
       "mrdTunnelAdminState": mrdTunnelAdminState,
       "mrdGroupTable": mrdGroupTable,
       "mrdGroupEntry": mrdGroupEntry,
       "mrdGroupID": mrdGroupID,
       "mrdGroupVlanMask": mrdGroupVlanMask,
       "mrdGroupSrcIP": mrdGroupSrcIP,
       "mrdGroupSrcIPNet": mrdGroupSrcIPNet,
       "mrdGroupSrcNetMask": mrdGroupSrcNetMask,
       "mrdGroupMetric": mrdGroupMetric,
       "mrdGroupThreshold": mrdGroupThreshold,
       "mrdGroupRate": mrdGroupRate,
       "mrdGroupPacketsIn": mrdGroupPacketsIn,
       "mrdGroupPacketsOut": mrdGroupPacketsOut,
       "mrdGroupOneWayFlg": mrdGroupOneWayFlg,
       "mrdGroupDownFlg": mrdGroupDownFlg,
       "mrdGroupDisabledFlg": mrdGroupDisabledFlg,
       "mrdGroupQuerierFlg": mrdGroupQuerierFlg,
       "mrdGroupSrcRteFlg": mrdGroupSrcRteFlg,
       "mrdGroupLeafFlg": mrdGroupLeafFlg,
       "mrdGroupIgmpv1Flg": mrdGroupIgmpv1Flg,
       "mrdTunnelListTable": mrdTunnelListTable,
       "mrdTunnelListEntry": mrdTunnelListEntry,
       "mrdTunnelListGrpID": mrdTunnelListGrpID,
       "mrdTunnelListVlanMask": mrdTunnelListVlanMask,
       "mrdTunnelListSrcIP": mrdTunnelListSrcIP,
       "mrdTunnelListDstIP": mrdTunnelListDstIP,
       "mrdTunnelListMetric": mrdTunnelListMetric,
       "mrdTunnelListThreshold": mrdTunnelListThreshold,
       "mrdTunnelListRate": mrdTunnelListRate,
       "mrdTunnelListPacketsIn": mrdTunnelListPacketsIn,
       "mrdTunnelListPacketsOut": mrdTunnelListPacketsOut,
       "mrdTunnelListOneWayFlg": mrdTunnelListOneWayFlg,
       "mrdTunnelListDownFlg": mrdTunnelListDownFlg,
       "mrdTunnelListDisabledFlg": mrdTunnelListDisabledFlg,
       "mrdTunnelListQuerierFlg": mrdTunnelListQuerierFlg,
       "mrdTunnelListSrcRteFlg": mrdTunnelListSrcRteFlg,
       "mrdTunnelListLeafFlg": mrdTunnelListLeafFlg,
       "mrdTunnelListIgmpv1Flg": mrdTunnelListIgmpv1Flg,
       "mrdPeerTable": mrdPeerTable,
       "mrdPeerEntry": mrdPeerEntry,
       "mrdPeerGrpID": mrdPeerGrpID,
       "mrdPeerVlanMask": mrdPeerVlanMask,
       "mrdPeerSrcIP": mrdPeerSrcIP,
       "mrdPeerPeerIP": mrdPeerPeerIP,
       "mrdPeerMajorLevel": mrdPeerMajorLevel,
       "mrdPeerMinorLevel": mrdPeerMinorLevel,
       "mrdPeerTimer": mrdPeerTimer,
       "mrdPeerFlags": mrdPeerFlags,
       "mrdPeerLeafFlag": mrdPeerLeafFlag,
       "mrdPeerPruneFlag": mrdPeerPruneFlag,
       "mrdPeerGenIdFlag": mrdPeerGenIdFlag,
       "mrdPeerMtraceFlag": mrdPeerMtraceFlag,
       "mrdAltNetList": mrdAltNetList,
       "mrdAltNetListEntry": mrdAltNetListEntry,
       "mrdAltNetListGrpID": mrdAltNetListGrpID,
       "mrdAltNetListVlanMask": mrdAltNetListVlanMask,
       "mrdAltNetListSrcIP": mrdAltNetListSrcIP,
       "mrdAltNetListAltNetIP": mrdAltNetListAltNetIP,
       "mrdAltNetListAltNetNetMask": mrdAltNetListAltNetNetMask,
       "mrdBoundaryList": mrdBoundaryList,
       "mrdBoundaryListEntry": mrdBoundaryListEntry,
       "mrdBoundaryListGrpID": mrdBoundaryListGrpID,
       "mrdBoundaryListVlanMask": mrdBoundaryListVlanMask,
       "mrdBoundaryListSrcIP": mrdBoundaryListSrcIP,
       "mrdBoundaryListBoundaryIP": mrdBoundaryListBoundaryIP,
       "mrdBoundaryListBoundaryNetMask": mrdBoundaryListBoundaryNetMask,
       "mrdGroupMemTable": mrdGroupMemTable,
       "mrdGroupMemEntry": mrdGroupMemEntry,
       "mrdGroupMemGrpID": mrdGroupMemGrpID,
       "mrdGroupMemVlanMask": mrdGroupMemVlanMask,
       "mrdGroupMemSrcIP": mrdGroupMemSrcIP,
       "mrdGroupMemIP": mrdGroupMemIP,
       "mrdGroupMemTimer": mrdGroupMemTimer,
       "mrdForwardingTable": mrdForwardingTable,
       "mrdForwardingEntry": mrdForwardingEntry,
       "mrdForwardingSrcIP": mrdForwardingSrcIP,
       "mrdForwardingDstIP": mrdForwardingDstIP,
       "mrdForwardingGrpID": mrdForwardingGrpID,
       "mrdForwardingVlanMask": mrdForwardingVlanMask,
       "mrdForwardingSrcGrpID": mrdForwardingSrcGrpID,
       "mrdForwardingSrcVlanMask": mrdForwardingSrcVlanMask,
       "mrdPruneTable": mrdPruneTable,
       "mrdPruneEntry": mrdPruneEntry,
       "mrdPruneDstGroup": mrdPruneDstGroup,
       "mrdPrunePruningRouter": mrdPrunePruningRouter,
       "mrdPruneGrpID": mrdPruneGrpID,
       "mrdPruneVlanMask": mrdPruneVlanMask,
       "mrdPruneTimer": mrdPruneTimer,
       "mrdRouteTable": mrdRouteTable,
       "mrdRouteEntry": mrdRouteEntry,
       "mrdRouteOriginIP": mrdRouteOriginIP,
       "mrdRouteOriginMask": mrdRouteOriginMask,
       "mrdRouteGatewayIP": mrdRouteGatewayIP,
       "mrdRouteGrpID": mrdRouteGrpID,
       "mrdRouteVlanMask": mrdRouteVlanMask,
       "mrdRouteLeafFlag": mrdRouteLeafFlag,
       "mrdRouteTunFlag": mrdRouteTunFlag,
       "mrdRouteSrcGrpID": mrdRouteSrcGrpID,
       "mrdRouteSrcVlanMask": mrdRouteSrcVlanMask,
       "mrdRouteMetric": mrdRouteMetric,
       "mrdRouteTimer": mrdRouteTimer}
)

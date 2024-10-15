# SNMP MIB module (IPV4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPV4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:19 2024
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

(apIpv4,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "apIpv4")

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
 NotificationType,
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
    "NotificationType",
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


# MODULE-IDENTITY

apIpv4Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApIpv4SourceRoute_Type(Integer32):
    """Custom type apIpv4SourceRoute based on Integer32"""
    defaultValue = 2

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


_ApIpv4SourceRoute_Type.__name__ = "Integer32"
_ApIpv4SourceRoute_Object = MibScalar
apIpv4SourceRoute = _ApIpv4SourceRoute_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 2),
    _ApIpv4SourceRoute_Type()
)
apIpv4SourceRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4SourceRoute.setStatus("current")


class _ApIpv4RecordRoute_Type(Integer32):
    """Custom type apIpv4RecordRoute based on Integer32"""
    defaultValue = 2

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


_ApIpv4RecordRoute_Type.__name__ = "Integer32"
_ApIpv4RecordRoute_Object = MibScalar
apIpv4RecordRoute = _ApIpv4RecordRoute_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 3),
    _ApIpv4RecordRoute_Type()
)
apIpv4RecordRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4RecordRoute.setStatus("current")


class _ApIpv4SubnetBcast_Type(Integer32):
    """Custom type apIpv4SubnetBcast based on Integer32"""
    defaultValue = 2

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


_ApIpv4SubnetBcast_Type.__name__ = "Integer32"
_ApIpv4SubnetBcast_Object = MibScalar
apIpv4SubnetBcast = _ApIpv4SubnetBcast_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 4),
    _ApIpv4SubnetBcast_Type()
)
apIpv4SubnetBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4SubnetBcast.setStatus("current")


class _ApIpv4EcmpMethod_Type(Integer32):
    """Custom type apIpv4EcmpMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("address", 1),
          ("round", 2))
    )


_ApIpv4EcmpMethod_Type.__name__ = "Integer32"
_ApIpv4EcmpMethod_Object = MibScalar
apIpv4EcmpMethod = _ApIpv4EcmpMethod_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 5),
    _ApIpv4EcmpMethod_Type()
)
apIpv4EcmpMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4EcmpMethod.setStatus("current")


class _ApIpv4OrphanTimer_Type(Integer32):
    """Custom type apIpv4OrphanTimer based on Integer32"""
    defaultValue = 180


_ApIpv4OrphanTimer_Object = MibScalar
apIpv4OrphanTimer = _ApIpv4OrphanTimer_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 6),
    _ApIpv4OrphanTimer_Type()
)
apIpv4OrphanTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OrphanTimer.setStatus("current")


class _ApIpv4LogRouteChanges_Type(Integer32):
    """Custom type apIpv4LogRouteChanges based on Integer32"""
    defaultValue = 2

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


_ApIpv4LogRouteChanges_Type.__name__ = "Integer32"
_ApIpv4LogRouteChanges_Object = MibScalar
apIpv4LogRouteChanges = _ApIpv4LogRouteChanges_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 7),
    _ApIpv4LogRouteChanges_Type()
)
apIpv4LogRouteChanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4LogRouteChanges.setStatus("current")
_ApIpv4ReachRoutes_Type = Gauge32
_ApIpv4ReachRoutes_Object = MibScalar
apIpv4ReachRoutes = _ApIpv4ReachRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 8),
    _ApIpv4ReachRoutes_Type()
)
apIpv4ReachRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4ReachRoutes.setStatus("current")
_ApIpv4ReachRoutesMem_Type = Gauge32
_ApIpv4ReachRoutesMem_Object = MibScalar
apIpv4ReachRoutesMem = _ApIpv4ReachRoutesMem_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 9),
    _ApIpv4ReachRoutesMem_Type()
)
apIpv4ReachRoutesMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4ReachRoutesMem.setStatus("current")
_ApIpv4TotalRoutes_Type = Gauge32
_ApIpv4TotalRoutes_Object = MibScalar
apIpv4TotalRoutes = _ApIpv4TotalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 10),
    _ApIpv4TotalRoutes_Type()
)
apIpv4TotalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4TotalRoutes.setStatus("current")
_ApIpv4TotalRoutesMem_Type = Gauge32
_ApIpv4TotalRoutesMem_Object = MibScalar
apIpv4TotalRoutesMem = _ApIpv4TotalRoutesMem_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 11),
    _ApIpv4TotalRoutesMem_Type()
)
apIpv4TotalRoutesMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4TotalRoutesMem.setStatus("current")
_ApIpv4ReachHosts_Type = Gauge32
_ApIpv4ReachHosts_Object = MibScalar
apIpv4ReachHosts = _ApIpv4ReachHosts_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 12),
    _ApIpv4ReachHosts_Type()
)
apIpv4ReachHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4ReachHosts.setStatus("current")
_ApIpv4ReachHostsMem_Type = Gauge32
_ApIpv4ReachHostsMem_Object = MibScalar
apIpv4ReachHostsMem = _ApIpv4ReachHostsMem_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 13),
    _ApIpv4ReachHostsMem_Type()
)
apIpv4ReachHostsMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4ReachHostsMem.setStatus("current")
_ApIpv4TotalHosts_Type = Gauge32
_ApIpv4TotalHosts_Object = MibScalar
apIpv4TotalHosts = _ApIpv4TotalHosts_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 14),
    _ApIpv4TotalHosts_Type()
)
apIpv4TotalHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4TotalHosts.setStatus("current")
_ApIpv4TotalHostsMem_Type = Gauge32
_ApIpv4TotalHostsMem_Object = MibScalar
apIpv4TotalHostsMem = _ApIpv4TotalHostsMem_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 15),
    _ApIpv4TotalHostsMem_Type()
)
apIpv4TotalHostsMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4TotalHostsMem.setStatus("current")
_ApIpv4PoolMem_Type = Gauge32
_ApIpv4PoolMem_Object = MibScalar
apIpv4PoolMem = _ApIpv4PoolMem_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 16),
    _ApIpv4PoolMem_Type()
)
apIpv4PoolMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4PoolMem.setStatus("current")


class _ApIpv4B2BRedundancy_Type(TruthValue):
    """Custom type apIpv4B2BRedundancy based on TruthValue"""


_ApIpv4B2BRedundancy_Object = MibScalar
apIpv4B2BRedundancy = _ApIpv4B2BRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 17),
    _ApIpv4B2BRedundancy_Type()
)
apIpv4B2BRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4B2BRedundancy.setStatus("current")


class _ApIpv4Opportunistic_Type(Integer32):
    """Custom type apIpv4Opportunistic based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("disable", 3),
          ("local", 1))
    )


_ApIpv4Opportunistic_Type.__name__ = "Integer32"
_ApIpv4Opportunistic_Object = MibScalar
apIpv4Opportunistic = _ApIpv4Opportunistic_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 18),
    _ApIpv4Opportunistic_Type()
)
apIpv4Opportunistic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4Opportunistic.setStatus("current")


class _ApIpv4RedundancyState_Type(Integer32):
    """Custom type apIpv4RedundancyState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("init", 1),
          ("master", 3))
    )


_ApIpv4RedundancyState_Type.__name__ = "Integer32"
_ApIpv4RedundancyState_Object = MibScalar
apIpv4RedundancyState = _ApIpv4RedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 19),
    _ApIpv4RedundancyState_Type()
)
apIpv4RedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyState.setStatus("current")
_ApIpv4RedundancyIf_Type = IpAddress
_ApIpv4RedundancyIf_Object = MibScalar
apIpv4RedundancyIf = _ApIpv4RedundancyIf_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 20),
    _ApIpv4RedundancyIf_Type()
)
apIpv4RedundancyIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyIf.setStatus("current")
_ApIpv4RedundancyMaster_Type = IpAddress
_ApIpv4RedundancyMaster_Object = MibScalar
apIpv4RedundancyMaster = _ApIpv4RedundancyMaster_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 21),
    _ApIpv4RedundancyMaster_Type()
)
apIpv4RedundancyMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyMaster.setStatus("current")


class _ApIpv4RedundancyMasterMode_Type(TruthValue):
    """Custom type apIpv4RedundancyMasterMode based on TruthValue"""


_ApIpv4RedundancyMasterMode_Object = MibScalar
apIpv4RedundancyMasterMode = _ApIpv4RedundancyMasterMode_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 22),
    _ApIpv4RedundancyMasterMode_Type()
)
apIpv4RedundancyMasterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4RedundancyMasterMode.setStatus("current")


class _ApIpv4EcmpSticky_Type(Integer32):
    """Custom type apIpv4EcmpSticky based on Integer32"""
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


_ApIpv4EcmpSticky_Type.__name__ = "Integer32"
_ApIpv4EcmpSticky_Object = MibScalar
apIpv4EcmpSticky = _ApIpv4EcmpSticky_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 23),
    _ApIpv4EcmpSticky_Type()
)
apIpv4EcmpSticky.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4EcmpSticky.setStatus("current")


class _ApIpv4ImplicitService_Type(Integer32):
    """Custom type apIpv4ImplicitService based on Integer32"""
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


_ApIpv4ImplicitService_Type.__name__ = "Integer32"
_ApIpv4ImplicitService_Object = MibScalar
apIpv4ImplicitService = _ApIpv4ImplicitService_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 24),
    _ApIpv4ImplicitService_Type()
)
apIpv4ImplicitService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4ImplicitService.setStatus("current")
_ApIpv4RedundancyLinkFailTable_Object = MibTable
apIpv4RedundancyLinkFailTable = _ApIpv4RedundancyLinkFailTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 25)
)
if mibBuilder.loadTexts:
    apIpv4RedundancyLinkFailTable.setStatus("current")
_ApIpv4RedundancyLinkFailEntry_Object = MibTableRow
apIpv4RedundancyLinkFailEntry = _ApIpv4RedundancyLinkFailEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 25, 1)
)
apIpv4RedundancyLinkFailEntry.setIndexNames(
    (0, "IPV4-MIB", "apIpv4RedundancyLinkFailIfIndex"),
)
if mibBuilder.loadTexts:
    apIpv4RedundancyLinkFailEntry.setStatus("current")


class _ApIpv4RedundancyLinkFailIfIndex_Type(Integer32):
    """Custom type apIpv4RedundancyLinkFailIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ApIpv4RedundancyLinkFailIfIndex_Type.__name__ = "Integer32"
_ApIpv4RedundancyLinkFailIfIndex_Object = MibTableColumn
apIpv4RedundancyLinkFailIfIndex = _ApIpv4RedundancyLinkFailIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 25, 1, 1),
    _ApIpv4RedundancyLinkFailIfIndex_Type()
)
apIpv4RedundancyLinkFailIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyLinkFailIfIndex.setStatus("current")
_ApIpv4RedundancyLinkStatus_Type = RowStatus
_ApIpv4RedundancyLinkStatus_Object = MibTableColumn
apIpv4RedundancyLinkStatus = _ApIpv4RedundancyLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 25, 1, 2),
    _ApIpv4RedundancyLinkStatus_Type()
)
apIpv4RedundancyLinkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RedundancyLinkStatus.setStatus("current")


class _ApIpv4RedundancyFailReason_Type(Integer32):
    """Custom type apIpv4RedundancyFailReason based on Integer32"""
    defaultValue = 0

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
        *(("noFailure", 0),
          ("otherSwitchAssertMaster", 3),
          ("phylinkFail", 1),
          ("uplinkFailure", 2))
    )


_ApIpv4RedundancyFailReason_Type.__name__ = "Integer32"
_ApIpv4RedundancyFailReason_Object = MibScalar
apIpv4RedundancyFailReason = _ApIpv4RedundancyFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 26),
    _ApIpv4RedundancyFailReason_Type()
)
apIpv4RedundancyFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RedundancyFailReason.setStatus("current")


class _ApIpv4VrrpVRID_Type(Integer32):
    """Custom type apIpv4VrrpVRID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApIpv4VrrpVRID_Type.__name__ = "Integer32"
_ApIpv4VrrpVRID_Object = MibScalar
apIpv4VrrpVRID = _ApIpv4VrrpVRID_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 27),
    _ApIpv4VrrpVRID_Type()
)
apIpv4VrrpVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4VrrpVRID.setStatus("current")


class _ApIpv4VrrpPriority_Type(Integer32):
    """Custom type apIpv4VrrpPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApIpv4VrrpPriority_Type.__name__ = "Integer32"
_ApIpv4VrrpPriority_Object = MibScalar
apIpv4VrrpPriority = _ApIpv4VrrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 28),
    _ApIpv4VrrpPriority_Type()
)
apIpv4VrrpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4VrrpPriority.setStatus("current")


class _ApIpv4numUplinkServices_Type(Integer32):
    """Custom type apIpv4numUplinkServices based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_ApIpv4numUplinkServices_Type.__name__ = "Integer32"
_ApIpv4numUplinkServices_Object = MibScalar
apIpv4numUplinkServices = _ApIpv4numUplinkServices_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 29),
    _ApIpv4numUplinkServices_Type()
)
apIpv4numUplinkServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4numUplinkServices.setStatus("current")


class _ApIpv4numViableUplinks_Type(Integer32):
    """Custom type apIpv4numViableUplinks based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_ApIpv4numViableUplinks_Type.__name__ = "Integer32"
_ApIpv4numViableUplinks_Object = MibScalar
apIpv4numViableUplinks = _ApIpv4numViableUplinks_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 30),
    _ApIpv4numViableUplinks_Type()
)
apIpv4numViableUplinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4numViableUplinks.setStatus("current")


class _ApIpv4numPhylinkMarked_Type(Integer32):
    """Custom type apIpv4numPhylinkMarked based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_ApIpv4numPhylinkMarked_Type.__name__ = "Integer32"
_ApIpv4numPhylinkMarked_Object = MibScalar
apIpv4numPhylinkMarked = _ApIpv4numPhylinkMarked_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 31),
    _ApIpv4numPhylinkMarked_Type()
)
apIpv4numPhylinkMarked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4numPhylinkMarked.setStatus("current")


class _ApIpv4toMasterStateCnt_Type(Integer32):
    """Custom type apIpv4toMasterStateCnt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ApIpv4toMasterStateCnt_Type.__name__ = "Integer32"
_ApIpv4toMasterStateCnt_Object = MibScalar
apIpv4toMasterStateCnt = _ApIpv4toMasterStateCnt_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 32),
    _ApIpv4toMasterStateCnt_Type()
)
apIpv4toMasterStateCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4toMasterStateCnt.setStatus("current")


class _ApIpv4toBackupStateCnt_Type(Integer32):
    """Custom type apIpv4toBackupStateCnt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ApIpv4toBackupStateCnt_Type.__name__ = "Integer32"
_ApIpv4toBackupStateCnt_Object = MibScalar
apIpv4toBackupStateCnt = _ApIpv4toBackupStateCnt_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 33),
    _ApIpv4toBackupStateCnt_Type()
)
apIpv4toBackupStateCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4toBackupStateCnt.setStatus("current")

# Managed Objects groups


# Notification objects

apIpv4RedundancyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 1, 0, 1)
)
if mibBuilder.loadTexts:
    apIpv4RedundancyTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPV4-MIB",
    **{"apIpv4RedundancyTrap": apIpv4RedundancyTrap,
       "apIpv4Mib": apIpv4Mib,
       "apIpv4SourceRoute": apIpv4SourceRoute,
       "apIpv4RecordRoute": apIpv4RecordRoute,
       "apIpv4SubnetBcast": apIpv4SubnetBcast,
       "apIpv4EcmpMethod": apIpv4EcmpMethod,
       "apIpv4OrphanTimer": apIpv4OrphanTimer,
       "apIpv4LogRouteChanges": apIpv4LogRouteChanges,
       "apIpv4ReachRoutes": apIpv4ReachRoutes,
       "apIpv4ReachRoutesMem": apIpv4ReachRoutesMem,
       "apIpv4TotalRoutes": apIpv4TotalRoutes,
       "apIpv4TotalRoutesMem": apIpv4TotalRoutesMem,
       "apIpv4ReachHosts": apIpv4ReachHosts,
       "apIpv4ReachHostsMem": apIpv4ReachHostsMem,
       "apIpv4TotalHosts": apIpv4TotalHosts,
       "apIpv4TotalHostsMem": apIpv4TotalHostsMem,
       "apIpv4PoolMem": apIpv4PoolMem,
       "apIpv4B2BRedundancy": apIpv4B2BRedundancy,
       "apIpv4Opportunistic": apIpv4Opportunistic,
       "apIpv4RedundancyState": apIpv4RedundancyState,
       "apIpv4RedundancyIf": apIpv4RedundancyIf,
       "apIpv4RedundancyMaster": apIpv4RedundancyMaster,
       "apIpv4RedundancyMasterMode": apIpv4RedundancyMasterMode,
       "apIpv4EcmpSticky": apIpv4EcmpSticky,
       "apIpv4ImplicitService": apIpv4ImplicitService,
       "apIpv4RedundancyLinkFailTable": apIpv4RedundancyLinkFailTable,
       "apIpv4RedundancyLinkFailEntry": apIpv4RedundancyLinkFailEntry,
       "apIpv4RedundancyLinkFailIfIndex": apIpv4RedundancyLinkFailIfIndex,
       "apIpv4RedundancyLinkStatus": apIpv4RedundancyLinkStatus,
       "apIpv4RedundancyFailReason": apIpv4RedundancyFailReason,
       "apIpv4VrrpVRID": apIpv4VrrpVRID,
       "apIpv4VrrpPriority": apIpv4VrrpPriority,
       "apIpv4numUplinkServices": apIpv4numUplinkServices,
       "apIpv4numViableUplinks": apIpv4numViableUplinks,
       "apIpv4numPhylinkMarked": apIpv4numPhylinkMarked,
       "apIpv4toMasterStateCnt": apIpv4toMasterStateCnt,
       "apIpv4toBackupStateCnt": apIpv4toBackupStateCnt}
)

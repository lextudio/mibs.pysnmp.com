# SNMP MIB module (IPV4-STATIC-ROUTES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPV4-STATIC-ROUTES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:21 2024
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

(apIpv4StaticRoutes,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "apIpv4StaticRoutes")

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


# MODULE-IDENTITY

apIpv4StaticRoutesMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApIpv4StaticRouteTable_Object = MibTable
apIpv4StaticRouteTable = _ApIpv4StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 2)
)
if mibBuilder.loadTexts:
    apIpv4StaticRouteTable.setStatus("current")
_ApIpv4StaticRouteEntry_Object = MibTableRow
apIpv4StaticRouteEntry = _ApIpv4StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 2, 1)
)
apIpv4StaticRouteEntry.setIndexNames(
    (0, "IPV4-STATIC-ROUTES-MIB", "apIpv4SrAddress"),
    (0, "IPV4-STATIC-ROUTES-MIB", "apIpv4SrPrefixLen"),
    (0, "IPV4-STATIC-ROUTES-MIB", "apIpv4SrNextHop"),
)
if mibBuilder.loadTexts:
    apIpv4StaticRouteEntry.setStatus("current")
_ApIpv4SrAddress_Type = IpAddress
_ApIpv4SrAddress_Object = MibTableColumn
apIpv4SrAddress = _ApIpv4SrAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 2, 1, 1),
    _ApIpv4SrAddress_Type()
)
apIpv4SrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4SrAddress.setStatus("current")
_ApIpv4SrPrefixLen_Type = Integer32
_ApIpv4SrPrefixLen_Object = MibTableColumn
apIpv4SrPrefixLen = _ApIpv4SrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 2, 1, 2),
    _ApIpv4SrPrefixLen_Type()
)
apIpv4SrPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4SrPrefixLen.setStatus("current")
_ApIpv4SrNextHop_Type = IpAddress
_ApIpv4SrNextHop_Object = MibTableColumn
apIpv4SrNextHop = _ApIpv4SrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 2, 1, 3),
    _ApIpv4SrNextHop_Type()
)
apIpv4SrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4SrNextHop.setStatus("current")


class _ApIpv4SrDistance_Type(Integer32):
    """Custom type apIpv4SrDistance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_ApIpv4SrDistance_Type.__name__ = "Integer32"
_ApIpv4SrDistance_Object = MibTableColumn
apIpv4SrDistance = _ApIpv4SrDistance_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 2, 1, 4),
    _ApIpv4SrDistance_Type()
)
apIpv4SrDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4SrDistance.setStatus("current")
_ApIpv4SrRepeat_Type = Integer32
_ApIpv4SrRepeat_Object = MibTableColumn
apIpv4SrRepeat = _ApIpv4SrRepeat_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 2, 1, 5),
    _ApIpv4SrRepeat_Type()
)
apIpv4SrRepeat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4SrRepeat.setStatus("current")


class _ApIpv4SrInUse_Type(Integer32):
    """Custom type apIpv4SrInUse based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 1),
          ("notInUse", 2))
    )


_ApIpv4SrInUse_Type.__name__ = "Integer32"
_ApIpv4SrInUse_Object = MibTableColumn
apIpv4SrInUse = _ApIpv4SrInUse_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 2, 1, 6),
    _ApIpv4SrInUse_Type()
)
apIpv4SrInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4SrInUse.setStatus("current")
_ApIpv4SrStatus_Type = RowStatus
_ApIpv4SrStatus_Object = MibTableColumn
apIpv4SrStatus = _ApIpv4SrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 2, 1, 7),
    _ApIpv4SrStatus_Type()
)
apIpv4SrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4SrStatus.setStatus("current")
_ApIpv4SrScmOnly_Type = TruthValue
_ApIpv4SrScmOnly_Object = MibTableColumn
apIpv4SrScmOnly = _ApIpv4SrScmOnly_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 2, 1, 8),
    _ApIpv4SrScmOnly_Type()
)
apIpv4SrScmOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4SrScmOnly.setStatus("current")
_ApIpv4SrFirewall_Type = TruthValue
_ApIpv4SrFirewall_Object = MibTableColumn
apIpv4SrFirewall = _ApIpv4SrFirewall_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 2, 1, 9),
    _ApIpv4SrFirewall_Type()
)
apIpv4SrFirewall.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4SrFirewall.setStatus("current")


class _ApIpv4SrRouteIndex_Type(Integer32):
    """Custom type apIpv4SrRouteIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ApIpv4SrRouteIndex_Type.__name__ = "Integer32"
_ApIpv4SrRouteIndex_Object = MibTableColumn
apIpv4SrRouteIndex = _ApIpv4SrRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 2, 1, 10),
    _ApIpv4SrRouteIndex_Type()
)
apIpv4SrRouteIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4SrRouteIndex.setStatus("current")
_ApIpv4StaticFirewallTable_Object = MibTable
apIpv4StaticFirewallTable = _ApIpv4StaticFirewallTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 3)
)
if mibBuilder.loadTexts:
    apIpv4StaticFirewallTable.setStatus("current")
_ApIpv4StaticFirewallEntry_Object = MibTableRow
apIpv4StaticFirewallEntry = _ApIpv4StaticFirewallEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 3, 1)
)
apIpv4StaticFirewallEntry.setIndexNames(
    (0, "IPV4-STATIC-ROUTES-MIB", "apIpv4FirewallIndex"),
)
if mibBuilder.loadTexts:
    apIpv4StaticFirewallEntry.setStatus("current")


class _ApIpv4FirewallIndex_Type(Integer32):
    """Custom type apIpv4FirewallIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ApIpv4FirewallIndex_Type.__name__ = "Integer32"
_ApIpv4FirewallIndex_Object = MibTableColumn
apIpv4FirewallIndex = _ApIpv4FirewallIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 3, 1, 1),
    _ApIpv4FirewallIndex_Type()
)
apIpv4FirewallIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4FirewallIndex.setStatus("current")
_ApIpv4FirewallNextHop_Type = IpAddress
_ApIpv4FirewallNextHop_Object = MibTableColumn
apIpv4FirewallNextHop = _ApIpv4FirewallNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 3, 1, 2),
    _ApIpv4FirewallNextHop_Type()
)
apIpv4FirewallNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4FirewallNextHop.setStatus("current")
_ApIpv4FirewallRemoteAddress_Type = IpAddress
_ApIpv4FirewallRemoteAddress_Object = MibTableColumn
apIpv4FirewallRemoteAddress = _ApIpv4FirewallRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 3, 1, 3),
    _ApIpv4FirewallRemoteAddress_Type()
)
apIpv4FirewallRemoteAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4FirewallRemoteAddress.setStatus("current")
_ApIpv4FirewallRemoteSwitch_Type = IpAddress
_ApIpv4FirewallRemoteSwitch_Object = MibTableColumn
apIpv4FirewallRemoteSwitch = _ApIpv4FirewallRemoteSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 3, 1, 4),
    _ApIpv4FirewallRemoteSwitch_Type()
)
apIpv4FirewallRemoteSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4FirewallRemoteSwitch.setStatus("current")
_ApIpv4FirewallStatus_Type = RowStatus
_ApIpv4FirewallStatus_Object = MibTableColumn
apIpv4FirewallStatus = _ApIpv4FirewallStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 5, 3, 1, 5),
    _ApIpv4FirewallStatus_Type()
)
apIpv4FirewallStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4FirewallStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPV4-STATIC-ROUTES-MIB",
    **{"apIpv4StaticRoutesMib": apIpv4StaticRoutesMib,
       "apIpv4StaticRouteTable": apIpv4StaticRouteTable,
       "apIpv4StaticRouteEntry": apIpv4StaticRouteEntry,
       "apIpv4SrAddress": apIpv4SrAddress,
       "apIpv4SrPrefixLen": apIpv4SrPrefixLen,
       "apIpv4SrNextHop": apIpv4SrNextHop,
       "apIpv4SrDistance": apIpv4SrDistance,
       "apIpv4SrRepeat": apIpv4SrRepeat,
       "apIpv4SrInUse": apIpv4SrInUse,
       "apIpv4SrStatus": apIpv4SrStatus,
       "apIpv4SrScmOnly": apIpv4SrScmOnly,
       "apIpv4SrFirewall": apIpv4SrFirewall,
       "apIpv4SrRouteIndex": apIpv4SrRouteIndex,
       "apIpv4StaticFirewallTable": apIpv4StaticFirewallTable,
       "apIpv4StaticFirewallEntry": apIpv4StaticFirewallEntry,
       "apIpv4FirewallIndex": apIpv4FirewallIndex,
       "apIpv4FirewallNextHop": apIpv4FirewallNextHop,
       "apIpv4FirewallRemoteAddress": apIpv4FirewallRemoteAddress,
       "apIpv4FirewallRemoteSwitch": apIpv4FirewallRemoteSwitch,
       "apIpv4FirewallStatus": apIpv4FirewallStatus}
)

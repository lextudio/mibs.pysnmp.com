# SNMP MIB module (IPV4-RIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPV4-RIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:20 2024
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

(apIpv4Rip,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "apIpv4Rip")

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

apIpv4RipMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApIpv4RipRedistributeStatic_Type(Integer32):
    """Custom type apIpv4RipRedistributeStatic based on Integer32"""
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


_ApIpv4RipRedistributeStatic_Type.__name__ = "Integer32"
_ApIpv4RipRedistributeStatic_Object = MibScalar
apIpv4RipRedistributeStatic = _ApIpv4RipRedistributeStatic_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 2),
    _ApIpv4RipRedistributeStatic_Type()
)
apIpv4RipRedistributeStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4RipRedistributeStatic.setStatus("current")


class _ApIpv4RipStaticMetric_Type(Integer32):
    """Custom type apIpv4RipStaticMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ApIpv4RipStaticMetric_Type.__name__ = "Integer32"
_ApIpv4RipStaticMetric_Object = MibScalar
apIpv4RipStaticMetric = _ApIpv4RipStaticMetric_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 3),
    _ApIpv4RipStaticMetric_Type()
)
apIpv4RipStaticMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4RipStaticMetric.setStatus("current")


class _ApIpv4RipRedistributeOspf_Type(Integer32):
    """Custom type apIpv4RipRedistributeOspf based on Integer32"""
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


_ApIpv4RipRedistributeOspf_Type.__name__ = "Integer32"
_ApIpv4RipRedistributeOspf_Object = MibScalar
apIpv4RipRedistributeOspf = _ApIpv4RipRedistributeOspf_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 4),
    _ApIpv4RipRedistributeOspf_Type()
)
apIpv4RipRedistributeOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4RipRedistributeOspf.setStatus("current")


class _ApIpv4RipOspfMetric_Type(Integer32):
    """Custom type apIpv4RipOspfMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ApIpv4RipOspfMetric_Type.__name__ = "Integer32"
_ApIpv4RipOspfMetric_Object = MibScalar
apIpv4RipOspfMetric = _ApIpv4RipOspfMetric_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 5),
    _ApIpv4RipOspfMetric_Type()
)
apIpv4RipOspfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4RipOspfMetric.setStatus("current")


class _ApIpv4RipRedistributeLocal_Type(Integer32):
    """Custom type apIpv4RipRedistributeLocal based on Integer32"""
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


_ApIpv4RipRedistributeLocal_Type.__name__ = "Integer32"
_ApIpv4RipRedistributeLocal_Object = MibScalar
apIpv4RipRedistributeLocal = _ApIpv4RipRedistributeLocal_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 6),
    _ApIpv4RipRedistributeLocal_Type()
)
apIpv4RipRedistributeLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4RipRedistributeLocal.setStatus("current")


class _ApIpv4RipLocalMetric_Type(Integer32):
    """Custom type apIpv4RipLocalMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ApIpv4RipLocalMetric_Type.__name__ = "Integer32"
_ApIpv4RipLocalMetric_Object = MibScalar
apIpv4RipLocalMetric = _ApIpv4RipLocalMetric_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 7),
    _ApIpv4RipLocalMetric_Type()
)
apIpv4RipLocalMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4RipLocalMetric.setStatus("current")
_ApIpv4RipAdvRouteTable_Object = MibTable
apIpv4RipAdvRouteTable = _ApIpv4RipAdvRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 8)
)
if mibBuilder.loadTexts:
    apIpv4RipAdvRouteTable.setStatus("current")
_ApIpv4RipAdvRouteEntry_Object = MibTableRow
apIpv4RipAdvRouteEntry = _ApIpv4RipAdvRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 8, 1)
)
apIpv4RipAdvRouteEntry.setIndexNames(
    (0, "IPV4-RIP-MIB", "apIpv4RipAdvRoutePrefix"),
    (0, "IPV4-RIP-MIB", "apIpv4RipAdvRoutePrefixLen"),
)
if mibBuilder.loadTexts:
    apIpv4RipAdvRouteEntry.setStatus("current")
_ApIpv4RipAdvRoutePrefix_Type = IpAddress
_ApIpv4RipAdvRoutePrefix_Object = MibTableColumn
apIpv4RipAdvRoutePrefix = _ApIpv4RipAdvRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 8, 1, 1),
    _ApIpv4RipAdvRoutePrefix_Type()
)
apIpv4RipAdvRoutePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RipAdvRoutePrefix.setStatus("current")


class _ApIpv4RipAdvRoutePrefixLen_Type(Integer32):
    """Custom type apIpv4RipAdvRoutePrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ApIpv4RipAdvRoutePrefixLen_Type.__name__ = "Integer32"
_ApIpv4RipAdvRoutePrefixLen_Object = MibTableColumn
apIpv4RipAdvRoutePrefixLen = _ApIpv4RipAdvRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 8, 1, 2),
    _ApIpv4RipAdvRoutePrefixLen_Type()
)
apIpv4RipAdvRoutePrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RipAdvRoutePrefixLen.setStatus("current")


class _ApIpv4RipAdvRouteMetric_Type(Integer32):
    """Custom type apIpv4RipAdvRouteMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ApIpv4RipAdvRouteMetric_Type.__name__ = "Integer32"
_ApIpv4RipAdvRouteMetric_Object = MibTableColumn
apIpv4RipAdvRouteMetric = _ApIpv4RipAdvRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 8, 1, 3),
    _ApIpv4RipAdvRouteMetric_Type()
)
apIpv4RipAdvRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RipAdvRouteMetric.setStatus("current")
_ApIpv4RipAdvRouteStatus_Type = RowStatus
_ApIpv4RipAdvRouteStatus_Object = MibTableColumn
apIpv4RipAdvRouteStatus = _ApIpv4RipAdvRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 8, 1, 4),
    _ApIpv4RipAdvRouteStatus_Type()
)
apIpv4RipAdvRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RipAdvRouteStatus.setStatus("current")
_ApIpv4RipIfAdvRouteTable_Object = MibTable
apIpv4RipIfAdvRouteTable = _ApIpv4RipIfAdvRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 9)
)
if mibBuilder.loadTexts:
    apIpv4RipIfAdvRouteTable.setStatus("current")
_ApIpv4RipIfAdvRouteEntry_Object = MibTableRow
apIpv4RipIfAdvRouteEntry = _ApIpv4RipIfAdvRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 9, 1)
)
apIpv4RipIfAdvRouteEntry.setIndexNames(
    (0, "IPV4-RIP-MIB", "apIpv4RipIfAdvRouteAddress"),
    (0, "IPV4-RIP-MIB", "apIpv4RipIfAdvRoutePrefix"),
    (0, "IPV4-RIP-MIB", "apIpv4RipIfAdvRoutePrefixLen"),
)
if mibBuilder.loadTexts:
    apIpv4RipIfAdvRouteEntry.setStatus("current")
_ApIpv4RipIfAdvRouteAddress_Type = IpAddress
_ApIpv4RipIfAdvRouteAddress_Object = MibTableColumn
apIpv4RipIfAdvRouteAddress = _ApIpv4RipIfAdvRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 9, 1, 1),
    _ApIpv4RipIfAdvRouteAddress_Type()
)
apIpv4RipIfAdvRouteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RipIfAdvRouteAddress.setStatus("current")
_ApIpv4RipIfAdvRoutePrefix_Type = IpAddress
_ApIpv4RipIfAdvRoutePrefix_Object = MibTableColumn
apIpv4RipIfAdvRoutePrefix = _ApIpv4RipIfAdvRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 9, 1, 2),
    _ApIpv4RipIfAdvRoutePrefix_Type()
)
apIpv4RipIfAdvRoutePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RipIfAdvRoutePrefix.setStatus("current")


class _ApIpv4RipIfAdvRoutePrefixLen_Type(Integer32):
    """Custom type apIpv4RipIfAdvRoutePrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ApIpv4RipIfAdvRoutePrefixLen_Type.__name__ = "Integer32"
_ApIpv4RipIfAdvRoutePrefixLen_Object = MibTableColumn
apIpv4RipIfAdvRoutePrefixLen = _ApIpv4RipIfAdvRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 9, 1, 3),
    _ApIpv4RipIfAdvRoutePrefixLen_Type()
)
apIpv4RipIfAdvRoutePrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RipIfAdvRoutePrefixLen.setStatus("current")


class _ApIpv4RipIfAdvRouteMetric_Type(Integer32):
    """Custom type apIpv4RipIfAdvRouteMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ApIpv4RipIfAdvRouteMetric_Type.__name__ = "Integer32"
_ApIpv4RipIfAdvRouteMetric_Object = MibTableColumn
apIpv4RipIfAdvRouteMetric = _ApIpv4RipIfAdvRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 9, 1, 4),
    _ApIpv4RipIfAdvRouteMetric_Type()
)
apIpv4RipIfAdvRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RipIfAdvRouteMetric.setStatus("current")
_ApIpv4RipIfAdvRouteStatus_Type = RowStatus
_ApIpv4RipIfAdvRouteStatus_Object = MibTableColumn
apIpv4RipIfAdvRouteStatus = _ApIpv4RipIfAdvRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 9, 1, 5),
    _ApIpv4RipIfAdvRouteStatus_Type()
)
apIpv4RipIfAdvRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RipIfAdvRouteStatus.setStatus("current")
_ApIpv4RipIfTable_Object = MibTable
apIpv4RipIfTable = _ApIpv4RipIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 10)
)
if mibBuilder.loadTexts:
    apIpv4RipIfTable.setStatus("current")
_ApIpv4RipIfEntry_Object = MibTableRow
apIpv4RipIfEntry = _ApIpv4RipIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 10, 1)
)
apIpv4RipIfEntry.setIndexNames(
    (0, "IPV4-RIP-MIB", "apIpv4RipIfAddress"),
)
if mibBuilder.loadTexts:
    apIpv4RipIfEntry.setStatus("current")
_ApIpv4RipIfAddress_Type = IpAddress
_ApIpv4RipIfAddress_Object = MibTableColumn
apIpv4RipIfAddress = _ApIpv4RipIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 10, 1, 1),
    _ApIpv4RipIfAddress_Type()
)
apIpv4RipIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4RipIfAddress.setStatus("current")
_ApIpv4RipIfLogTx_Type = TruthValue
_ApIpv4RipIfLogTx_Object = MibTableColumn
apIpv4RipIfLogTx = _ApIpv4RipIfLogTx_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 10, 1, 2),
    _ApIpv4RipIfLogTx_Type()
)
apIpv4RipIfLogTx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RipIfLogTx.setStatus("current")
_ApIpv4RipIfLogRx_Type = TruthValue
_ApIpv4RipIfLogRx_Object = MibTableColumn
apIpv4RipIfLogRx = _ApIpv4RipIfLogRx_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 10, 1, 3),
    _ApIpv4RipIfLogRx_Type()
)
apIpv4RipIfLogRx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4RipIfLogRx.setStatus("current")


class _ApIpv4RipEqualCostRoutes_Type(Integer32):
    """Custom type apIpv4RipEqualCostRoutes based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ApIpv4RipEqualCostRoutes_Type.__name__ = "Integer32"
_ApIpv4RipEqualCostRoutes_Object = MibScalar
apIpv4RipEqualCostRoutes = _ApIpv4RipEqualCostRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 11),
    _ApIpv4RipEqualCostRoutes_Type()
)
apIpv4RipEqualCostRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4RipEqualCostRoutes.setStatus("current")


class _ApIpv4RipRedistributeFirewall_Type(Integer32):
    """Custom type apIpv4RipRedistributeFirewall based on Integer32"""
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


_ApIpv4RipRedistributeFirewall_Type.__name__ = "Integer32"
_ApIpv4RipRedistributeFirewall_Object = MibScalar
apIpv4RipRedistributeFirewall = _ApIpv4RipRedistributeFirewall_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 12),
    _ApIpv4RipRedistributeFirewall_Type()
)
apIpv4RipRedistributeFirewall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4RipRedistributeFirewall.setStatus("current")


class _ApIpv4RipFirewallMetric_Type(Integer32):
    """Custom type apIpv4RipFirewallMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ApIpv4RipFirewallMetric_Type.__name__ = "Integer32"
_ApIpv4RipFirewallMetric_Object = MibScalar
apIpv4RipFirewallMetric = _ApIpv4RipFirewallMetric_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 13),
    _ApIpv4RipFirewallMetric_Type()
)
apIpv4RipFirewallMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4RipFirewallMetric.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPV4-RIP-MIB",
    **{"apIpv4RipMib": apIpv4RipMib,
       "apIpv4RipRedistributeStatic": apIpv4RipRedistributeStatic,
       "apIpv4RipStaticMetric": apIpv4RipStaticMetric,
       "apIpv4RipRedistributeOspf": apIpv4RipRedistributeOspf,
       "apIpv4RipOspfMetric": apIpv4RipOspfMetric,
       "apIpv4RipRedistributeLocal": apIpv4RipRedistributeLocal,
       "apIpv4RipLocalMetric": apIpv4RipLocalMetric,
       "apIpv4RipAdvRouteTable": apIpv4RipAdvRouteTable,
       "apIpv4RipAdvRouteEntry": apIpv4RipAdvRouteEntry,
       "apIpv4RipAdvRoutePrefix": apIpv4RipAdvRoutePrefix,
       "apIpv4RipAdvRoutePrefixLen": apIpv4RipAdvRoutePrefixLen,
       "apIpv4RipAdvRouteMetric": apIpv4RipAdvRouteMetric,
       "apIpv4RipAdvRouteStatus": apIpv4RipAdvRouteStatus,
       "apIpv4RipIfAdvRouteTable": apIpv4RipIfAdvRouteTable,
       "apIpv4RipIfAdvRouteEntry": apIpv4RipIfAdvRouteEntry,
       "apIpv4RipIfAdvRouteAddress": apIpv4RipIfAdvRouteAddress,
       "apIpv4RipIfAdvRoutePrefix": apIpv4RipIfAdvRoutePrefix,
       "apIpv4RipIfAdvRoutePrefixLen": apIpv4RipIfAdvRoutePrefixLen,
       "apIpv4RipIfAdvRouteMetric": apIpv4RipIfAdvRouteMetric,
       "apIpv4RipIfAdvRouteStatus": apIpv4RipIfAdvRouteStatus,
       "apIpv4RipIfTable": apIpv4RipIfTable,
       "apIpv4RipIfEntry": apIpv4RipIfEntry,
       "apIpv4RipIfAddress": apIpv4RipIfAddress,
       "apIpv4RipIfLogTx": apIpv4RipIfLogTx,
       "apIpv4RipIfLogRx": apIpv4RipIfLogRx,
       "apIpv4RipEqualCostRoutes": apIpv4RipEqualCostRoutes,
       "apIpv4RipRedistributeFirewall": apIpv4RipRedistributeFirewall,
       "apIpv4RipFirewallMetric": apIpv4RipFirewallMetric}
)

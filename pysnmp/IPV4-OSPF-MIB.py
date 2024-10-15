# SNMP MIB module (IPV4-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPV4-OSPF-MIB
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

(apIpv4Ospf,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "apIpv4Ospf")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

apIpv4OspfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApIpv4OspfRedistributeLocal_Type(Integer32):
    """Custom type apIpv4OspfRedistributeLocal based on Integer32"""
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


_ApIpv4OspfRedistributeLocal_Type.__name__ = "Integer32"
_ApIpv4OspfRedistributeLocal_Object = MibScalar
apIpv4OspfRedistributeLocal = _ApIpv4OspfRedistributeLocal_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 2),
    _ApIpv4OspfRedistributeLocal_Type()
)
apIpv4OspfRedistributeLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfRedistributeLocal.setStatus("current")


class _ApIpv4OspfLocalType_Type(Integer32):
    """Custom type apIpv4OspfLocalType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aseType1", 1),
          ("aseType2", 2))
    )


_ApIpv4OspfLocalType_Type.__name__ = "Integer32"
_ApIpv4OspfLocalType_Object = MibScalar
apIpv4OspfLocalType = _ApIpv4OspfLocalType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 3),
    _ApIpv4OspfLocalType_Type()
)
apIpv4OspfLocalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfLocalType.setStatus("current")


class _ApIpv4OspfLocalMetric_Type(Integer32):
    """Custom type apIpv4OspfLocalMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_ApIpv4OspfLocalMetric_Type.__name__ = "Integer32"
_ApIpv4OspfLocalMetric_Object = MibScalar
apIpv4OspfLocalMetric = _ApIpv4OspfLocalMetric_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 4),
    _ApIpv4OspfLocalMetric_Type()
)
apIpv4OspfLocalMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfLocalMetric.setStatus("current")


class _ApIpv4OspfLocalTag_Type(Integer32):
    """Custom type apIpv4OspfLocalTag based on Integer32"""
    defaultValue = 0


_ApIpv4OspfLocalTag_Object = MibScalar
apIpv4OspfLocalTag = _ApIpv4OspfLocalTag_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 5),
    _ApIpv4OspfLocalTag_Type()
)
apIpv4OspfLocalTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfLocalTag.setStatus("current")


class _ApIpv4OspfRedistributeStatic_Type(Integer32):
    """Custom type apIpv4OspfRedistributeStatic based on Integer32"""
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


_ApIpv4OspfRedistributeStatic_Type.__name__ = "Integer32"
_ApIpv4OspfRedistributeStatic_Object = MibScalar
apIpv4OspfRedistributeStatic = _ApIpv4OspfRedistributeStatic_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 6),
    _ApIpv4OspfRedistributeStatic_Type()
)
apIpv4OspfRedistributeStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfRedistributeStatic.setStatus("current")


class _ApIpv4OspfStaticType_Type(Integer32):
    """Custom type apIpv4OspfStaticType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aseType1", 1),
          ("aseType2", 2))
    )


_ApIpv4OspfStaticType_Type.__name__ = "Integer32"
_ApIpv4OspfStaticType_Object = MibScalar
apIpv4OspfStaticType = _ApIpv4OspfStaticType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 7),
    _ApIpv4OspfStaticType_Type()
)
apIpv4OspfStaticType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfStaticType.setStatus("current")


class _ApIpv4OspfStaticMetric_Type(Integer32):
    """Custom type apIpv4OspfStaticMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_ApIpv4OspfStaticMetric_Type.__name__ = "Integer32"
_ApIpv4OspfStaticMetric_Object = MibScalar
apIpv4OspfStaticMetric = _ApIpv4OspfStaticMetric_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 8),
    _ApIpv4OspfStaticMetric_Type()
)
apIpv4OspfStaticMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfStaticMetric.setStatus("current")


class _ApIpv4OspfStaticTag_Type(Integer32):
    """Custom type apIpv4OspfStaticTag based on Integer32"""
    defaultValue = 0


_ApIpv4OspfStaticTag_Object = MibScalar
apIpv4OspfStaticTag = _ApIpv4OspfStaticTag_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 9),
    _ApIpv4OspfStaticTag_Type()
)
apIpv4OspfStaticTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfStaticTag.setStatus("current")


class _ApIpv4OspfRedistributeRip_Type(Integer32):
    """Custom type apIpv4OspfRedistributeRip based on Integer32"""
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


_ApIpv4OspfRedistributeRip_Type.__name__ = "Integer32"
_ApIpv4OspfRedistributeRip_Object = MibScalar
apIpv4OspfRedistributeRip = _ApIpv4OspfRedistributeRip_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 10),
    _ApIpv4OspfRedistributeRip_Type()
)
apIpv4OspfRedistributeRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfRedistributeRip.setStatus("current")


class _ApIpv4OspfRipType_Type(Integer32):
    """Custom type apIpv4OspfRipType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aseType1", 1),
          ("aseType2", 2))
    )


_ApIpv4OspfRipType_Type.__name__ = "Integer32"
_ApIpv4OspfRipType_Object = MibScalar
apIpv4OspfRipType = _ApIpv4OspfRipType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 11),
    _ApIpv4OspfRipType_Type()
)
apIpv4OspfRipType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfRipType.setStatus("current")


class _ApIpv4OspfRipMetric_Type(Integer32):
    """Custom type apIpv4OspfRipMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_ApIpv4OspfRipMetric_Type.__name__ = "Integer32"
_ApIpv4OspfRipMetric_Object = MibScalar
apIpv4OspfRipMetric = _ApIpv4OspfRipMetric_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 12),
    _ApIpv4OspfRipMetric_Type()
)
apIpv4OspfRipMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfRipMetric.setStatus("current")


class _ApIpv4OspfRipTag_Type(Integer32):
    """Custom type apIpv4OspfRipTag based on Integer32"""
    defaultValue = 0


_ApIpv4OspfRipTag_Object = MibScalar
apIpv4OspfRipTag = _ApIpv4OspfRipTag_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 13),
    _ApIpv4OspfRipTag_Type()
)
apIpv4OspfRipTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfRipTag.setStatus("current")


class _ApIpv4OspfOriginateDefault_Type(Integer32):
    """Custom type apIpv4OspfOriginateDefault based on Integer32"""
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


_ApIpv4OspfOriginateDefault_Type.__name__ = "Integer32"
_ApIpv4OspfOriginateDefault_Object = MibScalar
apIpv4OspfOriginateDefault = _ApIpv4OspfOriginateDefault_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 14),
    _ApIpv4OspfOriginateDefault_Type()
)
apIpv4OspfOriginateDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfOriginateDefault.setStatus("current")


class _ApIpv4OspfDefaultType_Type(Integer32):
    """Custom type apIpv4OspfDefaultType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aseType1", 1),
          ("aseType2", 2))
    )


_ApIpv4OspfDefaultType_Type.__name__ = "Integer32"
_ApIpv4OspfDefaultType_Object = MibScalar
apIpv4OspfDefaultType = _ApIpv4OspfDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 15),
    _ApIpv4OspfDefaultType_Type()
)
apIpv4OspfDefaultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfDefaultType.setStatus("current")


class _ApIpv4OspfDefaultMetric_Type(Integer32):
    """Custom type apIpv4OspfDefaultMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_ApIpv4OspfDefaultMetric_Type.__name__ = "Integer32"
_ApIpv4OspfDefaultMetric_Object = MibScalar
apIpv4OspfDefaultMetric = _ApIpv4OspfDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 16),
    _ApIpv4OspfDefaultMetric_Type()
)
apIpv4OspfDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfDefaultMetric.setStatus("current")


class _ApIpv4OspfDefaultTag_Type(Integer32):
    """Custom type apIpv4OspfDefaultTag based on Integer32"""
    defaultValue = 0


_ApIpv4OspfDefaultTag_Object = MibScalar
apIpv4OspfDefaultTag = _ApIpv4OspfDefaultTag_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 17),
    _ApIpv4OspfDefaultTag_Type()
)
apIpv4OspfDefaultTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfDefaultTag.setStatus("current")


class _ApIpv4OspfRedistributeFirewall_Type(Integer32):
    """Custom type apIpv4OspfRedistributeFirewall based on Integer32"""
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


_ApIpv4OspfRedistributeFirewall_Type.__name__ = "Integer32"
_ApIpv4OspfRedistributeFirewall_Object = MibScalar
apIpv4OspfRedistributeFirewall = _ApIpv4OspfRedistributeFirewall_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 18),
    _ApIpv4OspfRedistributeFirewall_Type()
)
apIpv4OspfRedistributeFirewall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfRedistributeFirewall.setStatus("current")


class _ApIpv4OspfFirewallType_Type(Integer32):
    """Custom type apIpv4OspfFirewallType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aseType1", 1),
          ("aseType2", 2))
    )


_ApIpv4OspfFirewallType_Type.__name__ = "Integer32"
_ApIpv4OspfFirewallType_Object = MibScalar
apIpv4OspfFirewallType = _ApIpv4OspfFirewallType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 19),
    _ApIpv4OspfFirewallType_Type()
)
apIpv4OspfFirewallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfFirewallType.setStatus("current")


class _ApIpv4OspfFirewallMetric_Type(Integer32):
    """Custom type apIpv4OspfFirewallMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_ApIpv4OspfFirewallMetric_Type.__name__ = "Integer32"
_ApIpv4OspfFirewallMetric_Object = MibScalar
apIpv4OspfFirewallMetric = _ApIpv4OspfFirewallMetric_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 20),
    _ApIpv4OspfFirewallMetric_Type()
)
apIpv4OspfFirewallMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfFirewallMetric.setStatus("current")


class _ApIpv4OspfFirewallTag_Type(Integer32):
    """Custom type apIpv4OspfFirewallTag based on Integer32"""
    defaultValue = 0


_ApIpv4OspfFirewallTag_Object = MibScalar
apIpv4OspfFirewallTag = _ApIpv4OspfFirewallTag_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 21),
    _ApIpv4OspfFirewallTag_Type()
)
apIpv4OspfFirewallTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfFirewallTag.setStatus("current")
_ApIpv4OspfAdvRouteTable_Object = MibTable
apIpv4OspfAdvRouteTable = _ApIpv4OspfAdvRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 22)
)
if mibBuilder.loadTexts:
    apIpv4OspfAdvRouteTable.setStatus("current")
_ApIpv4OspfAdvRouteEntry_Object = MibTableRow
apIpv4OspfAdvRouteEntry = _ApIpv4OspfAdvRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 22, 1)
)
apIpv4OspfAdvRouteEntry.setIndexNames(
    (0, "IPV4-OSPF-MIB", "apIpv4OspfAdvRoutePrefix"),
    (0, "IPV4-OSPF-MIB", "apIpv4OspfAdvRoutePrefixLen"),
)
if mibBuilder.loadTexts:
    apIpv4OspfAdvRouteEntry.setStatus("current")
_ApIpv4OspfAdvRoutePrefix_Type = IpAddress
_ApIpv4OspfAdvRoutePrefix_Object = MibTableColumn
apIpv4OspfAdvRoutePrefix = _ApIpv4OspfAdvRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 22, 1, 1),
    _ApIpv4OspfAdvRoutePrefix_Type()
)
apIpv4OspfAdvRoutePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4OspfAdvRoutePrefix.setStatus("current")


class _ApIpv4OspfAdvRoutePrefixLen_Type(Integer32):
    """Custom type apIpv4OspfAdvRoutePrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ApIpv4OspfAdvRoutePrefixLen_Type.__name__ = "Integer32"
_ApIpv4OspfAdvRoutePrefixLen_Object = MibTableColumn
apIpv4OspfAdvRoutePrefixLen = _ApIpv4OspfAdvRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 22, 1, 2),
    _ApIpv4OspfAdvRoutePrefixLen_Type()
)
apIpv4OspfAdvRoutePrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4OspfAdvRoutePrefixLen.setStatus("current")


class _ApIpv4OspfAdvRouteType_Type(Integer32):
    """Custom type apIpv4OspfAdvRouteType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aseType1", 1),
          ("aseType2", 2))
    )


_ApIpv4OspfAdvRouteType_Type.__name__ = "Integer32"
_ApIpv4OspfAdvRouteType_Object = MibTableColumn
apIpv4OspfAdvRouteType = _ApIpv4OspfAdvRouteType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 22, 1, 3),
    _ApIpv4OspfAdvRouteType_Type()
)
apIpv4OspfAdvRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4OspfAdvRouteType.setStatus("current")


class _ApIpv4OspfAdvRouteMetric_Type(Integer32):
    """Custom type apIpv4OspfAdvRouteMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_ApIpv4OspfAdvRouteMetric_Type.__name__ = "Integer32"
_ApIpv4OspfAdvRouteMetric_Object = MibTableColumn
apIpv4OspfAdvRouteMetric = _ApIpv4OspfAdvRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 22, 1, 4),
    _ApIpv4OspfAdvRouteMetric_Type()
)
apIpv4OspfAdvRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4OspfAdvRouteMetric.setStatus("current")


class _ApIpv4OspfAdvRouteTag_Type(Integer32):
    """Custom type apIpv4OspfAdvRouteTag based on Integer32"""
    defaultValue = 0


_ApIpv4OspfAdvRouteTag_Object = MibTableColumn
apIpv4OspfAdvRouteTag = _ApIpv4OspfAdvRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 22, 1, 5),
    _ApIpv4OspfAdvRouteTag_Type()
)
apIpv4OspfAdvRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4OspfAdvRouteTag.setStatus("current")
_ApIpv4OspfAdvRouteStatus_Type = RowStatus
_ApIpv4OspfAdvRouteStatus_Object = MibTableColumn
apIpv4OspfAdvRouteStatus = _ApIpv4OspfAdvRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 22, 1, 6),
    _ApIpv4OspfAdvRouteStatus_Type()
)
apIpv4OspfAdvRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4OspfAdvRouteStatus.setStatus("current")
_ApIpv4OspfIfAdvRouteTable_Object = MibTable
apIpv4OspfIfAdvRouteTable = _ApIpv4OspfIfAdvRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 23)
)
if mibBuilder.loadTexts:
    apIpv4OspfIfAdvRouteTable.setStatus("current")
_ApIpv4OspfIfAdvRouteEntry_Object = MibTableRow
apIpv4OspfIfAdvRouteEntry = _ApIpv4OspfIfAdvRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 23, 1)
)
apIpv4OspfIfAdvRouteEntry.setIndexNames(
    (0, "IPV4-OSPF-MIB", "apIpv4OspfIfAdvRouteAddress"),
    (0, "IPV4-OSPF-MIB", "apIpv4OspfIfAdvRoutePrefix"),
    (0, "IPV4-OSPF-MIB", "apIpv4OspfIfAdvRoutePrefixLen"),
)
if mibBuilder.loadTexts:
    apIpv4OspfIfAdvRouteEntry.setStatus("current")
_ApIpv4OspfIfAdvRouteAddress_Type = IpAddress
_ApIpv4OspfIfAdvRouteAddress_Object = MibTableColumn
apIpv4OspfIfAdvRouteAddress = _ApIpv4OspfIfAdvRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 23, 1, 1),
    _ApIpv4OspfIfAdvRouteAddress_Type()
)
apIpv4OspfIfAdvRouteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4OspfIfAdvRouteAddress.setStatus("current")
_ApIpv4OspfIfAdvRoutePrefix_Type = IpAddress
_ApIpv4OspfIfAdvRoutePrefix_Object = MibTableColumn
apIpv4OspfIfAdvRoutePrefix = _ApIpv4OspfIfAdvRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 23, 1, 2),
    _ApIpv4OspfIfAdvRoutePrefix_Type()
)
apIpv4OspfIfAdvRoutePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4OspfIfAdvRoutePrefix.setStatus("current")


class _ApIpv4OspfIfAdvRoutePrefixLen_Type(Integer32):
    """Custom type apIpv4OspfIfAdvRoutePrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ApIpv4OspfIfAdvRoutePrefixLen_Type.__name__ = "Integer32"
_ApIpv4OspfIfAdvRoutePrefixLen_Object = MibTableColumn
apIpv4OspfIfAdvRoutePrefixLen = _ApIpv4OspfIfAdvRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 23, 1, 3),
    _ApIpv4OspfIfAdvRoutePrefixLen_Type()
)
apIpv4OspfIfAdvRoutePrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4OspfIfAdvRoutePrefixLen.setStatus("current")


class _ApIpv4OspfIfAdvRouteType_Type(Integer32):
    """Custom type apIpv4OspfIfAdvRouteType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aseType1", 1),
          ("aseType2", 2))
    )


_ApIpv4OspfIfAdvRouteType_Type.__name__ = "Integer32"
_ApIpv4OspfIfAdvRouteType_Object = MibTableColumn
apIpv4OspfIfAdvRouteType = _ApIpv4OspfIfAdvRouteType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 23, 1, 4),
    _ApIpv4OspfIfAdvRouteType_Type()
)
apIpv4OspfIfAdvRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4OspfIfAdvRouteType.setStatus("current")


class _ApIpv4OspfIfAdvRouteMetric_Type(Integer32):
    """Custom type apIpv4OspfIfAdvRouteMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_ApIpv4OspfIfAdvRouteMetric_Type.__name__ = "Integer32"
_ApIpv4OspfIfAdvRouteMetric_Object = MibTableColumn
apIpv4OspfIfAdvRouteMetric = _ApIpv4OspfIfAdvRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 23, 1, 5),
    _ApIpv4OspfIfAdvRouteMetric_Type()
)
apIpv4OspfIfAdvRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4OspfIfAdvRouteMetric.setStatus("current")


class _ApIpv4OspfIfAdvRouteTag_Type(Integer32):
    """Custom type apIpv4OspfIfAdvRouteTag based on Integer32"""
    defaultValue = 0


_ApIpv4OspfIfAdvRouteTag_Object = MibTableColumn
apIpv4OspfIfAdvRouteTag = _ApIpv4OspfIfAdvRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 23, 1, 6),
    _ApIpv4OspfIfAdvRouteTag_Type()
)
apIpv4OspfIfAdvRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4OspfIfAdvRouteTag.setStatus("current")
_ApIpv4OspfIfAdvRouteStatus_Type = RowStatus
_ApIpv4OspfIfAdvRouteStatus_Object = MibTableColumn
apIpv4OspfIfAdvRouteStatus = _ApIpv4OspfIfAdvRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 23, 1, 7),
    _ApIpv4OspfIfAdvRouteStatus_Type()
)
apIpv4OspfIfAdvRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4OspfIfAdvRouteStatus.setStatus("current")


class _ApIpv4OspfEqualCostRoutes_Type(Integer32):
    """Custom type apIpv4OspfEqualCostRoutes based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ApIpv4OspfEqualCostRoutes_Type.__name__ = "Integer32"
_ApIpv4OspfEqualCostRoutes_Object = MibScalar
apIpv4OspfEqualCostRoutes = _ApIpv4OspfEqualCostRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 2, 24),
    _ApIpv4OspfEqualCostRoutes_Type()
)
apIpv4OspfEqualCostRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4OspfEqualCostRoutes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPV4-OSPF-MIB",
    **{"apIpv4OspfMib": apIpv4OspfMib,
       "apIpv4OspfRedistributeLocal": apIpv4OspfRedistributeLocal,
       "apIpv4OspfLocalType": apIpv4OspfLocalType,
       "apIpv4OspfLocalMetric": apIpv4OspfLocalMetric,
       "apIpv4OspfLocalTag": apIpv4OspfLocalTag,
       "apIpv4OspfRedistributeStatic": apIpv4OspfRedistributeStatic,
       "apIpv4OspfStaticType": apIpv4OspfStaticType,
       "apIpv4OspfStaticMetric": apIpv4OspfStaticMetric,
       "apIpv4OspfStaticTag": apIpv4OspfStaticTag,
       "apIpv4OspfRedistributeRip": apIpv4OspfRedistributeRip,
       "apIpv4OspfRipType": apIpv4OspfRipType,
       "apIpv4OspfRipMetric": apIpv4OspfRipMetric,
       "apIpv4OspfRipTag": apIpv4OspfRipTag,
       "apIpv4OspfOriginateDefault": apIpv4OspfOriginateDefault,
       "apIpv4OspfDefaultType": apIpv4OspfDefaultType,
       "apIpv4OspfDefaultMetric": apIpv4OspfDefaultMetric,
       "apIpv4OspfDefaultTag": apIpv4OspfDefaultTag,
       "apIpv4OspfRedistributeFirewall": apIpv4OspfRedistributeFirewall,
       "apIpv4OspfFirewallType": apIpv4OspfFirewallType,
       "apIpv4OspfFirewallMetric": apIpv4OspfFirewallMetric,
       "apIpv4OspfFirewallTag": apIpv4OspfFirewallTag,
       "apIpv4OspfAdvRouteTable": apIpv4OspfAdvRouteTable,
       "apIpv4OspfAdvRouteEntry": apIpv4OspfAdvRouteEntry,
       "apIpv4OspfAdvRoutePrefix": apIpv4OspfAdvRoutePrefix,
       "apIpv4OspfAdvRoutePrefixLen": apIpv4OspfAdvRoutePrefixLen,
       "apIpv4OspfAdvRouteType": apIpv4OspfAdvRouteType,
       "apIpv4OspfAdvRouteMetric": apIpv4OspfAdvRouteMetric,
       "apIpv4OspfAdvRouteTag": apIpv4OspfAdvRouteTag,
       "apIpv4OspfAdvRouteStatus": apIpv4OspfAdvRouteStatus,
       "apIpv4OspfIfAdvRouteTable": apIpv4OspfIfAdvRouteTable,
       "apIpv4OspfIfAdvRouteEntry": apIpv4OspfIfAdvRouteEntry,
       "apIpv4OspfIfAdvRouteAddress": apIpv4OspfIfAdvRouteAddress,
       "apIpv4OspfIfAdvRoutePrefix": apIpv4OspfIfAdvRoutePrefix,
       "apIpv4OspfIfAdvRoutePrefixLen": apIpv4OspfIfAdvRoutePrefixLen,
       "apIpv4OspfIfAdvRouteType": apIpv4OspfIfAdvRouteType,
       "apIpv4OspfIfAdvRouteMetric": apIpv4OspfIfAdvRouteMetric,
       "apIpv4OspfIfAdvRouteTag": apIpv4OspfIfAdvRouteTag,
       "apIpv4OspfIfAdvRouteStatus": apIpv4OspfIfAdvRouteStatus,
       "apIpv4OspfEqualCostRoutes": apIpv4OspfEqualCostRoutes}
)

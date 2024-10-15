# SNMP MIB module (Wellfleet-IPV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-IPV6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:30 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(wfIpv6Group,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfIpv6Group")


# MODULE-IDENTITY


# Types definitions



class Ipv6Address(OctetString):
    """Custom type Ipv6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )





class Ipv6AddressPrefix(OctetString):
    """Custom type Ipv6AddressPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfIpv6RoutingGroup_ObjectIdentity = ObjectIdentity
wfIpv6RoutingGroup = _WfIpv6RoutingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1)
)
_WfIpv6RoutingGeneralGroup_ObjectIdentity = ObjectIdentity
wfIpv6RoutingGeneralGroup = _WfIpv6RoutingGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1)
)
_WfIpv6Base_ObjectIdentity = ObjectIdentity
wfIpv6Base = _WfIpv6Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 1)
)


class _WfIpv6BaseDelete_Type(Integer32):
    """Custom type wfIpv6BaseDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIpv6BaseDelete_Type.__name__ = "Integer32"
_WfIpv6BaseDelete_Object = MibScalar
wfIpv6BaseDelete = _WfIpv6BaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 1, 1),
    _WfIpv6BaseDelete_Type()
)
wfIpv6BaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6BaseDelete.setStatus("mandatory")


class _WfIpv6BaseDisable_Type(Integer32):
    """Custom type wfIpv6BaseDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpv6BaseDisable_Type.__name__ = "Integer32"
_WfIpv6BaseDisable_Object = MibScalar
wfIpv6BaseDisable = _WfIpv6BaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 1, 2),
    _WfIpv6BaseDisable_Type()
)
wfIpv6BaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6BaseDisable.setStatus("mandatory")


class _WfIpv6BaseState_Type(Integer32):
    """Custom type wfIpv6BaseState based on Integer32"""
    defaultValue = 5

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
        *(("down", 2),
          ("init", 3),
          ("invalid", 4),
          ("notpres", 5),
          ("up", 1))
    )


_WfIpv6BaseState_Type.__name__ = "Integer32"
_WfIpv6BaseState_Object = MibScalar
wfIpv6BaseState = _WfIpv6BaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 1, 3),
    _WfIpv6BaseState_Type()
)
wfIpv6BaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6BaseState.setStatus("mandatory")


class _WfIpv6BaseForwarding_Type(Integer32):
    """Custom type wfIpv6BaseForwarding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notforwarding", 2))
    )


_WfIpv6BaseForwarding_Type.__name__ = "Integer32"
_WfIpv6BaseForwarding_Object = MibScalar
wfIpv6BaseForwarding = _WfIpv6BaseForwarding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 1, 4),
    _WfIpv6BaseForwarding_Type()
)
wfIpv6BaseForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6BaseForwarding.setStatus("mandatory")


class _WfIpv6BaseDefaultHopLimit_Type(Integer32):
    """Custom type wfIpv6BaseDefaultHopLimit based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfIpv6BaseDefaultHopLimit_Type.__name__ = "Integer32"
_WfIpv6BaseDefaultHopLimit_Object = MibScalar
wfIpv6BaseDefaultHopLimit = _WfIpv6BaseDefaultHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 1, 5),
    _WfIpv6BaseDefaultHopLimit_Type()
)
wfIpv6BaseDefaultHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6BaseDefaultHopLimit.setStatus("mandatory")


class _WfIpv6BaseMinLinkMTU_Type(Integer32):
    """Custom type wfIpv6BaseMinLinkMTU based on Integer32"""
    defaultValue = 576

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(296, 65535),
    )


_WfIpv6BaseMinLinkMTU_Type.__name__ = "Integer32"
_WfIpv6BaseMinLinkMTU_Object = MibScalar
wfIpv6BaseMinLinkMTU = _WfIpv6BaseMinLinkMTU_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 1, 6),
    _WfIpv6BaseMinLinkMTU_Type()
)
wfIpv6BaseMinLinkMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6BaseMinLinkMTU.setStatus("mandatory")


class _WfIpv6BaseMTUDiscovery_Type(Integer32):
    """Custom type wfIpv6BaseMTUDiscovery based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpv6BaseMTUDiscovery_Type.__name__ = "Integer32"
_WfIpv6BaseMTUDiscovery_Object = MibScalar
wfIpv6BaseMTUDiscovery = _WfIpv6BaseMTUDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 1, 7),
    _WfIpv6BaseMTUDiscovery_Type()
)
wfIpv6BaseMTUDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6BaseMTUDiscovery.setStatus("mandatory")


class _WfIpv6BaseMTUTimeout_Type(Integer32):
    """Custom type wfIpv6BaseMTUTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 71582788),
    )


_WfIpv6BaseMTUTimeout_Type.__name__ = "Integer32"
_WfIpv6BaseMTUTimeout_Object = MibScalar
wfIpv6BaseMTUTimeout = _WfIpv6BaseMTUTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 1, 8),
    _WfIpv6BaseMTUTimeout_Type()
)
wfIpv6BaseMTUTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6BaseMTUTimeout.setStatus("mandatory")
_WfIpv6BaseIfNumber_Type = Integer32
_WfIpv6BaseIfNumber_Object = MibScalar
wfIpv6BaseIfNumber = _WfIpv6BaseIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 1, 9),
    _WfIpv6BaseIfNumber_Type()
)
wfIpv6BaseIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6BaseIfNumber.setStatus("mandatory")
_WfIpv6BaseNetworks_Type = Integer32
_WfIpv6BaseNetworks_Object = MibScalar
wfIpv6BaseNetworks = _WfIpv6BaseNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 1, 10),
    _WfIpv6BaseNetworks_Type()
)
wfIpv6BaseNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6BaseNetworks.setStatus("mandatory")
_WfIpv6BaseNodes_Type = Integer32
_WfIpv6BaseNodes_Object = MibScalar
wfIpv6BaseNodes = _WfIpv6BaseNodes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 1, 11),
    _WfIpv6BaseNodes_Type()
)
wfIpv6BaseNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6BaseNodes.setStatus("mandatory")


class _WfIpv6BaseHighestFilterRule_Type(Integer32):
    """Custom type wfIpv6BaseHighestFilterRule based on Integer32"""
    defaultValue = 31

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfIpv6BaseHighestFilterRule_Type.__name__ = "Integer32"
_WfIpv6BaseHighestFilterRule_Object = MibScalar
wfIpv6BaseHighestFilterRule = _WfIpv6BaseHighestFilterRule_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 1, 12),
    _WfIpv6BaseHighestFilterRule_Type()
)
wfIpv6BaseHighestFilterRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6BaseHighestFilterRule.setStatus("mandatory")
_WfIpv6IfTable_Object = MibTable
wfIpv6IfTable = _WfIpv6IfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wfIpv6IfTable.setStatus("mandatory")
_WfIpv6IfEntry_Object = MibTableRow
wfIpv6IfEntry = _WfIpv6IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1)
)
wfIpv6IfEntry.setIndexNames(
    (0, "Wellfleet-IPV6-MIB", "wfIpv6IfIndex"),
)
if mibBuilder.loadTexts:
    wfIpv6IfEntry.setStatus("mandatory")


class _WfIpv6IfDelete_Type(Integer32):
    """Custom type wfIpv6IfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpv6IfDelete_Type.__name__ = "Integer32"
_WfIpv6IfDelete_Object = MibTableColumn
wfIpv6IfDelete = _WfIpv6IfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 1),
    _WfIpv6IfDelete_Type()
)
wfIpv6IfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfDelete.setStatus("mandatory")


class _WfIpv6IfDisable_Type(Integer32):
    """Custom type wfIpv6IfDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpv6IfDisable_Type.__name__ = "Integer32"
_WfIpv6IfDisable_Object = MibTableColumn
wfIpv6IfDisable = _WfIpv6IfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 2),
    _WfIpv6IfDisable_Type()
)
wfIpv6IfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfDisable.setStatus("mandatory")


class _WfIpv6IfState_Type(Integer32):
    """Custom type wfIpv6IfState based on Integer32"""
    defaultValue = 6

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
        *(("down", 3),
          ("init", 4),
          ("invalid", 5),
          ("notpres", 6),
          ("tokenless", 2),
          ("up", 1))
    )


_WfIpv6IfState_Type.__name__ = "Integer32"
_WfIpv6IfState_Object = MibTableColumn
wfIpv6IfState = _WfIpv6IfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 3),
    _WfIpv6IfState_Type()
)
wfIpv6IfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfState.setStatus("mandatory")
_WfIpv6IfIndex_Type = Integer32
_WfIpv6IfIndex_Object = MibTableColumn
wfIpv6IfIndex = _WfIpv6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 4),
    _WfIpv6IfIndex_Type()
)
wfIpv6IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfIndex.setStatus("mandatory")


class _WfIpv6IfDescr_Type(DisplayString):
    """Custom type wfIpv6IfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WfIpv6IfDescr_Type.__name__ = "DisplayString"
_WfIpv6IfDescr_Object = MibTableColumn
wfIpv6IfDescr = _WfIpv6IfDescr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 5),
    _WfIpv6IfDescr_Type()
)
wfIpv6IfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfDescr.setStatus("mandatory")
_WfIpv6IfCircuit_Type = Integer32
_WfIpv6IfCircuit_Object = MibTableColumn
wfIpv6IfCircuit = _WfIpv6IfCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 6),
    _WfIpv6IfCircuit_Type()
)
wfIpv6IfCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfCircuit.setStatus("mandatory")


class _WfIpv6IfCfgToken_Type(OctetString):
    """Custom type wfIpv6IfCfgToken based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_WfIpv6IfCfgToken_Type.__name__ = "OctetString"
_WfIpv6IfCfgToken_Object = MibTableColumn
wfIpv6IfCfgToken = _WfIpv6IfCfgToken_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 7),
    _WfIpv6IfCfgToken_Type()
)
wfIpv6IfCfgToken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfCfgToken.setStatus("mandatory")


class _WfIpv6IfCfgTokenLength_Type(Integer32):
    """Custom type wfIpv6IfCfgTokenLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_WfIpv6IfCfgTokenLength_Type.__name__ = "Integer32"
_WfIpv6IfCfgTokenLength_Object = MibTableColumn
wfIpv6IfCfgTokenLength = _WfIpv6IfCfgTokenLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 8),
    _WfIpv6IfCfgTokenLength_Type()
)
wfIpv6IfCfgTokenLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfCfgTokenLength.setStatus("mandatory")
_WfIpv6IfToken_Type = OctetString
_WfIpv6IfToken_Object = MibTableColumn
wfIpv6IfToken = _WfIpv6IfToken_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 9),
    _WfIpv6IfToken_Type()
)
wfIpv6IfToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfToken.setStatus("mandatory")


class _WfIpv6IfTokenLength_Type(Integer32):
    """Custom type wfIpv6IfTokenLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_WfIpv6IfTokenLength_Type.__name__ = "Integer32"
_WfIpv6IfTokenLength_Object = MibTableColumn
wfIpv6IfTokenLength = _WfIpv6IfTokenLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 10),
    _WfIpv6IfTokenLength_Type()
)
wfIpv6IfTokenLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfTokenLength.setStatus("mandatory")
_WfIpv6IfCfgPhysicalAddress_Type = PhysAddress
_WfIpv6IfCfgPhysicalAddress_Object = MibTableColumn
wfIpv6IfCfgPhysicalAddress = _WfIpv6IfCfgPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 11),
    _WfIpv6IfCfgPhysicalAddress_Type()
)
wfIpv6IfCfgPhysicalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfCfgPhysicalAddress.setStatus("mandatory")
_WfIpv6IfPhysicalAddress_Type = PhysAddress
_WfIpv6IfPhysicalAddress_Object = MibTableColumn
wfIpv6IfPhysicalAddress = _WfIpv6IfPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 12),
    _WfIpv6IfPhysicalAddress_Type()
)
wfIpv6IfPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfPhysicalAddress.setStatus("mandatory")


class _WfIpv6IfCfgLinkMTU_Type(Integer32):
    """Custom type wfIpv6IfCfgLinkMTU based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfIpv6IfCfgLinkMTU_Type.__name__ = "Integer32"
_WfIpv6IfCfgLinkMTU_Object = MibTableColumn
wfIpv6IfCfgLinkMTU = _WfIpv6IfCfgLinkMTU_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 13),
    _WfIpv6IfCfgLinkMTU_Type()
)
wfIpv6IfCfgLinkMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfCfgLinkMTU.setStatus("mandatory")


class _WfIpv6IfFwdCacheSize_Type(Integer32):
    """Custom type wfIpv6IfFwdCacheSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20480),
    )


_WfIpv6IfFwdCacheSize_Type.__name__ = "Integer32"
_WfIpv6IfFwdCacheSize_Object = MibTableColumn
wfIpv6IfFwdCacheSize = _WfIpv6IfFwdCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 14),
    _WfIpv6IfFwdCacheSize_Type()
)
wfIpv6IfFwdCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfFwdCacheSize.setStatus("mandatory")


class _WfIpv6IfSlotMask_Type(Gauge32):
    """Custom type wfIpv6IfSlotMask based on Gauge32"""
    defaultValue = 4294705152


_WfIpv6IfSlotMask_Object = MibTableColumn
wfIpv6IfSlotMask = _WfIpv6IfSlotMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 15),
    _WfIpv6IfSlotMask_Type()
)
wfIpv6IfSlotMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfSlotMask.setStatus("mandatory")
_WfIpv6IfLastChange_Type = TimeTicks
_WfIpv6IfLastChange_Object = MibTableColumn
wfIpv6IfLastChange = _WfIpv6IfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 16),
    _WfIpv6IfLastChange_Type()
)
wfIpv6IfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfLastChange.setStatus("mandatory")
_WfIpv6IfReasmMaxSize_Type = Integer32
_WfIpv6IfReasmMaxSize_Object = MibTableColumn
wfIpv6IfReasmMaxSize = _WfIpv6IfReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 17),
    _WfIpv6IfReasmMaxSize_Type()
)
wfIpv6IfReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfReasmMaxSize.setStatus("mandatory")
_WfIpv6IfMaxInfo_Type = Integer32
_WfIpv6IfMaxInfo_Object = MibTableColumn
wfIpv6IfMaxInfo = _WfIpv6IfMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 18),
    _WfIpv6IfMaxInfo_Type()
)
wfIpv6IfMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfMaxInfo.setStatus("mandatory")


class _WfIpv6IfRedirect_Type(Integer32):
    """Custom type wfIpv6IfRedirect based on Integer32"""
    defaultValue = 1

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


_WfIpv6IfRedirect_Type.__name__ = "Integer32"
_WfIpv6IfRedirect_Object = MibTableColumn
wfIpv6IfRedirect = _WfIpv6IfRedirect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 19),
    _WfIpv6IfRedirect_Type()
)
wfIpv6IfRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfRedirect.setStatus("mandatory")


class _WfIpv6IfIcmpErrorLimit_Type(Integer32):
    """Custom type wfIpv6IfIcmpErrorLimit based on Integer32"""
    defaultValue = 100


_WfIpv6IfIcmpErrorLimit_Object = MibTableColumn
wfIpv6IfIcmpErrorLimit = _WfIpv6IfIcmpErrorLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 20),
    _WfIpv6IfIcmpErrorLimit_Type()
)
wfIpv6IfIcmpErrorLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfIcmpErrorLimit.setStatus("mandatory")


class _WfIpv6IfTrEndStation_Type(Integer32):
    """Custom type wfIpv6IfTrEndStation based on Integer32"""
    defaultValue = 2

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


_WfIpv6IfTrEndStation_Type.__name__ = "Integer32"
_WfIpv6IfTrEndStation_Object = MibTableColumn
wfIpv6IfTrEndStation = _WfIpv6IfTrEndStation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 21),
    _WfIpv6IfTrEndStation_Type()
)
wfIpv6IfTrEndStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfTrEndStation.setStatus("mandatory")
_WfIpv6IfSMDSGroupAddress_Type = OctetString
_WfIpv6IfSMDSGroupAddress_Object = MibTableColumn
wfIpv6IfSMDSGroupAddress = _WfIpv6IfSMDSGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 22),
    _WfIpv6IfSMDSGroupAddress_Type()
)
wfIpv6IfSMDSGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfSMDSGroupAddress.setStatus("mandatory")
_WfIpv6IfFRBcastDlci_Type = Integer32
_WfIpv6IfFRBcastDlci_Object = MibTableColumn
wfIpv6IfFRBcastDlci = _WfIpv6IfFRBcastDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 23),
    _WfIpv6IfFRBcastDlci_Type()
)
wfIpv6IfFRBcastDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfFRBcastDlci.setStatus("mandatory")
_WfIpv6IfFRMcast1Dlci_Type = Integer32
_WfIpv6IfFRMcast1Dlci_Object = MibTableColumn
wfIpv6IfFRMcast1Dlci = _WfIpv6IfFRMcast1Dlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 24),
    _WfIpv6IfFRMcast1Dlci_Type()
)
wfIpv6IfFRMcast1Dlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfFRMcast1Dlci.setStatus("mandatory")
_WfIpv6IfFRMcast2Dlci_Type = Integer32
_WfIpv6IfFRMcast2Dlci_Object = MibTableColumn
wfIpv6IfFRMcast2Dlci = _WfIpv6IfFRMcast2Dlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 25),
    _WfIpv6IfFRMcast2Dlci_Type()
)
wfIpv6IfFRMcast2Dlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfFRMcast2Dlci.setStatus("mandatory")


class _WfIpv6IfTunnelProtocol_Type(Integer32):
    """Custom type wfIpv6IfTunnelProtocol based on Integer32"""
    defaultValue = 1

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
        *(("ip4au", 5),
          ("ip4sa", 3),
          ("ip4st", 1),
          ("ip6au", 6),
          ("ip6sa", 4),
          ("ip6st", 2))
    )


_WfIpv6IfTunnelProtocol_Type.__name__ = "Integer32"
_WfIpv6IfTunnelProtocol_Object = MibTableColumn
wfIpv6IfTunnelProtocol = _WfIpv6IfTunnelProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 26),
    _WfIpv6IfTunnelProtocol_Type()
)
wfIpv6IfTunnelProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfTunnelProtocol.setStatus("mandatory")
_WfIpv6IfIPv4TunnelLocalAddress_Type = IpAddress
_WfIpv6IfIPv4TunnelLocalAddress_Object = MibTableColumn
wfIpv6IfIPv4TunnelLocalAddress = _WfIpv6IfIPv4TunnelLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 27),
    _WfIpv6IfIPv4TunnelLocalAddress_Type()
)
wfIpv6IfIPv4TunnelLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfIPv4TunnelLocalAddress.setStatus("mandatory")
_WfIpv6IfIPv4TunnelRemoteAddress_Type = IpAddress
_WfIpv6IfIPv4TunnelRemoteAddress_Object = MibTableColumn
wfIpv6IfIPv4TunnelRemoteAddress = _WfIpv6IfIPv4TunnelRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 28),
    _WfIpv6IfIPv4TunnelRemoteAddress_Type()
)
wfIpv6IfIPv4TunnelRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfIPv4TunnelRemoteAddress.setStatus("mandatory")


class _WfIpv6IfIpv6TunnelIfIndex_Type(Integer32):
    """Custom type wfIpv6IfIpv6TunnelIfIndex based on Integer32"""
    defaultValue = 0


_WfIpv6IfIpv6TunnelIfIndex_Object = MibTableColumn
wfIpv6IfIpv6TunnelIfIndex = _WfIpv6IfIpv6TunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 29),
    _WfIpv6IfIpv6TunnelIfIndex_Type()
)
wfIpv6IfIpv6TunnelIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfIpv6TunnelIfIndex.setStatus("mandatory")
_WfIpv6IfIpv6TunnelRemoteAddress_Type = Ipv6Address
_WfIpv6IfIpv6TunnelRemoteAddress_Object = MibTableColumn
wfIpv6IfIpv6TunnelRemoteAddress = _WfIpv6IfIpv6TunnelRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 2, 1, 30),
    _WfIpv6IfIpv6TunnelRemoteAddress_Type()
)
wfIpv6IfIpv6TunnelRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6IfIpv6TunnelRemoteAddress.setStatus("mandatory")
_WfIpv6AddrPrefixTable_Object = MibTable
wfIpv6AddrPrefixTable = _WfIpv6AddrPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wfIpv6AddrPrefixTable.setStatus("mandatory")
_WfIpv6AddrPrefixEntry_Object = MibTableRow
wfIpv6AddrPrefixEntry = _WfIpv6AddrPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 3, 1)
)
wfIpv6AddrPrefixEntry.setIndexNames(
    (0, "Wellfleet-IPV6-MIB", "wfIpv6AddrPrefixIfIndex"),
    (0, "Wellfleet-IPV6-MIB", "wfIpv6AddrPrefixIndex"),
)
if mibBuilder.loadTexts:
    wfIpv6AddrPrefixEntry.setStatus("mandatory")


class _WfIpv6AddrPrefixDelete_Type(Integer32):
    """Custom type wfIpv6AddrPrefixDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpv6AddrPrefixDelete_Type.__name__ = "Integer32"
_WfIpv6AddrPrefixDelete_Object = MibTableColumn
wfIpv6AddrPrefixDelete = _WfIpv6AddrPrefixDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 3, 1, 1),
    _WfIpv6AddrPrefixDelete_Type()
)
wfIpv6AddrPrefixDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6AddrPrefixDelete.setStatus("mandatory")


class _WfIpv6AddrPrefixDisable_Type(Integer32):
    """Custom type wfIpv6AddrPrefixDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpv6AddrPrefixDisable_Type.__name__ = "Integer32"
_WfIpv6AddrPrefixDisable_Object = MibTableColumn
wfIpv6AddrPrefixDisable = _WfIpv6AddrPrefixDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 3, 1, 2),
    _WfIpv6AddrPrefixDisable_Type()
)
wfIpv6AddrPrefixDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6AddrPrefixDisable.setStatus("mandatory")
_WfIpv6AddrPrefixIfIndex_Type = Integer32
_WfIpv6AddrPrefixIfIndex_Object = MibTableColumn
wfIpv6AddrPrefixIfIndex = _WfIpv6AddrPrefixIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 3, 1, 3),
    _WfIpv6AddrPrefixIfIndex_Type()
)
wfIpv6AddrPrefixIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6AddrPrefixIfIndex.setStatus("mandatory")
_WfIpv6AddrPrefixIndex_Type = Integer32
_WfIpv6AddrPrefixIndex_Object = MibTableColumn
wfIpv6AddrPrefixIndex = _WfIpv6AddrPrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 3, 1, 4),
    _WfIpv6AddrPrefixIndex_Type()
)
wfIpv6AddrPrefixIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6AddrPrefixIndex.setStatus("mandatory")
_WfIpv6AddrPrefix_Type = Ipv6AddressPrefix
_WfIpv6AddrPrefix_Object = MibTableColumn
wfIpv6AddrPrefix = _WfIpv6AddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 3, 1, 5),
    _WfIpv6AddrPrefix_Type()
)
wfIpv6AddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6AddrPrefix.setStatus("mandatory")


class _WfIpv6AddrPrefixLength_Type(Integer32):
    """Custom type wfIpv6AddrPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 128),
    )


_WfIpv6AddrPrefixLength_Type.__name__ = "Integer32"
_WfIpv6AddrPrefixLength_Object = MibTableColumn
wfIpv6AddrPrefixLength = _WfIpv6AddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 3, 1, 6),
    _WfIpv6AddrPrefixLength_Type()
)
wfIpv6AddrPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6AddrPrefixLength.setStatus("mandatory")


class _WfIpv6AddrPrefixPreference_Type(Integer32):
    """Custom type wfIpv6AddrPrefixPreference based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfIpv6AddrPrefixPreference_Type.__name__ = "Integer32"
_WfIpv6AddrPrefixPreference_Object = MibTableColumn
wfIpv6AddrPrefixPreference = _WfIpv6AddrPrefixPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 3, 1, 7),
    _WfIpv6AddrPrefixPreference_Type()
)
wfIpv6AddrPrefixPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6AddrPrefixPreference.setStatus("mandatory")


class _WfIpv6AddrPrefixCost_Type(Integer32):
    """Custom type wfIpv6AddrPrefixCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_WfIpv6AddrPrefixCost_Type.__name__ = "Integer32"
_WfIpv6AddrPrefixCost_Object = MibTableColumn
wfIpv6AddrPrefixCost = _WfIpv6AddrPrefixCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 3, 1, 8),
    _WfIpv6AddrPrefixCost_Type()
)
wfIpv6AddrPrefixCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6AddrPrefixCost.setStatus("mandatory")


class _WfIpv6AddrPrefixOnLinkFlag_Type(Integer32):
    """Custom type wfIpv6AddrPrefixOnLinkFlag based on Integer32"""
    defaultValue = 1

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


_WfIpv6AddrPrefixOnLinkFlag_Type.__name__ = "Integer32"
_WfIpv6AddrPrefixOnLinkFlag_Object = MibTableColumn
wfIpv6AddrPrefixOnLinkFlag = _WfIpv6AddrPrefixOnLinkFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 3, 1, 9),
    _WfIpv6AddrPrefixOnLinkFlag_Type()
)
wfIpv6AddrPrefixOnLinkFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6AddrPrefixOnLinkFlag.setStatus("mandatory")


class _WfIpv6AddrPrefixAutonomousFlag_Type(Integer32):
    """Custom type wfIpv6AddrPrefixAutonomousFlag based on Integer32"""
    defaultValue = 1

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


_WfIpv6AddrPrefixAutonomousFlag_Type.__name__ = "Integer32"
_WfIpv6AddrPrefixAutonomousFlag_Object = MibTableColumn
wfIpv6AddrPrefixAutonomousFlag = _WfIpv6AddrPrefixAutonomousFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 3, 1, 10),
    _WfIpv6AddrPrefixAutonomousFlag_Type()
)
wfIpv6AddrPrefixAutonomousFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6AddrPrefixAutonomousFlag.setStatus("mandatory")


class _WfIpv6AddrPrefixAdvPreferredLifetime_Type(Integer32):
    """Custom type wfIpv6AddrPrefixAdvPreferredLifetime based on Integer32"""
    defaultValue = 604800


_WfIpv6AddrPrefixAdvPreferredLifetime_Object = MibTableColumn
wfIpv6AddrPrefixAdvPreferredLifetime = _WfIpv6AddrPrefixAdvPreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 3, 1, 11),
    _WfIpv6AddrPrefixAdvPreferredLifetime_Type()
)
wfIpv6AddrPrefixAdvPreferredLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6AddrPrefixAdvPreferredLifetime.setStatus("mandatory")


class _WfIpv6AddrPrefixAdvValidLifetime_Type(Integer32):
    """Custom type wfIpv6AddrPrefixAdvValidLifetime based on Integer32"""
    defaultValue = -1


_WfIpv6AddrPrefixAdvValidLifetime_Object = MibTableColumn
wfIpv6AddrPrefixAdvValidLifetime = _WfIpv6AddrPrefixAdvValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 3, 1, 12),
    _WfIpv6AddrPrefixAdvValidLifetime_Type()
)
wfIpv6AddrPrefixAdvValidLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6AddrPrefixAdvValidLifetime.setStatus("mandatory")


class _WfIpv6AddrPrefixInvalid_Type(Integer32):
    """Custom type wfIpv6AddrPrefixInvalid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_WfIpv6AddrPrefixInvalid_Type.__name__ = "Integer32"
_WfIpv6AddrPrefixInvalid_Object = MibTableColumn
wfIpv6AddrPrefixInvalid = _WfIpv6AddrPrefixInvalid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 3, 1, 13),
    _WfIpv6AddrPrefixInvalid_Type()
)
wfIpv6AddrPrefixInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6AddrPrefixInvalid.setStatus("mandatory")


class _WfIpv6AddrPrefixAnycast_Type(Integer32):
    """Custom type wfIpv6AddrPrefixAnycast based on Integer32"""
    defaultValue = 2

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


_WfIpv6AddrPrefixAnycast_Type.__name__ = "Integer32"
_WfIpv6AddrPrefixAnycast_Object = MibTableColumn
wfIpv6AddrPrefixAnycast = _WfIpv6AddrPrefixAnycast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 3, 1, 14),
    _WfIpv6AddrPrefixAnycast_Type()
)
wfIpv6AddrPrefixAnycast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6AddrPrefixAnycast.setStatus("mandatory")
_WfIpv6AddrTable_Object = MibTable
wfIpv6AddrTable = _WfIpv6AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wfIpv6AddrTable.setStatus("mandatory")
_WfIpv6AddrEntry_Object = MibTableRow
wfIpv6AddrEntry = _WfIpv6AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 4, 1)
)
wfIpv6AddrEntry.setIndexNames(
    (0, "Wellfleet-IPV6-MIB", "wfIpv6AddrIfIndex"),
    (0, "Wellfleet-IPV6-MIB", "wfIpv6AddrAddress"),
)
if mibBuilder.loadTexts:
    wfIpv6AddrEntry.setStatus("mandatory")
_WfIpv6AddrIfIndex_Type = Integer32
_WfIpv6AddrIfIndex_Object = MibTableColumn
wfIpv6AddrIfIndex = _WfIpv6AddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 4, 1, 1),
    _WfIpv6AddrIfIndex_Type()
)
wfIpv6AddrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6AddrIfIndex.setStatus("mandatory")
_WfIpv6AddrAddress_Type = Ipv6Address
_WfIpv6AddrAddress_Object = MibTableColumn
wfIpv6AddrAddress = _WfIpv6AddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 4, 1, 2),
    _WfIpv6AddrAddress_Type()
)
wfIpv6AddrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6AddrAddress.setStatus("mandatory")
_WfIpv6AddrPfxLength_Type = Integer32
_WfIpv6AddrPfxLength_Object = MibTableColumn
wfIpv6AddrPfxLength = _WfIpv6AddrPfxLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 4, 1, 3),
    _WfIpv6AddrPfxLength_Type()
)
wfIpv6AddrPfxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6AddrPfxLength.setStatus("mandatory")


class _WfIpv6AddrType_Type(Integer32):
    """Custom type wfIpv6AddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stateful", 2),
          ("stateless", 1),
          ("unknown", 3))
    )


_WfIpv6AddrType_Type.__name__ = "Integer32"
_WfIpv6AddrType_Object = MibTableColumn
wfIpv6AddrType = _WfIpv6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 4, 1, 4),
    _WfIpv6AddrType_Type()
)
wfIpv6AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6AddrType.setStatus("mandatory")


class _WfIpv6AddrAnycastFlag_Type(Integer32):
    """Custom type wfIpv6AddrAnycastFlag based on Integer32"""
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


_WfIpv6AddrAnycastFlag_Type.__name__ = "Integer32"
_WfIpv6AddrAnycastFlag_Object = MibTableColumn
wfIpv6AddrAnycastFlag = _WfIpv6AddrAnycastFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 4, 1, 5),
    _WfIpv6AddrAnycastFlag_Type()
)
wfIpv6AddrAnycastFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6AddrAnycastFlag.setStatus("mandatory")


class _WfIpv6AddrStatus_Type(Integer32):
    """Custom type wfIpv6AddrStatus based on Integer32"""
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
        *(("deprecated", 2),
          ("inaccessible", 4),
          ("invalid", 3),
          ("preferred", 1),
          ("unknown", 5))
    )


_WfIpv6AddrStatus_Type.__name__ = "Integer32"
_WfIpv6AddrStatus_Object = MibTableColumn
wfIpv6AddrStatus = _WfIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 4, 1, 6),
    _WfIpv6AddrStatus_Type()
)
wfIpv6AddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6AddrStatus.setStatus("mandatory")
_WfIpv6IfStatsTable_Object = MibTable
wfIpv6IfStatsTable = _WfIpv6IfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wfIpv6IfStatsTable.setStatus("mandatory")
_WfIpv6IfStatsEntry_Object = MibTableRow
wfIpv6IfStatsEntry = _WfIpv6IfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1)
)
wfIpv6IfStatsEntry.setIndexNames(
    (0, "Wellfleet-IPV6-MIB", "wfIpv6IfStatsIfIndex"),
)
if mibBuilder.loadTexts:
    wfIpv6IfStatsEntry.setStatus("mandatory")
_WfIpv6IfStatsIfIndex_Type = Integer32
_WfIpv6IfStatsIfIndex_Object = MibTableColumn
wfIpv6IfStatsIfIndex = _WfIpv6IfStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 1),
    _WfIpv6IfStatsIfIndex_Type()
)
wfIpv6IfStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsIfIndex.setStatus("mandatory")
_WfIpv6IfStatsInReceives_Type = Counter32
_WfIpv6IfStatsInReceives_Object = MibTableColumn
wfIpv6IfStatsInReceives = _WfIpv6IfStatsInReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 2),
    _WfIpv6IfStatsInReceives_Type()
)
wfIpv6IfStatsInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsInReceives.setStatus("mandatory")
_WfIpv6IfStatsInHdrErrors_Type = Counter32
_WfIpv6IfStatsInHdrErrors_Object = MibTableColumn
wfIpv6IfStatsInHdrErrors = _WfIpv6IfStatsInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 3),
    _WfIpv6IfStatsInHdrErrors_Type()
)
wfIpv6IfStatsInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsInHdrErrors.setStatus("mandatory")
_WfIpv6IfStatsInTooBigErrors_Type = Counter32
_WfIpv6IfStatsInTooBigErrors_Object = MibTableColumn
wfIpv6IfStatsInTooBigErrors = _WfIpv6IfStatsInTooBigErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 4),
    _WfIpv6IfStatsInTooBigErrors_Type()
)
wfIpv6IfStatsInTooBigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsInTooBigErrors.setStatus("mandatory")
_WfIpv6IfStatsInNoRoutes_Type = Counter32
_WfIpv6IfStatsInNoRoutes_Object = MibTableColumn
wfIpv6IfStatsInNoRoutes = _WfIpv6IfStatsInNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 5),
    _WfIpv6IfStatsInNoRoutes_Type()
)
wfIpv6IfStatsInNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsInNoRoutes.setStatus("mandatory")
_WfIpv6IfStatsInAddrErrors_Type = Counter32
_WfIpv6IfStatsInAddrErrors_Object = MibTableColumn
wfIpv6IfStatsInAddrErrors = _WfIpv6IfStatsInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 6),
    _WfIpv6IfStatsInAddrErrors_Type()
)
wfIpv6IfStatsInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsInAddrErrors.setStatus("mandatory")
_WfIpv6IfStatsInUnknownProtos_Type = Counter32
_WfIpv6IfStatsInUnknownProtos_Object = MibTableColumn
wfIpv6IfStatsInUnknownProtos = _WfIpv6IfStatsInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 7),
    _WfIpv6IfStatsInUnknownProtos_Type()
)
wfIpv6IfStatsInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsInUnknownProtos.setStatus("mandatory")
_WfIpv6IfStatsInDiscards_Type = Counter32
_WfIpv6IfStatsInDiscards_Object = MibTableColumn
wfIpv6IfStatsInDiscards = _WfIpv6IfStatsInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 8),
    _WfIpv6IfStatsInDiscards_Type()
)
wfIpv6IfStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsInDiscards.setStatus("mandatory")
_WfIpv6IfStatsInDelivers_Type = Counter32
_WfIpv6IfStatsInDelivers_Object = MibTableColumn
wfIpv6IfStatsInDelivers = _WfIpv6IfStatsInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 9),
    _WfIpv6IfStatsInDelivers_Type()
)
wfIpv6IfStatsInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsInDelivers.setStatus("mandatory")
_WfIpv6IfStatsForwDatagrams_Type = Counter32
_WfIpv6IfStatsForwDatagrams_Object = MibTableColumn
wfIpv6IfStatsForwDatagrams = _WfIpv6IfStatsForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 10),
    _WfIpv6IfStatsForwDatagrams_Type()
)
wfIpv6IfStatsForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsForwDatagrams.setStatus("mandatory")
_WfIpv6IfStatsOutRequests_Type = Counter32
_WfIpv6IfStatsOutRequests_Object = MibTableColumn
wfIpv6IfStatsOutRequests = _WfIpv6IfStatsOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 11),
    _WfIpv6IfStatsOutRequests_Type()
)
wfIpv6IfStatsOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsOutRequests.setStatus("mandatory")
_WfIpv6IfStatsOutDiscards_Type = Counter32
_WfIpv6IfStatsOutDiscards_Object = MibTableColumn
wfIpv6IfStatsOutDiscards = _WfIpv6IfStatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 12),
    _WfIpv6IfStatsOutDiscards_Type()
)
wfIpv6IfStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsOutDiscards.setStatus("mandatory")
_WfIpv6IfStatsFragOKs_Type = Counter32
_WfIpv6IfStatsFragOKs_Object = MibTableColumn
wfIpv6IfStatsFragOKs = _WfIpv6IfStatsFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 13),
    _WfIpv6IfStatsFragOKs_Type()
)
wfIpv6IfStatsFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsFragOKs.setStatus("mandatory")
_WfIpv6IfStatsFragFails_Type = Counter32
_WfIpv6IfStatsFragFails_Object = MibTableColumn
wfIpv6IfStatsFragFails = _WfIpv6IfStatsFragFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 14),
    _WfIpv6IfStatsFragFails_Type()
)
wfIpv6IfStatsFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsFragFails.setStatus("mandatory")
_WfIpv6IfStatsFragCreates_Type = Counter32
_WfIpv6IfStatsFragCreates_Object = MibTableColumn
wfIpv6IfStatsFragCreates = _WfIpv6IfStatsFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 15),
    _WfIpv6IfStatsFragCreates_Type()
)
wfIpv6IfStatsFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsFragCreates.setStatus("mandatory")
_WfIpv6IfStatsCacheMisses_Type = Counter32
_WfIpv6IfStatsCacheMisses_Object = MibTableColumn
wfIpv6IfStatsCacheMisses = _WfIpv6IfStatsCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 16),
    _WfIpv6IfStatsCacheMisses_Type()
)
wfIpv6IfStatsCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsCacheMisses.setStatus("mandatory")
_WfIpv6IfStatsCacheNetworks_Type = Counter32
_WfIpv6IfStatsCacheNetworks_Object = MibTableColumn
wfIpv6IfStatsCacheNetworks = _WfIpv6IfStatsCacheNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 17),
    _WfIpv6IfStatsCacheNetworks_Type()
)
wfIpv6IfStatsCacheNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsCacheNetworks.setStatus("mandatory")
_WfIpv6IfStatsCacheRemoves_Type = Counter32
_WfIpv6IfStatsCacheRemoves_Object = MibTableColumn
wfIpv6IfStatsCacheRemoves = _WfIpv6IfStatsCacheRemoves_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 18),
    _WfIpv6IfStatsCacheRemoves_Type()
)
wfIpv6IfStatsCacheRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsCacheRemoves.setStatus("mandatory")
_WfIpv6IfStatsReasmReqds_Type = Counter32
_WfIpv6IfStatsReasmReqds_Object = MibTableColumn
wfIpv6IfStatsReasmReqds = _WfIpv6IfStatsReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 19),
    _WfIpv6IfStatsReasmReqds_Type()
)
wfIpv6IfStatsReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsReasmReqds.setStatus("mandatory")
_WfIpv6IfStatsReasmOKs_Type = Counter32
_WfIpv6IfStatsReasmOKs_Object = MibTableColumn
wfIpv6IfStatsReasmOKs = _WfIpv6IfStatsReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 20),
    _WfIpv6IfStatsReasmOKs_Type()
)
wfIpv6IfStatsReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsReasmOKs.setStatus("mandatory")
_WfIpv6IfStatsReasmFails_Type = Counter32
_WfIpv6IfStatsReasmFails_Object = MibTableColumn
wfIpv6IfStatsReasmFails = _WfIpv6IfStatsReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 21),
    _WfIpv6IfStatsReasmFails_Type()
)
wfIpv6IfStatsReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsReasmFails.setStatus("mandatory")
_WfIpv6IfStatsMcastInPkts_Type = Counter32
_WfIpv6IfStatsMcastInPkts_Object = MibTableColumn
wfIpv6IfStatsMcastInPkts = _WfIpv6IfStatsMcastInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 22),
    _WfIpv6IfStatsMcastInPkts_Type()
)
wfIpv6IfStatsMcastInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsMcastInPkts.setStatus("mandatory")
_WfIpv6IfStatsMcastOutPkts_Type = Counter32
_WfIpv6IfStatsMcastOutPkts_Object = MibTableColumn
wfIpv6IfStatsMcastOutPkts = _WfIpv6IfStatsMcastOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 23),
    _WfIpv6IfStatsMcastOutPkts_Type()
)
wfIpv6IfStatsMcastOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsMcastOutPkts.setStatus("mandatory")
_WfIpv6IfStatsInTruncatedPkts_Type = Counter32
_WfIpv6IfStatsInTruncatedPkts_Object = MibTableColumn
wfIpv6IfStatsInTruncatedPkts = _WfIpv6IfStatsInTruncatedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 5, 1, 24),
    _WfIpv6IfStatsInTruncatedPkts_Type()
)
wfIpv6IfStatsInTruncatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IfStatsInTruncatedPkts.setStatus("mandatory")
_WfIpv6StaticRouteTable_Object = MibTable
wfIpv6StaticRouteTable = _WfIpv6StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wfIpv6StaticRouteTable.setStatus("mandatory")
_WfIpv6StaticRouteEntry_Object = MibTableRow
wfIpv6StaticRouteEntry = _WfIpv6StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 6, 1)
)
wfIpv6StaticRouteEntry.setIndexNames(
    (0, "Wellfleet-IPV6-MIB", "wfIpv6StaticRouteIfIndex"),
    (0, "Wellfleet-IPV6-MIB", "wfIpv6StaticRouteId"),
)
if mibBuilder.loadTexts:
    wfIpv6StaticRouteEntry.setStatus("mandatory")


class _WfIpv6StaticRouteDelete_Type(Integer32):
    """Custom type wfIpv6StaticRouteDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpv6StaticRouteDelete_Type.__name__ = "Integer32"
_WfIpv6StaticRouteDelete_Object = MibTableColumn
wfIpv6StaticRouteDelete = _WfIpv6StaticRouteDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 6, 1, 1),
    _WfIpv6StaticRouteDelete_Type()
)
wfIpv6StaticRouteDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6StaticRouteDelete.setStatus("mandatory")


class _WfIpv6StaticRouteDisable_Type(Integer32):
    """Custom type wfIpv6StaticRouteDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpv6StaticRouteDisable_Type.__name__ = "Integer32"
_WfIpv6StaticRouteDisable_Object = MibTableColumn
wfIpv6StaticRouteDisable = _WfIpv6StaticRouteDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 6, 1, 2),
    _WfIpv6StaticRouteDisable_Type()
)
wfIpv6StaticRouteDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6StaticRouteDisable.setStatus("mandatory")
_WfIpv6StaticRouteIfIndex_Type = Integer32
_WfIpv6StaticRouteIfIndex_Object = MibTableColumn
wfIpv6StaticRouteIfIndex = _WfIpv6StaticRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 6, 1, 3),
    _WfIpv6StaticRouteIfIndex_Type()
)
wfIpv6StaticRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6StaticRouteIfIndex.setStatus("mandatory")
_WfIpv6StaticRouteId_Type = Integer32
_WfIpv6StaticRouteId_Object = MibTableColumn
wfIpv6StaticRouteId = _WfIpv6StaticRouteId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 6, 1, 4),
    _WfIpv6StaticRouteId_Type()
)
wfIpv6StaticRouteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6StaticRouteId.setStatus("mandatory")
_WfIpv6StaticRoutePfx_Type = Ipv6AddressPrefix
_WfIpv6StaticRoutePfx_Object = MibTableColumn
wfIpv6StaticRoutePfx = _WfIpv6StaticRoutePfx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 6, 1, 5),
    _WfIpv6StaticRoutePfx_Type()
)
wfIpv6StaticRoutePfx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6StaticRoutePfx.setStatus("mandatory")


class _WfIpv6StaticRoutePfxLength_Type(Integer32):
    """Custom type wfIpv6StaticRoutePfxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_WfIpv6StaticRoutePfxLength_Type.__name__ = "Integer32"
_WfIpv6StaticRoutePfxLength_Object = MibTableColumn
wfIpv6StaticRoutePfxLength = _WfIpv6StaticRoutePfxLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 6, 1, 6),
    _WfIpv6StaticRoutePfxLength_Type()
)
wfIpv6StaticRoutePfxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6StaticRoutePfxLength.setStatus("mandatory")
_WfIpv6StaticRouteNextHopAddr_Type = Ipv6Address
_WfIpv6StaticRouteNextHopAddr_Object = MibTableColumn
wfIpv6StaticRouteNextHopAddr = _WfIpv6StaticRouteNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 6, 1, 7),
    _WfIpv6StaticRouteNextHopAddr_Type()
)
wfIpv6StaticRouteNextHopAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6StaticRouteNextHopAddr.setStatus("mandatory")


class _WfIpv6StaticRoutePreference_Type(Integer32):
    """Custom type wfIpv6StaticRoutePreference based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfIpv6StaticRoutePreference_Type.__name__ = "Integer32"
_WfIpv6StaticRoutePreference_Object = MibTableColumn
wfIpv6StaticRoutePreference = _WfIpv6StaticRoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 6, 1, 8),
    _WfIpv6StaticRoutePreference_Type()
)
wfIpv6StaticRoutePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6StaticRoutePreference.setStatus("mandatory")


class _WfIpv6StaticRouteCost_Type(Integer32):
    """Custom type wfIpv6StaticRouteCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_WfIpv6StaticRouteCost_Type.__name__ = "Integer32"
_WfIpv6StaticRouteCost_Object = MibTableColumn
wfIpv6StaticRouteCost = _WfIpv6StaticRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 6, 1, 9),
    _WfIpv6StaticRouteCost_Type()
)
wfIpv6StaticRouteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6StaticRouteCost.setStatus("mandatory")


class _WfIpv6StaticRouteInvalid_Type(Integer32):
    """Custom type wfIpv6StaticRouteInvalid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_WfIpv6StaticRouteInvalid_Type.__name__ = "Integer32"
_WfIpv6StaticRouteInvalid_Object = MibTableColumn
wfIpv6StaticRouteInvalid = _WfIpv6StaticRouteInvalid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 6, 1, 10),
    _WfIpv6StaticRouteInvalid_Type()
)
wfIpv6StaticRouteInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6StaticRouteInvalid.setStatus("mandatory")
_WfIpv6AdjacentNodeTable_Object = MibTable
wfIpv6AdjacentNodeTable = _WfIpv6AdjacentNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 7)
)
if mibBuilder.loadTexts:
    wfIpv6AdjacentNodeTable.setStatus("mandatory")
_WfIpv6AdjacentNodeEntry_Object = MibTableRow
wfIpv6AdjacentNodeEntry = _WfIpv6AdjacentNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 7, 1)
)
wfIpv6AdjacentNodeEntry.setIndexNames(
    (0, "Wellfleet-IPV6-MIB", "wfIpv6AdjNodeIfIndex"),
    (0, "Wellfleet-IPV6-MIB", "wfIpv6AdjNodeAddress"),
)
if mibBuilder.loadTexts:
    wfIpv6AdjacentNodeEntry.setStatus("mandatory")


class _WfIpv6AdjNodeDelete_Type(Integer32):
    """Custom type wfIpv6AdjNodeDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpv6AdjNodeDelete_Type.__name__ = "Integer32"
_WfIpv6AdjNodeDelete_Object = MibTableColumn
wfIpv6AdjNodeDelete = _WfIpv6AdjNodeDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 7, 1, 1),
    _WfIpv6AdjNodeDelete_Type()
)
wfIpv6AdjNodeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6AdjNodeDelete.setStatus("mandatory")


class _WfIpv6AdjNodeDisable_Type(Integer32):
    """Custom type wfIpv6AdjNodeDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpv6AdjNodeDisable_Type.__name__ = "Integer32"
_WfIpv6AdjNodeDisable_Object = MibTableColumn
wfIpv6AdjNodeDisable = _WfIpv6AdjNodeDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 7, 1, 2),
    _WfIpv6AdjNodeDisable_Type()
)
wfIpv6AdjNodeDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6AdjNodeDisable.setStatus("mandatory")
_WfIpv6AdjNodeAddress_Type = Ipv6Address
_WfIpv6AdjNodeAddress_Object = MibTableColumn
wfIpv6AdjNodeAddress = _WfIpv6AdjNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 7, 1, 3),
    _WfIpv6AdjNodeAddress_Type()
)
wfIpv6AdjNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6AdjNodeAddress.setStatus("mandatory")
_WfIpv6AdjNodeIfIndex_Type = Integer32
_WfIpv6AdjNodeIfIndex_Object = MibTableColumn
wfIpv6AdjNodeIfIndex = _WfIpv6AdjNodeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 7, 1, 4),
    _WfIpv6AdjNodeIfIndex_Type()
)
wfIpv6AdjNodeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6AdjNodeIfIndex.setStatus("mandatory")
_WfIpv6AdjNodePhysicalAddr_Type = PhysAddress
_WfIpv6AdjNodePhysicalAddr_Object = MibTableColumn
wfIpv6AdjNodePhysicalAddr = _WfIpv6AdjNodePhysicalAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 7, 1, 5),
    _WfIpv6AdjNodePhysicalAddr_Type()
)
wfIpv6AdjNodePhysicalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6AdjNodePhysicalAddr.setStatus("mandatory")


class _WfIpv6AdjNodeEncaps_Type(Integer32):
    """Custom type wfIpv6AdjNodeEncaps based on Integer32"""
    defaultValue = 1

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
        *(("other", 1),
          ("pdn", 3),
          ("snap", 2),
          ("wan", 4))
    )


_WfIpv6AdjNodeEncaps_Type.__name__ = "Integer32"
_WfIpv6AdjNodeEncaps_Object = MibTableColumn
wfIpv6AdjNodeEncaps = _WfIpv6AdjNodeEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 7, 1, 6),
    _WfIpv6AdjNodeEncaps_Type()
)
wfIpv6AdjNodeEncaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6AdjNodeEncaps.setStatus("mandatory")


class _WfIpv6AdjNodePreference_Type(Integer32):
    """Custom type wfIpv6AdjNodePreference based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfIpv6AdjNodePreference_Type.__name__ = "Integer32"
_WfIpv6AdjNodePreference_Object = MibTableColumn
wfIpv6AdjNodePreference = _WfIpv6AdjNodePreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 7, 1, 7),
    _WfIpv6AdjNodePreference_Type()
)
wfIpv6AdjNodePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6AdjNodePreference.setStatus("mandatory")


class _WfIpv6AdjNodeCost_Type(Integer32):
    """Custom type wfIpv6AdjNodeCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_WfIpv6AdjNodeCost_Type.__name__ = "Integer32"
_WfIpv6AdjNodeCost_Object = MibTableColumn
wfIpv6AdjNodeCost = _WfIpv6AdjNodeCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 7, 1, 8),
    _WfIpv6AdjNodeCost_Type()
)
wfIpv6AdjNodeCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6AdjNodeCost.setStatus("mandatory")


class _WfIpv6AdjNodeInvalid_Type(Integer32):
    """Custom type wfIpv6AdjNodeInvalid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_WfIpv6AdjNodeInvalid_Type.__name__ = "Integer32"
_WfIpv6AdjNodeInvalid_Object = MibTableColumn
wfIpv6AdjNodeInvalid = _WfIpv6AdjNodeInvalid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 7, 1, 9),
    _WfIpv6AdjNodeInvalid_Type()
)
wfIpv6AdjNodeInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6AdjNodeInvalid.setStatus("mandatory")
_WfIpv6AdjNodeWanAddr_Type = DisplayString
_WfIpv6AdjNodeWanAddr_Object = MibTableColumn
wfIpv6AdjNodeWanAddr = _WfIpv6AdjNodeWanAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 7, 1, 10),
    _WfIpv6AdjNodeWanAddr_Type()
)
wfIpv6AdjNodeWanAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6AdjNodeWanAddr.setStatus("mandatory")
_WfIpv6RouteTable_Object = MibTable
wfIpv6RouteTable = _WfIpv6RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 8)
)
if mibBuilder.loadTexts:
    wfIpv6RouteTable.setStatus("mandatory")
_WfIpv6RouteEntry_Object = MibTableRow
wfIpv6RouteEntry = _WfIpv6RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 8, 1)
)
wfIpv6RouteEntry.setIndexNames(
    (0, "Wellfleet-IPV6-MIB", "wfIpv6RouteDest"),
    (0, "Wellfleet-IPV6-MIB", "wfIpv6RoutePfxLength"),
    (0, "Wellfleet-IPV6-MIB", "wfIpv6RouteIfIndex"),
    (0, "Wellfleet-IPV6-MIB", "wfIpv6RouteIndex"),
)
if mibBuilder.loadTexts:
    wfIpv6RouteEntry.setStatus("mandatory")
_WfIpv6RouteDest_Type = Ipv6Address
_WfIpv6RouteDest_Object = MibTableColumn
wfIpv6RouteDest = _WfIpv6RouteDest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 8, 1, 1),
    _WfIpv6RouteDest_Type()
)
wfIpv6RouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6RouteDest.setStatus("mandatory")
_WfIpv6RoutePfxLength_Type = Integer32
_WfIpv6RoutePfxLength_Object = MibTableColumn
wfIpv6RoutePfxLength = _WfIpv6RoutePfxLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 8, 1, 2),
    _WfIpv6RoutePfxLength_Type()
)
wfIpv6RoutePfxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6RoutePfxLength.setStatus("mandatory")
_WfIpv6RouteIfIndex_Type = Integer32
_WfIpv6RouteIfIndex_Object = MibTableColumn
wfIpv6RouteIfIndex = _WfIpv6RouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 8, 1, 3),
    _WfIpv6RouteIfIndex_Type()
)
wfIpv6RouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6RouteIfIndex.setStatus("mandatory")
_WfIpv6RouteIndex_Type = Integer32
_WfIpv6RouteIndex_Object = MibTableColumn
wfIpv6RouteIndex = _WfIpv6RouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 8, 1, 4),
    _WfIpv6RouteIndex_Type()
)
wfIpv6RouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6RouteIndex.setStatus("mandatory")
_WfIpv6RouteNextHop_Type = Ipv6Address
_WfIpv6RouteNextHop_Object = MibTableColumn
wfIpv6RouteNextHop = _WfIpv6RouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 8, 1, 5),
    _WfIpv6RouteNextHop_Type()
)
wfIpv6RouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6RouteNextHop.setStatus("mandatory")


class _WfIpv6RouteType_Type(Integer32):
    """Custom type wfIpv6RouteType based on Integer32"""
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
        *(("direct", 3),
          ("discard", 5),
          ("indirect", 4),
          ("invalid", 2),
          ("other", 1))
    )


_WfIpv6RouteType_Type.__name__ = "Integer32"
_WfIpv6RouteType_Object = MibTableColumn
wfIpv6RouteType = _WfIpv6RouteType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 8, 1, 6),
    _WfIpv6RouteType_Type()
)
wfIpv6RouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6RouteType.setStatus("mandatory")


class _WfIpv6RouteProtocol_Type(Integer32):
    """Custom type wfIpv6RouteProtocol based on Integer32"""
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
        *(("idrp", 7),
          ("local", 2),
          ("ndisc", 4),
          ("netmgmt", 3),
          ("ospf", 6),
          ("other", 1),
          ("rip", 5))
    )


_WfIpv6RouteProtocol_Type.__name__ = "Integer32"
_WfIpv6RouteProtocol_Object = MibTableColumn
wfIpv6RouteProtocol = _WfIpv6RouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 8, 1, 7),
    _WfIpv6RouteProtocol_Type()
)
wfIpv6RouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6RouteProtocol.setStatus("mandatory")
_WfIpv6RoutePolicy_Type = Integer32
_WfIpv6RoutePolicy_Object = MibTableColumn
wfIpv6RoutePolicy = _WfIpv6RoutePolicy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 8, 1, 8),
    _WfIpv6RoutePolicy_Type()
)
wfIpv6RoutePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6RoutePolicy.setStatus("mandatory")
_WfIpv6RouteAge_Type = Gauge32
_WfIpv6RouteAge_Object = MibTableColumn
wfIpv6RouteAge = _WfIpv6RouteAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 8, 1, 9),
    _WfIpv6RouteAge_Type()
)
wfIpv6RouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6RouteAge.setStatus("mandatory")


class _WfIpv6RouteNextHopRDI_Type(OctetString):
    """Custom type wfIpv6RouteNextHopRDI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_WfIpv6RouteNextHopRDI_Type.__name__ = "OctetString"
_WfIpv6RouteNextHopRDI_Object = MibTableColumn
wfIpv6RouteNextHopRDI = _WfIpv6RouteNextHopRDI_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 8, 1, 10),
    _WfIpv6RouteNextHopRDI_Type()
)
wfIpv6RouteNextHopRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6RouteNextHopRDI.setStatus("mandatory")
_WfIpv6RouteMetric_Type = Gauge32
_WfIpv6RouteMetric_Object = MibTableColumn
wfIpv6RouteMetric = _WfIpv6RouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 8, 1, 11),
    _WfIpv6RouteMetric_Type()
)
wfIpv6RouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6RouteMetric.setStatus("mandatory")
_WfIpv6RouteWeight_Type = Gauge32
_WfIpv6RouteWeight_Object = MibTableColumn
wfIpv6RouteWeight = _WfIpv6RouteWeight_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 8, 1, 12),
    _WfIpv6RouteWeight_Type()
)
wfIpv6RouteWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6RouteWeight.setStatus("mandatory")
_WfIpv6RouteInfo_Type = ObjectIdentifier
_WfIpv6RouteInfo_Object = MibTableColumn
wfIpv6RouteInfo = _WfIpv6RouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 8, 1, 13),
    _WfIpv6RouteInfo_Type()
)
wfIpv6RouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6RouteInfo.setStatus("mandatory")
_WfIpv6NetToMediaEntryTable_Object = MibTable
wfIpv6NetToMediaEntryTable = _WfIpv6NetToMediaEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 9)
)
if mibBuilder.loadTexts:
    wfIpv6NetToMediaEntryTable.setStatus("mandatory")
_WfIpv6NetToMediaEntry_Object = MibTableRow
wfIpv6NetToMediaEntry = _WfIpv6NetToMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 9, 1)
)
wfIpv6NetToMediaEntry.setIndexNames(
    (0, "Wellfleet-IPV6-MIB", "wfIpv6NetToMediaIfIndex"),
    (0, "Wellfleet-IPV6-MIB", "wfIpv6NetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    wfIpv6NetToMediaEntry.setStatus("mandatory")
_WfIpv6NetToMediaIfIndex_Type = Integer32
_WfIpv6NetToMediaIfIndex_Object = MibTableColumn
wfIpv6NetToMediaIfIndex = _WfIpv6NetToMediaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 9, 1, 1),
    _WfIpv6NetToMediaIfIndex_Type()
)
wfIpv6NetToMediaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6NetToMediaIfIndex.setStatus("mandatory")
_WfIpv6NetToMediaNetAddress_Type = Ipv6Address
_WfIpv6NetToMediaNetAddress_Object = MibTableColumn
wfIpv6NetToMediaNetAddress = _WfIpv6NetToMediaNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 9, 1, 2),
    _WfIpv6NetToMediaNetAddress_Type()
)
wfIpv6NetToMediaNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6NetToMediaNetAddress.setStatus("mandatory")
_WfIpv6NetToMediaPhysAddress_Type = PhysAddress
_WfIpv6NetToMediaPhysAddress_Object = MibTableColumn
wfIpv6NetToMediaPhysAddress = _WfIpv6NetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 9, 1, 3),
    _WfIpv6NetToMediaPhysAddress_Type()
)
wfIpv6NetToMediaPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6NetToMediaPhysAddress.setStatus("mandatory")


class _WfIpv6NetToMediaType_Type(Integer32):
    """Custom type wfIpv6NetToMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("other", 1),
          ("static", 3))
    )


_WfIpv6NetToMediaType_Type.__name__ = "Integer32"
_WfIpv6NetToMediaType_Object = MibTableColumn
wfIpv6NetToMediaType = _WfIpv6NetToMediaType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 9, 1, 4),
    _WfIpv6NetToMediaType_Type()
)
wfIpv6NetToMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6NetToMediaType.setStatus("mandatory")


class _WfIpv6NetToMediaInvalid_Type(Integer32):
    """Custom type wfIpv6NetToMediaInvalid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_WfIpv6NetToMediaInvalid_Type.__name__ = "Integer32"
_WfIpv6NetToMediaInvalid_Object = MibTableColumn
wfIpv6NetToMediaInvalid = _WfIpv6NetToMediaInvalid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 9, 1, 5),
    _WfIpv6NetToMediaInvalid_Type()
)
wfIpv6NetToMediaInvalid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6NetToMediaInvalid.setStatus("mandatory")
_WfIpv6DbgInfoTable_Object = MibTable
wfIpv6DbgInfoTable = _WfIpv6DbgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 10)
)
if mibBuilder.loadTexts:
    wfIpv6DbgInfoTable.setStatus("mandatory")
_WfIpv6DbgInfoEntry_Object = MibTableRow
wfIpv6DbgInfoEntry = _WfIpv6DbgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 10, 1)
)
wfIpv6DbgInfoEntry.setIndexNames(
    (0, "Wellfleet-IPV6-MIB", "wfIpv6DbgInfoSlot"),
)
if mibBuilder.loadTexts:
    wfIpv6DbgInfoEntry.setStatus("mandatory")
_WfIpv6DbgInfoSlot_Type = Integer32
_WfIpv6DbgInfoSlot_Object = MibTableColumn
wfIpv6DbgInfoSlot = _WfIpv6DbgInfoSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 10, 1, 1),
    _WfIpv6DbgInfoSlot_Type()
)
wfIpv6DbgInfoSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6DbgInfoSlot.setStatus("mandatory")


class _WfIpv6DbgInfoState_Type(Integer32):
    """Custom type wfIpv6DbgInfoState based on Integer32"""
    defaultValue = 5

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
        *(("down", 2),
          ("init", 3),
          ("invalid", 4),
          ("notpres", 5),
          ("up", 1))
    )


_WfIpv6DbgInfoState_Type.__name__ = "Integer32"
_WfIpv6DbgInfoState_Object = MibTableColumn
wfIpv6DbgInfoState = _WfIpv6DbgInfoState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 10, 1, 2),
    _WfIpv6DbgInfoState_Type()
)
wfIpv6DbgInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6DbgInfoState.setStatus("mandatory")
_WfIpv6DbgInfoNetworks_Type = Integer32
_WfIpv6DbgInfoNetworks_Object = MibTableColumn
wfIpv6DbgInfoNetworks = _WfIpv6DbgInfoNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 10, 1, 3),
    _WfIpv6DbgInfoNetworks_Type()
)
wfIpv6DbgInfoNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6DbgInfoNetworks.setStatus("mandatory")
_WfIpv6DbgInfoNodes_Type = Integer32
_WfIpv6DbgInfoNodes_Object = MibTableColumn
wfIpv6DbgInfoNodes = _WfIpv6DbgInfoNodes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 10, 1, 4),
    _WfIpv6DbgInfoNodes_Type()
)
wfIpv6DbgInfoNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6DbgInfoNodes.setStatus("mandatory")
_WfIpv6DbgInfoActiveInterfaces_Type = Integer32
_WfIpv6DbgInfoActiveInterfaces_Object = MibTableColumn
wfIpv6DbgInfoActiveInterfaces = _WfIpv6DbgInfoActiveInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 10, 1, 5),
    _WfIpv6DbgInfoActiveInterfaces_Type()
)
wfIpv6DbgInfoActiveInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6DbgInfoActiveInterfaces.setStatus("mandatory")
_WfIpv6DbgInfoRtmAddr_Type = Gauge32
_WfIpv6DbgInfoRtmAddr_Object = MibTableColumn
wfIpv6DbgInfoRtmAddr = _WfIpv6DbgInfoRtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 10, 1, 6),
    _WfIpv6DbgInfoRtmAddr_Type()
)
wfIpv6DbgInfoRtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6DbgInfoRtmAddr.setStatus("mandatory")
_WfIpv6FilterTable_Object = MibTable
wfIpv6FilterTable = _WfIpv6FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 11)
)
if mibBuilder.loadTexts:
    wfIpv6FilterTable.setStatus("mandatory")
_WfIpv6FilterEntry_Object = MibTableRow
wfIpv6FilterEntry = _WfIpv6FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 11, 1)
)
wfIpv6FilterEntry.setIndexNames(
    (0, "Wellfleet-IPV6-MIB", "wfIpv6FilterNumber"),
)
if mibBuilder.loadTexts:
    wfIpv6FilterEntry.setStatus("mandatory")


class _WfIpv6FilterDelete_Type(Integer32):
    """Custom type wfIpv6FilterDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpv6FilterDelete_Type.__name__ = "Integer32"
_WfIpv6FilterDelete_Object = MibTableColumn
wfIpv6FilterDelete = _WfIpv6FilterDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 11, 1, 1),
    _WfIpv6FilterDelete_Type()
)
wfIpv6FilterDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6FilterDelete.setStatus("mandatory")


class _WfIpv6FilterDisable_Type(Integer32):
    """Custom type wfIpv6FilterDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpv6FilterDisable_Type.__name__ = "Integer32"
_WfIpv6FilterDisable_Object = MibTableColumn
wfIpv6FilterDisable = _WfIpv6FilterDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 11, 1, 2),
    _WfIpv6FilterDisable_Type()
)
wfIpv6FilterDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6FilterDisable.setStatus("mandatory")
_WfIpv6FilterNumber_Type = Integer32
_WfIpv6FilterNumber_Object = MibTableColumn
wfIpv6FilterNumber = _WfIpv6FilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 11, 1, 3),
    _WfIpv6FilterNumber_Type()
)
wfIpv6FilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6FilterNumber.setStatus("mandatory")
_WfIpv6FilterName_Type = DisplayString
_WfIpv6FilterName_Object = MibTableColumn
wfIpv6FilterName = _WfIpv6FilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 11, 1, 4),
    _WfIpv6FilterName_Type()
)
wfIpv6FilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6FilterName.setStatus("mandatory")


class _WfIpv6FilterPrecedence_Type(Gauge32):
    """Custom type wfIpv6FilterPrecedence based on Gauge32"""
    defaultValue = 1


_WfIpv6FilterPrecedence_Object = MibTableColumn
wfIpv6FilterPrecedence = _WfIpv6FilterPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 11, 1, 5),
    _WfIpv6FilterPrecedence_Type()
)
wfIpv6FilterPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6FilterPrecedence.setStatus("mandatory")
_WfIpv6FilterPackets_Type = Counter32
_WfIpv6FilterPackets_Object = MibTableColumn
wfIpv6FilterPackets = _WfIpv6FilterPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 11, 1, 6),
    _WfIpv6FilterPackets_Type()
)
wfIpv6FilterPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6FilterPackets.setStatus("mandatory")
_WfIpv6FilterOctets_Type = Counter32
_WfIpv6FilterOctets_Object = MibTableColumn
wfIpv6FilterOctets = _WfIpv6FilterOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 11, 1, 7),
    _WfIpv6FilterOctets_Type()
)
wfIpv6FilterOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6FilterOctets.setStatus("mandatory")


class _WfIpv6FilterInIfIndex_Type(Integer32):
    """Custom type wfIpv6FilterInIfIndex based on Integer32"""
    defaultValue = 0


_WfIpv6FilterInIfIndex_Object = MibTableColumn
wfIpv6FilterInIfIndex = _WfIpv6FilterInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 11, 1, 8),
    _WfIpv6FilterInIfIndex_Type()
)
wfIpv6FilterInIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6FilterInIfIndex.setStatus("mandatory")


class _WfIpv6FilterOutIfIndex_Type(Integer32):
    """Custom type wfIpv6FilterOutIfIndex based on Integer32"""
    defaultValue = 0


_WfIpv6FilterOutIfIndex_Object = MibTableColumn
wfIpv6FilterOutIfIndex = _WfIpv6FilterOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 11, 1, 9),
    _WfIpv6FilterOutIfIndex_Type()
)
wfIpv6FilterOutIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6FilterOutIfIndex.setStatus("mandatory")
_WfIpv6FilterSrcAddresses_Type = OctetString
_WfIpv6FilterSrcAddresses_Object = MibTableColumn
wfIpv6FilterSrcAddresses = _WfIpv6FilterSrcAddresses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 11, 1, 10),
    _WfIpv6FilterSrcAddresses_Type()
)
wfIpv6FilterSrcAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6FilterSrcAddresses.setStatus("mandatory")
_WfIpv6FilterDstAddresses_Type = OctetString
_WfIpv6FilterDstAddresses_Object = MibTableColumn
wfIpv6FilterDstAddresses = _WfIpv6FilterDstAddresses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 11, 1, 11),
    _WfIpv6FilterDstAddresses_Type()
)
wfIpv6FilterDstAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6FilterDstAddresses.setStatus("mandatory")
_WfIpv6FilterProtocols_Type = OctetString
_WfIpv6FilterProtocols_Object = MibTableColumn
wfIpv6FilterProtocols = _WfIpv6FilterProtocols_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 11, 1, 12),
    _WfIpv6FilterProtocols_Type()
)
wfIpv6FilterProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6FilterProtocols.setStatus("mandatory")


class _WfIpv6FilterAction_Type(Integer32):
    """Custom type wfIpv6FilterAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_WfIpv6FilterAction_Type.__name__ = "Integer32"
_WfIpv6FilterAction_Object = MibTableColumn
wfIpv6FilterAction = _WfIpv6FilterAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 11, 1, 13),
    _WfIpv6FilterAction_Type()
)
wfIpv6FilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6FilterAction.setStatus("mandatory")


class _WfIpv6FilterLog_Type(Integer32):
    """Custom type wfIpv6FilterLog based on Integer32"""
    defaultValue = 2

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


_WfIpv6FilterLog_Type.__name__ = "Integer32"
_WfIpv6FilterLog_Object = MibTableColumn
wfIpv6FilterLog = _WfIpv6FilterLog_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 1, 11, 1, 14),
    _WfIpv6FilterLog_Type()
)
wfIpv6FilterLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6FilterLog.setStatus("mandatory")
_WfIpv6IcmpGroup_ObjectIdentity = ObjectIdentity
wfIpv6IcmpGroup = _WfIpv6IcmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2)
)
_WfIpv6IcmpTable_Object = MibTable
wfIpv6IcmpTable = _WfIpv6IcmpTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1)
)
if mibBuilder.loadTexts:
    wfIpv6IcmpTable.setStatus("mandatory")
_WfIpv6IcmpEntry_Object = MibTableRow
wfIpv6IcmpEntry = _WfIpv6IcmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1)
)
wfIpv6IcmpEntry.setIndexNames(
    (0, "Wellfleet-IPV6-MIB", "wfIpv6IcmpIfIndex"),
)
if mibBuilder.loadTexts:
    wfIpv6IcmpEntry.setStatus("mandatory")
_WfIpv6IcmpIfIndex_Type = Integer32
_WfIpv6IcmpIfIndex_Object = MibTableColumn
wfIpv6IcmpIfIndex = _WfIpv6IcmpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 1),
    _WfIpv6IcmpIfIndex_Type()
)
wfIpv6IcmpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpIfIndex.setStatus("mandatory")
_WfIpv6IcmpInMsgs_Type = Counter32
_WfIpv6IcmpInMsgs_Object = MibTableColumn
wfIpv6IcmpInMsgs = _WfIpv6IcmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 2),
    _WfIpv6IcmpInMsgs_Type()
)
wfIpv6IcmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpInMsgs.setStatus("mandatory")
_WfIpv6IcmpInErrors_Type = Counter32
_WfIpv6IcmpInErrors_Object = MibTableColumn
wfIpv6IcmpInErrors = _WfIpv6IcmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 3),
    _WfIpv6IcmpInErrors_Type()
)
wfIpv6IcmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpInErrors.setStatus("mandatory")
_WfIpv6IcmpInDestUnreachs_Type = Counter32
_WfIpv6IcmpInDestUnreachs_Object = MibTableColumn
wfIpv6IcmpInDestUnreachs = _WfIpv6IcmpInDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 4),
    _WfIpv6IcmpInDestUnreachs_Type()
)
wfIpv6IcmpInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpInDestUnreachs.setStatus("mandatory")
_WfIpv6IcmpInAdminProhibs_Type = Counter32
_WfIpv6IcmpInAdminProhibs_Object = MibTableColumn
wfIpv6IcmpInAdminProhibs = _WfIpv6IcmpInAdminProhibs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 5),
    _WfIpv6IcmpInAdminProhibs_Type()
)
wfIpv6IcmpInAdminProhibs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpInAdminProhibs.setStatus("mandatory")
_WfIpv6IcmpInTimeExcds_Type = Counter32
_WfIpv6IcmpInTimeExcds_Object = MibTableColumn
wfIpv6IcmpInTimeExcds = _WfIpv6IcmpInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 6),
    _WfIpv6IcmpInTimeExcds_Type()
)
wfIpv6IcmpInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpInTimeExcds.setStatus("mandatory")
_WfIpv6IcmpInParmProbs_Type = Counter32
_WfIpv6IcmpInParmProbs_Object = MibTableColumn
wfIpv6IcmpInParmProbs = _WfIpv6IcmpInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 7),
    _WfIpv6IcmpInParmProbs_Type()
)
wfIpv6IcmpInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpInParmProbs.setStatus("mandatory")
_WfIpv6IcmpInPktTooBigs_Type = Counter32
_WfIpv6IcmpInPktTooBigs_Object = MibTableColumn
wfIpv6IcmpInPktTooBigs = _WfIpv6IcmpInPktTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 8),
    _WfIpv6IcmpInPktTooBigs_Type()
)
wfIpv6IcmpInPktTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpInPktTooBigs.setStatus("mandatory")
_WfIpv6IcmpInEchos_Type = Counter32
_WfIpv6IcmpInEchos_Object = MibTableColumn
wfIpv6IcmpInEchos = _WfIpv6IcmpInEchos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 9),
    _WfIpv6IcmpInEchos_Type()
)
wfIpv6IcmpInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpInEchos.setStatus("mandatory")
_WfIpv6IcmpInEchoReps_Type = Counter32
_WfIpv6IcmpInEchoReps_Object = MibTableColumn
wfIpv6IcmpInEchoReps = _WfIpv6IcmpInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 10),
    _WfIpv6IcmpInEchoReps_Type()
)
wfIpv6IcmpInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpInEchoReps.setStatus("mandatory")
_WfIpv6IcmpInRouterSolicits_Type = Counter32
_WfIpv6IcmpInRouterSolicits_Object = MibTableColumn
wfIpv6IcmpInRouterSolicits = _WfIpv6IcmpInRouterSolicits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 11),
    _WfIpv6IcmpInRouterSolicits_Type()
)
wfIpv6IcmpInRouterSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpInRouterSolicits.setStatus("mandatory")
_WfIpv6IcmpInRouterAdvertisements_Type = Counter32
_WfIpv6IcmpInRouterAdvertisements_Object = MibTableColumn
wfIpv6IcmpInRouterAdvertisements = _WfIpv6IcmpInRouterAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 12),
    _WfIpv6IcmpInRouterAdvertisements_Type()
)
wfIpv6IcmpInRouterAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpInRouterAdvertisements.setStatus("mandatory")
_WfIpv6IcmpInNeighborSolicits_Type = Counter32
_WfIpv6IcmpInNeighborSolicits_Object = MibTableColumn
wfIpv6IcmpInNeighborSolicits = _WfIpv6IcmpInNeighborSolicits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 13),
    _WfIpv6IcmpInNeighborSolicits_Type()
)
wfIpv6IcmpInNeighborSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpInNeighborSolicits.setStatus("mandatory")
_WfIpv6IcmpInNeighborAdvertisements_Type = Counter32
_WfIpv6IcmpInNeighborAdvertisements_Object = MibTableColumn
wfIpv6IcmpInNeighborAdvertisements = _WfIpv6IcmpInNeighborAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 14),
    _WfIpv6IcmpInNeighborAdvertisements_Type()
)
wfIpv6IcmpInNeighborAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpInNeighborAdvertisements.setStatus("mandatory")
_WfIpv6IcmpInRedirects_Type = Counter32
_WfIpv6IcmpInRedirects_Object = MibTableColumn
wfIpv6IcmpInRedirects = _WfIpv6IcmpInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 15),
    _WfIpv6IcmpInRedirects_Type()
)
wfIpv6IcmpInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpInRedirects.setStatus("mandatory")
_WfIpv6IcmpInGroupMembQueries_Type = Counter32
_WfIpv6IcmpInGroupMembQueries_Object = MibTableColumn
wfIpv6IcmpInGroupMembQueries = _WfIpv6IcmpInGroupMembQueries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 16),
    _WfIpv6IcmpInGroupMembQueries_Type()
)
wfIpv6IcmpInGroupMembQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpInGroupMembQueries.setStatus("mandatory")
_WfIpv6IcmpInGroupMembResponses_Type = Counter32
_WfIpv6IcmpInGroupMembResponses_Object = MibTableColumn
wfIpv6IcmpInGroupMembResponses = _WfIpv6IcmpInGroupMembResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 17),
    _WfIpv6IcmpInGroupMembResponses_Type()
)
wfIpv6IcmpInGroupMembResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpInGroupMembResponses.setStatus("mandatory")
_WfIpv6IcmpInGroupMembReductions_Type = Counter32
_WfIpv6IcmpInGroupMembReductions_Object = MibTableColumn
wfIpv6IcmpInGroupMembReductions = _WfIpv6IcmpInGroupMembReductions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 18),
    _WfIpv6IcmpInGroupMembReductions_Type()
)
wfIpv6IcmpInGroupMembReductions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpInGroupMembReductions.setStatus("mandatory")
_WfIpv6IcmpOutMsgs_Type = Counter32
_WfIpv6IcmpOutMsgs_Object = MibTableColumn
wfIpv6IcmpOutMsgs = _WfIpv6IcmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 19),
    _WfIpv6IcmpOutMsgs_Type()
)
wfIpv6IcmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpOutMsgs.setStatus("mandatory")
_WfIpv6IcmpOutErrors_Type = Counter32
_WfIpv6IcmpOutErrors_Object = MibTableColumn
wfIpv6IcmpOutErrors = _WfIpv6IcmpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 20),
    _WfIpv6IcmpOutErrors_Type()
)
wfIpv6IcmpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpOutErrors.setStatus("mandatory")
_WfIpv6IcmpOutDestUnreachs_Type = Counter32
_WfIpv6IcmpOutDestUnreachs_Object = MibTableColumn
wfIpv6IcmpOutDestUnreachs = _WfIpv6IcmpOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 21),
    _WfIpv6IcmpOutDestUnreachs_Type()
)
wfIpv6IcmpOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpOutDestUnreachs.setStatus("mandatory")
_WfIpv6IcmpOutAdminProhibs_Type = Counter32
_WfIpv6IcmpOutAdminProhibs_Object = MibTableColumn
wfIpv6IcmpOutAdminProhibs = _WfIpv6IcmpOutAdminProhibs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 22),
    _WfIpv6IcmpOutAdminProhibs_Type()
)
wfIpv6IcmpOutAdminProhibs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpOutAdminProhibs.setStatus("mandatory")
_WfIpv6IcmpOutTimeExcds_Type = Counter32
_WfIpv6IcmpOutTimeExcds_Object = MibTableColumn
wfIpv6IcmpOutTimeExcds = _WfIpv6IcmpOutTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 23),
    _WfIpv6IcmpOutTimeExcds_Type()
)
wfIpv6IcmpOutTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpOutTimeExcds.setStatus("mandatory")
_WfIpv6IcmpOutParmProbs_Type = Counter32
_WfIpv6IcmpOutParmProbs_Object = MibTableColumn
wfIpv6IcmpOutParmProbs = _WfIpv6IcmpOutParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 24),
    _WfIpv6IcmpOutParmProbs_Type()
)
wfIpv6IcmpOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpOutParmProbs.setStatus("mandatory")
_WfIpv6IcmpOutPktTooBigs_Type = Counter32
_WfIpv6IcmpOutPktTooBigs_Object = MibTableColumn
wfIpv6IcmpOutPktTooBigs = _WfIpv6IcmpOutPktTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 25),
    _WfIpv6IcmpOutPktTooBigs_Type()
)
wfIpv6IcmpOutPktTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpOutPktTooBigs.setStatus("mandatory")
_WfIpv6IcmpOutEchos_Type = Counter32
_WfIpv6IcmpOutEchos_Object = MibTableColumn
wfIpv6IcmpOutEchos = _WfIpv6IcmpOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 26),
    _WfIpv6IcmpOutEchos_Type()
)
wfIpv6IcmpOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpOutEchos.setStatus("mandatory")
_WfIpv6IcmpOutEchoReps_Type = Counter32
_WfIpv6IcmpOutEchoReps_Object = MibTableColumn
wfIpv6IcmpOutEchoReps = _WfIpv6IcmpOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 27),
    _WfIpv6IcmpOutEchoReps_Type()
)
wfIpv6IcmpOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpOutEchoReps.setStatus("mandatory")
_WfIpv6IcmpOutRouterSolicits_Type = Counter32
_WfIpv6IcmpOutRouterSolicits_Object = MibTableColumn
wfIpv6IcmpOutRouterSolicits = _WfIpv6IcmpOutRouterSolicits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 28),
    _WfIpv6IcmpOutRouterSolicits_Type()
)
wfIpv6IcmpOutRouterSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpOutRouterSolicits.setStatus("mandatory")
_WfIpv6IcmpOutRouterAdvertisements_Type = Counter32
_WfIpv6IcmpOutRouterAdvertisements_Object = MibTableColumn
wfIpv6IcmpOutRouterAdvertisements = _WfIpv6IcmpOutRouterAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 29),
    _WfIpv6IcmpOutRouterAdvertisements_Type()
)
wfIpv6IcmpOutRouterAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpOutRouterAdvertisements.setStatus("mandatory")
_WfIpv6IcmpOutNeighborSolicits_Type = Counter32
_WfIpv6IcmpOutNeighborSolicits_Object = MibTableColumn
wfIpv6IcmpOutNeighborSolicits = _WfIpv6IcmpOutNeighborSolicits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 30),
    _WfIpv6IcmpOutNeighborSolicits_Type()
)
wfIpv6IcmpOutNeighborSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpOutNeighborSolicits.setStatus("mandatory")
_WfIpv6IcmpOutNeighborAdvertisements_Type = Counter32
_WfIpv6IcmpOutNeighborAdvertisements_Object = MibTableColumn
wfIpv6IcmpOutNeighborAdvertisements = _WfIpv6IcmpOutNeighborAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 31),
    _WfIpv6IcmpOutNeighborAdvertisements_Type()
)
wfIpv6IcmpOutNeighborAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpOutNeighborAdvertisements.setStatus("mandatory")
_WfIpv6IcmpOutRedirects_Type = Counter32
_WfIpv6IcmpOutRedirects_Object = MibTableColumn
wfIpv6IcmpOutRedirects = _WfIpv6IcmpOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 32),
    _WfIpv6IcmpOutRedirects_Type()
)
wfIpv6IcmpOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpOutRedirects.setStatus("mandatory")
_WfIpv6IcmpOutGroupMembQueries_Type = Counter32
_WfIpv6IcmpOutGroupMembQueries_Object = MibTableColumn
wfIpv6IcmpOutGroupMembQueries = _WfIpv6IcmpOutGroupMembQueries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 33),
    _WfIpv6IcmpOutGroupMembQueries_Type()
)
wfIpv6IcmpOutGroupMembQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpOutGroupMembQueries.setStatus("mandatory")
_WfIpv6IcmpOutGroupMembResponses_Type = Counter32
_WfIpv6IcmpOutGroupMembResponses_Object = MibTableColumn
wfIpv6IcmpOutGroupMembResponses = _WfIpv6IcmpOutGroupMembResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 34),
    _WfIpv6IcmpOutGroupMembResponses_Type()
)
wfIpv6IcmpOutGroupMembResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpOutGroupMembResponses.setStatus("mandatory")
_WfIpv6IcmpOutGroupMembReductions_Type = Counter32
_WfIpv6IcmpOutGroupMembReductions_Object = MibTableColumn
wfIpv6IcmpOutGroupMembReductions = _WfIpv6IcmpOutGroupMembReductions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 2, 1, 1, 35),
    _WfIpv6IcmpOutGroupMembReductions_Type()
)
wfIpv6IcmpOutGroupMembReductions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6IcmpOutGroupMembReductions.setStatus("mandatory")
_WfIpv6NDiscGroup_ObjectIdentity = ObjectIdentity
wfIpv6NDiscGroup = _WfIpv6NDiscGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 3)
)
_WfIpv6NdiscIfTable_Object = MibTable
wfIpv6NdiscIfTable = _WfIpv6NdiscIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 3, 1)
)
if mibBuilder.loadTexts:
    wfIpv6NdiscIfTable.setStatus("mandatory")
_WfIpv6NdiscIfEntry_Object = MibTableRow
wfIpv6NdiscIfEntry = _WfIpv6NdiscIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 3, 1, 1)
)
wfIpv6NdiscIfEntry.setIndexNames(
    (0, "Wellfleet-IPV6-MIB", "wfIpv6NdiscIfIndex"),
)
if mibBuilder.loadTexts:
    wfIpv6NdiscIfEntry.setStatus("mandatory")


class _WfIpv6NdiscIfDelete_Type(Integer32):
    """Custom type wfIpv6NdiscIfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpv6NdiscIfDelete_Type.__name__ = "Integer32"
_WfIpv6NdiscIfDelete_Object = MibTableColumn
wfIpv6NdiscIfDelete = _WfIpv6NdiscIfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 3, 1, 1, 1),
    _WfIpv6NdiscIfDelete_Type()
)
wfIpv6NdiscIfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6NdiscIfDelete.setStatus("mandatory")


class _WfIpv6NdiscIfDisable_Type(Integer32):
    """Custom type wfIpv6NdiscIfDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpv6NdiscIfDisable_Type.__name__ = "Integer32"
_WfIpv6NdiscIfDisable_Object = MibTableColumn
wfIpv6NdiscIfDisable = _WfIpv6NdiscIfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 3, 1, 1, 2),
    _WfIpv6NdiscIfDisable_Type()
)
wfIpv6NdiscIfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6NdiscIfDisable.setStatus("mandatory")


class _WfIpv6NdiscIfState_Type(Integer32):
    """Custom type wfIpv6NdiscIfState based on Integer32"""
    defaultValue = 5

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
        *(("down", 2),
          ("init", 3),
          ("invalid", 4),
          ("notpres", 5),
          ("up", 1))
    )


_WfIpv6NdiscIfState_Type.__name__ = "Integer32"
_WfIpv6NdiscIfState_Object = MibTableColumn
wfIpv6NdiscIfState = _WfIpv6NdiscIfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 3, 1, 1, 3),
    _WfIpv6NdiscIfState_Type()
)
wfIpv6NdiscIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6NdiscIfState.setStatus("mandatory")
_WfIpv6NdiscIfIndex_Type = Integer32
_WfIpv6NdiscIfIndex_Object = MibTableColumn
wfIpv6NdiscIfIndex = _WfIpv6NdiscIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 3, 1, 1, 4),
    _WfIpv6NdiscIfIndex_Type()
)
wfIpv6NdiscIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6NdiscIfIndex.setStatus("mandatory")


class _WfIpv6NdiscIfSendAdvertisements_Type(Integer32):
    """Custom type wfIpv6NdiscIfSendAdvertisements based on Integer32"""
    defaultValue = 2

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


_WfIpv6NdiscIfSendAdvertisements_Type.__name__ = "Integer32"
_WfIpv6NdiscIfSendAdvertisements_Object = MibTableColumn
wfIpv6NdiscIfSendAdvertisements = _WfIpv6NdiscIfSendAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 3, 1, 1, 5),
    _WfIpv6NdiscIfSendAdvertisements_Type()
)
wfIpv6NdiscIfSendAdvertisements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6NdiscIfSendAdvertisements.setStatus("mandatory")


class _WfIpv6NdiscIfManagedFlag_Type(Integer32):
    """Custom type wfIpv6NdiscIfManagedFlag based on Integer32"""
    defaultValue = 2

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


_WfIpv6NdiscIfManagedFlag_Type.__name__ = "Integer32"
_WfIpv6NdiscIfManagedFlag_Object = MibTableColumn
wfIpv6NdiscIfManagedFlag = _WfIpv6NdiscIfManagedFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 3, 1, 1, 6),
    _WfIpv6NdiscIfManagedFlag_Type()
)
wfIpv6NdiscIfManagedFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6NdiscIfManagedFlag.setStatus("mandatory")


class _WfIpv6NdiscIfOtherCfgFlag_Type(Integer32):
    """Custom type wfIpv6NdiscIfOtherCfgFlag based on Integer32"""
    defaultValue = 2

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


_WfIpv6NdiscIfOtherCfgFlag_Type.__name__ = "Integer32"
_WfIpv6NdiscIfOtherCfgFlag_Object = MibTableColumn
wfIpv6NdiscIfOtherCfgFlag = _WfIpv6NdiscIfOtherCfgFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 3, 1, 1, 7),
    _WfIpv6NdiscIfOtherCfgFlag_Type()
)
wfIpv6NdiscIfOtherCfgFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6NdiscIfOtherCfgFlag.setStatus("mandatory")


class _WfIpv6NdiscIfReachableTime_Type(Integer32):
    """Custom type wfIpv6NdiscIfReachableTime based on Integer32"""
    defaultValue = 0


_WfIpv6NdiscIfReachableTime_Object = MibTableColumn
wfIpv6NdiscIfReachableTime = _WfIpv6NdiscIfReachableTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 3, 1, 1, 8),
    _WfIpv6NdiscIfReachableTime_Type()
)
wfIpv6NdiscIfReachableTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6NdiscIfReachableTime.setStatus("mandatory")


class _WfIpv6NdiscIfRetransTimer_Type(Integer32):
    """Custom type wfIpv6NdiscIfRetransTimer based on Integer32"""
    defaultValue = 0


_WfIpv6NdiscIfRetransTimer_Object = MibTableColumn
wfIpv6NdiscIfRetransTimer = _WfIpv6NdiscIfRetransTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 3, 1, 1, 9),
    _WfIpv6NdiscIfRetransTimer_Type()
)
wfIpv6NdiscIfRetransTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6NdiscIfRetransTimer.setStatus("mandatory")


class _WfIpv6NdiscIfMaxHopLimit_Type(Integer32):
    """Custom type wfIpv6NdiscIfMaxHopLimit based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfIpv6NdiscIfMaxHopLimit_Type.__name__ = "Integer32"
_WfIpv6NdiscIfMaxHopLimit_Object = MibTableColumn
wfIpv6NdiscIfMaxHopLimit = _WfIpv6NdiscIfMaxHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 3, 1, 1, 10),
    _WfIpv6NdiscIfMaxHopLimit_Type()
)
wfIpv6NdiscIfMaxHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6NdiscIfMaxHopLimit.setStatus("mandatory")


class _WfIpv6NdiscIfMinRtrAdvInterval_Type(Integer32):
    """Custom type wfIpv6NdiscIfMinRtrAdvInterval based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1350),
    )


_WfIpv6NdiscIfMinRtrAdvInterval_Type.__name__ = "Integer32"
_WfIpv6NdiscIfMinRtrAdvInterval_Object = MibTableColumn
wfIpv6NdiscIfMinRtrAdvInterval = _WfIpv6NdiscIfMinRtrAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 3, 1, 1, 11),
    _WfIpv6NdiscIfMinRtrAdvInterval_Type()
)
wfIpv6NdiscIfMinRtrAdvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6NdiscIfMinRtrAdvInterval.setStatus("mandatory")


class _WfIpv6NdiscIfMaxRtrAdvInterval_Type(Integer32):
    """Custom type wfIpv6NdiscIfMaxRtrAdvInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_WfIpv6NdiscIfMaxRtrAdvInterval_Type.__name__ = "Integer32"
_WfIpv6NdiscIfMaxRtrAdvInterval_Object = MibTableColumn
wfIpv6NdiscIfMaxRtrAdvInterval = _WfIpv6NdiscIfMaxRtrAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 3, 1, 1, 12),
    _WfIpv6NdiscIfMaxRtrAdvInterval_Type()
)
wfIpv6NdiscIfMaxRtrAdvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6NdiscIfMaxRtrAdvInterval.setStatus("mandatory")


class _WfIpv6NdiscIfDefaultLifetime_Type(Integer32):
    """Custom type wfIpv6NdiscIfDefaultLifetime based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
    )


_WfIpv6NdiscIfDefaultLifetime_Type.__name__ = "Integer32"
_WfIpv6NdiscIfDefaultLifetime_Object = MibTableColumn
wfIpv6NdiscIfDefaultLifetime = _WfIpv6NdiscIfDefaultLifetime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 3, 1, 1, 13),
    _WfIpv6NdiscIfDefaultLifetime_Type()
)
wfIpv6NdiscIfDefaultLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6NdiscIfDefaultLifetime.setStatus("mandatory")


class _WfIpv6NdiscIfDupAddrDetectTransmits_Type(Integer32):
    """Custom type wfIpv6NdiscIfDupAddrDetectTransmits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WfIpv6NdiscIfDupAddrDetectTransmits_Type.__name__ = "Integer32"
_WfIpv6NdiscIfDupAddrDetectTransmits_Object = MibTableColumn
wfIpv6NdiscIfDupAddrDetectTransmits = _WfIpv6NdiscIfDupAddrDetectTransmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 3, 1, 1, 14),
    _WfIpv6NdiscIfDupAddrDetectTransmits_Type()
)
wfIpv6NdiscIfDupAddrDetectTransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6NdiscIfDupAddrDetectTransmits.setStatus("mandatory")
_WfIpv6UdpGroup_ObjectIdentity = ObjectIdentity
wfIpv6UdpGroup = _WfIpv6UdpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 4)
)
_WfIpv6Udp_ObjectIdentity = ObjectIdentity
wfIpv6Udp = _WfIpv6Udp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 4, 1)
)
_WfIpv6UdpInDatagrams_Type = Counter32
_WfIpv6UdpInDatagrams_Object = MibScalar
wfIpv6UdpInDatagrams = _WfIpv6UdpInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 4, 1, 1),
    _WfIpv6UdpInDatagrams_Type()
)
wfIpv6UdpInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6UdpInDatagrams.setStatus("mandatory")
_WfIpv6UdpNoPorts_Type = Counter32
_WfIpv6UdpNoPorts_Object = MibScalar
wfIpv6UdpNoPorts = _WfIpv6UdpNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 4, 1, 2),
    _WfIpv6UdpNoPorts_Type()
)
wfIpv6UdpNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6UdpNoPorts.setStatus("mandatory")
_WfIpv6UdpInErrors_Type = Counter32
_WfIpv6UdpInErrors_Object = MibScalar
wfIpv6UdpInErrors = _WfIpv6UdpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 4, 1, 3),
    _WfIpv6UdpInErrors_Type()
)
wfIpv6UdpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6UdpInErrors.setStatus("mandatory")
_WfIpv6UdpOutDatagrams_Type = Counter32
_WfIpv6UdpOutDatagrams_Object = MibScalar
wfIpv6UdpOutDatagrams = _WfIpv6UdpOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 4, 1, 4),
    _WfIpv6UdpOutDatagrams_Type()
)
wfIpv6UdpOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6UdpOutDatagrams.setStatus("mandatory")
_WfIpv6UdpTable_Object = MibTable
wfIpv6UdpTable = _WfIpv6UdpTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 4, 2)
)
if mibBuilder.loadTexts:
    wfIpv6UdpTable.setStatus("mandatory")
_WfIpv6UdpEntry_Object = MibTableRow
wfIpv6UdpEntry = _WfIpv6UdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 4, 2, 1)
)
wfIpv6UdpEntry.setIndexNames(
    (0, "Wellfleet-IPV6-MIB", "wfIpv6UdpLocalIfIndex"),
    (0, "Wellfleet-IPV6-MIB", "wfIpv6UdpLocalAddress"),
    (0, "Wellfleet-IPV6-MIB", "wfIpv6UdpLocalPort"),
)
if mibBuilder.loadTexts:
    wfIpv6UdpEntry.setStatus("mandatory")
_WfIpv6UdpLocalIfIndex_Type = Integer32
_WfIpv6UdpLocalIfIndex_Object = MibTableColumn
wfIpv6UdpLocalIfIndex = _WfIpv6UdpLocalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 4, 2, 1, 1),
    _WfIpv6UdpLocalIfIndex_Type()
)
wfIpv6UdpLocalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6UdpLocalIfIndex.setStatus("mandatory")
_WfIpv6UdpLocalAddress_Type = Ipv6Address
_WfIpv6UdpLocalAddress_Object = MibTableColumn
wfIpv6UdpLocalAddress = _WfIpv6UdpLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 4, 2, 1, 2),
    _WfIpv6UdpLocalAddress_Type()
)
wfIpv6UdpLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6UdpLocalAddress.setStatus("mandatory")
_WfIpv6UdpLocalPort_Type = Integer32
_WfIpv6UdpLocalPort_Object = MibTableColumn
wfIpv6UdpLocalPort = _WfIpv6UdpLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 4, 2, 1, 3),
    _WfIpv6UdpLocalPort_Type()
)
wfIpv6UdpLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6UdpLocalPort.setStatus("mandatory")
_WfIpv6LogGroup_ObjectIdentity = ObjectIdentity
wfIpv6LogGroup = _WfIpv6LogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 5)
)
_WfIpv6Log_ObjectIdentity = ObjectIdentity
wfIpv6Log = _WfIpv6Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 5, 1)
)


class _WfIpv6LogDelete_Type(Integer32):
    """Custom type wfIpv6LogDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfIpv6LogDelete_Type.__name__ = "Integer32"
_WfIpv6LogDelete_Object = MibScalar
wfIpv6LogDelete = _WfIpv6LogDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 5, 1, 1),
    _WfIpv6LogDelete_Type()
)
wfIpv6LogDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6LogDelete.setStatus("mandatory")


class _WfIpv6LogDisable_Type(Integer32):
    """Custom type wfIpv6LogDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpv6LogDisable_Type.__name__ = "Integer32"
_WfIpv6LogDisable_Object = MibScalar
wfIpv6LogDisable = _WfIpv6LogDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 5, 1, 2),
    _WfIpv6LogDisable_Type()
)
wfIpv6LogDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6LogDisable.setStatus("mandatory")


class _WfIpv6LogLevel_Type(Integer32):
    """Custom type wfIpv6LogLevel based on Integer32"""
    defaultValue = 3

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
        *(("debug", 1),
          ("fault", 5),
          ("info", 3),
          ("trace", 2),
          ("warning", 4))
    )


_WfIpv6LogLevel_Type.__name__ = "Integer32"
_WfIpv6LogLevel_Object = MibScalar
wfIpv6LogLevel = _WfIpv6LogLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 5, 1, 3),
    _WfIpv6LogLevel_Type()
)
wfIpv6LogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6LogLevel.setStatus("mandatory")


class _WfIpv6LogEvent_Type(Integer32):
    """Custom type wfIpv6LogEvent based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfIpv6LogEvent_Type.__name__ = "Integer32"
_WfIpv6LogEvent_Object = MibScalar
wfIpv6LogEvent = _WfIpv6LogEvent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 5, 1, 4),
    _WfIpv6LogEvent_Type()
)
wfIpv6LogEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6LogEvent.setStatus("mandatory")


class _WfIpv6LogEventDisable_Type(Integer32):
    """Custom type wfIpv6LogEventDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfIpv6LogEventDisable_Type.__name__ = "Integer32"
_WfIpv6LogEventDisable_Object = MibScalar
wfIpv6LogEventDisable = _WfIpv6LogEventDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 5, 1, 5),
    _WfIpv6LogEventDisable_Type()
)
wfIpv6LogEventDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6LogEventDisable.setStatus("mandatory")
_WfIpv6LogEvents_Type = OctetString
_WfIpv6LogEvents_Object = MibScalar
wfIpv6LogEvents = _WfIpv6LogEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 5, 1, 6),
    _WfIpv6LogEvents_Type()
)
wfIpv6LogEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpv6LogEvents.setStatus("mandatory")
_WfIpv6LogCfgEvents_Type = OctetString
_WfIpv6LogCfgEvents_Object = MibScalar
wfIpv6LogCfgEvents = _WfIpv6LogCfgEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 5, 1, 7),
    _WfIpv6LogCfgEvents_Type()
)
wfIpv6LogCfgEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpv6LogCfgEvents.setStatus("mandatory")
_WfIpv6PolicyGroup_ObjectIdentity = ObjectIdentity
wfIpv6PolicyGroup = _WfIpv6PolicyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-IPV6-MIB",
    **{"Ipv6Address": Ipv6Address,
       "Ipv6AddressPrefix": Ipv6AddressPrefix,
       "wfIpv6RoutingGroup": wfIpv6RoutingGroup,
       "wfIpv6RoutingGeneralGroup": wfIpv6RoutingGeneralGroup,
       "wfIpv6Base": wfIpv6Base,
       "wfIpv6BaseDelete": wfIpv6BaseDelete,
       "wfIpv6BaseDisable": wfIpv6BaseDisable,
       "wfIpv6BaseState": wfIpv6BaseState,
       "wfIpv6BaseForwarding": wfIpv6BaseForwarding,
       "wfIpv6BaseDefaultHopLimit": wfIpv6BaseDefaultHopLimit,
       "wfIpv6BaseMinLinkMTU": wfIpv6BaseMinLinkMTU,
       "wfIpv6BaseMTUDiscovery": wfIpv6BaseMTUDiscovery,
       "wfIpv6BaseMTUTimeout": wfIpv6BaseMTUTimeout,
       "wfIpv6BaseIfNumber": wfIpv6BaseIfNumber,
       "wfIpv6BaseNetworks": wfIpv6BaseNetworks,
       "wfIpv6BaseNodes": wfIpv6BaseNodes,
       "wfIpv6BaseHighestFilterRule": wfIpv6BaseHighestFilterRule,
       "wfIpv6IfTable": wfIpv6IfTable,
       "wfIpv6IfEntry": wfIpv6IfEntry,
       "wfIpv6IfDelete": wfIpv6IfDelete,
       "wfIpv6IfDisable": wfIpv6IfDisable,
       "wfIpv6IfState": wfIpv6IfState,
       "wfIpv6IfIndex": wfIpv6IfIndex,
       "wfIpv6IfDescr": wfIpv6IfDescr,
       "wfIpv6IfCircuit": wfIpv6IfCircuit,
       "wfIpv6IfCfgToken": wfIpv6IfCfgToken,
       "wfIpv6IfCfgTokenLength": wfIpv6IfCfgTokenLength,
       "wfIpv6IfToken": wfIpv6IfToken,
       "wfIpv6IfTokenLength": wfIpv6IfTokenLength,
       "wfIpv6IfCfgPhysicalAddress": wfIpv6IfCfgPhysicalAddress,
       "wfIpv6IfPhysicalAddress": wfIpv6IfPhysicalAddress,
       "wfIpv6IfCfgLinkMTU": wfIpv6IfCfgLinkMTU,
       "wfIpv6IfFwdCacheSize": wfIpv6IfFwdCacheSize,
       "wfIpv6IfSlotMask": wfIpv6IfSlotMask,
       "wfIpv6IfLastChange": wfIpv6IfLastChange,
       "wfIpv6IfReasmMaxSize": wfIpv6IfReasmMaxSize,
       "wfIpv6IfMaxInfo": wfIpv6IfMaxInfo,
       "wfIpv6IfRedirect": wfIpv6IfRedirect,
       "wfIpv6IfIcmpErrorLimit": wfIpv6IfIcmpErrorLimit,
       "wfIpv6IfTrEndStation": wfIpv6IfTrEndStation,
       "wfIpv6IfSMDSGroupAddress": wfIpv6IfSMDSGroupAddress,
       "wfIpv6IfFRBcastDlci": wfIpv6IfFRBcastDlci,
       "wfIpv6IfFRMcast1Dlci": wfIpv6IfFRMcast1Dlci,
       "wfIpv6IfFRMcast2Dlci": wfIpv6IfFRMcast2Dlci,
       "wfIpv6IfTunnelProtocol": wfIpv6IfTunnelProtocol,
       "wfIpv6IfIPv4TunnelLocalAddress": wfIpv6IfIPv4TunnelLocalAddress,
       "wfIpv6IfIPv4TunnelRemoteAddress": wfIpv6IfIPv4TunnelRemoteAddress,
       "wfIpv6IfIpv6TunnelIfIndex": wfIpv6IfIpv6TunnelIfIndex,
       "wfIpv6IfIpv6TunnelRemoteAddress": wfIpv6IfIpv6TunnelRemoteAddress,
       "wfIpv6AddrPrefixTable": wfIpv6AddrPrefixTable,
       "wfIpv6AddrPrefixEntry": wfIpv6AddrPrefixEntry,
       "wfIpv6AddrPrefixDelete": wfIpv6AddrPrefixDelete,
       "wfIpv6AddrPrefixDisable": wfIpv6AddrPrefixDisable,
       "wfIpv6AddrPrefixIfIndex": wfIpv6AddrPrefixIfIndex,
       "wfIpv6AddrPrefixIndex": wfIpv6AddrPrefixIndex,
       "wfIpv6AddrPrefix": wfIpv6AddrPrefix,
       "wfIpv6AddrPrefixLength": wfIpv6AddrPrefixLength,
       "wfIpv6AddrPrefixPreference": wfIpv6AddrPrefixPreference,
       "wfIpv6AddrPrefixCost": wfIpv6AddrPrefixCost,
       "wfIpv6AddrPrefixOnLinkFlag": wfIpv6AddrPrefixOnLinkFlag,
       "wfIpv6AddrPrefixAutonomousFlag": wfIpv6AddrPrefixAutonomousFlag,
       "wfIpv6AddrPrefixAdvPreferredLifetime": wfIpv6AddrPrefixAdvPreferredLifetime,
       "wfIpv6AddrPrefixAdvValidLifetime": wfIpv6AddrPrefixAdvValidLifetime,
       "wfIpv6AddrPrefixInvalid": wfIpv6AddrPrefixInvalid,
       "wfIpv6AddrPrefixAnycast": wfIpv6AddrPrefixAnycast,
       "wfIpv6AddrTable": wfIpv6AddrTable,
       "wfIpv6AddrEntry": wfIpv6AddrEntry,
       "wfIpv6AddrIfIndex": wfIpv6AddrIfIndex,
       "wfIpv6AddrAddress": wfIpv6AddrAddress,
       "wfIpv6AddrPfxLength": wfIpv6AddrPfxLength,
       "wfIpv6AddrType": wfIpv6AddrType,
       "wfIpv6AddrAnycastFlag": wfIpv6AddrAnycastFlag,
       "wfIpv6AddrStatus": wfIpv6AddrStatus,
       "wfIpv6IfStatsTable": wfIpv6IfStatsTable,
       "wfIpv6IfStatsEntry": wfIpv6IfStatsEntry,
       "wfIpv6IfStatsIfIndex": wfIpv6IfStatsIfIndex,
       "wfIpv6IfStatsInReceives": wfIpv6IfStatsInReceives,
       "wfIpv6IfStatsInHdrErrors": wfIpv6IfStatsInHdrErrors,
       "wfIpv6IfStatsInTooBigErrors": wfIpv6IfStatsInTooBigErrors,
       "wfIpv6IfStatsInNoRoutes": wfIpv6IfStatsInNoRoutes,
       "wfIpv6IfStatsInAddrErrors": wfIpv6IfStatsInAddrErrors,
       "wfIpv6IfStatsInUnknownProtos": wfIpv6IfStatsInUnknownProtos,
       "wfIpv6IfStatsInDiscards": wfIpv6IfStatsInDiscards,
       "wfIpv6IfStatsInDelivers": wfIpv6IfStatsInDelivers,
       "wfIpv6IfStatsForwDatagrams": wfIpv6IfStatsForwDatagrams,
       "wfIpv6IfStatsOutRequests": wfIpv6IfStatsOutRequests,
       "wfIpv6IfStatsOutDiscards": wfIpv6IfStatsOutDiscards,
       "wfIpv6IfStatsFragOKs": wfIpv6IfStatsFragOKs,
       "wfIpv6IfStatsFragFails": wfIpv6IfStatsFragFails,
       "wfIpv6IfStatsFragCreates": wfIpv6IfStatsFragCreates,
       "wfIpv6IfStatsCacheMisses": wfIpv6IfStatsCacheMisses,
       "wfIpv6IfStatsCacheNetworks": wfIpv6IfStatsCacheNetworks,
       "wfIpv6IfStatsCacheRemoves": wfIpv6IfStatsCacheRemoves,
       "wfIpv6IfStatsReasmReqds": wfIpv6IfStatsReasmReqds,
       "wfIpv6IfStatsReasmOKs": wfIpv6IfStatsReasmOKs,
       "wfIpv6IfStatsReasmFails": wfIpv6IfStatsReasmFails,
       "wfIpv6IfStatsMcastInPkts": wfIpv6IfStatsMcastInPkts,
       "wfIpv6IfStatsMcastOutPkts": wfIpv6IfStatsMcastOutPkts,
       "wfIpv6IfStatsInTruncatedPkts": wfIpv6IfStatsInTruncatedPkts,
       "wfIpv6StaticRouteTable": wfIpv6StaticRouteTable,
       "wfIpv6StaticRouteEntry": wfIpv6StaticRouteEntry,
       "wfIpv6StaticRouteDelete": wfIpv6StaticRouteDelete,
       "wfIpv6StaticRouteDisable": wfIpv6StaticRouteDisable,
       "wfIpv6StaticRouteIfIndex": wfIpv6StaticRouteIfIndex,
       "wfIpv6StaticRouteId": wfIpv6StaticRouteId,
       "wfIpv6StaticRoutePfx": wfIpv6StaticRoutePfx,
       "wfIpv6StaticRoutePfxLength": wfIpv6StaticRoutePfxLength,
       "wfIpv6StaticRouteNextHopAddr": wfIpv6StaticRouteNextHopAddr,
       "wfIpv6StaticRoutePreference": wfIpv6StaticRoutePreference,
       "wfIpv6StaticRouteCost": wfIpv6StaticRouteCost,
       "wfIpv6StaticRouteInvalid": wfIpv6StaticRouteInvalid,
       "wfIpv6AdjacentNodeTable": wfIpv6AdjacentNodeTable,
       "wfIpv6AdjacentNodeEntry": wfIpv6AdjacentNodeEntry,
       "wfIpv6AdjNodeDelete": wfIpv6AdjNodeDelete,
       "wfIpv6AdjNodeDisable": wfIpv6AdjNodeDisable,
       "wfIpv6AdjNodeAddress": wfIpv6AdjNodeAddress,
       "wfIpv6AdjNodeIfIndex": wfIpv6AdjNodeIfIndex,
       "wfIpv6AdjNodePhysicalAddr": wfIpv6AdjNodePhysicalAddr,
       "wfIpv6AdjNodeEncaps": wfIpv6AdjNodeEncaps,
       "wfIpv6AdjNodePreference": wfIpv6AdjNodePreference,
       "wfIpv6AdjNodeCost": wfIpv6AdjNodeCost,
       "wfIpv6AdjNodeInvalid": wfIpv6AdjNodeInvalid,
       "wfIpv6AdjNodeWanAddr": wfIpv6AdjNodeWanAddr,
       "wfIpv6RouteTable": wfIpv6RouteTable,
       "wfIpv6RouteEntry": wfIpv6RouteEntry,
       "wfIpv6RouteDest": wfIpv6RouteDest,
       "wfIpv6RoutePfxLength": wfIpv6RoutePfxLength,
       "wfIpv6RouteIfIndex": wfIpv6RouteIfIndex,
       "wfIpv6RouteIndex": wfIpv6RouteIndex,
       "wfIpv6RouteNextHop": wfIpv6RouteNextHop,
       "wfIpv6RouteType": wfIpv6RouteType,
       "wfIpv6RouteProtocol": wfIpv6RouteProtocol,
       "wfIpv6RoutePolicy": wfIpv6RoutePolicy,
       "wfIpv6RouteAge": wfIpv6RouteAge,
       "wfIpv6RouteNextHopRDI": wfIpv6RouteNextHopRDI,
       "wfIpv6RouteMetric": wfIpv6RouteMetric,
       "wfIpv6RouteWeight": wfIpv6RouteWeight,
       "wfIpv6RouteInfo": wfIpv6RouteInfo,
       "wfIpv6NetToMediaEntryTable": wfIpv6NetToMediaEntryTable,
       "wfIpv6NetToMediaEntry": wfIpv6NetToMediaEntry,
       "wfIpv6NetToMediaIfIndex": wfIpv6NetToMediaIfIndex,
       "wfIpv6NetToMediaNetAddress": wfIpv6NetToMediaNetAddress,
       "wfIpv6NetToMediaPhysAddress": wfIpv6NetToMediaPhysAddress,
       "wfIpv6NetToMediaType": wfIpv6NetToMediaType,
       "wfIpv6NetToMediaInvalid": wfIpv6NetToMediaInvalid,
       "wfIpv6DbgInfoTable": wfIpv6DbgInfoTable,
       "wfIpv6DbgInfoEntry": wfIpv6DbgInfoEntry,
       "wfIpv6DbgInfoSlot": wfIpv6DbgInfoSlot,
       "wfIpv6DbgInfoState": wfIpv6DbgInfoState,
       "wfIpv6DbgInfoNetworks": wfIpv6DbgInfoNetworks,
       "wfIpv6DbgInfoNodes": wfIpv6DbgInfoNodes,
       "wfIpv6DbgInfoActiveInterfaces": wfIpv6DbgInfoActiveInterfaces,
       "wfIpv6DbgInfoRtmAddr": wfIpv6DbgInfoRtmAddr,
       "wfIpv6FilterTable": wfIpv6FilterTable,
       "wfIpv6FilterEntry": wfIpv6FilterEntry,
       "wfIpv6FilterDelete": wfIpv6FilterDelete,
       "wfIpv6FilterDisable": wfIpv6FilterDisable,
       "wfIpv6FilterNumber": wfIpv6FilterNumber,
       "wfIpv6FilterName": wfIpv6FilterName,
       "wfIpv6FilterPrecedence": wfIpv6FilterPrecedence,
       "wfIpv6FilterPackets": wfIpv6FilterPackets,
       "wfIpv6FilterOctets": wfIpv6FilterOctets,
       "wfIpv6FilterInIfIndex": wfIpv6FilterInIfIndex,
       "wfIpv6FilterOutIfIndex": wfIpv6FilterOutIfIndex,
       "wfIpv6FilterSrcAddresses": wfIpv6FilterSrcAddresses,
       "wfIpv6FilterDstAddresses": wfIpv6FilterDstAddresses,
       "wfIpv6FilterProtocols": wfIpv6FilterProtocols,
       "wfIpv6FilterAction": wfIpv6FilterAction,
       "wfIpv6FilterLog": wfIpv6FilterLog,
       "wfIpv6IcmpGroup": wfIpv6IcmpGroup,
       "wfIpv6IcmpTable": wfIpv6IcmpTable,
       "wfIpv6IcmpEntry": wfIpv6IcmpEntry,
       "wfIpv6IcmpIfIndex": wfIpv6IcmpIfIndex,
       "wfIpv6IcmpInMsgs": wfIpv6IcmpInMsgs,
       "wfIpv6IcmpInErrors": wfIpv6IcmpInErrors,
       "wfIpv6IcmpInDestUnreachs": wfIpv6IcmpInDestUnreachs,
       "wfIpv6IcmpInAdminProhibs": wfIpv6IcmpInAdminProhibs,
       "wfIpv6IcmpInTimeExcds": wfIpv6IcmpInTimeExcds,
       "wfIpv6IcmpInParmProbs": wfIpv6IcmpInParmProbs,
       "wfIpv6IcmpInPktTooBigs": wfIpv6IcmpInPktTooBigs,
       "wfIpv6IcmpInEchos": wfIpv6IcmpInEchos,
       "wfIpv6IcmpInEchoReps": wfIpv6IcmpInEchoReps,
       "wfIpv6IcmpInRouterSolicits": wfIpv6IcmpInRouterSolicits,
       "wfIpv6IcmpInRouterAdvertisements": wfIpv6IcmpInRouterAdvertisements,
       "wfIpv6IcmpInNeighborSolicits": wfIpv6IcmpInNeighborSolicits,
       "wfIpv6IcmpInNeighborAdvertisements": wfIpv6IcmpInNeighborAdvertisements,
       "wfIpv6IcmpInRedirects": wfIpv6IcmpInRedirects,
       "wfIpv6IcmpInGroupMembQueries": wfIpv6IcmpInGroupMembQueries,
       "wfIpv6IcmpInGroupMembResponses": wfIpv6IcmpInGroupMembResponses,
       "wfIpv6IcmpInGroupMembReductions": wfIpv6IcmpInGroupMembReductions,
       "wfIpv6IcmpOutMsgs": wfIpv6IcmpOutMsgs,
       "wfIpv6IcmpOutErrors": wfIpv6IcmpOutErrors,
       "wfIpv6IcmpOutDestUnreachs": wfIpv6IcmpOutDestUnreachs,
       "wfIpv6IcmpOutAdminProhibs": wfIpv6IcmpOutAdminProhibs,
       "wfIpv6IcmpOutTimeExcds": wfIpv6IcmpOutTimeExcds,
       "wfIpv6IcmpOutParmProbs": wfIpv6IcmpOutParmProbs,
       "wfIpv6IcmpOutPktTooBigs": wfIpv6IcmpOutPktTooBigs,
       "wfIpv6IcmpOutEchos": wfIpv6IcmpOutEchos,
       "wfIpv6IcmpOutEchoReps": wfIpv6IcmpOutEchoReps,
       "wfIpv6IcmpOutRouterSolicits": wfIpv6IcmpOutRouterSolicits,
       "wfIpv6IcmpOutRouterAdvertisements": wfIpv6IcmpOutRouterAdvertisements,
       "wfIpv6IcmpOutNeighborSolicits": wfIpv6IcmpOutNeighborSolicits,
       "wfIpv6IcmpOutNeighborAdvertisements": wfIpv6IcmpOutNeighborAdvertisements,
       "wfIpv6IcmpOutRedirects": wfIpv6IcmpOutRedirects,
       "wfIpv6IcmpOutGroupMembQueries": wfIpv6IcmpOutGroupMembQueries,
       "wfIpv6IcmpOutGroupMembResponses": wfIpv6IcmpOutGroupMembResponses,
       "wfIpv6IcmpOutGroupMembReductions": wfIpv6IcmpOutGroupMembReductions,
       "wfIpv6NDiscGroup": wfIpv6NDiscGroup,
       "wfIpv6NdiscIfTable": wfIpv6NdiscIfTable,
       "wfIpv6NdiscIfEntry": wfIpv6NdiscIfEntry,
       "wfIpv6NdiscIfDelete": wfIpv6NdiscIfDelete,
       "wfIpv6NdiscIfDisable": wfIpv6NdiscIfDisable,
       "wfIpv6NdiscIfState": wfIpv6NdiscIfState,
       "wfIpv6NdiscIfIndex": wfIpv6NdiscIfIndex,
       "wfIpv6NdiscIfSendAdvertisements": wfIpv6NdiscIfSendAdvertisements,
       "wfIpv6NdiscIfManagedFlag": wfIpv6NdiscIfManagedFlag,
       "wfIpv6NdiscIfOtherCfgFlag": wfIpv6NdiscIfOtherCfgFlag,
       "wfIpv6NdiscIfReachableTime": wfIpv6NdiscIfReachableTime,
       "wfIpv6NdiscIfRetransTimer": wfIpv6NdiscIfRetransTimer,
       "wfIpv6NdiscIfMaxHopLimit": wfIpv6NdiscIfMaxHopLimit,
       "wfIpv6NdiscIfMinRtrAdvInterval": wfIpv6NdiscIfMinRtrAdvInterval,
       "wfIpv6NdiscIfMaxRtrAdvInterval": wfIpv6NdiscIfMaxRtrAdvInterval,
       "wfIpv6NdiscIfDefaultLifetime": wfIpv6NdiscIfDefaultLifetime,
       "wfIpv6NdiscIfDupAddrDetectTransmits": wfIpv6NdiscIfDupAddrDetectTransmits,
       "wfIpv6UdpGroup": wfIpv6UdpGroup,
       "wfIpv6Udp": wfIpv6Udp,
       "wfIpv6UdpInDatagrams": wfIpv6UdpInDatagrams,
       "wfIpv6UdpNoPorts": wfIpv6UdpNoPorts,
       "wfIpv6UdpInErrors": wfIpv6UdpInErrors,
       "wfIpv6UdpOutDatagrams": wfIpv6UdpOutDatagrams,
       "wfIpv6UdpTable": wfIpv6UdpTable,
       "wfIpv6UdpEntry": wfIpv6UdpEntry,
       "wfIpv6UdpLocalIfIndex": wfIpv6UdpLocalIfIndex,
       "wfIpv6UdpLocalAddress": wfIpv6UdpLocalAddress,
       "wfIpv6UdpLocalPort": wfIpv6UdpLocalPort,
       "wfIpv6LogGroup": wfIpv6LogGroup,
       "wfIpv6Log": wfIpv6Log,
       "wfIpv6LogDelete": wfIpv6LogDelete,
       "wfIpv6LogDisable": wfIpv6LogDisable,
       "wfIpv6LogLevel": wfIpv6LogLevel,
       "wfIpv6LogEvent": wfIpv6LogEvent,
       "wfIpv6LogEventDisable": wfIpv6LogEventDisable,
       "wfIpv6LogEvents": wfIpv6LogEvents,
       "wfIpv6LogCfgEvents": wfIpv6LogCfgEvents,
       "wfIpv6PolicyGroup": wfIpv6PolicyGroup}
)

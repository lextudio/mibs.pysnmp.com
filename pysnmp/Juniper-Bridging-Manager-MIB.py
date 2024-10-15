# SNMP MIB module (Juniper-Bridging-Manager-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-Bridging-Manager-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:49 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

juniBridgingMgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64)
)
juniBridgingMgrMIB.setRevisions(
        ("2002-10-11 20:25",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniBridgingMgrBridgeRouteMask(Integer32, TextualConvention):
    status = "current"


class JuniBridgingMgrNextIndex(Unsigned32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_JuniBridgingMgrBridgeGroup_ObjectIdentity = ObjectIdentity
juniBridgingMgrBridgeGroup = _JuniBridgingMgrBridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1)
)
_JuniBridgingMgrNextIndex_Type = JuniBridgingMgrNextIndex
_JuniBridgingMgrNextIndex_Object = MibScalar
juniBridgingMgrNextIndex = _JuniBridgingMgrNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 1),
    _JuniBridgingMgrNextIndex_Type()
)
juniBridgingMgrNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBridgingMgrNextIndex.setStatus("current")
_JuniBridgingMgrBridgeGroupTable_Object = MibTable
juniBridgingMgrBridgeGroupTable = _JuniBridgingMgrBridgeGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 3)
)
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeGroupTable.setStatus("current")
_JuniBridgingMgrBridgeGroupEntry_Object = MibTableRow
juniBridgingMgrBridgeGroupEntry = _JuniBridgingMgrBridgeGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 3, 1)
)
juniBridgingMgrBridgeGroupEntry.setIndexNames(
    (0, "Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeGroupIndex"),
)
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeGroupEntry.setStatus("current")


class _JuniBridgingMgrBridgeGroupIndex_Type(Unsigned32):
    """Custom type juniBridgingMgrBridgeGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JuniBridgingMgrBridgeGroupIndex_Type.__name__ = "Unsigned32"
_JuniBridgingMgrBridgeGroupIndex_Object = MibTableColumn
juniBridgingMgrBridgeGroupIndex = _JuniBridgingMgrBridgeGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 3, 1, 1),
    _JuniBridgingMgrBridgeGroupIndex_Type()
)
juniBridgingMgrBridgeGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeGroupIndex.setStatus("current")
_JuniBridgingMgrBridgeRowStatus_Type = RowStatus
_JuniBridgingMgrBridgeRowStatus_Object = MibTableColumn
juniBridgingMgrBridgeRowStatus = _JuniBridgingMgrBridgeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 3, 1, 2),
    _JuniBridgingMgrBridgeRowStatus_Type()
)
juniBridgingMgrBridgeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeRowStatus.setStatus("current")


class _JuniBridgingMgrBridgeGroupLearning_Type(Integer32):
    """Custom type juniBridgingMgrBridgeGroupLearning based on Integer32"""
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


_JuniBridgingMgrBridgeGroupLearning_Type.__name__ = "Integer32"
_JuniBridgingMgrBridgeGroupLearning_Object = MibTableColumn
juniBridgingMgrBridgeGroupLearning = _JuniBridgingMgrBridgeGroupLearning_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 3, 1, 3),
    _JuniBridgingMgrBridgeGroupLearning_Type()
)
juniBridgingMgrBridgeGroupLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeGroupLearning.setStatus("current")


class _JuniBridgingMgrBridgeGroupName_Type(DisplayString):
    """Custom type juniBridgingMgrBridgeGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBridgingMgrBridgeGroupName_Type.__name__ = "DisplayString"
_JuniBridgingMgrBridgeGroupName_Object = MibTableColumn
juniBridgingMgrBridgeGroupName = _JuniBridgingMgrBridgeGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 3, 1, 4),
    _JuniBridgingMgrBridgeGroupName_Type()
)
juniBridgingMgrBridgeGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeGroupName.setStatus("current")
_JuniBridgingMgrBridgeGroupSPolicyIndex_Type = Integer32
_JuniBridgingMgrBridgeGroupSPolicyIndex_Object = MibTableColumn
juniBridgingMgrBridgeGroupSPolicyIndex = _JuniBridgingMgrBridgeGroupSPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 3, 1, 5),
    _JuniBridgingMgrBridgeGroupSPolicyIndex_Type()
)
juniBridgingMgrBridgeGroupSPolicyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeGroupSPolicyIndex.setStatus("current")
_JuniBridgingMgrBridgeGroupRouteProtocol_Type = JuniBridgingMgrBridgeRouteMask
_JuniBridgingMgrBridgeGroupRouteProtocol_Object = MibTableColumn
juniBridgingMgrBridgeGroupRouteProtocol = _JuniBridgingMgrBridgeGroupRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 3, 1, 6),
    _JuniBridgingMgrBridgeGroupRouteProtocol_Type()
)
juniBridgingMgrBridgeGroupRouteProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeGroupRouteProtocol.setStatus("current")


class _JuniBridgingMgrBridgeGroupLearnCount_Type(Integer32):
    """Custom type juniBridgingMgrBridgeGroupLearnCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_JuniBridgingMgrBridgeGroupLearnCount_Type.__name__ = "Integer32"
_JuniBridgingMgrBridgeGroupLearnCount_Object = MibTableColumn
juniBridgingMgrBridgeGroupLearnCount = _JuniBridgingMgrBridgeGroupLearnCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 3, 1, 7),
    _JuniBridgingMgrBridgeGroupLearnCount_Type()
)
juniBridgingMgrBridgeGroupLearnCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeGroupLearnCount.setStatus("current")
_JuniBridgingMgrBridgeSubscriberPolicy_ObjectIdentity = ObjectIdentity
juniBridgingMgrBridgeSubscriberPolicy = _JuniBridgingMgrBridgeSubscriberPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2)
)


class _JuniBridgingMgrSubscriberNextIndex_Type(Integer32):
    """Custom type juniBridgingMgrSubscriberNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniBridgingMgrSubscriberNextIndex_Type.__name__ = "Integer32"
_JuniBridgingMgrSubscriberNextIndex_Object = MibScalar
juniBridgingMgrSubscriberNextIndex = _JuniBridgingMgrSubscriberNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 1),
    _JuniBridgingMgrSubscriberNextIndex_Type()
)
juniBridgingMgrSubscriberNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBridgingMgrSubscriberNextIndex.setStatus("current")
_JuniBridgingMgrBridgeSubscriberPolicyTable_Object = MibTable
juniBridgingMgrBridgeSubscriberPolicyTable = _JuniBridgingMgrBridgeSubscriberPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2)
)
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeSubscriberPolicyTable.setStatus("current")
_JuniBridgingMgrBridgeSubscriberPolicyEntry_Object = MibTableRow
juniBridgingMgrBridgeSubscriberPolicyEntry = _JuniBridgingMgrBridgeSubscriberPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1)
)
juniBridgingMgrBridgeSubscriberPolicyEntry.setIndexNames(
    (0, "Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyIndex"),
)
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeSubscriberPolicyEntry.setStatus("current")


class _JuniBridgingMgrBridgeSubscriberPolicyIndex_Type(Integer32):
    """Custom type juniBridgingMgrBridgeSubscriberPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniBridgingMgrBridgeSubscriberPolicyIndex_Type.__name__ = "Integer32"
_JuniBridgingMgrBridgeSubscriberPolicyIndex_Object = MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyIndex = _JuniBridgingMgrBridgeSubscriberPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 1),
    _JuniBridgingMgrBridgeSubscriberPolicyIndex_Type()
)
juniBridgingMgrBridgeSubscriberPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeSubscriberPolicyIndex.setStatus("current")
_JuniBridgingMgrBridgeSubscriberPolicyRowStatus_Type = RowStatus
_JuniBridgingMgrBridgeSubscriberPolicyRowStatus_Object = MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyRowStatus = _JuniBridgingMgrBridgeSubscriberPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 2),
    _JuniBridgingMgrBridgeSubscriberPolicyRowStatus_Type()
)
juniBridgingMgrBridgeSubscriberPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeSubscriberPolicyRowStatus.setStatus("current")


class _JuniBridgingMgrBridgeSubscriberPolicyArp_Type(Integer32):
    """Custom type juniBridgingMgrBridgeSubscriberPolicyArp based on Integer32"""
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


_JuniBridgingMgrBridgeSubscriberPolicyArp_Type.__name__ = "Integer32"
_JuniBridgingMgrBridgeSubscriberPolicyArp_Object = MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyArp = _JuniBridgingMgrBridgeSubscriberPolicyArp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 3),
    _JuniBridgingMgrBridgeSubscriberPolicyArp_Type()
)
juniBridgingMgrBridgeSubscriberPolicyArp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeSubscriberPolicyArp.setStatus("current")


class _JuniBridgingMgrBridgeSubscriberPolicyBroadcast_Type(Integer32):
    """Custom type juniBridgingMgrBridgeSubscriberPolicyBroadcast based on Integer32"""
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


_JuniBridgingMgrBridgeSubscriberPolicyBroadcast_Type.__name__ = "Integer32"
_JuniBridgingMgrBridgeSubscriberPolicyBroadcast_Object = MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyBroadcast = _JuniBridgingMgrBridgeSubscriberPolicyBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 4),
    _JuniBridgingMgrBridgeSubscriberPolicyBroadcast_Type()
)
juniBridgingMgrBridgeSubscriberPolicyBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeSubscriberPolicyBroadcast.setStatus("current")


class _JuniBridgingMgrBridgeSubscriberPolicyMulticast_Type(Integer32):
    """Custom type juniBridgingMgrBridgeSubscriberPolicyMulticast based on Integer32"""
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


_JuniBridgingMgrBridgeSubscriberPolicyMulticast_Type.__name__ = "Integer32"
_JuniBridgingMgrBridgeSubscriberPolicyMulticast_Object = MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyMulticast = _JuniBridgingMgrBridgeSubscriberPolicyMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 5),
    _JuniBridgingMgrBridgeSubscriberPolicyMulticast_Type()
)
juniBridgingMgrBridgeSubscriberPolicyMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeSubscriberPolicyMulticast.setStatus("current")


class _JuniBridgingMgrBridgeSubscriberPolicyUnknownUnicast_Type(Integer32):
    """Custom type juniBridgingMgrBridgeSubscriberPolicyUnknownUnicast based on Integer32"""
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


_JuniBridgingMgrBridgeSubscriberPolicyUnknownUnicast_Type.__name__ = "Integer32"
_JuniBridgingMgrBridgeSubscriberPolicyUnknownUnicast_Object = MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyUnknownUnicast = _JuniBridgingMgrBridgeSubscriberPolicyUnknownUnicast_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 6),
    _JuniBridgingMgrBridgeSubscriberPolicyUnknownUnicast_Type()
)
juniBridgingMgrBridgeSubscriberPolicyUnknownUnicast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeSubscriberPolicyUnknownUnicast.setStatus("current")


class _JuniBridgingMgrBridgeSubscriberPolicyIp_Type(Integer32):
    """Custom type juniBridgingMgrBridgeSubscriberPolicyIp based on Integer32"""
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


_JuniBridgingMgrBridgeSubscriberPolicyIp_Type.__name__ = "Integer32"
_JuniBridgingMgrBridgeSubscriberPolicyIp_Object = MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyIp = _JuniBridgingMgrBridgeSubscriberPolicyIp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 7),
    _JuniBridgingMgrBridgeSubscriberPolicyIp_Type()
)
juniBridgingMgrBridgeSubscriberPolicyIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeSubscriberPolicyIp.setStatus("current")


class _JuniBridgingMgrBridgeSubscriberPolicyUnknownProtocol_Type(Integer32):
    """Custom type juniBridgingMgrBridgeSubscriberPolicyUnknownProtocol based on Integer32"""
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


_JuniBridgingMgrBridgeSubscriberPolicyUnknownProtocol_Type.__name__ = "Integer32"
_JuniBridgingMgrBridgeSubscriberPolicyUnknownProtocol_Object = MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyUnknownProtocol = _JuniBridgingMgrBridgeSubscriberPolicyUnknownProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 8),
    _JuniBridgingMgrBridgeSubscriberPolicyUnknownProtocol_Type()
)
juniBridgingMgrBridgeSubscriberPolicyUnknownProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeSubscriberPolicyUnknownProtocol.setStatus("current")


class _JuniBridgingMgrBridgeSubscriberPolicyUnicast_Type(Integer32):
    """Custom type juniBridgingMgrBridgeSubscriberPolicyUnicast based on Integer32"""
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


_JuniBridgingMgrBridgeSubscriberPolicyUnicast_Type.__name__ = "Integer32"
_JuniBridgingMgrBridgeSubscriberPolicyUnicast_Object = MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyUnicast = _JuniBridgingMgrBridgeSubscriberPolicyUnicast_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 9),
    _JuniBridgingMgrBridgeSubscriberPolicyUnicast_Type()
)
juniBridgingMgrBridgeSubscriberPolicyUnicast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeSubscriberPolicyUnicast.setStatus("current")


class _JuniBridgingMgrBridgeSubscriberPolicyPPPoE_Type(Integer32):
    """Custom type juniBridgingMgrBridgeSubscriberPolicyPPPoE based on Integer32"""
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


_JuniBridgingMgrBridgeSubscriberPolicyPPPoE_Type.__name__ = "Integer32"
_JuniBridgingMgrBridgeSubscriberPolicyPPPoE_Object = MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyPPPoE = _JuniBridgingMgrBridgeSubscriberPolicyPPPoE_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 10),
    _JuniBridgingMgrBridgeSubscriberPolicyPPPoE_Type()
)
juniBridgingMgrBridgeSubscriberPolicyPPPoE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeSubscriberPolicyPPPoE.setStatus("current")


class _JuniBridgingMgrBridgeSubscriberPolicyRelearn_Type(Integer32):
    """Custom type juniBridgingMgrBridgeSubscriberPolicyRelearn based on Integer32"""
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


_JuniBridgingMgrBridgeSubscriberPolicyRelearn_Type.__name__ = "Integer32"
_JuniBridgingMgrBridgeSubscriberPolicyRelearn_Object = MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyRelearn = _JuniBridgingMgrBridgeSubscriberPolicyRelearn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 11),
    _JuniBridgingMgrBridgeSubscriberPolicyRelearn_Type()
)
juniBridgingMgrBridgeSubscriberPolicyRelearn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeSubscriberPolicyRelearn.setStatus("current")


class _JuniBridgingMgrBridgeSubscriberPolicyMpls_Type(Integer32):
    """Custom type juniBridgingMgrBridgeSubscriberPolicyMpls based on Integer32"""
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


_JuniBridgingMgrBridgeSubscriberPolicyMpls_Type.__name__ = "Integer32"
_JuniBridgingMgrBridgeSubscriberPolicyMpls_Object = MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyMpls = _JuniBridgingMgrBridgeSubscriberPolicyMpls_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 12),
    _JuniBridgingMgrBridgeSubscriberPolicyMpls_Type()
)
juniBridgingMgrBridgeSubscriberPolicyMpls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeSubscriberPolicyMpls.setStatus("current")


class _JuniBridgingMgrBridgeSubscriberPolicyName_Type(DisplayString):
    """Custom type juniBridgingMgrBridgeSubscriberPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBridgingMgrBridgeSubscriberPolicyName_Type.__name__ = "DisplayString"
_JuniBridgingMgrBridgeSubscriberPolicyName_Object = MibTableColumn
juniBridgingMgrBridgeSubscriberPolicyName = _JuniBridgingMgrBridgeSubscriberPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 13),
    _JuniBridgingMgrBridgeSubscriberPolicyName_Type()
)
juniBridgingMgrBridgeSubscriberPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeSubscriberPolicyName.setStatus("current")
_JuniBridgingMgrBridge_ObjectIdentity = ObjectIdentity
juniBridgingMgrBridge = _JuniBridgingMgrBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 3)
)


class _JuniBridgingMgrBridgeMode_Type(Integer32):
    """Custom type juniBridgingMgrBridgeMode based on Integer32"""
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
        *(("crb", 1),
          ("default", 0),
          ("irb", 2),
          ("other", 3))
    )


_JuniBridgingMgrBridgeMode_Type.__name__ = "Integer32"
_JuniBridgingMgrBridgeMode_Object = MibScalar
juniBridgingMgrBridgeMode = _JuniBridgingMgrBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 3, 1),
    _JuniBridgingMgrBridgeMode_Type()
)
juniBridgingMgrBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBridgingMgrBridgeMode.setStatus("current")
_JuniBridgingMgrConformance_ObjectIdentity = ObjectIdentity
juniBridgingMgrConformance = _JuniBridgingMgrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 4)
)
_JuniBridgingMgrCompliances_ObjectIdentity = ObjectIdentity
juniBridgingMgrCompliances = _JuniBridgingMgrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 4, 1)
)
_JuniBridgingMgrGroups_ObjectIdentity = ObjectIdentity
juniBridgingMgrGroups = _JuniBridgingMgrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 4, 2)
)

# Managed Objects groups

juniBridgingMgrConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 4, 2, 1)
)
juniBridgingMgrConfGroup.setObjects(
      *(("Juniper-Bridging-Manager-MIB", "juniBridgingMgrNextIndex"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeRowStatus"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeGroupLearning"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeGroupName"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeGroupSPolicyIndex"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeGroupRouteProtocol"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeGroupLearnCount"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrSubscriberNextIndex"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyRowStatus"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyArp"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyBroadcast"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyMulticast"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyUnknownUnicast"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyIp"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyUnknownProtocol"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyUnicast"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyPPPoE"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyRelearn"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyMpls"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyName"),
        ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeMode"))
)
if mibBuilder.loadTexts:
    juniBridgingMgrConfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniBridgingMgrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniBridgingMgrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-Bridging-Manager-MIB",
    **{"JuniBridgingMgrBridgeRouteMask": JuniBridgingMgrBridgeRouteMask,
       "JuniBridgingMgrNextIndex": JuniBridgingMgrNextIndex,
       "juniBridgingMgrMIB": juniBridgingMgrMIB,
       "juniBridgingMgrBridgeGroup": juniBridgingMgrBridgeGroup,
       "juniBridgingMgrNextIndex": juniBridgingMgrNextIndex,
       "juniBridgingMgrBridgeGroupTable": juniBridgingMgrBridgeGroupTable,
       "juniBridgingMgrBridgeGroupEntry": juniBridgingMgrBridgeGroupEntry,
       "juniBridgingMgrBridgeGroupIndex": juniBridgingMgrBridgeGroupIndex,
       "juniBridgingMgrBridgeRowStatus": juniBridgingMgrBridgeRowStatus,
       "juniBridgingMgrBridgeGroupLearning": juniBridgingMgrBridgeGroupLearning,
       "juniBridgingMgrBridgeGroupName": juniBridgingMgrBridgeGroupName,
       "juniBridgingMgrBridgeGroupSPolicyIndex": juniBridgingMgrBridgeGroupSPolicyIndex,
       "juniBridgingMgrBridgeGroupRouteProtocol": juniBridgingMgrBridgeGroupRouteProtocol,
       "juniBridgingMgrBridgeGroupLearnCount": juniBridgingMgrBridgeGroupLearnCount,
       "juniBridgingMgrBridgeSubscriberPolicy": juniBridgingMgrBridgeSubscriberPolicy,
       "juniBridgingMgrSubscriberNextIndex": juniBridgingMgrSubscriberNextIndex,
       "juniBridgingMgrBridgeSubscriberPolicyTable": juniBridgingMgrBridgeSubscriberPolicyTable,
       "juniBridgingMgrBridgeSubscriberPolicyEntry": juniBridgingMgrBridgeSubscriberPolicyEntry,
       "juniBridgingMgrBridgeSubscriberPolicyIndex": juniBridgingMgrBridgeSubscriberPolicyIndex,
       "juniBridgingMgrBridgeSubscriberPolicyRowStatus": juniBridgingMgrBridgeSubscriberPolicyRowStatus,
       "juniBridgingMgrBridgeSubscriberPolicyArp": juniBridgingMgrBridgeSubscriberPolicyArp,
       "juniBridgingMgrBridgeSubscriberPolicyBroadcast": juniBridgingMgrBridgeSubscriberPolicyBroadcast,
       "juniBridgingMgrBridgeSubscriberPolicyMulticast": juniBridgingMgrBridgeSubscriberPolicyMulticast,
       "juniBridgingMgrBridgeSubscriberPolicyUnknownUnicast": juniBridgingMgrBridgeSubscriberPolicyUnknownUnicast,
       "juniBridgingMgrBridgeSubscriberPolicyIp": juniBridgingMgrBridgeSubscriberPolicyIp,
       "juniBridgingMgrBridgeSubscriberPolicyUnknownProtocol": juniBridgingMgrBridgeSubscriberPolicyUnknownProtocol,
       "juniBridgingMgrBridgeSubscriberPolicyUnicast": juniBridgingMgrBridgeSubscriberPolicyUnicast,
       "juniBridgingMgrBridgeSubscriberPolicyPPPoE": juniBridgingMgrBridgeSubscriberPolicyPPPoE,
       "juniBridgingMgrBridgeSubscriberPolicyRelearn": juniBridgingMgrBridgeSubscriberPolicyRelearn,
       "juniBridgingMgrBridgeSubscriberPolicyMpls": juniBridgingMgrBridgeSubscriberPolicyMpls,
       "juniBridgingMgrBridgeSubscriberPolicyName": juniBridgingMgrBridgeSubscriberPolicyName,
       "juniBridgingMgrBridge": juniBridgingMgrBridge,
       "juniBridgingMgrBridgeMode": juniBridgingMgrBridgeMode,
       "juniBridgingMgrConformance": juniBridgingMgrConformance,
       "juniBridgingMgrCompliances": juniBridgingMgrCompliances,
       "juniBridgingMgrCompliance": juniBridgingMgrCompliance,
       "juniBridgingMgrGroups": juniBridgingMgrGroups,
       "juniBridgingMgrConfGroup": juniBridgingMgrConfGroup}
)

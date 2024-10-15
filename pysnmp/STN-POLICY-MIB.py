# SNMP MIB module (STN-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:12 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(stnSystems,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnSystems")

(stnRouterIndex,) = mibBuilder.importSymbols(
    "STN-ROUTER-MIB",
    "stnRouterIndex")


# MODULE-IDENTITY

stnPm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11)
)
stnPm.setRevisions(
        ("1900-05-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class StnPmPolicyMatchType(Integer32, TextualConvention):
    status = "current"
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
        *(("any", 1),
          ("dynamic", 4),
          ("range", 3),
          ("single", 2),
          ("subnet", 5))
    )



class StnPmSelectorType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet", 2),
          ("policy", 1))
    )



class StnPmAuthAlg(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hmac-md5", 2),
          ("hmac-sha", 3),
          ("none", 1))
    )



class StnPmEncrAlg(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("des", 2),
          ("des3", 3),
          ("none", 1))
    )



class StnPmDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )



class StnPmBitRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_StnPmObjects_ObjectIdentity = ObjectIdentity
stnPmObjects = _StnPmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1)
)
_StnPmService_ObjectIdentity = ObjectIdentity
stnPmService = _StnPmService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 1)
)
_StnPmServiceTable_Object = MibTable
stnPmServiceTable = _StnPmServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    stnPmServiceTable.setStatus("current")
_StnPmServiceEntry_Object = MibTableRow
stnPmServiceEntry = _StnPmServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 1, 1, 1)
)
stnPmServiceEntry.setIndexNames(
    (0, "STN-POLICY-MIB", "stnPmServiceIndex"),
)
if mibBuilder.loadTexts:
    stnPmServiceEntry.setStatus("current")
_StnPmServiceIndex_Type = Integer32
_StnPmServiceIndex_Object = MibTableColumn
stnPmServiceIndex = _StnPmServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 1, 1, 1, 1),
    _StnPmServiceIndex_Type()
)
stnPmServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmServiceIndex.setStatus("current")


class _StnPmServiceName_Type(DisplayString):
    """Custom type stnPmServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_StnPmServiceName_Type.__name__ = "DisplayString"
_StnPmServiceName_Object = MibTableColumn
stnPmServiceName = _StnPmServiceName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 1, 1, 1, 2),
    _StnPmServiceName_Type()
)
stnPmServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmServiceName.setStatus("current")
_StnPmServiceIdleTimeout_Type = Integer32
_StnPmServiceIdleTimeout_Object = MibTableColumn
stnPmServiceIdleTimeout = _StnPmServiceIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 1, 1, 1, 3),
    _StnPmServiceIdleTimeout_Type()
)
stnPmServiceIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmServiceIdleTimeout.setStatus("current")
_StnPmServiceNumPolicies_Type = Integer32
_StnPmServiceNumPolicies_Object = MibTableColumn
stnPmServiceNumPolicies = _StnPmServiceNumPolicies_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 1, 1, 1, 4),
    _StnPmServiceNumPolicies_Type()
)
stnPmServiceNumPolicies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmServiceNumPolicies.setStatus("current")
_StnPmServiceEnabled_Type = TruthValue
_StnPmServiceEnabled_Object = MibTableColumn
stnPmServiceEnabled = _StnPmServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 1, 1, 1, 5),
    _StnPmServiceEnabled_Type()
)
stnPmServiceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmServiceEnabled.setStatus("current")


class _StnPmServiceType_Type(Integer32):
    """Custom type stnPmServiceType based on Integer32"""
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
        *(("firewall", 2),
          ("forwarding", 4),
          ("ip-fileter", 3),
          ("mpls", 6),
          ("qos", 5),
          ("vpn", 1))
    )


_StnPmServiceType_Type.__name__ = "Integer32"
_StnPmServiceType_Object = MibTableColumn
stnPmServiceType = _StnPmServiceType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 1, 1, 1, 7),
    _StnPmServiceType_Type()
)
stnPmServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmServiceType.setStatus("current")
_StnPmServiceFirewallID_Type = Integer32
_StnPmServiceFirewallID_Object = MibTableColumn
stnPmServiceFirewallID = _StnPmServiceFirewallID_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 1, 1, 1, 8),
    _StnPmServiceFirewallID_Type()
)
stnPmServiceFirewallID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmServiceFirewallID.setStatus("current")
_StnPmPolicy_ObjectIdentity = ObjectIdentity
stnPmPolicy = _StnPmPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2)
)
_StnPmPolicyTable_Object = MibTable
stnPmPolicyTable = _StnPmPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    stnPmPolicyTable.setStatus("current")
_StnPmPolicyEntry_Object = MibTableRow
stnPmPolicyEntry = _StnPmPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1)
)
stnPmPolicyEntry.setIndexNames(
    (0, "STN-POLICY-MIB", "stnPmPolicyServiceIndex"),
    (0, "STN-POLICY-MIB", "stnPmPolicyIndex"),
)
if mibBuilder.loadTexts:
    stnPmPolicyEntry.setStatus("current")
_StnPmPolicyServiceIndex_Type = Integer32
_StnPmPolicyServiceIndex_Object = MibTableColumn
stnPmPolicyServiceIndex = _StnPmPolicyServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 1),
    _StnPmPolicyServiceIndex_Type()
)
stnPmPolicyServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyServiceIndex.setStatus("current")
_StnPmPolicyIndex_Type = Integer32
_StnPmPolicyIndex_Object = MibTableColumn
stnPmPolicyIndex = _StnPmPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 2),
    _StnPmPolicyIndex_Type()
)
stnPmPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyIndex.setStatus("current")


class _StnPmPolicyName_Type(DisplayString):
    """Custom type stnPmPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_StnPmPolicyName_Type.__name__ = "DisplayString"
_StnPmPolicyName_Object = MibTableColumn
stnPmPolicyName = _StnPmPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 3),
    _StnPmPolicyName_Type()
)
stnPmPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyName.setStatus("current")
_StnPmPolicySrcAddrMatchType_Type = StnPmPolicyMatchType
_StnPmPolicySrcAddrMatchType_Object = MibTableColumn
stnPmPolicySrcAddrMatchType = _StnPmPolicySrcAddrMatchType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 4),
    _StnPmPolicySrcAddrMatchType_Type()
)
stnPmPolicySrcAddrMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicySrcAddrMatchType.setStatus("current")
_StnPmPolicySrcAddr_Type = IpAddress
_StnPmPolicySrcAddr_Object = MibTableColumn
stnPmPolicySrcAddr = _StnPmPolicySrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 5),
    _StnPmPolicySrcAddr_Type()
)
stnPmPolicySrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicySrcAddr.setStatus("current")
_StnPmPolicySrcMask_Type = IpAddress
_StnPmPolicySrcMask_Object = MibTableColumn
stnPmPolicySrcMask = _StnPmPolicySrcMask_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 6),
    _StnPmPolicySrcMask_Type()
)
stnPmPolicySrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicySrcMask.setStatus("current")
_StnPmPolicySrcEndAddr_Type = IpAddress
_StnPmPolicySrcEndAddr_Object = MibTableColumn
stnPmPolicySrcEndAddr = _StnPmPolicySrcEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 7),
    _StnPmPolicySrcEndAddr_Type()
)
stnPmPolicySrcEndAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicySrcEndAddr.setStatus("current")
_StnPmPolicyDestAddrMatchType_Type = StnPmPolicyMatchType
_StnPmPolicyDestAddrMatchType_Object = MibTableColumn
stnPmPolicyDestAddrMatchType = _StnPmPolicyDestAddrMatchType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 8),
    _StnPmPolicyDestAddrMatchType_Type()
)
stnPmPolicyDestAddrMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyDestAddrMatchType.setStatus("current")
_StnPmPolicyDestAddr_Type = IpAddress
_StnPmPolicyDestAddr_Object = MibTableColumn
stnPmPolicyDestAddr = _StnPmPolicyDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 9),
    _StnPmPolicyDestAddr_Type()
)
stnPmPolicyDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyDestAddr.setStatus("current")
_StnPmPolicyDestMask_Type = IpAddress
_StnPmPolicyDestMask_Object = MibTableColumn
stnPmPolicyDestMask = _StnPmPolicyDestMask_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 10),
    _StnPmPolicyDestMask_Type()
)
stnPmPolicyDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyDestMask.setStatus("current")
_StnPmPolicyDestEndAddr_Type = IpAddress
_StnPmPolicyDestEndAddr_Object = MibTableColumn
stnPmPolicyDestEndAddr = _StnPmPolicyDestEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 11),
    _StnPmPolicyDestEndAddr_Type()
)
stnPmPolicyDestEndAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyDestEndAddr.setStatus("current")
_StnPmPolicySrcPortMatchType_Type = StnPmPolicyMatchType
_StnPmPolicySrcPortMatchType_Object = MibTableColumn
stnPmPolicySrcPortMatchType = _StnPmPolicySrcPortMatchType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 12),
    _StnPmPolicySrcPortMatchType_Type()
)
stnPmPolicySrcPortMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicySrcPortMatchType.setStatus("current")
_StnPmPolicySrcPort_Type = Integer32
_StnPmPolicySrcPort_Object = MibTableColumn
stnPmPolicySrcPort = _StnPmPolicySrcPort_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 13),
    _StnPmPolicySrcPort_Type()
)
stnPmPolicySrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicySrcPort.setStatus("current")
_StnPmPolicySrcEndPort_Type = Integer32
_StnPmPolicySrcEndPort_Object = MibTableColumn
stnPmPolicySrcEndPort = _StnPmPolicySrcEndPort_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 14),
    _StnPmPolicySrcEndPort_Type()
)
stnPmPolicySrcEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicySrcEndPort.setStatus("current")
_StnPmPolicyDestPortMatchType_Type = StnPmPolicyMatchType
_StnPmPolicyDestPortMatchType_Object = MibTableColumn
stnPmPolicyDestPortMatchType = _StnPmPolicyDestPortMatchType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 15),
    _StnPmPolicyDestPortMatchType_Type()
)
stnPmPolicyDestPortMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyDestPortMatchType.setStatus("current")
_StnPmPolicyDestPort_Type = Integer32
_StnPmPolicyDestPort_Object = MibTableColumn
stnPmPolicyDestPort = _StnPmPolicyDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 16),
    _StnPmPolicyDestPort_Type()
)
stnPmPolicyDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyDestPort.setStatus("current")
_StnPmPolicyDestEndPort_Type = Integer32
_StnPmPolicyDestEndPort_Object = MibTableColumn
stnPmPolicyDestEndPort = _StnPmPolicyDestEndPort_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 17),
    _StnPmPolicyDestEndPort_Type()
)
stnPmPolicyDestEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyDestEndPort.setStatus("current")
_StnPmPolicyProtocolMatchType_Type = StnPmPolicyMatchType
_StnPmPolicyProtocolMatchType_Object = MibTableColumn
stnPmPolicyProtocolMatchType = _StnPmPolicyProtocolMatchType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 18),
    _StnPmPolicyProtocolMatchType_Type()
)
stnPmPolicyProtocolMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyProtocolMatchType.setStatus("current")


class _StnPmPolicyProtocol_Type(Integer32):
    """Custom type stnPmPolicyProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              17,
              50,
              51,
              108)
        )
    )
    namedValues = NamedValues(
        *(("ah", 51),
          ("esp", 50),
          ("icmp", 1),
          ("ipcomp", 108),
          ("tcp", 6),
          ("udp", 17))
    )


_StnPmPolicyProtocol_Type.__name__ = "Integer32"
_StnPmPolicyProtocol_Object = MibTableColumn
stnPmPolicyProtocol = _StnPmPolicyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 19),
    _StnPmPolicyProtocol_Type()
)
stnPmPolicyProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyProtocol.setStatus("current")


class _StnPmPolicyAction_Type(Integer32):
    """Custom type stnPmPolicyAction based on Integer32"""
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
        *(("deny", 1),
          ("encaps", 4),
          ("fec", 6),
          ("permit", 2),
          ("reject", 5),
          ("secure", 3))
    )


_StnPmPolicyAction_Type.__name__ = "Integer32"
_StnPmPolicyAction_Object = MibTableColumn
stnPmPolicyAction = _StnPmPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 20),
    _StnPmPolicyAction_Type()
)
stnPmPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyAction.setStatus("current")
_StnPmPolicyActionID_Type = Integer32
_StnPmPolicyActionID_Object = MibTableColumn
stnPmPolicyActionID = _StnPmPolicyActionID_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 21),
    _StnPmPolicyActionID_Type()
)
stnPmPolicyActionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyActionID.setStatus("current")
_StnPmPolicyDirection_Type = StnPmDirection
_StnPmPolicyDirection_Object = MibTableColumn
stnPmPolicyDirection = _StnPmPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 22),
    _StnPmPolicyDirection_Type()
)
stnPmPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyDirection.setStatus("current")
_StnPmPolicyCreateMirror_Type = TruthValue
_StnPmPolicyCreateMirror_Object = MibTableColumn
stnPmPolicyCreateMirror = _StnPmPolicyCreateMirror_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 23),
    _StnPmPolicyCreateMirror_Type()
)
stnPmPolicyCreateMirror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyCreateMirror.setStatus("current")
_StnPmPolicySrcAddrSelector_Type = StnPmSelectorType
_StnPmPolicySrcAddrSelector_Object = MibTableColumn
stnPmPolicySrcAddrSelector = _StnPmPolicySrcAddrSelector_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 24),
    _StnPmPolicySrcAddrSelector_Type()
)
stnPmPolicySrcAddrSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicySrcAddrSelector.setStatus("current")
_StnPmPolicyDestAddrSelector_Type = StnPmSelectorType
_StnPmPolicyDestAddrSelector_Object = MibTableColumn
stnPmPolicyDestAddrSelector = _StnPmPolicyDestAddrSelector_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 25),
    _StnPmPolicyDestAddrSelector_Type()
)
stnPmPolicyDestAddrSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyDestAddrSelector.setStatus("current")
_StnPmPolicyEnabled_Type = TruthValue
_StnPmPolicyEnabled_Object = MibTableColumn
stnPmPolicyEnabled = _StnPmPolicyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 26),
    _StnPmPolicyEnabled_Type()
)
stnPmPolicyEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyEnabled.setStatus("current")
_StnPmPolicyMatches_Type = Integer32
_StnPmPolicyMatches_Object = MibTableColumn
stnPmPolicyMatches = _StnPmPolicyMatches_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 27),
    _StnPmPolicyMatches_Type()
)
stnPmPolicyMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyMatches.setStatus("current")
_StnPmPolicyMisses_Type = Integer32
_StnPmPolicyMisses_Object = MibTableColumn
stnPmPolicyMisses = _StnPmPolicyMisses_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 28),
    _StnPmPolicyMisses_Type()
)
stnPmPolicyMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyMisses.setStatus("current")
_StnPmPolicyMarkedOctets_Type = Counter64
_StnPmPolicyMarkedOctets_Object = MibTableColumn
stnPmPolicyMarkedOctets = _StnPmPolicyMarkedOctets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 29),
    _StnPmPolicyMarkedOctets_Type()
)
stnPmPolicyMarkedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyMarkedOctets.setStatus("current")
_StnPmPolicyMarkedPkts_Type = Counter64
_StnPmPolicyMarkedPkts_Object = MibTableColumn
stnPmPolicyMarkedPkts = _StnPmPolicyMarkedPkts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 30),
    _StnPmPolicyMarkedPkts_Type()
)
stnPmPolicyMarkedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyMarkedPkts.setStatus("current")
_StnPmPolicyIcmpTypes_Type = Unsigned32
_StnPmPolicyIcmpTypes_Object = MibTableColumn
stnPmPolicyIcmpTypes = _StnPmPolicyIcmpTypes_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 31),
    _StnPmPolicyIcmpTypes_Type()
)
stnPmPolicyIcmpTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyIcmpTypes.setStatus("current")
_StnPmPolicyTosByteMatchType_Type = StnPmPolicyMatchType
_StnPmPolicyTosByteMatchType_Object = MibTableColumn
stnPmPolicyTosByteMatchType = _StnPmPolicyTosByteMatchType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 32),
    _StnPmPolicyTosByteMatchType_Type()
)
stnPmPolicyTosByteMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyTosByteMatchType.setStatus("current")
_StnPmPolicyTosByteValue_Type = Integer32
_StnPmPolicyTosByteValue_Object = MibTableColumn
stnPmPolicyTosByteValue = _StnPmPolicyTosByteValue_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 33),
    _StnPmPolicyTosByteValue_Type()
)
stnPmPolicyTosByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyTosByteValue.setStatus("current")
_StnPmPolicyTosByteMask_Type = Integer32
_StnPmPolicyTosByteMask_Object = MibTableColumn
stnPmPolicyTosByteMask = _StnPmPolicyTosByteMask_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 34),
    _StnPmPolicyTosByteMask_Type()
)
stnPmPolicyTosByteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyTosByteMask.setStatus("current")
_StnPmPolicyMarkerID_Type = Integer32
_StnPmPolicyMarkerID_Object = MibTableColumn
stnPmPolicyMarkerID = _StnPmPolicyMarkerID_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 35),
    _StnPmPolicyMarkerID_Type()
)
stnPmPolicyMarkerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyMarkerID.setStatus("current")
_StnPmPolicyTxclassID_Type = Integer32
_StnPmPolicyTxclassID_Object = MibTableColumn
stnPmPolicyTxclassID = _StnPmPolicyTxclassID_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 2, 1, 1, 36),
    _StnPmPolicyTxclassID_Type()
)
stnPmPolicyTxclassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPolicyTxclassID.setStatus("current")
_StnPmPreference_ObjectIdentity = ObjectIdentity
stnPmPreference = _StnPmPreference_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 3)
)
_StnPmPreferenceTable_Object = MibTable
stnPmPreferenceTable = _StnPmPreferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    stnPmPreferenceTable.setStatus("current")
_StnPmPreferenceEntry_Object = MibTableRow
stnPmPreferenceEntry = _StnPmPreferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 3, 1, 1)
)
stnPmPreferenceEntry.setIndexNames(
    (0, "STN-POLICY-MIB", "stnPmPreferenceIndex"),
)
if mibBuilder.loadTexts:
    stnPmPreferenceEntry.setStatus("current")
_StnPmPreferenceIndex_Type = Integer32
_StnPmPreferenceIndex_Object = MibTableColumn
stnPmPreferenceIndex = _StnPmPreferenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 3, 1, 1, 1),
    _StnPmPreferenceIndex_Type()
)
stnPmPreferenceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPreferenceIndex.setStatus("current")
_StnPmPreferenceNum_Type = Integer32
_StnPmPreferenceNum_Object = MibTableColumn
stnPmPreferenceNum = _StnPmPreferenceNum_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 3, 1, 1, 2),
    _StnPmPreferenceNum_Type()
)
stnPmPreferenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPreferenceNum.setStatus("current")
_StnPmPreferenceAhAlg_Type = StnPmAuthAlg
_StnPmPreferenceAhAlg_Object = MibTableColumn
stnPmPreferenceAhAlg = _StnPmPreferenceAhAlg_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 3, 1, 1, 3),
    _StnPmPreferenceAhAlg_Type()
)
stnPmPreferenceAhAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPreferenceAhAlg.setStatus("current")
_StnPmPreferenceEspAuthAlg_Type = StnPmAuthAlg
_StnPmPreferenceEspAuthAlg_Object = MibTableColumn
stnPmPreferenceEspAuthAlg = _StnPmPreferenceEspAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 3, 1, 1, 4),
    _StnPmPreferenceEspAuthAlg_Type()
)
stnPmPreferenceEspAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPreferenceEspAuthAlg.setStatus("current")
_StnPmPreferenceEspEncrAlg_Type = StnPmEncrAlg
_StnPmPreferenceEspEncrAlg_Object = MibTableColumn
stnPmPreferenceEspEncrAlg = _StnPmPreferenceEspEncrAlg_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 3, 1, 1, 5),
    _StnPmPreferenceEspEncrAlg_Type()
)
stnPmPreferenceEspEncrAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPreferenceEspEncrAlg.setStatus("current")
_StnPmPreferenceLifeTime_Type = Integer32
_StnPmPreferenceLifeTime_Object = MibTableColumn
stnPmPreferenceLifeTime = _StnPmPreferenceLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 3, 1, 1, 6),
    _StnPmPreferenceLifeTime_Type()
)
stnPmPreferenceLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPreferenceLifeTime.setStatus("current")
_StnPmPreferenceLifeBytes_Type = Integer32
_StnPmPreferenceLifeBytes_Object = MibTableColumn
stnPmPreferenceLifeBytes = _StnPmPreferenceLifeBytes_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 3, 1, 1, 7),
    _StnPmPreferenceLifeBytes_Type()
)
stnPmPreferenceLifeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPreferenceLifeBytes.setStatus("current")
_StnPmPreferenceIPsecID_Type = Integer32
_StnPmPreferenceIPsecID_Object = MibTableColumn
stnPmPreferenceIPsecID = _StnPmPreferenceIPsecID_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 3, 1, 1, 8),
    _StnPmPreferenceIPsecID_Type()
)
stnPmPreferenceIPsecID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPreferenceIPsecID.setStatus("current")


class _StnPmPreferencePFSGroup_Type(Integer32):
    """Custom type stnPmPreferencePFSGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("group1", 1),
          ("group2", 2),
          ("group5", 5))
    )


_StnPmPreferencePFSGroup_Type.__name__ = "Integer32"
_StnPmPreferencePFSGroup_Object = MibTableColumn
stnPmPreferencePFSGroup = _StnPmPreferencePFSGroup_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 3, 1, 1, 9),
    _StnPmPreferencePFSGroup_Type()
)
stnPmPreferencePFSGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPreferencePFSGroup.setStatus("current")


class _StnPmPreferenceDescription_Type(DisplayString):
    """Custom type stnPmPreferenceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_StnPmPreferenceDescription_Type.__name__ = "DisplayString"
_StnPmPreferenceDescription_Object = MibTableColumn
stnPmPreferenceDescription = _StnPmPreferenceDescription_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 3, 1, 1, 10),
    _StnPmPreferenceDescription_Type()
)
stnPmPreferenceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmPreferenceDescription.setStatus("current")
_StnPmIPsec_ObjectIdentity = ObjectIdentity
stnPmIPsec = _StnPmIPsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 4)
)
_StnPmIPsecTable_Object = MibTable
stnPmIPsecTable = _StnPmIPsecTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 4, 1)
)
if mibBuilder.loadTexts:
    stnPmIPsecTable.setStatus("current")
_StnPmIPsecEntry_Object = MibTableRow
stnPmIPsecEntry = _StnPmIPsecEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 4, 1, 1)
)
stnPmIPsecEntry.setIndexNames(
    (0, "STN-POLICY-MIB", "stnPmIPsecIndex"),
)
if mibBuilder.loadTexts:
    stnPmIPsecEntry.setStatus("current")
_StnPmIPsecIndex_Type = Integer32
_StnPmIPsecIndex_Object = MibTableColumn
stnPmIPsecIndex = _StnPmIPsecIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 4, 1, 1, 1),
    _StnPmIPsecIndex_Type()
)
stnPmIPsecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmIPsecIndex.setStatus("current")
_StnPmIPsecPeerIpAddr_Type = IpAddress
_StnPmIPsecPeerIpAddr_Object = MibTableColumn
stnPmIPsecPeerIpAddr = _StnPmIPsecPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 4, 1, 1, 2),
    _StnPmIPsecPeerIpAddr_Type()
)
stnPmIPsecPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmIPsecPeerIpAddr.setStatus("current")
_StnPmIPsecLocalIpAddr_Type = IpAddress
_StnPmIPsecLocalIpAddr_Object = MibTableColumn
stnPmIPsecLocalIpAddr = _StnPmIPsecLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 4, 1, 1, 3),
    _StnPmIPsecLocalIpAddr_Type()
)
stnPmIPsecLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmIPsecLocalIpAddr.setStatus("current")


class _StnPmIPsecMode_Type(Integer32):
    """Custom type stnPmIPsecMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 2),
          ("tunnel", 1))
    )


_StnPmIPsecMode_Type.__name__ = "Integer32"
_StnPmIPsecMode_Object = MibTableColumn
stnPmIPsecMode = _StnPmIPsecMode_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 4, 1, 1, 4),
    _StnPmIPsecMode_Type()
)
stnPmIPsecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmIPsecMode.setStatus("current")


class _StnPmIPsecKeyNegType_Type(Integer32):
    """Custom type stnPmIPsecKeyNegType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ike", 1),
          ("manual", 2))
    )


_StnPmIPsecKeyNegType_Type.__name__ = "Integer32"
_StnPmIPsecKeyNegType_Object = MibTableColumn
stnPmIPsecKeyNegType = _StnPmIPsecKeyNegType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 4, 1, 1, 5),
    _StnPmIPsecKeyNegType_Type()
)
stnPmIPsecKeyNegType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmIPsecKeyNegType.setStatus("current")


class _StnPmIPsecName_Type(DisplayString):
    """Custom type stnPmIPsecName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_StnPmIPsecName_Type.__name__ = "DisplayString"
_StnPmIPsecName_Object = MibTableColumn
stnPmIPsecName = _StnPmIPsecName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 4, 1, 1, 6),
    _StnPmIPsecName_Type()
)
stnPmIPsecName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmIPsecName.setStatus("current")
_StnPmIPsecNumManualSAs_Type = Integer32
_StnPmIPsecNumManualSAs_Object = MibTableColumn
stnPmIPsecNumManualSAs = _StnPmIPsecNumManualSAs_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 4, 1, 1, 7),
    _StnPmIPsecNumManualSAs_Type()
)
stnPmIPsecNumManualSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmIPsecNumManualSAs.setStatus("current")
_StnPmIPsecNumPreferences_Type = Integer32
_StnPmIPsecNumPreferences_Object = MibTableColumn
stnPmIPsecNumPreferences = _StnPmIPsecNumPreferences_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 4, 1, 1, 8),
    _StnPmIPsecNumPreferences_Type()
)
stnPmIPsecNumPreferences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmIPsecNumPreferences.setStatus("current")
_StnPmIPsecReplayDetectionEnabled_Type = TruthValue
_StnPmIPsecReplayDetectionEnabled_Object = MibTableColumn
stnPmIPsecReplayDetectionEnabled = _StnPmIPsecReplayDetectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 4, 1, 1, 9),
    _StnPmIPsecReplayDetectionEnabled_Type()
)
stnPmIPsecReplayDetectionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmIPsecReplayDetectionEnabled.setStatus("current")
_StnPmEncaps_ObjectIdentity = ObjectIdentity
stnPmEncaps = _StnPmEncaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 5)
)
_StnPmEncapsTable_Object = MibTable
stnPmEncapsTable = _StnPmEncapsTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 5, 1)
)
if mibBuilder.loadTexts:
    stnPmEncapsTable.setStatus("current")
_StnPmEncapsEntry_Object = MibTableRow
stnPmEncapsEntry = _StnPmEncapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 5, 1, 1)
)
stnPmEncapsEntry.setIndexNames(
    (0, "STN-POLICY-MIB", "stnPmEncapsIndex"),
)
if mibBuilder.loadTexts:
    stnPmEncapsEntry.setStatus("current")
_StnPmEncapsIndex_Type = Integer32
_StnPmEncapsIndex_Object = MibTableColumn
stnPmEncapsIndex = _StnPmEncapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 5, 1, 1, 1),
    _StnPmEncapsIndex_Type()
)
stnPmEncapsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmEncapsIndex.setStatus("current")
_StnPmEncapsPeerIpAddr_Type = IpAddress
_StnPmEncapsPeerIpAddr_Object = MibTableColumn
stnPmEncapsPeerIpAddr = _StnPmEncapsPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 5, 1, 1, 2),
    _StnPmEncapsPeerIpAddr_Type()
)
stnPmEncapsPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmEncapsPeerIpAddr.setStatus("current")
_StnPmEncapsLocalIpAddr_Type = IpAddress
_StnPmEncapsLocalIpAddr_Object = MibTableColumn
stnPmEncapsLocalIpAddr = _StnPmEncapsLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 5, 1, 1, 3),
    _StnPmEncapsLocalIpAddr_Type()
)
stnPmEncapsLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmEncapsLocalIpAddr.setStatus("current")


class _StnPmEncapsType_Type(Integer32):
    """Custom type stnPmEncapsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip-gre", 2),
          ("ip-ip", 1))
    )


_StnPmEncapsType_Type.__name__ = "Integer32"
_StnPmEncapsType_Object = MibTableColumn
stnPmEncapsType = _StnPmEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 5, 1, 1, 4),
    _StnPmEncapsType_Type()
)
stnPmEncapsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmEncapsType.setStatus("current")
_StnPmEncapsGREKey_Type = Integer32
_StnPmEncapsGREKey_Object = MibTableColumn
stnPmEncapsGREKey = _StnPmEncapsGREKey_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 5, 1, 1, 5),
    _StnPmEncapsGREKey_Type()
)
stnPmEncapsGREKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmEncapsGREKey.setStatus("current")


class _StnPmEncapsName_Type(DisplayString):
    """Custom type stnPmEncapsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_StnPmEncapsName_Type.__name__ = "DisplayString"
_StnPmEncapsName_Object = MibTableColumn
stnPmEncapsName = _StnPmEncapsName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 5, 1, 1, 6),
    _StnPmEncapsName_Type()
)
stnPmEncapsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmEncapsName.setStatus("current")
_StnPmManualSa_ObjectIdentity = ObjectIdentity
stnPmManualSa = _StnPmManualSa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 6)
)
_StnPmManualSaTable_Object = MibTable
stnPmManualSaTable = _StnPmManualSaTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 6, 1)
)
if mibBuilder.loadTexts:
    stnPmManualSaTable.setStatus("current")
_StnPmManualSaEntry_Object = MibTableRow
stnPmManualSaEntry = _StnPmManualSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 6, 1, 1)
)
stnPmManualSaEntry.setIndexNames(
    (0, "STN-POLICY-MIB", "stnPmManualSaIndex"),
)
if mibBuilder.loadTexts:
    stnPmManualSaEntry.setStatus("current")
_StnPmManualSaIndex_Type = Integer32
_StnPmManualSaIndex_Object = MibTableColumn
stnPmManualSaIndex = _StnPmManualSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 6, 1, 1, 1),
    _StnPmManualSaIndex_Type()
)
stnPmManualSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmManualSaIndex.setStatus("current")
_StnPmManualSaPeerIpAddr_Type = IpAddress
_StnPmManualSaPeerIpAddr_Object = MibTableColumn
stnPmManualSaPeerIpAddr = _StnPmManualSaPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 6, 1, 1, 2),
    _StnPmManualSaPeerIpAddr_Type()
)
stnPmManualSaPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmManualSaPeerIpAddr.setStatus("current")
_StnPmManualSaDirection_Type = StnPmDirection
_StnPmManualSaDirection_Object = MibTableColumn
stnPmManualSaDirection = _StnPmManualSaDirection_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 6, 1, 1, 3),
    _StnPmManualSaDirection_Type()
)
stnPmManualSaDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmManualSaDirection.setStatus("current")
_StnPmManualSaSPI_Type = Integer32
_StnPmManualSaSPI_Object = MibTableColumn
stnPmManualSaSPI = _StnPmManualSaSPI_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 6, 1, 1, 4),
    _StnPmManualSaSPI_Type()
)
stnPmManualSaSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmManualSaSPI.setStatus("current")
_StnPmManualSaAhAlg_Type = StnPmAuthAlg
_StnPmManualSaAhAlg_Object = MibTableColumn
stnPmManualSaAhAlg = _StnPmManualSaAhAlg_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 6, 1, 1, 5),
    _StnPmManualSaAhAlg_Type()
)
stnPmManualSaAhAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmManualSaAhAlg.setStatus("current")


class _StnPmManualSaAhKey_Type(OctetString):
    """Custom type stnPmManualSaAhKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StnPmManualSaAhKey_Type.__name__ = "OctetString"
_StnPmManualSaAhKey_Object = MibTableColumn
stnPmManualSaAhKey = _StnPmManualSaAhKey_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 6, 1, 1, 6),
    _StnPmManualSaAhKey_Type()
)
stnPmManualSaAhKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmManualSaAhKey.setStatus("current")
_StnPmManualSaEspAuthAlg_Type = StnPmAuthAlg
_StnPmManualSaEspAuthAlg_Object = MibTableColumn
stnPmManualSaEspAuthAlg = _StnPmManualSaEspAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 6, 1, 1, 7),
    _StnPmManualSaEspAuthAlg_Type()
)
stnPmManualSaEspAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmManualSaEspAuthAlg.setStatus("current")


class _StnPmManualSaEspAuthKey_Type(OctetString):
    """Custom type stnPmManualSaEspAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StnPmManualSaEspAuthKey_Type.__name__ = "OctetString"
_StnPmManualSaEspAuthKey_Object = MibTableColumn
stnPmManualSaEspAuthKey = _StnPmManualSaEspAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 6, 1, 1, 8),
    _StnPmManualSaEspAuthKey_Type()
)
stnPmManualSaEspAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmManualSaEspAuthKey.setStatus("current")
_StnPmManualSaEspEncrAlg_Type = StnPmEncrAlg
_StnPmManualSaEspEncrAlg_Object = MibTableColumn
stnPmManualSaEspEncrAlg = _StnPmManualSaEspEncrAlg_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 6, 1, 1, 9),
    _StnPmManualSaEspEncrAlg_Type()
)
stnPmManualSaEspEncrAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmManualSaEspEncrAlg.setStatus("current")


class _StnPmManualSaEspEncrKey_Type(OctetString):
    """Custom type stnPmManualSaEspEncrKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StnPmManualSaEspEncrKey_Type.__name__ = "OctetString"
_StnPmManualSaEspEncrKey_Object = MibTableColumn
stnPmManualSaEspEncrKey = _StnPmManualSaEspEncrKey_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 6, 1, 1, 10),
    _StnPmManualSaEspEncrKey_Type()
)
stnPmManualSaEspEncrKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmManualSaEspEncrKey.setStatus("current")
_StnPmManualSaIPsecID_Type = Integer32
_StnPmManualSaIPsecID_Object = MibTableColumn
stnPmManualSaIPsecID = _StnPmManualSaIPsecID_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 6, 1, 1, 11),
    _StnPmManualSaIPsecID_Type()
)
stnPmManualSaIPsecID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmManualSaIPsecID.setStatus("current")


class _StnPmManualSaDescription_Type(DisplayString):
    """Custom type stnPmManualSaDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_StnPmManualSaDescription_Type.__name__ = "DisplayString"
_StnPmManualSaDescription_Object = MibTableColumn
stnPmManualSaDescription = _StnPmManualSaDescription_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 6, 1, 1, 12),
    _StnPmManualSaDescription_Type()
)
stnPmManualSaDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmManualSaDescription.setStatus("current")
_StnPmMarker_ObjectIdentity = ObjectIdentity
stnPmMarker = _StnPmMarker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 7)
)
_StnPmMarkerTable_Object = MibTable
stnPmMarkerTable = _StnPmMarkerTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 7, 1)
)
if mibBuilder.loadTexts:
    stnPmMarkerTable.setStatus("current")
_StnPmMarkerEntry_Object = MibTableRow
stnPmMarkerEntry = _StnPmMarkerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 7, 1, 1)
)
stnPmMarkerEntry.setIndexNames(
    (0, "STN-POLICY-MIB", "stnPmMarkerIndex"),
)
if mibBuilder.loadTexts:
    stnPmMarkerEntry.setStatus("current")
_StnPmMarkerIndex_Type = Integer32
_StnPmMarkerIndex_Object = MibTableColumn
stnPmMarkerIndex = _StnPmMarkerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 7, 1, 1, 1),
    _StnPmMarkerIndex_Type()
)
stnPmMarkerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmMarkerIndex.setStatus("current")


class _StnPmMarkerName_Type(DisplayString):
    """Custom type stnPmMarkerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_StnPmMarkerName_Type.__name__ = "DisplayString"
_StnPmMarkerName_Object = MibTableColumn
stnPmMarkerName = _StnPmMarkerName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 7, 1, 1, 2),
    _StnPmMarkerName_Type()
)
stnPmMarkerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmMarkerName.setStatus("current")
_StnPmMarkerByteValue_Type = Integer32
_StnPmMarkerByteValue_Object = MibTableColumn
stnPmMarkerByteValue = _StnPmMarkerByteValue_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 7, 1, 1, 3),
    _StnPmMarkerByteValue_Type()
)
stnPmMarkerByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmMarkerByteValue.setStatus("current")
_StnPmMarkerByteMask_Type = Integer32
_StnPmMarkerByteMask_Object = MibTableColumn
stnPmMarkerByteMask = _StnPmMarkerByteMask_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 7, 1, 1, 4),
    _StnPmMarkerByteMask_Type()
)
stnPmMarkerByteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmMarkerByteMask.setStatus("current")
_StnPmMarkerMarkedOctets_Type = Counter64
_StnPmMarkerMarkedOctets_Object = MibTableColumn
stnPmMarkerMarkedOctets = _StnPmMarkerMarkedOctets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 7, 1, 1, 5),
    _StnPmMarkerMarkedOctets_Type()
)
stnPmMarkerMarkedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmMarkerMarkedOctets.setStatus("current")
_StnPmMarkerMarkedPkts_Type = Counter64
_StnPmMarkerMarkedPkts_Object = MibTableColumn
stnPmMarkerMarkedPkts = _StnPmMarkerMarkedPkts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 7, 1, 1, 6),
    _StnPmMarkerMarkedPkts_Type()
)
stnPmMarkerMarkedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmMarkerMarkedPkts.setStatus("current")
_StnPmProfile_ObjectIdentity = ObjectIdentity
stnPmProfile = _StnPmProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8)
)
_StnPmProfileTable_Object = MibTable
stnPmProfileTable = _StnPmProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1)
)
if mibBuilder.loadTexts:
    stnPmProfileTable.setStatus("current")
_StnPmProfileEntry_Object = MibTableRow
stnPmProfileEntry = _StnPmProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1)
)
stnPmProfileEntry.setIndexNames(
    (0, "STN-POLICY-MIB", "stnPmProfileIndex"),
)
if mibBuilder.loadTexts:
    stnPmProfileEntry.setStatus("current")
_StnPmProfileIndex_Type = Integer32
_StnPmProfileIndex_Object = MibTableColumn
stnPmProfileIndex = _StnPmProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 1),
    _StnPmProfileIndex_Type()
)
stnPmProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileIndex.setStatus("current")
_StnPmProfileEnabled_Type = TruthValue
_StnPmProfileEnabled_Object = MibTableColumn
stnPmProfileEnabled = _StnPmProfileEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 2),
    _StnPmProfileEnabled_Type()
)
stnPmProfileEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileEnabled.setStatus("current")


class _StnPmProfileName_Type(DisplayString):
    """Custom type stnPmProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_StnPmProfileName_Type.__name__ = "DisplayString"
_StnPmProfileName_Object = MibTableColumn
stnPmProfileName = _StnPmProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 3),
    _StnPmProfileName_Type()
)
stnPmProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileName.setStatus("current")
_StnPmProfileCommittedRate_Type = Integer32
_StnPmProfileCommittedRate_Object = MibTableColumn
stnPmProfileCommittedRate = _StnPmProfileCommittedRate_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 4),
    _StnPmProfileCommittedRate_Type()
)
stnPmProfileCommittedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileCommittedRate.setStatus("current")
_StnPmProfileCommittedBurst_Type = Integer32
_StnPmProfileCommittedBurst_Object = MibTableColumn
stnPmProfileCommittedBurst = _StnPmProfileCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 5),
    _StnPmProfileCommittedBurst_Type()
)
stnPmProfileCommittedBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileCommittedBurst.setStatus("current")
_StnPmProfileExcessRate_Type = Integer32
_StnPmProfileExcessRate_Object = MibTableColumn
stnPmProfileExcessRate = _StnPmProfileExcessRate_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 6),
    _StnPmProfileExcessRate_Type()
)
stnPmProfileExcessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileExcessRate.setStatus("current")
_StnPmProfileExcessBurst_Type = Integer32
_StnPmProfileExcessBurst_Object = MibTableColumn
stnPmProfileExcessBurst = _StnPmProfileExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 7),
    _StnPmProfileExcessBurst_Type()
)
stnPmProfileExcessBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileExcessBurst.setStatus("current")


class _StnPmProfileConformAction_Type(Integer32):
    """Custom type stnPmProfileConformAction based on Integer32"""
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
        *(("deny", 1),
          ("markandforward", 3),
          ("permit", 2),
          ("shape", 4))
    )


_StnPmProfileConformAction_Type.__name__ = "Integer32"
_StnPmProfileConformAction_Object = MibTableColumn
stnPmProfileConformAction = _StnPmProfileConformAction_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 8),
    _StnPmProfileConformAction_Type()
)
stnPmProfileConformAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileConformAction.setStatus("current")
_StnPmProfileConformActionID_Type = Integer32
_StnPmProfileConformActionID_Object = MibTableColumn
stnPmProfileConformActionID = _StnPmProfileConformActionID_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 9),
    _StnPmProfileConformActionID_Type()
)
stnPmProfileConformActionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileConformActionID.setStatus("current")


class _StnPmProfileCautionAction_Type(Integer32):
    """Custom type stnPmProfileCautionAction based on Integer32"""
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
        *(("deny", 1),
          ("markandforward", 3),
          ("permit", 2),
          ("shape", 4))
    )


_StnPmProfileCautionAction_Type.__name__ = "Integer32"
_StnPmProfileCautionAction_Object = MibTableColumn
stnPmProfileCautionAction = _StnPmProfileCautionAction_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 10),
    _StnPmProfileCautionAction_Type()
)
stnPmProfileCautionAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileCautionAction.setStatus("current")
_StnPmProfileConformOctets_Type = Counter64
_StnPmProfileConformOctets_Object = MibTableColumn
stnPmProfileConformOctets = _StnPmProfileConformOctets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 11),
    _StnPmProfileConformOctets_Type()
)
stnPmProfileConformOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileConformOctets.setStatus("current")
_StnPmProfileConformPkts_Type = Counter64
_StnPmProfileConformPkts_Object = MibTableColumn
stnPmProfileConformPkts = _StnPmProfileConformPkts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 12),
    _StnPmProfileConformPkts_Type()
)
stnPmProfileConformPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileConformPkts.setStatus("current")
_StnPmProfileCautionActionID_Type = Integer32
_StnPmProfileCautionActionID_Object = MibTableColumn
stnPmProfileCautionActionID = _StnPmProfileCautionActionID_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 13),
    _StnPmProfileCautionActionID_Type()
)
stnPmProfileCautionActionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileCautionActionID.setStatus("current")


class _StnPmProfileExceedAction_Type(Integer32):
    """Custom type stnPmProfileExceedAction based on Integer32"""
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
        *(("deny", 1),
          ("markandforward", 3),
          ("permit", 2),
          ("shape", 4))
    )


_StnPmProfileExceedAction_Type.__name__ = "Integer32"
_StnPmProfileExceedAction_Object = MibTableColumn
stnPmProfileExceedAction = _StnPmProfileExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 14),
    _StnPmProfileExceedAction_Type()
)
stnPmProfileExceedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileExceedAction.setStatus("current")
_StnPmProfileCautionOctets_Type = Counter64
_StnPmProfileCautionOctets_Object = MibTableColumn
stnPmProfileCautionOctets = _StnPmProfileCautionOctets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 15),
    _StnPmProfileCautionOctets_Type()
)
stnPmProfileCautionOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileCautionOctets.setStatus("current")
_StnPmProfileCautionPkts_Type = Counter64
_StnPmProfileCautionPkts_Object = MibTableColumn
stnPmProfileCautionPkts = _StnPmProfileCautionPkts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 16),
    _StnPmProfileCautionPkts_Type()
)
stnPmProfileCautionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileCautionPkts.setStatus("current")
_StnPmProfileExceedActionID_Type = Integer32
_StnPmProfileExceedActionID_Object = MibTableColumn
stnPmProfileExceedActionID = _StnPmProfileExceedActionID_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 17),
    _StnPmProfileExceedActionID_Type()
)
stnPmProfileExceedActionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileExceedActionID.setStatus("current")
_StnPmProfileExceedOctets_Type = Counter64
_StnPmProfileExceedOctets_Object = MibTableColumn
stnPmProfileExceedOctets = _StnPmProfileExceedOctets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 18),
    _StnPmProfileExceedOctets_Type()
)
stnPmProfileExceedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileExceedOctets.setStatus("current")
_StnPmProfileExceedPkts_Type = Counter64
_StnPmProfileExceedPkts_Object = MibTableColumn
stnPmProfileExceedPkts = _StnPmProfileExceedPkts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 8, 1, 1, 19),
    _StnPmProfileExceedPkts_Type()
)
stnPmProfileExceedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmProfileExceedPkts.setStatus("current")
_StnPmQueue_ObjectIdentity = ObjectIdentity
stnPmQueue = _StnPmQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 9)
)
_StnPmQueueTable_Object = MibTable
stnPmQueueTable = _StnPmQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 9, 1)
)
if mibBuilder.loadTexts:
    stnPmQueueTable.setStatus("current")
_StnPmQueueEntry_Object = MibTableRow
stnPmQueueEntry = _StnPmQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 9, 1, 1)
)
stnPmQueueEntry.setIndexNames(
    (0, "STN-POLICY-MIB", "stnPmQueueIndex"),
)
if mibBuilder.loadTexts:
    stnPmQueueEntry.setStatus("current")
_StnPmQueueIndex_Type = Integer32
_StnPmQueueIndex_Object = MibTableColumn
stnPmQueueIndex = _StnPmQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 9, 1, 1, 1),
    _StnPmQueueIndex_Type()
)
stnPmQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmQueueIndex.setStatus("current")


class _StnPmQueueName_Type(DisplayString):
    """Custom type stnPmQueueName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_StnPmQueueName_Type.__name__ = "DisplayString"
_StnPmQueueName_Object = MibTableColumn
stnPmQueueName = _StnPmQueueName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 9, 1, 1, 2),
    _StnPmQueueName_Type()
)
stnPmQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmQueueName.setStatus("current")
_StnPmQueueThreshold_Type = Integer32
_StnPmQueueThreshold_Object = MibTableColumn
stnPmQueueThreshold = _StnPmQueueThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 9, 1, 1, 3),
    _StnPmQueueThreshold_Type()
)
stnPmQueueThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmQueueThreshold.setStatus("current")


class _StnPmQueueDropType_Type(Integer32):
    """Custom type stnPmQueueDropType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("headDrop", 3),
          ("other", 1),
          ("tailDrop", 2))
    )


_StnPmQueueDropType_Type.__name__ = "Integer32"
_StnPmQueueDropType_Object = MibTableColumn
stnPmQueueDropType = _StnPmQueueDropType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 9, 1, 1, 4),
    _StnPmQueueDropType_Type()
)
stnPmQueueDropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmQueueDropType.setStatus("current")
_StnPmQueueDropHCOctets_Type = Counter64
_StnPmQueueDropHCOctets_Object = MibTableColumn
stnPmQueueDropHCOctets = _StnPmQueueDropHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 9, 1, 1, 5),
    _StnPmQueueDropHCOctets_Type()
)
stnPmQueueDropHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmQueueDropHCOctets.setStatus("current")
_StnPmQueueDropHCPkts_Type = Counter64
_StnPmQueueDropHCPkts_Object = MibTableColumn
stnPmQueueDropHCPkts = _StnPmQueueDropHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 9, 1, 1, 6),
    _StnPmQueueDropHCPkts_Type()
)
stnPmQueueDropHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmQueueDropHCPkts.setStatus("current")
_StnPmQueueQueueLen_Type = Counter32
_StnPmQueueQueueLen_Object = MibTableColumn
stnPmQueueQueueLen = _StnPmQueueQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 9, 1, 1, 7),
    _StnPmQueueQueueLen_Type()
)
stnPmQueueQueueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmQueueQueueLen.setStatus("current")
_StnPmQueueMaxQueueLen_Type = Counter32
_StnPmQueueMaxQueueLen_Object = MibTableColumn
stnPmQueueMaxQueueLen = _StnPmQueueMaxQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 9, 1, 1, 8),
    _StnPmQueueMaxQueueLen_Type()
)
stnPmQueueMaxQueueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmQueueMaxQueueLen.setStatus("current")
_StnPmTraps_ObjectIdentity = ObjectIdentity
stnPmTraps = _StnPmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 10)
)
_StnPmFirewallTrap_ObjectIdentity = ObjectIdentity
stnPmFirewallTrap = _StnPmFirewallTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 10, 1)
)
_StnPmFirewallTrapVars_ObjectIdentity = ObjectIdentity
stnPmFirewallTrapVars = _StnPmFirewallTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 10, 1, 1)
)


class _StnPmFirewallEventLogMsg_Type(DisplayString):
    """Custom type stnPmFirewallEventLogMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StnPmFirewallEventLogMsg_Type.__name__ = "DisplayString"
_StnPmFirewallEventLogMsg_Object = MibScalar
stnPmFirewallEventLogMsg = _StnPmFirewallEventLogMsg_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 10, 1, 1, 1),
    _StnPmFirewallEventLogMsg_Type()
)
stnPmFirewallEventLogMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallEventLogMsg.setStatus("current")
_StnPmFirewallNotificationPrefix_ObjectIdentity = ObjectIdentity
stnPmFirewallNotificationPrefix = _StnPmFirewallNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 10, 1, 2)
)
_StnPmFirewallNotification_ObjectIdentity = ObjectIdentity
stnPmFirewallNotification = _StnPmFirewallNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 10, 1, 2, 0)
)
_StnPmQosTrap_ObjectIdentity = ObjectIdentity
stnPmQosTrap = _StnPmQosTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 10, 2)
)
_StnPmQosTrapVars_ObjectIdentity = ObjectIdentity
stnPmQosTrapVars = _StnPmQosTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 10, 2, 1)
)
_StnPmQosLatestFlowCB_Type = Integer32
_StnPmQosLatestFlowCB_Object = MibScalar
stnPmQosLatestFlowCB = _StnPmQosLatestFlowCB_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 10, 2, 1, 1),
    _StnPmQosLatestFlowCB_Type()
)
stnPmQosLatestFlowCB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmQosLatestFlowCB.setStatus("current")
_StnPmQosLastDroppedPacket_Type = Integer32
_StnPmQosLastDroppedPacket_Object = MibScalar
stnPmQosLastDroppedPacket = _StnPmQosLastDroppedPacket_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 10, 2, 1, 2),
    _StnPmQosLastDroppedPacket_Type()
)
stnPmQosLastDroppedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmQosLastDroppedPacket.setStatus("current")
_StnPmQosNotificationPrefix_ObjectIdentity = ObjectIdentity
stnPmQosNotificationPrefix = _StnPmQosNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 10, 2, 2)
)
_StnPmQosNotification_ObjectIdentity = ObjectIdentity
stnPmQosNotification = _StnPmQosNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 10, 2, 2, 0)
)
_StnPmFirewall_ObjectIdentity = ObjectIdentity
stnPmFirewall = _StnPmFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11)
)
_StnPmFirewallTable_Object = MibTable
stnPmFirewallTable = _StnPmFirewallTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1)
)
if mibBuilder.loadTexts:
    stnPmFirewallTable.setStatus("current")
_StnPmFirewallEntry_Object = MibTableRow
stnPmFirewallEntry = _StnPmFirewallEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1)
)
stnPmFirewallEntry.setIndexNames(
    (0, "STN-POLICY-MIB", "stnPmFirewallIndex"),
)
if mibBuilder.loadTexts:
    stnPmFirewallEntry.setStatus("current")
_StnPmFirewallIndex_Type = Integer32
_StnPmFirewallIndex_Object = MibTableColumn
stnPmFirewallIndex = _StnPmFirewallIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 1),
    _StnPmFirewallIndex_Type()
)
stnPmFirewallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallIndex.setStatus("current")


class _StnPmFirewallName_Type(DisplayString):
    """Custom type stnPmFirewallName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_StnPmFirewallName_Type.__name__ = "DisplayString"
_StnPmFirewallName_Object = MibTableColumn
stnPmFirewallName = _StnPmFirewallName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 2),
    _StnPmFirewallName_Type()
)
stnPmFirewallName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallName.setStatus("current")
_StnPmFirewallAcceptOtherIPOptions_Type = TruthValue
_StnPmFirewallAcceptOtherIPOptions_Object = MibTableColumn
stnPmFirewallAcceptOtherIPOptions = _StnPmFirewallAcceptOtherIPOptions_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 3),
    _StnPmFirewallAcceptOtherIPOptions_Type()
)
stnPmFirewallAcceptOtherIPOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallAcceptOtherIPOptions.setStatus("current")
_StnPmFirewallAcceptSourceRouting_Type = TruthValue
_StnPmFirewallAcceptSourceRouting_Object = MibTableColumn
stnPmFirewallAcceptSourceRouting = _StnPmFirewallAcceptSourceRouting_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 4),
    _StnPmFirewallAcceptSourceRouting_Type()
)
stnPmFirewallAcceptSourceRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallAcceptSourceRouting.setStatus("current")
_StnPmFirewallTcpAckLifeTime_Type = Integer32
_StnPmFirewallTcpAckLifeTime_Object = MibTableColumn
stnPmFirewallTcpAckLifeTime = _StnPmFirewallTcpAckLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 5),
    _StnPmFirewallTcpAckLifeTime_Type()
)
stnPmFirewallTcpAckLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallTcpAckLifeTime.setStatus("current")
_StnPmFirewallTcpSynLifeTime_Type = Integer32
_StnPmFirewallTcpSynLifeTime_Object = MibTableColumn
stnPmFirewallTcpSynLifeTime = _StnPmFirewallTcpSynLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 6),
    _StnPmFirewallTcpSynLifeTime_Type()
)
stnPmFirewallTcpSynLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallTcpSynLifeTime.setStatus("current")
_StnPmFirewallTcpFinLifeTime_Type = Integer32
_StnPmFirewallTcpFinLifeTime_Object = MibTableColumn
stnPmFirewallTcpFinLifeTime = _StnPmFirewallTcpFinLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 7),
    _StnPmFirewallTcpFinLifeTime_Type()
)
stnPmFirewallTcpFinLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallTcpFinLifeTime.setStatus("current")
_StnPmFirewallTcpRstLifeTime_Type = Integer32
_StnPmFirewallTcpRstLifeTime_Object = MibTableColumn
stnPmFirewallTcpRstLifeTime = _StnPmFirewallTcpRstLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 8),
    _StnPmFirewallTcpRstLifeTime_Type()
)
stnPmFirewallTcpRstLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallTcpRstLifeTime.setStatus("current")
_StnPmFirewallTcpInactivityLifeTime_Type = Integer32
_StnPmFirewallTcpInactivityLifeTime_Object = MibTableColumn
stnPmFirewallTcpInactivityLifeTime = _StnPmFirewallTcpInactivityLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 9),
    _StnPmFirewallTcpInactivityLifeTime_Type()
)
stnPmFirewallTcpInactivityLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallTcpInactivityLifeTime.setStatus("current")
_StnPmFirewallUdpInactivityLifeTime_Type = Integer32
_StnPmFirewallUdpInactivityLifeTime_Object = MibTableColumn
stnPmFirewallUdpInactivityLifeTime = _StnPmFirewallUdpInactivityLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 10),
    _StnPmFirewallUdpInactivityLifeTime_Type()
)
stnPmFirewallUdpInactivityLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallUdpInactivityLifeTime.setStatus("current")
_StnPmFirewallSynAttackDetection_Type = TruthValue
_StnPmFirewallSynAttackDetection_Object = MibTableColumn
stnPmFirewallSynAttackDetection = _StnPmFirewallSynAttackDetection_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 11),
    _StnPmFirewallSynAttackDetection_Type()
)
stnPmFirewallSynAttackDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallSynAttackDetection.setStatus("current")
_StnPmFirewallLandAttackDetection_Type = TruthValue
_StnPmFirewallLandAttackDetection_Object = MibTableColumn
stnPmFirewallLandAttackDetection = _StnPmFirewallLandAttackDetection_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 12),
    _StnPmFirewallLandAttackDetection_Type()
)
stnPmFirewallLandAttackDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallLandAttackDetection.setStatus("current")
_StnPmFirewallPingFloodingDetection_Type = TruthValue
_StnPmFirewallPingFloodingDetection_Object = MibTableColumn
stnPmFirewallPingFloodingDetection = _StnPmFirewallPingFloodingDetection_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 13),
    _StnPmFirewallPingFloodingDetection_Type()
)
stnPmFirewallPingFloodingDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallPingFloodingDetection.setStatus("current")
_StnPmFirewallPingOfDeathDetection_Type = TruthValue
_StnPmFirewallPingOfDeathDetection_Object = MibTableColumn
stnPmFirewallPingOfDeathDetection = _StnPmFirewallPingOfDeathDetection_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 14),
    _StnPmFirewallPingOfDeathDetection_Type()
)
stnPmFirewallPingOfDeathDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallPingOfDeathDetection.setStatus("current")
_StnPmFirewallPortScanDetection_Type = TruthValue
_StnPmFirewallPortScanDetection_Object = MibTableColumn
stnPmFirewallPortScanDetection = _StnPmFirewallPortScanDetection_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 15),
    _StnPmFirewallPortScanDetection_Type()
)
stnPmFirewallPortScanDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallPortScanDetection.setStatus("current")
_StnPmFirewallPingScanDetection_Type = TruthValue
_StnPmFirewallPingScanDetection_Object = MibTableColumn
stnPmFirewallPingScanDetection = _StnPmFirewallPingScanDetection_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 16),
    _StnPmFirewallPingScanDetection_Type()
)
stnPmFirewallPingScanDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallPingScanDetection.setStatus("current")
_StnPmFirewallTcpSynBacklogQueueSize_Type = Integer32
_StnPmFirewallTcpSynBacklogQueueSize_Object = MibTableColumn
stnPmFirewallTcpSynBacklogQueueSize = _StnPmFirewallTcpSynBacklogQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 17),
    _StnPmFirewallTcpSynBacklogQueueSize_Type()
)
stnPmFirewallTcpSynBacklogQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallTcpSynBacklogQueueSize.setStatus("current")
_StnPmFirewallPingsPerMinute_Type = Integer32
_StnPmFirewallPingsPerMinute_Object = MibTableColumn
stnPmFirewallPingsPerMinute = _StnPmFirewallPingsPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 18),
    _StnPmFirewallPingsPerMinute_Type()
)
stnPmFirewallPingsPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallPingsPerMinute.setStatus("current")
_StnPmFirewallMaxPingSize_Type = Integer32
_StnPmFirewallMaxPingSize_Object = MibTableColumn
stnPmFirewallMaxPingSize = _StnPmFirewallMaxPingSize_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 19),
    _StnPmFirewallMaxPingSize_Type()
)
stnPmFirewallMaxPingSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallMaxPingSize.setStatus("current")
_StnPmFirewallEnableDynamicPortApps_Type = Unsigned32
_StnPmFirewallEnableDynamicPortApps_Object = MibTableColumn
stnPmFirewallEnableDynamicPortApps = _StnPmFirewallEnableDynamicPortApps_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 20),
    _StnPmFirewallEnableDynamicPortApps_Type()
)
stnPmFirewallEnableDynamicPortApps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallEnableDynamicPortApps.setStatus("current")
_StnPmFirewallMaxDynHashTableSize_Type = Integer32
_StnPmFirewallMaxDynHashTableSize_Object = MibTableColumn
stnPmFirewallMaxDynHashTableSize = _StnPmFirewallMaxDynHashTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 21),
    _StnPmFirewallMaxDynHashTableSize_Type()
)
stnPmFirewallMaxDynHashTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallMaxDynHashTableSize.setStatus("current")
_StnPmFirewallMinLogPeriod_Type = Integer32
_StnPmFirewallMinLogPeriod_Object = MibTableColumn
stnPmFirewallMinLogPeriod = _StnPmFirewallMinLogPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 11, 1, 1, 22),
    _StnPmFirewallMinLogPeriod_Type()
)
stnPmFirewallMinLogPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallMinLogPeriod.setStatus("current")
_StnPmFirewallAction_ObjectIdentity = ObjectIdentity
stnPmFirewallAction = _StnPmFirewallAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 12)
)
_StnPmFirewallActionTable_Object = MibTable
stnPmFirewallActionTable = _StnPmFirewallActionTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 12, 1)
)
if mibBuilder.loadTexts:
    stnPmFirewallActionTable.setStatus("current")
_StnPmFirewallActionEntry_Object = MibTableRow
stnPmFirewallActionEntry = _StnPmFirewallActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 12, 1, 1)
)
stnPmFirewallActionEntry.setIndexNames(
    (0, "STN-POLICY-MIB", "stnPmFirewallActionIndex"),
)
if mibBuilder.loadTexts:
    stnPmFirewallActionEntry.setStatus("current")
_StnPmFirewallActionIndex_Type = Integer32
_StnPmFirewallActionIndex_Object = MibTableColumn
stnPmFirewallActionIndex = _StnPmFirewallActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 12, 1, 1, 1),
    _StnPmFirewallActionIndex_Type()
)
stnPmFirewallActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallActionIndex.setStatus("current")


class _StnPmFirewallActionName_Type(DisplayString):
    """Custom type stnPmFirewallActionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_StnPmFirewallActionName_Type.__name__ = "DisplayString"
_StnPmFirewallActionName_Object = MibTableColumn
stnPmFirewallActionName = _StnPmFirewallActionName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 12, 1, 1, 2),
    _StnPmFirewallActionName_Type()
)
stnPmFirewallActionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallActionName.setStatus("current")


class _StnPmFirewallActionTrackingType_Type(Integer32):
    """Custom type stnPmFirewallActionTrackingType based on Integer32"""
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
        *(("long", 3),
          ("none", 1),
          ("short", 2),
          ("trap", 4))
    )


_StnPmFirewallActionTrackingType_Type.__name__ = "Integer32"
_StnPmFirewallActionTrackingType_Object = MibTableColumn
stnPmFirewallActionTrackingType = _StnPmFirewallActionTrackingType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 12, 1, 1, 3),
    _StnPmFirewallActionTrackingType_Type()
)
stnPmFirewallActionTrackingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallActionTrackingType.setStatus("current")
_StnPmFirewallActionStateful_Type = TruthValue
_StnPmFirewallActionStateful_Object = MibTableColumn
stnPmFirewallActionStateful = _StnPmFirewallActionStateful_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 12, 1, 1, 4),
    _StnPmFirewallActionStateful_Type()
)
stnPmFirewallActionStateful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallActionStateful.setStatus("current")
_StnPmFirewallActionInactivityLifeTime_Type = Integer32
_StnPmFirewallActionInactivityLifeTime_Object = MibTableColumn
stnPmFirewallActionInactivityLifeTime = _StnPmFirewallActionInactivityLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 12, 1, 1, 5),
    _StnPmFirewallActionInactivityLifeTime_Type()
)
stnPmFirewallActionInactivityLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallActionInactivityLifeTime.setStatus("current")


class _StnPmFirewallActionRejectAction_Type(Integer32):
    """Custom type stnPmFirewallActionRejectAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("icmpUnreachPort", 2),
          ("none", 1),
          ("tcpReset", 3))
    )


_StnPmFirewallActionRejectAction_Type.__name__ = "Integer32"
_StnPmFirewallActionRejectAction_Object = MibTableColumn
stnPmFirewallActionRejectAction = _StnPmFirewallActionRejectAction_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 12, 1, 1, 6),
    _StnPmFirewallActionRejectAction_Type()
)
stnPmFirewallActionRejectAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmFirewallActionRejectAction.setStatus("current")
_StnPmServiceList_ObjectIdentity = ObjectIdentity
stnPmServiceList = _StnPmServiceList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 13)
)
_StnPmServiceListTable_Object = MibTable
stnPmServiceListTable = _StnPmServiceListTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 13, 1)
)
if mibBuilder.loadTexts:
    stnPmServiceListTable.setStatus("current")
_StnPmServiceListEntry_Object = MibTableRow
stnPmServiceListEntry = _StnPmServiceListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 13, 1, 1)
)
stnPmServiceListEntry.setIndexNames(
    (0, "STN-POLICY-MIB", "stnPmServiceListIndex"),
)
if mibBuilder.loadTexts:
    stnPmServiceListEntry.setStatus("current")
_StnPmServiceListIndex_Type = Integer32
_StnPmServiceListIndex_Object = MibTableColumn
stnPmServiceListIndex = _StnPmServiceListIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 13, 1, 1, 1),
    _StnPmServiceListIndex_Type()
)
stnPmServiceListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmServiceListIndex.setStatus("current")


class _StnPmServiceListName_Type(DisplayString):
    """Custom type stnPmServiceListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_StnPmServiceListName_Type.__name__ = "DisplayString"
_StnPmServiceListName_Object = MibTableColumn
stnPmServiceListName = _StnPmServiceListName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 13, 1, 1, 2),
    _StnPmServiceListName_Type()
)
stnPmServiceListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmServiceListName.setStatus("current")
_StnPmServiceListConnIdleTimeout_Type = Integer32
_StnPmServiceListConnIdleTimeout_Object = MibTableColumn
stnPmServiceListConnIdleTimeout = _StnPmServiceListConnIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 13, 1, 1, 3),
    _StnPmServiceListConnIdleTimeout_Type()
)
stnPmServiceListConnIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmServiceListConnIdleTimeout.setStatus("current")
_StnPmServiceListNumServices_Type = Integer32
_StnPmServiceListNumServices_Object = MibTableColumn
stnPmServiceListNumServices = _StnPmServiceListNumServices_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 13, 1, 1, 4),
    _StnPmServiceListNumServices_Type()
)
stnPmServiceListNumServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmServiceListNumServices.setStatus("current")
_StnPmServiceListEnabled_Type = TruthValue
_StnPmServiceListEnabled_Object = MibTableColumn
stnPmServiceListEnabled = _StnPmServiceListEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 13, 1, 1, 5),
    _StnPmServiceListEnabled_Type()
)
stnPmServiceListEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmServiceListEnabled.setStatus("current")
_StnPmSLService_ObjectIdentity = ObjectIdentity
stnPmSLService = _StnPmSLService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 14)
)
_StnPmSLServiceTable_Object = MibTable
stnPmSLServiceTable = _StnPmSLServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 14, 1)
)
if mibBuilder.loadTexts:
    stnPmSLServiceTable.setStatus("current")
_StnPmSLServiceEntry_Object = MibTableRow
stnPmSLServiceEntry = _StnPmSLServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 14, 1, 1)
)
stnPmSLServiceEntry.setIndexNames(
    (0, "STN-POLICY-MIB", "stnPmSLIndex"),
    (0, "STN-POLICY-MIB", "stnPmSLServiceIndex"),
)
if mibBuilder.loadTexts:
    stnPmSLServiceEntry.setStatus("current")
_StnPmSLIndex_Type = Integer32
_StnPmSLIndex_Object = MibTableColumn
stnPmSLIndex = _StnPmSLIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 14, 1, 1, 1),
    _StnPmSLIndex_Type()
)
stnPmSLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmSLIndex.setStatus("current")
_StnPmSLServiceIndex_Type = Integer32
_StnPmSLServiceIndex_Object = MibTableColumn
stnPmSLServiceIndex = _StnPmSLServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 14, 1, 1, 2),
    _StnPmSLServiceIndex_Type()
)
stnPmSLServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmSLServiceIndex.setStatus("current")


class _StnPmSLServiceName_Type(DisplayString):
    """Custom type stnPmSLServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_StnPmSLServiceName_Type.__name__ = "DisplayString"
_StnPmSLServiceName_Object = MibTableColumn
stnPmSLServiceName = _StnPmSLServiceName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 14, 1, 1, 3),
    _StnPmSLServiceName_Type()
)
stnPmSLServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmSLServiceName.setStatus("current")
_StnPmSLServiceIdleTimeout_Type = Integer32
_StnPmSLServiceIdleTimeout_Object = MibTableColumn
stnPmSLServiceIdleTimeout = _StnPmSLServiceIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 14, 1, 1, 4),
    _StnPmSLServiceIdleTimeout_Type()
)
stnPmSLServiceIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmSLServiceIdleTimeout.setStatus("current")
_StnPmSLServiceNumPolicies_Type = Integer32
_StnPmSLServiceNumPolicies_Object = MibTableColumn
stnPmSLServiceNumPolicies = _StnPmSLServiceNumPolicies_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 14, 1, 1, 5),
    _StnPmSLServiceNumPolicies_Type()
)
stnPmSLServiceNumPolicies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmSLServiceNumPolicies.setStatus("current")
_StnPmSLServiceEnabled_Type = TruthValue
_StnPmSLServiceEnabled_Object = MibTableColumn
stnPmSLServiceEnabled = _StnPmSLServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 14, 1, 1, 6),
    _StnPmSLServiceEnabled_Type()
)
stnPmSLServiceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmSLServiceEnabled.setStatus("current")


class _StnPmSLServiceType_Type(Integer32):
    """Custom type stnPmSLServiceType based on Integer32"""
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
        *(("firewall", 2),
          ("forwarding", 4),
          ("ip-fileter", 3),
          ("mpls", 6),
          ("qos", 5),
          ("vpn", 1))
    )


_StnPmSLServiceType_Type.__name__ = "Integer32"
_StnPmSLServiceType_Object = MibTableColumn
stnPmSLServiceType = _StnPmSLServiceType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 14, 1, 1, 7),
    _StnPmSLServiceType_Type()
)
stnPmSLServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmSLServiceType.setStatus("current")
_StnPmSLServiceFirewallID_Type = Integer32
_StnPmSLServiceFirewallID_Object = MibTableColumn
stnPmSLServiceFirewallID = _StnPmSLServiceFirewallID_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 14, 1, 1, 8),
    _StnPmSLServiceFirewallID_Type()
)
stnPmSLServiceFirewallID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmSLServiceFirewallID.setStatus("current")
_StnPmClass_ObjectIdentity = ObjectIdentity
stnPmClass = _StnPmClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15)
)
_StnPmClassTable_Object = MibTable
stnPmClassTable = _StnPmClassTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1)
)
if mibBuilder.loadTexts:
    stnPmClassTable.setStatus("current")
_StnPmClassEntry_Object = MibTableRow
stnPmClassEntry = _StnPmClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1)
)
stnPmClassEntry.setIndexNames(
    (0, "STN-POLICY-MIB", "stnPmIfIndex"),
    (0, "STN-POLICY-MIB", "stnPmTxclassInstance"),
)
if mibBuilder.loadTexts:
    stnPmClassEntry.setStatus("current")
_StnPmIfIndex_Type = InterfaceIndex
_StnPmIfIndex_Object = MibTableColumn
stnPmIfIndex = _StnPmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 1),
    _StnPmIfIndex_Type()
)
stnPmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmIfIndex.setStatus("current")
_StnPmTxclassInstance_Type = Integer32
_StnPmTxclassInstance_Object = MibTableColumn
stnPmTxclassInstance = _StnPmTxclassInstance_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 2),
    _StnPmTxclassInstance_Type()
)
stnPmTxclassInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmTxclassInstance.setStatus("current")


class _StnPmClassName_Type(DisplayString):
    """Custom type stnPmClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_StnPmClassName_Type.__name__ = "DisplayString"
_StnPmClassName_Object = MibTableColumn
stnPmClassName = _StnPmClassName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 3),
    _StnPmClassName_Type()
)
stnPmClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassName.setStatus("current")


class _StnPmClassParent_Type(DisplayString):
    """Custom type stnPmClassParent based on DisplayString"""
    defaultValue = OctetString("interface")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_StnPmClassParent_Type.__name__ = "DisplayString"
_StnPmClassParent_Object = MibTableColumn
stnPmClassParent = _StnPmClassParent_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 4),
    _StnPmClassParent_Type()
)
stnPmClassParent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassParent.setStatus("current")


class _StnPmClassRate_Type(StnPmBitRate):
    """Custom type stnPmClassRate based on StnPmBitRate"""
    defaultValue = 0


_StnPmClassRate_Object = MibTableColumn
stnPmClassRate = _StnPmClassRate_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 5),
    _StnPmClassRate_Type()
)
stnPmClassRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassRate.setStatus("current")
if mibBuilder.loadTexts:
    stnPmClassRate.setUnits("bits per second")


class _StnPmClassPriority_Type(Integer32):
    """Custom type stnPmClassPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_StnPmClassPriority_Type.__name__ = "Integer32"
_StnPmClassPriority_Object = MibTableColumn
stnPmClassPriority = _StnPmClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 6),
    _StnPmClassPriority_Type()
)
stnPmClassPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassPriority.setStatus("current")


class _StnPmClassMaxIdle_Type(Integer32):
    """Custom type stnPmClassMaxIdle based on Integer32"""
    defaultValue = 0


_StnPmClassMaxIdle_Object = MibTableColumn
stnPmClassMaxIdle = _StnPmClassMaxIdle_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 7),
    _StnPmClassMaxIdle_Type()
)
stnPmClassMaxIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassMaxIdle.setStatus("current")
if mibBuilder.loadTexts:
    stnPmClassMaxIdle.setUnits("tens of nanoseconds")


class _StnPmClassMinIdle_Type(Integer32):
    """Custom type stnPmClassMinIdle based on Integer32"""
    defaultValue = 0


_StnPmClassMinIdle_Object = MibTableColumn
stnPmClassMinIdle = _StnPmClassMinIdle_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 8),
    _StnPmClassMinIdle_Type()
)
stnPmClassMinIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassMinIdle.setStatus("current")
if mibBuilder.loadTexts:
    stnPmClassMinIdle.setUnits("tens of nanoseconds")


class _StnPmClassMaxQueueLen_Type(Integer32):
    """Custom type stnPmClassMaxQueueLen based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_StnPmClassMaxQueueLen_Type.__name__ = "Integer32"
_StnPmClassMaxQueueLen_Object = MibTableColumn
stnPmClassMaxQueueLen = _StnPmClassMaxQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 9),
    _StnPmClassMaxQueueLen_Type()
)
stnPmClassMaxQueueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassMaxQueueLen.setStatus("current")


class _StnPmClassOperStatus_Type(Integer32):
    """Custom type stnPmClassOperStatus based on Integer32"""
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
        *(("autoClassActive", 4),
          ("down", 2),
          ("downConflict", 3),
          ("up", 1))
    )


_StnPmClassOperStatus_Type.__name__ = "Integer32"
_StnPmClassOperStatus_Object = MibTableColumn
stnPmClassOperStatus = _StnPmClassOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 10),
    _StnPmClassOperStatus_Type()
)
stnPmClassOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassOperStatus.setStatus("current")


class _StnPmClassBwUse_Type(Integer32):
    """Custom type stnPmClassBwUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atLimit", 1),
          ("overLimit", 3),
          ("underLimit", 2))
    )


_StnPmClassBwUse_Type.__name__ = "Integer32"
_StnPmClassBwUse_Object = MibTableColumn
stnPmClassBwUse = _StnPmClassBwUse_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 11),
    _StnPmClassBwUse_Type()
)
stnPmClassBwUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassBwUse.setStatus("current")
_StnPmClassUnsatisfied_Type = TruthValue
_StnPmClassUnsatisfied_Object = MibTableColumn
stnPmClassUnsatisfied = _StnPmClassUnsatisfied_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 12),
    _StnPmClassUnsatisfied_Type()
)
stnPmClassUnsatisfied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassUnsatisfied.setStatus("current")


class _StnPmClassQueueSize_Type(Gauge32):
    """Custom type stnPmClassQueueSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_StnPmClassQueueSize_Type.__name__ = "Gauge32"
_StnPmClassQueueSize_Object = MibTableColumn
stnPmClassQueueSize = _StnPmClassQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 13),
    _StnPmClassQueueSize_Type()
)
stnPmClassQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassQueueSize.setStatus("current")


class _StnPmClassMaxRate_Type(StnPmBitRate):
    """Custom type stnPmClassMaxRate based on StnPmBitRate"""
    defaultValue = 0


_StnPmClassMaxRate_Object = MibTableColumn
stnPmClassMaxRate = _StnPmClassMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 14),
    _StnPmClassMaxRate_Type()
)
stnPmClassMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    stnPmClassMaxRate.setUnits("bits per second")


class _StnPmClassDescription_Type(DisplayString):
    """Custom type stnPmClassDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StnPmClassDescription_Type.__name__ = "DisplayString"
_StnPmClassDescription_Object = MibTableColumn
stnPmClassDescription = _StnPmClassDescription_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 15),
    _StnPmClassDescription_Type()
)
stnPmClassDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassDescription.setStatus("current")
_StnPmClassStatsHighWater_Type = Counter32
_StnPmClassStatsHighWater_Object = MibTableColumn
stnPmClassStatsHighWater = _StnPmClassStatsHighWater_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 16),
    _StnPmClassStatsHighWater_Type()
)
stnPmClassStatsHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassStatsHighWater.setStatus("current")
_StnPmClassStatsIdle_Type = Integer32
_StnPmClassStatsIdle_Object = MibTableColumn
stnPmClassStatsIdle = _StnPmClassStatsIdle_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 17),
    _StnPmClassStatsIdle_Type()
)
stnPmClassStatsIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassStatsIdle.setStatus("current")
if mibBuilder.loadTexts:
    stnPmClassStatsIdle.setUnits("tens of nanoseconds")
_StnPmClassStatsQueuedPkts_Type = Gauge32
_StnPmClassStatsQueuedPkts_Object = MibTableColumn
stnPmClassStatsQueuedPkts = _StnPmClassStatsQueuedPkts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 18),
    _StnPmClassStatsQueuedPkts_Type()
)
stnPmClassStatsQueuedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassStatsQueuedPkts.setStatus("current")
_StnPmClassStatsOctets_Type = Counter32
_StnPmClassStatsOctets_Object = MibTableColumn
stnPmClassStatsOctets = _StnPmClassStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 19),
    _StnPmClassStatsOctets_Type()
)
stnPmClassStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassStatsOctets.setStatus("current")
_StnPmClassStatsPkts_Type = Counter32
_StnPmClassStatsPkts_Object = MibTableColumn
stnPmClassStatsPkts = _StnPmClassStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 20),
    _StnPmClassStatsPkts_Type()
)
stnPmClassStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassStatsPkts.setStatus("current")
_StnPmClassStatsOverLimits_Type = Counter32
_StnPmClassStatsOverLimits_Object = MibTableColumn
stnPmClassStatsOverLimits = _StnPmClassStatsOverLimits_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 21),
    _StnPmClassStatsOverLimits_Type()
)
stnPmClassStatsOverLimits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassStatsOverLimits.setStatus("current")
_StnPmClassStatsBorrowAttempts_Type = Counter32
_StnPmClassStatsBorrowAttempts_Object = MibTableColumn
stnPmClassStatsBorrowAttempts = _StnPmClassStatsBorrowAttempts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 22),
    _StnPmClassStatsBorrowAttempts_Type()
)
stnPmClassStatsBorrowAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassStatsBorrowAttempts.setStatus("current")
_StnPmClassStatsDroppedOctets_Type = Counter32
_StnPmClassStatsDroppedOctets_Object = MibTableColumn
stnPmClassStatsDroppedOctets = _StnPmClassStatsDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 23),
    _StnPmClassStatsDroppedOctets_Type()
)
stnPmClassStatsDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassStatsDroppedOctets.setStatus("current")
_StnPmClassStatsDroppedPkts_Type = Counter32
_StnPmClassStatsDroppedPkts_Object = MibTableColumn
stnPmClassStatsDroppedPkts = _StnPmClassStatsDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 24),
    _StnPmClassStatsDroppedPkts_Type()
)
stnPmClassStatsDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassStatsDroppedPkts.setStatus("current")
_StnPmClassStatsThrottles_Type = Counter32
_StnPmClassStatsThrottles_Object = MibTableColumn
stnPmClassStatsThrottles = _StnPmClassStatsThrottles_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 25),
    _StnPmClassStatsThrottles_Type()
)
stnPmClassStatsThrottles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassStatsThrottles.setStatus("current")
_StnPmClassStatsUnsatisfieds_Type = Counter32
_StnPmClassStatsUnsatisfieds_Object = MibTableColumn
stnPmClassStatsUnsatisfieds = _StnPmClassStatsUnsatisfieds_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 26),
    _StnPmClassStatsUnsatisfieds_Type()
)
stnPmClassStatsUnsatisfieds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassStatsUnsatisfieds.setStatus("current")
_StnPmClassStatsAggrOctets_Type = Counter32
_StnPmClassStatsAggrOctets_Object = MibTableColumn
stnPmClassStatsAggrOctets = _StnPmClassStatsAggrOctets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 27),
    _StnPmClassStatsAggrOctets_Type()
)
stnPmClassStatsAggrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassStatsAggrOctets.setStatus("current")
_StnPmClassStatsAggrPkts_Type = Counter32
_StnPmClassStatsAggrPkts_Object = MibTableColumn
stnPmClassStatsAggrPkts = _StnPmClassStatsAggrPkts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 15, 1, 1, 28),
    _StnPmClassStatsAggrPkts_Type()
)
stnPmClassStatsAggrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPmClassStatsAggrPkts.setStatus("current")
_StnPMProxyTunnel_ObjectIdentity = ObjectIdentity
stnPMProxyTunnel = _StnPMProxyTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16)
)
_StnPmMibConformance_ObjectIdentity = ObjectIdentity
stnPmMibConformance = _StnPmMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 2)
)

# Managed Objects groups


# Notification objects

stnPmFirewallLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 10, 1, 2, 0, 1)
)
stnPmFirewallLog.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("STN-POLICY-MIB", "stnPmServiceIndex"),
        ("STN-POLICY-MIB", "stnPmPolicyIndex"),
        ("STN-POLICY-MIB", "stnPmFirewallEventLogMsg"))
)
if mibBuilder.loadTexts:
    stnPmFirewallLog.setStatus(
        "current"
    )

stnPmQosFlowCBCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 10, 2, 2, 0, 1)
)
stnPmQosFlowCBCreated.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("STN-POLICY-MIB", "stnPmQosLatestFlowCB"))
)
if mibBuilder.loadTexts:
    stnPmQosFlowCBCreated.setStatus(
        "current"
    )

stnPmQosFlowCBRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 10, 2, 2, 0, 2)
)
stnPmQosFlowCBRemoved.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("STN-POLICY-MIB", "stnPmQosLatestFlowCB"))
)
if mibBuilder.loadTexts:
    stnPmQosFlowCBRemoved.setStatus(
        "current"
    )

stnPmQosShapingPacketDiscard = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 10, 2, 2, 0, 3)
)
stnPmQosShapingPacketDiscard.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("STN-POLICY-MIB", "stnPmQosLastDroppedPacket"))
)
if mibBuilder.loadTexts:
    stnPmQosShapingPacketDiscard.setStatus(
        "current"
    )

stnPmQosThresholdPacketDiscard = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 10, 2, 2, 0, 4)
)
stnPmQosThresholdPacketDiscard.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("STN-POLICY-MIB", "stnPmQosLastDroppedPacket"))
)
if mibBuilder.loadTexts:
    stnPmQosThresholdPacketDiscard.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-POLICY-MIB",
    **{"StnPmPolicyMatchType": StnPmPolicyMatchType,
       "StnPmSelectorType": StnPmSelectorType,
       "StnPmAuthAlg": StnPmAuthAlg,
       "StnPmEncrAlg": StnPmEncrAlg,
       "StnPmDirection": StnPmDirection,
       "StnPmBitRate": StnPmBitRate,
       "stnPm": stnPm,
       "stnPmObjects": stnPmObjects,
       "stnPmService": stnPmService,
       "stnPmServiceTable": stnPmServiceTable,
       "stnPmServiceEntry": stnPmServiceEntry,
       "stnPmServiceIndex": stnPmServiceIndex,
       "stnPmServiceName": stnPmServiceName,
       "stnPmServiceIdleTimeout": stnPmServiceIdleTimeout,
       "stnPmServiceNumPolicies": stnPmServiceNumPolicies,
       "stnPmServiceEnabled": stnPmServiceEnabled,
       "stnPmServiceType": stnPmServiceType,
       "stnPmServiceFirewallID": stnPmServiceFirewallID,
       "stnPmPolicy": stnPmPolicy,
       "stnPmPolicyTable": stnPmPolicyTable,
       "stnPmPolicyEntry": stnPmPolicyEntry,
       "stnPmPolicyServiceIndex": stnPmPolicyServiceIndex,
       "stnPmPolicyIndex": stnPmPolicyIndex,
       "stnPmPolicyName": stnPmPolicyName,
       "stnPmPolicySrcAddrMatchType": stnPmPolicySrcAddrMatchType,
       "stnPmPolicySrcAddr": stnPmPolicySrcAddr,
       "stnPmPolicySrcMask": stnPmPolicySrcMask,
       "stnPmPolicySrcEndAddr": stnPmPolicySrcEndAddr,
       "stnPmPolicyDestAddrMatchType": stnPmPolicyDestAddrMatchType,
       "stnPmPolicyDestAddr": stnPmPolicyDestAddr,
       "stnPmPolicyDestMask": stnPmPolicyDestMask,
       "stnPmPolicyDestEndAddr": stnPmPolicyDestEndAddr,
       "stnPmPolicySrcPortMatchType": stnPmPolicySrcPortMatchType,
       "stnPmPolicySrcPort": stnPmPolicySrcPort,
       "stnPmPolicySrcEndPort": stnPmPolicySrcEndPort,
       "stnPmPolicyDestPortMatchType": stnPmPolicyDestPortMatchType,
       "stnPmPolicyDestPort": stnPmPolicyDestPort,
       "stnPmPolicyDestEndPort": stnPmPolicyDestEndPort,
       "stnPmPolicyProtocolMatchType": stnPmPolicyProtocolMatchType,
       "stnPmPolicyProtocol": stnPmPolicyProtocol,
       "stnPmPolicyAction": stnPmPolicyAction,
       "stnPmPolicyActionID": stnPmPolicyActionID,
       "stnPmPolicyDirection": stnPmPolicyDirection,
       "stnPmPolicyCreateMirror": stnPmPolicyCreateMirror,
       "stnPmPolicySrcAddrSelector": stnPmPolicySrcAddrSelector,
       "stnPmPolicyDestAddrSelector": stnPmPolicyDestAddrSelector,
       "stnPmPolicyEnabled": stnPmPolicyEnabled,
       "stnPmPolicyMatches": stnPmPolicyMatches,
       "stnPmPolicyMisses": stnPmPolicyMisses,
       "stnPmPolicyMarkedOctets": stnPmPolicyMarkedOctets,
       "stnPmPolicyMarkedPkts": stnPmPolicyMarkedPkts,
       "stnPmPolicyIcmpTypes": stnPmPolicyIcmpTypes,
       "stnPmPolicyTosByteMatchType": stnPmPolicyTosByteMatchType,
       "stnPmPolicyTosByteValue": stnPmPolicyTosByteValue,
       "stnPmPolicyTosByteMask": stnPmPolicyTosByteMask,
       "stnPmPolicyMarkerID": stnPmPolicyMarkerID,
       "stnPmPolicyTxclassID": stnPmPolicyTxclassID,
       "stnPmPreference": stnPmPreference,
       "stnPmPreferenceTable": stnPmPreferenceTable,
       "stnPmPreferenceEntry": stnPmPreferenceEntry,
       "stnPmPreferenceIndex": stnPmPreferenceIndex,
       "stnPmPreferenceNum": stnPmPreferenceNum,
       "stnPmPreferenceAhAlg": stnPmPreferenceAhAlg,
       "stnPmPreferenceEspAuthAlg": stnPmPreferenceEspAuthAlg,
       "stnPmPreferenceEspEncrAlg": stnPmPreferenceEspEncrAlg,
       "stnPmPreferenceLifeTime": stnPmPreferenceLifeTime,
       "stnPmPreferenceLifeBytes": stnPmPreferenceLifeBytes,
       "stnPmPreferenceIPsecID": stnPmPreferenceIPsecID,
       "stnPmPreferencePFSGroup": stnPmPreferencePFSGroup,
       "stnPmPreferenceDescription": stnPmPreferenceDescription,
       "stnPmIPsec": stnPmIPsec,
       "stnPmIPsecTable": stnPmIPsecTable,
       "stnPmIPsecEntry": stnPmIPsecEntry,
       "stnPmIPsecIndex": stnPmIPsecIndex,
       "stnPmIPsecPeerIpAddr": stnPmIPsecPeerIpAddr,
       "stnPmIPsecLocalIpAddr": stnPmIPsecLocalIpAddr,
       "stnPmIPsecMode": stnPmIPsecMode,
       "stnPmIPsecKeyNegType": stnPmIPsecKeyNegType,
       "stnPmIPsecName": stnPmIPsecName,
       "stnPmIPsecNumManualSAs": stnPmIPsecNumManualSAs,
       "stnPmIPsecNumPreferences": stnPmIPsecNumPreferences,
       "stnPmIPsecReplayDetectionEnabled": stnPmIPsecReplayDetectionEnabled,
       "stnPmEncaps": stnPmEncaps,
       "stnPmEncapsTable": stnPmEncapsTable,
       "stnPmEncapsEntry": stnPmEncapsEntry,
       "stnPmEncapsIndex": stnPmEncapsIndex,
       "stnPmEncapsPeerIpAddr": stnPmEncapsPeerIpAddr,
       "stnPmEncapsLocalIpAddr": stnPmEncapsLocalIpAddr,
       "stnPmEncapsType": stnPmEncapsType,
       "stnPmEncapsGREKey": stnPmEncapsGREKey,
       "stnPmEncapsName": stnPmEncapsName,
       "stnPmManualSa": stnPmManualSa,
       "stnPmManualSaTable": stnPmManualSaTable,
       "stnPmManualSaEntry": stnPmManualSaEntry,
       "stnPmManualSaIndex": stnPmManualSaIndex,
       "stnPmManualSaPeerIpAddr": stnPmManualSaPeerIpAddr,
       "stnPmManualSaDirection": stnPmManualSaDirection,
       "stnPmManualSaSPI": stnPmManualSaSPI,
       "stnPmManualSaAhAlg": stnPmManualSaAhAlg,
       "stnPmManualSaAhKey": stnPmManualSaAhKey,
       "stnPmManualSaEspAuthAlg": stnPmManualSaEspAuthAlg,
       "stnPmManualSaEspAuthKey": stnPmManualSaEspAuthKey,
       "stnPmManualSaEspEncrAlg": stnPmManualSaEspEncrAlg,
       "stnPmManualSaEspEncrKey": stnPmManualSaEspEncrKey,
       "stnPmManualSaIPsecID": stnPmManualSaIPsecID,
       "stnPmManualSaDescription": stnPmManualSaDescription,
       "stnPmMarker": stnPmMarker,
       "stnPmMarkerTable": stnPmMarkerTable,
       "stnPmMarkerEntry": stnPmMarkerEntry,
       "stnPmMarkerIndex": stnPmMarkerIndex,
       "stnPmMarkerName": stnPmMarkerName,
       "stnPmMarkerByteValue": stnPmMarkerByteValue,
       "stnPmMarkerByteMask": stnPmMarkerByteMask,
       "stnPmMarkerMarkedOctets": stnPmMarkerMarkedOctets,
       "stnPmMarkerMarkedPkts": stnPmMarkerMarkedPkts,
       "stnPmProfile": stnPmProfile,
       "stnPmProfileTable": stnPmProfileTable,
       "stnPmProfileEntry": stnPmProfileEntry,
       "stnPmProfileIndex": stnPmProfileIndex,
       "stnPmProfileEnabled": stnPmProfileEnabled,
       "stnPmProfileName": stnPmProfileName,
       "stnPmProfileCommittedRate": stnPmProfileCommittedRate,
       "stnPmProfileCommittedBurst": stnPmProfileCommittedBurst,
       "stnPmProfileExcessRate": stnPmProfileExcessRate,
       "stnPmProfileExcessBurst": stnPmProfileExcessBurst,
       "stnPmProfileConformAction": stnPmProfileConformAction,
       "stnPmProfileConformActionID": stnPmProfileConformActionID,
       "stnPmProfileCautionAction": stnPmProfileCautionAction,
       "stnPmProfileConformOctets": stnPmProfileConformOctets,
       "stnPmProfileConformPkts": stnPmProfileConformPkts,
       "stnPmProfileCautionActionID": stnPmProfileCautionActionID,
       "stnPmProfileExceedAction": stnPmProfileExceedAction,
       "stnPmProfileCautionOctets": stnPmProfileCautionOctets,
       "stnPmProfileCautionPkts": stnPmProfileCautionPkts,
       "stnPmProfileExceedActionID": stnPmProfileExceedActionID,
       "stnPmProfileExceedOctets": stnPmProfileExceedOctets,
       "stnPmProfileExceedPkts": stnPmProfileExceedPkts,
       "stnPmQueue": stnPmQueue,
       "stnPmQueueTable": stnPmQueueTable,
       "stnPmQueueEntry": stnPmQueueEntry,
       "stnPmQueueIndex": stnPmQueueIndex,
       "stnPmQueueName": stnPmQueueName,
       "stnPmQueueThreshold": stnPmQueueThreshold,
       "stnPmQueueDropType": stnPmQueueDropType,
       "stnPmQueueDropHCOctets": stnPmQueueDropHCOctets,
       "stnPmQueueDropHCPkts": stnPmQueueDropHCPkts,
       "stnPmQueueQueueLen": stnPmQueueQueueLen,
       "stnPmQueueMaxQueueLen": stnPmQueueMaxQueueLen,
       "stnPmTraps": stnPmTraps,
       "stnPmFirewallTrap": stnPmFirewallTrap,
       "stnPmFirewallTrapVars": stnPmFirewallTrapVars,
       "stnPmFirewallEventLogMsg": stnPmFirewallEventLogMsg,
       "stnPmFirewallNotificationPrefix": stnPmFirewallNotificationPrefix,
       "stnPmFirewallNotification": stnPmFirewallNotification,
       "stnPmFirewallLog": stnPmFirewallLog,
       "stnPmQosTrap": stnPmQosTrap,
       "stnPmQosTrapVars": stnPmQosTrapVars,
       "stnPmQosLatestFlowCB": stnPmQosLatestFlowCB,
       "stnPmQosLastDroppedPacket": stnPmQosLastDroppedPacket,
       "stnPmQosNotificationPrefix": stnPmQosNotificationPrefix,
       "stnPmQosNotification": stnPmQosNotification,
       "stnPmQosFlowCBCreated": stnPmQosFlowCBCreated,
       "stnPmQosFlowCBRemoved": stnPmQosFlowCBRemoved,
       "stnPmQosShapingPacketDiscard": stnPmQosShapingPacketDiscard,
       "stnPmQosThresholdPacketDiscard": stnPmQosThresholdPacketDiscard,
       "stnPmFirewall": stnPmFirewall,
       "stnPmFirewallTable": stnPmFirewallTable,
       "stnPmFirewallEntry": stnPmFirewallEntry,
       "stnPmFirewallIndex": stnPmFirewallIndex,
       "stnPmFirewallName": stnPmFirewallName,
       "stnPmFirewallAcceptOtherIPOptions": stnPmFirewallAcceptOtherIPOptions,
       "stnPmFirewallAcceptSourceRouting": stnPmFirewallAcceptSourceRouting,
       "stnPmFirewallTcpAckLifeTime": stnPmFirewallTcpAckLifeTime,
       "stnPmFirewallTcpSynLifeTime": stnPmFirewallTcpSynLifeTime,
       "stnPmFirewallTcpFinLifeTime": stnPmFirewallTcpFinLifeTime,
       "stnPmFirewallTcpRstLifeTime": stnPmFirewallTcpRstLifeTime,
       "stnPmFirewallTcpInactivityLifeTime": stnPmFirewallTcpInactivityLifeTime,
       "stnPmFirewallUdpInactivityLifeTime": stnPmFirewallUdpInactivityLifeTime,
       "stnPmFirewallSynAttackDetection": stnPmFirewallSynAttackDetection,
       "stnPmFirewallLandAttackDetection": stnPmFirewallLandAttackDetection,
       "stnPmFirewallPingFloodingDetection": stnPmFirewallPingFloodingDetection,
       "stnPmFirewallPingOfDeathDetection": stnPmFirewallPingOfDeathDetection,
       "stnPmFirewallPortScanDetection": stnPmFirewallPortScanDetection,
       "stnPmFirewallPingScanDetection": stnPmFirewallPingScanDetection,
       "stnPmFirewallTcpSynBacklogQueueSize": stnPmFirewallTcpSynBacklogQueueSize,
       "stnPmFirewallPingsPerMinute": stnPmFirewallPingsPerMinute,
       "stnPmFirewallMaxPingSize": stnPmFirewallMaxPingSize,
       "stnPmFirewallEnableDynamicPortApps": stnPmFirewallEnableDynamicPortApps,
       "stnPmFirewallMaxDynHashTableSize": stnPmFirewallMaxDynHashTableSize,
       "stnPmFirewallMinLogPeriod": stnPmFirewallMinLogPeriod,
       "stnPmFirewallAction": stnPmFirewallAction,
       "stnPmFirewallActionTable": stnPmFirewallActionTable,
       "stnPmFirewallActionEntry": stnPmFirewallActionEntry,
       "stnPmFirewallActionIndex": stnPmFirewallActionIndex,
       "stnPmFirewallActionName": stnPmFirewallActionName,
       "stnPmFirewallActionTrackingType": stnPmFirewallActionTrackingType,
       "stnPmFirewallActionStateful": stnPmFirewallActionStateful,
       "stnPmFirewallActionInactivityLifeTime": stnPmFirewallActionInactivityLifeTime,
       "stnPmFirewallActionRejectAction": stnPmFirewallActionRejectAction,
       "stnPmServiceList": stnPmServiceList,
       "stnPmServiceListTable": stnPmServiceListTable,
       "stnPmServiceListEntry": stnPmServiceListEntry,
       "stnPmServiceListIndex": stnPmServiceListIndex,
       "stnPmServiceListName": stnPmServiceListName,
       "stnPmServiceListConnIdleTimeout": stnPmServiceListConnIdleTimeout,
       "stnPmServiceListNumServices": stnPmServiceListNumServices,
       "stnPmServiceListEnabled": stnPmServiceListEnabled,
       "stnPmSLService": stnPmSLService,
       "stnPmSLServiceTable": stnPmSLServiceTable,
       "stnPmSLServiceEntry": stnPmSLServiceEntry,
       "stnPmSLIndex": stnPmSLIndex,
       "stnPmSLServiceIndex": stnPmSLServiceIndex,
       "stnPmSLServiceName": stnPmSLServiceName,
       "stnPmSLServiceIdleTimeout": stnPmSLServiceIdleTimeout,
       "stnPmSLServiceNumPolicies": stnPmSLServiceNumPolicies,
       "stnPmSLServiceEnabled": stnPmSLServiceEnabled,
       "stnPmSLServiceType": stnPmSLServiceType,
       "stnPmSLServiceFirewallID": stnPmSLServiceFirewallID,
       "stnPmClass": stnPmClass,
       "stnPmClassTable": stnPmClassTable,
       "stnPmClassEntry": stnPmClassEntry,
       "stnPmIfIndex": stnPmIfIndex,
       "stnPmTxclassInstance": stnPmTxclassInstance,
       "stnPmClassName": stnPmClassName,
       "stnPmClassParent": stnPmClassParent,
       "stnPmClassRate": stnPmClassRate,
       "stnPmClassPriority": stnPmClassPriority,
       "stnPmClassMaxIdle": stnPmClassMaxIdle,
       "stnPmClassMinIdle": stnPmClassMinIdle,
       "stnPmClassMaxQueueLen": stnPmClassMaxQueueLen,
       "stnPmClassOperStatus": stnPmClassOperStatus,
       "stnPmClassBwUse": stnPmClassBwUse,
       "stnPmClassUnsatisfied": stnPmClassUnsatisfied,
       "stnPmClassQueueSize": stnPmClassQueueSize,
       "stnPmClassMaxRate": stnPmClassMaxRate,
       "stnPmClassDescription": stnPmClassDescription,
       "stnPmClassStatsHighWater": stnPmClassStatsHighWater,
       "stnPmClassStatsIdle": stnPmClassStatsIdle,
       "stnPmClassStatsQueuedPkts": stnPmClassStatsQueuedPkts,
       "stnPmClassStatsOctets": stnPmClassStatsOctets,
       "stnPmClassStatsPkts": stnPmClassStatsPkts,
       "stnPmClassStatsOverLimits": stnPmClassStatsOverLimits,
       "stnPmClassStatsBorrowAttempts": stnPmClassStatsBorrowAttempts,
       "stnPmClassStatsDroppedOctets": stnPmClassStatsDroppedOctets,
       "stnPmClassStatsDroppedPkts": stnPmClassStatsDroppedPkts,
       "stnPmClassStatsThrottles": stnPmClassStatsThrottles,
       "stnPmClassStatsUnsatisfieds": stnPmClassStatsUnsatisfieds,
       "stnPmClassStatsAggrOctets": stnPmClassStatsAggrOctets,
       "stnPmClassStatsAggrPkts": stnPmClassStatsAggrPkts,
       "stnPMProxyTunnel": stnPMProxyTunnel,
       "stnPmMibConformance": stnPmMibConformance}
)

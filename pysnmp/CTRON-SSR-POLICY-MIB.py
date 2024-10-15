# SNMP MIB module (CTRON-SSR-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SSR-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:43 2024
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

(ssrMibs,) = mibBuilder.importSymbols(
    "CTRON-SSR-SMI-MIB",
    "ssrMibs")

(dot1qVlanStaticEntry,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qVlanStaticEntry")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

policyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 210)
)
policyMIB.setRevisions(
        ("2003-12-19 17:12",
         "2003-07-21 15:01",
         "2000-07-15 00:00",
         "1999-08-11 00:00",
         "1999-07-21 00:00",
         "1998-08-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class InterfaceIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class SSRPortComparator(Integer32, TextualConvention):
    status = "current"
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
        *(("eq", 2),
          ("gt", 5),
          ("lt", 4),
          ("neq", 3),
          ("notused", 1),
          ("range", 6))
    )



class SSRProtocol(Integer32, TextualConvention):
    status = "current"
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
        *(("icmp", 4),
          ("igmp", 5),
          ("ip", 1),
          ("ipx", 6),
          ("ipxrip", 8),
          ("ipxsap", 7),
          ("tcp", 2),
          ("udp", 3))
    )



class SSRsocketId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class SSRVlanIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4100),
    )



class SSRPortList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SSRFlowPolicyType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("denyFlow", 2),
          ("permitFlow", 1))
    )



class SSRFlowPolicyAction(Integer32, TextualConvention):
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
        *(("policyAfterRouteLookup", 2),
          ("policyBeforeRouteLookup", 1),
          ("useOnlyPolicyLookup", 3))
    )



class SSRFlowPolicyAclList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )



class SSRFlowNextHopList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )



class SSRFlowLoadPolicy(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("firstAvailable", 2),
          ("roundRobin", 3))
    )



# MIB Managed Objects in the order of their OIDs

_PolL3Group_ObjectIdentity = ObjectIdentity
polL3Group = _PolL3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12)
)
_PolAclServer_Type = TruthValue
_PolAclServer_Object = MibScalar
polAclServer = _PolAclServer_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 1),
    _PolAclServer_Type()
)
polAclServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclServer.setStatus("current")


class _PolAclNumber_Type(Integer32):
    """Custom type polAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PolAclNumber_Type.__name__ = "Integer32"
_PolAclNumber_Object = MibScalar
polAclNumber = _PolAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 2),
    _PolAclNumber_Type()
)
polAclNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polAclNumber.setStatus("current")
_PolAclLastChanged_Type = TimeTicks
_PolAclLastChanged_Object = MibScalar
polAclLastChanged = _PolAclLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 3),
    _PolAclLastChanged_Type()
)
polAclLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polAclLastChanged.setStatus("current")
_PolAclTable_Object = MibTable
polAclTable = _PolAclTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4)
)
if mibBuilder.loadTexts:
    polAclTable.setStatus("current")
_PolAclEntry_Object = MibTableRow
polAclEntry = _PolAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1)
)
polAclEntry.setIndexNames(
    (0, "CTRON-SSR-POLICY-MIB", "polAclName"),
    (0, "CTRON-SSR-POLICY-MIB", "polAclItem"),
)
if mibBuilder.loadTexts:
    polAclEntry.setStatus("current")
_PolAclName_Type = DisplayString
_PolAclName_Object = MibTableColumn
polAclName = _PolAclName_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1, 1),
    _PolAclName_Type()
)
polAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polAclName.setStatus("current")


class _PolAclItem_Type(Integer32):
    """Custom type polAclItem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_PolAclItem_Type.__name__ = "Integer32"
_PolAclItem_Object = MibTableColumn
polAclItem = _PolAclItem_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1, 2),
    _PolAclItem_Type()
)
polAclItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polAclItem.setStatus("current")


class _PolAclRestriction_Type(Integer32):
    """Custom type polAclRestriction based on Integer32"""
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


_PolAclRestriction_Type.__name__ = "Integer32"
_PolAclRestriction_Object = MibTableColumn
polAclRestriction = _PolAclRestriction_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1, 3),
    _PolAclRestriction_Type()
)
polAclRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclRestriction.setStatus("current")
_PolAclProtocol_Type = SSRProtocol
_PolAclProtocol_Object = MibTableColumn
polAclProtocol = _PolAclProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1, 4),
    _PolAclProtocol_Type()
)
polAclProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclProtocol.setStatus("current")
_PolAclSrcIp_Type = IpAddress
_PolAclSrcIp_Object = MibTableColumn
polAclSrcIp = _PolAclSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1, 5),
    _PolAclSrcIp_Type()
)
polAclSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclSrcIp.setStatus("current")
_PolAclSrcMask_Type = IpAddress
_PolAclSrcMask_Object = MibTableColumn
polAclSrcMask = _PolAclSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1, 6),
    _PolAclSrcMask_Type()
)
polAclSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclSrcMask.setStatus("current")
_PolAclDstIp_Type = IpAddress
_PolAclDstIp_Object = MibTableColumn
polAclDstIp = _PolAclDstIp_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1, 7),
    _PolAclDstIp_Type()
)
polAclDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclDstIp.setStatus("current")
_PolAclDstMask_Type = IpAddress
_PolAclDstMask_Object = MibTableColumn
polAclDstMask = _PolAclDstMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1, 8),
    _PolAclDstMask_Type()
)
polAclDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclDstMask.setStatus("current")


class _PolAclTOS_Type(Integer32):
    """Custom type polAclTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_PolAclTOS_Type.__name__ = "Integer32"
_PolAclTOS_Object = MibTableColumn
polAclTOS = _PolAclTOS_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1, 9),
    _PolAclTOS_Type()
)
polAclTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclTOS.setStatus("current")
_PolAclSrcPort_Type = SSRsocketId
_PolAclSrcPort_Object = MibTableColumn
polAclSrcPort = _PolAclSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1, 10),
    _PolAclSrcPort_Type()
)
polAclSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclSrcPort.setStatus("current")
_PolAclDstPort_Type = SSRsocketId
_PolAclDstPort_Object = MibTableColumn
polAclDstPort = _PolAclDstPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1, 11),
    _PolAclDstPort_Type()
)
polAclDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclDstPort.setStatus("current")


class _PolAclSrcOperator_Type(SSRPortComparator):
    """Custom type polAclSrcOperator based on SSRPortComparator"""


_PolAclSrcOperator_Object = MibTableColumn
polAclSrcOperator = _PolAclSrcOperator_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1, 12),
    _PolAclSrcOperator_Type()
)
polAclSrcOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclSrcOperator.setStatus("current")


class _PolAclDstOperator_Type(SSRPortComparator):
    """Custom type polAclDstOperator based on SSRPortComparator"""


_PolAclDstOperator_Object = MibTableColumn
polAclDstOperator = _PolAclDstOperator_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1, 13),
    _PolAclDstOperator_Type()
)
polAclDstOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclDstOperator.setStatus("current")


class _PolAclSrcHighRange_Type(Integer32):
    """Custom type polAclSrcHighRange based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_PolAclSrcHighRange_Type.__name__ = "Integer32"
_PolAclSrcHighRange_Object = MibTableColumn
polAclSrcHighRange = _PolAclSrcHighRange_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1, 14),
    _PolAclSrcHighRange_Type()
)
polAclSrcHighRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclSrcHighRange.setStatus("current")


class _PolAclDstHighRange_Type(Integer32):
    """Custom type polAclDstHighRange based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_PolAclDstHighRange_Type.__name__ = "Integer32"
_PolAclDstHighRange_Object = MibTableColumn
polAclDstHighRange = _PolAclDstHighRange_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1, 15),
    _PolAclDstHighRange_Type()
)
polAclDstHighRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclDstHighRange.setStatus("current")
_PolAclAuditTrail_Type = TruthValue
_PolAclAuditTrail_Object = MibTableColumn
polAclAuditTrail = _PolAclAuditTrail_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1, 16),
    _PolAclAuditTrail_Type()
)
polAclAuditTrail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclAuditTrail.setStatus("current")


class _PolAclCheckpoint_Type(Integer32):
    """Custom type polAclCheckpoint based on Integer32"""
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
        *(("daily", 2),
          ("endofcall", 5),
          ("hourly", 1),
          ("monthly", 4),
          ("weekly", 3))
    )


_PolAclCheckpoint_Type.__name__ = "Integer32"
_PolAclCheckpoint_Object = MibTableColumn
polAclCheckpoint = _PolAclCheckpoint_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1, 17),
    _PolAclCheckpoint_Type()
)
polAclCheckpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclCheckpoint.setStatus("current")
_PolAclRowStatus_Type = RowStatus
_PolAclRowStatus_Object = MibTableColumn
polAclRowStatus = _PolAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 4, 1, 18),
    _PolAclRowStatus_Type()
)
polAclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclRowStatus.setStatus("current")


class _PolAclServiceNumber_Type(Integer32):
    """Custom type polAclServiceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PolAclServiceNumber_Type.__name__ = "Integer32"
_PolAclServiceNumber_Object = MibScalar
polAclServiceNumber = _PolAclServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 5),
    _PolAclServiceNumber_Type()
)
polAclServiceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polAclServiceNumber.setStatus("current")
_PolAclServiceLastChanged_Type = TimeTicks
_PolAclServiceLastChanged_Object = MibScalar
polAclServiceLastChanged = _PolAclServiceLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 6),
    _PolAclServiceLastChanged_Type()
)
polAclServiceLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polAclServiceLastChanged.setStatus("current")
_PolAclServiceTable_Object = MibTable
polAclServiceTable = _PolAclServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 7)
)
if mibBuilder.loadTexts:
    polAclServiceTable.setStatus("current")
_PolAclServiceEntry_Object = MibTableRow
polAclServiceEntry = _PolAclServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 7, 1)
)
polAclServiceEntry.setIndexNames(
    (0, "CTRON-SSR-POLICY-MIB", "polAclServiceIfIndex"),
    (0, "CTRON-SSR-POLICY-MIB", "polAclName2"),
)
if mibBuilder.loadTexts:
    polAclServiceEntry.setStatus("current")
_PolAclServiceIfIndex_Type = InterfaceIndex
_PolAclServiceIfIndex_Object = MibTableColumn
polAclServiceIfIndex = _PolAclServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 7, 1, 1),
    _PolAclServiceIfIndex_Type()
)
polAclServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polAclServiceIfIndex.setStatus("current")
_PolAclName2_Type = DisplayString
_PolAclName2_Object = MibTableColumn
polAclName2 = _PolAclName2_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 7, 1, 2),
    _PolAclName2_Type()
)
polAclName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polAclName2.setStatus("current")


class _PolAclServiceDirection_Type(Integer32):
    """Custom type polAclServiceDirection based on Integer32"""
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
          ("egress", 2),
          ("ingress", 1))
    )


_PolAclServiceDirection_Type.__name__ = "Integer32"
_PolAclServiceDirection_Object = MibTableColumn
polAclServiceDirection = _PolAclServiceDirection_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 7, 1, 3),
    _PolAclServiceDirection_Type()
)
polAclServiceDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclServiceDirection.setStatus("current")
_PolAclServiceRowStatus_Type = RowStatus
_PolAclServiceRowStatus_Object = MibTableColumn
polAclServiceRowStatus = _PolAclServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 7, 1, 6),
    _PolAclServiceRowStatus_Type()
)
polAclServiceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polAclServiceRowStatus.setStatus("current")
_PolAclRemoteAllowed_Type = TruthValue
_PolAclRemoteAllowed_Object = MibScalar
polAclRemoteAllowed = _PolAclRemoteAllowed_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 9),
    _PolAclRemoteAllowed_Type()
)
polAclRemoteAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polAclRemoteAllowed.setStatus("current")


class _PolAclInterfaceNumber_Type(Integer32):
    """Custom type polAclInterfaceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PolAclInterfaceNumber_Type.__name__ = "Integer32"
_PolAclInterfaceNumber_Object = MibScalar
polAclInterfaceNumber = _PolAclInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 10),
    _PolAclInterfaceNumber_Type()
)
polAclInterfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polAclInterfaceNumber.setStatus("current")
_PolAclInterfaceLastChanged_Type = TimeTicks
_PolAclInterfaceLastChanged_Object = MibScalar
polAclInterfaceLastChanged = _PolAclInterfaceLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 11),
    _PolAclInterfaceLastChanged_Type()
)
polAclInterfaceLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polAclInterfaceLastChanged.setStatus("current")
_PolAclInterfaceTable_Object = MibTable
polAclInterfaceTable = _PolAclInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 12)
)
if mibBuilder.loadTexts:
    polAclInterfaceTable.setStatus("current")
_PolAclInterfaceEntry_Object = MibTableRow
polAclInterfaceEntry = _PolAclInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 12, 1)
)
polAclInterfaceEntry.setIndexNames(
    (0, "CTRON-SSR-POLICY-MIB", "polAclInterfaceIfIndex"),
    (0, "CTRON-SSR-POLICY-MIB", "polAclInterfaceDirection"),
)
if mibBuilder.loadTexts:
    polAclInterfaceEntry.setStatus("current")
_PolAclInterfaceIfIndex_Type = InterfaceIndex
_PolAclInterfaceIfIndex_Object = MibTableColumn
polAclInterfaceIfIndex = _PolAclInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 12, 1, 1),
    _PolAclInterfaceIfIndex_Type()
)
polAclInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polAclInterfaceIfIndex.setStatus("current")


class _PolAclInterfaceDirection_Type(Integer32):
    """Custom type polAclInterfaceDirection based on Integer32"""
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
          ("egress", 2),
          ("ingress", 1))
    )


_PolAclInterfaceDirection_Type.__name__ = "Integer32"
_PolAclInterfaceDirection_Object = MibTableColumn
polAclInterfaceDirection = _PolAclInterfaceDirection_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 12, 1, 2),
    _PolAclInterfaceDirection_Type()
)
polAclInterfaceDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polAclInterfaceDirection.setStatus("current")


class _PolAclPolicyStatus_Type(Integer32):
    """Custom type polAclPolicyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_PolAclPolicyStatus_Type.__name__ = "Integer32"
_PolAclPolicyStatus_Object = MibTableColumn
polAclPolicyStatus = _PolAclPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 12, 12, 1, 3),
    _PolAclPolicyStatus_Type()
)
polAclPolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polAclPolicyStatus.setStatus("current")
_PolL4Group_ObjectIdentity = ObjectIdentity
polL4Group = _PolL4Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15)
)
_PolL4PolicyBasedRoutingEnabled_Type = TruthValue
_PolL4PolicyBasedRoutingEnabled_Object = MibScalar
polL4PolicyBasedRoutingEnabled = _PolL4PolicyBasedRoutingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 1),
    _PolL4PolicyBasedRoutingEnabled_Type()
)
polL4PolicyBasedRoutingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4PolicyBasedRoutingEnabled.setStatus("current")


class _PolL4NumRouters_Type(Integer32):
    """Custom type polL4NumRouters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PolL4NumRouters_Type.__name__ = "Integer32"
_PolL4NumRouters_Object = MibScalar
polL4NumRouters = _PolL4NumRouters_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 5),
    _PolL4NumRouters_Type()
)
polL4NumRouters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4NumRouters.setStatus("current")
_PolL4NextHopTableLastChange_Type = TimeTicks
_PolL4NextHopTableLastChange_Object = MibScalar
polL4NextHopTableLastChange = _PolL4NextHopTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 10),
    _PolL4NextHopTableLastChange_Type()
)
polL4NextHopTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4NextHopTableLastChange.setStatus("current")
_PolL4NextHopTable_Object = MibTable
polL4NextHopTable = _PolL4NextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 20)
)
if mibBuilder.loadTexts:
    polL4NextHopTable.setStatus("current")
_PolL4NextHopEntry_Object = MibTableRow
polL4NextHopEntry = _PolL4NextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 20, 1)
)
polL4NextHopEntry.setIndexNames(
    (0, "CTRON-SSR-POLICY-MIB", "polL4NextHopRouter"),
)
if mibBuilder.loadTexts:
    polL4NextHopEntry.setStatus("current")
_PolL4NextHopRouter_Type = IpAddress
_PolL4NextHopRouter_Object = MibTableColumn
polL4NextHopRouter = _PolL4NextHopRouter_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 20, 1, 1),
    _PolL4NextHopRouter_Type()
)
polL4NextHopRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4NextHopRouter.setStatus("current")


class _PolL4NextHopState_Type(Integer32):
    """Custom type polL4NextHopState based on Integer32"""
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
        *(("macAcquired", 3),
          ("noArpReply", 4),
          ("unknown", 1),
          ("waitingForArp", 2))
    )


_PolL4NextHopState_Type.__name__ = "Integer32"
_PolL4NextHopState_Object = MibTableColumn
polL4NextHopState = _PolL4NextHopState_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 20, 1, 2),
    _PolL4NextHopState_Type()
)
polL4NextHopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4NextHopState.setStatus("current")
_PolL4NextHopPortOfExit_Type = InterfaceIndexOrZero
_PolL4NextHopPortOfExit_Object = MibTableColumn
polL4NextHopPortOfExit = _PolL4NextHopPortOfExit_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 20, 1, 3),
    _PolL4NextHopPortOfExit_Type()
)
polL4NextHopPortOfExit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4NextHopPortOfExit.setStatus("current")
_PolL4NextHopMacAddress_Type = MacAddress
_PolL4NextHopMacAddress_Object = MibTableColumn
polL4NextHopMacAddress = _PolL4NextHopMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 20, 1, 4),
    _PolL4NextHopMacAddress_Type()
)
polL4NextHopMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4NextHopMacAddress.setStatus("current")
_PolL4NextHopLastChange_Type = TimeTicks
_PolL4NextHopLastChange_Object = MibTableColumn
polL4NextHopLastChange = _PolL4NextHopLastChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 20, 1, 5),
    _PolL4NextHopLastChange_Type()
)
polL4NextHopLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4NextHopLastChange.setStatus("current")
_PolL4lowControlTableLastChange_Type = TimeTicks
_PolL4lowControlTableLastChange_Object = MibScalar
polL4lowControlTableLastChange = _PolL4lowControlTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 25),
    _PolL4lowControlTableLastChange_Type()
)
polL4lowControlTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4lowControlTableLastChange.setStatus("current")


class _PolL4NumPolicies_Type(Integer32):
    """Custom type polL4NumPolicies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PolL4NumPolicies_Type.__name__ = "Integer32"
_PolL4NumPolicies_Object = MibScalar
polL4NumPolicies = _PolL4NumPolicies_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 26),
    _PolL4NumPolicies_Type()
)
polL4NumPolicies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4NumPolicies.setStatus("current")
_PolL4lowControlTable_Object = MibTable
polL4lowControlTable = _PolL4lowControlTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 30)
)
if mibBuilder.loadTexts:
    polL4lowControlTable.setStatus("current")
_PolL4lowControlEntry_Object = MibTableRow
polL4lowControlEntry = _PolL4lowControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 30, 1)
)
polL4lowControlEntry.setIndexNames(
    (0, "CTRON-SSR-POLICY-MIB", "polL4PolicyName"),
    (0, "CTRON-SSR-POLICY-MIB", "polL4PolicySequence"),
    (0, "CTRON-SSR-POLICY-MIB", "polL4PolicyInstance"),
)
if mibBuilder.loadTexts:
    polL4lowControlEntry.setStatus("current")
_PolL4PolicyName_Type = DisplayString
_PolL4PolicyName_Object = MibTableColumn
polL4PolicyName = _PolL4PolicyName_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 30, 1, 1),
    _PolL4PolicyName_Type()
)
polL4PolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    polL4PolicyName.setStatus("current")


class _PolL4PolicySequence_Type(Integer32):
    """Custom type polL4PolicySequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PolL4PolicySequence_Type.__name__ = "Integer32"
_PolL4PolicySequence_Object = MibTableColumn
polL4PolicySequence = _PolL4PolicySequence_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 30, 1, 2),
    _PolL4PolicySequence_Type()
)
polL4PolicySequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    polL4PolicySequence.setStatus("current")


class _PolL4PolicyInstance_Type(Integer32):
    """Custom type polL4PolicyInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PolL4PolicyInstance_Type.__name__ = "Integer32"
_PolL4PolicyInstance_Object = MibTableColumn
polL4PolicyInstance = _PolL4PolicyInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 30, 1, 3),
    _PolL4PolicyInstance_Type()
)
polL4PolicyInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    polL4PolicyInstance.setStatus("current")


class _PolL4PolicyType_Type(SSRFlowPolicyType):
    """Custom type polL4PolicyType based on SSRFlowPolicyType"""


_PolL4PolicyType_Object = MibTableColumn
polL4PolicyType = _PolL4PolicyType_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 30, 1, 4),
    _PolL4PolicyType_Type()
)
polL4PolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    polL4PolicyType.setStatus("current")


class _PolL4PolicyAction_Type(SSRFlowPolicyAction):
    """Custom type polL4PolicyAction based on SSRFlowPolicyAction"""


_PolL4PolicyAction_Object = MibTableColumn
polL4PolicyAction = _PolL4PolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 30, 1, 5),
    _PolL4PolicyAction_Type()
)
polL4PolicyAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    polL4PolicyAction.setStatus("current")
_PolL4PolicyMatch_Type = SSRFlowPolicyAclList
_PolL4PolicyMatch_Object = MibTableColumn
polL4PolicyMatch = _PolL4PolicyMatch_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 30, 1, 6),
    _PolL4PolicyMatch_Type()
)
polL4PolicyMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    polL4PolicyMatch.setStatus("current")
_PolL4PolicyNextHops_Type = SSRFlowNextHopList
_PolL4PolicyNextHops_Object = MibTableColumn
polL4PolicyNextHops = _PolL4PolicyNextHops_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 30, 1, 7),
    _PolL4PolicyNextHops_Type()
)
polL4PolicyNextHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    polL4PolicyNextHops.setStatus("current")


class _PolL4PolicyLoading_Type(SSRFlowLoadPolicy):
    """Custom type polL4PolicyLoading based on SSRFlowLoadPolicy"""


_PolL4PolicyLoading_Object = MibTableColumn
polL4PolicyLoading = _PolL4PolicyLoading_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 30, 1, 8),
    _PolL4PolicyLoading_Type()
)
polL4PolicyLoading.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    polL4PolicyLoading.setStatus("current")


class _PolL4PolicyWatch_Type(TruthValue):
    """Custom type polL4PolicyWatch based on TruthValue"""


_PolL4PolicyWatch_Object = MibTableColumn
polL4PolicyWatch = _PolL4PolicyWatch_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 30, 1, 9),
    _PolL4PolicyWatch_Type()
)
polL4PolicyWatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    polL4PolicyWatch.setStatus("current")
_PolL4lowCreationTime_Type = TimeTicks
_PolL4lowCreationTime_Object = MibTableColumn
polL4lowCreationTime = _PolL4lowCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 30, 1, 10),
    _PolL4lowCreationTime_Type()
)
polL4lowCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4lowCreationTime.setStatus("current")
_PolL4lowActiveGates_Type = Gauge32
_PolL4lowActiveGates_Object = MibTableColumn
polL4lowActiveGates = _PolL4lowActiveGates_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 30, 1, 11),
    _PolL4lowActiveGates_Type()
)
polL4lowActiveGates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4lowActiveGates.setStatus("current")
_PolL4lowAppliedTimes_Type = Counter32
_PolL4lowAppliedTimes_Object = MibTableColumn
polL4lowAppliedTimes = _PolL4lowAppliedTimes_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 30, 1, 12),
    _PolL4lowAppliedTimes_Type()
)
polL4lowAppliedTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4lowAppliedTimes.setStatus("current")
_PolL4lowControlStatus_Type = RowStatus
_PolL4lowControlStatus_Object = MibTableColumn
polL4lowControlStatus = _PolL4lowControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 30, 1, 13),
    _PolL4lowControlStatus_Type()
)
polL4lowControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    polL4lowControlStatus.setStatus("current")
_PolL4GroupStats_ObjectIdentity = ObjectIdentity
polL4GroupStats = _PolL4GroupStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 35)
)
_PolL4lowLostRouters_Type = Counter32
_PolL4lowLostRouters_Object = MibScalar
polL4lowLostRouters = _PolL4lowLostRouters_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 35, 1),
    _PolL4lowLostRouters_Type()
)
polL4lowLostRouters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4lowLostRouters.setStatus("current")
_PolL4lowControlTableActivates_Type = Counter32
_PolL4lowControlTableActivates_Object = MibScalar
polL4lowControlTableActivates = _PolL4lowControlTableActivates_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 35, 2),
    _PolL4lowControlTableActivates_Type()
)
polL4lowControlTableActivates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4lowControlTableActivates.setStatus("current")
_PolL4lowControlTableActivateFails_Type = Counter32
_PolL4lowControlTableActivateFails_Object = MibScalar
polL4lowControlTableActivateFails = _PolL4lowControlTableActivateFails_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 35, 3),
    _PolL4lowControlTableActivateFails_Type()
)
polL4lowControlTableActivateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4lowControlTableActivateFails.setStatus("current")
_PolL4lowArpMappingChanges_Type = Counter32
_PolL4lowArpMappingChanges_Object = MibScalar
polL4lowArpMappingChanges = _PolL4lowArpMappingChanges_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 35, 4),
    _PolL4lowArpMappingChanges_Type()
)
polL4lowArpMappingChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4lowArpMappingChanges.setStatus("current")
_PolL4lowIcmpRedirects_Type = Counter32
_PolL4lowIcmpRedirects_Object = MibScalar
polL4lowIcmpRedirects = _PolL4lowIcmpRedirects_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 35, 16),
    _PolL4lowIcmpRedirects_Type()
)
polL4lowIcmpRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4lowIcmpRedirects.setStatus("current")
_PolL4lowMatchAttempts_Type = Counter32
_PolL4lowMatchAttempts_Object = MibScalar
polL4lowMatchAttempts = _PolL4lowMatchAttempts_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 15, 35, 17),
    _PolL4lowMatchAttempts_Type()
)
polL4lowMatchAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL4lowMatchAttempts.setStatus("current")
_PolL2Group_ObjectIdentity = ObjectIdentity
polL2Group = _PolL2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16)
)


class _PolL2FilterNumber_Type(Integer32):
    """Custom type polL2FilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PolL2FilterNumber_Type.__name__ = "Integer32"
_PolL2FilterNumber_Object = MibScalar
polL2FilterNumber = _PolL2FilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 1),
    _PolL2FilterNumber_Type()
)
polL2FilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL2FilterNumber.setStatus("current")
_PolL2FilterLastChanged_Type = TimeTicks
_PolL2FilterLastChanged_Object = MibScalar
polL2FilterLastChanged = _PolL2FilterLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 2),
    _PolL2FilterLastChanged_Type()
)
polL2FilterLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL2FilterLastChanged.setStatus("current")
_PolL2FilterTable_Object = MibTable
polL2FilterTable = _PolL2FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 3)
)
if mibBuilder.loadTexts:
    polL2FilterTable.setStatus("current")
_PolL2FilterEntry_Object = MibTableRow
polL2FilterEntry = _PolL2FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 3, 1)
)
polL2FilterEntry.setIndexNames(
    (0, "CTRON-SSR-POLICY-MIB", "polL2FilterIndex"),
)
if mibBuilder.loadTexts:
    polL2FilterEntry.setStatus("current")


class _PolL2FilterIndex_Type(Integer32):
    """Custom type polL2FilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PolL2FilterIndex_Type.__name__ = "Integer32"
_PolL2FilterIndex_Object = MibTableColumn
polL2FilterIndex = _PolL2FilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 3, 1, 1),
    _PolL2FilterIndex_Type()
)
polL2FilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    polL2FilterIndex.setStatus("current")


class _PolL2FilterDesc_Type(DisplayString):
    """Custom type polL2FilterDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_PolL2FilterDesc_Type.__name__ = "DisplayString"
_PolL2FilterDesc_Object = MibTableColumn
polL2FilterDesc = _PolL2FilterDesc_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 3, 1, 2),
    _PolL2FilterDesc_Type()
)
polL2FilterDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    polL2FilterDesc.setStatus("current")


class _PolL2FilterType_Type(Integer32):
    """Custom type polL2FilterType based on Integer32"""
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
        *(("addressFilter", 2),
          ("portAddressLock", 3),
          ("securePort", 4),
          ("staticEntry", 1))
    )


_PolL2FilterType_Type.__name__ = "Integer32"
_PolL2FilterType_Object = MibTableColumn
polL2FilterType = _PolL2FilterType_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 3, 1, 3),
    _PolL2FilterType_Type()
)
polL2FilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    polL2FilterType.setStatus("current")


class _PolL2FilterRestrictions_Type(Integer32):
    """Custom type polL2FilterRestrictions based on Integer32"""
    defaultValue = 4

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
        *(("allow", 1),
          ("blockEgress", 6),
          ("blockIngress", 5),
          ("disallow", 2),
          ("force", 3),
          ("none", 4))
    )


_PolL2FilterRestrictions_Type.__name__ = "Integer32"
_PolL2FilterRestrictions_Object = MibTableColumn
polL2FilterRestrictions = _PolL2FilterRestrictions_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 3, 1, 4),
    _PolL2FilterRestrictions_Type()
)
polL2FilterRestrictions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    polL2FilterRestrictions.setStatus("current")
_PolL2FilterSrcMacAddr_Type = MacAddress
_PolL2FilterSrcMacAddr_Object = MibTableColumn
polL2FilterSrcMacAddr = _PolL2FilterSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 3, 1, 5),
    _PolL2FilterSrcMacAddr_Type()
)
polL2FilterSrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    polL2FilterSrcMacAddr.setStatus("current")
_PolL2FilterDstMacAddr_Type = MacAddress
_PolL2FilterDstMacAddr_Object = MibTableColumn
polL2FilterDstMacAddr = _PolL2FilterDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 3, 1, 6),
    _PolL2FilterDstMacAddr_Type()
)
polL2FilterDstMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    polL2FilterDstMacAddr.setStatus("current")


class _PolL2FilterVlanId_Type(SSRVlanIndex):
    """Custom type polL2FilterVlanId based on SSRVlanIndex"""
    defaultValue = 1


_PolL2FilterVlanId_Object = MibTableColumn
polL2FilterVlanId = _PolL2FilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 3, 1, 7),
    _PolL2FilterVlanId_Type()
)
polL2FilterVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    polL2FilterVlanId.setStatus("current")
_PolL2FilterInPorts_Type = SSRPortList
_PolL2FilterInPorts_Object = MibTableColumn
polL2FilterInPorts = _PolL2FilterInPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 3, 1, 8),
    _PolL2FilterInPorts_Type()
)
polL2FilterInPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    polL2FilterInPorts.setStatus("current")
_PolL2FilterOutPorts_Type = SSRPortList
_PolL2FilterOutPorts_Object = MibTableColumn
polL2FilterOutPorts = _PolL2FilterOutPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 3, 1, 9),
    _PolL2FilterOutPorts_Type()
)
polL2FilterOutPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    polL2FilterOutPorts.setStatus("current")
_PolL2FilterCreationTime_Type = TimeTicks
_PolL2FilterCreationTime_Object = MibTableColumn
polL2FilterCreationTime = _PolL2FilterCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 3, 1, 10),
    _PolL2FilterCreationTime_Type()
)
polL2FilterCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polL2FilterCreationTime.setStatus("current")
_PolL2FilterStatus_Type = RowStatus
_PolL2FilterStatus_Object = MibTableColumn
polL2FilterStatus = _PolL2FilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 3, 1, 11),
    _PolL2FilterStatus_Type()
)
polL2FilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    polL2FilterStatus.setStatus("current")
_PolL2Dot1qVlanStaticTable_Object = MibTable
polL2Dot1qVlanStaticTable = _PolL2Dot1qVlanStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 4)
)
if mibBuilder.loadTexts:
    polL2Dot1qVlanStaticTable.setStatus("current")
_PolL2Dot1qVlanStaticEntry_Object = MibTableRow
polL2Dot1qVlanStaticEntry = _PolL2Dot1qVlanStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 4, 1)
)
if mibBuilder.loadTexts:
    polL2Dot1qVlanStaticEntry.setStatus("current")


class _PolL2Dot1qVlanStaticProtocols_Type(Bits):
    """Custom type polL2Dot1qVlanStaticProtocols based on Bits"""
    defaultBinValue = "001"

    namedValues = NamedValues(
        *(("appletalk", 4),
          ("bridged-protocols", 1),
          ("dec", 5),
          ("ip", 2),
          ("ipv6", 7),
          ("ipx", 3),
          ("reserved", 0),
          ("sna", 6))
    )

_PolL2Dot1qVlanStaticProtocols_Type.__name__ = "Bits"
_PolL2Dot1qVlanStaticProtocols_Object = MibTableColumn
polL2Dot1qVlanStaticProtocols = _PolL2Dot1qVlanStaticProtocols_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 4, 1, 1),
    _PolL2Dot1qVlanStaticProtocols_Type()
)
polL2Dot1qVlanStaticProtocols.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    polL2Dot1qVlanStaticProtocols.setStatus("current")


class _PolL2Dot1qVlanStaticL4Bridging_Type(TruthValue):
    """Custom type polL2Dot1qVlanStaticL4Bridging based on TruthValue"""


_PolL2Dot1qVlanStaticL4Bridging_Object = MibTableColumn
polL2Dot1qVlanStaticL4Bridging = _PolL2Dot1qVlanStaticL4Bridging_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 16, 4, 1, 2),
    _PolL2Dot1qVlanStaticL4Bridging_Type()
)
polL2Dot1qVlanStaticL4Bridging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    polL2Dot1qVlanStaticL4Bridging.setStatus("current")
_PolConformance_ObjectIdentity = ObjectIdentity
polConformance = _PolConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 210, 2)
)
_PolCompliances_ObjectIdentity = ObjectIdentity
polCompliances = _PolCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 210, 2, 1)
)
_PolGroups_ObjectIdentity = ObjectIdentity
polGroups = _PolGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 210, 2, 2)
)
dot1qVlanStaticEntry.registerAugmentions(
    ("CTRON-SSR-POLICY-MIB",
     "polL2Dot1qVlanStaticEntry")
)
polL2Dot1qVlanStaticEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())

# Managed Objects groups

polGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 210, 2, 2, 1)
)
polGroupV10.setObjects(
      *(("CTRON-SSR-POLICY-MIB", "polAclServer"),
        ("CTRON-SSR-POLICY-MIB", "polAclNumber"),
        ("CTRON-SSR-POLICY-MIB", "polAclLastChanged"),
        ("CTRON-SSR-POLICY-MIB", "polAclName"),
        ("CTRON-SSR-POLICY-MIB", "polAclItem"),
        ("CTRON-SSR-POLICY-MIB", "polAclRestriction"),
        ("CTRON-SSR-POLICY-MIB", "polAclProtocol"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcIp"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcMask"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstIp"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstMask"),
        ("CTRON-SSR-POLICY-MIB", "polAclTOS"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcPort"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstPort"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcOperator"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstOperator"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcHighRange"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstHighRange"),
        ("CTRON-SSR-POLICY-MIB", "polAclAuditTrail"),
        ("CTRON-SSR-POLICY-MIB", "polAclCheckpoint"),
        ("CTRON-SSR-POLICY-MIB", "polAclRowStatus"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceNumber"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceLastChanged"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceIfIndex"),
        ("CTRON-SSR-POLICY-MIB", "polAclName2"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceDirection"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceRowStatus"),
        ("CTRON-SSR-POLICY-MIB", "polAclRemoteAllowed"),
        ("CTRON-SSR-POLICY-MIB", "polAclInterfaceNumber"),
        ("CTRON-SSR-POLICY-MIB", "polAclInterfaceLastChanged"),
        ("CTRON-SSR-POLICY-MIB", "polAclInterfaceIfIndex"),
        ("CTRON-SSR-POLICY-MIB", "polAclInterfaceDirection"),
        ("CTRON-SSR-POLICY-MIB", "polAclPolicyStatus"))
)
if mibBuilder.loadTexts:
    polGroupV10.setStatus("deprecated")

polGroupV11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 210, 2, 2, 2)
)
polGroupV11.setObjects(
      *(("CTRON-SSR-POLICY-MIB", "polAclServer"),
        ("CTRON-SSR-POLICY-MIB", "polAclNumber"),
        ("CTRON-SSR-POLICY-MIB", "polAclLastChanged"),
        ("CTRON-SSR-POLICY-MIB", "polAclName"),
        ("CTRON-SSR-POLICY-MIB", "polAclItem"),
        ("CTRON-SSR-POLICY-MIB", "polAclRestriction"),
        ("CTRON-SSR-POLICY-MIB", "polAclProtocol"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcIp"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcMask"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstIp"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstMask"),
        ("CTRON-SSR-POLICY-MIB", "polAclTOS"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcPort"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstPort"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcOperator"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstOperator"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcHighRange"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstHighRange"),
        ("CTRON-SSR-POLICY-MIB", "polAclAuditTrail"),
        ("CTRON-SSR-POLICY-MIB", "polAclCheckpoint"),
        ("CTRON-SSR-POLICY-MIB", "polAclRowStatus"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceNumber"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceLastChanged"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceIfIndex"),
        ("CTRON-SSR-POLICY-MIB", "polAclName2"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceDirection"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceRowStatus"),
        ("CTRON-SSR-POLICY-MIB", "polAclRemoteAllowed"),
        ("CTRON-SSR-POLICY-MIB", "polAclInterfaceNumber"),
        ("CTRON-SSR-POLICY-MIB", "polAclInterfaceLastChanged"),
        ("CTRON-SSR-POLICY-MIB", "polAclInterfaceIfIndex"),
        ("CTRON-SSR-POLICY-MIB", "polAclInterfaceDirection"),
        ("CTRON-SSR-POLICY-MIB", "polAclPolicyStatus"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterLastChanged"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterNumber"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterDesc"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterType"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterRestrictions"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterSrcMacAddr"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterDstMacAddr"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterVlanId"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterInPorts"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterOutPorts"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterCreationTime"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterStatus"))
)
if mibBuilder.loadTexts:
    polGroupV11.setStatus("deprecated")

polGroupV12 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 210, 2, 2, 3)
)
polGroupV12.setObjects(
      *(("CTRON-SSR-POLICY-MIB", "polAclServer"),
        ("CTRON-SSR-POLICY-MIB", "polAclNumber"),
        ("CTRON-SSR-POLICY-MIB", "polAclLastChanged"),
        ("CTRON-SSR-POLICY-MIB", "polAclName"),
        ("CTRON-SSR-POLICY-MIB", "polAclItem"),
        ("CTRON-SSR-POLICY-MIB", "polAclRestriction"),
        ("CTRON-SSR-POLICY-MIB", "polAclProtocol"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcIp"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcMask"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstIp"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstMask"),
        ("CTRON-SSR-POLICY-MIB", "polAclTOS"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcPort"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstPort"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcOperator"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstOperator"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcHighRange"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstHighRange"),
        ("CTRON-SSR-POLICY-MIB", "polAclAuditTrail"),
        ("CTRON-SSR-POLICY-MIB", "polAclCheckpoint"),
        ("CTRON-SSR-POLICY-MIB", "polAclRowStatus"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceNumber"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceLastChanged"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceIfIndex"),
        ("CTRON-SSR-POLICY-MIB", "polAclName2"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceDirection"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceRowStatus"),
        ("CTRON-SSR-POLICY-MIB", "polAclRemoteAllowed"),
        ("CTRON-SSR-POLICY-MIB", "polAclInterfaceNumber"),
        ("CTRON-SSR-POLICY-MIB", "polAclInterfaceLastChanged"),
        ("CTRON-SSR-POLICY-MIB", "polAclInterfaceIfIndex"),
        ("CTRON-SSR-POLICY-MIB", "polAclInterfaceDirection"),
        ("CTRON-SSR-POLICY-MIB", "polAclPolicyStatus"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterLastChanged"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterNumber"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterDesc"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterType"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterRestrictions"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterSrcMacAddr"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterDstMacAddr"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterVlanId"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterInPorts"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterOutPorts"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterCreationTime"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterStatus"),
        ("CTRON-SSR-POLICY-MIB", "polL4PolicyBasedRoutingEnabled"),
        ("CTRON-SSR-POLICY-MIB", "polL4NumRouters"),
        ("CTRON-SSR-POLICY-MIB", "polL4NextHopTableLastChange"),
        ("CTRON-SSR-POLICY-MIB", "polL4NextHopRouter"),
        ("CTRON-SSR-POLICY-MIB", "polL4NextHopState"),
        ("CTRON-SSR-POLICY-MIB", "polL4NextHopPortOfExit"),
        ("CTRON-SSR-POLICY-MIB", "polL4NextHopMacAddress"),
        ("CTRON-SSR-POLICY-MIB", "polL4NextHopLastChange"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowControlTableLastChange"),
        ("CTRON-SSR-POLICY-MIB", "polL4NumPolicies"),
        ("CTRON-SSR-POLICY-MIB", "polL4PolicyType"),
        ("CTRON-SSR-POLICY-MIB", "polL4PolicyAction"),
        ("CTRON-SSR-POLICY-MIB", "polL4PolicyMatch"),
        ("CTRON-SSR-POLICY-MIB", "polL4PolicyNextHops"),
        ("CTRON-SSR-POLICY-MIB", "polL4PolicyLoading"),
        ("CTRON-SSR-POLICY-MIB", "polL4PolicyWatch"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowCreationTime"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowActiveGates"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowAppliedTimes"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowControlStatus"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowLostRouters"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowControlTableActivates"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowControlTableActivateFails"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowArpMappingChanges"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowIcmpRedirects"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowMatchAttempts"))
)
if mibBuilder.loadTexts:
    polGroupV12.setStatus("current")

polGroupV13 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 210, 2, 2, 4)
)
polGroupV13.setObjects(
      *(("CTRON-SSR-POLICY-MIB", "polAclServer"),
        ("CTRON-SSR-POLICY-MIB", "polAclNumber"),
        ("CTRON-SSR-POLICY-MIB", "polAclLastChanged"),
        ("CTRON-SSR-POLICY-MIB", "polAclName"),
        ("CTRON-SSR-POLICY-MIB", "polAclItem"),
        ("CTRON-SSR-POLICY-MIB", "polAclRestriction"),
        ("CTRON-SSR-POLICY-MIB", "polAclProtocol"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcIp"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcMask"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstIp"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstMask"),
        ("CTRON-SSR-POLICY-MIB", "polAclTOS"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcPort"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstPort"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcOperator"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstOperator"),
        ("CTRON-SSR-POLICY-MIB", "polAclSrcHighRange"),
        ("CTRON-SSR-POLICY-MIB", "polAclDstHighRange"),
        ("CTRON-SSR-POLICY-MIB", "polAclAuditTrail"),
        ("CTRON-SSR-POLICY-MIB", "polAclCheckpoint"),
        ("CTRON-SSR-POLICY-MIB", "polAclRowStatus"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceNumber"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceLastChanged"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceIfIndex"),
        ("CTRON-SSR-POLICY-MIB", "polAclName2"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceDirection"),
        ("CTRON-SSR-POLICY-MIB", "polAclServiceRowStatus"),
        ("CTRON-SSR-POLICY-MIB", "polAclRemoteAllowed"),
        ("CTRON-SSR-POLICY-MIB", "polAclInterfaceNumber"),
        ("CTRON-SSR-POLICY-MIB", "polAclInterfaceLastChanged"),
        ("CTRON-SSR-POLICY-MIB", "polAclInterfaceIfIndex"),
        ("CTRON-SSR-POLICY-MIB", "polAclInterfaceDirection"),
        ("CTRON-SSR-POLICY-MIB", "polAclPolicyStatus"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterLastChanged"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterNumber"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterDesc"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterType"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterRestrictions"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterSrcMacAddr"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterDstMacAddr"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterVlanId"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterInPorts"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterOutPorts"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterCreationTime"),
        ("CTRON-SSR-POLICY-MIB", "polL2FilterStatus"),
        ("CTRON-SSR-POLICY-MIB", "polL2Dot1qVlanStaticProtocols"),
        ("CTRON-SSR-POLICY-MIB", "polL2Dot1qVlanStaticL4Bridging"),
        ("CTRON-SSR-POLICY-MIB", "polL4PolicyBasedRoutingEnabled"),
        ("CTRON-SSR-POLICY-MIB", "polL4NumRouters"),
        ("CTRON-SSR-POLICY-MIB", "polL4NextHopTableLastChange"),
        ("CTRON-SSR-POLICY-MIB", "polL4NextHopRouter"),
        ("CTRON-SSR-POLICY-MIB", "polL4NextHopState"),
        ("CTRON-SSR-POLICY-MIB", "polL4NextHopPortOfExit"),
        ("CTRON-SSR-POLICY-MIB", "polL4NextHopMacAddress"),
        ("CTRON-SSR-POLICY-MIB", "polL4NextHopLastChange"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowControlTableLastChange"),
        ("CTRON-SSR-POLICY-MIB", "polL4NumPolicies"),
        ("CTRON-SSR-POLICY-MIB", "polL4PolicyType"),
        ("CTRON-SSR-POLICY-MIB", "polL4PolicyAction"),
        ("CTRON-SSR-POLICY-MIB", "polL4PolicyMatch"),
        ("CTRON-SSR-POLICY-MIB", "polL4PolicyNextHops"),
        ("CTRON-SSR-POLICY-MIB", "polL4PolicyLoading"),
        ("CTRON-SSR-POLICY-MIB", "polL4PolicyWatch"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowCreationTime"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowActiveGates"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowAppliedTimes"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowControlStatus"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowLostRouters"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowControlTableActivates"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowControlTableActivateFails"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowArpMappingChanges"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowIcmpRedirects"),
        ("CTRON-SSR-POLICY-MIB", "polL4lowMatchAttempts"))
)
if mibBuilder.loadTexts:
    polGroupV13.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

polComplianceV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 210, 2, 1, 1)
)
if mibBuilder.loadTexts:
    polComplianceV10.setStatus(
        "deprecated"
    )

polComplianceV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 210, 2, 1, 2)
)
if mibBuilder.loadTexts:
    polComplianceV11.setStatus(
        "deprecated"
    )

polComplianceV12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 210, 2, 1, 3)
)
if mibBuilder.loadTexts:
    polComplianceV12.setStatus(
        "current"
    )

polComplianceV13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 210, 2, 1, 4)
)
if mibBuilder.loadTexts:
    polComplianceV13.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SSR-POLICY-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "InterfaceIndexOrZero": InterfaceIndexOrZero,
       "SSRPortComparator": SSRPortComparator,
       "SSRProtocol": SSRProtocol,
       "SSRsocketId": SSRsocketId,
       "SSRVlanIndex": SSRVlanIndex,
       "SSRPortList": SSRPortList,
       "SSRFlowPolicyType": SSRFlowPolicyType,
       "SSRFlowPolicyAction": SSRFlowPolicyAction,
       "SSRFlowPolicyAclList": SSRFlowPolicyAclList,
       "SSRFlowNextHopList": SSRFlowNextHopList,
       "SSRFlowLoadPolicy": SSRFlowLoadPolicy,
       "polL3Group": polL3Group,
       "polAclServer": polAclServer,
       "polAclNumber": polAclNumber,
       "polAclLastChanged": polAclLastChanged,
       "polAclTable": polAclTable,
       "polAclEntry": polAclEntry,
       "polAclName": polAclName,
       "polAclItem": polAclItem,
       "polAclRestriction": polAclRestriction,
       "polAclProtocol": polAclProtocol,
       "polAclSrcIp": polAclSrcIp,
       "polAclSrcMask": polAclSrcMask,
       "polAclDstIp": polAclDstIp,
       "polAclDstMask": polAclDstMask,
       "polAclTOS": polAclTOS,
       "polAclSrcPort": polAclSrcPort,
       "polAclDstPort": polAclDstPort,
       "polAclSrcOperator": polAclSrcOperator,
       "polAclDstOperator": polAclDstOperator,
       "polAclSrcHighRange": polAclSrcHighRange,
       "polAclDstHighRange": polAclDstHighRange,
       "polAclAuditTrail": polAclAuditTrail,
       "polAclCheckpoint": polAclCheckpoint,
       "polAclRowStatus": polAclRowStatus,
       "polAclServiceNumber": polAclServiceNumber,
       "polAclServiceLastChanged": polAclServiceLastChanged,
       "polAclServiceTable": polAclServiceTable,
       "polAclServiceEntry": polAclServiceEntry,
       "polAclServiceIfIndex": polAclServiceIfIndex,
       "polAclName2": polAclName2,
       "polAclServiceDirection": polAclServiceDirection,
       "polAclServiceRowStatus": polAclServiceRowStatus,
       "polAclRemoteAllowed": polAclRemoteAllowed,
       "polAclInterfaceNumber": polAclInterfaceNumber,
       "polAclInterfaceLastChanged": polAclInterfaceLastChanged,
       "polAclInterfaceTable": polAclInterfaceTable,
       "polAclInterfaceEntry": polAclInterfaceEntry,
       "polAclInterfaceIfIndex": polAclInterfaceIfIndex,
       "polAclInterfaceDirection": polAclInterfaceDirection,
       "polAclPolicyStatus": polAclPolicyStatus,
       "polL4Group": polL4Group,
       "polL4PolicyBasedRoutingEnabled": polL4PolicyBasedRoutingEnabled,
       "polL4NumRouters": polL4NumRouters,
       "polL4NextHopTableLastChange": polL4NextHopTableLastChange,
       "polL4NextHopTable": polL4NextHopTable,
       "polL4NextHopEntry": polL4NextHopEntry,
       "polL4NextHopRouter": polL4NextHopRouter,
       "polL4NextHopState": polL4NextHopState,
       "polL4NextHopPortOfExit": polL4NextHopPortOfExit,
       "polL4NextHopMacAddress": polL4NextHopMacAddress,
       "polL4NextHopLastChange": polL4NextHopLastChange,
       "polL4lowControlTableLastChange": polL4lowControlTableLastChange,
       "polL4NumPolicies": polL4NumPolicies,
       "polL4lowControlTable": polL4lowControlTable,
       "polL4lowControlEntry": polL4lowControlEntry,
       "polL4PolicyName": polL4PolicyName,
       "polL4PolicySequence": polL4PolicySequence,
       "polL4PolicyInstance": polL4PolicyInstance,
       "polL4PolicyType": polL4PolicyType,
       "polL4PolicyAction": polL4PolicyAction,
       "polL4PolicyMatch": polL4PolicyMatch,
       "polL4PolicyNextHops": polL4PolicyNextHops,
       "polL4PolicyLoading": polL4PolicyLoading,
       "polL4PolicyWatch": polL4PolicyWatch,
       "polL4lowCreationTime": polL4lowCreationTime,
       "polL4lowActiveGates": polL4lowActiveGates,
       "polL4lowAppliedTimes": polL4lowAppliedTimes,
       "polL4lowControlStatus": polL4lowControlStatus,
       "polL4GroupStats": polL4GroupStats,
       "polL4lowLostRouters": polL4lowLostRouters,
       "polL4lowControlTableActivates": polL4lowControlTableActivates,
       "polL4lowControlTableActivateFails": polL4lowControlTableActivateFails,
       "polL4lowArpMappingChanges": polL4lowArpMappingChanges,
       "polL4lowIcmpRedirects": polL4lowIcmpRedirects,
       "polL4lowMatchAttempts": polL4lowMatchAttempts,
       "polL2Group": polL2Group,
       "polL2FilterNumber": polL2FilterNumber,
       "polL2FilterLastChanged": polL2FilterLastChanged,
       "polL2FilterTable": polL2FilterTable,
       "polL2FilterEntry": polL2FilterEntry,
       "polL2FilterIndex": polL2FilterIndex,
       "polL2FilterDesc": polL2FilterDesc,
       "polL2FilterType": polL2FilterType,
       "polL2FilterRestrictions": polL2FilterRestrictions,
       "polL2FilterSrcMacAddr": polL2FilterSrcMacAddr,
       "polL2FilterDstMacAddr": polL2FilterDstMacAddr,
       "polL2FilterVlanId": polL2FilterVlanId,
       "polL2FilterInPorts": polL2FilterInPorts,
       "polL2FilterOutPorts": polL2FilterOutPorts,
       "polL2FilterCreationTime": polL2FilterCreationTime,
       "polL2FilterStatus": polL2FilterStatus,
       "polL2Dot1qVlanStaticTable": polL2Dot1qVlanStaticTable,
       "polL2Dot1qVlanStaticEntry": polL2Dot1qVlanStaticEntry,
       "polL2Dot1qVlanStaticProtocols": polL2Dot1qVlanStaticProtocols,
       "polL2Dot1qVlanStaticL4Bridging": polL2Dot1qVlanStaticL4Bridging,
       "policyMIB": policyMIB,
       "polConformance": polConformance,
       "polCompliances": polCompliances,
       "polComplianceV10": polComplianceV10,
       "polComplianceV11": polComplianceV11,
       "polComplianceV12": polComplianceV12,
       "polComplianceV13": polComplianceV13,
       "polGroups": polGroups,
       "polGroupV10": polGroupV10,
       "polGroupV11": polGroupV11,
       "polGroupV12": polGroupV12,
       "polGroupV13": polGroupV13}
)

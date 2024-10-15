# SNMP MIB module (HM2-PLATFORM-QOS-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-PLATFORM-QOS-ACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:19 2024
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

(hm2PlatformQoS,) = mibBuilder.importSymbols(
    "HM2-PLATFORM-QOS-MIB",
    "hm2PlatformQoS")

(HmEnabledStatus,) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hm2PlatformQosAcl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2)
)
hm2PlatformQosAcl.setRevisions(
        ("2012-12-20 00:00",
         "2012-05-02 00:00",
         "2011-06-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EtypeValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class Ipv6AddressPrefix(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class AclBurstSize(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 128),
    )



class Hm2PortOperator(Integer32, TextualConvention):
    status = "current"
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
        *(("eq", 0),
          ("gt", 3),
          ("lt", 2),
          ("neq", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Hm2AgentAclNotifications_ObjectIdentity = ObjectIdentity
hm2AgentAclNotifications = _Hm2AgentAclNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 0)
)
_Hm2AgentAclTable_Object = MibTable
hm2AgentAclTable = _Hm2AgentAclTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hm2AgentAclTable.setStatus("current")
_Hm2AgentAclEntry_Object = MibTableRow
hm2AgentAclEntry = _Hm2AgentAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 1, 1)
)
hm2AgentAclEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentAclEntry.setStatus("current")


class _Hm2AgentAclIndex_Type(Integer32):
    """Custom type hm2AgentAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentAclIndex_Type.__name__ = "Integer32"
_Hm2AgentAclIndex_Object = MibTableColumn
hm2AgentAclIndex = _Hm2AgentAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 1, 1, 1),
    _Hm2AgentAclIndex_Type()
)
hm2AgentAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentAclIndex.setStatus("current")
_Hm2AgentAclStatus_Type = RowStatus
_Hm2AgentAclStatus_Object = MibTableColumn
hm2AgentAclStatus = _Hm2AgentAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 1, 1, 2),
    _Hm2AgentAclStatus_Type()
)
hm2AgentAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclStatus.setStatus("current")


class _Hm2AgentAclName_Type(DisplayString):
    """Custom type hm2AgentAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hm2AgentAclName_Type.__name__ = "DisplayString"
_Hm2AgentAclName_Object = MibTableColumn
hm2AgentAclName = _Hm2AgentAclName_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 1, 1, 3),
    _Hm2AgentAclName_Type()
)
hm2AgentAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclName.setStatus("current")


class _Hm2AgentAclStatsAction_Type(Integer32):
    """Custom type hm2AgentAclStatsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushAclHitCount", 2),
          ("other", 1))
    )


_Hm2AgentAclStatsAction_Type.__name__ = "Integer32"
_Hm2AgentAclStatsAction_Object = MibTableColumn
hm2AgentAclStatsAction = _Hm2AgentAclStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 1, 1, 248),
    _Hm2AgentAclStatsAction_Type()
)
hm2AgentAclStatsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclStatsAction.setStatus("current")
_Hm2AgentAclRuleTable_Object = MibTable
hm2AgentAclRuleTable = _Hm2AgentAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4)
)
if mibBuilder.loadTexts:
    hm2AgentAclRuleTable.setStatus("current")
_Hm2AgentAclRuleEntry_Object = MibTableRow
hm2AgentAclRuleEntry = _Hm2AgentAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1)
)
hm2AgentAclRuleEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclIndex"),
    (0, "HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclRuleIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentAclRuleEntry.setStatus("current")


class _Hm2AgentAclRuleIndex_Type(Integer32):
    """Custom type hm2AgentAclRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentAclRuleIndex_Type.__name__ = "Integer32"
_Hm2AgentAclRuleIndex_Object = MibTableColumn
hm2AgentAclRuleIndex = _Hm2AgentAclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 1),
    _Hm2AgentAclRuleIndex_Type()
)
hm2AgentAclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentAclRuleIndex.setStatus("current")


class _Hm2AgentAclRuleAction_Type(Integer32):
    """Custom type hm2AgentAclRuleAction based on Integer32"""
    defaultValue = 2

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


_Hm2AgentAclRuleAction_Type.__name__ = "Integer32"
_Hm2AgentAclRuleAction_Object = MibTableColumn
hm2AgentAclRuleAction = _Hm2AgentAclRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 2),
    _Hm2AgentAclRuleAction_Type()
)
hm2AgentAclRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleAction.setStatus("current")


class _Hm2AgentAclRuleProtocol_Type(Integer32):
    """Custom type hm2AgentAclRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_Hm2AgentAclRuleProtocol_Type.__name__ = "Integer32"
_Hm2AgentAclRuleProtocol_Object = MibTableColumn
hm2AgentAclRuleProtocol = _Hm2AgentAclRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 3),
    _Hm2AgentAclRuleProtocol_Type()
)
hm2AgentAclRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleProtocol.setStatus("current")
_Hm2AgentAclRuleSrcIpAddress_Type = IpAddress
_Hm2AgentAclRuleSrcIpAddress_Object = MibTableColumn
hm2AgentAclRuleSrcIpAddress = _Hm2AgentAclRuleSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 4),
    _Hm2AgentAclRuleSrcIpAddress_Type()
)
hm2AgentAclRuleSrcIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleSrcIpAddress.setStatus("current")
_Hm2AgentAclRuleSrcIpMask_Type = IpAddress
_Hm2AgentAclRuleSrcIpMask_Object = MibTableColumn
hm2AgentAclRuleSrcIpMask = _Hm2AgentAclRuleSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 5),
    _Hm2AgentAclRuleSrcIpMask_Type()
)
hm2AgentAclRuleSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleSrcIpMask.setStatus("current")
_Hm2AgentAclRuleSrcL4Port_Type = Integer32
_Hm2AgentAclRuleSrcL4Port_Object = MibTableColumn
hm2AgentAclRuleSrcL4Port = _Hm2AgentAclRuleSrcL4Port_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 6),
    _Hm2AgentAclRuleSrcL4Port_Type()
)
hm2AgentAclRuleSrcL4Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleSrcL4Port.setStatus("current")
_Hm2AgentAclRuleSrcL4PortRangeStart_Type = Integer32
_Hm2AgentAclRuleSrcL4PortRangeStart_Object = MibTableColumn
hm2AgentAclRuleSrcL4PortRangeStart = _Hm2AgentAclRuleSrcL4PortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 7),
    _Hm2AgentAclRuleSrcL4PortRangeStart_Type()
)
hm2AgentAclRuleSrcL4PortRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleSrcL4PortRangeStart.setStatus("current")
_Hm2AgentAclRuleSrcL4PortRangeEnd_Type = Integer32
_Hm2AgentAclRuleSrcL4PortRangeEnd_Object = MibTableColumn
hm2AgentAclRuleSrcL4PortRangeEnd = _Hm2AgentAclRuleSrcL4PortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 8),
    _Hm2AgentAclRuleSrcL4PortRangeEnd_Type()
)
hm2AgentAclRuleSrcL4PortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleSrcL4PortRangeEnd.setStatus("current")
_Hm2AgentAclRuleDestIpAddress_Type = IpAddress
_Hm2AgentAclRuleDestIpAddress_Object = MibTableColumn
hm2AgentAclRuleDestIpAddress = _Hm2AgentAclRuleDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 9),
    _Hm2AgentAclRuleDestIpAddress_Type()
)
hm2AgentAclRuleDestIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleDestIpAddress.setStatus("current")
_Hm2AgentAclRuleDestIpMask_Type = IpAddress
_Hm2AgentAclRuleDestIpMask_Object = MibTableColumn
hm2AgentAclRuleDestIpMask = _Hm2AgentAclRuleDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 10),
    _Hm2AgentAclRuleDestIpMask_Type()
)
hm2AgentAclRuleDestIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleDestIpMask.setStatus("current")
_Hm2AgentAclRuleDestL4Port_Type = Integer32
_Hm2AgentAclRuleDestL4Port_Object = MibTableColumn
hm2AgentAclRuleDestL4Port = _Hm2AgentAclRuleDestL4Port_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 11),
    _Hm2AgentAclRuleDestL4Port_Type()
)
hm2AgentAclRuleDestL4Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleDestL4Port.setStatus("current")
_Hm2AgentAclRuleDestL4PortRangeStart_Type = Integer32
_Hm2AgentAclRuleDestL4PortRangeStart_Object = MibTableColumn
hm2AgentAclRuleDestL4PortRangeStart = _Hm2AgentAclRuleDestL4PortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 12),
    _Hm2AgentAclRuleDestL4PortRangeStart_Type()
)
hm2AgentAclRuleDestL4PortRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleDestL4PortRangeStart.setStatus("current")
_Hm2AgentAclRuleDestL4PortRangeEnd_Type = Integer32
_Hm2AgentAclRuleDestL4PortRangeEnd_Object = MibTableColumn
hm2AgentAclRuleDestL4PortRangeEnd = _Hm2AgentAclRuleDestL4PortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 13),
    _Hm2AgentAclRuleDestL4PortRangeEnd_Type()
)
hm2AgentAclRuleDestL4PortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleDestL4PortRangeEnd.setStatus("current")
_Hm2AgentAclRuleIPDSCP_Type = Integer32
_Hm2AgentAclRuleIPDSCP_Object = MibTableColumn
hm2AgentAclRuleIPDSCP = _Hm2AgentAclRuleIPDSCP_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 14),
    _Hm2AgentAclRuleIPDSCP_Type()
)
hm2AgentAclRuleIPDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleIPDSCP.setStatus("current")
_Hm2AgentAclRuleIpPrecedence_Type = Integer32
_Hm2AgentAclRuleIpPrecedence_Object = MibTableColumn
hm2AgentAclRuleIpPrecedence = _Hm2AgentAclRuleIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 15),
    _Hm2AgentAclRuleIpPrecedence_Type()
)
hm2AgentAclRuleIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleIpPrecedence.setStatus("current")
_Hm2AgentAclRuleIpTosBits_Type = Integer32
_Hm2AgentAclRuleIpTosBits_Object = MibTableColumn
hm2AgentAclRuleIpTosBits = _Hm2AgentAclRuleIpTosBits_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 16),
    _Hm2AgentAclRuleIpTosBits_Type()
)
hm2AgentAclRuleIpTosBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleIpTosBits.setStatus("current")
_Hm2AgentAclRuleIpTosMask_Type = Integer32
_Hm2AgentAclRuleIpTosMask_Object = MibTableColumn
hm2AgentAclRuleIpTosMask = _Hm2AgentAclRuleIpTosMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 17),
    _Hm2AgentAclRuleIpTosMask_Type()
)
hm2AgentAclRuleIpTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleIpTosMask.setStatus("current")
_Hm2AgentAclRuleStatus_Type = RowStatus
_Hm2AgentAclRuleStatus_Object = MibTableColumn
hm2AgentAclRuleStatus = _Hm2AgentAclRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 18),
    _Hm2AgentAclRuleStatus_Type()
)
hm2AgentAclRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleStatus.setStatus("current")


class _Hm2AgentAclRuleAssignQueueId_Type(Unsigned32):
    """Custom type hm2AgentAclRuleAssignQueueId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_Hm2AgentAclRuleAssignQueueId_Type.__name__ = "Unsigned32"
_Hm2AgentAclRuleAssignQueueId_Object = MibTableColumn
hm2AgentAclRuleAssignQueueId = _Hm2AgentAclRuleAssignQueueId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 19),
    _Hm2AgentAclRuleAssignQueueId_Type()
)
hm2AgentAclRuleAssignQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleAssignQueueId.setStatus("current")


class _Hm2AgentAclRuleRedirectIntf_Type(InterfaceIndexOrZero):
    """Custom type hm2AgentAclRuleRedirectIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2AgentAclRuleRedirectIntf_Object = MibTableColumn
hm2AgentAclRuleRedirectIntf = _Hm2AgentAclRuleRedirectIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 20),
    _Hm2AgentAclRuleRedirectIntf_Type()
)
hm2AgentAclRuleRedirectIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleRedirectIntf.setStatus("current")


class _Hm2AgentAclRuleMatchEvery_Type(TruthValue):
    """Custom type hm2AgentAclRuleMatchEvery based on TruthValue"""


_Hm2AgentAclRuleMatchEvery_Object = MibTableColumn
hm2AgentAclRuleMatchEvery = _Hm2AgentAclRuleMatchEvery_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 21),
    _Hm2AgentAclRuleMatchEvery_Type()
)
hm2AgentAclRuleMatchEvery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleMatchEvery.setStatus("current")


class _Hm2AgentAclRuleMirrorIntf_Type(InterfaceIndexOrZero):
    """Custom type hm2AgentAclRuleMirrorIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2AgentAclRuleMirrorIntf_Object = MibTableColumn
hm2AgentAclRuleMirrorIntf = _Hm2AgentAclRuleMirrorIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 22),
    _Hm2AgentAclRuleMirrorIntf_Type()
)
hm2AgentAclRuleMirrorIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleMirrorIntf.setStatus("current")
_Hm2AgentAclRuleLogging_Type = TruthValue
_Hm2AgentAclRuleLogging_Object = MibTableColumn
hm2AgentAclRuleLogging = _Hm2AgentAclRuleLogging_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 23),
    _Hm2AgentAclRuleLogging_Type()
)
hm2AgentAclRuleLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleLogging.setStatus("current")


class _Hm2AgentAclRuleTimeRangeName_Type(DisplayString):
    """Custom type hm2AgentAclRuleTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hm2AgentAclRuleTimeRangeName_Type.__name__ = "DisplayString"
_Hm2AgentAclRuleTimeRangeName_Object = MibTableColumn
hm2AgentAclRuleTimeRangeName = _Hm2AgentAclRuleTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 24),
    _Hm2AgentAclRuleTimeRangeName_Type()
)
hm2AgentAclRuleTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleTimeRangeName.setStatus("current")


class _Hm2AgentAclRuleTimeRangeStatus_Type(Integer32):
    """Custom type hm2AgentAclRuleTimeRangeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_Hm2AgentAclRuleTimeRangeStatus_Type.__name__ = "Integer32"
_Hm2AgentAclRuleTimeRangeStatus_Object = MibTableColumn
hm2AgentAclRuleTimeRangeStatus = _Hm2AgentAclRuleTimeRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 25),
    _Hm2AgentAclRuleTimeRangeStatus_Type()
)
hm2AgentAclRuleTimeRangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentAclRuleTimeRangeStatus.setStatus("current")


class _Hm2AgentAclRuleRedirectExtAgentId_Type(Unsigned32):
    """Custom type hm2AgentAclRuleRedirectExtAgentId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_Hm2AgentAclRuleRedirectExtAgentId_Type.__name__ = "Unsigned32"
_Hm2AgentAclRuleRedirectExtAgentId_Object = MibTableColumn
hm2AgentAclRuleRedirectExtAgentId = _Hm2AgentAclRuleRedirectExtAgentId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 28),
    _Hm2AgentAclRuleRedirectExtAgentId_Type()
)
hm2AgentAclRuleRedirectExtAgentId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleRedirectExtAgentId.setStatus("current")


class _Hm2AgentAclRuleIcmpType_Type(Integer32):
    """Custom type hm2AgentAclRuleIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_Hm2AgentAclRuleIcmpType_Type.__name__ = "Integer32"
_Hm2AgentAclRuleIcmpType_Object = MibTableColumn
hm2AgentAclRuleIcmpType = _Hm2AgentAclRuleIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 29),
    _Hm2AgentAclRuleIcmpType_Type()
)
hm2AgentAclRuleIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleIcmpType.setStatus("current")


class _Hm2AgentAclRuleIcmpCode_Type(Integer32):
    """Custom type hm2AgentAclRuleIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_Hm2AgentAclRuleIcmpCode_Type.__name__ = "Integer32"
_Hm2AgentAclRuleIcmpCode_Object = MibTableColumn
hm2AgentAclRuleIcmpCode = _Hm2AgentAclRuleIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 30),
    _Hm2AgentAclRuleIcmpCode_Type()
)
hm2AgentAclRuleIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleIcmpCode.setStatus("current")


class _Hm2AgentAclRuleIgmpType_Type(Integer32):
    """Custom type hm2AgentAclRuleIgmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_Hm2AgentAclRuleIgmpType_Type.__name__ = "Integer32"
_Hm2AgentAclRuleIgmpType_Object = MibTableColumn
hm2AgentAclRuleIgmpType = _Hm2AgentAclRuleIgmpType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 31),
    _Hm2AgentAclRuleIgmpType_Type()
)
hm2AgentAclRuleIgmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleIgmpType.setStatus("current")
_Hm2AgentAclRuleEstablished_Type = TruthValue
_Hm2AgentAclRuleEstablished_Object = MibTableColumn
hm2AgentAclRuleEstablished = _Hm2AgentAclRuleEstablished_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 32),
    _Hm2AgentAclRuleEstablished_Type()
)
hm2AgentAclRuleEstablished.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleEstablished.setStatus("current")
_Hm2AgentAclRuleFragments_Type = TruthValue
_Hm2AgentAclRuleFragments_Object = MibTableColumn
hm2AgentAclRuleFragments = _Hm2AgentAclRuleFragments_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 33),
    _Hm2AgentAclRuleFragments_Type()
)
hm2AgentAclRuleFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleFragments.setStatus("current")
_Hm2AgentAclRuleIndexNextFree_Type = Integer32
_Hm2AgentAclRuleIndexNextFree_Object = MibTableColumn
hm2AgentAclRuleIndexNextFree = _Hm2AgentAclRuleIndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 248),
    _Hm2AgentAclRuleIndexNextFree_Type()
)
hm2AgentAclRuleIndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentAclRuleIndexNextFree.setStatus("current")


class _Hm2AgentAclRuleRateLimitCrateUnit_Type(Integer32):
    """Custom type hm2AgentAclRuleRateLimitCrateUnit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 2),
          ("pps", 1))
    )


_Hm2AgentAclRuleRateLimitCrateUnit_Type.__name__ = "Integer32"
_Hm2AgentAclRuleRateLimitCrateUnit_Object = MibTableColumn
hm2AgentAclRuleRateLimitCrateUnit = _Hm2AgentAclRuleRateLimitCrateUnit_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 249),
    _Hm2AgentAclRuleRateLimitCrateUnit_Type()
)
hm2AgentAclRuleRateLimitCrateUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleRateLimitCrateUnit.setStatus("current")


class _Hm2AgentAclRuleRateLimitCrate_Type(Unsigned32):
    """Custom type hm2AgentAclRuleRateLimitCrate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_Hm2AgentAclRuleRateLimitCrate_Type.__name__ = "Unsigned32"
_Hm2AgentAclRuleRateLimitCrate_Object = MibTableColumn
hm2AgentAclRuleRateLimitCrate = _Hm2AgentAclRuleRateLimitCrate_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 250),
    _Hm2AgentAclRuleRateLimitCrate_Type()
)
hm2AgentAclRuleRateLimitCrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleRateLimitCrate.setStatus("current")


class _Hm2AgentAclRuleRateLimitCburst_Type(AclBurstSize):
    """Custom type hm2AgentAclRuleRateLimitCburst based on AclBurstSize"""
    defaultValue = 0


_Hm2AgentAclRuleRateLimitCburst_Object = MibTableColumn
hm2AgentAclRuleRateLimitCburst = _Hm2AgentAclRuleRateLimitCburst_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 251),
    _Hm2AgentAclRuleRateLimitCburst_Type()
)
hm2AgentAclRuleRateLimitCburst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleRateLimitCburst.setStatus("current")


class _Hm2AgentAclRuleStatsAction_Type(Integer32):
    """Custom type hm2AgentAclRuleStatsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushRuleHitCount", 2),
          ("other", 1))
    )


_Hm2AgentAclRuleStatsAction_Type.__name__ = "Integer32"
_Hm2AgentAclRuleStatsAction_Object = MibTableColumn
hm2AgentAclRuleStatsAction = _Hm2AgentAclRuleStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 252),
    _Hm2AgentAclRuleStatsAction_Type()
)
hm2AgentAclRuleStatsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleStatsAction.setStatus("current")
_Hm2AgentAclRuleHitCount_Type = Counter64
_Hm2AgentAclRuleHitCount_Object = MibTableColumn
hm2AgentAclRuleHitCount = _Hm2AgentAclRuleHitCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 253),
    _Hm2AgentAclRuleHitCount_Type()
)
hm2AgentAclRuleHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentAclRuleHitCount.setStatus("current")
_Hm2AgentAclRuleHitCountDiscontinuityTime_Type = TimeStamp
_Hm2AgentAclRuleHitCountDiscontinuityTime_Object = MibTableColumn
hm2AgentAclRuleHitCountDiscontinuityTime = _Hm2AgentAclRuleHitCountDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 254),
    _Hm2AgentAclRuleHitCountDiscontinuityTime_Type()
)
hm2AgentAclRuleHitCountDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentAclRuleHitCountDiscontinuityTime.setStatus("current")
_Hm2AgentAclRuleTcpFlagBits_Type = Integer32
_Hm2AgentAclRuleTcpFlagBits_Object = MibTableColumn
hm2AgentAclRuleTcpFlagBits = _Hm2AgentAclRuleTcpFlagBits_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 255),
    _Hm2AgentAclRuleTcpFlagBits_Type()
)
hm2AgentAclRuleTcpFlagBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleTcpFlagBits.setStatus("current")
_Hm2AgentAclRuleTcpFlagMask_Type = Integer32
_Hm2AgentAclRuleTcpFlagMask_Object = MibTableColumn
hm2AgentAclRuleTcpFlagMask = _Hm2AgentAclRuleTcpFlagMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 256),
    _Hm2AgentAclRuleTcpFlagMask_Type()
)
hm2AgentAclRuleTcpFlagMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleTcpFlagMask.setStatus("current")


class _Hm2AgentAclRuleSrcL4PortOperator_Type(Hm2PortOperator):
    """Custom type hm2AgentAclRuleSrcL4PortOperator based on Hm2PortOperator"""


_Hm2AgentAclRuleSrcL4PortOperator_Object = MibTableColumn
hm2AgentAclRuleSrcL4PortOperator = _Hm2AgentAclRuleSrcL4PortOperator_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 257),
    _Hm2AgentAclRuleSrcL4PortOperator_Type()
)
hm2AgentAclRuleSrcL4PortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleSrcL4PortOperator.setStatus("current")


class _Hm2AgentAclRuleDstL4PortOperator_Type(Hm2PortOperator):
    """Custom type hm2AgentAclRuleDstL4PortOperator based on Hm2PortOperator"""


_Hm2AgentAclRuleDstL4PortOperator_Object = MibTableColumn
hm2AgentAclRuleDstL4PortOperator = _Hm2AgentAclRuleDstL4PortOperator_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 4, 1, 258),
    _Hm2AgentAclRuleDstL4PortOperator_Type()
)
hm2AgentAclRuleDstL4PortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclRuleDstL4PortOperator.setStatus("current")
_Hm2AgentAclMacIndexNextFree_Type = Integer32
_Hm2AgentAclMacIndexNextFree_Object = MibScalar
hm2AgentAclMacIndexNextFree = _Hm2AgentAclMacIndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 5),
    _Hm2AgentAclMacIndexNextFree_Type()
)
hm2AgentAclMacIndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentAclMacIndexNextFree.setStatus("current")
_Hm2AgentAclMacTable_Object = MibTable
hm2AgentAclMacTable = _Hm2AgentAclMacTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 6)
)
if mibBuilder.loadTexts:
    hm2AgentAclMacTable.setStatus("current")
_Hm2AgentAclMacEntry_Object = MibTableRow
hm2AgentAclMacEntry = _Hm2AgentAclMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 6, 1)
)
hm2AgentAclMacEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclMacIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentAclMacEntry.setStatus("current")


class _Hm2AgentAclMacIndex_Type(Integer32):
    """Custom type hm2AgentAclMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentAclMacIndex_Type.__name__ = "Integer32"
_Hm2AgentAclMacIndex_Object = MibTableColumn
hm2AgentAclMacIndex = _Hm2AgentAclMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 6, 1, 1),
    _Hm2AgentAclMacIndex_Type()
)
hm2AgentAclMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentAclMacIndex.setStatus("current")


class _Hm2AgentAclMacName_Type(DisplayString):
    """Custom type hm2AgentAclMacName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hm2AgentAclMacName_Type.__name__ = "DisplayString"
_Hm2AgentAclMacName_Object = MibTableColumn
hm2AgentAclMacName = _Hm2AgentAclMacName_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 6, 1, 2),
    _Hm2AgentAclMacName_Type()
)
hm2AgentAclMacName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacName.setStatus("current")
_Hm2AgentAclMacStatus_Type = RowStatus
_Hm2AgentAclMacStatus_Object = MibTableColumn
hm2AgentAclMacStatus = _Hm2AgentAclMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 6, 1, 3),
    _Hm2AgentAclMacStatus_Type()
)
hm2AgentAclMacStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacStatus.setStatus("current")


class _Hm2AgentAclMacStatsAction_Type(Integer32):
    """Custom type hm2AgentAclMacStatsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushAclHitCount", 2),
          ("other", 1))
    )


_Hm2AgentAclMacStatsAction_Type.__name__ = "Integer32"
_Hm2AgentAclMacStatsAction_Object = MibTableColumn
hm2AgentAclMacStatsAction = _Hm2AgentAclMacStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 6, 1, 248),
    _Hm2AgentAclMacStatsAction_Type()
)
hm2AgentAclMacStatsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacStatsAction.setStatus("current")
_Hm2AgentAclMacRuleTable_Object = MibTable
hm2AgentAclMacRuleTable = _Hm2AgentAclMacRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7)
)
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleTable.setStatus("current")
_Hm2AgentAclMacRuleEntry_Object = MibTableRow
hm2AgentAclMacRuleEntry = _Hm2AgentAclMacRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1)
)
hm2AgentAclMacRuleEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclMacIndex"),
    (0, "HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclMacRuleIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleEntry.setStatus("current")


class _Hm2AgentAclMacRuleIndex_Type(Integer32):
    """Custom type hm2AgentAclMacRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentAclMacRuleIndex_Type.__name__ = "Integer32"
_Hm2AgentAclMacRuleIndex_Object = MibTableColumn
hm2AgentAclMacRuleIndex = _Hm2AgentAclMacRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 1),
    _Hm2AgentAclMacRuleIndex_Type()
)
hm2AgentAclMacRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleIndex.setStatus("current")


class _Hm2AgentAclMacRuleAction_Type(Integer32):
    """Custom type hm2AgentAclMacRuleAction based on Integer32"""
    defaultValue = 2

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


_Hm2AgentAclMacRuleAction_Type.__name__ = "Integer32"
_Hm2AgentAclMacRuleAction_Object = MibTableColumn
hm2AgentAclMacRuleAction = _Hm2AgentAclMacRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 2),
    _Hm2AgentAclMacRuleAction_Type()
)
hm2AgentAclMacRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleAction.setStatus("current")


class _Hm2AgentAclMacRuleCos_Type(Unsigned32):
    """Custom type hm2AgentAclMacRuleCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_Hm2AgentAclMacRuleCos_Type.__name__ = "Unsigned32"
_Hm2AgentAclMacRuleCos_Object = MibTableColumn
hm2AgentAclMacRuleCos = _Hm2AgentAclMacRuleCos_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 3),
    _Hm2AgentAclMacRuleCos_Type()
)
hm2AgentAclMacRuleCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleCos.setStatus("current")


class _Hm2AgentAclMacRuleCos2_Type(Unsigned32):
    """Custom type hm2AgentAclMacRuleCos2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_Hm2AgentAclMacRuleCos2_Type.__name__ = "Unsigned32"
_Hm2AgentAclMacRuleCos2_Object = MibTableColumn
hm2AgentAclMacRuleCos2 = _Hm2AgentAclMacRuleCos2_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 4),
    _Hm2AgentAclMacRuleCos2_Type()
)
hm2AgentAclMacRuleCos2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleCos2.setStatus("current")
_Hm2AgentAclMacRuleDestMacAddr_Type = MacAddress
_Hm2AgentAclMacRuleDestMacAddr_Object = MibTableColumn
hm2AgentAclMacRuleDestMacAddr = _Hm2AgentAclMacRuleDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 5),
    _Hm2AgentAclMacRuleDestMacAddr_Type()
)
hm2AgentAclMacRuleDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleDestMacAddr.setStatus("current")
_Hm2AgentAclMacRuleDestMacMask_Type = MacAddress
_Hm2AgentAclMacRuleDestMacMask_Object = MibTableColumn
hm2AgentAclMacRuleDestMacMask = _Hm2AgentAclMacRuleDestMacMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 6),
    _Hm2AgentAclMacRuleDestMacMask_Type()
)
hm2AgentAclMacRuleDestMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleDestMacMask.setStatus("current")


class _Hm2AgentAclMacRuleEtypeKey_Type(Integer32):
    """Custom type hm2AgentAclMacRuleEtypeKey based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              248)
        )
    )
    namedValues = NamedValues(
        *(("appletalk", 2),
          ("arp", 3),
          ("custom", 1),
          ("ethercat", 18),
          ("ibmsna", 4),
          ("ipv4", 5),
          ("ipv6", 6),
          ("ipxnew", 15),
          ("ipxold", 7),
          ("mplsmcast", 8),
          ("mplsucast", 9),
          ("netbios", 10),
          ("novell", 11),
          ("powerlink", 17),
          ("pppoe", 248),
          ("pppoedisc", 12),
          ("pppoesess", 14),
          ("profinet", 16),
          ("rarp", 13))
    )


_Hm2AgentAclMacRuleEtypeKey_Type.__name__ = "Integer32"
_Hm2AgentAclMacRuleEtypeKey_Object = MibTableColumn
hm2AgentAclMacRuleEtypeKey = _Hm2AgentAclMacRuleEtypeKey_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 7),
    _Hm2AgentAclMacRuleEtypeKey_Type()
)
hm2AgentAclMacRuleEtypeKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleEtypeKey.setStatus("current")
_Hm2AgentAclMacRuleEtypeValue_Type = EtypeValue
_Hm2AgentAclMacRuleEtypeValue_Object = MibTableColumn
hm2AgentAclMacRuleEtypeValue = _Hm2AgentAclMacRuleEtypeValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 8),
    _Hm2AgentAclMacRuleEtypeValue_Type()
)
hm2AgentAclMacRuleEtypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleEtypeValue.setStatus("current")
_Hm2AgentAclMacRuleSrcMacAddr_Type = MacAddress
_Hm2AgentAclMacRuleSrcMacAddr_Object = MibTableColumn
hm2AgentAclMacRuleSrcMacAddr = _Hm2AgentAclMacRuleSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 9),
    _Hm2AgentAclMacRuleSrcMacAddr_Type()
)
hm2AgentAclMacRuleSrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleSrcMacAddr.setStatus("current")
_Hm2AgentAclMacRuleSrcMacMask_Type = MacAddress
_Hm2AgentAclMacRuleSrcMacMask_Object = MibTableColumn
hm2AgentAclMacRuleSrcMacMask = _Hm2AgentAclMacRuleSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 10),
    _Hm2AgentAclMacRuleSrcMacMask_Type()
)
hm2AgentAclMacRuleSrcMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleSrcMacMask.setStatus("current")


class _Hm2AgentAclMacRuleVlanId_Type(Unsigned32):
    """Custom type hm2AgentAclMacRuleVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4042),
    )


_Hm2AgentAclMacRuleVlanId_Type.__name__ = "Unsigned32"
_Hm2AgentAclMacRuleVlanId_Object = MibTableColumn
hm2AgentAclMacRuleVlanId = _Hm2AgentAclMacRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 11),
    _Hm2AgentAclMacRuleVlanId_Type()
)
hm2AgentAclMacRuleVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleVlanId.setStatus("current")


class _Hm2AgentAclMacRuleVlanIdRangeStart_Type(Unsigned32):
    """Custom type hm2AgentAclMacRuleVlanIdRangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4042),
    )


_Hm2AgentAclMacRuleVlanIdRangeStart_Type.__name__ = "Unsigned32"
_Hm2AgentAclMacRuleVlanIdRangeStart_Object = MibTableColumn
hm2AgentAclMacRuleVlanIdRangeStart = _Hm2AgentAclMacRuleVlanIdRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 12),
    _Hm2AgentAclMacRuleVlanIdRangeStart_Type()
)
hm2AgentAclMacRuleVlanIdRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleVlanIdRangeStart.setStatus("current")


class _Hm2AgentAclMacRuleVlanIdRangeEnd_Type(Unsigned32):
    """Custom type hm2AgentAclMacRuleVlanIdRangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4042),
    )


_Hm2AgentAclMacRuleVlanIdRangeEnd_Type.__name__ = "Unsigned32"
_Hm2AgentAclMacRuleVlanIdRangeEnd_Object = MibTableColumn
hm2AgentAclMacRuleVlanIdRangeEnd = _Hm2AgentAclMacRuleVlanIdRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 13),
    _Hm2AgentAclMacRuleVlanIdRangeEnd_Type()
)
hm2AgentAclMacRuleVlanIdRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleVlanIdRangeEnd.setStatus("current")


class _Hm2AgentAclMacRuleVlanId2_Type(Unsigned32):
    """Custom type hm2AgentAclMacRuleVlanId2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4042),
    )


_Hm2AgentAclMacRuleVlanId2_Type.__name__ = "Unsigned32"
_Hm2AgentAclMacRuleVlanId2_Object = MibTableColumn
hm2AgentAclMacRuleVlanId2 = _Hm2AgentAclMacRuleVlanId2_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 14),
    _Hm2AgentAclMacRuleVlanId2_Type()
)
hm2AgentAclMacRuleVlanId2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleVlanId2.setStatus("current")


class _Hm2AgentAclMacRuleVlanId2RangeStart_Type(Unsigned32):
    """Custom type hm2AgentAclMacRuleVlanId2RangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4042),
    )


_Hm2AgentAclMacRuleVlanId2RangeStart_Type.__name__ = "Unsigned32"
_Hm2AgentAclMacRuleVlanId2RangeStart_Object = MibTableColumn
hm2AgentAclMacRuleVlanId2RangeStart = _Hm2AgentAclMacRuleVlanId2RangeStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 15),
    _Hm2AgentAclMacRuleVlanId2RangeStart_Type()
)
hm2AgentAclMacRuleVlanId2RangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleVlanId2RangeStart.setStatus("current")


class _Hm2AgentAclMacRuleVlanId2RangeEnd_Type(Unsigned32):
    """Custom type hm2AgentAclMacRuleVlanId2RangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4042),
    )


_Hm2AgentAclMacRuleVlanId2RangeEnd_Type.__name__ = "Unsigned32"
_Hm2AgentAclMacRuleVlanId2RangeEnd_Object = MibTableColumn
hm2AgentAclMacRuleVlanId2RangeEnd = _Hm2AgentAclMacRuleVlanId2RangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 16),
    _Hm2AgentAclMacRuleVlanId2RangeEnd_Type()
)
hm2AgentAclMacRuleVlanId2RangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleVlanId2RangeEnd.setStatus("current")
_Hm2AgentAclMacRuleStatus_Type = RowStatus
_Hm2AgentAclMacRuleStatus_Object = MibTableColumn
hm2AgentAclMacRuleStatus = _Hm2AgentAclMacRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 17),
    _Hm2AgentAclMacRuleStatus_Type()
)
hm2AgentAclMacRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleStatus.setStatus("current")


class _Hm2AgentAclMacRuleAssignQueueId_Type(Unsigned32):
    """Custom type hm2AgentAclMacRuleAssignQueueId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_Hm2AgentAclMacRuleAssignQueueId_Type.__name__ = "Unsigned32"
_Hm2AgentAclMacRuleAssignQueueId_Object = MibTableColumn
hm2AgentAclMacRuleAssignQueueId = _Hm2AgentAclMacRuleAssignQueueId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 18),
    _Hm2AgentAclMacRuleAssignQueueId_Type()
)
hm2AgentAclMacRuleAssignQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleAssignQueueId.setStatus("current")


class _Hm2AgentAclMacRuleRedirectIntf_Type(InterfaceIndexOrZero):
    """Custom type hm2AgentAclMacRuleRedirectIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2AgentAclMacRuleRedirectIntf_Object = MibTableColumn
hm2AgentAclMacRuleRedirectIntf = _Hm2AgentAclMacRuleRedirectIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 19),
    _Hm2AgentAclMacRuleRedirectIntf_Type()
)
hm2AgentAclMacRuleRedirectIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleRedirectIntf.setStatus("current")
_Hm2AgentAclMacRuleMatchEvery_Type = TruthValue
_Hm2AgentAclMacRuleMatchEvery_Object = MibTableColumn
hm2AgentAclMacRuleMatchEvery = _Hm2AgentAclMacRuleMatchEvery_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 20),
    _Hm2AgentAclMacRuleMatchEvery_Type()
)
hm2AgentAclMacRuleMatchEvery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleMatchEvery.setStatus("current")


class _Hm2AgentAclMacRuleMirrorIntf_Type(InterfaceIndexOrZero):
    """Custom type hm2AgentAclMacRuleMirrorIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2AgentAclMacRuleMirrorIntf_Object = MibTableColumn
hm2AgentAclMacRuleMirrorIntf = _Hm2AgentAclMacRuleMirrorIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 21),
    _Hm2AgentAclMacRuleMirrorIntf_Type()
)
hm2AgentAclMacRuleMirrorIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleMirrorIntf.setStatus("current")
_Hm2AgentAclMacRuleLogging_Type = TruthValue
_Hm2AgentAclMacRuleLogging_Object = MibTableColumn
hm2AgentAclMacRuleLogging = _Hm2AgentAclMacRuleLogging_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 22),
    _Hm2AgentAclMacRuleLogging_Type()
)
hm2AgentAclMacRuleLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleLogging.setStatus("current")


class _Hm2AgentAclMacRuleTimeRangeName_Type(DisplayString):
    """Custom type hm2AgentAclMacRuleTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hm2AgentAclMacRuleTimeRangeName_Type.__name__ = "DisplayString"
_Hm2AgentAclMacRuleTimeRangeName_Object = MibTableColumn
hm2AgentAclMacRuleTimeRangeName = _Hm2AgentAclMacRuleTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 23),
    _Hm2AgentAclMacRuleTimeRangeName_Type()
)
hm2AgentAclMacRuleTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleTimeRangeName.setStatus("current")


class _Hm2AgentAclMacRuleTimeRangeStatus_Type(Integer32):
    """Custom type hm2AgentAclMacRuleTimeRangeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_Hm2AgentAclMacRuleTimeRangeStatus_Type.__name__ = "Integer32"
_Hm2AgentAclMacRuleTimeRangeStatus_Object = MibTableColumn
hm2AgentAclMacRuleTimeRangeStatus = _Hm2AgentAclMacRuleTimeRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 24),
    _Hm2AgentAclMacRuleTimeRangeStatus_Type()
)
hm2AgentAclMacRuleTimeRangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleTimeRangeStatus.setStatus("current")
_Hm2AgentAclMacRuleIndexNextFree_Type = Integer32
_Hm2AgentAclMacRuleIndexNextFree_Object = MibTableColumn
hm2AgentAclMacRuleIndexNextFree = _Hm2AgentAclMacRuleIndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 248),
    _Hm2AgentAclMacRuleIndexNextFree_Type()
)
hm2AgentAclMacRuleIndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleIndexNextFree.setStatus("current")


class _Hm2AgentAclMacRuleRateLimitCrateUnit_Type(Integer32):
    """Custom type hm2AgentAclMacRuleRateLimitCrateUnit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 2),
          ("pps", 1))
    )


_Hm2AgentAclMacRuleRateLimitCrateUnit_Type.__name__ = "Integer32"
_Hm2AgentAclMacRuleRateLimitCrateUnit_Object = MibTableColumn
hm2AgentAclMacRuleRateLimitCrateUnit = _Hm2AgentAclMacRuleRateLimitCrateUnit_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 249),
    _Hm2AgentAclMacRuleRateLimitCrateUnit_Type()
)
hm2AgentAclMacRuleRateLimitCrateUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleRateLimitCrateUnit.setStatus("current")


class _Hm2AgentAclMacRuleRateLimitCrate_Type(Unsigned32):
    """Custom type hm2AgentAclMacRuleRateLimitCrate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_Hm2AgentAclMacRuleRateLimitCrate_Type.__name__ = "Unsigned32"
_Hm2AgentAclMacRuleRateLimitCrate_Object = MibTableColumn
hm2AgentAclMacRuleRateLimitCrate = _Hm2AgentAclMacRuleRateLimitCrate_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 250),
    _Hm2AgentAclMacRuleRateLimitCrate_Type()
)
hm2AgentAclMacRuleRateLimitCrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleRateLimitCrate.setStatus("current")


class _Hm2AgentAclMacRuleRateLimitCburst_Type(AclBurstSize):
    """Custom type hm2AgentAclMacRuleRateLimitCburst based on AclBurstSize"""
    defaultValue = 0


_Hm2AgentAclMacRuleRateLimitCburst_Object = MibTableColumn
hm2AgentAclMacRuleRateLimitCburst = _Hm2AgentAclMacRuleRateLimitCburst_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 251),
    _Hm2AgentAclMacRuleRateLimitCburst_Type()
)
hm2AgentAclMacRuleRateLimitCburst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleRateLimitCburst.setStatus("current")


class _Hm2AgentAclMacRuleStatsAction_Type(Integer32):
    """Custom type hm2AgentAclMacRuleStatsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushRuleHitCount", 2),
          ("other", 1))
    )


_Hm2AgentAclMacRuleStatsAction_Type.__name__ = "Integer32"
_Hm2AgentAclMacRuleStatsAction_Object = MibTableColumn
hm2AgentAclMacRuleStatsAction = _Hm2AgentAclMacRuleStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 252),
    _Hm2AgentAclMacRuleStatsAction_Type()
)
hm2AgentAclMacRuleStatsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleStatsAction.setStatus("current")
_Hm2AgentAclMacRuleHitCount_Type = Counter64
_Hm2AgentAclMacRuleHitCount_Object = MibTableColumn
hm2AgentAclMacRuleHitCount = _Hm2AgentAclMacRuleHitCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 253),
    _Hm2AgentAclMacRuleHitCount_Type()
)
hm2AgentAclMacRuleHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleHitCount.setStatus("current")
_Hm2AgentAclMacRuleHitCountDiscontinuityTime_Type = TimeStamp
_Hm2AgentAclMacRuleHitCountDiscontinuityTime_Object = MibTableColumn
hm2AgentAclMacRuleHitCountDiscontinuityTime = _Hm2AgentAclMacRuleHitCountDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 7, 1, 254),
    _Hm2AgentAclMacRuleHitCountDiscontinuityTime_Type()
)
hm2AgentAclMacRuleHitCountDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentAclMacRuleHitCountDiscontinuityTime.setStatus("current")
_Hm2AgentAclIfTable_Object = MibTable
hm2AgentAclIfTable = _Hm2AgentAclIfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 8)
)
if mibBuilder.loadTexts:
    hm2AgentAclIfTable.setStatus("current")
_Hm2AgentAclIfEntry_Object = MibTableRow
hm2AgentAclIfEntry = _Hm2AgentAclIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 8, 1)
)
hm2AgentAclIfEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclIfIndex"),
    (0, "HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclIfDirection"),
    (0, "HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclIfSequence"),
    (0, "HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclIfAclType"),
    (0, "HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclIfAclId"),
)
if mibBuilder.loadTexts:
    hm2AgentAclIfEntry.setStatus("current")


class _Hm2AgentAclIfIndex_Type(Integer32):
    """Custom type hm2AgentAclIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentAclIfIndex_Type.__name__ = "Integer32"
_Hm2AgentAclIfIndex_Object = MibTableColumn
hm2AgentAclIfIndex = _Hm2AgentAclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 8, 1, 1),
    _Hm2AgentAclIfIndex_Type()
)
hm2AgentAclIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentAclIfIndex.setStatus("current")


class _Hm2AgentAclIfDirection_Type(Integer32):
    """Custom type hm2AgentAclIfDirection based on Integer32"""
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


_Hm2AgentAclIfDirection_Type.__name__ = "Integer32"
_Hm2AgentAclIfDirection_Object = MibTableColumn
hm2AgentAclIfDirection = _Hm2AgentAclIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 8, 1, 2),
    _Hm2AgentAclIfDirection_Type()
)
hm2AgentAclIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentAclIfDirection.setStatus("current")


class _Hm2AgentAclIfSequence_Type(Unsigned32):
    """Custom type hm2AgentAclIfSequence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hm2AgentAclIfSequence_Type.__name__ = "Unsigned32"
_Hm2AgentAclIfSequence_Object = MibTableColumn
hm2AgentAclIfSequence = _Hm2AgentAclIfSequence_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 8, 1, 3),
    _Hm2AgentAclIfSequence_Type()
)
hm2AgentAclIfSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentAclIfSequence.setStatus("current")


class _Hm2AgentAclIfAclType_Type(Integer32):
    """Custom type hm2AgentAclIfAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ipv6", 3),
          ("mac", 2))
    )


_Hm2AgentAclIfAclType_Type.__name__ = "Integer32"
_Hm2AgentAclIfAclType_Object = MibTableColumn
hm2AgentAclIfAclType = _Hm2AgentAclIfAclType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 8, 1, 4),
    _Hm2AgentAclIfAclType_Type()
)
hm2AgentAclIfAclType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2AgentAclIfAclType.setStatus("current")


class _Hm2AgentAclIfAclId_Type(Integer32):
    """Custom type hm2AgentAclIfAclId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentAclIfAclId_Type.__name__ = "Integer32"
_Hm2AgentAclIfAclId_Object = MibTableColumn
hm2AgentAclIfAclId = _Hm2AgentAclIfAclId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 8, 1, 5),
    _Hm2AgentAclIfAclId_Type()
)
hm2AgentAclIfAclId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2AgentAclIfAclId.setStatus("current")
_Hm2AgentAclIfStatus_Type = RowStatus
_Hm2AgentAclIfStatus_Object = MibTableColumn
hm2AgentAclIfStatus = _Hm2AgentAclIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 8, 1, 6),
    _Hm2AgentAclIfStatus_Type()
)
hm2AgentAclIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclIfStatus.setStatus("current")
_Hm2AgentAclLoggingGroup_ObjectIdentity = ObjectIdentity
hm2AgentAclLoggingGroup = _Hm2AgentAclLoggingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 9)
)


class _Hm2AgentAclTrapRuleIndex_Type(Integer32):
    """Custom type hm2AgentAclTrapRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentAclTrapRuleIndex_Type.__name__ = "Integer32"
_Hm2AgentAclTrapRuleIndex_Object = MibScalar
hm2AgentAclTrapRuleIndex = _Hm2AgentAclTrapRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 9, 2),
    _Hm2AgentAclTrapRuleIndex_Type()
)
hm2AgentAclTrapRuleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2AgentAclTrapRuleIndex.setStatus("current")


class _Hm2AgentAclTrapRuleAction_Type(Integer32):
    """Custom type hm2AgentAclTrapRuleAction based on Integer32"""
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


_Hm2AgentAclTrapRuleAction_Type.__name__ = "Integer32"
_Hm2AgentAclTrapRuleAction_Object = MibScalar
hm2AgentAclTrapRuleAction = _Hm2AgentAclTrapRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 9, 3),
    _Hm2AgentAclTrapRuleAction_Type()
)
hm2AgentAclTrapRuleAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2AgentAclTrapRuleAction.setStatus("current")
_Hm2AgentAclTrapRuleHitCount_Type = Counter64
_Hm2AgentAclTrapRuleHitCount_Object = MibScalar
hm2AgentAclTrapRuleHitCount = _Hm2AgentAclTrapRuleHitCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 9, 4),
    _Hm2AgentAclTrapRuleHitCount_Type()
)
hm2AgentAclTrapRuleHitCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2AgentAclTrapRuleHitCount.setStatus("current")


class _Hm2AgentAclTrapFlag_Type(HmEnabledStatus):
    """Custom type hm2AgentAclTrapFlag based on HmEnabledStatus"""


_Hm2AgentAclTrapFlag_Object = MibScalar
hm2AgentAclTrapFlag = _Hm2AgentAclTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 9, 5),
    _Hm2AgentAclTrapFlag_Type()
)
hm2AgentAclTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentAclTrapFlag.setStatus("current")


class _Hm2AgentAclTrapRuleTimeRangeName_Type(DisplayString):
    """Custom type hm2AgentAclTrapRuleTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hm2AgentAclTrapRuleTimeRangeName_Type.__name__ = "DisplayString"
_Hm2AgentAclTrapRuleTimeRangeName_Object = MibScalar
hm2AgentAclTrapRuleTimeRangeName = _Hm2AgentAclTrapRuleTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 9, 6),
    _Hm2AgentAclTrapRuleTimeRangeName_Type()
)
hm2AgentAclTrapRuleTimeRangeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2AgentAclTrapRuleTimeRangeName.setStatus("current")


class _Hm2AgentAclTrapRuleTimeRangeNotification_Type(Integer32):
    """Custom type hm2AgentAclTrapRuleTimeRangeNotification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("deactivate", 2),
          ("delete", 3))
    )


_Hm2AgentAclTrapRuleTimeRangeNotification_Type.__name__ = "Integer32"
_Hm2AgentAclTrapRuleTimeRangeNotification_Object = MibScalar
hm2AgentAclTrapRuleTimeRangeNotification = _Hm2AgentAclTrapRuleTimeRangeNotification_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 9, 7),
    _Hm2AgentAclTrapRuleTimeRangeNotification_Type()
)
hm2AgentAclTrapRuleTimeRangeNotification.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2AgentAclTrapRuleTimeRangeNotification.setStatus("current")


class _Hm2AgentAclTrapRuleInstallationStatus_Type(Integer32):
    """Custom type hm2AgentAclTrapRuleInstallationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 1),
          ("success", 2))
    )


_Hm2AgentAclTrapRuleInstallationStatus_Type.__name__ = "Integer32"
_Hm2AgentAclTrapRuleInstallationStatus_Object = MibScalar
hm2AgentAclTrapRuleInstallationStatus = _Hm2AgentAclTrapRuleInstallationStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 9, 8),
    _Hm2AgentAclTrapRuleInstallationStatus_Type()
)
hm2AgentAclTrapRuleInstallationStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2AgentAclTrapRuleInstallationStatus.setStatus("current")
_Hm2AgentAclTrapRuleHitCountHigh_Type = Gauge32
_Hm2AgentAclTrapRuleHitCountHigh_Object = MibScalar
hm2AgentAclTrapRuleHitCountHigh = _Hm2AgentAclTrapRuleHitCountHigh_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 9, 248),
    _Hm2AgentAclTrapRuleHitCountHigh_Type()
)
hm2AgentAclTrapRuleHitCountHigh.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2AgentAclTrapRuleHitCountHigh.setStatus("current")
_Hm2AgentAclTrapRuleHitCountLow_Type = Gauge32
_Hm2AgentAclTrapRuleHitCountLow_Object = MibScalar
hm2AgentAclTrapRuleHitCountLow = _Hm2AgentAclTrapRuleHitCountLow_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 9, 249),
    _Hm2AgentAclTrapRuleHitCountLow_Type()
)
hm2AgentAclTrapRuleHitCountLow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2AgentAclTrapRuleHitCountLow.setStatus("current")
_Hm2AgentAclVlanTable_Object = MibTable
hm2AgentAclVlanTable = _Hm2AgentAclVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 13)
)
if mibBuilder.loadTexts:
    hm2AgentAclVlanTable.setStatus("current")
_Hm2AgentAclVlanEntry_Object = MibTableRow
hm2AgentAclVlanEntry = _Hm2AgentAclVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 13, 1)
)
hm2AgentAclVlanEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclVlanIndex"),
    (0, "HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclVlanDirection"),
    (0, "HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclVlanSequence"),
    (0, "HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclVlanAclType"),
    (0, "HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclVlanAclId"),
)
if mibBuilder.loadTexts:
    hm2AgentAclVlanEntry.setStatus("current")


class _Hm2AgentAclVlanIndex_Type(Integer32):
    """Custom type hm2AgentAclVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentAclVlanIndex_Type.__name__ = "Integer32"
_Hm2AgentAclVlanIndex_Object = MibTableColumn
hm2AgentAclVlanIndex = _Hm2AgentAclVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 13, 1, 1),
    _Hm2AgentAclVlanIndex_Type()
)
hm2AgentAclVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentAclVlanIndex.setStatus("current")


class _Hm2AgentAclVlanDirection_Type(Integer32):
    """Custom type hm2AgentAclVlanDirection based on Integer32"""
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


_Hm2AgentAclVlanDirection_Type.__name__ = "Integer32"
_Hm2AgentAclVlanDirection_Object = MibTableColumn
hm2AgentAclVlanDirection = _Hm2AgentAclVlanDirection_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 13, 1, 2),
    _Hm2AgentAclVlanDirection_Type()
)
hm2AgentAclVlanDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentAclVlanDirection.setStatus("current")


class _Hm2AgentAclVlanSequence_Type(Unsigned32):
    """Custom type hm2AgentAclVlanSequence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hm2AgentAclVlanSequence_Type.__name__ = "Unsigned32"
_Hm2AgentAclVlanSequence_Object = MibTableColumn
hm2AgentAclVlanSequence = _Hm2AgentAclVlanSequence_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 13, 1, 3),
    _Hm2AgentAclVlanSequence_Type()
)
hm2AgentAclVlanSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentAclVlanSequence.setStatus("current")


class _Hm2AgentAclVlanAclType_Type(Integer32):
    """Custom type hm2AgentAclVlanAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ipv6", 3),
          ("mac", 2))
    )


_Hm2AgentAclVlanAclType_Type.__name__ = "Integer32"
_Hm2AgentAclVlanAclType_Object = MibTableColumn
hm2AgentAclVlanAclType = _Hm2AgentAclVlanAclType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 13, 1, 4),
    _Hm2AgentAclVlanAclType_Type()
)
hm2AgentAclVlanAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentAclVlanAclType.setStatus("current")


class _Hm2AgentAclVlanAclId_Type(Integer32):
    """Custom type hm2AgentAclVlanAclId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentAclVlanAclId_Type.__name__ = "Integer32"
_Hm2AgentAclVlanAclId_Object = MibTableColumn
hm2AgentAclVlanAclId = _Hm2AgentAclVlanAclId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 13, 1, 5),
    _Hm2AgentAclVlanAclId_Type()
)
hm2AgentAclVlanAclId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentAclVlanAclId.setStatus("current")
_Hm2AgentAclVlanStatus_Type = RowStatus
_Hm2AgentAclVlanStatus_Object = MibTableColumn
hm2AgentAclVlanStatus = _Hm2AgentAclVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 13, 1, 6),
    _Hm2AgentAclVlanStatus_Type()
)
hm2AgentAclVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentAclVlanStatus.setStatus("current")
_Hm2AgentAclNamedIpv4IndexNextFree_Type = Integer32
_Hm2AgentAclNamedIpv4IndexNextFree_Object = MibScalar
hm2AgentAclNamedIpv4IndexNextFree = _Hm2AgentAclNamedIpv4IndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 14),
    _Hm2AgentAclNamedIpv4IndexNextFree_Type()
)
hm2AgentAclNamedIpv4IndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentAclNamedIpv4IndexNextFree.setStatus("current")
_Hm2AgentOperatorRuleAssignOutboundInvalid_ObjectIdentity = ObjectIdentity
hm2AgentOperatorRuleAssignOutboundInvalid = _Hm2AgentOperatorRuleAssignOutboundInvalid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 248)
)
if mibBuilder.loadTexts:
    hm2AgentOperatorRuleAssignOutboundInvalid.setStatus("current")

# Managed Objects groups


# Notification objects

hm2AgentAclTrapRuleLogEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 0, 1)
)
hm2AgentAclTrapRuleLogEvent.setObjects(
      *(("HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclIfAclType"),
        ("HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclIfAclId"),
        ("HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclTrapRuleIndex"),
        ("HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclTrapRuleAction"),
        ("HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclTrapRuleHitCount"))
)
if mibBuilder.loadTexts:
    hm2AgentAclTrapRuleLogEvent.setStatus(
        "current"
    )

hm2AgentAclTrapRuleTimeRangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 0, 2)
)
hm2AgentAclTrapRuleTimeRangeEvent.setObjects(
      *(("HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclIfAclType"),
        ("HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclIfAclId"),
        ("HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclTrapRuleIndex"),
        ("HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclTrapRuleTimeRangeName"),
        ("HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclTrapRuleTimeRangeNotification"),
        ("HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclTrapRuleInstallationStatus"))
)
if mibBuilder.loadTexts:
    hm2AgentAclTrapRuleTimeRangeEvent.setStatus(
        "current"
    )

hm2AgentAclTrapRuleLogEventV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 12, 3, 2, 0, 248)
)
hm2AgentAclTrapRuleLogEventV1.setObjects(
      *(("HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclIfAclType"),
        ("HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclIfAclId"),
        ("HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclTrapRuleIndex"),
        ("HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclTrapRuleAction"),
        ("HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclTrapRuleHitCountHigh"),
        ("HM2-PLATFORM-QOS-ACL-MIB", "hm2AgentAclTrapRuleHitCountLow"))
)
if mibBuilder.loadTexts:
    hm2AgentAclTrapRuleLogEventV1.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PLATFORM-QOS-ACL-MIB",
    **{"EtypeValue": EtypeValue,
       "Ipv6AddressPrefix": Ipv6AddressPrefix,
       "AclBurstSize": AclBurstSize,
       "Hm2PortOperator": Hm2PortOperator,
       "hm2PlatformQosAcl": hm2PlatformQosAcl,
       "hm2AgentAclNotifications": hm2AgentAclNotifications,
       "hm2AgentAclTrapRuleLogEvent": hm2AgentAclTrapRuleLogEvent,
       "hm2AgentAclTrapRuleTimeRangeEvent": hm2AgentAclTrapRuleTimeRangeEvent,
       "hm2AgentAclTrapRuleLogEventV1": hm2AgentAclTrapRuleLogEventV1,
       "hm2AgentAclTable": hm2AgentAclTable,
       "hm2AgentAclEntry": hm2AgentAclEntry,
       "hm2AgentAclIndex": hm2AgentAclIndex,
       "hm2AgentAclStatus": hm2AgentAclStatus,
       "hm2AgentAclName": hm2AgentAclName,
       "hm2AgentAclStatsAction": hm2AgentAclStatsAction,
       "hm2AgentAclRuleTable": hm2AgentAclRuleTable,
       "hm2AgentAclRuleEntry": hm2AgentAclRuleEntry,
       "hm2AgentAclRuleIndex": hm2AgentAclRuleIndex,
       "hm2AgentAclRuleAction": hm2AgentAclRuleAction,
       "hm2AgentAclRuleProtocol": hm2AgentAclRuleProtocol,
       "hm2AgentAclRuleSrcIpAddress": hm2AgentAclRuleSrcIpAddress,
       "hm2AgentAclRuleSrcIpMask": hm2AgentAclRuleSrcIpMask,
       "hm2AgentAclRuleSrcL4Port": hm2AgentAclRuleSrcL4Port,
       "hm2AgentAclRuleSrcL4PortRangeStart": hm2AgentAclRuleSrcL4PortRangeStart,
       "hm2AgentAclRuleSrcL4PortRangeEnd": hm2AgentAclRuleSrcL4PortRangeEnd,
       "hm2AgentAclRuleDestIpAddress": hm2AgentAclRuleDestIpAddress,
       "hm2AgentAclRuleDestIpMask": hm2AgentAclRuleDestIpMask,
       "hm2AgentAclRuleDestL4Port": hm2AgentAclRuleDestL4Port,
       "hm2AgentAclRuleDestL4PortRangeStart": hm2AgentAclRuleDestL4PortRangeStart,
       "hm2AgentAclRuleDestL4PortRangeEnd": hm2AgentAclRuleDestL4PortRangeEnd,
       "hm2AgentAclRuleIPDSCP": hm2AgentAclRuleIPDSCP,
       "hm2AgentAclRuleIpPrecedence": hm2AgentAclRuleIpPrecedence,
       "hm2AgentAclRuleIpTosBits": hm2AgentAclRuleIpTosBits,
       "hm2AgentAclRuleIpTosMask": hm2AgentAclRuleIpTosMask,
       "hm2AgentAclRuleStatus": hm2AgentAclRuleStatus,
       "hm2AgentAclRuleAssignQueueId": hm2AgentAclRuleAssignQueueId,
       "hm2AgentAclRuleRedirectIntf": hm2AgentAclRuleRedirectIntf,
       "hm2AgentAclRuleMatchEvery": hm2AgentAclRuleMatchEvery,
       "hm2AgentAclRuleMirrorIntf": hm2AgentAclRuleMirrorIntf,
       "hm2AgentAclRuleLogging": hm2AgentAclRuleLogging,
       "hm2AgentAclRuleTimeRangeName": hm2AgentAclRuleTimeRangeName,
       "hm2AgentAclRuleTimeRangeStatus": hm2AgentAclRuleTimeRangeStatus,
       "hm2AgentAclRuleRedirectExtAgentId": hm2AgentAclRuleRedirectExtAgentId,
       "hm2AgentAclRuleIcmpType": hm2AgentAclRuleIcmpType,
       "hm2AgentAclRuleIcmpCode": hm2AgentAclRuleIcmpCode,
       "hm2AgentAclRuleIgmpType": hm2AgentAclRuleIgmpType,
       "hm2AgentAclRuleEstablished": hm2AgentAclRuleEstablished,
       "hm2AgentAclRuleFragments": hm2AgentAclRuleFragments,
       "hm2AgentAclRuleIndexNextFree": hm2AgentAclRuleIndexNextFree,
       "hm2AgentAclRuleRateLimitCrateUnit": hm2AgentAclRuleRateLimitCrateUnit,
       "hm2AgentAclRuleRateLimitCrate": hm2AgentAclRuleRateLimitCrate,
       "hm2AgentAclRuleRateLimitCburst": hm2AgentAclRuleRateLimitCburst,
       "hm2AgentAclRuleStatsAction": hm2AgentAclRuleStatsAction,
       "hm2AgentAclRuleHitCount": hm2AgentAclRuleHitCount,
       "hm2AgentAclRuleHitCountDiscontinuityTime": hm2AgentAclRuleHitCountDiscontinuityTime,
       "hm2AgentAclRuleTcpFlagBits": hm2AgentAclRuleTcpFlagBits,
       "hm2AgentAclRuleTcpFlagMask": hm2AgentAclRuleTcpFlagMask,
       "hm2AgentAclRuleSrcL4PortOperator": hm2AgentAclRuleSrcL4PortOperator,
       "hm2AgentAclRuleDstL4PortOperator": hm2AgentAclRuleDstL4PortOperator,
       "hm2AgentAclMacIndexNextFree": hm2AgentAclMacIndexNextFree,
       "hm2AgentAclMacTable": hm2AgentAclMacTable,
       "hm2AgentAclMacEntry": hm2AgentAclMacEntry,
       "hm2AgentAclMacIndex": hm2AgentAclMacIndex,
       "hm2AgentAclMacName": hm2AgentAclMacName,
       "hm2AgentAclMacStatus": hm2AgentAclMacStatus,
       "hm2AgentAclMacStatsAction": hm2AgentAclMacStatsAction,
       "hm2AgentAclMacRuleTable": hm2AgentAclMacRuleTable,
       "hm2AgentAclMacRuleEntry": hm2AgentAclMacRuleEntry,
       "hm2AgentAclMacRuleIndex": hm2AgentAclMacRuleIndex,
       "hm2AgentAclMacRuleAction": hm2AgentAclMacRuleAction,
       "hm2AgentAclMacRuleCos": hm2AgentAclMacRuleCos,
       "hm2AgentAclMacRuleCos2": hm2AgentAclMacRuleCos2,
       "hm2AgentAclMacRuleDestMacAddr": hm2AgentAclMacRuleDestMacAddr,
       "hm2AgentAclMacRuleDestMacMask": hm2AgentAclMacRuleDestMacMask,
       "hm2AgentAclMacRuleEtypeKey": hm2AgentAclMacRuleEtypeKey,
       "hm2AgentAclMacRuleEtypeValue": hm2AgentAclMacRuleEtypeValue,
       "hm2AgentAclMacRuleSrcMacAddr": hm2AgentAclMacRuleSrcMacAddr,
       "hm2AgentAclMacRuleSrcMacMask": hm2AgentAclMacRuleSrcMacMask,
       "hm2AgentAclMacRuleVlanId": hm2AgentAclMacRuleVlanId,
       "hm2AgentAclMacRuleVlanIdRangeStart": hm2AgentAclMacRuleVlanIdRangeStart,
       "hm2AgentAclMacRuleVlanIdRangeEnd": hm2AgentAclMacRuleVlanIdRangeEnd,
       "hm2AgentAclMacRuleVlanId2": hm2AgentAclMacRuleVlanId2,
       "hm2AgentAclMacRuleVlanId2RangeStart": hm2AgentAclMacRuleVlanId2RangeStart,
       "hm2AgentAclMacRuleVlanId2RangeEnd": hm2AgentAclMacRuleVlanId2RangeEnd,
       "hm2AgentAclMacRuleStatus": hm2AgentAclMacRuleStatus,
       "hm2AgentAclMacRuleAssignQueueId": hm2AgentAclMacRuleAssignQueueId,
       "hm2AgentAclMacRuleRedirectIntf": hm2AgentAclMacRuleRedirectIntf,
       "hm2AgentAclMacRuleMatchEvery": hm2AgentAclMacRuleMatchEvery,
       "hm2AgentAclMacRuleMirrorIntf": hm2AgentAclMacRuleMirrorIntf,
       "hm2AgentAclMacRuleLogging": hm2AgentAclMacRuleLogging,
       "hm2AgentAclMacRuleTimeRangeName": hm2AgentAclMacRuleTimeRangeName,
       "hm2AgentAclMacRuleTimeRangeStatus": hm2AgentAclMacRuleTimeRangeStatus,
       "hm2AgentAclMacRuleIndexNextFree": hm2AgentAclMacRuleIndexNextFree,
       "hm2AgentAclMacRuleRateLimitCrateUnit": hm2AgentAclMacRuleRateLimitCrateUnit,
       "hm2AgentAclMacRuleRateLimitCrate": hm2AgentAclMacRuleRateLimitCrate,
       "hm2AgentAclMacRuleRateLimitCburst": hm2AgentAclMacRuleRateLimitCburst,
       "hm2AgentAclMacRuleStatsAction": hm2AgentAclMacRuleStatsAction,
       "hm2AgentAclMacRuleHitCount": hm2AgentAclMacRuleHitCount,
       "hm2AgentAclMacRuleHitCountDiscontinuityTime": hm2AgentAclMacRuleHitCountDiscontinuityTime,
       "hm2AgentAclIfTable": hm2AgentAclIfTable,
       "hm2AgentAclIfEntry": hm2AgentAclIfEntry,
       "hm2AgentAclIfIndex": hm2AgentAclIfIndex,
       "hm2AgentAclIfDirection": hm2AgentAclIfDirection,
       "hm2AgentAclIfSequence": hm2AgentAclIfSequence,
       "hm2AgentAclIfAclType": hm2AgentAclIfAclType,
       "hm2AgentAclIfAclId": hm2AgentAclIfAclId,
       "hm2AgentAclIfStatus": hm2AgentAclIfStatus,
       "hm2AgentAclLoggingGroup": hm2AgentAclLoggingGroup,
       "hm2AgentAclTrapRuleIndex": hm2AgentAclTrapRuleIndex,
       "hm2AgentAclTrapRuleAction": hm2AgentAclTrapRuleAction,
       "hm2AgentAclTrapRuleHitCount": hm2AgentAclTrapRuleHitCount,
       "hm2AgentAclTrapFlag": hm2AgentAclTrapFlag,
       "hm2AgentAclTrapRuleTimeRangeName": hm2AgentAclTrapRuleTimeRangeName,
       "hm2AgentAclTrapRuleTimeRangeNotification": hm2AgentAclTrapRuleTimeRangeNotification,
       "hm2AgentAclTrapRuleInstallationStatus": hm2AgentAclTrapRuleInstallationStatus,
       "hm2AgentAclTrapRuleHitCountHigh": hm2AgentAclTrapRuleHitCountHigh,
       "hm2AgentAclTrapRuleHitCountLow": hm2AgentAclTrapRuleHitCountLow,
       "hm2AgentAclVlanTable": hm2AgentAclVlanTable,
       "hm2AgentAclVlanEntry": hm2AgentAclVlanEntry,
       "hm2AgentAclVlanIndex": hm2AgentAclVlanIndex,
       "hm2AgentAclVlanDirection": hm2AgentAclVlanDirection,
       "hm2AgentAclVlanSequence": hm2AgentAclVlanSequence,
       "hm2AgentAclVlanAclType": hm2AgentAclVlanAclType,
       "hm2AgentAclVlanAclId": hm2AgentAclVlanAclId,
       "hm2AgentAclVlanStatus": hm2AgentAclVlanStatus,
       "hm2AgentAclNamedIpv4IndexNextFree": hm2AgentAclNamedIpv4IndexNextFree,
       "hm2AgentOperatorRuleAssignOutboundInvalid": hm2AgentOperatorRuleAssignOutboundInvalid}
)

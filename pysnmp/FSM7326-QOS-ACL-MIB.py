# SNMP MIB module (FSM7326-QOS-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FSM7326-QOS-ACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:32 2024
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

(fsm7326QOS,) = mibBuilder.importSymbols(
    "FSM7326-QOS-MIB",
    "fsm7326QOS")

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

fsm7326QOSACL = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2)
)
fsm7326QOSACL.setRevisions(
        ("2003-11-10 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AclTable_Object = MibTable
aclTable = _AclTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 1)
)
if mibBuilder.loadTexts:
    aclTable.setStatus("current")
_AclEntry_Object = MibTableRow
aclEntry = _AclEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 1, 1)
)
aclEntry.setIndexNames(
    (0, "FSM7326-QOS-ACL-MIB", "aclIndex"),
)
if mibBuilder.loadTexts:
    aclEntry.setStatus("current")
_AclIndex_Type = Integer32
_AclIndex_Object = MibTableColumn
aclIndex = _AclIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 1, 1, 1),
    _AclIndex_Type()
)
aclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIndex.setStatus("current")
_AclStatus_Type = RowStatus
_AclStatus_Object = MibTableColumn
aclStatus = _AclStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 1, 1, 3),
    _AclStatus_Type()
)
aclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclStatus.setStatus("current")
_AclIfTable_Object = MibTable
aclIfTable = _AclIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 2)
)
if mibBuilder.loadTexts:
    aclIfTable.setStatus("current")
_AclIfEntry_Object = MibTableRow
aclIfEntry = _AclIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 2, 1)
)
aclIfEntry.setIndexNames(
    (0, "FSM7326-QOS-ACL-MIB", "aclIndex"),
    (0, "FSM7326-QOS-ACL-MIB", "aclIfIndex"),
    (0, "FSM7326-QOS-ACL-MIB", "aclIfDirection"),
)
if mibBuilder.loadTexts:
    aclIfEntry.setStatus("current")
_AclIfIndex_Type = Integer32
_AclIfIndex_Object = MibTableColumn
aclIfIndex = _AclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 2, 1, 1),
    _AclIfIndex_Type()
)
aclIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIfIndex.setStatus("current")


class _AclIfDirection_Type(Integer32):
    """Custom type aclIfDirection based on Integer32"""
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


_AclIfDirection_Type.__name__ = "Integer32"
_AclIfDirection_Object = MibTableColumn
aclIfDirection = _AclIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 2, 1, 2),
    _AclIfDirection_Type()
)
aclIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIfDirection.setStatus("current")
_AclIfStatus_Type = RowStatus
_AclIfStatus_Object = MibTableColumn
aclIfStatus = _AclIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 2, 1, 3),
    _AclIfStatus_Type()
)
aclIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIfStatus.setStatus("current")
_AclRuleTable_Object = MibTable
aclRuleTable = _AclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3)
)
if mibBuilder.loadTexts:
    aclRuleTable.setStatus("current")
_AclRuleEntry_Object = MibTableRow
aclRuleEntry = _AclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1)
)
aclRuleEntry.setIndexNames(
    (0, "FSM7326-QOS-ACL-MIB", "aclIndex"),
    (0, "FSM7326-QOS-ACL-MIB", "aclRuleIndex"),
)
if mibBuilder.loadTexts:
    aclRuleEntry.setStatus("current")
_AclRuleIndex_Type = Integer32
_AclRuleIndex_Object = MibTableColumn
aclRuleIndex = _AclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 1),
    _AclRuleIndex_Type()
)
aclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclRuleIndex.setStatus("current")


class _AclRuleAction_Type(Integer32):
    """Custom type aclRuleAction based on Integer32"""
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


_AclRuleAction_Type.__name__ = "Integer32"
_AclRuleAction_Object = MibTableColumn
aclRuleAction = _AclRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 2),
    _AclRuleAction_Type()
)
aclRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleAction.setStatus("current")


class _AclRuleProtocol_Type(Integer32):
    """Custom type aclRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AclRuleProtocol_Type.__name__ = "Integer32"
_AclRuleProtocol_Object = MibTableColumn
aclRuleProtocol = _AclRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 3),
    _AclRuleProtocol_Type()
)
aclRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleProtocol.setStatus("current")
_AclRuleSrcIpAddress_Type = IpAddress
_AclRuleSrcIpAddress_Object = MibTableColumn
aclRuleSrcIpAddress = _AclRuleSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 4),
    _AclRuleSrcIpAddress_Type()
)
aclRuleSrcIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleSrcIpAddress.setStatus("current")
_AclRuleSrcIpMask_Type = IpAddress
_AclRuleSrcIpMask_Object = MibTableColumn
aclRuleSrcIpMask = _AclRuleSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 5),
    _AclRuleSrcIpMask_Type()
)
aclRuleSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleSrcIpMask.setStatus("current")
_AclRuleSrcL4Port_Type = Integer32
_AclRuleSrcL4Port_Object = MibTableColumn
aclRuleSrcL4Port = _AclRuleSrcL4Port_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 6),
    _AclRuleSrcL4Port_Type()
)
aclRuleSrcL4Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleSrcL4Port.setStatus("current")
_AclRuleSrcL4PortRangeStart_Type = Integer32
_AclRuleSrcL4PortRangeStart_Object = MibTableColumn
aclRuleSrcL4PortRangeStart = _AclRuleSrcL4PortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 7),
    _AclRuleSrcL4PortRangeStart_Type()
)
aclRuleSrcL4PortRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleSrcL4PortRangeStart.setStatus("current")
_AclRuleSrcL4PortRangeEnd_Type = Integer32
_AclRuleSrcL4PortRangeEnd_Object = MibTableColumn
aclRuleSrcL4PortRangeEnd = _AclRuleSrcL4PortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 8),
    _AclRuleSrcL4PortRangeEnd_Type()
)
aclRuleSrcL4PortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleSrcL4PortRangeEnd.setStatus("current")
_AclRuleDestIpAddress_Type = IpAddress
_AclRuleDestIpAddress_Object = MibTableColumn
aclRuleDestIpAddress = _AclRuleDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 9),
    _AclRuleDestIpAddress_Type()
)
aclRuleDestIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleDestIpAddress.setStatus("current")
_AclRuleDestIpMask_Type = IpAddress
_AclRuleDestIpMask_Object = MibTableColumn
aclRuleDestIpMask = _AclRuleDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 10),
    _AclRuleDestIpMask_Type()
)
aclRuleDestIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleDestIpMask.setStatus("current")
_AclRuleDestL4Port_Type = Integer32
_AclRuleDestL4Port_Object = MibTableColumn
aclRuleDestL4Port = _AclRuleDestL4Port_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 11),
    _AclRuleDestL4Port_Type()
)
aclRuleDestL4Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleDestL4Port.setStatus("current")
_AclRuleDestL4PortRangeStart_Type = Integer32
_AclRuleDestL4PortRangeStart_Object = MibTableColumn
aclRuleDestL4PortRangeStart = _AclRuleDestL4PortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 12),
    _AclRuleDestL4PortRangeStart_Type()
)
aclRuleDestL4PortRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleDestL4PortRangeStart.setStatus("current")
_AclRuleDestL4PortRangeEnd_Type = Integer32
_AclRuleDestL4PortRangeEnd_Object = MibTableColumn
aclRuleDestL4PortRangeEnd = _AclRuleDestL4PortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 13),
    _AclRuleDestL4PortRangeEnd_Type()
)
aclRuleDestL4PortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleDestL4PortRangeEnd.setStatus("current")
_AclRuleIPDSCP_Type = Integer32
_AclRuleIPDSCP_Object = MibTableColumn
aclRuleIPDSCP = _AclRuleIPDSCP_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 14),
    _AclRuleIPDSCP_Type()
)
aclRuleIPDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleIPDSCP.setStatus("current")
_AclRuleIpPrecedence_Type = Integer32
_AclRuleIpPrecedence_Object = MibTableColumn
aclRuleIpPrecedence = _AclRuleIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 15),
    _AclRuleIpPrecedence_Type()
)
aclRuleIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleIpPrecedence.setStatus("current")
_AclRuleIpTosBits_Type = Integer32
_AclRuleIpTosBits_Object = MibTableColumn
aclRuleIpTosBits = _AclRuleIpTosBits_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 16),
    _AclRuleIpTosBits_Type()
)
aclRuleIpTosBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleIpTosBits.setStatus("current")
_AclRuleIpTosMask_Type = Integer32
_AclRuleIpTosMask_Object = MibTableColumn
aclRuleIpTosMask = _AclRuleIpTosMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 17),
    _AclRuleIpTosMask_Type()
)
aclRuleIpTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleIpTosMask.setStatus("current")
_AclRuleStatus_Type = RowStatus
_AclRuleStatus_Object = MibTableColumn
aclRuleStatus = _AclRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 3, 2, 3, 1, 18),
    _AclRuleStatus_Type()
)
aclRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSM7326-QOS-ACL-MIB",
    **{"fsm7326QOSACL": fsm7326QOSACL,
       "aclTable": aclTable,
       "aclEntry": aclEntry,
       "aclIndex": aclIndex,
       "aclStatus": aclStatus,
       "aclIfTable": aclIfTable,
       "aclIfEntry": aclIfEntry,
       "aclIfIndex": aclIfIndex,
       "aclIfDirection": aclIfDirection,
       "aclIfStatus": aclIfStatus,
       "aclRuleTable": aclRuleTable,
       "aclRuleEntry": aclRuleEntry,
       "aclRuleIndex": aclRuleIndex,
       "aclRuleAction": aclRuleAction,
       "aclRuleProtocol": aclRuleProtocol,
       "aclRuleSrcIpAddress": aclRuleSrcIpAddress,
       "aclRuleSrcIpMask": aclRuleSrcIpMask,
       "aclRuleSrcL4Port": aclRuleSrcL4Port,
       "aclRuleSrcL4PortRangeStart": aclRuleSrcL4PortRangeStart,
       "aclRuleSrcL4PortRangeEnd": aclRuleSrcL4PortRangeEnd,
       "aclRuleDestIpAddress": aclRuleDestIpAddress,
       "aclRuleDestIpMask": aclRuleDestIpMask,
       "aclRuleDestL4Port": aclRuleDestL4Port,
       "aclRuleDestL4PortRangeStart": aclRuleDestL4PortRangeStart,
       "aclRuleDestL4PortRangeEnd": aclRuleDestL4PortRangeEnd,
       "aclRuleIPDSCP": aclRuleIPDSCP,
       "aclRuleIpPrecedence": aclRuleIpPrecedence,
       "aclRuleIpTosBits": aclRuleIpTosBits,
       "aclRuleIpTosMask": aclRuleIpTosMask,
       "aclRuleStatus": aclRuleStatus}
)

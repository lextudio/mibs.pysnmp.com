# SNMP MIB module (HIRSCHMANN-MMP4-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HIRSCHMANN-MMP4-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:40 2024
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

(hmPlatform4,) = mibBuilder.importSymbols(
    "HIRSCHMANN-MMP4-BASICL2-MIB",
    "hmPlatform4")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hmPlatform4QOS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 3)
)
hmPlatform4QOS.setRevisions(
        ("2005-08-18 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EtypeValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )



class PercentByFives(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(35, 35),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(45, 45),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(55, 55),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(65, 65),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(75, 75),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(85, 85),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(95, 95),
        ValueRangeConstraint(100, 100),
    )



class Sixteenths(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



# MIB Managed Objects in the order of their OIDs

_HmAgentQOSACL_ObjectIdentity = ObjectIdentity
hmAgentQOSACL = _HmAgentQOSACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2)
)
_AclTable_Object = MibTable
aclTable = _AclTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 1)
)
if mibBuilder.loadTexts:
    aclTable.setStatus("current")
_AclEntry_Object = MibTableRow
aclEntry = _AclEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 1, 1)
)
aclEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "aclIndex"),
)
if mibBuilder.loadTexts:
    aclEntry.setStatus("current")
_AclIndex_Type = Integer32
_AclIndex_Object = MibTableColumn
aclIndex = _AclIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 1, 1, 1),
    _AclIndex_Type()
)
aclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIndex.setStatus("current")
_AclStatus_Type = RowStatus
_AclStatus_Object = MibTableColumn
aclStatus = _AclStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 1, 1, 3),
    _AclStatus_Type()
)
aclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclStatus.setStatus("current")
_AclRuleTable_Object = MibTable
aclRuleTable = _AclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4)
)
if mibBuilder.loadTexts:
    aclRuleTable.setStatus("current")
_AclRuleEntry_Object = MibTableRow
aclRuleEntry = _AclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1)
)
aclRuleEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "aclIndex"),
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "aclRuleIndex"),
)
if mibBuilder.loadTexts:
    aclRuleEntry.setStatus("current")
_AclRuleIndex_Type = Integer32
_AclRuleIndex_Object = MibTableColumn
aclRuleIndex = _AclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 3),
    _AclRuleProtocol_Type()
)
aclRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleProtocol.setStatus("current")
_AclRuleSrcIpAddress_Type = IpAddress
_AclRuleSrcIpAddress_Object = MibTableColumn
aclRuleSrcIpAddress = _AclRuleSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 4),
    _AclRuleSrcIpAddress_Type()
)
aclRuleSrcIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleSrcIpAddress.setStatus("current")
_AclRuleSrcIpMask_Type = IpAddress
_AclRuleSrcIpMask_Object = MibTableColumn
aclRuleSrcIpMask = _AclRuleSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 5),
    _AclRuleSrcIpMask_Type()
)
aclRuleSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleSrcIpMask.setStatus("current")
_AclRuleSrcL4Port_Type = Integer32
_AclRuleSrcL4Port_Object = MibTableColumn
aclRuleSrcL4Port = _AclRuleSrcL4Port_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 6),
    _AclRuleSrcL4Port_Type()
)
aclRuleSrcL4Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleSrcL4Port.setStatus("current")
_AclRuleSrcL4PortRangeStart_Type = Integer32
_AclRuleSrcL4PortRangeStart_Object = MibTableColumn
aclRuleSrcL4PortRangeStart = _AclRuleSrcL4PortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 7),
    _AclRuleSrcL4PortRangeStart_Type()
)
aclRuleSrcL4PortRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleSrcL4PortRangeStart.setStatus("current")
_AclRuleSrcL4PortRangeEnd_Type = Integer32
_AclRuleSrcL4PortRangeEnd_Object = MibTableColumn
aclRuleSrcL4PortRangeEnd = _AclRuleSrcL4PortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 8),
    _AclRuleSrcL4PortRangeEnd_Type()
)
aclRuleSrcL4PortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleSrcL4PortRangeEnd.setStatus("current")
_AclRuleDestIpAddress_Type = IpAddress
_AclRuleDestIpAddress_Object = MibTableColumn
aclRuleDestIpAddress = _AclRuleDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 9),
    _AclRuleDestIpAddress_Type()
)
aclRuleDestIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleDestIpAddress.setStatus("current")
_AclRuleDestIpMask_Type = IpAddress
_AclRuleDestIpMask_Object = MibTableColumn
aclRuleDestIpMask = _AclRuleDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 10),
    _AclRuleDestIpMask_Type()
)
aclRuleDestIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleDestIpMask.setStatus("current")
_AclRuleDestL4Port_Type = Integer32
_AclRuleDestL4Port_Object = MibTableColumn
aclRuleDestL4Port = _AclRuleDestL4Port_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 11),
    _AclRuleDestL4Port_Type()
)
aclRuleDestL4Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleDestL4Port.setStatus("current")
_AclRuleDestL4PortRangeStart_Type = Integer32
_AclRuleDestL4PortRangeStart_Object = MibTableColumn
aclRuleDestL4PortRangeStart = _AclRuleDestL4PortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 12),
    _AclRuleDestL4PortRangeStart_Type()
)
aclRuleDestL4PortRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleDestL4PortRangeStart.setStatus("current")
_AclRuleDestL4PortRangeEnd_Type = Integer32
_AclRuleDestL4PortRangeEnd_Object = MibTableColumn
aclRuleDestL4PortRangeEnd = _AclRuleDestL4PortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 13),
    _AclRuleDestL4PortRangeEnd_Type()
)
aclRuleDestL4PortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleDestL4PortRangeEnd.setStatus("current")
_AclRuleIPDSCP_Type = Integer32
_AclRuleIPDSCP_Object = MibTableColumn
aclRuleIPDSCP = _AclRuleIPDSCP_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 14),
    _AclRuleIPDSCP_Type()
)
aclRuleIPDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleIPDSCP.setStatus("current")
_AclRuleIpPrecedence_Type = Integer32
_AclRuleIpPrecedence_Object = MibTableColumn
aclRuleIpPrecedence = _AclRuleIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 15),
    _AclRuleIpPrecedence_Type()
)
aclRuleIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleIpPrecedence.setStatus("current")
_AclRuleIpTosBits_Type = Integer32
_AclRuleIpTosBits_Object = MibTableColumn
aclRuleIpTosBits = _AclRuleIpTosBits_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 16),
    _AclRuleIpTosBits_Type()
)
aclRuleIpTosBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleIpTosBits.setStatus("current")
_AclRuleIpTosMask_Type = Integer32
_AclRuleIpTosMask_Object = MibTableColumn
aclRuleIpTosMask = _AclRuleIpTosMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 17),
    _AclRuleIpTosMask_Type()
)
aclRuleIpTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleIpTosMask.setStatus("current")
_AclRuleStatus_Type = RowStatus
_AclRuleStatus_Object = MibTableColumn
aclRuleStatus = _AclRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 18),
    _AclRuleStatus_Type()
)
aclRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleStatus.setStatus("current")
_AclRuleAssignQueueId_Type = Unsigned32
_AclRuleAssignQueueId_Object = MibTableColumn
aclRuleAssignQueueId = _AclRuleAssignQueueId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 19),
    _AclRuleAssignQueueId_Type()
)
aclRuleAssignQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleAssignQueueId.setStatus("current")


class _AclRuleRedirectIntf_Type(InterfaceIndexOrZero):
    """Custom type aclRuleRedirectIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_AclRuleRedirectIntf_Object = MibTableColumn
aclRuleRedirectIntf = _AclRuleRedirectIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 20),
    _AclRuleRedirectIntf_Type()
)
aclRuleRedirectIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleRedirectIntf.setStatus("current")
_AclRuleMatchEvery_Type = TruthValue
_AclRuleMatchEvery_Object = MibTableColumn
aclRuleMatchEvery = _AclRuleMatchEvery_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 4, 1, 21),
    _AclRuleMatchEvery_Type()
)
aclRuleMatchEvery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleMatchEvery.setStatus("current")
_AclMacIndexNextFree_Type = Integer32
_AclMacIndexNextFree_Object = MibScalar
aclMacIndexNextFree = _AclMacIndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 5),
    _AclMacIndexNextFree_Type()
)
aclMacIndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclMacIndexNextFree.setStatus("current")
_AclMacTable_Object = MibTable
aclMacTable = _AclMacTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 6)
)
if mibBuilder.loadTexts:
    aclMacTable.setStatus("current")
_AclMacEntry_Object = MibTableRow
aclMacEntry = _AclMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 6, 1)
)
aclMacEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "aclMacIndex"),
)
if mibBuilder.loadTexts:
    aclMacEntry.setStatus("current")
_AclMacIndex_Type = Integer32
_AclMacIndex_Object = MibTableColumn
aclMacIndex = _AclMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 6, 1, 1),
    _AclMacIndex_Type()
)
aclMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclMacIndex.setStatus("current")


class _AclMacName_Type(DisplayString):
    """Custom type aclMacName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AclMacName_Type.__name__ = "DisplayString"
_AclMacName_Object = MibTableColumn
aclMacName = _AclMacName_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 6, 1, 2),
    _AclMacName_Type()
)
aclMacName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacName.setStatus("current")
_AclMacStatus_Type = RowStatus
_AclMacStatus_Object = MibTableColumn
aclMacStatus = _AclMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 6, 1, 3),
    _AclMacStatus_Type()
)
aclMacStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacStatus.setStatus("current")
_AclMacRuleTable_Object = MibTable
aclMacRuleTable = _AclMacRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7)
)
if mibBuilder.loadTexts:
    aclMacRuleTable.setStatus("current")
_AclMacRuleEntry_Object = MibTableRow
aclMacRuleEntry = _AclMacRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1)
)
aclMacRuleEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "aclMacIndex"),
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "aclMacRuleIndex"),
)
if mibBuilder.loadTexts:
    aclMacRuleEntry.setStatus("current")
_AclMacRuleIndex_Type = Integer32
_AclMacRuleIndex_Object = MibTableColumn
aclMacRuleIndex = _AclMacRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 1),
    _AclMacRuleIndex_Type()
)
aclMacRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclMacRuleIndex.setStatus("current")


class _AclMacRuleAction_Type(Integer32):
    """Custom type aclMacRuleAction based on Integer32"""
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


_AclMacRuleAction_Type.__name__ = "Integer32"
_AclMacRuleAction_Object = MibTableColumn
aclMacRuleAction = _AclMacRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 2),
    _AclMacRuleAction_Type()
)
aclMacRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleAction.setStatus("current")


class _AclMacRuleCos_Type(Unsigned32):
    """Custom type aclMacRuleCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclMacRuleCos_Type.__name__ = "Unsigned32"
_AclMacRuleCos_Object = MibTableColumn
aclMacRuleCos = _AclMacRuleCos_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 3),
    _AclMacRuleCos_Type()
)
aclMacRuleCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleCos.setStatus("current")


class _AclMacRuleCos2_Type(Unsigned32):
    """Custom type aclMacRuleCos2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclMacRuleCos2_Type.__name__ = "Unsigned32"
_AclMacRuleCos2_Object = MibTableColumn
aclMacRuleCos2 = _AclMacRuleCos2_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 4),
    _AclMacRuleCos2_Type()
)
aclMacRuleCos2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleCos2.setStatus("current")
_AclMacRuleDestMacAddr_Type = MacAddress
_AclMacRuleDestMacAddr_Object = MibTableColumn
aclMacRuleDestMacAddr = _AclMacRuleDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 5),
    _AclMacRuleDestMacAddr_Type()
)
aclMacRuleDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleDestMacAddr.setStatus("current")
_AclMacRuleDestMacMask_Type = MacAddress
_AclMacRuleDestMacMask_Object = MibTableColumn
aclMacRuleDestMacMask = _AclMacRuleDestMacMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 6),
    _AclMacRuleDestMacMask_Type()
)
aclMacRuleDestMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleDestMacMask.setStatus("current")


class _AclMacRuleEtypeKey_Type(Integer32):
    """Custom type aclMacRuleEtypeKey based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("appletalk", 2),
          ("arp", 3),
          ("custom", 1),
          ("ibmsna", 4),
          ("ipv4", 5),
          ("ipv6", 6),
          ("ipx", 7),
          ("mplsmcast", 8),
          ("mplsucast", 9),
          ("netbios", 10),
          ("novell", 11),
          ("pppoe", 12),
          ("rarp", 13))
    )


_AclMacRuleEtypeKey_Type.__name__ = "Integer32"
_AclMacRuleEtypeKey_Object = MibTableColumn
aclMacRuleEtypeKey = _AclMacRuleEtypeKey_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 7),
    _AclMacRuleEtypeKey_Type()
)
aclMacRuleEtypeKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleEtypeKey.setStatus("current")
_AclMacRuleEtypeValue_Type = EtypeValue
_AclMacRuleEtypeValue_Object = MibTableColumn
aclMacRuleEtypeValue = _AclMacRuleEtypeValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 8),
    _AclMacRuleEtypeValue_Type()
)
aclMacRuleEtypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleEtypeValue.setStatus("current")
_AclMacRuleSrcMacAddr_Type = MacAddress
_AclMacRuleSrcMacAddr_Object = MibTableColumn
aclMacRuleSrcMacAddr = _AclMacRuleSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 9),
    _AclMacRuleSrcMacAddr_Type()
)
aclMacRuleSrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleSrcMacAddr.setStatus("current")
_AclMacRuleSrcMacMask_Type = MacAddress
_AclMacRuleSrcMacMask_Object = MibTableColumn
aclMacRuleSrcMacMask = _AclMacRuleSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 10),
    _AclMacRuleSrcMacMask_Type()
)
aclMacRuleSrcMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleSrcMacMask.setStatus("current")


class _AclMacRuleVlanId_Type(Unsigned32):
    """Custom type aclMacRuleVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AclMacRuleVlanId_Type.__name__ = "Unsigned32"
_AclMacRuleVlanId_Object = MibTableColumn
aclMacRuleVlanId = _AclMacRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 11),
    _AclMacRuleVlanId_Type()
)
aclMacRuleVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleVlanId.setStatus("current")


class _AclMacRuleVlanIdRangeStart_Type(Unsigned32):
    """Custom type aclMacRuleVlanIdRangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AclMacRuleVlanIdRangeStart_Type.__name__ = "Unsigned32"
_AclMacRuleVlanIdRangeStart_Object = MibTableColumn
aclMacRuleVlanIdRangeStart = _AclMacRuleVlanIdRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 12),
    _AclMacRuleVlanIdRangeStart_Type()
)
aclMacRuleVlanIdRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleVlanIdRangeStart.setStatus("current")


class _AclMacRuleVlanIdRangeEnd_Type(Unsigned32):
    """Custom type aclMacRuleVlanIdRangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AclMacRuleVlanIdRangeEnd_Type.__name__ = "Unsigned32"
_AclMacRuleVlanIdRangeEnd_Object = MibTableColumn
aclMacRuleVlanIdRangeEnd = _AclMacRuleVlanIdRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 13),
    _AclMacRuleVlanIdRangeEnd_Type()
)
aclMacRuleVlanIdRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleVlanIdRangeEnd.setStatus("current")


class _AclMacRuleVlanId2_Type(Unsigned32):
    """Custom type aclMacRuleVlanId2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AclMacRuleVlanId2_Type.__name__ = "Unsigned32"
_AclMacRuleVlanId2_Object = MibTableColumn
aclMacRuleVlanId2 = _AclMacRuleVlanId2_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 14),
    _AclMacRuleVlanId2_Type()
)
aclMacRuleVlanId2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleVlanId2.setStatus("current")


class _AclMacRuleVlanId2RangeStart_Type(Unsigned32):
    """Custom type aclMacRuleVlanId2RangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AclMacRuleVlanId2RangeStart_Type.__name__ = "Unsigned32"
_AclMacRuleVlanId2RangeStart_Object = MibTableColumn
aclMacRuleVlanId2RangeStart = _AclMacRuleVlanId2RangeStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 15),
    _AclMacRuleVlanId2RangeStart_Type()
)
aclMacRuleVlanId2RangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleVlanId2RangeStart.setStatus("current")


class _AclMacRuleVlanId2RangeEnd_Type(Unsigned32):
    """Custom type aclMacRuleVlanId2RangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AclMacRuleVlanId2RangeEnd_Type.__name__ = "Unsigned32"
_AclMacRuleVlanId2RangeEnd_Object = MibTableColumn
aclMacRuleVlanId2RangeEnd = _AclMacRuleVlanId2RangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 16),
    _AclMacRuleVlanId2RangeEnd_Type()
)
aclMacRuleVlanId2RangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleVlanId2RangeEnd.setStatus("current")
_AclMacRuleStatus_Type = RowStatus
_AclMacRuleStatus_Object = MibTableColumn
aclMacRuleStatus = _AclMacRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 17),
    _AclMacRuleStatus_Type()
)
aclMacRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleStatus.setStatus("current")
_AclMacRuleAssignQueueId_Type = Unsigned32
_AclMacRuleAssignQueueId_Object = MibTableColumn
aclMacRuleAssignQueueId = _AclMacRuleAssignQueueId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 18),
    _AclMacRuleAssignQueueId_Type()
)
aclMacRuleAssignQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleAssignQueueId.setStatus("current")


class _AclMacRuleRedirectIntf_Type(InterfaceIndexOrZero):
    """Custom type aclMacRuleRedirectIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_AclMacRuleRedirectIntf_Object = MibTableColumn
aclMacRuleRedirectIntf = _AclMacRuleRedirectIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 19),
    _AclMacRuleRedirectIntf_Type()
)
aclMacRuleRedirectIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleRedirectIntf.setStatus("current")
_AclMacRuleMatchEvery_Type = TruthValue
_AclMacRuleMatchEvery_Object = MibTableColumn
aclMacRuleMatchEvery = _AclMacRuleMatchEvery_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 7, 1, 20),
    _AclMacRuleMatchEvery_Type()
)
aclMacRuleMatchEvery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleMatchEvery.setStatus("current")
_AclIfTable_Object = MibTable
aclIfTable = _AclIfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 8)
)
if mibBuilder.loadTexts:
    aclIfTable.setStatus("current")
_AclIfEntry_Object = MibTableRow
aclIfEntry = _AclIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 8, 1)
)
aclIfEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "aclIfIndex"),
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "aclIfDirection"),
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "aclIfSequence"),
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "aclIfAclType"),
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "aclIfAclId"),
)
if mibBuilder.loadTexts:
    aclIfEntry.setStatus("current")
_AclIfIndex_Type = Integer32
_AclIfIndex_Object = MibTableColumn
aclIfIndex = _AclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 8, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 8, 1, 2),
    _AclIfDirection_Type()
)
aclIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIfDirection.setStatus("current")


class _AclIfSequence_Type(Unsigned32):
    """Custom type aclIfSequence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AclIfSequence_Type.__name__ = "Unsigned32"
_AclIfSequence_Object = MibTableColumn
aclIfSequence = _AclIfSequence_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 8, 1, 3),
    _AclIfSequence_Type()
)
aclIfSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIfSequence.setStatus("current")


class _AclIfAclType_Type(Integer32):
    """Custom type aclIfAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2))
    )


_AclIfAclType_Type.__name__ = "Integer32"
_AclIfAclType_Object = MibTableColumn
aclIfAclType = _AclIfAclType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 8, 1, 4),
    _AclIfAclType_Type()
)
aclIfAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIfAclType.setStatus("current")
_AclIfAclId_Type = Integer32
_AclIfAclId_Object = MibTableColumn
aclIfAclId = _AclIfAclId_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 8, 1, 5),
    _AclIfAclId_Type()
)
aclIfAclId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIfAclId.setStatus("current")
_AclIfStatus_Type = RowStatus
_AclIfStatus_Object = MibTableColumn
aclIfStatus = _AclIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 2, 8, 1, 6),
    _AclIfStatus_Type()
)
aclIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIfStatus.setStatus("current")
_HmAgentQOSCOS_ObjectIdentity = ObjectIdentity
hmAgentQOSCOS = _HmAgentQOSCOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3)
)
_HmAgentCosMapCfgGroup_ObjectIdentity = ObjectIdentity
hmAgentCosMapCfgGroup = _HmAgentCosMapCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 1)
)
_HmAgentCosMapIpPrecTable_Object = MibTable
hmAgentCosMapIpPrecTable = _HmAgentCosMapIpPrecTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hmAgentCosMapIpPrecTable.setStatus("current")
_HmAgentCosMapIpPrecEntry_Object = MibTableRow
hmAgentCosMapIpPrecEntry = _HmAgentCosMapIpPrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 1, 1, 1)
)
hmAgentCosMapIpPrecEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "hmAgentCosMapIpPrecIntfIndex"),
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "hmAgentCosMapIpPrecValue"),
)
if mibBuilder.loadTexts:
    hmAgentCosMapIpPrecEntry.setStatus("current")
_HmAgentCosMapIpPrecIntfIndex_Type = InterfaceIndexOrZero
_HmAgentCosMapIpPrecIntfIndex_Object = MibTableColumn
hmAgentCosMapIpPrecIntfIndex = _HmAgentCosMapIpPrecIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 1, 1, 1, 1),
    _HmAgentCosMapIpPrecIntfIndex_Type()
)
hmAgentCosMapIpPrecIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentCosMapIpPrecIntfIndex.setStatus("current")


class _HmAgentCosMapIpPrecValue_Type(Unsigned32):
    """Custom type hmAgentCosMapIpPrecValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HmAgentCosMapIpPrecValue_Type.__name__ = "Unsigned32"
_HmAgentCosMapIpPrecValue_Object = MibTableColumn
hmAgentCosMapIpPrecValue = _HmAgentCosMapIpPrecValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 1, 1, 1, 2),
    _HmAgentCosMapIpPrecValue_Type()
)
hmAgentCosMapIpPrecValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentCosMapIpPrecValue.setStatus("current")


class _HmAgentCosMapIpPrecTrafficClass_Type(Unsigned32):
    """Custom type hmAgentCosMapIpPrecTrafficClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HmAgentCosMapIpPrecTrafficClass_Type.__name__ = "Unsigned32"
_HmAgentCosMapIpPrecTrafficClass_Object = MibTableColumn
hmAgentCosMapIpPrecTrafficClass = _HmAgentCosMapIpPrecTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 1, 1, 1, 3),
    _HmAgentCosMapIpPrecTrafficClass_Type()
)
hmAgentCosMapIpPrecTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentCosMapIpPrecTrafficClass.setStatus("current")
_HmAgentCosMapIpDscpTable_Object = MibTable
hmAgentCosMapIpDscpTable = _HmAgentCosMapIpDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hmAgentCosMapIpDscpTable.setStatus("current")
_HmAgentCosMapIpDscpEntry_Object = MibTableRow
hmAgentCosMapIpDscpEntry = _HmAgentCosMapIpDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 1, 2, 1)
)
hmAgentCosMapIpDscpEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "hmAgentCosMapIpDscpIntfIndex"),
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "hmAgentCosMapIpDscpValue"),
)
if mibBuilder.loadTexts:
    hmAgentCosMapIpDscpEntry.setStatus("current")
_HmAgentCosMapIpDscpIntfIndex_Type = InterfaceIndexOrZero
_HmAgentCosMapIpDscpIntfIndex_Object = MibTableColumn
hmAgentCosMapIpDscpIntfIndex = _HmAgentCosMapIpDscpIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 1, 2, 1, 1),
    _HmAgentCosMapIpDscpIntfIndex_Type()
)
hmAgentCosMapIpDscpIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentCosMapIpDscpIntfIndex.setStatus("current")


class _HmAgentCosMapIpDscpValue_Type(Unsigned32):
    """Custom type hmAgentCosMapIpDscpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HmAgentCosMapIpDscpValue_Type.__name__ = "Unsigned32"
_HmAgentCosMapIpDscpValue_Object = MibTableColumn
hmAgentCosMapIpDscpValue = _HmAgentCosMapIpDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 1, 2, 1, 2),
    _HmAgentCosMapIpDscpValue_Type()
)
hmAgentCosMapIpDscpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentCosMapIpDscpValue.setStatus("current")


class _HmAgentCosMapIpDscpTrafficClass_Type(Unsigned32):
    """Custom type hmAgentCosMapIpDscpTrafficClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HmAgentCosMapIpDscpTrafficClass_Type.__name__ = "Unsigned32"
_HmAgentCosMapIpDscpTrafficClass_Object = MibTableColumn
hmAgentCosMapIpDscpTrafficClass = _HmAgentCosMapIpDscpTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 1, 2, 1, 3),
    _HmAgentCosMapIpDscpTrafficClass_Type()
)
hmAgentCosMapIpDscpTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentCosMapIpDscpTrafficClass.setStatus("current")
_HmAgentCosMapIntfTrustTable_Object = MibTable
hmAgentCosMapIntfTrustTable = _HmAgentCosMapIntfTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hmAgentCosMapIntfTrustTable.setStatus("current")
_HmAgentCosMapIntfTrustEntry_Object = MibTableRow
hmAgentCosMapIntfTrustEntry = _HmAgentCosMapIntfTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 1, 3, 1)
)
hmAgentCosMapIntfTrustEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "hmAgentCosMapIntfTrustIntfIndex"),
)
if mibBuilder.loadTexts:
    hmAgentCosMapIntfTrustEntry.setStatus("current")
_HmAgentCosMapIntfTrustIntfIndex_Type = InterfaceIndexOrZero
_HmAgentCosMapIntfTrustIntfIndex_Object = MibTableColumn
hmAgentCosMapIntfTrustIntfIndex = _HmAgentCosMapIntfTrustIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 1, 3, 1, 1),
    _HmAgentCosMapIntfTrustIntfIndex_Type()
)
hmAgentCosMapIntfTrustIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentCosMapIntfTrustIntfIndex.setStatus("current")


class _HmAgentCosMapIntfTrustMode_Type(Integer32):
    """Custom type hmAgentCosMapIntfTrustMode based on Integer32"""
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
        *(("trustDot1p", 2),
          ("trustIpDscp", 4),
          ("trustIpPrecedence", 3),
          ("untrusted", 1))
    )


_HmAgentCosMapIntfTrustMode_Type.__name__ = "Integer32"
_HmAgentCosMapIntfTrustMode_Object = MibTableColumn
hmAgentCosMapIntfTrustMode = _HmAgentCosMapIntfTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 1, 3, 1, 2),
    _HmAgentCosMapIntfTrustMode_Type()
)
hmAgentCosMapIntfTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentCosMapIntfTrustMode.setStatus("current")
_HmAgentCosMapUntrustedTrafficClass_Type = Unsigned32
_HmAgentCosMapUntrustedTrafficClass_Object = MibTableColumn
hmAgentCosMapUntrustedTrafficClass = _HmAgentCosMapUntrustedTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 1, 3, 1, 3),
    _HmAgentCosMapUntrustedTrafficClass_Type()
)
hmAgentCosMapUntrustedTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentCosMapUntrustedTrafficClass.setStatus("current")
_HmAgentCosQueueCfgGroup_ObjectIdentity = ObjectIdentity
hmAgentCosQueueCfgGroup = _HmAgentCosQueueCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 2)
)
_HmAgentCosQueueNumQueuesPerPort_Type = Unsigned32
_HmAgentCosQueueNumQueuesPerPort_Object = MibScalar
hmAgentCosQueueNumQueuesPerPort = _HmAgentCosQueueNumQueuesPerPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 2, 1),
    _HmAgentCosQueueNumQueuesPerPort_Type()
)
hmAgentCosQueueNumQueuesPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentCosQueueNumQueuesPerPort.setStatus("current")
_HmAgentCosQueueNumDropPrecedenceLevels_Type = Unsigned32
_HmAgentCosQueueNumDropPrecedenceLevels_Object = MibScalar
hmAgentCosQueueNumDropPrecedenceLevels = _HmAgentCosQueueNumDropPrecedenceLevels_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 2, 2),
    _HmAgentCosQueueNumDropPrecedenceLevels_Type()
)
hmAgentCosQueueNumDropPrecedenceLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentCosQueueNumDropPrecedenceLevels.setStatus("current")
_HmAgentCosQueueControlTable_Object = MibTable
hmAgentCosQueueControlTable = _HmAgentCosQueueControlTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 2, 3)
)
if mibBuilder.loadTexts:
    hmAgentCosQueueControlTable.setStatus("current")
_HmAgentCosQueueControlEntry_Object = MibTableRow
hmAgentCosQueueControlEntry = _HmAgentCosQueueControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 2, 3, 1)
)
hmAgentCosQueueControlEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "hmAgentCosQueueIntfIndex"),
)
if mibBuilder.loadTexts:
    hmAgentCosQueueControlEntry.setStatus("current")
_HmAgentCosQueueIntfIndex_Type = InterfaceIndexOrZero
_HmAgentCosQueueIntfIndex_Object = MibTableColumn
hmAgentCosQueueIntfIndex = _HmAgentCosQueueIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 2, 3, 1, 1),
    _HmAgentCosQueueIntfIndex_Type()
)
hmAgentCosQueueIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentCosQueueIntfIndex.setStatus("current")


class _HmAgentCosQueueIntfShapingRate_Type(Unsigned32):
    """Custom type hmAgentCosQueueIntfShapingRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HmAgentCosQueueIntfShapingRate_Type.__name__ = "Unsigned32"
_HmAgentCosQueueIntfShapingRate_Object = MibTableColumn
hmAgentCosQueueIntfShapingRate = _HmAgentCosQueueIntfShapingRate_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 2, 3, 1, 2),
    _HmAgentCosQueueIntfShapingRate_Type()
)
hmAgentCosQueueIntfShapingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentCosQueueIntfShapingRate.setStatus("current")


class _HmAgentCosQueueMgmtTypeIntf_Type(Integer32):
    """Custom type hmAgentCosQueueMgmtTypeIntf based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("taildrop", 1),
          ("wred", 2))
    )


_HmAgentCosQueueMgmtTypeIntf_Type.__name__ = "Integer32"
_HmAgentCosQueueMgmtTypeIntf_Object = MibTableColumn
hmAgentCosQueueMgmtTypeIntf = _HmAgentCosQueueMgmtTypeIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 2, 3, 1, 3),
    _HmAgentCosQueueMgmtTypeIntf_Type()
)
hmAgentCosQueueMgmtTypeIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentCosQueueMgmtTypeIntf.setStatus("current")


class _HmAgentCosQueueWredDecayExponent_Type(Unsigned32):
    """Custom type hmAgentCosQueueWredDecayExponent based on Unsigned32"""
    defaultValue = 9

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HmAgentCosQueueWredDecayExponent_Type.__name__ = "Unsigned32"
_HmAgentCosQueueWredDecayExponent_Object = MibTableColumn
hmAgentCosQueueWredDecayExponent = _HmAgentCosQueueWredDecayExponent_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 2, 3, 1, 4),
    _HmAgentCosQueueWredDecayExponent_Type()
)
hmAgentCosQueueWredDecayExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentCosQueueWredDecayExponent.setStatus("current")


class _HmAgentCosQueueDefaultsRestore_Type(Integer32):
    """Custom type hmAgentCosQueueDefaultsRestore based on Integer32"""
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


_HmAgentCosQueueDefaultsRestore_Type.__name__ = "Integer32"
_HmAgentCosQueueDefaultsRestore_Object = MibTableColumn
hmAgentCosQueueDefaultsRestore = _HmAgentCosQueueDefaultsRestore_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 2, 3, 1, 5),
    _HmAgentCosQueueDefaultsRestore_Type()
)
hmAgentCosQueueDefaultsRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentCosQueueDefaultsRestore.setStatus("current")
_HmAgentCosQueueTable_Object = MibTable
hmAgentCosQueueTable = _HmAgentCosQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 2, 4)
)
if mibBuilder.loadTexts:
    hmAgentCosQueueTable.setStatus("current")
_HmAgentCosQueueEntry_Object = MibTableRow
hmAgentCosQueueEntry = _HmAgentCosQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 2, 4, 1)
)
hmAgentCosQueueEntry.setIndexNames(
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "hmAgentCosQueueIntfIndex"),
    (0, "HIRSCHMANN-MMP4-QOS-MIB", "hmAgentCosQueueIndex"),
)
if mibBuilder.loadTexts:
    hmAgentCosQueueEntry.setStatus("current")
_HmAgentCosQueueIndex_Type = Unsigned32
_HmAgentCosQueueIndex_Object = MibTableColumn
hmAgentCosQueueIndex = _HmAgentCosQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 2, 4, 1, 1),
    _HmAgentCosQueueIndex_Type()
)
hmAgentCosQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmAgentCosQueueIndex.setStatus("current")


class _HmAgentCosQueueSchedulerType_Type(Integer32):
    """Custom type hmAgentCosQueueSchedulerType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("weighted", 2))
    )


_HmAgentCosQueueSchedulerType_Type.__name__ = "Integer32"
_HmAgentCosQueueSchedulerType_Object = MibTableColumn
hmAgentCosQueueSchedulerType = _HmAgentCosQueueSchedulerType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 2, 4, 1, 2),
    _HmAgentCosQueueSchedulerType_Type()
)
hmAgentCosQueueSchedulerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentCosQueueSchedulerType.setStatus("current")


class _HmAgentCosQueueMinBandwidth_Type(Unsigned32):
    """Custom type hmAgentCosQueueMinBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HmAgentCosQueueMinBandwidth_Type.__name__ = "Unsigned32"
_HmAgentCosQueueMinBandwidth_Object = MibTableColumn
hmAgentCosQueueMinBandwidth = _HmAgentCosQueueMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 2, 4, 1, 3),
    _HmAgentCosQueueMinBandwidth_Type()
)
hmAgentCosQueueMinBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentCosQueueMinBandwidth.setStatus("current")


class _HmAgentCosQueueMaxBandwidth_Type(Unsigned32):
    """Custom type hmAgentCosQueueMaxBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HmAgentCosQueueMaxBandwidth_Type.__name__ = "Unsigned32"
_HmAgentCosQueueMaxBandwidth_Object = MibTableColumn
hmAgentCosQueueMaxBandwidth = _HmAgentCosQueueMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 2, 4, 1, 4),
    _HmAgentCosQueueMaxBandwidth_Type()
)
hmAgentCosQueueMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentCosQueueMaxBandwidth.setStatus("current")


class _HmAgentCosQueueMgmtType_Type(Integer32):
    """Custom type hmAgentCosQueueMgmtType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("taildrop", 1),
          ("wred", 2))
    )


_HmAgentCosQueueMgmtType_Type.__name__ = "Integer32"
_HmAgentCosQueueMgmtType_Object = MibTableColumn
hmAgentCosQueueMgmtType = _HmAgentCosQueueMgmtType_Object(
    (1, 3, 6, 1, 4, 1, 248, 15, 3, 3, 2, 4, 1, 5),
    _HmAgentCosQueueMgmtType_Type()
)
hmAgentCosQueueMgmtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentCosQueueMgmtType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIRSCHMANN-MMP4-QOS-MIB",
    **{"EtypeValue": EtypeValue,
       "PercentByFives": PercentByFives,
       "Sixteenths": Sixteenths,
       "hmPlatform4QOS": hmPlatform4QOS,
       "hmAgentQOSACL": hmAgentQOSACL,
       "aclTable": aclTable,
       "aclEntry": aclEntry,
       "aclIndex": aclIndex,
       "aclStatus": aclStatus,
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
       "aclRuleStatus": aclRuleStatus,
       "aclRuleAssignQueueId": aclRuleAssignQueueId,
       "aclRuleRedirectIntf": aclRuleRedirectIntf,
       "aclRuleMatchEvery": aclRuleMatchEvery,
       "aclMacIndexNextFree": aclMacIndexNextFree,
       "aclMacTable": aclMacTable,
       "aclMacEntry": aclMacEntry,
       "aclMacIndex": aclMacIndex,
       "aclMacName": aclMacName,
       "aclMacStatus": aclMacStatus,
       "aclMacRuleTable": aclMacRuleTable,
       "aclMacRuleEntry": aclMacRuleEntry,
       "aclMacRuleIndex": aclMacRuleIndex,
       "aclMacRuleAction": aclMacRuleAction,
       "aclMacRuleCos": aclMacRuleCos,
       "aclMacRuleCos2": aclMacRuleCos2,
       "aclMacRuleDestMacAddr": aclMacRuleDestMacAddr,
       "aclMacRuleDestMacMask": aclMacRuleDestMacMask,
       "aclMacRuleEtypeKey": aclMacRuleEtypeKey,
       "aclMacRuleEtypeValue": aclMacRuleEtypeValue,
       "aclMacRuleSrcMacAddr": aclMacRuleSrcMacAddr,
       "aclMacRuleSrcMacMask": aclMacRuleSrcMacMask,
       "aclMacRuleVlanId": aclMacRuleVlanId,
       "aclMacRuleVlanIdRangeStart": aclMacRuleVlanIdRangeStart,
       "aclMacRuleVlanIdRangeEnd": aclMacRuleVlanIdRangeEnd,
       "aclMacRuleVlanId2": aclMacRuleVlanId2,
       "aclMacRuleVlanId2RangeStart": aclMacRuleVlanId2RangeStart,
       "aclMacRuleVlanId2RangeEnd": aclMacRuleVlanId2RangeEnd,
       "aclMacRuleStatus": aclMacRuleStatus,
       "aclMacRuleAssignQueueId": aclMacRuleAssignQueueId,
       "aclMacRuleRedirectIntf": aclMacRuleRedirectIntf,
       "aclMacRuleMatchEvery": aclMacRuleMatchEvery,
       "aclIfTable": aclIfTable,
       "aclIfEntry": aclIfEntry,
       "aclIfIndex": aclIfIndex,
       "aclIfDirection": aclIfDirection,
       "aclIfSequence": aclIfSequence,
       "aclIfAclType": aclIfAclType,
       "aclIfAclId": aclIfAclId,
       "aclIfStatus": aclIfStatus,
       "hmAgentQOSCOS": hmAgentQOSCOS,
       "hmAgentCosMapCfgGroup": hmAgentCosMapCfgGroup,
       "hmAgentCosMapIpPrecTable": hmAgentCosMapIpPrecTable,
       "hmAgentCosMapIpPrecEntry": hmAgentCosMapIpPrecEntry,
       "hmAgentCosMapIpPrecIntfIndex": hmAgentCosMapIpPrecIntfIndex,
       "hmAgentCosMapIpPrecValue": hmAgentCosMapIpPrecValue,
       "hmAgentCosMapIpPrecTrafficClass": hmAgentCosMapIpPrecTrafficClass,
       "hmAgentCosMapIpDscpTable": hmAgentCosMapIpDscpTable,
       "hmAgentCosMapIpDscpEntry": hmAgentCosMapIpDscpEntry,
       "hmAgentCosMapIpDscpIntfIndex": hmAgentCosMapIpDscpIntfIndex,
       "hmAgentCosMapIpDscpValue": hmAgentCosMapIpDscpValue,
       "hmAgentCosMapIpDscpTrafficClass": hmAgentCosMapIpDscpTrafficClass,
       "hmAgentCosMapIntfTrustTable": hmAgentCosMapIntfTrustTable,
       "hmAgentCosMapIntfTrustEntry": hmAgentCosMapIntfTrustEntry,
       "hmAgentCosMapIntfTrustIntfIndex": hmAgentCosMapIntfTrustIntfIndex,
       "hmAgentCosMapIntfTrustMode": hmAgentCosMapIntfTrustMode,
       "hmAgentCosMapUntrustedTrafficClass": hmAgentCosMapUntrustedTrafficClass,
       "hmAgentCosQueueCfgGroup": hmAgentCosQueueCfgGroup,
       "hmAgentCosQueueNumQueuesPerPort": hmAgentCosQueueNumQueuesPerPort,
       "hmAgentCosQueueNumDropPrecedenceLevels": hmAgentCosQueueNumDropPrecedenceLevels,
       "hmAgentCosQueueControlTable": hmAgentCosQueueControlTable,
       "hmAgentCosQueueControlEntry": hmAgentCosQueueControlEntry,
       "hmAgentCosQueueIntfIndex": hmAgentCosQueueIntfIndex,
       "hmAgentCosQueueIntfShapingRate": hmAgentCosQueueIntfShapingRate,
       "hmAgentCosQueueMgmtTypeIntf": hmAgentCosQueueMgmtTypeIntf,
       "hmAgentCosQueueWredDecayExponent": hmAgentCosQueueWredDecayExponent,
       "hmAgentCosQueueDefaultsRestore": hmAgentCosQueueDefaultsRestore,
       "hmAgentCosQueueTable": hmAgentCosQueueTable,
       "hmAgentCosQueueEntry": hmAgentCosQueueEntry,
       "hmAgentCosQueueIndex": hmAgentCosQueueIndex,
       "hmAgentCosQueueSchedulerType": hmAgentCosQueueSchedulerType,
       "hmAgentCosQueueMinBandwidth": hmAgentCosQueueMinBandwidth,
       "hmAgentCosQueueMaxBandwidth": hmAgentCosQueueMaxBandwidth,
       "hmAgentCosQueueMgmtType": hmAgentCosQueueMgmtType}
)

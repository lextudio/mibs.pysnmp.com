# SNMP MIB module (FASTPATH-QOS-DIFFSERV-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FASTPATH-QOS-DIFFSERV-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:07 2024
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

(fastPathQOS,) = mibBuilder.importSymbols(
    "FASTPATH-QOS-MIB",
    "fastPathQOS")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetPortNumber")

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
 PhysAddress,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fastPathQOSDiffServPrivate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7)
)
fastPathQOSDiffServPrivate.setRevisions(
        ("2007-11-12 00:00",
         "2007-05-23 00:00",
         "2005-06-23 00:00",
         "2004-10-06 00:00",
         "2003-11-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class QosBurstSize(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )



class IntfDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )



class EtypeValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )



class Ipv6AddressPrefix(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



# MIB Managed Objects in the order of their OIDs

_AgentDiffServGenStatusGroup_ObjectIdentity = ObjectIdentity
agentDiffServGenStatusGroup = _AgentDiffServGenStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 1)
)


class _AgentDiffServGenStatusAdminMode_Type(Integer32):
    """Custom type agentDiffServGenStatusAdminMode based on Integer32"""
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


_AgentDiffServGenStatusAdminMode_Type.__name__ = "Integer32"
_AgentDiffServGenStatusAdminMode_Object = MibScalar
agentDiffServGenStatusAdminMode = _AgentDiffServGenStatusAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 1, 1),
    _AgentDiffServGenStatusAdminMode_Type()
)
agentDiffServGenStatusAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDiffServGenStatusAdminMode.setStatus("current")
_AgentDiffServGenStatusClassTableSize_Type = Unsigned32
_AgentDiffServGenStatusClassTableSize_Object = MibScalar
agentDiffServGenStatusClassTableSize = _AgentDiffServGenStatusClassTableSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 1, 2),
    _AgentDiffServGenStatusClassTableSize_Type()
)
agentDiffServGenStatusClassTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServGenStatusClassTableSize.setStatus("current")
_AgentDiffServGenStatusClassTableMax_Type = Unsigned32
_AgentDiffServGenStatusClassTableMax_Object = MibScalar
agentDiffServGenStatusClassTableMax = _AgentDiffServGenStatusClassTableMax_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 1, 3),
    _AgentDiffServGenStatusClassTableMax_Type()
)
agentDiffServGenStatusClassTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServGenStatusClassTableMax.setStatus("current")
_AgentDiffServGenStatusClassRuleTableSize_Type = Unsigned32
_AgentDiffServGenStatusClassRuleTableSize_Object = MibScalar
agentDiffServGenStatusClassRuleTableSize = _AgentDiffServGenStatusClassRuleTableSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 1, 4),
    _AgentDiffServGenStatusClassRuleTableSize_Type()
)
agentDiffServGenStatusClassRuleTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServGenStatusClassRuleTableSize.setStatus("current")
_AgentDiffServGenStatusClassRuleTableMax_Type = Unsigned32
_AgentDiffServGenStatusClassRuleTableMax_Object = MibScalar
agentDiffServGenStatusClassRuleTableMax = _AgentDiffServGenStatusClassRuleTableMax_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 1, 5),
    _AgentDiffServGenStatusClassRuleTableMax_Type()
)
agentDiffServGenStatusClassRuleTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServGenStatusClassRuleTableMax.setStatus("current")
_AgentDiffServGenStatusPolicyTableSize_Type = Unsigned32
_AgentDiffServGenStatusPolicyTableSize_Object = MibScalar
agentDiffServGenStatusPolicyTableSize = _AgentDiffServGenStatusPolicyTableSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 1, 6),
    _AgentDiffServGenStatusPolicyTableSize_Type()
)
agentDiffServGenStatusPolicyTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServGenStatusPolicyTableSize.setStatus("current")
_AgentDiffServGenStatusPolicyTableMax_Type = Unsigned32
_AgentDiffServGenStatusPolicyTableMax_Object = MibScalar
agentDiffServGenStatusPolicyTableMax = _AgentDiffServGenStatusPolicyTableMax_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 1, 7),
    _AgentDiffServGenStatusPolicyTableMax_Type()
)
agentDiffServGenStatusPolicyTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServGenStatusPolicyTableMax.setStatus("current")
_AgentDiffServGenStatusPolicyInstTableSize_Type = Unsigned32
_AgentDiffServGenStatusPolicyInstTableSize_Object = MibScalar
agentDiffServGenStatusPolicyInstTableSize = _AgentDiffServGenStatusPolicyInstTableSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 1, 8),
    _AgentDiffServGenStatusPolicyInstTableSize_Type()
)
agentDiffServGenStatusPolicyInstTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServGenStatusPolicyInstTableSize.setStatus("current")
_AgentDiffServGenStatusPolicyInstTableMax_Type = Unsigned32
_AgentDiffServGenStatusPolicyInstTableMax_Object = MibScalar
agentDiffServGenStatusPolicyInstTableMax = _AgentDiffServGenStatusPolicyInstTableMax_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 1, 9),
    _AgentDiffServGenStatusPolicyInstTableMax_Type()
)
agentDiffServGenStatusPolicyInstTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServGenStatusPolicyInstTableMax.setStatus("current")
_AgentDiffServGenStatusPolicyAttrTableSize_Type = Unsigned32
_AgentDiffServGenStatusPolicyAttrTableSize_Object = MibScalar
agentDiffServGenStatusPolicyAttrTableSize = _AgentDiffServGenStatusPolicyAttrTableSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 1, 10),
    _AgentDiffServGenStatusPolicyAttrTableSize_Type()
)
agentDiffServGenStatusPolicyAttrTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServGenStatusPolicyAttrTableSize.setStatus("current")
_AgentDiffServGenStatusPolicyAttrTableMax_Type = Unsigned32
_AgentDiffServGenStatusPolicyAttrTableMax_Object = MibScalar
agentDiffServGenStatusPolicyAttrTableMax = _AgentDiffServGenStatusPolicyAttrTableMax_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 1, 11),
    _AgentDiffServGenStatusPolicyAttrTableMax_Type()
)
agentDiffServGenStatusPolicyAttrTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServGenStatusPolicyAttrTableMax.setStatus("current")
_AgentDiffServGenStatusServiceTableSize_Type = Unsigned32
_AgentDiffServGenStatusServiceTableSize_Object = MibScalar
agentDiffServGenStatusServiceTableSize = _AgentDiffServGenStatusServiceTableSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 1, 12),
    _AgentDiffServGenStatusServiceTableSize_Type()
)
agentDiffServGenStatusServiceTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServGenStatusServiceTableSize.setStatus("current")
_AgentDiffServGenStatusServiceTableMax_Type = Unsigned32
_AgentDiffServGenStatusServiceTableMax_Object = MibScalar
agentDiffServGenStatusServiceTableMax = _AgentDiffServGenStatusServiceTableMax_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 1, 13),
    _AgentDiffServGenStatusServiceTableMax_Type()
)
agentDiffServGenStatusServiceTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServGenStatusServiceTableMax.setStatus("current")
_AgentDiffServClassGroup_ObjectIdentity = ObjectIdentity
agentDiffServClassGroup = _AgentDiffServClassGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2)
)
_AgentDiffServClassIndexNextFree_Type = Unsigned32
_AgentDiffServClassIndexNextFree_Object = MibScalar
agentDiffServClassIndexNextFree = _AgentDiffServClassIndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 1),
    _AgentDiffServClassIndexNextFree_Type()
)
agentDiffServClassIndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServClassIndexNextFree.setStatus("current")
_AgentDiffServClassTable_Object = MibTable
agentDiffServClassTable = _AgentDiffServClassTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 2)
)
if mibBuilder.loadTexts:
    agentDiffServClassTable.setStatus("current")
_AgentDiffServClassEntry_Object = MibTableRow
agentDiffServClassEntry = _AgentDiffServClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 2, 1)
)
agentDiffServClassEntry.setIndexNames(
    (0, "FASTPATH-QOS-DIFFSERV-PRIVATE-MIB", "agentDiffServClassIndex"),
)
if mibBuilder.loadTexts:
    agentDiffServClassEntry.setStatus("current")
_AgentDiffServClassIndex_Type = Unsigned32
_AgentDiffServClassIndex_Object = MibTableColumn
agentDiffServClassIndex = _AgentDiffServClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 2, 1, 1),
    _AgentDiffServClassIndex_Type()
)
agentDiffServClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDiffServClassIndex.setStatus("current")


class _AgentDiffServClassName_Type(DisplayString):
    """Custom type agentDiffServClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AgentDiffServClassName_Type.__name__ = "DisplayString"
_AgentDiffServClassName_Object = MibTableColumn
agentDiffServClassName = _AgentDiffServClassName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 2, 1, 2),
    _AgentDiffServClassName_Type()
)
agentDiffServClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassName.setStatus("current")


class _AgentDiffServClassType_Type(Integer32):
    """Custom type agentDiffServClassType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acl", 3),
          ("all", 1),
          ("any", 2))
    )


_AgentDiffServClassType_Type.__name__ = "Integer32"
_AgentDiffServClassType_Object = MibTableColumn
agentDiffServClassType = _AgentDiffServClassType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 2, 1, 3),
    _AgentDiffServClassType_Type()
)
agentDiffServClassType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassType.setStatus("current")
_AgentDiffServClassAclNum_Type = Unsigned32
_AgentDiffServClassAclNum_Object = MibTableColumn
agentDiffServClassAclNum = _AgentDiffServClassAclNum_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 2, 1, 4),
    _AgentDiffServClassAclNum_Type()
)
agentDiffServClassAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassAclNum.setStatus("current")
_AgentDiffServClassRuleIndexNextFree_Type = Unsigned32
_AgentDiffServClassRuleIndexNextFree_Object = MibTableColumn
agentDiffServClassRuleIndexNextFree = _AgentDiffServClassRuleIndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 2, 1, 5),
    _AgentDiffServClassRuleIndexNextFree_Type()
)
agentDiffServClassRuleIndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServClassRuleIndexNextFree.setStatus("current")


class _AgentDiffServClassStorageType_Type(StorageType):
    """Custom type agentDiffServClassStorageType based on StorageType"""


_AgentDiffServClassStorageType_Object = MibTableColumn
agentDiffServClassStorageType = _AgentDiffServClassStorageType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 2, 1, 6),
    _AgentDiffServClassStorageType_Type()
)
agentDiffServClassStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassStorageType.setStatus("current")
_AgentDiffServClassRowStatus_Type = RowStatus
_AgentDiffServClassRowStatus_Object = MibTableColumn
agentDiffServClassRowStatus = _AgentDiffServClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 2, 1, 7),
    _AgentDiffServClassRowStatus_Type()
)
agentDiffServClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRowStatus.setStatus("current")


class _AgentDiffServClassAclType_Type(Integer32):
    """Custom type agentDiffServClassAclType based on Integer32"""
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


_AgentDiffServClassAclType_Type.__name__ = "Integer32"
_AgentDiffServClassAclType_Object = MibTableColumn
agentDiffServClassAclType = _AgentDiffServClassAclType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 2, 1, 8),
    _AgentDiffServClassAclType_Type()
)
agentDiffServClassAclType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassAclType.setStatus("current")


class _AgentDiffServClassProtoType_Type(Integer32):
    """Custom type agentDiffServClassProtoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AgentDiffServClassProtoType_Type.__name__ = "Integer32"
_AgentDiffServClassProtoType_Object = MibTableColumn
agentDiffServClassProtoType = _AgentDiffServClassProtoType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 2, 1, 9),
    _AgentDiffServClassProtoType_Type()
)
agentDiffServClassProtoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassProtoType.setStatus("current")
_AgentDiffServClassRuleTable_Object = MibTable
agentDiffServClassRuleTable = _AgentDiffServClassRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3)
)
if mibBuilder.loadTexts:
    agentDiffServClassRuleTable.setStatus("current")
_AgentDiffServClassRuleEntry_Object = MibTableRow
agentDiffServClassRuleEntry = _AgentDiffServClassRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1)
)
agentDiffServClassRuleEntry.setIndexNames(
    (0, "FASTPATH-QOS-DIFFSERV-PRIVATE-MIB", "agentDiffServClassIndex"),
    (0, "FASTPATH-QOS-DIFFSERV-PRIVATE-MIB", "agentDiffServClassRuleIndex"),
)
if mibBuilder.loadTexts:
    agentDiffServClassRuleEntry.setStatus("current")
_AgentDiffServClassRuleIndex_Type = Unsigned32
_AgentDiffServClassRuleIndex_Object = MibTableColumn
agentDiffServClassRuleIndex = _AgentDiffServClassRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 1),
    _AgentDiffServClassRuleIndex_Type()
)
agentDiffServClassRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDiffServClassRuleIndex.setStatus("current")


class _AgentDiffServClassRuleMatchEntryType_Type(Integer32):
    """Custom type agentDiffServClassRuleMatchEntryType based on Integer32"""
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
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("cos", 1),
          ("cos2", 15),
          ("dstPrefix", 21),
          ("dstip", 2),
          ("dstl4port", 3),
          ("dstmac", 4),
          ("etype", 16),
          ("every", 5),
          ("flowLabel", 19),
          ("ipdscp", 6),
          ("ipprecedence", 7),
          ("iptos", 8),
          ("protocol", 9),
          ("refclass", 10),
          ("srcPrefix", 20),
          ("srcip", 11),
          ("srcl4port", 12),
          ("srcmac", 13),
          ("vlan", 14),
          ("vlanid", 17),
          ("vlanid2", 18))
    )


_AgentDiffServClassRuleMatchEntryType_Type.__name__ = "Integer32"
_AgentDiffServClassRuleMatchEntryType_Object = MibTableColumn
agentDiffServClassRuleMatchEntryType = _AgentDiffServClassRuleMatchEntryType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 2),
    _AgentDiffServClassRuleMatchEntryType_Type()
)
agentDiffServClassRuleMatchEntryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchEntryType.setStatus("current")


class _AgentDiffServClassRuleMatchCos_Type(Unsigned32):
    """Custom type agentDiffServClassRuleMatchCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentDiffServClassRuleMatchCos_Type.__name__ = "Unsigned32"
_AgentDiffServClassRuleMatchCos_Object = MibTableColumn
agentDiffServClassRuleMatchCos = _AgentDiffServClassRuleMatchCos_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 3),
    _AgentDiffServClassRuleMatchCos_Type()
)
agentDiffServClassRuleMatchCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchCos.setStatus("current")
_AgentDiffServClassRuleMatchDstIpAddr_Type = IpAddress
_AgentDiffServClassRuleMatchDstIpAddr_Object = MibTableColumn
agentDiffServClassRuleMatchDstIpAddr = _AgentDiffServClassRuleMatchDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 4),
    _AgentDiffServClassRuleMatchDstIpAddr_Type()
)
agentDiffServClassRuleMatchDstIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchDstIpAddr.setStatus("current")
_AgentDiffServClassRuleMatchDstIpMask_Type = IpAddress
_AgentDiffServClassRuleMatchDstIpMask_Object = MibTableColumn
agentDiffServClassRuleMatchDstIpMask = _AgentDiffServClassRuleMatchDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 5),
    _AgentDiffServClassRuleMatchDstIpMask_Type()
)
agentDiffServClassRuleMatchDstIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchDstIpMask.setStatus("current")
_AgentDiffServClassRuleMatchDstL4PortStart_Type = InetPortNumber
_AgentDiffServClassRuleMatchDstL4PortStart_Object = MibTableColumn
agentDiffServClassRuleMatchDstL4PortStart = _AgentDiffServClassRuleMatchDstL4PortStart_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 6),
    _AgentDiffServClassRuleMatchDstL4PortStart_Type()
)
agentDiffServClassRuleMatchDstL4PortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchDstL4PortStart.setStatus("current")
_AgentDiffServClassRuleMatchDstL4PortEnd_Type = InetPortNumber
_AgentDiffServClassRuleMatchDstL4PortEnd_Object = MibTableColumn
agentDiffServClassRuleMatchDstL4PortEnd = _AgentDiffServClassRuleMatchDstL4PortEnd_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 7),
    _AgentDiffServClassRuleMatchDstL4PortEnd_Type()
)
agentDiffServClassRuleMatchDstL4PortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchDstL4PortEnd.setStatus("current")
_AgentDiffServClassRuleMatchDstMacAddr_Type = MacAddress
_AgentDiffServClassRuleMatchDstMacAddr_Object = MibTableColumn
agentDiffServClassRuleMatchDstMacAddr = _AgentDiffServClassRuleMatchDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 8),
    _AgentDiffServClassRuleMatchDstMacAddr_Type()
)
agentDiffServClassRuleMatchDstMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchDstMacAddr.setStatus("current")
_AgentDiffServClassRuleMatchDstMacMask_Type = MacAddress
_AgentDiffServClassRuleMatchDstMacMask_Object = MibTableColumn
agentDiffServClassRuleMatchDstMacMask = _AgentDiffServClassRuleMatchDstMacMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 9),
    _AgentDiffServClassRuleMatchDstMacMask_Type()
)
agentDiffServClassRuleMatchDstMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchDstMacMask.setStatus("current")
_AgentDiffServClassRuleMatchEvery_Type = TruthValue
_AgentDiffServClassRuleMatchEvery_Object = MibTableColumn
agentDiffServClassRuleMatchEvery = _AgentDiffServClassRuleMatchEvery_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 10),
    _AgentDiffServClassRuleMatchEvery_Type()
)
agentDiffServClassRuleMatchEvery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchEvery.setStatus("current")


class _AgentDiffServClassRuleMatchIpDscp_Type(Unsigned32):
    """Custom type agentDiffServClassRuleMatchIpDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AgentDiffServClassRuleMatchIpDscp_Type.__name__ = "Unsigned32"
_AgentDiffServClassRuleMatchIpDscp_Object = MibTableColumn
agentDiffServClassRuleMatchIpDscp = _AgentDiffServClassRuleMatchIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 11),
    _AgentDiffServClassRuleMatchIpDscp_Type()
)
agentDiffServClassRuleMatchIpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchIpDscp.setStatus("current")


class _AgentDiffServClassRuleMatchIpPrecedence_Type(Unsigned32):
    """Custom type agentDiffServClassRuleMatchIpPrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentDiffServClassRuleMatchIpPrecedence_Type.__name__ = "Unsigned32"
_AgentDiffServClassRuleMatchIpPrecedence_Object = MibTableColumn
agentDiffServClassRuleMatchIpPrecedence = _AgentDiffServClassRuleMatchIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 12),
    _AgentDiffServClassRuleMatchIpPrecedence_Type()
)
agentDiffServClassRuleMatchIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchIpPrecedence.setStatus("current")


class _AgentDiffServClassRuleMatchIpTosBits_Type(OctetString):
    """Custom type agentDiffServClassRuleMatchIpTosBits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AgentDiffServClassRuleMatchIpTosBits_Type.__name__ = "OctetString"
_AgentDiffServClassRuleMatchIpTosBits_Object = MibTableColumn
agentDiffServClassRuleMatchIpTosBits = _AgentDiffServClassRuleMatchIpTosBits_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 13),
    _AgentDiffServClassRuleMatchIpTosBits_Type()
)
agentDiffServClassRuleMatchIpTosBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchIpTosBits.setStatus("current")


class _AgentDiffServClassRuleMatchIpTosMask_Type(OctetString):
    """Custom type agentDiffServClassRuleMatchIpTosMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AgentDiffServClassRuleMatchIpTosMask_Type.__name__ = "OctetString"
_AgentDiffServClassRuleMatchIpTosMask_Object = MibTableColumn
agentDiffServClassRuleMatchIpTosMask = _AgentDiffServClassRuleMatchIpTosMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 14),
    _AgentDiffServClassRuleMatchIpTosMask_Type()
)
agentDiffServClassRuleMatchIpTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchIpTosMask.setStatus("current")


class _AgentDiffServClassRuleMatchProtocolNum_Type(Unsigned32):
    """Custom type agentDiffServClassRuleMatchProtocolNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentDiffServClassRuleMatchProtocolNum_Type.__name__ = "Unsigned32"
_AgentDiffServClassRuleMatchProtocolNum_Object = MibTableColumn
agentDiffServClassRuleMatchProtocolNum = _AgentDiffServClassRuleMatchProtocolNum_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 15),
    _AgentDiffServClassRuleMatchProtocolNum_Type()
)
agentDiffServClassRuleMatchProtocolNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchProtocolNum.setStatus("current")
_AgentDiffServClassRuleMatchRefClassIndex_Type = Unsigned32
_AgentDiffServClassRuleMatchRefClassIndex_Object = MibTableColumn
agentDiffServClassRuleMatchRefClassIndex = _AgentDiffServClassRuleMatchRefClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 16),
    _AgentDiffServClassRuleMatchRefClassIndex_Type()
)
agentDiffServClassRuleMatchRefClassIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchRefClassIndex.setStatus("current")
_AgentDiffServClassRuleMatchSrcIpAddr_Type = IpAddress
_AgentDiffServClassRuleMatchSrcIpAddr_Object = MibTableColumn
agentDiffServClassRuleMatchSrcIpAddr = _AgentDiffServClassRuleMatchSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 17),
    _AgentDiffServClassRuleMatchSrcIpAddr_Type()
)
agentDiffServClassRuleMatchSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchSrcIpAddr.setStatus("current")
_AgentDiffServClassRuleMatchSrcIpMask_Type = IpAddress
_AgentDiffServClassRuleMatchSrcIpMask_Object = MibTableColumn
agentDiffServClassRuleMatchSrcIpMask = _AgentDiffServClassRuleMatchSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 18),
    _AgentDiffServClassRuleMatchSrcIpMask_Type()
)
agentDiffServClassRuleMatchSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchSrcIpMask.setStatus("current")
_AgentDiffServClassRuleMatchSrcL4PortStart_Type = InetPortNumber
_AgentDiffServClassRuleMatchSrcL4PortStart_Object = MibTableColumn
agentDiffServClassRuleMatchSrcL4PortStart = _AgentDiffServClassRuleMatchSrcL4PortStart_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 19),
    _AgentDiffServClassRuleMatchSrcL4PortStart_Type()
)
agentDiffServClassRuleMatchSrcL4PortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchSrcL4PortStart.setStatus("current")
_AgentDiffServClassRuleMatchSrcL4PortEnd_Type = InetPortNumber
_AgentDiffServClassRuleMatchSrcL4PortEnd_Object = MibTableColumn
agentDiffServClassRuleMatchSrcL4PortEnd = _AgentDiffServClassRuleMatchSrcL4PortEnd_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 20),
    _AgentDiffServClassRuleMatchSrcL4PortEnd_Type()
)
agentDiffServClassRuleMatchSrcL4PortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchSrcL4PortEnd.setStatus("current")
_AgentDiffServClassRuleMatchSrcMacAddr_Type = MacAddress
_AgentDiffServClassRuleMatchSrcMacAddr_Object = MibTableColumn
agentDiffServClassRuleMatchSrcMacAddr = _AgentDiffServClassRuleMatchSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 21),
    _AgentDiffServClassRuleMatchSrcMacAddr_Type()
)
agentDiffServClassRuleMatchSrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchSrcMacAddr.setStatus("current")
_AgentDiffServClassRuleMatchSrcMacMask_Type = MacAddress
_AgentDiffServClassRuleMatchSrcMacMask_Object = MibTableColumn
agentDiffServClassRuleMatchSrcMacMask = _AgentDiffServClassRuleMatchSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 22),
    _AgentDiffServClassRuleMatchSrcMacMask_Type()
)
agentDiffServClassRuleMatchSrcMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchSrcMacMask.setStatus("current")


class _AgentDiffServClassRuleMatchVlanId_Type(Unsigned32):
    """Custom type agentDiffServClassRuleMatchVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AgentDiffServClassRuleMatchVlanId_Type.__name__ = "Unsigned32"
_AgentDiffServClassRuleMatchVlanId_Object = MibTableColumn
agentDiffServClassRuleMatchVlanId = _AgentDiffServClassRuleMatchVlanId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 23),
    _AgentDiffServClassRuleMatchVlanId_Type()
)
agentDiffServClassRuleMatchVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchVlanId.setStatus("obsolete")
_AgentDiffServClassRuleMatchExcludeFlag_Type = TruthValue
_AgentDiffServClassRuleMatchExcludeFlag_Object = MibTableColumn
agentDiffServClassRuleMatchExcludeFlag = _AgentDiffServClassRuleMatchExcludeFlag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 24),
    _AgentDiffServClassRuleMatchExcludeFlag_Type()
)
agentDiffServClassRuleMatchExcludeFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchExcludeFlag.setStatus("current")


class _AgentDiffServClassRuleStorageType_Type(StorageType):
    """Custom type agentDiffServClassRuleStorageType based on StorageType"""


_AgentDiffServClassRuleStorageType_Object = MibTableColumn
agentDiffServClassRuleStorageType = _AgentDiffServClassRuleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 25),
    _AgentDiffServClassRuleStorageType_Type()
)
agentDiffServClassRuleStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleStorageType.setStatus("current")
_AgentDiffServClassRuleRowStatus_Type = RowStatus
_AgentDiffServClassRuleRowStatus_Object = MibTableColumn
agentDiffServClassRuleRowStatus = _AgentDiffServClassRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 26),
    _AgentDiffServClassRuleRowStatus_Type()
)
agentDiffServClassRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleRowStatus.setStatus("current")


class _AgentDiffServClassRuleMatchCos2_Type(Unsigned32):
    """Custom type agentDiffServClassRuleMatchCos2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentDiffServClassRuleMatchCos2_Type.__name__ = "Unsigned32"
_AgentDiffServClassRuleMatchCos2_Object = MibTableColumn
agentDiffServClassRuleMatchCos2 = _AgentDiffServClassRuleMatchCos2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 27),
    _AgentDiffServClassRuleMatchCos2_Type()
)
agentDiffServClassRuleMatchCos2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchCos2.setStatus("current")


class _AgentDiffServClassRuleMatchEtypeKey_Type(Integer32):
    """Custom type agentDiffServClassRuleMatchEtypeKey based on Integer32"""
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


_AgentDiffServClassRuleMatchEtypeKey_Type.__name__ = "Integer32"
_AgentDiffServClassRuleMatchEtypeKey_Object = MibTableColumn
agentDiffServClassRuleMatchEtypeKey = _AgentDiffServClassRuleMatchEtypeKey_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 28),
    _AgentDiffServClassRuleMatchEtypeKey_Type()
)
agentDiffServClassRuleMatchEtypeKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchEtypeKey.setStatus("current")
_AgentDiffServClassRuleMatchEtypeValue_Type = EtypeValue
_AgentDiffServClassRuleMatchEtypeValue_Object = MibTableColumn
agentDiffServClassRuleMatchEtypeValue = _AgentDiffServClassRuleMatchEtypeValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 29),
    _AgentDiffServClassRuleMatchEtypeValue_Type()
)
agentDiffServClassRuleMatchEtypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchEtypeValue.setStatus("current")


class _AgentDiffServClassRuleMatchVlanIdStart_Type(Unsigned32):
    """Custom type agentDiffServClassRuleMatchVlanIdStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AgentDiffServClassRuleMatchVlanIdStart_Type.__name__ = "Unsigned32"
_AgentDiffServClassRuleMatchVlanIdStart_Object = MibTableColumn
agentDiffServClassRuleMatchVlanIdStart = _AgentDiffServClassRuleMatchVlanIdStart_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 30),
    _AgentDiffServClassRuleMatchVlanIdStart_Type()
)
agentDiffServClassRuleMatchVlanIdStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchVlanIdStart.setStatus("current")


class _AgentDiffServClassRuleMatchVlanIdEnd_Type(Unsigned32):
    """Custom type agentDiffServClassRuleMatchVlanIdEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AgentDiffServClassRuleMatchVlanIdEnd_Type.__name__ = "Unsigned32"
_AgentDiffServClassRuleMatchVlanIdEnd_Object = MibTableColumn
agentDiffServClassRuleMatchVlanIdEnd = _AgentDiffServClassRuleMatchVlanIdEnd_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 31),
    _AgentDiffServClassRuleMatchVlanIdEnd_Type()
)
agentDiffServClassRuleMatchVlanIdEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchVlanIdEnd.setStatus("current")


class _AgentDiffServClassRuleMatchVlanId2Start_Type(Unsigned32):
    """Custom type agentDiffServClassRuleMatchVlanId2Start based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AgentDiffServClassRuleMatchVlanId2Start_Type.__name__ = "Unsigned32"
_AgentDiffServClassRuleMatchVlanId2Start_Object = MibTableColumn
agentDiffServClassRuleMatchVlanId2Start = _AgentDiffServClassRuleMatchVlanId2Start_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 32),
    _AgentDiffServClassRuleMatchVlanId2Start_Type()
)
agentDiffServClassRuleMatchVlanId2Start.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchVlanId2Start.setStatus("current")


class _AgentDiffServClassRuleMatchVlanId2End_Type(Unsigned32):
    """Custom type agentDiffServClassRuleMatchVlanId2End based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AgentDiffServClassRuleMatchVlanId2End_Type.__name__ = "Unsigned32"
_AgentDiffServClassRuleMatchVlanId2End_Object = MibTableColumn
agentDiffServClassRuleMatchVlanId2End = _AgentDiffServClassRuleMatchVlanId2End_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 33),
    _AgentDiffServClassRuleMatchVlanId2End_Type()
)
agentDiffServClassRuleMatchVlanId2End.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchVlanId2End.setStatus("current")


class _AgentDiffServClassRuleMatchFlowLabel_Type(Unsigned32):
    """Custom type agentDiffServClassRuleMatchFlowLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_AgentDiffServClassRuleMatchFlowLabel_Type.__name__ = "Unsigned32"
_AgentDiffServClassRuleMatchFlowLabel_Object = MibTableColumn
agentDiffServClassRuleMatchFlowLabel = _AgentDiffServClassRuleMatchFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 34),
    _AgentDiffServClassRuleMatchFlowLabel_Type()
)
agentDiffServClassRuleMatchFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchFlowLabel.setStatus("current")
_AgentDiffServClassRuleMatchDstIpv6Prefix_Type = Ipv6AddressPrefix
_AgentDiffServClassRuleMatchDstIpv6Prefix_Object = MibTableColumn
agentDiffServClassRuleMatchDstIpv6Prefix = _AgentDiffServClassRuleMatchDstIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 35),
    _AgentDiffServClassRuleMatchDstIpv6Prefix_Type()
)
agentDiffServClassRuleMatchDstIpv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchDstIpv6Prefix.setStatus("current")
_AgentDiffServClassRuleMatchSrcIpv6Prefix_Type = Ipv6AddressPrefix
_AgentDiffServClassRuleMatchSrcIpv6Prefix_Object = MibTableColumn
agentDiffServClassRuleMatchSrcIpv6Prefix = _AgentDiffServClassRuleMatchSrcIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 36),
    _AgentDiffServClassRuleMatchSrcIpv6Prefix_Type()
)
agentDiffServClassRuleMatchSrcIpv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchSrcIpv6Prefix.setStatus("current")


class _AgentDiffServClassRuleMatchDstIpv6PrefixLength_Type(Integer32):
    """Custom type agentDiffServClassRuleMatchDstIpv6PrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AgentDiffServClassRuleMatchDstIpv6PrefixLength_Type.__name__ = "Integer32"
_AgentDiffServClassRuleMatchDstIpv6PrefixLength_Object = MibTableColumn
agentDiffServClassRuleMatchDstIpv6PrefixLength = _AgentDiffServClassRuleMatchDstIpv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 37),
    _AgentDiffServClassRuleMatchDstIpv6PrefixLength_Type()
)
agentDiffServClassRuleMatchDstIpv6PrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchDstIpv6PrefixLength.setStatus("current")


class _AgentDiffServClassRuleMatchSrcIpv6PrefixLength_Type(Integer32):
    """Custom type agentDiffServClassRuleMatchSrcIpv6PrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AgentDiffServClassRuleMatchSrcIpv6PrefixLength_Type.__name__ = "Integer32"
_AgentDiffServClassRuleMatchSrcIpv6PrefixLength_Object = MibTableColumn
agentDiffServClassRuleMatchSrcIpv6PrefixLength = _AgentDiffServClassRuleMatchSrcIpv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 2, 3, 1, 38),
    _AgentDiffServClassRuleMatchSrcIpv6PrefixLength_Type()
)
agentDiffServClassRuleMatchSrcIpv6PrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServClassRuleMatchSrcIpv6PrefixLength.setStatus("current")
_AgentDiffServPolicyGroup_ObjectIdentity = ObjectIdentity
agentDiffServPolicyGroup = _AgentDiffServPolicyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3)
)
_AgentDiffServPolicyIndexNextFree_Type = Unsigned32
_AgentDiffServPolicyIndexNextFree_Object = MibScalar
agentDiffServPolicyIndexNextFree = _AgentDiffServPolicyIndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 1),
    _AgentDiffServPolicyIndexNextFree_Type()
)
agentDiffServPolicyIndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyIndexNextFree.setStatus("current")
_AgentDiffServPolicyTable_Object = MibTable
agentDiffServPolicyTable = _AgentDiffServPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 2)
)
if mibBuilder.loadTexts:
    agentDiffServPolicyTable.setStatus("current")
_AgentDiffServPolicyEntry_Object = MibTableRow
agentDiffServPolicyEntry = _AgentDiffServPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 2, 1)
)
agentDiffServPolicyEntry.setIndexNames(
    (0, "FASTPATH-QOS-DIFFSERV-PRIVATE-MIB", "agentDiffServPolicyIndex"),
)
if mibBuilder.loadTexts:
    agentDiffServPolicyEntry.setStatus("current")
_AgentDiffServPolicyIndex_Type = Unsigned32
_AgentDiffServPolicyIndex_Object = MibTableColumn
agentDiffServPolicyIndex = _AgentDiffServPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 2, 1, 1),
    _AgentDiffServPolicyIndex_Type()
)
agentDiffServPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDiffServPolicyIndex.setStatus("current")


class _AgentDiffServPolicyName_Type(DisplayString):
    """Custom type agentDiffServPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AgentDiffServPolicyName_Type.__name__ = "DisplayString"
_AgentDiffServPolicyName_Object = MibTableColumn
agentDiffServPolicyName = _AgentDiffServPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 2, 1, 2),
    _AgentDiffServPolicyName_Type()
)
agentDiffServPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyName.setStatus("current")
_AgentDiffServPolicyType_Type = IntfDirection
_AgentDiffServPolicyType_Object = MibTableColumn
agentDiffServPolicyType = _AgentDiffServPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 2, 1, 3),
    _AgentDiffServPolicyType_Type()
)
agentDiffServPolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyType.setStatus("current")
_AgentDiffServPolicyInstIndexNextFree_Type = Unsigned32
_AgentDiffServPolicyInstIndexNextFree_Object = MibTableColumn
agentDiffServPolicyInstIndexNextFree = _AgentDiffServPolicyInstIndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 2, 1, 4),
    _AgentDiffServPolicyInstIndexNextFree_Type()
)
agentDiffServPolicyInstIndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyInstIndexNextFree.setStatus("current")


class _AgentDiffServPolicyStorageType_Type(StorageType):
    """Custom type agentDiffServPolicyStorageType based on StorageType"""


_AgentDiffServPolicyStorageType_Object = MibTableColumn
agentDiffServPolicyStorageType = _AgentDiffServPolicyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 2, 1, 5),
    _AgentDiffServPolicyStorageType_Type()
)
agentDiffServPolicyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyStorageType.setStatus("current")
_AgentDiffServPolicyRowStatus_Type = RowStatus
_AgentDiffServPolicyRowStatus_Object = MibTableColumn
agentDiffServPolicyRowStatus = _AgentDiffServPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 2, 1, 6),
    _AgentDiffServPolicyRowStatus_Type()
)
agentDiffServPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyRowStatus.setStatus("current")
_AgentDiffServPolicyInstTable_Object = MibTable
agentDiffServPolicyInstTable = _AgentDiffServPolicyInstTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 3)
)
if mibBuilder.loadTexts:
    agentDiffServPolicyInstTable.setStatus("current")
_AgentDiffServPolicyInstEntry_Object = MibTableRow
agentDiffServPolicyInstEntry = _AgentDiffServPolicyInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 3, 1)
)
agentDiffServPolicyInstEntry.setIndexNames(
    (0, "FASTPATH-QOS-DIFFSERV-PRIVATE-MIB", "agentDiffServPolicyIndex"),
    (0, "FASTPATH-QOS-DIFFSERV-PRIVATE-MIB", "agentDiffServPolicyInstIndex"),
)
if mibBuilder.loadTexts:
    agentDiffServPolicyInstEntry.setStatus("current")
_AgentDiffServPolicyInstIndex_Type = Unsigned32
_AgentDiffServPolicyInstIndex_Object = MibTableColumn
agentDiffServPolicyInstIndex = _AgentDiffServPolicyInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 3, 1, 1),
    _AgentDiffServPolicyInstIndex_Type()
)
agentDiffServPolicyInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDiffServPolicyInstIndex.setStatus("current")
_AgentDiffServPolicyInstClassIndex_Type = Unsigned32
_AgentDiffServPolicyInstClassIndex_Object = MibTableColumn
agentDiffServPolicyInstClassIndex = _AgentDiffServPolicyInstClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 3, 1, 2),
    _AgentDiffServPolicyInstClassIndex_Type()
)
agentDiffServPolicyInstClassIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyInstClassIndex.setStatus("current")
_AgentDiffServPolicyInstAttrIndexNextFree_Type = Unsigned32
_AgentDiffServPolicyInstAttrIndexNextFree_Object = MibTableColumn
agentDiffServPolicyInstAttrIndexNextFree = _AgentDiffServPolicyInstAttrIndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 3, 1, 3),
    _AgentDiffServPolicyInstAttrIndexNextFree_Type()
)
agentDiffServPolicyInstAttrIndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyInstAttrIndexNextFree.setStatus("current")


class _AgentDiffServPolicyInstStorageType_Type(StorageType):
    """Custom type agentDiffServPolicyInstStorageType based on StorageType"""


_AgentDiffServPolicyInstStorageType_Object = MibTableColumn
agentDiffServPolicyInstStorageType = _AgentDiffServPolicyInstStorageType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 3, 1, 4),
    _AgentDiffServPolicyInstStorageType_Type()
)
agentDiffServPolicyInstStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyInstStorageType.setStatus("current")
_AgentDiffServPolicyInstRowStatus_Type = RowStatus
_AgentDiffServPolicyInstRowStatus_Object = MibTableColumn
agentDiffServPolicyInstRowStatus = _AgentDiffServPolicyInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 3, 1, 5),
    _AgentDiffServPolicyInstRowStatus_Type()
)
agentDiffServPolicyInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyInstRowStatus.setStatus("current")
_AgentDiffServPolicyAttrTable_Object = MibTable
agentDiffServPolicyAttrTable = _AgentDiffServPolicyAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4)
)
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrTable.setStatus("current")
_AgentDiffServPolicyAttrEntry_Object = MibTableRow
agentDiffServPolicyAttrEntry = _AgentDiffServPolicyAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1)
)
agentDiffServPolicyAttrEntry.setIndexNames(
    (0, "FASTPATH-QOS-DIFFSERV-PRIVATE-MIB", "agentDiffServPolicyIndex"),
    (0, "FASTPATH-QOS-DIFFSERV-PRIVATE-MIB", "agentDiffServPolicyInstIndex"),
    (0, "FASTPATH-QOS-DIFFSERV-PRIVATE-MIB", "agentDiffServPolicyAttrIndex"),
)
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrEntry.setStatus("current")
_AgentDiffServPolicyAttrIndex_Type = Unsigned32
_AgentDiffServPolicyAttrIndex_Object = MibTableColumn
agentDiffServPolicyAttrIndex = _AgentDiffServPolicyAttrIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 1),
    _AgentDiffServPolicyAttrIndex_Type()
)
agentDiffServPolicyAttrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrIndex.setStatus("current")


class _AgentDiffServPolicyAttrStmtEntryType_Type(Integer32):
    """Custom type agentDiffServPolicyAttrStmtEntryType based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("assignQueue", 12),
          ("bandwidth", 1),
          ("drop", 13),
          ("expedite", 2),
          ("markCos2Val", 14),
          ("markCosAsSecCos", 17),
          ("markCosVal", 3),
          ("markIpDscpVal", 4),
          ("markIpPrecedenceVal", 5),
          ("mirror", 16),
          ("policeSimple", 6),
          ("policeSinglerate", 7),
          ("policeTworate", 8),
          ("randomdrop", 9),
          ("redirect", 15),
          ("shapeAverage", 10),
          ("shapePeak", 11))
    )


_AgentDiffServPolicyAttrStmtEntryType_Type.__name__ = "Integer32"
_AgentDiffServPolicyAttrStmtEntryType_Object = MibTableColumn
agentDiffServPolicyAttrStmtEntryType = _AgentDiffServPolicyAttrStmtEntryType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 2),
    _AgentDiffServPolicyAttrStmtEntryType_Type()
)
agentDiffServPolicyAttrStmtEntryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtEntryType.setStatus("current")
_AgentDiffServPolicyAttrStmtBandwidthCrate_Type = Unsigned32
_AgentDiffServPolicyAttrStmtBandwidthCrate_Object = MibTableColumn
agentDiffServPolicyAttrStmtBandwidthCrate = _AgentDiffServPolicyAttrStmtBandwidthCrate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 3),
    _AgentDiffServPolicyAttrStmtBandwidthCrate_Type()
)
agentDiffServPolicyAttrStmtBandwidthCrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtBandwidthCrate.setStatus("obsolete")


class _AgentDiffServPolicyAttrStmtBandwidthCrateUnits_Type(Integer32):
    """Custom type agentDiffServPolicyAttrStmtBandwidthCrateUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 1),
          ("percentage", 2))
    )


_AgentDiffServPolicyAttrStmtBandwidthCrateUnits_Type.__name__ = "Integer32"
_AgentDiffServPolicyAttrStmtBandwidthCrateUnits_Object = MibTableColumn
agentDiffServPolicyAttrStmtBandwidthCrateUnits = _AgentDiffServPolicyAttrStmtBandwidthCrateUnits_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 4),
    _AgentDiffServPolicyAttrStmtBandwidthCrateUnits_Type()
)
agentDiffServPolicyAttrStmtBandwidthCrateUnits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtBandwidthCrateUnits.setStatus("obsolete")
_AgentDiffServPolicyAttrStmtExpediteCrate_Type = Unsigned32
_AgentDiffServPolicyAttrStmtExpediteCrate_Object = MibTableColumn
agentDiffServPolicyAttrStmtExpediteCrate = _AgentDiffServPolicyAttrStmtExpediteCrate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 5),
    _AgentDiffServPolicyAttrStmtExpediteCrate_Type()
)
agentDiffServPolicyAttrStmtExpediteCrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtExpediteCrate.setStatus("obsolete")


class _AgentDiffServPolicyAttrStmtExpediteCrateUnits_Type(Integer32):
    """Custom type agentDiffServPolicyAttrStmtExpediteCrateUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 1),
          ("percentage", 2))
    )


_AgentDiffServPolicyAttrStmtExpediteCrateUnits_Type.__name__ = "Integer32"
_AgentDiffServPolicyAttrStmtExpediteCrateUnits_Object = MibTableColumn
agentDiffServPolicyAttrStmtExpediteCrateUnits = _AgentDiffServPolicyAttrStmtExpediteCrateUnits_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 6),
    _AgentDiffServPolicyAttrStmtExpediteCrateUnits_Type()
)
agentDiffServPolicyAttrStmtExpediteCrateUnits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtExpediteCrateUnits.setStatus("obsolete")


class _AgentDiffServPolicyAttrStmtExpediteCburst_Type(QosBurstSize):
    """Custom type agentDiffServPolicyAttrStmtExpediteCburst based on QosBurstSize"""
    defaultValue = 4


_AgentDiffServPolicyAttrStmtExpediteCburst_Object = MibTableColumn
agentDiffServPolicyAttrStmtExpediteCburst = _AgentDiffServPolicyAttrStmtExpediteCburst_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 7),
    _AgentDiffServPolicyAttrStmtExpediteCburst_Type()
)
agentDiffServPolicyAttrStmtExpediteCburst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtExpediteCburst.setStatus("obsolete")


class _AgentDiffServPolicyAttrStmtMarkCosVal_Type(Unsigned32):
    """Custom type agentDiffServPolicyAttrStmtMarkCosVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentDiffServPolicyAttrStmtMarkCosVal_Type.__name__ = "Unsigned32"
_AgentDiffServPolicyAttrStmtMarkCosVal_Object = MibTableColumn
agentDiffServPolicyAttrStmtMarkCosVal = _AgentDiffServPolicyAttrStmtMarkCosVal_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 8),
    _AgentDiffServPolicyAttrStmtMarkCosVal_Type()
)
agentDiffServPolicyAttrStmtMarkCosVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtMarkCosVal.setStatus("current")


class _AgentDiffServPolicyAttrStmtMarkIpDscpVal_Type(Unsigned32):
    """Custom type agentDiffServPolicyAttrStmtMarkIpDscpVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AgentDiffServPolicyAttrStmtMarkIpDscpVal_Type.__name__ = "Unsigned32"
_AgentDiffServPolicyAttrStmtMarkIpDscpVal_Object = MibTableColumn
agentDiffServPolicyAttrStmtMarkIpDscpVal = _AgentDiffServPolicyAttrStmtMarkIpDscpVal_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 9),
    _AgentDiffServPolicyAttrStmtMarkIpDscpVal_Type()
)
agentDiffServPolicyAttrStmtMarkIpDscpVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtMarkIpDscpVal.setStatus("current")


class _AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal_Type(Unsigned32):
    """Custom type agentDiffServPolicyAttrStmtMarkIpPrecedenceVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal_Type.__name__ = "Unsigned32"
_AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal_Object = MibTableColumn
agentDiffServPolicyAttrStmtMarkIpPrecedenceVal = _AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 10),
    _AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal_Type()
)
agentDiffServPolicyAttrStmtMarkIpPrecedenceVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtMarkIpPrecedenceVal.setStatus("current")


class _AgentDiffServPolicyAttrStmtPoliceConformAct_Type(Integer32):
    """Custom type agentDiffServPolicyAttrStmtPoliceConformAct based on Integer32"""
    defaultValue = 4

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
        *(("drop", 1),
          ("markcos", 5),
          ("markcos2", 6),
          ("markcosAsSecCos", 7),
          ("markdscp", 2),
          ("markprec", 3),
          ("send", 4))
    )


_AgentDiffServPolicyAttrStmtPoliceConformAct_Type.__name__ = "Integer32"
_AgentDiffServPolicyAttrStmtPoliceConformAct_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceConformAct = _AgentDiffServPolicyAttrStmtPoliceConformAct_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 11),
    _AgentDiffServPolicyAttrStmtPoliceConformAct_Type()
)
agentDiffServPolicyAttrStmtPoliceConformAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceConformAct.setStatus("current")


class _AgentDiffServPolicyAttrStmtPoliceConformVal_Type(Unsigned32):
    """Custom type agentDiffServPolicyAttrStmtPoliceConformVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AgentDiffServPolicyAttrStmtPoliceConformVal_Type.__name__ = "Unsigned32"
_AgentDiffServPolicyAttrStmtPoliceConformVal_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceConformVal = _AgentDiffServPolicyAttrStmtPoliceConformVal_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 12),
    _AgentDiffServPolicyAttrStmtPoliceConformVal_Type()
)
agentDiffServPolicyAttrStmtPoliceConformVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceConformVal.setStatus("current")


class _AgentDiffServPolicyAttrStmtPoliceExceedAct_Type(Integer32):
    """Custom type agentDiffServPolicyAttrStmtPoliceExceedAct based on Integer32"""
    defaultValue = 1

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
        *(("drop", 1),
          ("markcos", 5),
          ("markcos2", 6),
          ("markcosAsSecCos", 7),
          ("markdscp", 2),
          ("markprec", 3),
          ("send", 4))
    )


_AgentDiffServPolicyAttrStmtPoliceExceedAct_Type.__name__ = "Integer32"
_AgentDiffServPolicyAttrStmtPoliceExceedAct_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceExceedAct = _AgentDiffServPolicyAttrStmtPoliceExceedAct_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 13),
    _AgentDiffServPolicyAttrStmtPoliceExceedAct_Type()
)
agentDiffServPolicyAttrStmtPoliceExceedAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceExceedAct.setStatus("current")


class _AgentDiffServPolicyAttrStmtPoliceExceedVal_Type(Unsigned32):
    """Custom type agentDiffServPolicyAttrStmtPoliceExceedVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AgentDiffServPolicyAttrStmtPoliceExceedVal_Type.__name__ = "Unsigned32"
_AgentDiffServPolicyAttrStmtPoliceExceedVal_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceExceedVal = _AgentDiffServPolicyAttrStmtPoliceExceedVal_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 14),
    _AgentDiffServPolicyAttrStmtPoliceExceedVal_Type()
)
agentDiffServPolicyAttrStmtPoliceExceedVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceExceedVal.setStatus("current")


class _AgentDiffServPolicyAttrStmtPoliceNonconformAct_Type(Integer32):
    """Custom type agentDiffServPolicyAttrStmtPoliceNonconformAct based on Integer32"""
    defaultValue = 1

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
        *(("drop", 1),
          ("markcos", 5),
          ("markcos2", 6),
          ("markcosAsSecCos", 7),
          ("markdscp", 2),
          ("markprec", 3),
          ("send", 4))
    )


_AgentDiffServPolicyAttrStmtPoliceNonconformAct_Type.__name__ = "Integer32"
_AgentDiffServPolicyAttrStmtPoliceNonconformAct_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceNonconformAct = _AgentDiffServPolicyAttrStmtPoliceNonconformAct_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 15),
    _AgentDiffServPolicyAttrStmtPoliceNonconformAct_Type()
)
agentDiffServPolicyAttrStmtPoliceNonconformAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceNonconformAct.setStatus("current")


class _AgentDiffServPolicyAttrStmtPoliceNonconformVal_Type(Unsigned32):
    """Custom type agentDiffServPolicyAttrStmtPoliceNonconformVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AgentDiffServPolicyAttrStmtPoliceNonconformVal_Type.__name__ = "Unsigned32"
_AgentDiffServPolicyAttrStmtPoliceNonconformVal_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceNonconformVal = _AgentDiffServPolicyAttrStmtPoliceNonconformVal_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 16),
    _AgentDiffServPolicyAttrStmtPoliceNonconformVal_Type()
)
agentDiffServPolicyAttrStmtPoliceNonconformVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceNonconformVal.setStatus("current")
_AgentDiffServPolicyAttrStmtPoliceSimpleCrate_Type = Unsigned32
_AgentDiffServPolicyAttrStmtPoliceSimpleCrate_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceSimpleCrate = _AgentDiffServPolicyAttrStmtPoliceSimpleCrate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 17),
    _AgentDiffServPolicyAttrStmtPoliceSimpleCrate_Type()
)
agentDiffServPolicyAttrStmtPoliceSimpleCrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceSimpleCrate.setStatus("current")
_AgentDiffServPolicyAttrStmtPoliceSimpleCburst_Type = QosBurstSize
_AgentDiffServPolicyAttrStmtPoliceSimpleCburst_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceSimpleCburst = _AgentDiffServPolicyAttrStmtPoliceSimpleCburst_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 18),
    _AgentDiffServPolicyAttrStmtPoliceSimpleCburst_Type()
)
agentDiffServPolicyAttrStmtPoliceSimpleCburst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceSimpleCburst.setStatus("current")
_AgentDiffServPolicyAttrStmtPoliceSinglerateCrate_Type = Unsigned32
_AgentDiffServPolicyAttrStmtPoliceSinglerateCrate_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceSinglerateCrate = _AgentDiffServPolicyAttrStmtPoliceSinglerateCrate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 19),
    _AgentDiffServPolicyAttrStmtPoliceSinglerateCrate_Type()
)
agentDiffServPolicyAttrStmtPoliceSinglerateCrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceSinglerateCrate.setStatus("current")
_AgentDiffServPolicyAttrStmtPoliceSinglerateCburst_Type = QosBurstSize
_AgentDiffServPolicyAttrStmtPoliceSinglerateCburst_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceSinglerateCburst = _AgentDiffServPolicyAttrStmtPoliceSinglerateCburst_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 20),
    _AgentDiffServPolicyAttrStmtPoliceSinglerateCburst_Type()
)
agentDiffServPolicyAttrStmtPoliceSinglerateCburst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceSinglerateCburst.setStatus("current")
_AgentDiffServPolicyAttrStmtPoliceSinglerateEburst_Type = QosBurstSize
_AgentDiffServPolicyAttrStmtPoliceSinglerateEburst_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceSinglerateEburst = _AgentDiffServPolicyAttrStmtPoliceSinglerateEburst_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 21),
    _AgentDiffServPolicyAttrStmtPoliceSinglerateEburst_Type()
)
agentDiffServPolicyAttrStmtPoliceSinglerateEburst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceSinglerateEburst.setStatus("current")
_AgentDiffServPolicyAttrStmtPoliceTworateCrate_Type = Unsigned32
_AgentDiffServPolicyAttrStmtPoliceTworateCrate_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceTworateCrate = _AgentDiffServPolicyAttrStmtPoliceTworateCrate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 22),
    _AgentDiffServPolicyAttrStmtPoliceTworateCrate_Type()
)
agentDiffServPolicyAttrStmtPoliceTworateCrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceTworateCrate.setStatus("current")
_AgentDiffServPolicyAttrStmtPoliceTworateCburst_Type = QosBurstSize
_AgentDiffServPolicyAttrStmtPoliceTworateCburst_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceTworateCburst = _AgentDiffServPolicyAttrStmtPoliceTworateCburst_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 23),
    _AgentDiffServPolicyAttrStmtPoliceTworateCburst_Type()
)
agentDiffServPolicyAttrStmtPoliceTworateCburst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceTworateCburst.setStatus("current")
_AgentDiffServPolicyAttrStmtPoliceTworatePrate_Type = Unsigned32
_AgentDiffServPolicyAttrStmtPoliceTworatePrate_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceTworatePrate = _AgentDiffServPolicyAttrStmtPoliceTworatePrate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 24),
    _AgentDiffServPolicyAttrStmtPoliceTworatePrate_Type()
)
agentDiffServPolicyAttrStmtPoliceTworatePrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceTworatePrate.setStatus("current")
_AgentDiffServPolicyAttrStmtPoliceTworatePburst_Type = QosBurstSize
_AgentDiffServPolicyAttrStmtPoliceTworatePburst_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceTworatePburst = _AgentDiffServPolicyAttrStmtPoliceTworatePburst_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 25),
    _AgentDiffServPolicyAttrStmtPoliceTworatePburst_Type()
)
agentDiffServPolicyAttrStmtPoliceTworatePburst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceTworatePburst.setStatus("current")


class _AgentDiffServPolicyAttrStmtRandomdropMinThresh_Type(Unsigned32):
    """Custom type agentDiffServPolicyAttrStmtRandomdropMinThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250000),
    )


_AgentDiffServPolicyAttrStmtRandomdropMinThresh_Type.__name__ = "Unsigned32"
_AgentDiffServPolicyAttrStmtRandomdropMinThresh_Object = MibTableColumn
agentDiffServPolicyAttrStmtRandomdropMinThresh = _AgentDiffServPolicyAttrStmtRandomdropMinThresh_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 26),
    _AgentDiffServPolicyAttrStmtRandomdropMinThresh_Type()
)
agentDiffServPolicyAttrStmtRandomdropMinThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtRandomdropMinThresh.setStatus("obsolete")


class _AgentDiffServPolicyAttrStmtRandomdropMaxThresh_Type(Unsigned32):
    """Custom type agentDiffServPolicyAttrStmtRandomdropMaxThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_AgentDiffServPolicyAttrStmtRandomdropMaxThresh_Type.__name__ = "Unsigned32"
_AgentDiffServPolicyAttrStmtRandomdropMaxThresh_Object = MibTableColumn
agentDiffServPolicyAttrStmtRandomdropMaxThresh = _AgentDiffServPolicyAttrStmtRandomdropMaxThresh_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 27),
    _AgentDiffServPolicyAttrStmtRandomdropMaxThresh_Type()
)
agentDiffServPolicyAttrStmtRandomdropMaxThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtRandomdropMaxThresh.setStatus("obsolete")


class _AgentDiffServPolicyAttrStmtRandomdropMaxDropProb_Type(Unsigned32):
    """Custom type agentDiffServPolicyAttrStmtRandomdropMaxDropProb based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AgentDiffServPolicyAttrStmtRandomdropMaxDropProb_Type.__name__ = "Unsigned32"
_AgentDiffServPolicyAttrStmtRandomdropMaxDropProb_Object = MibTableColumn
agentDiffServPolicyAttrStmtRandomdropMaxDropProb = _AgentDiffServPolicyAttrStmtRandomdropMaxDropProb_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 28),
    _AgentDiffServPolicyAttrStmtRandomdropMaxDropProb_Type()
)
agentDiffServPolicyAttrStmtRandomdropMaxDropProb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtRandomdropMaxDropProb.setStatus("obsolete")


class _AgentDiffServPolicyAttrStmtRandomdropSamplingRate_Type(Unsigned32):
    """Custom type agentDiffServPolicyAttrStmtRandomdropSamplingRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_AgentDiffServPolicyAttrStmtRandomdropSamplingRate_Type.__name__ = "Unsigned32"
_AgentDiffServPolicyAttrStmtRandomdropSamplingRate_Object = MibTableColumn
agentDiffServPolicyAttrStmtRandomdropSamplingRate = _AgentDiffServPolicyAttrStmtRandomdropSamplingRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 29),
    _AgentDiffServPolicyAttrStmtRandomdropSamplingRate_Type()
)
agentDiffServPolicyAttrStmtRandomdropSamplingRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtRandomdropSamplingRate.setStatus("obsolete")


class _AgentDiffServPolicyAttrStmtRandomdropDecayExponent_Type(Unsigned32):
    """Custom type agentDiffServPolicyAttrStmtRandomdropDecayExponent based on Unsigned32"""
    defaultValue = 9

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AgentDiffServPolicyAttrStmtRandomdropDecayExponent_Type.__name__ = "Unsigned32"
_AgentDiffServPolicyAttrStmtRandomdropDecayExponent_Object = MibTableColumn
agentDiffServPolicyAttrStmtRandomdropDecayExponent = _AgentDiffServPolicyAttrStmtRandomdropDecayExponent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 30),
    _AgentDiffServPolicyAttrStmtRandomdropDecayExponent_Type()
)
agentDiffServPolicyAttrStmtRandomdropDecayExponent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtRandomdropDecayExponent.setStatus("obsolete")
_AgentDiffServPolicyAttrStmtShapeAverageCrate_Type = Unsigned32
_AgentDiffServPolicyAttrStmtShapeAverageCrate_Object = MibTableColumn
agentDiffServPolicyAttrStmtShapeAverageCrate = _AgentDiffServPolicyAttrStmtShapeAverageCrate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 31),
    _AgentDiffServPolicyAttrStmtShapeAverageCrate_Type()
)
agentDiffServPolicyAttrStmtShapeAverageCrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtShapeAverageCrate.setStatus("obsolete")
_AgentDiffServPolicyAttrStmtShapePeakCrate_Type = Unsigned32
_AgentDiffServPolicyAttrStmtShapePeakCrate_Object = MibTableColumn
agentDiffServPolicyAttrStmtShapePeakCrate = _AgentDiffServPolicyAttrStmtShapePeakCrate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 32),
    _AgentDiffServPolicyAttrStmtShapePeakCrate_Type()
)
agentDiffServPolicyAttrStmtShapePeakCrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtShapePeakCrate.setStatus("obsolete")
_AgentDiffServPolicyAttrStmtShapePeakPrate_Type = Unsigned32
_AgentDiffServPolicyAttrStmtShapePeakPrate_Object = MibTableColumn
agentDiffServPolicyAttrStmtShapePeakPrate = _AgentDiffServPolicyAttrStmtShapePeakPrate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 33),
    _AgentDiffServPolicyAttrStmtShapePeakPrate_Type()
)
agentDiffServPolicyAttrStmtShapePeakPrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtShapePeakPrate.setStatus("obsolete")


class _AgentDiffServPolicyAttrStorageType_Type(StorageType):
    """Custom type agentDiffServPolicyAttrStorageType based on StorageType"""


_AgentDiffServPolicyAttrStorageType_Object = MibTableColumn
agentDiffServPolicyAttrStorageType = _AgentDiffServPolicyAttrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 34),
    _AgentDiffServPolicyAttrStorageType_Type()
)
agentDiffServPolicyAttrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStorageType.setStatus("current")
_AgentDiffServPolicyAttrRowStatus_Type = RowStatus
_AgentDiffServPolicyAttrRowStatus_Object = MibTableColumn
agentDiffServPolicyAttrRowStatus = _AgentDiffServPolicyAttrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 35),
    _AgentDiffServPolicyAttrRowStatus_Type()
)
agentDiffServPolicyAttrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrRowStatus.setStatus("current")
_AgentDiffServPolicyAttrStmtAssignQueueId_Type = Unsigned32
_AgentDiffServPolicyAttrStmtAssignQueueId_Object = MibTableColumn
agentDiffServPolicyAttrStmtAssignQueueId = _AgentDiffServPolicyAttrStmtAssignQueueId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 36),
    _AgentDiffServPolicyAttrStmtAssignQueueId_Type()
)
agentDiffServPolicyAttrStmtAssignQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtAssignQueueId.setStatus("current")
_AgentDiffServPolicyAttrStmtDrop_Type = TruthValue
_AgentDiffServPolicyAttrStmtDrop_Object = MibTableColumn
agentDiffServPolicyAttrStmtDrop = _AgentDiffServPolicyAttrStmtDrop_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 37),
    _AgentDiffServPolicyAttrStmtDrop_Type()
)
agentDiffServPolicyAttrStmtDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtDrop.setStatus("current")


class _AgentDiffServPolicyAttrStmtMarkCos2Val_Type(Unsigned32):
    """Custom type agentDiffServPolicyAttrStmtMarkCos2Val based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentDiffServPolicyAttrStmtMarkCos2Val_Type.__name__ = "Unsigned32"
_AgentDiffServPolicyAttrStmtMarkCos2Val_Object = MibTableColumn
agentDiffServPolicyAttrStmtMarkCos2Val = _AgentDiffServPolicyAttrStmtMarkCos2Val_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 38),
    _AgentDiffServPolicyAttrStmtMarkCos2Val_Type()
)
agentDiffServPolicyAttrStmtMarkCos2Val.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtMarkCos2Val.setStatus("current")


class _AgentDiffServPolicyAttrStmtPoliceColorConformIndex_Type(Unsigned32):
    """Custom type agentDiffServPolicyAttrStmtPoliceColorConformIndex based on Unsigned32"""
    defaultValue = 0


_AgentDiffServPolicyAttrStmtPoliceColorConformIndex_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceColorConformIndex = _AgentDiffServPolicyAttrStmtPoliceColorConformIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 39),
    _AgentDiffServPolicyAttrStmtPoliceColorConformIndex_Type()
)
agentDiffServPolicyAttrStmtPoliceColorConformIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceColorConformIndex.setStatus("current")


class _AgentDiffServPolicyAttrStmtPoliceColorConformMode_Type(Integer32):
    """Custom type agentDiffServPolicyAttrStmtPoliceColorConformMode based on Integer32"""
    defaultValue = 1

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
        *(("blind", 1),
          ("cos", 2),
          ("cos2", 3),
          ("ipdscp", 4),
          ("ipprec", 5))
    )


_AgentDiffServPolicyAttrStmtPoliceColorConformMode_Type.__name__ = "Integer32"
_AgentDiffServPolicyAttrStmtPoliceColorConformMode_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceColorConformMode = _AgentDiffServPolicyAttrStmtPoliceColorConformMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 40),
    _AgentDiffServPolicyAttrStmtPoliceColorConformMode_Type()
)
agentDiffServPolicyAttrStmtPoliceColorConformMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceColorConformMode.setStatus("current")
_AgentDiffServPolicyAttrStmtPoliceColorConformVal_Type = Unsigned32
_AgentDiffServPolicyAttrStmtPoliceColorConformVal_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceColorConformVal = _AgentDiffServPolicyAttrStmtPoliceColorConformVal_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 41),
    _AgentDiffServPolicyAttrStmtPoliceColorConformVal_Type()
)
agentDiffServPolicyAttrStmtPoliceColorConformVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceColorConformVal.setStatus("current")


class _AgentDiffServPolicyAttrStmtPoliceColorExceedIndex_Type(Unsigned32):
    """Custom type agentDiffServPolicyAttrStmtPoliceColorExceedIndex based on Unsigned32"""
    defaultValue = 0


_AgentDiffServPolicyAttrStmtPoliceColorExceedIndex_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceColorExceedIndex = _AgentDiffServPolicyAttrStmtPoliceColorExceedIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 42),
    _AgentDiffServPolicyAttrStmtPoliceColorExceedIndex_Type()
)
agentDiffServPolicyAttrStmtPoliceColorExceedIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceColorExceedIndex.setStatus("current")


class _AgentDiffServPolicyAttrStmtPoliceColorExceedMode_Type(Integer32):
    """Custom type agentDiffServPolicyAttrStmtPoliceColorExceedMode based on Integer32"""
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
        *(("blind", 1),
          ("cos", 2),
          ("cos2", 3),
          ("ipdscp", 4),
          ("ipprec", 5),
          ("unused", 6))
    )


_AgentDiffServPolicyAttrStmtPoliceColorExceedMode_Type.__name__ = "Integer32"
_AgentDiffServPolicyAttrStmtPoliceColorExceedMode_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceColorExceedMode = _AgentDiffServPolicyAttrStmtPoliceColorExceedMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 43),
    _AgentDiffServPolicyAttrStmtPoliceColorExceedMode_Type()
)
agentDiffServPolicyAttrStmtPoliceColorExceedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceColorExceedMode.setStatus("current")
_AgentDiffServPolicyAttrStmtPoliceColorExceedVal_Type = Unsigned32
_AgentDiffServPolicyAttrStmtPoliceColorExceedVal_Object = MibTableColumn
agentDiffServPolicyAttrStmtPoliceColorExceedVal = _AgentDiffServPolicyAttrStmtPoliceColorExceedVal_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 44),
    _AgentDiffServPolicyAttrStmtPoliceColorExceedVal_Type()
)
agentDiffServPolicyAttrStmtPoliceColorExceedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtPoliceColorExceedVal.setStatus("current")
_AgentDiffServPolicyAttrStmtRedirectIntf_Type = InterfaceIndex
_AgentDiffServPolicyAttrStmtRedirectIntf_Object = MibTableColumn
agentDiffServPolicyAttrStmtRedirectIntf = _AgentDiffServPolicyAttrStmtRedirectIntf_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 45),
    _AgentDiffServPolicyAttrStmtRedirectIntf_Type()
)
agentDiffServPolicyAttrStmtRedirectIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtRedirectIntf.setStatus("current")
_AgentDiffServPolicyAttrStmtMirrorIntf_Type = InterfaceIndex
_AgentDiffServPolicyAttrStmtMirrorIntf_Object = MibTableColumn
agentDiffServPolicyAttrStmtMirrorIntf = _AgentDiffServPolicyAttrStmtMirrorIntf_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 46),
    _AgentDiffServPolicyAttrStmtMirrorIntf_Type()
)
agentDiffServPolicyAttrStmtMirrorIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtMirrorIntf.setStatus("current")
_AgentDiffServPolicyAttrStmtMarkCosAsSecCos_Type = TruthValue
_AgentDiffServPolicyAttrStmtMarkCosAsSecCos_Object = MibScalar
agentDiffServPolicyAttrStmtMarkCosAsSecCos = _AgentDiffServPolicyAttrStmtMarkCosAsSecCos_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 4, 1, 47),
    _AgentDiffServPolicyAttrStmtMarkCosAsSecCos_Type()
)
agentDiffServPolicyAttrStmtMarkCosAsSecCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyAttrStmtMarkCosAsSecCos.setStatus("current")
_AgentDiffServPolicyPerfInTable_Object = MibTable
agentDiffServPolicyPerfInTable = _AgentDiffServPolicyPerfInTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 5)
)
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfInTable.setStatus("current")
_AgentDiffServPolicyPerfInEntry_Object = MibTableRow
agentDiffServPolicyPerfInEntry = _AgentDiffServPolicyPerfInEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 5, 1)
)
agentDiffServPolicyPerfInEntry.setIndexNames(
    (0, "FASTPATH-QOS-DIFFSERV-PRIVATE-MIB", "agentDiffServPolicyIndex"),
    (0, "FASTPATH-QOS-DIFFSERV-PRIVATE-MIB", "agentDiffServPolicyInstIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfInEntry.setStatus("current")
_AgentDiffServPolicyPerfInOfferedOctets_Type = Counter32
_AgentDiffServPolicyPerfInOfferedOctets_Object = MibTableColumn
agentDiffServPolicyPerfInOfferedOctets = _AgentDiffServPolicyPerfInOfferedOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 5, 1, 1),
    _AgentDiffServPolicyPerfInOfferedOctets_Type()
)
agentDiffServPolicyPerfInOfferedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfInOfferedOctets.setStatus("current")
_AgentDiffServPolicyPerfInOfferedPackets_Type = Counter32
_AgentDiffServPolicyPerfInOfferedPackets_Object = MibTableColumn
agentDiffServPolicyPerfInOfferedPackets = _AgentDiffServPolicyPerfInOfferedPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 5, 1, 2),
    _AgentDiffServPolicyPerfInOfferedPackets_Type()
)
agentDiffServPolicyPerfInOfferedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfInOfferedPackets.setStatus("current")
_AgentDiffServPolicyPerfInDiscardedOctets_Type = Counter32
_AgentDiffServPolicyPerfInDiscardedOctets_Object = MibTableColumn
agentDiffServPolicyPerfInDiscardedOctets = _AgentDiffServPolicyPerfInDiscardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 5, 1, 3),
    _AgentDiffServPolicyPerfInDiscardedOctets_Type()
)
agentDiffServPolicyPerfInDiscardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfInDiscardedOctets.setStatus("current")
_AgentDiffServPolicyPerfInDiscardedPackets_Type = Counter32
_AgentDiffServPolicyPerfInDiscardedPackets_Object = MibTableColumn
agentDiffServPolicyPerfInDiscardedPackets = _AgentDiffServPolicyPerfInDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 5, 1, 4),
    _AgentDiffServPolicyPerfInDiscardedPackets_Type()
)
agentDiffServPolicyPerfInDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfInDiscardedPackets.setStatus("current")
_AgentDiffServPolicyPerfInHCOfferedOctets_Type = Counter64
_AgentDiffServPolicyPerfInHCOfferedOctets_Object = MibTableColumn
agentDiffServPolicyPerfInHCOfferedOctets = _AgentDiffServPolicyPerfInHCOfferedOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 5, 1, 5),
    _AgentDiffServPolicyPerfInHCOfferedOctets_Type()
)
agentDiffServPolicyPerfInHCOfferedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfInHCOfferedOctets.setStatus("current")
_AgentDiffServPolicyPerfInHCOfferedPackets_Type = Counter64
_AgentDiffServPolicyPerfInHCOfferedPackets_Object = MibTableColumn
agentDiffServPolicyPerfInHCOfferedPackets = _AgentDiffServPolicyPerfInHCOfferedPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 5, 1, 6),
    _AgentDiffServPolicyPerfInHCOfferedPackets_Type()
)
agentDiffServPolicyPerfInHCOfferedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfInHCOfferedPackets.setStatus("current")
_AgentDiffServPolicyPerfInHCDiscardedOctets_Type = Counter64
_AgentDiffServPolicyPerfInHCDiscardedOctets_Object = MibTableColumn
agentDiffServPolicyPerfInHCDiscardedOctets = _AgentDiffServPolicyPerfInHCDiscardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 5, 1, 7),
    _AgentDiffServPolicyPerfInHCDiscardedOctets_Type()
)
agentDiffServPolicyPerfInHCDiscardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfInHCDiscardedOctets.setStatus("current")
_AgentDiffServPolicyPerfInHCDiscardedPackets_Type = Counter64
_AgentDiffServPolicyPerfInHCDiscardedPackets_Object = MibTableColumn
agentDiffServPolicyPerfInHCDiscardedPackets = _AgentDiffServPolicyPerfInHCDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 5, 1, 8),
    _AgentDiffServPolicyPerfInHCDiscardedPackets_Type()
)
agentDiffServPolicyPerfInHCDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfInHCDiscardedPackets.setStatus("current")


class _AgentDiffServPolicyPerfInStorageType_Type(StorageType):
    """Custom type agentDiffServPolicyPerfInStorageType based on StorageType"""


_AgentDiffServPolicyPerfInStorageType_Object = MibTableColumn
agentDiffServPolicyPerfInStorageType = _AgentDiffServPolicyPerfInStorageType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 5, 1, 9),
    _AgentDiffServPolicyPerfInStorageType_Type()
)
agentDiffServPolicyPerfInStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfInStorageType.setStatus("current")
_AgentDiffServPolicyPerfInRowStatus_Type = RowStatus
_AgentDiffServPolicyPerfInRowStatus_Object = MibTableColumn
agentDiffServPolicyPerfInRowStatus = _AgentDiffServPolicyPerfInRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 5, 1, 10),
    _AgentDiffServPolicyPerfInRowStatus_Type()
)
agentDiffServPolicyPerfInRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfInRowStatus.setStatus("current")
_AgentDiffServPolicyPerfOutTable_Object = MibTable
agentDiffServPolicyPerfOutTable = _AgentDiffServPolicyPerfOutTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6)
)
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutTable.setStatus("current")
_AgentDiffServPolicyPerfOutEntry_Object = MibTableRow
agentDiffServPolicyPerfOutEntry = _AgentDiffServPolicyPerfOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1)
)
agentDiffServPolicyPerfOutEntry.setIndexNames(
    (0, "FASTPATH-QOS-DIFFSERV-PRIVATE-MIB", "agentDiffServPolicyIndex"),
    (0, "FASTPATH-QOS-DIFFSERV-PRIVATE-MIB", "agentDiffServPolicyInstIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutEntry.setStatus("current")
_AgentDiffServPolicyPerfOutTailDroppedOctets_Type = Counter32
_AgentDiffServPolicyPerfOutTailDroppedOctets_Object = MibTableColumn
agentDiffServPolicyPerfOutTailDroppedOctets = _AgentDiffServPolicyPerfOutTailDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 1),
    _AgentDiffServPolicyPerfOutTailDroppedOctets_Type()
)
agentDiffServPolicyPerfOutTailDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutTailDroppedOctets.setStatus("obsolete")
_AgentDiffServPolicyPerfOutTailDroppedPackets_Type = Counter32
_AgentDiffServPolicyPerfOutTailDroppedPackets_Object = MibTableColumn
agentDiffServPolicyPerfOutTailDroppedPackets = _AgentDiffServPolicyPerfOutTailDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 2),
    _AgentDiffServPolicyPerfOutTailDroppedPackets_Type()
)
agentDiffServPolicyPerfOutTailDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutTailDroppedPackets.setStatus("obsolete")
_AgentDiffServPolicyPerfOutRandomDroppedOctets_Type = Counter32
_AgentDiffServPolicyPerfOutRandomDroppedOctets_Object = MibTableColumn
agentDiffServPolicyPerfOutRandomDroppedOctets = _AgentDiffServPolicyPerfOutRandomDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 3),
    _AgentDiffServPolicyPerfOutRandomDroppedOctets_Type()
)
agentDiffServPolicyPerfOutRandomDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutRandomDroppedOctets.setStatus("obsolete")
_AgentDiffServPolicyPerfOutRandomDroppedPackets_Type = Counter32
_AgentDiffServPolicyPerfOutRandomDroppedPackets_Object = MibTableColumn
agentDiffServPolicyPerfOutRandomDroppedPackets = _AgentDiffServPolicyPerfOutRandomDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 4),
    _AgentDiffServPolicyPerfOutRandomDroppedPackets_Type()
)
agentDiffServPolicyPerfOutRandomDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutRandomDroppedPackets.setStatus("obsolete")
_AgentDiffServPolicyPerfOutShapeDelayedOctets_Type = Counter32
_AgentDiffServPolicyPerfOutShapeDelayedOctets_Object = MibTableColumn
agentDiffServPolicyPerfOutShapeDelayedOctets = _AgentDiffServPolicyPerfOutShapeDelayedOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 5),
    _AgentDiffServPolicyPerfOutShapeDelayedOctets_Type()
)
agentDiffServPolicyPerfOutShapeDelayedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutShapeDelayedOctets.setStatus("obsolete")
_AgentDiffServPolicyPerfOutShapeDelayedPackets_Type = Counter32
_AgentDiffServPolicyPerfOutShapeDelayedPackets_Object = MibTableColumn
agentDiffServPolicyPerfOutShapeDelayedPackets = _AgentDiffServPolicyPerfOutShapeDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 6),
    _AgentDiffServPolicyPerfOutShapeDelayedPackets_Type()
)
agentDiffServPolicyPerfOutShapeDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutShapeDelayedPackets.setStatus("obsolete")
_AgentDiffServPolicyPerfOutSentOctets_Type = Counter32
_AgentDiffServPolicyPerfOutSentOctets_Object = MibTableColumn
agentDiffServPolicyPerfOutSentOctets = _AgentDiffServPolicyPerfOutSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 7),
    _AgentDiffServPolicyPerfOutSentOctets_Type()
)
agentDiffServPolicyPerfOutSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutSentOctets.setStatus("obsolete")
_AgentDiffServPolicyPerfOutSentPackets_Type = Counter32
_AgentDiffServPolicyPerfOutSentPackets_Object = MibTableColumn
agentDiffServPolicyPerfOutSentPackets = _AgentDiffServPolicyPerfOutSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 8),
    _AgentDiffServPolicyPerfOutSentPackets_Type()
)
agentDiffServPolicyPerfOutSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutSentPackets.setStatus("obsolete")
_AgentDiffServPolicyPerfOutHCTailDroppedOctets_Type = Counter64
_AgentDiffServPolicyPerfOutHCTailDroppedOctets_Object = MibTableColumn
agentDiffServPolicyPerfOutHCTailDroppedOctets = _AgentDiffServPolicyPerfOutHCTailDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 9),
    _AgentDiffServPolicyPerfOutHCTailDroppedOctets_Type()
)
agentDiffServPolicyPerfOutHCTailDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutHCTailDroppedOctets.setStatus("obsolete")
_AgentDiffServPolicyPerfOutHCTailDroppedPackets_Type = Counter64
_AgentDiffServPolicyPerfOutHCTailDroppedPackets_Object = MibTableColumn
agentDiffServPolicyPerfOutHCTailDroppedPackets = _AgentDiffServPolicyPerfOutHCTailDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 10),
    _AgentDiffServPolicyPerfOutHCTailDroppedPackets_Type()
)
agentDiffServPolicyPerfOutHCTailDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutHCTailDroppedPackets.setStatus("obsolete")
_AgentDiffServPolicyPerfOutHCRandomDroppedOctets_Type = Counter64
_AgentDiffServPolicyPerfOutHCRandomDroppedOctets_Object = MibTableColumn
agentDiffServPolicyPerfOutHCRandomDroppedOctets = _AgentDiffServPolicyPerfOutHCRandomDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 11),
    _AgentDiffServPolicyPerfOutHCRandomDroppedOctets_Type()
)
agentDiffServPolicyPerfOutHCRandomDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutHCRandomDroppedOctets.setStatus("obsolete")
_AgentDiffServPolicyPerfOutHCRandomDroppedPackets_Type = Counter64
_AgentDiffServPolicyPerfOutHCRandomDroppedPackets_Object = MibTableColumn
agentDiffServPolicyPerfOutHCRandomDroppedPackets = _AgentDiffServPolicyPerfOutHCRandomDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 12),
    _AgentDiffServPolicyPerfOutHCRandomDroppedPackets_Type()
)
agentDiffServPolicyPerfOutHCRandomDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutHCRandomDroppedPackets.setStatus("obsolete")
_AgentDiffServPolicyPerfOutHCShapeDelayedOctets_Type = Counter64
_AgentDiffServPolicyPerfOutHCShapeDelayedOctets_Object = MibTableColumn
agentDiffServPolicyPerfOutHCShapeDelayedOctets = _AgentDiffServPolicyPerfOutHCShapeDelayedOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 13),
    _AgentDiffServPolicyPerfOutHCShapeDelayedOctets_Type()
)
agentDiffServPolicyPerfOutHCShapeDelayedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutHCShapeDelayedOctets.setStatus("obsolete")
_AgentDiffServPolicyPerfOutHCShapeDelayedPackets_Type = Counter64
_AgentDiffServPolicyPerfOutHCShapeDelayedPackets_Object = MibTableColumn
agentDiffServPolicyPerfOutHCShapeDelayedPackets = _AgentDiffServPolicyPerfOutHCShapeDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 14),
    _AgentDiffServPolicyPerfOutHCShapeDelayedPackets_Type()
)
agentDiffServPolicyPerfOutHCShapeDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutHCShapeDelayedPackets.setStatus("obsolete")
_AgentDiffServPolicyPerfOutHCSentOctets_Type = Counter64
_AgentDiffServPolicyPerfOutHCSentOctets_Object = MibTableColumn
agentDiffServPolicyPerfOutHCSentOctets = _AgentDiffServPolicyPerfOutHCSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 15),
    _AgentDiffServPolicyPerfOutHCSentOctets_Type()
)
agentDiffServPolicyPerfOutHCSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutHCSentOctets.setStatus("obsolete")
_AgentDiffServPolicyPerfOutHCSentPackets_Type = Counter64
_AgentDiffServPolicyPerfOutHCSentPackets_Object = MibTableColumn
agentDiffServPolicyPerfOutHCSentPackets = _AgentDiffServPolicyPerfOutHCSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 16),
    _AgentDiffServPolicyPerfOutHCSentPackets_Type()
)
agentDiffServPolicyPerfOutHCSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutHCSentPackets.setStatus("obsolete")


class _AgentDiffServPolicyPerfOutStorageType_Type(StorageType):
    """Custom type agentDiffServPolicyPerfOutStorageType based on StorageType"""


_AgentDiffServPolicyPerfOutStorageType_Object = MibTableColumn
agentDiffServPolicyPerfOutStorageType = _AgentDiffServPolicyPerfOutStorageType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 17),
    _AgentDiffServPolicyPerfOutStorageType_Type()
)
agentDiffServPolicyPerfOutStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutStorageType.setStatus("current")
_AgentDiffServPolicyPerfOutRowStatus_Type = RowStatus
_AgentDiffServPolicyPerfOutRowStatus_Object = MibTableColumn
agentDiffServPolicyPerfOutRowStatus = _AgentDiffServPolicyPerfOutRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 18),
    _AgentDiffServPolicyPerfOutRowStatus_Type()
)
agentDiffServPolicyPerfOutRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutRowStatus.setStatus("current")
_AgentDiffServPolicyPerfOutOfferedOctets_Type = Counter32
_AgentDiffServPolicyPerfOutOfferedOctets_Object = MibTableColumn
agentDiffServPolicyPerfOutOfferedOctets = _AgentDiffServPolicyPerfOutOfferedOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 19),
    _AgentDiffServPolicyPerfOutOfferedOctets_Type()
)
agentDiffServPolicyPerfOutOfferedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutOfferedOctets.setStatus("current")
_AgentDiffServPolicyPerfOutOfferedPackets_Type = Counter32
_AgentDiffServPolicyPerfOutOfferedPackets_Object = MibTableColumn
agentDiffServPolicyPerfOutOfferedPackets = _AgentDiffServPolicyPerfOutOfferedPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 20),
    _AgentDiffServPolicyPerfOutOfferedPackets_Type()
)
agentDiffServPolicyPerfOutOfferedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutOfferedPackets.setStatus("current")
_AgentDiffServPolicyPerfOutDiscardedOctets_Type = Counter32
_AgentDiffServPolicyPerfOutDiscardedOctets_Object = MibTableColumn
agentDiffServPolicyPerfOutDiscardedOctets = _AgentDiffServPolicyPerfOutDiscardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 21),
    _AgentDiffServPolicyPerfOutDiscardedOctets_Type()
)
agentDiffServPolicyPerfOutDiscardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutDiscardedOctets.setStatus("current")
_AgentDiffServPolicyPerfOutDiscardedPackets_Type = Counter32
_AgentDiffServPolicyPerfOutDiscardedPackets_Object = MibTableColumn
agentDiffServPolicyPerfOutDiscardedPackets = _AgentDiffServPolicyPerfOutDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 22),
    _AgentDiffServPolicyPerfOutDiscardedPackets_Type()
)
agentDiffServPolicyPerfOutDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutDiscardedPackets.setStatus("current")
_AgentDiffServPolicyPerfOutHCOfferedOctets_Type = Counter64
_AgentDiffServPolicyPerfOutHCOfferedOctets_Object = MibTableColumn
agentDiffServPolicyPerfOutHCOfferedOctets = _AgentDiffServPolicyPerfOutHCOfferedOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 23),
    _AgentDiffServPolicyPerfOutHCOfferedOctets_Type()
)
agentDiffServPolicyPerfOutHCOfferedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutHCOfferedOctets.setStatus("current")
_AgentDiffServPolicyPerfOutHCOfferedPackets_Type = Counter64
_AgentDiffServPolicyPerfOutHCOfferedPackets_Object = MibTableColumn
agentDiffServPolicyPerfOutHCOfferedPackets = _AgentDiffServPolicyPerfOutHCOfferedPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 24),
    _AgentDiffServPolicyPerfOutHCOfferedPackets_Type()
)
agentDiffServPolicyPerfOutHCOfferedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutHCOfferedPackets.setStatus("current")
_AgentDiffServPolicyPerfOutHCDiscardedOctets_Type = Counter64
_AgentDiffServPolicyPerfOutHCDiscardedOctets_Object = MibTableColumn
agentDiffServPolicyPerfOutHCDiscardedOctets = _AgentDiffServPolicyPerfOutHCDiscardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 25),
    _AgentDiffServPolicyPerfOutHCDiscardedOctets_Type()
)
agentDiffServPolicyPerfOutHCDiscardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutHCDiscardedOctets.setStatus("current")
_AgentDiffServPolicyPerfOutHCDiscardedPackets_Type = Counter64
_AgentDiffServPolicyPerfOutHCDiscardedPackets_Object = MibTableColumn
agentDiffServPolicyPerfOutHCDiscardedPackets = _AgentDiffServPolicyPerfOutHCDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 3, 6, 1, 26),
    _AgentDiffServPolicyPerfOutHCDiscardedPackets_Type()
)
agentDiffServPolicyPerfOutHCDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServPolicyPerfOutHCDiscardedPackets.setStatus("current")
_AgentDiffServServiceGroup_ObjectIdentity = ObjectIdentity
agentDiffServServiceGroup = _AgentDiffServServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4)
)
_AgentDiffServServiceTable_Object = MibTable
agentDiffServServiceTable = _AgentDiffServServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 1)
)
if mibBuilder.loadTexts:
    agentDiffServServiceTable.setStatus("current")
_AgentDiffServServiceEntry_Object = MibTableRow
agentDiffServServiceEntry = _AgentDiffServServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 1, 1)
)
agentDiffServServiceEntry.setIndexNames(
    (0, "FASTPATH-QOS-DIFFSERV-PRIVATE-MIB", "agentDiffServServiceIfIndex"),
    (0, "FASTPATH-QOS-DIFFSERV-PRIVATE-MIB", "agentDiffServServiceIfDirection"),
)
if mibBuilder.loadTexts:
    agentDiffServServiceEntry.setStatus("current")
_AgentDiffServServiceIfIndex_Type = InterfaceIndex
_AgentDiffServServiceIfIndex_Object = MibTableColumn
agentDiffServServiceIfIndex = _AgentDiffServServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 1, 1, 1),
    _AgentDiffServServiceIfIndex_Type()
)
agentDiffServServiceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDiffServServiceIfIndex.setStatus("current")
_AgentDiffServServiceIfDirection_Type = IntfDirection
_AgentDiffServServiceIfDirection_Object = MibTableColumn
agentDiffServServiceIfDirection = _AgentDiffServServiceIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 1, 1, 2),
    _AgentDiffServServiceIfDirection_Type()
)
agentDiffServServiceIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDiffServServiceIfDirection.setStatus("current")
_AgentDiffServServicePolicyIndex_Type = Unsigned32
_AgentDiffServServicePolicyIndex_Object = MibTableColumn
agentDiffServServicePolicyIndex = _AgentDiffServServicePolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 1, 1, 3),
    _AgentDiffServServicePolicyIndex_Type()
)
agentDiffServServicePolicyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServServicePolicyIndex.setStatus("current")


class _AgentDiffServServiceIfOperStatus_Type(Integer32):
    """Custom type agentDiffServServiceIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AgentDiffServServiceIfOperStatus_Type.__name__ = "Integer32"
_AgentDiffServServiceIfOperStatus_Object = MibTableColumn
agentDiffServServiceIfOperStatus = _AgentDiffServServiceIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 1, 1, 4),
    _AgentDiffServServiceIfOperStatus_Type()
)
agentDiffServServiceIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServServiceIfOperStatus.setStatus("current")


class _AgentDiffServServiceStorageType_Type(StorageType):
    """Custom type agentDiffServServiceStorageType based on StorageType"""


_AgentDiffServServiceStorageType_Object = MibTableColumn
agentDiffServServiceStorageType = _AgentDiffServServiceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 1, 1, 5),
    _AgentDiffServServiceStorageType_Type()
)
agentDiffServServiceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServServiceStorageType.setStatus("current")
_AgentDiffServServiceRowStatus_Type = RowStatus
_AgentDiffServServiceRowStatus_Object = MibTableColumn
agentDiffServServiceRowStatus = _AgentDiffServServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 1, 1, 6),
    _AgentDiffServServiceRowStatus_Type()
)
agentDiffServServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDiffServServiceRowStatus.setStatus("current")
_AgentDiffServServicePerfTable_Object = MibTable
agentDiffServServicePerfTable = _AgentDiffServServicePerfTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 2)
)
if mibBuilder.loadTexts:
    agentDiffServServicePerfTable.setStatus("current")
_AgentDiffServServicePerfEntry_Object = MibTableRow
agentDiffServServicePerfEntry = _AgentDiffServServicePerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 2, 1)
)
if mibBuilder.loadTexts:
    agentDiffServServicePerfEntry.setStatus("current")
_AgentDiffServServicePerfOfferedOctets_Type = Counter32
_AgentDiffServServicePerfOfferedOctets_Object = MibTableColumn
agentDiffServServicePerfOfferedOctets = _AgentDiffServServicePerfOfferedOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 2, 1, 1),
    _AgentDiffServServicePerfOfferedOctets_Type()
)
agentDiffServServicePerfOfferedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServServicePerfOfferedOctets.setStatus("current")
_AgentDiffServServicePerfOfferedPackets_Type = Counter32
_AgentDiffServServicePerfOfferedPackets_Object = MibTableColumn
agentDiffServServicePerfOfferedPackets = _AgentDiffServServicePerfOfferedPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 2, 1, 2),
    _AgentDiffServServicePerfOfferedPackets_Type()
)
agentDiffServServicePerfOfferedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServServicePerfOfferedPackets.setStatus("current")
_AgentDiffServServicePerfDiscardedOctets_Type = Counter32
_AgentDiffServServicePerfDiscardedOctets_Object = MibTableColumn
agentDiffServServicePerfDiscardedOctets = _AgentDiffServServicePerfDiscardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 2, 1, 3),
    _AgentDiffServServicePerfDiscardedOctets_Type()
)
agentDiffServServicePerfDiscardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServServicePerfDiscardedOctets.setStatus("current")
_AgentDiffServServicePerfDiscardedPackets_Type = Counter32
_AgentDiffServServicePerfDiscardedPackets_Object = MibTableColumn
agentDiffServServicePerfDiscardedPackets = _AgentDiffServServicePerfDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 2, 1, 4),
    _AgentDiffServServicePerfDiscardedPackets_Type()
)
agentDiffServServicePerfDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServServicePerfDiscardedPackets.setStatus("current")
_AgentDiffServServicePerfSentOctets_Type = Counter32
_AgentDiffServServicePerfSentOctets_Object = MibTableColumn
agentDiffServServicePerfSentOctets = _AgentDiffServServicePerfSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 2, 1, 5),
    _AgentDiffServServicePerfSentOctets_Type()
)
agentDiffServServicePerfSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServServicePerfSentOctets.setStatus("current")
_AgentDiffServServicePerfSentPackets_Type = Counter32
_AgentDiffServServicePerfSentPackets_Object = MibTableColumn
agentDiffServServicePerfSentPackets = _AgentDiffServServicePerfSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 2, 1, 6),
    _AgentDiffServServicePerfSentPackets_Type()
)
agentDiffServServicePerfSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServServicePerfSentPackets.setStatus("current")
_AgentDiffServServicePerfHCOfferedOctets_Type = Counter64
_AgentDiffServServicePerfHCOfferedOctets_Object = MibTableColumn
agentDiffServServicePerfHCOfferedOctets = _AgentDiffServServicePerfHCOfferedOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 2, 1, 7),
    _AgentDiffServServicePerfHCOfferedOctets_Type()
)
agentDiffServServicePerfHCOfferedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServServicePerfHCOfferedOctets.setStatus("current")
_AgentDiffServServicePerfHCOfferedPackets_Type = Counter64
_AgentDiffServServicePerfHCOfferedPackets_Object = MibTableColumn
agentDiffServServicePerfHCOfferedPackets = _AgentDiffServServicePerfHCOfferedPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 2, 1, 8),
    _AgentDiffServServicePerfHCOfferedPackets_Type()
)
agentDiffServServicePerfHCOfferedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServServicePerfHCOfferedPackets.setStatus("current")
_AgentDiffServServicePerfHCDiscardedOctets_Type = Counter64
_AgentDiffServServicePerfHCDiscardedOctets_Object = MibTableColumn
agentDiffServServicePerfHCDiscardedOctets = _AgentDiffServServicePerfHCDiscardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 2, 1, 9),
    _AgentDiffServServicePerfHCDiscardedOctets_Type()
)
agentDiffServServicePerfHCDiscardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServServicePerfHCDiscardedOctets.setStatus("current")
_AgentDiffServServicePerfHCDiscardedPackets_Type = Counter64
_AgentDiffServServicePerfHCDiscardedPackets_Object = MibTableColumn
agentDiffServServicePerfHCDiscardedPackets = _AgentDiffServServicePerfHCDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 2, 1, 10),
    _AgentDiffServServicePerfHCDiscardedPackets_Type()
)
agentDiffServServicePerfHCDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServServicePerfHCDiscardedPackets.setStatus("current")
_AgentDiffServServicePerfHCSentOctets_Type = Counter64
_AgentDiffServServicePerfHCSentOctets_Object = MibTableColumn
agentDiffServServicePerfHCSentOctets = _AgentDiffServServicePerfHCSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 2, 1, 11),
    _AgentDiffServServicePerfHCSentOctets_Type()
)
agentDiffServServicePerfHCSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServServicePerfHCSentOctets.setStatus("current")
_AgentDiffServServicePerfHCSentPackets_Type = Counter64
_AgentDiffServServicePerfHCSentPackets_Object = MibTableColumn
agentDiffServServicePerfHCSentPackets = _AgentDiffServServicePerfHCSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 7, 4, 2, 1, 12),
    _AgentDiffServServicePerfHCSentPackets_Type()
)
agentDiffServServicePerfHCSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDiffServServicePerfHCSentPackets.setStatus("current")
agentDiffServServiceEntry.registerAugmentions(
    ("FASTPATH-QOS-DIFFSERV-PRIVATE-MIB",
     "agentDiffServServicePerfEntry")
)
agentDiffServServicePerfEntry.setIndexNames(*agentDiffServServiceEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FASTPATH-QOS-DIFFSERV-PRIVATE-MIB",
    **{"QosBurstSize": QosBurstSize,
       "IntfDirection": IntfDirection,
       "EtypeValue": EtypeValue,
       "Ipv6AddressPrefix": Ipv6AddressPrefix,
       "fastPathQOSDiffServPrivate": fastPathQOSDiffServPrivate,
       "agentDiffServGenStatusGroup": agentDiffServGenStatusGroup,
       "agentDiffServGenStatusAdminMode": agentDiffServGenStatusAdminMode,
       "agentDiffServGenStatusClassTableSize": agentDiffServGenStatusClassTableSize,
       "agentDiffServGenStatusClassTableMax": agentDiffServGenStatusClassTableMax,
       "agentDiffServGenStatusClassRuleTableSize": agentDiffServGenStatusClassRuleTableSize,
       "agentDiffServGenStatusClassRuleTableMax": agentDiffServGenStatusClassRuleTableMax,
       "agentDiffServGenStatusPolicyTableSize": agentDiffServGenStatusPolicyTableSize,
       "agentDiffServGenStatusPolicyTableMax": agentDiffServGenStatusPolicyTableMax,
       "agentDiffServGenStatusPolicyInstTableSize": agentDiffServGenStatusPolicyInstTableSize,
       "agentDiffServGenStatusPolicyInstTableMax": agentDiffServGenStatusPolicyInstTableMax,
       "agentDiffServGenStatusPolicyAttrTableSize": agentDiffServGenStatusPolicyAttrTableSize,
       "agentDiffServGenStatusPolicyAttrTableMax": agentDiffServGenStatusPolicyAttrTableMax,
       "agentDiffServGenStatusServiceTableSize": agentDiffServGenStatusServiceTableSize,
       "agentDiffServGenStatusServiceTableMax": agentDiffServGenStatusServiceTableMax,
       "agentDiffServClassGroup": agentDiffServClassGroup,
       "agentDiffServClassIndexNextFree": agentDiffServClassIndexNextFree,
       "agentDiffServClassTable": agentDiffServClassTable,
       "agentDiffServClassEntry": agentDiffServClassEntry,
       "agentDiffServClassIndex": agentDiffServClassIndex,
       "agentDiffServClassName": agentDiffServClassName,
       "agentDiffServClassType": agentDiffServClassType,
       "agentDiffServClassAclNum": agentDiffServClassAclNum,
       "agentDiffServClassRuleIndexNextFree": agentDiffServClassRuleIndexNextFree,
       "agentDiffServClassStorageType": agentDiffServClassStorageType,
       "agentDiffServClassRowStatus": agentDiffServClassRowStatus,
       "agentDiffServClassAclType": agentDiffServClassAclType,
       "agentDiffServClassProtoType": agentDiffServClassProtoType,
       "agentDiffServClassRuleTable": agentDiffServClassRuleTable,
       "agentDiffServClassRuleEntry": agentDiffServClassRuleEntry,
       "agentDiffServClassRuleIndex": agentDiffServClassRuleIndex,
       "agentDiffServClassRuleMatchEntryType": agentDiffServClassRuleMatchEntryType,
       "agentDiffServClassRuleMatchCos": agentDiffServClassRuleMatchCos,
       "agentDiffServClassRuleMatchDstIpAddr": agentDiffServClassRuleMatchDstIpAddr,
       "agentDiffServClassRuleMatchDstIpMask": agentDiffServClassRuleMatchDstIpMask,
       "agentDiffServClassRuleMatchDstL4PortStart": agentDiffServClassRuleMatchDstL4PortStart,
       "agentDiffServClassRuleMatchDstL4PortEnd": agentDiffServClassRuleMatchDstL4PortEnd,
       "agentDiffServClassRuleMatchDstMacAddr": agentDiffServClassRuleMatchDstMacAddr,
       "agentDiffServClassRuleMatchDstMacMask": agentDiffServClassRuleMatchDstMacMask,
       "agentDiffServClassRuleMatchEvery": agentDiffServClassRuleMatchEvery,
       "agentDiffServClassRuleMatchIpDscp": agentDiffServClassRuleMatchIpDscp,
       "agentDiffServClassRuleMatchIpPrecedence": agentDiffServClassRuleMatchIpPrecedence,
       "agentDiffServClassRuleMatchIpTosBits": agentDiffServClassRuleMatchIpTosBits,
       "agentDiffServClassRuleMatchIpTosMask": agentDiffServClassRuleMatchIpTosMask,
       "agentDiffServClassRuleMatchProtocolNum": agentDiffServClassRuleMatchProtocolNum,
       "agentDiffServClassRuleMatchRefClassIndex": agentDiffServClassRuleMatchRefClassIndex,
       "agentDiffServClassRuleMatchSrcIpAddr": agentDiffServClassRuleMatchSrcIpAddr,
       "agentDiffServClassRuleMatchSrcIpMask": agentDiffServClassRuleMatchSrcIpMask,
       "agentDiffServClassRuleMatchSrcL4PortStart": agentDiffServClassRuleMatchSrcL4PortStart,
       "agentDiffServClassRuleMatchSrcL4PortEnd": agentDiffServClassRuleMatchSrcL4PortEnd,
       "agentDiffServClassRuleMatchSrcMacAddr": agentDiffServClassRuleMatchSrcMacAddr,
       "agentDiffServClassRuleMatchSrcMacMask": agentDiffServClassRuleMatchSrcMacMask,
       "agentDiffServClassRuleMatchVlanId": agentDiffServClassRuleMatchVlanId,
       "agentDiffServClassRuleMatchExcludeFlag": agentDiffServClassRuleMatchExcludeFlag,
       "agentDiffServClassRuleStorageType": agentDiffServClassRuleStorageType,
       "agentDiffServClassRuleRowStatus": agentDiffServClassRuleRowStatus,
       "agentDiffServClassRuleMatchCos2": agentDiffServClassRuleMatchCos2,
       "agentDiffServClassRuleMatchEtypeKey": agentDiffServClassRuleMatchEtypeKey,
       "agentDiffServClassRuleMatchEtypeValue": agentDiffServClassRuleMatchEtypeValue,
       "agentDiffServClassRuleMatchVlanIdStart": agentDiffServClassRuleMatchVlanIdStart,
       "agentDiffServClassRuleMatchVlanIdEnd": agentDiffServClassRuleMatchVlanIdEnd,
       "agentDiffServClassRuleMatchVlanId2Start": agentDiffServClassRuleMatchVlanId2Start,
       "agentDiffServClassRuleMatchVlanId2End": agentDiffServClassRuleMatchVlanId2End,
       "agentDiffServClassRuleMatchFlowLabel": agentDiffServClassRuleMatchFlowLabel,
       "agentDiffServClassRuleMatchDstIpv6Prefix": agentDiffServClassRuleMatchDstIpv6Prefix,
       "agentDiffServClassRuleMatchSrcIpv6Prefix": agentDiffServClassRuleMatchSrcIpv6Prefix,
       "agentDiffServClassRuleMatchDstIpv6PrefixLength": agentDiffServClassRuleMatchDstIpv6PrefixLength,
       "agentDiffServClassRuleMatchSrcIpv6PrefixLength": agentDiffServClassRuleMatchSrcIpv6PrefixLength,
       "agentDiffServPolicyGroup": agentDiffServPolicyGroup,
       "agentDiffServPolicyIndexNextFree": agentDiffServPolicyIndexNextFree,
       "agentDiffServPolicyTable": agentDiffServPolicyTable,
       "agentDiffServPolicyEntry": agentDiffServPolicyEntry,
       "agentDiffServPolicyIndex": agentDiffServPolicyIndex,
       "agentDiffServPolicyName": agentDiffServPolicyName,
       "agentDiffServPolicyType": agentDiffServPolicyType,
       "agentDiffServPolicyInstIndexNextFree": agentDiffServPolicyInstIndexNextFree,
       "agentDiffServPolicyStorageType": agentDiffServPolicyStorageType,
       "agentDiffServPolicyRowStatus": agentDiffServPolicyRowStatus,
       "agentDiffServPolicyInstTable": agentDiffServPolicyInstTable,
       "agentDiffServPolicyInstEntry": agentDiffServPolicyInstEntry,
       "agentDiffServPolicyInstIndex": agentDiffServPolicyInstIndex,
       "agentDiffServPolicyInstClassIndex": agentDiffServPolicyInstClassIndex,
       "agentDiffServPolicyInstAttrIndexNextFree": agentDiffServPolicyInstAttrIndexNextFree,
       "agentDiffServPolicyInstStorageType": agentDiffServPolicyInstStorageType,
       "agentDiffServPolicyInstRowStatus": agentDiffServPolicyInstRowStatus,
       "agentDiffServPolicyAttrTable": agentDiffServPolicyAttrTable,
       "agentDiffServPolicyAttrEntry": agentDiffServPolicyAttrEntry,
       "agentDiffServPolicyAttrIndex": agentDiffServPolicyAttrIndex,
       "agentDiffServPolicyAttrStmtEntryType": agentDiffServPolicyAttrStmtEntryType,
       "agentDiffServPolicyAttrStmtBandwidthCrate": agentDiffServPolicyAttrStmtBandwidthCrate,
       "agentDiffServPolicyAttrStmtBandwidthCrateUnits": agentDiffServPolicyAttrStmtBandwidthCrateUnits,
       "agentDiffServPolicyAttrStmtExpediteCrate": agentDiffServPolicyAttrStmtExpediteCrate,
       "agentDiffServPolicyAttrStmtExpediteCrateUnits": agentDiffServPolicyAttrStmtExpediteCrateUnits,
       "agentDiffServPolicyAttrStmtExpediteCburst": agentDiffServPolicyAttrStmtExpediteCburst,
       "agentDiffServPolicyAttrStmtMarkCosVal": agentDiffServPolicyAttrStmtMarkCosVal,
       "agentDiffServPolicyAttrStmtMarkIpDscpVal": agentDiffServPolicyAttrStmtMarkIpDscpVal,
       "agentDiffServPolicyAttrStmtMarkIpPrecedenceVal": agentDiffServPolicyAttrStmtMarkIpPrecedenceVal,
       "agentDiffServPolicyAttrStmtPoliceConformAct": agentDiffServPolicyAttrStmtPoliceConformAct,
       "agentDiffServPolicyAttrStmtPoliceConformVal": agentDiffServPolicyAttrStmtPoliceConformVal,
       "agentDiffServPolicyAttrStmtPoliceExceedAct": agentDiffServPolicyAttrStmtPoliceExceedAct,
       "agentDiffServPolicyAttrStmtPoliceExceedVal": agentDiffServPolicyAttrStmtPoliceExceedVal,
       "agentDiffServPolicyAttrStmtPoliceNonconformAct": agentDiffServPolicyAttrStmtPoliceNonconformAct,
       "agentDiffServPolicyAttrStmtPoliceNonconformVal": agentDiffServPolicyAttrStmtPoliceNonconformVal,
       "agentDiffServPolicyAttrStmtPoliceSimpleCrate": agentDiffServPolicyAttrStmtPoliceSimpleCrate,
       "agentDiffServPolicyAttrStmtPoliceSimpleCburst": agentDiffServPolicyAttrStmtPoliceSimpleCburst,
       "agentDiffServPolicyAttrStmtPoliceSinglerateCrate": agentDiffServPolicyAttrStmtPoliceSinglerateCrate,
       "agentDiffServPolicyAttrStmtPoliceSinglerateCburst": agentDiffServPolicyAttrStmtPoliceSinglerateCburst,
       "agentDiffServPolicyAttrStmtPoliceSinglerateEburst": agentDiffServPolicyAttrStmtPoliceSinglerateEburst,
       "agentDiffServPolicyAttrStmtPoliceTworateCrate": agentDiffServPolicyAttrStmtPoliceTworateCrate,
       "agentDiffServPolicyAttrStmtPoliceTworateCburst": agentDiffServPolicyAttrStmtPoliceTworateCburst,
       "agentDiffServPolicyAttrStmtPoliceTworatePrate": agentDiffServPolicyAttrStmtPoliceTworatePrate,
       "agentDiffServPolicyAttrStmtPoliceTworatePburst": agentDiffServPolicyAttrStmtPoliceTworatePburst,
       "agentDiffServPolicyAttrStmtRandomdropMinThresh": agentDiffServPolicyAttrStmtRandomdropMinThresh,
       "agentDiffServPolicyAttrStmtRandomdropMaxThresh": agentDiffServPolicyAttrStmtRandomdropMaxThresh,
       "agentDiffServPolicyAttrStmtRandomdropMaxDropProb": agentDiffServPolicyAttrStmtRandomdropMaxDropProb,
       "agentDiffServPolicyAttrStmtRandomdropSamplingRate": agentDiffServPolicyAttrStmtRandomdropSamplingRate,
       "agentDiffServPolicyAttrStmtRandomdropDecayExponent": agentDiffServPolicyAttrStmtRandomdropDecayExponent,
       "agentDiffServPolicyAttrStmtShapeAverageCrate": agentDiffServPolicyAttrStmtShapeAverageCrate,
       "agentDiffServPolicyAttrStmtShapePeakCrate": agentDiffServPolicyAttrStmtShapePeakCrate,
       "agentDiffServPolicyAttrStmtShapePeakPrate": agentDiffServPolicyAttrStmtShapePeakPrate,
       "agentDiffServPolicyAttrStorageType": agentDiffServPolicyAttrStorageType,
       "agentDiffServPolicyAttrRowStatus": agentDiffServPolicyAttrRowStatus,
       "agentDiffServPolicyAttrStmtAssignQueueId": agentDiffServPolicyAttrStmtAssignQueueId,
       "agentDiffServPolicyAttrStmtDrop": agentDiffServPolicyAttrStmtDrop,
       "agentDiffServPolicyAttrStmtMarkCos2Val": agentDiffServPolicyAttrStmtMarkCos2Val,
       "agentDiffServPolicyAttrStmtPoliceColorConformIndex": agentDiffServPolicyAttrStmtPoliceColorConformIndex,
       "agentDiffServPolicyAttrStmtPoliceColorConformMode": agentDiffServPolicyAttrStmtPoliceColorConformMode,
       "agentDiffServPolicyAttrStmtPoliceColorConformVal": agentDiffServPolicyAttrStmtPoliceColorConformVal,
       "agentDiffServPolicyAttrStmtPoliceColorExceedIndex": agentDiffServPolicyAttrStmtPoliceColorExceedIndex,
       "agentDiffServPolicyAttrStmtPoliceColorExceedMode": agentDiffServPolicyAttrStmtPoliceColorExceedMode,
       "agentDiffServPolicyAttrStmtPoliceColorExceedVal": agentDiffServPolicyAttrStmtPoliceColorExceedVal,
       "agentDiffServPolicyAttrStmtRedirectIntf": agentDiffServPolicyAttrStmtRedirectIntf,
       "agentDiffServPolicyAttrStmtMirrorIntf": agentDiffServPolicyAttrStmtMirrorIntf,
       "agentDiffServPolicyAttrStmtMarkCosAsSecCos": agentDiffServPolicyAttrStmtMarkCosAsSecCos,
       "agentDiffServPolicyPerfInTable": agentDiffServPolicyPerfInTable,
       "agentDiffServPolicyPerfInEntry": agentDiffServPolicyPerfInEntry,
       "agentDiffServPolicyPerfInOfferedOctets": agentDiffServPolicyPerfInOfferedOctets,
       "agentDiffServPolicyPerfInOfferedPackets": agentDiffServPolicyPerfInOfferedPackets,
       "agentDiffServPolicyPerfInDiscardedOctets": agentDiffServPolicyPerfInDiscardedOctets,
       "agentDiffServPolicyPerfInDiscardedPackets": agentDiffServPolicyPerfInDiscardedPackets,
       "agentDiffServPolicyPerfInHCOfferedOctets": agentDiffServPolicyPerfInHCOfferedOctets,
       "agentDiffServPolicyPerfInHCOfferedPackets": agentDiffServPolicyPerfInHCOfferedPackets,
       "agentDiffServPolicyPerfInHCDiscardedOctets": agentDiffServPolicyPerfInHCDiscardedOctets,
       "agentDiffServPolicyPerfInHCDiscardedPackets": agentDiffServPolicyPerfInHCDiscardedPackets,
       "agentDiffServPolicyPerfInStorageType": agentDiffServPolicyPerfInStorageType,
       "agentDiffServPolicyPerfInRowStatus": agentDiffServPolicyPerfInRowStatus,
       "agentDiffServPolicyPerfOutTable": agentDiffServPolicyPerfOutTable,
       "agentDiffServPolicyPerfOutEntry": agentDiffServPolicyPerfOutEntry,
       "agentDiffServPolicyPerfOutTailDroppedOctets": agentDiffServPolicyPerfOutTailDroppedOctets,
       "agentDiffServPolicyPerfOutTailDroppedPackets": agentDiffServPolicyPerfOutTailDroppedPackets,
       "agentDiffServPolicyPerfOutRandomDroppedOctets": agentDiffServPolicyPerfOutRandomDroppedOctets,
       "agentDiffServPolicyPerfOutRandomDroppedPackets": agentDiffServPolicyPerfOutRandomDroppedPackets,
       "agentDiffServPolicyPerfOutShapeDelayedOctets": agentDiffServPolicyPerfOutShapeDelayedOctets,
       "agentDiffServPolicyPerfOutShapeDelayedPackets": agentDiffServPolicyPerfOutShapeDelayedPackets,
       "agentDiffServPolicyPerfOutSentOctets": agentDiffServPolicyPerfOutSentOctets,
       "agentDiffServPolicyPerfOutSentPackets": agentDiffServPolicyPerfOutSentPackets,
       "agentDiffServPolicyPerfOutHCTailDroppedOctets": agentDiffServPolicyPerfOutHCTailDroppedOctets,
       "agentDiffServPolicyPerfOutHCTailDroppedPackets": agentDiffServPolicyPerfOutHCTailDroppedPackets,
       "agentDiffServPolicyPerfOutHCRandomDroppedOctets": agentDiffServPolicyPerfOutHCRandomDroppedOctets,
       "agentDiffServPolicyPerfOutHCRandomDroppedPackets": agentDiffServPolicyPerfOutHCRandomDroppedPackets,
       "agentDiffServPolicyPerfOutHCShapeDelayedOctets": agentDiffServPolicyPerfOutHCShapeDelayedOctets,
       "agentDiffServPolicyPerfOutHCShapeDelayedPackets": agentDiffServPolicyPerfOutHCShapeDelayedPackets,
       "agentDiffServPolicyPerfOutHCSentOctets": agentDiffServPolicyPerfOutHCSentOctets,
       "agentDiffServPolicyPerfOutHCSentPackets": agentDiffServPolicyPerfOutHCSentPackets,
       "agentDiffServPolicyPerfOutStorageType": agentDiffServPolicyPerfOutStorageType,
       "agentDiffServPolicyPerfOutRowStatus": agentDiffServPolicyPerfOutRowStatus,
       "agentDiffServPolicyPerfOutOfferedOctets": agentDiffServPolicyPerfOutOfferedOctets,
       "agentDiffServPolicyPerfOutOfferedPackets": agentDiffServPolicyPerfOutOfferedPackets,
       "agentDiffServPolicyPerfOutDiscardedOctets": agentDiffServPolicyPerfOutDiscardedOctets,
       "agentDiffServPolicyPerfOutDiscardedPackets": agentDiffServPolicyPerfOutDiscardedPackets,
       "agentDiffServPolicyPerfOutHCOfferedOctets": agentDiffServPolicyPerfOutHCOfferedOctets,
       "agentDiffServPolicyPerfOutHCOfferedPackets": agentDiffServPolicyPerfOutHCOfferedPackets,
       "agentDiffServPolicyPerfOutHCDiscardedOctets": agentDiffServPolicyPerfOutHCDiscardedOctets,
       "agentDiffServPolicyPerfOutHCDiscardedPackets": agentDiffServPolicyPerfOutHCDiscardedPackets,
       "agentDiffServServiceGroup": agentDiffServServiceGroup,
       "agentDiffServServiceTable": agentDiffServServiceTable,
       "agentDiffServServiceEntry": agentDiffServServiceEntry,
       "agentDiffServServiceIfIndex": agentDiffServServiceIfIndex,
       "agentDiffServServiceIfDirection": agentDiffServServiceIfDirection,
       "agentDiffServServicePolicyIndex": agentDiffServServicePolicyIndex,
       "agentDiffServServiceIfOperStatus": agentDiffServServiceIfOperStatus,
       "agentDiffServServiceStorageType": agentDiffServServiceStorageType,
       "agentDiffServServiceRowStatus": agentDiffServServiceRowStatus,
       "agentDiffServServicePerfTable": agentDiffServServicePerfTable,
       "agentDiffServServicePerfEntry": agentDiffServServicePerfEntry,
       "agentDiffServServicePerfOfferedOctets": agentDiffServServicePerfOfferedOctets,
       "agentDiffServServicePerfOfferedPackets": agentDiffServServicePerfOfferedPackets,
       "agentDiffServServicePerfDiscardedOctets": agentDiffServServicePerfDiscardedOctets,
       "agentDiffServServicePerfDiscardedPackets": agentDiffServServicePerfDiscardedPackets,
       "agentDiffServServicePerfSentOctets": agentDiffServServicePerfSentOctets,
       "agentDiffServServicePerfSentPackets": agentDiffServServicePerfSentPackets,
       "agentDiffServServicePerfHCOfferedOctets": agentDiffServServicePerfHCOfferedOctets,
       "agentDiffServServicePerfHCOfferedPackets": agentDiffServServicePerfHCOfferedPackets,
       "agentDiffServServicePerfHCDiscardedOctets": agentDiffServServicePerfHCDiscardedOctets,
       "agentDiffServServicePerfHCDiscardedPackets": agentDiffServServicePerfHCDiscardedPackets,
       "agentDiffServServicePerfHCSentOctets": agentDiffServServicePerfHCSentOctets,
       "agentDiffServServicePerfHCSentPackets": agentDiffServServicePerfHCSentPackets}
)

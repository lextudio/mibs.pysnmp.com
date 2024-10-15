# SNMP MIB module (HM2-PLATFORM-QOS-DIFFSERV-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-PLATFORM-QOS-DIFFSERV-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:21 2024
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

(HmEnabledStatus,
 hm2PlatformMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2PlatformMibs")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hm2PlatformQOSDiffServPrivate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7)
)
hm2PlatformQOSDiffServPrivate.setRevisions(
        ("2011-10-28 00:00",)
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

_Hm2AgentDiffServGenStatusGroup_ObjectIdentity = ObjectIdentity
hm2AgentDiffServGenStatusGroup = _Hm2AgentDiffServGenStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 1)
)


class _Hm2AgentDiffServGenStatusAdminMode_Type(HmEnabledStatus):
    """Custom type hm2AgentDiffServGenStatusAdminMode based on HmEnabledStatus"""


_Hm2AgentDiffServGenStatusAdminMode_Object = MibScalar
hm2AgentDiffServGenStatusAdminMode = _Hm2AgentDiffServGenStatusAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 1, 1),
    _Hm2AgentDiffServGenStatusAdminMode_Type()
)
hm2AgentDiffServGenStatusAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDiffServGenStatusAdminMode.setStatus("current")
_Hm2AgentDiffServGenStatusClassTableSize_Type = Unsigned32
_Hm2AgentDiffServGenStatusClassTableSize_Object = MibScalar
hm2AgentDiffServGenStatusClassTableSize = _Hm2AgentDiffServGenStatusClassTableSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 1, 2),
    _Hm2AgentDiffServGenStatusClassTableSize_Type()
)
hm2AgentDiffServGenStatusClassTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServGenStatusClassTableSize.setStatus("current")
_Hm2AgentDiffServGenStatusClassTableMax_Type = Unsigned32
_Hm2AgentDiffServGenStatusClassTableMax_Object = MibScalar
hm2AgentDiffServGenStatusClassTableMax = _Hm2AgentDiffServGenStatusClassTableMax_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 1, 3),
    _Hm2AgentDiffServGenStatusClassTableMax_Type()
)
hm2AgentDiffServGenStatusClassTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServGenStatusClassTableMax.setStatus("current")
_Hm2AgentDiffServGenStatusClassRuleTableSize_Type = Unsigned32
_Hm2AgentDiffServGenStatusClassRuleTableSize_Object = MibScalar
hm2AgentDiffServGenStatusClassRuleTableSize = _Hm2AgentDiffServGenStatusClassRuleTableSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 1, 4),
    _Hm2AgentDiffServGenStatusClassRuleTableSize_Type()
)
hm2AgentDiffServGenStatusClassRuleTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServGenStatusClassRuleTableSize.setStatus("current")
_Hm2AgentDiffServGenStatusClassRuleTableMax_Type = Unsigned32
_Hm2AgentDiffServGenStatusClassRuleTableMax_Object = MibScalar
hm2AgentDiffServGenStatusClassRuleTableMax = _Hm2AgentDiffServGenStatusClassRuleTableMax_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 1, 5),
    _Hm2AgentDiffServGenStatusClassRuleTableMax_Type()
)
hm2AgentDiffServGenStatusClassRuleTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServGenStatusClassRuleTableMax.setStatus("current")
_Hm2AgentDiffServGenStatusPolicyTableSize_Type = Unsigned32
_Hm2AgentDiffServGenStatusPolicyTableSize_Object = MibScalar
hm2AgentDiffServGenStatusPolicyTableSize = _Hm2AgentDiffServGenStatusPolicyTableSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 1, 6),
    _Hm2AgentDiffServGenStatusPolicyTableSize_Type()
)
hm2AgentDiffServGenStatusPolicyTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServGenStatusPolicyTableSize.setStatus("current")
_Hm2AgentDiffServGenStatusPolicyTableMax_Type = Unsigned32
_Hm2AgentDiffServGenStatusPolicyTableMax_Object = MibScalar
hm2AgentDiffServGenStatusPolicyTableMax = _Hm2AgentDiffServGenStatusPolicyTableMax_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 1, 7),
    _Hm2AgentDiffServGenStatusPolicyTableMax_Type()
)
hm2AgentDiffServGenStatusPolicyTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServGenStatusPolicyTableMax.setStatus("current")
_Hm2AgentDiffServGenStatusPolicyInstTableSize_Type = Unsigned32
_Hm2AgentDiffServGenStatusPolicyInstTableSize_Object = MibScalar
hm2AgentDiffServGenStatusPolicyInstTableSize = _Hm2AgentDiffServGenStatusPolicyInstTableSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 1, 8),
    _Hm2AgentDiffServGenStatusPolicyInstTableSize_Type()
)
hm2AgentDiffServGenStatusPolicyInstTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServGenStatusPolicyInstTableSize.setStatus("current")
_Hm2AgentDiffServGenStatusPolicyInstTableMax_Type = Unsigned32
_Hm2AgentDiffServGenStatusPolicyInstTableMax_Object = MibScalar
hm2AgentDiffServGenStatusPolicyInstTableMax = _Hm2AgentDiffServGenStatusPolicyInstTableMax_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 1, 9),
    _Hm2AgentDiffServGenStatusPolicyInstTableMax_Type()
)
hm2AgentDiffServGenStatusPolicyInstTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServGenStatusPolicyInstTableMax.setStatus("current")
_Hm2AgentDiffServGenStatusPolicyAttrTableSize_Type = Unsigned32
_Hm2AgentDiffServGenStatusPolicyAttrTableSize_Object = MibScalar
hm2AgentDiffServGenStatusPolicyAttrTableSize = _Hm2AgentDiffServGenStatusPolicyAttrTableSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 1, 10),
    _Hm2AgentDiffServGenStatusPolicyAttrTableSize_Type()
)
hm2AgentDiffServGenStatusPolicyAttrTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServGenStatusPolicyAttrTableSize.setStatus("current")
_Hm2AgentDiffServGenStatusPolicyAttrTableMax_Type = Unsigned32
_Hm2AgentDiffServGenStatusPolicyAttrTableMax_Object = MibScalar
hm2AgentDiffServGenStatusPolicyAttrTableMax = _Hm2AgentDiffServGenStatusPolicyAttrTableMax_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 1, 11),
    _Hm2AgentDiffServGenStatusPolicyAttrTableMax_Type()
)
hm2AgentDiffServGenStatusPolicyAttrTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServGenStatusPolicyAttrTableMax.setStatus("current")
_Hm2AgentDiffServGenStatusServiceTableSize_Type = Unsigned32
_Hm2AgentDiffServGenStatusServiceTableSize_Object = MibScalar
hm2AgentDiffServGenStatusServiceTableSize = _Hm2AgentDiffServGenStatusServiceTableSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 1, 12),
    _Hm2AgentDiffServGenStatusServiceTableSize_Type()
)
hm2AgentDiffServGenStatusServiceTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServGenStatusServiceTableSize.setStatus("current")
_Hm2AgentDiffServGenStatusServiceTableMax_Type = Unsigned32
_Hm2AgentDiffServGenStatusServiceTableMax_Object = MibScalar
hm2AgentDiffServGenStatusServiceTableMax = _Hm2AgentDiffServGenStatusServiceTableMax_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 1, 13),
    _Hm2AgentDiffServGenStatusServiceTableMax_Type()
)
hm2AgentDiffServGenStatusServiceTableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServGenStatusServiceTableMax.setStatus("current")
_Hm2AgentDiffServClassGroup_ObjectIdentity = ObjectIdentity
hm2AgentDiffServClassGroup = _Hm2AgentDiffServClassGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2)
)
_Hm2AgentDiffServClassIndexNextFree_Type = Unsigned32
_Hm2AgentDiffServClassIndexNextFree_Object = MibScalar
hm2AgentDiffServClassIndexNextFree = _Hm2AgentDiffServClassIndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 1),
    _Hm2AgentDiffServClassIndexNextFree_Type()
)
hm2AgentDiffServClassIndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassIndexNextFree.setStatus("current")
_Hm2AgentDiffServClassTable_Object = MibTable
hm2AgentDiffServClassTable = _Hm2AgentDiffServClassTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 2)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServClassTable.setStatus("current")
_Hm2AgentDiffServClassEntry_Object = MibTableRow
hm2AgentDiffServClassEntry = _Hm2AgentDiffServClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 2, 1)
)
hm2AgentDiffServClassEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-DIFFSERV-PRIVATE-MIB", "hm2AgentDiffServClassIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDiffServClassEntry.setStatus("current")
_Hm2AgentDiffServClassIndex_Type = Unsigned32
_Hm2AgentDiffServClassIndex_Object = MibTableColumn
hm2AgentDiffServClassIndex = _Hm2AgentDiffServClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 2, 1, 1),
    _Hm2AgentDiffServClassIndex_Type()
)
hm2AgentDiffServClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassIndex.setStatus("current")


class _Hm2AgentDiffServClassName_Type(DisplayString):
    """Custom type hm2AgentDiffServClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hm2AgentDiffServClassName_Type.__name__ = "DisplayString"
_Hm2AgentDiffServClassName_Object = MibTableColumn
hm2AgentDiffServClassName = _Hm2AgentDiffServClassName_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 2, 1, 2),
    _Hm2AgentDiffServClassName_Type()
)
hm2AgentDiffServClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassName.setStatus("current")


class _Hm2AgentDiffServClassType_Type(Integer32):
    """Custom type hm2AgentDiffServClassType based on Integer32"""
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


_Hm2AgentDiffServClassType_Type.__name__ = "Integer32"
_Hm2AgentDiffServClassType_Object = MibTableColumn
hm2AgentDiffServClassType = _Hm2AgentDiffServClassType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 2, 1, 3),
    _Hm2AgentDiffServClassType_Type()
)
hm2AgentDiffServClassType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassType.setStatus("current")
_Hm2AgentDiffServClassRuleIndexNextFree_Type = Unsigned32
_Hm2AgentDiffServClassRuleIndexNextFree_Object = MibTableColumn
hm2AgentDiffServClassRuleIndexNextFree = _Hm2AgentDiffServClassRuleIndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 2, 1, 5),
    _Hm2AgentDiffServClassRuleIndexNextFree_Type()
)
hm2AgentDiffServClassRuleIndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleIndexNextFree.setStatus("current")


class _Hm2AgentDiffServClassStorageType_Type(StorageType):
    """Custom type hm2AgentDiffServClassStorageType based on StorageType"""


_Hm2AgentDiffServClassStorageType_Object = MibTableColumn
hm2AgentDiffServClassStorageType = _Hm2AgentDiffServClassStorageType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 2, 1, 6),
    _Hm2AgentDiffServClassStorageType_Type()
)
hm2AgentDiffServClassStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassStorageType.setStatus("current")
_Hm2AgentDiffServClassRowStatus_Type = RowStatus
_Hm2AgentDiffServClassRowStatus_Object = MibTableColumn
hm2AgentDiffServClassRowStatus = _Hm2AgentDiffServClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 2, 1, 7),
    _Hm2AgentDiffServClassRowStatus_Type()
)
hm2AgentDiffServClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRowStatus.setStatus("current")


class _Hm2AgentDiffServClassProtoType_Type(Integer32):
    """Custom type hm2AgentDiffServClassProtoType based on Integer32"""
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


_Hm2AgentDiffServClassProtoType_Type.__name__ = "Integer32"
_Hm2AgentDiffServClassProtoType_Object = MibTableColumn
hm2AgentDiffServClassProtoType = _Hm2AgentDiffServClassProtoType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 2, 1, 9),
    _Hm2AgentDiffServClassProtoType_Type()
)
hm2AgentDiffServClassProtoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassProtoType.setStatus("current")
_Hm2AgentDiffServClassRuleTable_Object = MibTable
hm2AgentDiffServClassRuleTable = _Hm2AgentDiffServClassRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleTable.setStatus("current")
_Hm2AgentDiffServClassRuleEntry_Object = MibTableRow
hm2AgentDiffServClassRuleEntry = _Hm2AgentDiffServClassRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1)
)
hm2AgentDiffServClassRuleEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-DIFFSERV-PRIVATE-MIB", "hm2AgentDiffServClassIndex"),
    (0, "HM2-PLATFORM-QOS-DIFFSERV-PRIVATE-MIB", "hm2AgentDiffServClassRuleIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleEntry.setStatus("current")
_Hm2AgentDiffServClassRuleIndex_Type = Unsigned32
_Hm2AgentDiffServClassRuleIndex_Object = MibTableColumn
hm2AgentDiffServClassRuleIndex = _Hm2AgentDiffServClassRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 1),
    _Hm2AgentDiffServClassRuleIndex_Type()
)
hm2AgentDiffServClassRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleIndex.setStatus("current")


class _Hm2AgentDiffServClassRuleMatchEntryType_Type(Integer32):
    """Custom type hm2AgentDiffServClassRuleMatchEntryType based on Integer32"""
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


_Hm2AgentDiffServClassRuleMatchEntryType_Type.__name__ = "Integer32"
_Hm2AgentDiffServClassRuleMatchEntryType_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchEntryType = _Hm2AgentDiffServClassRuleMatchEntryType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 2),
    _Hm2AgentDiffServClassRuleMatchEntryType_Type()
)
hm2AgentDiffServClassRuleMatchEntryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchEntryType.setStatus("current")


class _Hm2AgentDiffServClassRuleMatchCos_Type(Unsigned32):
    """Custom type hm2AgentDiffServClassRuleMatchCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2AgentDiffServClassRuleMatchCos_Type.__name__ = "Unsigned32"
_Hm2AgentDiffServClassRuleMatchCos_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchCos = _Hm2AgentDiffServClassRuleMatchCos_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 3),
    _Hm2AgentDiffServClassRuleMatchCos_Type()
)
hm2AgentDiffServClassRuleMatchCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchCos.setStatus("current")
_Hm2AgentDiffServClassRuleMatchDstIpAddr_Type = IpAddress
_Hm2AgentDiffServClassRuleMatchDstIpAddr_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchDstIpAddr = _Hm2AgentDiffServClassRuleMatchDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 4),
    _Hm2AgentDiffServClassRuleMatchDstIpAddr_Type()
)
hm2AgentDiffServClassRuleMatchDstIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchDstIpAddr.setStatus("current")
_Hm2AgentDiffServClassRuleMatchDstIpMask_Type = IpAddress
_Hm2AgentDiffServClassRuleMatchDstIpMask_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchDstIpMask = _Hm2AgentDiffServClassRuleMatchDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 5),
    _Hm2AgentDiffServClassRuleMatchDstIpMask_Type()
)
hm2AgentDiffServClassRuleMatchDstIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchDstIpMask.setStatus("current")
_Hm2AgentDiffServClassRuleMatchDstL4PortStart_Type = InetPortNumber
_Hm2AgentDiffServClassRuleMatchDstL4PortStart_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchDstL4PortStart = _Hm2AgentDiffServClassRuleMatchDstL4PortStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 6),
    _Hm2AgentDiffServClassRuleMatchDstL4PortStart_Type()
)
hm2AgentDiffServClassRuleMatchDstL4PortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchDstL4PortStart.setStatus("current")
_Hm2AgentDiffServClassRuleMatchDstL4PortEnd_Type = InetPortNumber
_Hm2AgentDiffServClassRuleMatchDstL4PortEnd_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchDstL4PortEnd = _Hm2AgentDiffServClassRuleMatchDstL4PortEnd_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 7),
    _Hm2AgentDiffServClassRuleMatchDstL4PortEnd_Type()
)
hm2AgentDiffServClassRuleMatchDstL4PortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchDstL4PortEnd.setStatus("current")
_Hm2AgentDiffServClassRuleMatchDstMacAddr_Type = MacAddress
_Hm2AgentDiffServClassRuleMatchDstMacAddr_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchDstMacAddr = _Hm2AgentDiffServClassRuleMatchDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 8),
    _Hm2AgentDiffServClassRuleMatchDstMacAddr_Type()
)
hm2AgentDiffServClassRuleMatchDstMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchDstMacAddr.setStatus("current")
_Hm2AgentDiffServClassRuleMatchDstMacMask_Type = MacAddress
_Hm2AgentDiffServClassRuleMatchDstMacMask_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchDstMacMask = _Hm2AgentDiffServClassRuleMatchDstMacMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 9),
    _Hm2AgentDiffServClassRuleMatchDstMacMask_Type()
)
hm2AgentDiffServClassRuleMatchDstMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchDstMacMask.setStatus("current")
_Hm2AgentDiffServClassRuleMatchEvery_Type = TruthValue
_Hm2AgentDiffServClassRuleMatchEvery_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchEvery = _Hm2AgentDiffServClassRuleMatchEvery_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 10),
    _Hm2AgentDiffServClassRuleMatchEvery_Type()
)
hm2AgentDiffServClassRuleMatchEvery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchEvery.setStatus("current")


class _Hm2AgentDiffServClassRuleMatchIpDscp_Type(Unsigned32):
    """Custom type hm2AgentDiffServClassRuleMatchIpDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hm2AgentDiffServClassRuleMatchIpDscp_Type.__name__ = "Unsigned32"
_Hm2AgentDiffServClassRuleMatchIpDscp_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchIpDscp = _Hm2AgentDiffServClassRuleMatchIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 11),
    _Hm2AgentDiffServClassRuleMatchIpDscp_Type()
)
hm2AgentDiffServClassRuleMatchIpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchIpDscp.setStatus("current")


class _Hm2AgentDiffServClassRuleMatchIpPrecedence_Type(Unsigned32):
    """Custom type hm2AgentDiffServClassRuleMatchIpPrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2AgentDiffServClassRuleMatchIpPrecedence_Type.__name__ = "Unsigned32"
_Hm2AgentDiffServClassRuleMatchIpPrecedence_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchIpPrecedence = _Hm2AgentDiffServClassRuleMatchIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 12),
    _Hm2AgentDiffServClassRuleMatchIpPrecedence_Type()
)
hm2AgentDiffServClassRuleMatchIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchIpPrecedence.setStatus("current")


class _Hm2AgentDiffServClassRuleMatchIpTosBits_Type(OctetString):
    """Custom type hm2AgentDiffServClassRuleMatchIpTosBits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Hm2AgentDiffServClassRuleMatchIpTosBits_Type.__name__ = "OctetString"
_Hm2AgentDiffServClassRuleMatchIpTosBits_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchIpTosBits = _Hm2AgentDiffServClassRuleMatchIpTosBits_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 13),
    _Hm2AgentDiffServClassRuleMatchIpTosBits_Type()
)
hm2AgentDiffServClassRuleMatchIpTosBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchIpTosBits.setStatus("current")


class _Hm2AgentDiffServClassRuleMatchIpTosMask_Type(OctetString):
    """Custom type hm2AgentDiffServClassRuleMatchIpTosMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Hm2AgentDiffServClassRuleMatchIpTosMask_Type.__name__ = "OctetString"
_Hm2AgentDiffServClassRuleMatchIpTosMask_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchIpTosMask = _Hm2AgentDiffServClassRuleMatchIpTosMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 14),
    _Hm2AgentDiffServClassRuleMatchIpTosMask_Type()
)
hm2AgentDiffServClassRuleMatchIpTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchIpTosMask.setStatus("current")


class _Hm2AgentDiffServClassRuleMatchProtocolNum_Type(Unsigned32):
    """Custom type hm2AgentDiffServClassRuleMatchProtocolNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hm2AgentDiffServClassRuleMatchProtocolNum_Type.__name__ = "Unsigned32"
_Hm2AgentDiffServClassRuleMatchProtocolNum_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchProtocolNum = _Hm2AgentDiffServClassRuleMatchProtocolNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 15),
    _Hm2AgentDiffServClassRuleMatchProtocolNum_Type()
)
hm2AgentDiffServClassRuleMatchProtocolNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchProtocolNum.setStatus("current")
_Hm2AgentDiffServClassRuleMatchRefClassIndex_Type = Unsigned32
_Hm2AgentDiffServClassRuleMatchRefClassIndex_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchRefClassIndex = _Hm2AgentDiffServClassRuleMatchRefClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 16),
    _Hm2AgentDiffServClassRuleMatchRefClassIndex_Type()
)
hm2AgentDiffServClassRuleMatchRefClassIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchRefClassIndex.setStatus("current")
_Hm2AgentDiffServClassRuleMatchSrcIpAddr_Type = IpAddress
_Hm2AgentDiffServClassRuleMatchSrcIpAddr_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchSrcIpAddr = _Hm2AgentDiffServClassRuleMatchSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 17),
    _Hm2AgentDiffServClassRuleMatchSrcIpAddr_Type()
)
hm2AgentDiffServClassRuleMatchSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchSrcIpAddr.setStatus("current")
_Hm2AgentDiffServClassRuleMatchSrcIpMask_Type = IpAddress
_Hm2AgentDiffServClassRuleMatchSrcIpMask_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchSrcIpMask = _Hm2AgentDiffServClassRuleMatchSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 18),
    _Hm2AgentDiffServClassRuleMatchSrcIpMask_Type()
)
hm2AgentDiffServClassRuleMatchSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchSrcIpMask.setStatus("current")
_Hm2AgentDiffServClassRuleMatchSrcL4PortStart_Type = InetPortNumber
_Hm2AgentDiffServClassRuleMatchSrcL4PortStart_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchSrcL4PortStart = _Hm2AgentDiffServClassRuleMatchSrcL4PortStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 19),
    _Hm2AgentDiffServClassRuleMatchSrcL4PortStart_Type()
)
hm2AgentDiffServClassRuleMatchSrcL4PortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchSrcL4PortStart.setStatus("current")
_Hm2AgentDiffServClassRuleMatchSrcL4PortEnd_Type = InetPortNumber
_Hm2AgentDiffServClassRuleMatchSrcL4PortEnd_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchSrcL4PortEnd = _Hm2AgentDiffServClassRuleMatchSrcL4PortEnd_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 20),
    _Hm2AgentDiffServClassRuleMatchSrcL4PortEnd_Type()
)
hm2AgentDiffServClassRuleMatchSrcL4PortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchSrcL4PortEnd.setStatus("current")
_Hm2AgentDiffServClassRuleMatchSrcMacAddr_Type = MacAddress
_Hm2AgentDiffServClassRuleMatchSrcMacAddr_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchSrcMacAddr = _Hm2AgentDiffServClassRuleMatchSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 21),
    _Hm2AgentDiffServClassRuleMatchSrcMacAddr_Type()
)
hm2AgentDiffServClassRuleMatchSrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchSrcMacAddr.setStatus("current")
_Hm2AgentDiffServClassRuleMatchSrcMacMask_Type = MacAddress
_Hm2AgentDiffServClassRuleMatchSrcMacMask_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchSrcMacMask = _Hm2AgentDiffServClassRuleMatchSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 22),
    _Hm2AgentDiffServClassRuleMatchSrcMacMask_Type()
)
hm2AgentDiffServClassRuleMatchSrcMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchSrcMacMask.setStatus("current")
_Hm2AgentDiffServClassRuleMatchExcludeFlag_Type = TruthValue
_Hm2AgentDiffServClassRuleMatchExcludeFlag_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchExcludeFlag = _Hm2AgentDiffServClassRuleMatchExcludeFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 24),
    _Hm2AgentDiffServClassRuleMatchExcludeFlag_Type()
)
hm2AgentDiffServClassRuleMatchExcludeFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchExcludeFlag.setStatus("current")


class _Hm2AgentDiffServClassRuleStorageType_Type(StorageType):
    """Custom type hm2AgentDiffServClassRuleStorageType based on StorageType"""


_Hm2AgentDiffServClassRuleStorageType_Object = MibTableColumn
hm2AgentDiffServClassRuleStorageType = _Hm2AgentDiffServClassRuleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 25),
    _Hm2AgentDiffServClassRuleStorageType_Type()
)
hm2AgentDiffServClassRuleStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleStorageType.setStatus("current")
_Hm2AgentDiffServClassRuleRowStatus_Type = RowStatus
_Hm2AgentDiffServClassRuleRowStatus_Object = MibTableColumn
hm2AgentDiffServClassRuleRowStatus = _Hm2AgentDiffServClassRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 26),
    _Hm2AgentDiffServClassRuleRowStatus_Type()
)
hm2AgentDiffServClassRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleRowStatus.setStatus("current")


class _Hm2AgentDiffServClassRuleMatchCos2_Type(Unsigned32):
    """Custom type hm2AgentDiffServClassRuleMatchCos2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2AgentDiffServClassRuleMatchCos2_Type.__name__ = "Unsigned32"
_Hm2AgentDiffServClassRuleMatchCos2_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchCos2 = _Hm2AgentDiffServClassRuleMatchCos2_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 27),
    _Hm2AgentDiffServClassRuleMatchCos2_Type()
)
hm2AgentDiffServClassRuleMatchCos2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchCos2.setStatus("current")


class _Hm2AgentDiffServClassRuleMatchEtypeKey_Type(Integer32):
    """Custom type hm2AgentDiffServClassRuleMatchEtypeKey based on Integer32"""
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


_Hm2AgentDiffServClassRuleMatchEtypeKey_Type.__name__ = "Integer32"
_Hm2AgentDiffServClassRuleMatchEtypeKey_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchEtypeKey = _Hm2AgentDiffServClassRuleMatchEtypeKey_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 28),
    _Hm2AgentDiffServClassRuleMatchEtypeKey_Type()
)
hm2AgentDiffServClassRuleMatchEtypeKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchEtypeKey.setStatus("current")
_Hm2AgentDiffServClassRuleMatchEtypeValue_Type = EtypeValue
_Hm2AgentDiffServClassRuleMatchEtypeValue_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchEtypeValue = _Hm2AgentDiffServClassRuleMatchEtypeValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 29),
    _Hm2AgentDiffServClassRuleMatchEtypeValue_Type()
)
hm2AgentDiffServClassRuleMatchEtypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchEtypeValue.setStatus("current")


class _Hm2AgentDiffServClassRuleMatchVlanIdStart_Type(Unsigned32):
    """Custom type hm2AgentDiffServClassRuleMatchVlanIdStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4042),
    )


_Hm2AgentDiffServClassRuleMatchVlanIdStart_Type.__name__ = "Unsigned32"
_Hm2AgentDiffServClassRuleMatchVlanIdStart_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchVlanIdStart = _Hm2AgentDiffServClassRuleMatchVlanIdStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 30),
    _Hm2AgentDiffServClassRuleMatchVlanIdStart_Type()
)
hm2AgentDiffServClassRuleMatchVlanIdStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchVlanIdStart.setStatus("current")


class _Hm2AgentDiffServClassRuleMatchVlanIdEnd_Type(Unsigned32):
    """Custom type hm2AgentDiffServClassRuleMatchVlanIdEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4042),
    )


_Hm2AgentDiffServClassRuleMatchVlanIdEnd_Type.__name__ = "Unsigned32"
_Hm2AgentDiffServClassRuleMatchVlanIdEnd_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchVlanIdEnd = _Hm2AgentDiffServClassRuleMatchVlanIdEnd_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 31),
    _Hm2AgentDiffServClassRuleMatchVlanIdEnd_Type()
)
hm2AgentDiffServClassRuleMatchVlanIdEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchVlanIdEnd.setStatus("current")


class _Hm2AgentDiffServClassRuleMatchVlanId2Start_Type(Unsigned32):
    """Custom type hm2AgentDiffServClassRuleMatchVlanId2Start based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4042),
    )


_Hm2AgentDiffServClassRuleMatchVlanId2Start_Type.__name__ = "Unsigned32"
_Hm2AgentDiffServClassRuleMatchVlanId2Start_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchVlanId2Start = _Hm2AgentDiffServClassRuleMatchVlanId2Start_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 32),
    _Hm2AgentDiffServClassRuleMatchVlanId2Start_Type()
)
hm2AgentDiffServClassRuleMatchVlanId2Start.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchVlanId2Start.setStatus("current")


class _Hm2AgentDiffServClassRuleMatchVlanId2End_Type(Unsigned32):
    """Custom type hm2AgentDiffServClassRuleMatchVlanId2End based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4042),
    )


_Hm2AgentDiffServClassRuleMatchVlanId2End_Type.__name__ = "Unsigned32"
_Hm2AgentDiffServClassRuleMatchVlanId2End_Object = MibTableColumn
hm2AgentDiffServClassRuleMatchVlanId2End = _Hm2AgentDiffServClassRuleMatchVlanId2End_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 2, 3, 1, 33),
    _Hm2AgentDiffServClassRuleMatchVlanId2End_Type()
)
hm2AgentDiffServClassRuleMatchVlanId2End.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchVlanId2End.setStatus("current")
_Hm2AgentDiffServPolicyGroup_ObjectIdentity = ObjectIdentity
hm2AgentDiffServPolicyGroup = _Hm2AgentDiffServPolicyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3)
)
_Hm2AgentDiffServPolicyIndexNextFree_Type = Unsigned32
_Hm2AgentDiffServPolicyIndexNextFree_Object = MibScalar
hm2AgentDiffServPolicyIndexNextFree = _Hm2AgentDiffServPolicyIndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 1),
    _Hm2AgentDiffServPolicyIndexNextFree_Type()
)
hm2AgentDiffServPolicyIndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyIndexNextFree.setStatus("current")
_Hm2AgentDiffServPolicyTable_Object = MibTable
hm2AgentDiffServPolicyTable = _Hm2AgentDiffServPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 2)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyTable.setStatus("current")
_Hm2AgentDiffServPolicyEntry_Object = MibTableRow
hm2AgentDiffServPolicyEntry = _Hm2AgentDiffServPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 2, 1)
)
hm2AgentDiffServPolicyEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-DIFFSERV-PRIVATE-MIB", "hm2AgentDiffServPolicyIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyEntry.setStatus("current")
_Hm2AgentDiffServPolicyIndex_Type = Unsigned32
_Hm2AgentDiffServPolicyIndex_Object = MibTableColumn
hm2AgentDiffServPolicyIndex = _Hm2AgentDiffServPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 2, 1, 1),
    _Hm2AgentDiffServPolicyIndex_Type()
)
hm2AgentDiffServPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyIndex.setStatus("current")


class _Hm2AgentDiffServPolicyName_Type(DisplayString):
    """Custom type hm2AgentDiffServPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hm2AgentDiffServPolicyName_Type.__name__ = "DisplayString"
_Hm2AgentDiffServPolicyName_Object = MibTableColumn
hm2AgentDiffServPolicyName = _Hm2AgentDiffServPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 2, 1, 2),
    _Hm2AgentDiffServPolicyName_Type()
)
hm2AgentDiffServPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyName.setStatus("current")
_Hm2AgentDiffServPolicyType_Type = IntfDirection
_Hm2AgentDiffServPolicyType_Object = MibTableColumn
hm2AgentDiffServPolicyType = _Hm2AgentDiffServPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 2, 1, 3),
    _Hm2AgentDiffServPolicyType_Type()
)
hm2AgentDiffServPolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyType.setStatus("current")
_Hm2AgentDiffServPolicyInstIndexNextFree_Type = Unsigned32
_Hm2AgentDiffServPolicyInstIndexNextFree_Object = MibTableColumn
hm2AgentDiffServPolicyInstIndexNextFree = _Hm2AgentDiffServPolicyInstIndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 2, 1, 4),
    _Hm2AgentDiffServPolicyInstIndexNextFree_Type()
)
hm2AgentDiffServPolicyInstIndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyInstIndexNextFree.setStatus("current")


class _Hm2AgentDiffServPolicyStorageType_Type(StorageType):
    """Custom type hm2AgentDiffServPolicyStorageType based on StorageType"""


_Hm2AgentDiffServPolicyStorageType_Object = MibTableColumn
hm2AgentDiffServPolicyStorageType = _Hm2AgentDiffServPolicyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 2, 1, 5),
    _Hm2AgentDiffServPolicyStorageType_Type()
)
hm2AgentDiffServPolicyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyStorageType.setStatus("current")
_Hm2AgentDiffServPolicyRowStatus_Type = RowStatus
_Hm2AgentDiffServPolicyRowStatus_Object = MibTableColumn
hm2AgentDiffServPolicyRowStatus = _Hm2AgentDiffServPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 2, 1, 6),
    _Hm2AgentDiffServPolicyRowStatus_Type()
)
hm2AgentDiffServPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyRowStatus.setStatus("current")
_Hm2AgentDiffServPolicyInstTable_Object = MibTable
hm2AgentDiffServPolicyInstTable = _Hm2AgentDiffServPolicyInstTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 3)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyInstTable.setStatus("current")
_Hm2AgentDiffServPolicyInstEntry_Object = MibTableRow
hm2AgentDiffServPolicyInstEntry = _Hm2AgentDiffServPolicyInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 3, 1)
)
hm2AgentDiffServPolicyInstEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-DIFFSERV-PRIVATE-MIB", "hm2AgentDiffServPolicyIndex"),
    (0, "HM2-PLATFORM-QOS-DIFFSERV-PRIVATE-MIB", "hm2AgentDiffServPolicyInstIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyInstEntry.setStatus("current")
_Hm2AgentDiffServPolicyInstIndex_Type = Unsigned32
_Hm2AgentDiffServPolicyInstIndex_Object = MibTableColumn
hm2AgentDiffServPolicyInstIndex = _Hm2AgentDiffServPolicyInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 3, 1, 1),
    _Hm2AgentDiffServPolicyInstIndex_Type()
)
hm2AgentDiffServPolicyInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyInstIndex.setStatus("current")
_Hm2AgentDiffServPolicyInstClassIndex_Type = Unsigned32
_Hm2AgentDiffServPolicyInstClassIndex_Object = MibTableColumn
hm2AgentDiffServPolicyInstClassIndex = _Hm2AgentDiffServPolicyInstClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 3, 1, 2),
    _Hm2AgentDiffServPolicyInstClassIndex_Type()
)
hm2AgentDiffServPolicyInstClassIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyInstClassIndex.setStatus("current")
_Hm2AgentDiffServPolicyInstAttrIndexNextFree_Type = Unsigned32
_Hm2AgentDiffServPolicyInstAttrIndexNextFree_Object = MibTableColumn
hm2AgentDiffServPolicyInstAttrIndexNextFree = _Hm2AgentDiffServPolicyInstAttrIndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 3, 1, 3),
    _Hm2AgentDiffServPolicyInstAttrIndexNextFree_Type()
)
hm2AgentDiffServPolicyInstAttrIndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyInstAttrIndexNextFree.setStatus("current")


class _Hm2AgentDiffServPolicyInstStorageType_Type(StorageType):
    """Custom type hm2AgentDiffServPolicyInstStorageType based on StorageType"""


_Hm2AgentDiffServPolicyInstStorageType_Object = MibTableColumn
hm2AgentDiffServPolicyInstStorageType = _Hm2AgentDiffServPolicyInstStorageType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 3, 1, 4),
    _Hm2AgentDiffServPolicyInstStorageType_Type()
)
hm2AgentDiffServPolicyInstStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyInstStorageType.setStatus("current")
_Hm2AgentDiffServPolicyInstRowStatus_Type = RowStatus
_Hm2AgentDiffServPolicyInstRowStatus_Object = MibTableColumn
hm2AgentDiffServPolicyInstRowStatus = _Hm2AgentDiffServPolicyInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 3, 1, 5),
    _Hm2AgentDiffServPolicyInstRowStatus_Type()
)
hm2AgentDiffServPolicyInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyInstRowStatus.setStatus("current")
_Hm2AgentDiffServPolicyAttrTable_Object = MibTable
hm2AgentDiffServPolicyAttrTable = _Hm2AgentDiffServPolicyAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrTable.setStatus("current")
_Hm2AgentDiffServPolicyAttrEntry_Object = MibTableRow
hm2AgentDiffServPolicyAttrEntry = _Hm2AgentDiffServPolicyAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1)
)
hm2AgentDiffServPolicyAttrEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-DIFFSERV-PRIVATE-MIB", "hm2AgentDiffServPolicyIndex"),
    (0, "HM2-PLATFORM-QOS-DIFFSERV-PRIVATE-MIB", "hm2AgentDiffServPolicyInstIndex"),
    (0, "HM2-PLATFORM-QOS-DIFFSERV-PRIVATE-MIB", "hm2AgentDiffServPolicyAttrIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrEntry.setStatus("current")
_Hm2AgentDiffServPolicyAttrIndex_Type = Unsigned32
_Hm2AgentDiffServPolicyAttrIndex_Object = MibTableColumn
hm2AgentDiffServPolicyAttrIndex = _Hm2AgentDiffServPolicyAttrIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 1),
    _Hm2AgentDiffServPolicyAttrIndex_Type()
)
hm2AgentDiffServPolicyAttrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrIndex.setStatus("current")


class _Hm2AgentDiffServPolicyAttrStmtEntryType_Type(Integer32):
    """Custom type hm2AgentDiffServPolicyAttrStmtEntryType based on Integer32"""
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


_Hm2AgentDiffServPolicyAttrStmtEntryType_Type.__name__ = "Integer32"
_Hm2AgentDiffServPolicyAttrStmtEntryType_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtEntryType = _Hm2AgentDiffServPolicyAttrStmtEntryType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 2),
    _Hm2AgentDiffServPolicyAttrStmtEntryType_Type()
)
hm2AgentDiffServPolicyAttrStmtEntryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtEntryType.setStatus("current")


class _Hm2AgentDiffServPolicyAttrStmtMarkCosVal_Type(Unsigned32):
    """Custom type hm2AgentDiffServPolicyAttrStmtMarkCosVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2AgentDiffServPolicyAttrStmtMarkCosVal_Type.__name__ = "Unsigned32"
_Hm2AgentDiffServPolicyAttrStmtMarkCosVal_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtMarkCosVal = _Hm2AgentDiffServPolicyAttrStmtMarkCosVal_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 8),
    _Hm2AgentDiffServPolicyAttrStmtMarkCosVal_Type()
)
hm2AgentDiffServPolicyAttrStmtMarkCosVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtMarkCosVal.setStatus("current")


class _Hm2AgentDiffServPolicyAttrStmtMarkIpDscpVal_Type(Unsigned32):
    """Custom type hm2AgentDiffServPolicyAttrStmtMarkIpDscpVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hm2AgentDiffServPolicyAttrStmtMarkIpDscpVal_Type.__name__ = "Unsigned32"
_Hm2AgentDiffServPolicyAttrStmtMarkIpDscpVal_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtMarkIpDscpVal = _Hm2AgentDiffServPolicyAttrStmtMarkIpDscpVal_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 9),
    _Hm2AgentDiffServPolicyAttrStmtMarkIpDscpVal_Type()
)
hm2AgentDiffServPolicyAttrStmtMarkIpDscpVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtMarkIpDscpVal.setStatus("current")


class _Hm2AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal_Type(Unsigned32):
    """Custom type hm2AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal_Type.__name__ = "Unsigned32"
_Hm2AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal = _Hm2AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 10),
    _Hm2AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal_Type()
)
hm2AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal.setStatus("current")


class _Hm2AgentDiffServPolicyAttrStmtPoliceConformAct_Type(Integer32):
    """Custom type hm2AgentDiffServPolicyAttrStmtPoliceConformAct based on Integer32"""
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


_Hm2AgentDiffServPolicyAttrStmtPoliceConformAct_Type.__name__ = "Integer32"
_Hm2AgentDiffServPolicyAttrStmtPoliceConformAct_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceConformAct = _Hm2AgentDiffServPolicyAttrStmtPoliceConformAct_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 11),
    _Hm2AgentDiffServPolicyAttrStmtPoliceConformAct_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceConformAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceConformAct.setStatus("current")


class _Hm2AgentDiffServPolicyAttrStmtPoliceConformVal_Type(Unsigned32):
    """Custom type hm2AgentDiffServPolicyAttrStmtPoliceConformVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hm2AgentDiffServPolicyAttrStmtPoliceConformVal_Type.__name__ = "Unsigned32"
_Hm2AgentDiffServPolicyAttrStmtPoliceConformVal_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceConformVal = _Hm2AgentDiffServPolicyAttrStmtPoliceConformVal_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 12),
    _Hm2AgentDiffServPolicyAttrStmtPoliceConformVal_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceConformVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceConformVal.setStatus("current")


class _Hm2AgentDiffServPolicyAttrStmtPoliceExceedAct_Type(Integer32):
    """Custom type hm2AgentDiffServPolicyAttrStmtPoliceExceedAct based on Integer32"""
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


_Hm2AgentDiffServPolicyAttrStmtPoliceExceedAct_Type.__name__ = "Integer32"
_Hm2AgentDiffServPolicyAttrStmtPoliceExceedAct_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceExceedAct = _Hm2AgentDiffServPolicyAttrStmtPoliceExceedAct_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 13),
    _Hm2AgentDiffServPolicyAttrStmtPoliceExceedAct_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceExceedAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceExceedAct.setStatus("current")


class _Hm2AgentDiffServPolicyAttrStmtPoliceExceedVal_Type(Unsigned32):
    """Custom type hm2AgentDiffServPolicyAttrStmtPoliceExceedVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hm2AgentDiffServPolicyAttrStmtPoliceExceedVal_Type.__name__ = "Unsigned32"
_Hm2AgentDiffServPolicyAttrStmtPoliceExceedVal_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceExceedVal = _Hm2AgentDiffServPolicyAttrStmtPoliceExceedVal_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 14),
    _Hm2AgentDiffServPolicyAttrStmtPoliceExceedVal_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceExceedVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceExceedVal.setStatus("current")


class _Hm2AgentDiffServPolicyAttrStmtPoliceNonconformAct_Type(Integer32):
    """Custom type hm2AgentDiffServPolicyAttrStmtPoliceNonconformAct based on Integer32"""
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


_Hm2AgentDiffServPolicyAttrStmtPoliceNonconformAct_Type.__name__ = "Integer32"
_Hm2AgentDiffServPolicyAttrStmtPoliceNonconformAct_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceNonconformAct = _Hm2AgentDiffServPolicyAttrStmtPoliceNonconformAct_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 15),
    _Hm2AgentDiffServPolicyAttrStmtPoliceNonconformAct_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceNonconformAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceNonconformAct.setStatus("current")


class _Hm2AgentDiffServPolicyAttrStmtPoliceNonconformVal_Type(Unsigned32):
    """Custom type hm2AgentDiffServPolicyAttrStmtPoliceNonconformVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hm2AgentDiffServPolicyAttrStmtPoliceNonconformVal_Type.__name__ = "Unsigned32"
_Hm2AgentDiffServPolicyAttrStmtPoliceNonconformVal_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceNonconformVal = _Hm2AgentDiffServPolicyAttrStmtPoliceNonconformVal_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 16),
    _Hm2AgentDiffServPolicyAttrStmtPoliceNonconformVal_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceNonconformVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceNonconformVal.setStatus("current")
_Hm2AgentDiffServPolicyAttrStmtPoliceSimpleCrate_Type = Unsigned32
_Hm2AgentDiffServPolicyAttrStmtPoliceSimpleCrate_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceSimpleCrate = _Hm2AgentDiffServPolicyAttrStmtPoliceSimpleCrate_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 17),
    _Hm2AgentDiffServPolicyAttrStmtPoliceSimpleCrate_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceSimpleCrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceSimpleCrate.setStatus("current")
_Hm2AgentDiffServPolicyAttrStmtPoliceSimpleCburst_Type = QosBurstSize
_Hm2AgentDiffServPolicyAttrStmtPoliceSimpleCburst_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceSimpleCburst = _Hm2AgentDiffServPolicyAttrStmtPoliceSimpleCburst_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 18),
    _Hm2AgentDiffServPolicyAttrStmtPoliceSimpleCburst_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceSimpleCburst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceSimpleCburst.setStatus("current")
_Hm2AgentDiffServPolicyAttrStmtPoliceSinglerateCrate_Type = Unsigned32
_Hm2AgentDiffServPolicyAttrStmtPoliceSinglerateCrate_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceSinglerateCrate = _Hm2AgentDiffServPolicyAttrStmtPoliceSinglerateCrate_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 19),
    _Hm2AgentDiffServPolicyAttrStmtPoliceSinglerateCrate_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceSinglerateCrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceSinglerateCrate.setStatus("current")
_Hm2AgentDiffServPolicyAttrStmtPoliceSinglerateCburst_Type = QosBurstSize
_Hm2AgentDiffServPolicyAttrStmtPoliceSinglerateCburst_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceSinglerateCburst = _Hm2AgentDiffServPolicyAttrStmtPoliceSinglerateCburst_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 20),
    _Hm2AgentDiffServPolicyAttrStmtPoliceSinglerateCburst_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceSinglerateCburst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceSinglerateCburst.setStatus("current")
_Hm2AgentDiffServPolicyAttrStmtPoliceSinglerateEburst_Type = QosBurstSize
_Hm2AgentDiffServPolicyAttrStmtPoliceSinglerateEburst_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceSinglerateEburst = _Hm2AgentDiffServPolicyAttrStmtPoliceSinglerateEburst_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 21),
    _Hm2AgentDiffServPolicyAttrStmtPoliceSinglerateEburst_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceSinglerateEburst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceSinglerateEburst.setStatus("current")
_Hm2AgentDiffServPolicyAttrStmtPoliceTworateCrate_Type = Unsigned32
_Hm2AgentDiffServPolicyAttrStmtPoliceTworateCrate_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceTworateCrate = _Hm2AgentDiffServPolicyAttrStmtPoliceTworateCrate_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 22),
    _Hm2AgentDiffServPolicyAttrStmtPoliceTworateCrate_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceTworateCrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceTworateCrate.setStatus("current")
_Hm2AgentDiffServPolicyAttrStmtPoliceTworateCburst_Type = QosBurstSize
_Hm2AgentDiffServPolicyAttrStmtPoliceTworateCburst_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceTworateCburst = _Hm2AgentDiffServPolicyAttrStmtPoliceTworateCburst_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 23),
    _Hm2AgentDiffServPolicyAttrStmtPoliceTworateCburst_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceTworateCburst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceTworateCburst.setStatus("current")
_Hm2AgentDiffServPolicyAttrStmtPoliceTworatePrate_Type = Unsigned32
_Hm2AgentDiffServPolicyAttrStmtPoliceTworatePrate_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceTworatePrate = _Hm2AgentDiffServPolicyAttrStmtPoliceTworatePrate_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 24),
    _Hm2AgentDiffServPolicyAttrStmtPoliceTworatePrate_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceTworatePrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceTworatePrate.setStatus("current")
_Hm2AgentDiffServPolicyAttrStmtPoliceTworatePburst_Type = QosBurstSize
_Hm2AgentDiffServPolicyAttrStmtPoliceTworatePburst_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceTworatePburst = _Hm2AgentDiffServPolicyAttrStmtPoliceTworatePburst_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 25),
    _Hm2AgentDiffServPolicyAttrStmtPoliceTworatePburst_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceTworatePburst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceTworatePburst.setStatus("current")


class _Hm2AgentDiffServPolicyAttrStorageType_Type(StorageType):
    """Custom type hm2AgentDiffServPolicyAttrStorageType based on StorageType"""


_Hm2AgentDiffServPolicyAttrStorageType_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStorageType = _Hm2AgentDiffServPolicyAttrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 34),
    _Hm2AgentDiffServPolicyAttrStorageType_Type()
)
hm2AgentDiffServPolicyAttrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStorageType.setStatus("current")
_Hm2AgentDiffServPolicyAttrRowStatus_Type = RowStatus
_Hm2AgentDiffServPolicyAttrRowStatus_Object = MibTableColumn
hm2AgentDiffServPolicyAttrRowStatus = _Hm2AgentDiffServPolicyAttrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 35),
    _Hm2AgentDiffServPolicyAttrRowStatus_Type()
)
hm2AgentDiffServPolicyAttrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrRowStatus.setStatus("current")
_Hm2AgentDiffServPolicyAttrStmtAssignQueueId_Type = Unsigned32
_Hm2AgentDiffServPolicyAttrStmtAssignQueueId_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtAssignQueueId = _Hm2AgentDiffServPolicyAttrStmtAssignQueueId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 36),
    _Hm2AgentDiffServPolicyAttrStmtAssignQueueId_Type()
)
hm2AgentDiffServPolicyAttrStmtAssignQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtAssignQueueId.setStatus("current")
_Hm2AgentDiffServPolicyAttrStmtDrop_Type = TruthValue
_Hm2AgentDiffServPolicyAttrStmtDrop_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtDrop = _Hm2AgentDiffServPolicyAttrStmtDrop_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 37),
    _Hm2AgentDiffServPolicyAttrStmtDrop_Type()
)
hm2AgentDiffServPolicyAttrStmtDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtDrop.setStatus("current")


class _Hm2AgentDiffServPolicyAttrStmtMarkCos2Val_Type(Unsigned32):
    """Custom type hm2AgentDiffServPolicyAttrStmtMarkCos2Val based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2AgentDiffServPolicyAttrStmtMarkCos2Val_Type.__name__ = "Unsigned32"
_Hm2AgentDiffServPolicyAttrStmtMarkCos2Val_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtMarkCos2Val = _Hm2AgentDiffServPolicyAttrStmtMarkCos2Val_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 38),
    _Hm2AgentDiffServPolicyAttrStmtMarkCos2Val_Type()
)
hm2AgentDiffServPolicyAttrStmtMarkCos2Val.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtMarkCos2Val.setStatus("current")


class _Hm2AgentDiffServPolicyAttrStmtPoliceColorConformIndex_Type(Unsigned32):
    """Custom type hm2AgentDiffServPolicyAttrStmtPoliceColorConformIndex based on Unsigned32"""
    defaultValue = 0


_Hm2AgentDiffServPolicyAttrStmtPoliceColorConformIndex_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceColorConformIndex = _Hm2AgentDiffServPolicyAttrStmtPoliceColorConformIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 39),
    _Hm2AgentDiffServPolicyAttrStmtPoliceColorConformIndex_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceColorConformIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceColorConformIndex.setStatus("current")


class _Hm2AgentDiffServPolicyAttrStmtPoliceColorConformMode_Type(Integer32):
    """Custom type hm2AgentDiffServPolicyAttrStmtPoliceColorConformMode based on Integer32"""
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


_Hm2AgentDiffServPolicyAttrStmtPoliceColorConformMode_Type.__name__ = "Integer32"
_Hm2AgentDiffServPolicyAttrStmtPoliceColorConformMode_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceColorConformMode = _Hm2AgentDiffServPolicyAttrStmtPoliceColorConformMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 40),
    _Hm2AgentDiffServPolicyAttrStmtPoliceColorConformMode_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceColorConformMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceColorConformMode.setStatus("current")
_Hm2AgentDiffServPolicyAttrStmtPoliceColorConformVal_Type = Unsigned32
_Hm2AgentDiffServPolicyAttrStmtPoliceColorConformVal_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceColorConformVal = _Hm2AgentDiffServPolicyAttrStmtPoliceColorConformVal_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 41),
    _Hm2AgentDiffServPolicyAttrStmtPoliceColorConformVal_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceColorConformVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceColorConformVal.setStatus("current")


class _Hm2AgentDiffServPolicyAttrStmtPoliceColorExceedIndex_Type(Unsigned32):
    """Custom type hm2AgentDiffServPolicyAttrStmtPoliceColorExceedIndex based on Unsigned32"""
    defaultValue = 0


_Hm2AgentDiffServPolicyAttrStmtPoliceColorExceedIndex_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceColorExceedIndex = _Hm2AgentDiffServPolicyAttrStmtPoliceColorExceedIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 42),
    _Hm2AgentDiffServPolicyAttrStmtPoliceColorExceedIndex_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceColorExceedIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceColorExceedIndex.setStatus("current")


class _Hm2AgentDiffServPolicyAttrStmtPoliceColorExceedMode_Type(Integer32):
    """Custom type hm2AgentDiffServPolicyAttrStmtPoliceColorExceedMode based on Integer32"""
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


_Hm2AgentDiffServPolicyAttrStmtPoliceColorExceedMode_Type.__name__ = "Integer32"
_Hm2AgentDiffServPolicyAttrStmtPoliceColorExceedMode_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceColorExceedMode = _Hm2AgentDiffServPolicyAttrStmtPoliceColorExceedMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 43),
    _Hm2AgentDiffServPolicyAttrStmtPoliceColorExceedMode_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceColorExceedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceColorExceedMode.setStatus("current")
_Hm2AgentDiffServPolicyAttrStmtPoliceColorExceedVal_Type = Unsigned32
_Hm2AgentDiffServPolicyAttrStmtPoliceColorExceedVal_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtPoliceColorExceedVal = _Hm2AgentDiffServPolicyAttrStmtPoliceColorExceedVal_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 44),
    _Hm2AgentDiffServPolicyAttrStmtPoliceColorExceedVal_Type()
)
hm2AgentDiffServPolicyAttrStmtPoliceColorExceedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtPoliceColorExceedVal.setStatus("current")
_Hm2AgentDiffServPolicyAttrStmtRedirectIntf_Type = InterfaceIndex
_Hm2AgentDiffServPolicyAttrStmtRedirectIntf_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtRedirectIntf = _Hm2AgentDiffServPolicyAttrStmtRedirectIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 45),
    _Hm2AgentDiffServPolicyAttrStmtRedirectIntf_Type()
)
hm2AgentDiffServPolicyAttrStmtRedirectIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtRedirectIntf.setStatus("current")
_Hm2AgentDiffServPolicyAttrStmtMirrorIntf_Type = InterfaceIndex
_Hm2AgentDiffServPolicyAttrStmtMirrorIntf_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtMirrorIntf = _Hm2AgentDiffServPolicyAttrStmtMirrorIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 46),
    _Hm2AgentDiffServPolicyAttrStmtMirrorIntf_Type()
)
hm2AgentDiffServPolicyAttrStmtMirrorIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtMirrorIntf.setStatus("current")
_Hm2AgentDiffServPolicyAttrStmtMarkCosAsSecCos_Type = TruthValue
_Hm2AgentDiffServPolicyAttrStmtMarkCosAsSecCos_Object = MibTableColumn
hm2AgentDiffServPolicyAttrStmtMarkCosAsSecCos = _Hm2AgentDiffServPolicyAttrStmtMarkCosAsSecCos_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 4, 1, 47),
    _Hm2AgentDiffServPolicyAttrStmtMarkCosAsSecCos_Type()
)
hm2AgentDiffServPolicyAttrStmtMarkCosAsSecCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyAttrStmtMarkCosAsSecCos.setStatus("current")
_Hm2AgentDiffServPolicyPerfInTable_Object = MibTable
hm2AgentDiffServPolicyPerfInTable = _Hm2AgentDiffServPolicyPerfInTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 5)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyPerfInTable.setStatus("current")
_Hm2AgentDiffServPolicyPerfInEntry_Object = MibTableRow
hm2AgentDiffServPolicyPerfInEntry = _Hm2AgentDiffServPolicyPerfInEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 5, 1)
)
hm2AgentDiffServPolicyPerfInEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-DIFFSERV-PRIVATE-MIB", "hm2AgentDiffServPolicyIndex"),
    (0, "HM2-PLATFORM-QOS-DIFFSERV-PRIVATE-MIB", "hm2AgentDiffServPolicyInstIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyPerfInEntry.setStatus("current")
_Hm2AgentDiffServPolicyPerfInOfferedPackets_Type = Counter32
_Hm2AgentDiffServPolicyPerfInOfferedPackets_Object = MibTableColumn
hm2AgentDiffServPolicyPerfInOfferedPackets = _Hm2AgentDiffServPolicyPerfInOfferedPackets_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 5, 1, 2),
    _Hm2AgentDiffServPolicyPerfInOfferedPackets_Type()
)
hm2AgentDiffServPolicyPerfInOfferedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyPerfInOfferedPackets.setStatus("current")
_Hm2AgentDiffServPolicyPerfInDiscardedPackets_Type = Counter32
_Hm2AgentDiffServPolicyPerfInDiscardedPackets_Object = MibTableColumn
hm2AgentDiffServPolicyPerfInDiscardedPackets = _Hm2AgentDiffServPolicyPerfInDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 5, 1, 4),
    _Hm2AgentDiffServPolicyPerfInDiscardedPackets_Type()
)
hm2AgentDiffServPolicyPerfInDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyPerfInDiscardedPackets.setStatus("current")
_Hm2AgentDiffServPolicyPerfInHCOfferedPackets_Type = Counter64
_Hm2AgentDiffServPolicyPerfInHCOfferedPackets_Object = MibTableColumn
hm2AgentDiffServPolicyPerfInHCOfferedPackets = _Hm2AgentDiffServPolicyPerfInHCOfferedPackets_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 5, 1, 6),
    _Hm2AgentDiffServPolicyPerfInHCOfferedPackets_Type()
)
hm2AgentDiffServPolicyPerfInHCOfferedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyPerfInHCOfferedPackets.setStatus("current")
_Hm2AgentDiffServPolicyPerfInHCDiscardedPackets_Type = Counter64
_Hm2AgentDiffServPolicyPerfInHCDiscardedPackets_Object = MibTableColumn
hm2AgentDiffServPolicyPerfInHCDiscardedPackets = _Hm2AgentDiffServPolicyPerfInHCDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 5, 1, 8),
    _Hm2AgentDiffServPolicyPerfInHCDiscardedPackets_Type()
)
hm2AgentDiffServPolicyPerfInHCDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyPerfInHCDiscardedPackets.setStatus("current")


class _Hm2AgentDiffServPolicyPerfInStorageType_Type(StorageType):
    """Custom type hm2AgentDiffServPolicyPerfInStorageType based on StorageType"""


_Hm2AgentDiffServPolicyPerfInStorageType_Object = MibTableColumn
hm2AgentDiffServPolicyPerfInStorageType = _Hm2AgentDiffServPolicyPerfInStorageType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 5, 1, 9),
    _Hm2AgentDiffServPolicyPerfInStorageType_Type()
)
hm2AgentDiffServPolicyPerfInStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyPerfInStorageType.setStatus("current")
_Hm2AgentDiffServPolicyPerfInRowStatus_Type = RowStatus
_Hm2AgentDiffServPolicyPerfInRowStatus_Object = MibTableColumn
hm2AgentDiffServPolicyPerfInRowStatus = _Hm2AgentDiffServPolicyPerfInRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 5, 1, 10),
    _Hm2AgentDiffServPolicyPerfInRowStatus_Type()
)
hm2AgentDiffServPolicyPerfInRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyPerfInRowStatus.setStatus("current")
_Hm2AgentDiffServPolicyPerfOutTable_Object = MibTable
hm2AgentDiffServPolicyPerfOutTable = _Hm2AgentDiffServPolicyPerfOutTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 6)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyPerfOutTable.setStatus("current")
_Hm2AgentDiffServPolicyPerfOutEntry_Object = MibTableRow
hm2AgentDiffServPolicyPerfOutEntry = _Hm2AgentDiffServPolicyPerfOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 6, 1)
)
hm2AgentDiffServPolicyPerfOutEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-DIFFSERV-PRIVATE-MIB", "hm2AgentDiffServPolicyIndex"),
    (0, "HM2-PLATFORM-QOS-DIFFSERV-PRIVATE-MIB", "hm2AgentDiffServPolicyInstIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyPerfOutEntry.setStatus("current")
_Hm2AgentDiffServPolicyPerfOutOfferedPackets_Type = Counter32
_Hm2AgentDiffServPolicyPerfOutOfferedPackets_Object = MibTableColumn
hm2AgentDiffServPolicyPerfOutOfferedPackets = _Hm2AgentDiffServPolicyPerfOutOfferedPackets_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 6, 1, 18),
    _Hm2AgentDiffServPolicyPerfOutOfferedPackets_Type()
)
hm2AgentDiffServPolicyPerfOutOfferedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyPerfOutOfferedPackets.setStatus("current")
_Hm2AgentDiffServPolicyPerfOutDiscardedPackets_Type = Counter32
_Hm2AgentDiffServPolicyPerfOutDiscardedPackets_Object = MibTableColumn
hm2AgentDiffServPolicyPerfOutDiscardedPackets = _Hm2AgentDiffServPolicyPerfOutDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 6, 1, 20),
    _Hm2AgentDiffServPolicyPerfOutDiscardedPackets_Type()
)
hm2AgentDiffServPolicyPerfOutDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyPerfOutDiscardedPackets.setStatus("current")
_Hm2AgentDiffServPolicyPerfOutHCOfferedPackets_Type = Counter64
_Hm2AgentDiffServPolicyPerfOutHCOfferedPackets_Object = MibTableColumn
hm2AgentDiffServPolicyPerfOutHCOfferedPackets = _Hm2AgentDiffServPolicyPerfOutHCOfferedPackets_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 6, 1, 22),
    _Hm2AgentDiffServPolicyPerfOutHCOfferedPackets_Type()
)
hm2AgentDiffServPolicyPerfOutHCOfferedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyPerfOutHCOfferedPackets.setStatus("current")
_Hm2AgentDiffServPolicyPerfOutHCDiscardedPackets_Type = Counter64
_Hm2AgentDiffServPolicyPerfOutHCDiscardedPackets_Object = MibTableColumn
hm2AgentDiffServPolicyPerfOutHCDiscardedPackets = _Hm2AgentDiffServPolicyPerfOutHCDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 6, 1, 24),
    _Hm2AgentDiffServPolicyPerfOutHCDiscardedPackets_Type()
)
hm2AgentDiffServPolicyPerfOutHCDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyPerfOutHCDiscardedPackets.setStatus("current")


class _Hm2AgentDiffServPolicyPerfOutStorageType_Type(StorageType):
    """Custom type hm2AgentDiffServPolicyPerfOutStorageType based on StorageType"""


_Hm2AgentDiffServPolicyPerfOutStorageType_Object = MibTableColumn
hm2AgentDiffServPolicyPerfOutStorageType = _Hm2AgentDiffServPolicyPerfOutStorageType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 6, 1, 25),
    _Hm2AgentDiffServPolicyPerfOutStorageType_Type()
)
hm2AgentDiffServPolicyPerfOutStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyPerfOutStorageType.setStatus("current")
_Hm2AgentDiffServPolicyPerfOutRowStatus_Type = RowStatus
_Hm2AgentDiffServPolicyPerfOutRowStatus_Object = MibTableColumn
hm2AgentDiffServPolicyPerfOutRowStatus = _Hm2AgentDiffServPolicyPerfOutRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 3, 6, 1, 26),
    _Hm2AgentDiffServPolicyPerfOutRowStatus_Type()
)
hm2AgentDiffServPolicyPerfOutRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyPerfOutRowStatus.setStatus("current")
_Hm2AgentDiffServServiceGroup_ObjectIdentity = ObjectIdentity
hm2AgentDiffServServiceGroup = _Hm2AgentDiffServServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 4)
)
_Hm2AgentDiffServServiceTable_Object = MibTable
hm2AgentDiffServServiceTable = _Hm2AgentDiffServServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 4, 1)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServServiceTable.setStatus("current")
_Hm2AgentDiffServServiceEntry_Object = MibTableRow
hm2AgentDiffServServiceEntry = _Hm2AgentDiffServServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 4, 1, 1)
)
hm2AgentDiffServServiceEntry.setIndexNames(
    (0, "HM2-PLATFORM-QOS-DIFFSERV-PRIVATE-MIB", "hm2AgentDiffServServiceIfIndex"),
    (0, "HM2-PLATFORM-QOS-DIFFSERV-PRIVATE-MIB", "hm2AgentDiffServServiceIfDirection"),
)
if mibBuilder.loadTexts:
    hm2AgentDiffServServiceEntry.setStatus("current")
_Hm2AgentDiffServServiceIfIndex_Type = InterfaceIndex
_Hm2AgentDiffServServiceIfIndex_Object = MibTableColumn
hm2AgentDiffServServiceIfIndex = _Hm2AgentDiffServServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 4, 1, 1, 1),
    _Hm2AgentDiffServServiceIfIndex_Type()
)
hm2AgentDiffServServiceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDiffServServiceIfIndex.setStatus("current")
_Hm2AgentDiffServServiceIfDirection_Type = IntfDirection
_Hm2AgentDiffServServiceIfDirection_Object = MibTableColumn
hm2AgentDiffServServiceIfDirection = _Hm2AgentDiffServServiceIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 4, 1, 1, 2),
    _Hm2AgentDiffServServiceIfDirection_Type()
)
hm2AgentDiffServServiceIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDiffServServiceIfDirection.setStatus("current")
_Hm2AgentDiffServServicePolicyIndex_Type = Unsigned32
_Hm2AgentDiffServServicePolicyIndex_Object = MibTableColumn
hm2AgentDiffServServicePolicyIndex = _Hm2AgentDiffServServicePolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 4, 1, 1, 3),
    _Hm2AgentDiffServServicePolicyIndex_Type()
)
hm2AgentDiffServServicePolicyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServServicePolicyIndex.setStatus("current")


class _Hm2AgentDiffServServiceIfOperStatus_Type(Integer32):
    """Custom type hm2AgentDiffServServiceIfOperStatus based on Integer32"""
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


_Hm2AgentDiffServServiceIfOperStatus_Type.__name__ = "Integer32"
_Hm2AgentDiffServServiceIfOperStatus_Object = MibTableColumn
hm2AgentDiffServServiceIfOperStatus = _Hm2AgentDiffServServiceIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 4, 1, 1, 4),
    _Hm2AgentDiffServServiceIfOperStatus_Type()
)
hm2AgentDiffServServiceIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDiffServServiceIfOperStatus.setStatus("current")


class _Hm2AgentDiffServServiceStorageType_Type(StorageType):
    """Custom type hm2AgentDiffServServiceStorageType based on StorageType"""


_Hm2AgentDiffServServiceStorageType_Object = MibTableColumn
hm2AgentDiffServServiceStorageType = _Hm2AgentDiffServServiceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 4, 1, 1, 5),
    _Hm2AgentDiffServServiceStorageType_Type()
)
hm2AgentDiffServServiceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServServiceStorageType.setStatus("current")
_Hm2AgentDiffServServiceRowStatus_Type = RowStatus
_Hm2AgentDiffServServiceRowStatus_Object = MibTableColumn
hm2AgentDiffServServiceRowStatus = _Hm2AgentDiffServServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 4, 1, 1, 6),
    _Hm2AgentDiffServServiceRowStatus_Type()
)
hm2AgentDiffServServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentDiffServServiceRowStatus.setStatus("current")
_Hm2AgentDiffServSNMPExtensionGroup_ObjectIdentity = ObjectIdentity
hm2AgentDiffServSNMPExtensionGroup = _Hm2AgentDiffServSNMPExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248)
)
_Hm2AgentDiffServClassNameInUseErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServClassNameInUseErrorReturn = _Hm2AgentDiffServClassNameInUseErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 1)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServClassNameInUseErrorReturn.setStatus("current")
_Hm2AgentDiffServClassHasRulesErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServClassHasRulesErrorReturn = _Hm2AgentDiffServClassHasRulesErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 2)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServClassHasRulesErrorReturn.setStatus("current")
_Hm2AgentDiffServClassHasReferencesErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServClassHasReferencesErrorReturn = _Hm2AgentDiffServClassHasReferencesErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 3)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServClassHasReferencesErrorReturn.setStatus("current")
_Hm2AgentDiffServClassTableFullErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServClassTableFullErrorReturn = _Hm2AgentDiffServClassTableFullErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 4)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServClassTableFullErrorReturn.setStatus("current")
_Hm2AgentDiffServClassRuleTableFullErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServClassRuleTableFullErrorReturn = _Hm2AgentDiffServClassRuleTableFullErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 5)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleTableFullErrorReturn.setStatus("current")
_Hm2AgentDiffServClassIndexOutOfRangeErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServClassIndexOutOfRangeErrorReturn = _Hm2AgentDiffServClassIndexOutOfRangeErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 6)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServClassIndexOutOfRangeErrorReturn.setStatus("current")
_Hm2AgentDiffServClassRuleIndexOutOfRangeErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServClassRuleIndexOutOfRangeErrorReturn = _Hm2AgentDiffServClassRuleIndexOutOfRangeErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 7)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleIndexOutOfRangeErrorReturn.setStatus("current")
_Hm2AgentDiffServClassRuleColorRefErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServClassRuleColorRefErrorReturn = _Hm2AgentDiffServClassRuleColorRefErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 8)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleColorRefErrorReturn.setStatus("current")
_Hm2AgentDiffServClassRuleInUseErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServClassRuleInUseErrorReturn = _Hm2AgentDiffServClassRuleInUseErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 9)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleInUseErrorReturn.setStatus("current")
_Hm2AgentDiffServClassRuleInvalidReferenceErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServClassRuleInvalidReferenceErrorReturn = _Hm2AgentDiffServClassRuleInvalidReferenceErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 10)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleInvalidReferenceErrorReturn.setStatus("current")
_Hm2AgentDiffServClassRuleReferenceLoopErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServClassRuleReferenceLoopErrorReturn = _Hm2AgentDiffServClassRuleReferenceLoopErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 11)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleReferenceLoopErrorReturn.setStatus("current")
_Hm2AgentDiffServClassRuleMatchSecCosErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServClassRuleMatchSecCosErrorReturn = _Hm2AgentDiffServClassRuleMatchSecCosErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 12)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServClassRuleMatchSecCosErrorReturn.setStatus("current")
_Hm2AgentDiffServPolicyTableFullErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServPolicyTableFullErrorReturn = _Hm2AgentDiffServPolicyTableFullErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 13)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyTableFullErrorReturn.setStatus("current")
_Hm2AgentDiffServPolicyNameInUseErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServPolicyNameInUseErrorReturn = _Hm2AgentDiffServPolicyNameInUseErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 14)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyNameInUseErrorReturn.setStatus("current")
_Hm2AgentDiffServPolicyHasInstancesErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServPolicyHasInstancesErrorReturn = _Hm2AgentDiffServPolicyHasInstancesErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 15)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyHasInstancesErrorReturn.setStatus("current")
_Hm2AgentDiffServPolicyHasReferencesErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServPolicyHasReferencesErrorReturn = _Hm2AgentDiffServPolicyHasReferencesErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 16)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyHasReferencesErrorReturn.setStatus("current")
_Hm2AgentDiffServPolicyIndexOutOfRangeErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServPolicyIndexOutOfRangeErrorReturn = _Hm2AgentDiffServPolicyIndexOutOfRangeErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 17)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServPolicyIndexOutOfRangeErrorReturn.setStatus("current")
_Hm2AgentDiffServInstanceIndexOutOfRangeErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServInstanceIndexOutOfRangeErrorReturn = _Hm2AgentDiffServInstanceIndexOutOfRangeErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 18)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServInstanceIndexOutOfRangeErrorReturn.setStatus("current")
_Hm2AgentDiffServInstanceTableFullErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServInstanceTableFullErrorReturn = _Hm2AgentDiffServInstanceTableFullErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 19)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServInstanceTableFullErrorReturn.setStatus("current")
_Hm2AgentDiffServInstanceHasAttributesErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServInstanceHasAttributesErrorReturn = _Hm2AgentDiffServInstanceHasAttributesErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 20)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServInstanceHasAttributesErrorReturn.setStatus("current")
_Hm2AgentDiffServAttributeIndexOutOfRangeErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServAttributeIndexOutOfRangeErrorReturn = _Hm2AgentDiffServAttributeIndexOutOfRangeErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 21)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServAttributeIndexOutOfRangeErrorReturn.setStatus("current")
_Hm2AgentDiffServAttributeTableFullErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServAttributeTableFullErrorReturn = _Hm2AgentDiffServAttributeTableFullErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 22)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServAttributeTableFullErrorReturn.setStatus("current")
_Hm2AgentDiffServAttributeIncompatibilityErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServAttributeIncompatibilityErrorReturn = _Hm2AgentDiffServAttributeIncompatibilityErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 23)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServAttributeIncompatibilityErrorReturn.setStatus("current")
_Hm2AgentDiffServAttributeActionSetCosAsSecCosErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServAttributeActionSetCosAsSecCosErrorReturn = _Hm2AgentDiffServAttributeActionSetCosAsSecCosErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 24)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServAttributeActionSetCosAsSecCosErrorReturn.setStatus("current")
_Hm2AgentDiffServAttributeConformColorClassIndexErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServAttributeConformColorClassIndexErrorReturn = _Hm2AgentDiffServAttributeConformColorClassIndexErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 25)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServAttributeConformColorClassIndexErrorReturn.setStatus("current")
_Hm2AgentDiffServServiceInvalidInterfaceErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServServiceInvalidInterfaceErrorReturn = _Hm2AgentDiffServServiceInvalidInterfaceErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 26)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServServiceInvalidInterfaceErrorReturn.setStatus("current")
_Hm2AgentDiffServServiceInvalidDirectionErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServServiceInvalidDirectionErrorReturn = _Hm2AgentDiffServServiceInvalidDirectionErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 27)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServServiceInvalidDirectionErrorReturn.setStatus("current")
_Hm2AgentDiffServServiceTableFullErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServServiceTableFullErrorReturn = _Hm2AgentDiffServServiceTableFullErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 28)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServServiceTableFullErrorReturn.setStatus("current")
_Hm2AgentDiffServServiceInvalidPolicyTypeErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServServiceInvalidPolicyTypeErrorReturn = _Hm2AgentDiffServServiceInvalidPolicyTypeErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 29)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServServiceInvalidPolicyTypeErrorReturn.setStatus("current")
_Hm2AgentDiffServInstanceExistsErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServInstanceExistsErrorReturn = _Hm2AgentDiffServInstanceExistsErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 30)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServInstanceExistsErrorReturn.setStatus("current")
_Hm2AgentDiffServInstanceInvalidClassErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentDiffServInstanceInvalidClassErrorReturn = _Hm2AgentDiffServInstanceInvalidClassErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 7, 248, 31)
)
if mibBuilder.loadTexts:
    hm2AgentDiffServInstanceInvalidClassErrorReturn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PLATFORM-QOS-DIFFSERV-PRIVATE-MIB",
    **{"QosBurstSize": QosBurstSize,
       "IntfDirection": IntfDirection,
       "EtypeValue": EtypeValue,
       "Ipv6AddressPrefix": Ipv6AddressPrefix,
       "hm2PlatformQOSDiffServPrivate": hm2PlatformQOSDiffServPrivate,
       "hm2AgentDiffServGenStatusGroup": hm2AgentDiffServGenStatusGroup,
       "hm2AgentDiffServGenStatusAdminMode": hm2AgentDiffServGenStatusAdminMode,
       "hm2AgentDiffServGenStatusClassTableSize": hm2AgentDiffServGenStatusClassTableSize,
       "hm2AgentDiffServGenStatusClassTableMax": hm2AgentDiffServGenStatusClassTableMax,
       "hm2AgentDiffServGenStatusClassRuleTableSize": hm2AgentDiffServGenStatusClassRuleTableSize,
       "hm2AgentDiffServGenStatusClassRuleTableMax": hm2AgentDiffServGenStatusClassRuleTableMax,
       "hm2AgentDiffServGenStatusPolicyTableSize": hm2AgentDiffServGenStatusPolicyTableSize,
       "hm2AgentDiffServGenStatusPolicyTableMax": hm2AgentDiffServGenStatusPolicyTableMax,
       "hm2AgentDiffServGenStatusPolicyInstTableSize": hm2AgentDiffServGenStatusPolicyInstTableSize,
       "hm2AgentDiffServGenStatusPolicyInstTableMax": hm2AgentDiffServGenStatusPolicyInstTableMax,
       "hm2AgentDiffServGenStatusPolicyAttrTableSize": hm2AgentDiffServGenStatusPolicyAttrTableSize,
       "hm2AgentDiffServGenStatusPolicyAttrTableMax": hm2AgentDiffServGenStatusPolicyAttrTableMax,
       "hm2AgentDiffServGenStatusServiceTableSize": hm2AgentDiffServGenStatusServiceTableSize,
       "hm2AgentDiffServGenStatusServiceTableMax": hm2AgentDiffServGenStatusServiceTableMax,
       "hm2AgentDiffServClassGroup": hm2AgentDiffServClassGroup,
       "hm2AgentDiffServClassIndexNextFree": hm2AgentDiffServClassIndexNextFree,
       "hm2AgentDiffServClassTable": hm2AgentDiffServClassTable,
       "hm2AgentDiffServClassEntry": hm2AgentDiffServClassEntry,
       "hm2AgentDiffServClassIndex": hm2AgentDiffServClassIndex,
       "hm2AgentDiffServClassName": hm2AgentDiffServClassName,
       "hm2AgentDiffServClassType": hm2AgentDiffServClassType,
       "hm2AgentDiffServClassRuleIndexNextFree": hm2AgentDiffServClassRuleIndexNextFree,
       "hm2AgentDiffServClassStorageType": hm2AgentDiffServClassStorageType,
       "hm2AgentDiffServClassRowStatus": hm2AgentDiffServClassRowStatus,
       "hm2AgentDiffServClassProtoType": hm2AgentDiffServClassProtoType,
       "hm2AgentDiffServClassRuleTable": hm2AgentDiffServClassRuleTable,
       "hm2AgentDiffServClassRuleEntry": hm2AgentDiffServClassRuleEntry,
       "hm2AgentDiffServClassRuleIndex": hm2AgentDiffServClassRuleIndex,
       "hm2AgentDiffServClassRuleMatchEntryType": hm2AgentDiffServClassRuleMatchEntryType,
       "hm2AgentDiffServClassRuleMatchCos": hm2AgentDiffServClassRuleMatchCos,
       "hm2AgentDiffServClassRuleMatchDstIpAddr": hm2AgentDiffServClassRuleMatchDstIpAddr,
       "hm2AgentDiffServClassRuleMatchDstIpMask": hm2AgentDiffServClassRuleMatchDstIpMask,
       "hm2AgentDiffServClassRuleMatchDstL4PortStart": hm2AgentDiffServClassRuleMatchDstL4PortStart,
       "hm2AgentDiffServClassRuleMatchDstL4PortEnd": hm2AgentDiffServClassRuleMatchDstL4PortEnd,
       "hm2AgentDiffServClassRuleMatchDstMacAddr": hm2AgentDiffServClassRuleMatchDstMacAddr,
       "hm2AgentDiffServClassRuleMatchDstMacMask": hm2AgentDiffServClassRuleMatchDstMacMask,
       "hm2AgentDiffServClassRuleMatchEvery": hm2AgentDiffServClassRuleMatchEvery,
       "hm2AgentDiffServClassRuleMatchIpDscp": hm2AgentDiffServClassRuleMatchIpDscp,
       "hm2AgentDiffServClassRuleMatchIpPrecedence": hm2AgentDiffServClassRuleMatchIpPrecedence,
       "hm2AgentDiffServClassRuleMatchIpTosBits": hm2AgentDiffServClassRuleMatchIpTosBits,
       "hm2AgentDiffServClassRuleMatchIpTosMask": hm2AgentDiffServClassRuleMatchIpTosMask,
       "hm2AgentDiffServClassRuleMatchProtocolNum": hm2AgentDiffServClassRuleMatchProtocolNum,
       "hm2AgentDiffServClassRuleMatchRefClassIndex": hm2AgentDiffServClassRuleMatchRefClassIndex,
       "hm2AgentDiffServClassRuleMatchSrcIpAddr": hm2AgentDiffServClassRuleMatchSrcIpAddr,
       "hm2AgentDiffServClassRuleMatchSrcIpMask": hm2AgentDiffServClassRuleMatchSrcIpMask,
       "hm2AgentDiffServClassRuleMatchSrcL4PortStart": hm2AgentDiffServClassRuleMatchSrcL4PortStart,
       "hm2AgentDiffServClassRuleMatchSrcL4PortEnd": hm2AgentDiffServClassRuleMatchSrcL4PortEnd,
       "hm2AgentDiffServClassRuleMatchSrcMacAddr": hm2AgentDiffServClassRuleMatchSrcMacAddr,
       "hm2AgentDiffServClassRuleMatchSrcMacMask": hm2AgentDiffServClassRuleMatchSrcMacMask,
       "hm2AgentDiffServClassRuleMatchExcludeFlag": hm2AgentDiffServClassRuleMatchExcludeFlag,
       "hm2AgentDiffServClassRuleStorageType": hm2AgentDiffServClassRuleStorageType,
       "hm2AgentDiffServClassRuleRowStatus": hm2AgentDiffServClassRuleRowStatus,
       "hm2AgentDiffServClassRuleMatchCos2": hm2AgentDiffServClassRuleMatchCos2,
       "hm2AgentDiffServClassRuleMatchEtypeKey": hm2AgentDiffServClassRuleMatchEtypeKey,
       "hm2AgentDiffServClassRuleMatchEtypeValue": hm2AgentDiffServClassRuleMatchEtypeValue,
       "hm2AgentDiffServClassRuleMatchVlanIdStart": hm2AgentDiffServClassRuleMatchVlanIdStart,
       "hm2AgentDiffServClassRuleMatchVlanIdEnd": hm2AgentDiffServClassRuleMatchVlanIdEnd,
       "hm2AgentDiffServClassRuleMatchVlanId2Start": hm2AgentDiffServClassRuleMatchVlanId2Start,
       "hm2AgentDiffServClassRuleMatchVlanId2End": hm2AgentDiffServClassRuleMatchVlanId2End,
       "hm2AgentDiffServPolicyGroup": hm2AgentDiffServPolicyGroup,
       "hm2AgentDiffServPolicyIndexNextFree": hm2AgentDiffServPolicyIndexNextFree,
       "hm2AgentDiffServPolicyTable": hm2AgentDiffServPolicyTable,
       "hm2AgentDiffServPolicyEntry": hm2AgentDiffServPolicyEntry,
       "hm2AgentDiffServPolicyIndex": hm2AgentDiffServPolicyIndex,
       "hm2AgentDiffServPolicyName": hm2AgentDiffServPolicyName,
       "hm2AgentDiffServPolicyType": hm2AgentDiffServPolicyType,
       "hm2AgentDiffServPolicyInstIndexNextFree": hm2AgentDiffServPolicyInstIndexNextFree,
       "hm2AgentDiffServPolicyStorageType": hm2AgentDiffServPolicyStorageType,
       "hm2AgentDiffServPolicyRowStatus": hm2AgentDiffServPolicyRowStatus,
       "hm2AgentDiffServPolicyInstTable": hm2AgentDiffServPolicyInstTable,
       "hm2AgentDiffServPolicyInstEntry": hm2AgentDiffServPolicyInstEntry,
       "hm2AgentDiffServPolicyInstIndex": hm2AgentDiffServPolicyInstIndex,
       "hm2AgentDiffServPolicyInstClassIndex": hm2AgentDiffServPolicyInstClassIndex,
       "hm2AgentDiffServPolicyInstAttrIndexNextFree": hm2AgentDiffServPolicyInstAttrIndexNextFree,
       "hm2AgentDiffServPolicyInstStorageType": hm2AgentDiffServPolicyInstStorageType,
       "hm2AgentDiffServPolicyInstRowStatus": hm2AgentDiffServPolicyInstRowStatus,
       "hm2AgentDiffServPolicyAttrTable": hm2AgentDiffServPolicyAttrTable,
       "hm2AgentDiffServPolicyAttrEntry": hm2AgentDiffServPolicyAttrEntry,
       "hm2AgentDiffServPolicyAttrIndex": hm2AgentDiffServPolicyAttrIndex,
       "hm2AgentDiffServPolicyAttrStmtEntryType": hm2AgentDiffServPolicyAttrStmtEntryType,
       "hm2AgentDiffServPolicyAttrStmtMarkCosVal": hm2AgentDiffServPolicyAttrStmtMarkCosVal,
       "hm2AgentDiffServPolicyAttrStmtMarkIpDscpVal": hm2AgentDiffServPolicyAttrStmtMarkIpDscpVal,
       "hm2AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal": hm2AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal,
       "hm2AgentDiffServPolicyAttrStmtPoliceConformAct": hm2AgentDiffServPolicyAttrStmtPoliceConformAct,
       "hm2AgentDiffServPolicyAttrStmtPoliceConformVal": hm2AgentDiffServPolicyAttrStmtPoliceConformVal,
       "hm2AgentDiffServPolicyAttrStmtPoliceExceedAct": hm2AgentDiffServPolicyAttrStmtPoliceExceedAct,
       "hm2AgentDiffServPolicyAttrStmtPoliceExceedVal": hm2AgentDiffServPolicyAttrStmtPoliceExceedVal,
       "hm2AgentDiffServPolicyAttrStmtPoliceNonconformAct": hm2AgentDiffServPolicyAttrStmtPoliceNonconformAct,
       "hm2AgentDiffServPolicyAttrStmtPoliceNonconformVal": hm2AgentDiffServPolicyAttrStmtPoliceNonconformVal,
       "hm2AgentDiffServPolicyAttrStmtPoliceSimpleCrate": hm2AgentDiffServPolicyAttrStmtPoliceSimpleCrate,
       "hm2AgentDiffServPolicyAttrStmtPoliceSimpleCburst": hm2AgentDiffServPolicyAttrStmtPoliceSimpleCburst,
       "hm2AgentDiffServPolicyAttrStmtPoliceSinglerateCrate": hm2AgentDiffServPolicyAttrStmtPoliceSinglerateCrate,
       "hm2AgentDiffServPolicyAttrStmtPoliceSinglerateCburst": hm2AgentDiffServPolicyAttrStmtPoliceSinglerateCburst,
       "hm2AgentDiffServPolicyAttrStmtPoliceSinglerateEburst": hm2AgentDiffServPolicyAttrStmtPoliceSinglerateEburst,
       "hm2AgentDiffServPolicyAttrStmtPoliceTworateCrate": hm2AgentDiffServPolicyAttrStmtPoliceTworateCrate,
       "hm2AgentDiffServPolicyAttrStmtPoliceTworateCburst": hm2AgentDiffServPolicyAttrStmtPoliceTworateCburst,
       "hm2AgentDiffServPolicyAttrStmtPoliceTworatePrate": hm2AgentDiffServPolicyAttrStmtPoliceTworatePrate,
       "hm2AgentDiffServPolicyAttrStmtPoliceTworatePburst": hm2AgentDiffServPolicyAttrStmtPoliceTworatePburst,
       "hm2AgentDiffServPolicyAttrStorageType": hm2AgentDiffServPolicyAttrStorageType,
       "hm2AgentDiffServPolicyAttrRowStatus": hm2AgentDiffServPolicyAttrRowStatus,
       "hm2AgentDiffServPolicyAttrStmtAssignQueueId": hm2AgentDiffServPolicyAttrStmtAssignQueueId,
       "hm2AgentDiffServPolicyAttrStmtDrop": hm2AgentDiffServPolicyAttrStmtDrop,
       "hm2AgentDiffServPolicyAttrStmtMarkCos2Val": hm2AgentDiffServPolicyAttrStmtMarkCos2Val,
       "hm2AgentDiffServPolicyAttrStmtPoliceColorConformIndex": hm2AgentDiffServPolicyAttrStmtPoliceColorConformIndex,
       "hm2AgentDiffServPolicyAttrStmtPoliceColorConformMode": hm2AgentDiffServPolicyAttrStmtPoliceColorConformMode,
       "hm2AgentDiffServPolicyAttrStmtPoliceColorConformVal": hm2AgentDiffServPolicyAttrStmtPoliceColorConformVal,
       "hm2AgentDiffServPolicyAttrStmtPoliceColorExceedIndex": hm2AgentDiffServPolicyAttrStmtPoliceColorExceedIndex,
       "hm2AgentDiffServPolicyAttrStmtPoliceColorExceedMode": hm2AgentDiffServPolicyAttrStmtPoliceColorExceedMode,
       "hm2AgentDiffServPolicyAttrStmtPoliceColorExceedVal": hm2AgentDiffServPolicyAttrStmtPoliceColorExceedVal,
       "hm2AgentDiffServPolicyAttrStmtRedirectIntf": hm2AgentDiffServPolicyAttrStmtRedirectIntf,
       "hm2AgentDiffServPolicyAttrStmtMirrorIntf": hm2AgentDiffServPolicyAttrStmtMirrorIntf,
       "hm2AgentDiffServPolicyAttrStmtMarkCosAsSecCos": hm2AgentDiffServPolicyAttrStmtMarkCosAsSecCos,
       "hm2AgentDiffServPolicyPerfInTable": hm2AgentDiffServPolicyPerfInTable,
       "hm2AgentDiffServPolicyPerfInEntry": hm2AgentDiffServPolicyPerfInEntry,
       "hm2AgentDiffServPolicyPerfInOfferedPackets": hm2AgentDiffServPolicyPerfInOfferedPackets,
       "hm2AgentDiffServPolicyPerfInDiscardedPackets": hm2AgentDiffServPolicyPerfInDiscardedPackets,
       "hm2AgentDiffServPolicyPerfInHCOfferedPackets": hm2AgentDiffServPolicyPerfInHCOfferedPackets,
       "hm2AgentDiffServPolicyPerfInHCDiscardedPackets": hm2AgentDiffServPolicyPerfInHCDiscardedPackets,
       "hm2AgentDiffServPolicyPerfInStorageType": hm2AgentDiffServPolicyPerfInStorageType,
       "hm2AgentDiffServPolicyPerfInRowStatus": hm2AgentDiffServPolicyPerfInRowStatus,
       "hm2AgentDiffServPolicyPerfOutTable": hm2AgentDiffServPolicyPerfOutTable,
       "hm2AgentDiffServPolicyPerfOutEntry": hm2AgentDiffServPolicyPerfOutEntry,
       "hm2AgentDiffServPolicyPerfOutOfferedPackets": hm2AgentDiffServPolicyPerfOutOfferedPackets,
       "hm2AgentDiffServPolicyPerfOutDiscardedPackets": hm2AgentDiffServPolicyPerfOutDiscardedPackets,
       "hm2AgentDiffServPolicyPerfOutHCOfferedPackets": hm2AgentDiffServPolicyPerfOutHCOfferedPackets,
       "hm2AgentDiffServPolicyPerfOutHCDiscardedPackets": hm2AgentDiffServPolicyPerfOutHCDiscardedPackets,
       "hm2AgentDiffServPolicyPerfOutStorageType": hm2AgentDiffServPolicyPerfOutStorageType,
       "hm2AgentDiffServPolicyPerfOutRowStatus": hm2AgentDiffServPolicyPerfOutRowStatus,
       "hm2AgentDiffServServiceGroup": hm2AgentDiffServServiceGroup,
       "hm2AgentDiffServServiceTable": hm2AgentDiffServServiceTable,
       "hm2AgentDiffServServiceEntry": hm2AgentDiffServServiceEntry,
       "hm2AgentDiffServServiceIfIndex": hm2AgentDiffServServiceIfIndex,
       "hm2AgentDiffServServiceIfDirection": hm2AgentDiffServServiceIfDirection,
       "hm2AgentDiffServServicePolicyIndex": hm2AgentDiffServServicePolicyIndex,
       "hm2AgentDiffServServiceIfOperStatus": hm2AgentDiffServServiceIfOperStatus,
       "hm2AgentDiffServServiceStorageType": hm2AgentDiffServServiceStorageType,
       "hm2AgentDiffServServiceRowStatus": hm2AgentDiffServServiceRowStatus,
       "hm2AgentDiffServSNMPExtensionGroup": hm2AgentDiffServSNMPExtensionGroup,
       "hm2AgentDiffServClassNameInUseErrorReturn": hm2AgentDiffServClassNameInUseErrorReturn,
       "hm2AgentDiffServClassHasRulesErrorReturn": hm2AgentDiffServClassHasRulesErrorReturn,
       "hm2AgentDiffServClassHasReferencesErrorReturn": hm2AgentDiffServClassHasReferencesErrorReturn,
       "hm2AgentDiffServClassTableFullErrorReturn": hm2AgentDiffServClassTableFullErrorReturn,
       "hm2AgentDiffServClassRuleTableFullErrorReturn": hm2AgentDiffServClassRuleTableFullErrorReturn,
       "hm2AgentDiffServClassIndexOutOfRangeErrorReturn": hm2AgentDiffServClassIndexOutOfRangeErrorReturn,
       "hm2AgentDiffServClassRuleIndexOutOfRangeErrorReturn": hm2AgentDiffServClassRuleIndexOutOfRangeErrorReturn,
       "hm2AgentDiffServClassRuleColorRefErrorReturn": hm2AgentDiffServClassRuleColorRefErrorReturn,
       "hm2AgentDiffServClassRuleInUseErrorReturn": hm2AgentDiffServClassRuleInUseErrorReturn,
       "hm2AgentDiffServClassRuleInvalidReferenceErrorReturn": hm2AgentDiffServClassRuleInvalidReferenceErrorReturn,
       "hm2AgentDiffServClassRuleReferenceLoopErrorReturn": hm2AgentDiffServClassRuleReferenceLoopErrorReturn,
       "hm2AgentDiffServClassRuleMatchSecCosErrorReturn": hm2AgentDiffServClassRuleMatchSecCosErrorReturn,
       "hm2AgentDiffServPolicyTableFullErrorReturn": hm2AgentDiffServPolicyTableFullErrorReturn,
       "hm2AgentDiffServPolicyNameInUseErrorReturn": hm2AgentDiffServPolicyNameInUseErrorReturn,
       "hm2AgentDiffServPolicyHasInstancesErrorReturn": hm2AgentDiffServPolicyHasInstancesErrorReturn,
       "hm2AgentDiffServPolicyHasReferencesErrorReturn": hm2AgentDiffServPolicyHasReferencesErrorReturn,
       "hm2AgentDiffServPolicyIndexOutOfRangeErrorReturn": hm2AgentDiffServPolicyIndexOutOfRangeErrorReturn,
       "hm2AgentDiffServInstanceIndexOutOfRangeErrorReturn": hm2AgentDiffServInstanceIndexOutOfRangeErrorReturn,
       "hm2AgentDiffServInstanceTableFullErrorReturn": hm2AgentDiffServInstanceTableFullErrorReturn,
       "hm2AgentDiffServInstanceHasAttributesErrorReturn": hm2AgentDiffServInstanceHasAttributesErrorReturn,
       "hm2AgentDiffServAttributeIndexOutOfRangeErrorReturn": hm2AgentDiffServAttributeIndexOutOfRangeErrorReturn,
       "hm2AgentDiffServAttributeTableFullErrorReturn": hm2AgentDiffServAttributeTableFullErrorReturn,
       "hm2AgentDiffServAttributeIncompatibilityErrorReturn": hm2AgentDiffServAttributeIncompatibilityErrorReturn,
       "hm2AgentDiffServAttributeActionSetCosAsSecCosErrorReturn": hm2AgentDiffServAttributeActionSetCosAsSecCosErrorReturn,
       "hm2AgentDiffServAttributeConformColorClassIndexErrorReturn": hm2AgentDiffServAttributeConformColorClassIndexErrorReturn,
       "hm2AgentDiffServServiceInvalidInterfaceErrorReturn": hm2AgentDiffServServiceInvalidInterfaceErrorReturn,
       "hm2AgentDiffServServiceInvalidDirectionErrorReturn": hm2AgentDiffServServiceInvalidDirectionErrorReturn,
       "hm2AgentDiffServServiceTableFullErrorReturn": hm2AgentDiffServServiceTableFullErrorReturn,
       "hm2AgentDiffServServiceInvalidPolicyTypeErrorReturn": hm2AgentDiffServServiceInvalidPolicyTypeErrorReturn,
       "hm2AgentDiffServInstanceExistsErrorReturn": hm2AgentDiffServInstanceExistsErrorReturn,
       "hm2AgentDiffServInstanceInvalidClassErrorReturn": hm2AgentDiffServInstanceInvalidClassErrorReturn}
)

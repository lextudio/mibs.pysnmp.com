# SNMP MIB module (HPN-ICF-PBR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-PBR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:25 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfPBR = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113)
)
hpnicfPBR.setRevisions(
        ("2010-12-10 15:58",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfPBRObjects_ObjectIdentity = ObjectIdentity
hpnicfPBRObjects = _HpnicfPBRObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 1)
)
_HpnicfPBRGlobal_ObjectIdentity = ObjectIdentity
hpnicfPBRGlobal = _HpnicfPBRGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 1, 1)
)


class _HpnicfPBRNexthopTrapEnabled_Type(TruthValue):
    """Custom type hpnicfPBRNexthopTrapEnabled based on TruthValue"""


_HpnicfPBRNexthopTrapEnabled_Object = MibScalar
hpnicfPBRNexthopTrapEnabled = _HpnicfPBRNexthopTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 1, 1, 1),
    _HpnicfPBRNexthopTrapEnabled_Type()
)
hpnicfPBRNexthopTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPBRNexthopTrapEnabled.setStatus("current")


class _HpnicfPBRLocalPolicy_Type(DisplayString):
    """Custom type hpnicfPBRLocalPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_HpnicfPBRLocalPolicy_Type.__name__ = "DisplayString"
_HpnicfPBRLocalPolicy_Object = MibScalar
hpnicfPBRLocalPolicy = _HpnicfPBRLocalPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 1, 1, 2),
    _HpnicfPBRLocalPolicy_Type()
)
hpnicfPBRLocalPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPBRLocalPolicy.setStatus("current")


class _HpnicfPBRIPv6NexthopTrapEnabled_Type(TruthValue):
    """Custom type hpnicfPBRIPv6NexthopTrapEnabled based on TruthValue"""


_HpnicfPBRIPv6NexthopTrapEnabled_Object = MibScalar
hpnicfPBRIPv6NexthopTrapEnabled = _HpnicfPBRIPv6NexthopTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 1, 1, 3),
    _HpnicfPBRIPv6NexthopTrapEnabled_Type()
)
hpnicfPBRIPv6NexthopTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPBRIPv6NexthopTrapEnabled.setStatus("current")
_HpnicfPBRMibTrap_ObjectIdentity = ObjectIdentity
hpnicfPBRMibTrap = _HpnicfPBRMibTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 1, 2)
)
_HpnicfPBRTrapObjects_ObjectIdentity = ObjectIdentity
hpnicfPBRTrapObjects = _HpnicfPBRTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 1, 2, 1)
)
_HpnicfPBRNexthopAddrType_Type = InetAddressType
_HpnicfPBRNexthopAddrType_Object = MibScalar
hpnicfPBRNexthopAddrType = _HpnicfPBRNexthopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 1, 2, 1, 1),
    _HpnicfPBRNexthopAddrType_Type()
)
hpnicfPBRNexthopAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPBRNexthopAddrType.setStatus("current")
_HpnicfPBRNexthopAddr_Type = InetAddress
_HpnicfPBRNexthopAddr_Object = MibScalar
hpnicfPBRNexthopAddr = _HpnicfPBRNexthopAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 1, 2, 1, 2),
    _HpnicfPBRNexthopAddr_Type()
)
hpnicfPBRNexthopAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPBRNexthopAddr.setStatus("current")
_HpnicfPBRTraps_ObjectIdentity = ObjectIdentity
hpnicfPBRTraps = _HpnicfPBRTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 1, 2, 2)
)
_HpnicfPBRTrapsPrefix_ObjectIdentity = ObjectIdentity
hpnicfPBRTrapsPrefix = _HpnicfPBRTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 1, 2, 2, 0)
)
_HpnicfPBRTables_ObjectIdentity = ObjectIdentity
hpnicfPBRTables = _HpnicfPBRTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2)
)
_HpnicfPBRMibPolicyNodeTable_Object = MibTable
hpnicfPBRMibPolicyNodeTable = _HpnicfPBRMibPolicyNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfPBRMibPolicyNodeTable.setStatus("current")
_HpnicfPBRMibPolicyNodeEntry_Object = MibTableRow
hpnicfPBRMibPolicyNodeEntry = _HpnicfPBRMibPolicyNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 1, 1)
)
hpnicfPBRMibPolicyNodeEntry.setIndexNames(
    (0, "HPN-ICF-PBR-MIB", "hpnicfPBRMibPolicyNodeAddrType"),
    (0, "HPN-ICF-PBR-MIB", "hpnicfPBRMibPolicyName"),
    (0, "HPN-ICF-PBR-MIB", "hpnicfPBRMibPolicyNodeId"),
)
if mibBuilder.loadTexts:
    hpnicfPBRMibPolicyNodeEntry.setStatus("current")
_HpnicfPBRMibPolicyNodeAddrType_Type = InetAddressType
_HpnicfPBRMibPolicyNodeAddrType_Object = MibTableColumn
hpnicfPBRMibPolicyNodeAddrType = _HpnicfPBRMibPolicyNodeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 1, 1, 1),
    _HpnicfPBRMibPolicyNodeAddrType_Type()
)
hpnicfPBRMibPolicyNodeAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPBRMibPolicyNodeAddrType.setStatus("current")


class _HpnicfPBRMibPolicyName_Type(DisplayString):
    """Custom type hpnicfPBRMibPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_HpnicfPBRMibPolicyName_Type.__name__ = "DisplayString"
_HpnicfPBRMibPolicyName_Object = MibTableColumn
hpnicfPBRMibPolicyName = _HpnicfPBRMibPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 1, 1, 2),
    _HpnicfPBRMibPolicyName_Type()
)
hpnicfPBRMibPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPBRMibPolicyName.setStatus("current")


class _HpnicfPBRMibPolicyNodeId_Type(Integer32):
    """Custom type hpnicfPBRMibPolicyNodeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfPBRMibPolicyNodeId_Type.__name__ = "Integer32"
_HpnicfPBRMibPolicyNodeId_Object = MibTableColumn
hpnicfPBRMibPolicyNodeId = _HpnicfPBRMibPolicyNodeId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 1, 1, 3),
    _HpnicfPBRMibPolicyNodeId_Type()
)
hpnicfPBRMibPolicyNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPBRMibPolicyNodeId.setStatus("current")


class _HpnicfPBRMibPolicyNodeMode_Type(TruthValue):
    """Custom type hpnicfPBRMibPolicyNodeMode based on TruthValue"""


_HpnicfPBRMibPolicyNodeMode_Object = MibTableColumn
hpnicfPBRMibPolicyNodeMode = _HpnicfPBRMibPolicyNodeMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 1, 1, 4),
    _HpnicfPBRMibPolicyNodeMode_Type()
)
hpnicfPBRMibPolicyNodeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPBRMibPolicyNodeMode.setStatus("current")
_HpnicfPBRMibPolicyNodeRowStatus_Type = RowStatus
_HpnicfPBRMibPolicyNodeRowStatus_Object = MibTableColumn
hpnicfPBRMibPolicyNodeRowStatus = _HpnicfPBRMibPolicyNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 1, 1, 5),
    _HpnicfPBRMibPolicyNodeRowStatus_Type()
)
hpnicfPBRMibPolicyNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPBRMibPolicyNodeRowStatus.setStatus("current")
_HpnicfPBRMibIfPolicyTable_Object = MibTable
hpnicfPBRMibIfPolicyTable = _HpnicfPBRMibIfPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfPBRMibIfPolicyTable.setStatus("current")
_HpnicfPBRMibIfPolicyEntry_Object = MibTableRow
hpnicfPBRMibIfPolicyEntry = _HpnicfPBRMibIfPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 2, 1)
)
hpnicfPBRMibIfPolicyEntry.setIndexNames(
    (0, "HPN-ICF-PBR-MIB", "hpnicfPBRMibPolicyAddressType"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPBRMibIfPolicyEntry.setStatus("current")
_HpnicfPBRMibPolicyAddressType_Type = InetAddressType
_HpnicfPBRMibPolicyAddressType_Object = MibTableColumn
hpnicfPBRMibPolicyAddressType = _HpnicfPBRMibPolicyAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 2, 1, 1),
    _HpnicfPBRMibPolicyAddressType_Type()
)
hpnicfPBRMibPolicyAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPBRMibPolicyAddressType.setStatus("current")


class _HpnicfPBRMibAppliedPolicyName_Type(DisplayString):
    """Custom type hpnicfPBRMibAppliedPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_HpnicfPBRMibAppliedPolicyName_Type.__name__ = "DisplayString"
_HpnicfPBRMibAppliedPolicyName_Object = MibTableColumn
hpnicfPBRMibAppliedPolicyName = _HpnicfPBRMibAppliedPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 2, 1, 2),
    _HpnicfPBRMibAppliedPolicyName_Type()
)
hpnicfPBRMibAppliedPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPBRMibAppliedPolicyName.setStatus("current")
_HpnicfPBRMibIfPolicyRowStatus_Type = RowStatus
_HpnicfPBRMibIfPolicyRowStatus_Object = MibTableColumn
hpnicfPBRMibIfPolicyRowStatus = _HpnicfPBRMibIfPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 2, 1, 3),
    _HpnicfPBRMibIfPolicyRowStatus_Type()
)
hpnicfPBRMibIfPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPBRMibIfPolicyRowStatus.setStatus("current")
_HpnicfPBRMibMatchAclTable_Object = MibTable
hpnicfPBRMibMatchAclTable = _HpnicfPBRMibMatchAclTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfPBRMibMatchAclTable.setStatus("current")
_HpnicfPBRMibMatchAclEntry_Object = MibTableRow
hpnicfPBRMibMatchAclEntry = _HpnicfPBRMibMatchAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 3, 1)
)
hpnicfPBRMibMatchAclEntry.setIndexNames(
    (0, "HPN-ICF-PBR-MIB", "hpnicfPBRMibPolicyNodeAddrType"),
    (0, "HPN-ICF-PBR-MIB", "hpnicfPBRMibPolicyName"),
    (0, "HPN-ICF-PBR-MIB", "hpnicfPBRMibPolicyNodeId"),
)
if mibBuilder.loadTexts:
    hpnicfPBRMibMatchAclEntry.setStatus("current")
_HpnicfPBRMibAclGroupId_Type = Integer32
_HpnicfPBRMibAclGroupId_Object = MibTableColumn
hpnicfPBRMibAclGroupId = _HpnicfPBRMibAclGroupId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 3, 1, 1),
    _HpnicfPBRMibAclGroupId_Type()
)
hpnicfPBRMibAclGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPBRMibAclGroupId.setStatus("current")
_HpnicfPBRMibApplyPrecedenceTable_Object = MibTable
hpnicfPBRMibApplyPrecedenceTable = _HpnicfPBRMibApplyPrecedenceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyPrecedenceTable.setStatus("current")
_HpnicfPBRMibApplyPrecedenceEntry_Object = MibTableRow
hpnicfPBRMibApplyPrecedenceEntry = _HpnicfPBRMibApplyPrecedenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 4, 1)
)
hpnicfPBRMibApplyPrecedenceEntry.setIndexNames(
    (0, "HPN-ICF-PBR-MIB", "hpnicfPBRMibPolicyNodeAddrType"),
    (0, "HPN-ICF-PBR-MIB", "hpnicfPBRMibPolicyName"),
    (0, "HPN-ICF-PBR-MIB", "hpnicfPBRMibPolicyNodeId"),
)
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyPrecedenceEntry.setStatus("current")
_HpnicfPBRMibApplyPrecedenceValue_Type = Integer32
_HpnicfPBRMibApplyPrecedenceValue_Object = MibTableColumn
hpnicfPBRMibApplyPrecedenceValue = _HpnicfPBRMibApplyPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 4, 1, 1),
    _HpnicfPBRMibApplyPrecedenceValue_Type()
)
hpnicfPBRMibApplyPrecedenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyPrecedenceValue.setStatus("current")
_HpnicfPBRMibApplyNexthopTable_Object = MibTable
hpnicfPBRMibApplyNexthopTable = _HpnicfPBRMibApplyNexthopTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyNexthopTable.setStatus("current")
_HpnicfPBRMibApplyNexthopEntry_Object = MibTableRow
hpnicfPBRMibApplyNexthopEntry = _HpnicfPBRMibApplyNexthopEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 5, 1)
)
hpnicfPBRMibApplyNexthopEntry.setIndexNames(
    (0, "HPN-ICF-PBR-MIB", "hpnicfPBRMibPolicyNodeAddrType"),
    (0, "HPN-ICF-PBR-MIB", "hpnicfPBRMibPolicyName"),
    (0, "HPN-ICF-PBR-MIB", "hpnicfPBRMibPolicyNodeId"),
    (0, "HPN-ICF-PBR-MIB", "hpnicfPBRMibApplyNexthopIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyNexthopEntry.setStatus("current")


class _HpnicfPBRMibApplyNexthopIndex_Type(Integer32):
    """Custom type hpnicfPBRMibApplyNexthopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfPBRMibApplyNexthopIndex_Type.__name__ = "Integer32"
_HpnicfPBRMibApplyNexthopIndex_Object = MibTableColumn
hpnicfPBRMibApplyNexthopIndex = _HpnicfPBRMibApplyNexthopIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 5, 1, 1),
    _HpnicfPBRMibApplyNexthopIndex_Type()
)
hpnicfPBRMibApplyNexthopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyNexthopIndex.setStatus("current")


class _HpnicfPBRMibApplyNexthopVpnName_Type(DisplayString):
    """Custom type hpnicfPBRMibApplyNexthopVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HpnicfPBRMibApplyNexthopVpnName_Type.__name__ = "DisplayString"
_HpnicfPBRMibApplyNexthopVpnName_Object = MibTableColumn
hpnicfPBRMibApplyNexthopVpnName = _HpnicfPBRMibApplyNexthopVpnName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 5, 1, 2),
    _HpnicfPBRMibApplyNexthopVpnName_Type()
)
hpnicfPBRMibApplyNexthopVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyNexthopVpnName.setStatus("current")
_HpnicfPBRMibApplyNexthopAddressType_Type = InetAddressType
_HpnicfPBRMibApplyNexthopAddressType_Object = MibTableColumn
hpnicfPBRMibApplyNexthopAddressType = _HpnicfPBRMibApplyNexthopAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 5, 1, 3),
    _HpnicfPBRMibApplyNexthopAddressType_Type()
)
hpnicfPBRMibApplyNexthopAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyNexthopAddressType.setStatus("current")
_HpnicfPBRMibApplyNexthopAddress_Type = InetAddress
_HpnicfPBRMibApplyNexthopAddress_Object = MibTableColumn
hpnicfPBRMibApplyNexthopAddress = _HpnicfPBRMibApplyNexthopAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 5, 1, 4),
    _HpnicfPBRMibApplyNexthopAddress_Type()
)
hpnicfPBRMibApplyNexthopAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyNexthopAddress.setStatus("current")
_HpnicfPBRMibApplyNexthopTrackId_Type = Integer32
_HpnicfPBRMibApplyNexthopTrackId_Object = MibTableColumn
hpnicfPBRMibApplyNexthopTrackId = _HpnicfPBRMibApplyNexthopTrackId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 5, 1, 5),
    _HpnicfPBRMibApplyNexthopTrackId_Type()
)
hpnicfPBRMibApplyNexthopTrackId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyNexthopTrackId.setStatus("current")


class _HpnicfPBRMibApplyNexthopDirect_Type(TruthValue):
    """Custom type hpnicfPBRMibApplyNexthopDirect based on TruthValue"""


_HpnicfPBRMibApplyNexthopDirect_Object = MibTableColumn
hpnicfPBRMibApplyNexthopDirect = _HpnicfPBRMibApplyNexthopDirect_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 5, 1, 6),
    _HpnicfPBRMibApplyNexthopDirect_Type()
)
hpnicfPBRMibApplyNexthopDirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyNexthopDirect.setStatus("current")
_HpnicfPBRMibApplyNexthopRowStatus_Type = RowStatus
_HpnicfPBRMibApplyNexthopRowStatus_Object = MibTableColumn
hpnicfPBRMibApplyNexthopRowStatus = _HpnicfPBRMibApplyNexthopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 5, 1, 7),
    _HpnicfPBRMibApplyNexthopRowStatus_Type()
)
hpnicfPBRMibApplyNexthopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyNexthopRowStatus.setStatus("current")
_HpnicfPBRMibApplyDefaultNexthopTable_Object = MibTable
hpnicfPBRMibApplyDefaultNexthopTable = _HpnicfPBRMibApplyDefaultNexthopTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyDefaultNexthopTable.setStatus("current")
_HpnicfPBRMibApplyDefaultNexthopEntry_Object = MibTableRow
hpnicfPBRMibApplyDefaultNexthopEntry = _HpnicfPBRMibApplyDefaultNexthopEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 6, 1)
)
hpnicfPBRMibApplyDefaultNexthopEntry.setIndexNames(
    (0, "HPN-ICF-PBR-MIB", "hpnicfPBRMibPolicyNodeAddrType"),
    (0, "HPN-ICF-PBR-MIB", "hpnicfPBRMibPolicyName"),
    (0, "HPN-ICF-PBR-MIB", "hpnicfPBRMibPolicyNodeId"),
    (0, "HPN-ICF-PBR-MIB", "hpnicfPBRMibApplyDefaultNexthopIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyDefaultNexthopEntry.setStatus("current")


class _HpnicfPBRMibApplyDefaultNexthopIndex_Type(Integer32):
    """Custom type hpnicfPBRMibApplyDefaultNexthopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfPBRMibApplyDefaultNexthopIndex_Type.__name__ = "Integer32"
_HpnicfPBRMibApplyDefaultNexthopIndex_Object = MibTableColumn
hpnicfPBRMibApplyDefaultNexthopIndex = _HpnicfPBRMibApplyDefaultNexthopIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 6, 1, 1),
    _HpnicfPBRMibApplyDefaultNexthopIndex_Type()
)
hpnicfPBRMibApplyDefaultNexthopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyDefaultNexthopIndex.setStatus("current")


class _HpnicfPBRMibApplyDefaultNexthopVpnName_Type(DisplayString):
    """Custom type hpnicfPBRMibApplyDefaultNexthopVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HpnicfPBRMibApplyDefaultNexthopVpnName_Type.__name__ = "DisplayString"
_HpnicfPBRMibApplyDefaultNexthopVpnName_Object = MibTableColumn
hpnicfPBRMibApplyDefaultNexthopVpnName = _HpnicfPBRMibApplyDefaultNexthopVpnName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 6, 1, 2),
    _HpnicfPBRMibApplyDefaultNexthopVpnName_Type()
)
hpnicfPBRMibApplyDefaultNexthopVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyDefaultNexthopVpnName.setStatus("current")
_HpnicfPBRMibApplyDefaultNexthopAddressType_Type = InetAddressType
_HpnicfPBRMibApplyDefaultNexthopAddressType_Object = MibTableColumn
hpnicfPBRMibApplyDefaultNexthopAddressType = _HpnicfPBRMibApplyDefaultNexthopAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 6, 1, 3),
    _HpnicfPBRMibApplyDefaultNexthopAddressType_Type()
)
hpnicfPBRMibApplyDefaultNexthopAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyDefaultNexthopAddressType.setStatus("current")
_HpnicfPBRMibApplyDefaultNexthopAddress_Type = InetAddress
_HpnicfPBRMibApplyDefaultNexthopAddress_Object = MibTableColumn
hpnicfPBRMibApplyDefaultNexthopAddress = _HpnicfPBRMibApplyDefaultNexthopAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 6, 1, 4),
    _HpnicfPBRMibApplyDefaultNexthopAddress_Type()
)
hpnicfPBRMibApplyDefaultNexthopAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyDefaultNexthopAddress.setStatus("current")
_HpnicfPBRMibApplyDefaultNexthopTrackId_Type = Integer32
_HpnicfPBRMibApplyDefaultNexthopTrackId_Object = MibTableColumn
hpnicfPBRMibApplyDefaultNexthopTrackId = _HpnicfPBRMibApplyDefaultNexthopTrackId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 6, 1, 5),
    _HpnicfPBRMibApplyDefaultNexthopTrackId_Type()
)
hpnicfPBRMibApplyDefaultNexthopTrackId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyDefaultNexthopTrackId.setStatus("current")


class _HpnicfPBRMibApplyDefaultNexthopDirect_Type(TruthValue):
    """Custom type hpnicfPBRMibApplyDefaultNexthopDirect based on TruthValue"""


_HpnicfPBRMibApplyDefaultNexthopDirect_Object = MibTableColumn
hpnicfPBRMibApplyDefaultNexthopDirect = _HpnicfPBRMibApplyDefaultNexthopDirect_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 6, 1, 6),
    _HpnicfPBRMibApplyDefaultNexthopDirect_Type()
)
hpnicfPBRMibApplyDefaultNexthopDirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyDefaultNexthopDirect.setStatus("current")
_HpnicfPBRMibApplyDefaultNexthopRowStatus_Type = RowStatus
_HpnicfPBRMibApplyDefaultNexthopRowStatus_Object = MibTableColumn
hpnicfPBRMibApplyDefaultNexthopRowStatus = _HpnicfPBRMibApplyDefaultNexthopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 2, 6, 1, 7),
    _HpnicfPBRMibApplyDefaultNexthopRowStatus_Type()
)
hpnicfPBRMibApplyDefaultNexthopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPBRMibApplyDefaultNexthopRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfPBRNexthopFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113, 1, 2, 2, 0, 1)
)
hpnicfPBRNexthopFailedTrap.setObjects(
      *(("HPN-ICF-PBR-MIB", "hpnicfPBRNexthopAddrType"),
        ("HPN-ICF-PBR-MIB", "hpnicfPBRNexthopAddr"))
)
if mibBuilder.loadTexts:
    hpnicfPBRNexthopFailedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-PBR-MIB",
    **{"hpnicfPBR": hpnicfPBR,
       "hpnicfPBRObjects": hpnicfPBRObjects,
       "hpnicfPBRGlobal": hpnicfPBRGlobal,
       "hpnicfPBRNexthopTrapEnabled": hpnicfPBRNexthopTrapEnabled,
       "hpnicfPBRLocalPolicy": hpnicfPBRLocalPolicy,
       "hpnicfPBRIPv6NexthopTrapEnabled": hpnicfPBRIPv6NexthopTrapEnabled,
       "hpnicfPBRMibTrap": hpnicfPBRMibTrap,
       "hpnicfPBRTrapObjects": hpnicfPBRTrapObjects,
       "hpnicfPBRNexthopAddrType": hpnicfPBRNexthopAddrType,
       "hpnicfPBRNexthopAddr": hpnicfPBRNexthopAddr,
       "hpnicfPBRTraps": hpnicfPBRTraps,
       "hpnicfPBRTrapsPrefix": hpnicfPBRTrapsPrefix,
       "hpnicfPBRNexthopFailedTrap": hpnicfPBRNexthopFailedTrap,
       "hpnicfPBRTables": hpnicfPBRTables,
       "hpnicfPBRMibPolicyNodeTable": hpnicfPBRMibPolicyNodeTable,
       "hpnicfPBRMibPolicyNodeEntry": hpnicfPBRMibPolicyNodeEntry,
       "hpnicfPBRMibPolicyNodeAddrType": hpnicfPBRMibPolicyNodeAddrType,
       "hpnicfPBRMibPolicyName": hpnicfPBRMibPolicyName,
       "hpnicfPBRMibPolicyNodeId": hpnicfPBRMibPolicyNodeId,
       "hpnicfPBRMibPolicyNodeMode": hpnicfPBRMibPolicyNodeMode,
       "hpnicfPBRMibPolicyNodeRowStatus": hpnicfPBRMibPolicyNodeRowStatus,
       "hpnicfPBRMibIfPolicyTable": hpnicfPBRMibIfPolicyTable,
       "hpnicfPBRMibIfPolicyEntry": hpnicfPBRMibIfPolicyEntry,
       "hpnicfPBRMibPolicyAddressType": hpnicfPBRMibPolicyAddressType,
       "hpnicfPBRMibAppliedPolicyName": hpnicfPBRMibAppliedPolicyName,
       "hpnicfPBRMibIfPolicyRowStatus": hpnicfPBRMibIfPolicyRowStatus,
       "hpnicfPBRMibMatchAclTable": hpnicfPBRMibMatchAclTable,
       "hpnicfPBRMibMatchAclEntry": hpnicfPBRMibMatchAclEntry,
       "hpnicfPBRMibAclGroupId": hpnicfPBRMibAclGroupId,
       "hpnicfPBRMibApplyPrecedenceTable": hpnicfPBRMibApplyPrecedenceTable,
       "hpnicfPBRMibApplyPrecedenceEntry": hpnicfPBRMibApplyPrecedenceEntry,
       "hpnicfPBRMibApplyPrecedenceValue": hpnicfPBRMibApplyPrecedenceValue,
       "hpnicfPBRMibApplyNexthopTable": hpnicfPBRMibApplyNexthopTable,
       "hpnicfPBRMibApplyNexthopEntry": hpnicfPBRMibApplyNexthopEntry,
       "hpnicfPBRMibApplyNexthopIndex": hpnicfPBRMibApplyNexthopIndex,
       "hpnicfPBRMibApplyNexthopVpnName": hpnicfPBRMibApplyNexthopVpnName,
       "hpnicfPBRMibApplyNexthopAddressType": hpnicfPBRMibApplyNexthopAddressType,
       "hpnicfPBRMibApplyNexthopAddress": hpnicfPBRMibApplyNexthopAddress,
       "hpnicfPBRMibApplyNexthopTrackId": hpnicfPBRMibApplyNexthopTrackId,
       "hpnicfPBRMibApplyNexthopDirect": hpnicfPBRMibApplyNexthopDirect,
       "hpnicfPBRMibApplyNexthopRowStatus": hpnicfPBRMibApplyNexthopRowStatus,
       "hpnicfPBRMibApplyDefaultNexthopTable": hpnicfPBRMibApplyDefaultNexthopTable,
       "hpnicfPBRMibApplyDefaultNexthopEntry": hpnicfPBRMibApplyDefaultNexthopEntry,
       "hpnicfPBRMibApplyDefaultNexthopIndex": hpnicfPBRMibApplyDefaultNexthopIndex,
       "hpnicfPBRMibApplyDefaultNexthopVpnName": hpnicfPBRMibApplyDefaultNexthopVpnName,
       "hpnicfPBRMibApplyDefaultNexthopAddressType": hpnicfPBRMibApplyDefaultNexthopAddressType,
       "hpnicfPBRMibApplyDefaultNexthopAddress": hpnicfPBRMibApplyDefaultNexthopAddress,
       "hpnicfPBRMibApplyDefaultNexthopTrackId": hpnicfPBRMibApplyDefaultNexthopTrackId,
       "hpnicfPBRMibApplyDefaultNexthopDirect": hpnicfPBRMibApplyDefaultNexthopDirect,
       "hpnicfPBRMibApplyDefaultNexthopRowStatus": hpnicfPBRMibApplyDefaultNexthopRowStatus}
)

# SNMP MIB module (INTEL-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:02 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class EthMacAddress(OctetString):
    """Custom type EthMacAddress based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 11)
)
_VlanPolicy_ObjectIdentity = ObjectIdentity
vlanPolicy = _VlanPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1)
)


class _VlanPolicyDomainName_Type(DisplayString):
    """Custom type vlanPolicyDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VlanPolicyDomainName_Type.__name__ = "DisplayString"
_VlanPolicyDomainName_Object = MibScalar
vlanPolicyDomainName = _VlanPolicyDomainName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 1),
    _VlanPolicyDomainName_Type()
)
vlanPolicyDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPolicyDomainName.setStatus("mandatory")
_VlanPolicyServerSeqNo_Type = Integer32
_VlanPolicyServerSeqNo_Object = MibScalar
vlanPolicyServerSeqNo = _VlanPolicyServerSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 2),
    _VlanPolicyServerSeqNo_Type()
)
vlanPolicyServerSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPolicyServerSeqNo.setStatus("mandatory")
_VlanPolicyClientSeqNo_Type = Integer32
_VlanPolicyClientSeqNo_Object = MibScalar
vlanPolicyClientSeqNo = _VlanPolicyClientSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 3),
    _VlanPolicyClientSeqNo_Type()
)
vlanPolicyClientSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPolicyClientSeqNo.setStatus("mandatory")


class _VlanPolicyMode_Type(Integer32):
    """Custom type vlanPolicyMode based on Integer32"""
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
        *(("fullVlan", 1),
          ("fullVlanForStack", 3),
          ("standalone", 2),
          ("standaloneForStack", 4))
    )


_VlanPolicyMode_Type.__name__ = "Integer32"
_VlanPolicyMode_Object = MibScalar
vlanPolicyMode = _VlanPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 4),
    _VlanPolicyMode_Type()
)
vlanPolicyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPolicyMode.setStatus("mandatory")
_VlanPolicyChangedStamp_Type = TimeTicks
_VlanPolicyChangedStamp_Object = MibScalar
vlanPolicyChangedStamp = _VlanPolicyChangedStamp_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 5),
    _VlanPolicyChangedStamp_Type()
)
vlanPolicyChangedStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPolicyChangedStamp.setStatus("mandatory")
_VlanPolicyNextVlanId_Type = Integer32
_VlanPolicyNextVlanId_Object = MibScalar
vlanPolicyNextVlanId = _VlanPolicyNextVlanId_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 6),
    _VlanPolicyNextVlanId_Type()
)
vlanPolicyNextVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPolicyNextVlanId.setStatus("mandatory")


class _VlanPolicyLastApiError_Type(Integer32):
    """Custom type vlanPolicyLastApiError based on Integer32"""
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
              21,
              22,
              25,
              26,
              27,
              30,
              31,
              32,
              33,
              34,
              35,
              37,
              38,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              50,
              51,
              52,
              53,
              54,
              55,
              56)
        )
    )
    namedValues = NamedValues(
        *(("commandUnknown", 12),
          ("configurationChanged", 42),
          ("currentVersionTooOld", 43),
          ("domainUnknown", 30),
          ("editTokenLostToForcedRelease", 41),
          ("editTokenNotAllocated", 3),
          ("entryAlreadyExist", 13),
          ("entryNotFound", 22),
          ("errorClearingDb", 37),
          ("errorInitializing", 35),
          ("illegalEntryId", 10),
          ("illegalIndex", 7),
          ("illegalLocalPointer", 33),
          ("illegalName", 8),
          ("illegalNvpDbPointer", 32),
          ("illegalPointer", 38),
          ("illegalPortEntry", 20),
          ("illegalVlanId", 4),
          ("ipNetViolation", 15),
          ("macVlanServerTimeOut", 40),
          ("maximumNumberOfEntriesReached", 17),
          ("moreEntriesExist", 21),
          ("multiStpChangeGlobalExist", 53),
          ("multiStpChangePortOverlapping", 55),
          ("multiStpChangeWrongVlanMode", 54),
          ("nameTooLong", 18),
          ("noDatabaseInFlash", 9),
          ("noEntriesDefined", 26),
          ("noIpNet", 19),
          ("noLocalInfoPresent", 31),
          ("noVlansDefined", 16),
          ("notAllowedWhenRunningMultiStp", 56),
          ("optionUnknown", 11),
          ("outOfMemory", 1),
          ("recursiveReferencing", 14),
          ("saveError", 25),
          ("serverIsLost", 50),
          ("tokenAllocatedForDbUpdate", 48),
          ("tokenAllocationTimeOut", 47),
          ("tokenClaimRequestAlreadyPending", 45),
          ("tokenIsAlreadyAllocated", 46),
          ("tokenReclaimFromNewServerFailed", 51),
          ("tokenTakenByOther", 2),
          ("vlanAlreadyActive", 5),
          ("vlanAlreadyDeactive", 6),
          ("vlanIdMismatch", 52),
          ("vlanNameAlreadyExist", 27),
          ("wrongDatabaseVersion", 34),
          ("wrongDomainName", 44))
    )


_VlanPolicyLastApiError_Type.__name__ = "Integer32"
_VlanPolicyLastApiError_Object = MibScalar
vlanPolicyLastApiError = _VlanPolicyLastApiError_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 7),
    _VlanPolicyLastApiError_Type()
)
vlanPolicyLastApiError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPolicyLastApiError.setStatus("mandatory")


class _VlanPolicyChangeOperation_Type(Integer32):
    """Custom type vlanPolicyChangeOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("rename", 2))
    )


_VlanPolicyChangeOperation_Type.__name__ = "Integer32"
_VlanPolicyChangeOperation_Object = MibScalar
vlanPolicyChangeOperation = _VlanPolicyChangeOperation_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 8),
    _VlanPolicyChangeOperation_Type()
)
vlanPolicyChangeOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPolicyChangeOperation.setStatus("mandatory")
_VlanPolicyVlanTable_Object = MibTable
vlanPolicyVlanTable = _VlanPolicyVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 9)
)
if mibBuilder.loadTexts:
    vlanPolicyVlanTable.setStatus("mandatory")
_PolicyVlanEntry_Object = MibTableRow
policyVlanEntry = _PolicyVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 9, 1)
)
policyVlanEntry.setIndexNames(
    (0, "INTEL-VLAN-MIB", "policyVlanId"),
)
if mibBuilder.loadTexts:
    policyVlanEntry.setStatus("mandatory")
_PolicyVlanId_Type = Integer32
_PolicyVlanId_Object = MibTableColumn
policyVlanId = _PolicyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 9, 1, 1),
    _PolicyVlanId_Type()
)
policyVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyVlanId.setStatus("mandatory")


class _PolicyVlanName_Type(DisplayString):
    """Custom type policyVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PolicyVlanName_Type.__name__ = "DisplayString"
_PolicyVlanName_Object = MibTableColumn
policyVlanName = _PolicyVlanName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 9, 1, 2),
    _PolicyVlanName_Type()
)
policyVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyVlanName.setStatus("mandatory")


class _PolicyVlanCreateObj_Type(OctetString):
    """Custom type policyVlanCreateObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PolicyVlanCreateObj_Type.__name__ = "OctetString"
_PolicyVlanCreateObj_Object = MibTableColumn
policyVlanCreateObj = _PolicyVlanCreateObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 9, 1, 3),
    _PolicyVlanCreateObj_Type()
)
policyVlanCreateObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyVlanCreateObj.setStatus("mandatory")


class _PolicyVlanDeleteObj_Type(Integer32):
    """Custom type policyVlanDeleteObj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_PolicyVlanDeleteObj_Type.__name__ = "Integer32"
_PolicyVlanDeleteObj_Object = MibTableColumn
policyVlanDeleteObj = _PolicyVlanDeleteObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 9, 1, 4),
    _PolicyVlanDeleteObj_Type()
)
policyVlanDeleteObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyVlanDeleteObj.setStatus("mandatory")
_VlanPolicyMacRuleTable_Object = MibTable
vlanPolicyMacRuleTable = _VlanPolicyMacRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 10)
)
if mibBuilder.loadTexts:
    vlanPolicyMacRuleTable.setStatus("mandatory")
_PolicyMacRuleEntry_Object = MibTableRow
policyMacRuleEntry = _PolicyMacRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 10, 1)
)
policyMacRuleEntry.setIndexNames(
    (0, "INTEL-VLAN-MIB", "policyMacRuleVlanId"),
    (0, "INTEL-VLAN-MIB", "policyMacRuleAddress"),
)
if mibBuilder.loadTexts:
    policyMacRuleEntry.setStatus("mandatory")
_PolicyMacRuleVlanId_Type = Integer32
_PolicyMacRuleVlanId_Object = MibTableColumn
policyMacRuleVlanId = _PolicyMacRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 10, 1, 1),
    _PolicyMacRuleVlanId_Type()
)
policyMacRuleVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyMacRuleVlanId.setStatus("mandatory")


class _PolicyMacRuleAddress_Type(EthMacAddress):
    """Custom type policyMacRuleAddress based on EthMacAddress"""
    subtypeSpec = EthMacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PolicyMacRuleAddress_Type.__name__ = "EthMacAddress"
_PolicyMacRuleAddress_Object = MibTableColumn
policyMacRuleAddress = _PolicyMacRuleAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 10, 1, 2),
    _PolicyMacRuleAddress_Type()
)
policyMacRuleAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyMacRuleAddress.setStatus("mandatory")
_PolicyMacRuleCreateObj_Type = OctetString
_PolicyMacRuleCreateObj_Object = MibTableColumn
policyMacRuleCreateObj = _PolicyMacRuleCreateObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 10, 1, 3),
    _PolicyMacRuleCreateObj_Type()
)
policyMacRuleCreateObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyMacRuleCreateObj.setStatus("mandatory")


class _PolicyMacRuleDeleteObj_Type(Integer32):
    """Custom type policyMacRuleDeleteObj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_PolicyMacRuleDeleteObj_Type.__name__ = "Integer32"
_PolicyMacRuleDeleteObj_Object = MibTableColumn
policyMacRuleDeleteObj = _PolicyMacRuleDeleteObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 10, 1, 4),
    _PolicyMacRuleDeleteObj_Type()
)
policyMacRuleDeleteObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyMacRuleDeleteObj.setStatus("mandatory")
_VlanPolicyIslMacRuleTable_Object = MibTable
vlanPolicyIslMacRuleTable = _VlanPolicyIslMacRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 11)
)
if mibBuilder.loadTexts:
    vlanPolicyIslMacRuleTable.setStatus("mandatory")
_PolicyIslMacRuleEntry_Object = MibTableRow
policyIslMacRuleEntry = _PolicyIslMacRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 11, 1)
)
policyIslMacRuleEntry.setIndexNames(
    (0, "INTEL-VLAN-MIB", "policyIslMacRuleVlanId"),
    (0, "INTEL-VLAN-MIB", "policyIslMacRuleAddress"),
)
if mibBuilder.loadTexts:
    policyIslMacRuleEntry.setStatus("mandatory")
_PolicyIslMacRuleVlanId_Type = Integer32
_PolicyIslMacRuleVlanId_Object = MibTableColumn
policyIslMacRuleVlanId = _PolicyIslMacRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 11, 1, 1),
    _PolicyIslMacRuleVlanId_Type()
)
policyIslMacRuleVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyIslMacRuleVlanId.setStatus("mandatory")


class _PolicyIslMacRuleAddress_Type(EthMacAddress):
    """Custom type policyIslMacRuleAddress based on EthMacAddress"""
    subtypeSpec = EthMacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PolicyIslMacRuleAddress_Type.__name__ = "EthMacAddress"
_PolicyIslMacRuleAddress_Object = MibTableColumn
policyIslMacRuleAddress = _PolicyIslMacRuleAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 11, 1, 2),
    _PolicyIslMacRuleAddress_Type()
)
policyIslMacRuleAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyIslMacRuleAddress.setStatus("mandatory")
_PolicyIslMacRuleCreateObj_Type = OctetString
_PolicyIslMacRuleCreateObj_Object = MibTableColumn
policyIslMacRuleCreateObj = _PolicyIslMacRuleCreateObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 11, 1, 3),
    _PolicyIslMacRuleCreateObj_Type()
)
policyIslMacRuleCreateObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyIslMacRuleCreateObj.setStatus("mandatory")


class _PolicyIslMacRuleDeleteObj_Type(Integer32):
    """Custom type policyIslMacRuleDeleteObj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_PolicyIslMacRuleDeleteObj_Type.__name__ = "Integer32"
_PolicyIslMacRuleDeleteObj_Object = MibTableColumn
policyIslMacRuleDeleteObj = _PolicyIslMacRuleDeleteObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 11, 1, 4),
    _PolicyIslMacRuleDeleteObj_Type()
)
policyIslMacRuleDeleteObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyIslMacRuleDeleteObj.setStatus("mandatory")
_VlanPolicyIpRuleTable_Object = MibTable
vlanPolicyIpRuleTable = _VlanPolicyIpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 12)
)
if mibBuilder.loadTexts:
    vlanPolicyIpRuleTable.setStatus("mandatory")
_PolicyIpRuleEntry_Object = MibTableRow
policyIpRuleEntry = _PolicyIpRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 12, 1)
)
policyIpRuleEntry.setIndexNames(
    (0, "INTEL-VLAN-MIB", "policyIpRuleVlanId"),
    (0, "INTEL-VLAN-MIB", "policyIpRuleAddress"),
)
if mibBuilder.loadTexts:
    policyIpRuleEntry.setStatus("mandatory")
_PolicyIpRuleVlanId_Type = Integer32
_PolicyIpRuleVlanId_Object = MibTableColumn
policyIpRuleVlanId = _PolicyIpRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 12, 1, 1),
    _PolicyIpRuleVlanId_Type()
)
policyIpRuleVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyIpRuleVlanId.setStatus("mandatory")
_PolicyIpRuleAddress_Type = IpAddress
_PolicyIpRuleAddress_Object = MibTableColumn
policyIpRuleAddress = _PolicyIpRuleAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 12, 1, 2),
    _PolicyIpRuleAddress_Type()
)
policyIpRuleAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyIpRuleAddress.setStatus("mandatory")
_PolicyIpRuleCreateObj_Type = OctetString
_PolicyIpRuleCreateObj_Object = MibTableColumn
policyIpRuleCreateObj = _PolicyIpRuleCreateObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 12, 1, 3),
    _PolicyIpRuleCreateObj_Type()
)
policyIpRuleCreateObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyIpRuleCreateObj.setStatus("mandatory")


class _PolicyIpRuleDeleteObj_Type(Integer32):
    """Custom type policyIpRuleDeleteObj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_PolicyIpRuleDeleteObj_Type.__name__ = "Integer32"
_PolicyIpRuleDeleteObj_Object = MibTableColumn
policyIpRuleDeleteObj = _PolicyIpRuleDeleteObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 12, 1, 4),
    _PolicyIpRuleDeleteObj_Type()
)
policyIpRuleDeleteObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyIpRuleDeleteObj.setStatus("mandatory")
_VlanPolicyIpNetRuleTable_Object = MibTable
vlanPolicyIpNetRuleTable = _VlanPolicyIpNetRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 13)
)
if mibBuilder.loadTexts:
    vlanPolicyIpNetRuleTable.setStatus("mandatory")
_PolicyIpNetRuleEntry_Object = MibTableRow
policyIpNetRuleEntry = _PolicyIpNetRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 13, 1)
)
policyIpNetRuleEntry.setIndexNames(
    (0, "INTEL-VLAN-MIB", "policyIpNetRuleVlanId"),
    (0, "INTEL-VLAN-MIB", "policyIpNetRuleAddress"),
)
if mibBuilder.loadTexts:
    policyIpNetRuleEntry.setStatus("mandatory")
_PolicyIpNetRuleVlanId_Type = Integer32
_PolicyIpNetRuleVlanId_Object = MibTableColumn
policyIpNetRuleVlanId = _PolicyIpNetRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 13, 1, 1),
    _PolicyIpNetRuleVlanId_Type()
)
policyIpNetRuleVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyIpNetRuleVlanId.setStatus("mandatory")
_PolicyIpNetRuleAddress_Type = IpAddress
_PolicyIpNetRuleAddress_Object = MibTableColumn
policyIpNetRuleAddress = _PolicyIpNetRuleAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 13, 1, 2),
    _PolicyIpNetRuleAddress_Type()
)
policyIpNetRuleAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyIpNetRuleAddress.setStatus("mandatory")
_PolicyIpNetRuleMask_Type = IpAddress
_PolicyIpNetRuleMask_Object = MibTableColumn
policyIpNetRuleMask = _PolicyIpNetRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 13, 1, 3),
    _PolicyIpNetRuleMask_Type()
)
policyIpNetRuleMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyIpNetRuleMask.setStatus("mandatory")


class _PolicyIpNetRuleCreateObj_Type(OctetString):
    """Custom type policyIpNetRuleCreateObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_PolicyIpNetRuleCreateObj_Type.__name__ = "OctetString"
_PolicyIpNetRuleCreateObj_Object = MibTableColumn
policyIpNetRuleCreateObj = _PolicyIpNetRuleCreateObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 13, 1, 4),
    _PolicyIpNetRuleCreateObj_Type()
)
policyIpNetRuleCreateObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyIpNetRuleCreateObj.setStatus("mandatory")


class _PolicyIpNetRuleDeleteObj_Type(Integer32):
    """Custom type policyIpNetRuleDeleteObj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_PolicyIpNetRuleDeleteObj_Type.__name__ = "Integer32"
_PolicyIpNetRuleDeleteObj_Object = MibTableColumn
policyIpNetRuleDeleteObj = _PolicyIpNetRuleDeleteObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 13, 1, 5),
    _PolicyIpNetRuleDeleteObj_Type()
)
policyIpNetRuleDeleteObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyIpNetRuleDeleteObj.setStatus("mandatory")
_VlanPolicyPortRuleTable_Object = MibTable
vlanPolicyPortRuleTable = _VlanPolicyPortRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 14)
)
if mibBuilder.loadTexts:
    vlanPolicyPortRuleTable.setStatus("mandatory")
_PolicyPortRuleEntry_Object = MibTableRow
policyPortRuleEntry = _PolicyPortRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 14, 1)
)
policyPortRuleEntry.setIndexNames(
    (0, "INTEL-VLAN-MIB", "policyPortRuleVlanId"),
    (0, "INTEL-VLAN-MIB", "policyPortRuleNumber"),
)
if mibBuilder.loadTexts:
    policyPortRuleEntry.setStatus("mandatory")
_PolicyPortRuleVlanId_Type = Integer32
_PolicyPortRuleVlanId_Object = MibTableColumn
policyPortRuleVlanId = _PolicyPortRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 14, 1, 1),
    _PolicyPortRuleVlanId_Type()
)
policyPortRuleVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPortRuleVlanId.setStatus("mandatory")
_PolicyPortRuleNumber_Type = Integer32
_PolicyPortRuleNumber_Object = MibTableColumn
policyPortRuleNumber = _PolicyPortRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 14, 1, 2),
    _PolicyPortRuleNumber_Type()
)
policyPortRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPortRuleNumber.setStatus("mandatory")
_PolicyPortRuleCreateObj_Type = OctetString
_PolicyPortRuleCreateObj_Object = MibTableColumn
policyPortRuleCreateObj = _PolicyPortRuleCreateObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 14, 1, 3),
    _PolicyPortRuleCreateObj_Type()
)
policyPortRuleCreateObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyPortRuleCreateObj.setStatus("mandatory")


class _PolicyPortRuleDeleteObj_Type(Integer32):
    """Custom type policyPortRuleDeleteObj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_PolicyPortRuleDeleteObj_Type.__name__ = "Integer32"
_PolicyPortRuleDeleteObj_Object = MibTableColumn
policyPortRuleDeleteObj = _PolicyPortRuleDeleteObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 14, 1, 4),
    _PolicyPortRuleDeleteObj_Type()
)
policyPortRuleDeleteObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyPortRuleDeleteObj.setStatus("mandatory")
_VlanPolicyPortSettingsTable_Object = MibTable
vlanPolicyPortSettingsTable = _VlanPolicyPortSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 15)
)
if mibBuilder.loadTexts:
    vlanPolicyPortSettingsTable.setStatus("mandatory")
_PolicyPortSettingsEntry_Object = MibTableRow
policyPortSettingsEntry = _PolicyPortSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 15, 1)
)
policyPortSettingsEntry.setIndexNames(
    (0, "INTEL-VLAN-MIB", "policyPortSettingsPortNumber"),
)
if mibBuilder.loadTexts:
    policyPortSettingsEntry.setStatus("mandatory")
_PolicyPortSettingsPortNumber_Type = Integer32
_PolicyPortSettingsPortNumber_Object = MibTableColumn
policyPortSettingsPortNumber = _PolicyPortSettingsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 15, 1, 1),
    _PolicyPortSettingsPortNumber_Type()
)
policyPortSettingsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPortSettingsPortNumber.setStatus("mandatory")


class _PolicyPortSettingsIpLearning_Type(Integer32):
    """Custom type policyPortSettingsIpLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipLearningDisabled", 1),
          ("ipLearningEnabled", 2))
    )


_PolicyPortSettingsIpLearning_Type.__name__ = "Integer32"
_PolicyPortSettingsIpLearning_Object = MibTableColumn
policyPortSettingsIpLearning = _PolicyPortSettingsIpLearning_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 15, 1, 2),
    _PolicyPortSettingsIpLearning_Type()
)
policyPortSettingsIpLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyPortSettingsIpLearning.setStatus("mandatory")


class _VlanPolicyAllPortSettingsIpLearning_Type(Integer32):
    """Custom type vlanPolicyAllPortSettingsIpLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipLearningDisabled", 1),
          ("ipLearningEnabled", 2),
          ("ipLearningMixed", 3))
    )


_VlanPolicyAllPortSettingsIpLearning_Type.__name__ = "Integer32"
_VlanPolicyAllPortSettingsIpLearning_Object = MibScalar
vlanPolicyAllPortSettingsIpLearning = _VlanPolicyAllPortSettingsIpLearning_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 16),
    _VlanPolicyAllPortSettingsIpLearning_Type()
)
vlanPolicyAllPortSettingsIpLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPolicyAllPortSettingsIpLearning.setStatus("mandatory")
_VlanPolicyAssignManagementVlan_Type = Integer32
_VlanPolicyAssignManagementVlan_Object = MibScalar
vlanPolicyAssignManagementVlan = _VlanPolicyAssignManagementVlan_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 17),
    _VlanPolicyAssignManagementVlan_Type()
)
vlanPolicyAssignManagementVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPolicyAssignManagementVlan.setStatus("mandatory")


class _VlanPolicyConfigConfState_Type(Integer32):
    """Custom type vlanPolicyConfigConfState based on Integer32"""
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
        *(("confirm", 5),
          ("confirmedNewConf", 4),
          ("notReady", 1),
          ("ready", 2),
          ("revertedToOldConf", 3))
    )


_VlanPolicyConfigConfState_Type.__name__ = "Integer32"
_VlanPolicyConfigConfState_Object = MibScalar
vlanPolicyConfigConfState = _VlanPolicyConfigConfState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 18),
    _VlanPolicyConfigConfState_Type()
)
vlanPolicyConfigConfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPolicyConfigConfState.setStatus("mandatory")
_VlanPolicyConfigConfTimerValue_Type = Integer32
_VlanPolicyConfigConfTimerValue_Object = MibScalar
vlanPolicyConfigConfTimerValue = _VlanPolicyConfigConfTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 19),
    _VlanPolicyConfigConfTimerValue_Type()
)
vlanPolicyConfigConfTimerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPolicyConfigConfTimerValue.setStatus("mandatory")
_VlanPolicySupportedVlanModes_Type = Integer32
_VlanPolicySupportedVlanModes_Object = MibScalar
vlanPolicySupportedVlanModes = _VlanPolicySupportedVlanModes_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 20),
    _VlanPolicySupportedVlanModes_Type()
)
vlanPolicySupportedVlanModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPolicySupportedVlanModes.setStatus("mandatory")
_VlanPolicyRevert2Default_Type = Integer32
_VlanPolicyRevert2Default_Object = MibScalar
vlanPolicyRevert2Default = _VlanPolicyRevert2Default_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 21),
    _VlanPolicyRevert2Default_Type()
)
vlanPolicyRevert2Default.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPolicyRevert2Default.setStatus("mandatory")
_VlanPolicyMacVlanServerPriority_Type = Integer32
_VlanPolicyMacVlanServerPriority_Object = MibScalar
vlanPolicyMacVlanServerPriority = _VlanPolicyMacVlanServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 22),
    _VlanPolicyMacVlanServerPriority_Type()
)
vlanPolicyMacVlanServerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPolicyMacVlanServerPriority.setStatus("mandatory")


class _VlanPolicyAutoMoveMgtIpLink_Type(Integer32):
    """Custom type vlanPolicyAutoMoveMgtIpLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoMoveMgtDisabled", 2),
          ("autoMoveMgtEnabled", 1))
    )


_VlanPolicyAutoMoveMgtIpLink_Type.__name__ = "Integer32"
_VlanPolicyAutoMoveMgtIpLink_Object = MibScalar
vlanPolicyAutoMoveMgtIpLink = _VlanPolicyAutoMoveMgtIpLink_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 23),
    _VlanPolicyAutoMoveMgtIpLink_Type()
)
vlanPolicyAutoMoveMgtIpLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPolicyAutoMoveMgtIpLink.setStatus("mandatory")
_VlanPolicyStackPortRuleTable_Object = MibTable
vlanPolicyStackPortRuleTable = _VlanPolicyStackPortRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 24)
)
if mibBuilder.loadTexts:
    vlanPolicyStackPortRuleTable.setStatus("mandatory")
_PolicyStackPortRuleEntry_Object = MibTableRow
policyStackPortRuleEntry = _PolicyStackPortRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 24, 1)
)
policyStackPortRuleEntry.setIndexNames(
    (0, "INTEL-VLAN-MIB", "policyStackPortRuleVlanId"),
    (0, "INTEL-VLAN-MIB", "policyStackPortRuleSwitchMac"),
    (0, "INTEL-VLAN-MIB", "policyStackPortRuleNumber"),
)
if mibBuilder.loadTexts:
    policyStackPortRuleEntry.setStatus("mandatory")
_PolicyStackPortRuleVlanId_Type = Integer32
_PolicyStackPortRuleVlanId_Object = MibTableColumn
policyStackPortRuleVlanId = _PolicyStackPortRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 24, 1, 1),
    _PolicyStackPortRuleVlanId_Type()
)
policyStackPortRuleVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyStackPortRuleVlanId.setStatus("mandatory")


class _PolicyStackPortRuleSwitchMac_Type(EthMacAddress):
    """Custom type policyStackPortRuleSwitchMac based on EthMacAddress"""
    subtypeSpec = EthMacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PolicyStackPortRuleSwitchMac_Type.__name__ = "EthMacAddress"
_PolicyStackPortRuleSwitchMac_Object = MibTableColumn
policyStackPortRuleSwitchMac = _PolicyStackPortRuleSwitchMac_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 24, 1, 2),
    _PolicyStackPortRuleSwitchMac_Type()
)
policyStackPortRuleSwitchMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyStackPortRuleSwitchMac.setStatus("mandatory")
_PolicyStackPortRuleNumber_Type = Integer32
_PolicyStackPortRuleNumber_Object = MibTableColumn
policyStackPortRuleNumber = _PolicyStackPortRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 24, 1, 3),
    _PolicyStackPortRuleNumber_Type()
)
policyStackPortRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyStackPortRuleNumber.setStatus("mandatory")
_PolicyStackPortRuleCreateObj_Type = OctetString
_PolicyStackPortRuleCreateObj_Object = MibTableColumn
policyStackPortRuleCreateObj = _PolicyStackPortRuleCreateObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 24, 1, 4),
    _PolicyStackPortRuleCreateObj_Type()
)
policyStackPortRuleCreateObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyStackPortRuleCreateObj.setStatus("mandatory")


class _PolicyStackPortRuleDeleteObj_Type(Integer32):
    """Custom type policyStackPortRuleDeleteObj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_PolicyStackPortRuleDeleteObj_Type.__name__ = "Integer32"
_PolicyStackPortRuleDeleteObj_Object = MibTableColumn
policyStackPortRuleDeleteObj = _PolicyStackPortRuleDeleteObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 24, 1, 5),
    _PolicyStackPortRuleDeleteObj_Type()
)
policyStackPortRuleDeleteObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyStackPortRuleDeleteObj.setStatus("mandatory")


class _VlanPolicyUseMultiSTP_Type(Integer32):
    """Custom type vlanPolicyUseMultiSTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_VlanPolicyUseMultiSTP_Type.__name__ = "Integer32"
_VlanPolicyUseMultiSTP_Object = MibScalar
vlanPolicyUseMultiSTP = _VlanPolicyUseMultiSTP_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 25),
    _VlanPolicyUseMultiSTP_Type()
)
vlanPolicyUseMultiSTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPolicyUseMultiSTP.setStatus("mandatory")


class _VlanPolicyFwdLearnPckts_Type(Integer32):
    """Custom type vlanPolicyFwdLearnPckts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_VlanPolicyFwdLearnPckts_Type.__name__ = "Integer32"
_VlanPolicyFwdLearnPckts_Object = MibScalar
vlanPolicyFwdLearnPckts = _VlanPolicyFwdLearnPckts_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 1, 26),
    _VlanPolicyFwdLearnPckts_Type()
)
vlanPolicyFwdLearnPckts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPolicyFwdLearnPckts.setStatus("mandatory")
_VlanLearned_ObjectIdentity = ObjectIdentity
vlanLearned = _VlanLearned_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2)
)
_VlanLearnedVersion_Type = Integer32
_VlanLearnedVersion_Object = MibScalar
vlanLearnedVersion = _VlanLearnedVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 1),
    _VlanLearnedVersion_Type()
)
vlanLearnedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanLearnedVersion.setStatus("mandatory")


class _VlanLearnedServerState_Type(Integer32):
    """Custom type vlanLearnedServerState based on Integer32"""
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
        *(("active", 4),
          ("initActive", 1),
          ("initPassive", 2),
          ("passive", 3))
    )


_VlanLearnedServerState_Type.__name__ = "Integer32"
_VlanLearnedServerState_Object = MibScalar
vlanLearnedServerState = _VlanLearnedServerState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 2),
    _VlanLearnedServerState_Type()
)
vlanLearnedServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanLearnedServerState.setStatus("mandatory")


class _VlanLearnedServerPriority_Type(Integer32):
    """Custom type vlanLearnedServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlanLearnedServerPriority_Type.__name__ = "Integer32"
_VlanLearnedServerPriority_Object = MibScalar
vlanLearnedServerPriority = _VlanLearnedServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 3),
    _VlanLearnedServerPriority_Type()
)
vlanLearnedServerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanLearnedServerPriority.setStatus("mandatory")
_VlanLearnedServerIPAddress_Type = IpAddress
_VlanLearnedServerIPAddress_Object = MibScalar
vlanLearnedServerIPAddress = _VlanLearnedServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 4),
    _VlanLearnedServerIPAddress_Type()
)
vlanLearnedServerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanLearnedServerIPAddress.setStatus("mandatory")


class _VlanLearnedServerMACAddress_Type(EthMacAddress):
    """Custom type vlanLearnedServerMACAddress based on EthMacAddress"""
    subtypeSpec = EthMacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_VlanLearnedServerMACAddress_Type.__name__ = "EthMacAddress"
_VlanLearnedServerMACAddress_Object = MibScalar
vlanLearnedServerMACAddress = _VlanLearnedServerMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 5),
    _VlanLearnedServerMACAddress_Type()
)
vlanLearnedServerMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanLearnedServerMACAddress.setStatus("mandatory")
_VlanLearnedServerPortNo_Type = Integer32
_VlanLearnedServerPortNo_Object = MibScalar
vlanLearnedServerPortNo = _VlanLearnedServerPortNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 6),
    _VlanLearnedServerPortNo_Type()
)
vlanLearnedServerPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanLearnedServerPortNo.setStatus("mandatory")


class _VlanLearnedServerNameChangeTimer_Type(Integer32):
    """Custom type vlanLearnedServerNameChangeTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlanLearnedServerNameChangeTimer_Type.__name__ = "Integer32"
_VlanLearnedServerNameChangeTimer_Object = MibScalar
vlanLearnedServerNameChangeTimer = _VlanLearnedServerNameChangeTimer_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 7),
    _VlanLearnedServerNameChangeTimer_Type()
)
vlanLearnedServerNameChangeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanLearnedServerNameChangeTimer.setStatus("mandatory")


class _VlanLearnedServerExpiryTimer_Type(Integer32):
    """Custom type vlanLearnedServerExpiryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VlanLearnedServerExpiryTimer_Type.__name__ = "Integer32"
_VlanLearnedServerExpiryTimer_Object = MibScalar
vlanLearnedServerExpiryTimer = _VlanLearnedServerExpiryTimer_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 8),
    _VlanLearnedServerExpiryTimer_Type()
)
vlanLearnedServerExpiryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanLearnedServerExpiryTimer.setStatus("mandatory")
_VlanLearnedMacTable_Object = MibTable
vlanLearnedMacTable = _VlanLearnedMacTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 9)
)
if mibBuilder.loadTexts:
    vlanLearnedMacTable.setStatus("mandatory")
_LearnedMacEntry_Object = MibTableRow
learnedMacEntry = _LearnedMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 9, 1)
)
learnedMacEntry.setIndexNames(
    (0, "INTEL-VLAN-MIB", "learnedMacAddress"),
)
if mibBuilder.loadTexts:
    learnedMacEntry.setStatus("mandatory")


class _LearnedMacAddress_Type(EthMacAddress):
    """Custom type learnedMacAddress based on EthMacAddress"""
    subtypeSpec = EthMacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LearnedMacAddress_Type.__name__ = "EthMacAddress"
_LearnedMacAddress_Object = MibTableColumn
learnedMacAddress = _LearnedMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 9, 1, 1),
    _LearnedMacAddress_Type()
)
learnedMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learnedMacAddress.setStatus("mandatory")


class _LearnedMacType_Type(OctetString):
    """Custom type learnedMacType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LearnedMacType_Type.__name__ = "OctetString"
_LearnedMacType_Object = MibTableColumn
learnedMacType = _LearnedMacType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 9, 1, 2),
    _LearnedMacType_Type()
)
learnedMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learnedMacType.setStatus("mandatory")
_LearnedMacPortNo_Type = Integer32
_LearnedMacPortNo_Object = MibTableColumn
learnedMacPortNo = _LearnedMacPortNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 9, 1, 3),
    _LearnedMacPortNo_Type()
)
learnedMacPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learnedMacPortNo.setStatus("mandatory")
_LearnedMacIpAddress_Type = IpAddress
_LearnedMacIpAddress_Object = MibTableColumn
learnedMacIpAddress = _LearnedMacIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 9, 1, 4),
    _LearnedMacIpAddress_Type()
)
learnedMacIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learnedMacIpAddress.setStatus("mandatory")
_VlanLearnedMacVlanTable_Object = MibTable
vlanLearnedMacVlanTable = _VlanLearnedMacVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 10)
)
if mibBuilder.loadTexts:
    vlanLearnedMacVlanTable.setStatus("mandatory")
_LearnedMacVlanEntry_Object = MibTableRow
learnedMacVlanEntry = _LearnedMacVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 10, 1)
)
learnedMacVlanEntry.setIndexNames(
    (0, "INTEL-VLAN-MIB", "learnedMacVlanMac"),
    (0, "INTEL-VLAN-MIB", "learnedMacVlanIndex"),
)
if mibBuilder.loadTexts:
    learnedMacVlanEntry.setStatus("mandatory")


class _LearnedMacVlanMac_Type(EthMacAddress):
    """Custom type learnedMacVlanMac based on EthMacAddress"""
    subtypeSpec = EthMacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LearnedMacVlanMac_Type.__name__ = "EthMacAddress"
_LearnedMacVlanMac_Object = MibTableColumn
learnedMacVlanMac = _LearnedMacVlanMac_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 10, 1, 1),
    _LearnedMacVlanMac_Type()
)
learnedMacVlanMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learnedMacVlanMac.setStatus("mandatory")
_LearnedMacVlanIndex_Type = Integer32
_LearnedMacVlanIndex_Object = MibTableColumn
learnedMacVlanIndex = _LearnedMacVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 10, 1, 2),
    _LearnedMacVlanIndex_Type()
)
learnedMacVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learnedMacVlanIndex.setStatus("mandatory")


class _LearnedMacVlanName_Type(DisplayString):
    """Custom type learnedMacVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LearnedMacVlanName_Type.__name__ = "DisplayString"
_LearnedMacVlanName_Object = MibTableColumn
learnedMacVlanName = _LearnedMacVlanName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 10, 1, 3),
    _LearnedMacVlanName_Type()
)
learnedMacVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learnedMacVlanName.setStatus("mandatory")
_VlanLearnedVlanPortTable_Object = MibTable
vlanLearnedVlanPortTable = _VlanLearnedVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 11)
)
if mibBuilder.loadTexts:
    vlanLearnedVlanPortTable.setStatus("mandatory")
_LearnedVlanPortEntry_Object = MibTableRow
learnedVlanPortEntry = _LearnedVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 11, 1)
)
learnedVlanPortEntry.setIndexNames(
    (0, "INTEL-VLAN-MIB", "learnedVlanPortNo"),
    (0, "INTEL-VLAN-MIB", "learnedVlanPortVlanIndex"),
)
if mibBuilder.loadTexts:
    learnedVlanPortEntry.setStatus("mandatory")
_LearnedVlanPortNo_Type = Integer32
_LearnedVlanPortNo_Object = MibTableColumn
learnedVlanPortNo = _LearnedVlanPortNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 11, 1, 1),
    _LearnedVlanPortNo_Type()
)
learnedVlanPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learnedVlanPortNo.setStatus("mandatory")
_LearnedVlanPortVlanIndex_Type = Integer32
_LearnedVlanPortVlanIndex_Object = MibTableColumn
learnedVlanPortVlanIndex = _LearnedVlanPortVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 11, 1, 2),
    _LearnedVlanPortVlanIndex_Type()
)
learnedVlanPortVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learnedVlanPortVlanIndex.setStatus("mandatory")


class _LearnedVlanPortVlanName_Type(DisplayString):
    """Custom type learnedVlanPortVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LearnedVlanPortVlanName_Type.__name__ = "DisplayString"
_LearnedVlanPortVlanName_Object = MibTableColumn
learnedVlanPortVlanName = _LearnedVlanPortVlanName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 11, 1, 3),
    _LearnedVlanPortVlanName_Type()
)
learnedVlanPortVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learnedVlanPortVlanName.setStatus("mandatory")
_VlanLearnedVlanIdTable_Object = MibTable
vlanLearnedVlanIdTable = _VlanLearnedVlanIdTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 12)
)
if mibBuilder.loadTexts:
    vlanLearnedVlanIdTable.setStatus("mandatory")
_LearnedVlanIdEntry_Object = MibTableRow
learnedVlanIdEntry = _LearnedVlanIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 12, 1)
)
learnedVlanIdEntry.setIndexNames(
    (0, "INTEL-VLAN-MIB", "learnedVlanId"),
)
if mibBuilder.loadTexts:
    learnedVlanIdEntry.setStatus("mandatory")
_LearnedVlanId_Type = Integer32
_LearnedVlanId_Object = MibTableColumn
learnedVlanId = _LearnedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 12, 1, 1),
    _LearnedVlanId_Type()
)
learnedVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learnedVlanId.setStatus("mandatory")


class _LearnedVlanIdVlanName_Type(DisplayString):
    """Custom type learnedVlanIdVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LearnedVlanIdVlanName_Type.__name__ = "DisplayString"
_LearnedVlanIdVlanName_Object = MibTableColumn
learnedVlanIdVlanName = _LearnedVlanIdVlanName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 12, 1, 2),
    _LearnedVlanIdVlanName_Type()
)
learnedVlanIdVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learnedVlanIdVlanName.setStatus("mandatory")


class _VlanLearnedSnmpMgtVlanIds_Type(OctetString):
    """Custom type vlanLearnedSnmpMgtVlanIds based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VlanLearnedSnmpMgtVlanIds_Type.__name__ = "OctetString"
_VlanLearnedSnmpMgtVlanIds_Object = MibScalar
vlanLearnedSnmpMgtVlanIds = _VlanLearnedSnmpMgtVlanIds_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 13),
    _VlanLearnedSnmpMgtVlanIds_Type()
)
vlanLearnedSnmpMgtVlanIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanLearnedSnmpMgtVlanIds.setStatus("mandatory")
_VlanLearnedMacVlanFlush_Type = Integer32
_VlanLearnedMacVlanFlush_Object = MibScalar
vlanLearnedMacVlanFlush = _VlanLearnedMacVlanFlush_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 2, 14),
    _VlanLearnedMacVlanFlush_Type()
)
vlanLearnedMacVlanFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanLearnedMacVlanFlush.setStatus("mandatory")
_VlanIsl_ObjectIdentity = ObjectIdentity
vlanIsl = _VlanIsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 3)
)
_IslTable_Object = MibTable
islTable = _IslTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 3, 1)
)
if mibBuilder.loadTexts:
    islTable.setStatus("mandatory")
_IslEntry_Object = MibTableRow
islEntry = _IslEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 3, 1, 1)
)
islEntry.setIndexNames(
    (0, "INTEL-VLAN-MIB", "islIfIndex"),
    (0, "INTEL-VLAN-MIB", "islMacAddress"),
)
if mibBuilder.loadTexts:
    islEntry.setStatus("mandatory")
_IslIfIndex_Type = Integer32
_IslIfIndex_Object = MibTableColumn
islIfIndex = _IslIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 3, 1, 1, 1),
    _IslIfIndex_Type()
)
islIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    islIfIndex.setStatus("mandatory")


class _IslMacAddress_Type(EthMacAddress):
    """Custom type islMacAddress based on EthMacAddress"""
    subtypeSpec = EthMacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IslMacAddress_Type.__name__ = "EthMacAddress"
_IslMacAddress_Object = MibTableColumn
islMacAddress = _IslMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 3, 1, 1, 2),
    _IslMacAddress_Type()
)
islMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    islMacAddress.setStatus("mandatory")
_IslIpAddress_Type = IpAddress
_IslIpAddress_Object = MibTableColumn
islIpAddress = _IslIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 3, 1, 1, 3),
    _IslIpAddress_Type()
)
islIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    islIpAddress.setStatus("mandatory")
_VlanEditToken_ObjectIdentity = ObjectIdentity
vlanEditToken = _VlanEditToken_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 4)
)


class _EditTokenOwnerMacAddress_Type(EthMacAddress):
    """Custom type editTokenOwnerMacAddress based on EthMacAddress"""
    subtypeSpec = EthMacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EditTokenOwnerMacAddress_Type.__name__ = "EthMacAddress"
_EditTokenOwnerMacAddress_Object = MibScalar
editTokenOwnerMacAddress = _EditTokenOwnerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 4, 1),
    _EditTokenOwnerMacAddress_Type()
)
editTokenOwnerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    editTokenOwnerMacAddress.setStatus("mandatory")
_EditTokenOwnerIpAddress_Type = IpAddress
_EditTokenOwnerIpAddress_Object = MibScalar
editTokenOwnerIpAddress = _EditTokenOwnerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 4, 2),
    _EditTokenOwnerIpAddress_Type()
)
editTokenOwnerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    editTokenOwnerIpAddress.setStatus("mandatory")


class _EditTokenOwnerSysName_Type(DisplayString):
    """Custom type editTokenOwnerSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EditTokenOwnerSysName_Type.__name__ = "DisplayString"
_EditTokenOwnerSysName_Object = MibScalar
editTokenOwnerSysName = _EditTokenOwnerSysName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 4, 3),
    _EditTokenOwnerSysName_Type()
)
editTokenOwnerSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    editTokenOwnerSysName.setStatus("mandatory")


class _EditTokenOwnerApplication_Type(Integer32):
    """Custom type editTokenOwnerApplication based on Integer32"""
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
        *(("externalTftpGet", 5),
          ("externalTftpPut", 6),
          ("loadFromFlash", 7),
          ("localManagement", 1),
          ("nvpdbTftp", 3),
          ("serverUpdate", 4),
          ("snmp", 2))
    )


_EditTokenOwnerApplication_Type.__name__ = "Integer32"
_EditTokenOwnerApplication_Object = MibScalar
editTokenOwnerApplication = _EditTokenOwnerApplication_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 4, 4),
    _EditTokenOwnerApplication_Type()
)
editTokenOwnerApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    editTokenOwnerApplication.setStatus("mandatory")
_EditTokenOwnerSnmpIpAddress_Type = IpAddress
_EditTokenOwnerSnmpIpAddress_Object = MibScalar
editTokenOwnerSnmpIpAddress = _EditTokenOwnerSnmpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 4, 5),
    _EditTokenOwnerSnmpIpAddress_Type()
)
editTokenOwnerSnmpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    editTokenOwnerSnmpIpAddress.setStatus("mandatory")


class _EditTokenClaimReq_Type(OctetString):
    """Custom type editTokenClaimReq based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EditTokenClaimReq_Type.__name__ = "OctetString"
_EditTokenClaimReq_Object = MibScalar
editTokenClaimReq = _EditTokenClaimReq_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 4, 6),
    _EditTokenClaimReq_Type()
)
editTokenClaimReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    editTokenClaimReq.setStatus("mandatory")


class _EditTokenLastClaimRspRetVal_Type(Integer32):
    """Custom type editTokenLastClaimRspRetVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99,
              100,
              101,
              102,
              103,
              104,
              105)
        )
    )
    namedValues = NamedValues(
        *(("failClaiming", 100),
          ("failGetBuffer", 103),
          ("failNotReady", 105),
          ("failReqTimeout", 102),
          ("failTaken", 2),
          ("failTakenThisSwitch", 101),
          ("failUpdating", 104),
          ("failVersionTooOld", 3),
          ("failWrongDomainName", 4),
          ("notReady", 99),
          ("success", 1))
    )


_EditTokenLastClaimRspRetVal_Type.__name__ = "Integer32"
_EditTokenLastClaimRspRetVal_Object = MibScalar
editTokenLastClaimRspRetVal = _EditTokenLastClaimRspRetVal_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 4, 7),
    _EditTokenLastClaimRspRetVal_Type()
)
editTokenLastClaimRspRetVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    editTokenLastClaimRspRetVal.setStatus("mandatory")


class _EditTokenReleaseReq_Type(Integer32):
    """Custom type editTokenReleaseReq based on Integer32"""
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
        *(("modeChangeRestoreDefault", 4),
          ("noSave", 1),
          ("save", 2),
          ("saveWithConfirmOption", 3))
    )


_EditTokenReleaseReq_Type.__name__ = "Integer32"
_EditTokenReleaseReq_Object = MibScalar
editTokenReleaseReq = _EditTokenReleaseReq_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 4, 8),
    _EditTokenReleaseReq_Type()
)
editTokenReleaseReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    editTokenReleaseReq.setStatus("mandatory")


class _EditTokenLastReleaseRspRetVal_Type(Integer32):
    """Custom type editTokenLastReleaseRspRetVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99,
              100,
              101,
              102,
              104,
              105,
              106,
              107,
              108)
        )
    )
    namedValues = NamedValues(
        *(("failClaiming", 100),
          ("failForceReleased", 102),
          ("failLocalError", 107),
          ("failNotOwner", 3),
          ("failNotReady", 108),
          ("failNotTaken", 2),
          ("failNotTakenThisAppl", 106),
          ("failReleasing", 104),
          ("failReplacing", 4),
          ("failReqTimeout", 101),
          ("failSaving", 105),
          ("notReady", 99),
          ("success", 1))
    )


_EditTokenLastReleaseRspRetVal_Type.__name__ = "Integer32"
_EditTokenLastReleaseRspRetVal_Object = MibScalar
editTokenLastReleaseRspRetVal = _EditTokenLastReleaseRspRetVal_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 4, 9),
    _EditTokenLastReleaseRspRetVal_Type()
)
editTokenLastReleaseRspRetVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    editTokenLastReleaseRspRetVal.setStatus("mandatory")
_EditTokenForceReleaseReq_Type = Integer32
_EditTokenForceReleaseReq_Object = MibScalar
editTokenForceReleaseReq = _EditTokenForceReleaseReq_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 4, 10),
    _EditTokenForceReleaseReq_Type()
)
editTokenForceReleaseReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    editTokenForceReleaseReq.setStatus("mandatory")


class _EditTokenClientState_Type(Integer32):
    """Custom type editTokenClientState based on Integer32"""
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
        *(("claiming", 3),
          ("expectingNewNvpdb", 6),
          ("notTaken", 1),
          ("reclaiming", 5),
          ("releasing", 4),
          ("taken", 2))
    )


_EditTokenClientState_Type.__name__ = "Integer32"
_EditTokenClientState_Object = MibScalar
editTokenClientState = _EditTokenClientState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 4, 11),
    _EditTokenClientState_Type()
)
editTokenClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    editTokenClientState.setStatus("mandatory")
_EditTokenTakenTime_Type = TimeTicks
_EditTokenTakenTime_Object = MibScalar
editTokenTakenTime = _EditTokenTakenTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 4, 12),
    _EditTokenTakenTime_Type()
)
editTokenTakenTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    editTokenTakenTime.setStatus("mandatory")


class _EditTokenLastForceReleaseRspRetVal_Type(Integer32):
    """Custom type editTokenLastForceReleaseRspRetVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 4),
          ("notReady", 99),
          ("notTaken", 3),
          ("success", 1),
          ("timeout", 2))
    )


_EditTokenLastForceReleaseRspRetVal_Type.__name__ = "Integer32"
_EditTokenLastForceReleaseRspRetVal_Object = MibScalar
editTokenLastForceReleaseRspRetVal = _EditTokenLastForceReleaseRspRetVal_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 4, 13),
    _EditTokenLastForceReleaseRspRetVal_Type()
)
editTokenLastForceReleaseRspRetVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    editTokenLastForceReleaseRspRetVal.setStatus("mandatory")


class _EditTokenServerState_Type(Integer32):
    """Custom type editTokenServerState based on Integer32"""
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
        *(("forceReleasing", 4),
          ("notTaken", 1),
          ("releasing", 2),
          ("taken", 3))
    )


_EditTokenServerState_Type.__name__ = "Integer32"
_EditTokenServerState_Object = MibScalar
editTokenServerState = _EditTokenServerState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 4, 14),
    _EditTokenServerState_Type()
)
editTokenServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    editTokenServerState.setStatus("mandatory")
_VlanTrapObjects_ObjectIdentity = ObjectIdentity
vlanTrapObjects = _VlanTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 6)
)


class _PreviousVlanDomainName_Type(DisplayString):
    """Custom type previousVlanDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PreviousVlanDomainName_Type.__name__ = "DisplayString"
_PreviousVlanDomainName_Object = MibScalar
previousVlanDomainName = _PreviousVlanDomainName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 6, 1),
    _PreviousVlanDomainName_Type()
)
previousVlanDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    previousVlanDomainName.setStatus("mandatory")
_VlanParsingErrorNo_Type = Integer32
_VlanParsingErrorNo_Object = MibScalar
vlanParsingErrorNo = _VlanParsingErrorNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 6, 2),
    _VlanParsingErrorNo_Type()
)
vlanParsingErrorNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanParsingErrorNo.setStatus("mandatory")


class _VlanParsingErrorText_Type(OctetString):
    """Custom type vlanParsingErrorText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VlanParsingErrorText_Type.__name__ = "OctetString"
_VlanParsingErrorText_Object = MibScalar
vlanParsingErrorText = _VlanParsingErrorText_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 6, 3),
    _VlanParsingErrorText_Type()
)
vlanParsingErrorText.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanParsingErrorText.setStatus("mandatory")
_OriginatorIpAddress_Type = IpAddress
_OriginatorIpAddress_Object = MibScalar
originatorIpAddress = _OriginatorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 6, 4),
    _OriginatorIpAddress_Type()
)
originatorIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    originatorIpAddress.setStatus("mandatory")


class _OriginatorMacAddress_Type(EthMacAddress):
    """Custom type originatorMacAddress based on EthMacAddress"""
    subtypeSpec = EthMacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OriginatorMacAddress_Type.__name__ = "EthMacAddress"
_OriginatorMacAddress_Object = MibScalar
originatorMacAddress = _OriginatorMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 6, 5),
    _OriginatorMacAddress_Type()
)
originatorMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    originatorMacAddress.setStatus("mandatory")


class _OriginatorSysName_Type(OctetString):
    """Custom type originatorSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OriginatorSysName_Type.__name__ = "OctetString"
_OriginatorSysName_Object = MibScalar
originatorSysName = _OriginatorSysName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 6, 6),
    _OriginatorSysName_Type()
)
originatorSysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    originatorSysName.setStatus("mandatory")
_OriginatorMgtStationIpAddress_Type = IpAddress
_OriginatorMgtStationIpAddress_Object = MibScalar
originatorMgtStationIpAddress = _OriginatorMgtStationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 6, 7),
    _OriginatorMgtStationIpAddress_Type()
)
originatorMgtStationIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    originatorMgtStationIpAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects

globalVlanConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 0, 1)
)
globalVlanConfigurationChange.setObjects(
    ("INTEL-VLAN-MIB", "vlanPolicyDomainName")
)
if mibBuilder.loadTexts:
    globalVlanConfigurationChange.setStatus(
        ""
    )

localConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 0, 2)
)
localConfigurationChange.setObjects(
      *(("INTEL-VLAN-MIB", "vlanPolicyDomainName"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    localConfigurationChange.setStatus(
        ""
    )

invalidVlanConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 0, 3)
)
invalidVlanConfiguration.setObjects(
      *(("INTEL-VLAN-MIB", "vlanPolicyDomainName"),
        ("INTEL-VLAN-MIB", "vlanParsingErrorNo"),
        ("INTEL-VLAN-MIB", "vlanParsingErrorText"))
)
if mibBuilder.loadTexts:
    invalidVlanConfiguration.setStatus(
        ""
    )

domainNameChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 0, 5)
)
domainNameChange.setObjects(
      *(("INTEL-VLAN-MIB", "previousVlanDomainName"),
        ("INTEL-VLAN-MIB", "vlanPolicyDomainName"))
)
if mibBuilder.loadTexts:
    domainNameChange.setStatus(
        ""
    )

newSwitchInDomain = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 0, 6)
)
newSwitchInDomain.setObjects(
      *(("INTEL-VLAN-MIB", "vlanPolicyDomainName"),
        ("INTEL-VLAN-MIB", "islIfIndex"),
        ("INTEL-VLAN-MIB", "islMacAddress"),
        ("INTEL-VLAN-MIB", "islIpAddress"))
)
if mibBuilder.loadTexts:
    newSwitchInDomain.setStatus(
        ""
    )

missingSwitchInDomain = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 0, 7)
)
missingSwitchInDomain.setObjects(
      *(("INTEL-VLAN-MIB", "vlanPolicyDomainName"),
        ("INTEL-VLAN-MIB", "islIfIndex"),
        ("INTEL-VLAN-MIB", "islMacAddress"),
        ("INTEL-VLAN-MIB", "islIpAddress"))
)
if mibBuilder.loadTexts:
    missingSwitchInDomain.setStatus(
        ""
    )

editTokenForceRelease = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 0, 8)
)
editTokenForceRelease.setObjects(
      *(("INTEL-VLAN-MIB", "vlanPolicyDomainName"),
        ("INTEL-VLAN-MIB", "originatorIpAddress"),
        ("INTEL-VLAN-MIB", "originatorMacAddress"),
        ("INTEL-VLAN-MIB", "originatorSysName"),
        ("INTEL-VLAN-MIB", "originatorMgtStationIpAddress"))
)
if mibBuilder.loadTexts:
    editTokenForceRelease.setStatus(
        ""
    )

editTokenRequestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 0, 9)
)
editTokenRequestFailed.setObjects(
      *(("INTEL-VLAN-MIB", "vlanPolicyDomainName"),
        ("INTEL-VLAN-MIB", "originatorMgtStationIpAddress"))
)
if mibBuilder.loadTexts:
    editTokenRequestFailed.setStatus(
        ""
    )

configConfirmFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 0, 10)
)
configConfirmFailed.setObjects(
      *(("INTEL-VLAN-MIB", "vlanPolicyDomainName"),
        ("INTEL-VLAN-MIB", "originatorSysName"))
)
if mibBuilder.loadTexts:
    configConfirmFailed.setStatus(
        ""
    )

vlanLearnedDatabaseFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 11, 0, 11)
)
vlanLearnedDatabaseFull.setObjects(
    ("INTEL-VLAN-MIB", "vlanPolicyDomainName")
)
if mibBuilder.loadTexts:
    vlanLearnedDatabaseFull.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-VLAN-MIB",
    **{"EthMacAddress": EthMacAddress,
       "vlan": vlan,
       "globalVlanConfigurationChange": globalVlanConfigurationChange,
       "localConfigurationChange": localConfigurationChange,
       "invalidVlanConfiguration": invalidVlanConfiguration,
       "domainNameChange": domainNameChange,
       "newSwitchInDomain": newSwitchInDomain,
       "missingSwitchInDomain": missingSwitchInDomain,
       "editTokenForceRelease": editTokenForceRelease,
       "editTokenRequestFailed": editTokenRequestFailed,
       "configConfirmFailed": configConfirmFailed,
       "vlanLearnedDatabaseFull": vlanLearnedDatabaseFull,
       "vlanPolicy": vlanPolicy,
       "vlanPolicyDomainName": vlanPolicyDomainName,
       "vlanPolicyServerSeqNo": vlanPolicyServerSeqNo,
       "vlanPolicyClientSeqNo": vlanPolicyClientSeqNo,
       "vlanPolicyMode": vlanPolicyMode,
       "vlanPolicyChangedStamp": vlanPolicyChangedStamp,
       "vlanPolicyNextVlanId": vlanPolicyNextVlanId,
       "vlanPolicyLastApiError": vlanPolicyLastApiError,
       "vlanPolicyChangeOperation": vlanPolicyChangeOperation,
       "vlanPolicyVlanTable": vlanPolicyVlanTable,
       "policyVlanEntry": policyVlanEntry,
       "policyVlanId": policyVlanId,
       "policyVlanName": policyVlanName,
       "policyVlanCreateObj": policyVlanCreateObj,
       "policyVlanDeleteObj": policyVlanDeleteObj,
       "vlanPolicyMacRuleTable": vlanPolicyMacRuleTable,
       "policyMacRuleEntry": policyMacRuleEntry,
       "policyMacRuleVlanId": policyMacRuleVlanId,
       "policyMacRuleAddress": policyMacRuleAddress,
       "policyMacRuleCreateObj": policyMacRuleCreateObj,
       "policyMacRuleDeleteObj": policyMacRuleDeleteObj,
       "vlanPolicyIslMacRuleTable": vlanPolicyIslMacRuleTable,
       "policyIslMacRuleEntry": policyIslMacRuleEntry,
       "policyIslMacRuleVlanId": policyIslMacRuleVlanId,
       "policyIslMacRuleAddress": policyIslMacRuleAddress,
       "policyIslMacRuleCreateObj": policyIslMacRuleCreateObj,
       "policyIslMacRuleDeleteObj": policyIslMacRuleDeleteObj,
       "vlanPolicyIpRuleTable": vlanPolicyIpRuleTable,
       "policyIpRuleEntry": policyIpRuleEntry,
       "policyIpRuleVlanId": policyIpRuleVlanId,
       "policyIpRuleAddress": policyIpRuleAddress,
       "policyIpRuleCreateObj": policyIpRuleCreateObj,
       "policyIpRuleDeleteObj": policyIpRuleDeleteObj,
       "vlanPolicyIpNetRuleTable": vlanPolicyIpNetRuleTable,
       "policyIpNetRuleEntry": policyIpNetRuleEntry,
       "policyIpNetRuleVlanId": policyIpNetRuleVlanId,
       "policyIpNetRuleAddress": policyIpNetRuleAddress,
       "policyIpNetRuleMask": policyIpNetRuleMask,
       "policyIpNetRuleCreateObj": policyIpNetRuleCreateObj,
       "policyIpNetRuleDeleteObj": policyIpNetRuleDeleteObj,
       "vlanPolicyPortRuleTable": vlanPolicyPortRuleTable,
       "policyPortRuleEntry": policyPortRuleEntry,
       "policyPortRuleVlanId": policyPortRuleVlanId,
       "policyPortRuleNumber": policyPortRuleNumber,
       "policyPortRuleCreateObj": policyPortRuleCreateObj,
       "policyPortRuleDeleteObj": policyPortRuleDeleteObj,
       "vlanPolicyPortSettingsTable": vlanPolicyPortSettingsTable,
       "policyPortSettingsEntry": policyPortSettingsEntry,
       "policyPortSettingsPortNumber": policyPortSettingsPortNumber,
       "policyPortSettingsIpLearning": policyPortSettingsIpLearning,
       "vlanPolicyAllPortSettingsIpLearning": vlanPolicyAllPortSettingsIpLearning,
       "vlanPolicyAssignManagementVlan": vlanPolicyAssignManagementVlan,
       "vlanPolicyConfigConfState": vlanPolicyConfigConfState,
       "vlanPolicyConfigConfTimerValue": vlanPolicyConfigConfTimerValue,
       "vlanPolicySupportedVlanModes": vlanPolicySupportedVlanModes,
       "vlanPolicyRevert2Default": vlanPolicyRevert2Default,
       "vlanPolicyMacVlanServerPriority": vlanPolicyMacVlanServerPriority,
       "vlanPolicyAutoMoveMgtIpLink": vlanPolicyAutoMoveMgtIpLink,
       "vlanPolicyStackPortRuleTable": vlanPolicyStackPortRuleTable,
       "policyStackPortRuleEntry": policyStackPortRuleEntry,
       "policyStackPortRuleVlanId": policyStackPortRuleVlanId,
       "policyStackPortRuleSwitchMac": policyStackPortRuleSwitchMac,
       "policyStackPortRuleNumber": policyStackPortRuleNumber,
       "policyStackPortRuleCreateObj": policyStackPortRuleCreateObj,
       "policyStackPortRuleDeleteObj": policyStackPortRuleDeleteObj,
       "vlanPolicyUseMultiSTP": vlanPolicyUseMultiSTP,
       "vlanPolicyFwdLearnPckts": vlanPolicyFwdLearnPckts,
       "vlanLearned": vlanLearned,
       "vlanLearnedVersion": vlanLearnedVersion,
       "vlanLearnedServerState": vlanLearnedServerState,
       "vlanLearnedServerPriority": vlanLearnedServerPriority,
       "vlanLearnedServerIPAddress": vlanLearnedServerIPAddress,
       "vlanLearnedServerMACAddress": vlanLearnedServerMACAddress,
       "vlanLearnedServerPortNo": vlanLearnedServerPortNo,
       "vlanLearnedServerNameChangeTimer": vlanLearnedServerNameChangeTimer,
       "vlanLearnedServerExpiryTimer": vlanLearnedServerExpiryTimer,
       "vlanLearnedMacTable": vlanLearnedMacTable,
       "learnedMacEntry": learnedMacEntry,
       "learnedMacAddress": learnedMacAddress,
       "learnedMacType": learnedMacType,
       "learnedMacPortNo": learnedMacPortNo,
       "learnedMacIpAddress": learnedMacIpAddress,
       "vlanLearnedMacVlanTable": vlanLearnedMacVlanTable,
       "learnedMacVlanEntry": learnedMacVlanEntry,
       "learnedMacVlanMac": learnedMacVlanMac,
       "learnedMacVlanIndex": learnedMacVlanIndex,
       "learnedMacVlanName": learnedMacVlanName,
       "vlanLearnedVlanPortTable": vlanLearnedVlanPortTable,
       "learnedVlanPortEntry": learnedVlanPortEntry,
       "learnedVlanPortNo": learnedVlanPortNo,
       "learnedVlanPortVlanIndex": learnedVlanPortVlanIndex,
       "learnedVlanPortVlanName": learnedVlanPortVlanName,
       "vlanLearnedVlanIdTable": vlanLearnedVlanIdTable,
       "learnedVlanIdEntry": learnedVlanIdEntry,
       "learnedVlanId": learnedVlanId,
       "learnedVlanIdVlanName": learnedVlanIdVlanName,
       "vlanLearnedSnmpMgtVlanIds": vlanLearnedSnmpMgtVlanIds,
       "vlanLearnedMacVlanFlush": vlanLearnedMacVlanFlush,
       "vlanIsl": vlanIsl,
       "islTable": islTable,
       "islEntry": islEntry,
       "islIfIndex": islIfIndex,
       "islMacAddress": islMacAddress,
       "islIpAddress": islIpAddress,
       "vlanEditToken": vlanEditToken,
       "editTokenOwnerMacAddress": editTokenOwnerMacAddress,
       "editTokenOwnerIpAddress": editTokenOwnerIpAddress,
       "editTokenOwnerSysName": editTokenOwnerSysName,
       "editTokenOwnerApplication": editTokenOwnerApplication,
       "editTokenOwnerSnmpIpAddress": editTokenOwnerSnmpIpAddress,
       "editTokenClaimReq": editTokenClaimReq,
       "editTokenLastClaimRspRetVal": editTokenLastClaimRspRetVal,
       "editTokenReleaseReq": editTokenReleaseReq,
       "editTokenLastReleaseRspRetVal": editTokenLastReleaseRspRetVal,
       "editTokenForceReleaseReq": editTokenForceReleaseReq,
       "editTokenClientState": editTokenClientState,
       "editTokenTakenTime": editTokenTakenTime,
       "editTokenLastForceReleaseRspRetVal": editTokenLastForceReleaseRspRetVal,
       "editTokenServerState": editTokenServerState,
       "vlanTrapObjects": vlanTrapObjects,
       "previousVlanDomainName": previousVlanDomainName,
       "vlanParsingErrorNo": vlanParsingErrorNo,
       "vlanParsingErrorText": vlanParsingErrorText,
       "originatorIpAddress": originatorIpAddress,
       "originatorMacAddress": originatorMacAddress,
       "originatorSysName": originatorSysName,
       "originatorMgtStationIpAddress": originatorMgtStationIpAddress}
)

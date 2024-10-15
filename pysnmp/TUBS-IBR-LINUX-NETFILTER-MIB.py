# SNMP MIB module (TUBS-IBR-LINUX-NETFILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TUBS-IBR-LINUX-NETFILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:54 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(ibr,) = mibBuilder.importSymbols(
    "TUBS-SMI",
    "ibr")


# MODULE-IDENTITY

lnfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13)
)
lnfMIB.setRevisions(
        ("2002-07-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LnfTarget(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("accept", 4),
          ("chain", 7),
          ("drop", 3),
          ("none", 1),
          ("other", 2),
          ("queue", 5),
          ("return", 6))
    )



# MIB Managed Objects in the order of their OIDs

_LnfObjects_ObjectIdentity = ObjectIdentity
lnfObjects = _LnfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1)
)
_LnfLastChange_Type = TimeStamp
_LnfLastChange_Object = MibScalar
lnfLastChange = _LnfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 1),
    _LnfLastChange_Type()
)
lnfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnfLastChange.setStatus("current")
_LnfTableTable_Object = MibTable
lnfTableTable = _LnfTableTable_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 2)
)
if mibBuilder.loadTexts:
    lnfTableTable.setStatus("current")
_LnfTableEntry_Object = MibTableRow
lnfTableEntry = _LnfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 2, 1)
)
lnfTableEntry.setIndexNames(
    (0, "TUBS-IBR-LINUX-NETFILTER-MIB", "lnfTableAddressType"),
    (0, "TUBS-IBR-LINUX-NETFILTER-MIB", "lnfTableName"),
)
if mibBuilder.loadTexts:
    lnfTableEntry.setStatus("current")


class _LnfTableAddressType_Type(InetAddressType):
    """Custom type lnfTableAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_LnfTableAddressType_Type.__name__ = "InetAddressType"
_LnfTableAddressType_Object = MibTableColumn
lnfTableAddressType = _LnfTableAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 2, 1, 1),
    _LnfTableAddressType_Type()
)
lnfTableAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnfTableAddressType.setStatus("current")


class _LnfTableName_Type(SnmpAdminString):
    """Custom type lnfTableName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LnfTableName_Type.__name__ = "SnmpAdminString"
_LnfTableName_Object = MibTableColumn
lnfTableName = _LnfTableName_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 2, 1, 2),
    _LnfTableName_Type()
)
lnfTableName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnfTableName.setStatus("current")
_LnfTableLastChange_Type = TimeStamp
_LnfTableLastChange_Object = MibTableColumn
lnfTableLastChange = _LnfTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 2, 1, 3),
    _LnfTableLastChange_Type()
)
lnfTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnfTableLastChange.setStatus("current")
_LnfChainTable_Object = MibTable
lnfChainTable = _LnfChainTable_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 3)
)
if mibBuilder.loadTexts:
    lnfChainTable.setStatus("current")
_LnfChainEntry_Object = MibTableRow
lnfChainEntry = _LnfChainEntry_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 3, 1)
)
lnfChainEntry.setIndexNames(
    (0, "TUBS-IBR-LINUX-NETFILTER-MIB", "lnfTableAddressType"),
    (0, "TUBS-IBR-LINUX-NETFILTER-MIB", "lnfTableName"),
    (0, "TUBS-IBR-LINUX-NETFILTER-MIB", "lnfChainName"),
)
if mibBuilder.loadTexts:
    lnfChainEntry.setStatus("current")


class _LnfChainName_Type(SnmpAdminString):
    """Custom type lnfChainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LnfChainName_Type.__name__ = "SnmpAdminString"
_LnfChainName_Object = MibTableColumn
lnfChainName = _LnfChainName_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 3, 1, 1),
    _LnfChainName_Type()
)
lnfChainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnfChainName.setStatus("current")
_LnfChainPackets_Type = Counter64
_LnfChainPackets_Object = MibTableColumn
lnfChainPackets = _LnfChainPackets_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 3, 1, 2),
    _LnfChainPackets_Type()
)
lnfChainPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnfChainPackets.setStatus("current")
_LnfChainOctets_Type = Counter64
_LnfChainOctets_Object = MibTableColumn
lnfChainOctets = _LnfChainOctets_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 3, 1, 3),
    _LnfChainOctets_Type()
)
lnfChainOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnfChainOctets.setStatus("current")


class _LnfChainTarget_Type(LnfTarget):
    """Custom type lnfChainTarget based on LnfTarget"""
    defaultValue = 6

    subtypeSpec = LnfTarget.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("accept", 4),
          ("drop", 3),
          ("return", 6))
    )


_LnfChainTarget_Type.__name__ = "LnfTarget"
_LnfChainTarget_Object = MibTableColumn
lnfChainTarget = _LnfChainTarget_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 3, 1, 4),
    _LnfChainTarget_Type()
)
lnfChainTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfChainTarget.setStatus("current")
_LnfChainLastChange_Type = TimeStamp
_LnfChainLastChange_Object = MibTableColumn
lnfChainLastChange = _LnfChainLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 3, 1, 5),
    _LnfChainLastChange_Type()
)
lnfChainLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnfChainLastChange.setStatus("current")
_LnfChainStorage_Type = StorageType
_LnfChainStorage_Object = MibTableColumn
lnfChainStorage = _LnfChainStorage_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 3, 1, 6),
    _LnfChainStorage_Type()
)
lnfChainStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfChainStorage.setStatus("current")
_LnfChainStatus_Type = RowStatus
_LnfChainStatus_Object = MibTableColumn
lnfChainStatus = _LnfChainStatus_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 3, 1, 7),
    _LnfChainStatus_Type()
)
lnfChainStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfChainStatus.setStatus("current")
_LnfRuleTable_Object = MibTable
lnfRuleTable = _LnfRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4)
)
if mibBuilder.loadTexts:
    lnfRuleTable.setStatus("current")
_LnfRuleEntry_Object = MibTableRow
lnfRuleEntry = _LnfRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1)
)
lnfRuleEntry.setIndexNames(
    (0, "TUBS-IBR-LINUX-NETFILTER-MIB", "lnfTableAddressType"),
    (0, "TUBS-IBR-LINUX-NETFILTER-MIB", "lnfTableName"),
    (0, "TUBS-IBR-LINUX-NETFILTER-MIB", "lnfChainName"),
    (0, "TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleIndex"),
)
if mibBuilder.loadTexts:
    lnfRuleEntry.setStatus("current")
_LnfRuleIndex_Type = Unsigned32
_LnfRuleIndex_Object = MibTableColumn
lnfRuleIndex = _LnfRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 1),
    _LnfRuleIndex_Type()
)
lnfRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnfRuleIndex.setStatus("current")


class _LnfRuleProtocol_Type(Unsigned32):
    """Custom type lnfRuleProtocol based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LnfRuleProtocol_Type.__name__ = "Unsigned32"
_LnfRuleProtocol_Object = MibTableColumn
lnfRuleProtocol = _LnfRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 2),
    _LnfRuleProtocol_Type()
)
lnfRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfRuleProtocol.setStatus("current")


class _LnfRuleProtocolInv_Type(TruthValue):
    """Custom type lnfRuleProtocolInv based on TruthValue"""


_LnfRuleProtocolInv_Object = MibTableColumn
lnfRuleProtocolInv = _LnfRuleProtocolInv_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 3),
    _LnfRuleProtocolInv_Type()
)
lnfRuleProtocolInv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfRuleProtocolInv.setStatus("current")
_LnfRuleSourceAddress_Type = InetAddress
_LnfRuleSourceAddress_Object = MibTableColumn
lnfRuleSourceAddress = _LnfRuleSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 4),
    _LnfRuleSourceAddress_Type()
)
lnfRuleSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfRuleSourceAddress.setStatus("current")


class _LnfRuleSourceAddressPrefixLength_Type(InetAddressPrefixLength):
    """Custom type lnfRuleSourceAddressPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_LnfRuleSourceAddressPrefixLength_Object = MibTableColumn
lnfRuleSourceAddressPrefixLength = _LnfRuleSourceAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 5),
    _LnfRuleSourceAddressPrefixLength_Type()
)
lnfRuleSourceAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfRuleSourceAddressPrefixLength.setStatus("current")


class _LnfRuleSourceAddressInv_Type(TruthValue):
    """Custom type lnfRuleSourceAddressInv based on TruthValue"""


_LnfRuleSourceAddressInv_Object = MibTableColumn
lnfRuleSourceAddressInv = _LnfRuleSourceAddressInv_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 6),
    _LnfRuleSourceAddressInv_Type()
)
lnfRuleSourceAddressInv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfRuleSourceAddressInv.setStatus("current")
_LnfRuleDestinationAddress_Type = InetAddress
_LnfRuleDestinationAddress_Object = MibTableColumn
lnfRuleDestinationAddress = _LnfRuleDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 7),
    _LnfRuleDestinationAddress_Type()
)
lnfRuleDestinationAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfRuleDestinationAddress.setStatus("current")


class _LnfRuleDestinationAddressPrefixLength_Type(InetAddressPrefixLength):
    """Custom type lnfRuleDestinationAddressPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_LnfRuleDestinationAddressPrefixLength_Object = MibTableColumn
lnfRuleDestinationAddressPrefixLength = _LnfRuleDestinationAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 8),
    _LnfRuleDestinationAddressPrefixLength_Type()
)
lnfRuleDestinationAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfRuleDestinationAddressPrefixLength.setStatus("current")


class _LnfRuleDestinationAddressInv_Type(TruthValue):
    """Custom type lnfRuleDestinationAddressInv based on TruthValue"""


_LnfRuleDestinationAddressInv_Object = MibTableColumn
lnfRuleDestinationAddressInv = _LnfRuleDestinationAddressInv_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 9),
    _LnfRuleDestinationAddressInv_Type()
)
lnfRuleDestinationAddressInv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfRuleDestinationAddressInv.setStatus("current")


class _LnfRuleInInterface_Type(SnmpAdminString):
    """Custom type lnfRuleInInterface based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LnfRuleInInterface_Type.__name__ = "SnmpAdminString"
_LnfRuleInInterface_Object = MibTableColumn
lnfRuleInInterface = _LnfRuleInInterface_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 10),
    _LnfRuleInInterface_Type()
)
lnfRuleInInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfRuleInInterface.setStatus("current")


class _LnfRuleInInterfaceInv_Type(TruthValue):
    """Custom type lnfRuleInInterfaceInv based on TruthValue"""


_LnfRuleInInterfaceInv_Object = MibTableColumn
lnfRuleInInterfaceInv = _LnfRuleInInterfaceInv_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 11),
    _LnfRuleInInterfaceInv_Type()
)
lnfRuleInInterfaceInv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfRuleInInterfaceInv.setStatus("current")


class _LnfRuleOutInterface_Type(SnmpAdminString):
    """Custom type lnfRuleOutInterface based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LnfRuleOutInterface_Type.__name__ = "SnmpAdminString"
_LnfRuleOutInterface_Object = MibTableColumn
lnfRuleOutInterface = _LnfRuleOutInterface_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 12),
    _LnfRuleOutInterface_Type()
)
lnfRuleOutInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfRuleOutInterface.setStatus("current")


class _LnfRuleOutInterfaceInv_Type(TruthValue):
    """Custom type lnfRuleOutInterfaceInv based on TruthValue"""


_LnfRuleOutInterfaceInv_Object = MibTableColumn
lnfRuleOutInterfaceInv = _LnfRuleOutInterfaceInv_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 13),
    _LnfRuleOutInterfaceInv_Type()
)
lnfRuleOutInterfaceInv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfRuleOutInterfaceInv.setStatus("current")


class _LnfRuleFragment_Type(TruthValue):
    """Custom type lnfRuleFragment based on TruthValue"""


_LnfRuleFragment_Object = MibTableColumn
lnfRuleFragment = _LnfRuleFragment_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 14),
    _LnfRuleFragment_Type()
)
lnfRuleFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfRuleFragment.setStatus("current")


class _LnfRuleFragmentInv_Type(TruthValue):
    """Custom type lnfRuleFragmentInv based on TruthValue"""


_LnfRuleFragmentInv_Object = MibTableColumn
lnfRuleFragmentInv = _LnfRuleFragmentInv_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 15),
    _LnfRuleFragmentInv_Type()
)
lnfRuleFragmentInv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfRuleFragmentInv.setStatus("current")
_LnfRulePackets_Type = Counter64
_LnfRulePackets_Object = MibTableColumn
lnfRulePackets = _LnfRulePackets_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 16),
    _LnfRulePackets_Type()
)
lnfRulePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnfRulePackets.setStatus("current")
_LnfRuleOctets_Type = Counter64
_LnfRuleOctets_Object = MibTableColumn
lnfRuleOctets = _LnfRuleOctets_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 17),
    _LnfRuleOctets_Type()
)
lnfRuleOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnfRuleOctets.setStatus("current")


class _LnfRuleTarget_Type(LnfTarget):
    """Custom type lnfRuleTarget based on LnfTarget"""


_LnfRuleTarget_Object = MibTableColumn
lnfRuleTarget = _LnfRuleTarget_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 18),
    _LnfRuleTarget_Type()
)
lnfRuleTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfRuleTarget.setStatus("current")


class _LnfRuleTargetChain_Type(SnmpAdminString):
    """Custom type lnfRuleTargetChain based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LnfRuleTargetChain_Type.__name__ = "SnmpAdminString"
_LnfRuleTargetChain_Object = MibTableColumn
lnfRuleTargetChain = _LnfRuleTargetChain_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 19),
    _LnfRuleTargetChain_Type()
)
lnfRuleTargetChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfRuleTargetChain.setStatus("current")


class _LnfRuleTrapEnable_Type(TruthValue):
    """Custom type lnfRuleTrapEnable based on TruthValue"""


_LnfRuleTrapEnable_Object = MibTableColumn
lnfRuleTrapEnable = _LnfRuleTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 20),
    _LnfRuleTrapEnable_Type()
)
lnfRuleTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lnfRuleTrapEnable.setStatus("current")
_LnfRuleLastChange_Type = TimeStamp
_LnfRuleLastChange_Object = MibTableColumn
lnfRuleLastChange = _LnfRuleLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 21),
    _LnfRuleLastChange_Type()
)
lnfRuleLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnfRuleLastChange.setStatus("current")
_LnfRuleStorage_Type = StorageType
_LnfRuleStorage_Object = MibTableColumn
lnfRuleStorage = _LnfRuleStorage_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 22),
    _LnfRuleStorage_Type()
)
lnfRuleStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfRuleStorage.setStatus("current")
_LnfRuleStatus_Type = RowStatus
_LnfRuleStatus_Object = MibTableColumn
lnfRuleStatus = _LnfRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 23),
    _LnfRuleStatus_Type()
)
lnfRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lnfRuleStatus.setStatus("current")
_LnfTraps_ObjectIdentity = ObjectIdentity
lnfTraps = _LnfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 2)
)
_LnfNotifications_ObjectIdentity = ObjectIdentity
lnfNotifications = _LnfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 2, 0)
)
_LnfConformance_ObjectIdentity = ObjectIdentity
lnfConformance = _LnfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 3)
)
_LnfCompliances_ObjectIdentity = ObjectIdentity
lnfCompliances = _LnfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 3, 1)
)
_LnfGroups_ObjectIdentity = ObjectIdentity
lnfGroups = _LnfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 3, 2)
)

# Managed Objects groups

lnfGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 3, 2, 1)
)
lnfGeneralGroup.setObjects(
      *(("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfLastChange"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfTableLastChange"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfChainPackets"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfChainOctets"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfChainTarget"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfChainLastChange"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfChainStorage"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfChainStatus"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleProtocol"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleProtocolInv"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleSourceAddress"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleSourceAddressPrefixLength"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleSourceAddressInv"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleDestinationAddress"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleDestinationAddressPrefixLength"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleDestinationAddressInv"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleInInterface"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleInInterfaceInv"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleOutInterface"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleOutInterfaceInv"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleFragment"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleFragmentInv"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRulePackets"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleOctets"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleTarget"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleTargetChain"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleTrapEnable"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleLastChange"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleStorage"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleStatus"))
)
if mibBuilder.loadTexts:
    lnfGeneralGroup.setStatus("current")


# Notification objects

lnfRuleMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 2, 0, 1)
)
lnfRuleMatch.setObjects(
      *(("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRulePackets"),
        ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleOctets"))
)
if mibBuilder.loadTexts:
    lnfRuleMatch.setStatus(
        "current"
    )


# Notifications groups

lnfNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 3, 2, 2)
)
lnfNotificationGroup.setObjects(
    ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleMatch")
)
if mibBuilder.loadTexts:
    lnfNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lnfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1575, 1, 13, 3, 1, 1)
)
if mibBuilder.loadTexts:
    lnfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TUBS-IBR-LINUX-NETFILTER-MIB",
    **{"LnfTarget": LnfTarget,
       "lnfMIB": lnfMIB,
       "lnfObjects": lnfObjects,
       "lnfLastChange": lnfLastChange,
       "lnfTableTable": lnfTableTable,
       "lnfTableEntry": lnfTableEntry,
       "lnfTableAddressType": lnfTableAddressType,
       "lnfTableName": lnfTableName,
       "lnfTableLastChange": lnfTableLastChange,
       "lnfChainTable": lnfChainTable,
       "lnfChainEntry": lnfChainEntry,
       "lnfChainName": lnfChainName,
       "lnfChainPackets": lnfChainPackets,
       "lnfChainOctets": lnfChainOctets,
       "lnfChainTarget": lnfChainTarget,
       "lnfChainLastChange": lnfChainLastChange,
       "lnfChainStorage": lnfChainStorage,
       "lnfChainStatus": lnfChainStatus,
       "lnfRuleTable": lnfRuleTable,
       "lnfRuleEntry": lnfRuleEntry,
       "lnfRuleIndex": lnfRuleIndex,
       "lnfRuleProtocol": lnfRuleProtocol,
       "lnfRuleProtocolInv": lnfRuleProtocolInv,
       "lnfRuleSourceAddress": lnfRuleSourceAddress,
       "lnfRuleSourceAddressPrefixLength": lnfRuleSourceAddressPrefixLength,
       "lnfRuleSourceAddressInv": lnfRuleSourceAddressInv,
       "lnfRuleDestinationAddress": lnfRuleDestinationAddress,
       "lnfRuleDestinationAddressPrefixLength": lnfRuleDestinationAddressPrefixLength,
       "lnfRuleDestinationAddressInv": lnfRuleDestinationAddressInv,
       "lnfRuleInInterface": lnfRuleInInterface,
       "lnfRuleInInterfaceInv": lnfRuleInInterfaceInv,
       "lnfRuleOutInterface": lnfRuleOutInterface,
       "lnfRuleOutInterfaceInv": lnfRuleOutInterfaceInv,
       "lnfRuleFragment": lnfRuleFragment,
       "lnfRuleFragmentInv": lnfRuleFragmentInv,
       "lnfRulePackets": lnfRulePackets,
       "lnfRuleOctets": lnfRuleOctets,
       "lnfRuleTarget": lnfRuleTarget,
       "lnfRuleTargetChain": lnfRuleTargetChain,
       "lnfRuleTrapEnable": lnfRuleTrapEnable,
       "lnfRuleLastChange": lnfRuleLastChange,
       "lnfRuleStorage": lnfRuleStorage,
       "lnfRuleStatus": lnfRuleStatus,
       "lnfTraps": lnfTraps,
       "lnfNotifications": lnfNotifications,
       "lnfRuleMatch": lnfRuleMatch,
       "lnfConformance": lnfConformance,
       "lnfCompliances": lnfCompliances,
       "lnfCompliance": lnfCompliance,
       "lnfGroups": lnfGroups,
       "lnfGeneralGroup": lnfGeneralGroup,
       "lnfNotificationGroup": lnfNotificationGroup}
)

# SNMP MIB module (CISCO-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:29 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoIpProtocol,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoIpProtocol")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoACLMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 808)
)
ciscoACLMIB.setRevisions(
        ("2013-03-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CaAclTrafficDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )



class CaAclACLIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CaAclSequenceNumber(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CaAclPortOperator(Integer32, TextualConvention):
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
        *(("eq", 3),
          ("gt", 2),
          ("lt", 1),
          ("neq", 4),
          ("range", 5))
    )



class CaAclAction(Integer32, TextualConvention):
    status = "current"
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



class CaAclLogOption(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("logInput", 2))
    )



class CaAclTcpFlagsMatch(Integer32, TextualConvention):
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
        *(("matchAll", 2),
          ("matchAny", 1),
          ("matchNone", 3))
    )



class CaAclPrecedenceValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("flash", 3),
          ("flashOverride", 4),
          ("immediate", 2),
          ("internet", 6),
          ("network", 7),
          ("priority", 1),
          ("routine", 0))
    )



# MIB Managed Objects in the order of their OIDs

_CaAclMIBObjects_ObjectIdentity = ObjectIdentity
caAclMIBObjects = _CaAclMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1)
)
_CaAclConfiguration_ObjectIdentity = ObjectIdentity
caAclConfiguration = _CaAclConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1)
)
_CaAclCfgTable_Object = MibTable
caAclCfgTable = _CaAclCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 1)
)
if mibBuilder.loadTexts:
    caAclCfgTable.setStatus("current")
_CaAclCfgTableEntry_Object = MibTableRow
caAclCfgTableEntry = _CaAclCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 1, 1)
)
caAclCfgTableEntry.setIndexNames(
    (0, "CISCO-ACL-MIB", "caAclIndex"),
    (0, "CISCO-ACL-MIB", "caAclAddressType"),
)
if mibBuilder.loadTexts:
    caAclCfgTableEntry.setStatus("current")
_CaAclIndex_Type = CaAclACLIndex
_CaAclIndex_Object = MibTableColumn
caAclIndex = _CaAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 1, 1, 1),
    _CaAclIndex_Type()
)
caAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caAclIndex.setStatus("current")
_CaAclAddressType_Type = InetAddressType
_CaAclAddressType_Object = MibTableColumn
caAclAddressType = _CaAclAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 1, 1, 2),
    _CaAclAddressType_Type()
)
caAclAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caAclAddressType.setStatus("current")


class _CaAclName_Type(SnmpAdminString):
    """Custom type caAclName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CaAclName_Type.__name__ = "SnmpAdminString"
_CaAclName_Object = MibTableColumn
caAclName = _CaAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 1, 1, 3),
    _CaAclName_Type()
)
caAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclName.setStatus("current")
_CaAclRowStatus_Type = RowStatus
_CaAclRowStatus_Object = MibTableColumn
caAclRowStatus = _CaAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 1, 1, 4),
    _CaAclRowStatus_Type()
)
caAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclRowStatus.setStatus("current")
_CaAclIPV4ACECfgTable_Object = MibTable
caAclIPV4ACECfgTable = _CaAclIPV4ACECfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2)
)
if mibBuilder.loadTexts:
    caAclIPV4ACECfgTable.setStatus("current")
_CaAclIPV4ACECfgTableEntry_Object = MibTableRow
caAclIPV4ACECfgTableEntry = _CaAclIPV4ACECfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1)
)
caAclIPV4ACECfgTableEntry.setIndexNames(
    (0, "CISCO-ACL-MIB", "caAclIndex"),
    (0, "CISCO-ACL-MIB", "caAclAddressType"),
    (0, "CISCO-ACL-MIB", "caAclIPV4ACESequenceNumber"),
)
if mibBuilder.loadTexts:
    caAclIPV4ACECfgTableEntry.setStatus("current")
_CaAclIPV4ACESequenceNumber_Type = CaAclSequenceNumber
_CaAclIPV4ACESequenceNumber_Object = MibTableColumn
caAclIPV4ACESequenceNumber = _CaAclIPV4ACESequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 1),
    _CaAclIPV4ACESequenceNumber_Type()
)
caAclIPV4ACESequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caAclIPV4ACESequenceNumber.setStatus("current")
_CaAclIPV4ACEAction_Type = CaAclAction
_CaAclIPV4ACEAction_Object = MibTableColumn
caAclIPV4ACEAction = _CaAclIPV4ACEAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 2),
    _CaAclIPV4ACEAction_Type()
)
caAclIPV4ACEAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACEAction.setStatus("current")
_CaAclIPV4ACEProtocol_Type = CiscoIpProtocol
_CaAclIPV4ACEProtocol_Object = MibTableColumn
caAclIPV4ACEProtocol = _CaAclIPV4ACEProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 3),
    _CaAclIPV4ACEProtocol_Type()
)
caAclIPV4ACEProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACEProtocol.setStatus("current")
_CaAclIPV4ACESourceAddress_Type = InetAddress
_CaAclIPV4ACESourceAddress_Object = MibTableColumn
caAclIPV4ACESourceAddress = _CaAclIPV4ACESourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 4),
    _CaAclIPV4ACESourceAddress_Type()
)
caAclIPV4ACESourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACESourceAddress.setStatus("current")
_CaAclIPV4ACESourceWildCardMask_Type = InetAddress
_CaAclIPV4ACESourceWildCardMask_Object = MibTableColumn
caAclIPV4ACESourceWildCardMask = _CaAclIPV4ACESourceWildCardMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 5),
    _CaAclIPV4ACESourceWildCardMask_Type()
)
caAclIPV4ACESourceWildCardMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACESourceWildCardMask.setStatus("current")


class _CaAclIPV4ACESourceNetworkGroup_Type(SnmpAdminString):
    """Custom type caAclIPV4ACESourceNetworkGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CaAclIPV4ACESourceNetworkGroup_Type.__name__ = "SnmpAdminString"
_CaAclIPV4ACESourceNetworkGroup_Object = MibTableColumn
caAclIPV4ACESourceNetworkGroup = _CaAclIPV4ACESourceNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 6),
    _CaAclIPV4ACESourceNetworkGroup_Type()
)
caAclIPV4ACESourceNetworkGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACESourceNetworkGroup.setStatus("current")
_CaAclIPV4ACESourcePortOperator_Type = CaAclPortOperator
_CaAclIPV4ACESourcePortOperator_Object = MibTableColumn
caAclIPV4ACESourcePortOperator = _CaAclIPV4ACESourcePortOperator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 7),
    _CaAclIPV4ACESourcePortOperator_Type()
)
caAclIPV4ACESourcePortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACESourcePortOperator.setStatus("current")
_CaAclIPV4ACESourcePort_Type = InetPortNumber
_CaAclIPV4ACESourcePort_Object = MibTableColumn
caAclIPV4ACESourcePort = _CaAclIPV4ACESourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 8),
    _CaAclIPV4ACESourcePort_Type()
)
caAclIPV4ACESourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACESourcePort.setStatus("current")
_CaAclIPV4ACESourcePortUpper_Type = InetPortNumber
_CaAclIPV4ACESourcePortUpper_Object = MibTableColumn
caAclIPV4ACESourcePortUpper = _CaAclIPV4ACESourcePortUpper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 9),
    _CaAclIPV4ACESourcePortUpper_Type()
)
caAclIPV4ACESourcePortUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACESourcePortUpper.setStatus("current")


class _CaAclIPV4ACESourcePortGroup_Type(SnmpAdminString):
    """Custom type caAclIPV4ACESourcePortGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CaAclIPV4ACESourcePortGroup_Type.__name__ = "SnmpAdminString"
_CaAclIPV4ACESourcePortGroup_Object = MibTableColumn
caAclIPV4ACESourcePortGroup = _CaAclIPV4ACESourcePortGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 10),
    _CaAclIPV4ACESourcePortGroup_Type()
)
caAclIPV4ACESourcePortGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACESourcePortGroup.setStatus("current")
_CaAclIPV4ACEDestinationAddress_Type = InetAddress
_CaAclIPV4ACEDestinationAddress_Object = MibTableColumn
caAclIPV4ACEDestinationAddress = _CaAclIPV4ACEDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 11),
    _CaAclIPV4ACEDestinationAddress_Type()
)
caAclIPV4ACEDestinationAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACEDestinationAddress.setStatus("current")
_CaAclIPV4ACEDestinationWildCardMask_Type = InetAddress
_CaAclIPV4ACEDestinationWildCardMask_Object = MibTableColumn
caAclIPV4ACEDestinationWildCardMask = _CaAclIPV4ACEDestinationWildCardMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 12),
    _CaAclIPV4ACEDestinationWildCardMask_Type()
)
caAclIPV4ACEDestinationWildCardMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACEDestinationWildCardMask.setStatus("current")


class _CaAclIPV4ACEDestinationNetworkGroup_Type(SnmpAdminString):
    """Custom type caAclIPV4ACEDestinationNetworkGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CaAclIPV4ACEDestinationNetworkGroup_Type.__name__ = "SnmpAdminString"
_CaAclIPV4ACEDestinationNetworkGroup_Object = MibTableColumn
caAclIPV4ACEDestinationNetworkGroup = _CaAclIPV4ACEDestinationNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 13),
    _CaAclIPV4ACEDestinationNetworkGroup_Type()
)
caAclIPV4ACEDestinationNetworkGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACEDestinationNetworkGroup.setStatus("current")
_CaAclIPV4ACEDestinationPortOperator_Type = CaAclPortOperator
_CaAclIPV4ACEDestinationPortOperator_Object = MibTableColumn
caAclIPV4ACEDestinationPortOperator = _CaAclIPV4ACEDestinationPortOperator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 14),
    _CaAclIPV4ACEDestinationPortOperator_Type()
)
caAclIPV4ACEDestinationPortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACEDestinationPortOperator.setStatus("current")
_CaAclIPV4ACEDestinationPort_Type = InetPortNumber
_CaAclIPV4ACEDestinationPort_Object = MibTableColumn
caAclIPV4ACEDestinationPort = _CaAclIPV4ACEDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 15),
    _CaAclIPV4ACEDestinationPort_Type()
)
caAclIPV4ACEDestinationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACEDestinationPort.setStatus("current")
_CaAclIPV4ACEDestinationPortUpper_Type = InetPortNumber
_CaAclIPV4ACEDestinationPortUpper_Object = MibTableColumn
caAclIPV4ACEDestinationPortUpper = _CaAclIPV4ACEDestinationPortUpper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 16),
    _CaAclIPV4ACEDestinationPortUpper_Type()
)
caAclIPV4ACEDestinationPortUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACEDestinationPortUpper.setStatus("current")


class _CaAclIPV4ACEDestinationPortGroup_Type(SnmpAdminString):
    """Custom type caAclIPV4ACEDestinationPortGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CaAclIPV4ACEDestinationPortGroup_Type.__name__ = "SnmpAdminString"
_CaAclIPV4ACEDestinationPortGroup_Object = MibTableColumn
caAclIPV4ACEDestinationPortGroup = _CaAclIPV4ACEDestinationPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 17),
    _CaAclIPV4ACEDestinationPortGroup_Type()
)
caAclIPV4ACEDestinationPortGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACEDestinationPortGroup.setStatus("current")


class _CaAclIPV4ACEDscpValue_Type(Unsigned32):
    """Custom type caAclIPV4ACEDscpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CaAclIPV4ACEDscpValue_Type.__name__ = "Unsigned32"
_CaAclIPV4ACEDscpValue_Object = MibTableColumn
caAclIPV4ACEDscpValue = _CaAclIPV4ACEDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 18),
    _CaAclIPV4ACEDscpValue_Type()
)
caAclIPV4ACEDscpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACEDscpValue.setStatus("current")


class _CaAclIPV4ACETcpFlagsValue_Type(Unsigned32):
    """Custom type caAclIPV4ACETcpFlagsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CaAclIPV4ACETcpFlagsValue_Type.__name__ = "Unsigned32"
_CaAclIPV4ACETcpFlagsValue_Object = MibTableColumn
caAclIPV4ACETcpFlagsValue = _CaAclIPV4ACETcpFlagsValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 19),
    _CaAclIPV4ACETcpFlagsValue_Type()
)
caAclIPV4ACETcpFlagsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACETcpFlagsValue.setStatus("current")


class _CaAclIPV4ACETcpFlagsMask_Type(Unsigned32):
    """Custom type caAclIPV4ACETcpFlagsMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CaAclIPV4ACETcpFlagsMask_Type.__name__ = "Unsigned32"
_CaAclIPV4ACETcpFlagsMask_Object = MibTableColumn
caAclIPV4ACETcpFlagsMask = _CaAclIPV4ACETcpFlagsMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 20),
    _CaAclIPV4ACETcpFlagsMask_Type()
)
caAclIPV4ACETcpFlagsMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACETcpFlagsMask.setStatus("current")
_CaAclIPV4ACETcpFlagsMatchType_Type = CaAclTcpFlagsMatch
_CaAclIPV4ACETcpFlagsMatchType_Object = MibTableColumn
caAclIPV4ACETcpFlagsMatchType = _CaAclIPV4ACETcpFlagsMatchType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 21),
    _CaAclIPV4ACETcpFlagsMatchType_Type()
)
caAclIPV4ACETcpFlagsMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACETcpFlagsMatchType.setStatus("current")


class _CaAclIPV4ACETosValue_Type(Unsigned32):
    """Custom type caAclIPV4ACETosValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CaAclIPV4ACETosValue_Type.__name__ = "Unsigned32"
_CaAclIPV4ACETosValue_Object = MibTableColumn
caAclIPV4ACETosValue = _CaAclIPV4ACETosValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 22),
    _CaAclIPV4ACETosValue_Type()
)
caAclIPV4ACETosValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACETosValue.setStatus("current")
_CaAclIPV4ACEPrecedenceValue_Type = CaAclPrecedenceValue
_CaAclIPV4ACEPrecedenceValue_Object = MibTableColumn
caAclIPV4ACEPrecedenceValue = _CaAclIPV4ACEPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 23),
    _CaAclIPV4ACEPrecedenceValue_Type()
)
caAclIPV4ACEPrecedenceValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACEPrecedenceValue.setStatus("current")
_CaAclIPV4ACELogOption_Type = CaAclLogOption
_CaAclIPV4ACELogOption_Object = MibTableColumn
caAclIPV4ACELogOption = _CaAclIPV4ACELogOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 24),
    _CaAclIPV4ACELogOption_Type()
)
caAclIPV4ACELogOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACELogOption.setStatus("current")


class _CaAclIPV4ACECounterLabel_Type(SnmpAdminString):
    """Custom type caAclIPV4ACECounterLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CaAclIPV4ACECounterLabel_Type.__name__ = "SnmpAdminString"
_CaAclIPV4ACECounterLabel_Object = MibTableColumn
caAclIPV4ACECounterLabel = _CaAclIPV4ACECounterLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 25),
    _CaAclIPV4ACECounterLabel_Type()
)
caAclIPV4ACECounterLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACECounterLabel.setStatus("current")


class _CaAclIPV4ACERemark_Type(SnmpAdminString):
    """Custom type caAclIPV4ACERemark based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CaAclIPV4ACERemark_Type.__name__ = "SnmpAdminString"
_CaAclIPV4ACERemark_Object = MibTableColumn
caAclIPV4ACERemark = _CaAclIPV4ACERemark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 26),
    _CaAclIPV4ACERemark_Type()
)
caAclIPV4ACERemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACERemark.setStatus("current")
_CaAclIPV4ACERowStatus_Type = RowStatus
_CaAclIPV4ACERowStatus_Object = MibTableColumn
caAclIPV4ACERowStatus = _CaAclIPV4ACERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 2, 1, 27),
    _CaAclIPV4ACERowStatus_Type()
)
caAclIPV4ACERowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV4ACERowStatus.setStatus("current")
_CaAclIPV6ACECfgTable_Object = MibTable
caAclIPV6ACECfgTable = _CaAclIPV6ACECfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3)
)
if mibBuilder.loadTexts:
    caAclIPV6ACECfgTable.setStatus("current")
_CaAclIPV6ACECfgTableEntry_Object = MibTableRow
caAclIPV6ACECfgTableEntry = _CaAclIPV6ACECfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1)
)
caAclIPV6ACECfgTableEntry.setIndexNames(
    (0, "CISCO-ACL-MIB", "caAclIndex"),
    (0, "CISCO-ACL-MIB", "caAclAddressType"),
    (0, "CISCO-ACL-MIB", "caAclIPV6ACESequenceNumber"),
)
if mibBuilder.loadTexts:
    caAclIPV6ACECfgTableEntry.setStatus("current")
_CaAclIPV6ACESequenceNumber_Type = CaAclSequenceNumber
_CaAclIPV6ACESequenceNumber_Object = MibTableColumn
caAclIPV6ACESequenceNumber = _CaAclIPV6ACESequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 1),
    _CaAclIPV6ACESequenceNumber_Type()
)
caAclIPV6ACESequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caAclIPV6ACESequenceNumber.setStatus("current")
_CaAclIPV6ACEAction_Type = CaAclAction
_CaAclIPV6ACEAction_Object = MibTableColumn
caAclIPV6ACEAction = _CaAclIPV6ACEAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 2),
    _CaAclIPV6ACEAction_Type()
)
caAclIPV6ACEAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACEAction.setStatus("current")
_CaAclIPV6ACEProtocol_Type = CiscoIpProtocol
_CaAclIPV6ACEProtocol_Object = MibTableColumn
caAclIPV6ACEProtocol = _CaAclIPV6ACEProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 3),
    _CaAclIPV6ACEProtocol_Type()
)
caAclIPV6ACEProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACEProtocol.setStatus("current")
_CaAclIPV6ACESourceAddress_Type = InetAddress
_CaAclIPV6ACESourceAddress_Object = MibTableColumn
caAclIPV6ACESourceAddress = _CaAclIPV6ACESourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 4),
    _CaAclIPV6ACESourceAddress_Type()
)
caAclIPV6ACESourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACESourceAddress.setStatus("current")


class _CaAclIPV6ACESourcePrefixLength_Type(Integer32):
    """Custom type caAclIPV6ACESourcePrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CaAclIPV6ACESourcePrefixLength_Type.__name__ = "Integer32"
_CaAclIPV6ACESourcePrefixLength_Object = MibTableColumn
caAclIPV6ACESourcePrefixLength = _CaAclIPV6ACESourcePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 5),
    _CaAclIPV6ACESourcePrefixLength_Type()
)
caAclIPV6ACESourcePrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACESourcePrefixLength.setStatus("current")


class _CaAclIPV6ACESourceNetworkGroup_Type(SnmpAdminString):
    """Custom type caAclIPV6ACESourceNetworkGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CaAclIPV6ACESourceNetworkGroup_Type.__name__ = "SnmpAdminString"
_CaAclIPV6ACESourceNetworkGroup_Object = MibTableColumn
caAclIPV6ACESourceNetworkGroup = _CaAclIPV6ACESourceNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 6),
    _CaAclIPV6ACESourceNetworkGroup_Type()
)
caAclIPV6ACESourceNetworkGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACESourceNetworkGroup.setStatus("current")
_CaAclIPV6ACESourcePortOperator_Type = CaAclPortOperator
_CaAclIPV6ACESourcePortOperator_Object = MibTableColumn
caAclIPV6ACESourcePortOperator = _CaAclIPV6ACESourcePortOperator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 7),
    _CaAclIPV6ACESourcePortOperator_Type()
)
caAclIPV6ACESourcePortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACESourcePortOperator.setStatus("current")
_CaAclIPV6ACESourcePort_Type = InetPortNumber
_CaAclIPV6ACESourcePort_Object = MibTableColumn
caAclIPV6ACESourcePort = _CaAclIPV6ACESourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 8),
    _CaAclIPV6ACESourcePort_Type()
)
caAclIPV6ACESourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACESourcePort.setStatus("current")
_CaAclIPV6ACESourcePortUpper_Type = InetPortNumber
_CaAclIPV6ACESourcePortUpper_Object = MibTableColumn
caAclIPV6ACESourcePortUpper = _CaAclIPV6ACESourcePortUpper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 9),
    _CaAclIPV6ACESourcePortUpper_Type()
)
caAclIPV6ACESourcePortUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACESourcePortUpper.setStatus("current")


class _CaAclIPV6ACESourcePortGroup_Type(SnmpAdminString):
    """Custom type caAclIPV6ACESourcePortGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CaAclIPV6ACESourcePortGroup_Type.__name__ = "SnmpAdminString"
_CaAclIPV6ACESourcePortGroup_Object = MibTableColumn
caAclIPV6ACESourcePortGroup = _CaAclIPV6ACESourcePortGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 10),
    _CaAclIPV6ACESourcePortGroup_Type()
)
caAclIPV6ACESourcePortGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACESourcePortGroup.setStatus("current")
_CaAclIPV6ACEDestinationAddress_Type = InetAddress
_CaAclIPV6ACEDestinationAddress_Object = MibTableColumn
caAclIPV6ACEDestinationAddress = _CaAclIPV6ACEDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 11),
    _CaAclIPV6ACEDestinationAddress_Type()
)
caAclIPV6ACEDestinationAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACEDestinationAddress.setStatus("current")


class _CaAclIPV6ACEDestinationPrefixLength_Type(Integer32):
    """Custom type caAclIPV6ACEDestinationPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CaAclIPV6ACEDestinationPrefixLength_Type.__name__ = "Integer32"
_CaAclIPV6ACEDestinationPrefixLength_Object = MibTableColumn
caAclIPV6ACEDestinationPrefixLength = _CaAclIPV6ACEDestinationPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 12),
    _CaAclIPV6ACEDestinationPrefixLength_Type()
)
caAclIPV6ACEDestinationPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACEDestinationPrefixLength.setStatus("current")


class _CaAclIPV6ACEDestinationNetworkGroup_Type(SnmpAdminString):
    """Custom type caAclIPV6ACEDestinationNetworkGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CaAclIPV6ACEDestinationNetworkGroup_Type.__name__ = "SnmpAdminString"
_CaAclIPV6ACEDestinationNetworkGroup_Object = MibTableColumn
caAclIPV6ACEDestinationNetworkGroup = _CaAclIPV6ACEDestinationNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 13),
    _CaAclIPV6ACEDestinationNetworkGroup_Type()
)
caAclIPV6ACEDestinationNetworkGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACEDestinationNetworkGroup.setStatus("current")
_CaAclIPV6ACEDestinationPortOperator_Type = CaAclPortOperator
_CaAclIPV6ACEDestinationPortOperator_Object = MibTableColumn
caAclIPV6ACEDestinationPortOperator = _CaAclIPV6ACEDestinationPortOperator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 14),
    _CaAclIPV6ACEDestinationPortOperator_Type()
)
caAclIPV6ACEDestinationPortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACEDestinationPortOperator.setStatus("current")
_CaAclIPV6ACEDestinationPort_Type = InetPortNumber
_CaAclIPV6ACEDestinationPort_Object = MibTableColumn
caAclIPV6ACEDestinationPort = _CaAclIPV6ACEDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 15),
    _CaAclIPV6ACEDestinationPort_Type()
)
caAclIPV6ACEDestinationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACEDestinationPort.setStatus("current")
_CaAclIPV6ACEDestinationPortUpper_Type = InetPortNumber
_CaAclIPV6ACEDestinationPortUpper_Object = MibTableColumn
caAclIPV6ACEDestinationPortUpper = _CaAclIPV6ACEDestinationPortUpper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 16),
    _CaAclIPV6ACEDestinationPortUpper_Type()
)
caAclIPV6ACEDestinationPortUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACEDestinationPortUpper.setStatus("current")


class _CaAclIPV6ACEDestinationPortGroup_Type(SnmpAdminString):
    """Custom type caAclIPV6ACEDestinationPortGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CaAclIPV6ACEDestinationPortGroup_Type.__name__ = "SnmpAdminString"
_CaAclIPV6ACEDestinationPortGroup_Object = MibTableColumn
caAclIPV6ACEDestinationPortGroup = _CaAclIPV6ACEDestinationPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 17),
    _CaAclIPV6ACEDestinationPortGroup_Type()
)
caAclIPV6ACEDestinationPortGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACEDestinationPortGroup.setStatus("current")


class _CaAclIPV6ACETrafficClassValue_Type(Unsigned32):
    """Custom type caAclIPV6ACETrafficClassValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CaAclIPV6ACETrafficClassValue_Type.__name__ = "Unsigned32"
_CaAclIPV6ACETrafficClassValue_Object = MibTableColumn
caAclIPV6ACETrafficClassValue = _CaAclIPV6ACETrafficClassValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 18),
    _CaAclIPV6ACETrafficClassValue_Type()
)
caAclIPV6ACETrafficClassValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACETrafficClassValue.setStatus("current")


class _CaAclIPV6ACETcpFlagsValue_Type(Unsigned32):
    """Custom type caAclIPV6ACETcpFlagsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CaAclIPV6ACETcpFlagsValue_Type.__name__ = "Unsigned32"
_CaAclIPV6ACETcpFlagsValue_Object = MibTableColumn
caAclIPV6ACETcpFlagsValue = _CaAclIPV6ACETcpFlagsValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 19),
    _CaAclIPV6ACETcpFlagsValue_Type()
)
caAclIPV6ACETcpFlagsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACETcpFlagsValue.setStatus("current")


class _CaAclIPV6ACETcpFlagsMask_Type(Unsigned32):
    """Custom type caAclIPV6ACETcpFlagsMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CaAclIPV6ACETcpFlagsMask_Type.__name__ = "Unsigned32"
_CaAclIPV6ACETcpFlagsMask_Object = MibTableColumn
caAclIPV6ACETcpFlagsMask = _CaAclIPV6ACETcpFlagsMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 20),
    _CaAclIPV6ACETcpFlagsMask_Type()
)
caAclIPV6ACETcpFlagsMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACETcpFlagsMask.setStatus("current")
_CaAclIPV6ACETcpFlagsMatchType_Type = CaAclTcpFlagsMatch
_CaAclIPV6ACETcpFlagsMatchType_Object = MibTableColumn
caAclIPV6ACETcpFlagsMatchType = _CaAclIPV6ACETcpFlagsMatchType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 21),
    _CaAclIPV6ACETcpFlagsMatchType_Type()
)
caAclIPV6ACETcpFlagsMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACETcpFlagsMatchType.setStatus("current")
_CaAclIPV6ACELogOption_Type = CaAclLogOption
_CaAclIPV6ACELogOption_Object = MibTableColumn
caAclIPV6ACELogOption = _CaAclIPV6ACELogOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 22),
    _CaAclIPV6ACELogOption_Type()
)
caAclIPV6ACELogOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACELogOption.setStatus("current")


class _CaAclIPV6ACECounterLabel_Type(SnmpAdminString):
    """Custom type caAclIPV6ACECounterLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CaAclIPV6ACECounterLabel_Type.__name__ = "SnmpAdminString"
_CaAclIPV6ACECounterLabel_Object = MibTableColumn
caAclIPV6ACECounterLabel = _CaAclIPV6ACECounterLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 23),
    _CaAclIPV6ACECounterLabel_Type()
)
caAclIPV6ACECounterLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACECounterLabel.setStatus("current")


class _CaAclIPV6ACERemark_Type(SnmpAdminString):
    """Custom type caAclIPV6ACERemark based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CaAclIPV6ACERemark_Type.__name__ = "SnmpAdminString"
_CaAclIPV6ACERemark_Object = MibTableColumn
caAclIPV6ACERemark = _CaAclIPV6ACERemark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 24),
    _CaAclIPV6ACERemark_Type()
)
caAclIPV6ACERemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACERemark.setStatus("current")
_CaAclIPV6ACERowStatus_Type = RowStatus
_CaAclIPV6ACERowStatus_Object = MibTableColumn
caAclIPV6ACERowStatus = _CaAclIPV6ACERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 3, 1, 25),
    _CaAclIPV6ACERowStatus_Type()
)
caAclIPV6ACERowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclIPV6ACERowStatus.setStatus("current")
_CaAclAccessGroupCfgTable_Object = MibTable
caAclAccessGroupCfgTable = _CaAclAccessGroupCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 4)
)
if mibBuilder.loadTexts:
    caAclAccessGroupCfgTable.setStatus("current")
_CaAclAccessGroupCfgEntry_Object = MibTableRow
caAclAccessGroupCfgEntry = _CaAclAccessGroupCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 4, 1)
)
caAclAccessGroupCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ACL-MIB", "caAclAccessGroupCfgAddressType"),
    (0, "CISCO-ACL-MIB", "caAclAccessGroupDirection"),
    (0, "CISCO-ACL-MIB", "caAclAccessGroupSequenceNumber"),
)
if mibBuilder.loadTexts:
    caAclAccessGroupCfgEntry.setStatus("current")
_CaAclAccessGroupACL_Type = CaAclACLIndex
_CaAclAccessGroupACL_Object = MibTableColumn
caAclAccessGroupACL = _CaAclAccessGroupACL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 4, 1, 1),
    _CaAclAccessGroupACL_Type()
)
caAclAccessGroupACL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclAccessGroupACL.setStatus("current")
_CaAclAccessGroupCfgAddressType_Type = InetAddressType
_CaAclAccessGroupCfgAddressType_Object = MibTableColumn
caAclAccessGroupCfgAddressType = _CaAclAccessGroupCfgAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 4, 1, 2),
    _CaAclAccessGroupCfgAddressType_Type()
)
caAclAccessGroupCfgAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caAclAccessGroupCfgAddressType.setStatus("current")
_CaAclAccessGroupDirection_Type = CaAclTrafficDirection
_CaAclAccessGroupDirection_Object = MibTableColumn
caAclAccessGroupDirection = _CaAclAccessGroupDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 4, 1, 3),
    _CaAclAccessGroupDirection_Type()
)
caAclAccessGroupDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caAclAccessGroupDirection.setStatus("current")
_CaAclAccessGroupSequenceNumber_Type = CaAclSequenceNumber
_CaAclAccessGroupSequenceNumber_Object = MibTableColumn
caAclAccessGroupSequenceNumber = _CaAclAccessGroupSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 4, 1, 4),
    _CaAclAccessGroupSequenceNumber_Type()
)
caAclAccessGroupSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caAclAccessGroupSequenceNumber.setStatus("current")
_CaAclAccessGroupRowStatus_Type = RowStatus
_CaAclAccessGroupRowStatus_Object = MibTableColumn
caAclAccessGroupRowStatus = _CaAclAccessGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 1, 4, 1, 5),
    _CaAclAccessGroupRowStatus_Type()
)
caAclAccessGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAclAccessGroupRowStatus.setStatus("current")
_CaAclStats_ObjectIdentity = ObjectIdentity
caAclStats = _CaAclStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 2)
)
_CaAclLabelIntfStatsTable_Object = MibTable
caAclLabelIntfStatsTable = _CaAclLabelIntfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 2, 1)
)
if mibBuilder.loadTexts:
    caAclLabelIntfStatsTable.setStatus("current")
_CaAclLabelIntfStatsEntry_Object = MibTableRow
caAclLabelIntfStatsEntry = _CaAclLabelIntfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 2, 1, 1)
)
caAclLabelIntfStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ACL-MIB", "caAclAccessGroupCfgAddressType"),
    (0, "CISCO-ACL-MIB", "caAclAccessGroupDirection"),
    (0, "CISCO-ACL-MIB", "caAclIntfStatsCounterLabelName"),
)
if mibBuilder.loadTexts:
    caAclLabelIntfStatsEntry.setStatus("current")


class _CaAclIntfStatsCounterLabelName_Type(SnmpAdminString):
    """Custom type caAclIntfStatsCounterLabelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CaAclIntfStatsCounterLabelName_Type.__name__ = "SnmpAdminString"
_CaAclIntfStatsCounterLabelName_Object = MibTableColumn
caAclIntfStatsCounterLabelName = _CaAclIntfStatsCounterLabelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 2, 1, 1, 1),
    _CaAclIntfStatsCounterLabelName_Type()
)
caAclIntfStatsCounterLabelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caAclIntfStatsCounterLabelName.setStatus("current")
_CaAclIntfStatsPackets_Type = Counter64
_CaAclIntfStatsPackets_Object = MibTableColumn
caAclIntfStatsPackets = _CaAclIntfStatsPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 2, 1, 1, 2),
    _CaAclIntfStatsPackets_Type()
)
caAclIntfStatsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caAclIntfStatsPackets.setStatus("current")
if mibBuilder.loadTexts:
    caAclIntfStatsPackets.setUnits("packets")
_CaAclIntfStatsOctets_Type = Counter64
_CaAclIntfStatsOctets_Object = MibTableColumn
caAclIntfStatsOctets = _CaAclIntfStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 1, 2, 1, 1, 3),
    _CaAclIntfStatsOctets_Type()
)
caAclIntfStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caAclIntfStatsOctets.setStatus("current")
if mibBuilder.loadTexts:
    caAclIntfStatsOctets.setUnits("bytes")
_CaAclMIBConformance_ObjectIdentity = ObjectIdentity
caAclMIBConformance = _CaAclMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 2)
)
_CaAclMIBACEConform_ObjectIdentity = ObjectIdentity
caAclMIBACEConform = _CaAclMIBACEConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 2, 1)
)
_CaAclMIBACECompliances_ObjectIdentity = ObjectIdentity
caAclMIBACECompliances = _CaAclMIBACECompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 2, 1, 1)
)
_CaAclMIBCfgGroups_ObjectIdentity = ObjectIdentity
caAclMIBCfgGroups = _CaAclMIBCfgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 2, 1, 2)
)

# Managed Objects groups

caAclMIBCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 2, 1, 2, 1)
)
caAclMIBCfgGroup.setObjects(
      *(("CISCO-ACL-MIB", "caAclName"),
        ("CISCO-ACL-MIB", "caAclRowStatus"))
)
if mibBuilder.loadTexts:
    caAclMIBCfgGroup.setStatus("current")

caAclIPV4ACLMIBACEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 2, 1, 2, 2)
)
caAclIPV4ACLMIBACEGroup.setObjects(
      *(("CISCO-ACL-MIB", "caAclIPV4ACEAction"),
        ("CISCO-ACL-MIB", "caAclIPV4ACEProtocol"),
        ("CISCO-ACL-MIB", "caAclIPV4ACESourceAddress"),
        ("CISCO-ACL-MIB", "caAclIPV4ACESourceWildCardMask"),
        ("CISCO-ACL-MIB", "caAclIPV4ACESourceNetworkGroup"),
        ("CISCO-ACL-MIB", "caAclIPV4ACESourcePortOperator"),
        ("CISCO-ACL-MIB", "caAclIPV4ACESourcePort"),
        ("CISCO-ACL-MIB", "caAclIPV4ACESourcePortUpper"),
        ("CISCO-ACL-MIB", "caAclIPV4ACESourcePortGroup"),
        ("CISCO-ACL-MIB", "caAclIPV4ACEDestinationAddress"),
        ("CISCO-ACL-MIB", "caAclIPV4ACEDestinationWildCardMask"),
        ("CISCO-ACL-MIB", "caAclIPV4ACEDestinationNetworkGroup"),
        ("CISCO-ACL-MIB", "caAclIPV4ACEDestinationPortOperator"),
        ("CISCO-ACL-MIB", "caAclIPV4ACEDestinationPort"),
        ("CISCO-ACL-MIB", "caAclIPV4ACEDestinationPortUpper"),
        ("CISCO-ACL-MIB", "caAclIPV4ACEDestinationPortGroup"),
        ("CISCO-ACL-MIB", "caAclIPV4ACEDscpValue"),
        ("CISCO-ACL-MIB", "caAclIPV4ACETcpFlagsValue"),
        ("CISCO-ACL-MIB", "caAclIPV4ACETcpFlagsMask"),
        ("CISCO-ACL-MIB", "caAclIPV4ACETcpFlagsMatchType"),
        ("CISCO-ACL-MIB", "caAclIPV4ACETosValue"),
        ("CISCO-ACL-MIB", "caAclIPV4ACEPrecedenceValue"),
        ("CISCO-ACL-MIB", "caAclIPV4ACELogOption"),
        ("CISCO-ACL-MIB", "caAclIPV4ACECounterLabel"),
        ("CISCO-ACL-MIB", "caAclIPV4ACERemark"),
        ("CISCO-ACL-MIB", "caAclIPV4ACERowStatus"))
)
if mibBuilder.loadTexts:
    caAclIPV4ACLMIBACEGroup.setStatus("current")

caAclIPV6ACLMIBACEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 2, 1, 2, 3)
)
caAclIPV6ACLMIBACEGroup.setObjects(
      *(("CISCO-ACL-MIB", "caAclIPV6ACEAction"),
        ("CISCO-ACL-MIB", "caAclIPV6ACEProtocol"),
        ("CISCO-ACL-MIB", "caAclIPV6ACESourceAddress"),
        ("CISCO-ACL-MIB", "caAclIPV6ACESourcePrefixLength"),
        ("CISCO-ACL-MIB", "caAclIPV6ACESourceNetworkGroup"),
        ("CISCO-ACL-MIB", "caAclIPV6ACESourcePortOperator"),
        ("CISCO-ACL-MIB", "caAclIPV6ACESourcePort"),
        ("CISCO-ACL-MIB", "caAclIPV6ACESourcePortUpper"),
        ("CISCO-ACL-MIB", "caAclIPV6ACESourcePortGroup"),
        ("CISCO-ACL-MIB", "caAclIPV6ACEDestinationAddress"),
        ("CISCO-ACL-MIB", "caAclIPV6ACEDestinationPrefixLength"),
        ("CISCO-ACL-MIB", "caAclIPV6ACEDestinationNetworkGroup"),
        ("CISCO-ACL-MIB", "caAclIPV6ACEDestinationPortOperator"),
        ("CISCO-ACL-MIB", "caAclIPV6ACEDestinationPort"),
        ("CISCO-ACL-MIB", "caAclIPV6ACEDestinationPortUpper"),
        ("CISCO-ACL-MIB", "caAclIPV6ACEDestinationPortGroup"),
        ("CISCO-ACL-MIB", "caAclIPV6ACETcpFlagsValue"),
        ("CISCO-ACL-MIB", "caAclIPV6ACETcpFlagsMask"),
        ("CISCO-ACL-MIB", "caAclIPV6ACETcpFlagsMatchType"),
        ("CISCO-ACL-MIB", "caAclIPV6ACETrafficClassValue"),
        ("CISCO-ACL-MIB", "caAclIPV6ACELogOption"),
        ("CISCO-ACL-MIB", "caAclIPV6ACECounterLabel"),
        ("CISCO-ACL-MIB", "caAclIPV6ACERemark"),
        ("CISCO-ACL-MIB", "caAclIPV6ACERowStatus"))
)
if mibBuilder.loadTexts:
    caAclIPV6ACLMIBACEGroup.setStatus("current")

caAclMIBAccessGroupCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 2, 1, 2, 4)
)
caAclMIBAccessGroupCfgGroup.setObjects(
      *(("CISCO-ACL-MIB", "caAclAccessGroupACL"),
        ("CISCO-ACL-MIB", "caAclAccessGroupRowStatus"))
)
if mibBuilder.loadTexts:
    caAclMIBAccessGroupCfgGroup.setStatus("current")

caAclMIBCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 2, 1, 2, 5)
)
caAclMIBCounterGroup.setObjects(
      *(("CISCO-ACL-MIB", "caAclIntfStatsPackets"),
        ("CISCO-ACL-MIB", "caAclIntfStatsOctets"))
)
if mibBuilder.loadTexts:
    caAclMIBCounterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

caAclMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 808, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    caAclMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ACL-MIB",
    **{"CaAclTrafficDirection": CaAclTrafficDirection,
       "CaAclACLIndex": CaAclACLIndex,
       "CaAclSequenceNumber": CaAclSequenceNumber,
       "CaAclPortOperator": CaAclPortOperator,
       "CaAclAction": CaAclAction,
       "CaAclLogOption": CaAclLogOption,
       "CaAclTcpFlagsMatch": CaAclTcpFlagsMatch,
       "CaAclPrecedenceValue": CaAclPrecedenceValue,
       "ciscoACLMIB": ciscoACLMIB,
       "caAclMIBObjects": caAclMIBObjects,
       "caAclConfiguration": caAclConfiguration,
       "caAclCfgTable": caAclCfgTable,
       "caAclCfgTableEntry": caAclCfgTableEntry,
       "caAclIndex": caAclIndex,
       "caAclAddressType": caAclAddressType,
       "caAclName": caAclName,
       "caAclRowStatus": caAclRowStatus,
       "caAclIPV4ACECfgTable": caAclIPV4ACECfgTable,
       "caAclIPV4ACECfgTableEntry": caAclIPV4ACECfgTableEntry,
       "caAclIPV4ACESequenceNumber": caAclIPV4ACESequenceNumber,
       "caAclIPV4ACEAction": caAclIPV4ACEAction,
       "caAclIPV4ACEProtocol": caAclIPV4ACEProtocol,
       "caAclIPV4ACESourceAddress": caAclIPV4ACESourceAddress,
       "caAclIPV4ACESourceWildCardMask": caAclIPV4ACESourceWildCardMask,
       "caAclIPV4ACESourceNetworkGroup": caAclIPV4ACESourceNetworkGroup,
       "caAclIPV4ACESourcePortOperator": caAclIPV4ACESourcePortOperator,
       "caAclIPV4ACESourcePort": caAclIPV4ACESourcePort,
       "caAclIPV4ACESourcePortUpper": caAclIPV4ACESourcePortUpper,
       "caAclIPV4ACESourcePortGroup": caAclIPV4ACESourcePortGroup,
       "caAclIPV4ACEDestinationAddress": caAclIPV4ACEDestinationAddress,
       "caAclIPV4ACEDestinationWildCardMask": caAclIPV4ACEDestinationWildCardMask,
       "caAclIPV4ACEDestinationNetworkGroup": caAclIPV4ACEDestinationNetworkGroup,
       "caAclIPV4ACEDestinationPortOperator": caAclIPV4ACEDestinationPortOperator,
       "caAclIPV4ACEDestinationPort": caAclIPV4ACEDestinationPort,
       "caAclIPV4ACEDestinationPortUpper": caAclIPV4ACEDestinationPortUpper,
       "caAclIPV4ACEDestinationPortGroup": caAclIPV4ACEDestinationPortGroup,
       "caAclIPV4ACEDscpValue": caAclIPV4ACEDscpValue,
       "caAclIPV4ACETcpFlagsValue": caAclIPV4ACETcpFlagsValue,
       "caAclIPV4ACETcpFlagsMask": caAclIPV4ACETcpFlagsMask,
       "caAclIPV4ACETcpFlagsMatchType": caAclIPV4ACETcpFlagsMatchType,
       "caAclIPV4ACETosValue": caAclIPV4ACETosValue,
       "caAclIPV4ACEPrecedenceValue": caAclIPV4ACEPrecedenceValue,
       "caAclIPV4ACELogOption": caAclIPV4ACELogOption,
       "caAclIPV4ACECounterLabel": caAclIPV4ACECounterLabel,
       "caAclIPV4ACERemark": caAclIPV4ACERemark,
       "caAclIPV4ACERowStatus": caAclIPV4ACERowStatus,
       "caAclIPV6ACECfgTable": caAclIPV6ACECfgTable,
       "caAclIPV6ACECfgTableEntry": caAclIPV6ACECfgTableEntry,
       "caAclIPV6ACESequenceNumber": caAclIPV6ACESequenceNumber,
       "caAclIPV6ACEAction": caAclIPV6ACEAction,
       "caAclIPV6ACEProtocol": caAclIPV6ACEProtocol,
       "caAclIPV6ACESourceAddress": caAclIPV6ACESourceAddress,
       "caAclIPV6ACESourcePrefixLength": caAclIPV6ACESourcePrefixLength,
       "caAclIPV6ACESourceNetworkGroup": caAclIPV6ACESourceNetworkGroup,
       "caAclIPV6ACESourcePortOperator": caAclIPV6ACESourcePortOperator,
       "caAclIPV6ACESourcePort": caAclIPV6ACESourcePort,
       "caAclIPV6ACESourcePortUpper": caAclIPV6ACESourcePortUpper,
       "caAclIPV6ACESourcePortGroup": caAclIPV6ACESourcePortGroup,
       "caAclIPV6ACEDestinationAddress": caAclIPV6ACEDestinationAddress,
       "caAclIPV6ACEDestinationPrefixLength": caAclIPV6ACEDestinationPrefixLength,
       "caAclIPV6ACEDestinationNetworkGroup": caAclIPV6ACEDestinationNetworkGroup,
       "caAclIPV6ACEDestinationPortOperator": caAclIPV6ACEDestinationPortOperator,
       "caAclIPV6ACEDestinationPort": caAclIPV6ACEDestinationPort,
       "caAclIPV6ACEDestinationPortUpper": caAclIPV6ACEDestinationPortUpper,
       "caAclIPV6ACEDestinationPortGroup": caAclIPV6ACEDestinationPortGroup,
       "caAclIPV6ACETrafficClassValue": caAclIPV6ACETrafficClassValue,
       "caAclIPV6ACETcpFlagsValue": caAclIPV6ACETcpFlagsValue,
       "caAclIPV6ACETcpFlagsMask": caAclIPV6ACETcpFlagsMask,
       "caAclIPV6ACETcpFlagsMatchType": caAclIPV6ACETcpFlagsMatchType,
       "caAclIPV6ACELogOption": caAclIPV6ACELogOption,
       "caAclIPV6ACECounterLabel": caAclIPV6ACECounterLabel,
       "caAclIPV6ACERemark": caAclIPV6ACERemark,
       "caAclIPV6ACERowStatus": caAclIPV6ACERowStatus,
       "caAclAccessGroupCfgTable": caAclAccessGroupCfgTable,
       "caAclAccessGroupCfgEntry": caAclAccessGroupCfgEntry,
       "caAclAccessGroupACL": caAclAccessGroupACL,
       "caAclAccessGroupCfgAddressType": caAclAccessGroupCfgAddressType,
       "caAclAccessGroupDirection": caAclAccessGroupDirection,
       "caAclAccessGroupSequenceNumber": caAclAccessGroupSequenceNumber,
       "caAclAccessGroupRowStatus": caAclAccessGroupRowStatus,
       "caAclStats": caAclStats,
       "caAclLabelIntfStatsTable": caAclLabelIntfStatsTable,
       "caAclLabelIntfStatsEntry": caAclLabelIntfStatsEntry,
       "caAclIntfStatsCounterLabelName": caAclIntfStatsCounterLabelName,
       "caAclIntfStatsPackets": caAclIntfStatsPackets,
       "caAclIntfStatsOctets": caAclIntfStatsOctets,
       "caAclMIBConformance": caAclMIBConformance,
       "caAclMIBACEConform": caAclMIBACEConform,
       "caAclMIBACECompliances": caAclMIBACECompliances,
       "caAclMIBCompliance": caAclMIBCompliance,
       "caAclMIBCfgGroups": caAclMIBCfgGroups,
       "caAclMIBCfgGroup": caAclMIBCfgGroup,
       "caAclIPV4ACLMIBACEGroup": caAclIPV4ACLMIBACEGroup,
       "caAclIPV6ACLMIBACEGroup": caAclIPV6ACLMIBACEGroup,
       "caAclMIBAccessGroupCfgGroup": caAclMIBAccessGroupCfgGroup,
       "caAclMIBCounterGroup": caAclMIBCounterGroup}
)

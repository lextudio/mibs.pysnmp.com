# SNMP MIB module (BDCOM-QOS-PIB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BDCOM-QOS-PIB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:35 2024
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

(bdcomPibToMib,) = mibBuilder.importSymbols(
    "BDCOM-SMI",
    "bdcomPibToMib")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

bdcomQosPIBMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1)
)
bdcomQosPIBMIB.setRevisions(
        ("2003-10-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Dscp(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class QosLayer2Cos(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class QueueRange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("eightQ", 8),
          ("fourQ", 4),
          ("oneQ", 1),
          ("sixteenQ", 16),
          ("sixtyFourQ", 64),
          ("thirtyTwoQ", 32),
          ("threeQ", 3),
          ("twoQ", 2))
    )



class ThresholdSetRange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eightT", 8),
          ("fourT", 4),
          ("oneT", 1),
          ("twoT", 2),
          ("zeroT", 0))
    )



class Percent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class QosInterfaceQueueType(Integer32, TextualConvention):
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("eightQ1t", 17),
          ("eightQ2t", 18),
          ("eightQ4t", 19),
          ("eightQ8t", 20),
          ("fourQ1t", 13),
          ("fourQ2t", 14),
          ("fourQ4t", 15),
          ("fourQ8t", 16),
          ("oneP1Q0t", 27),
          ("oneP1Q4t", 28),
          ("oneP1Q8t", 29),
          ("oneP2Q1t", 30),
          ("oneP2Q2t", 31),
          ("oneP3Q1t", 32),
          ("oneP7Q8t", 33),
          ("oneQ1t", 1),
          ("oneQ2t", 2),
          ("oneQ4t", 3),
          ("oneQ8t", 4),
          ("sixteenQ1t", 21),
          ("sixteenQ2t", 22),
          ("sixteenQ4t", 23),
          ("sixtyfourQ1t", 24),
          ("sixtyfourQ2t", 25),
          ("sixtyfourQ4t", 26),
          ("threeQ1t", 9),
          ("threeQ2t", 10),
          ("threeQ4t", 11),
          ("threeQ8t", 12),
          ("twoQ1t", 5),
          ("twoQ2t", 6),
          ("twoQ4t", 7),
          ("twoQ8t", 8))
    )



class QosInterfaceTypeCapabilities(Bits, TextualConvention):
    status = "current"


class RoleCombination(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class PolicyInstanceId(Unsigned32, TextualConvention):
    status = "current"


class Unsigned64(Counter64, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_QosPIBConformance_ObjectIdentity = ObjectIdentity
qosPIBConformance = _QosPIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1)
)
_QosPIBCompliances_ObjectIdentity = ObjectIdentity
qosPIBCompliances = _QosPIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 1)
)
_QosPIBGroups_ObjectIdentity = ObjectIdentity
qosPIBGroups = _QosPIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2)
)
_QosDeviceConfig_ObjectIdentity = ObjectIdentity
qosDeviceConfig = _QosDeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2)
)
_QosDevicePibIncarnationTable_Object = MibTable
qosDevicePibIncarnationTable = _QosDevicePibIncarnationTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    qosDevicePibIncarnationTable.setStatus("current")
_QosDevicePibIncarnationEntry_Object = MibTableRow
qosDevicePibIncarnationEntry = _QosDevicePibIncarnationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 1, 1)
)
qosDevicePibIncarnationEntry.setIndexNames(
    (0, "BDCOM-QOS-PIB-MIB", "qosDeviceIncarnationId"),
)
if mibBuilder.loadTexts:
    qosDevicePibIncarnationEntry.setStatus("current")
_QosDeviceIncarnationId_Type = PolicyInstanceId
_QosDeviceIncarnationId_Object = MibTableColumn
qosDeviceIncarnationId = _QosDeviceIncarnationId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 1, 1, 1),
    _QosDeviceIncarnationId_Type()
)
qosDeviceIncarnationId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosDeviceIncarnationId.setStatus("current")
_QosDevicePdpName_Type = DisplayString
_QosDevicePdpName_Object = MibTableColumn
qosDevicePdpName = _QosDevicePdpName_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 1, 1, 2),
    _QosDevicePdpName_Type()
)
qosDevicePdpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDevicePdpName.setStatus("current")


class _QosDevicePibIncarnation_Type(OctetString):
    """Custom type qosDevicePibIncarnation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_QosDevicePibIncarnation_Type.__name__ = "OctetString"
_QosDevicePibIncarnation_Object = MibTableColumn
qosDevicePibIncarnation = _QosDevicePibIncarnation_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 1, 1, 3),
    _QosDevicePibIncarnation_Type()
)
qosDevicePibIncarnation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDevicePibIncarnation.setStatus("current")
_QosDevicePibTtl_Type = Unsigned32
_QosDevicePibTtl_Object = MibTableColumn
qosDevicePibTtl = _QosDevicePibTtl_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 1, 1, 4),
    _QosDevicePibTtl_Type()
)
qosDevicePibTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDevicePibTtl.setStatus("current")
_QosDeviceAttributeTable_Object = MibTable
qosDeviceAttributeTable = _QosDeviceAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    qosDeviceAttributeTable.setStatus("current")
_QosDeviceAttributeEntry_Object = MibTableRow
qosDeviceAttributeEntry = _QosDeviceAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 2, 1)
)
qosDeviceAttributeEntry.setIndexNames(
    (0, "BDCOM-QOS-PIB-MIB", "qosDeviceAttributeId"),
)
if mibBuilder.loadTexts:
    qosDeviceAttributeEntry.setStatus("current")
_QosDeviceAttributeId_Type = PolicyInstanceId
_QosDeviceAttributeId_Object = MibTableColumn
qosDeviceAttributeId = _QosDeviceAttributeId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 2, 1, 1),
    _QosDeviceAttributeId_Type()
)
qosDeviceAttributeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosDeviceAttributeId.setStatus("current")
_QosDevicePepDomain_Type = DisplayString
_QosDevicePepDomain_Object = MibTableColumn
qosDevicePepDomain = _QosDevicePepDomain_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 2, 1, 2),
    _QosDevicePepDomain_Type()
)
qosDevicePepDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDevicePepDomain.setStatus("current")
_QosDevicePrimaryPdp_Type = IpAddress
_QosDevicePrimaryPdp_Object = MibTableColumn
qosDevicePrimaryPdp = _QosDevicePrimaryPdp_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 2, 1, 3),
    _QosDevicePrimaryPdp_Type()
)
qosDevicePrimaryPdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDevicePrimaryPdp.setStatus("current")
_QosDeviceSecondaryPdp_Type = IpAddress
_QosDeviceSecondaryPdp_Object = MibTableColumn
qosDeviceSecondaryPdp = _QosDeviceSecondaryPdp_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 2, 1, 4),
    _QosDeviceSecondaryPdp_Type()
)
qosDeviceSecondaryPdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDeviceSecondaryPdp.setStatus("current")
_QosDeviceMaxMessageSize_Type = Unsigned32
_QosDeviceMaxMessageSize_Object = MibTableColumn
qosDeviceMaxMessageSize = _QosDeviceMaxMessageSize_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 2, 1, 5),
    _QosDeviceMaxMessageSize_Type()
)
qosDeviceMaxMessageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDeviceMaxMessageSize.setStatus("current")


class _QosDeviceCapabilities_Type(Bits):
    """Custom type qosDeviceCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dscp", 3),
          ("ipPrecedence", 2),
          ("layer2Cos", 1),
          ("unspecified", 0))
    )

_QosDeviceCapabilities_Type.__name__ = "Bits"
_QosDeviceCapabilities_Object = MibTableColumn
qosDeviceCapabilities = _QosDeviceCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 2, 1, 6),
    _QosDeviceCapabilities_Type()
)
qosDeviceCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDeviceCapabilities.setStatus("current")
_QosInterfaceTypeTable_Object = MibTable
qosInterfaceTypeTable = _QosInterfaceTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    qosInterfaceTypeTable.setStatus("current")
_QosInterfaceTypeEntry_Object = MibTableRow
qosInterfaceTypeEntry = _QosInterfaceTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 3, 1)
)
qosInterfaceTypeEntry.setIndexNames(
    (0, "BDCOM-QOS-PIB-MIB", "qosInterfaceTypeId"),
)
if mibBuilder.loadTexts:
    qosInterfaceTypeEntry.setStatus("current")
_QosInterfaceTypeId_Type = PolicyInstanceId
_QosInterfaceTypeId_Object = MibTableColumn
qosInterfaceTypeId = _QosInterfaceTypeId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 3, 1, 1),
    _QosInterfaceTypeId_Type()
)
qosInterfaceTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosInterfaceTypeId.setStatus("current")
_QosInterfaceQueueType_Type = QosInterfaceQueueType
_QosInterfaceQueueType_Object = MibTableColumn
qosInterfaceQueueType = _QosInterfaceQueueType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 3, 1, 2),
    _QosInterfaceQueueType_Type()
)
qosInterfaceQueueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosInterfaceQueueType.setStatus("current")
_QosInterfaceTypeRoles_Type = RoleCombination
_QosInterfaceTypeRoles_Object = MibTableColumn
qosInterfaceTypeRoles = _QosInterfaceTypeRoles_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 3, 1, 3),
    _QosInterfaceTypeRoles_Type()
)
qosInterfaceTypeRoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosInterfaceTypeRoles.setStatus("current")
_QosInterfaceTypeCapabilities_Type = QosInterfaceTypeCapabilities
_QosInterfaceTypeCapabilities_Object = MibTableColumn
qosInterfaceTypeCapabilities = _QosInterfaceTypeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 2, 3, 1, 4),
    _QosInterfaceTypeCapabilities_Type()
)
qosInterfaceTypeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosInterfaceTypeCapabilities.setStatus("current")
_QosDomainConfig_ObjectIdentity = ObjectIdentity
qosDomainConfig = _QosDomainConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 3)
)
_QosDiffServMappingTable_Object = MibTable
qosDiffServMappingTable = _QosDiffServMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qosDiffServMappingTable.setStatus("current")
_QosDiffServMappingEntry_Object = MibTableRow
qosDiffServMappingEntry = _QosDiffServMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 3, 1, 1)
)
qosDiffServMappingEntry.setIndexNames(
    (0, "BDCOM-QOS-PIB-MIB", "qosDscp"),
)
if mibBuilder.loadTexts:
    qosDiffServMappingEntry.setStatus("current")
_QosDscp_Type = Dscp
_QosDscp_Object = MibTableColumn
qosDscp = _QosDscp_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 3, 1, 1, 1),
    _QosDscp_Type()
)
qosDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosDscp.setStatus("current")
_QosMarkedDscp_Type = Dscp
_QosMarkedDscp_Object = MibTableColumn
qosMarkedDscp = _QosMarkedDscp_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 3, 1, 1, 2),
    _QosMarkedDscp_Type()
)
qosMarkedDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMarkedDscp.setStatus("current")
_QosL2Cos_Type = QosLayer2Cos
_QosL2Cos_Object = MibTableColumn
qosL2Cos = _QosL2Cos_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 3, 1, 1, 3),
    _QosL2Cos_Type()
)
qosL2Cos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosL2Cos.setStatus("current")
_QosCosToDscpTable_Object = MibTable
qosCosToDscpTable = _QosCosToDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    qosCosToDscpTable.setStatus("current")
_QosCosToDscpEntry_Object = MibTableRow
qosCosToDscpEntry = _QosCosToDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 3, 2, 1)
)
qosCosToDscpEntry.setIndexNames(
    (0, "BDCOM-QOS-PIB-MIB", "qosCosToDscpCos"),
)
if mibBuilder.loadTexts:
    qosCosToDscpEntry.setStatus("current")
_QosCosToDscpCos_Type = QosLayer2Cos
_QosCosToDscpCos_Object = MibTableColumn
qosCosToDscpCos = _QosCosToDscpCos_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 3, 2, 1, 1),
    _QosCosToDscpCos_Type()
)
qosCosToDscpCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosCosToDscpCos.setStatus("current")
_QosCosToDscpDscp_Type = Dscp
_QosCosToDscpDscp_Object = MibTableColumn
qosCosToDscpDscp = _QosCosToDscpDscp_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 3, 2, 1, 2),
    _QosCosToDscpDscp_Type()
)
qosCosToDscpDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCosToDscpDscp.setStatus("current")
_QosUnmatchedPolicy_ObjectIdentity = ObjectIdentity
qosUnmatchedPolicy = _QosUnmatchedPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 4)
)
_QosUnmatchedPolicyTable_Object = MibTable
qosUnmatchedPolicyTable = _QosUnmatchedPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    qosUnmatchedPolicyTable.setStatus("current")
_QosUnmatchedPolicyEntry_Object = MibTableRow
qosUnmatchedPolicyEntry = _QosUnmatchedPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 4, 1, 1)
)
qosUnmatchedPolicyEntry.setIndexNames(
    (0, "BDCOM-QOS-PIB-MIB", "qosUnmatchedPolicyId"),
)
if mibBuilder.loadTexts:
    qosUnmatchedPolicyEntry.setStatus("current")
_QosUnmatchedPolicyId_Type = PolicyInstanceId
_QosUnmatchedPolicyId_Object = MibTableColumn
qosUnmatchedPolicyId = _QosUnmatchedPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 4, 1, 1, 1),
    _QosUnmatchedPolicyId_Type()
)
qosUnmatchedPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosUnmatchedPolicyId.setStatus("current")
_QosUnmatchedPolicyRole_Type = RoleCombination
_QosUnmatchedPolicyRole_Object = MibTableColumn
qosUnmatchedPolicyRole = _QosUnmatchedPolicyRole_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 4, 1, 1, 2),
    _QosUnmatchedPolicyRole_Type()
)
qosUnmatchedPolicyRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosUnmatchedPolicyRole.setStatus("current")


class _QosUnmatchedPolicyDirection_Type(Integer32):
    """Custom type qosUnmatchedPolicyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in", 0),
          ("out", 1))
    )


_QosUnmatchedPolicyDirection_Type.__name__ = "Integer32"
_QosUnmatchedPolicyDirection_Object = MibTableColumn
qosUnmatchedPolicyDirection = _QosUnmatchedPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 4, 1, 1, 3),
    _QosUnmatchedPolicyDirection_Type()
)
qosUnmatchedPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosUnmatchedPolicyDirection.setStatus("current")
_QosUnmatchedPolicyDscp_Type = Dscp
_QosUnmatchedPolicyDscp_Object = MibTableColumn
qosUnmatchedPolicyDscp = _QosUnmatchedPolicyDscp_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 4, 1, 1, 4),
    _QosUnmatchedPolicyDscp_Type()
)
qosUnmatchedPolicyDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosUnmatchedPolicyDscp.setStatus("current")
_QosUnmatchedPolicyDscpTrusted_Type = TruthValue
_QosUnmatchedPolicyDscpTrusted_Object = MibTableColumn
qosUnmatchedPolicyDscpTrusted = _QosUnmatchedPolicyDscpTrusted_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 4, 1, 1, 5),
    _QosUnmatchedPolicyDscpTrusted_Type()
)
qosUnmatchedPolicyDscpTrusted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosUnmatchedPolicyDscpTrusted.setStatus("current")
_QosUnmatchPolMicroFlowPolicerId_Type = PolicyInstanceId
_QosUnmatchPolMicroFlowPolicerId_Object = MibTableColumn
qosUnmatchPolMicroFlowPolicerId = _QosUnmatchPolMicroFlowPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 4, 1, 1, 6),
    _QosUnmatchPolMicroFlowPolicerId_Type()
)
qosUnmatchPolMicroFlowPolicerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosUnmatchPolMicroFlowPolicerId.setStatus("current")
_QosUnmatchedPolicyAggregateId_Type = PolicyInstanceId
_QosUnmatchedPolicyAggregateId_Object = MibTableColumn
qosUnmatchedPolicyAggregateId = _QosUnmatchedPolicyAggregateId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 4, 1, 1, 7),
    _QosUnmatchedPolicyAggregateId_Type()
)
qosUnmatchedPolicyAggregateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosUnmatchedPolicyAggregateId.setStatus("current")
_QosPolicer_ObjectIdentity = ObjectIdentity
qosPolicer = _QosPolicer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 5)
)
_QosPolicerTable_Object = MibTable
qosPolicerTable = _QosPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    qosPolicerTable.setStatus("current")
_QosPolicerEntry_Object = MibTableRow
qosPolicerEntry = _QosPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 5, 1, 1)
)
qosPolicerEntry.setIndexNames(
    (0, "BDCOM-QOS-PIB-MIB", "qosPolicerId"),
)
if mibBuilder.loadTexts:
    qosPolicerEntry.setStatus("current")
_QosPolicerId_Type = PolicyInstanceId
_QosPolicerId_Object = MibTableColumn
qosPolicerId = _QosPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 5, 1, 1, 1),
    _QosPolicerId_Type()
)
qosPolicerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosPolicerId.setStatus("current")
_QosPolicerRate_Type = Unsigned64
_QosPolicerRate_Object = MibTableColumn
qosPolicerRate = _QosPolicerRate_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 5, 1, 1, 2),
    _QosPolicerRate_Type()
)
qosPolicerRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPolicerRate.setStatus("current")
_QosPolicerNormalBurst_Type = Unsigned32
_QosPolicerNormalBurst_Object = MibTableColumn
qosPolicerNormalBurst = _QosPolicerNormalBurst_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 5, 1, 1, 3),
    _QosPolicerNormalBurst_Type()
)
qosPolicerNormalBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPolicerNormalBurst.setStatus("current")
_QosPolicerExcessBurst_Type = Unsigned32
_QosPolicerExcessBurst_Object = MibTableColumn
qosPolicerExcessBurst = _QosPolicerExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 5, 1, 1, 4),
    _QosPolicerExcessBurst_Type()
)
qosPolicerExcessBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPolicerExcessBurst.setStatus("current")


class _QosPolicerAction_Type(Integer32):
    """Custom type qosPolicerAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 0),
          ("mark", 1),
          ("shape", 2))
    )


_QosPolicerAction_Type.__name__ = "Integer32"
_QosPolicerAction_Object = MibTableColumn
qosPolicerAction = _QosPolicerAction_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 5, 1, 1, 5),
    _QosPolicerAction_Type()
)
qosPolicerAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPolicerAction.setStatus("current")
_QosAggregateTable_Object = MibTable
qosAggregateTable = _QosAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    qosAggregateTable.setStatus("current")
_QosAggregateEntry_Object = MibTableRow
qosAggregateEntry = _QosAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 5, 2, 1)
)
qosAggregateEntry.setIndexNames(
    (0, "BDCOM-QOS-PIB-MIB", "qosAggregateId"),
)
if mibBuilder.loadTexts:
    qosAggregateEntry.setStatus("current")
_QosAggregateId_Type = PolicyInstanceId
_QosAggregateId_Object = MibTableColumn
qosAggregateId = _QosAggregateId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 5, 2, 1, 1),
    _QosAggregateId_Type()
)
qosAggregateId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosAggregateId.setStatus("current")
_QosAggregatePolicerId_Type = PolicyInstanceId
_QosAggregatePolicerId_Object = MibTableColumn
qosAggregatePolicerId = _QosAggregatePolicerId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 5, 2, 1, 2),
    _QosAggregatePolicerId_Type()
)
qosAggregatePolicerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosAggregatePolicerId.setStatus("current")
_QosMacQos_ObjectIdentity = ObjectIdentity
qosMacQos = _QosMacQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 6)
)
_QosMacClassificationTable_Object = MibTable
qosMacClassificationTable = _QosMacClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    qosMacClassificationTable.setStatus("current")
_QosMacClassificationEntry_Object = MibTableRow
qosMacClassificationEntry = _QosMacClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 6, 1, 1)
)
qosMacClassificationEntry.setIndexNames(
    (0, "BDCOM-QOS-PIB-MIB", "qosMacClassificationId"),
)
if mibBuilder.loadTexts:
    qosMacClassificationEntry.setStatus("current")
_QosMacClassificationId_Type = PolicyInstanceId
_QosMacClassificationId_Object = MibTableColumn
qosMacClassificationId = _QosMacClassificationId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 6, 1, 1, 1),
    _QosMacClassificationId_Type()
)
qosMacClassificationId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosMacClassificationId.setStatus("current")


class _QosDstMacVlan_Type(Integer32):
    """Custom type qosDstMacVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_QosDstMacVlan_Type.__name__ = "Integer32"
_QosDstMacVlan_Object = MibTableColumn
qosDstMacVlan = _QosDstMacVlan_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 6, 1, 1, 2),
    _QosDstMacVlan_Type()
)
qosDstMacVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDstMacVlan.setStatus("current")
_QosDstMacAddress_Type = MacAddress
_QosDstMacAddress_Object = MibTableColumn
qosDstMacAddress = _QosDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 6, 1, 1, 3),
    _QosDstMacAddress_Type()
)
qosDstMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDstMacAddress.setStatus("current")
_QosDstMacCos_Type = QosLayer2Cos
_QosDstMacCos_Object = MibTableColumn
qosDstMacCos = _QosDstMacCos_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 6, 1, 1, 4),
    _QosDstMacCos_Type()
)
qosDstMacCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDstMacCos.setStatus("current")
_QosIpQos_ObjectIdentity = ObjectIdentity
qosIpQos = _QosIpQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7)
)
_QosIpAceTable_Object = MibTable
qosIpAceTable = _QosIpAceTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    qosIpAceTable.setStatus("current")
_QosIpAceEntry_Object = MibTableRow
qosIpAceEntry = _QosIpAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 1, 1)
)
qosIpAceEntry.setIndexNames(
    (0, "BDCOM-QOS-PIB-MIB", "qosIpAceId"),
)
if mibBuilder.loadTexts:
    qosIpAceEntry.setStatus("current")
_QosIpAceId_Type = PolicyInstanceId
_QosIpAceId_Object = MibTableColumn
qosIpAceId = _QosIpAceId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 1, 1, 1),
    _QosIpAceId_Type()
)
qosIpAceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIpAceId.setStatus("current")
_QosIpAceDstAddr_Type = IpAddress
_QosIpAceDstAddr_Object = MibTableColumn
qosIpAceDstAddr = _QosIpAceDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 1, 1, 2),
    _QosIpAceDstAddr_Type()
)
qosIpAceDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAceDstAddr.setStatus("current")
_QosIpAceDstAddrMask_Type = IpAddress
_QosIpAceDstAddrMask_Object = MibTableColumn
qosIpAceDstAddrMask = _QosIpAceDstAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 1, 1, 3),
    _QosIpAceDstAddrMask_Type()
)
qosIpAceDstAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAceDstAddrMask.setStatus("current")
_QosIpAceSrcAddr_Type = IpAddress
_QosIpAceSrcAddr_Object = MibTableColumn
qosIpAceSrcAddr = _QosIpAceSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 1, 1, 4),
    _QosIpAceSrcAddr_Type()
)
qosIpAceSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAceSrcAddr.setStatus("current")
_QosIpAceSrcAddrMask_Type = IpAddress
_QosIpAceSrcAddrMask_Object = MibTableColumn
qosIpAceSrcAddrMask = _QosIpAceSrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 1, 1, 5),
    _QosIpAceSrcAddrMask_Type()
)
qosIpAceSrcAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAceSrcAddrMask.setStatus("current")
_QosIpAceDscpMin_Type = Dscp
_QosIpAceDscpMin_Object = MibTableColumn
qosIpAceDscpMin = _QosIpAceDscpMin_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 1, 1, 6),
    _QosIpAceDscpMin_Type()
)
qosIpAceDscpMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAceDscpMin.setStatus("current")
_QosIpAceDscpMax_Type = Dscp
_QosIpAceDscpMax_Object = MibTableColumn
qosIpAceDscpMax = _QosIpAceDscpMax_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 1, 1, 7),
    _QosIpAceDscpMax_Type()
)
qosIpAceDscpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAceDscpMax.setStatus("current")


class _QosIpAceProtocol_Type(Integer32):
    """Custom type qosIpAceProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QosIpAceProtocol_Type.__name__ = "Integer32"
_QosIpAceProtocol_Object = MibTableColumn
qosIpAceProtocol = _QosIpAceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 1, 1, 8),
    _QosIpAceProtocol_Type()
)
qosIpAceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAceProtocol.setStatus("current")


class _QosIpAceDstL4PortMin_Type(Integer32):
    """Custom type qosIpAceDstL4PortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QosIpAceDstL4PortMin_Type.__name__ = "Integer32"
_QosIpAceDstL4PortMin_Object = MibTableColumn
qosIpAceDstL4PortMin = _QosIpAceDstL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 1, 1, 9),
    _QosIpAceDstL4PortMin_Type()
)
qosIpAceDstL4PortMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAceDstL4PortMin.setStatus("current")


class _QosIpAceDstL4PortMax_Type(Integer32):
    """Custom type qosIpAceDstL4PortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QosIpAceDstL4PortMax_Type.__name__ = "Integer32"
_QosIpAceDstL4PortMax_Object = MibTableColumn
qosIpAceDstL4PortMax = _QosIpAceDstL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 1, 1, 10),
    _QosIpAceDstL4PortMax_Type()
)
qosIpAceDstL4PortMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAceDstL4PortMax.setStatus("current")


class _QosIpAceSrcL4PortMin_Type(Integer32):
    """Custom type qosIpAceSrcL4PortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QosIpAceSrcL4PortMin_Type.__name__ = "Integer32"
_QosIpAceSrcL4PortMin_Object = MibTableColumn
qosIpAceSrcL4PortMin = _QosIpAceSrcL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 1, 1, 11),
    _QosIpAceSrcL4PortMin_Type()
)
qosIpAceSrcL4PortMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAceSrcL4PortMin.setStatus("current")


class _QosIpAceSrcL4PortMax_Type(Integer32):
    """Custom type qosIpAceSrcL4PortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QosIpAceSrcL4PortMax_Type.__name__ = "Integer32"
_QosIpAceSrcL4PortMax_Object = MibTableColumn
qosIpAceSrcL4PortMax = _QosIpAceSrcL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 1, 1, 12),
    _QosIpAceSrcL4PortMax_Type()
)
qosIpAceSrcL4PortMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAceSrcL4PortMax.setStatus("current")
_QosIpAcePermit_Type = TruthValue
_QosIpAcePermit_Object = MibTableColumn
qosIpAcePermit = _QosIpAcePermit_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 1, 1, 13),
    _QosIpAcePermit_Type()
)
qosIpAcePermit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAcePermit.setStatus("current")
_QosIpAclDefinitionTable_Object = MibTable
qosIpAclDefinitionTable = _QosIpAclDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    qosIpAclDefinitionTable.setStatus("current")
_QosIpAclDefinitionEntry_Object = MibTableRow
qosIpAclDefinitionEntry = _QosIpAclDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 2, 1)
)
qosIpAclDefinitionEntry.setIndexNames(
    (0, "BDCOM-QOS-PIB-MIB", "qosIpAclDefinitionId"),
)
if mibBuilder.loadTexts:
    qosIpAclDefinitionEntry.setStatus("current")
_QosIpAclDefinitionId_Type = PolicyInstanceId
_QosIpAclDefinitionId_Object = MibTableColumn
qosIpAclDefinitionId = _QosIpAclDefinitionId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 2, 1, 1),
    _QosIpAclDefinitionId_Type()
)
qosIpAclDefinitionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIpAclDefinitionId.setStatus("current")
_QosIpAclId_Type = PolicyInstanceId
_QosIpAclId_Object = MibTableColumn
qosIpAclId = _QosIpAclId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 2, 1, 2),
    _QosIpAclId_Type()
)
qosIpAclId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAclId.setStatus("current")
_QosIpAceOrder_Type = Unsigned32
_QosIpAceOrder_Object = MibTableColumn
qosIpAceOrder = _QosIpAceOrder_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 2, 1, 3),
    _QosIpAceOrder_Type()
)
qosIpAceOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAceOrder.setStatus("current")
_QosIpAclDefAceId_Type = PolicyInstanceId
_QosIpAclDefAceId_Object = MibTableColumn
qosIpAclDefAceId = _QosIpAclDefAceId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 2, 1, 4),
    _QosIpAclDefAceId_Type()
)
qosIpAclDefAceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAclDefAceId.setStatus("current")
_QosIpAclActionTable_Object = MibTable
qosIpAclActionTable = _QosIpAclActionTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 3)
)
if mibBuilder.loadTexts:
    qosIpAclActionTable.setStatus("current")
_QosIpAclActionEntry_Object = MibTableRow
qosIpAclActionEntry = _QosIpAclActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 3, 1)
)
qosIpAclActionEntry.setIndexNames(
    (0, "BDCOM-QOS-PIB-MIB", "qosIpAclActionId"),
)
if mibBuilder.loadTexts:
    qosIpAclActionEntry.setStatus("current")
_QosIpAclActionId_Type = PolicyInstanceId
_QosIpAclActionId_Object = MibTableColumn
qosIpAclActionId = _QosIpAclActionId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 3, 1, 1),
    _QosIpAclActionId_Type()
)
qosIpAclActionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIpAclActionId.setStatus("current")
_QosIpAclActAclId_Type = PolicyInstanceId
_QosIpAclActAclId_Object = MibTableColumn
qosIpAclActAclId = _QosIpAclActAclId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 3, 1, 2),
    _QosIpAclActAclId_Type()
)
qosIpAclActAclId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAclActAclId.setStatus("current")
_QosIpAclInterfaceRoles_Type = RoleCombination
_QosIpAclInterfaceRoles_Object = MibTableColumn
qosIpAclInterfaceRoles = _QosIpAclInterfaceRoles_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 3, 1, 3),
    _QosIpAclInterfaceRoles_Type()
)
qosIpAclInterfaceRoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAclInterfaceRoles.setStatus("current")


class _QosIpAclInterfaceDirection_Type(Integer32):
    """Custom type qosIpAclInterfaceDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in", 0),
          ("out", 1))
    )


_QosIpAclInterfaceDirection_Type.__name__ = "Integer32"
_QosIpAclInterfaceDirection_Object = MibTableColumn
qosIpAclInterfaceDirection = _QosIpAclInterfaceDirection_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 3, 1, 4),
    _QosIpAclInterfaceDirection_Type()
)
qosIpAclInterfaceDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAclInterfaceDirection.setStatus("current")
_QosIpAclOrder_Type = Unsigned32
_QosIpAclOrder_Object = MibTableColumn
qosIpAclOrder = _QosIpAclOrder_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 3, 1, 5),
    _QosIpAclOrder_Type()
)
qosIpAclOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAclOrder.setStatus("current")
_QosIpAclDscp_Type = Dscp
_QosIpAclDscp_Object = MibTableColumn
qosIpAclDscp = _QosIpAclDscp_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 3, 1, 6),
    _QosIpAclDscp_Type()
)
qosIpAclDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAclDscp.setStatus("current")
_QosIpAclDscpTrusted_Type = TruthValue
_QosIpAclDscpTrusted_Object = MibTableColumn
qosIpAclDscpTrusted = _QosIpAclDscpTrusted_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 3, 1, 7),
    _QosIpAclDscpTrusted_Type()
)
qosIpAclDscpTrusted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAclDscpTrusted.setStatus("current")
_QosIpAclMicroFlowPolicerId_Type = PolicyInstanceId
_QosIpAclMicroFlowPolicerId_Object = MibTableColumn
qosIpAclMicroFlowPolicerId = _QosIpAclMicroFlowPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 3, 1, 8),
    _QosIpAclMicroFlowPolicerId_Type()
)
qosIpAclMicroFlowPolicerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAclMicroFlowPolicerId.setStatus("current")
_QosIpAclAggregateId_Type = PolicyInstanceId
_QosIpAclAggregateId_Object = MibTableColumn
qosIpAclAggregateId = _QosIpAclAggregateId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 7, 3, 1, 9),
    _QosIpAclAggregateId_Type()
)
qosIpAclAggregateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIpAclAggregateId.setStatus("current")
_QosIfParameters_ObjectIdentity = ObjectIdentity
qosIfParameters = _QosIfParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8)
)
_QosIfSchedulingPreferencesTable_Object = MibTable
qosIfSchedulingPreferencesTable = _QosIfSchedulingPreferencesTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    qosIfSchedulingPreferencesTable.setStatus("current")
_QosIfSchedulingPreferenceEntry_Object = MibTableRow
qosIfSchedulingPreferenceEntry = _QosIfSchedulingPreferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 1, 1)
)
qosIfSchedulingPreferenceEntry.setIndexNames(
    (0, "BDCOM-QOS-PIB-MIB", "qosIfSchedulingPreferenceId"),
)
if mibBuilder.loadTexts:
    qosIfSchedulingPreferenceEntry.setStatus("current")
_QosIfSchedulingPreferenceId_Type = PolicyInstanceId
_QosIfSchedulingPreferenceId_Object = MibTableColumn
qosIfSchedulingPreferenceId = _QosIfSchedulingPreferenceId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 1, 1, 1),
    _QosIfSchedulingPreferenceId_Type()
)
qosIfSchedulingPreferenceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIfSchedulingPreferenceId.setStatus("current")
_QosIfSchedulingRoles_Type = RoleCombination
_QosIfSchedulingRoles_Object = MibTableColumn
qosIfSchedulingRoles = _QosIfSchedulingRoles_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 1, 1, 2),
    _QosIfSchedulingRoles_Type()
)
qosIfSchedulingRoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfSchedulingRoles.setStatus("current")


class _QosIfSchedulingPreference_Type(Integer32):
    """Custom type qosIfSchedulingPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QosIfSchedulingPreference_Type.__name__ = "Integer32"
_QosIfSchedulingPreference_Object = MibTableColumn
qosIfSchedulingPreference = _QosIfSchedulingPreference_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 1, 1, 3),
    _QosIfSchedulingPreference_Type()
)
qosIfSchedulingPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfSchedulingPreference.setStatus("current")


class _QosIfSchedulingDiscipline_Type(Integer32):
    """Custom type qosIfSchedulingDiscipline based on Integer32"""
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
        *(("classBasedWFQ", 5),
          ("customQueueing", 3),
          ("fifo", 6),
          ("pqCbwfq", 8),
          ("pqWrr", 7),
          ("priorityQueueing", 4),
          ("weightedFairQueueing", 1),
          ("weightedRoundRobin", 2))
    )


_QosIfSchedulingDiscipline_Type.__name__ = "Integer32"
_QosIfSchedulingDiscipline_Object = MibTableColumn
qosIfSchedulingDiscipline = _QosIfSchedulingDiscipline_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 1, 1, 4),
    _QosIfSchedulingDiscipline_Type()
)
qosIfSchedulingDiscipline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfSchedulingDiscipline.setStatus("current")
_QosIfSchedulingQueueType_Type = QosInterfaceQueueType
_QosIfSchedulingQueueType_Object = MibTableColumn
qosIfSchedulingQueueType = _QosIfSchedulingQueueType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 1, 1, 5),
    _QosIfSchedulingQueueType_Type()
)
qosIfSchedulingQueueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfSchedulingQueueType.setStatus("current")
_QosIfDropPreferenceTable_Object = MibTable
qosIfDropPreferenceTable = _QosIfDropPreferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    qosIfDropPreferenceTable.setStatus("current")
_QosIfDropPreferenceEntry_Object = MibTableRow
qosIfDropPreferenceEntry = _QosIfDropPreferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 2, 1)
)
qosIfDropPreferenceEntry.setIndexNames(
    (0, "BDCOM-QOS-PIB-MIB", "qosIfDropPreferenceId"),
)
if mibBuilder.loadTexts:
    qosIfDropPreferenceEntry.setStatus("current")
_QosIfDropPreferenceId_Type = PolicyInstanceId
_QosIfDropPreferenceId_Object = MibTableColumn
qosIfDropPreferenceId = _QosIfDropPreferenceId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 2, 1, 1),
    _QosIfDropPreferenceId_Type()
)
qosIfDropPreferenceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIfDropPreferenceId.setStatus("current")
_QosIfDropRoles_Type = RoleCombination
_QosIfDropRoles_Object = MibTableColumn
qosIfDropRoles = _QosIfDropRoles_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 2, 1, 2),
    _QosIfDropRoles_Type()
)
qosIfDropRoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfDropRoles.setStatus("current")


class _QosIfDropPreference_Type(Integer32):
    """Custom type qosIfDropPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QosIfDropPreference_Type.__name__ = "Integer32"
_QosIfDropPreference_Object = MibTableColumn
qosIfDropPreference = _QosIfDropPreference_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 2, 1, 3),
    _QosIfDropPreference_Type()
)
qosIfDropPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfDropPreference.setStatus("current")


class _QosIfDropDiscipline_Type(Integer32):
    """Custom type qosIfDropDiscipline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qosIfDropTailDrop", 2),
          ("qosIfDropWRED", 1))
    )


_QosIfDropDiscipline_Type.__name__ = "Integer32"
_QosIfDropDiscipline_Object = MibTableColumn
qosIfDropDiscipline = _QosIfDropDiscipline_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 2, 1, 4),
    _QosIfDropDiscipline_Type()
)
qosIfDropDiscipline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfDropDiscipline.setStatus("current")
_QosIfDscpAssignmentTable_Object = MibTable
qosIfDscpAssignmentTable = _QosIfDscpAssignmentTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 3)
)
if mibBuilder.loadTexts:
    qosIfDscpAssignmentTable.setStatus("current")
_QosIfDscpAssignmentEntry_Object = MibTableRow
qosIfDscpAssignmentEntry = _QosIfDscpAssignmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 3, 1)
)
qosIfDscpAssignmentEntry.setIndexNames(
    (0, "BDCOM-QOS-PIB-MIB", "qosIfDscpAssignmentId"),
)
if mibBuilder.loadTexts:
    qosIfDscpAssignmentEntry.setStatus("current")
_QosIfDscpAssignmentId_Type = PolicyInstanceId
_QosIfDscpAssignmentId_Object = MibTableColumn
qosIfDscpAssignmentId = _QosIfDscpAssignmentId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 3, 1, 1),
    _QosIfDscpAssignmentId_Type()
)
qosIfDscpAssignmentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIfDscpAssignmentId.setStatus("current")
_QosIfDscpRoles_Type = RoleCombination
_QosIfDscpRoles_Object = MibTableColumn
qosIfDscpRoles = _QosIfDscpRoles_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 3, 1, 2),
    _QosIfDscpRoles_Type()
)
qosIfDscpRoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfDscpRoles.setStatus("current")
_QosIfQueueType_Type = QosInterfaceQueueType
_QosIfQueueType_Object = MibTableColumn
qosIfQueueType = _QosIfQueueType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 3, 1, 3),
    _QosIfQueueType_Type()
)
qosIfQueueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfQueueType.setStatus("current")
_QosIfDscp_Type = Dscp
_QosIfDscp_Object = MibTableColumn
qosIfDscp = _QosIfDscp_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 3, 1, 4),
    _QosIfDscp_Type()
)
qosIfDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfDscp.setStatus("current")


class _QosIfQueue_Type(Integer32):
    """Custom type qosIfQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_QosIfQueue_Type.__name__ = "Integer32"
_QosIfQueue_Object = MibTableColumn
qosIfQueue = _QosIfQueue_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 3, 1, 5),
    _QosIfQueue_Type()
)
qosIfQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfQueue.setStatus("current")


class _QosIfThresholdSet_Type(Integer32):
    """Custom type qosIfThresholdSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_QosIfThresholdSet_Type.__name__ = "Integer32"
_QosIfThresholdSet_Object = MibTableColumn
qosIfThresholdSet = _QosIfThresholdSet_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 3, 1, 6),
    _QosIfThresholdSet_Type()
)
qosIfThresholdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfThresholdSet.setStatus("current")
_QosIfRedTable_Object = MibTable
qosIfRedTable = _QosIfRedTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 4)
)
if mibBuilder.loadTexts:
    qosIfRedTable.setStatus("current")
_QosIfRedEntry_Object = MibTableRow
qosIfRedEntry = _QosIfRedEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 4, 1)
)
qosIfRedEntry.setIndexNames(
    (0, "BDCOM-QOS-PIB-MIB", "qosIfRedId"),
)
if mibBuilder.loadTexts:
    qosIfRedEntry.setStatus("current")
_QosIfRedId_Type = PolicyInstanceId
_QosIfRedId_Object = MibTableColumn
qosIfRedId = _QosIfRedId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 4, 1, 1),
    _QosIfRedId_Type()
)
qosIfRedId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIfRedId.setStatus("current")
_QosIfRedRoles_Type = RoleCombination
_QosIfRedRoles_Object = MibTableColumn
qosIfRedRoles = _QosIfRedRoles_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 4, 1, 2),
    _QosIfRedRoles_Type()
)
qosIfRedRoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfRedRoles.setStatus("current")
_QosIfRedNumThresholdSets_Type = ThresholdSetRange
_QosIfRedNumThresholdSets_Object = MibTableColumn
qosIfRedNumThresholdSets = _QosIfRedNumThresholdSets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 4, 1, 3),
    _QosIfRedNumThresholdSets_Type()
)
qosIfRedNumThresholdSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfRedNumThresholdSets.setStatus("current")


class _QosIfRedThresholdSet_Type(Integer32):
    """Custom type qosIfRedThresholdSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_QosIfRedThresholdSet_Type.__name__ = "Integer32"
_QosIfRedThresholdSet_Object = MibTableColumn
qosIfRedThresholdSet = _QosIfRedThresholdSet_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 4, 1, 4),
    _QosIfRedThresholdSet_Type()
)
qosIfRedThresholdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfRedThresholdSet.setStatus("current")
_QosIfRedThresholdSetLower_Type = Percent
_QosIfRedThresholdSetLower_Object = MibTableColumn
qosIfRedThresholdSetLower = _QosIfRedThresholdSetLower_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 4, 1, 5),
    _QosIfRedThresholdSetLower_Type()
)
qosIfRedThresholdSetLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfRedThresholdSetLower.setStatus("current")
_QosIfRedThresholdSetUpper_Type = Percent
_QosIfRedThresholdSetUpper_Object = MibTableColumn
qosIfRedThresholdSetUpper = _QosIfRedThresholdSetUpper_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 4, 1, 6),
    _QosIfRedThresholdSetUpper_Type()
)
qosIfRedThresholdSetUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfRedThresholdSetUpper.setStatus("current")
_QosIfTailDropTable_Object = MibTable
qosIfTailDropTable = _QosIfTailDropTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 5)
)
if mibBuilder.loadTexts:
    qosIfTailDropTable.setStatus("current")
_QosIfTailDropEntry_Object = MibTableRow
qosIfTailDropEntry = _QosIfTailDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 5, 1)
)
qosIfTailDropEntry.setIndexNames(
    (0, "BDCOM-QOS-PIB-MIB", "qosIfTailDropId"),
)
if mibBuilder.loadTexts:
    qosIfTailDropEntry.setStatus("current")
_QosIfTailDropId_Type = PolicyInstanceId
_QosIfTailDropId_Object = MibTableColumn
qosIfTailDropId = _QosIfTailDropId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 5, 1, 1),
    _QosIfTailDropId_Type()
)
qosIfTailDropId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIfTailDropId.setStatus("current")
_QosIfTailDropRoles_Type = RoleCombination
_QosIfTailDropRoles_Object = MibTableColumn
qosIfTailDropRoles = _QosIfTailDropRoles_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 5, 1, 2),
    _QosIfTailDropRoles_Type()
)
qosIfTailDropRoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfTailDropRoles.setStatus("current")
_QosIfTailDropNumThresholdSets_Type = ThresholdSetRange
_QosIfTailDropNumThresholdSets_Object = MibTableColumn
qosIfTailDropNumThresholdSets = _QosIfTailDropNumThresholdSets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 5, 1, 3),
    _QosIfTailDropNumThresholdSets_Type()
)
qosIfTailDropNumThresholdSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfTailDropNumThresholdSets.setStatus("current")


class _QosIfTailDropThresholdSet_Type(Integer32):
    """Custom type qosIfTailDropThresholdSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_QosIfTailDropThresholdSet_Type.__name__ = "Integer32"
_QosIfTailDropThresholdSet_Object = MibTableColumn
qosIfTailDropThresholdSet = _QosIfTailDropThresholdSet_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 5, 1, 4),
    _QosIfTailDropThresholdSet_Type()
)
qosIfTailDropThresholdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfTailDropThresholdSet.setStatus("current")
_QosIfTailDropThresholdSetValue_Type = Percent
_QosIfTailDropThresholdSetValue_Object = MibTableColumn
qosIfTailDropThresholdSetValue = _QosIfTailDropThresholdSetValue_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 5, 1, 5),
    _QosIfTailDropThresholdSetValue_Type()
)
qosIfTailDropThresholdSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfTailDropThresholdSetValue.setStatus("current")
_QosIfWeightsTable_Object = MibTable
qosIfWeightsTable = _QosIfWeightsTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 6)
)
if mibBuilder.loadTexts:
    qosIfWeightsTable.setStatus("current")
_QosIfWeightsEntry_Object = MibTableRow
qosIfWeightsEntry = _QosIfWeightsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 6, 1)
)
qosIfWeightsEntry.setIndexNames(
    (0, "BDCOM-QOS-PIB-MIB", "qosIfWeightsId"),
)
if mibBuilder.loadTexts:
    qosIfWeightsEntry.setStatus("current")
_QosIfWeightsId_Type = PolicyInstanceId
_QosIfWeightsId_Object = MibTableColumn
qosIfWeightsId = _QosIfWeightsId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 6, 1, 1),
    _QosIfWeightsId_Type()
)
qosIfWeightsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIfWeightsId.setStatus("current")
_QosIfWeightsRoles_Type = RoleCombination
_QosIfWeightsRoles_Object = MibTableColumn
qosIfWeightsRoles = _QosIfWeightsRoles_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 6, 1, 2),
    _QosIfWeightsRoles_Type()
)
qosIfWeightsRoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfWeightsRoles.setStatus("current")
_QosIfWeightsNumQueues_Type = QueueRange
_QosIfWeightsNumQueues_Object = MibTableColumn
qosIfWeightsNumQueues = _QosIfWeightsNumQueues_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 6, 1, 3),
    _QosIfWeightsNumQueues_Type()
)
qosIfWeightsNumQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfWeightsNumQueues.setStatus("current")


class _QosIfWeightsQueue_Type(Integer32):
    """Custom type qosIfWeightsQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_QosIfWeightsQueue_Type.__name__ = "Integer32"
_QosIfWeightsQueue_Object = MibTableColumn
qosIfWeightsQueue = _QosIfWeightsQueue_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 6, 1, 4),
    _QosIfWeightsQueue_Type()
)
qosIfWeightsQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfWeightsQueue.setStatus("current")
_QosIfWeightsDrainSize_Type = Unsigned32
_QosIfWeightsDrainSize_Object = MibTableColumn
qosIfWeightsDrainSize = _QosIfWeightsDrainSize_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 6, 1, 5),
    _QosIfWeightsDrainSize_Type()
)
qosIfWeightsDrainSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfWeightsDrainSize.setStatus("current")
_QosIfWeightsQueueSize_Type = Unsigned32
_QosIfWeightsQueueSize_Object = MibTableColumn
qosIfWeightsQueueSize = _QosIfWeightsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 8, 6, 1, 6),
    _QosIfWeightsQueueSize_Type()
)
qosIfWeightsQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfWeightsQueueSize.setStatus("current")

# Managed Objects groups

qosDevicePibIncarnationTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2, 1)
)
qosDevicePibIncarnationTableGroup.setObjects(
      *(("BDCOM-QOS-PIB-MIB", "qosDevicePdpName"),
        ("BDCOM-QOS-PIB-MIB", "qosDevicePibIncarnation"),
        ("BDCOM-QOS-PIB-MIB", "qosDevicePibTtl"))
)
if mibBuilder.loadTexts:
    qosDevicePibIncarnationTableGroup.setStatus("current")

qosDeviceAttributeTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2, 2)
)
qosDeviceAttributeTableGroup.setObjects(
      *(("BDCOM-QOS-PIB-MIB", "qosDevicePepDomain"),
        ("BDCOM-QOS-PIB-MIB", "qosDevicePrimaryPdp"),
        ("BDCOM-QOS-PIB-MIB", "qosDeviceSecondaryPdp"),
        ("BDCOM-QOS-PIB-MIB", "qosDeviceMaxMessageSize"),
        ("BDCOM-QOS-PIB-MIB", "qosDeviceCapabilities"))
)
if mibBuilder.loadTexts:
    qosDeviceAttributeTableGroup.setStatus("current")

qosInterfaceTypeTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2, 3)
)
qosInterfaceTypeTableGroup.setObjects(
      *(("BDCOM-QOS-PIB-MIB", "qosInterfaceQueueType"),
        ("BDCOM-QOS-PIB-MIB", "qosInterfaceTypeRoles"),
        ("BDCOM-QOS-PIB-MIB", "qosInterfaceTypeCapabilities"))
)
if mibBuilder.loadTexts:
    qosInterfaceTypeTableGroup.setStatus("current")

qosDiffServMappingTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2, 4)
)
qosDiffServMappingTableGroup.setObjects(
      *(("BDCOM-QOS-PIB-MIB", "qosMarkedDscp"),
        ("BDCOM-QOS-PIB-MIB", "qosL2Cos"))
)
if mibBuilder.loadTexts:
    qosDiffServMappingTableGroup.setStatus("current")

qosCosToDscpTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2, 5)
)
qosCosToDscpTableGroup.setObjects(
    ("BDCOM-QOS-PIB-MIB", "qosCosToDscpDscp")
)
if mibBuilder.loadTexts:
    qosCosToDscpTableGroup.setStatus("current")

qosUnmatchedPolicyTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2, 6)
)
qosUnmatchedPolicyTableGroup.setObjects(
      *(("BDCOM-QOS-PIB-MIB", "qosUnmatchedPolicyRole"),
        ("BDCOM-QOS-PIB-MIB", "qosUnmatchedPolicyDirection"),
        ("BDCOM-QOS-PIB-MIB", "qosUnmatchedPolicyDscp"),
        ("BDCOM-QOS-PIB-MIB", "qosUnmatchedPolicyDscpTrusted"),
        ("BDCOM-QOS-PIB-MIB", "qosUnmatchPolMicroFlowPolicerId"),
        ("BDCOM-QOS-PIB-MIB", "qosUnmatchedPolicyAggregateId"))
)
if mibBuilder.loadTexts:
    qosUnmatchedPolicyTableGroup.setStatus("current")

qosPolicerTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2, 7)
)
qosPolicerTableGroup.setObjects(
      *(("BDCOM-QOS-PIB-MIB", "qosPolicerRate"),
        ("BDCOM-QOS-PIB-MIB", "qosPolicerNormalBurst"),
        ("BDCOM-QOS-PIB-MIB", "qosPolicerExcessBurst"),
        ("BDCOM-QOS-PIB-MIB", "qosPolicerAction"))
)
if mibBuilder.loadTexts:
    qosPolicerTableGroup.setStatus("current")

qosAggregateTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2, 8)
)
qosAggregateTableGroup.setObjects(
    ("BDCOM-QOS-PIB-MIB", "qosAggregatePolicerId")
)
if mibBuilder.loadTexts:
    qosAggregateTableGroup.setStatus("current")

qosMacClassificationTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2, 9)
)
qosMacClassificationTableGroup.setObjects(
      *(("BDCOM-QOS-PIB-MIB", "qosDstMacVlan"),
        ("BDCOM-QOS-PIB-MIB", "qosDstMacAddress"),
        ("BDCOM-QOS-PIB-MIB", "qosDstMacCos"))
)
if mibBuilder.loadTexts:
    qosMacClassificationTableGroup.setStatus("current")

qosIpAceTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2, 10)
)
qosIpAceTableGroup.setObjects(
      *(("BDCOM-QOS-PIB-MIB", "qosIpAceDstAddr"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAceDstAddrMask"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAceSrcAddr"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAceSrcAddrMask"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAceDscpMin"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAceDscpMax"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAceProtocol"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAceDstL4PortMin"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAceDstL4PortMax"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAceSrcL4PortMin"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAceSrcL4PortMax"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAcePermit"))
)
if mibBuilder.loadTexts:
    qosIpAceTableGroup.setStatus("current")

qosIpAclDefinitionTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2, 11)
)
qosIpAclDefinitionTableGroup.setObjects(
      *(("BDCOM-QOS-PIB-MIB", "qosIpAclId"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAceOrder"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAclDefAceId"))
)
if mibBuilder.loadTexts:
    qosIpAclDefinitionTableGroup.setStatus("current")

qosIpAclActionTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2, 12)
)
qosIpAclActionTableGroup.setObjects(
      *(("BDCOM-QOS-PIB-MIB", "qosIpAclActAclId"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAclInterfaceRoles"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAclInterfaceDirection"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAclOrder"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAclDscp"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAclDscpTrusted"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAclMicroFlowPolicerId"),
        ("BDCOM-QOS-PIB-MIB", "qosIpAclAggregateId"))
)
if mibBuilder.loadTexts:
    qosIpAclActionTableGroup.setStatus("current")

qosIfSchedulingPreferencesTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2, 13)
)
qosIfSchedulingPreferencesTableGroup.setObjects(
      *(("BDCOM-QOS-PIB-MIB", "qosIfSchedulingRoles"),
        ("BDCOM-QOS-PIB-MIB", "qosIfSchedulingPreference"),
        ("BDCOM-QOS-PIB-MIB", "qosIfSchedulingDiscipline"),
        ("BDCOM-QOS-PIB-MIB", "qosIfSchedulingQueueType"))
)
if mibBuilder.loadTexts:
    qosIfSchedulingPreferencesTableGroup.setStatus("current")

qosIfDropPreferenceTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2, 14)
)
qosIfDropPreferenceTableGroup.setObjects(
      *(("BDCOM-QOS-PIB-MIB", "qosIfDropRoles"),
        ("BDCOM-QOS-PIB-MIB", "qosIfDropPreference"),
        ("BDCOM-QOS-PIB-MIB", "qosIfDropDiscipline"))
)
if mibBuilder.loadTexts:
    qosIfDropPreferenceTableGroup.setStatus("current")

qosIfDscpAssignmentTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2, 15)
)
qosIfDscpAssignmentTableGroup.setObjects(
      *(("BDCOM-QOS-PIB-MIB", "qosIfDscpRoles"),
        ("BDCOM-QOS-PIB-MIB", "qosIfQueueType"),
        ("BDCOM-QOS-PIB-MIB", "qosIfDscp"),
        ("BDCOM-QOS-PIB-MIB", "qosIfQueue"),
        ("BDCOM-QOS-PIB-MIB", "qosIfThresholdSet"))
)
if mibBuilder.loadTexts:
    qosIfDscpAssignmentTableGroup.setStatus("current")

qosIfRedTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2, 16)
)
qosIfRedTableGroup.setObjects(
      *(("BDCOM-QOS-PIB-MIB", "qosIfRedRoles"),
        ("BDCOM-QOS-PIB-MIB", "qosIfRedNumThresholdSets"),
        ("BDCOM-QOS-PIB-MIB", "qosIfRedThresholdSet"),
        ("BDCOM-QOS-PIB-MIB", "qosIfRedThresholdSetLower"),
        ("BDCOM-QOS-PIB-MIB", "qosIfRedThresholdSetUpper"))
)
if mibBuilder.loadTexts:
    qosIfRedTableGroup.setStatus("current")

qosIfTailDropTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2, 17)
)
qosIfTailDropTableGroup.setObjects(
      *(("BDCOM-QOS-PIB-MIB", "qosIfTailDropRoles"),
        ("BDCOM-QOS-PIB-MIB", "qosIfTailDropNumThresholdSets"),
        ("BDCOM-QOS-PIB-MIB", "qosIfTailDropThresholdSet"),
        ("BDCOM-QOS-PIB-MIB", "qosIfTailDropThresholdSetValue"))
)
if mibBuilder.loadTexts:
    qosIfTailDropTableGroup.setStatus("current")

qosIfWeightsTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 2, 18)
)
qosIfWeightsTableGroup.setObjects(
      *(("BDCOM-QOS-PIB-MIB", "qosIfWeightsRoles"),
        ("BDCOM-QOS-PIB-MIB", "qosIfWeightsNumQueues"),
        ("BDCOM-QOS-PIB-MIB", "qosIfWeightsQueue"),
        ("BDCOM-QOS-PIB-MIB", "qosIfWeightsDrainSize"),
        ("BDCOM-QOS-PIB-MIB", "qosIfWeightsQueueSize"))
)
if mibBuilder.loadTexts:
    qosIfWeightsTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qosPIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qosPIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BDCOM-QOS-PIB-MIB",
    **{"Dscp": Dscp,
       "QosLayer2Cos": QosLayer2Cos,
       "QueueRange": QueueRange,
       "ThresholdSetRange": ThresholdSetRange,
       "Percent": Percent,
       "QosInterfaceQueueType": QosInterfaceQueueType,
       "QosInterfaceTypeCapabilities": QosInterfaceTypeCapabilities,
       "RoleCombination": RoleCombination,
       "PolicyInstanceId": PolicyInstanceId,
       "Unsigned64": Unsigned64,
       "bdcomQosPIBMIB": bdcomQosPIBMIB,
       "qosPIBConformance": qosPIBConformance,
       "qosPIBCompliances": qosPIBCompliances,
       "qosPIBCompliance": qosPIBCompliance,
       "qosPIBGroups": qosPIBGroups,
       "qosDevicePibIncarnationTableGroup": qosDevicePibIncarnationTableGroup,
       "qosDeviceAttributeTableGroup": qosDeviceAttributeTableGroup,
       "qosInterfaceTypeTableGroup": qosInterfaceTypeTableGroup,
       "qosDiffServMappingTableGroup": qosDiffServMappingTableGroup,
       "qosCosToDscpTableGroup": qosCosToDscpTableGroup,
       "qosUnmatchedPolicyTableGroup": qosUnmatchedPolicyTableGroup,
       "qosPolicerTableGroup": qosPolicerTableGroup,
       "qosAggregateTableGroup": qosAggregateTableGroup,
       "qosMacClassificationTableGroup": qosMacClassificationTableGroup,
       "qosIpAceTableGroup": qosIpAceTableGroup,
       "qosIpAclDefinitionTableGroup": qosIpAclDefinitionTableGroup,
       "qosIpAclActionTableGroup": qosIpAclActionTableGroup,
       "qosIfSchedulingPreferencesTableGroup": qosIfSchedulingPreferencesTableGroup,
       "qosIfDropPreferenceTableGroup": qosIfDropPreferenceTableGroup,
       "qosIfDscpAssignmentTableGroup": qosIfDscpAssignmentTableGroup,
       "qosIfRedTableGroup": qosIfRedTableGroup,
       "qosIfTailDropTableGroup": qosIfTailDropTableGroup,
       "qosIfWeightsTableGroup": qosIfWeightsTableGroup,
       "qosDeviceConfig": qosDeviceConfig,
       "qosDevicePibIncarnationTable": qosDevicePibIncarnationTable,
       "qosDevicePibIncarnationEntry": qosDevicePibIncarnationEntry,
       "qosDeviceIncarnationId": qosDeviceIncarnationId,
       "qosDevicePdpName": qosDevicePdpName,
       "qosDevicePibIncarnation": qosDevicePibIncarnation,
       "qosDevicePibTtl": qosDevicePibTtl,
       "qosDeviceAttributeTable": qosDeviceAttributeTable,
       "qosDeviceAttributeEntry": qosDeviceAttributeEntry,
       "qosDeviceAttributeId": qosDeviceAttributeId,
       "qosDevicePepDomain": qosDevicePepDomain,
       "qosDevicePrimaryPdp": qosDevicePrimaryPdp,
       "qosDeviceSecondaryPdp": qosDeviceSecondaryPdp,
       "qosDeviceMaxMessageSize": qosDeviceMaxMessageSize,
       "qosDeviceCapabilities": qosDeviceCapabilities,
       "qosInterfaceTypeTable": qosInterfaceTypeTable,
       "qosInterfaceTypeEntry": qosInterfaceTypeEntry,
       "qosInterfaceTypeId": qosInterfaceTypeId,
       "qosInterfaceQueueType": qosInterfaceQueueType,
       "qosInterfaceTypeRoles": qosInterfaceTypeRoles,
       "qosInterfaceTypeCapabilities": qosInterfaceTypeCapabilities,
       "qosDomainConfig": qosDomainConfig,
       "qosDiffServMappingTable": qosDiffServMappingTable,
       "qosDiffServMappingEntry": qosDiffServMappingEntry,
       "qosDscp": qosDscp,
       "qosMarkedDscp": qosMarkedDscp,
       "qosL2Cos": qosL2Cos,
       "qosCosToDscpTable": qosCosToDscpTable,
       "qosCosToDscpEntry": qosCosToDscpEntry,
       "qosCosToDscpCos": qosCosToDscpCos,
       "qosCosToDscpDscp": qosCosToDscpDscp,
       "qosUnmatchedPolicy": qosUnmatchedPolicy,
       "qosUnmatchedPolicyTable": qosUnmatchedPolicyTable,
       "qosUnmatchedPolicyEntry": qosUnmatchedPolicyEntry,
       "qosUnmatchedPolicyId": qosUnmatchedPolicyId,
       "qosUnmatchedPolicyRole": qosUnmatchedPolicyRole,
       "qosUnmatchedPolicyDirection": qosUnmatchedPolicyDirection,
       "qosUnmatchedPolicyDscp": qosUnmatchedPolicyDscp,
       "qosUnmatchedPolicyDscpTrusted": qosUnmatchedPolicyDscpTrusted,
       "qosUnmatchPolMicroFlowPolicerId": qosUnmatchPolMicroFlowPolicerId,
       "qosUnmatchedPolicyAggregateId": qosUnmatchedPolicyAggregateId,
       "qosPolicer": qosPolicer,
       "qosPolicerTable": qosPolicerTable,
       "qosPolicerEntry": qosPolicerEntry,
       "qosPolicerId": qosPolicerId,
       "qosPolicerRate": qosPolicerRate,
       "qosPolicerNormalBurst": qosPolicerNormalBurst,
       "qosPolicerExcessBurst": qosPolicerExcessBurst,
       "qosPolicerAction": qosPolicerAction,
       "qosAggregateTable": qosAggregateTable,
       "qosAggregateEntry": qosAggregateEntry,
       "qosAggregateId": qosAggregateId,
       "qosAggregatePolicerId": qosAggregatePolicerId,
       "qosMacQos": qosMacQos,
       "qosMacClassificationTable": qosMacClassificationTable,
       "qosMacClassificationEntry": qosMacClassificationEntry,
       "qosMacClassificationId": qosMacClassificationId,
       "qosDstMacVlan": qosDstMacVlan,
       "qosDstMacAddress": qosDstMacAddress,
       "qosDstMacCos": qosDstMacCos,
       "qosIpQos": qosIpQos,
       "qosIpAceTable": qosIpAceTable,
       "qosIpAceEntry": qosIpAceEntry,
       "qosIpAceId": qosIpAceId,
       "qosIpAceDstAddr": qosIpAceDstAddr,
       "qosIpAceDstAddrMask": qosIpAceDstAddrMask,
       "qosIpAceSrcAddr": qosIpAceSrcAddr,
       "qosIpAceSrcAddrMask": qosIpAceSrcAddrMask,
       "qosIpAceDscpMin": qosIpAceDscpMin,
       "qosIpAceDscpMax": qosIpAceDscpMax,
       "qosIpAceProtocol": qosIpAceProtocol,
       "qosIpAceDstL4PortMin": qosIpAceDstL4PortMin,
       "qosIpAceDstL4PortMax": qosIpAceDstL4PortMax,
       "qosIpAceSrcL4PortMin": qosIpAceSrcL4PortMin,
       "qosIpAceSrcL4PortMax": qosIpAceSrcL4PortMax,
       "qosIpAcePermit": qosIpAcePermit,
       "qosIpAclDefinitionTable": qosIpAclDefinitionTable,
       "qosIpAclDefinitionEntry": qosIpAclDefinitionEntry,
       "qosIpAclDefinitionId": qosIpAclDefinitionId,
       "qosIpAclId": qosIpAclId,
       "qosIpAceOrder": qosIpAceOrder,
       "qosIpAclDefAceId": qosIpAclDefAceId,
       "qosIpAclActionTable": qosIpAclActionTable,
       "qosIpAclActionEntry": qosIpAclActionEntry,
       "qosIpAclActionId": qosIpAclActionId,
       "qosIpAclActAclId": qosIpAclActAclId,
       "qosIpAclInterfaceRoles": qosIpAclInterfaceRoles,
       "qosIpAclInterfaceDirection": qosIpAclInterfaceDirection,
       "qosIpAclOrder": qosIpAclOrder,
       "qosIpAclDscp": qosIpAclDscp,
       "qosIpAclDscpTrusted": qosIpAclDscpTrusted,
       "qosIpAclMicroFlowPolicerId": qosIpAclMicroFlowPolicerId,
       "qosIpAclAggregateId": qosIpAclAggregateId,
       "qosIfParameters": qosIfParameters,
       "qosIfSchedulingPreferencesTable": qosIfSchedulingPreferencesTable,
       "qosIfSchedulingPreferenceEntry": qosIfSchedulingPreferenceEntry,
       "qosIfSchedulingPreferenceId": qosIfSchedulingPreferenceId,
       "qosIfSchedulingRoles": qosIfSchedulingRoles,
       "qosIfSchedulingPreference": qosIfSchedulingPreference,
       "qosIfSchedulingDiscipline": qosIfSchedulingDiscipline,
       "qosIfSchedulingQueueType": qosIfSchedulingQueueType,
       "qosIfDropPreferenceTable": qosIfDropPreferenceTable,
       "qosIfDropPreferenceEntry": qosIfDropPreferenceEntry,
       "qosIfDropPreferenceId": qosIfDropPreferenceId,
       "qosIfDropRoles": qosIfDropRoles,
       "qosIfDropPreference": qosIfDropPreference,
       "qosIfDropDiscipline": qosIfDropDiscipline,
       "qosIfDscpAssignmentTable": qosIfDscpAssignmentTable,
       "qosIfDscpAssignmentEntry": qosIfDscpAssignmentEntry,
       "qosIfDscpAssignmentId": qosIfDscpAssignmentId,
       "qosIfDscpRoles": qosIfDscpRoles,
       "qosIfQueueType": qosIfQueueType,
       "qosIfDscp": qosIfDscp,
       "qosIfQueue": qosIfQueue,
       "qosIfThresholdSet": qosIfThresholdSet,
       "qosIfRedTable": qosIfRedTable,
       "qosIfRedEntry": qosIfRedEntry,
       "qosIfRedId": qosIfRedId,
       "qosIfRedRoles": qosIfRedRoles,
       "qosIfRedNumThresholdSets": qosIfRedNumThresholdSets,
       "qosIfRedThresholdSet": qosIfRedThresholdSet,
       "qosIfRedThresholdSetLower": qosIfRedThresholdSetLower,
       "qosIfRedThresholdSetUpper": qosIfRedThresholdSetUpper,
       "qosIfTailDropTable": qosIfTailDropTable,
       "qosIfTailDropEntry": qosIfTailDropEntry,
       "qosIfTailDropId": qosIfTailDropId,
       "qosIfTailDropRoles": qosIfTailDropRoles,
       "qosIfTailDropNumThresholdSets": qosIfTailDropNumThresholdSets,
       "qosIfTailDropThresholdSet": qosIfTailDropThresholdSet,
       "qosIfTailDropThresholdSetValue": qosIfTailDropThresholdSetValue,
       "qosIfWeightsTable": qosIfWeightsTable,
       "qosIfWeightsEntry": qosIfWeightsEntry,
       "qosIfWeightsId": qosIfWeightsId,
       "qosIfWeightsRoles": qosIfWeightsRoles,
       "qosIfWeightsNumQueues": qosIfWeightsNumQueues,
       "qosIfWeightsQueue": qosIfWeightsQueue,
       "qosIfWeightsDrainSize": qosIfWeightsDrainSize,
       "qosIfWeightsQueueSize": qosIfWeightsQueueSize}
)

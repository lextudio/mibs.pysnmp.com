# SNMP MIB module (CISCO-CATOS-ACL-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CATOS-ACL-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:04 2024
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

(Dscp,
 Percent,
 QosInterfaceQueueType,
 QosLayer2Cos) = mibBuilder.importSymbols(
    "CISCO-QOS-PIB-MIB",
    "Dscp",
    "Percent",
    "QosInterfaceQueueType",
    "QosLayer2Cos")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(cseFlowDataEntry,) = mibBuilder.importSymbols(
    "CISCO-SWITCH-ENGINE-MIB",
    "cseFlowDataEntry")

(CiscoIpProtocol,
 CiscoPortList) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoIpProtocol",
    "CiscoPortList")

(VlanIndex,) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "VlanIndex")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCatOSAclQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 179)
)
ciscoCatOSAclQosMIB.setRevisions(
        ("2007-11-02 00:00",
         "2006-07-15 00:00",
         "2005-07-26 00:00",
         "2004-05-26 00:00",
         "2003-11-26 00:00",
         "2003-10-28 00:00",
         "2003-09-30 00:00",
         "2003-07-01 00:00",
         "2003-03-05 00:00",
         "2002-10-10 00:00",
         "2002-01-17 00:00",
         "2001-10-18 00:00",
         "2001-02-15 00:00",
         "2001-02-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CaqAclName(OctetString, TextualConvention):
    status = "current"
    displayHint = "31a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class CaqPolicerName(OctetString, TextualConvention):
    status = "current"
    displayHint = "31a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class CaqPolicerNameOrEmpty(OctetString, TextualConvention):
    status = "current"
    displayHint = "31a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



class CaqAdjacencyName(OctetString, TextualConvention):
    status = "current"
    displayHint = "18a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 18),
    )



class CaqDirection(Integer32, TextualConvention):
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



class CaqIpPrecedence(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class CaqQueueNumber(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class CaqThresholdNumber(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class CaqHitCountAclType(Integer32, TextualConvention):
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
        *(("ipSecurity", 1),
          ("ipxSecurity", 2),
          ("macSecurity", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCatOSAclQosMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCatOSAclQosMIBObjects = _CiscoCatOSAclQosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1)
)
_CaqGlobalObjects_ObjectIdentity = ObjectIdentity
caqGlobalObjects = _CaqGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1)
)
_CaqCosToDscpTable_Object = MibTable
caqCosToDscpTable = _CaqCosToDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 1)
)
if mibBuilder.loadTexts:
    caqCosToDscpTable.setStatus("current")
_CaqCosToDscpEntry_Object = MibTableRow
caqCosToDscpEntry = _CaqCosToDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 1, 1)
)
caqCosToDscpEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqCosToDscpCos"),
)
if mibBuilder.loadTexts:
    caqCosToDscpEntry.setStatus("current")
_CaqCosToDscpCos_Type = QosLayer2Cos
_CaqCosToDscpCos_Object = MibTableColumn
caqCosToDscpCos = _CaqCosToDscpCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 1, 1, 1),
    _CaqCosToDscpCos_Type()
)
caqCosToDscpCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqCosToDscpCos.setStatus("current")
_CaqCosToDscpDscp_Type = Dscp
_CaqCosToDscpDscp_Object = MibTableColumn
caqCosToDscpDscp = _CaqCosToDscpDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 1, 1, 2),
    _CaqCosToDscpDscp_Type()
)
caqCosToDscpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqCosToDscpDscp.setStatus("current")
_CaqIpPrecToDscpTable_Object = MibTable
caqIpPrecToDscpTable = _CaqIpPrecToDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 2)
)
if mibBuilder.loadTexts:
    caqIpPrecToDscpTable.setStatus("current")
_CaqIpPrecToDscpEntry_Object = MibTableRow
caqIpPrecToDscpEntry = _CaqIpPrecToDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 2, 1)
)
caqIpPrecToDscpEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqIpPrecToDscpIpPrec"),
)
if mibBuilder.loadTexts:
    caqIpPrecToDscpEntry.setStatus("current")
_CaqIpPrecToDscpIpPrec_Type = CaqIpPrecedence
_CaqIpPrecToDscpIpPrec_Object = MibTableColumn
caqIpPrecToDscpIpPrec = _CaqIpPrecToDscpIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 2, 1, 1),
    _CaqIpPrecToDscpIpPrec_Type()
)
caqIpPrecToDscpIpPrec.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqIpPrecToDscpIpPrec.setStatus("current")
_CaqIpPrecToDscpDscp_Type = Dscp
_CaqIpPrecToDscpDscp_Object = MibTableColumn
caqIpPrecToDscpDscp = _CaqIpPrecToDscpDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 2, 1, 2),
    _CaqIpPrecToDscpDscp_Type()
)
caqIpPrecToDscpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqIpPrecToDscpDscp.setStatus("current")
_CaqDscpMappingTable_Object = MibTable
caqDscpMappingTable = _CaqDscpMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 3)
)
if mibBuilder.loadTexts:
    caqDscpMappingTable.setStatus("current")
_CaqDscpMappingEntry_Object = MibTableRow
caqDscpMappingEntry = _CaqDscpMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 3, 1)
)
caqDscpMappingEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqDscpMappingDscp"),
)
if mibBuilder.loadTexts:
    caqDscpMappingEntry.setStatus("current")
_CaqDscpMappingDscp_Type = Dscp
_CaqDscpMappingDscp_Object = MibTableColumn
caqDscpMappingDscp = _CaqDscpMappingDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 3, 1, 1),
    _CaqDscpMappingDscp_Type()
)
caqDscpMappingDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqDscpMappingDscp.setStatus("current")
_CaqDscpMappingCos_Type = QosLayer2Cos
_CaqDscpMappingCos_Object = MibTableColumn
caqDscpMappingCos = _CaqDscpMappingCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 3, 1, 2),
    _CaqDscpMappingCos_Type()
)
caqDscpMappingCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqDscpMappingCos.setStatus("current")
_CaqDscpMappingNRPolicedDscp_Type = Dscp
_CaqDscpMappingNRPolicedDscp_Object = MibTableColumn
caqDscpMappingNRPolicedDscp = _CaqDscpMappingNRPolicedDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 3, 1, 3),
    _CaqDscpMappingNRPolicedDscp_Type()
)
caqDscpMappingNRPolicedDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqDscpMappingNRPolicedDscp.setStatus("current")
_CaqDscpMappingERPolicedDscp_Type = Dscp
_CaqDscpMappingERPolicedDscp_Object = MibTableColumn
caqDscpMappingERPolicedDscp = _CaqDscpMappingERPolicedDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 3, 1, 4),
    _CaqDscpMappingERPolicedDscp_Type()
)
caqDscpMappingERPolicedDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqDscpMappingERPolicedDscp.setStatus("current")
_CaqCosAssignmentTable_Object = MibTable
caqCosAssignmentTable = _CaqCosAssignmentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 4)
)
if mibBuilder.loadTexts:
    caqCosAssignmentTable.setStatus("current")
_CaqCosAssignmentEntry_Object = MibTableRow
caqCosAssignmentEntry = _CaqCosAssignmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 4, 1)
)
caqCosAssignmentEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqCosAssignQueueType"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqCosAssignCos"),
)
if mibBuilder.loadTexts:
    caqCosAssignmentEntry.setStatus("current")
_CaqCosAssignQueueType_Type = QosInterfaceQueueType
_CaqCosAssignQueueType_Object = MibTableColumn
caqCosAssignQueueType = _CaqCosAssignQueueType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 4, 1, 1),
    _CaqCosAssignQueueType_Type()
)
caqCosAssignQueueType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqCosAssignQueueType.setStatus("current")
_CaqCosAssignCos_Type = QosLayer2Cos
_CaqCosAssignCos_Object = MibTableColumn
caqCosAssignCos = _CaqCosAssignCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 4, 1, 2),
    _CaqCosAssignCos_Type()
)
caqCosAssignCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqCosAssignCos.setStatus("current")
_CaqCosAssignQueueNumber_Type = CaqQueueNumber
_CaqCosAssignQueueNumber_Object = MibTableColumn
caqCosAssignQueueNumber = _CaqCosAssignQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 4, 1, 3),
    _CaqCosAssignQueueNumber_Type()
)
caqCosAssignQueueNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqCosAssignQueueNumber.setStatus("current")
_CaqCosAssignThresholdNumber_Type = CaqThresholdNumber
_CaqCosAssignThresholdNumber_Object = MibTableColumn
caqCosAssignThresholdNumber = _CaqCosAssignThresholdNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 4, 1, 4),
    _CaqCosAssignThresholdNumber_Type()
)
caqCosAssignThresholdNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqCosAssignThresholdNumber.setStatus("current")
_CaqQueueThresholdTable_Object = MibTable
caqQueueThresholdTable = _CaqQueueThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 5)
)
if mibBuilder.loadTexts:
    caqQueueThresholdTable.setStatus("current")
_CaqQueueThresholdEntry_Object = MibTableRow
caqQueueThresholdEntry = _CaqQueueThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 5, 1)
)
caqQueueThresholdEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqQueueThreshQueueType"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqQueueThreshQueueIndex"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqQueueThreshThresholdIndex"),
)
if mibBuilder.loadTexts:
    caqQueueThresholdEntry.setStatus("current")
_CaqQueueThreshQueueType_Type = QosInterfaceQueueType
_CaqQueueThreshQueueType_Object = MibTableColumn
caqQueueThreshQueueType = _CaqQueueThreshQueueType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 5, 1, 1),
    _CaqQueueThreshQueueType_Type()
)
caqQueueThreshQueueType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqQueueThreshQueueType.setStatus("current")
_CaqQueueThreshQueueIndex_Type = CaqQueueNumber
_CaqQueueThreshQueueIndex_Object = MibTableColumn
caqQueueThreshQueueIndex = _CaqQueueThreshQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 5, 1, 2),
    _CaqQueueThreshQueueIndex_Type()
)
caqQueueThreshQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqQueueThreshQueueIndex.setStatus("current")
_CaqQueueThreshThresholdIndex_Type = CaqThresholdNumber
_CaqQueueThreshThresholdIndex_Object = MibTableColumn
caqQueueThreshThresholdIndex = _CaqQueueThreshThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 5, 1, 3),
    _CaqQueueThreshThresholdIndex_Type()
)
caqQueueThreshThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqQueueThreshThresholdIndex.setStatus("current")


class _CaqQueueThreshDropAlgorithm_Type(Integer32):
    """Custom type caqQueueThreshDropAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tailDrop", 1),
          ("wred", 2))
    )


_CaqQueueThreshDropAlgorithm_Type.__name__ = "Integer32"
_CaqQueueThreshDropAlgorithm_Object = MibTableColumn
caqQueueThreshDropAlgorithm = _CaqQueueThreshDropAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 5, 1, 4),
    _CaqQueueThreshDropAlgorithm_Type()
)
caqQueueThreshDropAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqQueueThreshDropAlgorithm.setStatus("current")


class _CaqQueueThreshDropThreshold_Type(Unsigned32):
    """Custom type caqQueueThreshDropThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CaqQueueThreshDropThreshold_Type.__name__ = "Unsigned32"
_CaqQueueThreshDropThreshold_Object = MibTableColumn
caqQueueThreshDropThreshold = _CaqQueueThreshDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 5, 1, 5),
    _CaqQueueThreshDropThreshold_Type()
)
caqQueueThreshDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqQueueThreshDropThreshold.setStatus("current")
if mibBuilder.loadTexts:
    caqQueueThreshDropThreshold.setUnits("percent")
_CaqQueueThreshMinWredThreshold_Type = Percent
_CaqQueueThreshMinWredThreshold_Object = MibTableColumn
caqQueueThreshMinWredThreshold = _CaqQueueThreshMinWredThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 5, 1, 6),
    _CaqQueueThreshMinWredThreshold_Type()
)
caqQueueThreshMinWredThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqQueueThreshMinWredThreshold.setStatus("current")


class _CaqQueueThreshMaxWredThreshold_Type(Unsigned32):
    """Custom type caqQueueThreshMaxWredThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CaqQueueThreshMaxWredThreshold_Type.__name__ = "Unsigned32"
_CaqQueueThreshMaxWredThreshold_Object = MibTableColumn
caqQueueThreshMaxWredThreshold = _CaqQueueThreshMaxWredThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 5, 1, 7),
    _CaqQueueThreshMaxWredThreshold_Type()
)
caqQueueThreshMaxWredThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqQueueThreshMaxWredThreshold.setStatus("current")
if mibBuilder.loadTexts:
    caqQueueThreshMaxWredThreshold.setUnits("percent")
_CaqQueueTable_Object = MibTable
caqQueueTable = _CaqQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 6)
)
if mibBuilder.loadTexts:
    caqQueueTable.setStatus("current")
_CaqQueueEntry_Object = MibTableRow
caqQueueEntry = _CaqQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 6, 1)
)
caqQueueEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqQueueDirection"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqQueueType"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqQueueNumber"),
)
if mibBuilder.loadTexts:
    caqQueueEntry.setStatus("current")
_CaqQueueDirection_Type = CaqDirection
_CaqQueueDirection_Object = MibTableColumn
caqQueueDirection = _CaqQueueDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 6, 1, 1),
    _CaqQueueDirection_Type()
)
caqQueueDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqQueueDirection.setStatus("current")
_CaqQueueType_Type = QosInterfaceQueueType
_CaqQueueType_Object = MibTableColumn
caqQueueType = _CaqQueueType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 6, 1, 2),
    _CaqQueueType_Type()
)
caqQueueType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqQueueType.setStatus("current")
_CaqQueueNumber_Type = CaqQueueNumber
_CaqQueueNumber_Object = MibTableColumn
caqQueueNumber = _CaqQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 6, 1, 3),
    _CaqQueueNumber_Type()
)
caqQueueNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqQueueNumber.setStatus("current")


class _CaqQueueWrrWeight_Type(Unsigned32):
    """Custom type caqQueueWrrWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CaqQueueWrrWeight_Type.__name__ = "Unsigned32"
_CaqQueueWrrWeight_Object = MibTableColumn
caqQueueWrrWeight = _CaqQueueWrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 6, 1, 4),
    _CaqQueueWrrWeight_Type()
)
caqQueueWrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqQueueWrrWeight.setStatus("current")


class _CaqQueueBufferSizeRatio_Type(Unsigned32):
    """Custom type caqQueueBufferSizeRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CaqQueueBufferSizeRatio_Type.__name__ = "Unsigned32"
_CaqQueueBufferSizeRatio_Object = MibTableColumn
caqQueueBufferSizeRatio = _CaqQueueBufferSizeRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 6, 1, 5),
    _CaqQueueBufferSizeRatio_Type()
)
caqQueueBufferSizeRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqQueueBufferSizeRatio.setStatus("current")
if mibBuilder.loadTexts:
    caqQueueBufferSizeRatio.setUnits("percent")
_CaqDscpMutationMapTable_Object = MibTable
caqDscpMutationMapTable = _CaqDscpMutationMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 7)
)
if mibBuilder.loadTexts:
    caqDscpMutationMapTable.setStatus("current")
_CaqDscpMutationMapEntry_Object = MibTableRow
caqDscpMutationMapEntry = _CaqDscpMutationMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 7, 1)
)
caqDscpMutationMapEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqDscpMutationTableId"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqDscpMutationOldDscp"),
)
if mibBuilder.loadTexts:
    caqDscpMutationMapEntry.setStatus("current")
_CaqDscpMutationTableId_Type = Unsigned32
_CaqDscpMutationTableId_Object = MibTableColumn
caqDscpMutationTableId = _CaqDscpMutationTableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 7, 1, 1),
    _CaqDscpMutationTableId_Type()
)
caqDscpMutationTableId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqDscpMutationTableId.setStatus("current")
_CaqDscpMutationOldDscp_Type = Dscp
_CaqDscpMutationOldDscp_Object = MibTableColumn
caqDscpMutationOldDscp = _CaqDscpMutationOldDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 7, 1, 2),
    _CaqDscpMutationOldDscp_Type()
)
caqDscpMutationOldDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqDscpMutationOldDscp.setStatus("current")
_CaqDscpMutationNewDscp_Type = Dscp
_CaqDscpMutationNewDscp_Object = MibTableColumn
caqDscpMutationNewDscp = _CaqDscpMutationNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 7, 1, 3),
    _CaqDscpMutationNewDscp_Type()
)
caqDscpMutationNewDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqDscpMutationNewDscp.setStatus("current")
_CaqVlanMutationIdMapTable_Object = MibTable
caqVlanMutationIdMapTable = _CaqVlanMutationIdMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 8)
)
if mibBuilder.loadTexts:
    caqVlanMutationIdMapTable.setStatus("current")
_CaqVlanMutationIdMapEntry_Object = MibTableRow
caqVlanMutationIdMapEntry = _CaqVlanMutationIdMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 8, 1)
)
caqVlanMutationIdMapEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqVlanMutationIndex"),
)
if mibBuilder.loadTexts:
    caqVlanMutationIdMapEntry.setStatus("current")
_CaqVlanMutationIndex_Type = VlanIndex
_CaqVlanMutationIndex_Object = MibTableColumn
caqVlanMutationIndex = _CaqVlanMutationIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 8, 1, 1),
    _CaqVlanMutationIndex_Type()
)
caqVlanMutationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqVlanMutationIndex.setStatus("current")
_CaqVlanMutationTableId_Type = Unsigned32
_CaqVlanMutationTableId_Object = MibTableColumn
caqVlanMutationTableId = _CaqVlanMutationTableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 8, 1, 2),
    _CaqVlanMutationTableId_Type()
)
caqVlanMutationTableId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVlanMutationTableId.setStatus("current")
_CaqDscpRewriteEnabled_Type = TruthValue
_CaqDscpRewriteEnabled_Object = MibScalar
caqDscpRewriteEnabled = _CaqDscpRewriteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 9),
    _CaqDscpRewriteEnabled_Type()
)
caqDscpRewriteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqDscpRewriteEnabled.setStatus("current")


class _CaqMacPktClassifyVlansLow_Type(OctetString):
    """Custom type caqMacPktClassifyVlansLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CaqMacPktClassifyVlansLow_Type.__name__ = "OctetString"
_CaqMacPktClassifyVlansLow_Object = MibScalar
caqMacPktClassifyVlansLow = _CaqMacPktClassifyVlansLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 10),
    _CaqMacPktClassifyVlansLow_Type()
)
caqMacPktClassifyVlansLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqMacPktClassifyVlansLow.setStatus("current")


class _CaqMacPktClassifyVlansHigh_Type(OctetString):
    """Custom type caqMacPktClassifyVlansHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CaqMacPktClassifyVlansHigh_Type.__name__ = "OctetString"
_CaqMacPktClassifyVlansHigh_Object = MibScalar
caqMacPktClassifyVlansHigh = _CaqMacPktClassifyVlansHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 1, 11),
    _CaqMacPktClassifyVlansHigh_Type()
)
caqMacPktClassifyVlansHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqMacPktClassifyVlansHigh.setStatus("current")
_CaqInterfaceObjects_ObjectIdentity = ObjectIdentity
caqInterfaceObjects = _CaqInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2)
)
_CaqIfConfigTable_Object = MibTable
caqIfConfigTable = _CaqIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 1)
)
if mibBuilder.loadTexts:
    caqIfConfigTable.setStatus("current")
_CaqIfConfigEntry_Object = MibTableRow
caqIfConfigEntry = _CaqIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 1, 1)
)
caqIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    caqIfConfigEntry.setStatus("current")
_CaqIfCos_Type = QosLayer2Cos
_CaqIfCos_Object = MibTableColumn
caqIfCos = _CaqIfCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 1, 1, 1),
    _CaqIfCos_Type()
)
caqIfCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqIfCos.setStatus("current")


class _CaqIfTrustStateConfig_Type(Integer32):
    """Custom type caqIfTrustStateConfig based on Integer32"""
    defaultValue = 1

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
        *(("trustCoS", 2),
          ("trustDscp", 4),
          ("trustIpPrec", 3),
          ("untrusted", 1))
    )


_CaqIfTrustStateConfig_Type.__name__ = "Integer32"
_CaqIfTrustStateConfig_Object = MibTableColumn
caqIfTrustStateConfig = _CaqIfTrustStateConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 1, 1, 2),
    _CaqIfTrustStateConfig_Type()
)
caqIfTrustStateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqIfTrustStateConfig.setStatus("current")


class _CaqIfAclBase_Type(Integer32):
    """Custom type caqIfAclBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 2),
          ("vlan", 1))
    )


_CaqIfAclBase_Type.__name__ = "Integer32"
_CaqIfAclBase_Object = MibTableColumn
caqIfAclBase = _CaqIfAclBase_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 1, 1, 3),
    _CaqIfAclBase_Type()
)
caqIfAclBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqIfAclBase.setStatus("current")


class _CaqIfTrustDevice_Type(Bits):
    """Custom type caqIfTrustDevice based on Bits"""
    namedValues = NamedValues(
        ("trustCiscoIPPhone", 0)
    )

_CaqIfTrustDevice_Type.__name__ = "Bits"
_CaqIfTrustDevice_Object = MibTableColumn
caqIfTrustDevice = _CaqIfTrustDevice_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 1, 1, 4),
    _CaqIfTrustDevice_Type()
)
caqIfTrustDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqIfTrustDevice.setStatus("current")


class _CaqIfOperTrustState_Type(Integer32):
    """Custom type caqIfOperTrustState based on Integer32"""
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
        *(("trustCoS", 2),
          ("trustDscp", 4),
          ("trustIpPrec", 3),
          ("untrusted", 1))
    )


_CaqIfOperTrustState_Type.__name__ = "Integer32"
_CaqIfOperTrustState_Object = MibTableColumn
caqIfOperTrustState = _CaqIfOperTrustState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 1, 1, 5),
    _CaqIfOperTrustState_Type()
)
caqIfOperTrustState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIfOperTrustState.setStatus("current")
_CaqClassifierTable_Object = MibTable
caqClassifierTable = _CaqClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 2)
)
if mibBuilder.loadTexts:
    caqClassifierTable.setStatus("current")
_CaqClassifierEntry_Object = MibTableRow
caqClassifierEntry = _CaqClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 2, 1)
)
caqClassifierEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqClassifierAclType"),
    (1, "CISCO-CATOS-ACL-QOS-MIB", "caqClassifierAclName"),
)
if mibBuilder.loadTexts:
    caqClassifierEntry.setStatus("current")


class _CaqClassifierAclType_Type(Integer32):
    """Custom type caqClassifierAclType based on Integer32"""
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
        *(("ipQos", 1),
          ("ipSecurity", 4),
          ("ipxQos", 2),
          ("ipxSecurity", 5),
          ("macQos", 3),
          ("macSecurity", 6))
    )


_CaqClassifierAclType_Type.__name__ = "Integer32"
_CaqClassifierAclType_Object = MibTableColumn
caqClassifierAclType = _CaqClassifierAclType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 2, 1, 1),
    _CaqClassifierAclType_Type()
)
caqClassifierAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqClassifierAclType.setStatus("current")
_CaqClassifierAclName_Type = CaqAclName
_CaqClassifierAclName_Object = MibTableColumn
caqClassifierAclName = _CaqClassifierAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 2, 1, 2),
    _CaqClassifierAclName_Type()
)
caqClassifierAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqClassifierAclName.setStatus("current")
_CaqClassifierMapStatus_Type = RowStatus
_CaqClassifierMapStatus_Object = MibTableColumn
caqClassifierMapStatus = _CaqClassifierMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 2, 1, 3),
    _CaqClassifierMapStatus_Type()
)
caqClassifierMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqClassifierMapStatus.setStatus("current")


class _CaqClassifierMapDirection_Type(Bits):
    """Custom type caqClassifierMapDirection based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("egress", 1),
          ("ingress", 0))
    )

_CaqClassifierMapDirection_Type.__name__ = "Bits"
_CaqClassifierMapDirection_Object = MibTableColumn
caqClassifierMapDirection = _CaqClassifierMapDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 2, 1, 4),
    _CaqClassifierMapDirection_Type()
)
caqClassifierMapDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqClassifierMapDirection.setStatus("current")
_CaqIfSecurityAclConfigTable_Object = MibTable
caqIfSecurityAclConfigTable = _CaqIfSecurityAclConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 3)
)
if mibBuilder.loadTexts:
    caqIfSecurityAclConfigTable.setStatus("current")
_CaqIfSecurityAclConfigEntry_Object = MibTableRow
caqIfSecurityAclConfigEntry = _CaqIfSecurityAclConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 3, 1)
)
caqIfSecurityAclConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    caqIfSecurityAclConfigEntry.setStatus("current")


class _CaqIfSecurityAclBase_Type(Integer32):
    """Custom type caqIfSecurityAclBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("merge", 3),
          ("port", 1),
          ("vlan", 2))
    )


_CaqIfSecurityAclBase_Type.__name__ = "Integer32"
_CaqIfSecurityAclBase_Object = MibTableColumn
caqIfSecurityAclBase = _CaqIfSecurityAclBase_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 3, 1, 1),
    _CaqIfSecurityAclBase_Type()
)
caqIfSecurityAclBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqIfSecurityAclBase.setStatus("current")
_CaqIpOperClassifierTable_Object = MibTable
caqIpOperClassifierTable = _CaqIpOperClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 4)
)
if mibBuilder.loadTexts:
    caqIpOperClassifierTable.setStatus("current")
_CaqIpOperClassifierEntry_Object = MibTableRow
caqIpOperClassifierEntry = _CaqIpOperClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 4, 1)
)
caqIpOperClassifierEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqIpOperAclFeature"),
)
if mibBuilder.loadTexts:
    caqIpOperClassifierEntry.setStatus("current")


class _CaqIpOperAclFeature_Type(Integer32):
    """Custom type caqIpOperAclFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egressIpQos", 2),
          ("ingressIpQos", 1),
          ("ipSecurity", 3))
    )


_CaqIpOperAclFeature_Type.__name__ = "Integer32"
_CaqIpOperAclFeature_Object = MibTableColumn
caqIpOperAclFeature = _CaqIpOperAclFeature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 4, 1, 1),
    _CaqIpOperAclFeature_Type()
)
caqIpOperAclFeature.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqIpOperAclFeature.setStatus("current")
_CaqIpOperAclName_Type = SnmpAdminString
_CaqIpOperAclName_Object = MibTableColumn
caqIpOperAclName = _CaqIpOperAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 4, 1, 2),
    _CaqIpOperAclName_Type()
)
caqIpOperAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpOperAclName.setStatus("current")


class _CaqIpOperAclMapSource_Type(Bits):
    """Custom type caqIpOperAclMapSource based on Bits"""
    namedValues = NamedValues(
        *(("configured", 0),
          ("dot1x", 1),
          ("eou", 4),
          ("macAuth", 2),
          ("webAuth", 3))
    )

_CaqIpOperAclMapSource_Type.__name__ = "Bits"
_CaqIpOperAclMapSource_Object = MibTableColumn
caqIpOperAclMapSource = _CaqIpOperAclMapSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 4, 1, 3),
    _CaqIpOperAclMapSource_Type()
)
caqIpOperAclMapSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpOperAclMapSource.setStatus("current")
_CaqDownloadClassifierTable_Object = MibTable
caqDownloadClassifierTable = _CaqDownloadClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 5)
)
if mibBuilder.loadTexts:
    caqDownloadClassifierTable.setStatus("current")
_CaqDownloadClassifierEntry_Object = MibTableRow
caqDownloadClassifierEntry = _CaqDownloadClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 5, 1)
)
caqDownloadClassifierEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqDownloadAclFeature"),
)
if mibBuilder.loadTexts:
    caqDownloadClassifierEntry.setStatus("current")


class _CaqDownloadAclFeature_Type(Integer32):
    """Custom type caqDownloadAclFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egressIpQos", 2),
          ("ingressIpQos", 1),
          ("ipSecurity", 3))
    )


_CaqDownloadAclFeature_Type.__name__ = "Integer32"
_CaqDownloadAclFeature_Object = MibTableColumn
caqDownloadAclFeature = _CaqDownloadAclFeature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 5, 1, 1),
    _CaqDownloadAclFeature_Type()
)
caqDownloadAclFeature.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqDownloadAclFeature.setStatus("current")
_CaqDownloadClassifierAclName_Type = CaqAclName
_CaqDownloadClassifierAclName_Object = MibTableColumn
caqDownloadClassifierAclName = _CaqDownloadClassifierAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 5, 1, 2),
    _CaqDownloadClassifierAclName_Type()
)
caqDownloadClassifierAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqDownloadClassifierAclName.setStatus("current")


class _CaqDownloadMapSource_Type(Integer32):
    """Custom type caqDownloadMapSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 1),
          ("macAuth", 2))
    )


_CaqDownloadMapSource_Type.__name__ = "Integer32"
_CaqDownloadMapSource_Object = MibTableColumn
caqDownloadMapSource = _CaqDownloadMapSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 5, 1, 3),
    _CaqDownloadMapSource_Type()
)
caqDownloadMapSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqDownloadMapSource.setStatus("current")


class _CaqDownloadAclType_Type(Integer32):
    """Custom type caqDownloadAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pacl", 1),
          ("vacl", 2))
    )


_CaqDownloadAclType_Type.__name__ = "Integer32"
_CaqDownloadAclType_Object = MibTableColumn
caqDownloadAclType = _CaqDownloadAclType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 2, 5, 1, 4),
    _CaqDownloadAclType_Type()
)
caqDownloadAclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqDownloadAclType.setStatus("current")
_CaqAclObjects_ObjectIdentity = ObjectIdentity
caqAclObjects = _CaqAclObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3)
)


class _CaqAclCapabilities_Type(Bits):
    """Custom type caqAclCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("ipQos", 0),
          ("ipSecurity", 3),
          ("ipxQos", 1),
          ("ipxSecurity", 4),
          ("macQos", 2),
          ("macSecurity", 5))
    )

_CaqAclCapabilities_Type.__name__ = "Bits"
_CaqAclCapabilities_Object = MibScalar
caqAclCapabilities = _CaqAclCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 1),
    _CaqAclCapabilities_Type()
)
caqAclCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAclCapabilities.setStatus("current")
_CaqIpAceTable_Object = MibTable
caqIpAceTable = _CaqIpAceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2)
)
if mibBuilder.loadTexts:
    caqIpAceTable.setStatus("current")
_CaqIpAceEntry_Object = MibTableRow
caqIpAceEntry = _CaqIpAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1)
)
caqIpAceEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqIpAceFeature"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqIpAclName"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqIpAceIndex"),
)
if mibBuilder.loadTexts:
    caqIpAceEntry.setStatus("current")


class _CaqIpAceFeature_Type(Integer32):
    """Custom type caqIpAceFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qos", 1),
          ("security", 2))
    )


_CaqIpAceFeature_Type.__name__ = "Integer32"
_CaqIpAceFeature_Object = MibTableColumn
caqIpAceFeature = _CaqIpAceFeature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 1),
    _CaqIpAceFeature_Type()
)
caqIpAceFeature.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqIpAceFeature.setStatus("current")
_CaqIpAclName_Type = CaqAclName
_CaqIpAclName_Object = MibTableColumn
caqIpAclName = _CaqIpAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 2),
    _CaqIpAclName_Type()
)
caqIpAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqIpAclName.setStatus("current")


class _CaqIpAceIndex_Type(Unsigned32):
    """Custom type caqIpAceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CaqIpAceIndex_Type.__name__ = "Unsigned32"
_CaqIpAceIndex_Object = MibTableColumn
caqIpAceIndex = _CaqIpAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 3),
    _CaqIpAceIndex_Type()
)
caqIpAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqIpAceIndex.setStatus("current")


class _CaqIpAceMatchedAction_Type(Unsigned32):
    """Custom type caqIpAceMatchedAction based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CaqIpAceMatchedAction_Type.__name__ = "Unsigned32"
_CaqIpAceMatchedAction_Object = MibTableColumn
caqIpAceMatchedAction = _CaqIpAceMatchedAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 4),
    _CaqIpAceMatchedAction_Type()
)
caqIpAceMatchedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceMatchedAction.setStatus("current")


class _CaqIpAceProtocolType_Type(Unsigned32):
    """Custom type caqIpAceProtocolType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CaqIpAceProtocolType_Type.__name__ = "Unsigned32"
_CaqIpAceProtocolType_Object = MibTableColumn
caqIpAceProtocolType = _CaqIpAceProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 5),
    _CaqIpAceProtocolType_Type()
)
caqIpAceProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceProtocolType.setStatus("current")
_CaqIpAceAddrType_Type = InetAddressType
_CaqIpAceAddrType_Object = MibTableColumn
caqIpAceAddrType = _CaqIpAceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 6),
    _CaqIpAceAddrType_Type()
)
caqIpAceAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpAceAddrType.setStatus("current")
_CaqIpAceSrcIp_Type = InetAddress
_CaqIpAceSrcIp_Object = MibTableColumn
caqIpAceSrcIp = _CaqIpAceSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 7),
    _CaqIpAceSrcIp_Type()
)
caqIpAceSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceSrcIp.setStatus("current")
_CaqIpAceSrcIpMask_Type = InetAddress
_CaqIpAceSrcIpMask_Object = MibTableColumn
caqIpAceSrcIpMask = _CaqIpAceSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 8),
    _CaqIpAceSrcIpMask_Type()
)
caqIpAceSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceSrcIpMask.setStatus("current")


class _CaqIpAceSrcPortOp_Type(Integer32):
    """Custom type caqIpAceSrcPortOp based on Integer32"""
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
        *(("eq", 4),
          ("gt", 3),
          ("lt", 2),
          ("neq", 5),
          ("noOperator", 1),
          ("range", 6))
    )


_CaqIpAceSrcPortOp_Type.__name__ = "Integer32"
_CaqIpAceSrcPortOp_Object = MibTableColumn
caqIpAceSrcPortOp = _CaqIpAceSrcPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 9),
    _CaqIpAceSrcPortOp_Type()
)
caqIpAceSrcPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceSrcPortOp.setStatus("current")


class _CaqIpAceSrcPort_Type(Unsigned32):
    """Custom type caqIpAceSrcPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaqIpAceSrcPort_Type.__name__ = "Unsigned32"
_CaqIpAceSrcPort_Object = MibTableColumn
caqIpAceSrcPort = _CaqIpAceSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 10),
    _CaqIpAceSrcPort_Type()
)
caqIpAceSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceSrcPort.setStatus("current")


class _CaqIpAceSrcPortRange_Type(Unsigned32):
    """Custom type caqIpAceSrcPortRange based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaqIpAceSrcPortRange_Type.__name__ = "Unsigned32"
_CaqIpAceSrcPortRange_Object = MibTableColumn
caqIpAceSrcPortRange = _CaqIpAceSrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 11),
    _CaqIpAceSrcPortRange_Type()
)
caqIpAceSrcPortRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceSrcPortRange.setStatus("current")


class _CaqIpAceDestIp_Type(InetAddress):
    """Custom type caqIpAceDestIp based on InetAddress"""
    defaultHexValue = "00000000"


_CaqIpAceDestIp_Object = MibTableColumn
caqIpAceDestIp = _CaqIpAceDestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 12),
    _CaqIpAceDestIp_Type()
)
caqIpAceDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceDestIp.setStatus("current")


class _CaqIpAceDestIpMask_Type(InetAddress):
    """Custom type caqIpAceDestIpMask based on InetAddress"""
    defaultHexValue = "FFFFFFFF"


_CaqIpAceDestIpMask_Object = MibTableColumn
caqIpAceDestIpMask = _CaqIpAceDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 13),
    _CaqIpAceDestIpMask_Type()
)
caqIpAceDestIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceDestIpMask.setStatus("current")


class _CaqIpAceDestPortOp_Type(Integer32):
    """Custom type caqIpAceDestPortOp based on Integer32"""
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
        *(("eq", 4),
          ("gt", 3),
          ("lt", 2),
          ("neq", 5),
          ("noOperator", 1),
          ("range", 6))
    )


_CaqIpAceDestPortOp_Type.__name__ = "Integer32"
_CaqIpAceDestPortOp_Object = MibTableColumn
caqIpAceDestPortOp = _CaqIpAceDestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 14),
    _CaqIpAceDestPortOp_Type()
)
caqIpAceDestPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceDestPortOp.setStatus("current")


class _CaqIpAceDestPort_Type(Unsigned32):
    """Custom type caqIpAceDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaqIpAceDestPort_Type.__name__ = "Unsigned32"
_CaqIpAceDestPort_Object = MibTableColumn
caqIpAceDestPort = _CaqIpAceDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 15),
    _CaqIpAceDestPort_Type()
)
caqIpAceDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceDestPort.setStatus("current")


class _CaqIpAceDestPortRange_Type(Unsigned32):
    """Custom type caqIpAceDestPortRange based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaqIpAceDestPortRange_Type.__name__ = "Unsigned32"
_CaqIpAceDestPortRange_Object = MibTableColumn
caqIpAceDestPortRange = _CaqIpAceDestPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 16),
    _CaqIpAceDestPortRange_Type()
)
caqIpAceDestPortRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceDestPortRange.setStatus("current")


class _CaqIpAceTosMatchCriteria_Type(Integer32):
    """Custom type caqIpAceTosMatchCriteria based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("matchDscp", 2),
          ("matchIpPrec", 3),
          ("none", 1))
    )


_CaqIpAceTosMatchCriteria_Type.__name__ = "Integer32"
_CaqIpAceTosMatchCriteria_Object = MibTableColumn
caqIpAceTosMatchCriteria = _CaqIpAceTosMatchCriteria_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 17),
    _CaqIpAceTosMatchCriteria_Type()
)
caqIpAceTosMatchCriteria.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceTosMatchCriteria.setStatus("current")


class _CaqIpAceIpPrec_Type(CaqIpPrecedence):
    """Custom type caqIpAceIpPrec based on CaqIpPrecedence"""
    defaultValue = 0


_CaqIpAceIpPrec_Object = MibTableColumn
caqIpAceIpPrec = _CaqIpAceIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 18),
    _CaqIpAceIpPrec_Type()
)
caqIpAceIpPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceIpPrec.setStatus("current")


class _CaqIpAceDscp_Type(Dscp):
    """Custom type caqIpAceDscp based on Dscp"""
    defaultValue = 0


_CaqIpAceDscp_Object = MibTableColumn
caqIpAceDscp = _CaqIpAceDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 19),
    _CaqIpAceDscp_Type()
)
caqIpAceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceDscp.setStatus("current")


class _CaqIpAceProtocolMatchCriteria_Type(Integer32):
    """Custom type caqIpAceProtocolMatchCriteria based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("matchEapoudp", 7),
          ("matchEstablished", 5),
          ("matchIcmpType", 3),
          ("matchIcmpTypeAndCode", 4),
          ("matchIgmpType", 2),
          ("matchSecurityId", 6),
          ("matchUrlRedirect", 8),
          ("none", 1))
    )


_CaqIpAceProtocolMatchCriteria_Type.__name__ = "Integer32"
_CaqIpAceProtocolMatchCriteria_Object = MibTableColumn
caqIpAceProtocolMatchCriteria = _CaqIpAceProtocolMatchCriteria_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 20),
    _CaqIpAceProtocolMatchCriteria_Type()
)
caqIpAceProtocolMatchCriteria.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceProtocolMatchCriteria.setStatus("current")


class _CaqIpAceIcmpType_Type(Unsigned32):
    """Custom type caqIpAceIcmpType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CaqIpAceIcmpType_Type.__name__ = "Unsigned32"
_CaqIpAceIcmpType_Object = MibTableColumn
caqIpAceIcmpType = _CaqIpAceIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 21),
    _CaqIpAceIcmpType_Type()
)
caqIpAceIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceIcmpType.setStatus("current")


class _CaqIpAceIcmpCode_Type(Unsigned32):
    """Custom type caqIpAceIcmpCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CaqIpAceIcmpCode_Type.__name__ = "Unsigned32"
_CaqIpAceIcmpCode_Object = MibTableColumn
caqIpAceIcmpCode = _CaqIpAceIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 22),
    _CaqIpAceIcmpCode_Type()
)
caqIpAceIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceIcmpCode.setStatus("current")


class _CaqIpAceIgmpType_Type(Unsigned32):
    """Custom type caqIpAceIgmpType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CaqIpAceIgmpType_Type.__name__ = "Unsigned32"
_CaqIpAceIgmpType_Object = MibTableColumn
caqIpAceIgmpType = _CaqIpAceIgmpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 23),
    _CaqIpAceIgmpType_Type()
)
caqIpAceIgmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceIgmpType.setStatus("current")


class _CaqIpAceOrderPosition_Type(Unsigned32):
    """Custom type caqIpAceOrderPosition based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaqIpAceOrderPosition_Type.__name__ = "Unsigned32"
_CaqIpAceOrderPosition_Object = MibTableColumn
caqIpAceOrderPosition = _CaqIpAceOrderPosition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 24),
    _CaqIpAceOrderPosition_Type()
)
caqIpAceOrderPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpAceOrderPosition.setStatus("current")


class _CaqIpAceBeforePosition_Type(Unsigned32):
    """Custom type caqIpAceBeforePosition based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaqIpAceBeforePosition_Type.__name__ = "Unsigned32"
_CaqIpAceBeforePosition_Object = MibTableColumn
caqIpAceBeforePosition = _CaqIpAceBeforePosition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 25),
    _CaqIpAceBeforePosition_Type()
)
caqIpAceBeforePosition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceBeforePosition.setStatus("current")
_CaqIpAceStatus_Type = RowStatus
_CaqIpAceStatus_Object = MibTableColumn
caqIpAceStatus = _CaqIpAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 26),
    _CaqIpAceStatus_Type()
)
caqIpAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceStatus.setStatus("current")


class _CaqIpAceSecurityId_Type(Unsigned32):
    """Custom type caqIpAceSecurityId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 233),
    )


_CaqIpAceSecurityId_Type.__name__ = "Unsigned32"
_CaqIpAceSecurityId_Object = MibTableColumn
caqIpAceSecurityId = _CaqIpAceSecurityId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 27),
    _CaqIpAceSecurityId_Type()
)
caqIpAceSecurityId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceSecurityId.setStatus("current")
_CaqIpAceSrcGroup_Type = SnmpAdminString
_CaqIpAceSrcGroup_Object = MibTableColumn
caqIpAceSrcGroup = _CaqIpAceSrcGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 28),
    _CaqIpAceSrcGroup_Type()
)
caqIpAceSrcGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceSrcGroup.setStatus("current")
_CaqIpAceDestGroup_Type = SnmpAdminString
_CaqIpAceDestGroup_Object = MibTableColumn
caqIpAceDestGroup = _CaqIpAceDestGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 29),
    _CaqIpAceDestGroup_Type()
)
caqIpAceDestGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpAceDestGroup.setStatus("current")


class _CaqIpAceType_Type(Integer32):
    """Custom type caqIpAceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("systemGenerated", 2))
    )


_CaqIpAceType_Type.__name__ = "Integer32"
_CaqIpAceType_Object = MibTableColumn
caqIpAceType = _CaqIpAceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 2, 1, 30),
    _CaqIpAceType_Type()
)
caqIpAceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpAceType.setStatus("current")
_CaqIpxAceTable_Object = MibTable
caqIpxAceTable = _CaqIpxAceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 3)
)
if mibBuilder.loadTexts:
    caqIpxAceTable.setStatus("current")
_CaqIpxAceEntry_Object = MibTableRow
caqIpxAceEntry = _CaqIpxAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 3, 1)
)
caqIpxAceEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqIpxAceFeature"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqIpxAclName"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqIpxAceIndex"),
)
if mibBuilder.loadTexts:
    caqIpxAceEntry.setStatus("current")


class _CaqIpxAceFeature_Type(Integer32):
    """Custom type caqIpxAceFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qos", 1),
          ("security", 2))
    )


_CaqIpxAceFeature_Type.__name__ = "Integer32"
_CaqIpxAceFeature_Object = MibTableColumn
caqIpxAceFeature = _CaqIpxAceFeature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 3, 1, 1),
    _CaqIpxAceFeature_Type()
)
caqIpxAceFeature.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqIpxAceFeature.setStatus("current")
_CaqIpxAclName_Type = CaqAclName
_CaqIpxAclName_Object = MibTableColumn
caqIpxAclName = _CaqIpxAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 3, 1, 2),
    _CaqIpxAclName_Type()
)
caqIpxAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqIpxAclName.setStatus("current")


class _CaqIpxAceIndex_Type(Unsigned32):
    """Custom type caqIpxAceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CaqIpxAceIndex_Type.__name__ = "Unsigned32"
_CaqIpxAceIndex_Object = MibTableColumn
caqIpxAceIndex = _CaqIpxAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 3, 1, 3),
    _CaqIpxAceIndex_Type()
)
caqIpxAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqIpxAceIndex.setStatus("current")


class _CaqIpxAceMatchedAction_Type(Unsigned32):
    """Custom type caqIpxAceMatchedAction based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CaqIpxAceMatchedAction_Type.__name__ = "Unsigned32"
_CaqIpxAceMatchedAction_Object = MibTableColumn
caqIpxAceMatchedAction = _CaqIpxAceMatchedAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 3, 1, 4),
    _CaqIpxAceMatchedAction_Type()
)
caqIpxAceMatchedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpxAceMatchedAction.setStatus("current")


class _CaqIpxAceSrcNet_Type(OctetString):
    """Custom type caqIpxAceSrcNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CaqIpxAceSrcNet_Type.__name__ = "OctetString"
_CaqIpxAceSrcNet_Object = MibTableColumn
caqIpxAceSrcNet = _CaqIpxAceSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 3, 1, 5),
    _CaqIpxAceSrcNet_Type()
)
caqIpxAceSrcNet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpxAceSrcNet.setStatus("current")


class _CaqIpxAceDestMatchCriteria_Type(Bits):
    """Custom type caqIpxAceDestMatchCriteria based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("matchIpxDestNet", 1),
          ("matchIpxDestNetMask", 3),
          ("matchIpxDestNode", 2),
          ("matchIpxDestNodeMask", 4),
          ("matchProtocol", 0))
    )

_CaqIpxAceDestMatchCriteria_Type.__name__ = "Bits"
_CaqIpxAceDestMatchCriteria_Object = MibTableColumn
caqIpxAceDestMatchCriteria = _CaqIpxAceDestMatchCriteria_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 3, 1, 6),
    _CaqIpxAceDestMatchCriteria_Type()
)
caqIpxAceDestMatchCriteria.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpxAceDestMatchCriteria.setStatus("current")


class _CaqIpxAceProtocolType_Type(Unsigned32):
    """Custom type caqIpxAceProtocolType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CaqIpxAceProtocolType_Type.__name__ = "Unsigned32"
_CaqIpxAceProtocolType_Object = MibTableColumn
caqIpxAceProtocolType = _CaqIpxAceProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 3, 1, 7),
    _CaqIpxAceProtocolType_Type()
)
caqIpxAceProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpxAceProtocolType.setStatus("current")


class _CaqIpxAceDestNet_Type(OctetString):
    """Custom type caqIpxAceDestNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CaqIpxAceDestNet_Type.__name__ = "OctetString"
_CaqIpxAceDestNet_Object = MibTableColumn
caqIpxAceDestNet = _CaqIpxAceDestNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 3, 1, 8),
    _CaqIpxAceDestNet_Type()
)
caqIpxAceDestNet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpxAceDestNet.setStatus("current")


class _CaqIpxAceDestNode_Type(OctetString):
    """Custom type caqIpxAceDestNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CaqIpxAceDestNode_Type.__name__ = "OctetString"
_CaqIpxAceDestNode_Object = MibTableColumn
caqIpxAceDestNode = _CaqIpxAceDestNode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 3, 1, 9),
    _CaqIpxAceDestNode_Type()
)
caqIpxAceDestNode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpxAceDestNode.setStatus("current")


class _CaqIpxAceDestNetMask_Type(OctetString):
    """Custom type caqIpxAceDestNetMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CaqIpxAceDestNetMask_Type.__name__ = "OctetString"
_CaqIpxAceDestNetMask_Object = MibTableColumn
caqIpxAceDestNetMask = _CaqIpxAceDestNetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 3, 1, 10),
    _CaqIpxAceDestNetMask_Type()
)
caqIpxAceDestNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpxAceDestNetMask.setStatus("current")


class _CaqIpxAceDestNodeMask_Type(OctetString):
    """Custom type caqIpxAceDestNodeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CaqIpxAceDestNodeMask_Type.__name__ = "OctetString"
_CaqIpxAceDestNodeMask_Object = MibTableColumn
caqIpxAceDestNodeMask = _CaqIpxAceDestNodeMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 3, 1, 11),
    _CaqIpxAceDestNodeMask_Type()
)
caqIpxAceDestNodeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpxAceDestNodeMask.setStatus("current")


class _CaqIpxAceOrderPosition_Type(Unsigned32):
    """Custom type caqIpxAceOrderPosition based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaqIpxAceOrderPosition_Type.__name__ = "Unsigned32"
_CaqIpxAceOrderPosition_Object = MibTableColumn
caqIpxAceOrderPosition = _CaqIpxAceOrderPosition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 3, 1, 12),
    _CaqIpxAceOrderPosition_Type()
)
caqIpxAceOrderPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpxAceOrderPosition.setStatus("current")


class _CaqIpxAceBeforePosition_Type(Unsigned32):
    """Custom type caqIpxAceBeforePosition based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaqIpxAceBeforePosition_Type.__name__ = "Unsigned32"
_CaqIpxAceBeforePosition_Object = MibTableColumn
caqIpxAceBeforePosition = _CaqIpxAceBeforePosition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 3, 1, 13),
    _CaqIpxAceBeforePosition_Type()
)
caqIpxAceBeforePosition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpxAceBeforePosition.setStatus("current")
_CaqIpxAceStatus_Type = RowStatus
_CaqIpxAceStatus_Object = MibTableColumn
caqIpxAceStatus = _CaqIpxAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 3, 1, 14),
    _CaqIpxAceStatus_Type()
)
caqIpxAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqIpxAceStatus.setStatus("current")
_CaqMacAceTable_Object = MibTable
caqMacAceTable = _CaqMacAceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 4)
)
if mibBuilder.loadTexts:
    caqMacAceTable.setStatus("current")
_CaqMacAceEntry_Object = MibTableRow
caqMacAceEntry = _CaqMacAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 4, 1)
)
caqMacAceEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqMacAceFeature"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqMacAclName"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqMacAceIndex"),
)
if mibBuilder.loadTexts:
    caqMacAceEntry.setStatus("current")


class _CaqMacAceFeature_Type(Integer32):
    """Custom type caqMacAceFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qos", 1),
          ("security", 2))
    )


_CaqMacAceFeature_Type.__name__ = "Integer32"
_CaqMacAceFeature_Object = MibTableColumn
caqMacAceFeature = _CaqMacAceFeature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 4, 1, 1),
    _CaqMacAceFeature_Type()
)
caqMacAceFeature.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqMacAceFeature.setStatus("current")
_CaqMacAclName_Type = CaqAclName
_CaqMacAclName_Object = MibTableColumn
caqMacAclName = _CaqMacAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 4, 1, 2),
    _CaqMacAclName_Type()
)
caqMacAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqMacAclName.setStatus("current")


class _CaqMacAceIndex_Type(Unsigned32):
    """Custom type caqMacAceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CaqMacAceIndex_Type.__name__ = "Unsigned32"
_CaqMacAceIndex_Object = MibTableColumn
caqMacAceIndex = _CaqMacAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 4, 1, 3),
    _CaqMacAceIndex_Type()
)
caqMacAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqMacAceIndex.setStatus("current")


class _CaqMacAceMatchedAction_Type(Unsigned32):
    """Custom type caqMacAceMatchedAction based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CaqMacAceMatchedAction_Type.__name__ = "Unsigned32"
_CaqMacAceMatchedAction_Object = MibTableColumn
caqMacAceMatchedAction = _CaqMacAceMatchedAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 4, 1, 4),
    _CaqMacAceMatchedAction_Type()
)
caqMacAceMatchedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqMacAceMatchedAction.setStatus("current")
_CaqMacAceSrcMac_Type = MacAddress
_CaqMacAceSrcMac_Object = MibTableColumn
caqMacAceSrcMac = _CaqMacAceSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 4, 1, 5),
    _CaqMacAceSrcMac_Type()
)
caqMacAceSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqMacAceSrcMac.setStatus("current")
_CaqMacAceSrcMacMask_Type = MacAddress
_CaqMacAceSrcMacMask_Object = MibTableColumn
caqMacAceSrcMacMask = _CaqMacAceSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 4, 1, 6),
    _CaqMacAceSrcMacMask_Type()
)
caqMacAceSrcMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqMacAceSrcMacMask.setStatus("current")
_CaqMacAceDestMac_Type = MacAddress
_CaqMacAceDestMac_Object = MibTableColumn
caqMacAceDestMac = _CaqMacAceDestMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 4, 1, 7),
    _CaqMacAceDestMac_Type()
)
caqMacAceDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqMacAceDestMac.setStatus("current")
_CaqMacAceDestMacMask_Type = MacAddress
_CaqMacAceDestMacMask_Object = MibTableColumn
caqMacAceDestMacMask = _CaqMacAceDestMacMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 4, 1, 8),
    _CaqMacAceDestMacMask_Type()
)
caqMacAceDestMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqMacAceDestMacMask.setStatus("current")


class _CaqMacAceEthertype_Type(Unsigned32):
    """Custom type caqMacAceEthertype based on Unsigned32"""
    defaultHexValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaqMacAceEthertype_Type.__name__ = "Unsigned32"
_CaqMacAceEthertype_Object = MibTableColumn
caqMacAceEthertype = _CaqMacAceEthertype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 4, 1, 9),
    _CaqMacAceEthertype_Type()
)
caqMacAceEthertype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqMacAceEthertype.setStatus("current")


class _CaqMacAceOrderPosition_Type(Unsigned32):
    """Custom type caqMacAceOrderPosition based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaqMacAceOrderPosition_Type.__name__ = "Unsigned32"
_CaqMacAceOrderPosition_Object = MibTableColumn
caqMacAceOrderPosition = _CaqMacAceOrderPosition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 4, 1, 10),
    _CaqMacAceOrderPosition_Type()
)
caqMacAceOrderPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqMacAceOrderPosition.setStatus("current")


class _CaqMacAceBeforePosition_Type(Unsigned32):
    """Custom type caqMacAceBeforePosition based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaqMacAceBeforePosition_Type.__name__ = "Unsigned32"
_CaqMacAceBeforePosition_Object = MibTableColumn
caqMacAceBeforePosition = _CaqMacAceBeforePosition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 4, 1, 11),
    _CaqMacAceBeforePosition_Type()
)
caqMacAceBeforePosition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqMacAceBeforePosition.setStatus("current")
_CaqMacAceStatus_Type = RowStatus
_CaqMacAceStatus_Object = MibTableColumn
caqMacAceStatus = _CaqMacAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 4, 1, 12),
    _CaqMacAceStatus_Type()
)
caqMacAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqMacAceStatus.setStatus("current")


class _CaqMacAceMatchCriteria_Type(Bits):
    """Custom type caqMacAceMatchCriteria based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("matchCos", 0),
          ("matchVlan", 1))
    )

_CaqMacAceMatchCriteria_Type.__name__ = "Bits"
_CaqMacAceMatchCriteria_Object = MibTableColumn
caqMacAceMatchCriteria = _CaqMacAceMatchCriteria_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 4, 1, 13),
    _CaqMacAceMatchCriteria_Type()
)
caqMacAceMatchCriteria.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqMacAceMatchCriteria.setStatus("current")
_CaqMacAceCos_Type = QosLayer2Cos
_CaqMacAceCos_Object = MibTableColumn
caqMacAceCos = _CaqMacAceCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 4, 1, 14),
    _CaqMacAceCos_Type()
)
caqMacAceCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqMacAceCos.setStatus("current")
_CaqMacAceVlan_Type = VlanIndex
_CaqMacAceVlan_Object = MibTableColumn
caqMacAceVlan = _CaqMacAceVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 4, 1, 15),
    _CaqMacAceVlan_Type()
)
caqMacAceVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqMacAceVlan.setStatus("current")


class _CaqFlowPolicingCpb_Type(Bits):
    """Custom type caqFlowPolicingCpb based on Bits"""
    namedValues = NamedValues(
        *(("aggregate", 1),
          ("microFlow", 0))
    )

_CaqFlowPolicingCpb_Type.__name__ = "Bits"
_CaqFlowPolicingCpb_Object = MibScalar
caqFlowPolicingCpb = _CaqFlowPolicingCpb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 5),
    _CaqFlowPolicingCpb_Type()
)
caqFlowPolicingCpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqFlowPolicingCpb.setStatus("current")
_CaqQosActionSelectTable_Object = MibTable
caqQosActionSelectTable = _CaqQosActionSelectTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 6)
)
if mibBuilder.loadTexts:
    caqQosActionSelectTable.setStatus("current")
_CaqQosActionSelectEntry_Object = MibTableRow
caqQosActionSelectEntry = _CaqQosActionSelectEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 6, 1)
)
caqQosActionSelectEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqQosActionSelectIndex"),
)
if mibBuilder.loadTexts:
    caqQosActionSelectEntry.setStatus("current")


class _CaqQosActionSelectIndex_Type(Unsigned32):
    """Custom type caqQosActionSelectIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CaqQosActionSelectIndex_Type.__name__ = "Unsigned32"
_CaqQosActionSelectIndex_Object = MibTableColumn
caqQosActionSelectIndex = _CaqQosActionSelectIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 6, 1, 1),
    _CaqQosActionSelectIndex_Type()
)
caqQosActionSelectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqQosActionSelectIndex.setStatus("current")


class _CaqQosActionSelectTrust_Type(Integer32):
    """Custom type caqQosActionSelectTrust based on Integer32"""
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
        *(("noTrust", 1),
          ("trustCos", 2),
          ("trustDscp", 4),
          ("trustIpPrec", 3))
    )


_CaqQosActionSelectTrust_Type.__name__ = "Integer32"
_CaqQosActionSelectTrust_Object = MibTableColumn
caqQosActionSelectTrust = _CaqQosActionSelectTrust_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 6, 1, 2),
    _CaqQosActionSelectTrust_Type()
)
caqQosActionSelectTrust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqQosActionSelectTrust.setStatus("current")
_CaqQosActionSelectDscp_Type = Dscp
_CaqQosActionSelectDscp_Object = MibTableColumn
caqQosActionSelectDscp = _CaqQosActionSelectDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 6, 1, 4),
    _CaqQosActionSelectDscp_Type()
)
caqQosActionSelectDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqQosActionSelectDscp.setStatus("current")
_CaqQosActionSelectMicroflow_Type = CaqPolicerNameOrEmpty
_CaqQosActionSelectMicroflow_Object = MibTableColumn
caqQosActionSelectMicroflow = _CaqQosActionSelectMicroflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 6, 1, 5),
    _CaqQosActionSelectMicroflow_Type()
)
caqQosActionSelectMicroflow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqQosActionSelectMicroflow.setStatus("current")
_CaqQosActionSelectAggregate_Type = CaqPolicerNameOrEmpty
_CaqQosActionSelectAggregate_Object = MibTableColumn
caqQosActionSelectAggregate = _CaqQosActionSelectAggregate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 6, 1, 6),
    _CaqQosActionSelectAggregate_Type()
)
caqQosActionSelectAggregate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqQosActionSelectAggregate.setStatus("current")
_CaqQosActionSelectStatus_Type = RowStatus
_CaqQosActionSelectStatus_Object = MibTableColumn
caqQosActionSelectStatus = _CaqQosActionSelectStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 6, 1, 7),
    _CaqQosActionSelectStatus_Type()
)
caqQosActionSelectStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqQosActionSelectStatus.setStatus("current")
_CaqFlowPolicerExcessRateSupport_Type = TruthValue
_CaqFlowPolicerExcessRateSupport_Object = MibScalar
caqFlowPolicerExcessRateSupport = _CaqFlowPolicerExcessRateSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 7),
    _CaqFlowPolicerExcessRateSupport_Type()
)
caqFlowPolicerExcessRateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqFlowPolicerExcessRateSupport.setStatus("current")
_CaqFlowPolicerTable_Object = MibTable
caqFlowPolicerTable = _CaqFlowPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 8)
)
if mibBuilder.loadTexts:
    caqFlowPolicerTable.setStatus("current")
_CaqFlowPolicerEntry_Object = MibTableRow
caqFlowPolicerEntry = _CaqFlowPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 8, 1)
)
caqFlowPolicerEntry.setIndexNames(
    (1, "CISCO-CATOS-ACL-QOS-MIB", "caqFlowPolicerName"),
)
if mibBuilder.loadTexts:
    caqFlowPolicerEntry.setStatus("current")
_CaqFlowPolicerName_Type = CaqPolicerName
_CaqFlowPolicerName_Object = MibTableColumn
caqFlowPolicerName = _CaqFlowPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 8, 1, 1),
    _CaqFlowPolicerName_Type()
)
caqFlowPolicerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqFlowPolicerName.setStatus("current")


class _CaqFlowPolicerType_Type(Integer32):
    """Custom type caqFlowPolicerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 2),
          ("microflow", 1))
    )


_CaqFlowPolicerType_Type.__name__ = "Integer32"
_CaqFlowPolicerType_Object = MibTableColumn
caqFlowPolicerType = _CaqFlowPolicerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 8, 1, 2),
    _CaqFlowPolicerType_Type()
)
caqFlowPolicerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqFlowPolicerType.setStatus("current")


class _CaqFlowPolicerNormalRateRequest_Type(Integer32):
    """Custom type caqFlowPolicerNormalRateRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 8000000),
    )


_CaqFlowPolicerNormalRateRequest_Type.__name__ = "Integer32"
_CaqFlowPolicerNormalRateRequest_Object = MibTableColumn
caqFlowPolicerNormalRateRequest = _CaqFlowPolicerNormalRateRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 8, 1, 3),
    _CaqFlowPolicerNormalRateRequest_Type()
)
caqFlowPolicerNormalRateRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqFlowPolicerNormalRateRequest.setStatus("current")
if mibBuilder.loadTexts:
    caqFlowPolicerNormalRateRequest.setUnits("kbps")
_CaqFlowPolicerNormalRateGrant_Type = Integer32
_CaqFlowPolicerNormalRateGrant_Object = MibTableColumn
caqFlowPolicerNormalRateGrant = _CaqFlowPolicerNormalRateGrant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 8, 1, 4),
    _CaqFlowPolicerNormalRateGrant_Type()
)
caqFlowPolicerNormalRateGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqFlowPolicerNormalRateGrant.setStatus("current")
if mibBuilder.loadTexts:
    caqFlowPolicerNormalRateGrant.setUnits("kbps")


class _CaqFlowPolicerNormalRateAction_Type(Integer32):
    """Custom type caqFlowPolicerNormalRateAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("policedDscp", 2))
    )


_CaqFlowPolicerNormalRateAction_Type.__name__ = "Integer32"
_CaqFlowPolicerNormalRateAction_Object = MibTableColumn
caqFlowPolicerNormalRateAction = _CaqFlowPolicerNormalRateAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 8, 1, 5),
    _CaqFlowPolicerNormalRateAction_Type()
)
caqFlowPolicerNormalRateAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqFlowPolicerNormalRateAction.setStatus("current")


class _CaqFlowPolicerExcessRateRequest_Type(Integer32):
    """Custom type caqFlowPolicerExcessRateRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 8000000),
    )


_CaqFlowPolicerExcessRateRequest_Type.__name__ = "Integer32"
_CaqFlowPolicerExcessRateRequest_Object = MibTableColumn
caqFlowPolicerExcessRateRequest = _CaqFlowPolicerExcessRateRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 8, 1, 6),
    _CaqFlowPolicerExcessRateRequest_Type()
)
caqFlowPolicerExcessRateRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqFlowPolicerExcessRateRequest.setStatus("current")
if mibBuilder.loadTexts:
    caqFlowPolicerExcessRateRequest.setUnits("kbps")
_CaqFlowPolicerExcessRateGrant_Type = Integer32
_CaqFlowPolicerExcessRateGrant_Object = MibTableColumn
caqFlowPolicerExcessRateGrant = _CaqFlowPolicerExcessRateGrant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 8, 1, 7),
    _CaqFlowPolicerExcessRateGrant_Type()
)
caqFlowPolicerExcessRateGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqFlowPolicerExcessRateGrant.setStatus("current")
if mibBuilder.loadTexts:
    caqFlowPolicerExcessRateGrant.setUnits("kbps")


class _CaqFlowPolicerExcessRateAction_Type(Integer32):
    """Custom type caqFlowPolicerExcessRateAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("policedDscp", 2))
    )


_CaqFlowPolicerExcessRateAction_Type.__name__ = "Integer32"
_CaqFlowPolicerExcessRateAction_Object = MibTableColumn
caqFlowPolicerExcessRateAction = _CaqFlowPolicerExcessRateAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 8, 1, 8),
    _CaqFlowPolicerExcessRateAction_Type()
)
caqFlowPolicerExcessRateAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqFlowPolicerExcessRateAction.setStatus("current")


class _CaqFlowPolicerBurstSizeRequest_Type(Integer32):
    """Custom type caqFlowPolicerBurstSizeRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32000),
    )


_CaqFlowPolicerBurstSizeRequest_Type.__name__ = "Integer32"
_CaqFlowPolicerBurstSizeRequest_Object = MibTableColumn
caqFlowPolicerBurstSizeRequest = _CaqFlowPolicerBurstSizeRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 8, 1, 9),
    _CaqFlowPolicerBurstSizeRequest_Type()
)
caqFlowPolicerBurstSizeRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqFlowPolicerBurstSizeRequest.setStatus("current")
if mibBuilder.loadTexts:
    caqFlowPolicerBurstSizeRequest.setUnits("kilo-bits")
_CaqFlowPolicerBurstSizeGrant_Type = Integer32
_CaqFlowPolicerBurstSizeGrant_Object = MibTableColumn
caqFlowPolicerBurstSizeGrant = _CaqFlowPolicerBurstSizeGrant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 8, 1, 10),
    _CaqFlowPolicerBurstSizeGrant_Type()
)
caqFlowPolicerBurstSizeGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqFlowPolicerBurstSizeGrant.setStatus("current")
if mibBuilder.loadTexts:
    caqFlowPolicerBurstSizeGrant.setUnits("kilo-bits")
_CaqFlowPolicerStatus_Type = RowStatus
_CaqFlowPolicerStatus_Object = MibTableColumn
caqFlowPolicerStatus = _CaqFlowPolicerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 8, 1, 11),
    _CaqFlowPolicerStatus_Type()
)
caqFlowPolicerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqFlowPolicerStatus.setStatus("current")


class _CaqFlowPolicerExcessBurstRequest_Type(Unsigned32):
    """Custom type caqFlowPolicerExcessBurstRequest based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32000),
    )


_CaqFlowPolicerExcessBurstRequest_Type.__name__ = "Unsigned32"
_CaqFlowPolicerExcessBurstRequest_Object = MibTableColumn
caqFlowPolicerExcessBurstRequest = _CaqFlowPolicerExcessBurstRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 8, 1, 12),
    _CaqFlowPolicerExcessBurstRequest_Type()
)
caqFlowPolicerExcessBurstRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqFlowPolicerExcessBurstRequest.setStatus("current")
if mibBuilder.loadTexts:
    caqFlowPolicerExcessBurstRequest.setUnits("kilo-bits")


class _CaqFlowPolicerExcessBurstGrant_Type(Unsigned32):
    """Custom type caqFlowPolicerExcessBurstGrant based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32000),
    )


_CaqFlowPolicerExcessBurstGrant_Type.__name__ = "Unsigned32"
_CaqFlowPolicerExcessBurstGrant_Object = MibTableColumn
caqFlowPolicerExcessBurstGrant = _CaqFlowPolicerExcessBurstGrant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 8, 1, 13),
    _CaqFlowPolicerExcessBurstGrant_Type()
)
caqFlowPolicerExcessBurstGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqFlowPolicerExcessBurstGrant.setStatus("current")
if mibBuilder.loadTexts:
    caqFlowPolicerExcessBurstGrant.setUnits("kilo-bits")
_CaqSecurityActionTable_Object = MibTable
caqSecurityActionTable = _CaqSecurityActionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 9)
)
if mibBuilder.loadTexts:
    caqSecurityActionTable.setStatus("current")
_CaqSecurityActionEntry_Object = MibTableRow
caqSecurityActionEntry = _CaqSecurityActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 9, 1)
)
caqSecurityActionEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqSecurityActionIndex"),
)
if mibBuilder.loadTexts:
    caqSecurityActionEntry.setStatus("current")


class _CaqSecurityActionIndex_Type(Unsigned32):
    """Custom type caqSecurityActionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CaqSecurityActionIndex_Type.__name__ = "Unsigned32"
_CaqSecurityActionIndex_Object = MibTableColumn
caqSecurityActionIndex = _CaqSecurityActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 9, 1, 1),
    _CaqSecurityActionIndex_Type()
)
caqSecurityActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqSecurityActionIndex.setStatus("current")


class _CaqSecurityAction_Type(Integer32):
    """Custom type caqSecurityAction based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("denyArpInspWithLog", 7),
          ("denyArpInspection", 6),
          ("denyWithLog", 5),
          ("include", 9),
          ("permit", 1),
          ("permitArpInspection", 8),
          ("redirect", 3),
          ("redirectWithAdj", 4))
    )


_CaqSecurityAction_Type.__name__ = "Integer32"
_CaqSecurityAction_Object = MibTableColumn
caqSecurityAction = _CaqSecurityAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 9, 1, 2),
    _CaqSecurityAction_Type()
)
caqSecurityAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqSecurityAction.setStatus("current")


class _CaqSecurityRedirectPortList_Type(OctetString):
    """Custom type caqSecurityRedirectPortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CaqSecurityRedirectPortList_Type.__name__ = "OctetString"
_CaqSecurityRedirectPortList_Object = MibTableColumn
caqSecurityRedirectPortList = _CaqSecurityRedirectPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 9, 1, 3),
    _CaqSecurityRedirectPortList_Type()
)
caqSecurityRedirectPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqSecurityRedirectPortList.setStatus("deprecated")


class _CaqSecurityCapture_Type(TruthValue):
    """Custom type caqSecurityCapture based on TruthValue"""


_CaqSecurityCapture_Object = MibTableColumn
caqSecurityCapture = _CaqSecurityCapture_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 9, 1, 4),
    _CaqSecurityCapture_Type()
)
caqSecurityCapture.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqSecurityCapture.setStatus("current")
_CaqSecurityActionStatus_Type = RowStatus
_CaqSecurityActionStatus_Object = MibTableColumn
caqSecurityActionStatus = _CaqSecurityActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 9, 1, 5),
    _CaqSecurityActionStatus_Type()
)
caqSecurityActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqSecurityActionStatus.setStatus("current")


class _CaqSecurityAdjIndex_Type(Unsigned32):
    """Custom type caqSecurityAdjIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaqSecurityAdjIndex_Type.__name__ = "Unsigned32"
_CaqSecurityAdjIndex_Object = MibTableColumn
caqSecurityAdjIndex = _CaqSecurityAdjIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 9, 1, 6),
    _CaqSecurityAdjIndex_Type()
)
caqSecurityAdjIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqSecurityAdjIndex.setStatus("current")


class _CaqSecurityArpMacAddress_Type(MacAddress):
    """Custom type caqSecurityArpMacAddress based on MacAddress"""
    defaultHexValue = "FFFFFFFFFFFF"


_CaqSecurityArpMacAddress_Object = MibTableColumn
caqSecurityArpMacAddress = _CaqSecurityArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 9, 1, 7),
    _CaqSecurityArpMacAddress_Type()
)
caqSecurityArpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqSecurityArpMacAddress.setStatus("current")


class _CaqSecurityRedirect2kPortList_Type(OctetString):
    """Custom type caqSecurityRedirect2kPortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CaqSecurityRedirect2kPortList_Type.__name__ = "OctetString"
_CaqSecurityRedirect2kPortList_Object = MibTableColumn
caqSecurityRedirect2kPortList = _CaqSecurityRedirect2kPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 9, 1, 8),
    _CaqSecurityRedirect2kPortList_Type()
)
caqSecurityRedirect2kPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqSecurityRedirect2kPortList.setStatus("current")


class _CaqSecurityDownloadedAceFeature_Type(Integer32):
    """Custom type caqSecurityDownloadedAceFeature based on Integer32"""
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
        *(("dot1x", 2),
          ("eou", 5),
          ("ipPhone", 6),
          ("macAuth", 3),
          ("notApplicable", 1),
          ("webAuth", 4))
    )


_CaqSecurityDownloadedAceFeature_Type.__name__ = "Integer32"
_CaqSecurityDownloadedAceFeature_Object = MibTableColumn
caqSecurityDownloadedAceFeature = _CaqSecurityDownloadedAceFeature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 9, 1, 9),
    _CaqSecurityDownloadedAceFeature_Type()
)
caqSecurityDownloadedAceFeature.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqSecurityDownloadedAceFeature.setStatus("current")
_CaqSecurityAclCaptureIfTable_Object = MibTable
caqSecurityAclCaptureIfTable = _CaqSecurityAclCaptureIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 10)
)
if mibBuilder.loadTexts:
    caqSecurityAclCaptureIfTable.setStatus("current")
_CaqSecurityAclCaptureIfEntry_Object = MibTableRow
caqSecurityAclCaptureIfEntry = _CaqSecurityAclCaptureIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 10, 1)
)
caqSecurityAclCaptureIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    caqSecurityAclCaptureIfEntry.setStatus("current")


class _CaqSecurityAclCaptureEnable_Type(TruthValue):
    """Custom type caqSecurityAclCaptureEnable based on TruthValue"""


_CaqSecurityAclCaptureEnable_Object = MibTableColumn
caqSecurityAclCaptureEnable = _CaqSecurityAclCaptureEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 10, 1, 1),
    _CaqSecurityAclCaptureEnable_Type()
)
caqSecurityAclCaptureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqSecurityAclCaptureEnable.setStatus("current")
_CaqFlowPolicerExcessBurstSupport_Type = TruthValue
_CaqFlowPolicerExcessBurstSupport_Object = MibScalar
caqFlowPolicerExcessBurstSupport = _CaqFlowPolicerExcessBurstSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 11),
    _CaqFlowPolicerExcessBurstSupport_Type()
)
caqFlowPolicerExcessBurstSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqFlowPolicerExcessBurstSupport.setStatus("current")


class _CaqSecurityRateLimitFeatures_Type(Bits):
    """Custom type caqSecurityRateLimitFeatures based on Bits"""
    namedValues = NamedValues(
        *(("arpInspection", 0),
          ("dhcpSnooping", 2),
          ("dot1xDHCP", 1))
    )

_CaqSecurityRateLimitFeatures_Type.__name__ = "Bits"
_CaqSecurityRateLimitFeatures_Object = MibScalar
caqSecurityRateLimitFeatures = _CaqSecurityRateLimitFeatures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 12),
    _CaqSecurityRateLimitFeatures_Type()
)
caqSecurityRateLimitFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqSecurityRateLimitFeatures.setStatus("current")
_CaqSecurityAclRateLimit_Type = Unsigned32
_CaqSecurityAclRateLimit_Object = MibScalar
caqSecurityAclRateLimit = _CaqSecurityAclRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 13),
    _CaqSecurityAclRateLimit_Type()
)
caqSecurityAclRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqSecurityAclRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    caqSecurityAclRateLimit.setUnits("packet per second")
_CaqQosDefaultActionTable_Object = MibTable
caqQosDefaultActionTable = _CaqQosDefaultActionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 14)
)
if mibBuilder.loadTexts:
    caqQosDefaultActionTable.setStatus("current")
_CaqQosDefaultActionEntry_Object = MibTableRow
caqQosDefaultActionEntry = _CaqQosDefaultActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 14, 1)
)
caqQosDefaultActionEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqQosTrafficDirection"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqQosTrafficType"),
)
if mibBuilder.loadTexts:
    caqQosDefaultActionEntry.setStatus("current")
_CaqQosTrafficDirection_Type = CaqDirection
_CaqQosTrafficDirection_Object = MibTableColumn
caqQosTrafficDirection = _CaqQosTrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 14, 1, 1),
    _CaqQosTrafficDirection_Type()
)
caqQosTrafficDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqQosTrafficDirection.setStatus("current")


class _CaqQosTrafficType_Type(Integer32):
    """Custom type caqQosTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("ipx", 3),
          ("mac", 1))
    )


_CaqQosTrafficType_Type.__name__ = "Integer32"
_CaqQosTrafficType_Object = MibTableColumn
caqQosTrafficType = _CaqQosTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 14, 1, 2),
    _CaqQosTrafficType_Type()
)
caqQosTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqQosTrafficType.setStatus("current")


class _CaqQosDefaultTrustState_Type(Integer32):
    """Custom type caqQosDefaultTrustState based on Integer32"""
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
        *(("noTrust", 1),
          ("trustCos", 2),
          ("trustDscp", 4),
          ("trustIpPrec", 3))
    )


_CaqQosDefaultTrustState_Type.__name__ = "Integer32"
_CaqQosDefaultTrustState_Object = MibTableColumn
caqQosDefaultTrustState = _CaqQosDefaultTrustState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 14, 1, 3),
    _CaqQosDefaultTrustState_Type()
)
caqQosDefaultTrustState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqQosDefaultTrustState.setStatus("current")
_CaqQosDefaultDscp_Type = Dscp
_CaqQosDefaultDscp_Object = MibTableColumn
caqQosDefaultDscp = _CaqQosDefaultDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 14, 1, 4),
    _CaqQosDefaultDscp_Type()
)
caqQosDefaultDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqQosDefaultDscp.setStatus("current")
_CaqQosDefaultMicroflow_Type = CaqPolicerNameOrEmpty
_CaqQosDefaultMicroflow_Object = MibTableColumn
caqQosDefaultMicroflow = _CaqQosDefaultMicroflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 14, 1, 5),
    _CaqQosDefaultMicroflow_Type()
)
caqQosDefaultMicroflow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqQosDefaultMicroflow.setStatus("current")
_CaqQosDefaultAggregate_Type = CaqPolicerNameOrEmpty
_CaqQosDefaultAggregate_Object = MibTableColumn
caqQosDefaultAggregate = _CaqQosDefaultAggregate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 14, 1, 6),
    _CaqQosDefaultAggregate_Type()
)
caqQosDefaultAggregate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqQosDefaultAggregate.setStatus("current")


class _CaqAclFeatureCpb_Type(Bits):
    """Custom type caqAclFeatureCpb based on Bits"""
    namedValues = NamedValues(
        *(("portAclHitCount", 1),
          ("vlanAclHitCount", 0))
    )

_CaqAclFeatureCpb_Type.__name__ = "Bits"
_CaqAclFeatureCpb_Object = MibScalar
caqAclFeatureCpb = _CaqAclFeatureCpb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 3, 15),
    _CaqAclFeatureCpb_Type()
)
caqAclFeatureCpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAclFeatureCpb.setStatus("current")
_CaqQosStatsObjects_ObjectIdentity = ObjectIdentity
caqQosStatsObjects = _CaqQosStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4)
)
_CaqL3PacketsDropByPolicer_Type = Counter64
_CaqL3PacketsDropByPolicer_Object = MibScalar
caqL3PacketsDropByPolicer = _CaqL3PacketsDropByPolicer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 1),
    _CaqL3PacketsDropByPolicer_Type()
)
caqL3PacketsDropByPolicer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqL3PacketsDropByPolicer.setStatus("current")
_CaqTosChangedIpPackets_Type = Counter64
_CaqTosChangedIpPackets_Object = MibScalar
caqTosChangedIpPackets = _CaqTosChangedIpPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 2),
    _CaqTosChangedIpPackets_Type()
)
caqTosChangedIpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqTosChangedIpPackets.setStatus("current")
_CaqCosChangedIpPackets_Type = Counter64
_CaqCosChangedIpPackets_Object = MibScalar
caqCosChangedIpPackets = _CaqCosChangedIpPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 3),
    _CaqCosChangedIpPackets_Type()
)
caqCosChangedIpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqCosChangedIpPackets.setStatus("current")
_CaqCosChangedNonIpPackets_Type = Counter64
_CaqCosChangedNonIpPackets_Object = MibScalar
caqCosChangedNonIpPackets = _CaqCosChangedNonIpPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 4),
    _CaqCosChangedNonIpPackets_Type()
)
caqCosChangedNonIpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqCosChangedNonIpPackets.setStatus("current")
_CaqPortStatsTable_Object = MibTable
caqPortStatsTable = _CaqPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 5)
)
if mibBuilder.loadTexts:
    caqPortStatsTable.setStatus("current")
_CaqPortStatsEntry_Object = MibTableRow
caqPortStatsEntry = _CaqPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 5, 1)
)
caqPortStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqPortStatsDirection"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqPortStatsQueueNumber"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqPortStatsThresholdNumber"),
)
if mibBuilder.loadTexts:
    caqPortStatsEntry.setStatus("current")
_CaqPortStatsDirection_Type = CaqDirection
_CaqPortStatsDirection_Object = MibTableColumn
caqPortStatsDirection = _CaqPortStatsDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 5, 1, 1),
    _CaqPortStatsDirection_Type()
)
caqPortStatsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqPortStatsDirection.setStatus("current")
_CaqPortStatsQueueNumber_Type = CaqQueueNumber
_CaqPortStatsQueueNumber_Object = MibTableColumn
caqPortStatsQueueNumber = _CaqPortStatsQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 5, 1, 2),
    _CaqPortStatsQueueNumber_Type()
)
caqPortStatsQueueNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqPortStatsQueueNumber.setStatus("current")
_CaqPortStatsThresholdNumber_Type = CaqThresholdNumber
_CaqPortStatsThresholdNumber_Object = MibTableColumn
caqPortStatsThresholdNumber = _CaqPortStatsThresholdNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 5, 1, 3),
    _CaqPortStatsThresholdNumber_Type()
)
caqPortStatsThresholdNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqPortStatsThresholdNumber.setStatus("current")
_CaqPortStatsDropPkts_Type = Counter64
_CaqPortStatsDropPkts_Object = MibTableColumn
caqPortStatsDropPkts = _CaqPortStatsDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 5, 1, 4),
    _CaqPortStatsDropPkts_Type()
)
caqPortStatsDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqPortStatsDropPkts.setStatus("current")
_CaqPortStatsDropPktsAveRate_Type = Gauge32
_CaqPortStatsDropPktsAveRate_Object = MibTableColumn
caqPortStatsDropPktsAveRate = _CaqPortStatsDropPktsAveRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 5, 1, 5),
    _CaqPortStatsDropPktsAveRate_Type()
)
caqPortStatsDropPktsAveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqPortStatsDropPktsAveRate.setStatus("current")
if mibBuilder.loadTexts:
    caqPortStatsDropPktsAveRate.setUnits("packets per second")
_CaqPortStatsDropPktsPeakRate_Type = Gauge32
_CaqPortStatsDropPktsPeakRate_Object = MibTableColumn
caqPortStatsDropPktsPeakRate = _CaqPortStatsDropPktsPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 5, 1, 6),
    _CaqPortStatsDropPktsPeakRate_Type()
)
caqPortStatsDropPktsPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqPortStatsDropPktsPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    caqPortStatsDropPktsPeakRate.setUnits("packets per second")
_CaqFlowStatsTable_Object = MibTable
caqFlowStatsTable = _CaqFlowStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 6)
)
if mibBuilder.loadTexts:
    caqFlowStatsTable.setStatus("current")
_CaqFlowStatsEntry_Object = MibTableRow
caqFlowStatsEntry = _CaqFlowStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 6, 1)
)
if mibBuilder.loadTexts:
    caqFlowStatsEntry.setStatus("current")
_CaqFlowStatsOutOfProfilePackets_Type = Counter64
_CaqFlowStatsOutOfProfilePackets_Object = MibTableColumn
caqFlowStatsOutOfProfilePackets = _CaqFlowStatsOutOfProfilePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 6, 1, 1),
    _CaqFlowStatsOutOfProfilePackets_Type()
)
caqFlowStatsOutOfProfilePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqFlowStatsOutOfProfilePackets.setStatus("current")
_CaqAggPolicerStatsTable_Object = MibTable
caqAggPolicerStatsTable = _CaqAggPolicerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 7)
)
if mibBuilder.loadTexts:
    caqAggPolicerStatsTable.setStatus("current")
_CaqAggPolicerStatsEntry_Object = MibTableRow
caqAggPolicerStatsEntry = _CaqAggPolicerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 7, 1)
)
caqAggPolicerStatsEntry.setIndexNames(
    (1, "CISCO-CATOS-ACL-QOS-MIB", "caqAggPolicerName"),
)
if mibBuilder.loadTexts:
    caqAggPolicerStatsEntry.setStatus("current")
_CaqAggPolicerName_Type = CaqPolicerName
_CaqAggPolicerName_Object = MibTableColumn
caqAggPolicerName = _CaqAggPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 7, 1, 1),
    _CaqAggPolicerName_Type()
)
caqAggPolicerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqAggPolicerName.setStatus("current")
_CaqAggPolicerPackets_Type = Counter64
_CaqAggPolicerPackets_Object = MibTableColumn
caqAggPolicerPackets = _CaqAggPolicerPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 7, 1, 2),
    _CaqAggPolicerPackets_Type()
)
caqAggPolicerPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAggPolicerPackets.setStatus("current")
_CaqAggPolicerNRExceedPackets_Type = Counter64
_CaqAggPolicerNRExceedPackets_Object = MibTableColumn
caqAggPolicerNRExceedPackets = _CaqAggPolicerNRExceedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 7, 1, 3),
    _CaqAggPolicerNRExceedPackets_Type()
)
caqAggPolicerNRExceedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAggPolicerNRExceedPackets.setStatus("current")
_CaqAggPolicerERExceedPackets_Type = Counter64
_CaqAggPolicerERExceedPackets_Object = MibTableColumn
caqAggPolicerERExceedPackets = _CaqAggPolicerERExceedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 7, 1, 4),
    _CaqAggPolicerERExceedPackets_Type()
)
caqAggPolicerERExceedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAggPolicerERExceedPackets.setStatus("current")
_CaqAggPolicerOctets_Type = Counter64
_CaqAggPolicerOctets_Object = MibTableColumn
caqAggPolicerOctets = _CaqAggPolicerOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 7, 1, 5),
    _CaqAggPolicerOctets_Type()
)
caqAggPolicerOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAggPolicerOctets.setStatus("current")
_CaqAggPolicerNRExceedOctets_Type = Counter64
_CaqAggPolicerNRExceedOctets_Object = MibTableColumn
caqAggPolicerNRExceedOctets = _CaqAggPolicerNRExceedOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 7, 1, 6),
    _CaqAggPolicerNRExceedOctets_Type()
)
caqAggPolicerNRExceedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAggPolicerNRExceedOctets.setStatus("current")
_CaqAggPolicerERExceedOctets_Type = Counter64
_CaqAggPolicerERExceedOctets_Object = MibTableColumn
caqAggPolicerERExceedOctets = _CaqAggPolicerERExceedOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 7, 1, 7),
    _CaqAggPolicerERExceedOctets_Type()
)
caqAggPolicerERExceedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAggPolicerERExceedOctets.setStatus("current")
_CaqAggPolicerOctetsRate_Type = CounterBasedGauge64
_CaqAggPolicerOctetsRate_Object = MibTableColumn
caqAggPolicerOctetsRate = _CaqAggPolicerOctetsRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 7, 1, 8),
    _CaqAggPolicerOctetsRate_Type()
)
caqAggPolicerOctetsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAggPolicerOctetsRate.setStatus("current")
if mibBuilder.loadTexts:
    caqAggPolicerOctetsRate.setUnits("kbps")
_CaqAggPolicerNRExceedOctetsRate_Type = CounterBasedGauge64
_CaqAggPolicerNRExceedOctetsRate_Object = MibTableColumn
caqAggPolicerNRExceedOctetsRate = _CaqAggPolicerNRExceedOctetsRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 7, 1, 9),
    _CaqAggPolicerNRExceedOctetsRate_Type()
)
caqAggPolicerNRExceedOctetsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAggPolicerNRExceedOctetsRate.setStatus("current")
if mibBuilder.loadTexts:
    caqAggPolicerNRExceedOctetsRate.setUnits("kbps")
_CaqAggPolicerERExceedOctetsRate_Type = CounterBasedGauge64
_CaqAggPolicerERExceedOctetsRate_Object = MibTableColumn
caqAggPolicerERExceedOctetsRate = _CaqAggPolicerERExceedOctetsRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 7, 1, 10),
    _CaqAggPolicerERExceedOctetsRate_Type()
)
caqAggPolicerERExceedOctetsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAggPolicerERExceedOctetsRate.setStatus("current")
if mibBuilder.loadTexts:
    caqAggPolicerERExceedOctetsRate.setUnits("kbps")
_CaqAggPolicerOctetsPeakRate_Type = CounterBasedGauge64
_CaqAggPolicerOctetsPeakRate_Object = MibTableColumn
caqAggPolicerOctetsPeakRate = _CaqAggPolicerOctetsPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 7, 1, 11),
    _CaqAggPolicerOctetsPeakRate_Type()
)
caqAggPolicerOctetsPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAggPolicerOctetsPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    caqAggPolicerOctetsPeakRate.setUnits("kbps")
_CaqAggPolicerPacketsRate_Type = CounterBasedGauge64
_CaqAggPolicerPacketsRate_Object = MibTableColumn
caqAggPolicerPacketsRate = _CaqAggPolicerPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 7, 1, 12),
    _CaqAggPolicerPacketsRate_Type()
)
caqAggPolicerPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAggPolicerPacketsRate.setStatus("current")
if mibBuilder.loadTexts:
    caqAggPolicerPacketsRate.setUnits("packets per second")
_CaqAggPolicerNRExceedPacketsRate_Type = CounterBasedGauge64
_CaqAggPolicerNRExceedPacketsRate_Object = MibTableColumn
caqAggPolicerNRExceedPacketsRate = _CaqAggPolicerNRExceedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 7, 1, 13),
    _CaqAggPolicerNRExceedPacketsRate_Type()
)
caqAggPolicerNRExceedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAggPolicerNRExceedPacketsRate.setStatus("current")
if mibBuilder.loadTexts:
    caqAggPolicerNRExceedPacketsRate.setUnits("packets per second")
_CaqAggPolicerERExceedPacketsRate_Type = CounterBasedGauge64
_CaqAggPolicerERExceedPacketsRate_Object = MibTableColumn
caqAggPolicerERExceedPacketsRate = _CaqAggPolicerERExceedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 7, 1, 14),
    _CaqAggPolicerERExceedPacketsRate_Type()
)
caqAggPolicerERExceedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAggPolicerERExceedPacketsRate.setStatus("current")
if mibBuilder.loadTexts:
    caqAggPolicerERExceedPacketsRate.setUnits("packets per second")
_CaqAggPolicerPacketsPeakRate_Type = CounterBasedGauge64
_CaqAggPolicerPacketsPeakRate_Object = MibTableColumn
caqAggPolicerPacketsPeakRate = _CaqAggPolicerPacketsPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 7, 1, 15),
    _CaqAggPolicerPacketsPeakRate_Type()
)
caqAggPolicerPacketsPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAggPolicerPacketsPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    caqAggPolicerPacketsPeakRate.setUnits("packets per second")
_CaqL3PacketsDropByPolicerAveRate_Type = CounterBasedGauge64
_CaqL3PacketsDropByPolicerAveRate_Object = MibScalar
caqL3PacketsDropByPolicerAveRate = _CaqL3PacketsDropByPolicerAveRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 8),
    _CaqL3PacketsDropByPolicerAveRate_Type()
)
caqL3PacketsDropByPolicerAveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqL3PacketsDropByPolicerAveRate.setStatus("current")
if mibBuilder.loadTexts:
    caqL3PacketsDropByPolicerAveRate.setUnits("packets per second")
_CaqL3PacketsDropByPolicerPeakRate_Type = CounterBasedGauge64
_CaqL3PacketsDropByPolicerPeakRate_Object = MibScalar
caqL3PacketsDropByPolicerPeakRate = _CaqL3PacketsDropByPolicerPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 9),
    _CaqL3PacketsDropByPolicerPeakRate_Type()
)
caqL3PacketsDropByPolicerPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqL3PacketsDropByPolicerPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    caqL3PacketsDropByPolicerPeakRate.setUnits("packets per second")
_CaqTosChangedIpPacketsAveRate_Type = CounterBasedGauge64
_CaqTosChangedIpPacketsAveRate_Object = MibScalar
caqTosChangedIpPacketsAveRate = _CaqTosChangedIpPacketsAveRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 10),
    _CaqTosChangedIpPacketsAveRate_Type()
)
caqTosChangedIpPacketsAveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqTosChangedIpPacketsAveRate.setStatus("current")
if mibBuilder.loadTexts:
    caqTosChangedIpPacketsAveRate.setUnits("packets per second")
_CaqTosChangedIpPacketsPeakRate_Type = CounterBasedGauge64
_CaqTosChangedIpPacketsPeakRate_Object = MibScalar
caqTosChangedIpPacketsPeakRate = _CaqTosChangedIpPacketsPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 11),
    _CaqTosChangedIpPacketsPeakRate_Type()
)
caqTosChangedIpPacketsPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqTosChangedIpPacketsPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    caqTosChangedIpPacketsPeakRate.setUnits("packets per second")
_CaqCosChangedIpPacketsAveRate_Type = CounterBasedGauge64
_CaqCosChangedIpPacketsAveRate_Object = MibScalar
caqCosChangedIpPacketsAveRate = _CaqCosChangedIpPacketsAveRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 12),
    _CaqCosChangedIpPacketsAveRate_Type()
)
caqCosChangedIpPacketsAveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqCosChangedIpPacketsAveRate.setStatus("current")
if mibBuilder.loadTexts:
    caqCosChangedIpPacketsAveRate.setUnits("packets per second")
_CaqCosChangedIpPacketsPeakRate_Type = CounterBasedGauge64
_CaqCosChangedIpPacketsPeakRate_Object = MibScalar
caqCosChangedIpPacketsPeakRate = _CaqCosChangedIpPacketsPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 13),
    _CaqCosChangedIpPacketsPeakRate_Type()
)
caqCosChangedIpPacketsPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqCosChangedIpPacketsPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    caqCosChangedIpPacketsPeakRate.setUnits("packets per second")
_CaqCosChangedNonIpPacketsAveRate_Type = CounterBasedGauge64
_CaqCosChangedNonIpPacketsAveRate_Object = MibScalar
caqCosChangedNonIpPacketsAveRate = _CaqCosChangedNonIpPacketsAveRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 14),
    _CaqCosChangedNonIpPacketsAveRate_Type()
)
caqCosChangedNonIpPacketsAveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqCosChangedNonIpPacketsAveRate.setStatus("current")
if mibBuilder.loadTexts:
    caqCosChangedNonIpPacketsAveRate.setUnits("packets per second")
_CaqCosChangedNonIpPacketPeakRate_Type = CounterBasedGauge64
_CaqCosChangedNonIpPacketPeakRate_Object = MibScalar
caqCosChangedNonIpPacketPeakRate = _CaqCosChangedNonIpPacketPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 4, 15),
    _CaqCosChangedNonIpPacketPeakRate_Type()
)
caqCosChangedNonIpPacketPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqCosChangedNonIpPacketPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    caqCosChangedNonIpPacketPeakRate.setUnits("packets per second")
_CaqExtObjects_ObjectIdentity = ObjectIdentity
caqExtObjects = _CaqExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 5)
)
_CaqBridgedPolicerTable_Object = MibTable
caqBridgedPolicerTable = _CaqBridgedPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 5, 1)
)
if mibBuilder.loadTexts:
    caqBridgedPolicerTable.setStatus("current")
_CaqBridgedPolicerEntry_Object = MibTableRow
caqBridgedPolicerEntry = _CaqBridgedPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 5, 1, 1)
)
caqBridgedPolicerEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqBridgedFlowVlanIndex"),
)
if mibBuilder.loadTexts:
    caqBridgedPolicerEntry.setStatus("current")
_CaqBridgedFlowVlanIndex_Type = VlanIndex
_CaqBridgedFlowVlanIndex_Object = MibTableColumn
caqBridgedFlowVlanIndex = _CaqBridgedFlowVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 5, 1, 1, 1),
    _CaqBridgedFlowVlanIndex_Type()
)
caqBridgedFlowVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqBridgedFlowVlanIndex.setStatus("current")


class _CaqBridgedFlowEnabled_Type(TruthValue):
    """Custom type caqBridgedFlowEnabled based on TruthValue"""


_CaqBridgedFlowEnabled_Object = MibTableColumn
caqBridgedFlowEnabled = _CaqBridgedFlowEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 5, 1, 1, 2),
    _CaqBridgedFlowEnabled_Type()
)
caqBridgedFlowEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqBridgedFlowEnabled.setStatus("current")
_CaqCosMacVlanRouterTable_Object = MibTable
caqCosMacVlanRouterTable = _CaqCosMacVlanRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 5, 2)
)
if mibBuilder.loadTexts:
    caqCosMacVlanRouterTable.setStatus("current")
_CaqCosMacVlanRouterEntry_Object = MibTableRow
caqCosMacVlanRouterEntry = _CaqCosMacVlanRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 5, 2, 1)
)
caqCosMacVlanRouterEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqCosMacAddress"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqCosVlanNumber"),
)
if mibBuilder.loadTexts:
    caqCosMacVlanRouterEntry.setStatus("current")
_CaqCosMacAddress_Type = MacAddress
_CaqCosMacAddress_Object = MibTableColumn
caqCosMacAddress = _CaqCosMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 5, 2, 1, 1),
    _CaqCosMacAddress_Type()
)
caqCosMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqCosMacAddress.setStatus("current")
_CaqCosVlanNumber_Type = VlanIndex
_CaqCosVlanNumber_Object = MibTableColumn
caqCosVlanNumber = _CaqCosVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 5, 2, 1, 2),
    _CaqCosVlanNumber_Type()
)
caqCosVlanNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqCosVlanNumber.setStatus("current")


class _CaqMacAddressCpb_Type(Bits):
    """Custom type caqMacAddressCpb based on Bits"""
    namedValues = NamedValues(
        *(("cosVlanMac", 1),
          ("routerMac", 0))
    )

_CaqMacAddressCpb_Type.__name__ = "Bits"
_CaqMacAddressCpb_Object = MibTableColumn
caqMacAddressCpb = _CaqMacAddressCpb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 5, 2, 1, 3),
    _CaqMacAddressCpb_Type()
)
caqMacAddressCpb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqMacAddressCpb.setStatus("current")
_CaqCosValue_Type = QosLayer2Cos
_CaqCosValue_Object = MibTableColumn
caqCosValue = _CaqCosValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 5, 2, 1, 4),
    _CaqCosValue_Type()
)
caqCosValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqCosValue.setStatus("current")
_CaqCosMacVlanRouterStatus_Type = RowStatus
_CaqCosMacVlanRouterStatus_Object = MibTableColumn
caqCosMacVlanRouterStatus = _CaqCosMacVlanRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 5, 2, 1, 5),
    _CaqCosMacVlanRouterStatus_Type()
)
caqCosMacVlanRouterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqCosMacVlanRouterStatus.setStatus("current")
_CaqPbfObjects_ObjectIdentity = ObjectIdentity
caqPbfObjects = _CaqPbfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 6)
)


class _CaqPbfStatus_Type(Integer32):
    """Custom type caqPbfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macAddrNotSet", 2),
          ("macAddrOk", 1),
          ("msfcPresent", 3))
    )


_CaqPbfStatus_Type.__name__ = "Integer32"
_CaqPbfStatus_Object = MibScalar
caqPbfStatus = _CaqPbfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 6, 1),
    _CaqPbfStatus_Type()
)
caqPbfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqPbfStatus.setStatus("current")
_CaqPbfMacAddress_Type = MacAddress
_CaqPbfMacAddress_Object = MibScalar
caqPbfMacAddress = _CaqPbfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 6, 2),
    _CaqPbfMacAddress_Type()
)
caqPbfMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqPbfMacAddress.setStatus("current")
_CaqAdjacencyTable_Object = MibTable
caqAdjacencyTable = _CaqAdjacencyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 6, 3)
)
if mibBuilder.loadTexts:
    caqAdjacencyTable.setStatus("current")
_CaqAdjacencyEntry_Object = MibTableRow
caqAdjacencyEntry = _CaqAdjacencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 6, 3, 1)
)
caqAdjacencyEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqAdjIndex"),
)
if mibBuilder.loadTexts:
    caqAdjacencyEntry.setStatus("current")


class _CaqAdjIndex_Type(Unsigned32):
    """Custom type caqAdjIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CaqAdjIndex_Type.__name__ = "Unsigned32"
_CaqAdjIndex_Object = MibTableColumn
caqAdjIndex = _CaqAdjIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 6, 3, 1, 1),
    _CaqAdjIndex_Type()
)
caqAdjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqAdjIndex.setStatus("current")
_CaqAdjDstVlanNumber_Type = VlanIndex
_CaqAdjDstVlanNumber_Object = MibTableColumn
caqAdjDstVlanNumber = _CaqAdjDstVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 6, 3, 1, 2),
    _CaqAdjDstVlanNumber_Type()
)
caqAdjDstVlanNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqAdjDstVlanNumber.setStatus("current")
_CaqAdjDstMacAddress_Type = MacAddress
_CaqAdjDstMacAddress_Object = MibTableColumn
caqAdjDstMacAddress = _CaqAdjDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 6, 3, 1, 3),
    _CaqAdjDstMacAddress_Type()
)
caqAdjDstMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqAdjDstMacAddress.setStatus("current")
_CaqAdjSrcMacAddress_Type = MacAddress
_CaqAdjSrcMacAddress_Object = MibTableColumn
caqAdjSrcMacAddress = _CaqAdjSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 6, 3, 1, 4),
    _CaqAdjSrcMacAddress_Type()
)
caqAdjSrcMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqAdjSrcMacAddress.setStatus("current")
_CaqAdjName_Type = CaqAdjacencyName
_CaqAdjName_Object = MibTableColumn
caqAdjName = _CaqAdjName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 6, 3, 1, 5),
    _CaqAdjName_Type()
)
caqAdjName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqAdjName.setStatus("current")


class _CaqAdjMtu_Type(Unsigned32):
    """Custom type caqAdjMtu based on Unsigned32"""
    defaultValue = 9216

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 18190),
    )


_CaqAdjMtu_Type.__name__ = "Unsigned32"
_CaqAdjMtu_Object = MibTableColumn
caqAdjMtu = _CaqAdjMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 6, 3, 1, 6),
    _CaqAdjMtu_Type()
)
caqAdjMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqAdjMtu.setStatus("current")
if mibBuilder.loadTexts:
    caqAdjMtu.setUnits("bytes")
_CaqAdjHitCount_Type = Counter64
_CaqAdjHitCount_Object = MibTableColumn
caqAdjHitCount = _CaqAdjHitCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 6, 3, 1, 7),
    _CaqAdjHitCount_Type()
)
caqAdjHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAdjHitCount.setStatus("current")
_CaqAdjStatus_Type = RowStatus
_CaqAdjStatus_Object = MibTableColumn
caqAdjStatus = _CaqAdjStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 6, 3, 1, 8),
    _CaqAdjStatus_Type()
)
caqAdjStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caqAdjStatus.setStatus("current")
_CaqLoggingObjects_ObjectIdentity = ObjectIdentity
caqLoggingObjects = _CaqLoggingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7)
)


class _CaqAclLogMaxFlow_Type(Unsigned32):
    """Custom type caqAclLogMaxFlow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2048),
    )


_CaqAclLogMaxFlow_Type.__name__ = "Unsigned32"
_CaqAclLogMaxFlow_Object = MibScalar
caqAclLogMaxFlow = _CaqAclLogMaxFlow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 1),
    _CaqAclLogMaxFlow_Type()
)
caqAclLogMaxFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqAclLogMaxFlow.setStatus("current")


class _CaqAclSecurityLoggingRateLimit_Type(Unsigned32):
    """Custom type caqAclSecurityLoggingRateLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 5000),
    )


_CaqAclSecurityLoggingRateLimit_Type.__name__ = "Unsigned32"
_CaqAclSecurityLoggingRateLimit_Object = MibScalar
caqAclSecurityLoggingRateLimit = _CaqAclSecurityLoggingRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 2),
    _CaqAclSecurityLoggingRateLimit_Type()
)
caqAclSecurityLoggingRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqAclSecurityLoggingRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    caqAclSecurityLoggingRateLimit.setUnits("packet per second")


class _CaqAclRouterAclRateLimit_Type(Unsigned32):
    """Custom type caqAclRouterAclRateLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CaqAclRouterAclRateLimit_Type.__name__ = "Unsigned32"
_CaqAclRouterAclRateLimit_Object = MibScalar
caqAclRouterAclRateLimit = _CaqAclRouterAclRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 3),
    _CaqAclRouterAclRateLimit_Type()
)
caqAclRouterAclRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqAclRouterAclRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    caqAclRouterAclRateLimit.setUnits("packet per second")
_CaqIpFlowLoggingTable_Object = MibTable
caqIpFlowLoggingTable = _CaqIpFlowLoggingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4)
)
if mibBuilder.loadTexts:
    caqIpFlowLoggingTable.setStatus("current")
_CaqIpFlowLoggingEntry_Object = MibTableRow
caqIpFlowLoggingEntry = _CaqIpFlowLoggingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1)
)
caqIpFlowLoggingEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowLoggingIndex"),
)
if mibBuilder.loadTexts:
    caqIpFlowLoggingEntry.setStatus("current")


class _CaqIpFlowLoggingIndex_Type(Unsigned32):
    """Custom type caqIpFlowLoggingIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CaqIpFlowLoggingIndex_Type.__name__ = "Unsigned32"
_CaqIpFlowLoggingIndex_Object = MibTableColumn
caqIpFlowLoggingIndex = _CaqIpFlowLoggingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 1),
    _CaqIpFlowLoggingIndex_Type()
)
caqIpFlowLoggingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqIpFlowLoggingIndex.setStatus("current")
_CaqIpFlowVlan_Type = VlanIndex
_CaqIpFlowVlan_Object = MibTableColumn
caqIpFlowVlan = _CaqIpFlowVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 2),
    _CaqIpFlowVlan_Type()
)
caqIpFlowVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowVlan.setStatus("current")
_CaqIpFlowIfIndex_Type = InterfaceIndex
_CaqIpFlowIfIndex_Object = MibTableColumn
caqIpFlowIfIndex = _CaqIpFlowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 3),
    _CaqIpFlowIfIndex_Type()
)
caqIpFlowIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowIfIndex.setStatus("current")


class _CaqIpFlowProtocolType_Type(Unsigned32):
    """Custom type caqIpFlowProtocolType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CaqIpFlowProtocolType_Type.__name__ = "Unsigned32"
_CaqIpFlowProtocolType_Object = MibTableColumn
caqIpFlowProtocolType = _CaqIpFlowProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 4),
    _CaqIpFlowProtocolType_Type()
)
caqIpFlowProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowProtocolType.setStatus("current")
_CaqIpFlowAddrType_Type = InetAddressType
_CaqIpFlowAddrType_Object = MibTableColumn
caqIpFlowAddrType = _CaqIpFlowAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 5),
    _CaqIpFlowAddrType_Type()
)
caqIpFlowAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowAddrType.setStatus("current")
_CaqIpFlowSrcIp_Type = InetAddress
_CaqIpFlowSrcIp_Object = MibTableColumn
caqIpFlowSrcIp = _CaqIpFlowSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 6),
    _CaqIpFlowSrcIp_Type()
)
caqIpFlowSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowSrcIp.setStatus("current")


class _CaqIpFlowSrcPort_Type(Integer32):
    """Custom type caqIpFlowSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_CaqIpFlowSrcPort_Type.__name__ = "Integer32"
_CaqIpFlowSrcPort_Object = MibTableColumn
caqIpFlowSrcPort = _CaqIpFlowSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 7),
    _CaqIpFlowSrcPort_Type()
)
caqIpFlowSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowSrcPort.setStatus("current")
_CaqIpFlowDestIp_Type = InetAddress
_CaqIpFlowDestIp_Object = MibTableColumn
caqIpFlowDestIp = _CaqIpFlowDestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 8),
    _CaqIpFlowDestIp_Type()
)
caqIpFlowDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowDestIp.setStatus("current")


class _CaqIpFlowDestPort_Type(Integer32):
    """Custom type caqIpFlowDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_CaqIpFlowDestPort_Type.__name__ = "Integer32"
_CaqIpFlowDestPort_Object = MibTableColumn
caqIpFlowDestPort = _CaqIpFlowDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 9),
    _CaqIpFlowDestPort_Type()
)
caqIpFlowDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowDestPort.setStatus("current")


class _CaqIpFlowIcmpType_Type(Integer32):
    """Custom type caqIpFlowIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_CaqIpFlowIcmpType_Type.__name__ = "Integer32"
_CaqIpFlowIcmpType_Object = MibTableColumn
caqIpFlowIcmpType = _CaqIpFlowIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 10),
    _CaqIpFlowIcmpType_Type()
)
caqIpFlowIcmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowIcmpType.setStatus("current")


class _CaqIpFlowIcmpCode_Type(Integer32):
    """Custom type caqIpFlowIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_CaqIpFlowIcmpCode_Type.__name__ = "Integer32"
_CaqIpFlowIcmpCode_Object = MibTableColumn
caqIpFlowIcmpCode = _CaqIpFlowIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 11),
    _CaqIpFlowIcmpCode_Type()
)
caqIpFlowIcmpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowIcmpCode.setStatus("current")


class _CaqIpFlowIgmpType_Type(Integer32):
    """Custom type caqIpFlowIgmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 15),
    )


_CaqIpFlowIgmpType_Type.__name__ = "Integer32"
_CaqIpFlowIgmpType_Object = MibTableColumn
caqIpFlowIgmpType = _CaqIpFlowIgmpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 12),
    _CaqIpFlowIgmpType_Type()
)
caqIpFlowIgmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowIgmpType.setStatus("current")


class _CaqIpFlowArpOpcode_Type(Integer32):
    """Custom type caqIpFlowArpOpcode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("reply", 3),
          ("request", 2))
    )


_CaqIpFlowArpOpcode_Type.__name__ = "Integer32"
_CaqIpFlowArpOpcode_Object = MibTableColumn
caqIpFlowArpOpcode = _CaqIpFlowArpOpcode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 13),
    _CaqIpFlowArpOpcode_Type()
)
caqIpFlowArpOpcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowArpOpcode.setStatus("current")
_CaqIpFlowArpSrcMacAddr_Type = MacAddress
_CaqIpFlowArpSrcMacAddr_Object = MibTableColumn
caqIpFlowArpSrcMacAddr = _CaqIpFlowArpSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 14),
    _CaqIpFlowArpSrcMacAddr_Type()
)
caqIpFlowArpSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowArpSrcMacAddr.setStatus("current")
_CaqIpFlowArpHeaderSrcMacAddr_Type = MacAddress
_CaqIpFlowArpHeaderSrcMacAddr_Object = MibTableColumn
caqIpFlowArpHeaderSrcMacAddr = _CaqIpFlowArpHeaderSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 15),
    _CaqIpFlowArpHeaderSrcMacAddr_Type()
)
caqIpFlowArpHeaderSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowArpHeaderSrcMacAddr.setStatus("current")
_CaqIpFlowPacketsCount_Type = Counter32
_CaqIpFlowPacketsCount_Object = MibTableColumn
caqIpFlowPacketsCount = _CaqIpFlowPacketsCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 16),
    _CaqIpFlowPacketsCount_Type()
)
caqIpFlowPacketsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowPacketsCount.setStatus("current")
if mibBuilder.loadTexts:
    caqIpFlowPacketsCount.setUnits("packets")
_CaqIpFlowLoggingTTL_Type = Unsigned32
_CaqIpFlowLoggingTTL_Object = MibTableColumn
caqIpFlowLoggingTTL = _CaqIpFlowLoggingTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 17),
    _CaqIpFlowLoggingTTL_Type()
)
caqIpFlowLoggingTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowLoggingTTL.setStatus("current")
if mibBuilder.loadTexts:
    caqIpFlowLoggingTTL.setUnits("seconds")


class _CaqIpFlowArpLoggingSource_Type(Integer32):
    """Custom type caqIpFlowArpLoggingSource based on Integer32"""
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
          ("dai", 2),
          ("notApplicable", 1))
    )


_CaqIpFlowArpLoggingSource_Type.__name__ = "Integer32"
_CaqIpFlowArpLoggingSource_Object = MibTableColumn
caqIpFlowArpLoggingSource = _CaqIpFlowArpLoggingSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 18),
    _CaqIpFlowArpLoggingSource_Type()
)
caqIpFlowArpLoggingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowArpLoggingSource.setStatus("current")
_CaqIpFlowArpAclName_Type = SnmpAdminString
_CaqIpFlowArpAclName_Object = MibTableColumn
caqIpFlowArpAclName = _CaqIpFlowArpAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 19),
    _CaqIpFlowArpAclName_Type()
)
caqIpFlowArpAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowArpAclName.setStatus("current")
_CaqIpFlowArpAceNumber_Type = Unsigned32
_CaqIpFlowArpAceNumber_Object = MibTableColumn
caqIpFlowArpAceNumber = _CaqIpFlowArpAceNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 7, 4, 1, 20),
    _CaqIpFlowArpAceNumber_Type()
)
caqIpFlowArpAceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpFlowArpAceNumber.setStatus("current")
_CaqArpInspObjects_ObjectIdentity = ObjectIdentity
caqArpInspObjects = _CaqArpInspObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 8)
)


class _CaqAclArpInspMatchMac_Type(Integer32):
    """Custom type caqAclArpInspMatchMac based on Integer32"""
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
        *(("disable", 1),
          ("drop", 3),
          ("dropAndLog", 4),
          ("enable", 2))
    )


_CaqAclArpInspMatchMac_Type.__name__ = "Integer32"
_CaqAclArpInspMatchMac_Object = MibScalar
caqAclArpInspMatchMac = _CaqAclArpInspMatchMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 8, 2),
    _CaqAclArpInspMatchMac_Type()
)
caqAclArpInspMatchMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqAclArpInspMatchMac.setStatus("current")


class _CaqAclArpInspAddrValidation_Type(Integer32):
    """Custom type caqAclArpInspAddrValidation based on Integer32"""
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
        *(("disable", 1),
          ("drop", 3),
          ("dropAndLog", 4),
          ("enable", 2))
    )


_CaqAclArpInspAddrValidation_Type.__name__ = "Integer32"
_CaqAclArpInspAddrValidation_Object = MibScalar
caqAclArpInspAddrValidation = _CaqAclArpInspAddrValidation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 8, 3),
    _CaqAclArpInspAddrValidation_Type()
)
caqAclArpInspAddrValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqAclArpInspAddrValidation.setStatus("current")
_CaqArpInspGlobalForwardedPkts_Type = Counter64
_CaqArpInspGlobalForwardedPkts_Object = MibScalar
caqArpInspGlobalForwardedPkts = _CaqArpInspGlobalForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 8, 4),
    _CaqArpInspGlobalForwardedPkts_Type()
)
caqArpInspGlobalForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqArpInspGlobalForwardedPkts.setStatus("current")
if mibBuilder.loadTexts:
    caqArpInspGlobalForwardedPkts.setUnits("packets")
_CaqArpInspGlobalDroppedPkts_Type = Counter64
_CaqArpInspGlobalDroppedPkts_Object = MibScalar
caqArpInspGlobalDroppedPkts = _CaqArpInspGlobalDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 8, 5),
    _CaqArpInspGlobalDroppedPkts_Type()
)
caqArpInspGlobalDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqArpInspGlobalDroppedPkts.setStatus("current")
if mibBuilder.loadTexts:
    caqArpInspGlobalDroppedPkts.setUnits("packets")
_CaqRARPForwardedPkts_Type = Counter64
_CaqRARPForwardedPkts_Object = MibScalar
caqRARPForwardedPkts = _CaqRARPForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 8, 6),
    _CaqRARPForwardedPkts_Type()
)
caqRARPForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqRARPForwardedPkts.setStatus("current")
if mibBuilder.loadTexts:
    caqRARPForwardedPkts.setUnits("packets")
_CaqMatchedMacFailedPkts_Type = Counter64
_CaqMatchedMacFailedPkts_Object = MibScalar
caqMatchedMacFailedPkts = _CaqMatchedMacFailedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 8, 7),
    _CaqMatchedMacFailedPkts_Type()
)
caqMatchedMacFailedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqMatchedMacFailedPkts.setStatus("current")
if mibBuilder.loadTexts:
    caqMatchedMacFailedPkts.setUnits("packets")
_CaqAddrValidationFailedPkts_Type = Counter64
_CaqAddrValidationFailedPkts_Object = MibScalar
caqAddrValidationFailedPkts = _CaqAddrValidationFailedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 8, 8),
    _CaqAddrValidationFailedPkts_Type()
)
caqAddrValidationFailedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAddrValidationFailedPkts.setStatus("current")
if mibBuilder.loadTexts:
    caqAddrValidationFailedPkts.setUnits("packets")
_CaqArpInspIpDroppedPkts_Type = Counter64
_CaqArpInspIpDroppedPkts_Object = MibScalar
caqArpInspIpDroppedPkts = _CaqArpInspIpDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 8, 9),
    _CaqArpInspIpDroppedPkts_Type()
)
caqArpInspIpDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqArpInspIpDroppedPkts.setStatus("current")
if mibBuilder.loadTexts:
    caqArpInspIpDroppedPkts.setUnits("packets")
_CaqArpInspStatsTable_Object = MibTable
caqArpInspStatsTable = _CaqArpInspStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 8, 10)
)
if mibBuilder.loadTexts:
    caqArpInspStatsTable.setStatus("current")
_CaqArpInspStatsEntry_Object = MibTableRow
caqArpInspStatsEntry = _CaqArpInspStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 8, 10, 1)
)
caqArpInspStatsEntry.setIndexNames(
    (1, "CISCO-CATOS-ACL-QOS-MIB", "caqArpInspAclName"),
)
if mibBuilder.loadTexts:
    caqArpInspStatsEntry.setStatus("current")
_CaqArpInspAclName_Type = CaqAclName
_CaqArpInspAclName_Object = MibTableColumn
caqArpInspAclName = _CaqArpInspAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 8, 10, 1, 1),
    _CaqArpInspAclName_Type()
)
caqArpInspAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqArpInspAclName.setStatus("current")
_CaqArpInspForwardedPackets_Type = Counter64
_CaqArpInspForwardedPackets_Object = MibTableColumn
caqArpInspForwardedPackets = _CaqArpInspForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 8, 10, 1, 2),
    _CaqArpInspForwardedPackets_Type()
)
caqArpInspForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqArpInspForwardedPackets.setStatus("current")
if mibBuilder.loadTexts:
    caqArpInspForwardedPackets.setUnits("packets")
_CaqArpInspDroppedPackets_Type = Counter64
_CaqArpInspDroppedPackets_Object = MibTableColumn
caqArpInspDroppedPackets = _CaqArpInspDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 8, 10, 1, 3),
    _CaqArpInspDroppedPackets_Type()
)
caqArpInspDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqArpInspDroppedPackets.setStatus("current")
if mibBuilder.loadTexts:
    caqArpInspDroppedPackets.setUnits("packets")
_CaqIfArpInspConfigTable_Object = MibTable
caqIfArpInspConfigTable = _CaqIfArpInspConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 8, 11)
)
if mibBuilder.loadTexts:
    caqIfArpInspConfigTable.setStatus("current")
_CaqIfArpInspConfigEntry_Object = MibTableRow
caqIfArpInspConfigEntry = _CaqIfArpInspConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 8, 11, 1)
)
caqIfArpInspConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    caqIfArpInspConfigEntry.setStatus("current")


class _CaqIfArpInspDropThreshold_Type(Unsigned32):
    """Custom type caqIfArpInspDropThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_CaqIfArpInspDropThreshold_Type.__name__ = "Unsigned32"
_CaqIfArpInspDropThreshold_Object = MibTableColumn
caqIfArpInspDropThreshold = _CaqIfArpInspDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 8, 11, 1, 1),
    _CaqIfArpInspDropThreshold_Type()
)
caqIfArpInspDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqIfArpInspDropThreshold.setStatus("current")
if mibBuilder.loadTexts:
    caqIfArpInspDropThreshold.setUnits("packet per second")


class _CaqIfArpInspShutdownThreshold_Type(Unsigned32):
    """Custom type caqIfArpInspShutdownThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_CaqIfArpInspShutdownThreshold_Type.__name__ = "Unsigned32"
_CaqIfArpInspShutdownThreshold_Object = MibTableColumn
caqIfArpInspShutdownThreshold = _CaqIfArpInspShutdownThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 8, 11, 1, 2),
    _CaqIfArpInspShutdownThreshold_Type()
)
caqIfArpInspShutdownThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqIfArpInspShutdownThreshold.setStatus("current")
if mibBuilder.loadTexts:
    caqIfArpInspShutdownThreshold.setUnits("packet per second")
_CaqAclHitCountObjects_ObjectIdentity = ObjectIdentity
caqAclHitCountObjects = _CaqAclHitCountObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9)
)


class _CaqAclHitCountVlansLow_Type(OctetString):
    """Custom type caqAclHitCountVlansLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CaqAclHitCountVlansLow_Type.__name__ = "OctetString"
_CaqAclHitCountVlansLow_Object = MibScalar
caqAclHitCountVlansLow = _CaqAclHitCountVlansLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 1),
    _CaqAclHitCountVlansLow_Type()
)
caqAclHitCountVlansLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqAclHitCountVlansLow.setStatus("current")


class _CaqAclHitCountVlansHigh_Type(OctetString):
    """Custom type caqAclHitCountVlansHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CaqAclHitCountVlansHigh_Type.__name__ = "OctetString"
_CaqAclHitCountVlansHigh_Object = MibScalar
caqAclHitCountVlansHigh = _CaqAclHitCountVlansHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 2),
    _CaqAclHitCountVlansHigh_Type()
)
caqAclHitCountVlansHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqAclHitCountVlansHigh.setStatus("current")
_CaqAclHitCountPortList_Type = CiscoPortList
_CaqAclHitCountPortList_Object = MibScalar
caqAclHitCountPortList = _CaqAclHitCountPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 3),
    _CaqAclHitCountPortList_Type()
)
caqAclHitCountPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqAclHitCountPortList.setStatus("current")
_CaqAclHitCountTable_Object = MibTable
caqAclHitCountTable = _CaqAclHitCountTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 4)
)
if mibBuilder.loadTexts:
    caqAclHitCountTable.setStatus("current")
_CaqAclHitCountEntry_Object = MibTableRow
caqAclHitCountEntry = _CaqAclHitCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 4, 1)
)
caqAclHitCountEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqAclHitCountAclType"),
    (1, "CISCO-CATOS-ACL-QOS-MIB", "caqAclHitCountAclName"),
)
if mibBuilder.loadTexts:
    caqAclHitCountEntry.setStatus("current")
_CaqAclHitCountAclType_Type = CaqHitCountAclType
_CaqAclHitCountAclType_Object = MibTableColumn
caqAclHitCountAclType = _CaqAclHitCountAclType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 4, 1, 1),
    _CaqAclHitCountAclType_Type()
)
caqAclHitCountAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqAclHitCountAclType.setStatus("current")
_CaqAclHitCountAclName_Type = CaqAclName
_CaqAclHitCountAclName_Object = MibTableColumn
caqAclHitCountAclName = _CaqAclHitCountAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 4, 1, 2),
    _CaqAclHitCountAclName_Type()
)
caqAclHitCountAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqAclHitCountAclName.setStatus("current")
_CaqAclHitCountEnable_Type = TruthValue
_CaqAclHitCountEnable_Object = MibTableColumn
caqAclHitCountEnable = _CaqAclHitCountEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 4, 1, 3),
    _CaqAclHitCountEnable_Type()
)
caqAclHitCountEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqAclHitCountEnable.setStatus("current")
_CaqAceHitCountTable_Object = MibTable
caqAceHitCountTable = _CaqAceHitCountTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 5)
)
if mibBuilder.loadTexts:
    caqAceHitCountTable.setStatus("current")
_CaqAceHitCountEntry_Object = MibTableRow
caqAceHitCountEntry = _CaqAceHitCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 5, 1)
)
caqAceHitCountEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqAceHitCountAclType"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqAceHitCountAclName"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqAceHitCountAceIndex"),
)
if mibBuilder.loadTexts:
    caqAceHitCountEntry.setStatus("current")
_CaqAceHitCountAclType_Type = CaqHitCountAclType
_CaqAceHitCountAclType_Object = MibTableColumn
caqAceHitCountAclType = _CaqAceHitCountAclType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 5, 1, 1),
    _CaqAceHitCountAclType_Type()
)
caqAceHitCountAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqAceHitCountAclType.setStatus("current")
_CaqAceHitCountAclName_Type = CaqAclName
_CaqAceHitCountAclName_Object = MibTableColumn
caqAceHitCountAclName = _CaqAceHitCountAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 5, 1, 2),
    _CaqAceHitCountAclName_Type()
)
caqAceHitCountAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqAceHitCountAclName.setStatus("current")


class _CaqAceHitCountAceIndex_Type(Unsigned32):
    """Custom type caqAceHitCountAceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CaqAceHitCountAceIndex_Type.__name__ = "Unsigned32"
_CaqAceHitCountAceIndex_Object = MibTableColumn
caqAceHitCountAceIndex = _CaqAceHitCountAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 5, 1, 3),
    _CaqAceHitCountAceIndex_Type()
)
caqAceHitCountAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqAceHitCountAceIndex.setStatus("current")
_CaqAceHitCountEnable_Type = TruthValue
_CaqAceHitCountEnable_Object = MibTableColumn
caqAceHitCountEnable = _CaqAceHitCountEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 5, 1, 4),
    _CaqAceHitCountEnable_Type()
)
caqAceHitCountEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqAceHitCountEnable.setStatus("current")
_CaqAceIngressHitCount_Type = Counter64
_CaqAceIngressHitCount_Object = MibTableColumn
caqAceIngressHitCount = _CaqAceIngressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 5, 1, 5),
    _CaqAceIngressHitCount_Type()
)
caqAceIngressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAceIngressHitCount.setStatus("current")
_CaqAceEgressHitCount_Type = Counter64
_CaqAceEgressHitCount_Object = MibTableColumn
caqAceEgressHitCount = _CaqAceEgressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 5, 1, 6),
    _CaqAceEgressHitCount_Type()
)
caqAceEgressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqAceEgressHitCount.setStatus("current")
_CaqIfAclHitCountTable_Object = MibTable
caqIfAclHitCountTable = _CaqIfAclHitCountTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 6)
)
if mibBuilder.loadTexts:
    caqIfAclHitCountTable.setStatus("current")
_CaqIfAclHitCountEntry_Object = MibTableRow
caqIfAclHitCountEntry = _CaqIfAclHitCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 6, 1)
)
caqIfAclHitCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqIfAclHitCountAclType"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqIfAclHitCountAclName"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqIfAclHitCountAceIndex"),
)
if mibBuilder.loadTexts:
    caqIfAclHitCountEntry.setStatus("current")
_CaqIfAclHitCountAclType_Type = CaqHitCountAclType
_CaqIfAclHitCountAclType_Object = MibTableColumn
caqIfAclHitCountAclType = _CaqIfAclHitCountAclType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 6, 1, 1),
    _CaqIfAclHitCountAclType_Type()
)
caqIfAclHitCountAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqIfAclHitCountAclType.setStatus("current")
_CaqIfAclHitCountAclName_Type = CaqAclName
_CaqIfAclHitCountAclName_Object = MibTableColumn
caqIfAclHitCountAclName = _CaqIfAclHitCountAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 6, 1, 2),
    _CaqIfAclHitCountAclName_Type()
)
caqIfAclHitCountAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqIfAclHitCountAclName.setStatus("current")


class _CaqIfAclHitCountAceIndex_Type(Unsigned32):
    """Custom type caqIfAclHitCountAceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CaqIfAclHitCountAceIndex_Type.__name__ = "Unsigned32"
_CaqIfAclHitCountAceIndex_Object = MibTableColumn
caqIfAclHitCountAceIndex = _CaqIfAclHitCountAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 6, 1, 3),
    _CaqIfAclHitCountAceIndex_Type()
)
caqIfAclHitCountAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqIfAclHitCountAceIndex.setStatus("current")
_CaqIfAclIngressHitCount_Type = Counter64
_CaqIfAclIngressHitCount_Object = MibTableColumn
caqIfAclIngressHitCount = _CaqIfAclIngressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 6, 1, 4),
    _CaqIfAclIngressHitCount_Type()
)
caqIfAclIngressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIfAclIngressHitCount.setStatus("current")
_CaqIfAclEgressHitCount_Type = Counter64
_CaqIfAclEgressHitCount_Object = MibTableColumn
caqIfAclEgressHitCount = _CaqIfAclEgressHitCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 9, 6, 1, 5),
    _CaqIfAclEgressHitCount_Type()
)
caqIfAclEgressHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIfAclEgressHitCount.setStatus("current")
_CaqDownloadAclObjects_ObjectIdentity = ObjectIdentity
caqDownloadAclObjects = _CaqDownloadAclObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10)
)
_CaqDownloadAclInfoTable_Object = MibTable
caqDownloadAclInfoTable = _CaqDownloadAclInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 1)
)
if mibBuilder.loadTexts:
    caqDownloadAclInfoTable.setStatus("current")
_CaqDownloadAclInfoEntry_Object = MibTableRow
caqDownloadAclInfoEntry = _CaqDownloadAclInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 1, 1)
)
caqDownloadAclInfoEntry.setIndexNames(
    (1, "CISCO-CATOS-ACL-QOS-MIB", "caqDownloadAclName"),
)
if mibBuilder.loadTexts:
    caqDownloadAclInfoEntry.setStatus("current")


class _CaqDownloadAclName_Type(SnmpAdminString):
    """Custom type caqDownloadAclName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CaqDownloadAclName_Type.__name__ = "SnmpAdminString"
_CaqDownloadAclName_Object = MibTableColumn
caqDownloadAclName = _CaqDownloadAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 1, 1, 1),
    _CaqDownloadAclName_Type()
)
caqDownloadAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqDownloadAclName.setStatus("current")
_CaqDownloadAclUserCount_Type = Unsigned32
_CaqDownloadAclUserCount_Object = MibTableColumn
caqDownloadAclUserCount = _CaqDownloadAclUserCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 1, 1, 2),
    _CaqDownloadAclUserCount_Type()
)
caqDownloadAclUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqDownloadAclUserCount.setStatus("current")
_CaqDownloadAclDownloadTime_Type = DateAndTime
_CaqDownloadAclDownloadTime_Object = MibTableColumn
caqDownloadAclDownloadTime = _CaqDownloadAclDownloadTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 1, 1, 3),
    _CaqDownloadAclDownloadTime_Type()
)
caqDownloadAclDownloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqDownloadAclDownloadTime.setStatus("current")
_CaqIpDownloadAceTable_Object = MibTable
caqIpDownloadAceTable = _CaqIpDownloadAceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2)
)
if mibBuilder.loadTexts:
    caqIpDownloadAceTable.setStatus("current")
_CaqIpDownloadAceEntry_Object = MibTableRow
caqIpDownloadAceEntry = _CaqIpDownloadAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1)
)
caqIpDownloadAceEntry.setIndexNames(
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAclName"),
    (0, "CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceIndex"),
)
if mibBuilder.loadTexts:
    caqIpDownloadAceEntry.setStatus("current")
_CaqIpDownloadAclName_Type = SnmpAdminString
_CaqIpDownloadAclName_Object = MibTableColumn
caqIpDownloadAclName = _CaqIpDownloadAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 1),
    _CaqIpDownloadAclName_Type()
)
caqIpDownloadAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqIpDownloadAclName.setStatus("current")
_CaqIpDownloadAceIndex_Type = Unsigned32
_CaqIpDownloadAceIndex_Object = MibTableColumn
caqIpDownloadAceIndex = _CaqIpDownloadAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 2),
    _CaqIpDownloadAceIndex_Type()
)
caqIpDownloadAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqIpDownloadAceIndex.setStatus("current")


class _CaqIpDownloadAceMatchedAction_Type(Integer32):
    """Custom type caqIpDownloadAceMatchedAction based on Integer32"""
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
        *(("deny", 2),
          ("denyAndLog", 3),
          ("permit", 1),
          ("permitAndCapture", 4))
    )


_CaqIpDownloadAceMatchedAction_Type.__name__ = "Integer32"
_CaqIpDownloadAceMatchedAction_Object = MibTableColumn
caqIpDownloadAceMatchedAction = _CaqIpDownloadAceMatchedAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 3),
    _CaqIpDownloadAceMatchedAction_Type()
)
caqIpDownloadAceMatchedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDownloadAceMatchedAction.setStatus("current")
_CaqIpDownloadAceProtocolType_Type = CiscoIpProtocol
_CaqIpDownloadAceProtocolType_Object = MibTableColumn
caqIpDownloadAceProtocolType = _CaqIpDownloadAceProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 4),
    _CaqIpDownloadAceProtocolType_Type()
)
caqIpDownloadAceProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDownloadAceProtocolType.setStatus("current")
_CaqIpDownloadAceAddrType_Type = InetAddressType
_CaqIpDownloadAceAddrType_Object = MibTableColumn
caqIpDownloadAceAddrType = _CaqIpDownloadAceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 5),
    _CaqIpDownloadAceAddrType_Type()
)
caqIpDownloadAceAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDownloadAceAddrType.setStatus("current")
_CaqIpDownloadAceSrcIp_Type = InetAddress
_CaqIpDownloadAceSrcIp_Object = MibTableColumn
caqIpDownloadAceSrcIp = _CaqIpDownloadAceSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 6),
    _CaqIpDownloadAceSrcIp_Type()
)
caqIpDownloadAceSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDownloadAceSrcIp.setStatus("current")
_CaqIpDownloadAceSrcIpMask_Type = InetAddress
_CaqIpDownloadAceSrcIpMask_Object = MibTableColumn
caqIpDownloadAceSrcIpMask = _CaqIpDownloadAceSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 7),
    _CaqIpDownloadAceSrcIpMask_Type()
)
caqIpDownloadAceSrcIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDownloadAceSrcIpMask.setStatus("current")


class _CaqIpDownloadAceSrcPortOp_Type(Integer32):
    """Custom type caqIpDownloadAceSrcPortOp based on Integer32"""
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
        *(("eq", 4),
          ("gt", 3),
          ("lt", 2),
          ("neq", 5),
          ("noOperator", 1),
          ("range", 6))
    )


_CaqIpDownloadAceSrcPortOp_Type.__name__ = "Integer32"
_CaqIpDownloadAceSrcPortOp_Object = MibTableColumn
caqIpDownloadAceSrcPortOp = _CaqIpDownloadAceSrcPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 8),
    _CaqIpDownloadAceSrcPortOp_Type()
)
caqIpDownloadAceSrcPortOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDownloadAceSrcPortOp.setStatus("current")
_CaqIpDownloadAceSrcPort_Type = InetPortNumber
_CaqIpDownloadAceSrcPort_Object = MibTableColumn
caqIpDownloadAceSrcPort = _CaqIpDownloadAceSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 9),
    _CaqIpDownloadAceSrcPort_Type()
)
caqIpDownloadAceSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDownloadAceSrcPort.setStatus("current")
_CaqIpDownloadAceSrcPortRange_Type = InetPortNumber
_CaqIpDownloadAceSrcPortRange_Object = MibTableColumn
caqIpDownloadAceSrcPortRange = _CaqIpDownloadAceSrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 10),
    _CaqIpDownloadAceSrcPortRange_Type()
)
caqIpDownloadAceSrcPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDownloadAceSrcPortRange.setStatus("current")
_CaqIpDownloadAceDestIp_Type = InetAddress
_CaqIpDownloadAceDestIp_Object = MibTableColumn
caqIpDownloadAceDestIp = _CaqIpDownloadAceDestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 11),
    _CaqIpDownloadAceDestIp_Type()
)
caqIpDownloadAceDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDownloadAceDestIp.setStatus("current")
_CaqIpDownloadAceDestIpMask_Type = InetAddress
_CaqIpDownloadAceDestIpMask_Object = MibTableColumn
caqIpDownloadAceDestIpMask = _CaqIpDownloadAceDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 12),
    _CaqIpDownloadAceDestIpMask_Type()
)
caqIpDownloadAceDestIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDownloadAceDestIpMask.setStatus("current")


class _CaqIpDownloadAceDestPortOp_Type(Integer32):
    """Custom type caqIpDownloadAceDestPortOp based on Integer32"""
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
        *(("eq", 4),
          ("gt", 3),
          ("lt", 2),
          ("neq", 5),
          ("noOperator", 1),
          ("range", 6))
    )


_CaqIpDownloadAceDestPortOp_Type.__name__ = "Integer32"
_CaqIpDownloadAceDestPortOp_Object = MibTableColumn
caqIpDownloadAceDestPortOp = _CaqIpDownloadAceDestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 13),
    _CaqIpDownloadAceDestPortOp_Type()
)
caqIpDownloadAceDestPortOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDownloadAceDestPortOp.setStatus("current")
_CaqIpDownloadAceDestPort_Type = InetPortNumber
_CaqIpDownloadAceDestPort_Object = MibTableColumn
caqIpDownloadAceDestPort = _CaqIpDownloadAceDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 14),
    _CaqIpDownloadAceDestPort_Type()
)
caqIpDownloadAceDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDownloadAceDestPort.setStatus("current")
_CaqIpDownloadAceDestPortRange_Type = InetPortNumber
_CaqIpDownloadAceDestPortRange_Object = MibTableColumn
caqIpDownloadAceDestPortRange = _CaqIpDownloadAceDestPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 15),
    _CaqIpDownloadAceDestPortRange_Type()
)
caqIpDownloadAceDestPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDownloadAceDestPortRange.setStatus("current")


class _CaqIpDownloadAceTosMatchCriteria_Type(Integer32):
    """Custom type caqIpDownloadAceTosMatchCriteria based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("matchDscp", 2),
          ("matchIpPrec", 3),
          ("none", 1))
    )


_CaqIpDownloadAceTosMatchCriteria_Type.__name__ = "Integer32"
_CaqIpDownloadAceTosMatchCriteria_Object = MibTableColumn
caqIpDownloadAceTosMatchCriteria = _CaqIpDownloadAceTosMatchCriteria_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 16),
    _CaqIpDownloadAceTosMatchCriteria_Type()
)
caqIpDownloadAceTosMatchCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDownloadAceTosMatchCriteria.setStatus("current")
_CaqIpDownloadAceIpPrec_Type = CaqIpPrecedence
_CaqIpDownloadAceIpPrec_Object = MibTableColumn
caqIpDownloadAceIpPrec = _CaqIpDownloadAceIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 17),
    _CaqIpDownloadAceIpPrec_Type()
)
caqIpDownloadAceIpPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDownloadAceIpPrec.setStatus("current")
_CaqIpDownloadAceDscp_Type = Dscp
_CaqIpDownloadAceDscp_Object = MibTableColumn
caqIpDownloadAceDscp = _CaqIpDownloadAceDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 18),
    _CaqIpDownloadAceDscp_Type()
)
caqIpDownloadAceDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDownloadAceDscp.setStatus("current")


class _CaqIpDnldAcePrtocolMatchCriteria_Type(Integer32):
    """Custom type caqIpDnldAcePrtocolMatchCriteria based on Integer32"""
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
        *(("matchEstablished", 4),
          ("matchIcmpType", 2),
          ("matchIcmpTypeAndCode", 3),
          ("none", 1))
    )


_CaqIpDnldAcePrtocolMatchCriteria_Type.__name__ = "Integer32"
_CaqIpDnldAcePrtocolMatchCriteria_Object = MibTableColumn
caqIpDnldAcePrtocolMatchCriteria = _CaqIpDnldAcePrtocolMatchCriteria_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 19),
    _CaqIpDnldAcePrtocolMatchCriteria_Type()
)
caqIpDnldAcePrtocolMatchCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDnldAcePrtocolMatchCriteria.setStatus("current")
_CaqIpDownloadAceIcmpType_Type = Unsigned32
_CaqIpDownloadAceIcmpType_Object = MibTableColumn
caqIpDownloadAceIcmpType = _CaqIpDownloadAceIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 20),
    _CaqIpDownloadAceIcmpType_Type()
)
caqIpDownloadAceIcmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDownloadAceIcmpType.setStatus("current")
_CaqIpDownloadAceIcmpCode_Type = Unsigned32
_CaqIpDownloadAceIcmpCode_Object = MibTableColumn
caqIpDownloadAceIcmpCode = _CaqIpDownloadAceIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 2, 1, 21),
    _CaqIpDownloadAceIcmpCode_Type()
)
caqIpDownloadAceIcmpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIpDownloadAceIcmpCode.setStatus("current")
_CaqIfDownloadAclTable_Object = MibTable
caqIfDownloadAclTable = _CaqIfDownloadAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 3)
)
if mibBuilder.loadTexts:
    caqIfDownloadAclTable.setStatus("current")
_CaqIfDownloadAclEntry_Object = MibTableRow
caqIfDownloadAclEntry = _CaqIfDownloadAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 3, 1)
)
caqIfDownloadAclEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (1, "CISCO-CATOS-ACL-QOS-MIB", "caqDownloadAclName"),
)
if mibBuilder.loadTexts:
    caqIfDownloadAclEntry.setStatus("current")


class _CaqIfDownloadAclFeature_Type(Integer32):
    """Custom type caqIfDownloadAclFeature based on Integer32"""
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
        *(("dot1x", 1),
          ("eou", 2),
          ("macAuth", 3),
          ("webAuth", 4))
    )


_CaqIfDownloadAclFeature_Type.__name__ = "Integer32"
_CaqIfDownloadAclFeature_Object = MibTableColumn
caqIfDownloadAclFeature = _CaqIfDownloadAclFeature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 3, 1, 1),
    _CaqIfDownloadAclFeature_Type()
)
caqIfDownloadAclFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIfDownloadAclFeature.setStatus("current")
_CaqIfDownloadAclAddressType_Type = InetAddressType
_CaqIfDownloadAclAddressType_Object = MibTableColumn
caqIfDownloadAclAddressType = _CaqIfDownloadAclAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 3, 1, 2),
    _CaqIfDownloadAclAddressType_Type()
)
caqIfDownloadAclAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIfDownloadAclAddressType.setStatus("current")
_CaqIfDownloadAclHostAddress_Type = InetAddress
_CaqIfDownloadAclHostAddress_Object = MibTableColumn
caqIfDownloadAclHostAddress = _CaqIfDownloadAclHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 3, 1, 3),
    _CaqIfDownloadAclHostAddress_Type()
)
caqIfDownloadAclHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIfDownloadAclHostAddress.setStatus("current")
_CaqIfIpPhoneMapTable_Object = MibTable
caqIfIpPhoneMapTable = _CaqIfIpPhoneMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 4)
)
if mibBuilder.loadTexts:
    caqIfIpPhoneMapTable.setStatus("current")
_CaqIfIpPhoneMapEntry_Object = MibTableRow
caqIfIpPhoneMapEntry = _CaqIfIpPhoneMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 4, 1)
)
caqIfIpPhoneMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    caqIfIpPhoneMapEntry.setStatus("current")
_CaqIfIpPhoneAddressType_Type = InetAddressType
_CaqIfIpPhoneAddressType_Object = MibTableColumn
caqIfIpPhoneAddressType = _CaqIfIpPhoneAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 4, 1, 1),
    _CaqIfIpPhoneAddressType_Type()
)
caqIfIpPhoneAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIfIpPhoneAddressType.setStatus("current")
_CaqIfIpPhoneHostAddress_Type = InetAddress
_CaqIfIpPhoneHostAddress_Object = MibTableColumn
caqIfIpPhoneHostAddress = _CaqIfIpPhoneHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 1, 10, 4, 1, 2),
    _CaqIfIpPhoneHostAddress_Type()
)
caqIfIpPhoneHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqIfIpPhoneHostAddress.setStatus("current")
_CaqMIBNotifications_ObjectIdentity = ObjectIdentity
caqMIBNotifications = _CaqMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 2)
)
_CaqMIBConformance_ObjectIdentity = ObjectIdentity
caqMIBConformance = _CaqMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3)
)
_CaqMIBCompliances_ObjectIdentity = ObjectIdentity
caqMIBCompliances = _CaqMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 1)
)
_CaqMIBGroups_ObjectIdentity = ObjectIdentity
caqMIBGroups = _CaqMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2)
)
cseFlowDataEntry.registerAugmentions(
    ("CISCO-CATOS-ACL-QOS-MIB",
     "caqFlowStatsEntry")
)
caqFlowStatsEntry.setIndexNames(*cseFlowDataEntry.getIndexNames())

# Managed Objects groups

caqIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 1)
)
caqIfConfigGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqIfTrustStateConfig"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIfCos"))
)
if mibBuilder.loadTexts:
    caqIfConfigGroup.setStatus("current")

caqIfAclConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 2)
)
caqIfAclConfigGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqIfAclBase"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqClassifierMapStatus"))
)
if mibBuilder.loadTexts:
    caqIfAclConfigGroup.setStatus("current")

caqAclCpbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 3)
)
caqAclCpbGroup.setObjects(
    ("CISCO-CATOS-ACL-QOS-MIB", "caqAclCapabilities")
)
if mibBuilder.loadTexts:
    caqAclCpbGroup.setStatus("current")

caqIpAceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 4)
)
caqIpAceGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceMatchedAction"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceProtocolType"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceAddrType"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceSrcIp"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceSrcIpMask"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceSrcPortOp"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceSrcPort"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceSrcPortRange"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceDestIp"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceDestIpMask"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceDestPortOp"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceDestPort"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceDestPortRange"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceTosMatchCriteria"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceProtocolMatchCriteria"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceIpPrec"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceDscp"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceIcmpType"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceIcmpCode"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceIgmpType"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceOrderPosition"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceBeforePosition"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceStatus"))
)
if mibBuilder.loadTexts:
    caqIpAceGroup.setStatus("current")

caqIpxAceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 5)
)
caqIpxAceGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqIpxAceMatchedAction"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpxAceSrcNet"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpxAceDestMatchCriteria"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpxAceDestNet"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpxAceProtocolType"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpxAceDestNode"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpxAceDestNetMask"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpxAceDestNodeMask"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpxAceOrderPosition"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpxAceBeforePosition"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpxAceStatus"))
)
if mibBuilder.loadTexts:
    caqIpxAceGroup.setStatus("current")

caqMacAceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 6)
)
caqMacAceGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqMacAceMatchedAction"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqMacAceSrcMac"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqMacAceSrcMacMask"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqMacAceDestMac"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqMacAceDestMacMask"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqMacAceEthertype"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqMacAceOrderPosition"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqMacAceBeforePosition"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqMacAceStatus"))
)
if mibBuilder.loadTexts:
    caqMacAceGroup.setStatus("current")

caqActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 7)
)
caqActionGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqQosActionSelectTrust"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqQosActionSelectDscp"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqQosActionSelectMicroflow"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqQosActionSelectAggregate"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqQosActionSelectStatus"))
)
if mibBuilder.loadTexts:
    caqActionGroup.setStatus("current")

caqPolicingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 8)
)
caqPolicingGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqFlowPolicerType"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqFlowPolicerExcessRateSupport"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqFlowPolicerNormalRateRequest"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqFlowPolicerNormalRateGrant"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqFlowPolicerBurstSizeRequest"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqFlowPolicerBurstSizeGrant"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqFlowPolicerNormalRateAction"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqFlowPolicerStatus"))
)
if mibBuilder.loadTexts:
    caqPolicingGroup.setStatus("current")

caqQosExcessRateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 9)
)
caqQosExcessRateGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqFlowPolicerExcessRateRequest"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqFlowPolicerExcessRateGrant"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqFlowPolicerExcessRateAction"))
)
if mibBuilder.loadTexts:
    caqQosExcessRateGroup.setStatus("current")

caqQosMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 10)
)
caqQosMappingGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqCosToDscpDscp"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpPrecToDscpDscp"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqDscpMappingCos"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqDscpMappingNRPolicedDscp"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqDscpMappingERPolicedDscp"))
)
if mibBuilder.loadTexts:
    caqQosMappingGroup.setStatus("current")

caqQueueAssignmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 11)
)
caqQueueAssignmentGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqCosAssignQueueNumber"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqCosAssignThresholdNumber"))
)
if mibBuilder.loadTexts:
    caqQueueAssignmentGroup.setStatus("current")

caqQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 12)
)
caqQueueGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqQueueThreshDropAlgorithm"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqQueueThreshDropThreshold"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqQueueThreshMinWredThreshold"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqQueueThreshMaxWredThreshold"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqQueueWrrWeight"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqQueueBufferSizeRatio"))
)
if mibBuilder.loadTexts:
    caqQueueGroup.setStatus("current")

caqQosBridgedFlowPolicerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 13)
)
caqQosBridgedFlowPolicerGroup.setObjects(
    ("CISCO-CATOS-ACL-QOS-MIB", "caqBridgedFlowEnabled")
)
if mibBuilder.loadTexts:
    caqQosBridgedFlowPolicerGroup.setStatus("current")

caqQosMacVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 14)
)
caqQosMacVlanGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqMacAddressCpb"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqCosValue"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqCosMacVlanRouterStatus"))
)
if mibBuilder.loadTexts:
    caqQosMacVlanGroup.setStatus("current")

caqQosStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 15)
)
caqQosStatsGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqL3PacketsDropByPolicer"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqTosChangedIpPackets"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqCosChangedIpPackets"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqCosChangedNonIpPackets"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqPortStatsDropPkts"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqFlowStatsOutOfProfilePackets"))
)
if mibBuilder.loadTexts:
    caqQosStatsGroup.setStatus("current")

caqSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 16)
)
caqSecurityGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqSecurityAction"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqSecurityCapture"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqSecurityRedirectPortList"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqSecurityActionStatus"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqSecurityAclCaptureEnable"))
)
if mibBuilder.loadTexts:
    caqSecurityGroup.setStatus("deprecated")

caqFlowPolicingCpbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 17)
)
caqFlowPolicingCpbGroup.setObjects(
    ("CISCO-CATOS-ACL-QOS-MIB", "caqFlowPolicingCpb")
)
if mibBuilder.loadTexts:
    caqFlowPolicingCpbGroup.setStatus("current")

caqQosStatsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 18)
)
caqQosStatsGroup2.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqAggPolicerPackets"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAggPolicerNRExceedPackets"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAggPolicerERExceedPackets"))
)
if mibBuilder.loadTexts:
    caqQosStatsGroup2.setStatus("current")

caqSecurityPBFGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 19)
)
caqSecurityPBFGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqPbfStatus"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqPbfMacAddress"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAdjDstVlanNumber"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAdjDstMacAddress"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAdjSrcMacAddress"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAdjName"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAdjMtu"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAdjHitCount"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAdjStatus"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqSecurityAdjIndex"))
)
if mibBuilder.loadTexts:
    caqSecurityPBFGroup.setStatus("current")

caqQosExcessBurstGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 20)
)
caqQosExcessBurstGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqFlowPolicerExcessBurstSupport"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqFlowPolicerExcessBurstRequest"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqFlowPolicerExcessBurstGrant"))
)
if mibBuilder.loadTexts:
    caqQosExcessBurstGroup.setStatus("current")

caqIfTrustDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 21)
)
caqIfTrustDeviceGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqIfTrustDevice"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIfOperTrustState"))
)
if mibBuilder.loadTexts:
    caqIfTrustDeviceGroup.setStatus("current")

caqLoggingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 22)
)
caqLoggingGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqAclLogMaxFlow"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAclSecurityLoggingRateLimit"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAclRouterAclRateLimit"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowVlan"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowIfIndex"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowProtocolType"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowAddrType"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowSrcIp"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowSrcPort"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowDestIp"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowDestPort"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowIcmpType"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowIcmpCode"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowIgmpType"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowArpOpcode"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowArpSrcMacAddr"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowArpHeaderSrcMacAddr"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowPacketsCount"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowLoggingTTL"))
)
if mibBuilder.loadTexts:
    caqLoggingGroup.setStatus("current")

caqArpInspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 23)
)
caqArpInspGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqSecurityArpMacAddress"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAclArpInspMatchMac"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAclArpInspAddrValidation"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqArpInspGlobalForwardedPkts"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqArpInspGlobalDroppedPkts"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqRARPForwardedPkts"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqMatchedMacFailedPkts"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAddrValidationFailedPkts"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqArpInspIpDroppedPkts"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqArpInspForwardedPackets"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqArpInspDroppedPackets"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIfArpInspDropThreshold"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIfArpInspShutdownThreshold"))
)
if mibBuilder.loadTexts:
    caqArpInspGroup.setStatus("current")

caqSecurityRateLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 24)
)
caqSecurityRateLimitGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqSecurityRateLimitFeatures"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqSecurityAclRateLimit"))
)
if mibBuilder.loadTexts:
    caqSecurityRateLimitGroup.setStatus("current")

caqDscpMutationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 25)
)
caqDscpMutationGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqDscpMutationNewDscp"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqVlanMutationTableId"))
)
if mibBuilder.loadTexts:
    caqDscpMutationGroup.setStatus("current")

caqQosDefaultActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 26)
)
caqQosDefaultActionGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqQosDefaultTrustState"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqQosDefaultDscp"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqQosDefaultMicroflow"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqQosDefaultAggregate"))
)
if mibBuilder.loadTexts:
    caqQosDefaultActionGroup.setStatus("current")

caqIfAclConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 27)
)
caqIfAclConfigGroup2.setObjects(
    ("CISCO-CATOS-ACL-QOS-MIB", "caqClassifierMapDirection")
)
if mibBuilder.loadTexts:
    caqIfAclConfigGroup2.setStatus("current")

caqIpEspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 28)
)
caqIpEspGroup.setObjects(
    ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceSecurityId")
)
if mibBuilder.loadTexts:
    caqIpEspGroup.setStatus("current")

caqDscpRewriteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 29)
)
caqDscpRewriteGroup.setObjects(
    ("CISCO-CATOS-ACL-QOS-MIB", "caqDscpRewriteEnabled")
)
if mibBuilder.loadTexts:
    caqDscpRewriteGroup.setStatus("current")

caqAggPolicerOctetStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 30)
)
caqAggPolicerOctetStatsGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqAggPolicerOctets"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAggPolicerNRExceedOctets"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAggPolicerERExceedOctets"))
)
if mibBuilder.loadTexts:
    caqAggPolicerOctetStatsGroup.setStatus("current")

caqSecurityGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 31)
)
caqSecurityGroup2.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqSecurityAction"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqSecurityCapture"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqSecurityRedirect2kPortList"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqSecurityActionStatus"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqSecurityAclCaptureEnable"))
)
if mibBuilder.loadTexts:
    caqSecurityGroup2.setStatus("current")

caqIfSecurityAclConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 32)
)
caqIfSecurityAclConfigGroup.setObjects(
    ("CISCO-CATOS-ACL-QOS-MIB", "caqIfSecurityAclBase")
)
if mibBuilder.loadTexts:
    caqIfSecurityAclConfigGroup.setStatus("current")

caqIpAceExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 33)
)
caqIpAceExtGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceSrcGroup"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceDestGroup"))
)
if mibBuilder.loadTexts:
    caqIpAceExtGroup.setStatus("current")

caqAclHitCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 34)
)
caqAclHitCountGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqAclHitCountEnable"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAceHitCountEnable"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAceIngressHitCount"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAceEgressHitCount"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIfAclIngressHitCount"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIfAclEgressHitCount"))
)
if mibBuilder.loadTexts:
    caqAclHitCountGroup.setStatus("current")

caqMacAceExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 35)
)
caqMacAceExtGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqMacAceMatchCriteria"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqMacAceVlan"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqMacAceCos"))
)
if mibBuilder.loadTexts:
    caqMacAceExtGroup.setStatus("current")

caqMacPktClassifyVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 36)
)
caqMacPktClassifyVlanGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqMacPktClassifyVlansLow"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqMacPktClassifyVlansHigh"))
)
if mibBuilder.loadTexts:
    caqMacPktClassifyVlanGroup.setStatus("current")

caqAclFeatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 37)
)
caqAclFeatureGroup.setObjects(
    ("CISCO-CATOS-ACL-QOS-MIB", "caqAclFeatureCpb")
)
if mibBuilder.loadTexts:
    caqAclFeatureGroup.setStatus("current")

caqPortAclHitCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 38)
)
caqPortAclHitCountGroup.setObjects(
    ("CISCO-CATOS-ACL-QOS-MIB", "caqAclHitCountPortList")
)
if mibBuilder.loadTexts:
    caqPortAclHitCountGroup.setStatus("current")

caqVlanAclHitCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 39)
)
caqVlanAclHitCountGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqAclHitCountVlansLow"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAclHitCountVlansHigh"))
)
if mibBuilder.loadTexts:
    caqVlanAclHitCountGroup.setStatus("current")

caqQosL3StatsRateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 40)
)
caqQosL3StatsRateGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqL3PacketsDropByPolicerAveRate"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqTosChangedIpPacketsAveRate"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqCosChangedNonIpPacketsAveRate"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqCosChangedIpPacketsAveRate"))
)
if mibBuilder.loadTexts:
    caqQosL3StatsRateGroup.setStatus("current")

caqQosL3StatsPeakGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 41)
)
caqQosL3StatsPeakGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqCosChangedNonIpPacketPeakRate"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqCosChangedIpPacketsPeakRate"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqL3PacketsDropByPolicerPeakRate"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqTosChangedIpPacketsPeakRate"))
)
if mibBuilder.loadTexts:
    caqQosL3StatsPeakGroup.setStatus("current")

caqAggPolicerOctetsRateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 42)
)
caqAggPolicerOctetsRateGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqAggPolicerOctetsRate"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAggPolicerNRExceedOctetsRate"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAggPolicerERExceedOctetsRate"))
)
if mibBuilder.loadTexts:
    caqAggPolicerOctetsRateGroup.setStatus("current")

caqAggPolicerPacketsRateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 43)
)
caqAggPolicerPacketsRateGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqAggPolicerPacketsRate"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAggPolicerNRExceedPacketsRate"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqAggPolicerERExceedPacketsRate"))
)
if mibBuilder.loadTexts:
    caqAggPolicerPacketsRateGroup.setStatus("current")

caqAggPolicerOctetsPeakGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 44)
)
caqAggPolicerOctetsPeakGroup.setObjects(
    ("CISCO-CATOS-ACL-QOS-MIB", "caqAggPolicerOctetsPeakRate")
)
if mibBuilder.loadTexts:
    caqAggPolicerOctetsPeakGroup.setStatus("current")

caqAggPolicerPacketsPeakGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 45)
)
caqAggPolicerPacketsPeakGroup.setObjects(
    ("CISCO-CATOS-ACL-QOS-MIB", "caqAggPolicerPacketsPeakRate")
)
if mibBuilder.loadTexts:
    caqAggPolicerPacketsPeakGroup.setStatus("current")

caqQosPortRateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 46)
)
caqQosPortRateGroup.setObjects(
    ("CISCO-CATOS-ACL-QOS-MIB", "caqPortStatsDropPktsAveRate")
)
if mibBuilder.loadTexts:
    caqQosPortRateGroup.setStatus("current")

caqQosPortPeakGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 47)
)
caqQosPortPeakGroup.setObjects(
    ("CISCO-CATOS-ACL-QOS-MIB", "caqPortStatsDropPktsPeakRate")
)
if mibBuilder.loadTexts:
    caqQosPortPeakGroup.setStatus("current")

caqSecurityActionDnldAceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 48)
)
caqSecurityActionDnldAceGroup.setObjects(
    ("CISCO-CATOS-ACL-QOS-MIB", "caqSecurityDownloadedAceFeature")
)
if mibBuilder.loadTexts:
    caqSecurityActionDnldAceGroup.setStatus("current")

caqSecurityDownloadAclInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 49)
)
caqSecurityDownloadAclInfoGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqDownloadAclUserCount"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqDownloadAclDownloadTime"))
)
if mibBuilder.loadTexts:
    caqSecurityDownloadAclInfoGroup.setStatus("current")

caqSecurityDownloadIpAceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 50)
)
caqSecurityDownloadIpAceGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceMatchedAction"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceProtocolType"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceAddrType"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceSrcIp"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceSrcIpMask"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceSrcPortOp"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceSrcPort"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceSrcPortRange"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceDestIp"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceDestIpMask"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceDestPortOp"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceDestPort"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceDestPortRange"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceTosMatchCriteria"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceIpPrec"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceDscp"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpDnldAcePrtocolMatchCriteria"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceIcmpType"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpDownloadAceIcmpCode"))
)
if mibBuilder.loadTexts:
    caqSecurityDownloadIpAceGroup.setStatus("current")

caqIfDownloadAclMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 51)
)
caqIfDownloadAclMapGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqIfDownloadAclFeature"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIfDownloadAclAddressType"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIfDownloadAclHostAddress"))
)
if mibBuilder.loadTexts:
    caqIfDownloadAclMapGroup.setStatus("current")

caqIfIpPhoneMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 52)
)
caqIfIpPhoneMapGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqIfIpPhoneAddressType"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIfIpPhoneHostAddress"))
)
if mibBuilder.loadTexts:
    caqIfIpPhoneMapGroup.setStatus("current")

caqIpAceTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 53)
)
caqIpAceTypeGroup.setObjects(
    ("CISCO-CATOS-ACL-QOS-MIB", "caqIpAceType")
)
if mibBuilder.loadTexts:
    caqIpAceTypeGroup.setStatus("current")

caqIpOperClassifierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 54)
)
caqIpOperClassifierGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqIpOperAclName"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpOperAclMapSource"))
)
if mibBuilder.loadTexts:
    caqIpOperClassifierGroup.setStatus("current")

caqDownloadClassifierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 55)
)
caqDownloadClassifierGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqDownloadClassifierAclName"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqDownloadMapSource"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqDownloadAclType"))
)
if mibBuilder.loadTexts:
    caqDownloadClassifierGroup.setStatus("current")

caqArpLoggingSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 2, 56)
)
caqArpLoggingSourceGroup.setObjects(
      *(("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowArpLoggingSource"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowArpAclName"),
        ("CISCO-CATOS-ACL-QOS-MIB", "caqIpFlowArpAceNumber"))
)
if mibBuilder.loadTexts:
    caqArpLoggingSourceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

caqMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 1, 1)
)
if mibBuilder.loadTexts:
    caqMIBCompliance.setStatus(
        "deprecated"
    )

caqMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 1, 2)
)
if mibBuilder.loadTexts:
    caqMIBCompliance2.setStatus(
        "deprecated"
    )

caqMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 1, 3)
)
if mibBuilder.loadTexts:
    caqMIBCompliance3.setStatus(
        "deprecated"
    )

caqMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 179, 3, 1, 4)
)
if mibBuilder.loadTexts:
    caqMIBCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CATOS-ACL-QOS-MIB",
    **{"CaqAclName": CaqAclName,
       "CaqPolicerName": CaqPolicerName,
       "CaqPolicerNameOrEmpty": CaqPolicerNameOrEmpty,
       "CaqAdjacencyName": CaqAdjacencyName,
       "CaqDirection": CaqDirection,
       "CaqIpPrecedence": CaqIpPrecedence,
       "CaqQueueNumber": CaqQueueNumber,
       "CaqThresholdNumber": CaqThresholdNumber,
       "CaqHitCountAclType": CaqHitCountAclType,
       "ciscoCatOSAclQosMIB": ciscoCatOSAclQosMIB,
       "ciscoCatOSAclQosMIBObjects": ciscoCatOSAclQosMIBObjects,
       "caqGlobalObjects": caqGlobalObjects,
       "caqCosToDscpTable": caqCosToDscpTable,
       "caqCosToDscpEntry": caqCosToDscpEntry,
       "caqCosToDscpCos": caqCosToDscpCos,
       "caqCosToDscpDscp": caqCosToDscpDscp,
       "caqIpPrecToDscpTable": caqIpPrecToDscpTable,
       "caqIpPrecToDscpEntry": caqIpPrecToDscpEntry,
       "caqIpPrecToDscpIpPrec": caqIpPrecToDscpIpPrec,
       "caqIpPrecToDscpDscp": caqIpPrecToDscpDscp,
       "caqDscpMappingTable": caqDscpMappingTable,
       "caqDscpMappingEntry": caqDscpMappingEntry,
       "caqDscpMappingDscp": caqDscpMappingDscp,
       "caqDscpMappingCos": caqDscpMappingCos,
       "caqDscpMappingNRPolicedDscp": caqDscpMappingNRPolicedDscp,
       "caqDscpMappingERPolicedDscp": caqDscpMappingERPolicedDscp,
       "caqCosAssignmentTable": caqCosAssignmentTable,
       "caqCosAssignmentEntry": caqCosAssignmentEntry,
       "caqCosAssignQueueType": caqCosAssignQueueType,
       "caqCosAssignCos": caqCosAssignCos,
       "caqCosAssignQueueNumber": caqCosAssignQueueNumber,
       "caqCosAssignThresholdNumber": caqCosAssignThresholdNumber,
       "caqQueueThresholdTable": caqQueueThresholdTable,
       "caqQueueThresholdEntry": caqQueueThresholdEntry,
       "caqQueueThreshQueueType": caqQueueThreshQueueType,
       "caqQueueThreshQueueIndex": caqQueueThreshQueueIndex,
       "caqQueueThreshThresholdIndex": caqQueueThreshThresholdIndex,
       "caqQueueThreshDropAlgorithm": caqQueueThreshDropAlgorithm,
       "caqQueueThreshDropThreshold": caqQueueThreshDropThreshold,
       "caqQueueThreshMinWredThreshold": caqQueueThreshMinWredThreshold,
       "caqQueueThreshMaxWredThreshold": caqQueueThreshMaxWredThreshold,
       "caqQueueTable": caqQueueTable,
       "caqQueueEntry": caqQueueEntry,
       "caqQueueDirection": caqQueueDirection,
       "caqQueueType": caqQueueType,
       "caqQueueNumber": caqQueueNumber,
       "caqQueueWrrWeight": caqQueueWrrWeight,
       "caqQueueBufferSizeRatio": caqQueueBufferSizeRatio,
       "caqDscpMutationMapTable": caqDscpMutationMapTable,
       "caqDscpMutationMapEntry": caqDscpMutationMapEntry,
       "caqDscpMutationTableId": caqDscpMutationTableId,
       "caqDscpMutationOldDscp": caqDscpMutationOldDscp,
       "caqDscpMutationNewDscp": caqDscpMutationNewDscp,
       "caqVlanMutationIdMapTable": caqVlanMutationIdMapTable,
       "caqVlanMutationIdMapEntry": caqVlanMutationIdMapEntry,
       "caqVlanMutationIndex": caqVlanMutationIndex,
       "caqVlanMutationTableId": caqVlanMutationTableId,
       "caqDscpRewriteEnabled": caqDscpRewriteEnabled,
       "caqMacPktClassifyVlansLow": caqMacPktClassifyVlansLow,
       "caqMacPktClassifyVlansHigh": caqMacPktClassifyVlansHigh,
       "caqInterfaceObjects": caqInterfaceObjects,
       "caqIfConfigTable": caqIfConfigTable,
       "caqIfConfigEntry": caqIfConfigEntry,
       "caqIfCos": caqIfCos,
       "caqIfTrustStateConfig": caqIfTrustStateConfig,
       "caqIfAclBase": caqIfAclBase,
       "caqIfTrustDevice": caqIfTrustDevice,
       "caqIfOperTrustState": caqIfOperTrustState,
       "caqClassifierTable": caqClassifierTable,
       "caqClassifierEntry": caqClassifierEntry,
       "caqClassifierAclType": caqClassifierAclType,
       "caqClassifierAclName": caqClassifierAclName,
       "caqClassifierMapStatus": caqClassifierMapStatus,
       "caqClassifierMapDirection": caqClassifierMapDirection,
       "caqIfSecurityAclConfigTable": caqIfSecurityAclConfigTable,
       "caqIfSecurityAclConfigEntry": caqIfSecurityAclConfigEntry,
       "caqIfSecurityAclBase": caqIfSecurityAclBase,
       "caqIpOperClassifierTable": caqIpOperClassifierTable,
       "caqIpOperClassifierEntry": caqIpOperClassifierEntry,
       "caqIpOperAclFeature": caqIpOperAclFeature,
       "caqIpOperAclName": caqIpOperAclName,
       "caqIpOperAclMapSource": caqIpOperAclMapSource,
       "caqDownloadClassifierTable": caqDownloadClassifierTable,
       "caqDownloadClassifierEntry": caqDownloadClassifierEntry,
       "caqDownloadAclFeature": caqDownloadAclFeature,
       "caqDownloadClassifierAclName": caqDownloadClassifierAclName,
       "caqDownloadMapSource": caqDownloadMapSource,
       "caqDownloadAclType": caqDownloadAclType,
       "caqAclObjects": caqAclObjects,
       "caqAclCapabilities": caqAclCapabilities,
       "caqIpAceTable": caqIpAceTable,
       "caqIpAceEntry": caqIpAceEntry,
       "caqIpAceFeature": caqIpAceFeature,
       "caqIpAclName": caqIpAclName,
       "caqIpAceIndex": caqIpAceIndex,
       "caqIpAceMatchedAction": caqIpAceMatchedAction,
       "caqIpAceProtocolType": caqIpAceProtocolType,
       "caqIpAceAddrType": caqIpAceAddrType,
       "caqIpAceSrcIp": caqIpAceSrcIp,
       "caqIpAceSrcIpMask": caqIpAceSrcIpMask,
       "caqIpAceSrcPortOp": caqIpAceSrcPortOp,
       "caqIpAceSrcPort": caqIpAceSrcPort,
       "caqIpAceSrcPortRange": caqIpAceSrcPortRange,
       "caqIpAceDestIp": caqIpAceDestIp,
       "caqIpAceDestIpMask": caqIpAceDestIpMask,
       "caqIpAceDestPortOp": caqIpAceDestPortOp,
       "caqIpAceDestPort": caqIpAceDestPort,
       "caqIpAceDestPortRange": caqIpAceDestPortRange,
       "caqIpAceTosMatchCriteria": caqIpAceTosMatchCriteria,
       "caqIpAceIpPrec": caqIpAceIpPrec,
       "caqIpAceDscp": caqIpAceDscp,
       "caqIpAceProtocolMatchCriteria": caqIpAceProtocolMatchCriteria,
       "caqIpAceIcmpType": caqIpAceIcmpType,
       "caqIpAceIcmpCode": caqIpAceIcmpCode,
       "caqIpAceIgmpType": caqIpAceIgmpType,
       "caqIpAceOrderPosition": caqIpAceOrderPosition,
       "caqIpAceBeforePosition": caqIpAceBeforePosition,
       "caqIpAceStatus": caqIpAceStatus,
       "caqIpAceSecurityId": caqIpAceSecurityId,
       "caqIpAceSrcGroup": caqIpAceSrcGroup,
       "caqIpAceDestGroup": caqIpAceDestGroup,
       "caqIpAceType": caqIpAceType,
       "caqIpxAceTable": caqIpxAceTable,
       "caqIpxAceEntry": caqIpxAceEntry,
       "caqIpxAceFeature": caqIpxAceFeature,
       "caqIpxAclName": caqIpxAclName,
       "caqIpxAceIndex": caqIpxAceIndex,
       "caqIpxAceMatchedAction": caqIpxAceMatchedAction,
       "caqIpxAceSrcNet": caqIpxAceSrcNet,
       "caqIpxAceDestMatchCriteria": caqIpxAceDestMatchCriteria,
       "caqIpxAceProtocolType": caqIpxAceProtocolType,
       "caqIpxAceDestNet": caqIpxAceDestNet,
       "caqIpxAceDestNode": caqIpxAceDestNode,
       "caqIpxAceDestNetMask": caqIpxAceDestNetMask,
       "caqIpxAceDestNodeMask": caqIpxAceDestNodeMask,
       "caqIpxAceOrderPosition": caqIpxAceOrderPosition,
       "caqIpxAceBeforePosition": caqIpxAceBeforePosition,
       "caqIpxAceStatus": caqIpxAceStatus,
       "caqMacAceTable": caqMacAceTable,
       "caqMacAceEntry": caqMacAceEntry,
       "caqMacAceFeature": caqMacAceFeature,
       "caqMacAclName": caqMacAclName,
       "caqMacAceIndex": caqMacAceIndex,
       "caqMacAceMatchedAction": caqMacAceMatchedAction,
       "caqMacAceSrcMac": caqMacAceSrcMac,
       "caqMacAceSrcMacMask": caqMacAceSrcMacMask,
       "caqMacAceDestMac": caqMacAceDestMac,
       "caqMacAceDestMacMask": caqMacAceDestMacMask,
       "caqMacAceEthertype": caqMacAceEthertype,
       "caqMacAceOrderPosition": caqMacAceOrderPosition,
       "caqMacAceBeforePosition": caqMacAceBeforePosition,
       "caqMacAceStatus": caqMacAceStatus,
       "caqMacAceMatchCriteria": caqMacAceMatchCriteria,
       "caqMacAceCos": caqMacAceCos,
       "caqMacAceVlan": caqMacAceVlan,
       "caqFlowPolicingCpb": caqFlowPolicingCpb,
       "caqQosActionSelectTable": caqQosActionSelectTable,
       "caqQosActionSelectEntry": caqQosActionSelectEntry,
       "caqQosActionSelectIndex": caqQosActionSelectIndex,
       "caqQosActionSelectTrust": caqQosActionSelectTrust,
       "caqQosActionSelectDscp": caqQosActionSelectDscp,
       "caqQosActionSelectMicroflow": caqQosActionSelectMicroflow,
       "caqQosActionSelectAggregate": caqQosActionSelectAggregate,
       "caqQosActionSelectStatus": caqQosActionSelectStatus,
       "caqFlowPolicerExcessRateSupport": caqFlowPolicerExcessRateSupport,
       "caqFlowPolicerTable": caqFlowPolicerTable,
       "caqFlowPolicerEntry": caqFlowPolicerEntry,
       "caqFlowPolicerName": caqFlowPolicerName,
       "caqFlowPolicerType": caqFlowPolicerType,
       "caqFlowPolicerNormalRateRequest": caqFlowPolicerNormalRateRequest,
       "caqFlowPolicerNormalRateGrant": caqFlowPolicerNormalRateGrant,
       "caqFlowPolicerNormalRateAction": caqFlowPolicerNormalRateAction,
       "caqFlowPolicerExcessRateRequest": caqFlowPolicerExcessRateRequest,
       "caqFlowPolicerExcessRateGrant": caqFlowPolicerExcessRateGrant,
       "caqFlowPolicerExcessRateAction": caqFlowPolicerExcessRateAction,
       "caqFlowPolicerBurstSizeRequest": caqFlowPolicerBurstSizeRequest,
       "caqFlowPolicerBurstSizeGrant": caqFlowPolicerBurstSizeGrant,
       "caqFlowPolicerStatus": caqFlowPolicerStatus,
       "caqFlowPolicerExcessBurstRequest": caqFlowPolicerExcessBurstRequest,
       "caqFlowPolicerExcessBurstGrant": caqFlowPolicerExcessBurstGrant,
       "caqSecurityActionTable": caqSecurityActionTable,
       "caqSecurityActionEntry": caqSecurityActionEntry,
       "caqSecurityActionIndex": caqSecurityActionIndex,
       "caqSecurityAction": caqSecurityAction,
       "caqSecurityRedirectPortList": caqSecurityRedirectPortList,
       "caqSecurityCapture": caqSecurityCapture,
       "caqSecurityActionStatus": caqSecurityActionStatus,
       "caqSecurityAdjIndex": caqSecurityAdjIndex,
       "caqSecurityArpMacAddress": caqSecurityArpMacAddress,
       "caqSecurityRedirect2kPortList": caqSecurityRedirect2kPortList,
       "caqSecurityDownloadedAceFeature": caqSecurityDownloadedAceFeature,
       "caqSecurityAclCaptureIfTable": caqSecurityAclCaptureIfTable,
       "caqSecurityAclCaptureIfEntry": caqSecurityAclCaptureIfEntry,
       "caqSecurityAclCaptureEnable": caqSecurityAclCaptureEnable,
       "caqFlowPolicerExcessBurstSupport": caqFlowPolicerExcessBurstSupport,
       "caqSecurityRateLimitFeatures": caqSecurityRateLimitFeatures,
       "caqSecurityAclRateLimit": caqSecurityAclRateLimit,
       "caqQosDefaultActionTable": caqQosDefaultActionTable,
       "caqQosDefaultActionEntry": caqQosDefaultActionEntry,
       "caqQosTrafficDirection": caqQosTrafficDirection,
       "caqQosTrafficType": caqQosTrafficType,
       "caqQosDefaultTrustState": caqQosDefaultTrustState,
       "caqQosDefaultDscp": caqQosDefaultDscp,
       "caqQosDefaultMicroflow": caqQosDefaultMicroflow,
       "caqQosDefaultAggregate": caqQosDefaultAggregate,
       "caqAclFeatureCpb": caqAclFeatureCpb,
       "caqQosStatsObjects": caqQosStatsObjects,
       "caqL3PacketsDropByPolicer": caqL3PacketsDropByPolicer,
       "caqTosChangedIpPackets": caqTosChangedIpPackets,
       "caqCosChangedIpPackets": caqCosChangedIpPackets,
       "caqCosChangedNonIpPackets": caqCosChangedNonIpPackets,
       "caqPortStatsTable": caqPortStatsTable,
       "caqPortStatsEntry": caqPortStatsEntry,
       "caqPortStatsDirection": caqPortStatsDirection,
       "caqPortStatsQueueNumber": caqPortStatsQueueNumber,
       "caqPortStatsThresholdNumber": caqPortStatsThresholdNumber,
       "caqPortStatsDropPkts": caqPortStatsDropPkts,
       "caqPortStatsDropPktsAveRate": caqPortStatsDropPktsAveRate,
       "caqPortStatsDropPktsPeakRate": caqPortStatsDropPktsPeakRate,
       "caqFlowStatsTable": caqFlowStatsTable,
       "caqFlowStatsEntry": caqFlowStatsEntry,
       "caqFlowStatsOutOfProfilePackets": caqFlowStatsOutOfProfilePackets,
       "caqAggPolicerStatsTable": caqAggPolicerStatsTable,
       "caqAggPolicerStatsEntry": caqAggPolicerStatsEntry,
       "caqAggPolicerName": caqAggPolicerName,
       "caqAggPolicerPackets": caqAggPolicerPackets,
       "caqAggPolicerNRExceedPackets": caqAggPolicerNRExceedPackets,
       "caqAggPolicerERExceedPackets": caqAggPolicerERExceedPackets,
       "caqAggPolicerOctets": caqAggPolicerOctets,
       "caqAggPolicerNRExceedOctets": caqAggPolicerNRExceedOctets,
       "caqAggPolicerERExceedOctets": caqAggPolicerERExceedOctets,
       "caqAggPolicerOctetsRate": caqAggPolicerOctetsRate,
       "caqAggPolicerNRExceedOctetsRate": caqAggPolicerNRExceedOctetsRate,
       "caqAggPolicerERExceedOctetsRate": caqAggPolicerERExceedOctetsRate,
       "caqAggPolicerOctetsPeakRate": caqAggPolicerOctetsPeakRate,
       "caqAggPolicerPacketsRate": caqAggPolicerPacketsRate,
       "caqAggPolicerNRExceedPacketsRate": caqAggPolicerNRExceedPacketsRate,
       "caqAggPolicerERExceedPacketsRate": caqAggPolicerERExceedPacketsRate,
       "caqAggPolicerPacketsPeakRate": caqAggPolicerPacketsPeakRate,
       "caqL3PacketsDropByPolicerAveRate": caqL3PacketsDropByPolicerAveRate,
       "caqL3PacketsDropByPolicerPeakRate": caqL3PacketsDropByPolicerPeakRate,
       "caqTosChangedIpPacketsAveRate": caqTosChangedIpPacketsAveRate,
       "caqTosChangedIpPacketsPeakRate": caqTosChangedIpPacketsPeakRate,
       "caqCosChangedIpPacketsAveRate": caqCosChangedIpPacketsAveRate,
       "caqCosChangedIpPacketsPeakRate": caqCosChangedIpPacketsPeakRate,
       "caqCosChangedNonIpPacketsAveRate": caqCosChangedNonIpPacketsAveRate,
       "caqCosChangedNonIpPacketPeakRate": caqCosChangedNonIpPacketPeakRate,
       "caqExtObjects": caqExtObjects,
       "caqBridgedPolicerTable": caqBridgedPolicerTable,
       "caqBridgedPolicerEntry": caqBridgedPolicerEntry,
       "caqBridgedFlowVlanIndex": caqBridgedFlowVlanIndex,
       "caqBridgedFlowEnabled": caqBridgedFlowEnabled,
       "caqCosMacVlanRouterTable": caqCosMacVlanRouterTable,
       "caqCosMacVlanRouterEntry": caqCosMacVlanRouterEntry,
       "caqCosMacAddress": caqCosMacAddress,
       "caqCosVlanNumber": caqCosVlanNumber,
       "caqMacAddressCpb": caqMacAddressCpb,
       "caqCosValue": caqCosValue,
       "caqCosMacVlanRouterStatus": caqCosMacVlanRouterStatus,
       "caqPbfObjects": caqPbfObjects,
       "caqPbfStatus": caqPbfStatus,
       "caqPbfMacAddress": caqPbfMacAddress,
       "caqAdjacencyTable": caqAdjacencyTable,
       "caqAdjacencyEntry": caqAdjacencyEntry,
       "caqAdjIndex": caqAdjIndex,
       "caqAdjDstVlanNumber": caqAdjDstVlanNumber,
       "caqAdjDstMacAddress": caqAdjDstMacAddress,
       "caqAdjSrcMacAddress": caqAdjSrcMacAddress,
       "caqAdjName": caqAdjName,
       "caqAdjMtu": caqAdjMtu,
       "caqAdjHitCount": caqAdjHitCount,
       "caqAdjStatus": caqAdjStatus,
       "caqLoggingObjects": caqLoggingObjects,
       "caqAclLogMaxFlow": caqAclLogMaxFlow,
       "caqAclSecurityLoggingRateLimit": caqAclSecurityLoggingRateLimit,
       "caqAclRouterAclRateLimit": caqAclRouterAclRateLimit,
       "caqIpFlowLoggingTable": caqIpFlowLoggingTable,
       "caqIpFlowLoggingEntry": caqIpFlowLoggingEntry,
       "caqIpFlowLoggingIndex": caqIpFlowLoggingIndex,
       "caqIpFlowVlan": caqIpFlowVlan,
       "caqIpFlowIfIndex": caqIpFlowIfIndex,
       "caqIpFlowProtocolType": caqIpFlowProtocolType,
       "caqIpFlowAddrType": caqIpFlowAddrType,
       "caqIpFlowSrcIp": caqIpFlowSrcIp,
       "caqIpFlowSrcPort": caqIpFlowSrcPort,
       "caqIpFlowDestIp": caqIpFlowDestIp,
       "caqIpFlowDestPort": caqIpFlowDestPort,
       "caqIpFlowIcmpType": caqIpFlowIcmpType,
       "caqIpFlowIcmpCode": caqIpFlowIcmpCode,
       "caqIpFlowIgmpType": caqIpFlowIgmpType,
       "caqIpFlowArpOpcode": caqIpFlowArpOpcode,
       "caqIpFlowArpSrcMacAddr": caqIpFlowArpSrcMacAddr,
       "caqIpFlowArpHeaderSrcMacAddr": caqIpFlowArpHeaderSrcMacAddr,
       "caqIpFlowPacketsCount": caqIpFlowPacketsCount,
       "caqIpFlowLoggingTTL": caqIpFlowLoggingTTL,
       "caqIpFlowArpLoggingSource": caqIpFlowArpLoggingSource,
       "caqIpFlowArpAclName": caqIpFlowArpAclName,
       "caqIpFlowArpAceNumber": caqIpFlowArpAceNumber,
       "caqArpInspObjects": caqArpInspObjects,
       "caqAclArpInspMatchMac": caqAclArpInspMatchMac,
       "caqAclArpInspAddrValidation": caqAclArpInspAddrValidation,
       "caqArpInspGlobalForwardedPkts": caqArpInspGlobalForwardedPkts,
       "caqArpInspGlobalDroppedPkts": caqArpInspGlobalDroppedPkts,
       "caqRARPForwardedPkts": caqRARPForwardedPkts,
       "caqMatchedMacFailedPkts": caqMatchedMacFailedPkts,
       "caqAddrValidationFailedPkts": caqAddrValidationFailedPkts,
       "caqArpInspIpDroppedPkts": caqArpInspIpDroppedPkts,
       "caqArpInspStatsTable": caqArpInspStatsTable,
       "caqArpInspStatsEntry": caqArpInspStatsEntry,
       "caqArpInspAclName": caqArpInspAclName,
       "caqArpInspForwardedPackets": caqArpInspForwardedPackets,
       "caqArpInspDroppedPackets": caqArpInspDroppedPackets,
       "caqIfArpInspConfigTable": caqIfArpInspConfigTable,
       "caqIfArpInspConfigEntry": caqIfArpInspConfigEntry,
       "caqIfArpInspDropThreshold": caqIfArpInspDropThreshold,
       "caqIfArpInspShutdownThreshold": caqIfArpInspShutdownThreshold,
       "caqAclHitCountObjects": caqAclHitCountObjects,
       "caqAclHitCountVlansLow": caqAclHitCountVlansLow,
       "caqAclHitCountVlansHigh": caqAclHitCountVlansHigh,
       "caqAclHitCountPortList": caqAclHitCountPortList,
       "caqAclHitCountTable": caqAclHitCountTable,
       "caqAclHitCountEntry": caqAclHitCountEntry,
       "caqAclHitCountAclType": caqAclHitCountAclType,
       "caqAclHitCountAclName": caqAclHitCountAclName,
       "caqAclHitCountEnable": caqAclHitCountEnable,
       "caqAceHitCountTable": caqAceHitCountTable,
       "caqAceHitCountEntry": caqAceHitCountEntry,
       "caqAceHitCountAclType": caqAceHitCountAclType,
       "caqAceHitCountAclName": caqAceHitCountAclName,
       "caqAceHitCountAceIndex": caqAceHitCountAceIndex,
       "caqAceHitCountEnable": caqAceHitCountEnable,
       "caqAceIngressHitCount": caqAceIngressHitCount,
       "caqAceEgressHitCount": caqAceEgressHitCount,
       "caqIfAclHitCountTable": caqIfAclHitCountTable,
       "caqIfAclHitCountEntry": caqIfAclHitCountEntry,
       "caqIfAclHitCountAclType": caqIfAclHitCountAclType,
       "caqIfAclHitCountAclName": caqIfAclHitCountAclName,
       "caqIfAclHitCountAceIndex": caqIfAclHitCountAceIndex,
       "caqIfAclIngressHitCount": caqIfAclIngressHitCount,
       "caqIfAclEgressHitCount": caqIfAclEgressHitCount,
       "caqDownloadAclObjects": caqDownloadAclObjects,
       "caqDownloadAclInfoTable": caqDownloadAclInfoTable,
       "caqDownloadAclInfoEntry": caqDownloadAclInfoEntry,
       "caqDownloadAclName": caqDownloadAclName,
       "caqDownloadAclUserCount": caqDownloadAclUserCount,
       "caqDownloadAclDownloadTime": caqDownloadAclDownloadTime,
       "caqIpDownloadAceTable": caqIpDownloadAceTable,
       "caqIpDownloadAceEntry": caqIpDownloadAceEntry,
       "caqIpDownloadAclName": caqIpDownloadAclName,
       "caqIpDownloadAceIndex": caqIpDownloadAceIndex,
       "caqIpDownloadAceMatchedAction": caqIpDownloadAceMatchedAction,
       "caqIpDownloadAceProtocolType": caqIpDownloadAceProtocolType,
       "caqIpDownloadAceAddrType": caqIpDownloadAceAddrType,
       "caqIpDownloadAceSrcIp": caqIpDownloadAceSrcIp,
       "caqIpDownloadAceSrcIpMask": caqIpDownloadAceSrcIpMask,
       "caqIpDownloadAceSrcPortOp": caqIpDownloadAceSrcPortOp,
       "caqIpDownloadAceSrcPort": caqIpDownloadAceSrcPort,
       "caqIpDownloadAceSrcPortRange": caqIpDownloadAceSrcPortRange,
       "caqIpDownloadAceDestIp": caqIpDownloadAceDestIp,
       "caqIpDownloadAceDestIpMask": caqIpDownloadAceDestIpMask,
       "caqIpDownloadAceDestPortOp": caqIpDownloadAceDestPortOp,
       "caqIpDownloadAceDestPort": caqIpDownloadAceDestPort,
       "caqIpDownloadAceDestPortRange": caqIpDownloadAceDestPortRange,
       "caqIpDownloadAceTosMatchCriteria": caqIpDownloadAceTosMatchCriteria,
       "caqIpDownloadAceIpPrec": caqIpDownloadAceIpPrec,
       "caqIpDownloadAceDscp": caqIpDownloadAceDscp,
       "caqIpDnldAcePrtocolMatchCriteria": caqIpDnldAcePrtocolMatchCriteria,
       "caqIpDownloadAceIcmpType": caqIpDownloadAceIcmpType,
       "caqIpDownloadAceIcmpCode": caqIpDownloadAceIcmpCode,
       "caqIfDownloadAclTable": caqIfDownloadAclTable,
       "caqIfDownloadAclEntry": caqIfDownloadAclEntry,
       "caqIfDownloadAclFeature": caqIfDownloadAclFeature,
       "caqIfDownloadAclAddressType": caqIfDownloadAclAddressType,
       "caqIfDownloadAclHostAddress": caqIfDownloadAclHostAddress,
       "caqIfIpPhoneMapTable": caqIfIpPhoneMapTable,
       "caqIfIpPhoneMapEntry": caqIfIpPhoneMapEntry,
       "caqIfIpPhoneAddressType": caqIfIpPhoneAddressType,
       "caqIfIpPhoneHostAddress": caqIfIpPhoneHostAddress,
       "caqMIBNotifications": caqMIBNotifications,
       "caqMIBConformance": caqMIBConformance,
       "caqMIBCompliances": caqMIBCompliances,
       "caqMIBCompliance": caqMIBCompliance,
       "caqMIBCompliance2": caqMIBCompliance2,
       "caqMIBCompliance3": caqMIBCompliance3,
       "caqMIBCompliance4": caqMIBCompliance4,
       "caqMIBGroups": caqMIBGroups,
       "caqIfConfigGroup": caqIfConfigGroup,
       "caqIfAclConfigGroup": caqIfAclConfigGroup,
       "caqAclCpbGroup": caqAclCpbGroup,
       "caqIpAceGroup": caqIpAceGroup,
       "caqIpxAceGroup": caqIpxAceGroup,
       "caqMacAceGroup": caqMacAceGroup,
       "caqActionGroup": caqActionGroup,
       "caqPolicingGroup": caqPolicingGroup,
       "caqQosExcessRateGroup": caqQosExcessRateGroup,
       "caqQosMappingGroup": caqQosMappingGroup,
       "caqQueueAssignmentGroup": caqQueueAssignmentGroup,
       "caqQueueGroup": caqQueueGroup,
       "caqQosBridgedFlowPolicerGroup": caqQosBridgedFlowPolicerGroup,
       "caqQosMacVlanGroup": caqQosMacVlanGroup,
       "caqQosStatsGroup": caqQosStatsGroup,
       "caqSecurityGroup": caqSecurityGroup,
       "caqFlowPolicingCpbGroup": caqFlowPolicingCpbGroup,
       "caqQosStatsGroup2": caqQosStatsGroup2,
       "caqSecurityPBFGroup": caqSecurityPBFGroup,
       "caqQosExcessBurstGroup": caqQosExcessBurstGroup,
       "caqIfTrustDeviceGroup": caqIfTrustDeviceGroup,
       "caqLoggingGroup": caqLoggingGroup,
       "caqArpInspGroup": caqArpInspGroup,
       "caqSecurityRateLimitGroup": caqSecurityRateLimitGroup,
       "caqDscpMutationGroup": caqDscpMutationGroup,
       "caqQosDefaultActionGroup": caqQosDefaultActionGroup,
       "caqIfAclConfigGroup2": caqIfAclConfigGroup2,
       "caqIpEspGroup": caqIpEspGroup,
       "caqDscpRewriteGroup": caqDscpRewriteGroup,
       "caqAggPolicerOctetStatsGroup": caqAggPolicerOctetStatsGroup,
       "caqSecurityGroup2": caqSecurityGroup2,
       "caqIfSecurityAclConfigGroup": caqIfSecurityAclConfigGroup,
       "caqIpAceExtGroup": caqIpAceExtGroup,
       "caqAclHitCountGroup": caqAclHitCountGroup,
       "caqMacAceExtGroup": caqMacAceExtGroup,
       "caqMacPktClassifyVlanGroup": caqMacPktClassifyVlanGroup,
       "caqAclFeatureGroup": caqAclFeatureGroup,
       "caqPortAclHitCountGroup": caqPortAclHitCountGroup,
       "caqVlanAclHitCountGroup": caqVlanAclHitCountGroup,
       "caqQosL3StatsRateGroup": caqQosL3StatsRateGroup,
       "caqQosL3StatsPeakGroup": caqQosL3StatsPeakGroup,
       "caqAggPolicerOctetsRateGroup": caqAggPolicerOctetsRateGroup,
       "caqAggPolicerPacketsRateGroup": caqAggPolicerPacketsRateGroup,
       "caqAggPolicerOctetsPeakGroup": caqAggPolicerOctetsPeakGroup,
       "caqAggPolicerPacketsPeakGroup": caqAggPolicerPacketsPeakGroup,
       "caqQosPortRateGroup": caqQosPortRateGroup,
       "caqQosPortPeakGroup": caqQosPortPeakGroup,
       "caqSecurityActionDnldAceGroup": caqSecurityActionDnldAceGroup,
       "caqSecurityDownloadAclInfoGroup": caqSecurityDownloadAclInfoGroup,
       "caqSecurityDownloadIpAceGroup": caqSecurityDownloadIpAceGroup,
       "caqIfDownloadAclMapGroup": caqIfDownloadAclMapGroup,
       "caqIfIpPhoneMapGroup": caqIfIpPhoneMapGroup,
       "caqIpAceTypeGroup": caqIpAceTypeGroup,
       "caqIpOperClassifierGroup": caqIpOperClassifierGroup,
       "caqDownloadClassifierGroup": caqDownloadClassifierGroup,
       "caqArpLoggingSourceGroup": caqArpLoggingSourceGroup}
)

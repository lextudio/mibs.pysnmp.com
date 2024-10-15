# SNMP MIB module (NTN-QOS-POLICY-EVOL-PIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTN-QOS-POLICY-EVOL-PIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:41 2024
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

(bnIfExtnPort,
 bnIfExtnSlot) = mibBuilder.importSymbols(
    "BN-IF-EXTENSIONS-MIB",
    "bnIfExtnPort",
    "bnIfExtnSlot")

(Dscp,
 DscpOrAny) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp",
    "DscpOrAny")

(IndexInteger,
 IndexIntegerNextFree) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IndexInteger",
    "IndexIntegerNextFree")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv4,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(BurstSize,) = mibBuilder.importSymbols(
    "INTEGRATED-SERVICES-MIB",
    "BurstSize")

(Role,
 RoleCombination) = mibBuilder.importSymbols(
    "POLICY-FRAMEWORK-PIB",
    "Role",
    "RoleCombination")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "zeroDotZero")

(AutonomousType,
 DisplayString,
 MacAddress,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")

(policy,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "policy")


# MODULE-IDENTITY

ntnQosPolicyEvolPib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7)
)
ntnQosPolicyEvolPib.setRevisions(
        ("2015-02-20 00:00",
         "2014-04-03 00:00",
         "2014-02-14 00:00",
         "2012-06-14 00:00",
         "2012-05-16 00:00",
         "2012-03-16 00:00",
         "2012-01-13 00:00",
         "2011-07-26 00:00",
         "2011-07-15 00:00",
         "2011-04-15 00:00",
         "2010-03-08 00:00",
         "2010-01-05 00:00",
         "2009-11-05 00:00",
         "2009-08-11 00:00",
         "2009-03-26 00:00",
         "2009-01-05 00:00",
         "2008-11-05 00:00",
         "2008-07-09 00:00",
         "2008-07-02 00:00",
         "2008-06-26 00:00",
         "2008-05-29 00:00",
         "2006-09-28 00:00",
         "2006-04-21 00:00",
         "2005-02-03 00:00",
         "2004-10-25 00:00",
         "2004-09-20 00:00",
         "2004-07-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IndexIntegerOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class QosIeee802Cos(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class FlowIdOrAny(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1048575),
    )



class DscpUpdate(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(64, 64),
    )



class VersionIndicator(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )



class FcId(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x.1x.1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class InterfaceList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



# MIB Managed Objects in the order of their OIDs

_NtnQosPolicyEvolPibClasses_ObjectIdentity = ObjectIdentity
ntnQosPolicyEvolPibClasses = _NtnQosPolicyEvolPibClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1)
)
_NtnQosInterfaceTypeTable_Object = MibTable
ntnQosInterfaceTypeTable = _NtnQosInterfaceTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 1)
)
if mibBuilder.loadTexts:
    ntnQosInterfaceTypeTable.setStatus("current")
_NtnQosInterfaceTypeEntry_Object = MibTableRow
ntnQosInterfaceTypeEntry = _NtnQosInterfaceTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 1, 1)
)
ntnQosInterfaceTypeEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosInterfaceTypeId"),
)
if mibBuilder.loadTexts:
    ntnQosInterfaceTypeEntry.setStatus("current")
_NtnQosInterfaceTypeId_Type = IndexInteger
_NtnQosInterfaceTypeId_Object = MibTableColumn
ntnQosInterfaceTypeId = _NtnQosInterfaceTypeId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 1, 1, 1),
    _NtnQosInterfaceTypeId_Type()
)
ntnQosInterfaceTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosInterfaceTypeId.setStatus("current")
_NtnQosInterfaceTypeRoles_Type = RoleCombination
_NtnQosInterfaceTypeRoles_Object = MibTableColumn
ntnQosInterfaceTypeRoles = _NtnQosInterfaceTypeRoles_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 1, 1, 2),
    _NtnQosInterfaceTypeRoles_Type()
)
ntnQosInterfaceTypeRoles.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosInterfaceTypeRoles.setStatus("current")


class _NtnQosInterfaceTypeIfClass_Type(Integer32):
    """Custom type ntnQosInterfaceTypeIfClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonTrusted", 2),
          ("trusted", 1),
          ("unrestricted", 3))
    )


_NtnQosInterfaceTypeIfClass_Type.__name__ = "Integer32"
_NtnQosInterfaceTypeIfClass_Object = MibTableColumn
ntnQosInterfaceTypeIfClass = _NtnQosInterfaceTypeIfClass_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 1, 1, 3),
    _NtnQosInterfaceTypeIfClass_Type()
)
ntnQosInterfaceTypeIfClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosInterfaceTypeIfClass.setStatus("current")


class _NtnQosInterfaceTypeCapabilities_Type(Bits):
    """Custom type ntnQosInterfaceTypeCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("input802Classification", 3),
          ("inputIpClassification", 1),
          ("other", 0),
          ("output802Classification", 4),
          ("outputIpClassification", 2))
    )

_NtnQosInterfaceTypeCapabilities_Type.__name__ = "Bits"
_NtnQosInterfaceTypeCapabilities_Object = MibTableColumn
ntnQosInterfaceTypeCapabilities = _NtnQosInterfaceTypeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 1, 1, 4),
    _NtnQosInterfaceTypeCapabilities_Type()
)
ntnQosInterfaceTypeCapabilities.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosInterfaceTypeCapabilities.setStatus("current")


class _NtnQosInterfaceTypeStorageType_Type(StorageType):
    """Custom type ntnQosInterfaceTypeStorageType based on StorageType"""


_NtnQosInterfaceTypeStorageType_Object = MibTableColumn
ntnQosInterfaceTypeStorageType = _NtnQosInterfaceTypeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 1, 1, 5),
    _NtnQosInterfaceTypeStorageType_Type()
)
ntnQosInterfaceTypeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosInterfaceTypeStorageType.setStatus("current")
_NtnQosInterfaceTypeStatus_Type = RowStatus
_NtnQosInterfaceTypeStatus_Object = MibTableColumn
ntnQosInterfaceTypeStatus = _NtnQosInterfaceTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 1, 1, 6),
    _NtnQosInterfaceTypeStatus_Type()
)
ntnQosInterfaceTypeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosInterfaceTypeStatus.setStatus("current")
_NtnQosQsetPriAssignmentTable_Object = MibTable
ntnQosQsetPriAssignmentTable = _NtnQosQsetPriAssignmentTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 2)
)
if mibBuilder.loadTexts:
    ntnQosQsetPriAssignmentTable.setStatus("current")
_NtnQosQsetPriAssignmentEntry_Object = MibTableRow
ntnQosQsetPriAssignmentEntry = _NtnQosQsetPriAssignmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 2, 1)
)
ntnQosQsetPriAssignmentEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosQsetPriAssignmentId"),
)
if mibBuilder.loadTexts:
    ntnQosQsetPriAssignmentEntry.setStatus("current")
_NtnQosQsetPriAssignmentId_Type = IndexInteger
_NtnQosQsetPriAssignmentId_Object = MibTableColumn
ntnQosQsetPriAssignmentId = _NtnQosQsetPriAssignmentId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 2, 1, 1),
    _NtnQosQsetPriAssignmentId_Type()
)
ntnQosQsetPriAssignmentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosQsetPriAssignmentId.setStatus("current")


class _NtnQosQsetPriAssignmentQset_Type(Integer32):
    """Custom type ntnQosQsetPriAssignmentQset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtnQosQsetPriAssignmentQset_Type.__name__ = "Integer32"
_NtnQosQsetPriAssignmentQset_Object = MibTableColumn
ntnQosQsetPriAssignmentQset = _NtnQosQsetPriAssignmentQset_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 2, 1, 2),
    _NtnQosQsetPriAssignmentQset_Type()
)
ntnQosQsetPriAssignmentQset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosQsetPriAssignmentQset.setStatus("current")
_NtnQosQsetPriAssignmentPri_Type = QosIeee802Cos
_NtnQosQsetPriAssignmentPri_Object = MibTableColumn
ntnQosQsetPriAssignmentPri = _NtnQosQsetPriAssignmentPri_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 2, 1, 3),
    _NtnQosQsetPriAssignmentPri_Type()
)
ntnQosQsetPriAssignmentPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosQsetPriAssignmentPri.setStatus("current")


class _NtnQosQsetPriAssignmentQueue_Type(Integer32):
    """Custom type ntnQosQsetPriAssignmentQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NtnQosQsetPriAssignmentQueue_Type.__name__ = "Integer32"
_NtnQosQsetPriAssignmentQueue_Object = MibTableColumn
ntnQosQsetPriAssignmentQueue = _NtnQosQsetPriAssignmentQueue_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 2, 1, 4),
    _NtnQosQsetPriAssignmentQueue_Type()
)
ntnQosQsetPriAssignmentQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosQsetPriAssignmentQueue.setStatus("current")


class _NtnQosQsetPriAssignmentStorageType_Type(StorageType):
    """Custom type ntnQosQsetPriAssignmentStorageType based on StorageType"""


_NtnQosQsetPriAssignmentStorageType_Object = MibTableColumn
ntnQosQsetPriAssignmentStorageType = _NtnQosQsetPriAssignmentStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 2, 1, 5),
    _NtnQosQsetPriAssignmentStorageType_Type()
)
ntnQosQsetPriAssignmentStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosQsetPriAssignmentStorageType.setStatus("current")
_NtnQosQsetPriAssignmentStatus_Type = RowStatus
_NtnQosQsetPriAssignmentStatus_Object = MibTableColumn
ntnQosQsetPriAssignmentStatus = _NtnQosQsetPriAssignmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 2, 1, 6),
    _NtnQosQsetPriAssignmentStatus_Type()
)
ntnQosQsetPriAssignmentStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosQsetPriAssignmentStatus.setStatus("current")
_NtnQosQsetDscpAssignmentTable_Object = MibTable
ntnQosQsetDscpAssignmentTable = _NtnQosQsetDscpAssignmentTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 3)
)
if mibBuilder.loadTexts:
    ntnQosQsetDscpAssignmentTable.setStatus("current")
_NtnQosQsetDscpAssignmentEntry_Object = MibTableRow
ntnQosQsetDscpAssignmentEntry = _NtnQosQsetDscpAssignmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 3, 1)
)
ntnQosQsetDscpAssignmentEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosQsetDscpAssignmentId"),
)
if mibBuilder.loadTexts:
    ntnQosQsetDscpAssignmentEntry.setStatus("current")
_NtnQosQsetDscpAssignmentId_Type = IndexInteger
_NtnQosQsetDscpAssignmentId_Object = MibTableColumn
ntnQosQsetDscpAssignmentId = _NtnQosQsetDscpAssignmentId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 3, 1, 1),
    _NtnQosQsetDscpAssignmentId_Type()
)
ntnQosQsetDscpAssignmentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosQsetDscpAssignmentId.setStatus("current")


class _NtnQosQsetDscpAssignmentQset_Type(Integer32):
    """Custom type ntnQosQsetDscpAssignmentQset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtnQosQsetDscpAssignmentQset_Type.__name__ = "Integer32"
_NtnQosQsetDscpAssignmentQset_Object = MibTableColumn
ntnQosQsetDscpAssignmentQset = _NtnQosQsetDscpAssignmentQset_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 3, 1, 2),
    _NtnQosQsetDscpAssignmentQset_Type()
)
ntnQosQsetDscpAssignmentQset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosQsetDscpAssignmentQset.setStatus("current")
_NtnQosQsetDscpAssignmentDscp_Type = Dscp
_NtnQosQsetDscpAssignmentDscp_Object = MibTableColumn
ntnQosQsetDscpAssignmentDscp = _NtnQosQsetDscpAssignmentDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 3, 1, 3),
    _NtnQosQsetDscpAssignmentDscp_Type()
)
ntnQosQsetDscpAssignmentDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosQsetDscpAssignmentDscp.setStatus("current")


class _NtnQosQsetDscpAssignmentQueue_Type(Integer32):
    """Custom type ntnQosQsetDscpAssignmentQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NtnQosQsetDscpAssignmentQueue_Type.__name__ = "Integer32"
_NtnQosQsetDscpAssignmentQueue_Object = MibTableColumn
ntnQosQsetDscpAssignmentQueue = _NtnQosQsetDscpAssignmentQueue_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 3, 1, 4),
    _NtnQosQsetDscpAssignmentQueue_Type()
)
ntnQosQsetDscpAssignmentQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosQsetDscpAssignmentQueue.setStatus("current")


class _NtnQosQsetDscpAssignmentStorageType_Type(StorageType):
    """Custom type ntnQosQsetDscpAssignmentStorageType based on StorageType"""


_NtnQosQsetDscpAssignmentStorageType_Object = MibTableColumn
ntnQosQsetDscpAssignmentStorageType = _NtnQosQsetDscpAssignmentStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 3, 1, 5),
    _NtnQosQsetDscpAssignmentStorageType_Type()
)
ntnQosQsetDscpAssignmentStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosQsetDscpAssignmentStorageType.setStatus("current")
_NtnQosQsetDscpAssignmentStatus_Type = RowStatus
_NtnQosQsetDscpAssignmentStatus_Object = MibTableColumn
ntnQosQsetDscpAssignmentStatus = _NtnQosQsetDscpAssignmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 3, 1, 6),
    _NtnQosQsetDscpAssignmentStatus_Type()
)
ntnQosQsetDscpAssignmentStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosQsetDscpAssignmentStatus.setStatus("current")
_NtnQosShapingParamsTable_Object = MibTable
ntnQosShapingParamsTable = _NtnQosShapingParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 4)
)
if mibBuilder.loadTexts:
    ntnQosShapingParamsTable.setStatus("current")
_NtnQosShapingParamsEntry_Object = MibTableRow
ntnQosShapingParamsEntry = _NtnQosShapingParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 4, 1)
)
ntnQosShapingParamsEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosShapingParamsId"),
)
if mibBuilder.loadTexts:
    ntnQosShapingParamsEntry.setStatus("current")
_NtnQosShapingParamsId_Type = IndexInteger
_NtnQosShapingParamsId_Object = MibTableColumn
ntnQosShapingParamsId = _NtnQosShapingParamsId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 4, 1, 1),
    _NtnQosShapingParamsId_Type()
)
ntnQosShapingParamsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosShapingParamsId.setStatus("current")


class _NtnQosShapingParamsRate_Type(Unsigned32):
    """Custom type ntnQosShapingParamsRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NtnQosShapingParamsRate_Type.__name__ = "Unsigned32"
_NtnQosShapingParamsRate_Object = MibTableColumn
ntnQosShapingParamsRate = _NtnQosShapingParamsRate_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 4, 1, 2),
    _NtnQosShapingParamsRate_Type()
)
ntnQosShapingParamsRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosShapingParamsRate.setStatus("current")
_NtnQosShapingParamsBurstSize_Type = Unsigned32
_NtnQosShapingParamsBurstSize_Object = MibTableColumn
ntnQosShapingParamsBurstSize = _NtnQosShapingParamsBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 4, 1, 3),
    _NtnQosShapingParamsBurstSize_Type()
)
ntnQosShapingParamsBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosShapingParamsBurstSize.setStatus("current")


class _NtnQosShapingParamsQueueSize_Type(Integer32):
    """Custom type ntnQosShapingParamsQueueSize based on Integer32"""
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
        *(("eightPkts", 4),
          ("fourPkts", 3),
          ("onePkt", 1),
          ("sixteenPkts", 5),
          ("twoPkts", 2))
    )


_NtnQosShapingParamsQueueSize_Type.__name__ = "Integer32"
_NtnQosShapingParamsQueueSize_Object = MibTableColumn
ntnQosShapingParamsQueueSize = _NtnQosShapingParamsQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 4, 1, 4),
    _NtnQosShapingParamsQueueSize_Type()
)
ntnQosShapingParamsQueueSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosShapingParamsQueueSize.setStatus("current")


class _NtnQosShapingParamsStorageType_Type(StorageType):
    """Custom type ntnQosShapingParamsStorageType based on StorageType"""


_NtnQosShapingParamsStorageType_Object = MibTableColumn
ntnQosShapingParamsStorageType = _NtnQosShapingParamsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 4, 1, 5),
    _NtnQosShapingParamsStorageType_Type()
)
ntnQosShapingParamsStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosShapingParamsStorageType.setStatus("current")
_NtnQosShapingParamsStatus_Type = RowStatus
_NtnQosShapingParamsStatus_Object = MibTableColumn
ntnQosShapingParamsStatus = _NtnQosShapingParamsStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 4, 1, 6),
    _NtnQosShapingParamsStatus_Type()
)
ntnQosShapingParamsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosShapingParamsStatus.setStatus("current")


class _NtnQosShapingParamsLabel_Type(SnmpAdminString):
    """Custom type ntnQosShapingParamsLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtnQosShapingParamsLabel_Type.__name__ = "SnmpAdminString"
_NtnQosShapingParamsLabel_Object = MibTableColumn
ntnQosShapingParamsLabel = _NtnQosShapingParamsLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 4, 1, 7),
    _NtnQosShapingParamsLabel_Type()
)
ntnQosShapingParamsLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosShapingParamsLabel.setStatus("current")
_NtnClassifierClasses_ObjectIdentity = ObjectIdentity
ntnClassifierClasses = _NtnClassifierClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5)
)
_NtnDsMultiFieldClfrNextFree_Type = IndexIntegerNextFree
_NtnDsMultiFieldClfrNextFree_Object = MibScalar
ntnDsMultiFieldClfrNextFree = _NtnDsMultiFieldClfrNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 1),
    _NtnDsMultiFieldClfrNextFree_Type()
)
ntnDsMultiFieldClfrNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrNextFree.setStatus("current")
_NtnDsMultiFieldClfrTable_Object = MibTable
ntnDsMultiFieldClfrTable = _NtnDsMultiFieldClfrTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrTable.setStatus("current")
_NtnDsMultiFieldClfrEntry_Object = MibTableRow
ntnDsMultiFieldClfrEntry = _NtnDsMultiFieldClfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1)
)
ntnDsMultiFieldClfrEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrId"),
)
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrEntry.setStatus("current")
_NtnDsMultiFieldClfrId_Type = IndexInteger
_NtnDsMultiFieldClfrId_Object = MibTableColumn
ntnDsMultiFieldClfrId = _NtnDsMultiFieldClfrId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 1),
    _NtnDsMultiFieldClfrId_Type()
)
ntnDsMultiFieldClfrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrId.setStatus("current")


class _NtnDsMultiFieldClfrAddrType_Type(InetAddressType):
    """Custom type ntnDsMultiFieldClfrAddrType based on InetAddressType"""


_NtnDsMultiFieldClfrAddrType_Object = MibTableColumn
ntnDsMultiFieldClfrAddrType = _NtnDsMultiFieldClfrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 2),
    _NtnDsMultiFieldClfrAddrType_Type()
)
ntnDsMultiFieldClfrAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrAddrType.setStatus("current")


class _NtnDsMultiFieldClfrDstAddr_Type(InetAddress):
    """Custom type ntnDsMultiFieldClfrDstAddr based on InetAddress"""
    defaultHexValue = "00000000"


_NtnDsMultiFieldClfrDstAddr_Object = MibTableColumn
ntnDsMultiFieldClfrDstAddr = _NtnDsMultiFieldClfrDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 3),
    _NtnDsMultiFieldClfrDstAddr_Type()
)
ntnDsMultiFieldClfrDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrDstAddr.setStatus("current")


class _NtnDsMultiFieldClfrDstPrefixLength_Type(InetAddressPrefixLength):
    """Custom type ntnDsMultiFieldClfrDstPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_NtnDsMultiFieldClfrDstPrefixLength_Object = MibTableColumn
ntnDsMultiFieldClfrDstPrefixLength = _NtnDsMultiFieldClfrDstPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 4),
    _NtnDsMultiFieldClfrDstPrefixLength_Type()
)
ntnDsMultiFieldClfrDstPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrDstPrefixLength.setStatus("current")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrDstPrefixLength.setUnits("bits")


class _NtnDsMultiFieldClfrSrcAddr_Type(InetAddress):
    """Custom type ntnDsMultiFieldClfrSrcAddr based on InetAddress"""
    defaultHexValue = "00000000"


_NtnDsMultiFieldClfrSrcAddr_Object = MibTableColumn
ntnDsMultiFieldClfrSrcAddr = _NtnDsMultiFieldClfrSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 5),
    _NtnDsMultiFieldClfrSrcAddr_Type()
)
ntnDsMultiFieldClfrSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrSrcAddr.setStatus("current")


class _NtnDsMultiFieldClfrSrcPrefixLength_Type(InetAddressPrefixLength):
    """Custom type ntnDsMultiFieldClfrSrcPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_NtnDsMultiFieldClfrSrcPrefixLength_Object = MibTableColumn
ntnDsMultiFieldClfrSrcPrefixLength = _NtnDsMultiFieldClfrSrcPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 6),
    _NtnDsMultiFieldClfrSrcPrefixLength_Type()
)
ntnDsMultiFieldClfrSrcPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrSrcPrefixLength.setStatus("current")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrSrcPrefixLength.setUnits("bits")


class _NtnDsMultiFieldClfrDscp_Type(DscpOrAny):
    """Custom type ntnDsMultiFieldClfrDscp based on DscpOrAny"""
    defaultValue = -1


_NtnDsMultiFieldClfrDscp_Object = MibTableColumn
ntnDsMultiFieldClfrDscp = _NtnDsMultiFieldClfrDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 7),
    _NtnDsMultiFieldClfrDscp_Type()
)
ntnDsMultiFieldClfrDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrDscp.setStatus("current")


class _NtnDsMultiFieldClfrFlowId_Type(FlowIdOrAny):
    """Custom type ntnDsMultiFieldClfrFlowId based on FlowIdOrAny"""
    defaultValue = -1


_NtnDsMultiFieldClfrFlowId_Object = MibTableColumn
ntnDsMultiFieldClfrFlowId = _NtnDsMultiFieldClfrFlowId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 8),
    _NtnDsMultiFieldClfrFlowId_Type()
)
ntnDsMultiFieldClfrFlowId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrFlowId.setStatus("current")


class _NtnDsMultiFieldClfrProtocol_Type(Unsigned32):
    """Custom type ntnDsMultiFieldClfrProtocol based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NtnDsMultiFieldClfrProtocol_Type.__name__ = "Unsigned32"
_NtnDsMultiFieldClfrProtocol_Object = MibTableColumn
ntnDsMultiFieldClfrProtocol = _NtnDsMultiFieldClfrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 9),
    _NtnDsMultiFieldClfrProtocol_Type()
)
ntnDsMultiFieldClfrProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrProtocol.setStatus("current")


class _NtnDsMultiFieldClfrDstL4PortMin_Type(InetPortNumber):
    """Custom type ntnDsMultiFieldClfrDstL4PortMin based on InetPortNumber"""
    defaultValue = 0


_NtnDsMultiFieldClfrDstL4PortMin_Object = MibTableColumn
ntnDsMultiFieldClfrDstL4PortMin = _NtnDsMultiFieldClfrDstL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 10),
    _NtnDsMultiFieldClfrDstL4PortMin_Type()
)
ntnDsMultiFieldClfrDstL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrDstL4PortMin.setStatus("current")


class _NtnDsMultiFieldClfrDstL4PortMax_Type(InetPortNumber):
    """Custom type ntnDsMultiFieldClfrDstL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_NtnDsMultiFieldClfrDstL4PortMax_Object = MibTableColumn
ntnDsMultiFieldClfrDstL4PortMax = _NtnDsMultiFieldClfrDstL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 11),
    _NtnDsMultiFieldClfrDstL4PortMax_Type()
)
ntnDsMultiFieldClfrDstL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrDstL4PortMax.setStatus("current")


class _NtnDsMultiFieldClfrSrcL4PortMin_Type(InetPortNumber):
    """Custom type ntnDsMultiFieldClfrSrcL4PortMin based on InetPortNumber"""
    defaultValue = 0


_NtnDsMultiFieldClfrSrcL4PortMin_Object = MibTableColumn
ntnDsMultiFieldClfrSrcL4PortMin = _NtnDsMultiFieldClfrSrcL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 12),
    _NtnDsMultiFieldClfrSrcL4PortMin_Type()
)
ntnDsMultiFieldClfrSrcL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrSrcL4PortMin.setStatus("current")


class _NtnDsMultiFieldClfrSrcL4PortMax_Type(InetPortNumber):
    """Custom type ntnDsMultiFieldClfrSrcL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_NtnDsMultiFieldClfrSrcL4PortMax_Object = MibTableColumn
ntnDsMultiFieldClfrSrcL4PortMax = _NtnDsMultiFieldClfrSrcL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 13),
    _NtnDsMultiFieldClfrSrcL4PortMax_Type()
)
ntnDsMultiFieldClfrSrcL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrSrcL4PortMax.setStatus("current")


class _NtnDsMultiFieldClfrStorage_Type(StorageType):
    """Custom type ntnDsMultiFieldClfrStorage based on StorageType"""


_NtnDsMultiFieldClfrStorage_Object = MibTableColumn
ntnDsMultiFieldClfrStorage = _NtnDsMultiFieldClfrStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 14),
    _NtnDsMultiFieldClfrStorage_Type()
)
ntnDsMultiFieldClfrStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrStorage.setStatus("current")
_NtnDsMultiFieldClfrStatus_Type = RowStatus
_NtnDsMultiFieldClfrStatus_Object = MibTableColumn
ntnDsMultiFieldClfrStatus = _NtnDsMultiFieldClfrStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 15),
    _NtnDsMultiFieldClfrStatus_Type()
)
ntnDsMultiFieldClfrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrStatus.setStatus("current")


class _NtnDsMultiFieldClfrLabel_Type(SnmpAdminString):
    """Custom type ntnDsMultiFieldClfrLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtnDsMultiFieldClfrLabel_Type.__name__ = "SnmpAdminString"
_NtnDsMultiFieldClfrLabel_Object = MibTableColumn
ntnDsMultiFieldClfrLabel = _NtnDsMultiFieldClfrLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 16),
    _NtnDsMultiFieldClfrLabel_Type()
)
ntnDsMultiFieldClfrLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrLabel.setStatus("current")


class _NtnDsMultiFieldClfrSessionId_Type(Unsigned32):
    """Custom type ntnDsMultiFieldClfrSessionId based on Unsigned32"""
    defaultValue = 0


_NtnDsMultiFieldClfrSessionId_Object = MibTableColumn
ntnDsMultiFieldClfrSessionId = _NtnDsMultiFieldClfrSessionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 17),
    _NtnDsMultiFieldClfrSessionId_Type()
)
ntnDsMultiFieldClfrSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrSessionId.setStatus("current")


class _NtnDsMultiFieldClfrVersion_Type(VersionIndicator):
    """Custom type ntnDsMultiFieldClfrVersion based on VersionIndicator"""


_NtnDsMultiFieldClfrVersion_Object = MibTableColumn
ntnDsMultiFieldClfrVersion = _NtnDsMultiFieldClfrVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 18),
    _NtnDsMultiFieldClfrVersion_Type()
)
ntnDsMultiFieldClfrVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrVersion.setStatus("current")


class _NtnDsMultiFieldClfrIpFlags_Type(Bits):
    """Custom type ntnDsMultiFieldClfrIpFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("ipv4DfFlagSet", 1),
          ("ipv4MfFlagSet", 0))
    )

_NtnDsMultiFieldClfrIpFlags_Type.__name__ = "Bits"
_NtnDsMultiFieldClfrIpFlags_Object = MibTableColumn
ntnDsMultiFieldClfrIpFlags = _NtnDsMultiFieldClfrIpFlags_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 19),
    _NtnDsMultiFieldClfrIpFlags_Type()
)
ntnDsMultiFieldClfrIpFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrIpFlags.setStatus("current")


class _NtnDsMultiFieldClfrTcpCtrlFlags_Type(Bits):
    """Custom type ntnDsMultiFieldClfrTcpCtrlFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("tcpAckFlagSet", 1),
          ("tcpFinFlagSet", 5),
          ("tcpPshFlagSet", 2),
          ("tcpRstFlagSet", 3),
          ("tcpSynFlagSet", 4),
          ("tcpUrgFlagSet", 0))
    )

_NtnDsMultiFieldClfrTcpCtrlFlags_Type.__name__ = "Bits"
_NtnDsMultiFieldClfrTcpCtrlFlags_Object = MibTableColumn
ntnDsMultiFieldClfrTcpCtrlFlags = _NtnDsMultiFieldClfrTcpCtrlFlags_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 20),
    _NtnDsMultiFieldClfrTcpCtrlFlags_Type()
)
ntnDsMultiFieldClfrTcpCtrlFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrTcpCtrlFlags.setStatus("current")


class _NtnDsMultiFieldClfrIpv4Options_Type(Integer32):
    """Custom type ntnDsMultiFieldClfrIpv4Options based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 3),
          ("ipv4OptionsNotPresent", 2),
          ("ipv4OptionsPresent", 1))
    )


_NtnDsMultiFieldClfrIpv4Options_Type.__name__ = "Integer32"
_NtnDsMultiFieldClfrIpv4Options_Object = MibTableColumn
ntnDsMultiFieldClfrIpv4Options = _NtnDsMultiFieldClfrIpv4Options_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 2, 1, 21),
    _NtnDsMultiFieldClfrIpv4Options_Type()
)
ntnDsMultiFieldClfrIpv4Options.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrIpv4Options.setStatus("current")
_NtnL2MultiFieldClfrNextFree_Type = IndexIntegerNextFree
_NtnL2MultiFieldClfrNextFree_Object = MibScalar
ntnL2MultiFieldClfrNextFree = _NtnL2MultiFieldClfrNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 3),
    _NtnL2MultiFieldClfrNextFree_Type()
)
ntnL2MultiFieldClfrNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrNextFree.setStatus("current")
_NtnL2MultiFieldClfrTable_Object = MibTable
ntnL2MultiFieldClfrTable = _NtnL2MultiFieldClfrTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4)
)
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrTable.setStatus("current")
_NtnL2MultiFieldClfrEntry_Object = MibTableRow
ntnL2MultiFieldClfrEntry = _NtnL2MultiFieldClfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1)
)
ntnL2MultiFieldClfrEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrId"),
)
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrEntry.setStatus("current")
_NtnL2MultiFieldClfrId_Type = IndexInteger
_NtnL2MultiFieldClfrId_Object = MibTableColumn
ntnL2MultiFieldClfrId = _NtnL2MultiFieldClfrId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 1),
    _NtnL2MultiFieldClfrId_Type()
)
ntnL2MultiFieldClfrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrId.setStatus("current")


class _NtnL2MultiFieldClfrDstAddr_Type(MacAddress):
    """Custom type ntnL2MultiFieldClfrDstAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_NtnL2MultiFieldClfrDstAddr_Object = MibTableColumn
ntnL2MultiFieldClfrDstAddr = _NtnL2MultiFieldClfrDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 2),
    _NtnL2MultiFieldClfrDstAddr_Type()
)
ntnL2MultiFieldClfrDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrDstAddr.setStatus("current")


class _NtnL2MultiFieldClfrDstAddrMask_Type(MacAddress):
    """Custom type ntnL2MultiFieldClfrDstAddrMask based on MacAddress"""
    defaultHexValue = "000000000000"


_NtnL2MultiFieldClfrDstAddrMask_Object = MibTableColumn
ntnL2MultiFieldClfrDstAddrMask = _NtnL2MultiFieldClfrDstAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 3),
    _NtnL2MultiFieldClfrDstAddrMask_Type()
)
ntnL2MultiFieldClfrDstAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrDstAddrMask.setStatus("current")


class _NtnL2MultiFieldClfrSrcAddr_Type(MacAddress):
    """Custom type ntnL2MultiFieldClfrSrcAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_NtnL2MultiFieldClfrSrcAddr_Object = MibTableColumn
ntnL2MultiFieldClfrSrcAddr = _NtnL2MultiFieldClfrSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 4),
    _NtnL2MultiFieldClfrSrcAddr_Type()
)
ntnL2MultiFieldClfrSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrSrcAddr.setStatus("current")


class _NtnL2MultiFieldClfrSrcAddrMask_Type(MacAddress):
    """Custom type ntnL2MultiFieldClfrSrcAddrMask based on MacAddress"""
    defaultHexValue = "000000000000"


_NtnL2MultiFieldClfrSrcAddrMask_Object = MibTableColumn
ntnL2MultiFieldClfrSrcAddrMask = _NtnL2MultiFieldClfrSrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 5),
    _NtnL2MultiFieldClfrSrcAddrMask_Type()
)
ntnL2MultiFieldClfrSrcAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrSrcAddrMask.setStatus("current")


class _NtnL2MultiFieldClfrVlanIdMin_Type(Integer32):
    """Custom type ntnL2MultiFieldClfrVlanIdMin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_NtnL2MultiFieldClfrVlanIdMin_Type.__name__ = "Integer32"
_NtnL2MultiFieldClfrVlanIdMin_Object = MibTableColumn
ntnL2MultiFieldClfrVlanIdMin = _NtnL2MultiFieldClfrVlanIdMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 6),
    _NtnL2MultiFieldClfrVlanIdMin_Type()
)
ntnL2MultiFieldClfrVlanIdMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrVlanIdMin.setStatus("current")


class _NtnL2MultiFieldClfrVlanIdMax_Type(Integer32):
    """Custom type ntnL2MultiFieldClfrVlanIdMax based on Integer32"""
    defaultValue = 4094

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_NtnL2MultiFieldClfrVlanIdMax_Type.__name__ = "Integer32"
_NtnL2MultiFieldClfrVlanIdMax_Object = MibTableColumn
ntnL2MultiFieldClfrVlanIdMax = _NtnL2MultiFieldClfrVlanIdMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 7),
    _NtnL2MultiFieldClfrVlanIdMax_Type()
)
ntnL2MultiFieldClfrVlanIdMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrVlanIdMax.setStatus("current")


class _NtnL2MultiFieldClfrVlanTag_Type(Integer32):
    """Custom type ntnL2MultiFieldClfrVlanTag based on Integer32"""
    defaultValue = 3

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
        *(("doubleTagged", 4),
          ("ignore", 3),
          ("tagged", 2),
          ("untagged", 1))
    )


_NtnL2MultiFieldClfrVlanTag_Type.__name__ = "Integer32"
_NtnL2MultiFieldClfrVlanTag_Object = MibTableColumn
ntnL2MultiFieldClfrVlanTag = _NtnL2MultiFieldClfrVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 8),
    _NtnL2MultiFieldClfrVlanTag_Type()
)
ntnL2MultiFieldClfrVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrVlanTag.setStatus("current")


class _NtnL2MultiFieldClfrEtherType_Type(Integer32):
    """Custom type ntnL2MultiFieldClfrEtherType based on Integer32"""
    defaultHexValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NtnL2MultiFieldClfrEtherType_Type.__name__ = "Integer32"
_NtnL2MultiFieldClfrEtherType_Object = MibTableColumn
ntnL2MultiFieldClfrEtherType = _NtnL2MultiFieldClfrEtherType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 9),
    _NtnL2MultiFieldClfrEtherType_Type()
)
ntnL2MultiFieldClfrEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrEtherType.setStatus("current")


class _NtnL2MultiFieldClfrUserPriority_Type(Integer32):
    """Custom type ntnL2MultiFieldClfrUserPriority based on Integer32"""
    defaultValue = 9

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
        *(("matchAllPriorities", 9),
          ("matchPriority0", 1),
          ("matchPriority1", 2),
          ("matchPriority2", 3),
          ("matchPriority3", 4),
          ("matchPriority4", 5),
          ("matchPriority5", 6),
          ("matchPriority6", 7),
          ("matchPriority7", 8))
    )


_NtnL2MultiFieldClfrUserPriority_Type.__name__ = "Integer32"
_NtnL2MultiFieldClfrUserPriority_Object = MibTableColumn
ntnL2MultiFieldClfrUserPriority = _NtnL2MultiFieldClfrUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 10),
    _NtnL2MultiFieldClfrUserPriority_Type()
)
ntnL2MultiFieldClfrUserPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrUserPriority.setStatus("current")


class _NtnL2MultiFieldClfrStorage_Type(StorageType):
    """Custom type ntnL2MultiFieldClfrStorage based on StorageType"""


_NtnL2MultiFieldClfrStorage_Object = MibTableColumn
ntnL2MultiFieldClfrStorage = _NtnL2MultiFieldClfrStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 11),
    _NtnL2MultiFieldClfrStorage_Type()
)
ntnL2MultiFieldClfrStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrStorage.setStatus("current")
_NtnL2MultiFieldClfrStatus_Type = RowStatus
_NtnL2MultiFieldClfrStatus_Object = MibTableColumn
ntnL2MultiFieldClfrStatus = _NtnL2MultiFieldClfrStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 12),
    _NtnL2MultiFieldClfrStatus_Type()
)
ntnL2MultiFieldClfrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrStatus.setStatus("current")


class _NtnL2MultiFieldClfrLabel_Type(SnmpAdminString):
    """Custom type ntnL2MultiFieldClfrLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtnL2MultiFieldClfrLabel_Type.__name__ = "SnmpAdminString"
_NtnL2MultiFieldClfrLabel_Object = MibTableColumn
ntnL2MultiFieldClfrLabel = _NtnL2MultiFieldClfrLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 13),
    _NtnL2MultiFieldClfrLabel_Type()
)
ntnL2MultiFieldClfrLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrLabel.setStatus("current")


class _NtnL2MultiFieldClfrSessionId_Type(Unsigned32):
    """Custom type ntnL2MultiFieldClfrSessionId based on Unsigned32"""
    defaultValue = 0


_NtnL2MultiFieldClfrSessionId_Object = MibTableColumn
ntnL2MultiFieldClfrSessionId = _NtnL2MultiFieldClfrSessionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 14),
    _NtnL2MultiFieldClfrSessionId_Type()
)
ntnL2MultiFieldClfrSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrSessionId.setStatus("current")


class _NtnL2MultiFieldClfrVersion_Type(VersionIndicator):
    """Custom type ntnL2MultiFieldClfrVersion based on VersionIndicator"""


_NtnL2MultiFieldClfrVersion_Object = MibTableColumn
ntnL2MultiFieldClfrVersion = _NtnL2MultiFieldClfrVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 15),
    _NtnL2MultiFieldClfrVersion_Type()
)
ntnL2MultiFieldClfrVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrVersion.setStatus("current")


class _NtnL2MultiFieldClfrPktType_Type(Integer32):
    """Custom type ntnL2MultiFieldClfrPktType based on Integer32"""
    defaultValue = 4

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
        *(("ethernetII", 1),
          ("ignore", 4),
          ("llc", 3),
          ("snap", 2))
    )


_NtnL2MultiFieldClfrPktType_Type.__name__ = "Integer32"
_NtnL2MultiFieldClfrPktType_Object = MibTableColumn
ntnL2MultiFieldClfrPktType = _NtnL2MultiFieldClfrPktType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 16),
    _NtnL2MultiFieldClfrPktType_Type()
)
ntnL2MultiFieldClfrPktType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrPktType.setStatus("current")


class _NtnL2MultiFieldClfrIvidMin_Type(Integer32):
    """Custom type ntnL2MultiFieldClfrIvidMin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_NtnL2MultiFieldClfrIvidMin_Type.__name__ = "Integer32"
_NtnL2MultiFieldClfrIvidMin_Object = MibTableColumn
ntnL2MultiFieldClfrIvidMin = _NtnL2MultiFieldClfrIvidMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 17),
    _NtnL2MultiFieldClfrIvidMin_Type()
)
ntnL2MultiFieldClfrIvidMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrIvidMin.setStatus("current")


class _NtnL2MultiFieldClfrIvidMax_Type(Integer32):
    """Custom type ntnL2MultiFieldClfrIvidMax based on Integer32"""
    defaultValue = 4094

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_NtnL2MultiFieldClfrIvidMax_Type.__name__ = "Integer32"
_NtnL2MultiFieldClfrIvidMax_Object = MibTableColumn
ntnL2MultiFieldClfrIvidMax = _NtnL2MultiFieldClfrIvidMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 18),
    _NtnL2MultiFieldClfrIvidMax_Type()
)
ntnL2MultiFieldClfrIvidMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrIvidMax.setStatus("current")


class _NtnL2MultiFieldClfrTPID_Type(Integer32):
    """Custom type ntnL2MultiFieldClfrTPID based on Integer32"""
    defaultHexValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NtnL2MultiFieldClfrTPID_Type.__name__ = "Integer32"
_NtnL2MultiFieldClfrTPID_Object = MibTableColumn
ntnL2MultiFieldClfrTPID = _NtnL2MultiFieldClfrTPID_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 19),
    _NtnL2MultiFieldClfrTPID_Type()
)
ntnL2MultiFieldClfrTPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrTPID.setStatus("current")


class _NtnL2MultiFieldClfrCFI_Type(Integer32):
    """Custom type ntnL2MultiFieldClfrCFI based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cfiOne", 2),
          ("cfiZero", 1),
          ("ignore", 3))
    )


_NtnL2MultiFieldClfrCFI_Type.__name__ = "Integer32"
_NtnL2MultiFieldClfrCFI_Object = MibTableColumn
ntnL2MultiFieldClfrCFI = _NtnL2MultiFieldClfrCFI_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 20),
    _NtnL2MultiFieldClfrCFI_Type()
)
ntnL2MultiFieldClfrCFI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrCFI.setStatus("current")


class _NtnL2MultiFieldClfrITPID_Type(Integer32):
    """Custom type ntnL2MultiFieldClfrITPID based on Integer32"""
    defaultHexValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NtnL2MultiFieldClfrITPID_Type.__name__ = "Integer32"
_NtnL2MultiFieldClfrITPID_Object = MibTableColumn
ntnL2MultiFieldClfrITPID = _NtnL2MultiFieldClfrITPID_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 21),
    _NtnL2MultiFieldClfrITPID_Type()
)
ntnL2MultiFieldClfrITPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrITPID.setStatus("current")


class _NtnL2MultiFieldClfrICFI_Type(Integer32):
    """Custom type ntnL2MultiFieldClfrICFI based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cfiOne", 2),
          ("cfiZero", 1),
          ("ignore", 3))
    )


_NtnL2MultiFieldClfrICFI_Type.__name__ = "Integer32"
_NtnL2MultiFieldClfrICFI_Object = MibTableColumn
ntnL2MultiFieldClfrICFI = _NtnL2MultiFieldClfrICFI_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 22),
    _NtnL2MultiFieldClfrICFI_Type()
)
ntnL2MultiFieldClfrICFI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrICFI.setStatus("current")


class _NtnL2MultiFieldClfrIUserPriority_Type(Integer32):
    """Custom type ntnL2MultiFieldClfrIUserPriority based on Integer32"""
    defaultValue = 9

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
        *(("matchAllPriorities", 9),
          ("matchPriority0", 1),
          ("matchPriority1", 2),
          ("matchPriority2", 3),
          ("matchPriority3", 4),
          ("matchPriority4", 5),
          ("matchPriority5", 6),
          ("matchPriority6", 7),
          ("matchPriority7", 8))
    )


_NtnL2MultiFieldClfrIUserPriority_Type.__name__ = "Integer32"
_NtnL2MultiFieldClfrIUserPriority_Object = MibTableColumn
ntnL2MultiFieldClfrIUserPriority = _NtnL2MultiFieldClfrIUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 4, 1, 23),
    _NtnL2MultiFieldClfrIUserPriority_Type()
)
ntnL2MultiFieldClfrIUserPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrIUserPriority.setStatus("current")
_NtnSystemClfrNextFree_Type = IndexIntegerNextFree
_NtnSystemClfrNextFree_Object = MibScalar
ntnSystemClfrNextFree = _NtnSystemClfrNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 5),
    _NtnSystemClfrNextFree_Type()
)
ntnSystemClfrNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnSystemClfrNextFree.setStatus("current")
_NtnSystemClfrTable_Object = MibTable
ntnSystemClfrTable = _NtnSystemClfrTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6)
)
if mibBuilder.loadTexts:
    ntnSystemClfrTable.setStatus("current")
_NtnSystemClfrEntry_Object = MibTableRow
ntnSystemClfrEntry = _NtnSystemClfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1)
)
ntnSystemClfrEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrId"),
)
if mibBuilder.loadTexts:
    ntnSystemClfrEntry.setStatus("current")
_NtnSystemClfrId_Type = IndexInteger
_NtnSystemClfrId_Object = MibTableColumn
ntnSystemClfrId = _NtnSystemClfrId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 1),
    _NtnSystemClfrId_Type()
)
ntnSystemClfrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnSystemClfrId.setStatus("current")


class _NtnSystemClfrUnknownUcastFrames_Type(TruthValue):
    """Custom type ntnSystemClfrUnknownUcastFrames based on TruthValue"""


_NtnSystemClfrUnknownUcastFrames_Object = MibTableColumn
ntnSystemClfrUnknownUcastFrames = _NtnSystemClfrUnknownUcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 2),
    _NtnSystemClfrUnknownUcastFrames_Type()
)
ntnSystemClfrUnknownUcastFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrUnknownUcastFrames.setStatus("current")


class _NtnSystemClfrUnknownMcastFrames_Type(TruthValue):
    """Custom type ntnSystemClfrUnknownMcastFrames based on TruthValue"""


_NtnSystemClfrUnknownMcastFrames_Object = MibTableColumn
ntnSystemClfrUnknownMcastFrames = _NtnSystemClfrUnknownMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 3),
    _NtnSystemClfrUnknownMcastFrames_Type()
)
ntnSystemClfrUnknownMcastFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrUnknownMcastFrames.setStatus("current")


class _NtnSystemClfrKnownUcastFrames_Type(TruthValue):
    """Custom type ntnSystemClfrKnownUcastFrames based on TruthValue"""


_NtnSystemClfrKnownUcastFrames_Object = MibTableColumn
ntnSystemClfrKnownUcastFrames = _NtnSystemClfrKnownUcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 4),
    _NtnSystemClfrKnownUcastFrames_Type()
)
ntnSystemClfrKnownUcastFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrKnownUcastFrames.setStatus("current")


class _NtnSystemClfrKnownMcastFrames_Type(TruthValue):
    """Custom type ntnSystemClfrKnownMcastFrames based on TruthValue"""


_NtnSystemClfrKnownMcastFrames_Object = MibTableColumn
ntnSystemClfrKnownMcastFrames = _NtnSystemClfrKnownMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 5),
    _NtnSystemClfrKnownMcastFrames_Type()
)
ntnSystemClfrKnownMcastFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrKnownMcastFrames.setStatus("current")


class _NtnSystemClfrBcastFrames_Type(TruthValue):
    """Custom type ntnSystemClfrBcastFrames based on TruthValue"""


_NtnSystemClfrBcastFrames_Object = MibTableColumn
ntnSystemClfrBcastFrames = _NtnSystemClfrBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 6),
    _NtnSystemClfrBcastFrames_Type()
)
ntnSystemClfrBcastFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrBcastFrames.setStatus("current")


class _NtnSystemClfrPatternPosition_Type(OctetString):
    """Custom type ntnSystemClfrPatternPosition based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NtnSystemClfrPatternPosition_Type.__name__ = "OctetString"
_NtnSystemClfrPatternPosition_Object = MibTableColumn
ntnSystemClfrPatternPosition = _NtnSystemClfrPatternPosition_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 7),
    _NtnSystemClfrPatternPosition_Type()
)
ntnSystemClfrPatternPosition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrPatternPosition.setStatus("current")


class _NtnSystemClfrPatternData_Type(OctetString):
    """Custom type ntnSystemClfrPatternData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NtnSystemClfrPatternData_Type.__name__ = "OctetString"
_NtnSystemClfrPatternData_Object = MibTableColumn
ntnSystemClfrPatternData = _NtnSystemClfrPatternData_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 8),
    _NtnSystemClfrPatternData_Type()
)
ntnSystemClfrPatternData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrPatternData.setStatus("current")


class _NtnSystemClfrStorage_Type(StorageType):
    """Custom type ntnSystemClfrStorage based on StorageType"""


_NtnSystemClfrStorage_Object = MibTableColumn
ntnSystemClfrStorage = _NtnSystemClfrStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 9),
    _NtnSystemClfrStorage_Type()
)
ntnSystemClfrStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrStorage.setStatus("current")
_NtnSystemClfrStatus_Type = RowStatus
_NtnSystemClfrStatus_Object = MibTableColumn
ntnSystemClfrStatus = _NtnSystemClfrStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 10),
    _NtnSystemClfrStatus_Type()
)
ntnSystemClfrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrStatus.setStatus("current")


class _NtnSystemClfrPatternFormat_Type(Integer32):
    """Custom type ntnSystemClfrPatternFormat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("doubleTagged", 3),
          ("tagged", 2),
          ("untagged", 1))
    )


_NtnSystemClfrPatternFormat_Type.__name__ = "Integer32"
_NtnSystemClfrPatternFormat_Object = MibTableColumn
ntnSystemClfrPatternFormat = _NtnSystemClfrPatternFormat_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 11),
    _NtnSystemClfrPatternFormat_Type()
)
ntnSystemClfrPatternFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrPatternFormat.setStatus("current")


class _NtnSystemClfrLabel_Type(SnmpAdminString):
    """Custom type ntnSystemClfrLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtnSystemClfrLabel_Type.__name__ = "SnmpAdminString"
_NtnSystemClfrLabel_Object = MibTableColumn
ntnSystemClfrLabel = _NtnSystemClfrLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 12),
    _NtnSystemClfrLabel_Type()
)
ntnSystemClfrLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrLabel.setStatus("current")


class _NtnSystemClfrSessionId_Type(Unsigned32):
    """Custom type ntnSystemClfrSessionId based on Unsigned32"""
    defaultValue = 0


_NtnSystemClfrSessionId_Object = MibTableColumn
ntnSystemClfrSessionId = _NtnSystemClfrSessionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 13),
    _NtnSystemClfrSessionId_Type()
)
ntnSystemClfrSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrSessionId.setStatus("current")


class _NtnSystemClfrVersion_Type(VersionIndicator):
    """Custom type ntnSystemClfrVersion based on VersionIndicator"""


_NtnSystemClfrVersion_Object = MibTableColumn
ntnSystemClfrVersion = _NtnSystemClfrVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 14),
    _NtnSystemClfrVersion_Type()
)
ntnSystemClfrVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrVersion.setStatus("current")


class _NtnSystemClfrUnknownIpMcast_Type(TruthValue):
    """Custom type ntnSystemClfrUnknownIpMcast based on TruthValue"""


_NtnSystemClfrUnknownIpMcast_Object = MibTableColumn
ntnSystemClfrUnknownIpMcast = _NtnSystemClfrUnknownIpMcast_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 15),
    _NtnSystemClfrUnknownIpMcast_Type()
)
ntnSystemClfrUnknownIpMcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrUnknownIpMcast.setStatus("current")


class _NtnSystemClfrKnownIpMcast_Type(TruthValue):
    """Custom type ntnSystemClfrKnownIpMcast based on TruthValue"""


_NtnSystemClfrKnownIpMcast_Object = MibTableColumn
ntnSystemClfrKnownIpMcast = _NtnSystemClfrKnownIpMcast_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 16),
    _NtnSystemClfrKnownIpMcast_Type()
)
ntnSystemClfrKnownIpMcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrKnownIpMcast.setStatus("current")


class _NtnSystemClfrNonIpPkt_Type(TruthValue):
    """Custom type ntnSystemClfrNonIpPkt based on TruthValue"""


_NtnSystemClfrNonIpPkt_Object = MibTableColumn
ntnSystemClfrNonIpPkt = _NtnSystemClfrNonIpPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 17),
    _NtnSystemClfrNonIpPkt_Type()
)
ntnSystemClfrNonIpPkt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrNonIpPkt.setStatus("current")


class _NtnSystemClfrPatternIpVersion_Type(Integer32):
    """Custom type ntnSystemClfrPatternIpVersion based on Integer32"""
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
        *(("ipv4", 3),
          ("ipv6", 4),
          ("nonIp", 2),
          ("notApplicable", 1))
    )


_NtnSystemClfrPatternIpVersion_Type.__name__ = "Integer32"
_NtnSystemClfrPatternIpVersion_Object = MibTableColumn
ntnSystemClfrPatternIpVersion = _NtnSystemClfrPatternIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 18),
    _NtnSystemClfrPatternIpVersion_Type()
)
ntnSystemClfrPatternIpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrPatternIpVersion.setStatus("current")


class _NtnSystemClfrUnknownNonIpMcast_Type(TruthValue):
    """Custom type ntnSystemClfrUnknownNonIpMcast based on TruthValue"""


_NtnSystemClfrUnknownNonIpMcast_Object = MibTableColumn
ntnSystemClfrUnknownNonIpMcast = _NtnSystemClfrUnknownNonIpMcast_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 19),
    _NtnSystemClfrUnknownNonIpMcast_Type()
)
ntnSystemClfrUnknownNonIpMcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrUnknownNonIpMcast.setStatus("current")


class _NtnSystemClfrKnownNonIpMcast_Type(TruthValue):
    """Custom type ntnSystemClfrKnownNonIpMcast based on TruthValue"""


_NtnSystemClfrKnownNonIpMcast_Object = MibTableColumn
ntnSystemClfrKnownNonIpMcast = _NtnSystemClfrKnownNonIpMcast_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 20),
    _NtnSystemClfrKnownNonIpMcast_Type()
)
ntnSystemClfrKnownNonIpMcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrKnownNonIpMcast.setStatus("current")


class _NtnSystemClfrPatternL2Format_Type(Integer32):
    """Custom type ntnSystemClfrPatternL2Format based on Integer32"""
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
        *(("ethernetII", 2),
          ("llc", 4),
          ("notApplicable", 1),
          ("snap", 3))
    )


_NtnSystemClfrPatternL2Format_Type.__name__ = "Integer32"
_NtnSystemClfrPatternL2Format_Object = MibTableColumn
ntnSystemClfrPatternL2Format = _NtnSystemClfrPatternL2Format_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 6, 1, 21),
    _NtnSystemClfrPatternL2Format_Type()
)
ntnSystemClfrPatternL2Format.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnSystemClfrPatternL2Format.setStatus("current")
_NtnClfrComponentNextFree_Type = IndexIntegerNextFree
_NtnClfrComponentNextFree_Object = MibScalar
ntnClfrComponentNextFree = _NtnClfrComponentNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 7),
    _NtnClfrComponentNextFree_Type()
)
ntnClfrComponentNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnClfrComponentNextFree.setStatus("current")
_NtnClfrComponentTable_Object = MibTable
ntnClfrComponentTable = _NtnClfrComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 8)
)
if mibBuilder.loadTexts:
    ntnClfrComponentTable.setStatus("current")
_NtnClfrComponentEntry_Object = MibTableRow
ntnClfrComponentEntry = _NtnClfrComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 8, 1)
)
ntnClfrComponentEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnClfrComponentId"),
)
if mibBuilder.loadTexts:
    ntnClfrComponentEntry.setStatus("current")
_NtnClfrComponentId_Type = IndexInteger
_NtnClfrComponentId_Object = MibTableColumn
ntnClfrComponentId = _NtnClfrComponentId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 8, 1, 1),
    _NtnClfrComponentId_Type()
)
ntnClfrComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnClfrComponentId.setStatus("current")
_NtnClfrComponentSpecific_Type = RowPointer
_NtnClfrComponentSpecific_Object = MibTableColumn
ntnClfrComponentSpecific = _NtnClfrComponentSpecific_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 8, 1, 2),
    _NtnClfrComponentSpecific_Type()
)
ntnClfrComponentSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnClfrComponentSpecific.setStatus("current")


class _NtnClfrComponentSetId_Type(Unsigned32):
    """Custom type ntnClfrComponentSetId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtnClfrComponentSetId_Type.__name__ = "Unsigned32"
_NtnClfrComponentSetId_Object = MibTableColumn
ntnClfrComponentSetId = _NtnClfrComponentSetId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 8, 1, 3),
    _NtnClfrComponentSetId_Type()
)
ntnClfrComponentSetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnClfrComponentSetId.setStatus("current")


class _NtnClfrComponentLabel_Type(SnmpAdminString):
    """Custom type ntnClfrComponentLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtnClfrComponentLabel_Type.__name__ = "SnmpAdminString"
_NtnClfrComponentLabel_Object = MibTableColumn
ntnClfrComponentLabel = _NtnClfrComponentLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 8, 1, 4),
    _NtnClfrComponentLabel_Type()
)
ntnClfrComponentLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnClfrComponentLabel.setStatus("current")


class _NtnClfrComponentStorage_Type(StorageType):
    """Custom type ntnClfrComponentStorage based on StorageType"""


_NtnClfrComponentStorage_Object = MibTableColumn
ntnClfrComponentStorage = _NtnClfrComponentStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 8, 1, 5),
    _NtnClfrComponentStorage_Type()
)
ntnClfrComponentStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnClfrComponentStorage.setStatus("current")
_NtnClfrComponentStatus_Type = RowStatus
_NtnClfrComponentStatus_Object = MibTableColumn
ntnClfrComponentStatus = _NtnClfrComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 8, 1, 6),
    _NtnClfrComponentStatus_Type()
)
ntnClfrComponentStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnClfrComponentStatus.setStatus("current")


class _NtnClfrComponentSessionId_Type(Unsigned32):
    """Custom type ntnClfrComponentSessionId based on Unsigned32"""
    defaultValue = 0


_NtnClfrComponentSessionId_Object = MibTableColumn
ntnClfrComponentSessionId = _NtnClfrComponentSessionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 8, 1, 7),
    _NtnClfrComponentSessionId_Type()
)
ntnClfrComponentSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnClfrComponentSessionId.setStatus("current")


class _NtnClfrComponentVersion_Type(VersionIndicator):
    """Custom type ntnClfrComponentVersion based on VersionIndicator"""


_NtnClfrComponentVersion_Object = MibTableColumn
ntnClfrComponentVersion = _NtnClfrComponentVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 8, 1, 8),
    _NtnClfrComponentVersion_Type()
)
ntnClfrComponentVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnClfrComponentVersion.setStatus("current")
_NtnClfrBlockNextFree_Type = IndexIntegerNextFree
_NtnClfrBlockNextFree_Object = MibScalar
ntnClfrBlockNextFree = _NtnClfrBlockNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 9),
    _NtnClfrBlockNextFree_Type()
)
ntnClfrBlockNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnClfrBlockNextFree.setStatus("current")
_NtnClfrBlockTable_Object = MibTable
ntnClfrBlockTable = _NtnClfrBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 10)
)
if mibBuilder.loadTexts:
    ntnClfrBlockTable.setStatus("current")
_NtnClfrBlockEntry_Object = MibTableRow
ntnClfrBlockEntry = _NtnClfrBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 10, 1)
)
ntnClfrBlockEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnClfrBlockId"),
)
if mibBuilder.loadTexts:
    ntnClfrBlockEntry.setStatus("current")
_NtnClfrBlockId_Type = IndexInteger
_NtnClfrBlockId_Object = MibTableColumn
ntnClfrBlockId = _NtnClfrBlockId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 10, 1, 1),
    _NtnClfrBlockId_Type()
)
ntnClfrBlockId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnClfrBlockId.setStatus("current")


class _NtnClfrBlockNumber_Type(Unsigned32):
    """Custom type ntnClfrBlockNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtnClfrBlockNumber_Type.__name__ = "Unsigned32"
_NtnClfrBlockNumber_Object = MibTableColumn
ntnClfrBlockNumber = _NtnClfrBlockNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 10, 1, 2),
    _NtnClfrBlockNumber_Type()
)
ntnClfrBlockNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnClfrBlockNumber.setStatus("current")


class _NtnClfrBlockClfrCompSetId_Type(Unsigned32):
    """Custom type ntnClfrBlockClfrCompSetId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtnClfrBlockClfrCompSetId_Type.__name__ = "Unsigned32"
_NtnClfrBlockClfrCompSetId_Object = MibTableColumn
ntnClfrBlockClfrCompSetId = _NtnClfrBlockClfrCompSetId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 10, 1, 3),
    _NtnClfrBlockClfrCompSetId_Type()
)
ntnClfrBlockClfrCompSetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnClfrBlockClfrCompSetId.setStatus("current")


class _NtnClfrBlockMeter_Type(IndexIntegerOrZero):
    """Custom type ntnClfrBlockMeter based on IndexIntegerOrZero"""
    defaultValue = 0


_NtnClfrBlockMeter_Object = MibTableColumn
ntnClfrBlockMeter = _NtnClfrBlockMeter_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 10, 1, 4),
    _NtnClfrBlockMeter_Type()
)
ntnClfrBlockMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnClfrBlockMeter.setStatus("current")


class _NtnClfrBlockAction_Type(IndexIntegerOrZero):
    """Custom type ntnClfrBlockAction based on IndexIntegerOrZero"""
    defaultValue = 0


_NtnClfrBlockAction_Object = MibTableColumn
ntnClfrBlockAction = _NtnClfrBlockAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 10, 1, 5),
    _NtnClfrBlockAction_Type()
)
ntnClfrBlockAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnClfrBlockAction.setStatus("current")


class _NtnClfrBlockLabel_Type(SnmpAdminString):
    """Custom type ntnClfrBlockLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtnClfrBlockLabel_Type.__name__ = "SnmpAdminString"
_NtnClfrBlockLabel_Object = MibTableColumn
ntnClfrBlockLabel = _NtnClfrBlockLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 10, 1, 6),
    _NtnClfrBlockLabel_Type()
)
ntnClfrBlockLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnClfrBlockLabel.setStatus("current")


class _NtnClfrBlockStorage_Type(StorageType):
    """Custom type ntnClfrBlockStorage based on StorageType"""


_NtnClfrBlockStorage_Object = MibTableColumn
ntnClfrBlockStorage = _NtnClfrBlockStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 10, 1, 7),
    _NtnClfrBlockStorage_Type()
)
ntnClfrBlockStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnClfrBlockStorage.setStatus("current")
_NtnClfrBlockStatus_Type = RowStatus
_NtnClfrBlockStatus_Object = MibTableColumn
ntnClfrBlockStatus = _NtnClfrBlockStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 10, 1, 8),
    _NtnClfrBlockStatus_Type()
)
ntnClfrBlockStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnClfrBlockStatus.setStatus("current")


class _NtnClfrBlockSessionId_Type(Unsigned32):
    """Custom type ntnClfrBlockSessionId based on Unsigned32"""
    defaultValue = 0


_NtnClfrBlockSessionId_Object = MibTableColumn
ntnClfrBlockSessionId = _NtnClfrBlockSessionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 10, 1, 9),
    _NtnClfrBlockSessionId_Type()
)
ntnClfrBlockSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnClfrBlockSessionId.setStatus("current")


class _NtnClfrBlockVersion_Type(VersionIndicator):
    """Custom type ntnClfrBlockVersion based on VersionIndicator"""


_NtnClfrBlockVersion_Object = MibTableColumn
ntnClfrBlockVersion = _NtnClfrBlockVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 10, 1, 10),
    _NtnClfrBlockVersion_Type()
)
ntnClfrBlockVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnClfrBlockVersion.setStatus("current")


class _NtnClfrBlockPrecedence_Type(Unsigned32):
    """Custom type ntnClfrBlockPrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NtnClfrBlockPrecedence_Type.__name__ = "Unsigned32"
_NtnClfrBlockPrecedence_Object = MibTableColumn
ntnClfrBlockPrecedence = _NtnClfrBlockPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 10, 1, 11),
    _NtnClfrBlockPrecedence_Type()
)
ntnClfrBlockPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnClfrBlockPrecedence.setStatus("current")
_NtnClfrComponentSetNextFree_Type = IndexIntegerNextFree
_NtnClfrComponentSetNextFree_Object = MibScalar
ntnClfrComponentSetNextFree = _NtnClfrComponentSetNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 11),
    _NtnClfrComponentSetNextFree_Type()
)
ntnClfrComponentSetNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnClfrComponentSetNextFree.setStatus("current")
_NtnClfrBlockNumberNextFree_Type = IndexIntegerNextFree
_NtnClfrBlockNumberNextFree_Object = MibScalar
ntnClfrBlockNumberNextFree = _NtnClfrBlockNumberNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 5, 12),
    _NtnClfrBlockNumberNextFree_Type()
)
ntnClfrBlockNumberNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnClfrBlockNumberNextFree.setStatus("current")
_NtnQosMeterClasses_ObjectIdentity = ObjectIdentity
ntnQosMeterClasses = _NtnQosMeterClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6)
)
_NtnQosMeterNextFree_Type = IndexIntegerNextFree
_NtnQosMeterNextFree_Object = MibScalar
ntnQosMeterNextFree = _NtnQosMeterNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 1),
    _NtnQosMeterNextFree_Type()
)
ntnQosMeterNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosMeterNextFree.setStatus("current")
_NtnQosMeterTable_Object = MibTable
ntnQosMeterTable = _NtnQosMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 2)
)
if mibBuilder.loadTexts:
    ntnQosMeterTable.setStatus("current")
_NtnQosMeterEntry_Object = MibTableRow
ntnQosMeterEntry = _NtnQosMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 2, 1)
)
ntnQosMeterEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosMeterId"),
)
if mibBuilder.loadTexts:
    ntnQosMeterEntry.setStatus("current")
_NtnQosMeterId_Type = IndexInteger
_NtnQosMeterId_Object = MibTableColumn
ntnQosMeterId = _NtnQosMeterId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 2, 1, 1),
    _NtnQosMeterId_Type()
)
ntnQosMeterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosMeterId.setStatus("current")
_NtnQosMeterSucceedNext_Type = RowPointer
_NtnQosMeterSucceedNext_Object = MibTableColumn
ntnQosMeterSucceedNext = _NtnQosMeterSucceedNext_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 2, 1, 2),
    _NtnQosMeterSucceedNext_Type()
)
ntnQosMeterSucceedNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosMeterSucceedNext.setStatus("current")
_NtnQosMeterFailNext_Type = RowPointer
_NtnQosMeterFailNext_Object = MibTableColumn
ntnQosMeterFailNext = _NtnQosMeterFailNext_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 2, 1, 3),
    _NtnQosMeterFailNext_Type()
)
ntnQosMeterFailNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosMeterFailNext.setStatus("current")
_NtnQosMeterSpecific_Type = RowPointer
_NtnQosMeterSpecific_Object = MibTableColumn
ntnQosMeterSpecific = _NtnQosMeterSpecific_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 2, 1, 4),
    _NtnQosMeterSpecific_Type()
)
ntnQosMeterSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosMeterSpecific.setStatus("current")
_NtnQosMeterOutOfProfileStats_Type = IndexIntegerOrZero
_NtnQosMeterOutOfProfileStats_Object = MibTableColumn
ntnQosMeterOutOfProfileStats = _NtnQosMeterOutOfProfileStats_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 2, 1, 5),
    _NtnQosMeterOutOfProfileStats_Type()
)
ntnQosMeterOutOfProfileStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosMeterOutOfProfileStats.setStatus("current")


class _NtnQosMeterLabel_Type(SnmpAdminString):
    """Custom type ntnQosMeterLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtnQosMeterLabel_Type.__name__ = "SnmpAdminString"
_NtnQosMeterLabel_Object = MibTableColumn
ntnQosMeterLabel = _NtnQosMeterLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 2, 1, 6),
    _NtnQosMeterLabel_Type()
)
ntnQosMeterLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosMeterLabel.setStatus("current")


class _NtnQosMeterStorage_Type(StorageType):
    """Custom type ntnQosMeterStorage based on StorageType"""


_NtnQosMeterStorage_Object = MibTableColumn
ntnQosMeterStorage = _NtnQosMeterStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 2, 1, 7),
    _NtnQosMeterStorage_Type()
)
ntnQosMeterStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosMeterStorage.setStatus("current")
_NtnQosMeterStatus_Type = RowStatus
_NtnQosMeterStatus_Object = MibTableColumn
ntnQosMeterStatus = _NtnQosMeterStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 2, 1, 8),
    _NtnQosMeterStatus_Type()
)
ntnQosMeterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosMeterStatus.setStatus("current")
_NtnQosMeterSessionId_Type = Unsigned32
_NtnQosMeterSessionId_Object = MibTableColumn
ntnQosMeterSessionId = _NtnQosMeterSessionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 2, 1, 9),
    _NtnQosMeterSessionId_Type()
)
ntnQosMeterSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosMeterSessionId.setStatus("current")


class _NtnQosMeterVersion_Type(VersionIndicator):
    """Custom type ntnQosMeterVersion based on VersionIndicator"""


_NtnQosMeterVersion_Object = MibTableColumn
ntnQosMeterVersion = _NtnQosMeterVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 2, 1, 10),
    _NtnQosMeterVersion_Type()
)
ntnQosMeterVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosMeterVersion.setStatus("current")
_NtnQosTBParamNextFree_Type = IndexIntegerNextFree
_NtnQosTBParamNextFree_Object = MibScalar
ntnQosTBParamNextFree = _NtnQosTBParamNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 3),
    _NtnQosTBParamNextFree_Type()
)
ntnQosTBParamNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosTBParamNextFree.setStatus("current")
_NtnQosTBParamTable_Object = MibTable
ntnQosTBParamTable = _NtnQosTBParamTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 4)
)
if mibBuilder.loadTexts:
    ntnQosTBParamTable.setStatus("current")
_NtnQosTBParamEntry_Object = MibTableRow
ntnQosTBParamEntry = _NtnQosTBParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 4, 1)
)
ntnQosTBParamEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosTBParamId"),
)
if mibBuilder.loadTexts:
    ntnQosTBParamEntry.setStatus("current")
_NtnQosTBParamId_Type = IndexInteger
_NtnQosTBParamId_Object = MibTableColumn
ntnQosTBParamId = _NtnQosTBParamId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 4, 1, 1),
    _NtnQosTBParamId_Type()
)
ntnQosTBParamId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosTBParamId.setStatus("current")


class _NtnQosTBParamType_Type(AutonomousType):
    """Custom type ntnQosTBParamType based on AutonomousType"""
    defaultValue = (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 5, 1)


_NtnQosTBParamType_Object = MibTableColumn
ntnQosTBParamType = _NtnQosTBParamType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 4, 1, 2),
    _NtnQosTBParamType_Type()
)
ntnQosTBParamType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosTBParamType.setStatus("current")


class _NtnQosTBParamRate_Type(Unsigned32):
    """Custom type ntnQosTBParamRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NtnQosTBParamRate_Type.__name__ = "Unsigned32"
_NtnQosTBParamRate_Object = MibTableColumn
ntnQosTBParamRate = _NtnQosTBParamRate_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 4, 1, 3),
    _NtnQosTBParamRate_Type()
)
ntnQosTBParamRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosTBParamRate.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTBParamRate.setUnits("kilobits per second")
_NtnQosTBParamBurstSize_Type = BurstSize
_NtnQosTBParamBurstSize_Object = MibTableColumn
ntnQosTBParamBurstSize = _NtnQosTBParamBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 4, 1, 4),
    _NtnQosTBParamBurstSize_Type()
)
ntnQosTBParamBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosTBParamBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTBParamBurstSize.setUnits("Bytes")


class _NtnQosTBParamInterval_Type(Unsigned32):
    """Custom type ntnQosTBParamInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NtnQosTBParamInterval_Type.__name__ = "Unsigned32"
_NtnQosTBParamInterval_Object = MibTableColumn
ntnQosTBParamInterval = _NtnQosTBParamInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 4, 1, 5),
    _NtnQosTBParamInterval_Type()
)
ntnQosTBParamInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosTBParamInterval.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTBParamInterval.setUnits("microseconds")


class _NtnQosTBParamLabel_Type(SnmpAdminString):
    """Custom type ntnQosTBParamLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtnQosTBParamLabel_Type.__name__ = "SnmpAdminString"
_NtnQosTBParamLabel_Object = MibTableColumn
ntnQosTBParamLabel = _NtnQosTBParamLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 4, 1, 6),
    _NtnQosTBParamLabel_Type()
)
ntnQosTBParamLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosTBParamLabel.setStatus("current")


class _NtnQosTBParamStorage_Type(StorageType):
    """Custom type ntnQosTBParamStorage based on StorageType"""


_NtnQosTBParamStorage_Object = MibTableColumn
ntnQosTBParamStorage = _NtnQosTBParamStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 4, 1, 7),
    _NtnQosTBParamStorage_Type()
)
ntnQosTBParamStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosTBParamStorage.setStatus("current")
_NtnQosTBParamStatus_Type = RowStatus
_NtnQosTBParamStatus_Object = MibTableColumn
ntnQosTBParamStatus = _NtnQosTBParamStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 4, 1, 8),
    _NtnQosTBParamStatus_Type()
)
ntnQosTBParamStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosTBParamStatus.setStatus("current")


class _NtnQosTBParamSessionId_Type(Unsigned32):
    """Custom type ntnQosTBParamSessionId based on Unsigned32"""
    defaultValue = 0


_NtnQosTBParamSessionId_Object = MibTableColumn
ntnQosTBParamSessionId = _NtnQosTBParamSessionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 4, 1, 9),
    _NtnQosTBParamSessionId_Type()
)
ntnQosTBParamSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosTBParamSessionId.setStatus("current")


class _NtnQosTBParamVersion_Type(VersionIndicator):
    """Custom type ntnQosTBParamVersion based on VersionIndicator"""


_NtnQosTBParamVersion_Object = MibTableColumn
ntnQosTBParamVersion = _NtnQosTBParamVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 4, 1, 10),
    _NtnQosTBParamVersion_Type()
)
ntnQosTBParamVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosTBParamVersion.setStatus("current")


class _NtnQosTBParamMinRate_Type(Unsigned32):
    """Custom type ntnQosTBParamMinRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NtnQosTBParamMinRate_Type.__name__ = "Unsigned32"
_NtnQosTBParamMinRate_Object = MibTableColumn
ntnQosTBParamMinRate = _NtnQosTBParamMinRate_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 4, 1, 11),
    _NtnQosTBParamMinRate_Type()
)
ntnQosTBParamMinRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosTBParamMinRate.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosTBParamMinRate.setUnits("kilobits per second")
_NtnQosTBMeters_ObjectIdentity = ObjectIdentity
ntnQosTBMeters = _NtnQosTBMeters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 5)
)
_NtnQosTBParamSimpleTokenBucket_ObjectIdentity = ObjectIdentity
ntnQosTBParamSimpleTokenBucket = _NtnQosTBParamSimpleTokenBucket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 5, 1)
)
if mibBuilder.loadTexts:
    ntnQosTBParamSimpleTokenBucket.setStatus("current")
_NtnQosTBParamAvgRate_ObjectIdentity = ObjectIdentity
ntnQosTBParamAvgRate = _NtnQosTBParamAvgRate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 5, 2)
)
if mibBuilder.loadTexts:
    ntnQosTBParamAvgRate.setStatus("current")
_NtnQosTBParamSrTCMBlind_ObjectIdentity = ObjectIdentity
ntnQosTBParamSrTCMBlind = _NtnQosTBParamSrTCMBlind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 5, 3)
)
if mibBuilder.loadTexts:
    ntnQosTBParamSrTCMBlind.setStatus("current")
_NtnQosTBParamSrTCMAware_ObjectIdentity = ObjectIdentity
ntnQosTBParamSrTCMAware = _NtnQosTBParamSrTCMAware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 5, 4)
)
if mibBuilder.loadTexts:
    ntnQosTBParamSrTCMAware.setStatus("current")
_NtnQosTBParamTrTCMBlind_ObjectIdentity = ObjectIdentity
ntnQosTBParamTrTCMBlind = _NtnQosTBParamTrTCMBlind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 5, 5)
)
if mibBuilder.loadTexts:
    ntnQosTBParamTrTCMBlind.setStatus("current")
_NtnQosTBParamTrTCMAware_ObjectIdentity = ObjectIdentity
ntnQosTBParamTrTCMAware = _NtnQosTBParamTrTCMAware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 5, 6)
)
if mibBuilder.loadTexts:
    ntnQosTBParamTrTCMAware.setStatus("current")
_NtnQosTBParamTswTCM_ObjectIdentity = ObjectIdentity
ntnQosTBParamTswTCM = _NtnQosTBParamTswTCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 5, 7)
)
if mibBuilder.loadTexts:
    ntnQosTBParamTswTCM.setStatus("current")
_NtnQosActionClasses_ObjectIdentity = ObjectIdentity
ntnQosActionClasses = _NtnQosActionClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7)
)
_NtnQosBaseActionNextFree_Type = IndexIntegerNextFree
_NtnQosBaseActionNextFree_Object = MibScalar
ntnQosBaseActionNextFree = _NtnQosBaseActionNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 1),
    _NtnQosBaseActionNextFree_Type()
)
ntnQosBaseActionNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosBaseActionNextFree.setStatus("current")
_NtnQosBaseActionTable_Object = MibTable
ntnQosBaseActionTable = _NtnQosBaseActionTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 2)
)
if mibBuilder.loadTexts:
    ntnQosBaseActionTable.setStatus("current")
_NtnQosBaseActionEntry_Object = MibTableRow
ntnQosBaseActionEntry = _NtnQosBaseActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 2, 1)
)
ntnQosBaseActionEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosBaseActionId"),
)
if mibBuilder.loadTexts:
    ntnQosBaseActionEntry.setStatus("current")
_NtnQosBaseActionId_Type = IndexInteger
_NtnQosBaseActionId_Object = MibTableColumn
ntnQosBaseActionId = _NtnQosBaseActionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 2, 1, 1),
    _NtnQosBaseActionId_Type()
)
ntnQosBaseActionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosBaseActionId.setStatus("current")


class _NtnQosBaseActionDrop_Type(Integer32):
    """Custom type ntnQosBaseActionDrop based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deferredPass", 3),
          ("dontDrop", 2),
          ("drop", 1))
    )


_NtnQosBaseActionDrop_Type.__name__ = "Integer32"
_NtnQosBaseActionDrop_Object = MibTableColumn
ntnQosBaseActionDrop = _NtnQosBaseActionDrop_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 2, 1, 2),
    _NtnQosBaseActionDrop_Type()
)
ntnQosBaseActionDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosBaseActionDrop.setStatus("current")


class _NtnQosBaseActionUpdateDscp_Type(DscpUpdate):
    """Custom type ntnQosBaseActionUpdateDscp based on DscpUpdate"""
    defaultValue = -1


_NtnQosBaseActionUpdateDscp_Object = MibTableColumn
ntnQosBaseActionUpdateDscp = _NtnQosBaseActionUpdateDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 2, 1, 3),
    _NtnQosBaseActionUpdateDscp_Type()
)
ntnQosBaseActionUpdateDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosBaseActionUpdateDscp.setStatus("current")


class _NtnQosBaseActionUpdateUserPriority_Type(Integer32):
    """Custom type ntnQosBaseActionUpdateUserPriority based on Integer32"""
    defaultValue = 12

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
        *(("deriveFromEgressDscp", 11),
          ("deriveFromIngressDscp", 10),
          ("deriveFromIngressTosPrec", 9),
          ("ignore", 12),
          ("markAsPriority0", 1),
          ("markAsPriority1", 2),
          ("markAsPriority2", 3),
          ("markAsPriority3", 4),
          ("markAsPriority4", 5),
          ("markAsPriority5", 6),
          ("markAsPriority6", 7),
          ("markAsPriority7", 8),
          ("markAsPriorityCopy", 13))
    )


_NtnQosBaseActionUpdateUserPriority_Type.__name__ = "Integer32"
_NtnQosBaseActionUpdateUserPriority_Object = MibTableColumn
ntnQosBaseActionUpdateUserPriority = _NtnQosBaseActionUpdateUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 2, 1, 4),
    _NtnQosBaseActionUpdateUserPriority_Type()
)
ntnQosBaseActionUpdateUserPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosBaseActionUpdateUserPriority.setStatus("current")


class _NtnQosBaseActionSetDropPrecedence_Type(Integer32):
    """Custom type ntnQosBaseActionSetDropPrecedence based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highDropPrec", 2),
          ("lowDropPrec", 1))
    )


_NtnQosBaseActionSetDropPrecedence_Type.__name__ = "Integer32"
_NtnQosBaseActionSetDropPrecedence_Object = MibTableColumn
ntnQosBaseActionSetDropPrecedence = _NtnQosBaseActionSetDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 2, 1, 5),
    _NtnQosBaseActionSetDropPrecedence_Type()
)
ntnQosBaseActionSetDropPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosBaseActionSetDropPrecedence.setStatus("current")


class _NtnQosBaseActionCopyToCpu_Type(TruthValue):
    """Custom type ntnQosBaseActionCopyToCpu based on TruthValue"""


_NtnQosBaseActionCopyToCpu_Object = MibTableColumn
ntnQosBaseActionCopyToCpu = _NtnQosBaseActionCopyToCpu_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 2, 1, 6),
    _NtnQosBaseActionCopyToCpu_Type()
)
ntnQosBaseActionCopyToCpu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosBaseActionCopyToCpu.setStatus("current")


class _NtnQosBaseActionMirrorFrame_Type(TruthValue):
    """Custom type ntnQosBaseActionMirrorFrame based on TruthValue"""


_NtnQosBaseActionMirrorFrame_Object = MibTableColumn
ntnQosBaseActionMirrorFrame = _NtnQosBaseActionMirrorFrame_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 2, 1, 7),
    _NtnQosBaseActionMirrorFrame_Type()
)
ntnQosBaseActionMirrorFrame.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosBaseActionMirrorFrame.setStatus("current")


class _NtnQosBaseActionExtension_Type(RowPointer):
    """Custom type ntnQosBaseActionExtension based on RowPointer"""
    defaultValue = (0, 0)


_NtnQosBaseActionExtension_Object = MibTableColumn
ntnQosBaseActionExtension = _NtnQosBaseActionExtension_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 2, 1, 8),
    _NtnQosBaseActionExtension_Type()
)
ntnQosBaseActionExtension.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosBaseActionExtension.setStatus("current")


class _NtnQosBaseActionLabel_Type(SnmpAdminString):
    """Custom type ntnQosBaseActionLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtnQosBaseActionLabel_Type.__name__ = "SnmpAdminString"
_NtnQosBaseActionLabel_Object = MibTableColumn
ntnQosBaseActionLabel = _NtnQosBaseActionLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 2, 1, 9),
    _NtnQosBaseActionLabel_Type()
)
ntnQosBaseActionLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosBaseActionLabel.setStatus("current")


class _NtnQosBaseActionStorage_Type(StorageType):
    """Custom type ntnQosBaseActionStorage based on StorageType"""


_NtnQosBaseActionStorage_Object = MibTableColumn
ntnQosBaseActionStorage = _NtnQosBaseActionStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 2, 1, 10),
    _NtnQosBaseActionStorage_Type()
)
ntnQosBaseActionStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosBaseActionStorage.setStatus("current")
_NtnQosBaseActionStatus_Type = RowStatus
_NtnQosBaseActionStatus_Object = MibTableColumn
ntnQosBaseActionStatus = _NtnQosBaseActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 2, 1, 11),
    _NtnQosBaseActionStatus_Type()
)
ntnQosBaseActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosBaseActionStatus.setStatus("current")
_NtnQosBaseActionSessionId_Type = Unsigned32
_NtnQosBaseActionSessionId_Object = MibTableColumn
ntnQosBaseActionSessionId = _NtnQosBaseActionSessionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 2, 1, 12),
    _NtnQosBaseActionSessionId_Type()
)
ntnQosBaseActionSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosBaseActionSessionId.setStatus("current")
_NtnQosIfcActionNextFree_Type = IndexIntegerNextFree
_NtnQosIfcActionNextFree_Object = MibScalar
ntnQosIfcActionNextFree = _NtnQosIfcActionNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 3),
    _NtnQosIfcActionNextFree_Type()
)
ntnQosIfcActionNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosIfcActionNextFree.setStatus("current")
_NtnQosIfcActionTable_Object = MibTable
ntnQosIfcActionTable = _NtnQosIfcActionTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 4)
)
if mibBuilder.loadTexts:
    ntnQosIfcActionTable.setStatus("current")
_NtnQosIfcActionEntry_Object = MibTableRow
ntnQosIfcActionEntry = _NtnQosIfcActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 4, 1)
)
ntnQosIfcActionEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfcActionId"),
)
if mibBuilder.loadTexts:
    ntnQosIfcActionEntry.setStatus("current")
_NtnQosIfcActionId_Type = IndexInteger
_NtnQosIfcActionId_Object = MibTableColumn
ntnQosIfcActionId = _NtnQosIfcActionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 4, 1, 1),
    _NtnQosIfcActionId_Type()
)
ntnQosIfcActionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosIfcActionId.setStatus("current")


class _NtnQosIfcActionUpdateVlanId_Type(Integer32):
    """Custom type ntnQosIfcActionUpdateVlanId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4094),
    )


_NtnQosIfcActionUpdateVlanId_Type.__name__ = "Integer32"
_NtnQosIfcActionUpdateVlanId_Object = MibTableColumn
ntnQosIfcActionUpdateVlanId = _NtnQosIfcActionUpdateVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 4, 1, 2),
    _NtnQosIfcActionUpdateVlanId_Type()
)
ntnQosIfcActionUpdateVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfcActionUpdateVlanId.setStatus("current")


class _NtnQosIfcActionSetEgressMask_Type(OctetString):
    """Custom type ntnQosIfcActionSetEgressMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(64, 64),
    )


_NtnQosIfcActionSetEgressMask_Type.__name__ = "OctetString"
_NtnQosIfcActionSetEgressMask_Object = MibTableColumn
ntnQosIfcActionSetEgressMask = _NtnQosIfcActionSetEgressMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 4, 1, 3),
    _NtnQosIfcActionSetEgressMask_Type()
)
ntnQosIfcActionSetEgressMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfcActionSetEgressMask.setStatus("current")


class _NtnQosIfcActionSetEgressUcastIfc_Type(InterfaceIndexOrZero):
    """Custom type ntnQosIfcActionSetEgressUcastIfc based on InterfaceIndexOrZero"""
    defaultValue = 0


_NtnQosIfcActionSetEgressUcastIfc_Object = MibTableColumn
ntnQosIfcActionSetEgressUcastIfc = _NtnQosIfcActionSetEgressUcastIfc_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 4, 1, 4),
    _NtnQosIfcActionSetEgressUcastIfc_Type()
)
ntnQosIfcActionSetEgressUcastIfc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfcActionSetEgressUcastIfc.setStatus("current")


class _NtnQosIfcActionSetEgressNUcastIfc_Type(InterfaceIndexOrZero):
    """Custom type ntnQosIfcActionSetEgressNUcastIfc based on InterfaceIndexOrZero"""
    defaultValue = 0


_NtnQosIfcActionSetEgressNUcastIfc_Object = MibTableColumn
ntnQosIfcActionSetEgressNUcastIfc = _NtnQosIfcActionSetEgressNUcastIfc_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 4, 1, 5),
    _NtnQosIfcActionSetEgressNUcastIfc_Type()
)
ntnQosIfcActionSetEgressNUcastIfc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfcActionSetEgressNUcastIfc.setStatus("current")


class _NtnQosIfcActionExtension_Type(RowPointer):
    """Custom type ntnQosIfcActionExtension based on RowPointer"""
    defaultValue = (0, 0)


_NtnQosIfcActionExtension_Object = MibTableColumn
ntnQosIfcActionExtension = _NtnQosIfcActionExtension_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 4, 1, 6),
    _NtnQosIfcActionExtension_Type()
)
ntnQosIfcActionExtension.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfcActionExtension.setStatus("current")


class _NtnQosIfcActionLabel_Type(SnmpAdminString):
    """Custom type ntnQosIfcActionLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtnQosIfcActionLabel_Type.__name__ = "SnmpAdminString"
_NtnQosIfcActionLabel_Object = MibTableColumn
ntnQosIfcActionLabel = _NtnQosIfcActionLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 4, 1, 7),
    _NtnQosIfcActionLabel_Type()
)
ntnQosIfcActionLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfcActionLabel.setStatus("current")


class _NtnQosIfcActionStorage_Type(StorageType):
    """Custom type ntnQosIfcActionStorage based on StorageType"""


_NtnQosIfcActionStorage_Object = MibTableColumn
ntnQosIfcActionStorage = _NtnQosIfcActionStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 4, 1, 8),
    _NtnQosIfcActionStorage_Type()
)
ntnQosIfcActionStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfcActionStorage.setStatus("current")
_NtnQosIfcActionStatus_Type = RowStatus
_NtnQosIfcActionStatus_Object = MibTableColumn
ntnQosIfcActionStatus = _NtnQosIfcActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 4, 1, 9),
    _NtnQosIfcActionStatus_Type()
)
ntnQosIfcActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfcActionStatus.setStatus("current")
_NtnQosIfcActionSessionId_Type = Unsigned32
_NtnQosIfcActionSessionId_Object = MibTableColumn
ntnQosIfcActionSessionId = _NtnQosIfcActionSessionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 7, 4, 1, 10),
    _NtnQosIfcActionSessionId_Type()
)
ntnQosIfcActionSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfcActionSessionId.setStatus("current")
_NtnQosPolicyClasses_ObjectIdentity = ObjectIdentity
ntnQosPolicyClasses = _NtnQosPolicyClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8)
)
_NtnQosPolicyNextFree_Type = IndexIntegerNextFree
_NtnQosPolicyNextFree_Object = MibScalar
ntnQosPolicyNextFree = _NtnQosPolicyNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 1),
    _NtnQosPolicyNextFree_Type()
)
ntnQosPolicyNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyNextFree.setStatus("current")
_NtnQosPolicyTable_Object = MibTable
ntnQosPolicyTable = _NtnQosPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2)
)
if mibBuilder.loadTexts:
    ntnQosPolicyTable.setStatus("current")
_NtnQosPolicyEntry_Object = MibTableRow
ntnQosPolicyEntry = _NtnQosPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2, 1)
)
ntnQosPolicyEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyId"),
)
if mibBuilder.loadTexts:
    ntnQosPolicyEntry.setStatus("current")
_NtnQosPolicyId_Type = IndexInteger
_NtnQosPolicyId_Object = MibTableColumn
ntnQosPolicyId = _NtnQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2, 1, 1),
    _NtnQosPolicyId_Type()
)
ntnQosPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosPolicyId.setStatus("current")


class _NtnQosPolicyClassifierType_Type(Integer32):
    """Custom type ntnQosPolicyClassifierType based on Integer32"""
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
        *(("blockOfClfrs", 2),
          ("filterSetBlockOfClfrs", 4),
          ("filterSetIndividualClfr", 3),
          ("individualClfr", 1))
    )


_NtnQosPolicyClassifierType_Type.__name__ = "Integer32"
_NtnQosPolicyClassifierType_Object = MibTableColumn
ntnQosPolicyClassifierType = _NtnQosPolicyClassifierType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2, 1, 2),
    _NtnQosPolicyClassifierType_Type()
)
ntnQosPolicyClassifierType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosPolicyClassifierType.setStatus("current")


class _NtnQosPolicyClassifierId_Type(Unsigned32):
    """Custom type ntnQosPolicyClassifierId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtnQosPolicyClassifierId_Type.__name__ = "Unsigned32"
_NtnQosPolicyClassifierId_Object = MibTableColumn
ntnQosPolicyClassifierId = _NtnQosPolicyClassifierId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2, 1, 3),
    _NtnQosPolicyClassifierId_Type()
)
ntnQosPolicyClassifierId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosPolicyClassifierId.setStatus("current")
_NtnQosPolicyInterfaceRoles_Type = RoleCombination
_NtnQosPolicyInterfaceRoles_Object = MibTableColumn
ntnQosPolicyInterfaceRoles = _NtnQosPolicyInterfaceRoles_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2, 1, 4),
    _NtnQosPolicyInterfaceRoles_Type()
)
ntnQosPolicyInterfaceRoles.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosPolicyInterfaceRoles.setStatus("current")


class _NtnQosPolicyPrecedence_Type(Unsigned32):
    """Custom type ntnQosPolicyPrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtnQosPolicyPrecedence_Type.__name__ = "Unsigned32"
_NtnQosPolicyPrecedence_Object = MibTableColumn
ntnQosPolicyPrecedence = _NtnQosPolicyPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2, 1, 5),
    _NtnQosPolicyPrecedence_Type()
)
ntnQosPolicyPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosPolicyPrecedence.setStatus("current")
_NtnQosPolicyMeter_Type = IndexIntegerOrZero
_NtnQosPolicyMeter_Object = MibTableColumn
ntnQosPolicyMeter = _NtnQosPolicyMeter_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2, 1, 6),
    _NtnQosPolicyMeter_Type()
)
ntnQosPolicyMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosPolicyMeter.setStatus("current")


class _NtnQosPolicyAction_Type(IndexIntegerOrZero):
    """Custom type ntnQosPolicyAction based on IndexIntegerOrZero"""
    defaultValue = 0


_NtnQosPolicyAction_Object = MibTableColumn
ntnQosPolicyAction = _NtnQosPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2, 1, 7),
    _NtnQosPolicyAction_Type()
)
ntnQosPolicyAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosPolicyAction.setStatus("current")


class _NtnQosPolicyNonMatchAction_Type(IndexIntegerOrZero):
    """Custom type ntnQosPolicyNonMatchAction based on IndexIntegerOrZero"""
    defaultValue = 0


_NtnQosPolicyNonMatchAction_Object = MibTableColumn
ntnQosPolicyNonMatchAction = _NtnQosPolicyNonMatchAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2, 1, 8),
    _NtnQosPolicyNonMatchAction_Type()
)
ntnQosPolicyNonMatchAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosPolicyNonMatchAction.setStatus("current")


class _NtnQosPolicyLabel_Type(SnmpAdminString):
    """Custom type ntnQosPolicyLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtnQosPolicyLabel_Type.__name__ = "SnmpAdminString"
_NtnQosPolicyLabel_Object = MibTableColumn
ntnQosPolicyLabel = _NtnQosPolicyLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2, 1, 9),
    _NtnQosPolicyLabel_Type()
)
ntnQosPolicyLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosPolicyLabel.setStatus("current")


class _NtnQosPolicyStorage_Type(StorageType):
    """Custom type ntnQosPolicyStorage based on StorageType"""


_NtnQosPolicyStorage_Object = MibTableColumn
ntnQosPolicyStorage = _NtnQosPolicyStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2, 1, 10),
    _NtnQosPolicyStorage_Type()
)
ntnQosPolicyStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosPolicyStorage.setStatus("current")
_NtnQosPolicyStatus_Type = RowStatus
_NtnQosPolicyStatus_Object = MibTableColumn
ntnQosPolicyStatus = _NtnQosPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2, 1, 11),
    _NtnQosPolicyStatus_Type()
)
ntnQosPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosPolicyStatus.setStatus("current")


class _NtnQosPolicyStats_Type(IndexIntegerOrZero):
    """Custom type ntnQosPolicyStats based on IndexIntegerOrZero"""
    defaultValue = 0


_NtnQosPolicyStats_Object = MibTableColumn
ntnQosPolicyStats = _NtnQosPolicyStats_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2, 1, 12),
    _NtnQosPolicyStats_Type()
)
ntnQosPolicyStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosPolicyStats.setStatus("current")


class _NtnQosPolicyStatsType_Type(Integer32):
    """Custom type ntnQosPolicyStatsType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggregateClfr", 2),
          ("individualClfr", 1))
    )


_NtnQosPolicyStatsType_Type.__name__ = "Integer32"
_NtnQosPolicyStatsType_Object = MibTableColumn
ntnQosPolicyStatsType = _NtnQosPolicyStatsType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2, 1, 13),
    _NtnQosPolicyStatsType_Type()
)
ntnQosPolicyStatsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosPolicyStatsType.setStatus("current")
_NtnQosPolicyInterfaceIndex_Type = InterfaceIndexOrZero
_NtnQosPolicyInterfaceIndex_Object = MibTableColumn
ntnQosPolicyInterfaceIndex = _NtnQosPolicyInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2, 1, 14),
    _NtnQosPolicyInterfaceIndex_Type()
)
ntnQosPolicyInterfaceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosPolicyInterfaceIndex.setStatus("current")


class _NtnQosPolicySessionId_Type(Unsigned32):
    """Custom type ntnQosPolicySessionId based on Unsigned32"""
    defaultValue = 0


_NtnQosPolicySessionId_Object = MibTableColumn
ntnQosPolicySessionId = _NtnQosPolicySessionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2, 1, 15),
    _NtnQosPolicySessionId_Type()
)
ntnQosPolicySessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosPolicySessionId.setStatus("current")


class _NtnQosPolicyVersion_Type(VersionIndicator):
    """Custom type ntnQosPolicyVersion based on VersionIndicator"""


_NtnQosPolicyVersion_Object = MibTableColumn
ntnQosPolicyVersion = _NtnQosPolicyVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2, 1, 16),
    _NtnQosPolicyVersion_Type()
)
ntnQosPolicyVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosPolicyVersion.setStatus("current")


class _NtnQosPolicyMeteringMode_Type(Integer32):
    """Custom type ntnQosPolicyMeteringMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blockBasedMetering", 3),
          ("noMetering", 1),
          ("policyBasedMetering", 2))
    )


_NtnQosPolicyMeteringMode_Type.__name__ = "Integer32"
_NtnQosPolicyMeteringMode_Object = MibTableColumn
ntnQosPolicyMeteringMode = _NtnQosPolicyMeteringMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 2, 1, 17),
    _NtnQosPolicyMeteringMode_Type()
)
ntnQosPolicyMeteringMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyMeteringMode.setStatus("current")
_NtnQosCountActNextFree_Type = IndexIntegerNextFree
_NtnQosCountActNextFree_Object = MibScalar
ntnQosCountActNextFree = _NtnQosCountActNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 3),
    _NtnQosCountActNextFree_Type()
)
ntnQosCountActNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosCountActNextFree.setStatus("current")
_NtnQosCountActTable_Object = MibTable
ntnQosCountActTable = _NtnQosCountActTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 4)
)
if mibBuilder.loadTexts:
    ntnQosCountActTable.setStatus("current")
_NtnQosCountActEntry_Object = MibTableRow
ntnQosCountActEntry = _NtnQosCountActEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 4, 1)
)
ntnQosCountActEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosCountActId"),
)
if mibBuilder.loadTexts:
    ntnQosCountActEntry.setStatus("current")
_NtnQosCountActId_Type = IndexInteger
_NtnQosCountActId_Object = MibTableColumn
ntnQosCountActId = _NtnQosCountActId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 4, 1, 1),
    _NtnQosCountActId_Type()
)
ntnQosCountActId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosCountActId.setStatus("current")
_NtnQosCountActOctets_Type = Counter64
_NtnQosCountActOctets_Object = MibTableColumn
ntnQosCountActOctets = _NtnQosCountActOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 4, 1, 2),
    _NtnQosCountActOctets_Type()
)
ntnQosCountActOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosCountActOctets.setStatus("current")
_NtnQosCountActPkts_Type = Counter64
_NtnQosCountActPkts_Object = MibTableColumn
ntnQosCountActPkts = _NtnQosCountActPkts_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 4, 1, 3),
    _NtnQosCountActPkts_Type()
)
ntnQosCountActPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosCountActPkts.setStatus("current")


class _NtnQosCountActStorage_Type(StorageType):
    """Custom type ntnQosCountActStorage based on StorageType"""


_NtnQosCountActStorage_Object = MibTableColumn
ntnQosCountActStorage = _NtnQosCountActStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 4, 1, 4),
    _NtnQosCountActStorage_Type()
)
ntnQosCountActStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosCountActStorage.setStatus("current")
_NtnQosCountActStatus_Type = RowStatus
_NtnQosCountActStatus_Object = MibTableColumn
ntnQosCountActStatus = _NtnQosCountActStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 4, 1, 5),
    _NtnQosCountActStatus_Type()
)
ntnQosCountActStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosCountActStatus.setStatus("current")
_NtnQosCountActSessionId_Type = Unsigned32
_NtnQosCountActSessionId_Object = MibTableColumn
ntnQosCountActSessionId = _NtnQosCountActSessionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 4, 1, 6),
    _NtnQosCountActSessionId_Type()
)
ntnQosCountActSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosCountActSessionId.setStatus("current")
_NtnQosFilterStatsTable_Object = MibTable
ntnQosFilterStatsTable = _NtnQosFilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 5)
)
if mibBuilder.loadTexts:
    ntnQosFilterStatsTable.setStatus("current")
_NtnQosFilterStatsEntry_Object = MibTableRow
ntnQosFilterStatsEntry = _NtnQosFilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 5, 1)
)
ntnQosFilterStatsEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterStatsPolicyId"),
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterStatsFilterId"),
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterStatsInterfaceId"),
)
if mibBuilder.loadTexts:
    ntnQosFilterStatsEntry.setStatus("current")
_NtnQosFilterStatsPolicyId_Type = IndexInteger
_NtnQosFilterStatsPolicyId_Object = MibTableColumn
ntnQosFilterStatsPolicyId = _NtnQosFilterStatsPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 5, 1, 1),
    _NtnQosFilterStatsPolicyId_Type()
)
ntnQosFilterStatsPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosFilterStatsPolicyId.setStatus("current")
_NtnQosFilterStatsFilterId_Type = IndexIntegerOrZero
_NtnQosFilterStatsFilterId_Object = MibTableColumn
ntnQosFilterStatsFilterId = _NtnQosFilterStatsFilterId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 5, 1, 2),
    _NtnQosFilterStatsFilterId_Type()
)
ntnQosFilterStatsFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosFilterStatsFilterId.setStatus("current")
_NtnQosFilterStatsInterfaceId_Type = InterfaceIndex
_NtnQosFilterStatsInterfaceId_Object = MibTableColumn
ntnQosFilterStatsInterfaceId = _NtnQosFilterStatsInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 5, 1, 3),
    _NtnQosFilterStatsInterfaceId_Type()
)
ntnQosFilterStatsInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosFilterStatsInterfaceId.setStatus("current")
_NtnQosFilterStatsInProfileOctets_Type = Counter64
_NtnQosFilterStatsInProfileOctets_Object = MibTableColumn
ntnQosFilterStatsInProfileOctets = _NtnQosFilterStatsInProfileOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 5, 1, 4),
    _NtnQosFilterStatsInProfileOctets_Type()
)
ntnQosFilterStatsInProfileOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosFilterStatsInProfileOctets.setStatus("current")
_NtnQosFilterStatsInProfilePkts_Type = Counter64
_NtnQosFilterStatsInProfilePkts_Object = MibTableColumn
ntnQosFilterStatsInProfilePkts = _NtnQosFilterStatsInProfilePkts_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 5, 1, 5),
    _NtnQosFilterStatsInProfilePkts_Type()
)
ntnQosFilterStatsInProfilePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosFilterStatsInProfilePkts.setStatus("current")
_NtnQosFilterStatsOutOfProfileOctets_Type = Counter64
_NtnQosFilterStatsOutOfProfileOctets_Object = MibTableColumn
ntnQosFilterStatsOutOfProfileOctets = _NtnQosFilterStatsOutOfProfileOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 5, 1, 6),
    _NtnQosFilterStatsOutOfProfileOctets_Type()
)
ntnQosFilterStatsOutOfProfileOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosFilterStatsOutOfProfileOctets.setStatus("current")
_NtnQosFilterStatsOutOfProfilePkts_Type = Counter64
_NtnQosFilterStatsOutOfProfilePkts_Object = MibTableColumn
ntnQosFilterStatsOutOfProfilePkts = _NtnQosFilterStatsOutOfProfilePkts_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 5, 1, 7),
    _NtnQosFilterStatsOutOfProfilePkts_Type()
)
ntnQosFilterStatsOutOfProfilePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosFilterStatsOutOfProfilePkts.setStatus("current")


class _NtnQosFilterStatsStorage_Type(StorageType):
    """Custom type ntnQosFilterStatsStorage based on StorageType"""


_NtnQosFilterStatsStorage_Object = MibTableColumn
ntnQosFilterStatsStorage = _NtnQosFilterStatsStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 5, 1, 8),
    _NtnQosFilterStatsStorage_Type()
)
ntnQosFilterStatsStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosFilterStatsStorage.setStatus("current")
_NtnQosFilterStatsStatus_Type = RowStatus
_NtnQosFilterStatsStatus_Object = MibTableColumn
ntnQosFilterStatsStatus = _NtnQosFilterStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 5, 1, 9),
    _NtnQosFilterStatsStatus_Type()
)
ntnQosFilterStatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosFilterStatsStatus.setStatus("current")
_NtnQosPolicyDiagsTable_Object = MibTable
ntnQosPolicyDiagsTable = _NtnQosPolicyDiagsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 6)
)
if mibBuilder.loadTexts:
    ntnQosPolicyDiagsTable.setStatus("current")
_NtnQosPolicyDiagsEntry_Object = MibTableRow
ntnQosPolicyDiagsEntry = _NtnQosPolicyDiagsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 6, 1)
)
if mibBuilder.loadTexts:
    ntnQosPolicyDiagsEntry.setStatus("current")
_NtnQosPolicyDiagsMasksConsumed_Type = Unsigned32
_NtnQosPolicyDiagsMasksConsumed_Object = MibTableColumn
ntnQosPolicyDiagsMasksConsumed = _NtnQosPolicyDiagsMasksConsumed_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 6, 1, 1),
    _NtnQosPolicyDiagsMasksConsumed_Type()
)
ntnQosPolicyDiagsMasksConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyDiagsMasksConsumed.setStatus("current")
_NtnQosPolicyDiagsFiltersConsumed_Type = Unsigned32
_NtnQosPolicyDiagsFiltersConsumed_Object = MibTableColumn
ntnQosPolicyDiagsFiltersConsumed = _NtnQosPolicyDiagsFiltersConsumed_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 6, 1, 2),
    _NtnQosPolicyDiagsFiltersConsumed_Type()
)
ntnQosPolicyDiagsFiltersConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyDiagsFiltersConsumed.setStatus("current")
_NtnQosPolicyDiagsMetersConsumed_Type = Unsigned32
_NtnQosPolicyDiagsMetersConsumed_Object = MibTableColumn
ntnQosPolicyDiagsMetersConsumed = _NtnQosPolicyDiagsMetersConsumed_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 6, 1, 3),
    _NtnQosPolicyDiagsMetersConsumed_Type()
)
ntnQosPolicyDiagsMetersConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyDiagsMetersConsumed.setStatus("current")
_NtnQosPolicyDiagsNonQosMasksConsumed_Type = Unsigned32
_NtnQosPolicyDiagsNonQosMasksConsumed_Object = MibTableColumn
ntnQosPolicyDiagsNonQosMasksConsumed = _NtnQosPolicyDiagsNonQosMasksConsumed_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 6, 1, 4),
    _NtnQosPolicyDiagsNonQosMasksConsumed_Type()
)
ntnQosPolicyDiagsNonQosMasksConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyDiagsNonQosMasksConsumed.setStatus("current")
_NtnQosPolicyDiagsNonQosFiltersConsumed_Type = Unsigned32
_NtnQosPolicyDiagsNonQosFiltersConsumed_Object = MibTableColumn
ntnQosPolicyDiagsNonQosFiltersConsumed = _NtnQosPolicyDiagsNonQosFiltersConsumed_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 6, 1, 5),
    _NtnQosPolicyDiagsNonQosFiltersConsumed_Type()
)
ntnQosPolicyDiagsNonQosFiltersConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyDiagsNonQosFiltersConsumed.setStatus("current")
_NtnQosPolicyDiagsNonQosMetersConsumed_Type = Unsigned32
_NtnQosPolicyDiagsNonQosMetersConsumed_Object = MibTableColumn
ntnQosPolicyDiagsNonQosMetersConsumed = _NtnQosPolicyDiagsNonQosMetersConsumed_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 6, 1, 6),
    _NtnQosPolicyDiagsNonQosMetersConsumed_Type()
)
ntnQosPolicyDiagsNonQosMetersConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyDiagsNonQosMetersConsumed.setStatus("current")
_NtnQosPolicyDiagsCountersConsumed_Type = Unsigned32
_NtnQosPolicyDiagsCountersConsumed_Object = MibTableColumn
ntnQosPolicyDiagsCountersConsumed = _NtnQosPolicyDiagsCountersConsumed_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 6, 1, 7),
    _NtnQosPolicyDiagsCountersConsumed_Type()
)
ntnQosPolicyDiagsCountersConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyDiagsCountersConsumed.setStatus("current")
_NtnQosPolicyDiagsTotalMasksAvail_Type = Unsigned32
_NtnQosPolicyDiagsTotalMasksAvail_Object = MibTableColumn
ntnQosPolicyDiagsTotalMasksAvail = _NtnQosPolicyDiagsTotalMasksAvail_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 6, 1, 8),
    _NtnQosPolicyDiagsTotalMasksAvail_Type()
)
ntnQosPolicyDiagsTotalMasksAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyDiagsTotalMasksAvail.setStatus("current")
_NtnQosPolicyDiagsTotalFiltersAvail_Type = Unsigned32
_NtnQosPolicyDiagsTotalFiltersAvail_Object = MibTableColumn
ntnQosPolicyDiagsTotalFiltersAvail = _NtnQosPolicyDiagsTotalFiltersAvail_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 6, 1, 9),
    _NtnQosPolicyDiagsTotalFiltersAvail_Type()
)
ntnQosPolicyDiagsTotalFiltersAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyDiagsTotalFiltersAvail.setStatus("current")
_NtnQosPolicyDiagsTotalMetersAvail_Type = Unsigned32
_NtnQosPolicyDiagsTotalMetersAvail_Object = MibTableColumn
ntnQosPolicyDiagsTotalMetersAvail = _NtnQosPolicyDiagsTotalMetersAvail_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 6, 1, 10),
    _NtnQosPolicyDiagsTotalMetersAvail_Type()
)
ntnQosPolicyDiagsTotalMetersAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyDiagsTotalMetersAvail.setStatus("current")
_NtnQosPolicyDiagsTotalCountersAvail_Type = Unsigned32
_NtnQosPolicyDiagsTotalCountersAvail_Object = MibTableColumn
ntnQosPolicyDiagsTotalCountersAvail = _NtnQosPolicyDiagsTotalCountersAvail_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 6, 1, 11),
    _NtnQosPolicyDiagsTotalCountersAvail_Type()
)
ntnQosPolicyDiagsTotalCountersAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyDiagsTotalCountersAvail.setStatus("current")
_NtnQosPolicyPrecResDiagsTable_Object = MibTable
ntnQosPolicyPrecResDiagsTable = _NtnQosPolicyPrecResDiagsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7)
)
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsTable.setStatus("current")
_NtnQosPolicyPrecResDiagsEntry_Object = MibTableRow
ntnQosPolicyPrecResDiagsEntry = _NtnQosPolicyPrecResDiagsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7, 1)
)
ntnQosPolicyPrecResDiagsEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyPrecResDiagsPrec"),
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyPrecResDiagsInterface"),
)
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsEntry.setStatus("current")


class _NtnQosPolicyPrecResDiagsPrec_Type(Unsigned32):
    """Custom type ntnQosPolicyPrecResDiagsPrec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtnQosPolicyPrecResDiagsPrec_Type.__name__ = "Unsigned32"
_NtnQosPolicyPrecResDiagsPrec_Object = MibTableColumn
ntnQosPolicyPrecResDiagsPrec = _NtnQosPolicyPrecResDiagsPrec_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7, 1, 1),
    _NtnQosPolicyPrecResDiagsPrec_Type()
)
ntnQosPolicyPrecResDiagsPrec.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsPrec.setStatus("current")
_NtnQosPolicyPrecResDiagsInterface_Type = InterfaceIndex
_NtnQosPolicyPrecResDiagsInterface_Object = MibTableColumn
ntnQosPolicyPrecResDiagsInterface = _NtnQosPolicyPrecResDiagsInterface_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7, 1, 2),
    _NtnQosPolicyPrecResDiagsInterface_Type()
)
ntnQosPolicyPrecResDiagsInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsInterface.setStatus("current")
_NtnQosPolicyPrecResDiagsKeysConsumed_Type = Unsigned32
_NtnQosPolicyPrecResDiagsKeysConsumed_Object = MibTableColumn
ntnQosPolicyPrecResDiagsKeysConsumed = _NtnQosPolicyPrecResDiagsKeysConsumed_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7, 1, 3),
    _NtnQosPolicyPrecResDiagsKeysConsumed_Type()
)
ntnQosPolicyPrecResDiagsKeysConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsKeysConsumed.setStatus("current")
_NtnQosPolicyPrecResDiagsFiltersConsumed_Type = Unsigned32
_NtnQosPolicyPrecResDiagsFiltersConsumed_Object = MibTableColumn
ntnQosPolicyPrecResDiagsFiltersConsumed = _NtnQosPolicyPrecResDiagsFiltersConsumed_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7, 1, 4),
    _NtnQosPolicyPrecResDiagsFiltersConsumed_Type()
)
ntnQosPolicyPrecResDiagsFiltersConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsFiltersConsumed.setStatus("current")
_NtnQosPolicyPrecResDiagsMetersConsumed_Type = Unsigned32
_NtnQosPolicyPrecResDiagsMetersConsumed_Object = MibTableColumn
ntnQosPolicyPrecResDiagsMetersConsumed = _NtnQosPolicyPrecResDiagsMetersConsumed_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7, 1, 5),
    _NtnQosPolicyPrecResDiagsMetersConsumed_Type()
)
ntnQosPolicyPrecResDiagsMetersConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsMetersConsumed.setStatus("current")
_NtnQosPolicyPrecResDiagsNonQosKeysConsumed_Type = Unsigned32
_NtnQosPolicyPrecResDiagsNonQosKeysConsumed_Object = MibTableColumn
ntnQosPolicyPrecResDiagsNonQosKeysConsumed = _NtnQosPolicyPrecResDiagsNonQosKeysConsumed_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7, 1, 6),
    _NtnQosPolicyPrecResDiagsNonQosKeysConsumed_Type()
)
ntnQosPolicyPrecResDiagsNonQosKeysConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsNonQosKeysConsumed.setStatus("current")
_NtnQosPolicyPrecResDiagsNonQosFiltersConsumed_Type = Unsigned32
_NtnQosPolicyPrecResDiagsNonQosFiltersConsumed_Object = MibTableColumn
ntnQosPolicyPrecResDiagsNonQosFiltersConsumed = _NtnQosPolicyPrecResDiagsNonQosFiltersConsumed_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7, 1, 7),
    _NtnQosPolicyPrecResDiagsNonQosFiltersConsumed_Type()
)
ntnQosPolicyPrecResDiagsNonQosFiltersConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsNonQosFiltersConsumed.setStatus("current")
_NtnQosPolicyPrecResDiagsNonQosMetersConsumed_Type = Unsigned32
_NtnQosPolicyPrecResDiagsNonQosMetersConsumed_Object = MibTableColumn
ntnQosPolicyPrecResDiagsNonQosMetersConsumed = _NtnQosPolicyPrecResDiagsNonQosMetersConsumed_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7, 1, 8),
    _NtnQosPolicyPrecResDiagsNonQosMetersConsumed_Type()
)
ntnQosPolicyPrecResDiagsNonQosMetersConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsNonQosMetersConsumed.setStatus("current")
_NtnQosPolicyPrecResDiagsCountersConsumed_Type = Unsigned32
_NtnQosPolicyPrecResDiagsCountersConsumed_Object = MibTableColumn
ntnQosPolicyPrecResDiagsCountersConsumed = _NtnQosPolicyPrecResDiagsCountersConsumed_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7, 1, 9),
    _NtnQosPolicyPrecResDiagsCountersConsumed_Type()
)
ntnQosPolicyPrecResDiagsCountersConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsCountersConsumed.setStatus("current")
_NtnQosPolicyPrecResDiagsTotalKeysAvail_Type = Unsigned32
_NtnQosPolicyPrecResDiagsTotalKeysAvail_Object = MibTableColumn
ntnQosPolicyPrecResDiagsTotalKeysAvail = _NtnQosPolicyPrecResDiagsTotalKeysAvail_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7, 1, 10),
    _NtnQosPolicyPrecResDiagsTotalKeysAvail_Type()
)
ntnQosPolicyPrecResDiagsTotalKeysAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsTotalKeysAvail.setStatus("current")
_NtnQosPolicyPrecResDiagsTotalFiltersAvail_Type = Unsigned32
_NtnQosPolicyPrecResDiagsTotalFiltersAvail_Object = MibTableColumn
ntnQosPolicyPrecResDiagsTotalFiltersAvail = _NtnQosPolicyPrecResDiagsTotalFiltersAvail_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7, 1, 11),
    _NtnQosPolicyPrecResDiagsTotalFiltersAvail_Type()
)
ntnQosPolicyPrecResDiagsTotalFiltersAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsTotalFiltersAvail.setStatus("current")
_NtnQosPolicyPrecResDiagsTotalMetersAvail_Type = Unsigned32
_NtnQosPolicyPrecResDiagsTotalMetersAvail_Object = MibTableColumn
ntnQosPolicyPrecResDiagsTotalMetersAvail = _NtnQosPolicyPrecResDiagsTotalMetersAvail_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7, 1, 12),
    _NtnQosPolicyPrecResDiagsTotalMetersAvail_Type()
)
ntnQosPolicyPrecResDiagsTotalMetersAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsTotalMetersAvail.setStatus("current")
_NtnQosPolicyPrecResDiagsTotalCountersAvail_Type = Unsigned32
_NtnQosPolicyPrecResDiagsTotalCountersAvail_Object = MibTableColumn
ntnQosPolicyPrecResDiagsTotalCountersAvail = _NtnQosPolicyPrecResDiagsTotalCountersAvail_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7, 1, 13),
    _NtnQosPolicyPrecResDiagsTotalCountersAvail_Type()
)
ntnQosPolicyPrecResDiagsTotalCountersAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsTotalCountersAvail.setStatus("current")
_NtnQosPolicyPrecResDiagsRangeChkElemsConsumed_Type = Unsigned32
_NtnQosPolicyPrecResDiagsRangeChkElemsConsumed_Object = MibTableColumn
ntnQosPolicyPrecResDiagsRangeChkElemsConsumed = _NtnQosPolicyPrecResDiagsRangeChkElemsConsumed_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7, 1, 14),
    _NtnQosPolicyPrecResDiagsRangeChkElemsConsumed_Type()
)
ntnQosPolicyPrecResDiagsRangeChkElemsConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsRangeChkElemsConsumed.setStatus("current")
_NtnQosPolicyPrecResDiagsApplicationIdUsed_Type = Unsigned32
_NtnQosPolicyPrecResDiagsApplicationIdUsed_Object = MibTableColumn
ntnQosPolicyPrecResDiagsApplicationIdUsed = _NtnQosPolicyPrecResDiagsApplicationIdUsed_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7, 1, 15),
    _NtnQosPolicyPrecResDiagsApplicationIdUsed_Type()
)
ntnQosPolicyPrecResDiagsApplicationIdUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsApplicationIdUsed.setStatus("current")


class _NtnQosPolicyPrecResDiagsApplicationNameUsed_Type(SnmpAdminString):
    """Custom type ntnQosPolicyPrecResDiagsApplicationNameUsed based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtnQosPolicyPrecResDiagsApplicationNameUsed_Type.__name__ = "SnmpAdminString"
_NtnQosPolicyPrecResDiagsApplicationNameUsed_Object = MibTableColumn
ntnQosPolicyPrecResDiagsApplicationNameUsed = _NtnQosPolicyPrecResDiagsApplicationNameUsed_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7, 1, 16),
    _NtnQosPolicyPrecResDiagsApplicationNameUsed_Type()
)
ntnQosPolicyPrecResDiagsApplicationNameUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsApplicationNameUsed.setStatus("current")
_NtnQosPolicyPrecResDiagsRangeChkElemsAvail_Type = Unsigned32
_NtnQosPolicyPrecResDiagsRangeChkElemsAvail_Object = MibTableColumn
ntnQosPolicyPrecResDiagsRangeChkElemsAvail = _NtnQosPolicyPrecResDiagsRangeChkElemsAvail_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 8, 7, 1, 17),
    _NtnQosPolicyPrecResDiagsRangeChkElemsAvail_Type()
)
ntnQosPolicyPrecResDiagsRangeChkElemsAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsRangeChkElemsAvail.setStatus("current")
_NtnQosInterfaceClasses_ObjectIdentity = ObjectIdentity
ntnQosInterfaceClasses = _NtnQosInterfaceClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9)
)
_NtnQosIfAssignmentTable_Object = MibTable
ntnQosIfAssignmentTable = _NtnQosIfAssignmentTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 1)
)
if mibBuilder.loadTexts:
    ntnQosIfAssignmentTable.setStatus("current")
_NtnQosIfAssignmentEntry_Object = MibTableRow
ntnQosIfAssignmentEntry = _NtnQosIfAssignmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 1, 1)
)
ntnQosIfAssignmentEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfAssignmentIfIndex"),
)
if mibBuilder.loadTexts:
    ntnQosIfAssignmentEntry.setStatus("current")
_NtnQosIfAssignmentIfIndex_Type = InterfaceIndex
_NtnQosIfAssignmentIfIndex_Object = MibTableColumn
ntnQosIfAssignmentIfIndex = _NtnQosIfAssignmentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 1, 1, 1),
    _NtnQosIfAssignmentIfIndex_Type()
)
ntnQosIfAssignmentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosIfAssignmentIfIndex.setStatus("current")
_NtnQosIfAssignmentRoleCombination_Type = RoleCombination
_NtnQosIfAssignmentRoleCombination_Object = MibTableColumn
ntnQosIfAssignmentRoleCombination = _NtnQosIfAssignmentRoleCombination_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 1, 1, 2),
    _NtnQosIfAssignmentRoleCombination_Type()
)
ntnQosIfAssignmentRoleCombination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfAssignmentRoleCombination.setStatus("current")
_NtnQosIfAssignmentQueueSet_Type = Integer32
_NtnQosIfAssignmentQueueSet_Object = MibTableColumn
ntnQosIfAssignmentQueueSet = _NtnQosIfAssignmentQueueSet_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 1, 1, 3),
    _NtnQosIfAssignmentQueueSet_Type()
)
ntnQosIfAssignmentQueueSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfAssignmentQueueSet.setStatus("current")


class _NtnQosIfAssignmentStorage_Type(StorageType):
    """Custom type ntnQosIfAssignmentStorage based on StorageType"""


_NtnQosIfAssignmentStorage_Object = MibTableColumn
ntnQosIfAssignmentStorage = _NtnQosIfAssignmentStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 1, 1, 4),
    _NtnQosIfAssignmentStorage_Type()
)
ntnQosIfAssignmentStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfAssignmentStorage.setStatus("current")
_NtnQosIfAssignmentStatus_Type = RowStatus
_NtnQosIfAssignmentStatus_Object = MibTableColumn
ntnQosIfAssignmentStatus = _NtnQosIfAssignmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 1, 1, 5),
    _NtnQosIfAssignmentStatus_Type()
)
ntnQosIfAssignmentStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfAssignmentStatus.setStatus("current")


class _NtnQosIfAssignmentCapabilities_Type(Bits):
    """Custom type ntnQosIfAssignmentCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("actionIPv6Remarking", 19),
          ("dappSupport", 31),
          ("input802Classification", 3),
          ("inputIpClassification", 1),
          ("inputSystemClassification", 5),
          ("meteringBucket16384K", 29),
          ("meteringBucket512K", 9),
          ("meteringBucket8192K", 10),
          ("meteringGranularity1000Kbps", 12),
          ("meteringGranularity64Kbps", 11),
          ("meteringRate1023", 7),
          ("meteringRate16383", 8),
          ("meteringRate32767", 27),
          ("meteringTypeSimpleTb", 20),
          ("meteringTypeSrTcm", 21),
          ("meteringTypeTrTcm", 22),
          ("other", 0),
          ("output802Classification", 4),
          ("outputIpClassification", 2),
          ("outputSystemClassification", 6),
          ("shapingBucket16384K", 30),
          ("shapingBucket512K", 15),
          ("shapingBucket8192K", 16),
          ("shapingGranularity1000Kbps", 18),
          ("shapingGranularity64Kbps", 17),
          ("shapingRate1023", 13),
          ("shapingRate16383", 14),
          ("shapingRate32767", 28),
          ("shapingTypeCos", 24),
          ("shapingTypeInterface", 23),
          ("version1Caps", 25),
          ("version2Caps", 26))
    )

_NtnQosIfAssignmentCapabilities_Type.__name__ = "Bits"
_NtnQosIfAssignmentCapabilities_Object = MibTableColumn
ntnQosIfAssignmentCapabilities = _NtnQosIfAssignmentCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 1, 1, 6),
    _NtnQosIfAssignmentCapabilities_Type()
)
ntnQosIfAssignmentCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosIfAssignmentCapabilities.setStatus("current")
_NtnQosIfQueueTable_Object = MibTable
ntnQosIfQueueTable = _NtnQosIfQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 2)
)
if mibBuilder.loadTexts:
    ntnQosIfQueueTable.setStatus("current")
_NtnQosIfQueueEntry_Object = MibTableRow
ntnQosIfQueueEntry = _NtnQosIfQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 2, 1)
)
ntnQosIfQueueEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfQueueId"),
)
if mibBuilder.loadTexts:
    ntnQosIfQueueEntry.setStatus("current")
_NtnQosIfQueueId_Type = IndexInteger
_NtnQosIfQueueId_Object = MibTableColumn
ntnQosIfQueueId = _NtnQosIfQueueId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 2, 1, 1),
    _NtnQosIfQueueId_Type()
)
ntnQosIfQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosIfQueueId.setStatus("current")


class _NtnQosIfQueueSetId_Type(Integer32):
    """Custom type ntnQosIfQueueSetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtnQosIfQueueSetId_Type.__name__ = "Integer32"
_NtnQosIfQueueSetId_Object = MibTableColumn
ntnQosIfQueueSetId = _NtnQosIfQueueSetId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 2, 1, 2),
    _NtnQosIfQueueSetId_Type()
)
ntnQosIfQueueSetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfQueueSetId.setStatus("current")


class _NtnQosIfQueueIndex_Type(Integer32):
    """Custom type ntnQosIfQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NtnQosIfQueueIndex_Type.__name__ = "Integer32"
_NtnQosIfQueueIndex_Object = MibTableColumn
ntnQosIfQueueIndex = _NtnQosIfQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 2, 1, 3),
    _NtnQosIfQueueIndex_Type()
)
ntnQosIfQueueIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfQueueIndex.setStatus("current")


class _NtnQosIfQueueDiscipline_Type(Integer32):
    """Custom type ntnQosIfQueueDiscipline based on Integer32"""
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
        *(("fifo", 1),
          ("fq", 3),
          ("pq", 2),
          ("wfq", 4),
          ("wrr", 5))
    )


_NtnQosIfQueueDiscipline_Type.__name__ = "Integer32"
_NtnQosIfQueueDiscipline_Object = MibTableColumn
ntnQosIfQueueDiscipline = _NtnQosIfQueueDiscipline_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 2, 1, 4),
    _NtnQosIfQueueDiscipline_Type()
)
ntnQosIfQueueDiscipline.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfQueueDiscipline.setStatus("current")
_NtnQosIfQueueDrainSize_Type = Unsigned32
_NtnQosIfQueueDrainSize_Object = MibTableColumn
ntnQosIfQueueDrainSize = _NtnQosIfQueueDrainSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 2, 1, 5),
    _NtnQosIfQueueDrainSize_Type()
)
ntnQosIfQueueDrainSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfQueueDrainSize.setStatus("current")
_NtnQosIfQueueAbsBandwidth_Type = Unsigned32
_NtnQosIfQueueAbsBandwidth_Object = MibTableColumn
ntnQosIfQueueAbsBandwidth = _NtnQosIfQueueAbsBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 2, 1, 6),
    _NtnQosIfQueueAbsBandwidth_Type()
)
ntnQosIfQueueAbsBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfQueueAbsBandwidth.setStatus("current")


class _NtnQosIfQueueBandwidthAllocation_Type(Integer32):
    """Custom type ntnQosIfQueueBandwidthAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("relative", 2))
    )


_NtnQosIfQueueBandwidthAllocation_Type.__name__ = "Integer32"
_NtnQosIfQueueBandwidthAllocation_Object = MibTableColumn
ntnQosIfQueueBandwidthAllocation = _NtnQosIfQueueBandwidthAllocation_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 2, 1, 7),
    _NtnQosIfQueueBandwidthAllocation_Type()
)
ntnQosIfQueueBandwidthAllocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfQueueBandwidthAllocation.setStatus("current")


class _NtnQosIfQueueServiceOrder_Type(Integer32):
    """Custom type ntnQosIfQueueServiceOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NtnQosIfQueueServiceOrder_Type.__name__ = "Integer32"
_NtnQosIfQueueServiceOrder_Object = MibTableColumn
ntnQosIfQueueServiceOrder = _NtnQosIfQueueServiceOrder_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 2, 1, 8),
    _NtnQosIfQueueServiceOrder_Type()
)
ntnQosIfQueueServiceOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfQueueServiceOrder.setStatus("current")
_NtnQosIfQueueSize_Type = Unsigned32
_NtnQosIfQueueSize_Object = MibTableColumn
ntnQosIfQueueSize = _NtnQosIfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 2, 1, 9),
    _NtnQosIfQueueSize_Type()
)
ntnQosIfQueueSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfQueueSize.setStatus("current")


class _NtnQosIfQueueStorage_Type(StorageType):
    """Custom type ntnQosIfQueueStorage based on StorageType"""


_NtnQosIfQueueStorage_Object = MibTableColumn
ntnQosIfQueueStorage = _NtnQosIfQueueStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 2, 1, 10),
    _NtnQosIfQueueStorage_Type()
)
ntnQosIfQueueStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfQueueStorage.setStatus("current")
_NtnQosIfQueueStatus_Type = RowStatus
_NtnQosIfQueueStatus_Object = MibTableColumn
ntnQosIfQueueStatus = _NtnQosIfQueueStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 2, 1, 11),
    _NtnQosIfQueueStatus_Type()
)
ntnQosIfQueueStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfQueueStatus.setStatus("current")
_NtnQosInterfaceRoleNextFree_Type = IndexIntegerNextFree
_NtnQosInterfaceRoleNextFree_Object = MibScalar
ntnQosInterfaceRoleNextFree = _NtnQosInterfaceRoleNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 3),
    _NtnQosInterfaceRoleNextFree_Type()
)
ntnQosInterfaceRoleNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosInterfaceRoleNextFree.setStatus("current")
_NtnQosInterfaceRoleTable_Object = MibTable
ntnQosInterfaceRoleTable = _NtnQosInterfaceRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 4)
)
if mibBuilder.loadTexts:
    ntnQosInterfaceRoleTable.setStatus("current")
_NtnQosInterfaceRoleEntry_Object = MibTableRow
ntnQosInterfaceRoleEntry = _NtnQosInterfaceRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 4, 1)
)
ntnQosInterfaceRoleEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosInterfaceRoleId"),
)
if mibBuilder.loadTexts:
    ntnQosInterfaceRoleEntry.setStatus("current")
_NtnQosInterfaceRoleId_Type = IndexInteger
_NtnQosInterfaceRoleId_Object = MibTableColumn
ntnQosInterfaceRoleId = _NtnQosInterfaceRoleId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 4, 1, 1),
    _NtnQosInterfaceRoleId_Type()
)
ntnQosInterfaceRoleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosInterfaceRoleId.setStatus("current")
_NtnQosInterfaceRoleRole_Type = Role
_NtnQosInterfaceRoleRole_Object = MibTableColumn
ntnQosInterfaceRoleRole = _NtnQosInterfaceRoleRole_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 4, 1, 2),
    _NtnQosInterfaceRoleRole_Type()
)
ntnQosInterfaceRoleRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosInterfaceRoleRole.setStatus("current")


class _NtnQosInterfaceRoleIfClass_Type(Integer32):
    """Custom type ntnQosInterfaceRoleIfClass based on Integer32"""
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
        *(("nonTrusted", 2),
          ("trusted", 1),
          ("unrestricted", 3),
          ("untrustedBasic", 5),
          ("untrustedv4v6", 4))
    )


_NtnQosInterfaceRoleIfClass_Type.__name__ = "Integer32"
_NtnQosInterfaceRoleIfClass_Object = MibTableColumn
ntnQosInterfaceRoleIfClass = _NtnQosInterfaceRoleIfClass_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 4, 1, 3),
    _NtnQosInterfaceRoleIfClass_Type()
)
ntnQosInterfaceRoleIfClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosInterfaceRoleIfClass.setStatus("current")


class _NtnQosInterfaceRoleCapabilities_Type(Bits):
    """Custom type ntnQosInterfaceRoleCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("actionIPv6Remarking", 19),
          ("input802Classification", 3),
          ("inputIpClassification", 1),
          ("inputSystemClassification", 5),
          ("meteringBucket16384K", 29),
          ("meteringBucket512K", 9),
          ("meteringBucket8192K", 10),
          ("meteringGranularity1000Kbps", 12),
          ("meteringGranularity64Kbps", 11),
          ("meteringRate1023", 7),
          ("meteringRate16383", 8),
          ("meteringRate32767", 27),
          ("meteringTypeSimpleTb", 20),
          ("meteringTypeSrTcm", 21),
          ("meteringTypeTrTcm", 22),
          ("other", 0),
          ("output802Classification", 4),
          ("outputIpClassification", 2),
          ("outputSystemClassification", 6),
          ("shapingBucket16384K", 30),
          ("shapingBucket512K", 15),
          ("shapingBucket8192K", 16),
          ("shapingGranularity1000Kbps", 18),
          ("shapingGranularity64Kbps", 17),
          ("shapingRate1023", 13),
          ("shapingRate16383", 14),
          ("shapingRate32767", 28),
          ("shapingTypeCos", 24),
          ("shapingTypeInterface", 23),
          ("version1Caps", 25),
          ("version2Caps", 26))
    )

_NtnQosInterfaceRoleCapabilities_Type.__name__ = "Bits"
_NtnQosInterfaceRoleCapabilities_Object = MibTableColumn
ntnQosInterfaceRoleCapabilities = _NtnQosInterfaceRoleCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 4, 1, 4),
    _NtnQosInterfaceRoleCapabilities_Type()
)
ntnQosInterfaceRoleCapabilities.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosInterfaceRoleCapabilities.setStatus("current")


class _NtnQosInterfaceRoleStorageType_Type(StorageType):
    """Custom type ntnQosInterfaceRoleStorageType based on StorageType"""


_NtnQosInterfaceRoleStorageType_Object = MibTableColumn
ntnQosInterfaceRoleStorageType = _NtnQosInterfaceRoleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 4, 1, 5),
    _NtnQosInterfaceRoleStorageType_Type()
)
ntnQosInterfaceRoleStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosInterfaceRoleStorageType.setStatus("current")
_NtnQosInterfaceRoleStatus_Type = RowStatus
_NtnQosInterfaceRoleStatus_Object = MibTableColumn
ntnQosInterfaceRoleStatus = _NtnQosInterfaceRoleStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 4, 1, 6),
    _NtnQosInterfaceRoleStatus_Type()
)
ntnQosInterfaceRoleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosInterfaceRoleStatus.setStatus("current")


class _NtnQosInterfaceRoleStatsTrackingType_Type(Integer32):
    """Custom type ntnQosInterfaceRoleStatsTrackingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 3),
          ("disabled", 1),
          ("individual", 2))
    )


_NtnQosInterfaceRoleStatsTrackingType_Type.__name__ = "Integer32"
_NtnQosInterfaceRoleStatsTrackingType_Object = MibTableColumn
ntnQosInterfaceRoleStatsTrackingType = _NtnQosInterfaceRoleStatsTrackingType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 4, 1, 7),
    _NtnQosInterfaceRoleStatsTrackingType_Type()
)
ntnQosInterfaceRoleStatsTrackingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosInterfaceRoleStatsTrackingType.setStatus("current")
_NtnQosUserRoleTable_Object = MibTable
ntnQosUserRoleTable = _NtnQosUserRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 5)
)
if mibBuilder.loadTexts:
    ntnQosUserRoleTable.setStatus("current")
_NtnQosUserRoleEntry_Object = MibTableRow
ntnQosUserRoleEntry = _NtnQosUserRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 5, 1)
)
ntnQosUserRoleEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserRoleIfIndex"),
)
if mibBuilder.loadTexts:
    ntnQosUserRoleEntry.setStatus("current")
_NtnQosUserRoleIfIndex_Type = InterfaceIndex
_NtnQosUserRoleIfIndex_Object = MibTableColumn
ntnQosUserRoleIfIndex = _NtnQosUserRoleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 5, 1, 1),
    _NtnQosUserRoleIfIndex_Type()
)
ntnQosUserRoleIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosUserRoleIfIndex.setStatus("current")
_NtnQosUserRoleRoleCombination_Type = RoleCombination
_NtnQosUserRoleRoleCombination_Object = MibTableColumn
ntnQosUserRoleRoleCombination = _NtnQosUserRoleRoleCombination_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 5, 1, 2),
    _NtnQosUserRoleRoleCombination_Type()
)
ntnQosUserRoleRoleCombination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosUserRoleRoleCombination.setStatus("current")


class _NtnQosUserRoleUserName_Type(SnmpAdminString):
    """Custom type ntnQosUserRoleUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NtnQosUserRoleUserName_Type.__name__ = "SnmpAdminString"
_NtnQosUserRoleUserName_Object = MibTableColumn
ntnQosUserRoleUserName = _NtnQosUserRoleUserName_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 5, 1, 3),
    _NtnQosUserRoleUserName_Type()
)
ntnQosUserRoleUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosUserRoleUserName.setStatus("current")


class _NtnQosUserRoleUserGroup_Type(SnmpAdminString):
    """Custom type ntnQosUserRoleUserGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtnQosUserRoleUserGroup_Type.__name__ = "SnmpAdminString"
_NtnQosUserRoleUserGroup_Object = MibTableColumn
ntnQosUserRoleUserGroup = _NtnQosUserRoleUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 5, 1, 4),
    _NtnQosUserRoleUserGroup_Type()
)
ntnQosUserRoleUserGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosUserRoleUserGroup.setStatus("current")
_NtnQosUserRoleSessionId_Type = Unsigned32
_NtnQosUserRoleSessionId_Object = MibTableColumn
ntnQosUserRoleSessionId = _NtnQosUserRoleSessionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 5, 1, 5),
    _NtnQosUserRoleSessionId_Type()
)
ntnQosUserRoleSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosUserRoleSessionId.setStatus("current")
_NtnQosUserRoleSessionStart_Type = Unsigned32
_NtnQosUserRoleSessionStart_Object = MibTableColumn
ntnQosUserRoleSessionStart = _NtnQosUserRoleSessionStart_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 5, 1, 6),
    _NtnQosUserRoleSessionStart_Type()
)
ntnQosUserRoleSessionStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosUserRoleSessionStart.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosUserRoleSessionStart.setUnits("seconds")
_NtnQosUserRoleSessionGroup_Type = Unsigned32
_NtnQosUserRoleSessionGroup_Object = MibTableColumn
ntnQosUserRoleSessionGroup = _NtnQosUserRoleSessionGroup_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 5, 1, 7),
    _NtnQosUserRoleSessionGroup_Type()
)
ntnQosUserRoleSessionGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosUserRoleSessionGroup.setStatus("current")


class _NtnQosUserRoleStorage_Type(StorageType):
    """Custom type ntnQosUserRoleStorage based on StorageType"""


_NtnQosUserRoleStorage_Object = MibTableColumn
ntnQosUserRoleStorage = _NtnQosUserRoleStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 5, 1, 8),
    _NtnQosUserRoleStorage_Type()
)
ntnQosUserRoleStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosUserRoleStorage.setStatus("current")
_NtnQosUserRoleStatus_Type = RowStatus
_NtnQosUserRoleStatus_Object = MibTableColumn
ntnQosUserRoleStatus = _NtnQosUserRoleStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 5, 1, 9),
    _NtnQosUserRoleStatus_Type()
)
ntnQosUserRoleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosUserRoleStatus.setStatus("current")
_NtnQosIfShapingTable_Object = MibTable
ntnQosIfShapingTable = _NtnQosIfShapingTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 6)
)
if mibBuilder.loadTexts:
    ntnQosIfShapingTable.setStatus("current")
_NtnQosIfShapingEntry_Object = MibTableRow
ntnQosIfShapingEntry = _NtnQosIfShapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 6, 1)
)
ntnQosIfShapingEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfShapingIfIndex"),
)
if mibBuilder.loadTexts:
    ntnQosIfShapingEntry.setStatus("current")
_NtnQosIfShapingIfIndex_Type = InterfaceIndex
_NtnQosIfShapingIfIndex_Object = MibTableColumn
ntnQosIfShapingIfIndex = _NtnQosIfShapingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 6, 1, 1),
    _NtnQosIfShapingIfIndex_Type()
)
ntnQosIfShapingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosIfShapingIfIndex.setStatus("current")
_NtnQosIfShapingSpecific_Type = RowPointer
_NtnQosIfShapingSpecific_Object = MibTableColumn
ntnQosIfShapingSpecific = _NtnQosIfShapingSpecific_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 6, 1, 2),
    _NtnQosIfShapingSpecific_Type()
)
ntnQosIfShapingSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfShapingSpecific.setStatus("current")


class _NtnQosIfShapingLabel_Type(SnmpAdminString):
    """Custom type ntnQosIfShapingLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtnQosIfShapingLabel_Type.__name__ = "SnmpAdminString"
_NtnQosIfShapingLabel_Object = MibTableColumn
ntnQosIfShapingLabel = _NtnQosIfShapingLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 6, 1, 3),
    _NtnQosIfShapingLabel_Type()
)
ntnQosIfShapingLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfShapingLabel.setStatus("current")


class _NtnQosIfShapingStorage_Type(StorageType):
    """Custom type ntnQosIfShapingStorage based on StorageType"""


_NtnQosIfShapingStorage_Object = MibTableColumn
ntnQosIfShapingStorage = _NtnQosIfShapingStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 6, 1, 4),
    _NtnQosIfShapingStorage_Type()
)
ntnQosIfShapingStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfShapingStorage.setStatus("current")
_NtnQosIfShapingStatus_Type = RowStatus
_NtnQosIfShapingStatus_Object = MibTableColumn
ntnQosIfShapingStatus = _NtnQosIfShapingStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 6, 1, 5),
    _NtnQosIfShapingStatus_Type()
)
ntnQosIfShapingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfShapingStatus.setStatus("current")
_NtnQosCosShapingTable_Object = MibTable
ntnQosCosShapingTable = _NtnQosCosShapingTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 7)
)
if mibBuilder.loadTexts:
    ntnQosCosShapingTable.setStatus("current")
_NtnQosCosShapingEntry_Object = MibTableRow
ntnQosCosShapingEntry = _NtnQosCosShapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 7, 1)
)
ntnQosCosShapingEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosCosShapingIfIndex"),
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosCosShapingCos"),
)
if mibBuilder.loadTexts:
    ntnQosCosShapingEntry.setStatus("current")
_NtnQosCosShapingIfIndex_Type = InterfaceIndex
_NtnQosCosShapingIfIndex_Object = MibTableColumn
ntnQosCosShapingIfIndex = _NtnQosCosShapingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 7, 1, 1),
    _NtnQosCosShapingIfIndex_Type()
)
ntnQosCosShapingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosCosShapingIfIndex.setStatus("current")
_NtnQosCosShapingCos_Type = QosIeee802Cos
_NtnQosCosShapingCos_Object = MibTableColumn
ntnQosCosShapingCos = _NtnQosCosShapingCos_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 7, 1, 2),
    _NtnQosCosShapingCos_Type()
)
ntnQosCosShapingCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosCosShapingCos.setStatus("current")
_NtnQosCosShapingSpecific_Type = RowPointer
_NtnQosCosShapingSpecific_Object = MibTableColumn
ntnQosCosShapingSpecific = _NtnQosCosShapingSpecific_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 7, 1, 3),
    _NtnQosCosShapingSpecific_Type()
)
ntnQosCosShapingSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosCosShapingSpecific.setStatus("current")


class _NtnQosCosShapingLabel_Type(SnmpAdminString):
    """Custom type ntnQosCosShapingLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtnQosCosShapingLabel_Type.__name__ = "SnmpAdminString"
_NtnQosCosShapingLabel_Object = MibTableColumn
ntnQosCosShapingLabel = _NtnQosCosShapingLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 7, 1, 4),
    _NtnQosCosShapingLabel_Type()
)
ntnQosCosShapingLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosCosShapingLabel.setStatus("current")


class _NtnQosCosShapingStorage_Type(StorageType):
    """Custom type ntnQosCosShapingStorage based on StorageType"""


_NtnQosCosShapingStorage_Object = MibTableColumn
ntnQosCosShapingStorage = _NtnQosCosShapingStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 7, 1, 5),
    _NtnQosCosShapingStorage_Type()
)
ntnQosCosShapingStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosCosShapingStorage.setStatus("current")
_NtnQosCosShapingStatus_Type = RowStatus
_NtnQosCosShapingStatus_Object = MibTableColumn
ntnQosCosShapingStatus = _NtnQosCosShapingStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 7, 1, 6),
    _NtnQosCosShapingStatus_Type()
)
ntnQosCosShapingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosCosShapingStatus.setStatus("current")
_NtnQosQueueShapingTable_Object = MibTable
ntnQosQueueShapingTable = _NtnQosQueueShapingTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 8)
)
if mibBuilder.loadTexts:
    ntnQosQueueShapingTable.setStatus("current")
_NtnQosQueueShapingEntry_Object = MibTableRow
ntnQosQueueShapingEntry = _NtnQosQueueShapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 8, 1)
)
ntnQosQueueShapingEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosQueueShapingIfIndex"),
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosQueueShapingQueue"),
)
if mibBuilder.loadTexts:
    ntnQosQueueShapingEntry.setStatus("current")
_NtnQosQueueShapingIfIndex_Type = InterfaceIndex
_NtnQosQueueShapingIfIndex_Object = MibTableColumn
ntnQosQueueShapingIfIndex = _NtnQosQueueShapingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 8, 1, 1),
    _NtnQosQueueShapingIfIndex_Type()
)
ntnQosQueueShapingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosQueueShapingIfIndex.setStatus("current")


class _NtnQosQueueShapingQueue_Type(Integer32):
    """Custom type ntnQosQueueShapingQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NtnQosQueueShapingQueue_Type.__name__ = "Integer32"
_NtnQosQueueShapingQueue_Object = MibTableColumn
ntnQosQueueShapingQueue = _NtnQosQueueShapingQueue_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 8, 1, 2),
    _NtnQosQueueShapingQueue_Type()
)
ntnQosQueueShapingQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosQueueShapingQueue.setStatus("current")
_NtnQosQueueShapingSpecific_Type = RowPointer
_NtnQosQueueShapingSpecific_Object = MibTableColumn
ntnQosQueueShapingSpecific = _NtnQosQueueShapingSpecific_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 8, 1, 3),
    _NtnQosQueueShapingSpecific_Type()
)
ntnQosQueueShapingSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosQueueShapingSpecific.setStatus("current")


class _NtnQosQueueShapingLabel_Type(SnmpAdminString):
    """Custom type ntnQosQueueShapingLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtnQosQueueShapingLabel_Type.__name__ = "SnmpAdminString"
_NtnQosQueueShapingLabel_Object = MibTableColumn
ntnQosQueueShapingLabel = _NtnQosQueueShapingLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 8, 1, 4),
    _NtnQosQueueShapingLabel_Type()
)
ntnQosQueueShapingLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosQueueShapingLabel.setStatus("current")


class _NtnQosQueueShapingStorage_Type(StorageType):
    """Custom type ntnQosQueueShapingStorage based on StorageType"""


_NtnQosQueueShapingStorage_Object = MibTableColumn
ntnQosQueueShapingStorage = _NtnQosQueueShapingStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 8, 1, 5),
    _NtnQosQueueShapingStorage_Type()
)
ntnQosQueueShapingStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosQueueShapingStorage.setStatus("current")
_NtnQosQueueShapingStatus_Type = RowStatus
_NtnQosQueueShapingStatus_Object = MibTableColumn
ntnQosQueueShapingStatus = _NtnQosQueueShapingStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 9, 8, 1, 6),
    _NtnQosQueueShapingStatus_Type()
)
ntnQosQueueShapingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosQueueShapingStatus.setStatus("current")
_NtnQosMappingClasses_ObjectIdentity = ObjectIdentity
ntnQosMappingClasses = _NtnQosMappingClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10)
)
_NtnQosDscpToCosTable_Object = MibTable
ntnQosDscpToCosTable = _NtnQosDscpToCosTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 1)
)
if mibBuilder.loadTexts:
    ntnQosDscpToCosTable.setStatus("current")
_NtnQosDscpToCosEntry_Object = MibTableRow
ntnQosDscpToCosEntry = _NtnQosDscpToCosEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 1, 1)
)
ntnQosDscpToCosEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosDscpToCosId"),
)
if mibBuilder.loadTexts:
    ntnQosDscpToCosEntry.setStatus("current")
_NtnQosDscpToCosId_Type = IndexInteger
_NtnQosDscpToCosId_Object = MibTableColumn
ntnQosDscpToCosId = _NtnQosDscpToCosId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 1, 1, 1),
    _NtnQosDscpToCosId_Type()
)
ntnQosDscpToCosId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosDscpToCosId.setStatus("current")
_NtnQosDscpToCosDscp_Type = Dscp
_NtnQosDscpToCosDscp_Object = MibTableColumn
ntnQosDscpToCosDscp = _NtnQosDscpToCosDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 1, 1, 2),
    _NtnQosDscpToCosDscp_Type()
)
ntnQosDscpToCosDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDscpToCosDscp.setStatus("current")
_NtnQosDscpToCosCos_Type = QosIeee802Cos
_NtnQosDscpToCosCos_Object = MibTableColumn
ntnQosDscpToCosCos = _NtnQosDscpToCosCos_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 1, 1, 3),
    _NtnQosDscpToCosCos_Type()
)
ntnQosDscpToCosCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDscpToCosCos.setStatus("current")


class _NtnQosDscpToCosDropPrec_Type(Integer32):
    """Custom type ntnQosDscpToCosDropPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highDropPrec", 2),
          ("lowDropPrec", 1))
    )


_NtnQosDscpToCosDropPrec_Type.__name__ = "Integer32"
_NtnQosDscpToCosDropPrec_Object = MibTableColumn
ntnQosDscpToCosDropPrec = _NtnQosDscpToCosDropPrec_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 1, 1, 4),
    _NtnQosDscpToCosDropPrec_Type()
)
ntnQosDscpToCosDropPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDscpToCosDropPrec.setStatus("current")


class _NtnQosDscpToCosLabel_Type(SnmpAdminString):
    """Custom type ntnQosDscpToCosLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtnQosDscpToCosLabel_Type.__name__ = "SnmpAdminString"
_NtnQosDscpToCosLabel_Object = MibTableColumn
ntnQosDscpToCosLabel = _NtnQosDscpToCosLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 1, 1, 5),
    _NtnQosDscpToCosLabel_Type()
)
ntnQosDscpToCosLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDscpToCosLabel.setStatus("current")


class _NtnQosDscpToCosStorage_Type(StorageType):
    """Custom type ntnQosDscpToCosStorage based on StorageType"""


_NtnQosDscpToCosStorage_Object = MibTableColumn
ntnQosDscpToCosStorage = _NtnQosDscpToCosStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 1, 1, 6),
    _NtnQosDscpToCosStorage_Type()
)
ntnQosDscpToCosStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDscpToCosStorage.setStatus("current")
_NtnQosDscpToCosStatus_Type = RowStatus
_NtnQosDscpToCosStatus_Object = MibTableColumn
ntnQosDscpToCosStatus = _NtnQosDscpToCosStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 1, 1, 7),
    _NtnQosDscpToCosStatus_Type()
)
ntnQosDscpToCosStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDscpToCosStatus.setStatus("current")
_NtnQosDscpToCosNewDscp_Type = Dscp
_NtnQosDscpToCosNewDscp_Object = MibTableColumn
ntnQosDscpToCosNewDscp = _NtnQosDscpToCosNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 1, 1, 8),
    _NtnQosDscpToCosNewDscp_Type()
)
ntnQosDscpToCosNewDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDscpToCosNewDscp.setStatus("current")
_NtnQosCosToDscpTable_Object = MibTable
ntnQosCosToDscpTable = _NtnQosCosToDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 2)
)
if mibBuilder.loadTexts:
    ntnQosCosToDscpTable.setStatus("current")
_NtnQosCosToDscpEntry_Object = MibTableRow
ntnQosCosToDscpEntry = _NtnQosCosToDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 2, 1)
)
ntnQosCosToDscpEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosCosToDscpId"),
)
if mibBuilder.loadTexts:
    ntnQosCosToDscpEntry.setStatus("current")
_NtnQosCosToDscpId_Type = IndexInteger
_NtnQosCosToDscpId_Object = MibTableColumn
ntnQosCosToDscpId = _NtnQosCosToDscpId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 2, 1, 1),
    _NtnQosCosToDscpId_Type()
)
ntnQosCosToDscpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosCosToDscpId.setStatus("current")
_NtnQosCosToDscpCos_Type = QosIeee802Cos
_NtnQosCosToDscpCos_Object = MibTableColumn
ntnQosCosToDscpCos = _NtnQosCosToDscpCos_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 2, 1, 2),
    _NtnQosCosToDscpCos_Type()
)
ntnQosCosToDscpCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosCosToDscpCos.setStatus("current")
_NtnQosCosToDscpDscp_Type = Dscp
_NtnQosCosToDscpDscp_Object = MibTableColumn
ntnQosCosToDscpDscp = _NtnQosCosToDscpDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 2, 1, 3),
    _NtnQosCosToDscpDscp_Type()
)
ntnQosCosToDscpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosCosToDscpDscp.setStatus("current")


class _NtnQosCosToDscpLabel_Type(SnmpAdminString):
    """Custom type ntnQosCosToDscpLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtnQosCosToDscpLabel_Type.__name__ = "SnmpAdminString"
_NtnQosCosToDscpLabel_Object = MibTableColumn
ntnQosCosToDscpLabel = _NtnQosCosToDscpLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 2, 1, 4),
    _NtnQosCosToDscpLabel_Type()
)
ntnQosCosToDscpLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosCosToDscpLabel.setStatus("current")


class _NtnQosCosToDscpStorage_Type(StorageType):
    """Custom type ntnQosCosToDscpStorage based on StorageType"""


_NtnQosCosToDscpStorage_Object = MibTableColumn
ntnQosCosToDscpStorage = _NtnQosCosToDscpStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 2, 1, 5),
    _NtnQosCosToDscpStorage_Type()
)
ntnQosCosToDscpStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosCosToDscpStorage.setStatus("current")
_NtnQosCosToDscpStatus_Type = RowStatus
_NtnQosCosToDscpStatus_Object = MibTableColumn
ntnQosCosToDscpStatus = _NtnQosCosToDscpStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 2, 1, 6),
    _NtnQosCosToDscpStatus_Type()
)
ntnQosCosToDscpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosCosToDscpStatus.setStatus("current")
_NtnQosMappingClassesScalars_ObjectIdentity = ObjectIdentity
ntnQosMappingClassesScalars = _NtnQosMappingClassesScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 3)
)


class _NtnQosMappingRestoreDefault_Type(Integer32):
    """Custom type ntnQosMappingRestoreDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cosToDscp", 3),
          ("dscpToCos", 2),
          ("other", 1))
    )


_NtnQosMappingRestoreDefault_Type.__name__ = "Integer32"
_NtnQosMappingRestoreDefault_Object = MibScalar
ntnQosMappingRestoreDefault = _NtnQosMappingRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 3, 1),
    _NtnQosMappingRestoreDefault_Type()
)
ntnQosMappingRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosMappingRestoreDefault.setStatus("current")
_NtnQosMappingDscpToCosEnabled_Type = TruthValue
_NtnQosMappingDscpToCosEnabled_Object = MibScalar
ntnQosMappingDscpToCosEnabled = _NtnQosMappingDscpToCosEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 3, 2),
    _NtnQosMappingDscpToCosEnabled_Type()
)
ntnQosMappingDscpToCosEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosMappingDscpToCosEnabled.setStatus("current")
_NtnQosMappingCosToDscpEnabled_Type = TruthValue
_NtnQosMappingCosToDscpEnabled_Object = MibScalar
ntnQosMappingCosToDscpEnabled = _NtnQosMappingCosToDscpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 10, 3, 3),
    _NtnQosMappingCosToDscpEnabled_Type()
)
ntnQosMappingCosToDscpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosMappingCosToDscpEnabled.setStatus("current")
_NtnQosPolicyAgtClasses_ObjectIdentity = ObjectIdentity
ntnQosPolicyAgtClasses = _NtnQosPolicyAgtClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11)
)
_NtnQosPrcSupportTable_Object = MibTable
ntnQosPrcSupportTable = _NtnQosPrcSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 1)
)
if mibBuilder.loadTexts:
    ntnQosPrcSupportTable.setStatus("current")
_NtnQosPrcSupportEntry_Object = MibTableRow
ntnQosPrcSupportEntry = _NtnQosPrcSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 1, 1)
)
ntnQosPrcSupportEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosPrcSupportId"),
)
if mibBuilder.loadTexts:
    ntnQosPrcSupportEntry.setStatus("current")
_NtnQosPrcSupportId_Type = IndexInteger
_NtnQosPrcSupportId_Object = MibTableColumn
ntnQosPrcSupportId = _NtnQosPrcSupportId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 1, 1, 1),
    _NtnQosPrcSupportId_Type()
)
ntnQosPrcSupportId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosPrcSupportId.setStatus("current")
_NtnQosPrcSupportSupportedPrc_Type = ObjectIdentifier
_NtnQosPrcSupportSupportedPrc_Object = MibTableColumn
ntnQosPrcSupportSupportedPrc = _NtnQosPrcSupportSupportedPrc_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 1, 1, 2),
    _NtnQosPrcSupportSupportedPrc_Type()
)
ntnQosPrcSupportSupportedPrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPrcSupportSupportedPrc.setStatus("current")


class _NtnQosPrcSupportSupportedAttrs_Type(OctetString):
    """Custom type ntnQosPrcSupportSupportedAttrs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_NtnQosPrcSupportSupportedAttrs_Type.__name__ = "OctetString"
_NtnQosPrcSupportSupportedAttrs_Object = MibTableColumn
ntnQosPrcSupportSupportedAttrs = _NtnQosPrcSupportSupportedAttrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 1, 1, 3),
    _NtnQosPrcSupportSupportedAttrs_Type()
)
ntnQosPrcSupportSupportedAttrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPrcSupportSupportedAttrs.setStatus("current")
_NtnQosPrcSupportMaxPris_Type = Unsigned32
_NtnQosPrcSupportMaxPris_Object = MibTableColumn
ntnQosPrcSupportMaxPris = _NtnQosPrcSupportMaxPris_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 1, 1, 4),
    _NtnQosPrcSupportMaxPris_Type()
)
ntnQosPrcSupportMaxPris.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPrcSupportMaxPris.setStatus("current")
_NtnQosPrcSupportCurrentPris_Type = Unsigned32
_NtnQosPrcSupportCurrentPris_Object = MibTableColumn
ntnQosPrcSupportCurrentPris = _NtnQosPrcSupportCurrentPris_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 1, 1, 5),
    _NtnQosPrcSupportCurrentPris_Type()
)
ntnQosPrcSupportCurrentPris.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPrcSupportCurrentPris.setStatus("current")
_NtnQosPolicyDeviceIdentTable_Object = MibTable
ntnQosPolicyDeviceIdentTable = _NtnQosPolicyDeviceIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 2)
)
if mibBuilder.loadTexts:
    ntnQosPolicyDeviceIdentTable.setStatus("current")
_NtnQosPolicyDeviceIdentEntry_Object = MibTableRow
ntnQosPolicyDeviceIdentEntry = _NtnQosPolicyDeviceIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 2, 1)
)
ntnQosPolicyDeviceIdentEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyDeviceIdentId"),
)
if mibBuilder.loadTexts:
    ntnQosPolicyDeviceIdentEntry.setStatus("current")
_NtnQosPolicyDeviceIdentId_Type = IndexInteger
_NtnQosPolicyDeviceIdentId_Object = MibTableColumn
ntnQosPolicyDeviceIdentId = _NtnQosPolicyDeviceIdentId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 2, 1, 1),
    _NtnQosPolicyDeviceIdentId_Type()
)
ntnQosPolicyDeviceIdentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosPolicyDeviceIdentId.setStatus("current")


class _NtnQosPolicyDeviceIdentDescr_Type(SnmpAdminString):
    """Custom type ntnQosPolicyDeviceIdentDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtnQosPolicyDeviceIdentDescr_Type.__name__ = "SnmpAdminString"
_NtnQosPolicyDeviceIdentDescr_Object = MibTableColumn
ntnQosPolicyDeviceIdentDescr = _NtnQosPolicyDeviceIdentDescr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 2, 1, 2),
    _NtnQosPolicyDeviceIdentDescr_Type()
)
ntnQosPolicyDeviceIdentDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyDeviceIdentDescr.setStatus("current")
_NtnQosPolicyDeviceIdentMaxMsg_Type = Unsigned32
_NtnQosPolicyDeviceIdentMaxMsg_Object = MibTableColumn
ntnQosPolicyDeviceIdentMaxMsg = _NtnQosPolicyDeviceIdentMaxMsg_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 2, 1, 3),
    _NtnQosPolicyDeviceIdentMaxMsg_Type()
)
ntnQosPolicyDeviceIdentMaxMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosPolicyDeviceIdentMaxMsg.setStatus("current")
_NtnQosConfigResetToDefaults_Type = TruthValue
_NtnQosConfigResetToDefaults_Object = MibScalar
ntnQosConfigResetToDefaults = _NtnQosConfigResetToDefaults_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 3),
    _NtnQosConfigResetToDefaults_Type()
)
ntnQosConfigResetToDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigResetToDefaults.setStatus("current")


class _NtnQosConfigTrackStatistics_Type(Integer32):
    """Custom type ntnQosConfigTrackStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 3),
          ("disabled", 1),
          ("individual", 2))
    )


_NtnQosConfigTrackStatistics_Type.__name__ = "Integer32"
_NtnQosConfigTrackStatistics_Object = MibScalar
ntnQosConfigTrackStatistics = _NtnQosConfigTrackStatistics_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 4),
    _NtnQosConfigTrackStatistics_Type()
)
ntnQosConfigTrackStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigTrackStatistics.setStatus("current")
_NtnQosConfigNVCommitDelay_Type = Unsigned32
_NtnQosConfigNVCommitDelay_Object = MibScalar
ntnQosConfigNVCommitDelay = _NtnQosConfigNVCommitDelay_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 5),
    _NtnQosConfigNVCommitDelay_Type()
)
ntnQosConfigNVCommitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigNVCommitDelay.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosConfigNVCommitDelay.setUnits("seconds")


class _NtnQosConfigDefaultQueueCfg_Type(Integer32):
    """Custom type ntnQosConfigDefaultQueueCfg based on Integer32"""
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
        *(("queueSetEight", 8),
          ("queueSetFive", 5),
          ("queueSetFour", 4),
          ("queueSetOne", 1),
          ("queueSetSeven", 7),
          ("queueSetSix", 6),
          ("queueSetThree", 3),
          ("queueSetTwo", 2))
    )


_NtnQosConfigDefaultQueueCfg_Type.__name__ = "Integer32"
_NtnQosConfigDefaultQueueCfg_Object = MibScalar
ntnQosConfigDefaultQueueCfg = _NtnQosConfigDefaultQueueCfg_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 6),
    _NtnQosConfigDefaultQueueCfg_Type()
)
ntnQosConfigDefaultQueueCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigDefaultQueueCfg.setStatus("current")


class _NtnQosConfigDefaultBufferingCaps_Type(Integer32):
    """Custom type ntnQosConfigDefaultBufferingCaps based on Integer32"""
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
        *(("lossless", 4),
          ("losslessPfc", 5),
          ("maximumOverAllocation", 3),
          ("mediumOverAllocation", 2),
          ("minimumOverAllocation", 1),
          ("spb-scaled", 6))
    )


_NtnQosConfigDefaultBufferingCaps_Type.__name__ = "Integer32"
_NtnQosConfigDefaultBufferingCaps_Object = MibScalar
ntnQosConfigDefaultBufferingCaps = _NtnQosConfigDefaultBufferingCaps_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 7),
    _NtnQosConfigDefaultBufferingCaps_Type()
)
ntnQosConfigDefaultBufferingCaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigDefaultBufferingCaps.setStatus("current")


class _NtnQosConfigUBPSupportLevel_Type(Integer32):
    """Custom type ntnQosConfigUBPSupportLevel based on Integer32"""
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
        *(("ubpSupportDisabled", 1),
          ("ubpSupportEPMData", 4),
          ("ubpSupportHighSecurityLocalData", 2),
          ("ubpSupportLowSecurityLocalData", 3))
    )


_NtnQosConfigUBPSupportLevel_Type.__name__ = "Integer32"
_NtnQosConfigUBPSupportLevel_Object = MibScalar
ntnQosConfigUBPSupportLevel = _NtnQosConfigUBPSupportLevel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 8),
    _NtnQosConfigUBPSupportLevel_Type()
)
ntnQosConfigUBPSupportLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigUBPSupportLevel.setStatus("current")


class _NtnQosConfigRoleAssocCompatLevel_Type(Integer32):
    """Custom type ntnQosConfigRoleAssocCompatLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("roleAssocCompatLoose", 1),
          ("roleAssocCompatStrict", 2))
    )


_NtnQosConfigRoleAssocCompatLevel_Type.__name__ = "Integer32"
_NtnQosConfigRoleAssocCompatLevel_Object = MibScalar
ntnQosConfigRoleAssocCompatLevel = _NtnQosConfigRoleAssocCompatLevel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 9),
    _NtnQosConfigRoleAssocCompatLevel_Type()
)
ntnQosConfigRoleAssocCompatLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigRoleAssocCompatLevel.setStatus("current")


class _NtnQosConfigDappEnable_Type(Integer32):
    """Custom type ntnQosConfigDappEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enableWithStatusTracking", 3),
          ("enableWithoutStatusTracking", 2))
    )


_NtnQosConfigDappEnable_Type.__name__ = "Integer32"
_NtnQosConfigDappEnable_Object = MibScalar
ntnQosConfigDappEnable = _NtnQosConfigDappEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 10),
    _NtnQosConfigDappEnable_Type()
)
ntnQosConfigDappEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigDappEnable.setStatus("current")


class _NtnQosConfigDappMinTcpHdrSize_Type(Integer32):
    """Custom type ntnQosConfigDappMinTcpHdrSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NtnQosConfigDappMinTcpHdrSize_Type.__name__ = "Integer32"
_NtnQosConfigDappMinTcpHdrSize_Object = MibScalar
ntnQosConfigDappMinTcpHdrSize = _NtnQosConfigDappMinTcpHdrSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 11),
    _NtnQosConfigDappMinTcpHdrSize_Type()
)
ntnQosConfigDappMinTcpHdrSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigDappMinTcpHdrSize.setStatus("current")


class _NtnQosConfigDappIpv4IcmpMaxLength_Type(Integer32):
    """Custom type ntnQosConfigDappIpv4IcmpMaxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_NtnQosConfigDappIpv4IcmpMaxLength_Type.__name__ = "Integer32"
_NtnQosConfigDappIpv4IcmpMaxLength_Object = MibScalar
ntnQosConfigDappIpv4IcmpMaxLength = _NtnQosConfigDappIpv4IcmpMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 12),
    _NtnQosConfigDappIpv4IcmpMaxLength_Type()
)
ntnQosConfigDappIpv4IcmpMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigDappIpv4IcmpMaxLength.setStatus("current")


class _NtnQosConfigDappIpv6IcmpMaxLength_Type(Integer32):
    """Custom type ntnQosConfigDappIpv6IcmpMaxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_NtnQosConfigDappIpv6IcmpMaxLength_Type.__name__ = "Integer32"
_NtnQosConfigDappIpv6IcmpMaxLength_Object = MibScalar
ntnQosConfigDappIpv6IcmpMaxLength = _NtnQosConfigDappIpv6IcmpMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 13),
    _NtnQosConfigDappIpv6IcmpMaxLength_Type()
)
ntnQosConfigDappIpv6IcmpMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigDappIpv6IcmpMaxLength.setStatus("current")


class _NtnQosConfigNtApplicationMode_Type(Integer32):
    """Custom type ntnQosConfigNtApplicationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enableMixedMode", 3),
          ("enablePureMode", 2))
    )


_NtnQosConfigNtApplicationMode_Type.__name__ = "Integer32"
_NtnQosConfigNtApplicationMode_Object = MibScalar
ntnQosConfigNtApplicationMode = _NtnQosConfigNtApplicationMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 14),
    _NtnQosConfigNtApplicationMode_Type()
)
ntnQosConfigNtApplicationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigNtApplicationMode.setStatus("current")


class _NtnQosConfigQosOperMode_Type(Integer32):
    """Custom type ntnQosConfigQosOperMode based on Integer32"""
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


_NtnQosConfigQosOperMode_Type.__name__ = "Integer32"
_NtnQosConfigQosOperMode_Object = MibScalar
ntnQosConfigQosOperMode = _NtnQosConfigQosOperMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 15),
    _NtnQosConfigQosOperMode_Type()
)
ntnQosConfigQosOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigQosOperMode.setStatus("current")


class _NtnQosConfigTrustedProcessingMode_Type(Integer32):
    """Custom type ntnQosConfigTrustedProcessingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDscpMapping", 2),
          ("partialDscpMapping", 1))
    )


_NtnQosConfigTrustedProcessingMode_Type.__name__ = "Integer32"
_NtnQosConfigTrustedProcessingMode_Object = MibScalar
ntnQosConfigTrustedProcessingMode = _NtnQosConfigTrustedProcessingMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 16),
    _NtnQosConfigTrustedProcessingMode_Type()
)
ntnQosConfigTrustedProcessingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigTrustedProcessingMode.setStatus("current")
_NtnQosConfigResetToPartialDefaults_Type = TruthValue
_NtnQosConfigResetToPartialDefaults_Object = MibScalar
ntnQosConfigResetToPartialDefaults = _NtnQosConfigResetToPartialDefaults_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 17),
    _NtnQosConfigResetToPartialDefaults_Type()
)
ntnQosConfigResetToPartialDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigResetToPartialDefaults.setStatus("current")
_NtnQosConfigClearStats_Type = TruthValue
_NtnQosConfigClearStats_Object = MibScalar
ntnQosConfigClearStats = _NtnQosConfigClearStats_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 18),
    _NtnQosConfigClearStats_Type()
)
ntnQosConfigClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigClearStats.setStatus("current")


class _NtnQosConfigFcoeRedirOperMode_Type(Integer32):
    """Custom type ntnQosConfigFcoeRedirOperMode based on Integer32"""
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


_NtnQosConfigFcoeRedirOperMode_Type.__name__ = "Integer32"
_NtnQosConfigFcoeRedirOperMode_Object = MibScalar
ntnQosConfigFcoeRedirOperMode = _NtnQosConfigFcoeRedirOperMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 19),
    _NtnQosConfigFcoeRedirOperMode_Type()
)
ntnQosConfigFcoeRedirOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigFcoeRedirOperMode.setStatus("current")
_NtnQosConfigFcoeControllerMacAddr_Type = MacAddress
_NtnQosConfigFcoeControllerMacAddr_Object = MibScalar
ntnQosConfigFcoeControllerMacAddr = _NtnQosConfigFcoeControllerMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 20),
    _NtnQosConfigFcoeControllerMacAddr_Type()
)
ntnQosConfigFcoeControllerMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigFcoeControllerMacAddr.setStatus("current")


class _NtnQosConfigFcoeRedirAvail_Type(Integer32):
    """Custom type ntnQosConfigFcoeRedirAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accessible", 1),
          ("notAccessible", 2))
    )


_NtnQosConfigFcoeRedirAvail_Type.__name__ = "Integer32"
_NtnQosConfigFcoeRedirAvail_Object = MibScalar
ntnQosConfigFcoeRedirAvail = _NtnQosConfigFcoeRedirAvail_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 21),
    _NtnQosConfigFcoeRedirAvail_Type()
)
ntnQosConfigFcoeRedirAvail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigFcoeRedirAvail.setStatus("current")
_NtnQosConfigFcoeControllerIfIndex_Type = InterfaceIndexOrZero
_NtnQosConfigFcoeControllerIfIndex_Object = MibScalar
ntnQosConfigFcoeControllerIfIndex = _NtnQosConfigFcoeControllerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 22),
    _NtnQosConfigFcoeControllerIfIndex_Type()
)
ntnQosConfigFcoeControllerIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigFcoeControllerIfIndex.setStatus("current")


class _NtnQosConfigFcoeControllerVlan_Type(Integer32):
    """Custom type ntnQosConfigFcoeControllerVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_NtnQosConfigFcoeControllerVlan_Type.__name__ = "Integer32"
_NtnQosConfigFcoeControllerVlan_Object = MibScalar
ntnQosConfigFcoeControllerVlan = _NtnQosConfigFcoeControllerVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 11, 23),
    _NtnQosConfigFcoeControllerVlan_Type()
)
ntnQosConfigFcoeControllerVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosConfigFcoeControllerVlan.setStatus("current")
_NtnQosInterfaceTypeNextFree_Type = IndexIntegerNextFree
_NtnQosInterfaceTypeNextFree_Object = MibScalar
ntnQosInterfaceTypeNextFree = _NtnQosInterfaceTypeNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 12),
    _NtnQosInterfaceTypeNextFree_Type()
)
ntnQosInterfaceTypeNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosInterfaceTypeNextFree.setStatus("current")
_NtnQosApplicationClasses_ObjectIdentity = ObjectIdentity
ntnQosApplicationClasses = _NtnQosApplicationClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13)
)
_NtnQosDsAccessElemNextFree_Type = IndexIntegerNextFree
_NtnQosDsAccessElemNextFree_Object = MibScalar
ntnQosDsAccessElemNextFree = _NtnQosDsAccessElemNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 1),
    _NtnQosDsAccessElemNextFree_Type()
)
ntnQosDsAccessElemNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemNextFree.setStatus("current")
_NtnQosDsAccessElemTable_Object = MibTable
ntnQosDsAccessElemTable = _NtnQosDsAccessElemTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2)
)
if mibBuilder.loadTexts:
    ntnQosDsAccessElemTable.setStatus("current")
_NtnQosDsAccessElemEntry_Object = MibTableRow
ntnQosDsAccessElemEntry = _NtnQosDsAccessElemEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1)
)
ntnQosDsAccessElemEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemId"),
)
if mibBuilder.loadTexts:
    ntnQosDsAccessElemEntry.setStatus("current")
_NtnQosDsAccessElemId_Type = IndexInteger
_NtnQosDsAccessElemId_Object = MibTableColumn
ntnQosDsAccessElemId = _NtnQosDsAccessElemId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 1),
    _NtnQosDsAccessElemId_Type()
)
ntnQosDsAccessElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemId.setStatus("current")


class _NtnQosDsAccessElemAddrType_Type(InetAddressType):
    """Custom type ntnQosDsAccessElemAddrType based on InetAddressType"""


_NtnQosDsAccessElemAddrType_Object = MibTableColumn
ntnQosDsAccessElemAddrType = _NtnQosDsAccessElemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 2),
    _NtnQosDsAccessElemAddrType_Type()
)
ntnQosDsAccessElemAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemAddrType.setStatus("current")


class _NtnQosDsAccessElemDstAddr_Type(InetAddress):
    """Custom type ntnQosDsAccessElemDstAddr based on InetAddress"""
    defaultHexValue = "00000000"


_NtnQosDsAccessElemDstAddr_Object = MibTableColumn
ntnQosDsAccessElemDstAddr = _NtnQosDsAccessElemDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 3),
    _NtnQosDsAccessElemDstAddr_Type()
)
ntnQosDsAccessElemDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemDstAddr.setStatus("current")


class _NtnQosDsAccessElemDstPrefixLength_Type(InetAddressPrefixLength):
    """Custom type ntnQosDsAccessElemDstPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_NtnQosDsAccessElemDstPrefixLength_Object = MibTableColumn
ntnQosDsAccessElemDstPrefixLength = _NtnQosDsAccessElemDstPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 4),
    _NtnQosDsAccessElemDstPrefixLength_Type()
)
ntnQosDsAccessElemDstPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemDstPrefixLength.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemDstPrefixLength.setUnits("bits")


class _NtnQosDsAccessElemSrcAddr_Type(InetAddress):
    """Custom type ntnQosDsAccessElemSrcAddr based on InetAddress"""
    defaultHexValue = "00000000"


_NtnQosDsAccessElemSrcAddr_Object = MibTableColumn
ntnQosDsAccessElemSrcAddr = _NtnQosDsAccessElemSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 5),
    _NtnQosDsAccessElemSrcAddr_Type()
)
ntnQosDsAccessElemSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemSrcAddr.setStatus("current")


class _NtnQosDsAccessElemSrcPrefixLength_Type(InetAddressPrefixLength):
    """Custom type ntnQosDsAccessElemSrcPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_NtnQosDsAccessElemSrcPrefixLength_Object = MibTableColumn
ntnQosDsAccessElemSrcPrefixLength = _NtnQosDsAccessElemSrcPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 6),
    _NtnQosDsAccessElemSrcPrefixLength_Type()
)
ntnQosDsAccessElemSrcPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemSrcPrefixLength.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemSrcPrefixLength.setUnits("bits")


class _NtnQosDsAccessElemDscp_Type(DscpOrAny):
    """Custom type ntnQosDsAccessElemDscp based on DscpOrAny"""
    defaultValue = -1


_NtnQosDsAccessElemDscp_Object = MibTableColumn
ntnQosDsAccessElemDscp = _NtnQosDsAccessElemDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 7),
    _NtnQosDsAccessElemDscp_Type()
)
ntnQosDsAccessElemDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemDscp.setStatus("current")


class _NtnQosDsAccessElemFlowId_Type(FlowIdOrAny):
    """Custom type ntnQosDsAccessElemFlowId based on FlowIdOrAny"""
    defaultValue = -1


_NtnQosDsAccessElemFlowId_Object = MibTableColumn
ntnQosDsAccessElemFlowId = _NtnQosDsAccessElemFlowId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 8),
    _NtnQosDsAccessElemFlowId_Type()
)
ntnQosDsAccessElemFlowId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemFlowId.setStatus("current")


class _NtnQosDsAccessElemProtocol_Type(Unsigned32):
    """Custom type ntnQosDsAccessElemProtocol based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NtnQosDsAccessElemProtocol_Type.__name__ = "Unsigned32"
_NtnQosDsAccessElemProtocol_Object = MibTableColumn
ntnQosDsAccessElemProtocol = _NtnQosDsAccessElemProtocol_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 9),
    _NtnQosDsAccessElemProtocol_Type()
)
ntnQosDsAccessElemProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemProtocol.setStatus("current")


class _NtnQosDsAccessElemDstL4PortMin_Type(InetPortNumber):
    """Custom type ntnQosDsAccessElemDstL4PortMin based on InetPortNumber"""
    defaultValue = 0


_NtnQosDsAccessElemDstL4PortMin_Object = MibTableColumn
ntnQosDsAccessElemDstL4PortMin = _NtnQosDsAccessElemDstL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 10),
    _NtnQosDsAccessElemDstL4PortMin_Type()
)
ntnQosDsAccessElemDstL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemDstL4PortMin.setStatus("current")


class _NtnQosDsAccessElemDstL4PortMax_Type(InetPortNumber):
    """Custom type ntnQosDsAccessElemDstL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_NtnQosDsAccessElemDstL4PortMax_Object = MibTableColumn
ntnQosDsAccessElemDstL4PortMax = _NtnQosDsAccessElemDstL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 11),
    _NtnQosDsAccessElemDstL4PortMax_Type()
)
ntnQosDsAccessElemDstL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemDstL4PortMax.setStatus("current")


class _NtnQosDsAccessElemSrcL4PortMin_Type(InetPortNumber):
    """Custom type ntnQosDsAccessElemSrcL4PortMin based on InetPortNumber"""
    defaultValue = 0


_NtnQosDsAccessElemSrcL4PortMin_Object = MibTableColumn
ntnQosDsAccessElemSrcL4PortMin = _NtnQosDsAccessElemSrcL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 12),
    _NtnQosDsAccessElemSrcL4PortMin_Type()
)
ntnQosDsAccessElemSrcL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemSrcL4PortMin.setStatus("current")


class _NtnQosDsAccessElemSrcL4PortMax_Type(InetPortNumber):
    """Custom type ntnQosDsAccessElemSrcL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_NtnQosDsAccessElemSrcL4PortMax_Object = MibTableColumn
ntnQosDsAccessElemSrcL4PortMax = _NtnQosDsAccessElemSrcL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 13),
    _NtnQosDsAccessElemSrcL4PortMax_Type()
)
ntnQosDsAccessElemSrcL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemSrcL4PortMax.setStatus("current")


class _NtnQosDsAccessElemActionDrop_Type(Integer32):
    """Custom type ntnQosDsAccessElemActionDrop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_NtnQosDsAccessElemActionDrop_Type.__name__ = "Integer32"
_NtnQosDsAccessElemActionDrop_Object = MibTableColumn
ntnQosDsAccessElemActionDrop = _NtnQosDsAccessElemActionDrop_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 14),
    _NtnQosDsAccessElemActionDrop_Type()
)
ntnQosDsAccessElemActionDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemActionDrop.setStatus("current")


class _NtnQosDsAccessElemActionRemarkDscp_Type(Integer32):
    """Custom type ntnQosDsAccessElemActionRemarkDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_NtnQosDsAccessElemActionRemarkDscp_Type.__name__ = "Integer32"
_NtnQosDsAccessElemActionRemarkDscp_Object = MibTableColumn
ntnQosDsAccessElemActionRemarkDscp = _NtnQosDsAccessElemActionRemarkDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 15),
    _NtnQosDsAccessElemActionRemarkDscp_Type()
)
ntnQosDsAccessElemActionRemarkDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemActionRemarkDscp.setStatus("current")


class _NtnQosDsAccessElemActionRemarkCos_Type(Integer32):
    """Custom type ntnQosDsAccessElemActionRemarkCos based on Integer32"""
    defaultValue = 9

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
        *(("ignore", 9),
          ("markAsPriority0", 1),
          ("markAsPriority1", 2),
          ("markAsPriority2", 3),
          ("markAsPriority3", 4),
          ("markAsPriority4", 5),
          ("markAsPriority5", 6),
          ("markAsPriority6", 7),
          ("markAsPriority7", 8))
    )


_NtnQosDsAccessElemActionRemarkCos_Type.__name__ = "Integer32"
_NtnQosDsAccessElemActionRemarkCos_Object = MibTableColumn
ntnQosDsAccessElemActionRemarkCos = _NtnQosDsAccessElemActionRemarkCos_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 16),
    _NtnQosDsAccessElemActionRemarkCos_Type()
)
ntnQosDsAccessElemActionRemarkCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemActionRemarkCos.setStatus("current")


class _NtnQosDsAccessElemActionSetPrec_Type(Integer32):
    """Custom type ntnQosDsAccessElemActionSetPrec based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highDropPrec", 2),
          ("lowDropPrec", 1))
    )


_NtnQosDsAccessElemActionSetPrec_Type.__name__ = "Integer32"
_NtnQosDsAccessElemActionSetPrec_Object = MibTableColumn
ntnQosDsAccessElemActionSetPrec = _NtnQosDsAccessElemActionSetPrec_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 17),
    _NtnQosDsAccessElemActionSetPrec_Type()
)
ntnQosDsAccessElemActionSetPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemActionSetPrec.setStatus("current")


class _NtnQosDsAccessElemName_Type(SnmpAdminString):
    """Custom type ntnQosDsAccessElemName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtnQosDsAccessElemName_Type.__name__ = "SnmpAdminString"
_NtnQosDsAccessElemName_Object = MibTableColumn
ntnQosDsAccessElemName = _NtnQosDsAccessElemName_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 18),
    _NtnQosDsAccessElemName_Type()
)
ntnQosDsAccessElemName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemName.setStatus("current")


class _NtnQosDsAccessElemBlock_Type(SnmpAdminString):
    """Custom type ntnQosDsAccessElemBlock based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtnQosDsAccessElemBlock_Type.__name__ = "SnmpAdminString"
_NtnQosDsAccessElemBlock_Object = MibTableColumn
ntnQosDsAccessElemBlock = _NtnQosDsAccessElemBlock_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 19),
    _NtnQosDsAccessElemBlock_Type()
)
ntnQosDsAccessElemBlock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemBlock.setStatus("current")


class _NtnQosDsAccessElemType_Type(Integer32):
    """Custom type ntnQosDsAccessElemType based on Integer32"""
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
        *(("dsAcl", 1),
          ("dsAppClfr", 2),
          ("dsMultimediaClfr", 3),
          ("dsUserDefinedClfr", 4))
    )


_NtnQosDsAccessElemType_Type.__name__ = "Integer32"
_NtnQosDsAccessElemType_Object = MibTableColumn
ntnQosDsAccessElemType = _NtnQosDsAccessElemType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 20),
    _NtnQosDsAccessElemType_Type()
)
ntnQosDsAccessElemType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemType.setStatus("current")


class _NtnQosDsAccessElemStorage_Type(StorageType):
    """Custom type ntnQosDsAccessElemStorage based on StorageType"""


_NtnQosDsAccessElemStorage_Object = MibTableColumn
ntnQosDsAccessElemStorage = _NtnQosDsAccessElemStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 21),
    _NtnQosDsAccessElemStorage_Type()
)
ntnQosDsAccessElemStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemStorage.setStatus("current")
_NtnQosDsAccessElemStatus_Type = RowStatus
_NtnQosDsAccessElemStatus_Object = MibTableColumn
ntnQosDsAccessElemStatus = _NtnQosDsAccessElemStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 22),
    _NtnQosDsAccessElemStatus_Type()
)
ntnQosDsAccessElemStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemStatus.setStatus("current")


class _NtnQosDsAccessElemEvalPrec_Type(Unsigned32):
    """Custom type ntnQosDsAccessElemEvalPrec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NtnQosDsAccessElemEvalPrec_Type.__name__ = "Unsigned32"
_NtnQosDsAccessElemEvalPrec_Object = MibTableColumn
ntnQosDsAccessElemEvalPrec = _NtnQosDsAccessElemEvalPrec_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 2, 1, 23),
    _NtnQosDsAccessElemEvalPrec_Type()
)
ntnQosDsAccessElemEvalPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsAccessElemEvalPrec.setStatus("current")
_NtnQosL2AccessElemNextFree_Type = IndexIntegerNextFree
_NtnQosL2AccessElemNextFree_Object = MibScalar
ntnQosL2AccessElemNextFree = _NtnQosL2AccessElemNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 3),
    _NtnQosL2AccessElemNextFree_Type()
)
ntnQosL2AccessElemNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemNextFree.setStatus("current")
_NtnQosL2AccessElemTable_Object = MibTable
ntnQosL2AccessElemTable = _NtnQosL2AccessElemTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4)
)
if mibBuilder.loadTexts:
    ntnQosL2AccessElemTable.setStatus("current")
_NtnQosL2AccessElemEntry_Object = MibTableRow
ntnQosL2AccessElemEntry = _NtnQosL2AccessElemEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1)
)
ntnQosL2AccessElemEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemId"),
)
if mibBuilder.loadTexts:
    ntnQosL2AccessElemEntry.setStatus("current")
_NtnQosL2AccessElemId_Type = IndexInteger
_NtnQosL2AccessElemId_Object = MibTableColumn
ntnQosL2AccessElemId = _NtnQosL2AccessElemId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 1),
    _NtnQosL2AccessElemId_Type()
)
ntnQosL2AccessElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemId.setStatus("current")


class _NtnQosL2AccessElemDstAddr_Type(MacAddress):
    """Custom type ntnQosL2AccessElemDstAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_NtnQosL2AccessElemDstAddr_Object = MibTableColumn
ntnQosL2AccessElemDstAddr = _NtnQosL2AccessElemDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 2),
    _NtnQosL2AccessElemDstAddr_Type()
)
ntnQosL2AccessElemDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemDstAddr.setStatus("current")


class _NtnQosL2AccessElemDstAddrMask_Type(MacAddress):
    """Custom type ntnQosL2AccessElemDstAddrMask based on MacAddress"""
    defaultHexValue = "000000000000"


_NtnQosL2AccessElemDstAddrMask_Object = MibTableColumn
ntnQosL2AccessElemDstAddrMask = _NtnQosL2AccessElemDstAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 3),
    _NtnQosL2AccessElemDstAddrMask_Type()
)
ntnQosL2AccessElemDstAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemDstAddrMask.setStatus("current")


class _NtnQosL2AccessElemSrcAddr_Type(MacAddress):
    """Custom type ntnQosL2AccessElemSrcAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_NtnQosL2AccessElemSrcAddr_Object = MibTableColumn
ntnQosL2AccessElemSrcAddr = _NtnQosL2AccessElemSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 4),
    _NtnQosL2AccessElemSrcAddr_Type()
)
ntnQosL2AccessElemSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemSrcAddr.setStatus("current")


class _NtnQosL2AccessElemSrcAddrMask_Type(MacAddress):
    """Custom type ntnQosL2AccessElemSrcAddrMask based on MacAddress"""
    defaultHexValue = "000000000000"


_NtnQosL2AccessElemSrcAddrMask_Object = MibTableColumn
ntnQosL2AccessElemSrcAddrMask = _NtnQosL2AccessElemSrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 5),
    _NtnQosL2AccessElemSrcAddrMask_Type()
)
ntnQosL2AccessElemSrcAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemSrcAddrMask.setStatus("current")


class _NtnQosL2AccessElemVlanIdMin_Type(Integer32):
    """Custom type ntnQosL2AccessElemVlanIdMin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_NtnQosL2AccessElemVlanIdMin_Type.__name__ = "Integer32"
_NtnQosL2AccessElemVlanIdMin_Object = MibTableColumn
ntnQosL2AccessElemVlanIdMin = _NtnQosL2AccessElemVlanIdMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 6),
    _NtnQosL2AccessElemVlanIdMin_Type()
)
ntnQosL2AccessElemVlanIdMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemVlanIdMin.setStatus("current")


class _NtnQosL2AccessElemVlanIdMax_Type(Integer32):
    """Custom type ntnQosL2AccessElemVlanIdMax based on Integer32"""
    defaultValue = 4094

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_NtnQosL2AccessElemVlanIdMax_Type.__name__ = "Integer32"
_NtnQosL2AccessElemVlanIdMax_Object = MibTableColumn
ntnQosL2AccessElemVlanIdMax = _NtnQosL2AccessElemVlanIdMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 7),
    _NtnQosL2AccessElemVlanIdMax_Type()
)
ntnQosL2AccessElemVlanIdMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemVlanIdMax.setStatus("current")


class _NtnQosL2AccessElemVlanTag_Type(Integer32):
    """Custom type ntnQosL2AccessElemVlanTag based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 3),
          ("tagged", 2),
          ("untagged", 1))
    )


_NtnQosL2AccessElemVlanTag_Type.__name__ = "Integer32"
_NtnQosL2AccessElemVlanTag_Object = MibTableColumn
ntnQosL2AccessElemVlanTag = _NtnQosL2AccessElemVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 8),
    _NtnQosL2AccessElemVlanTag_Type()
)
ntnQosL2AccessElemVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemVlanTag.setStatus("current")


class _NtnQosL2AccessElemEtherType_Type(Integer32):
    """Custom type ntnQosL2AccessElemEtherType based on Integer32"""
    defaultHexValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NtnQosL2AccessElemEtherType_Type.__name__ = "Integer32"
_NtnQosL2AccessElemEtherType_Object = MibTableColumn
ntnQosL2AccessElemEtherType = _NtnQosL2AccessElemEtherType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 9),
    _NtnQosL2AccessElemEtherType_Type()
)
ntnQosL2AccessElemEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemEtherType.setStatus("current")


class _NtnQosL2AccessElemUserPriority_Type(Integer32):
    """Custom type ntnQosL2AccessElemUserPriority based on Integer32"""
    defaultValue = 9

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
        *(("matchAllPriorities", 9),
          ("matchPriority0", 1),
          ("matchPriority1", 2),
          ("matchPriority2", 3),
          ("matchPriority3", 4),
          ("matchPriority4", 5),
          ("matchPriority5", 6),
          ("matchPriority6", 7),
          ("matchPriority7", 8))
    )


_NtnQosL2AccessElemUserPriority_Type.__name__ = "Integer32"
_NtnQosL2AccessElemUserPriority_Object = MibTableColumn
ntnQosL2AccessElemUserPriority = _NtnQosL2AccessElemUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 10),
    _NtnQosL2AccessElemUserPriority_Type()
)
ntnQosL2AccessElemUserPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemUserPriority.setStatus("current")


class _NtnQosL2AccessElemActionDrop_Type(Integer32):
    """Custom type ntnQosL2AccessElemActionDrop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_NtnQosL2AccessElemActionDrop_Type.__name__ = "Integer32"
_NtnQosL2AccessElemActionDrop_Object = MibTableColumn
ntnQosL2AccessElemActionDrop = _NtnQosL2AccessElemActionDrop_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 11),
    _NtnQosL2AccessElemActionDrop_Type()
)
ntnQosL2AccessElemActionDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemActionDrop.setStatus("current")


class _NtnQosL2AccessElemActionRemarkDscp_Type(Integer32):
    """Custom type ntnQosL2AccessElemActionRemarkDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_NtnQosL2AccessElemActionRemarkDscp_Type.__name__ = "Integer32"
_NtnQosL2AccessElemActionRemarkDscp_Object = MibTableColumn
ntnQosL2AccessElemActionRemarkDscp = _NtnQosL2AccessElemActionRemarkDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 12),
    _NtnQosL2AccessElemActionRemarkDscp_Type()
)
ntnQosL2AccessElemActionRemarkDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemActionRemarkDscp.setStatus("current")


class _NtnQosL2AccessElemActionRemarkCos_Type(Integer32):
    """Custom type ntnQosL2AccessElemActionRemarkCos based on Integer32"""
    defaultValue = 9

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
        *(("ignore", 9),
          ("markAsPriority0", 1),
          ("markAsPriority1", 2),
          ("markAsPriority2", 3),
          ("markAsPriority3", 4),
          ("markAsPriority4", 5),
          ("markAsPriority5", 6),
          ("markAsPriority6", 7),
          ("markAsPriority7", 8))
    )


_NtnQosL2AccessElemActionRemarkCos_Type.__name__ = "Integer32"
_NtnQosL2AccessElemActionRemarkCos_Object = MibTableColumn
ntnQosL2AccessElemActionRemarkCos = _NtnQosL2AccessElemActionRemarkCos_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 13),
    _NtnQosL2AccessElemActionRemarkCos_Type()
)
ntnQosL2AccessElemActionRemarkCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemActionRemarkCos.setStatus("current")


class _NtnQosL2AccessElemActionSetPrec_Type(Integer32):
    """Custom type ntnQosL2AccessElemActionSetPrec based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highDropPrec", 2),
          ("lowDropPrec", 1))
    )


_NtnQosL2AccessElemActionSetPrec_Type.__name__ = "Integer32"
_NtnQosL2AccessElemActionSetPrec_Object = MibTableColumn
ntnQosL2AccessElemActionSetPrec = _NtnQosL2AccessElemActionSetPrec_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 14),
    _NtnQosL2AccessElemActionSetPrec_Type()
)
ntnQosL2AccessElemActionSetPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemActionSetPrec.setStatus("current")


class _NtnQosL2AccessElemName_Type(SnmpAdminString):
    """Custom type ntnQosL2AccessElemName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtnQosL2AccessElemName_Type.__name__ = "SnmpAdminString"
_NtnQosL2AccessElemName_Object = MibTableColumn
ntnQosL2AccessElemName = _NtnQosL2AccessElemName_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 15),
    _NtnQosL2AccessElemName_Type()
)
ntnQosL2AccessElemName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemName.setStatus("current")


class _NtnQosL2AccessElemBlock_Type(SnmpAdminString):
    """Custom type ntnQosL2AccessElemBlock based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtnQosL2AccessElemBlock_Type.__name__ = "SnmpAdminString"
_NtnQosL2AccessElemBlock_Object = MibTableColumn
ntnQosL2AccessElemBlock = _NtnQosL2AccessElemBlock_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 16),
    _NtnQosL2AccessElemBlock_Type()
)
ntnQosL2AccessElemBlock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemBlock.setStatus("current")


class _NtnQosL2AccessElemType_Type(Integer32):
    """Custom type ntnQosL2AccessElemType based on Integer32"""
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
        *(("l2Acl", 1),
          ("l2AppClfr", 2),
          ("l2MultimediaClfr", 3),
          ("l2UserDefinedClfr", 4))
    )


_NtnQosL2AccessElemType_Type.__name__ = "Integer32"
_NtnQosL2AccessElemType_Object = MibTableColumn
ntnQosL2AccessElemType = _NtnQosL2AccessElemType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 17),
    _NtnQosL2AccessElemType_Type()
)
ntnQosL2AccessElemType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemType.setStatus("current")


class _NtnQosL2AccessElemStorage_Type(StorageType):
    """Custom type ntnQosL2AccessElemStorage based on StorageType"""


_NtnQosL2AccessElemStorage_Object = MibTableColumn
ntnQosL2AccessElemStorage = _NtnQosL2AccessElemStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 18),
    _NtnQosL2AccessElemStorage_Type()
)
ntnQosL2AccessElemStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemStorage.setStatus("current")
_NtnQosL2AccessElemStatus_Type = RowStatus
_NtnQosL2AccessElemStatus_Object = MibTableColumn
ntnQosL2AccessElemStatus = _NtnQosL2AccessElemStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 19),
    _NtnQosL2AccessElemStatus_Type()
)
ntnQosL2AccessElemStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemStatus.setStatus("current")


class _NtnQosL2AccessElemEvalPrec_Type(Unsigned32):
    """Custom type ntnQosL2AccessElemEvalPrec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NtnQosL2AccessElemEvalPrec_Type.__name__ = "Unsigned32"
_NtnQosL2AccessElemEvalPrec_Object = MibTableColumn
ntnQosL2AccessElemEvalPrec = _NtnQosL2AccessElemEvalPrec_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 4, 1, 20),
    _NtnQosL2AccessElemEvalPrec_Type()
)
ntnQosL2AccessElemEvalPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosL2AccessElemEvalPrec.setStatus("current")
_NtnQosAccessAsgnNextFree_Type = IndexIntegerNextFree
_NtnQosAccessAsgnNextFree_Object = MibScalar
ntnQosAccessAsgnNextFree = _NtnQosAccessAsgnNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 5),
    _NtnQosAccessAsgnNextFree_Type()
)
ntnQosAccessAsgnNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnNextFree.setStatus("current")
_NtnQosAccessAsgnTable_Object = MibTable
ntnQosAccessAsgnTable = _NtnQosAccessAsgnTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6)
)
if mibBuilder.loadTexts:
    ntnQosAccessAsgnTable.setStatus("current")
_NtnQosAccessAsgnEntry_Object = MibTableRow
ntnQosAccessAsgnEntry = _NtnQosAccessAsgnEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1)
)
ntnQosAccessAsgnEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnId"),
)
if mibBuilder.loadTexts:
    ntnQosAccessAsgnEntry.setStatus("current")
_NtnQosAccessAsgnId_Type = IndexInteger
_NtnQosAccessAsgnId_Object = MibTableColumn
ntnQosAccessAsgnId = _NtnQosAccessAsgnId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 1),
    _NtnQosAccessAsgnId_Type()
)
ntnQosAccessAsgnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnId.setStatus("current")


class _NtnQosAccessAsgnAclType_Type(Integer32):
    """Custom type ntnQosAccessAsgnAclType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("dsAcl", 1),
          ("dsAppClfr", 3),
          ("dsL2NsnaClfr", 8),
          ("dsL2TrafficProfile", 10),
          ("dsL2UbpClfr", 9),
          ("dsUserDefinedClfr", 5),
          ("l2Acl", 2),
          ("l2AppClfr", 4),
          ("l2UserDefinedClfr", 6),
          ("multimediaClfr", 7))
    )


_NtnQosAccessAsgnAclType_Type.__name__ = "Integer32"
_NtnQosAccessAsgnAclType_Object = MibTableColumn
ntnQosAccessAsgnAclType = _NtnQosAccessAsgnAclType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 2),
    _NtnQosAccessAsgnAclType_Type()
)
ntnQosAccessAsgnAclType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnAclType.setStatus("current")


class _NtnQosAccessAsgnName_Type(SnmpAdminString):
    """Custom type ntnQosAccessAsgnName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtnQosAccessAsgnName_Type.__name__ = "SnmpAdminString"
_NtnQosAccessAsgnName_Object = MibTableColumn
ntnQosAccessAsgnName = _NtnQosAccessAsgnName_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 3),
    _NtnQosAccessAsgnName_Type()
)
ntnQosAccessAsgnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnName.setStatus("current")
_NtnQosAccessAsgnIfIndex_Type = InterfaceIndexOrZero
_NtnQosAccessAsgnIfIndex_Object = MibTableColumn
ntnQosAccessAsgnIfIndex = _NtnQosAccessAsgnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 4),
    _NtnQosAccessAsgnIfIndex_Type()
)
ntnQosAccessAsgnIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnIfIndex.setStatus("current")


class _NtnQosAccessAsgnRate_Type(Unsigned32):
    """Custom type ntnQosAccessAsgnRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NtnQosAccessAsgnRate_Type.__name__ = "Unsigned32"
_NtnQosAccessAsgnRate_Object = MibTableColumn
ntnQosAccessAsgnRate = _NtnQosAccessAsgnRate_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 5),
    _NtnQosAccessAsgnRate_Type()
)
ntnQosAccessAsgnRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnRate.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnRate.setUnits("kilobits per second")


class _NtnQosAccessAsgnBurstSize_Type(BurstSize):
    """Custom type ntnQosAccessAsgnBurstSize based on BurstSize"""
    defaultValue = 0


_NtnQosAccessAsgnBurstSize_Object = MibTableColumn
ntnQosAccessAsgnBurstSize = _NtnQosAccessAsgnBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 6),
    _NtnQosAccessAsgnBurstSize_Type()
)
ntnQosAccessAsgnBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnBurstSize.setUnits("Bytes")


class _NtnQosAccessAsgnOutActionDrop_Type(Integer32):
    """Custom type ntnQosAccessAsgnOutActionDrop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_NtnQosAccessAsgnOutActionDrop_Type.__name__ = "Integer32"
_NtnQosAccessAsgnOutActionDrop_Object = MibTableColumn
ntnQosAccessAsgnOutActionDrop = _NtnQosAccessAsgnOutActionDrop_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 7),
    _NtnQosAccessAsgnOutActionDrop_Type()
)
ntnQosAccessAsgnOutActionDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnOutActionDrop.setStatus("current")


class _NtnQosAccessAsgnOutActionRemarkDscp_Type(Integer32):
    """Custom type ntnQosAccessAsgnOutActionRemarkDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_NtnQosAccessAsgnOutActionRemarkDscp_Type.__name__ = "Integer32"
_NtnQosAccessAsgnOutActionRemarkDscp_Object = MibTableColumn
ntnQosAccessAsgnOutActionRemarkDscp = _NtnQosAccessAsgnOutActionRemarkDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 8),
    _NtnQosAccessAsgnOutActionRemarkDscp_Type()
)
ntnQosAccessAsgnOutActionRemarkDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnOutActionRemarkDscp.setStatus("current")


class _NtnQosAccessAsgnOutActionRemarkCos_Type(Integer32):
    """Custom type ntnQosAccessAsgnOutActionRemarkCos based on Integer32"""
    defaultValue = 9

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
              11)
        )
    )
    namedValues = NamedValues(
        *(("deriveFromEgressDscp", 10),
          ("deriveFromIngressTosPrec", 11),
          ("ignore", 9),
          ("markAsPriority0", 1),
          ("markAsPriority1", 2),
          ("markAsPriority2", 3),
          ("markAsPriority3", 4),
          ("markAsPriority4", 5),
          ("markAsPriority5", 6),
          ("markAsPriority6", 7),
          ("markAsPriority7", 8))
    )


_NtnQosAccessAsgnOutActionRemarkCos_Type.__name__ = "Integer32"
_NtnQosAccessAsgnOutActionRemarkCos_Object = MibTableColumn
ntnQosAccessAsgnOutActionRemarkCos = _NtnQosAccessAsgnOutActionRemarkCos_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 9),
    _NtnQosAccessAsgnOutActionRemarkCos_Type()
)
ntnQosAccessAsgnOutActionRemarkCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnOutActionRemarkCos.setStatus("current")


class _NtnQosAccessAsgnOutActionSetPrec_Type(Integer32):
    """Custom type ntnQosAccessAsgnOutActionSetPrec based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highDropPrec", 2),
          ("lowDropPrec", 1))
    )


_NtnQosAccessAsgnOutActionSetPrec_Type.__name__ = "Integer32"
_NtnQosAccessAsgnOutActionSetPrec_Object = MibTableColumn
ntnQosAccessAsgnOutActionSetPrec = _NtnQosAccessAsgnOutActionSetPrec_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 10),
    _NtnQosAccessAsgnOutActionSetPrec_Type()
)
ntnQosAccessAsgnOutActionSetPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnOutActionSetPrec.setStatus("current")


class _NtnQosAccessAsgnStatsType_Type(Integer32):
    """Custom type ntnQosAccessAsgnStatsType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aggregateClfr", 2),
          ("individualClfr", 1),
          ("noStatsTracking", 3))
    )


_NtnQosAccessAsgnStatsType_Type.__name__ = "Integer32"
_NtnQosAccessAsgnStatsType_Object = MibTableColumn
ntnQosAccessAsgnStatsType = _NtnQosAccessAsgnStatsType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 11),
    _NtnQosAccessAsgnStatsType_Type()
)
ntnQosAccessAsgnStatsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnStatsType.setStatus("current")


class _NtnQosAccessAsgnStorage_Type(StorageType):
    """Custom type ntnQosAccessAsgnStorage based on StorageType"""


_NtnQosAccessAsgnStorage_Object = MibTableColumn
ntnQosAccessAsgnStorage = _NtnQosAccessAsgnStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 12),
    _NtnQosAccessAsgnStorage_Type()
)
ntnQosAccessAsgnStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnStorage.setStatus("current")
_NtnQosAccessAsgnStatus_Type = RowStatus
_NtnQosAccessAsgnStatus_Object = MibTableColumn
ntnQosAccessAsgnStatus = _NtnQosAccessAsgnStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 13),
    _NtnQosAccessAsgnStatus_Type()
)
ntnQosAccessAsgnStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnStatus.setStatus("current")


class _NtnQosAccessAsgnNonMatchActionDrop_Type(Integer32):
    """Custom type ntnQosAccessAsgnNonMatchActionDrop based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("defer", 3),
          ("drop", 1),
          ("pass", 2))
    )


_NtnQosAccessAsgnNonMatchActionDrop_Type.__name__ = "Integer32"
_NtnQosAccessAsgnNonMatchActionDrop_Object = MibTableColumn
ntnQosAccessAsgnNonMatchActionDrop = _NtnQosAccessAsgnNonMatchActionDrop_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 14),
    _NtnQosAccessAsgnNonMatchActionDrop_Type()
)
ntnQosAccessAsgnNonMatchActionDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnNonMatchActionDrop.setStatus("current")


class _NtnQosAccessAsgnMeterType_Type(AutonomousType):
    """Custom type ntnQosAccessAsgnMeterType based on AutonomousType"""
    defaultValue = (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 6, 5, 1)


_NtnQosAccessAsgnMeterType_Object = MibTableColumn
ntnQosAccessAsgnMeterType = _NtnQosAccessAsgnMeterType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 15),
    _NtnQosAccessAsgnMeterType_Type()
)
ntnQosAccessAsgnMeterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnMeterType.setStatus("current")


class _NtnQosAccessAsgnSecondaryRate_Type(Unsigned32):
    """Custom type ntnQosAccessAsgnSecondaryRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NtnQosAccessAsgnSecondaryRate_Type.__name__ = "Unsigned32"
_NtnQosAccessAsgnSecondaryRate_Object = MibTableColumn
ntnQosAccessAsgnSecondaryRate = _NtnQosAccessAsgnSecondaryRate_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 16),
    _NtnQosAccessAsgnSecondaryRate_Type()
)
ntnQosAccessAsgnSecondaryRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnSecondaryRate.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnSecondaryRate.setUnits("kilobits per second")


class _NtnQosAccessAsgnSecondaryBurstSize_Type(BurstSize):
    """Custom type ntnQosAccessAsgnSecondaryBurstSize based on BurstSize"""
    defaultValue = 0


_NtnQosAccessAsgnSecondaryBurstSize_Object = MibTableColumn
ntnQosAccessAsgnSecondaryBurstSize = _NtnQosAccessAsgnSecondaryBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 17),
    _NtnQosAccessAsgnSecondaryBurstSize_Type()
)
ntnQosAccessAsgnSecondaryBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnSecondaryBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnSecondaryBurstSize.setUnits("Bytes")


class _NtnQosAccessAsgnYelActionDrop_Type(Integer32):
    """Custom type ntnQosAccessAsgnYelActionDrop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_NtnQosAccessAsgnYelActionDrop_Type.__name__ = "Integer32"
_NtnQosAccessAsgnYelActionDrop_Object = MibTableColumn
ntnQosAccessAsgnYelActionDrop = _NtnQosAccessAsgnYelActionDrop_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 18),
    _NtnQosAccessAsgnYelActionDrop_Type()
)
ntnQosAccessAsgnYelActionDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnYelActionDrop.setStatus("current")


class _NtnQosAccessAsgnYelActionRemarkDscp_Type(Integer32):
    """Custom type ntnQosAccessAsgnYelActionRemarkDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_NtnQosAccessAsgnYelActionRemarkDscp_Type.__name__ = "Integer32"
_NtnQosAccessAsgnYelActionRemarkDscp_Object = MibTableColumn
ntnQosAccessAsgnYelActionRemarkDscp = _NtnQosAccessAsgnYelActionRemarkDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 19),
    _NtnQosAccessAsgnYelActionRemarkDscp_Type()
)
ntnQosAccessAsgnYelActionRemarkDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnYelActionRemarkDscp.setStatus("current")


class _NtnQosAccessAsgnYelActionRemarkCos_Type(Integer32):
    """Custom type ntnQosAccessAsgnYelActionRemarkCos based on Integer32"""
    defaultValue = 9

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
        *(("ignore", 9),
          ("markAsPriority0", 1),
          ("markAsPriority1", 2),
          ("markAsPriority2", 3),
          ("markAsPriority3", 4),
          ("markAsPriority4", 5),
          ("markAsPriority5", 6),
          ("markAsPriority6", 7),
          ("markAsPriority7", 8))
    )


_NtnQosAccessAsgnYelActionRemarkCos_Type.__name__ = "Integer32"
_NtnQosAccessAsgnYelActionRemarkCos_Object = MibTableColumn
ntnQosAccessAsgnYelActionRemarkCos = _NtnQosAccessAsgnYelActionRemarkCos_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 20),
    _NtnQosAccessAsgnYelActionRemarkCos_Type()
)
ntnQosAccessAsgnYelActionRemarkCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnYelActionRemarkCos.setStatus("current")


class _NtnQosAccessAsgnYelActionSetPrec_Type(Integer32):
    """Custom type ntnQosAccessAsgnYelActionSetPrec based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highDropPrec", 2),
          ("lowDropPrec", 1))
    )


_NtnQosAccessAsgnYelActionSetPrec_Type.__name__ = "Integer32"
_NtnQosAccessAsgnYelActionSetPrec_Object = MibTableColumn
ntnQosAccessAsgnYelActionSetPrec = _NtnQosAccessAsgnYelActionSetPrec_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 21),
    _NtnQosAccessAsgnYelActionSetPrec_Type()
)
ntnQosAccessAsgnYelActionSetPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnYelActionSetPrec.setStatus("current")


class _NtnQosAccessAsgnSetPriority_Type(Unsigned32):
    """Custom type ntnQosAccessAsgnSetPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NtnQosAccessAsgnSetPriority_Type.__name__ = "Unsigned32"
_NtnQosAccessAsgnSetPriority_Object = MibTableColumn
ntnQosAccessAsgnSetPriority = _NtnQosAccessAsgnSetPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 22),
    _NtnQosAccessAsgnSetPriority_Type()
)
ntnQosAccessAsgnSetPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnSetPriority.setStatus("current")


class _NtnQosAccessAsgnMeteringMode_Type(Integer32):
    """Custom type ntnQosAccessAsgnMeteringMode based on Integer32"""
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
        *(("noMetering", 1),
          ("perClassifierMetering", 4),
          ("perPolicyIndividualRateMetering", 3),
          ("perPolicyUniformRateMetering", 2))
    )


_NtnQosAccessAsgnMeteringMode_Type.__name__ = "Integer32"
_NtnQosAccessAsgnMeteringMode_Object = MibTableColumn
ntnQosAccessAsgnMeteringMode = _NtnQosAccessAsgnMeteringMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 6, 1, 23),
    _NtnQosAccessAsgnMeteringMode_Type()
)
ntnQosAccessAsgnMeteringMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosAccessAsgnMeteringMode.setStatus("current")
_NtnQosIfAppsTable_Object = MibTable
ntnQosIfAppsTable = _NtnQosIfAppsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 7)
)
if mibBuilder.loadTexts:
    ntnQosIfAppsTable.setStatus("current")
_NtnQosIfAppsEntry_Object = MibTableRow
ntnQosIfAppsEntry = _NtnQosIfAppsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 7, 1)
)
ntnQosIfAppsEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfAppsIfIndex"),
)
if mibBuilder.loadTexts:
    ntnQosIfAppsEntry.setStatus("current")
_NtnQosIfAppsIfIndex_Type = InterfaceIndex
_NtnQosIfAppsIfIndex_Object = MibTableColumn
ntnQosIfAppsIfIndex = _NtnQosIfAppsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 7, 1, 1),
    _NtnQosIfAppsIfIndex_Type()
)
ntnQosIfAppsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosIfAppsIfIndex.setStatus("current")


class _NtnQosIfAppsAppEnable_Type(Bits):
    """Custom type ntnQosIfAppsAppEnable based on Bits"""
    namedValues = NamedValues(
        *(("arpSpoofing", 1),
          ("bpduBlocker", 10),
          ("dhcpSnooping", 2),
          ("dhcpSpoofing", 3),
          ("dnsPort", 9),
          ("ftpPort", 8),
          ("nachia", 5),
          ("other", 0),
          ("sqlSlam", 4),
          ("synFinScan", 7),
          ("xmas", 6))
    )

_NtnQosIfAppsAppEnable_Type.__name__ = "Bits"
_NtnQosIfAppsAppEnable_Object = MibTableColumn
ntnQosIfAppsAppEnable = _NtnQosIfAppsAppEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 7, 1, 2),
    _NtnQosIfAppsAppEnable_Type()
)
ntnQosIfAppsAppEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfAppsAppEnable.setStatus("current")


class _NtnQosIfAppsDefaultGateway_Type(InetAddressIPv4):
    """Custom type ntnQosIfAppsDefaultGateway based on InetAddressIPv4"""
    defaultHexValue = "00000000"


_NtnQosIfAppsDefaultGateway_Object = MibTableColumn
ntnQosIfAppsDefaultGateway = _NtnQosIfAppsDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 7, 1, 3),
    _NtnQosIfAppsDefaultGateway_Type()
)
ntnQosIfAppsDefaultGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfAppsDefaultGateway.setStatus("current")


class _NtnQosIfAppsIfType_Type(Integer32):
    """Custom type ntnQosIfAppsIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("core", 2))
    )


_NtnQosIfAppsIfType_Type.__name__ = "Integer32"
_NtnQosIfAppsIfType_Object = MibTableColumn
ntnQosIfAppsIfType = _NtnQosIfAppsIfType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 7, 1, 4),
    _NtnQosIfAppsIfType_Type()
)
ntnQosIfAppsIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfAppsIfType.setStatus("current")


class _NtnQosIfAppsDHCPServer_Type(InetAddressIPv4):
    """Custom type ntnQosIfAppsDHCPServer based on InetAddressIPv4"""
    defaultHexValue = "00000000"


_NtnQosIfAppsDHCPServer_Object = MibTableColumn
ntnQosIfAppsDHCPServer = _NtnQosIfAppsDHCPServer_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 7, 1, 5),
    _NtnQosIfAppsDHCPServer_Type()
)
ntnQosIfAppsDHCPServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfAppsDHCPServer.setStatus("current")


class _NtnQosIfAppsStorage_Type(StorageType):
    """Custom type ntnQosIfAppsStorage based on StorageType"""


_NtnQosIfAppsStorage_Object = MibTableColumn
ntnQosIfAppsStorage = _NtnQosIfAppsStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 7, 1, 6),
    _NtnQosIfAppsStorage_Type()
)
ntnQosIfAppsStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfAppsStorage.setStatus("current")
_NtnQosIfAppsStatus_Type = RowStatus
_NtnQosIfAppsStatus_Object = MibTableColumn
ntnQosIfAppsStatus = _NtnQosIfAppsStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 7, 1, 7),
    _NtnQosIfAppsStatus_Type()
)
ntnQosIfAppsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosIfAppsStatus.setStatus("current")
_NtnQosUserPolicyNextFree_Type = IndexIntegerNextFree
_NtnQosUserPolicyNextFree_Object = MibScalar
ntnQosUserPolicyNextFree = _NtnQosUserPolicyNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 8),
    _NtnQosUserPolicyNextFree_Type()
)
ntnQosUserPolicyNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosUserPolicyNextFree.setStatus("current")
_NtnQosUserPolicyTable_Object = MibTable
ntnQosUserPolicyTable = _NtnQosUserPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 9)
)
if mibBuilder.loadTexts:
    ntnQosUserPolicyTable.setStatus("current")
_NtnQosUserPolicyEntry_Object = MibTableRow
ntnQosUserPolicyEntry = _NtnQosUserPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 9, 1)
)
ntnQosUserPolicyEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserPolicyId"),
)
if mibBuilder.loadTexts:
    ntnQosUserPolicyEntry.setStatus("current")
_NtnQosUserPolicyId_Type = IndexInteger
_NtnQosUserPolicyId_Object = MibTableColumn
ntnQosUserPolicyId = _NtnQosUserPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 9, 1, 1),
    _NtnQosUserPolicyId_Type()
)
ntnQosUserPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosUserPolicyId.setStatus("current")
_NtnQosUserPolicyIfIndex_Type = InterfaceIndex
_NtnQosUserPolicyIfIndex_Object = MibTableColumn
ntnQosUserPolicyIfIndex = _NtnQosUserPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 9, 1, 2),
    _NtnQosUserPolicyIfIndex_Type()
)
ntnQosUserPolicyIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosUserPolicyIfIndex.setStatus("current")
_NtnQosUserPolicyRoleCombination_Type = RoleCombination
_NtnQosUserPolicyRoleCombination_Object = MibTableColumn
ntnQosUserPolicyRoleCombination = _NtnQosUserPolicyRoleCombination_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 9, 1, 3),
    _NtnQosUserPolicyRoleCombination_Type()
)
ntnQosUserPolicyRoleCombination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosUserPolicyRoleCombination.setStatus("current")


class _NtnQosUserPolicyUserName_Type(SnmpAdminString):
    """Custom type ntnQosUserPolicyUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NtnQosUserPolicyUserName_Type.__name__ = "SnmpAdminString"
_NtnQosUserPolicyUserName_Object = MibTableColumn
ntnQosUserPolicyUserName = _NtnQosUserPolicyUserName_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 9, 1, 4),
    _NtnQosUserPolicyUserName_Type()
)
ntnQosUserPolicyUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosUserPolicyUserName.setStatus("current")


class _NtnQosUserPolicyUserGroup_Type(SnmpAdminString):
    """Custom type ntnQosUserPolicyUserGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtnQosUserPolicyUserGroup_Type.__name__ = "SnmpAdminString"
_NtnQosUserPolicyUserGroup_Object = MibTableColumn
ntnQosUserPolicyUserGroup = _NtnQosUserPolicyUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 9, 1, 5),
    _NtnQosUserPolicyUserGroup_Type()
)
ntnQosUserPolicyUserGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosUserPolicyUserGroup.setStatus("current")
_NtnQosUserPolicySessionId_Type = Unsigned32
_NtnQosUserPolicySessionId_Object = MibTableColumn
ntnQosUserPolicySessionId = _NtnQosUserPolicySessionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 9, 1, 6),
    _NtnQosUserPolicySessionId_Type()
)
ntnQosUserPolicySessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosUserPolicySessionId.setStatus("current")
_NtnQosUserPolicySessionStart_Type = Unsigned32
_NtnQosUserPolicySessionStart_Object = MibTableColumn
ntnQosUserPolicySessionStart = _NtnQosUserPolicySessionStart_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 9, 1, 7),
    _NtnQosUserPolicySessionStart_Type()
)
ntnQosUserPolicySessionStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosUserPolicySessionStart.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosUserPolicySessionStart.setUnits("seconds")
_NtnQosUserPolicySessionGroup_Type = Unsigned32
_NtnQosUserPolicySessionGroup_Object = MibTableColumn
ntnQosUserPolicySessionGroup = _NtnQosUserPolicySessionGroup_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 9, 1, 8),
    _NtnQosUserPolicySessionGroup_Type()
)
ntnQosUserPolicySessionGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosUserPolicySessionGroup.setStatus("current")


class _NtnQosUserPolicyStorage_Type(StorageType):
    """Custom type ntnQosUserPolicyStorage based on StorageType"""


_NtnQosUserPolicyStorage_Object = MibTableColumn
ntnQosUserPolicyStorage = _NtnQosUserPolicyStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 9, 1, 9),
    _NtnQosUserPolicyStorage_Type()
)
ntnQosUserPolicyStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosUserPolicyStorage.setStatus("current")
_NtnQosUserPolicyStatus_Type = RowStatus
_NtnQosUserPolicyStatus_Object = MibTableColumn
ntnQosUserPolicyStatus = _NtnQosUserPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 9, 1, 10),
    _NtnQosUserPolicyStatus_Type()
)
ntnQosUserPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosUserPolicyStatus.setStatus("current")


class _NtnQosUserPolicySrcMacAddr_Type(MacAddress):
    """Custom type ntnQosUserPolicySrcMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_NtnQosUserPolicySrcMacAddr_Object = MibTableColumn
ntnQosUserPolicySrcMacAddr = _NtnQosUserPolicySrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 9, 1, 11),
    _NtnQosUserPolicySrcMacAddr_Type()
)
ntnQosUserPolicySrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosUserPolicySrcMacAddr.setStatus("current")


class _NtnQosUserPolicySrcMacAddrMask_Type(MacAddress):
    """Custom type ntnQosUserPolicySrcMacAddrMask based on MacAddress"""
    defaultHexValue = "000000000000"


_NtnQosUserPolicySrcMacAddrMask_Object = MibTableColumn
ntnQosUserPolicySrcMacAddrMask = _NtnQosUserPolicySrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 9, 1, 12),
    _NtnQosUserPolicySrcMacAddrMask_Type()
)
ntnQosUserPolicySrcMacAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosUserPolicySrcMacAddrMask.setStatus("current")
_NtnQosDsL2AccessElemNextFree_Type = IndexIntegerNextFree
_NtnQosDsL2AccessElemNextFree_Object = MibScalar
ntnQosDsL2AccessElemNextFree = _NtnQosDsL2AccessElemNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 10),
    _NtnQosDsL2AccessElemNextFree_Type()
)
ntnQosDsL2AccessElemNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemNextFree.setStatus("current")
_NtnQosDsL2AccessElemTable_Object = MibTable
ntnQosDsL2AccessElemTable = _NtnQosDsL2AccessElemTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11)
)
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemTable.setStatus("current")
_NtnQosDsL2AccessElemEntry_Object = MibTableRow
ntnQosDsL2AccessElemEntry = _NtnQosDsL2AccessElemEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1)
)
ntnQosDsL2AccessElemEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemId"),
)
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemEntry.setStatus("current")
_NtnQosDsL2AccessElemId_Type = IndexInteger
_NtnQosDsL2AccessElemId_Object = MibTableColumn
ntnQosDsL2AccessElemId = _NtnQosDsL2AccessElemId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 1),
    _NtnQosDsL2AccessElemId_Type()
)
ntnQosDsL2AccessElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemId.setStatus("current")


class _NtnQosDsL2AccessElemAddrType_Type(InetAddressType):
    """Custom type ntnQosDsL2AccessElemAddrType based on InetAddressType"""


_NtnQosDsL2AccessElemAddrType_Object = MibTableColumn
ntnQosDsL2AccessElemAddrType = _NtnQosDsL2AccessElemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 2),
    _NtnQosDsL2AccessElemAddrType_Type()
)
ntnQosDsL2AccessElemAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemAddrType.setStatus("current")


class _NtnQosDsL2AccessElemDstIpAddr_Type(InetAddress):
    """Custom type ntnQosDsL2AccessElemDstIpAddr based on InetAddress"""
    defaultHexValue = "00000000"


_NtnQosDsL2AccessElemDstIpAddr_Object = MibTableColumn
ntnQosDsL2AccessElemDstIpAddr = _NtnQosDsL2AccessElemDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 3),
    _NtnQosDsL2AccessElemDstIpAddr_Type()
)
ntnQosDsL2AccessElemDstIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemDstIpAddr.setStatus("current")


class _NtnQosDsL2AccessElemDstIpPrefixLength_Type(InetAddressPrefixLength):
    """Custom type ntnQosDsL2AccessElemDstIpPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_NtnQosDsL2AccessElemDstIpPrefixLength_Object = MibTableColumn
ntnQosDsL2AccessElemDstIpPrefixLength = _NtnQosDsL2AccessElemDstIpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 4),
    _NtnQosDsL2AccessElemDstIpPrefixLength_Type()
)
ntnQosDsL2AccessElemDstIpPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemDstIpPrefixLength.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemDstIpPrefixLength.setUnits("bits")


class _NtnQosDsL2AccessElemSrcIpAddr_Type(InetAddress):
    """Custom type ntnQosDsL2AccessElemSrcIpAddr based on InetAddress"""
    defaultHexValue = "00000000"


_NtnQosDsL2AccessElemSrcIpAddr_Object = MibTableColumn
ntnQosDsL2AccessElemSrcIpAddr = _NtnQosDsL2AccessElemSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 5),
    _NtnQosDsL2AccessElemSrcIpAddr_Type()
)
ntnQosDsL2AccessElemSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemSrcIpAddr.setStatus("current")


class _NtnQosDsL2AccessElemSrcIpPrefixLength_Type(InetAddressPrefixLength):
    """Custom type ntnQosDsL2AccessElemSrcIpPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_NtnQosDsL2AccessElemSrcIpPrefixLength_Object = MibTableColumn
ntnQosDsL2AccessElemSrcIpPrefixLength = _NtnQosDsL2AccessElemSrcIpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 6),
    _NtnQosDsL2AccessElemSrcIpPrefixLength_Type()
)
ntnQosDsL2AccessElemSrcIpPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemSrcIpPrefixLength.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemSrcIpPrefixLength.setUnits("bits")


class _NtnQosDsL2AccessElemDscp_Type(DscpOrAny):
    """Custom type ntnQosDsL2AccessElemDscp based on DscpOrAny"""
    defaultValue = -1


_NtnQosDsL2AccessElemDscp_Object = MibTableColumn
ntnQosDsL2AccessElemDscp = _NtnQosDsL2AccessElemDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 7),
    _NtnQosDsL2AccessElemDscp_Type()
)
ntnQosDsL2AccessElemDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemDscp.setStatus("current")


class _NtnQosDsL2AccessElemFlowId_Type(FlowIdOrAny):
    """Custom type ntnQosDsL2AccessElemFlowId based on FlowIdOrAny"""
    defaultValue = -1


_NtnQosDsL2AccessElemFlowId_Object = MibTableColumn
ntnQosDsL2AccessElemFlowId = _NtnQosDsL2AccessElemFlowId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 8),
    _NtnQosDsL2AccessElemFlowId_Type()
)
ntnQosDsL2AccessElemFlowId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemFlowId.setStatus("current")


class _NtnQosDsL2AccessElemProtocol_Type(Unsigned32):
    """Custom type ntnQosDsL2AccessElemProtocol based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NtnQosDsL2AccessElemProtocol_Type.__name__ = "Unsigned32"
_NtnQosDsL2AccessElemProtocol_Object = MibTableColumn
ntnQosDsL2AccessElemProtocol = _NtnQosDsL2AccessElemProtocol_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 9),
    _NtnQosDsL2AccessElemProtocol_Type()
)
ntnQosDsL2AccessElemProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemProtocol.setStatus("current")


class _NtnQosDsL2AccessElemDstL4PortMin_Type(InetPortNumber):
    """Custom type ntnQosDsL2AccessElemDstL4PortMin based on InetPortNumber"""
    defaultValue = 0


_NtnQosDsL2AccessElemDstL4PortMin_Object = MibTableColumn
ntnQosDsL2AccessElemDstL4PortMin = _NtnQosDsL2AccessElemDstL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 10),
    _NtnQosDsL2AccessElemDstL4PortMin_Type()
)
ntnQosDsL2AccessElemDstL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemDstL4PortMin.setStatus("current")


class _NtnQosDsL2AccessElemDstL4PortMax_Type(InetPortNumber):
    """Custom type ntnQosDsL2AccessElemDstL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_NtnQosDsL2AccessElemDstL4PortMax_Object = MibTableColumn
ntnQosDsL2AccessElemDstL4PortMax = _NtnQosDsL2AccessElemDstL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 11),
    _NtnQosDsL2AccessElemDstL4PortMax_Type()
)
ntnQosDsL2AccessElemDstL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemDstL4PortMax.setStatus("current")


class _NtnQosDsL2AccessElemSrcL4PortMin_Type(InetPortNumber):
    """Custom type ntnQosDsL2AccessElemSrcL4PortMin based on InetPortNumber"""
    defaultValue = 0


_NtnQosDsL2AccessElemSrcL4PortMin_Object = MibTableColumn
ntnQosDsL2AccessElemSrcL4PortMin = _NtnQosDsL2AccessElemSrcL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 12),
    _NtnQosDsL2AccessElemSrcL4PortMin_Type()
)
ntnQosDsL2AccessElemSrcL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemSrcL4PortMin.setStatus("current")


class _NtnQosDsL2AccessElemSrcL4PortMax_Type(InetPortNumber):
    """Custom type ntnQosDsL2AccessElemSrcL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_NtnQosDsL2AccessElemSrcL4PortMax_Object = MibTableColumn
ntnQosDsL2AccessElemSrcL4PortMax = _NtnQosDsL2AccessElemSrcL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 13),
    _NtnQosDsL2AccessElemSrcL4PortMax_Type()
)
ntnQosDsL2AccessElemSrcL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemSrcL4PortMax.setStatus("current")


class _NtnQosDsL2AccessElemDstMacAddr_Type(MacAddress):
    """Custom type ntnQosDsL2AccessElemDstMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_NtnQosDsL2AccessElemDstMacAddr_Object = MibTableColumn
ntnQosDsL2AccessElemDstMacAddr = _NtnQosDsL2AccessElemDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 14),
    _NtnQosDsL2AccessElemDstMacAddr_Type()
)
ntnQosDsL2AccessElemDstMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemDstMacAddr.setStatus("current")


class _NtnQosDsL2AccessElemDstMacAddrMask_Type(MacAddress):
    """Custom type ntnQosDsL2AccessElemDstMacAddrMask based on MacAddress"""
    defaultHexValue = "000000000000"


_NtnQosDsL2AccessElemDstMacAddrMask_Object = MibTableColumn
ntnQosDsL2AccessElemDstMacAddrMask = _NtnQosDsL2AccessElemDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 15),
    _NtnQosDsL2AccessElemDstMacAddrMask_Type()
)
ntnQosDsL2AccessElemDstMacAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemDstMacAddrMask.setStatus("current")


class _NtnQosDsL2AccessElemSrcMacAddr_Type(MacAddress):
    """Custom type ntnQosDsL2AccessElemSrcMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_NtnQosDsL2AccessElemSrcMacAddr_Object = MibTableColumn
ntnQosDsL2AccessElemSrcMacAddr = _NtnQosDsL2AccessElemSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 16),
    _NtnQosDsL2AccessElemSrcMacAddr_Type()
)
ntnQosDsL2AccessElemSrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemSrcMacAddr.setStatus("current")


class _NtnQosDsL2AccessElemSrcMacAddrMask_Type(MacAddress):
    """Custom type ntnQosDsL2AccessElemSrcMacAddrMask based on MacAddress"""
    defaultHexValue = "000000000000"


_NtnQosDsL2AccessElemSrcMacAddrMask_Object = MibTableColumn
ntnQosDsL2AccessElemSrcMacAddrMask = _NtnQosDsL2AccessElemSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 17),
    _NtnQosDsL2AccessElemSrcMacAddrMask_Type()
)
ntnQosDsL2AccessElemSrcMacAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemSrcMacAddrMask.setStatus("current")


class _NtnQosDsL2AccessElemVlanIdMin_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemVlanIdMin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_NtnQosDsL2AccessElemVlanIdMin_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemVlanIdMin_Object = MibTableColumn
ntnQosDsL2AccessElemVlanIdMin = _NtnQosDsL2AccessElemVlanIdMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 18),
    _NtnQosDsL2AccessElemVlanIdMin_Type()
)
ntnQosDsL2AccessElemVlanIdMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemVlanIdMin.setStatus("current")


class _NtnQosDsL2AccessElemVlanIdMax_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemVlanIdMax based on Integer32"""
    defaultValue = 4094

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_NtnQosDsL2AccessElemVlanIdMax_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemVlanIdMax_Object = MibTableColumn
ntnQosDsL2AccessElemVlanIdMax = _NtnQosDsL2AccessElemVlanIdMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 19),
    _NtnQosDsL2AccessElemVlanIdMax_Type()
)
ntnQosDsL2AccessElemVlanIdMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemVlanIdMax.setStatus("current")


class _NtnQosDsL2AccessElemVlanTag_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemVlanTag based on Integer32"""
    defaultValue = 3

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
        *(("doubleTagged", 4),
          ("ignore", 3),
          ("tagged", 2),
          ("untagged", 1))
    )


_NtnQosDsL2AccessElemVlanTag_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemVlanTag_Object = MibTableColumn
ntnQosDsL2AccessElemVlanTag = _NtnQosDsL2AccessElemVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 20),
    _NtnQosDsL2AccessElemVlanTag_Type()
)
ntnQosDsL2AccessElemVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemVlanTag.setStatus("current")


class _NtnQosDsL2AccessElemEtherType_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemEtherType based on Integer32"""
    defaultHexValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NtnQosDsL2AccessElemEtherType_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemEtherType_Object = MibTableColumn
ntnQosDsL2AccessElemEtherType = _NtnQosDsL2AccessElemEtherType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 21),
    _NtnQosDsL2AccessElemEtherType_Type()
)
ntnQosDsL2AccessElemEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemEtherType.setStatus("current")


class _NtnQosDsL2AccessElemUserPriority_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemUserPriority based on Integer32"""
    defaultValue = 9

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
        *(("matchAllPriorities", 9),
          ("matchPriority0", 1),
          ("matchPriority1", 2),
          ("matchPriority2", 3),
          ("matchPriority3", 4),
          ("matchPriority4", 5),
          ("matchPriority5", 6),
          ("matchPriority6", 7),
          ("matchPriority7", 8))
    )


_NtnQosDsL2AccessElemUserPriority_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemUserPriority_Object = MibTableColumn
ntnQosDsL2AccessElemUserPriority = _NtnQosDsL2AccessElemUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 22),
    _NtnQosDsL2AccessElemUserPriority_Type()
)
ntnQosDsL2AccessElemUserPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemUserPriority.setStatus("current")


class _NtnQosDsL2AccessElemActionDrop_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemActionDrop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_NtnQosDsL2AccessElemActionDrop_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemActionDrop_Object = MibTableColumn
ntnQosDsL2AccessElemActionDrop = _NtnQosDsL2AccessElemActionDrop_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 23),
    _NtnQosDsL2AccessElemActionDrop_Type()
)
ntnQosDsL2AccessElemActionDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemActionDrop.setStatus("current")


class _NtnQosDsL2AccessElemActionRemarkDscp_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemActionRemarkDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_NtnQosDsL2AccessElemActionRemarkDscp_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemActionRemarkDscp_Object = MibTableColumn
ntnQosDsL2AccessElemActionRemarkDscp = _NtnQosDsL2AccessElemActionRemarkDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 24),
    _NtnQosDsL2AccessElemActionRemarkDscp_Type()
)
ntnQosDsL2AccessElemActionRemarkDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemActionRemarkDscp.setStatus("current")


class _NtnQosDsL2AccessElemActionRemarkCos_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemActionRemarkCos based on Integer32"""
    defaultValue = 9

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
              11)
        )
    )
    namedValues = NamedValues(
        *(("deriveFromEgressDscp", 10),
          ("deriveFromIngressTosPrec", 11),
          ("ignore", 9),
          ("markAsPriority0", 1),
          ("markAsPriority1", 2),
          ("markAsPriority2", 3),
          ("markAsPriority3", 4),
          ("markAsPriority4", 5),
          ("markAsPriority5", 6),
          ("markAsPriority6", 7),
          ("markAsPriority7", 8))
    )


_NtnQosDsL2AccessElemActionRemarkCos_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemActionRemarkCos_Object = MibTableColumn
ntnQosDsL2AccessElemActionRemarkCos = _NtnQosDsL2AccessElemActionRemarkCos_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 25),
    _NtnQosDsL2AccessElemActionRemarkCos_Type()
)
ntnQosDsL2AccessElemActionRemarkCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemActionRemarkCos.setStatus("current")


class _NtnQosDsL2AccessElemActionSetPrec_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemActionSetPrec based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highDropPrec", 2),
          ("lowDropPrec", 1))
    )


_NtnQosDsL2AccessElemActionSetPrec_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemActionSetPrec_Object = MibTableColumn
ntnQosDsL2AccessElemActionSetPrec = _NtnQosDsL2AccessElemActionSetPrec_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 26),
    _NtnQosDsL2AccessElemActionSetPrec_Type()
)
ntnQosDsL2AccessElemActionSetPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemActionSetPrec.setStatus("current")


class _NtnQosDsL2AccessElemName_Type(SnmpAdminString):
    """Custom type ntnQosDsL2AccessElemName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtnQosDsL2AccessElemName_Type.__name__ = "SnmpAdminString"
_NtnQosDsL2AccessElemName_Object = MibTableColumn
ntnQosDsL2AccessElemName = _NtnQosDsL2AccessElemName_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 27),
    _NtnQosDsL2AccessElemName_Type()
)
ntnQosDsL2AccessElemName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemName.setStatus("current")


class _NtnQosDsL2AccessElemBlock_Type(SnmpAdminString):
    """Custom type ntnQosDsL2AccessElemBlock based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtnQosDsL2AccessElemBlock_Type.__name__ = "SnmpAdminString"
_NtnQosDsL2AccessElemBlock_Object = MibTableColumn
ntnQosDsL2AccessElemBlock = _NtnQosDsL2AccessElemBlock_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 28),
    _NtnQosDsL2AccessElemBlock_Type()
)
ntnQosDsL2AccessElemBlock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemBlock.setStatus("current")


class _NtnQosDsL2AccessElemType_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dsL2NsnaClfr", 1),
          ("dsL2TrafficProfile", 3),
          ("dsL2UbpClfr", 2))
    )


_NtnQosDsL2AccessElemType_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemType_Object = MibTableColumn
ntnQosDsL2AccessElemType = _NtnQosDsL2AccessElemType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 29),
    _NtnQosDsL2AccessElemType_Type()
)
ntnQosDsL2AccessElemType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemType.setStatus("current")


class _NtnQosDsL2AccessElemStorage_Type(StorageType):
    """Custom type ntnQosDsL2AccessElemStorage based on StorageType"""


_NtnQosDsL2AccessElemStorage_Object = MibTableColumn
ntnQosDsL2AccessElemStorage = _NtnQosDsL2AccessElemStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 30),
    _NtnQosDsL2AccessElemStorage_Type()
)
ntnQosDsL2AccessElemStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemStorage.setStatus("current")
_NtnQosDsL2AccessElemStatus_Type = RowStatus
_NtnQosDsL2AccessElemStatus_Object = MibTableColumn
ntnQosDsL2AccessElemStatus = _NtnQosDsL2AccessElemStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 31),
    _NtnQosDsL2AccessElemStatus_Type()
)
ntnQosDsL2AccessElemStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemStatus.setStatus("current")


class _NtnQosDsL2AccessElemEvalPrec_Type(Unsigned32):
    """Custom type ntnQosDsL2AccessElemEvalPrec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NtnQosDsL2AccessElemEvalPrec_Type.__name__ = "Unsigned32"
_NtnQosDsL2AccessElemEvalPrec_Object = MibTableColumn
ntnQosDsL2AccessElemEvalPrec = _NtnQosDsL2AccessElemEvalPrec_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 32),
    _NtnQosDsL2AccessElemEvalPrec_Type()
)
ntnQosDsL2AccessElemEvalPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemEvalPrec.setStatus("current")


class _NtnQosDsL2AccessElemIpFlags_Type(Bits):
    """Custom type ntnQosDsL2AccessElemIpFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("ipv4DfFlagSet", 1),
          ("ipv4MfFlagSet", 0))
    )

_NtnQosDsL2AccessElemIpFlags_Type.__name__ = "Bits"
_NtnQosDsL2AccessElemIpFlags_Object = MibTableColumn
ntnQosDsL2AccessElemIpFlags = _NtnQosDsL2AccessElemIpFlags_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 33),
    _NtnQosDsL2AccessElemIpFlags_Type()
)
ntnQosDsL2AccessElemIpFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemIpFlags.setStatus("current")


class _NtnQosDsL2AccessElemTcpCtrlFlags_Type(Bits):
    """Custom type ntnQosDsL2AccessElemTcpCtrlFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("tcpAckFlagSet", 1),
          ("tcpFinFlagSet", 5),
          ("tcpPshFlagSet", 2),
          ("tcpRstFlagSet", 3),
          ("tcpSynFlagSet", 4),
          ("tcpUrgFlagSet", 0))
    )

_NtnQosDsL2AccessElemTcpCtrlFlags_Type.__name__ = "Bits"
_NtnQosDsL2AccessElemTcpCtrlFlags_Object = MibTableColumn
ntnQosDsL2AccessElemTcpCtrlFlags = _NtnQosDsL2AccessElemTcpCtrlFlags_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 34),
    _NtnQosDsL2AccessElemTcpCtrlFlags_Type()
)
ntnQosDsL2AccessElemTcpCtrlFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemTcpCtrlFlags.setStatus("current")


class _NtnQosDsL2AccessElemIpv4Options_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemIpv4Options based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 3),
          ("ipv4OptionsNotPresent", 2),
          ("ipv4OptionsPresent", 1))
    )


_NtnQosDsL2AccessElemIpv4Options_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemIpv4Options_Object = MibTableColumn
ntnQosDsL2AccessElemIpv4Options = _NtnQosDsL2AccessElemIpv4Options_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 35),
    _NtnQosDsL2AccessElemIpv4Options_Type()
)
ntnQosDsL2AccessElemIpv4Options.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemIpv4Options.setStatus("current")


class _NtnQosDsL2AccessElemPktType_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemPktType based on Integer32"""
    defaultValue = 4

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
        *(("ethernetII", 1),
          ("ignore", 4),
          ("llc", 3),
          ("snap", 2))
    )


_NtnQosDsL2AccessElemPktType_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemPktType_Object = MibTableColumn
ntnQosDsL2AccessElemPktType = _NtnQosDsL2AccessElemPktType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 36),
    _NtnQosDsL2AccessElemPktType_Type()
)
ntnQosDsL2AccessElemPktType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemPktType.setStatus("current")


class _NtnQosDsL2AccessElemIvidMin_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemIvidMin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_NtnQosDsL2AccessElemIvidMin_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemIvidMin_Object = MibTableColumn
ntnQosDsL2AccessElemIvidMin = _NtnQosDsL2AccessElemIvidMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 37),
    _NtnQosDsL2AccessElemIvidMin_Type()
)
ntnQosDsL2AccessElemIvidMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemIvidMin.setStatus("current")


class _NtnQosDsL2AccessElemIvidMax_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemIvidMax based on Integer32"""
    defaultValue = 4094

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_NtnQosDsL2AccessElemIvidMax_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemIvidMax_Object = MibTableColumn
ntnQosDsL2AccessElemIvidMax = _NtnQosDsL2AccessElemIvidMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 38),
    _NtnQosDsL2AccessElemIvidMax_Type()
)
ntnQosDsL2AccessElemIvidMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemIvidMax.setStatus("current")


class _NtnQosDsL2AccessElemUnknownUcastFrames_Type(TruthValue):
    """Custom type ntnQosDsL2AccessElemUnknownUcastFrames based on TruthValue"""


_NtnQosDsL2AccessElemUnknownUcastFrames_Object = MibTableColumn
ntnQosDsL2AccessElemUnknownUcastFrames = _NtnQosDsL2AccessElemUnknownUcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 39),
    _NtnQosDsL2AccessElemUnknownUcastFrames_Type()
)
ntnQosDsL2AccessElemUnknownUcastFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemUnknownUcastFrames.setStatus("current")


class _NtnQosDsL2AccessElemUnknownMcastFrames_Type(TruthValue):
    """Custom type ntnQosDsL2AccessElemUnknownMcastFrames based on TruthValue"""


_NtnQosDsL2AccessElemUnknownMcastFrames_Object = MibTableColumn
ntnQosDsL2AccessElemUnknownMcastFrames = _NtnQosDsL2AccessElemUnknownMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 40),
    _NtnQosDsL2AccessElemUnknownMcastFrames_Type()
)
ntnQosDsL2AccessElemUnknownMcastFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemUnknownMcastFrames.setStatus("current")


class _NtnQosDsL2AccessElemKnownUcastFrames_Type(TruthValue):
    """Custom type ntnQosDsL2AccessElemKnownUcastFrames based on TruthValue"""


_NtnQosDsL2AccessElemKnownUcastFrames_Object = MibTableColumn
ntnQosDsL2AccessElemKnownUcastFrames = _NtnQosDsL2AccessElemKnownUcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 41),
    _NtnQosDsL2AccessElemKnownUcastFrames_Type()
)
ntnQosDsL2AccessElemKnownUcastFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemKnownUcastFrames.setStatus("current")


class _NtnQosDsL2AccessElemKnownMcastFrames_Type(TruthValue):
    """Custom type ntnQosDsL2AccessElemKnownMcastFrames based on TruthValue"""


_NtnQosDsL2AccessElemKnownMcastFrames_Object = MibTableColumn
ntnQosDsL2AccessElemKnownMcastFrames = _NtnQosDsL2AccessElemKnownMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 42),
    _NtnQosDsL2AccessElemKnownMcastFrames_Type()
)
ntnQosDsL2AccessElemKnownMcastFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemKnownMcastFrames.setStatus("current")


class _NtnQosDsL2AccessElemBcastFrames_Type(TruthValue):
    """Custom type ntnQosDsL2AccessElemBcastFrames based on TruthValue"""


_NtnQosDsL2AccessElemBcastFrames_Object = MibTableColumn
ntnQosDsL2AccessElemBcastFrames = _NtnQosDsL2AccessElemBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 43),
    _NtnQosDsL2AccessElemBcastFrames_Type()
)
ntnQosDsL2AccessElemBcastFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemBcastFrames.setStatus("current")


class _NtnQosDsL2AccessElemUnknownIpMcast_Type(TruthValue):
    """Custom type ntnQosDsL2AccessElemUnknownIpMcast based on TruthValue"""


_NtnQosDsL2AccessElemUnknownIpMcast_Object = MibTableColumn
ntnQosDsL2AccessElemUnknownIpMcast = _NtnQosDsL2AccessElemUnknownIpMcast_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 44),
    _NtnQosDsL2AccessElemUnknownIpMcast_Type()
)
ntnQosDsL2AccessElemUnknownIpMcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemUnknownIpMcast.setStatus("current")


class _NtnQosDsL2AccessElemKnownIpMcast_Type(TruthValue):
    """Custom type ntnQosDsL2AccessElemKnownIpMcast based on TruthValue"""


_NtnQosDsL2AccessElemKnownIpMcast_Object = MibTableColumn
ntnQosDsL2AccessElemKnownIpMcast = _NtnQosDsL2AccessElemKnownIpMcast_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 45),
    _NtnQosDsL2AccessElemKnownIpMcast_Type()
)
ntnQosDsL2AccessElemKnownIpMcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemKnownIpMcast.setStatus("current")


class _NtnQosDsL2AccessElemNonIpPkt_Type(TruthValue):
    """Custom type ntnQosDsL2AccessElemNonIpPkt based on TruthValue"""


_NtnQosDsL2AccessElemNonIpPkt_Object = MibTableColumn
ntnQosDsL2AccessElemNonIpPkt = _NtnQosDsL2AccessElemNonIpPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 46),
    _NtnQosDsL2AccessElemNonIpPkt_Type()
)
ntnQosDsL2AccessElemNonIpPkt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemNonIpPkt.setStatus("current")


class _NtnQosDsL2AccessElemVersion_Type(VersionIndicator):
    """Custom type ntnQosDsL2AccessElemVersion based on VersionIndicator"""


_NtnQosDsL2AccessElemVersion_Object = MibTableColumn
ntnQosDsL2AccessElemVersion = _NtnQosDsL2AccessElemVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 47),
    _NtnQosDsL2AccessElemVersion_Type()
)
ntnQosDsL2AccessElemVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemVersion.setStatus("current")


class _NtnQosDsL2AccessElemUnknownNonIpMcast_Type(TruthValue):
    """Custom type ntnQosDsL2AccessElemUnknownNonIpMcast based on TruthValue"""


_NtnQosDsL2AccessElemUnknownNonIpMcast_Object = MibTableColumn
ntnQosDsL2AccessElemUnknownNonIpMcast = _NtnQosDsL2AccessElemUnknownNonIpMcast_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 48),
    _NtnQosDsL2AccessElemUnknownNonIpMcast_Type()
)
ntnQosDsL2AccessElemUnknownNonIpMcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemUnknownNonIpMcast.setStatus("current")


class _NtnQosDsL2AccessElemKnownNonIpMcast_Type(TruthValue):
    """Custom type ntnQosDsL2AccessElemKnownNonIpMcast based on TruthValue"""


_NtnQosDsL2AccessElemKnownNonIpMcast_Object = MibTableColumn
ntnQosDsL2AccessElemKnownNonIpMcast = _NtnQosDsL2AccessElemKnownNonIpMcast_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 49),
    _NtnQosDsL2AccessElemKnownNonIpMcast_Type()
)
ntnQosDsL2AccessElemKnownNonIpMcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemKnownNonIpMcast.setStatus("current")


class _NtnQosDsL2AccessElemMasterBlockMember_Type(TruthValue):
    """Custom type ntnQosDsL2AccessElemMasterBlockMember based on TruthValue"""


_NtnQosDsL2AccessElemMasterBlockMember_Object = MibTableColumn
ntnQosDsL2AccessElemMasterBlockMember = _NtnQosDsL2AccessElemMasterBlockMember_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 50),
    _NtnQosDsL2AccessElemMasterBlockMember_Type()
)
ntnQosDsL2AccessElemMasterBlockMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemMasterBlockMember.setStatus("current")


class _NtnQosDsL2AccessElemMeterType_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemMeterType based on Integer32"""
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
        *(("simpleTokenBucket", 1),
          ("srTCMAware", 3),
          ("srTCMBlind", 2),
          ("trTCMAware", 5),
          ("trTCMBlind", 4))
    )


_NtnQosDsL2AccessElemMeterType_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemMeterType_Object = MibTableColumn
ntnQosDsL2AccessElemMeterType = _NtnQosDsL2AccessElemMeterType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 51),
    _NtnQosDsL2AccessElemMeterType_Type()
)
ntnQosDsL2AccessElemMeterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemMeterType.setStatus("current")


class _NtnQosDsL2AccessElemRate_Type(Unsigned32):
    """Custom type ntnQosDsL2AccessElemRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NtnQosDsL2AccessElemRate_Type.__name__ = "Unsigned32"
_NtnQosDsL2AccessElemRate_Object = MibTableColumn
ntnQosDsL2AccessElemRate = _NtnQosDsL2AccessElemRate_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 52),
    _NtnQosDsL2AccessElemRate_Type()
)
ntnQosDsL2AccessElemRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemRate.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemRate.setUnits("kilobits per second")


class _NtnQosDsL2AccessElemBurstSize_Type(BurstSize):
    """Custom type ntnQosDsL2AccessElemBurstSize based on BurstSize"""
    defaultValue = 0


_NtnQosDsL2AccessElemBurstSize_Object = MibTableColumn
ntnQosDsL2AccessElemBurstSize = _NtnQosDsL2AccessElemBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 53),
    _NtnQosDsL2AccessElemBurstSize_Type()
)
ntnQosDsL2AccessElemBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemBurstSize.setUnits("Bytes")


class _NtnQosDsL2AccessElemOutActionDrop_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemOutActionDrop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_NtnQosDsL2AccessElemOutActionDrop_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemOutActionDrop_Object = MibTableColumn
ntnQosDsL2AccessElemOutActionDrop = _NtnQosDsL2AccessElemOutActionDrop_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 54),
    _NtnQosDsL2AccessElemOutActionDrop_Type()
)
ntnQosDsL2AccessElemOutActionDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemOutActionDrop.setStatus("current")


class _NtnQosDsL2AccessElemOutActionRemarkDscp_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemOutActionRemarkDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_NtnQosDsL2AccessElemOutActionRemarkDscp_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemOutActionRemarkDscp_Object = MibTableColumn
ntnQosDsL2AccessElemOutActionRemarkDscp = _NtnQosDsL2AccessElemOutActionRemarkDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 55),
    _NtnQosDsL2AccessElemOutActionRemarkDscp_Type()
)
ntnQosDsL2AccessElemOutActionRemarkDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemOutActionRemarkDscp.setStatus("current")


class _NtnQosDsL2AccessElemOutActionRemarkCos_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemOutActionRemarkCos based on Integer32"""
    defaultValue = 9

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
              11)
        )
    )
    namedValues = NamedValues(
        *(("deriveFromEgressDscp", 10),
          ("deriveFromIngressTosPrec", 11),
          ("ignore", 9),
          ("markAsPriority0", 1),
          ("markAsPriority1", 2),
          ("markAsPriority2", 3),
          ("markAsPriority3", 4),
          ("markAsPriority4", 5),
          ("markAsPriority5", 6),
          ("markAsPriority6", 7),
          ("markAsPriority7", 8))
    )


_NtnQosDsL2AccessElemOutActionRemarkCos_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemOutActionRemarkCos_Object = MibTableColumn
ntnQosDsL2AccessElemOutActionRemarkCos = _NtnQosDsL2AccessElemOutActionRemarkCos_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 56),
    _NtnQosDsL2AccessElemOutActionRemarkCos_Type()
)
ntnQosDsL2AccessElemOutActionRemarkCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemOutActionRemarkCos.setStatus("current")


class _NtnQosDsL2AccessElemOutActionSetPrec_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemOutActionSetPrec based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highDropPrec", 2),
          ("lowDropPrec", 1))
    )


_NtnQosDsL2AccessElemOutActionSetPrec_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemOutActionSetPrec_Object = MibTableColumn
ntnQosDsL2AccessElemOutActionSetPrec = _NtnQosDsL2AccessElemOutActionSetPrec_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 57),
    _NtnQosDsL2AccessElemOutActionSetPrec_Type()
)
ntnQosDsL2AccessElemOutActionSetPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemOutActionSetPrec.setStatus("current")


class _NtnQosDsL2AccessElemSecondaryRate_Type(Unsigned32):
    """Custom type ntnQosDsL2AccessElemSecondaryRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NtnQosDsL2AccessElemSecondaryRate_Type.__name__ = "Unsigned32"
_NtnQosDsL2AccessElemSecondaryRate_Object = MibTableColumn
ntnQosDsL2AccessElemSecondaryRate = _NtnQosDsL2AccessElemSecondaryRate_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 58),
    _NtnQosDsL2AccessElemSecondaryRate_Type()
)
ntnQosDsL2AccessElemSecondaryRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemSecondaryRate.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemSecondaryRate.setUnits("kilobits per second")


class _NtnQosDsL2AccessElemSecondaryBurstSize_Type(BurstSize):
    """Custom type ntnQosDsL2AccessElemSecondaryBurstSize based on BurstSize"""
    defaultValue = 0


_NtnQosDsL2AccessElemSecondaryBurstSize_Object = MibTableColumn
ntnQosDsL2AccessElemSecondaryBurstSize = _NtnQosDsL2AccessElemSecondaryBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 59),
    _NtnQosDsL2AccessElemSecondaryBurstSize_Type()
)
ntnQosDsL2AccessElemSecondaryBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemSecondaryBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemSecondaryBurstSize.setUnits("Bytes")


class _NtnQosDsL2AccessElemYelActionDrop_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemYelActionDrop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("pass", 2))
    )


_NtnQosDsL2AccessElemYelActionDrop_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemYelActionDrop_Object = MibTableColumn
ntnQosDsL2AccessElemYelActionDrop = _NtnQosDsL2AccessElemYelActionDrop_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 60),
    _NtnQosDsL2AccessElemYelActionDrop_Type()
)
ntnQosDsL2AccessElemYelActionDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemYelActionDrop.setStatus("current")


class _NtnQosDsL2AccessElemYelActionRemarkDscp_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemYelActionRemarkDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_NtnQosDsL2AccessElemYelActionRemarkDscp_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemYelActionRemarkDscp_Object = MibTableColumn
ntnQosDsL2AccessElemYelActionRemarkDscp = _NtnQosDsL2AccessElemYelActionRemarkDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 61),
    _NtnQosDsL2AccessElemYelActionRemarkDscp_Type()
)
ntnQosDsL2AccessElemYelActionRemarkDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemYelActionRemarkDscp.setStatus("current")


class _NtnQosDsL2AccessElemYelActionRemarkCos_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemYelActionRemarkCos based on Integer32"""
    defaultValue = 9

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
              11)
        )
    )
    namedValues = NamedValues(
        *(("deriveFromEgressDscp", 10),
          ("deriveFromIngressTosPrec", 11),
          ("ignore", 9),
          ("markAsPriority0", 1),
          ("markAsPriority1", 2),
          ("markAsPriority2", 3),
          ("markAsPriority3", 4),
          ("markAsPriority4", 5),
          ("markAsPriority5", 6),
          ("markAsPriority6", 7),
          ("markAsPriority7", 8))
    )


_NtnQosDsL2AccessElemYelActionRemarkCos_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemYelActionRemarkCos_Object = MibTableColumn
ntnQosDsL2AccessElemYelActionRemarkCos = _NtnQosDsL2AccessElemYelActionRemarkCos_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 62),
    _NtnQosDsL2AccessElemYelActionRemarkCos_Type()
)
ntnQosDsL2AccessElemYelActionRemarkCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemYelActionRemarkCos.setStatus("current")


class _NtnQosDsL2AccessElemYelActionSetPrec_Type(Integer32):
    """Custom type ntnQosDsL2AccessElemYelActionSetPrec based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highDropPrec", 2),
          ("lowDropPrec", 1))
    )


_NtnQosDsL2AccessElemYelActionSetPrec_Type.__name__ = "Integer32"
_NtnQosDsL2AccessElemYelActionSetPrec_Object = MibTableColumn
ntnQosDsL2AccessElemYelActionSetPrec = _NtnQosDsL2AccessElemYelActionSetPrec_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 11, 1, 63),
    _NtnQosDsL2AccessElemYelActionSetPrec_Type()
)
ntnQosDsL2AccessElemYelActionSetPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemYelActionSetPrec.setStatus("current")
_NtnQosFilterSetStatsTable_Object = MibTable
ntnQosFilterSetStatsTable = _NtnQosFilterSetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 12)
)
if mibBuilder.loadTexts:
    ntnQosFilterSetStatsTable.setStatus("current")
_NtnQosFilterSetStatsEntry_Object = MibTableRow
ntnQosFilterSetStatsEntry = _NtnQosFilterSetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 12, 1)
)
ntnQosFilterSetStatsEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterSetStatsAccessAsgnId"),
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterSetStatsPrecedence"),
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterSetStatsEvalOrder"),
)
if mibBuilder.loadTexts:
    ntnQosFilterSetStatsEntry.setStatus("current")
_NtnQosFilterSetStatsAccessAsgnId_Type = IndexInteger
_NtnQosFilterSetStatsAccessAsgnId_Object = MibTableColumn
ntnQosFilterSetStatsAccessAsgnId = _NtnQosFilterSetStatsAccessAsgnId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 12, 1, 1),
    _NtnQosFilterSetStatsAccessAsgnId_Type()
)
ntnQosFilterSetStatsAccessAsgnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosFilterSetStatsAccessAsgnId.setStatus("current")
_NtnQosFilterSetStatsPrecedence_Type = IndexInteger
_NtnQosFilterSetStatsPrecedence_Object = MibTableColumn
ntnQosFilterSetStatsPrecedence = _NtnQosFilterSetStatsPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 12, 1, 2),
    _NtnQosFilterSetStatsPrecedence_Type()
)
ntnQosFilterSetStatsPrecedence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosFilterSetStatsPrecedence.setStatus("current")
_NtnQosFilterSetStatsEvalOrder_Type = IndexInteger
_NtnQosFilterSetStatsEvalOrder_Object = MibTableColumn
ntnQosFilterSetStatsEvalOrder = _NtnQosFilterSetStatsEvalOrder_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 12, 1, 3),
    _NtnQosFilterSetStatsEvalOrder_Type()
)
ntnQosFilterSetStatsEvalOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosFilterSetStatsEvalOrder.setStatus("current")
_NtnQosFilterSetStatsInProfileOctets_Type = Counter64
_NtnQosFilterSetStatsInProfileOctets_Object = MibTableColumn
ntnQosFilterSetStatsInProfileOctets = _NtnQosFilterSetStatsInProfileOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 12, 1, 4),
    _NtnQosFilterSetStatsInProfileOctets_Type()
)
ntnQosFilterSetStatsInProfileOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosFilterSetStatsInProfileOctets.setStatus("current")
_NtnQosFilterSetStatsInProfilePkts_Type = Counter64
_NtnQosFilterSetStatsInProfilePkts_Object = MibTableColumn
ntnQosFilterSetStatsInProfilePkts = _NtnQosFilterSetStatsInProfilePkts_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 12, 1, 5),
    _NtnQosFilterSetStatsInProfilePkts_Type()
)
ntnQosFilterSetStatsInProfilePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosFilterSetStatsInProfilePkts.setStatus("current")
_NtnQosFilterSetStatsOutOfProfileOctets_Type = Counter64
_NtnQosFilterSetStatsOutOfProfileOctets_Object = MibTableColumn
ntnQosFilterSetStatsOutOfProfileOctets = _NtnQosFilterSetStatsOutOfProfileOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 12, 1, 6),
    _NtnQosFilterSetStatsOutOfProfileOctets_Type()
)
ntnQosFilterSetStatsOutOfProfileOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosFilterSetStatsOutOfProfileOctets.setStatus("current")
_NtnQosFilterSetStatsOutOfProfilePkts_Type = Counter64
_NtnQosFilterSetStatsOutOfProfilePkts_Object = MibTableColumn
ntnQosFilterSetStatsOutOfProfilePkts = _NtnQosFilterSetStatsOutOfProfilePkts_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 12, 1, 7),
    _NtnQosFilterSetStatsOutOfProfilePkts_Type()
)
ntnQosFilterSetStatsOutOfProfilePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosFilterSetStatsOutOfProfilePkts.setStatus("current")
_NtnQosFilterSetStatsAccessElemId_Type = Integer32
_NtnQosFilterSetStatsAccessElemId_Object = MibTableColumn
ntnQosFilterSetStatsAccessElemId = _NtnQosFilterSetStatsAccessElemId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 12, 1, 8),
    _NtnQosFilterSetStatsAccessElemId_Type()
)
ntnQosFilterSetStatsAccessElemId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosFilterSetStatsAccessElemId.setStatus("current")


class _NtnQosFilterSetStatsStorage_Type(StorageType):
    """Custom type ntnQosFilterSetStatsStorage based on StorageType"""


_NtnQosFilterSetStatsStorage_Object = MibTableColumn
ntnQosFilterSetStatsStorage = _NtnQosFilterSetStatsStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 12, 1, 9),
    _NtnQosFilterSetStatsStorage_Type()
)
ntnQosFilterSetStatsStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosFilterSetStatsStorage.setStatus("current")
_NtnQosFilterSetStatsStatus_Type = RowStatus
_NtnQosFilterSetStatsStatus_Object = MibTableColumn
ntnQosFilterSetStatsStatus = _NtnQosFilterSetStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 12, 1, 10),
    _NtnQosFilterSetStatsStatus_Type()
)
ntnQosFilterSetStatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntnQosFilterSetStatsStatus.setStatus("current")
_AvFcoeRedirNextFree_Type = IndexIntegerNextFree
_AvFcoeRedirNextFree_Object = MibScalar
avFcoeRedirNextFree = _AvFcoeRedirNextFree_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 13),
    _AvFcoeRedirNextFree_Type()
)
avFcoeRedirNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFcoeRedirNextFree.setStatus("current")
_AvFcoeRedirTable_Object = MibTable
avFcoeRedirTable = _AvFcoeRedirTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 14)
)
if mibBuilder.loadTexts:
    avFcoeRedirTable.setStatus("current")
_AvFcoeRedirEntry_Object = MibTableRow
avFcoeRedirEntry = _AvFcoeRedirEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 14, 1)
)
avFcoeRedirEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirId"),
)
if mibBuilder.loadTexts:
    avFcoeRedirEntry.setStatus("current")
_AvFcoeRedirId_Type = IndexInteger
_AvFcoeRedirId_Object = MibTableColumn
avFcoeRedirId = _AvFcoeRedirId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 14, 1, 1),
    _AvFcoeRedirId_Type()
)
avFcoeRedirId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avFcoeRedirId.setStatus("current")
_AvFcoeRedirDstId_Type = FcId
_AvFcoeRedirDstId_Object = MibTableColumn
avFcoeRedirDstId = _AvFcoeRedirDstId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 14, 1, 2),
    _AvFcoeRedirDstId_Type()
)
avFcoeRedirDstId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFcoeRedirDstId.setStatus("current")
_AvFcoeRedirIngressInterfaceList_Type = InterfaceList
_AvFcoeRedirIngressInterfaceList_Object = MibTableColumn
avFcoeRedirIngressInterfaceList = _AvFcoeRedirIngressInterfaceList_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 14, 1, 3),
    _AvFcoeRedirIngressInterfaceList_Type()
)
avFcoeRedirIngressInterfaceList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFcoeRedirIngressInterfaceList.setStatus("current")


class _AvFcoeRedirVlanIdMin_Type(Integer32):
    """Custom type avFcoeRedirVlanIdMin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AvFcoeRedirVlanIdMin_Type.__name__ = "Integer32"
_AvFcoeRedirVlanIdMin_Object = MibTableColumn
avFcoeRedirVlanIdMin = _AvFcoeRedirVlanIdMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 14, 1, 4),
    _AvFcoeRedirVlanIdMin_Type()
)
avFcoeRedirVlanIdMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFcoeRedirVlanIdMin.setStatus("current")


class _AvFcoeRedirVlanIdMax_Type(Integer32):
    """Custom type avFcoeRedirVlanIdMax based on Integer32"""
    defaultValue = 4094

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AvFcoeRedirVlanIdMax_Type.__name__ = "Integer32"
_AvFcoeRedirVlanIdMax_Object = MibTableColumn
avFcoeRedirVlanIdMax = _AvFcoeRedirVlanIdMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 14, 1, 5),
    _AvFcoeRedirVlanIdMax_Type()
)
avFcoeRedirVlanIdMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFcoeRedirVlanIdMax.setStatus("current")


class _AvFcoeRedirUserPriority_Type(Integer32):
    """Custom type avFcoeRedirUserPriority based on Integer32"""
    defaultValue = 9

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
        *(("matchAllPriorities", 9),
          ("matchPriority0", 1),
          ("matchPriority1", 2),
          ("matchPriority2", 3),
          ("matchPriority3", 4),
          ("matchPriority4", 5),
          ("matchPriority5", 6),
          ("matchPriority6", 7),
          ("matchPriority7", 8))
    )


_AvFcoeRedirUserPriority_Type.__name__ = "Integer32"
_AvFcoeRedirUserPriority_Object = MibTableColumn
avFcoeRedirUserPriority = _AvFcoeRedirUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 14, 1, 6),
    _AvFcoeRedirUserPriority_Type()
)
avFcoeRedirUserPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFcoeRedirUserPriority.setStatus("current")


class _AvFcoeRedirEtherType_Type(Integer32):
    """Custom type avFcoeRedirEtherType based on Integer32"""
    defaultHexValue = 35078

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AvFcoeRedirEtherType_Type.__name__ = "Integer32"
_AvFcoeRedirEtherType_Object = MibTableColumn
avFcoeRedirEtherType = _AvFcoeRedirEtherType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 14, 1, 7),
    _AvFcoeRedirEtherType_Type()
)
avFcoeRedirEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFcoeRedirEtherType.setStatus("current")


class _AvFcoeRedirSrcId_Type(FcId):
    """Custom type avFcoeRedirSrcId based on FcId"""
    defaultHexValue = "000000"


_AvFcoeRedirSrcId_Object = MibTableColumn
avFcoeRedirSrcId = _AvFcoeRedirSrcId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 14, 1, 8),
    _AvFcoeRedirSrcId_Type()
)
avFcoeRedirSrcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFcoeRedirSrcId.setStatus("current")
_AvFcoeRedirActionUpdateDstMac_Type = MacAddress
_AvFcoeRedirActionUpdateDstMac_Object = MibTableColumn
avFcoeRedirActionUpdateDstMac = _AvFcoeRedirActionUpdateDstMac_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 14, 1, 9),
    _AvFcoeRedirActionUpdateDstMac_Type()
)
avFcoeRedirActionUpdateDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFcoeRedirActionUpdateDstMac.setStatus("current")
_AvFcoeRedirActionUpdateSrcMac_Type = MacAddress
_AvFcoeRedirActionUpdateSrcMac_Object = MibTableColumn
avFcoeRedirActionUpdateSrcMac = _AvFcoeRedirActionUpdateSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 14, 1, 10),
    _AvFcoeRedirActionUpdateSrcMac_Type()
)
avFcoeRedirActionUpdateSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFcoeRedirActionUpdateSrcMac.setStatus("current")
_AvFcoeRedirActionEgressInterface_Type = InterfaceIndexOrZero
_AvFcoeRedirActionEgressInterface_Object = MibTableColumn
avFcoeRedirActionEgressInterface = _AvFcoeRedirActionEgressInterface_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 14, 1, 11),
    _AvFcoeRedirActionEgressInterface_Type()
)
avFcoeRedirActionEgressInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFcoeRedirActionEgressInterface.setStatus("current")


class _AvFcoeRedirName_Type(SnmpAdminString):
    """Custom type avFcoeRedirName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AvFcoeRedirName_Type.__name__ = "SnmpAdminString"
_AvFcoeRedirName_Object = MibTableColumn
avFcoeRedirName = _AvFcoeRedirName_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 14, 1, 12),
    _AvFcoeRedirName_Type()
)
avFcoeRedirName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFcoeRedirName.setStatus("current")


class _AvFcoeRedirStorage_Type(StorageType):
    """Custom type avFcoeRedirStorage based on StorageType"""


_AvFcoeRedirStorage_Object = MibTableColumn
avFcoeRedirStorage = _AvFcoeRedirStorage_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 14, 1, 13),
    _AvFcoeRedirStorage_Type()
)
avFcoeRedirStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFcoeRedirStorage.setStatus("current")
_AvFcoeRedirStatus_Type = RowStatus
_AvFcoeRedirStatus_Object = MibTableColumn
avFcoeRedirStatus = _AvFcoeRedirStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 14, 1, 14),
    _AvFcoeRedirStatus_Type()
)
avFcoeRedirStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFcoeRedirStatus.setStatus("current")
_AvFcoeRedirProcessedFrames_Type = Counter64
_AvFcoeRedirProcessedFrames_Object = MibTableColumn
avFcoeRedirProcessedFrames = _AvFcoeRedirProcessedFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 14, 1, 15),
    _AvFcoeRedirProcessedFrames_Type()
)
avFcoeRedirProcessedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFcoeRedirProcessedFrames.setStatus("current")


class _AvFcoeRedirActionEgressTrunkId_Type(Integer32):
    """Custom type avFcoeRedirActionEgressTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_AvFcoeRedirActionEgressTrunkId_Type.__name__ = "Integer32"
_AvFcoeRedirActionEgressTrunkId_Object = MibTableColumn
avFcoeRedirActionEgressTrunkId = _AvFcoeRedirActionEgressTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 13, 14, 1, 16),
    _AvFcoeRedirActionEgressTrunkId_Type()
)
avFcoeRedirActionEgressTrunkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFcoeRedirActionEgressTrunkId.setStatus("current")
_NtnQosDEITable_Object = MibTable
ntnQosDEITable = _NtnQosDEITable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 14)
)
if mibBuilder.loadTexts:
    ntnQosDEITable.setStatus("current")
_NtnQosDEIEntry_Object = MibTableRow
ntnQosDEIEntry = _NtnQosDEIEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 14, 1)
)
ntnQosDEIEntry.setIndexNames(
    (0, "NTN-QOS-POLICY-EVOL-PIB", "ntnQosDEIInterfaceId"),
)
if mibBuilder.loadTexts:
    ntnQosDEIEntry.setStatus("current")
_NtnQosDEIInterfaceId_Type = InterfaceIndex
_NtnQosDEIInterfaceId_Object = MibTableColumn
ntnQosDEIInterfaceId = _NtnQosDEIInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 14, 1, 1),
    _NtnQosDEIInterfaceId_Type()
)
ntnQosDEIInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntnQosDEIInterfaceId.setStatus("current")
_NtnQosDEIIngressColorFromDEI_Type = TruthValue
_NtnQosDEIIngressColorFromDEI_Object = MibTableColumn
ntnQosDEIIngressColorFromDEI = _NtnQosDEIIngressColorFromDEI_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 14, 1, 2),
    _NtnQosDEIIngressColorFromDEI_Type()
)
ntnQosDEIIngressColorFromDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosDEIIngressColorFromDEI.setStatus("current")
_NtnQosDEIEgressMarkDEI_Type = TruthValue
_NtnQosDEIEgressMarkDEI_Object = MibTableColumn
ntnQosDEIEgressMarkDEI = _NtnQosDEIEgressMarkDEI_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 14, 1, 3),
    _NtnQosDEIEgressMarkDEI_Type()
)
ntnQosDEIEgressMarkDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosDEIEgressMarkDEI.setStatus("current")
_NtnQosQuickPolicy_ObjectIdentity = ObjectIdentity
ntnQosQuickPolicy = _NtnQosQuickPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15)
)


class _NtnQosQuickPolicyControl_Type(Integer32):
    """Custom type ntnQosQuickPolicyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 2),
          ("delete", 3),
          ("none", 1))
    )


_NtnQosQuickPolicyControl_Type.__name__ = "Integer32"
_NtnQosQuickPolicyControl_Object = MibScalar
ntnQosQuickPolicyControl = _NtnQosQuickPolicyControl_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 1),
    _NtnQosQuickPolicyControl_Type()
)
ntnQosQuickPolicyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyControl.setStatus("current")
_NtnQosQuickPolicyPortList_Type = PortList
_NtnQosQuickPolicyPortList_Object = MibScalar
ntnQosQuickPolicyPortList = _NtnQosQuickPolicyPortList_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 2),
    _NtnQosQuickPolicyPortList_Type()
)
ntnQosQuickPolicyPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyPortList.setStatus("current")


class _NtnQosQuickPolicyAction_Type(Integer32):
    """Custom type ntnQosQuickPolicyAction based on Integer32"""
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
        *(("forward", 1),
          ("pbits", 2),
          ("rate", 3),
          ("trtcm", 4))
    )


_NtnQosQuickPolicyAction_Type.__name__ = "Integer32"
_NtnQosQuickPolicyAction_Object = MibScalar
ntnQosQuickPolicyAction = _NtnQosQuickPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 3),
    _NtnQosQuickPolicyAction_Type()
)
ntnQosQuickPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyAction.setStatus("current")
_NtnQosQuickPolicyId_Type = IndexInteger
_NtnQosQuickPolicyId_Object = MibScalar
ntnQosQuickPolicyId = _NtnQosQuickPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 4),
    _NtnQosQuickPolicyId_Type()
)
ntnQosQuickPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyId.setStatus("current")


class _NtnQosQuickPolicyPbitsValue_Type(Integer32):
    """Custom type ntnQosQuickPolicyPbitsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NtnQosQuickPolicyPbitsValue_Type.__name__ = "Integer32"
_NtnQosQuickPolicyPbitsValue_Object = MibScalar
ntnQosQuickPolicyPbitsValue = _NtnQosQuickPolicyPbitsValue_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 5),
    _NtnQosQuickPolicyPbitsValue_Type()
)
ntnQosQuickPolicyPbitsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyPbitsValue.setStatus("current")


class _NtnQosQuickPolicyRate_Type(Integer32):
    """Custom type ntnQosQuickPolicyRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 32000000),
    )


_NtnQosQuickPolicyRate_Type.__name__ = "Integer32"
_NtnQosQuickPolicyRate_Object = MibScalar
ntnQosQuickPolicyRate = _NtnQosQuickPolicyRate_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 6),
    _NtnQosQuickPolicyRate_Type()
)
ntnQosQuickPolicyRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyRate.setStatus("current")


class _NtnQosQuickPolicyTrTCMType_Type(Integer32):
    """Custom type ntnQosQuickPolicyTrTCMType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aware", 2),
          ("blind", 1))
    )


_NtnQosQuickPolicyTrTCMType_Type.__name__ = "Integer32"
_NtnQosQuickPolicyTrTCMType_Object = MibScalar
ntnQosQuickPolicyTrTCMType = _NtnQosQuickPolicyTrTCMType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 7),
    _NtnQosQuickPolicyTrTCMType_Type()
)
ntnQosQuickPolicyTrTCMType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyTrTCMType.setStatus("current")


class _NtnQosQuickPolicyCIRRate_Type(Integer32):
    """Custom type ntnQosQuickPolicyCIRRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 32000000),
    )


_NtnQosQuickPolicyCIRRate_Type.__name__ = "Integer32"
_NtnQosQuickPolicyCIRRate_Object = MibScalar
ntnQosQuickPolicyCIRRate = _NtnQosQuickPolicyCIRRate_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 8),
    _NtnQosQuickPolicyCIRRate_Type()
)
ntnQosQuickPolicyCIRRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyCIRRate.setStatus("current")


class _NtnQosQuickPolicyPIRRate_Type(Integer32):
    """Custom type ntnQosQuickPolicyPIRRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 32000000),
    )


_NtnQosQuickPolicyPIRRate_Type.__name__ = "Integer32"
_NtnQosQuickPolicyPIRRate_Object = MibScalar
ntnQosQuickPolicyPIRRate = _NtnQosQuickPolicyPIRRate_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 9),
    _NtnQosQuickPolicyPIRRate_Type()
)
ntnQosQuickPolicyPIRRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyPIRRate.setStatus("current")


class _NtnQosQuickPolicyTrackQiQType_Type(Integer32):
    """Custom type ntnQosQuickPolicyTrackQiQType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 3),
          ("qinq1", 1),
          ("qinq2", 2))
    )


_NtnQosQuickPolicyTrackQiQType_Type.__name__ = "Integer32"
_NtnQosQuickPolicyTrackQiQType_Object = MibScalar
ntnQosQuickPolicyTrackQiQType = _NtnQosQuickPolicyTrackQiQType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 10),
    _NtnQosQuickPolicyTrackQiQType_Type()
)
ntnQosQuickPolicyTrackQiQType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyTrackQiQType.setStatus("current")
_NtnQosQuickPolicyDscp_Type = Dscp
_NtnQosQuickPolicyDscp_Object = MibScalar
ntnQosQuickPolicyDscp = _NtnQosQuickPolicyDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 11),
    _NtnQosQuickPolicyDscp_Type()
)
ntnQosQuickPolicyDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyDscp.setStatus("current")


class _NtnQosQuickPolicyPriority_Type(Integer32):
    """Custom type ntnQosQuickPolicyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NtnQosQuickPolicyPriority_Type.__name__ = "Integer32"
_NtnQosQuickPolicyPriority_Object = MibScalar
ntnQosQuickPolicyPriority = _NtnQosQuickPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 12),
    _NtnQosQuickPolicyPriority_Type()
)
ntnQosQuickPolicyPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyPriority.setStatus("current")
_NtnQosQuickPolicyVid_Type = VlanId
_NtnQosQuickPolicyVid_Object = MibScalar
ntnQosQuickPolicyVid = _NtnQosQuickPolicyVid_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 13),
    _NtnQosQuickPolicyVid_Type()
)
ntnQosQuickPolicyVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyVid.setStatus("current")


class _NtnQosQuickPolicyTPID_Type(Integer32):
    """Custom type ntnQosQuickPolicyTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65534),
    )


_NtnQosQuickPolicyTPID_Type.__name__ = "Integer32"
_NtnQosQuickPolicyTPID_Object = MibScalar
ntnQosQuickPolicyTPID = _NtnQosQuickPolicyTPID_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 14),
    _NtnQosQuickPolicyTPID_Type()
)
ntnQosQuickPolicyTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyTPID.setStatus("current")
_NtnQosQuickPolicyIVid_Type = VlanId
_NtnQosQuickPolicyIVid_Object = MibScalar
ntnQosQuickPolicyIVid = _NtnQosQuickPolicyIVid_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 15),
    _NtnQosQuickPolicyIVid_Type()
)
ntnQosQuickPolicyIVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyIVid.setStatus("current")


class _NtnQosQuickPolicyITPID_Type(Integer32):
    """Custom type ntnQosQuickPolicyITPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65534),
    )


_NtnQosQuickPolicyITPID_Type.__name__ = "Integer32"
_NtnQosQuickPolicyITPID_Object = MibScalar
ntnQosQuickPolicyITPID = _NtnQosQuickPolicyITPID_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 16),
    _NtnQosQuickPolicyITPID_Type()
)
ntnQosQuickPolicyITPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyITPID.setStatus("current")


class _NtnQosQuickPolicyIPriority_Type(Integer32):
    """Custom type ntnQosQuickPolicyIPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NtnQosQuickPolicyIPriority_Type.__name__ = "Integer32"
_NtnQosQuickPolicyIPriority_Object = MibScalar
ntnQosQuickPolicyIPriority = _NtnQosQuickPolicyIPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 17),
    _NtnQosQuickPolicyIPriority_Type()
)
ntnQosQuickPolicyIPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyIPriority.setStatus("current")


class _NtnQosQuickPolicyPrecedence_Type(Integer32):
    """Custom type ntnQosQuickPolicyPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_NtnQosQuickPolicyPrecedence_Type.__name__ = "Integer32"
_NtnQosQuickPolicyPrecedence_Object = MibScalar
ntnQosQuickPolicyPrecedence = _NtnQosQuickPolicyPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 18),
    _NtnQosQuickPolicyPrecedence_Type()
)
ntnQosQuickPolicyPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyPrecedence.setStatus("current")
_NtnQosQuickPolicyTrackStatistics_Type = TruthValue
_NtnQosQuickPolicyTrackStatistics_Object = MibScalar
ntnQosQuickPolicyTrackStatistics = _NtnQosQuickPolicyTrackStatistics_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 15, 19),
    _NtnQosQuickPolicyTrackStatistics_Type()
)
ntnQosQuickPolicyTrackStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosQuickPolicyTrackStatistics.setStatus("current")
_NtnQosFilterLimiting_ObjectIdentity = ObjectIdentity
ntnQosFilterLimiting = _NtnQosFilterLimiting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 16)
)
_NtnQosFilterLimitingAdminEnabled_Type = TruthValue
_NtnQosFilterLimitingAdminEnabled_Object = MibScalar
ntnQosFilterLimitingAdminEnabled = _NtnQosFilterLimitingAdminEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 16, 1),
    _NtnQosFilterLimitingAdminEnabled_Type()
)
ntnQosFilterLimitingAdminEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntnQosFilterLimitingAdminEnabled.setStatus("current")
_NtnQosFilterLimitingOperEnabled_Type = TruthValue
_NtnQosFilterLimitingOperEnabled_Object = MibScalar
ntnQosFilterLimitingOperEnabled = _NtnQosFilterLimitingOperEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 1, 16, 2),
    _NtnQosFilterLimitingOperEnabled_Type()
)
ntnQosFilterLimitingOperEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntnQosFilterLimitingOperEnabled.setStatus("current")
_NtnQosPolicyEvolPibConformance_ObjectIdentity = ObjectIdentity
ntnQosPolicyEvolPibConformance = _NtnQosPolicyEvolPibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2)
)
_NtnQosPolicyEvolPibCompliances_ObjectIdentity = ObjectIdentity
ntnQosPolicyEvolPibCompliances = _NtnQosPolicyEvolPibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 1)
)
_NtnQosPolicyEvolPibGroups_ObjectIdentity = ObjectIdentity
ntnQosPolicyEvolPibGroups = _NtnQosPolicyEvolPibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2)
)
_NtnQosPolicyEvolPibNotifications_ObjectIdentity = ObjectIdentity
ntnQosPolicyEvolPibNotifications = _NtnQosPolicyEvolPibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 3)
)
ntnQosIfAssignmentEntry.registerAugmentions(
    ("NTN-QOS-POLICY-EVOL-PIB",
     "ntnQosPolicyDiagsEntry")
)
ntnQosPolicyDiagsEntry.setIndexNames(*ntnQosIfAssignmentEntry.getIndexNames())

# Managed Objects groups

ntnQosInterfaceTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 1)
)
ntnQosInterfaceTypeGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosInterfaceTypeRoles"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosInterfaceTypeIfClass"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosInterfaceTypeCapabilities"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosInterfaceTypeStorageType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosInterfaceTypeStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosInterfaceTypeNextFree"))
)
if mibBuilder.loadTexts:
    ntnQosInterfaceTypeGroup.setStatus("current")

ntnQosQsetPriAssignmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 2)
)
ntnQosQsetPriAssignmentGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQsetPriAssignmentQset"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQsetPriAssignmentPri"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQsetPriAssignmentQueue"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQsetPriAssignmentStorageType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQsetPriAssignmentStatus"))
)
if mibBuilder.loadTexts:
    ntnQosQsetPriAssignmentGroup.setStatus("current")

ntnQosQsetDscpAssignmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 3)
)
ntnQosQsetDscpAssignmentGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQsetDscpAssignmentQset"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQsetDscpAssignmentDscp"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQsetDscpAssignmentQueue"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQsetDscpAssignmentStorageType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQsetDscpAssignmentStatus"))
)
if mibBuilder.loadTexts:
    ntnQosQsetDscpAssignmentGroup.setStatus("current")

ntnQosShapingParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 4)
)
ntnQosShapingParamsGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosShapingParamsRate"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosShapingParamsBurstSize"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosShapingParamsQueueSize"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosShapingParamsStorageType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosShapingParamsStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosShapingParamsLabel"))
)
if mibBuilder.loadTexts:
    ntnQosShapingParamsGroup.setStatus("current")

ntnDsMultiFieldClfrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 5)
)
ntnDsMultiFieldClfrGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrNextFree"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrAddrType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrDstAddr"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrDstPrefixLength"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrSrcAddr"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrSrcPrefixLength"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrDscp"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrFlowId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrProtocol"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrDstL4PortMin"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrDstL4PortMax"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrSrcL4PortMin"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrSrcL4PortMax"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrLabel"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrSessionId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrVersion"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrIpFlags"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrTcpCtrlFlags"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnDsMultiFieldClfrIpv4Options"))
)
if mibBuilder.loadTexts:
    ntnDsMultiFieldClfrGroup.setStatus("current")

ntnL2MultiFieldClfrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 6)
)
ntnL2MultiFieldClfrGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrNextFree"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrDstAddr"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrDstAddrMask"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrSrcAddr"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrSrcAddrMask"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrVlanIdMin"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrVlanIdMax"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrVlanTag"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrEtherType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrUserPriority"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrLabel"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrSessionId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrVersion"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrPktType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrIvidMin"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrIvidMax"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrTPID"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrCFI"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrITPID"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrICFI"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnL2MultiFieldClfrIUserPriority"))
)
if mibBuilder.loadTexts:
    ntnL2MultiFieldClfrGroup.setStatus("current")

ntnSystemClfrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 7)
)
ntnSystemClfrGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrNextFree"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrUnknownUcastFrames"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrUnknownMcastFrames"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrKnownUcastFrames"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrKnownMcastFrames"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrBcastFrames"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrPatternPosition"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrPatternData"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrPatternFormat"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrLabel"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrSessionId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrVersion"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrUnknownIpMcast"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrKnownIpMcast"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrNonIpPkt"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrPatternIpVersion"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrUnknownNonIpMcast"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrKnownNonIpMcast"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnSystemClfrPatternL2Format"))
)
if mibBuilder.loadTexts:
    ntnSystemClfrGroup.setStatus("current")

ntnClfrComponentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 8)
)
ntnClfrComponentGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrComponentNextFree"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrComponentSpecific"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrComponentSetId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrComponentLabel"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrComponentStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrComponentStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrComponentSessionId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrComponentVersion"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrComponentSetNextFree"))
)
if mibBuilder.loadTexts:
    ntnClfrComponentGroup.setStatus("current")

ntnClfrBlockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 9)
)
ntnClfrBlockGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrBlockNextFree"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrBlockNumber"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrBlockClfrCompSetId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrBlockMeter"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrBlockAction"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrBlockLabel"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrBlockStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrBlockStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrBlockSessionId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrBlockNumberNextFree"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrBlockVersion"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnClfrBlockPrecedence"))
)
if mibBuilder.loadTexts:
    ntnClfrBlockGroup.setStatus("current")

ntnQosMeterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 10)
)
ntnQosMeterGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosMeterNextFree"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosMeterSucceedNext"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosMeterFailNext"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosMeterSpecific"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosMeterOutOfProfileStats"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosMeterLabel"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosMeterStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosMeterStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosMeterSessionId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosMeterVersion"))
)
if mibBuilder.loadTexts:
    ntnQosMeterGroup.setStatus("current")

ntnQosTBParamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 11)
)
ntnQosTBParamGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosTBParamNextFree"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosTBParamType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosTBParamRate"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosTBParamBurstSize"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosTBParamInterval"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosTBParamLabel"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosTBParamStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosTBParamStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosTBParamSessionId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosTBParamVersion"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosTBParamMinRate"))
)
if mibBuilder.loadTexts:
    ntnQosTBParamGroup.setStatus("current")

ntnQosBaseActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 12)
)
ntnQosBaseActionGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosBaseActionNextFree"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosBaseActionDrop"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosBaseActionUpdateDscp"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosBaseActionUpdateUserPriority"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosBaseActionSetDropPrecedence"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosBaseActionCopyToCpu"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosBaseActionMirrorFrame"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosBaseActionExtension"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosBaseActionLabel"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosBaseActionStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosBaseActionStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosBaseActionSessionId"))
)
if mibBuilder.loadTexts:
    ntnQosBaseActionGroup.setStatus("current")

ntnQosIfcActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 13)
)
ntnQosIfcActionGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfcActionNextFree"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfcActionUpdateVlanId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfcActionSetEgressMask"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfcActionSetEgressUcastIfc"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfcActionSetEgressNUcastIfc"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfcActionExtension"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfcActionLabel"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfcActionStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfcActionStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfcActionSessionId"))
)
if mibBuilder.loadTexts:
    ntnQosIfcActionGroup.setStatus("current")

ntnQosPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 14)
)
ntnQosPolicyGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyNextFree"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyClassifierType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyClassifierId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyInterfaceRoles"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyPrecedence"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyMeter"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyAction"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyNonMatchAction"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyLabel"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyStats"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyStatsType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyInterfaceIndex"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicySessionId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyVersion"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyMeteringMode"))
)
if mibBuilder.loadTexts:
    ntnQosPolicyGroup.setStatus("current")

ntnQosCountActGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 15)
)
ntnQosCountActGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosCountActNextFree"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosCountActOctets"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosCountActPkts"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosCountActStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosCountActStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosCountActSessionId"))
)
if mibBuilder.loadTexts:
    ntnQosCountActGroup.setStatus("current")

ntnQosFilterStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 16)
)
ntnQosFilterStatsGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterStatsInProfileOctets"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterStatsInProfilePkts"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterStatsOutOfProfileOctets"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterStatsOutOfProfilePkts"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterStatsStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterStatsStatus"))
)
if mibBuilder.loadTexts:
    ntnQosFilterStatsGroup.setStatus("current")

ntnQosPolicyDiagsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 17)
)
ntnQosPolicyDiagsGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyDiagsMasksConsumed"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyDiagsFiltersConsumed"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyDiagsMetersConsumed"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyDiagsNonQosMasksConsumed"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyDiagsNonQosFiltersConsumed"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyDiagsNonQosMetersConsumed"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyDiagsCountersConsumed"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyDiagsTotalMasksAvail"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyDiagsTotalFiltersAvail"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyDiagsTotalMetersAvail"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyDiagsTotalCountersAvail"))
)
if mibBuilder.loadTexts:
    ntnQosPolicyDiagsGroup.setStatus("current")

ntnQosIfAssignmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 18)
)
ntnQosIfAssignmentGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfAssignmentRoleCombination"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfAssignmentQueueSet"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfAssignmentStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfAssignmentStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfAssignmentCapabilities"))
)
if mibBuilder.loadTexts:
    ntnQosIfAssignmentGroup.setStatus("current")

ntnQosIfQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 19)
)
ntnQosIfQueueGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfQueueSetId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfQueueIndex"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfQueueDiscipline"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfQueueDrainSize"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfQueueAbsBandwidth"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfQueueBandwidthAllocation"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfQueueServiceOrder"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfQueueSize"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfQueueStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfQueueStatus"))
)
if mibBuilder.loadTexts:
    ntnQosIfQueueGroup.setStatus("current")

ntnQosDscpToCosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 20)
)
ntnQosDscpToCosGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDscpToCosDscp"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDscpToCosCos"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDscpToCosDropPrec"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDscpToCosLabel"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDscpToCosStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDscpToCosStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDscpToCosNewDscp"))
)
if mibBuilder.loadTexts:
    ntnQosDscpToCosGroup.setStatus("current")

ntnQosCosToDscpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 21)
)
ntnQosCosToDscpGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosCosToDscpCos"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosCosToDscpDscp"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosCosToDscpLabel"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosCosToDscpStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosCosToDscpStatus"))
)
if mibBuilder.loadTexts:
    ntnQosCosToDscpGroup.setStatus("current")

ntnQosPrcSupportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 22)
)
ntnQosPrcSupportGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPrcSupportSupportedPrc"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPrcSupportSupportedAttrs"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPrcSupportMaxPris"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPrcSupportCurrentPris"))
)
if mibBuilder.loadTexts:
    ntnQosPrcSupportGroup.setStatus("current")

ntnQosPolicyDeviceIdentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 23)
)
ntnQosPolicyDeviceIdentGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyDeviceIdentDescr"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyDeviceIdentMaxMsg"))
)
if mibBuilder.loadTexts:
    ntnQosPolicyDeviceIdentGroup.setStatus("current")

ntnQosAgentConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 24)
)
ntnQosAgentConfigGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigResetToDefaults"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigTrackStatistics"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigNVCommitDelay"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigDefaultQueueCfg"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigDefaultBufferingCaps"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigUBPSupportLevel"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigRoleAssocCompatLevel"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigDappEnable"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigDappMinTcpHdrSize"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigDappIpv4IcmpMaxLength"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigDappIpv6IcmpMaxLength"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigNtApplicationMode"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigQosOperMode"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigTrustedProcessingMode"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigResetToPartialDefaults"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigClearStats"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigFcoeRedirOperMode"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigFcoeControllerMacAddr"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigFcoeRedirAvail"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigFcoeControllerIfIndex"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigFcoeControllerVlan"))
)
if mibBuilder.loadTexts:
    ntnQosAgentConfigGroup.setStatus("current")

ntnQosInterfaceRoleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 25)
)
ntnQosInterfaceRoleGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosInterfaceRoleRole"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosInterfaceRoleIfClass"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosInterfaceRoleCapabilities"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosInterfaceRoleStorageType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosInterfaceRoleStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosInterfaceRoleStatsTrackingType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosInterfaceRoleNextFree"))
)
if mibBuilder.loadTexts:
    ntnQosInterfaceRoleGroup.setStatus("current")

ntnQosUserRoleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 26)
)
ntnQosUserRoleGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserRoleRoleCombination"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserRoleUserName"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserRoleUserGroup"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserRoleSessionId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserRoleSessionStart"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserRoleSessionGroup"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserRoleStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserRoleStatus"))
)
if mibBuilder.loadTexts:
    ntnQosUserRoleGroup.setStatus("current")

ntnQosIfShapingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 27)
)
ntnQosIfShapingGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfShapingSpecific"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfShapingLabel"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfShapingStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfShapingStatus"))
)
if mibBuilder.loadTexts:
    ntnQosIfShapingGroup.setStatus("current")

ntnQosDsAccessElemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 28)
)
ntnQosDsAccessElemGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemNextFree"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemAddrType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemDstAddr"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemDstPrefixLength"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemSrcAddr"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemSrcPrefixLength"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemDscp"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemFlowId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemProtocol"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemDstL4PortMin"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemDstL4PortMax"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemSrcL4PortMin"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemSrcL4PortMax"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemActionDrop"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemActionRemarkDscp"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemActionRemarkCos"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemActionSetPrec"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemName"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemBlock"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsAccessElemEvalPrec"))
)
if mibBuilder.loadTexts:
    ntnQosDsAccessElemGroup.setStatus("current")

ntnQosL2AccessElemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 29)
)
ntnQosL2AccessElemGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemNextFree"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemDstAddr"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemDstAddrMask"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemSrcAddr"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemSrcAddrMask"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemVlanIdMin"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemVlanIdMax"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemVlanTag"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemEtherType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemUserPriority"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemActionDrop"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemActionRemarkDscp"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemActionRemarkCos"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemActionSetPrec"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemName"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemBlock"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosL2AccessElemEvalPrec"))
)
if mibBuilder.loadTexts:
    ntnQosL2AccessElemGroup.setStatus("current")

ntnQosAccessAsgnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 30)
)
ntnQosAccessAsgnGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnNextFree"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnAclType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnName"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnIfIndex"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnRate"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnBurstSize"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnOutActionDrop"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnOutActionRemarkDscp"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnOutActionRemarkCos"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnOutActionSetPrec"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnStatsType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnNonMatchActionDrop"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnMeterType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnSecondaryRate"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnSecondaryBurstSize"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnYelActionDrop"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnYelActionRemarkDscp"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnYelActionRemarkCos"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnYelActionSetPrec"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnSetPriority"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosAccessAsgnMeteringMode"))
)
if mibBuilder.loadTexts:
    ntnQosAccessAsgnGroup.setStatus("current")

ntnQosIfAppsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 31)
)
ntnQosIfAppsGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfAppsAppEnable"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfAppsDefaultGateway"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfAppsIfType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfAppsDHCPServer"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfAppsStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosIfAppsStatus"))
)
if mibBuilder.loadTexts:
    ntnQosIfAppsGroup.setStatus("current")

ntnQosUserPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 32)
)
ntnQosUserPolicyGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserPolicyNextFree"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserPolicyIfIndex"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserPolicyRoleCombination"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserPolicyUserName"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserPolicyUserGroup"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserPolicySessionId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserPolicySessionStart"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserPolicySessionGroup"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserPolicyStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserPolicyStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserPolicySrcMacAddr"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserPolicySrcMacAddrMask"))
)
if mibBuilder.loadTexts:
    ntnQosUserPolicyGroup.setStatus("current")

ntnQosDsL2AccessElemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 33)
)
ntnQosDsL2AccessElemGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemNextFree"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemAddrType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemDstIpAddr"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemDstIpPrefixLength"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemSrcIpAddr"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemSrcIpPrefixLength"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemDscp"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemFlowId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemProtocol"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemDstL4PortMin"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemDstL4PortMax"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemSrcL4PortMin"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemSrcL4PortMax"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemDstMacAddr"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemDstMacAddrMask"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemSrcMacAddr"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemSrcMacAddrMask"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemVlanIdMin"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemVlanIdMax"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemVlanTag"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemEtherType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemUserPriority"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemActionDrop"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemActionRemarkDscp"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemActionRemarkCos"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemActionSetPrec"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemName"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemBlock"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemEvalPrec"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemIpFlags"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemTcpCtrlFlags"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemIpv4Options"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemPktType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemIvidMin"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemIvidMax"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemUnknownUcastFrames"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemUnknownMcastFrames"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemKnownUcastFrames"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemKnownMcastFrames"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemBcastFrames"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemUnknownIpMcast"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemKnownIpMcast"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemNonIpPkt"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemVersion"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemUnknownNonIpMcast"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemKnownNonIpMcast"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemMasterBlockMember"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemMeterType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemRate"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemBurstSize"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemOutActionDrop"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemOutActionRemarkDscp"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemOutActionRemarkCos"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemOutActionSetPrec"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemSecondaryRate"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemSecondaryBurstSize"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemYelActionDrop"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemYelActionRemarkDscp"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemYelActionRemarkCos"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDsL2AccessElemYelActionSetPrec"))
)
if mibBuilder.loadTexts:
    ntnQosDsL2AccessElemGroup.setStatus("current")

ntnQosCosShapingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 34)
)
ntnQosCosShapingGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosCosShapingSpecific"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosCosShapingLabel"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosCosShapingStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosCosShapingStatus"))
)
if mibBuilder.loadTexts:
    ntnQosCosShapingGroup.setStatus("current")

ntnQosPolicyPrecResDiagsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 35)
)
ntnQosPolicyPrecResDiagsGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyPrecResDiagsKeysConsumed"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyPrecResDiagsFiltersConsumed"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyPrecResDiagsMetersConsumed"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyPrecResDiagsNonQosKeysConsumed"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyPrecResDiagsNonQosFiltersConsumed"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyPrecResDiagsNonQosMetersConsumed"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyPrecResDiagsCountersConsumed"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyPrecResDiagsTotalKeysAvail"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyPrecResDiagsTotalFiltersAvail"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyPrecResDiagsTotalMetersAvail"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyPrecResDiagsTotalCountersAvail"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyPrecResDiagsRangeChkElemsConsumed"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyPrecResDiagsApplicationIdUsed"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyPrecResDiagsApplicationNameUsed"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyPrecResDiagsRangeChkElemsAvail"))
)
if mibBuilder.loadTexts:
    ntnQosPolicyPrecResDiagsGroup.setStatus("current")

ntnQosQueueShapingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 36)
)
ntnQosQueueShapingGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQueueShapingSpecific"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQueueShapingLabel"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQueueShapingStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQueueShapingStatus"))
)
if mibBuilder.loadTexts:
    ntnQosQueueShapingGroup.setStatus("current")

ntnQosFilterSetStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 37)
)
ntnQosFilterSetStatsGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterSetStatsInProfileOctets"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterSetStatsInProfilePkts"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterSetStatsOutOfProfileOctets"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterSetStatsOutOfProfilePkts"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterSetStatsAccessElemId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterSetStatsStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterSetStatsStatus"))
)
if mibBuilder.loadTexts:
    ntnQosFilterSetStatsGroup.setStatus("current")

avFcoeRedirGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 38)
)
avFcoeRedirGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirNextFree"),
        ("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirDstId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirIngressInterfaceList"),
        ("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirVlanIdMin"),
        ("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirVlanIdMax"),
        ("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirUserPriority"),
        ("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirEtherType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirSrcId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirActionUpdateDstMac"),
        ("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirActionUpdateSrcMac"),
        ("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirActionEgressInterface"),
        ("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirName"),
        ("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirStorage"),
        ("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirStatus"),
        ("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirProcessedFrames"),
        ("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirActionEgressTrunkId"))
)
if mibBuilder.loadTexts:
    avFcoeRedirGroup.setStatus("current")

ntnQosQuickPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 39)
)
ntnQosQuickPolicyGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyControl"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyPortList"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyAction"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyId"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyPbitsValue"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyRate"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyTrTCMType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyCIRRate"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyPIRRate"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyTrackQiQType"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyDscp"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyPriority"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyVid"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyTPID"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyIVid"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyITPID"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyIPriority"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyPrecedence"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosQuickPolicyTrackStatistics"))
)
if mibBuilder.loadTexts:
    ntnQosQuickPolicyGroup.setStatus("current")

ntnQosFilterLimitingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 40)
)
ntnQosFilterLimitingGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterLimitingAdminEnabled"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosFilterLimitingOperEnabled"))
)
if mibBuilder.loadTexts:
    ntnQosFilterLimitingGroup.setStatus("current")

ntnQosDEIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 41)
)
ntnQosDEIGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDEIIngressColorFromDEI"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosDEIEgressMarkDEI"))
)
if mibBuilder.loadTexts:
    ntnQosDEIGroup.setStatus("current")

ntnQosMappingScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 42)
)
ntnQosMappingScalarsGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosMappingRestoreDefault"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosMappingDscpToCosEnabled"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosMappingCosToDscpEnabled"))
)
if mibBuilder.loadTexts:
    ntnQosMappingScalarsGroup.setStatus("current")


# Notification objects

ntnQosPolicyEvolLocalUbpSessionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 3, 1)
)
ntnQosPolicyEvolLocalUbpSessionFailure.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosConfigUBPSupportLevel"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserPolicyIfIndex"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserPolicyUserName"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserPolicyUserGroup"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosUserPolicyRoleCombination"))
)
if mibBuilder.loadTexts:
    ntnQosPolicyEvolLocalUbpSessionFailure.setStatus(
        "current"
    )

ntnQosPolicyEvolDosAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 3, 2)
)
ntnQosPolicyEvolDosAttackDetected.setObjects(
      *(("BN-IF-EXTENSIONS-MIB", "bnIfExtnSlot"),
        ("BN-IF-EXTENSIONS-MIB", "bnIfExtnPort"))
)
if mibBuilder.loadTexts:
    ntnQosPolicyEvolDosAttackDetected.setStatus(
        "current"
    )

avFcoeRedirEgressIssueDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 3, 3)
)
avFcoeRedirEgressIssueDetected.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirActionEgressInterface"),
        ("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirActionEgressTrunkId"))
)
if mibBuilder.loadTexts:
    avFcoeRedirEgressIssueDetected.setStatus(
        "current"
    )


# Notifications groups

ntnQosNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 2, 43)
)
ntnQosNotificationGroup.setObjects(
      *(("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyEvolLocalUbpSessionFailure"),
        ("NTN-QOS-POLICY-EVOL-PIB", "ntnQosPolicyEvolDosAttackDetected"),
        ("NTN-QOS-POLICY-EVOL-PIB", "avFcoeRedirEgressIssueDetected"))
)
if mibBuilder.loadTexts:
    ntnQosNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ntnQosPolicyEvolPibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 4, 7, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ntnQosPolicyEvolPibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTN-QOS-POLICY-EVOL-PIB",
    **{"IndexIntegerOrZero": IndexIntegerOrZero,
       "QosIeee802Cos": QosIeee802Cos,
       "FlowIdOrAny": FlowIdOrAny,
       "DscpUpdate": DscpUpdate,
       "VersionIndicator": VersionIndicator,
       "FcId": FcId,
       "InterfaceList": InterfaceList,
       "ntnQosPolicyEvolPib": ntnQosPolicyEvolPib,
       "ntnQosPolicyEvolPibClasses": ntnQosPolicyEvolPibClasses,
       "ntnQosInterfaceTypeTable": ntnQosInterfaceTypeTable,
       "ntnQosInterfaceTypeEntry": ntnQosInterfaceTypeEntry,
       "ntnQosInterfaceTypeId": ntnQosInterfaceTypeId,
       "ntnQosInterfaceTypeRoles": ntnQosInterfaceTypeRoles,
       "ntnQosInterfaceTypeIfClass": ntnQosInterfaceTypeIfClass,
       "ntnQosInterfaceTypeCapabilities": ntnQosInterfaceTypeCapabilities,
       "ntnQosInterfaceTypeStorageType": ntnQosInterfaceTypeStorageType,
       "ntnQosInterfaceTypeStatus": ntnQosInterfaceTypeStatus,
       "ntnQosQsetPriAssignmentTable": ntnQosQsetPriAssignmentTable,
       "ntnQosQsetPriAssignmentEntry": ntnQosQsetPriAssignmentEntry,
       "ntnQosQsetPriAssignmentId": ntnQosQsetPriAssignmentId,
       "ntnQosQsetPriAssignmentQset": ntnQosQsetPriAssignmentQset,
       "ntnQosQsetPriAssignmentPri": ntnQosQsetPriAssignmentPri,
       "ntnQosQsetPriAssignmentQueue": ntnQosQsetPriAssignmentQueue,
       "ntnQosQsetPriAssignmentStorageType": ntnQosQsetPriAssignmentStorageType,
       "ntnQosQsetPriAssignmentStatus": ntnQosQsetPriAssignmentStatus,
       "ntnQosQsetDscpAssignmentTable": ntnQosQsetDscpAssignmentTable,
       "ntnQosQsetDscpAssignmentEntry": ntnQosQsetDscpAssignmentEntry,
       "ntnQosQsetDscpAssignmentId": ntnQosQsetDscpAssignmentId,
       "ntnQosQsetDscpAssignmentQset": ntnQosQsetDscpAssignmentQset,
       "ntnQosQsetDscpAssignmentDscp": ntnQosQsetDscpAssignmentDscp,
       "ntnQosQsetDscpAssignmentQueue": ntnQosQsetDscpAssignmentQueue,
       "ntnQosQsetDscpAssignmentStorageType": ntnQosQsetDscpAssignmentStorageType,
       "ntnQosQsetDscpAssignmentStatus": ntnQosQsetDscpAssignmentStatus,
       "ntnQosShapingParamsTable": ntnQosShapingParamsTable,
       "ntnQosShapingParamsEntry": ntnQosShapingParamsEntry,
       "ntnQosShapingParamsId": ntnQosShapingParamsId,
       "ntnQosShapingParamsRate": ntnQosShapingParamsRate,
       "ntnQosShapingParamsBurstSize": ntnQosShapingParamsBurstSize,
       "ntnQosShapingParamsQueueSize": ntnQosShapingParamsQueueSize,
       "ntnQosShapingParamsStorageType": ntnQosShapingParamsStorageType,
       "ntnQosShapingParamsStatus": ntnQosShapingParamsStatus,
       "ntnQosShapingParamsLabel": ntnQosShapingParamsLabel,
       "ntnClassifierClasses": ntnClassifierClasses,
       "ntnDsMultiFieldClfrNextFree": ntnDsMultiFieldClfrNextFree,
       "ntnDsMultiFieldClfrTable": ntnDsMultiFieldClfrTable,
       "ntnDsMultiFieldClfrEntry": ntnDsMultiFieldClfrEntry,
       "ntnDsMultiFieldClfrId": ntnDsMultiFieldClfrId,
       "ntnDsMultiFieldClfrAddrType": ntnDsMultiFieldClfrAddrType,
       "ntnDsMultiFieldClfrDstAddr": ntnDsMultiFieldClfrDstAddr,
       "ntnDsMultiFieldClfrDstPrefixLength": ntnDsMultiFieldClfrDstPrefixLength,
       "ntnDsMultiFieldClfrSrcAddr": ntnDsMultiFieldClfrSrcAddr,
       "ntnDsMultiFieldClfrSrcPrefixLength": ntnDsMultiFieldClfrSrcPrefixLength,
       "ntnDsMultiFieldClfrDscp": ntnDsMultiFieldClfrDscp,
       "ntnDsMultiFieldClfrFlowId": ntnDsMultiFieldClfrFlowId,
       "ntnDsMultiFieldClfrProtocol": ntnDsMultiFieldClfrProtocol,
       "ntnDsMultiFieldClfrDstL4PortMin": ntnDsMultiFieldClfrDstL4PortMin,
       "ntnDsMultiFieldClfrDstL4PortMax": ntnDsMultiFieldClfrDstL4PortMax,
       "ntnDsMultiFieldClfrSrcL4PortMin": ntnDsMultiFieldClfrSrcL4PortMin,
       "ntnDsMultiFieldClfrSrcL4PortMax": ntnDsMultiFieldClfrSrcL4PortMax,
       "ntnDsMultiFieldClfrStorage": ntnDsMultiFieldClfrStorage,
       "ntnDsMultiFieldClfrStatus": ntnDsMultiFieldClfrStatus,
       "ntnDsMultiFieldClfrLabel": ntnDsMultiFieldClfrLabel,
       "ntnDsMultiFieldClfrSessionId": ntnDsMultiFieldClfrSessionId,
       "ntnDsMultiFieldClfrVersion": ntnDsMultiFieldClfrVersion,
       "ntnDsMultiFieldClfrIpFlags": ntnDsMultiFieldClfrIpFlags,
       "ntnDsMultiFieldClfrTcpCtrlFlags": ntnDsMultiFieldClfrTcpCtrlFlags,
       "ntnDsMultiFieldClfrIpv4Options": ntnDsMultiFieldClfrIpv4Options,
       "ntnL2MultiFieldClfrNextFree": ntnL2MultiFieldClfrNextFree,
       "ntnL2MultiFieldClfrTable": ntnL2MultiFieldClfrTable,
       "ntnL2MultiFieldClfrEntry": ntnL2MultiFieldClfrEntry,
       "ntnL2MultiFieldClfrId": ntnL2MultiFieldClfrId,
       "ntnL2MultiFieldClfrDstAddr": ntnL2MultiFieldClfrDstAddr,
       "ntnL2MultiFieldClfrDstAddrMask": ntnL2MultiFieldClfrDstAddrMask,
       "ntnL2MultiFieldClfrSrcAddr": ntnL2MultiFieldClfrSrcAddr,
       "ntnL2MultiFieldClfrSrcAddrMask": ntnL2MultiFieldClfrSrcAddrMask,
       "ntnL2MultiFieldClfrVlanIdMin": ntnL2MultiFieldClfrVlanIdMin,
       "ntnL2MultiFieldClfrVlanIdMax": ntnL2MultiFieldClfrVlanIdMax,
       "ntnL2MultiFieldClfrVlanTag": ntnL2MultiFieldClfrVlanTag,
       "ntnL2MultiFieldClfrEtherType": ntnL2MultiFieldClfrEtherType,
       "ntnL2MultiFieldClfrUserPriority": ntnL2MultiFieldClfrUserPriority,
       "ntnL2MultiFieldClfrStorage": ntnL2MultiFieldClfrStorage,
       "ntnL2MultiFieldClfrStatus": ntnL2MultiFieldClfrStatus,
       "ntnL2MultiFieldClfrLabel": ntnL2MultiFieldClfrLabel,
       "ntnL2MultiFieldClfrSessionId": ntnL2MultiFieldClfrSessionId,
       "ntnL2MultiFieldClfrVersion": ntnL2MultiFieldClfrVersion,
       "ntnL2MultiFieldClfrPktType": ntnL2MultiFieldClfrPktType,
       "ntnL2MultiFieldClfrIvidMin": ntnL2MultiFieldClfrIvidMin,
       "ntnL2MultiFieldClfrIvidMax": ntnL2MultiFieldClfrIvidMax,
       "ntnL2MultiFieldClfrTPID": ntnL2MultiFieldClfrTPID,
       "ntnL2MultiFieldClfrCFI": ntnL2MultiFieldClfrCFI,
       "ntnL2MultiFieldClfrITPID": ntnL2MultiFieldClfrITPID,
       "ntnL2MultiFieldClfrICFI": ntnL2MultiFieldClfrICFI,
       "ntnL2MultiFieldClfrIUserPriority": ntnL2MultiFieldClfrIUserPriority,
       "ntnSystemClfrNextFree": ntnSystemClfrNextFree,
       "ntnSystemClfrTable": ntnSystemClfrTable,
       "ntnSystemClfrEntry": ntnSystemClfrEntry,
       "ntnSystemClfrId": ntnSystemClfrId,
       "ntnSystemClfrUnknownUcastFrames": ntnSystemClfrUnknownUcastFrames,
       "ntnSystemClfrUnknownMcastFrames": ntnSystemClfrUnknownMcastFrames,
       "ntnSystemClfrKnownUcastFrames": ntnSystemClfrKnownUcastFrames,
       "ntnSystemClfrKnownMcastFrames": ntnSystemClfrKnownMcastFrames,
       "ntnSystemClfrBcastFrames": ntnSystemClfrBcastFrames,
       "ntnSystemClfrPatternPosition": ntnSystemClfrPatternPosition,
       "ntnSystemClfrPatternData": ntnSystemClfrPatternData,
       "ntnSystemClfrStorage": ntnSystemClfrStorage,
       "ntnSystemClfrStatus": ntnSystemClfrStatus,
       "ntnSystemClfrPatternFormat": ntnSystemClfrPatternFormat,
       "ntnSystemClfrLabel": ntnSystemClfrLabel,
       "ntnSystemClfrSessionId": ntnSystemClfrSessionId,
       "ntnSystemClfrVersion": ntnSystemClfrVersion,
       "ntnSystemClfrUnknownIpMcast": ntnSystemClfrUnknownIpMcast,
       "ntnSystemClfrKnownIpMcast": ntnSystemClfrKnownIpMcast,
       "ntnSystemClfrNonIpPkt": ntnSystemClfrNonIpPkt,
       "ntnSystemClfrPatternIpVersion": ntnSystemClfrPatternIpVersion,
       "ntnSystemClfrUnknownNonIpMcast": ntnSystemClfrUnknownNonIpMcast,
       "ntnSystemClfrKnownNonIpMcast": ntnSystemClfrKnownNonIpMcast,
       "ntnSystemClfrPatternL2Format": ntnSystemClfrPatternL2Format,
       "ntnClfrComponentNextFree": ntnClfrComponentNextFree,
       "ntnClfrComponentTable": ntnClfrComponentTable,
       "ntnClfrComponentEntry": ntnClfrComponentEntry,
       "ntnClfrComponentId": ntnClfrComponentId,
       "ntnClfrComponentSpecific": ntnClfrComponentSpecific,
       "ntnClfrComponentSetId": ntnClfrComponentSetId,
       "ntnClfrComponentLabel": ntnClfrComponentLabel,
       "ntnClfrComponentStorage": ntnClfrComponentStorage,
       "ntnClfrComponentStatus": ntnClfrComponentStatus,
       "ntnClfrComponentSessionId": ntnClfrComponentSessionId,
       "ntnClfrComponentVersion": ntnClfrComponentVersion,
       "ntnClfrBlockNextFree": ntnClfrBlockNextFree,
       "ntnClfrBlockTable": ntnClfrBlockTable,
       "ntnClfrBlockEntry": ntnClfrBlockEntry,
       "ntnClfrBlockId": ntnClfrBlockId,
       "ntnClfrBlockNumber": ntnClfrBlockNumber,
       "ntnClfrBlockClfrCompSetId": ntnClfrBlockClfrCompSetId,
       "ntnClfrBlockMeter": ntnClfrBlockMeter,
       "ntnClfrBlockAction": ntnClfrBlockAction,
       "ntnClfrBlockLabel": ntnClfrBlockLabel,
       "ntnClfrBlockStorage": ntnClfrBlockStorage,
       "ntnClfrBlockStatus": ntnClfrBlockStatus,
       "ntnClfrBlockSessionId": ntnClfrBlockSessionId,
       "ntnClfrBlockVersion": ntnClfrBlockVersion,
       "ntnClfrBlockPrecedence": ntnClfrBlockPrecedence,
       "ntnClfrComponentSetNextFree": ntnClfrComponentSetNextFree,
       "ntnClfrBlockNumberNextFree": ntnClfrBlockNumberNextFree,
       "ntnQosMeterClasses": ntnQosMeterClasses,
       "ntnQosMeterNextFree": ntnQosMeterNextFree,
       "ntnQosMeterTable": ntnQosMeterTable,
       "ntnQosMeterEntry": ntnQosMeterEntry,
       "ntnQosMeterId": ntnQosMeterId,
       "ntnQosMeterSucceedNext": ntnQosMeterSucceedNext,
       "ntnQosMeterFailNext": ntnQosMeterFailNext,
       "ntnQosMeterSpecific": ntnQosMeterSpecific,
       "ntnQosMeterOutOfProfileStats": ntnQosMeterOutOfProfileStats,
       "ntnQosMeterLabel": ntnQosMeterLabel,
       "ntnQosMeterStorage": ntnQosMeterStorage,
       "ntnQosMeterStatus": ntnQosMeterStatus,
       "ntnQosMeterSessionId": ntnQosMeterSessionId,
       "ntnQosMeterVersion": ntnQosMeterVersion,
       "ntnQosTBParamNextFree": ntnQosTBParamNextFree,
       "ntnQosTBParamTable": ntnQosTBParamTable,
       "ntnQosTBParamEntry": ntnQosTBParamEntry,
       "ntnQosTBParamId": ntnQosTBParamId,
       "ntnQosTBParamType": ntnQosTBParamType,
       "ntnQosTBParamRate": ntnQosTBParamRate,
       "ntnQosTBParamBurstSize": ntnQosTBParamBurstSize,
       "ntnQosTBParamInterval": ntnQosTBParamInterval,
       "ntnQosTBParamLabel": ntnQosTBParamLabel,
       "ntnQosTBParamStorage": ntnQosTBParamStorage,
       "ntnQosTBParamStatus": ntnQosTBParamStatus,
       "ntnQosTBParamSessionId": ntnQosTBParamSessionId,
       "ntnQosTBParamVersion": ntnQosTBParamVersion,
       "ntnQosTBParamMinRate": ntnQosTBParamMinRate,
       "ntnQosTBMeters": ntnQosTBMeters,
       "ntnQosTBParamSimpleTokenBucket": ntnQosTBParamSimpleTokenBucket,
       "ntnQosTBParamAvgRate": ntnQosTBParamAvgRate,
       "ntnQosTBParamSrTCMBlind": ntnQosTBParamSrTCMBlind,
       "ntnQosTBParamSrTCMAware": ntnQosTBParamSrTCMAware,
       "ntnQosTBParamTrTCMBlind": ntnQosTBParamTrTCMBlind,
       "ntnQosTBParamTrTCMAware": ntnQosTBParamTrTCMAware,
       "ntnQosTBParamTswTCM": ntnQosTBParamTswTCM,
       "ntnQosActionClasses": ntnQosActionClasses,
       "ntnQosBaseActionNextFree": ntnQosBaseActionNextFree,
       "ntnQosBaseActionTable": ntnQosBaseActionTable,
       "ntnQosBaseActionEntry": ntnQosBaseActionEntry,
       "ntnQosBaseActionId": ntnQosBaseActionId,
       "ntnQosBaseActionDrop": ntnQosBaseActionDrop,
       "ntnQosBaseActionUpdateDscp": ntnQosBaseActionUpdateDscp,
       "ntnQosBaseActionUpdateUserPriority": ntnQosBaseActionUpdateUserPriority,
       "ntnQosBaseActionSetDropPrecedence": ntnQosBaseActionSetDropPrecedence,
       "ntnQosBaseActionCopyToCpu": ntnQosBaseActionCopyToCpu,
       "ntnQosBaseActionMirrorFrame": ntnQosBaseActionMirrorFrame,
       "ntnQosBaseActionExtension": ntnQosBaseActionExtension,
       "ntnQosBaseActionLabel": ntnQosBaseActionLabel,
       "ntnQosBaseActionStorage": ntnQosBaseActionStorage,
       "ntnQosBaseActionStatus": ntnQosBaseActionStatus,
       "ntnQosBaseActionSessionId": ntnQosBaseActionSessionId,
       "ntnQosIfcActionNextFree": ntnQosIfcActionNextFree,
       "ntnQosIfcActionTable": ntnQosIfcActionTable,
       "ntnQosIfcActionEntry": ntnQosIfcActionEntry,
       "ntnQosIfcActionId": ntnQosIfcActionId,
       "ntnQosIfcActionUpdateVlanId": ntnQosIfcActionUpdateVlanId,
       "ntnQosIfcActionSetEgressMask": ntnQosIfcActionSetEgressMask,
       "ntnQosIfcActionSetEgressUcastIfc": ntnQosIfcActionSetEgressUcastIfc,
       "ntnQosIfcActionSetEgressNUcastIfc": ntnQosIfcActionSetEgressNUcastIfc,
       "ntnQosIfcActionExtension": ntnQosIfcActionExtension,
       "ntnQosIfcActionLabel": ntnQosIfcActionLabel,
       "ntnQosIfcActionStorage": ntnQosIfcActionStorage,
       "ntnQosIfcActionStatus": ntnQosIfcActionStatus,
       "ntnQosIfcActionSessionId": ntnQosIfcActionSessionId,
       "ntnQosPolicyClasses": ntnQosPolicyClasses,
       "ntnQosPolicyNextFree": ntnQosPolicyNextFree,
       "ntnQosPolicyTable": ntnQosPolicyTable,
       "ntnQosPolicyEntry": ntnQosPolicyEntry,
       "ntnQosPolicyId": ntnQosPolicyId,
       "ntnQosPolicyClassifierType": ntnQosPolicyClassifierType,
       "ntnQosPolicyClassifierId": ntnQosPolicyClassifierId,
       "ntnQosPolicyInterfaceRoles": ntnQosPolicyInterfaceRoles,
       "ntnQosPolicyPrecedence": ntnQosPolicyPrecedence,
       "ntnQosPolicyMeter": ntnQosPolicyMeter,
       "ntnQosPolicyAction": ntnQosPolicyAction,
       "ntnQosPolicyNonMatchAction": ntnQosPolicyNonMatchAction,
       "ntnQosPolicyLabel": ntnQosPolicyLabel,
       "ntnQosPolicyStorage": ntnQosPolicyStorage,
       "ntnQosPolicyStatus": ntnQosPolicyStatus,
       "ntnQosPolicyStats": ntnQosPolicyStats,
       "ntnQosPolicyStatsType": ntnQosPolicyStatsType,
       "ntnQosPolicyInterfaceIndex": ntnQosPolicyInterfaceIndex,
       "ntnQosPolicySessionId": ntnQosPolicySessionId,
       "ntnQosPolicyVersion": ntnQosPolicyVersion,
       "ntnQosPolicyMeteringMode": ntnQosPolicyMeteringMode,
       "ntnQosCountActNextFree": ntnQosCountActNextFree,
       "ntnQosCountActTable": ntnQosCountActTable,
       "ntnQosCountActEntry": ntnQosCountActEntry,
       "ntnQosCountActId": ntnQosCountActId,
       "ntnQosCountActOctets": ntnQosCountActOctets,
       "ntnQosCountActPkts": ntnQosCountActPkts,
       "ntnQosCountActStorage": ntnQosCountActStorage,
       "ntnQosCountActStatus": ntnQosCountActStatus,
       "ntnQosCountActSessionId": ntnQosCountActSessionId,
       "ntnQosFilterStatsTable": ntnQosFilterStatsTable,
       "ntnQosFilterStatsEntry": ntnQosFilterStatsEntry,
       "ntnQosFilterStatsPolicyId": ntnQosFilterStatsPolicyId,
       "ntnQosFilterStatsFilterId": ntnQosFilterStatsFilterId,
       "ntnQosFilterStatsInterfaceId": ntnQosFilterStatsInterfaceId,
       "ntnQosFilterStatsInProfileOctets": ntnQosFilterStatsInProfileOctets,
       "ntnQosFilterStatsInProfilePkts": ntnQosFilterStatsInProfilePkts,
       "ntnQosFilterStatsOutOfProfileOctets": ntnQosFilterStatsOutOfProfileOctets,
       "ntnQosFilterStatsOutOfProfilePkts": ntnQosFilterStatsOutOfProfilePkts,
       "ntnQosFilterStatsStorage": ntnQosFilterStatsStorage,
       "ntnQosFilterStatsStatus": ntnQosFilterStatsStatus,
       "ntnQosPolicyDiagsTable": ntnQosPolicyDiagsTable,
       "ntnQosPolicyDiagsEntry": ntnQosPolicyDiagsEntry,
       "ntnQosPolicyDiagsMasksConsumed": ntnQosPolicyDiagsMasksConsumed,
       "ntnQosPolicyDiagsFiltersConsumed": ntnQosPolicyDiagsFiltersConsumed,
       "ntnQosPolicyDiagsMetersConsumed": ntnQosPolicyDiagsMetersConsumed,
       "ntnQosPolicyDiagsNonQosMasksConsumed": ntnQosPolicyDiagsNonQosMasksConsumed,
       "ntnQosPolicyDiagsNonQosFiltersConsumed": ntnQosPolicyDiagsNonQosFiltersConsumed,
       "ntnQosPolicyDiagsNonQosMetersConsumed": ntnQosPolicyDiagsNonQosMetersConsumed,
       "ntnQosPolicyDiagsCountersConsumed": ntnQosPolicyDiagsCountersConsumed,
       "ntnQosPolicyDiagsTotalMasksAvail": ntnQosPolicyDiagsTotalMasksAvail,
       "ntnQosPolicyDiagsTotalFiltersAvail": ntnQosPolicyDiagsTotalFiltersAvail,
       "ntnQosPolicyDiagsTotalMetersAvail": ntnQosPolicyDiagsTotalMetersAvail,
       "ntnQosPolicyDiagsTotalCountersAvail": ntnQosPolicyDiagsTotalCountersAvail,
       "ntnQosPolicyPrecResDiagsTable": ntnQosPolicyPrecResDiagsTable,
       "ntnQosPolicyPrecResDiagsEntry": ntnQosPolicyPrecResDiagsEntry,
       "ntnQosPolicyPrecResDiagsPrec": ntnQosPolicyPrecResDiagsPrec,
       "ntnQosPolicyPrecResDiagsInterface": ntnQosPolicyPrecResDiagsInterface,
       "ntnQosPolicyPrecResDiagsKeysConsumed": ntnQosPolicyPrecResDiagsKeysConsumed,
       "ntnQosPolicyPrecResDiagsFiltersConsumed": ntnQosPolicyPrecResDiagsFiltersConsumed,
       "ntnQosPolicyPrecResDiagsMetersConsumed": ntnQosPolicyPrecResDiagsMetersConsumed,
       "ntnQosPolicyPrecResDiagsNonQosKeysConsumed": ntnQosPolicyPrecResDiagsNonQosKeysConsumed,
       "ntnQosPolicyPrecResDiagsNonQosFiltersConsumed": ntnQosPolicyPrecResDiagsNonQosFiltersConsumed,
       "ntnQosPolicyPrecResDiagsNonQosMetersConsumed": ntnQosPolicyPrecResDiagsNonQosMetersConsumed,
       "ntnQosPolicyPrecResDiagsCountersConsumed": ntnQosPolicyPrecResDiagsCountersConsumed,
       "ntnQosPolicyPrecResDiagsTotalKeysAvail": ntnQosPolicyPrecResDiagsTotalKeysAvail,
       "ntnQosPolicyPrecResDiagsTotalFiltersAvail": ntnQosPolicyPrecResDiagsTotalFiltersAvail,
       "ntnQosPolicyPrecResDiagsTotalMetersAvail": ntnQosPolicyPrecResDiagsTotalMetersAvail,
       "ntnQosPolicyPrecResDiagsTotalCountersAvail": ntnQosPolicyPrecResDiagsTotalCountersAvail,
       "ntnQosPolicyPrecResDiagsRangeChkElemsConsumed": ntnQosPolicyPrecResDiagsRangeChkElemsConsumed,
       "ntnQosPolicyPrecResDiagsApplicationIdUsed": ntnQosPolicyPrecResDiagsApplicationIdUsed,
       "ntnQosPolicyPrecResDiagsApplicationNameUsed": ntnQosPolicyPrecResDiagsApplicationNameUsed,
       "ntnQosPolicyPrecResDiagsRangeChkElemsAvail": ntnQosPolicyPrecResDiagsRangeChkElemsAvail,
       "ntnQosInterfaceClasses": ntnQosInterfaceClasses,
       "ntnQosIfAssignmentTable": ntnQosIfAssignmentTable,
       "ntnQosIfAssignmentEntry": ntnQosIfAssignmentEntry,
       "ntnQosIfAssignmentIfIndex": ntnQosIfAssignmentIfIndex,
       "ntnQosIfAssignmentRoleCombination": ntnQosIfAssignmentRoleCombination,
       "ntnQosIfAssignmentQueueSet": ntnQosIfAssignmentQueueSet,
       "ntnQosIfAssignmentStorage": ntnQosIfAssignmentStorage,
       "ntnQosIfAssignmentStatus": ntnQosIfAssignmentStatus,
       "ntnQosIfAssignmentCapabilities": ntnQosIfAssignmentCapabilities,
       "ntnQosIfQueueTable": ntnQosIfQueueTable,
       "ntnQosIfQueueEntry": ntnQosIfQueueEntry,
       "ntnQosIfQueueId": ntnQosIfQueueId,
       "ntnQosIfQueueSetId": ntnQosIfQueueSetId,
       "ntnQosIfQueueIndex": ntnQosIfQueueIndex,
       "ntnQosIfQueueDiscipline": ntnQosIfQueueDiscipline,
       "ntnQosIfQueueDrainSize": ntnQosIfQueueDrainSize,
       "ntnQosIfQueueAbsBandwidth": ntnQosIfQueueAbsBandwidth,
       "ntnQosIfQueueBandwidthAllocation": ntnQosIfQueueBandwidthAllocation,
       "ntnQosIfQueueServiceOrder": ntnQosIfQueueServiceOrder,
       "ntnQosIfQueueSize": ntnQosIfQueueSize,
       "ntnQosIfQueueStorage": ntnQosIfQueueStorage,
       "ntnQosIfQueueStatus": ntnQosIfQueueStatus,
       "ntnQosInterfaceRoleNextFree": ntnQosInterfaceRoleNextFree,
       "ntnQosInterfaceRoleTable": ntnQosInterfaceRoleTable,
       "ntnQosInterfaceRoleEntry": ntnQosInterfaceRoleEntry,
       "ntnQosInterfaceRoleId": ntnQosInterfaceRoleId,
       "ntnQosInterfaceRoleRole": ntnQosInterfaceRoleRole,
       "ntnQosInterfaceRoleIfClass": ntnQosInterfaceRoleIfClass,
       "ntnQosInterfaceRoleCapabilities": ntnQosInterfaceRoleCapabilities,
       "ntnQosInterfaceRoleStorageType": ntnQosInterfaceRoleStorageType,
       "ntnQosInterfaceRoleStatus": ntnQosInterfaceRoleStatus,
       "ntnQosInterfaceRoleStatsTrackingType": ntnQosInterfaceRoleStatsTrackingType,
       "ntnQosUserRoleTable": ntnQosUserRoleTable,
       "ntnQosUserRoleEntry": ntnQosUserRoleEntry,
       "ntnQosUserRoleIfIndex": ntnQosUserRoleIfIndex,
       "ntnQosUserRoleRoleCombination": ntnQosUserRoleRoleCombination,
       "ntnQosUserRoleUserName": ntnQosUserRoleUserName,
       "ntnQosUserRoleUserGroup": ntnQosUserRoleUserGroup,
       "ntnQosUserRoleSessionId": ntnQosUserRoleSessionId,
       "ntnQosUserRoleSessionStart": ntnQosUserRoleSessionStart,
       "ntnQosUserRoleSessionGroup": ntnQosUserRoleSessionGroup,
       "ntnQosUserRoleStorage": ntnQosUserRoleStorage,
       "ntnQosUserRoleStatus": ntnQosUserRoleStatus,
       "ntnQosIfShapingTable": ntnQosIfShapingTable,
       "ntnQosIfShapingEntry": ntnQosIfShapingEntry,
       "ntnQosIfShapingIfIndex": ntnQosIfShapingIfIndex,
       "ntnQosIfShapingSpecific": ntnQosIfShapingSpecific,
       "ntnQosIfShapingLabel": ntnQosIfShapingLabel,
       "ntnQosIfShapingStorage": ntnQosIfShapingStorage,
       "ntnQosIfShapingStatus": ntnQosIfShapingStatus,
       "ntnQosCosShapingTable": ntnQosCosShapingTable,
       "ntnQosCosShapingEntry": ntnQosCosShapingEntry,
       "ntnQosCosShapingIfIndex": ntnQosCosShapingIfIndex,
       "ntnQosCosShapingCos": ntnQosCosShapingCos,
       "ntnQosCosShapingSpecific": ntnQosCosShapingSpecific,
       "ntnQosCosShapingLabel": ntnQosCosShapingLabel,
       "ntnQosCosShapingStorage": ntnQosCosShapingStorage,
       "ntnQosCosShapingStatus": ntnQosCosShapingStatus,
       "ntnQosQueueShapingTable": ntnQosQueueShapingTable,
       "ntnQosQueueShapingEntry": ntnQosQueueShapingEntry,
       "ntnQosQueueShapingIfIndex": ntnQosQueueShapingIfIndex,
       "ntnQosQueueShapingQueue": ntnQosQueueShapingQueue,
       "ntnQosQueueShapingSpecific": ntnQosQueueShapingSpecific,
       "ntnQosQueueShapingLabel": ntnQosQueueShapingLabel,
       "ntnQosQueueShapingStorage": ntnQosQueueShapingStorage,
       "ntnQosQueueShapingStatus": ntnQosQueueShapingStatus,
       "ntnQosMappingClasses": ntnQosMappingClasses,
       "ntnQosDscpToCosTable": ntnQosDscpToCosTable,
       "ntnQosDscpToCosEntry": ntnQosDscpToCosEntry,
       "ntnQosDscpToCosId": ntnQosDscpToCosId,
       "ntnQosDscpToCosDscp": ntnQosDscpToCosDscp,
       "ntnQosDscpToCosCos": ntnQosDscpToCosCos,
       "ntnQosDscpToCosDropPrec": ntnQosDscpToCosDropPrec,
       "ntnQosDscpToCosLabel": ntnQosDscpToCosLabel,
       "ntnQosDscpToCosStorage": ntnQosDscpToCosStorage,
       "ntnQosDscpToCosStatus": ntnQosDscpToCosStatus,
       "ntnQosDscpToCosNewDscp": ntnQosDscpToCosNewDscp,
       "ntnQosCosToDscpTable": ntnQosCosToDscpTable,
       "ntnQosCosToDscpEntry": ntnQosCosToDscpEntry,
       "ntnQosCosToDscpId": ntnQosCosToDscpId,
       "ntnQosCosToDscpCos": ntnQosCosToDscpCos,
       "ntnQosCosToDscpDscp": ntnQosCosToDscpDscp,
       "ntnQosCosToDscpLabel": ntnQosCosToDscpLabel,
       "ntnQosCosToDscpStorage": ntnQosCosToDscpStorage,
       "ntnQosCosToDscpStatus": ntnQosCosToDscpStatus,
       "ntnQosMappingClassesScalars": ntnQosMappingClassesScalars,
       "ntnQosMappingRestoreDefault": ntnQosMappingRestoreDefault,
       "ntnQosMappingDscpToCosEnabled": ntnQosMappingDscpToCosEnabled,
       "ntnQosMappingCosToDscpEnabled": ntnQosMappingCosToDscpEnabled,
       "ntnQosPolicyAgtClasses": ntnQosPolicyAgtClasses,
       "ntnQosPrcSupportTable": ntnQosPrcSupportTable,
       "ntnQosPrcSupportEntry": ntnQosPrcSupportEntry,
       "ntnQosPrcSupportId": ntnQosPrcSupportId,
       "ntnQosPrcSupportSupportedPrc": ntnQosPrcSupportSupportedPrc,
       "ntnQosPrcSupportSupportedAttrs": ntnQosPrcSupportSupportedAttrs,
       "ntnQosPrcSupportMaxPris": ntnQosPrcSupportMaxPris,
       "ntnQosPrcSupportCurrentPris": ntnQosPrcSupportCurrentPris,
       "ntnQosPolicyDeviceIdentTable": ntnQosPolicyDeviceIdentTable,
       "ntnQosPolicyDeviceIdentEntry": ntnQosPolicyDeviceIdentEntry,
       "ntnQosPolicyDeviceIdentId": ntnQosPolicyDeviceIdentId,
       "ntnQosPolicyDeviceIdentDescr": ntnQosPolicyDeviceIdentDescr,
       "ntnQosPolicyDeviceIdentMaxMsg": ntnQosPolicyDeviceIdentMaxMsg,
       "ntnQosConfigResetToDefaults": ntnQosConfigResetToDefaults,
       "ntnQosConfigTrackStatistics": ntnQosConfigTrackStatistics,
       "ntnQosConfigNVCommitDelay": ntnQosConfigNVCommitDelay,
       "ntnQosConfigDefaultQueueCfg": ntnQosConfigDefaultQueueCfg,
       "ntnQosConfigDefaultBufferingCaps": ntnQosConfigDefaultBufferingCaps,
       "ntnQosConfigUBPSupportLevel": ntnQosConfigUBPSupportLevel,
       "ntnQosConfigRoleAssocCompatLevel": ntnQosConfigRoleAssocCompatLevel,
       "ntnQosConfigDappEnable": ntnQosConfigDappEnable,
       "ntnQosConfigDappMinTcpHdrSize": ntnQosConfigDappMinTcpHdrSize,
       "ntnQosConfigDappIpv4IcmpMaxLength": ntnQosConfigDappIpv4IcmpMaxLength,
       "ntnQosConfigDappIpv6IcmpMaxLength": ntnQosConfigDappIpv6IcmpMaxLength,
       "ntnQosConfigNtApplicationMode": ntnQosConfigNtApplicationMode,
       "ntnQosConfigQosOperMode": ntnQosConfigQosOperMode,
       "ntnQosConfigTrustedProcessingMode": ntnQosConfigTrustedProcessingMode,
       "ntnQosConfigResetToPartialDefaults": ntnQosConfigResetToPartialDefaults,
       "ntnQosConfigClearStats": ntnQosConfigClearStats,
       "ntnQosConfigFcoeRedirOperMode": ntnQosConfigFcoeRedirOperMode,
       "ntnQosConfigFcoeControllerMacAddr": ntnQosConfigFcoeControllerMacAddr,
       "ntnQosConfigFcoeRedirAvail": ntnQosConfigFcoeRedirAvail,
       "ntnQosConfigFcoeControllerIfIndex": ntnQosConfigFcoeControllerIfIndex,
       "ntnQosConfigFcoeControllerVlan": ntnQosConfigFcoeControllerVlan,
       "ntnQosInterfaceTypeNextFree": ntnQosInterfaceTypeNextFree,
       "ntnQosApplicationClasses": ntnQosApplicationClasses,
       "ntnQosDsAccessElemNextFree": ntnQosDsAccessElemNextFree,
       "ntnQosDsAccessElemTable": ntnQosDsAccessElemTable,
       "ntnQosDsAccessElemEntry": ntnQosDsAccessElemEntry,
       "ntnQosDsAccessElemId": ntnQosDsAccessElemId,
       "ntnQosDsAccessElemAddrType": ntnQosDsAccessElemAddrType,
       "ntnQosDsAccessElemDstAddr": ntnQosDsAccessElemDstAddr,
       "ntnQosDsAccessElemDstPrefixLength": ntnQosDsAccessElemDstPrefixLength,
       "ntnQosDsAccessElemSrcAddr": ntnQosDsAccessElemSrcAddr,
       "ntnQosDsAccessElemSrcPrefixLength": ntnQosDsAccessElemSrcPrefixLength,
       "ntnQosDsAccessElemDscp": ntnQosDsAccessElemDscp,
       "ntnQosDsAccessElemFlowId": ntnQosDsAccessElemFlowId,
       "ntnQosDsAccessElemProtocol": ntnQosDsAccessElemProtocol,
       "ntnQosDsAccessElemDstL4PortMin": ntnQosDsAccessElemDstL4PortMin,
       "ntnQosDsAccessElemDstL4PortMax": ntnQosDsAccessElemDstL4PortMax,
       "ntnQosDsAccessElemSrcL4PortMin": ntnQosDsAccessElemSrcL4PortMin,
       "ntnQosDsAccessElemSrcL4PortMax": ntnQosDsAccessElemSrcL4PortMax,
       "ntnQosDsAccessElemActionDrop": ntnQosDsAccessElemActionDrop,
       "ntnQosDsAccessElemActionRemarkDscp": ntnQosDsAccessElemActionRemarkDscp,
       "ntnQosDsAccessElemActionRemarkCos": ntnQosDsAccessElemActionRemarkCos,
       "ntnQosDsAccessElemActionSetPrec": ntnQosDsAccessElemActionSetPrec,
       "ntnQosDsAccessElemName": ntnQosDsAccessElemName,
       "ntnQosDsAccessElemBlock": ntnQosDsAccessElemBlock,
       "ntnQosDsAccessElemType": ntnQosDsAccessElemType,
       "ntnQosDsAccessElemStorage": ntnQosDsAccessElemStorage,
       "ntnQosDsAccessElemStatus": ntnQosDsAccessElemStatus,
       "ntnQosDsAccessElemEvalPrec": ntnQosDsAccessElemEvalPrec,
       "ntnQosL2AccessElemNextFree": ntnQosL2AccessElemNextFree,
       "ntnQosL2AccessElemTable": ntnQosL2AccessElemTable,
       "ntnQosL2AccessElemEntry": ntnQosL2AccessElemEntry,
       "ntnQosL2AccessElemId": ntnQosL2AccessElemId,
       "ntnQosL2AccessElemDstAddr": ntnQosL2AccessElemDstAddr,
       "ntnQosL2AccessElemDstAddrMask": ntnQosL2AccessElemDstAddrMask,
       "ntnQosL2AccessElemSrcAddr": ntnQosL2AccessElemSrcAddr,
       "ntnQosL2AccessElemSrcAddrMask": ntnQosL2AccessElemSrcAddrMask,
       "ntnQosL2AccessElemVlanIdMin": ntnQosL2AccessElemVlanIdMin,
       "ntnQosL2AccessElemVlanIdMax": ntnQosL2AccessElemVlanIdMax,
       "ntnQosL2AccessElemVlanTag": ntnQosL2AccessElemVlanTag,
       "ntnQosL2AccessElemEtherType": ntnQosL2AccessElemEtherType,
       "ntnQosL2AccessElemUserPriority": ntnQosL2AccessElemUserPriority,
       "ntnQosL2AccessElemActionDrop": ntnQosL2AccessElemActionDrop,
       "ntnQosL2AccessElemActionRemarkDscp": ntnQosL2AccessElemActionRemarkDscp,
       "ntnQosL2AccessElemActionRemarkCos": ntnQosL2AccessElemActionRemarkCos,
       "ntnQosL2AccessElemActionSetPrec": ntnQosL2AccessElemActionSetPrec,
       "ntnQosL2AccessElemName": ntnQosL2AccessElemName,
       "ntnQosL2AccessElemBlock": ntnQosL2AccessElemBlock,
       "ntnQosL2AccessElemType": ntnQosL2AccessElemType,
       "ntnQosL2AccessElemStorage": ntnQosL2AccessElemStorage,
       "ntnQosL2AccessElemStatus": ntnQosL2AccessElemStatus,
       "ntnQosL2AccessElemEvalPrec": ntnQosL2AccessElemEvalPrec,
       "ntnQosAccessAsgnNextFree": ntnQosAccessAsgnNextFree,
       "ntnQosAccessAsgnTable": ntnQosAccessAsgnTable,
       "ntnQosAccessAsgnEntry": ntnQosAccessAsgnEntry,
       "ntnQosAccessAsgnId": ntnQosAccessAsgnId,
       "ntnQosAccessAsgnAclType": ntnQosAccessAsgnAclType,
       "ntnQosAccessAsgnName": ntnQosAccessAsgnName,
       "ntnQosAccessAsgnIfIndex": ntnQosAccessAsgnIfIndex,
       "ntnQosAccessAsgnRate": ntnQosAccessAsgnRate,
       "ntnQosAccessAsgnBurstSize": ntnQosAccessAsgnBurstSize,
       "ntnQosAccessAsgnOutActionDrop": ntnQosAccessAsgnOutActionDrop,
       "ntnQosAccessAsgnOutActionRemarkDscp": ntnQosAccessAsgnOutActionRemarkDscp,
       "ntnQosAccessAsgnOutActionRemarkCos": ntnQosAccessAsgnOutActionRemarkCos,
       "ntnQosAccessAsgnOutActionSetPrec": ntnQosAccessAsgnOutActionSetPrec,
       "ntnQosAccessAsgnStatsType": ntnQosAccessAsgnStatsType,
       "ntnQosAccessAsgnStorage": ntnQosAccessAsgnStorage,
       "ntnQosAccessAsgnStatus": ntnQosAccessAsgnStatus,
       "ntnQosAccessAsgnNonMatchActionDrop": ntnQosAccessAsgnNonMatchActionDrop,
       "ntnQosAccessAsgnMeterType": ntnQosAccessAsgnMeterType,
       "ntnQosAccessAsgnSecondaryRate": ntnQosAccessAsgnSecondaryRate,
       "ntnQosAccessAsgnSecondaryBurstSize": ntnQosAccessAsgnSecondaryBurstSize,
       "ntnQosAccessAsgnYelActionDrop": ntnQosAccessAsgnYelActionDrop,
       "ntnQosAccessAsgnYelActionRemarkDscp": ntnQosAccessAsgnYelActionRemarkDscp,
       "ntnQosAccessAsgnYelActionRemarkCos": ntnQosAccessAsgnYelActionRemarkCos,
       "ntnQosAccessAsgnYelActionSetPrec": ntnQosAccessAsgnYelActionSetPrec,
       "ntnQosAccessAsgnSetPriority": ntnQosAccessAsgnSetPriority,
       "ntnQosAccessAsgnMeteringMode": ntnQosAccessAsgnMeteringMode,
       "ntnQosIfAppsTable": ntnQosIfAppsTable,
       "ntnQosIfAppsEntry": ntnQosIfAppsEntry,
       "ntnQosIfAppsIfIndex": ntnQosIfAppsIfIndex,
       "ntnQosIfAppsAppEnable": ntnQosIfAppsAppEnable,
       "ntnQosIfAppsDefaultGateway": ntnQosIfAppsDefaultGateway,
       "ntnQosIfAppsIfType": ntnQosIfAppsIfType,
       "ntnQosIfAppsDHCPServer": ntnQosIfAppsDHCPServer,
       "ntnQosIfAppsStorage": ntnQosIfAppsStorage,
       "ntnQosIfAppsStatus": ntnQosIfAppsStatus,
       "ntnQosUserPolicyNextFree": ntnQosUserPolicyNextFree,
       "ntnQosUserPolicyTable": ntnQosUserPolicyTable,
       "ntnQosUserPolicyEntry": ntnQosUserPolicyEntry,
       "ntnQosUserPolicyId": ntnQosUserPolicyId,
       "ntnQosUserPolicyIfIndex": ntnQosUserPolicyIfIndex,
       "ntnQosUserPolicyRoleCombination": ntnQosUserPolicyRoleCombination,
       "ntnQosUserPolicyUserName": ntnQosUserPolicyUserName,
       "ntnQosUserPolicyUserGroup": ntnQosUserPolicyUserGroup,
       "ntnQosUserPolicySessionId": ntnQosUserPolicySessionId,
       "ntnQosUserPolicySessionStart": ntnQosUserPolicySessionStart,
       "ntnQosUserPolicySessionGroup": ntnQosUserPolicySessionGroup,
       "ntnQosUserPolicyStorage": ntnQosUserPolicyStorage,
       "ntnQosUserPolicyStatus": ntnQosUserPolicyStatus,
       "ntnQosUserPolicySrcMacAddr": ntnQosUserPolicySrcMacAddr,
       "ntnQosUserPolicySrcMacAddrMask": ntnQosUserPolicySrcMacAddrMask,
       "ntnQosDsL2AccessElemNextFree": ntnQosDsL2AccessElemNextFree,
       "ntnQosDsL2AccessElemTable": ntnQosDsL2AccessElemTable,
       "ntnQosDsL2AccessElemEntry": ntnQosDsL2AccessElemEntry,
       "ntnQosDsL2AccessElemId": ntnQosDsL2AccessElemId,
       "ntnQosDsL2AccessElemAddrType": ntnQosDsL2AccessElemAddrType,
       "ntnQosDsL2AccessElemDstIpAddr": ntnQosDsL2AccessElemDstIpAddr,
       "ntnQosDsL2AccessElemDstIpPrefixLength": ntnQosDsL2AccessElemDstIpPrefixLength,
       "ntnQosDsL2AccessElemSrcIpAddr": ntnQosDsL2AccessElemSrcIpAddr,
       "ntnQosDsL2AccessElemSrcIpPrefixLength": ntnQosDsL2AccessElemSrcIpPrefixLength,
       "ntnQosDsL2AccessElemDscp": ntnQosDsL2AccessElemDscp,
       "ntnQosDsL2AccessElemFlowId": ntnQosDsL2AccessElemFlowId,
       "ntnQosDsL2AccessElemProtocol": ntnQosDsL2AccessElemProtocol,
       "ntnQosDsL2AccessElemDstL4PortMin": ntnQosDsL2AccessElemDstL4PortMin,
       "ntnQosDsL2AccessElemDstL4PortMax": ntnQosDsL2AccessElemDstL4PortMax,
       "ntnQosDsL2AccessElemSrcL4PortMin": ntnQosDsL2AccessElemSrcL4PortMin,
       "ntnQosDsL2AccessElemSrcL4PortMax": ntnQosDsL2AccessElemSrcL4PortMax,
       "ntnQosDsL2AccessElemDstMacAddr": ntnQosDsL2AccessElemDstMacAddr,
       "ntnQosDsL2AccessElemDstMacAddrMask": ntnQosDsL2AccessElemDstMacAddrMask,
       "ntnQosDsL2AccessElemSrcMacAddr": ntnQosDsL2AccessElemSrcMacAddr,
       "ntnQosDsL2AccessElemSrcMacAddrMask": ntnQosDsL2AccessElemSrcMacAddrMask,
       "ntnQosDsL2AccessElemVlanIdMin": ntnQosDsL2AccessElemVlanIdMin,
       "ntnQosDsL2AccessElemVlanIdMax": ntnQosDsL2AccessElemVlanIdMax,
       "ntnQosDsL2AccessElemVlanTag": ntnQosDsL2AccessElemVlanTag,
       "ntnQosDsL2AccessElemEtherType": ntnQosDsL2AccessElemEtherType,
       "ntnQosDsL2AccessElemUserPriority": ntnQosDsL2AccessElemUserPriority,
       "ntnQosDsL2AccessElemActionDrop": ntnQosDsL2AccessElemActionDrop,
       "ntnQosDsL2AccessElemActionRemarkDscp": ntnQosDsL2AccessElemActionRemarkDscp,
       "ntnQosDsL2AccessElemActionRemarkCos": ntnQosDsL2AccessElemActionRemarkCos,
       "ntnQosDsL2AccessElemActionSetPrec": ntnQosDsL2AccessElemActionSetPrec,
       "ntnQosDsL2AccessElemName": ntnQosDsL2AccessElemName,
       "ntnQosDsL2AccessElemBlock": ntnQosDsL2AccessElemBlock,
       "ntnQosDsL2AccessElemType": ntnQosDsL2AccessElemType,
       "ntnQosDsL2AccessElemStorage": ntnQosDsL2AccessElemStorage,
       "ntnQosDsL2AccessElemStatus": ntnQosDsL2AccessElemStatus,
       "ntnQosDsL2AccessElemEvalPrec": ntnQosDsL2AccessElemEvalPrec,
       "ntnQosDsL2AccessElemIpFlags": ntnQosDsL2AccessElemIpFlags,
       "ntnQosDsL2AccessElemTcpCtrlFlags": ntnQosDsL2AccessElemTcpCtrlFlags,
       "ntnQosDsL2AccessElemIpv4Options": ntnQosDsL2AccessElemIpv4Options,
       "ntnQosDsL2AccessElemPktType": ntnQosDsL2AccessElemPktType,
       "ntnQosDsL2AccessElemIvidMin": ntnQosDsL2AccessElemIvidMin,
       "ntnQosDsL2AccessElemIvidMax": ntnQosDsL2AccessElemIvidMax,
       "ntnQosDsL2AccessElemUnknownUcastFrames": ntnQosDsL2AccessElemUnknownUcastFrames,
       "ntnQosDsL2AccessElemUnknownMcastFrames": ntnQosDsL2AccessElemUnknownMcastFrames,
       "ntnQosDsL2AccessElemKnownUcastFrames": ntnQosDsL2AccessElemKnownUcastFrames,
       "ntnQosDsL2AccessElemKnownMcastFrames": ntnQosDsL2AccessElemKnownMcastFrames,
       "ntnQosDsL2AccessElemBcastFrames": ntnQosDsL2AccessElemBcastFrames,
       "ntnQosDsL2AccessElemUnknownIpMcast": ntnQosDsL2AccessElemUnknownIpMcast,
       "ntnQosDsL2AccessElemKnownIpMcast": ntnQosDsL2AccessElemKnownIpMcast,
       "ntnQosDsL2AccessElemNonIpPkt": ntnQosDsL2AccessElemNonIpPkt,
       "ntnQosDsL2AccessElemVersion": ntnQosDsL2AccessElemVersion,
       "ntnQosDsL2AccessElemUnknownNonIpMcast": ntnQosDsL2AccessElemUnknownNonIpMcast,
       "ntnQosDsL2AccessElemKnownNonIpMcast": ntnQosDsL2AccessElemKnownNonIpMcast,
       "ntnQosDsL2AccessElemMasterBlockMember": ntnQosDsL2AccessElemMasterBlockMember,
       "ntnQosDsL2AccessElemMeterType": ntnQosDsL2AccessElemMeterType,
       "ntnQosDsL2AccessElemRate": ntnQosDsL2AccessElemRate,
       "ntnQosDsL2AccessElemBurstSize": ntnQosDsL2AccessElemBurstSize,
       "ntnQosDsL2AccessElemOutActionDrop": ntnQosDsL2AccessElemOutActionDrop,
       "ntnQosDsL2AccessElemOutActionRemarkDscp": ntnQosDsL2AccessElemOutActionRemarkDscp,
       "ntnQosDsL2AccessElemOutActionRemarkCos": ntnQosDsL2AccessElemOutActionRemarkCos,
       "ntnQosDsL2AccessElemOutActionSetPrec": ntnQosDsL2AccessElemOutActionSetPrec,
       "ntnQosDsL2AccessElemSecondaryRate": ntnQosDsL2AccessElemSecondaryRate,
       "ntnQosDsL2AccessElemSecondaryBurstSize": ntnQosDsL2AccessElemSecondaryBurstSize,
       "ntnQosDsL2AccessElemYelActionDrop": ntnQosDsL2AccessElemYelActionDrop,
       "ntnQosDsL2AccessElemYelActionRemarkDscp": ntnQosDsL2AccessElemYelActionRemarkDscp,
       "ntnQosDsL2AccessElemYelActionRemarkCos": ntnQosDsL2AccessElemYelActionRemarkCos,
       "ntnQosDsL2AccessElemYelActionSetPrec": ntnQosDsL2AccessElemYelActionSetPrec,
       "ntnQosFilterSetStatsTable": ntnQosFilterSetStatsTable,
       "ntnQosFilterSetStatsEntry": ntnQosFilterSetStatsEntry,
       "ntnQosFilterSetStatsAccessAsgnId": ntnQosFilterSetStatsAccessAsgnId,
       "ntnQosFilterSetStatsPrecedence": ntnQosFilterSetStatsPrecedence,
       "ntnQosFilterSetStatsEvalOrder": ntnQosFilterSetStatsEvalOrder,
       "ntnQosFilterSetStatsInProfileOctets": ntnQosFilterSetStatsInProfileOctets,
       "ntnQosFilterSetStatsInProfilePkts": ntnQosFilterSetStatsInProfilePkts,
       "ntnQosFilterSetStatsOutOfProfileOctets": ntnQosFilterSetStatsOutOfProfileOctets,
       "ntnQosFilterSetStatsOutOfProfilePkts": ntnQosFilterSetStatsOutOfProfilePkts,
       "ntnQosFilterSetStatsAccessElemId": ntnQosFilterSetStatsAccessElemId,
       "ntnQosFilterSetStatsStorage": ntnQosFilterSetStatsStorage,
       "ntnQosFilterSetStatsStatus": ntnQosFilterSetStatsStatus,
       "avFcoeRedirNextFree": avFcoeRedirNextFree,
       "avFcoeRedirTable": avFcoeRedirTable,
       "avFcoeRedirEntry": avFcoeRedirEntry,
       "avFcoeRedirId": avFcoeRedirId,
       "avFcoeRedirDstId": avFcoeRedirDstId,
       "avFcoeRedirIngressInterfaceList": avFcoeRedirIngressInterfaceList,
       "avFcoeRedirVlanIdMin": avFcoeRedirVlanIdMin,
       "avFcoeRedirVlanIdMax": avFcoeRedirVlanIdMax,
       "avFcoeRedirUserPriority": avFcoeRedirUserPriority,
       "avFcoeRedirEtherType": avFcoeRedirEtherType,
       "avFcoeRedirSrcId": avFcoeRedirSrcId,
       "avFcoeRedirActionUpdateDstMac": avFcoeRedirActionUpdateDstMac,
       "avFcoeRedirActionUpdateSrcMac": avFcoeRedirActionUpdateSrcMac,
       "avFcoeRedirActionEgressInterface": avFcoeRedirActionEgressInterface,
       "avFcoeRedirName": avFcoeRedirName,
       "avFcoeRedirStorage": avFcoeRedirStorage,
       "avFcoeRedirStatus": avFcoeRedirStatus,
       "avFcoeRedirProcessedFrames": avFcoeRedirProcessedFrames,
       "avFcoeRedirActionEgressTrunkId": avFcoeRedirActionEgressTrunkId,
       "ntnQosDEITable": ntnQosDEITable,
       "ntnQosDEIEntry": ntnQosDEIEntry,
       "ntnQosDEIInterfaceId": ntnQosDEIInterfaceId,
       "ntnQosDEIIngressColorFromDEI": ntnQosDEIIngressColorFromDEI,
       "ntnQosDEIEgressMarkDEI": ntnQosDEIEgressMarkDEI,
       "ntnQosQuickPolicy": ntnQosQuickPolicy,
       "ntnQosQuickPolicyControl": ntnQosQuickPolicyControl,
       "ntnQosQuickPolicyPortList": ntnQosQuickPolicyPortList,
       "ntnQosQuickPolicyAction": ntnQosQuickPolicyAction,
       "ntnQosQuickPolicyId": ntnQosQuickPolicyId,
       "ntnQosQuickPolicyPbitsValue": ntnQosQuickPolicyPbitsValue,
       "ntnQosQuickPolicyRate": ntnQosQuickPolicyRate,
       "ntnQosQuickPolicyTrTCMType": ntnQosQuickPolicyTrTCMType,
       "ntnQosQuickPolicyCIRRate": ntnQosQuickPolicyCIRRate,
       "ntnQosQuickPolicyPIRRate": ntnQosQuickPolicyPIRRate,
       "ntnQosQuickPolicyTrackQiQType": ntnQosQuickPolicyTrackQiQType,
       "ntnQosQuickPolicyDscp": ntnQosQuickPolicyDscp,
       "ntnQosQuickPolicyPriority": ntnQosQuickPolicyPriority,
       "ntnQosQuickPolicyVid": ntnQosQuickPolicyVid,
       "ntnQosQuickPolicyTPID": ntnQosQuickPolicyTPID,
       "ntnQosQuickPolicyIVid": ntnQosQuickPolicyIVid,
       "ntnQosQuickPolicyITPID": ntnQosQuickPolicyITPID,
       "ntnQosQuickPolicyIPriority": ntnQosQuickPolicyIPriority,
       "ntnQosQuickPolicyPrecedence": ntnQosQuickPolicyPrecedence,
       "ntnQosQuickPolicyTrackStatistics": ntnQosQuickPolicyTrackStatistics,
       "ntnQosFilterLimiting": ntnQosFilterLimiting,
       "ntnQosFilterLimitingAdminEnabled": ntnQosFilterLimitingAdminEnabled,
       "ntnQosFilterLimitingOperEnabled": ntnQosFilterLimitingOperEnabled,
       "ntnQosPolicyEvolPibConformance": ntnQosPolicyEvolPibConformance,
       "ntnQosPolicyEvolPibCompliances": ntnQosPolicyEvolPibCompliances,
       "ntnQosPolicyEvolPibCompliance": ntnQosPolicyEvolPibCompliance,
       "ntnQosPolicyEvolPibGroups": ntnQosPolicyEvolPibGroups,
       "ntnQosInterfaceTypeGroup": ntnQosInterfaceTypeGroup,
       "ntnQosQsetPriAssignmentGroup": ntnQosQsetPriAssignmentGroup,
       "ntnQosQsetDscpAssignmentGroup": ntnQosQsetDscpAssignmentGroup,
       "ntnQosShapingParamsGroup": ntnQosShapingParamsGroup,
       "ntnDsMultiFieldClfrGroup": ntnDsMultiFieldClfrGroup,
       "ntnL2MultiFieldClfrGroup": ntnL2MultiFieldClfrGroup,
       "ntnSystemClfrGroup": ntnSystemClfrGroup,
       "ntnClfrComponentGroup": ntnClfrComponentGroup,
       "ntnClfrBlockGroup": ntnClfrBlockGroup,
       "ntnQosMeterGroup": ntnQosMeterGroup,
       "ntnQosTBParamGroup": ntnQosTBParamGroup,
       "ntnQosBaseActionGroup": ntnQosBaseActionGroup,
       "ntnQosIfcActionGroup": ntnQosIfcActionGroup,
       "ntnQosPolicyGroup": ntnQosPolicyGroup,
       "ntnQosCountActGroup": ntnQosCountActGroup,
       "ntnQosFilterStatsGroup": ntnQosFilterStatsGroup,
       "ntnQosPolicyDiagsGroup": ntnQosPolicyDiagsGroup,
       "ntnQosIfAssignmentGroup": ntnQosIfAssignmentGroup,
       "ntnQosIfQueueGroup": ntnQosIfQueueGroup,
       "ntnQosDscpToCosGroup": ntnQosDscpToCosGroup,
       "ntnQosCosToDscpGroup": ntnQosCosToDscpGroup,
       "ntnQosPrcSupportGroup": ntnQosPrcSupportGroup,
       "ntnQosPolicyDeviceIdentGroup": ntnQosPolicyDeviceIdentGroup,
       "ntnQosAgentConfigGroup": ntnQosAgentConfigGroup,
       "ntnQosInterfaceRoleGroup": ntnQosInterfaceRoleGroup,
       "ntnQosUserRoleGroup": ntnQosUserRoleGroup,
       "ntnQosIfShapingGroup": ntnQosIfShapingGroup,
       "ntnQosDsAccessElemGroup": ntnQosDsAccessElemGroup,
       "ntnQosL2AccessElemGroup": ntnQosL2AccessElemGroup,
       "ntnQosAccessAsgnGroup": ntnQosAccessAsgnGroup,
       "ntnQosIfAppsGroup": ntnQosIfAppsGroup,
       "ntnQosUserPolicyGroup": ntnQosUserPolicyGroup,
       "ntnQosDsL2AccessElemGroup": ntnQosDsL2AccessElemGroup,
       "ntnQosCosShapingGroup": ntnQosCosShapingGroup,
       "ntnQosPolicyPrecResDiagsGroup": ntnQosPolicyPrecResDiagsGroup,
       "ntnQosQueueShapingGroup": ntnQosQueueShapingGroup,
       "ntnQosFilterSetStatsGroup": ntnQosFilterSetStatsGroup,
       "avFcoeRedirGroup": avFcoeRedirGroup,
       "ntnQosQuickPolicyGroup": ntnQosQuickPolicyGroup,
       "ntnQosFilterLimitingGroup": ntnQosFilterLimitingGroup,
       "ntnQosDEIGroup": ntnQosDEIGroup,
       "ntnQosMappingScalarsGroup": ntnQosMappingScalarsGroup,
       "ntnQosNotificationGroup": ntnQosNotificationGroup,
       "ntnQosPolicyEvolPibNotifications": ntnQosPolicyEvolPibNotifications,
       "ntnQosPolicyEvolLocalUbpSessionFailure": ntnQosPolicyEvolLocalUbpSessionFailure,
       "ntnQosPolicyEvolDosAttackDetected": ntnQosPolicyEvolDosAttackDetected,
       "avFcoeRedirEgressIssueDetected": avFcoeRedirEgressIssueDetected}
)

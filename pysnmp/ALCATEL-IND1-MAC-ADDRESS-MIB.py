# SNMP MIB module (ALCATEL-IND1-MAC-ADDRESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-MAC-ADDRESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:32 2024
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

(softentIND1MacAddress,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1MacAddress")

(vlanNumber,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-VLAN-MGR-MIB",
    "vlanNumber")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(dot1qVlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qVlanIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1MacAddressMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1)
)
alcatelIND1MacAddressMIB.setRevisions(
        ("2010-05-13 00:00",
         "2007-04-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MacAddressProtocolType(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1MacAddressMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1MacAddressMIBNotifications = _AlcatelIND1MacAddressMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1MacAddressMIBNotifications.setStatus("current")
_AlcatelIND1MacAddressMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1MacAddressMIBObjects = _AlcatelIND1MacAddressMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1MacAddressMIBObjects.setStatus("current")
_SlMacAddressAgingTable_Object = MibTable
slMacAddressAgingTable = _SlMacAddressAgingTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    slMacAddressAgingTable.setStatus("current")
_SlMacAddressAgingEntry_Object = MibTableRow
slMacAddressAgingEntry = _SlMacAddressAgingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 2, 1)
)
slMacAddressAgingEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    slMacAddressAgingEntry.setStatus("current")


class _SlMacAgingValue_Type(Integer32):
    """Custom type slMacAgingValue based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_SlMacAgingValue_Type.__name__ = "Integer32"
_SlMacAgingValue_Object = MibTableColumn
slMacAgingValue = _SlMacAgingValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 2, 1, 1),
    _SlMacAgingValue_Type()
)
slMacAgingValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slMacAgingValue.setStatus("current")
_SlMacAgingRowStatus_Type = RowStatus
_SlMacAgingRowStatus_Object = MibTableColumn
slMacAgingRowStatus = _SlMacAgingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 2, 1, 2),
    _SlMacAgingRowStatus_Type()
)
slMacAgingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slMacAgingRowStatus.setStatus("current")


class _SlDistributedMacMode_Type(Integer32):
    """Custom type slDistributedMacMode based on Integer32"""
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


_SlDistributedMacMode_Type.__name__ = "Integer32"
_SlDistributedMacMode_Object = MibScalar
slDistributedMacMode = _SlDistributedMacMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 5),
    _SlDistributedMacMode_Type()
)
slDistributedMacMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slDistributedMacMode.setStatus("current")
_SlMacLearningControlTable_Object = MibTable
slMacLearningControlTable = _SlMacLearningControlTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 7)
)
if mibBuilder.loadTexts:
    slMacLearningControlTable.setStatus("current")
_SlMacLearningControlEntry_Object = MibTableRow
slMacLearningControlEntry = _SlMacLearningControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 7, 1)
)
slMacLearningControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    slMacLearningControlEntry.setStatus("current")


class _SlMacLearningControlStatus_Type(Integer32):
    """Custom type slMacLearningControlStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlMacLearningControlStatus_Type.__name__ = "Integer32"
_SlMacLearningControlStatus_Object = MibTableColumn
slMacLearningControlStatus = _SlMacLearningControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 7, 1, 1),
    _SlMacLearningControlStatus_Type()
)
slMacLearningControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slMacLearningControlStatus.setStatus("current")
_AlaSlMacAddressGlobalTable_Object = MibTable
alaSlMacAddressGlobalTable = _AlaSlMacAddressGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alaSlMacAddressGlobalTable.setStatus("current")
_AlaSlMacAddressGlobalEntry_Object = MibTableRow
alaSlMacAddressGlobalEntry = _AlaSlMacAddressGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1)
)
alaSlMacAddressGlobalEntry.setIndexNames(
    (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacDomain"),
    (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slLocaleType"),
    (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slOriginId"),
    (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slServiceId"),
    (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slSubId"),
    (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressGbl"),
)
if mibBuilder.loadTexts:
    alaSlMacAddressGlobalEntry.setStatus("current")


class _SlMacDomain_Type(Integer32):
    """Custom type slMacDomain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("evb", 4),
          ("spbm", 3),
          ("vlan", 1),
          ("vpls", 2))
    )


_SlMacDomain_Type.__name__ = "Integer32"
_SlMacDomain_Object = MibTableColumn
slMacDomain = _SlMacDomain_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 1),
    _SlMacDomain_Type()
)
slMacDomain.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slMacDomain.setStatus("current")


class _SlLocaleType_Type(Integer32):
    """Custom type slLocaleType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("sBind", 2),
          ("sap", 1))
    )


_SlLocaleType_Type.__name__ = "Integer32"
_SlLocaleType_Object = MibTableColumn
slLocaleType = _SlLocaleType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 2),
    _SlLocaleType_Type()
)
slLocaleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slLocaleType.setStatus("current")


class _SlOriginId_Type(Integer32):
    """Custom type slOriginId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_SlOriginId_Type.__name__ = "Integer32"
_SlOriginId_Object = MibTableColumn
slOriginId = _SlOriginId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 3),
    _SlOriginId_Type()
)
slOriginId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slOriginId.setStatus("current")


class _SlServiceId_Type(Integer32):
    """Custom type slServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32767),
    )


_SlServiceId_Type.__name__ = "Integer32"
_SlServiceId_Object = MibTableColumn
slServiceId = _SlServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 4),
    _SlServiceId_Type()
)
slServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slServiceId.setStatus("current")


class _SlSubId_Type(Integer32):
    """Custom type slSubId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SlSubId_Type.__name__ = "Integer32"
_SlSubId_Object = MibTableColumn
slSubId = _SlSubId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 5),
    _SlSubId_Type()
)
slSubId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slSubId.setStatus("current")
_SlMacAddressGbl_Type = MacAddress
_SlMacAddressGbl_Object = MibTableColumn
slMacAddressGbl = _SlMacAddressGbl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 6),
    _SlMacAddressGbl_Type()
)
slMacAddressGbl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slMacAddressGbl.setStatus("current")


class _SlMacAddressGblManagement_Type(Integer32):
    """Custom type slMacAddressGblManagement based on Integer32"""
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
        *(("deleteOnReset", 2),
          ("deleteOnTimeout", 3),
          ("learned", 4),
          ("permanent", 1),
          ("staticMulticast", 5))
    )


_SlMacAddressGblManagement_Type.__name__ = "Integer32"
_SlMacAddressGblManagement_Object = MibTableColumn
slMacAddressGblManagement = _SlMacAddressGblManagement_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 7),
    _SlMacAddressGblManagement_Type()
)
slMacAddressGblManagement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slMacAddressGblManagement.setStatus("current")


class _SlMacAddressGblDisposition_Type(Integer32):
    """Custom type slMacAddressGblDisposition based on Integer32"""
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
        *(("bridging", 1),
          ("filtering", 2),
          ("hostIntegrity", 4),
          ("quarantined", 3),
          ("userNetworkProf", 5))
    )


_SlMacAddressGblDisposition_Type.__name__ = "Integer32"
_SlMacAddressGblDisposition_Object = MibTableColumn
slMacAddressGblDisposition = _SlMacAddressGblDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 8),
    _SlMacAddressGblDisposition_Type()
)
slMacAddressGblDisposition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slMacAddressGblDisposition.setStatus("current")
_SlMacAddressGblRowStatus_Type = RowStatus
_SlMacAddressGblRowStatus_Object = MibTableColumn
slMacAddressGblRowStatus = _SlMacAddressGblRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 9),
    _SlMacAddressGblRowStatus_Type()
)
slMacAddressGblRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slMacAddressGblRowStatus.setStatus("current")
_SlMacAddressGblProtocol_Type = MacAddressProtocolType
_SlMacAddressGblProtocol_Object = MibTableColumn
slMacAddressGblProtocol = _SlMacAddressGblProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 10),
    _SlMacAddressGblProtocol_Type()
)
slMacAddressGblProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slMacAddressGblProtocol.setStatus("current")
_SlMacAddressGblGroupField_Type = Unsigned32
_SlMacAddressGblGroupField_Object = MibTableColumn
slMacAddressGblGroupField = _SlMacAddressGblGroupField_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 11),
    _SlMacAddressGblGroupField_Type()
)
slMacAddressGblGroupField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slMacAddressGblGroupField.setStatus("current")


class _SlSvcISID_Type(Integer32):
    """Custom type slSvcISID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(256, 16777214),
    )


_SlSvcISID_Type.__name__ = "Integer32"
_SlSvcISID_Object = MibTableColumn
slSvcISID = _SlSvcISID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 8, 1, 12),
    _SlSvcISID_Type()
)
slSvcISID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slSvcISID.setStatus("current")
_SlMacLearningVlanControlTable_Object = MibTable
slMacLearningVlanControlTable = _SlMacLearningVlanControlTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 10)
)
if mibBuilder.loadTexts:
    slMacLearningVlanControlTable.setStatus("current")
_SlMacLearningVlanControlEntry_Object = MibTableRow
slMacLearningVlanControlEntry = _SlMacLearningVlanControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 10, 1)
)
slMacLearningVlanControlEntry.setIndexNames(
    (0, "ALCATEL-IND1-VLAN-MGR-MIB", "vlanNumber"),
)
if mibBuilder.loadTexts:
    slMacLearningVlanControlEntry.setStatus("current")


class _SlMacLearningVlanControlStatus_Type(Integer32):
    """Custom type slMacLearningVlanControlStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlMacLearningVlanControlStatus_Type.__name__ = "Integer32"
_SlMacLearningVlanControlStatus_Object = MibTableColumn
slMacLearningVlanControlStatus = _SlMacLearningVlanControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 1, 10, 1, 1),
    _SlMacLearningVlanControlStatus_Type()
)
slMacLearningVlanControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slMacLearningVlanControlStatus.setStatus("current")
_AlcatelIND1MacAddressMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1MacAddressMIBConformance = _AlcatelIND1MacAddressMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1MacAddressMIBConformance.setStatus("current")
_AlcatelIND1MacAddressMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1MacAddressMIBGroups = _AlcatelIND1MacAddressMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1MacAddressMIBGroups.setStatus("current")
_AlcatelIND1MacAddressMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1MacAddressMIBCompliances = _AlcatelIND1MacAddressMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1MacAddressMIBCompliances.setStatus("current")

# Managed Objects groups

slMacAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 2, 1, 1)
)
slMacAddressGroup.setObjects(
      *(("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressGblManagement"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressGblDisposition"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressGblRowStatus"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressGblProtocol"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressGblGroupField"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slSvcISID"))
)
if mibBuilder.loadTexts:
    slMacAddressGroup.setStatus("current")

slMacAgingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 2, 1, 2)
)
slMacAgingGroup.setObjects(
      *(("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAgingValue"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAgingRowStatus"))
)
if mibBuilder.loadTexts:
    slMacAgingGroup.setStatus("current")

slMacGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 2, 1, 3)
)
slMacGeneralGroup.setObjects(
    ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slDistributedMacMode")
)
if mibBuilder.loadTexts:
    slMacGeneralGroup.setStatus("current")

slMacLearningGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 2, 1, 4)
)
slMacLearningGroup.setObjects(
    ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacLearningControlStatus")
)
if mibBuilder.loadTexts:
    slMacLearningGroup.setStatus("current")

slMacVlanLearningGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 2, 1, 5)
)
slMacVlanLearningGroup.setObjects(
    ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacLearningVlanControlStatus")
)
if mibBuilder.loadTexts:
    slMacVlanLearningGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1MacAddressMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1MacAddressMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-MAC-ADDRESS-MIB",
    **{"MacAddressProtocolType": MacAddressProtocolType,
       "alcatelIND1MacAddressMIB": alcatelIND1MacAddressMIB,
       "alcatelIND1MacAddressMIBNotifications": alcatelIND1MacAddressMIBNotifications,
       "alcatelIND1MacAddressMIBObjects": alcatelIND1MacAddressMIBObjects,
       "slMacAddressAgingTable": slMacAddressAgingTable,
       "slMacAddressAgingEntry": slMacAddressAgingEntry,
       "slMacAgingValue": slMacAgingValue,
       "slMacAgingRowStatus": slMacAgingRowStatus,
       "slDistributedMacMode": slDistributedMacMode,
       "slMacLearningControlTable": slMacLearningControlTable,
       "slMacLearningControlEntry": slMacLearningControlEntry,
       "slMacLearningControlStatus": slMacLearningControlStatus,
       "alaSlMacAddressGlobalTable": alaSlMacAddressGlobalTable,
       "alaSlMacAddressGlobalEntry": alaSlMacAddressGlobalEntry,
       "slMacDomain": slMacDomain,
       "slLocaleType": slLocaleType,
       "slOriginId": slOriginId,
       "slServiceId": slServiceId,
       "slSubId": slSubId,
       "slMacAddressGbl": slMacAddressGbl,
       "slMacAddressGblManagement": slMacAddressGblManagement,
       "slMacAddressGblDisposition": slMacAddressGblDisposition,
       "slMacAddressGblRowStatus": slMacAddressGblRowStatus,
       "slMacAddressGblProtocol": slMacAddressGblProtocol,
       "slMacAddressGblGroupField": slMacAddressGblGroupField,
       "slSvcISID": slSvcISID,
       "slMacLearningVlanControlTable": slMacLearningVlanControlTable,
       "slMacLearningVlanControlEntry": slMacLearningVlanControlEntry,
       "slMacLearningVlanControlStatus": slMacLearningVlanControlStatus,
       "alcatelIND1MacAddressMIBConformance": alcatelIND1MacAddressMIBConformance,
       "alcatelIND1MacAddressMIBGroups": alcatelIND1MacAddressMIBGroups,
       "slMacAddressGroup": slMacAddressGroup,
       "slMacAgingGroup": slMacAgingGroup,
       "slMacGeneralGroup": slMacGeneralGroup,
       "slMacLearningGroup": slMacLearningGroup,
       "slMacVlanLearningGroup": slMacVlanLearningGroup,
       "alcatelIND1MacAddressMIBCompliances": alcatelIND1MacAddressMIBCompliances,
       "alcatelIND1MacAddressMIBCompliance": alcatelIND1MacAddressMIBCompliance}
)

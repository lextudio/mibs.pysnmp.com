# SNMP MIB module (ENERGY-OBJECT-CONTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENERGY-OBJECT-CONTEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:31 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(IANAEnergyRelationship,) = mibBuilder.importSymbols(
    "IANA-ENERGY-RELATION-MIB",
    "IANAEnergyRelationship")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

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

(UUIDorZero,) = mibBuilder.importSymbols(
    "UUID-TC-MIB",
    "UUIDorZero")


# MODULE-IDENTITY

energyObjectContextMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 231)
)
energyObjectContextMIB.setRevisions(
        ("2015-02-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PethPsePortIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class PethPsePortGroupIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class LldpPortNumberOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )



class EnergyObjectKeywordList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )



# MIB Managed Objects in the order of their OIDs

_EnergyObjectContextMIBNotifs_ObjectIdentity = ObjectIdentity
energyObjectContextMIBNotifs = _EnergyObjectContextMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 231, 0)
)
_EnergyObjectContextMIBObjects_ObjectIdentity = ObjectIdentity
energyObjectContextMIBObjects = _EnergyObjectContextMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 231, 1)
)
_EoTable_Object = MibTable
eoTable = _EoTable_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 1)
)
if mibBuilder.loadTexts:
    eoTable.setStatus("current")
_EoEntry_Object = MibTableRow
eoEntry = _EoEntry_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 1, 1)
)
eoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    eoEntry.setStatus("current")


class _EoEthPortIndex_Type(PethPsePortIndexOrZero):
    """Custom type eoEthPortIndex based on PethPsePortIndexOrZero"""
    defaultValue = 0


_EoEthPortIndex_Object = MibTableColumn
eoEthPortIndex = _EoEthPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 1),
    _EoEthPortIndex_Type()
)
eoEthPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoEthPortIndex.setStatus("current")


class _EoEthPortGrpIndex_Type(PethPsePortGroupIndexOrZero):
    """Custom type eoEthPortGrpIndex based on PethPsePortGroupIndexOrZero"""
    defaultValue = 0


_EoEthPortGrpIndex_Object = MibTableColumn
eoEthPortGrpIndex = _EoEthPortGrpIndex_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 2),
    _EoEthPortGrpIndex_Type()
)
eoEthPortGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoEthPortGrpIndex.setStatus("current")


class _EoLldpPortNumber_Type(LldpPortNumberOrZero):
    """Custom type eoLldpPortNumber based on LldpPortNumberOrZero"""
    defaultValue = 0


_EoLldpPortNumber_Object = MibTableColumn
eoLldpPortNumber = _EoLldpPortNumber_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 3),
    _EoLldpPortNumber_Type()
)
eoLldpPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoLldpPortNumber.setStatus("current")
_EoMgmtMacAddress_Type = MacAddress
_EoMgmtMacAddress_Object = MibTableColumn
eoMgmtMacAddress = _EoMgmtMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 4),
    _EoMgmtMacAddress_Type()
)
eoMgmtMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoMgmtMacAddress.setStatus("current")
_EoMgmtAddressType_Type = InetAddressType
_EoMgmtAddressType_Object = MibTableColumn
eoMgmtAddressType = _EoMgmtAddressType_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 5),
    _EoMgmtAddressType_Type()
)
eoMgmtAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoMgmtAddressType.setStatus("current")
_EoMgmtAddress_Type = InetAddress
_EoMgmtAddress_Object = MibTableColumn
eoMgmtAddress = _EoMgmtAddress_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 6),
    _EoMgmtAddress_Type()
)
eoMgmtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoMgmtAddress.setStatus("current")
_EoMgmtDNSName_Type = OctetString
_EoMgmtDNSName_Object = MibTableColumn
eoMgmtDNSName = _EoMgmtDNSName_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 7),
    _EoMgmtDNSName_Type()
)
eoMgmtDNSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoMgmtDNSName.setStatus("current")
_EoDomainName_Type = SnmpAdminString
_EoDomainName_Object = MibTableColumn
eoDomainName = _EoDomainName_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 8),
    _EoDomainName_Type()
)
eoDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoDomainName.setStatus("current")
_EoRoleDescription_Type = SnmpAdminString
_EoRoleDescription_Object = MibTableColumn
eoRoleDescription = _EoRoleDescription_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 9),
    _EoRoleDescription_Type()
)
eoRoleDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoRoleDescription.setStatus("current")
_EoKeywords_Type = EnergyObjectKeywordList
_EoKeywords_Object = MibTableColumn
eoKeywords = _EoKeywords_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 10),
    _EoKeywords_Type()
)
eoKeywords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoKeywords.setStatus("current")


class _EoImportance_Type(Integer32):
    """Custom type eoImportance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EoImportance_Type.__name__ = "Integer32"
_EoImportance_Object = MibTableColumn
eoImportance = _EoImportance_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 11),
    _EoImportance_Type()
)
eoImportance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoImportance.setStatus("current")


class _EoPowerCategory_Type(Integer32):
    """Custom type eoPowerCategory based on Integer32"""
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
        *(("consumer", 0),
          ("distributor", 3),
          ("meter", 2),
          ("producer", 1),
          ("store", 4))
    )


_EoPowerCategory_Type.__name__ = "Integer32"
_EoPowerCategory_Object = MibTableColumn
eoPowerCategory = _EoPowerCategory_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 12),
    _EoPowerCategory_Type()
)
eoPowerCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoPowerCategory.setStatus("current")
_EoAlternateKey_Type = SnmpAdminString
_EoAlternateKey_Object = MibTableColumn
eoAlternateKey = _EoAlternateKey_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 13),
    _EoAlternateKey_Type()
)
eoAlternateKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eoAlternateKey.setStatus("current")


class _EoPowerInterfaceType_Type(Integer32):
    """Custom type eoPowerInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 2),
          ("inlet", 0),
          ("outlet", 1))
    )


_EoPowerInterfaceType_Type.__name__ = "Integer32"
_EoPowerInterfaceType_Object = MibTableColumn
eoPowerInterfaceType = _EoPowerInterfaceType_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 14),
    _EoPowerInterfaceType_Type()
)
eoPowerInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eoPowerInterfaceType.setStatus("current")
_EoRelationTable_Object = MibTable
eoRelationTable = _EoRelationTable_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 2)
)
if mibBuilder.loadTexts:
    eoRelationTable.setStatus("current")
_EoRelationEntry_Object = MibTableRow
eoRelationEntry = _EoRelationEntry_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 2, 1)
)
eoRelationEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "ENERGY-OBJECT-CONTEXT-MIB", "eoRelationIndex"),
)
if mibBuilder.loadTexts:
    eoRelationEntry.setStatus("current")


class _EoRelationIndex_Type(Integer32):
    """Custom type eoRelationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EoRelationIndex_Type.__name__ = "Integer32"
_EoRelationIndex_Object = MibTableColumn
eoRelationIndex = _EoRelationIndex_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 1),
    _EoRelationIndex_Type()
)
eoRelationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eoRelationIndex.setStatus("current")
_EoRelationID_Type = UUIDorZero
_EoRelationID_Object = MibTableColumn
eoRelationID = _EoRelationID_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 2),
    _EoRelationID_Type()
)
eoRelationID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eoRelationID.setStatus("current")
_EoRelationship_Type = IANAEnergyRelationship
_EoRelationship_Object = MibTableColumn
eoRelationship = _EoRelationship_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 3),
    _EoRelationship_Type()
)
eoRelationship.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eoRelationship.setStatus("current")
_EoRelationStatus_Type = RowStatus
_EoRelationStatus_Object = MibTableColumn
eoRelationStatus = _EoRelationStatus_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 4),
    _EoRelationStatus_Type()
)
eoRelationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eoRelationStatus.setStatus("current")


class _EoRelationStorageType_Type(StorageType):
    """Custom type eoRelationStorageType based on StorageType"""


_EoRelationStorageType_Object = MibTableColumn
eoRelationStorageType = _EoRelationStorageType_Object(
    (1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 5),
    _EoRelationStorageType_Type()
)
eoRelationStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eoRelationStorageType.setStatus("current")
_EnergyObjectContextMIBConform_ObjectIdentity = ObjectIdentity
energyObjectContextMIBConform = _EnergyObjectContextMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 231, 2)
)
_EnergyObjectContextMIBCompliances_ObjectIdentity = ObjectIdentity
energyObjectContextMIBCompliances = _EnergyObjectContextMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 231, 2, 1)
)
_EnergyObjectContextMIBGroups_ObjectIdentity = ObjectIdentity
energyObjectContextMIBGroups = _EnergyObjectContextMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 231, 2, 2)
)

# Managed Objects groups

energyObjectContextMIBTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 231, 2, 2, 1)
)
energyObjectContextMIBTableGroup.setObjects(
      *(("ENERGY-OBJECT-CONTEXT-MIB", "eoDomainName"),
        ("ENERGY-OBJECT-CONTEXT-MIB", "eoRoleDescription"),
        ("ENERGY-OBJECT-CONTEXT-MIB", "eoAlternateKey"),
        ("ENERGY-OBJECT-CONTEXT-MIB", "eoKeywords"),
        ("ENERGY-OBJECT-CONTEXT-MIB", "eoImportance"),
        ("ENERGY-OBJECT-CONTEXT-MIB", "eoPowerCategory"),
        ("ENERGY-OBJECT-CONTEXT-MIB", "eoPowerInterfaceType"))
)
if mibBuilder.loadTexts:
    energyObjectContextMIBTableGroup.setStatus("current")

energyObjectOptionalMIBTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 231, 2, 2, 2)
)
energyObjectOptionalMIBTableGroup.setObjects(
      *(("ENERGY-OBJECT-CONTEXT-MIB", "eoEthPortIndex"),
        ("ENERGY-OBJECT-CONTEXT-MIB", "eoEthPortGrpIndex"),
        ("ENERGY-OBJECT-CONTEXT-MIB", "eoLldpPortNumber"),
        ("ENERGY-OBJECT-CONTEXT-MIB", "eoMgmtMacAddress"),
        ("ENERGY-OBJECT-CONTEXT-MIB", "eoMgmtAddressType"),
        ("ENERGY-OBJECT-CONTEXT-MIB", "eoMgmtAddress"),
        ("ENERGY-OBJECT-CONTEXT-MIB", "eoMgmtDNSName"))
)
if mibBuilder.loadTexts:
    energyObjectOptionalMIBTableGroup.setStatus("current")

energyObjectRelationTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 231, 2, 2, 3)
)
energyObjectRelationTableGroup.setObjects(
      *(("ENERGY-OBJECT-CONTEXT-MIB", "eoRelationID"),
        ("ENERGY-OBJECT-CONTEXT-MIB", "eoRelationship"),
        ("ENERGY-OBJECT-CONTEXT-MIB", "eoRelationStatus"),
        ("ENERGY-OBJECT-CONTEXT-MIB", "eoRelationStorageType"))
)
if mibBuilder.loadTexts:
    energyObjectRelationTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

energyObjectContextMIBFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 231, 2, 1, 1)
)
if mibBuilder.loadTexts:
    energyObjectContextMIBFullCompliance.setStatus(
        "current"
    )

energyObjectContextMIBReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 231, 2, 1, 2)
)
if mibBuilder.loadTexts:
    energyObjectContextMIBReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENERGY-OBJECT-CONTEXT-MIB",
    **{"PethPsePortIndexOrZero": PethPsePortIndexOrZero,
       "PethPsePortGroupIndexOrZero": PethPsePortGroupIndexOrZero,
       "LldpPortNumberOrZero": LldpPortNumberOrZero,
       "EnergyObjectKeywordList": EnergyObjectKeywordList,
       "energyObjectContextMIB": energyObjectContextMIB,
       "energyObjectContextMIBNotifs": energyObjectContextMIBNotifs,
       "energyObjectContextMIBObjects": energyObjectContextMIBObjects,
       "eoTable": eoTable,
       "eoEntry": eoEntry,
       "eoEthPortIndex": eoEthPortIndex,
       "eoEthPortGrpIndex": eoEthPortGrpIndex,
       "eoLldpPortNumber": eoLldpPortNumber,
       "eoMgmtMacAddress": eoMgmtMacAddress,
       "eoMgmtAddressType": eoMgmtAddressType,
       "eoMgmtAddress": eoMgmtAddress,
       "eoMgmtDNSName": eoMgmtDNSName,
       "eoDomainName": eoDomainName,
       "eoRoleDescription": eoRoleDescription,
       "eoKeywords": eoKeywords,
       "eoImportance": eoImportance,
       "eoPowerCategory": eoPowerCategory,
       "eoAlternateKey": eoAlternateKey,
       "eoPowerInterfaceType": eoPowerInterfaceType,
       "eoRelationTable": eoRelationTable,
       "eoRelationEntry": eoRelationEntry,
       "eoRelationIndex": eoRelationIndex,
       "eoRelationID": eoRelationID,
       "eoRelationship": eoRelationship,
       "eoRelationStatus": eoRelationStatus,
       "eoRelationStorageType": eoRelationStorageType,
       "energyObjectContextMIBConform": energyObjectContextMIBConform,
       "energyObjectContextMIBCompliances": energyObjectContextMIBCompliances,
       "energyObjectContextMIBFullCompliance": energyObjectContextMIBFullCompliance,
       "energyObjectContextMIBReadOnlyCompliance": energyObjectContextMIBReadOnlyCompliance,
       "energyObjectContextMIBGroups": energyObjectContextMIBGroups,
       "energyObjectContextMIBTableGroup": energyObjectContextMIBTableGroup,
       "energyObjectOptionalMIBTableGroup": energyObjectOptionalMIBTableGroup,
       "energyObjectRelationTableGroup": energyObjectRelationTableGroup}
)

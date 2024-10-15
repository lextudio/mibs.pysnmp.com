# SNMP MIB module (IPS-AUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPS-AUTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:07 2024
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

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

(AutonomousType,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ipsAuthMibModule = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 141)
)
ipsAuthMibModule.setRevisions(
        ("2006-05-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IpsAuthAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_IpsAuthNotifications_ObjectIdentity = ObjectIdentity
ipsAuthNotifications = _IpsAuthNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 0)
)
_IpsAuthObjects_ObjectIdentity = ObjectIdentity
ipsAuthObjects = _IpsAuthObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 1)
)
_IpsAuthDescriptors_ObjectIdentity = ObjectIdentity
ipsAuthDescriptors = _IpsAuthDescriptors_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 1, 1)
)
_IpsAuthMethodTypes_ObjectIdentity = ObjectIdentity
ipsAuthMethodTypes = _IpsAuthMethodTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipsAuthMethodTypes.setStatus("current")
_IpsAuthMethodNone_ObjectIdentity = ObjectIdentity
ipsAuthMethodNone = _IpsAuthMethodNone_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipsAuthMethodNone.setStatus("current")
_IpsAuthMethodSrp_ObjectIdentity = ObjectIdentity
ipsAuthMethodSrp = _IpsAuthMethodSrp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipsAuthMethodSrp.setStatus("current")
_IpsAuthMethodChap_ObjectIdentity = ObjectIdentity
ipsAuthMethodChap = _IpsAuthMethodChap_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ipsAuthMethodChap.setStatus("current")
_IpsAuthMethodKerberos_ObjectIdentity = ObjectIdentity
ipsAuthMethodKerberos = _IpsAuthMethodKerberos_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ipsAuthMethodKerberos.setStatus("current")
_IpsAuthInstance_ObjectIdentity = ObjectIdentity
ipsAuthInstance = _IpsAuthInstance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 1, 2)
)
_IpsAuthInstanceAttributesTable_Object = MibTable
ipsAuthInstanceAttributesTable = _IpsAuthInstanceAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ipsAuthInstanceAttributesTable.setStatus("current")
_IpsAuthInstanceAttributesEntry_Object = MibTableRow
ipsAuthInstanceAttributesEntry = _IpsAuthInstanceAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 2, 2, 1)
)
ipsAuthInstanceAttributesEntry.setIndexNames(
    (0, "IPS-AUTH-MIB", "ipsAuthInstIndex"),
)
if mibBuilder.loadTexts:
    ipsAuthInstanceAttributesEntry.setStatus("current")


class _IpsAuthInstIndex_Type(Unsigned32):
    """Custom type ipsAuthInstIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpsAuthInstIndex_Type.__name__ = "Unsigned32"
_IpsAuthInstIndex_Object = MibTableColumn
ipsAuthInstIndex = _IpsAuthInstIndex_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 2, 2, 1, 1),
    _IpsAuthInstIndex_Type()
)
ipsAuthInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsAuthInstIndex.setStatus("current")
_IpsAuthInstDescr_Type = SnmpAdminString
_IpsAuthInstDescr_Object = MibTableColumn
ipsAuthInstDescr = _IpsAuthInstDescr_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 2, 2, 1, 2),
    _IpsAuthInstDescr_Type()
)
ipsAuthInstDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsAuthInstDescr.setStatus("current")


class _IpsAuthInstStorageType_Type(StorageType):
    """Custom type ipsAuthInstStorageType based on StorageType"""


_IpsAuthInstStorageType_Object = MibTableColumn
ipsAuthInstStorageType = _IpsAuthInstStorageType_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 2, 2, 1, 3),
    _IpsAuthInstStorageType_Type()
)
ipsAuthInstStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsAuthInstStorageType.setStatus("current")
_IpsAuthIdentity_ObjectIdentity = ObjectIdentity
ipsAuthIdentity = _IpsAuthIdentity_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 1, 3)
)
_IpsAuthIdentAttributesTable_Object = MibTable
ipsAuthIdentAttributesTable = _IpsAuthIdentAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ipsAuthIdentAttributesTable.setStatus("current")
_IpsAuthIdentAttributesEntry_Object = MibTableRow
ipsAuthIdentAttributesEntry = _IpsAuthIdentAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 3, 1, 1)
)
ipsAuthIdentAttributesEntry.setIndexNames(
    (0, "IPS-AUTH-MIB", "ipsAuthInstIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"),
)
if mibBuilder.loadTexts:
    ipsAuthIdentAttributesEntry.setStatus("current")


class _IpsAuthIdentIndex_Type(Unsigned32):
    """Custom type ipsAuthIdentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpsAuthIdentIndex_Type.__name__ = "Unsigned32"
_IpsAuthIdentIndex_Object = MibTableColumn
ipsAuthIdentIndex = _IpsAuthIdentIndex_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 3, 1, 1, 1),
    _IpsAuthIdentIndex_Type()
)
ipsAuthIdentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsAuthIdentIndex.setStatus("current")
_IpsAuthIdentDescription_Type = SnmpAdminString
_IpsAuthIdentDescription_Object = MibTableColumn
ipsAuthIdentDescription = _IpsAuthIdentDescription_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 3, 1, 1, 2),
    _IpsAuthIdentDescription_Type()
)
ipsAuthIdentDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentDescription.setStatus("current")
_IpsAuthIdentRowStatus_Type = RowStatus
_IpsAuthIdentRowStatus_Object = MibTableColumn
ipsAuthIdentRowStatus = _IpsAuthIdentRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 3, 1, 1, 3),
    _IpsAuthIdentRowStatus_Type()
)
ipsAuthIdentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentRowStatus.setStatus("current")


class _IpsAuthIdentStorageType_Type(StorageType):
    """Custom type ipsAuthIdentStorageType based on StorageType"""


_IpsAuthIdentStorageType_Object = MibTableColumn
ipsAuthIdentStorageType = _IpsAuthIdentStorageType_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 3, 1, 1, 4),
    _IpsAuthIdentStorageType_Type()
)
ipsAuthIdentStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentStorageType.setStatus("current")
_IpsAuthIdentityName_ObjectIdentity = ObjectIdentity
ipsAuthIdentityName = _IpsAuthIdentityName_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 1, 4)
)
_IpsAuthIdentNameAttributesTable_Object = MibTable
ipsAuthIdentNameAttributesTable = _IpsAuthIdentNameAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ipsAuthIdentNameAttributesTable.setStatus("current")
_IpsAuthIdentNameAttributesEntry_Object = MibTableRow
ipsAuthIdentNameAttributesEntry = _IpsAuthIdentNameAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 4, 1, 1)
)
ipsAuthIdentNameAttributesEntry.setIndexNames(
    (0, "IPS-AUTH-MIB", "ipsAuthInstIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthIdentNameIndex"),
)
if mibBuilder.loadTexts:
    ipsAuthIdentNameAttributesEntry.setStatus("current")


class _IpsAuthIdentNameIndex_Type(Unsigned32):
    """Custom type ipsAuthIdentNameIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpsAuthIdentNameIndex_Type.__name__ = "Unsigned32"
_IpsAuthIdentNameIndex_Object = MibTableColumn
ipsAuthIdentNameIndex = _IpsAuthIdentNameIndex_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 4, 1, 1, 1),
    _IpsAuthIdentNameIndex_Type()
)
ipsAuthIdentNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsAuthIdentNameIndex.setStatus("current")
_IpsAuthIdentName_Type = SnmpAdminString
_IpsAuthIdentName_Object = MibTableColumn
ipsAuthIdentName = _IpsAuthIdentName_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 4, 1, 1, 2),
    _IpsAuthIdentName_Type()
)
ipsAuthIdentName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentName.setStatus("current")
_IpsAuthIdentNameRowStatus_Type = RowStatus
_IpsAuthIdentNameRowStatus_Object = MibTableColumn
ipsAuthIdentNameRowStatus = _IpsAuthIdentNameRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 4, 1, 1, 3),
    _IpsAuthIdentNameRowStatus_Type()
)
ipsAuthIdentNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentNameRowStatus.setStatus("current")


class _IpsAuthIdentNameStorageType_Type(StorageType):
    """Custom type ipsAuthIdentNameStorageType based on StorageType"""


_IpsAuthIdentNameStorageType_Object = MibTableColumn
ipsAuthIdentNameStorageType = _IpsAuthIdentNameStorageType_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 4, 1, 1, 4),
    _IpsAuthIdentNameStorageType_Type()
)
ipsAuthIdentNameStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentNameStorageType.setStatus("current")
_IpsAuthIdentityAddress_ObjectIdentity = ObjectIdentity
ipsAuthIdentityAddress = _IpsAuthIdentityAddress_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 1, 5)
)
_IpsAuthIdentAddrAttributesTable_Object = MibTable
ipsAuthIdentAddrAttributesTable = _IpsAuthIdentAddrAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ipsAuthIdentAddrAttributesTable.setStatus("current")
_IpsAuthIdentAddrAttributesEntry_Object = MibTableRow
ipsAuthIdentAddrAttributesEntry = _IpsAuthIdentAddrAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1)
)
ipsAuthIdentAddrAttributesEntry.setIndexNames(
    (0, "IPS-AUTH-MIB", "ipsAuthInstIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthIdentAddrIndex"),
)
if mibBuilder.loadTexts:
    ipsAuthIdentAddrAttributesEntry.setStatus("current")


class _IpsAuthIdentAddrIndex_Type(Unsigned32):
    """Custom type ipsAuthIdentAddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpsAuthIdentAddrIndex_Type.__name__ = "Unsigned32"
_IpsAuthIdentAddrIndex_Object = MibTableColumn
ipsAuthIdentAddrIndex = _IpsAuthIdentAddrIndex_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1, 1),
    _IpsAuthIdentAddrIndex_Type()
)
ipsAuthIdentAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsAuthIdentAddrIndex.setStatus("current")
_IpsAuthIdentAddrType_Type = AddressFamilyNumbers
_IpsAuthIdentAddrType_Object = MibTableColumn
ipsAuthIdentAddrType = _IpsAuthIdentAddrType_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1, 2),
    _IpsAuthIdentAddrType_Type()
)
ipsAuthIdentAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentAddrType.setStatus("current")
_IpsAuthIdentAddrStart_Type = IpsAuthAddress
_IpsAuthIdentAddrStart_Object = MibTableColumn
ipsAuthIdentAddrStart = _IpsAuthIdentAddrStart_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1, 3),
    _IpsAuthIdentAddrStart_Type()
)
ipsAuthIdentAddrStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentAddrStart.setStatus("current")
_IpsAuthIdentAddrEnd_Type = IpsAuthAddress
_IpsAuthIdentAddrEnd_Object = MibTableColumn
ipsAuthIdentAddrEnd = _IpsAuthIdentAddrEnd_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1, 4),
    _IpsAuthIdentAddrEnd_Type()
)
ipsAuthIdentAddrEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentAddrEnd.setStatus("current")
_IpsAuthIdentAddrRowStatus_Type = RowStatus
_IpsAuthIdentAddrRowStatus_Object = MibTableColumn
ipsAuthIdentAddrRowStatus = _IpsAuthIdentAddrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1, 5),
    _IpsAuthIdentAddrRowStatus_Type()
)
ipsAuthIdentAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentAddrRowStatus.setStatus("current")


class _IpsAuthIdentAddrStorageType_Type(StorageType):
    """Custom type ipsAuthIdentAddrStorageType based on StorageType"""


_IpsAuthIdentAddrStorageType_Object = MibTableColumn
ipsAuthIdentAddrStorageType = _IpsAuthIdentAddrStorageType_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1, 6),
    _IpsAuthIdentAddrStorageType_Type()
)
ipsAuthIdentAddrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentAddrStorageType.setStatus("current")
_IpsAuthCredential_ObjectIdentity = ObjectIdentity
ipsAuthCredential = _IpsAuthCredential_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 1, 6)
)
_IpsAuthCredentialAttributesTable_Object = MibTable
ipsAuthCredentialAttributesTable = _IpsAuthCredentialAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ipsAuthCredentialAttributesTable.setStatus("current")
_IpsAuthCredentialAttributesEntry_Object = MibTableRow
ipsAuthCredentialAttributesEntry = _IpsAuthCredentialAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 6, 1, 1)
)
ipsAuthCredentialAttributesEntry.setIndexNames(
    (0, "IPS-AUTH-MIB", "ipsAuthInstIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthCredIndex"),
)
if mibBuilder.loadTexts:
    ipsAuthCredentialAttributesEntry.setStatus("current")


class _IpsAuthCredIndex_Type(Unsigned32):
    """Custom type ipsAuthCredIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpsAuthCredIndex_Type.__name__ = "Unsigned32"
_IpsAuthCredIndex_Object = MibTableColumn
ipsAuthCredIndex = _IpsAuthCredIndex_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 6, 1, 1, 1),
    _IpsAuthCredIndex_Type()
)
ipsAuthCredIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsAuthCredIndex.setStatus("current")
_IpsAuthCredAuthMethod_Type = AutonomousType
_IpsAuthCredAuthMethod_Object = MibTableColumn
ipsAuthCredAuthMethod = _IpsAuthCredAuthMethod_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 6, 1, 1, 2),
    _IpsAuthCredAuthMethod_Type()
)
ipsAuthCredAuthMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredAuthMethod.setStatus("current")
_IpsAuthCredRowStatus_Type = RowStatus
_IpsAuthCredRowStatus_Object = MibTableColumn
ipsAuthCredRowStatus = _IpsAuthCredRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 6, 1, 1, 3),
    _IpsAuthCredRowStatus_Type()
)
ipsAuthCredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredRowStatus.setStatus("current")


class _IpsAuthCredStorageType_Type(StorageType):
    """Custom type ipsAuthCredStorageType based on StorageType"""


_IpsAuthCredStorageType_Object = MibTableColumn
ipsAuthCredStorageType = _IpsAuthCredStorageType_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 6, 1, 1, 4),
    _IpsAuthCredStorageType_Type()
)
ipsAuthCredStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredStorageType.setStatus("current")
_IpsAuthCredChap_ObjectIdentity = ObjectIdentity
ipsAuthCredChap = _IpsAuthCredChap_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 1, 7)
)
_IpsAuthCredChapAttributesTable_Object = MibTable
ipsAuthCredChapAttributesTable = _IpsAuthCredChapAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ipsAuthCredChapAttributesTable.setStatus("current")
_IpsAuthCredChapAttributesEntry_Object = MibTableRow
ipsAuthCredChapAttributesEntry = _IpsAuthCredChapAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 7, 1, 1)
)
ipsAuthCredChapAttributesEntry.setIndexNames(
    (0, "IPS-AUTH-MIB", "ipsAuthInstIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthCredIndex"),
)
if mibBuilder.loadTexts:
    ipsAuthCredChapAttributesEntry.setStatus("current")
_IpsAuthCredChapUserName_Type = SnmpAdminString
_IpsAuthCredChapUserName_Object = MibTableColumn
ipsAuthCredChapUserName = _IpsAuthCredChapUserName_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 7, 1, 1, 1),
    _IpsAuthCredChapUserName_Type()
)
ipsAuthCredChapUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredChapUserName.setStatus("current")
_IpsAuthCredChapRowStatus_Type = RowStatus
_IpsAuthCredChapRowStatus_Object = MibTableColumn
ipsAuthCredChapRowStatus = _IpsAuthCredChapRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 7, 1, 1, 2),
    _IpsAuthCredChapRowStatus_Type()
)
ipsAuthCredChapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredChapRowStatus.setStatus("current")


class _IpsAuthCredChapStorageType_Type(StorageType):
    """Custom type ipsAuthCredChapStorageType based on StorageType"""


_IpsAuthCredChapStorageType_Object = MibTableColumn
ipsAuthCredChapStorageType = _IpsAuthCredChapStorageType_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 7, 1, 1, 3),
    _IpsAuthCredChapStorageType_Type()
)
ipsAuthCredChapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredChapStorageType.setStatus("current")
_IpsAuthCredSrp_ObjectIdentity = ObjectIdentity
ipsAuthCredSrp = _IpsAuthCredSrp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 1, 8)
)
_IpsAuthCredSrpAttributesTable_Object = MibTable
ipsAuthCredSrpAttributesTable = _IpsAuthCredSrpAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 8, 1)
)
if mibBuilder.loadTexts:
    ipsAuthCredSrpAttributesTable.setStatus("current")
_IpsAuthCredSrpAttributesEntry_Object = MibTableRow
ipsAuthCredSrpAttributesEntry = _IpsAuthCredSrpAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 8, 1, 1)
)
ipsAuthCredSrpAttributesEntry.setIndexNames(
    (0, "IPS-AUTH-MIB", "ipsAuthInstIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthCredIndex"),
)
if mibBuilder.loadTexts:
    ipsAuthCredSrpAttributesEntry.setStatus("current")
_IpsAuthCredSrpUserName_Type = SnmpAdminString
_IpsAuthCredSrpUserName_Object = MibTableColumn
ipsAuthCredSrpUserName = _IpsAuthCredSrpUserName_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 8, 1, 1, 1),
    _IpsAuthCredSrpUserName_Type()
)
ipsAuthCredSrpUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredSrpUserName.setStatus("current")
_IpsAuthCredSrpRowStatus_Type = RowStatus
_IpsAuthCredSrpRowStatus_Object = MibTableColumn
ipsAuthCredSrpRowStatus = _IpsAuthCredSrpRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 8, 1, 1, 2),
    _IpsAuthCredSrpRowStatus_Type()
)
ipsAuthCredSrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredSrpRowStatus.setStatus("current")


class _IpsAuthCredSrpStorageType_Type(StorageType):
    """Custom type ipsAuthCredSrpStorageType based on StorageType"""


_IpsAuthCredSrpStorageType_Object = MibTableColumn
ipsAuthCredSrpStorageType = _IpsAuthCredSrpStorageType_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 8, 1, 1, 3),
    _IpsAuthCredSrpStorageType_Type()
)
ipsAuthCredSrpStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredSrpStorageType.setStatus("current")
_IpsAuthCredKerberos_ObjectIdentity = ObjectIdentity
ipsAuthCredKerberos = _IpsAuthCredKerberos_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 1, 9)
)
_IpsAuthCredKerbAttributesTable_Object = MibTable
ipsAuthCredKerbAttributesTable = _IpsAuthCredKerbAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 9, 1)
)
if mibBuilder.loadTexts:
    ipsAuthCredKerbAttributesTable.setStatus("current")
_IpsAuthCredKerbAttributesEntry_Object = MibTableRow
ipsAuthCredKerbAttributesEntry = _IpsAuthCredKerbAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 9, 1, 1)
)
ipsAuthCredKerbAttributesEntry.setIndexNames(
    (0, "IPS-AUTH-MIB", "ipsAuthInstIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthCredIndex"),
)
if mibBuilder.loadTexts:
    ipsAuthCredKerbAttributesEntry.setStatus("current")
_IpsAuthCredKerbPrincipal_Type = SnmpAdminString
_IpsAuthCredKerbPrincipal_Object = MibTableColumn
ipsAuthCredKerbPrincipal = _IpsAuthCredKerbPrincipal_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 9, 1, 1, 1),
    _IpsAuthCredKerbPrincipal_Type()
)
ipsAuthCredKerbPrincipal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredKerbPrincipal.setStatus("current")
_IpsAuthCredKerbRowStatus_Type = RowStatus
_IpsAuthCredKerbRowStatus_Object = MibTableColumn
ipsAuthCredKerbRowStatus = _IpsAuthCredKerbRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 9, 1, 1, 2),
    _IpsAuthCredKerbRowStatus_Type()
)
ipsAuthCredKerbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredKerbRowStatus.setStatus("current")


class _IpsAuthCredKerbStorageType_Type(StorageType):
    """Custom type ipsAuthCredKerbStorageType based on StorageType"""


_IpsAuthCredKerbStorageType_Object = MibTableColumn
ipsAuthCredKerbStorageType = _IpsAuthCredKerbStorageType_Object(
    (1, 3, 6, 1, 2, 1, 141, 1, 9, 1, 1, 3),
    _IpsAuthCredKerbStorageType_Type()
)
ipsAuthCredKerbStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredKerbStorageType.setStatus("current")
_IpsAuthConformance_ObjectIdentity = ObjectIdentity
ipsAuthConformance = _IpsAuthConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 2)
)
_IpsAuthCompliances_ObjectIdentity = ObjectIdentity
ipsAuthCompliances = _IpsAuthCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 2, 1)
)
_IpsAuthGroups_ObjectIdentity = ObjectIdentity
ipsAuthGroups = _IpsAuthGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 141, 2, 2)
)

# Managed Objects groups

ipsAuthInstanceAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 141, 2, 2, 1)
)
ipsAuthInstanceAttributesGroup.setObjects(
      *(("IPS-AUTH-MIB", "ipsAuthInstDescr"),
        ("IPS-AUTH-MIB", "ipsAuthInstStorageType"))
)
if mibBuilder.loadTexts:
    ipsAuthInstanceAttributesGroup.setStatus("current")

ipsAuthIdentAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 141, 2, 2, 2)
)
ipsAuthIdentAttributesGroup.setObjects(
      *(("IPS-AUTH-MIB", "ipsAuthIdentDescription"),
        ("IPS-AUTH-MIB", "ipsAuthIdentRowStatus"),
        ("IPS-AUTH-MIB", "ipsAuthIdentStorageType"))
)
if mibBuilder.loadTexts:
    ipsAuthIdentAttributesGroup.setStatus("current")

ipsAuthIdentNameAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 141, 2, 2, 3)
)
ipsAuthIdentNameAttributesGroup.setObjects(
      *(("IPS-AUTH-MIB", "ipsAuthIdentName"),
        ("IPS-AUTH-MIB", "ipsAuthIdentNameRowStatus"),
        ("IPS-AUTH-MIB", "ipsAuthIdentNameStorageType"))
)
if mibBuilder.loadTexts:
    ipsAuthIdentNameAttributesGroup.setStatus("current")

ipsAuthIdentAddrAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 141, 2, 2, 4)
)
ipsAuthIdentAddrAttributesGroup.setObjects(
      *(("IPS-AUTH-MIB", "ipsAuthIdentAddrType"),
        ("IPS-AUTH-MIB", "ipsAuthIdentAddrStart"),
        ("IPS-AUTH-MIB", "ipsAuthIdentAddrEnd"),
        ("IPS-AUTH-MIB", "ipsAuthIdentAddrRowStatus"),
        ("IPS-AUTH-MIB", "ipsAuthIdentAddrStorageType"))
)
if mibBuilder.loadTexts:
    ipsAuthIdentAddrAttributesGroup.setStatus("current")

ipsAuthIdentCredAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 141, 2, 2, 5)
)
ipsAuthIdentCredAttributesGroup.setObjects(
      *(("IPS-AUTH-MIB", "ipsAuthCredAuthMethod"),
        ("IPS-AUTH-MIB", "ipsAuthCredRowStatus"),
        ("IPS-AUTH-MIB", "ipsAuthCredStorageType"))
)
if mibBuilder.loadTexts:
    ipsAuthIdentCredAttributesGroup.setStatus("current")

ipsAuthIdentChapAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 141, 2, 2, 6)
)
ipsAuthIdentChapAttrGroup.setObjects(
      *(("IPS-AUTH-MIB", "ipsAuthCredChapUserName"),
        ("IPS-AUTH-MIB", "ipsAuthCredChapRowStatus"),
        ("IPS-AUTH-MIB", "ipsAuthCredChapStorageType"))
)
if mibBuilder.loadTexts:
    ipsAuthIdentChapAttrGroup.setStatus("current")

ipsAuthIdentSrpAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 141, 2, 2, 7)
)
ipsAuthIdentSrpAttrGroup.setObjects(
      *(("IPS-AUTH-MIB", "ipsAuthCredSrpUserName"),
        ("IPS-AUTH-MIB", "ipsAuthCredSrpRowStatus"),
        ("IPS-AUTH-MIB", "ipsAuthCredSrpStorageType"))
)
if mibBuilder.loadTexts:
    ipsAuthIdentSrpAttrGroup.setStatus("current")

ipsAuthIdentKerberosAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 141, 2, 2, 8)
)
ipsAuthIdentKerberosAttrGroup.setObjects(
      *(("IPS-AUTH-MIB", "ipsAuthCredKerbPrincipal"),
        ("IPS-AUTH-MIB", "ipsAuthCredKerbRowStatus"),
        ("IPS-AUTH-MIB", "ipsAuthCredKerbStorageType"))
)
if mibBuilder.loadTexts:
    ipsAuthIdentKerberosAttrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipsAuthComplianceV1 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 141, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ipsAuthComplianceV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPS-AUTH-MIB",
    **{"IpsAuthAddress": IpsAuthAddress,
       "ipsAuthMibModule": ipsAuthMibModule,
       "ipsAuthNotifications": ipsAuthNotifications,
       "ipsAuthObjects": ipsAuthObjects,
       "ipsAuthDescriptors": ipsAuthDescriptors,
       "ipsAuthMethodTypes": ipsAuthMethodTypes,
       "ipsAuthMethodNone": ipsAuthMethodNone,
       "ipsAuthMethodSrp": ipsAuthMethodSrp,
       "ipsAuthMethodChap": ipsAuthMethodChap,
       "ipsAuthMethodKerberos": ipsAuthMethodKerberos,
       "ipsAuthInstance": ipsAuthInstance,
       "ipsAuthInstanceAttributesTable": ipsAuthInstanceAttributesTable,
       "ipsAuthInstanceAttributesEntry": ipsAuthInstanceAttributesEntry,
       "ipsAuthInstIndex": ipsAuthInstIndex,
       "ipsAuthInstDescr": ipsAuthInstDescr,
       "ipsAuthInstStorageType": ipsAuthInstStorageType,
       "ipsAuthIdentity": ipsAuthIdentity,
       "ipsAuthIdentAttributesTable": ipsAuthIdentAttributesTable,
       "ipsAuthIdentAttributesEntry": ipsAuthIdentAttributesEntry,
       "ipsAuthIdentIndex": ipsAuthIdentIndex,
       "ipsAuthIdentDescription": ipsAuthIdentDescription,
       "ipsAuthIdentRowStatus": ipsAuthIdentRowStatus,
       "ipsAuthIdentStorageType": ipsAuthIdentStorageType,
       "ipsAuthIdentityName": ipsAuthIdentityName,
       "ipsAuthIdentNameAttributesTable": ipsAuthIdentNameAttributesTable,
       "ipsAuthIdentNameAttributesEntry": ipsAuthIdentNameAttributesEntry,
       "ipsAuthIdentNameIndex": ipsAuthIdentNameIndex,
       "ipsAuthIdentName": ipsAuthIdentName,
       "ipsAuthIdentNameRowStatus": ipsAuthIdentNameRowStatus,
       "ipsAuthIdentNameStorageType": ipsAuthIdentNameStorageType,
       "ipsAuthIdentityAddress": ipsAuthIdentityAddress,
       "ipsAuthIdentAddrAttributesTable": ipsAuthIdentAddrAttributesTable,
       "ipsAuthIdentAddrAttributesEntry": ipsAuthIdentAddrAttributesEntry,
       "ipsAuthIdentAddrIndex": ipsAuthIdentAddrIndex,
       "ipsAuthIdentAddrType": ipsAuthIdentAddrType,
       "ipsAuthIdentAddrStart": ipsAuthIdentAddrStart,
       "ipsAuthIdentAddrEnd": ipsAuthIdentAddrEnd,
       "ipsAuthIdentAddrRowStatus": ipsAuthIdentAddrRowStatus,
       "ipsAuthIdentAddrStorageType": ipsAuthIdentAddrStorageType,
       "ipsAuthCredential": ipsAuthCredential,
       "ipsAuthCredentialAttributesTable": ipsAuthCredentialAttributesTable,
       "ipsAuthCredentialAttributesEntry": ipsAuthCredentialAttributesEntry,
       "ipsAuthCredIndex": ipsAuthCredIndex,
       "ipsAuthCredAuthMethod": ipsAuthCredAuthMethod,
       "ipsAuthCredRowStatus": ipsAuthCredRowStatus,
       "ipsAuthCredStorageType": ipsAuthCredStorageType,
       "ipsAuthCredChap": ipsAuthCredChap,
       "ipsAuthCredChapAttributesTable": ipsAuthCredChapAttributesTable,
       "ipsAuthCredChapAttributesEntry": ipsAuthCredChapAttributesEntry,
       "ipsAuthCredChapUserName": ipsAuthCredChapUserName,
       "ipsAuthCredChapRowStatus": ipsAuthCredChapRowStatus,
       "ipsAuthCredChapStorageType": ipsAuthCredChapStorageType,
       "ipsAuthCredSrp": ipsAuthCredSrp,
       "ipsAuthCredSrpAttributesTable": ipsAuthCredSrpAttributesTable,
       "ipsAuthCredSrpAttributesEntry": ipsAuthCredSrpAttributesEntry,
       "ipsAuthCredSrpUserName": ipsAuthCredSrpUserName,
       "ipsAuthCredSrpRowStatus": ipsAuthCredSrpRowStatus,
       "ipsAuthCredSrpStorageType": ipsAuthCredSrpStorageType,
       "ipsAuthCredKerberos": ipsAuthCredKerberos,
       "ipsAuthCredKerbAttributesTable": ipsAuthCredKerbAttributesTable,
       "ipsAuthCredKerbAttributesEntry": ipsAuthCredKerbAttributesEntry,
       "ipsAuthCredKerbPrincipal": ipsAuthCredKerbPrincipal,
       "ipsAuthCredKerbRowStatus": ipsAuthCredKerbRowStatus,
       "ipsAuthCredKerbStorageType": ipsAuthCredKerbStorageType,
       "ipsAuthConformance": ipsAuthConformance,
       "ipsAuthCompliances": ipsAuthCompliances,
       "ipsAuthComplianceV1": ipsAuthComplianceV1,
       "ipsAuthGroups": ipsAuthGroups,
       "ipsAuthInstanceAttributesGroup": ipsAuthInstanceAttributesGroup,
       "ipsAuthIdentAttributesGroup": ipsAuthIdentAttributesGroup,
       "ipsAuthIdentNameAttributesGroup": ipsAuthIdentNameAttributesGroup,
       "ipsAuthIdentAddrAttributesGroup": ipsAuthIdentAddrAttributesGroup,
       "ipsAuthIdentCredAttributesGroup": ipsAuthIdentCredAttributesGroup,
       "ipsAuthIdentChapAttrGroup": ipsAuthIdentChapAttrGroup,
       "ipsAuthIdentSrpAttrGroup": ipsAuthIdentSrpAttrGroup,
       "ipsAuthIdentKerberosAttrGroup": ipsAuthIdentKerberosAttrGroup}
)

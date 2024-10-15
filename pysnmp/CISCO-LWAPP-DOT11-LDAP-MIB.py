# SNMP MIB module (CISCO-LWAPP-DOT11-LDAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-DOT11-LDAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:31 2024
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

(cLWlanIndex,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappDot11LdapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 614)
)
ciscoLwappDot11LdapMIB.setRevisions(
        ("2009-12-10 00:00",
         "2007-01-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CldlBindType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anonymous", 1),
          ("authenticated", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoLwappDot11LdapMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappDot11LdapMIBNotifs = _CiscoLwappDot11LdapMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 0)
)
_CiscoLwappDot11LdapMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappDot11LdapMIBObjects = _CiscoLwappDot11LdapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1)
)
_CldlConfig_ObjectIdentity = ObjectIdentity
cldlConfig = _CldlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1)
)
_CldlServerTable_Object = MibTable
cldlServerTable = _CldlServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cldlServerTable.setStatus("current")
_CldlServerEntry_Object = MibTableRow
cldlServerEntry = _CldlServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1)
)
cldlServerEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerIndex"),
)
if mibBuilder.loadTexts:
    cldlServerEntry.setStatus("current")


class _CldlServerIndex_Type(Unsigned32):
    """Custom type cldlServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CldlServerIndex_Type.__name__ = "Unsigned32"
_CldlServerIndex_Object = MibTableColumn
cldlServerIndex = _CldlServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 1),
    _CldlServerIndex_Type()
)
cldlServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldlServerIndex.setStatus("current")
_CldlServerAddressType_Type = InetAddressType
_CldlServerAddressType_Object = MibTableColumn
cldlServerAddressType = _CldlServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 2),
    _CldlServerAddressType_Type()
)
cldlServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlServerAddressType.setStatus("current")
_CldlServerAddress_Type = InetAddress
_CldlServerAddress_Object = MibTableColumn
cldlServerAddress = _CldlServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 3),
    _CldlServerAddress_Type()
)
cldlServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlServerAddress.setStatus("current")


class _CldlServerPortNum_Type(InetPortNumber):
    """Custom type cldlServerPortNum based on InetPortNumber"""
    defaultValue = 389


_CldlServerPortNum_Object = MibTableColumn
cldlServerPortNum = _CldlServerPortNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 4),
    _CldlServerPortNum_Type()
)
cldlServerPortNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlServerPortNum.setStatus("current")
_CldlServerState_Type = TruthValue
_CldlServerState_Object = MibTableColumn
cldlServerState = _CldlServerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 5),
    _CldlServerState_Type()
)
cldlServerState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlServerState.setStatus("current")


class _CldlServerTimeout_Type(Unsigned32):
    """Custom type cldlServerTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_CldlServerTimeout_Type.__name__ = "Unsigned32"
_CldlServerTimeout_Object = MibTableColumn
cldlServerTimeout = _CldlServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 6),
    _CldlServerTimeout_Type()
)
cldlServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cldlServerTimeout.setUnits("seconds")
_CldlServerUserBase_Type = DisplayString
_CldlServerUserBase_Object = MibTableColumn
cldlServerUserBase = _CldlServerUserBase_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 7),
    _CldlServerUserBase_Type()
)
cldlServerUserBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlServerUserBase.setStatus("current")
_CldlServerUserNameAttribute_Type = DisplayString
_CldlServerUserNameAttribute_Object = MibTableColumn
cldlServerUserNameAttribute = _CldlServerUserNameAttribute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 8),
    _CldlServerUserNameAttribute_Type()
)
cldlServerUserNameAttribute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlServerUserNameAttribute.setStatus("current")
_CldlServerUserName_Type = DisplayString
_CldlServerUserName_Object = MibTableColumn
cldlServerUserName = _CldlServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 9),
    _CldlServerUserName_Type()
)
cldlServerUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlServerUserName.setStatus("current")


class _CldlServerSecurityEnable_Type(TruthValue):
    """Custom type cldlServerSecurityEnable based on TruthValue"""


_CldlServerSecurityEnable_Object = MibTableColumn
cldlServerSecurityEnable = _CldlServerSecurityEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 10),
    _CldlServerSecurityEnable_Type()
)
cldlServerSecurityEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlServerSecurityEnable.setStatus("current")


class _CldlServerStorageType_Type(StorageType):
    """Custom type cldlServerStorageType based on StorageType"""


_CldlServerStorageType_Object = MibTableColumn
cldlServerStorageType = _CldlServerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 11),
    _CldlServerStorageType_Type()
)
cldlServerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlServerStorageType.setStatus("current")
_CldlServerRowStatus_Type = RowStatus
_CldlServerRowStatus_Object = MibTableColumn
cldlServerRowStatus = _CldlServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 12),
    _CldlServerRowStatus_Type()
)
cldlServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlServerRowStatus.setStatus("current")


class _CldlServerBindType_Type(CldlBindType):
    """Custom type cldlServerBindType based on CldlBindType"""


_CldlServerBindType_Object = MibTableColumn
cldlServerBindType = _CldlServerBindType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 13),
    _CldlServerBindType_Type()
)
cldlServerBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlServerBindType.setStatus("current")
_CldlServerAuthBindUserName_Type = SnmpAdminString
_CldlServerAuthBindUserName_Object = MibTableColumn
cldlServerAuthBindUserName = _CldlServerAuthBindUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 14),
    _CldlServerAuthBindUserName_Type()
)
cldlServerAuthBindUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlServerAuthBindUserName.setStatus("current")
_CldlServerAuthBindPassword_Type = SnmpAdminString
_CldlServerAuthBindPassword_Object = MibTableColumn
cldlServerAuthBindPassword = _CldlServerAuthBindPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 15),
    _CldlServerAuthBindPassword_Type()
)
cldlServerAuthBindPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldlServerAuthBindPassword.setStatus("current")
_CldlWlanLdapTable_Object = MibTable
cldlWlanLdapTable = _CldlWlanLdapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cldlWlanLdapTable.setStatus("current")
_CldlWlanLdapEntry_Object = MibTableRow
cldlWlanLdapEntry = _CldlWlanLdapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 2, 1)
)
cldlWlanLdapEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cldlWlanLdapEntry.setStatus("current")


class _CldlWlanLdapPrimaryServerIndex_Type(Unsigned32):
    """Custom type cldlWlanLdapPrimaryServerIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CldlWlanLdapPrimaryServerIndex_Type.__name__ = "Unsigned32"
_CldlWlanLdapPrimaryServerIndex_Object = MibTableColumn
cldlWlanLdapPrimaryServerIndex = _CldlWlanLdapPrimaryServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 2, 1, 1),
    _CldlWlanLdapPrimaryServerIndex_Type()
)
cldlWlanLdapPrimaryServerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldlWlanLdapPrimaryServerIndex.setStatus("current")


class _CldlWlanLdapSecondaryServerIndex_Type(Unsigned32):
    """Custom type cldlWlanLdapSecondaryServerIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CldlWlanLdapSecondaryServerIndex_Type.__name__ = "Unsigned32"
_CldlWlanLdapSecondaryServerIndex_Object = MibTableColumn
cldlWlanLdapSecondaryServerIndex = _CldlWlanLdapSecondaryServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 2, 1, 2),
    _CldlWlanLdapSecondaryServerIndex_Type()
)
cldlWlanLdapSecondaryServerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldlWlanLdapSecondaryServerIndex.setStatus("current")


class _CldlWlanLdapTertiaryServerIndex_Type(Unsigned32):
    """Custom type cldlWlanLdapTertiaryServerIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CldlWlanLdapTertiaryServerIndex_Type.__name__ = "Unsigned32"
_CldlWlanLdapTertiaryServerIndex_Object = MibTableColumn
cldlWlanLdapTertiaryServerIndex = _CldlWlanLdapTertiaryServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 2, 1, 3),
    _CldlWlanLdapTertiaryServerIndex_Type()
)
cldlWlanLdapTertiaryServerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldlWlanLdapTertiaryServerIndex.setStatus("current")
_CldlStatus_ObjectIdentity = ObjectIdentity
cldlStatus = _CldlStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 2)
)
_CiscoLwappDot11LdapMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappDot11LdapMIBConform = _CiscoLwappDot11LdapMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 2)
)
_CiscoLwappDot11LdapMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappDot11LdapMIBCompliances = _CiscoLwappDot11LdapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 2, 1)
)
_CiscoLwappDot11LdapMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappDot11LdapMIBGroups = _CiscoLwappDot11LdapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 2, 2)
)

# Managed Objects groups

ciscoLwappDot11LdapMIBConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 2, 2, 1)
)
ciscoLwappDot11LdapMIBConfigGroup.setObjects(
      *(("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerAddressType"),
        ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerAddress"),
        ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerPortNum"),
        ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerState"),
        ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerTimeout"),
        ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerUserBase"),
        ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerUserNameAttribute"),
        ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerUserName"),
        ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerSecurityEnable"),
        ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerRowStatus"),
        ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerStorageType"),
        ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlWlanLdapPrimaryServerIndex"),
        ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlWlanLdapSecondaryServerIndex"),
        ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlWlanLdapTertiaryServerIndex"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11LdapMIBConfigGroup.setStatus("current")

ciscoLwappDot11LdapMIBConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 2, 2, 2)
)
ciscoLwappDot11LdapMIBConfigGroupSup1.setObjects(
      *(("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerBindType"),
        ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerAuthBindUserName"),
        ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerAuthBindPassword"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11LdapMIBConfigGroupSup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappDot11LdapMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappDot11LdapMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappDot11LdapMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 614, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappDot11LdapMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-DOT11-LDAP-MIB",
    **{"CldlBindType": CldlBindType,
       "ciscoLwappDot11LdapMIB": ciscoLwappDot11LdapMIB,
       "ciscoLwappDot11LdapMIBNotifs": ciscoLwappDot11LdapMIBNotifs,
       "ciscoLwappDot11LdapMIBObjects": ciscoLwappDot11LdapMIBObjects,
       "cldlConfig": cldlConfig,
       "cldlServerTable": cldlServerTable,
       "cldlServerEntry": cldlServerEntry,
       "cldlServerIndex": cldlServerIndex,
       "cldlServerAddressType": cldlServerAddressType,
       "cldlServerAddress": cldlServerAddress,
       "cldlServerPortNum": cldlServerPortNum,
       "cldlServerState": cldlServerState,
       "cldlServerTimeout": cldlServerTimeout,
       "cldlServerUserBase": cldlServerUserBase,
       "cldlServerUserNameAttribute": cldlServerUserNameAttribute,
       "cldlServerUserName": cldlServerUserName,
       "cldlServerSecurityEnable": cldlServerSecurityEnable,
       "cldlServerStorageType": cldlServerStorageType,
       "cldlServerRowStatus": cldlServerRowStatus,
       "cldlServerBindType": cldlServerBindType,
       "cldlServerAuthBindUserName": cldlServerAuthBindUserName,
       "cldlServerAuthBindPassword": cldlServerAuthBindPassword,
       "cldlWlanLdapTable": cldlWlanLdapTable,
       "cldlWlanLdapEntry": cldlWlanLdapEntry,
       "cldlWlanLdapPrimaryServerIndex": cldlWlanLdapPrimaryServerIndex,
       "cldlWlanLdapSecondaryServerIndex": cldlWlanLdapSecondaryServerIndex,
       "cldlWlanLdapTertiaryServerIndex": cldlWlanLdapTertiaryServerIndex,
       "cldlStatus": cldlStatus,
       "ciscoLwappDot11LdapMIBConform": ciscoLwappDot11LdapMIBConform,
       "ciscoLwappDot11LdapMIBCompliances": ciscoLwappDot11LdapMIBCompliances,
       "ciscoLwappDot11LdapMIBCompliance": ciscoLwappDot11LdapMIBCompliance,
       "ciscoLwappDot11LdapMIBComplianceRev1": ciscoLwappDot11LdapMIBComplianceRev1,
       "ciscoLwappDot11LdapMIBGroups": ciscoLwappDot11LdapMIBGroups,
       "ciscoLwappDot11LdapMIBConfigGroup": ciscoLwappDot11LdapMIBConfigGroup,
       "ciscoLwappDot11LdapMIBConfigGroupSup1": ciscoLwappDot11LdapMIBConfigGroupSup1}
)

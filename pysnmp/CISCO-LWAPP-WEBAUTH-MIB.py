# SNMP MIB module (CISCO-LWAPP-WEBAUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-WEBAUTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:08 2024
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

(CiscoURLString,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappWebAuthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515)
)
ciscoLwappWebAuthMIB.setRevisions(
        ("2007-03-04 00:00",
         "2006-04-05 11:50")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappWebAuthMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappWebAuthMIBNotifs = _CiscoLwappWebAuthMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 0)
)
_CiscoLwappWebAuthMIBNotifObjs_ObjectIdentity = ObjectIdentity
ciscoLwappWebAuthMIBNotifObjs = _CiscoLwappWebAuthMIBNotifObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 1)
)


class _CLWAGuestUserName_Type(OctetString):
    """Custom type cLWAGuestUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_CLWAGuestUserName_Type.__name__ = "OctetString"
_CLWAGuestUserName_Object = MibScalar
cLWAGuestUserName = _CLWAGuestUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 1, 1),
    _CLWAGuestUserName_Type()
)
cLWAGuestUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLWAGuestUserName.setStatus("current")
_CiscoLwappWebAuthMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappWebAuthMIBObjects = _CiscoLwappWebAuthMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2)
)
_CiscoLwappWebAuthConfig_ObjectIdentity = ObjectIdentity
ciscoLwappWebAuthConfig = _CiscoLwappWebAuthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1)
)


class _CLWAWebAuthType_Type(Integer32):
    """Custom type cLWAWebAuthType based on Integer32"""
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
        *(("external", 3),
          ("internalCustom", 2),
          ("internalDefault", 1))
    )


_CLWAWebAuthType_Type.__name__ = "Integer32"
_CLWAWebAuthType_Object = MibScalar
cLWAWebAuthType = _CLWAWebAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 1),
    _CLWAWebAuthType_Type()
)
cLWAWebAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWAWebAuthType.setStatus("current")


class _CLWAManufacturerLogo_Type(TruthValue):
    """Custom type cLWAManufacturerLogo based on TruthValue"""


_CLWAManufacturerLogo_Object = MibScalar
cLWAManufacturerLogo = _CLWAManufacturerLogo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 2),
    _CLWAManufacturerLogo_Type()
)
cLWAManufacturerLogo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWAManufacturerLogo.setStatus("current")
_CLWACustomLogoFileName_Type = SnmpAdminString
_CLWACustomLogoFileName_Object = MibScalar
cLWACustomLogoFileName = _CLWACustomLogoFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 3),
    _CLWACustomLogoFileName_Type()
)
cLWACustomLogoFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWACustomLogoFileName.setStatus("current")


class _CLWACustomWebTitle_Type(SnmpAdminString):
    """Custom type cLWACustomWebTitle based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CLWACustomWebTitle_Type.__name__ = "SnmpAdminString"
_CLWACustomWebTitle_Object = MibScalar
cLWACustomWebTitle = _CLWACustomWebTitle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 4),
    _CLWACustomWebTitle_Type()
)
cLWACustomWebTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWACustomWebTitle.setStatus("current")
_CLWACustomWebMessage_Type = SnmpAdminString
_CLWACustomWebMessage_Object = MibScalar
cLWACustomWebMessage = _CLWACustomWebMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 5),
    _CLWACustomWebMessage_Type()
)
cLWACustomWebMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWACustomWebMessage.setStatus("current")
_CLWACustomWebRedirectURL_Type = CiscoURLString
_CLWACustomWebRedirectURL_Object = MibScalar
cLWACustomWebRedirectURL = _CLWACustomWebRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 6),
    _CLWACustomWebRedirectURL_Type()
)
cLWACustomWebRedirectURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWACustomWebRedirectURL.setStatus("current")
_CLWAExternalWebAuthURL_Type = CiscoURLString
_CLWAExternalWebAuthURL_Object = MibScalar
cLWAExternalWebAuthURL = _CLWAExternalWebAuthURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 1, 7),
    _CLWAExternalWebAuthURL_Type()
)
cLWAExternalWebAuthURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWAExternalWebAuthURL.setStatus("current")
_CiscoLwappWebAuthExtConfig_ObjectIdentity = ObjectIdentity
ciscoLwappWebAuthExtConfig = _CiscoLwappWebAuthExtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2)
)
_CLWAExternalWebServerTable_Object = MibTable
cLWAExternalWebServerTable = _CLWAExternalWebServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cLWAExternalWebServerTable.setStatus("current")
_CLWAExternalWebServerEntry_Object = MibTableRow
cLWAExternalWebServerEntry = _CLWAExternalWebServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2, 1, 1)
)
cLWAExternalWebServerEntry.setIndexNames(
    (0, "CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebServerIndex"),
)
if mibBuilder.loadTexts:
    cLWAExternalWebServerEntry.setStatus("current")


class _CLWAExternalWebServerIndex_Type(Unsigned32):
    """Custom type cLWAExternalWebServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CLWAExternalWebServerIndex_Type.__name__ = "Unsigned32"
_CLWAExternalWebServerIndex_Object = MibTableColumn
cLWAExternalWebServerIndex = _CLWAExternalWebServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2, 1, 1, 1),
    _CLWAExternalWebServerIndex_Type()
)
cLWAExternalWebServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWAExternalWebServerIndex.setStatus("current")
_CLWAExternalWebServerAddrType_Type = InetAddressType
_CLWAExternalWebServerAddrType_Object = MibTableColumn
cLWAExternalWebServerAddrType = _CLWAExternalWebServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2, 1, 1, 2),
    _CLWAExternalWebServerAddrType_Type()
)
cLWAExternalWebServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWAExternalWebServerAddrType.setStatus("current")
_CLWAExternalWebServerAddr_Type = InetAddress
_CLWAExternalWebServerAddr_Object = MibTableColumn
cLWAExternalWebServerAddr = _CLWAExternalWebServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2, 1, 1, 3),
    _CLWAExternalWebServerAddr_Type()
)
cLWAExternalWebServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWAExternalWebServerAddr.setStatus("current")
_CLWAExternalWebServerRowStatus_Type = RowStatus
_CLWAExternalWebServerRowStatus_Object = MibTableColumn
cLWAExternalWebServerRowStatus = _CLWAExternalWebServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 2, 1, 1, 4),
    _CLWAExternalWebServerRowStatus_Type()
)
cLWAExternalWebServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWAExternalWebServerRowStatus.setStatus("current")
_CiscoLwappLocalNetUserConfig_ObjectIdentity = ObjectIdentity
ciscoLwappLocalNetUserConfig = _CiscoLwappLocalNetUserConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3)
)
_CLWALocalNetUserTable_Object = MibTable
cLWALocalNetUserTable = _CLWALocalNetUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cLWALocalNetUserTable.setStatus("current")
_CLWALocalNetUserEntry_Object = MibTableRow
cLWALocalNetUserEntry = _CLWALocalNetUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 1, 1)
)
cLWALocalNetUserEntry.setIndexNames(
    (0, "CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserName"),
)
if mibBuilder.loadTexts:
    cLWALocalNetUserEntry.setStatus("current")


class _CLWALocalNetUserName_Type(SnmpAdminString):
    """Custom type cLWALocalNetUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CLWALocalNetUserName_Type.__name__ = "SnmpAdminString"
_CLWALocalNetUserName_Object = MibTableColumn
cLWALocalNetUserName = _CLWALocalNetUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 1, 1, 1),
    _CLWALocalNetUserName_Type()
)
cLWALocalNetUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWALocalNetUserName.setStatus("current")
_CLWALocalNetUserIsGuest_Type = TruthValue
_CLWALocalNetUserIsGuest_Object = MibTableColumn
cLWALocalNetUserIsGuest = _CLWALocalNetUserIsGuest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 2, 3, 1, 1, 2),
    _CLWALocalNetUserIsGuest_Type()
)
cLWALocalNetUserIsGuest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWALocalNetUserIsGuest.setStatus("current")
_CiscoLwappWebAuthMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappWebAuthMIBConform = _CiscoLwappWebAuthMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3)
)
_CiscoLwappWebAuthMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappWebAuthMIBCompliances = _CiscoLwappWebAuthMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 1)
)
_CiscoLwappWebAuthMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappWebAuthMIBGroups = _CiscoLwappWebAuthMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2)
)

# Managed Objects groups

cLWACustomWebAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 1)
)
cLWACustomWebAuthGroup.setObjects(
      *(("CISCO-LWAPP-WEBAUTH-MIB", "cLWAWebAuthType"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAManufacturerLogo"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomLogoFileName"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomWebTitle"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomWebMessage"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWACustomWebRedirectURL"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebAuthURL"))
)
if mibBuilder.loadTexts:
    cLWACustomWebAuthGroup.setStatus("current")

cLWAExternalWebAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 2)
)
cLWAExternalWebAuthGroup.setObjects(
      *(("CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebServerAddrType"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebServerAddr"),
        ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAExternalWebServerRowStatus"))
)
if mibBuilder.loadTexts:
    cLWAExternalWebAuthGroup.setStatus("current")

cLWAGuestAccessNotifObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 3)
)
cLWAGuestAccessNotifObjGroup.setObjects(
    ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserName")
)
if mibBuilder.loadTexts:
    cLWAGuestAccessNotifObjGroup.setStatus("current")

cLWAGuestUserConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 5)
)
cLWAGuestUserConfigGroup.setObjects(
    ("CISCO-LWAPP-WEBAUTH-MIB", "cLWALocalNetUserIsGuest")
)
if mibBuilder.loadTexts:
    cLWAGuestUserConfigGroup.setStatus("current")


# Notification objects

cLWAGuestUserRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 0, 1)
)
cLWAGuestUserRemoved.setObjects(
    ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserName")
)
if mibBuilder.loadTexts:
    cLWAGuestUserRemoved.setStatus(
        "current"
    )


# Notifications groups

cLWAGuestAccessNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 2, 4)
)
cLWAGuestAccessNotifGroup.setObjects(
    ("CISCO-LWAPP-WEBAUTH-MIB", "cLWAGuestUserRemoved")
)
if mibBuilder.loadTexts:
    cLWAGuestAccessNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cLWebAuthMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cLWebAuthMIBCompliance.setStatus(
        "deprecated"
    )

cLWebAuthMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 515, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cLWebAuthMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-WEBAUTH-MIB",
    **{"ciscoLwappWebAuthMIB": ciscoLwappWebAuthMIB,
       "ciscoLwappWebAuthMIBNotifs": ciscoLwappWebAuthMIBNotifs,
       "cLWAGuestUserRemoved": cLWAGuestUserRemoved,
       "ciscoLwappWebAuthMIBNotifObjs": ciscoLwappWebAuthMIBNotifObjs,
       "cLWAGuestUserName": cLWAGuestUserName,
       "ciscoLwappWebAuthMIBObjects": ciscoLwappWebAuthMIBObjects,
       "ciscoLwappWebAuthConfig": ciscoLwappWebAuthConfig,
       "cLWAWebAuthType": cLWAWebAuthType,
       "cLWAManufacturerLogo": cLWAManufacturerLogo,
       "cLWACustomLogoFileName": cLWACustomLogoFileName,
       "cLWACustomWebTitle": cLWACustomWebTitle,
       "cLWACustomWebMessage": cLWACustomWebMessage,
       "cLWACustomWebRedirectURL": cLWACustomWebRedirectURL,
       "cLWAExternalWebAuthURL": cLWAExternalWebAuthURL,
       "ciscoLwappWebAuthExtConfig": ciscoLwappWebAuthExtConfig,
       "cLWAExternalWebServerTable": cLWAExternalWebServerTable,
       "cLWAExternalWebServerEntry": cLWAExternalWebServerEntry,
       "cLWAExternalWebServerIndex": cLWAExternalWebServerIndex,
       "cLWAExternalWebServerAddrType": cLWAExternalWebServerAddrType,
       "cLWAExternalWebServerAddr": cLWAExternalWebServerAddr,
       "cLWAExternalWebServerRowStatus": cLWAExternalWebServerRowStatus,
       "ciscoLwappLocalNetUserConfig": ciscoLwappLocalNetUserConfig,
       "cLWALocalNetUserTable": cLWALocalNetUserTable,
       "cLWALocalNetUserEntry": cLWALocalNetUserEntry,
       "cLWALocalNetUserName": cLWALocalNetUserName,
       "cLWALocalNetUserIsGuest": cLWALocalNetUserIsGuest,
       "ciscoLwappWebAuthMIBConform": ciscoLwappWebAuthMIBConform,
       "ciscoLwappWebAuthMIBCompliances": ciscoLwappWebAuthMIBCompliances,
       "cLWebAuthMIBCompliance": cLWebAuthMIBCompliance,
       "cLWebAuthMIBComplianceRev1": cLWebAuthMIBComplianceRev1,
       "ciscoLwappWebAuthMIBGroups": ciscoLwappWebAuthMIBGroups,
       "cLWACustomWebAuthGroup": cLWACustomWebAuthGroup,
       "cLWAExternalWebAuthGroup": cLWAExternalWebAuthGroup,
       "cLWAGuestAccessNotifObjGroup": cLWAGuestAccessNotifObjGroup,
       "cLWAGuestAccessNotifGroup": cLWAGuestAccessNotifGroup,
       "cLWAGuestUserConfigGroup": cLWAGuestUserConfigGroup}
)

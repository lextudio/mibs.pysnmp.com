# SNMP MIB module (ADTRAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:03 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adtran = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdProducts_ObjectIdentity = ObjectIdentity
adProducts = _AdProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1)
)
_AdMgmt_ObjectIdentity = ObjectIdentity
adMgmt = _AdMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2)
)
_AdAdmin_ObjectIdentity = ObjectIdentity
adAdmin = _AdAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 3)
)
_AdProductInfo_ObjectIdentity = ObjectIdentity
adProductInfo = _AdProductInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 3, 1)
)
_AdProdName_Type = DisplayString
_AdProdName_Object = MibScalar
adProdName = _AdProdName_Object(
    (1, 3, 6, 1, 4, 1, 664, 3, 1, 1),
    _AdProdName_Type()
)
adProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adProdName.setStatus("current")
_AdProdPartNumber_Type = DisplayString
_AdProdPartNumber_Object = MibScalar
adProdPartNumber = _AdProdPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 3, 1, 2),
    _AdProdPartNumber_Type()
)
adProdPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adProdPartNumber.setStatus("current")
_AdProdCLEIcode_Type = DisplayString
_AdProdCLEIcode_Object = MibScalar
adProdCLEIcode = _AdProdCLEIcode_Object(
    (1, 3, 6, 1, 4, 1, 664, 3, 1, 3),
    _AdProdCLEIcode_Type()
)
adProdCLEIcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adProdCLEIcode.setStatus("current")
_AdProdSerialNumber_Type = DisplayString
_AdProdSerialNumber_Object = MibScalar
adProdSerialNumber = _AdProdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 3, 1, 4),
    _AdProdSerialNumber_Type()
)
adProdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adProdSerialNumber.setStatus("current")
_AdProdRevision_Type = DisplayString
_AdProdRevision_Object = MibScalar
adProdRevision = _AdProdRevision_Object(
    (1, 3, 6, 1, 4, 1, 664, 3, 1, 5),
    _AdProdRevision_Type()
)
adProdRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adProdRevision.setStatus("current")
_AdProdSwVersion_Type = DisplayString
_AdProdSwVersion_Object = MibScalar
adProdSwVersion = _AdProdSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 3, 1, 6),
    _AdProdSwVersion_Type()
)
adProdSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adProdSwVersion.setStatus("current")
_AdProdPhysAddress_Type = PhysAddress
_AdProdPhysAddress_Object = MibScalar
adProdPhysAddress = _AdProdPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 3, 1, 7),
    _AdProdPhysAddress_Type()
)
adProdPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adProdPhysAddress.setStatus("current")
_AdProdProductID_Type = ObjectIdentifier
_AdProdProductID_Object = MibScalar
adProdProductID = _AdProdProductID_Object(
    (1, 3, 6, 1, 4, 1, 664, 3, 1, 8),
    _AdProdProductID_Type()
)
adProdProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adProdProductID.setStatus("current")
_AdProdTransType_Type = DisplayString
_AdProdTransType_Object = MibScalar
adProdTransType = _AdProdTransType_Object(
    (1, 3, 6, 1, 4, 1, 664, 3, 1, 9),
    _AdProdTransType_Type()
)
adProdTransType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adProdTransType.setStatus("current")
_AdPerform_ObjectIdentity = ObjectIdentity
adPerform = _AdPerform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 4)
)
_AdShared_ObjectIdentity = ObjectIdentity
adShared = _AdShared_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5)
)
_AdIdentity_ObjectIdentity = ObjectIdentity
adIdentity = _AdIdentity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6)
)
_AdIdentityShared_ObjectIdentity = ObjectIdentity
adIdentityShared = _AdIdentityShared_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000)
)
_AdAgentCapModule_ObjectIdentity = ObjectIdentity
adAgentCapModule = _AdAgentCapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 7)
)
_AdAgentCapProduct_ObjectIdentity = ObjectIdentity
adAgentCapProduct = _AdAgentCapProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 7, 1)
)
_AdAgentCapShared_ObjectIdentity = ObjectIdentity
adAgentCapShared = _AdAgentCapShared_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 7, 2)
)
_AdConformance_ObjectIdentity = ObjectIdentity
adConformance = _AdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 99)
)
_AdCompliances_ObjectIdentity = ObjectIdentity
adCompliances = _AdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 99, 1)
)
_AdMIBGroups_ObjectIdentity = ObjectIdentity
adMIBGroups = _AdMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 99, 2)
)
_AdComplianceShared_ObjectIdentity = ObjectIdentity
adComplianceShared = _AdComplianceShared_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 99, 10000)
)

# Managed Objects groups

adBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 99, 2, 1)
)
adBaseGroup.setObjects(
      *(("ADTRAN-MIB", "adProdName"),
        ("ADTRAN-MIB", "adProdPartNumber"),
        ("ADTRAN-MIB", "adProdCLEIcode"),
        ("ADTRAN-MIB", "adProdSerialNumber"),
        ("ADTRAN-MIB", "adProdRevision"),
        ("ADTRAN-MIB", "adProdSwVersion"),
        ("ADTRAN-MIB", "adProdPhysAddress"),
        ("ADTRAN-MIB", "adProdProductID"))
)
if mibBuilder.loadTexts:
    adBaseGroup.setStatus("current")

adCNDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 99, 2, 2)
)
adCNDGroup.setObjects(
    ("ADTRAN-MIB", "adProdTransType")
)
if mibBuilder.loadTexts:
    adCNDGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 99, 1, 1)
)
if mibBuilder.loadTexts:
    adCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-MIB",
    **{"adtran": adtran,
       "adProducts": adProducts,
       "adMgmt": adMgmt,
       "adAdmin": adAdmin,
       "adProductInfo": adProductInfo,
       "adProdName": adProdName,
       "adProdPartNumber": adProdPartNumber,
       "adProdCLEIcode": adProdCLEIcode,
       "adProdSerialNumber": adProdSerialNumber,
       "adProdRevision": adProdRevision,
       "adProdSwVersion": adProdSwVersion,
       "adProdPhysAddress": adProdPhysAddress,
       "adProdProductID": adProdProductID,
       "adProdTransType": adProdTransType,
       "adPerform": adPerform,
       "adShared": adShared,
       "adIdentity": adIdentity,
       "adIdentityShared": adIdentityShared,
       "adAgentCapModule": adAgentCapModule,
       "adAgentCapProduct": adAgentCapProduct,
       "adAgentCapShared": adAgentCapShared,
       "adConformance": adConformance,
       "adCompliances": adCompliances,
       "adCompliance": adCompliance,
       "adMIBGroups": adMIBGroups,
       "adBaseGroup": adBaseGroup,
       "adCNDGroup": adCNDGroup,
       "adComplianceShared": adComplianceShared}
)

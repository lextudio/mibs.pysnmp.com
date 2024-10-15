# SNMP MIB module (NETFINITYSERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETFINITYSERVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:45 2024
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiDisplaystring(OctetString):
    """Custom type DmiDisplaystring based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(100, 100),
    )





class DmiDate(OctetString):
    """Custom type DmiDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(28, 28),
    )





class DmiComponentIndex(Integer32):
    """Custom type DmiComponentIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_NetFinity_ObjectIdentity = ObjectIdentity
netFinity = _NetFinity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 71)
)
_DmiMibs_ObjectIdentity = ObjectIdentity
dmiMibs = _DmiMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200)
)
_NetFinityServicesMIB_ObjectIdentity = ObjectIdentity
netFinityServicesMIB = _NetFinityServicesMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2)
)
_DmtfGroups3_ObjectIdentity = ObjectIdentity
dmtfGroups3 = _DmtfGroups3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1)
)
_TComponentid3_Object = MibTable
tComponentid3 = _TComponentid3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid3.setStatus("mandatory")
_EComponentid3_Object = MibTableRow
eComponentid3 = _EComponentid3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 1, 1)
)
eComponentid3.setIndexNames(
    (0, "NETFINITYSERVICES-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid3.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_TNetfinityAlert_Object = MibTable
tNetfinityAlert = _TNetfinityAlert_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tNetfinityAlert.setStatus("mandatory")
_ENetfinityAlert_Object = MibTableRow
eNetfinityAlert = _ENetfinityAlert_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 2, 1)
)
eNetfinityAlert.setIndexNames(
    (0, "NETFINITYSERVICES-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eNetfinityAlert.setStatus("mandatory")
_A2AlertText_Type = DmiDisplaystring
_A2AlertText_Object = MibTableColumn
a2AlertText = _A2AlertText_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 2, 1, 1),
    _A2AlertText_Type()
)
a2AlertText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2AlertText.setStatus("mandatory")
_A2Severity_Type = DmiInteger
_A2Severity_Object = MibTableColumn
a2Severity = _A2Severity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 2, 1, 2),
    _A2Severity_Type()
)
a2Severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Severity.setStatus("mandatory")
_A2AlertType_Type = DmiDisplaystring
_A2AlertType_Object = MibTableColumn
a2AlertType = _A2AlertType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 2, 1, 3),
    _A2AlertType_Type()
)
a2AlertType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2AlertType.setStatus("mandatory")
_A2ApplicationId_Type = DmiDisplaystring
_A2ApplicationId_Object = MibTableColumn
a2ApplicationId = _A2ApplicationId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 2, 1, 4),
    _A2ApplicationId_Type()
)
a2ApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2ApplicationId.setStatus("mandatory")
_A2ApplicationAlertType_Type = DmiInteger
_A2ApplicationAlertType_Object = MibTableColumn
a2ApplicationAlertType = _A2ApplicationAlertType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 2, 1, 5),
    _A2ApplicationAlertType_Type()
)
a2ApplicationAlertType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2ApplicationAlertType.setStatus("mandatory")
_A2AlertTimeAndDate_Type = DmiDate
_A2AlertTimeAndDate_Object = MibTableColumn
a2AlertTimeAndDate = _A2AlertTimeAndDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 2, 1, 6),
    _A2AlertTimeAndDate_Type()
)
a2AlertTimeAndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2AlertTimeAndDate.setStatus("mandatory")
_A2AlertSender_Type = DmiDisplaystring
_A2AlertSender_Object = MibTableColumn
a2AlertSender = _A2AlertSender_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 2, 1, 7),
    _A2AlertSender_Type()
)
a2AlertSender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2AlertSender.setStatus("mandatory")
_A2AlertSystemName_Type = DmiDisplaystring
_A2AlertSystemName_Object = MibTableColumn
a2AlertSystemName = _A2AlertSystemName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 2, 1, 8),
    _A2AlertSystemName_Type()
)
a2AlertSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2AlertSystemName.setStatus("mandatory")
_TNetfinityMonitorAttributes_Object = MibTable
tNetfinityMonitorAttributes = _TNetfinityMonitorAttributes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tNetfinityMonitorAttributes.setStatus("mandatory")
_ENetfinityMonitorAttributes_Object = MibTableRow
eNetfinityMonitorAttributes = _ENetfinityMonitorAttributes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 3, 1)
)
eNetfinityMonitorAttributes.setIndexNames(
    (0, "NETFINITYSERVICES-MIB", "DmiComponentIndex"),
    (0, "NETFINITYSERVICES-MIB", "a3AttributeId"),
)
if mibBuilder.loadTexts:
    eNetfinityMonitorAttributes.setStatus("mandatory")
_A3AttributeId_Type = DmiInteger
_A3AttributeId_Object = MibTableColumn
a3AttributeId = _A3AttributeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 3, 1, 1),
    _A3AttributeId_Type()
)
a3AttributeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3AttributeId.setStatus("mandatory")
_A3AttributeName_Type = DmiDisplaystring
_A3AttributeName_Object = MibTableColumn
a3AttributeName = _A3AttributeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 3, 1, 2),
    _A3AttributeName_Type()
)
a3AttributeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3AttributeName.setStatus("mandatory")
_A3CurrentValueInteger_Type = DmiInteger
_A3CurrentValueInteger_Object = MibTableColumn
a3CurrentValueInteger = _A3CurrentValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 3, 1, 3),
    _A3CurrentValueInteger_Type()
)
a3CurrentValueInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3CurrentValueInteger.setStatus("mandatory")
_A3NetfinityValueGroup_Object = MibTable
a3NetfinityValueGroup = _A3NetfinityValueGroup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    a3NetfinityValueGroup.setStatus("mandatory")
_A3CurrentValueThousandths_Type = DmiInteger
_A3CurrentValueThousandths_Object = MibTableColumn
a3CurrentValueThousandths = _A3CurrentValueThousandths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 3, 1, 4),
    _A3CurrentValueThousandths_Type()
)
a3CurrentValueThousandths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3CurrentValueThousandths.setStatus("mandatory")
_A3CurrentValueString_Type = DmiDisplaystring
_A3CurrentValueString_Object = MibTableColumn
a3CurrentValueString = _A3CurrentValueString_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 3, 1, 5),
    _A3CurrentValueString_Type()
)
a3CurrentValueString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3CurrentValueString.setStatus("mandatory")
_A3ValueUnits_Type = DmiDisplaystring
_A3ValueUnits_Object = MibTableColumn
a3ValueUnits = _A3ValueUnits_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 3, 1, 6),
    _A3ValueUnits_Type()
)
a3ValueUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ValueUnits.setStatus("mandatory")
_TNetfinityAttributeGroups_Object = MibTable
tNetfinityAttributeGroups = _TNetfinityAttributeGroups_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tNetfinityAttributeGroups.setStatus("mandatory")
_ENetfinityAttributeGroups_Object = MibTableRow
eNetfinityAttributeGroups = _ENetfinityAttributeGroups_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 4, 1)
)
eNetfinityAttributeGroups.setIndexNames(
    (0, "NETFINITYSERVICES-MIB", "DmiComponentIndex"),
    (0, "NETFINITYSERVICES-MIB", "a4AttributeGroupId"),
    (0, "NETFINITYSERVICES-MIB", "a4AttributeId"),
)
if mibBuilder.loadTexts:
    eNetfinityAttributeGroups.setStatus("mandatory")
_A4AttributeGroupId_Type = DmiInteger
_A4AttributeGroupId_Object = MibTableColumn
a4AttributeGroupId = _A4AttributeGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 4, 1, 1),
    _A4AttributeGroupId_Type()
)
a4AttributeGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4AttributeGroupId.setStatus("mandatory")
_A4AttributeId_Type = DmiInteger
_A4AttributeId_Object = MibTableColumn
a4AttributeId = _A4AttributeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 4, 1, 2),
    _A4AttributeId_Type()
)
a4AttributeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4AttributeId.setStatus("mandatory")
_A4AttributeGroupName_Type = DmiDisplaystring
_A4AttributeGroupName_Object = MibTableColumn
a4AttributeGroupName = _A4AttributeGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 4, 1, 3),
    _A4AttributeGroupName_Type()
)
a4AttributeGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4AttributeGroupName.setStatus("mandatory")
_A4AttributeName_Type = DmiDisplaystring
_A4AttributeName_Object = MibTableColumn
a4AttributeName = _A4AttributeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 4, 1, 4),
    _A4AttributeName_Type()
)
a4AttributeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4AttributeName.setStatus("mandatory")
_A4CurrentValueTextual_Type = DmiDisplaystring
_A4CurrentValueTextual_Object = MibTableColumn
a4CurrentValueTextual = _A4CurrentValueTextual_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 4, 1, 5),
    _A4CurrentValueTextual_Type()
)
a4CurrentValueTextual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4CurrentValueTextual.setStatus("mandatory")
_A4CurrentValueIndex_Type = DmiInteger
_A4CurrentValueIndex_Object = MibTableColumn
a4CurrentValueIndex = _A4CurrentValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 2, 1, 4, 1, 6),
    _A4CurrentValueIndex_Type()
)
a4CurrentValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4CurrentValueIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETFINITYSERVICES-MIB",
    **{"DmiInteger": DmiInteger,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDate": DmiDate,
       "DmiComponentIndex": DmiComponentIndex,
       "ibm": ibm,
       "ibmProd": ibmProd,
       "netFinity": netFinity,
       "dmiMibs": dmiMibs,
       "netFinityServicesMIB": netFinityServicesMIB,
       "dmtfGroups3": dmtfGroups3,
       "tComponentid3": tComponentid3,
       "eComponentid3": eComponentid3,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "tNetfinityAlert": tNetfinityAlert,
       "eNetfinityAlert": eNetfinityAlert,
       "a2AlertText": a2AlertText,
       "a2Severity": a2Severity,
       "a2AlertType": a2AlertType,
       "a2ApplicationId": a2ApplicationId,
       "a2ApplicationAlertType": a2ApplicationAlertType,
       "a2AlertTimeAndDate": a2AlertTimeAndDate,
       "a2AlertSender": a2AlertSender,
       "a2AlertSystemName": a2AlertSystemName,
       "tNetfinityMonitorAttributes": tNetfinityMonitorAttributes,
       "eNetfinityMonitorAttributes": eNetfinityMonitorAttributes,
       "a3AttributeId": a3AttributeId,
       "a3AttributeName": a3AttributeName,
       "a3CurrentValueInteger": a3CurrentValueInteger,
       "a3NetfinityValueGroup": a3NetfinityValueGroup,
       "a3CurrentValueThousandths": a3CurrentValueThousandths,
       "a3CurrentValueString": a3CurrentValueString,
       "a3ValueUnits": a3ValueUnits,
       "tNetfinityAttributeGroups": tNetfinityAttributeGroups,
       "eNetfinityAttributeGroups": eNetfinityAttributeGroups,
       "a4AttributeGroupId": a4AttributeGroupId,
       "a4AttributeId": a4AttributeId,
       "a4AttributeGroupName": a4AttributeGroupName,
       "a4AttributeName": a4AttributeName,
       "a4CurrentValueTextual": a4CurrentValueTextual,
       "a4CurrentValueIndex": a4CurrentValueIndex}
)

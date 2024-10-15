# SNMP MIB module (CISCO-SSM-PROV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SSM-PROV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:50 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

ciscoSsmProvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 448)
)
ciscoSsmProvMIB.setRevisions(
        ("2005-02-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSsmProvMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSsmProvMIBObjects = _CiscoSsmProvMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1)
)
_SsmProvConfiguration_ObjectIdentity = ObjectIdentity
ssmProvConfiguration = _SsmProvConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1)
)
_SsmProvFeatureTable_Object = MibTable
ssmProvFeatureTable = _SsmProvFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ssmProvFeatureTable.setStatus("current")
_SsmProvFeatureEntry_Object = MibTableRow
ssmProvFeatureEntry = _SsmProvFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 1, 1)
)
ssmProvFeatureEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SSM-PROV-MIB", "ssmProvFeatureName"),
)
if mibBuilder.loadTexts:
    ssmProvFeatureEntry.setStatus("current")


class _SsmProvFeatureName_Type(SnmpAdminString):
    """Custom type ssmProvFeatureName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_SsmProvFeatureName_Type.__name__ = "SnmpAdminString"
_SsmProvFeatureName_Object = MibTableColumn
ssmProvFeatureName = _SsmProvFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 1, 1, 1),
    _SsmProvFeatureName_Type()
)
ssmProvFeatureName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssmProvFeatureName.setStatus("current")
_SsmProvFeatureNeedsImage_Type = TruthValue
_SsmProvFeatureNeedsImage_Object = MibTableColumn
ssmProvFeatureNeedsImage = _SsmProvFeatureNeedsImage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 1, 1, 2),
    _SsmProvFeatureNeedsImage_Type()
)
ssmProvFeatureNeedsImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssmProvFeatureNeedsImage.setStatus("current")
_SsmProvFeatureIfTable_Object = MibTable
ssmProvFeatureIfTable = _SsmProvFeatureIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ssmProvFeatureIfTable.setStatus("current")
_SsmProvFeatureIfEntry_Object = MibTableRow
ssmProvFeatureIfEntry = _SsmProvFeatureIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 2, 1)
)
ssmProvFeatureIfEntry.setIndexNames(
    (0, "CISCO-SSM-PROV-MIB", "ssmProvFeatureIfStartPort"),
    (0, "CISCO-SSM-PROV-MIB", "ssmProvFeatureIfEndPort"),
    (0, "CISCO-SSM-PROV-MIB", "ssmProvFeatureIfFeatureName"),
)
if mibBuilder.loadTexts:
    ssmProvFeatureIfEntry.setStatus("current")
_SsmProvFeatureIfStartPort_Type = InterfaceIndex
_SsmProvFeatureIfStartPort_Object = MibTableColumn
ssmProvFeatureIfStartPort = _SsmProvFeatureIfStartPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 2, 1, 1),
    _SsmProvFeatureIfStartPort_Type()
)
ssmProvFeatureIfStartPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssmProvFeatureIfStartPort.setStatus("current")
_SsmProvFeatureIfEndPort_Type = InterfaceIndex
_SsmProvFeatureIfEndPort_Object = MibTableColumn
ssmProvFeatureIfEndPort = _SsmProvFeatureIfEndPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 2, 1, 2),
    _SsmProvFeatureIfEndPort_Type()
)
ssmProvFeatureIfEndPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssmProvFeatureIfEndPort.setStatus("current")


class _SsmProvFeatureIfFeatureName_Type(SnmpAdminString):
    """Custom type ssmProvFeatureIfFeatureName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_SsmProvFeatureIfFeatureName_Type.__name__ = "SnmpAdminString"
_SsmProvFeatureIfFeatureName_Object = MibTableColumn
ssmProvFeatureIfFeatureName = _SsmProvFeatureIfFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 2, 1, 3),
    _SsmProvFeatureIfFeatureName_Type()
)
ssmProvFeatureIfFeatureName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssmProvFeatureIfFeatureName.setStatus("current")


class _SsmProvFeatureIfForceRemove_Type(Integer32):
    """Custom type ssmProvFeatureIfForceRemove based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceReset", 1),
          ("noop", 2))
    )


_SsmProvFeatureIfForceRemove_Type.__name__ = "Integer32"
_SsmProvFeatureIfForceRemove_Object = MibTableColumn
ssmProvFeatureIfForceRemove = _SsmProvFeatureIfForceRemove_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 2, 1, 4),
    _SsmProvFeatureIfForceRemove_Type()
)
ssmProvFeatureIfForceRemove.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ssmProvFeatureIfForceRemove.setStatus("current")


class _SsmProvFeatureIfPartnerImageURI_Type(SnmpAdminString):
    """Custom type ssmProvFeatureIfPartnerImageURI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_SsmProvFeatureIfPartnerImageURI_Type.__name__ = "SnmpAdminString"
_SsmProvFeatureIfPartnerImageURI_Object = MibTableColumn
ssmProvFeatureIfPartnerImageURI = _SsmProvFeatureIfPartnerImageURI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 2, 1, 5),
    _SsmProvFeatureIfPartnerImageURI_Type()
)
ssmProvFeatureIfPartnerImageURI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ssmProvFeatureIfPartnerImageURI.setStatus("current")
_SsmProvFeatureIfRowStatus_Type = RowStatus
_SsmProvFeatureIfRowStatus_Object = MibTableColumn
ssmProvFeatureIfRowStatus = _SsmProvFeatureIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 2, 1, 6),
    _SsmProvFeatureIfRowStatus_Type()
)
ssmProvFeatureIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ssmProvFeatureIfRowStatus.setStatus("current")
_SsmProvDppTable_Object = MibTable
ssmProvDppTable = _SsmProvDppTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ssmProvDppTable.setStatus("current")
_SsmProvDppEntry_Object = MibTableRow
ssmProvDppEntry = _SsmProvDppEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 3, 1)
)
ssmProvDppEntry.setIndexNames(
    (0, "CISCO-SSM-PROV-MIB", "ssmProvDppStartPort"),
)
if mibBuilder.loadTexts:
    ssmProvDppEntry.setStatus("current")
_SsmProvDppStartPort_Type = InterfaceIndex
_SsmProvDppStartPort_Object = MibTableColumn
ssmProvDppStartPort = _SsmProvDppStartPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 3, 1, 1),
    _SsmProvDppStartPort_Type()
)
ssmProvDppStartPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssmProvDppStartPort.setStatus("current")
_SsmProvDppEndPort_Type = InterfaceIndex
_SsmProvDppEndPort_Object = MibTableColumn
ssmProvDppEndPort = _SsmProvDppEndPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 3, 1, 2),
    _SsmProvDppEndPort_Type()
)
ssmProvDppEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssmProvDppEndPort.setStatus("current")


class _SsmProvDppName_Type(SnmpAdminString):
    """Custom type ssmProvDppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_SsmProvDppName_Type.__name__ = "SnmpAdminString"
_SsmProvDppName_Object = MibTableColumn
ssmProvDppName = _SsmProvDppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 1, 1, 3, 1, 3),
    _SsmProvDppName_Type()
)
ssmProvDppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssmProvDppName.setStatus("current")
_CiscoSsmProvMIBConform_ObjectIdentity = ObjectIdentity
ciscoSsmProvMIBConform = _CiscoSsmProvMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 2)
)
_SsmProvMIBCompliances_ObjectIdentity = ObjectIdentity
ssmProvMIBCompliances = _SsmProvMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 2, 1)
)
_SsmProvMIBGroups_ObjectIdentity = ObjectIdentity
ssmProvMIBGroups = _SsmProvMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 2, 2)
)

# Managed Objects groups

ssmProvFeatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 2, 2, 1)
)
ssmProvFeatureGroup.setObjects(
    ("CISCO-SSM-PROV-MIB", "ssmProvFeatureNeedsImage")
)
if mibBuilder.loadTexts:
    ssmProvFeatureGroup.setStatus("current")

ssmProvFeatureIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 2, 2, 2)
)
ssmProvFeatureIfGroup.setObjects(
      *(("CISCO-SSM-PROV-MIB", "ssmProvFeatureIfForceRemove"),
        ("CISCO-SSM-PROV-MIB", "ssmProvFeatureIfPartnerImageURI"),
        ("CISCO-SSM-PROV-MIB", "ssmProvFeatureIfRowStatus"))
)
if mibBuilder.loadTexts:
    ssmProvFeatureIfGroup.setStatus("current")

ssmProvDppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 2, 2, 3)
)
ssmProvDppGroup.setObjects(
      *(("CISCO-SSM-PROV-MIB", "ssmProvDppEndPort"),
        ("CISCO-SSM-PROV-MIB", "ssmProvDppName"))
)
if mibBuilder.loadTexts:
    ssmProvDppGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ssmProvMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 448, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ssmProvMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SSM-PROV-MIB",
    **{"ciscoSsmProvMIB": ciscoSsmProvMIB,
       "ciscoSsmProvMIBObjects": ciscoSsmProvMIBObjects,
       "ssmProvConfiguration": ssmProvConfiguration,
       "ssmProvFeatureTable": ssmProvFeatureTable,
       "ssmProvFeatureEntry": ssmProvFeatureEntry,
       "ssmProvFeatureName": ssmProvFeatureName,
       "ssmProvFeatureNeedsImage": ssmProvFeatureNeedsImage,
       "ssmProvFeatureIfTable": ssmProvFeatureIfTable,
       "ssmProvFeatureIfEntry": ssmProvFeatureIfEntry,
       "ssmProvFeatureIfStartPort": ssmProvFeatureIfStartPort,
       "ssmProvFeatureIfEndPort": ssmProvFeatureIfEndPort,
       "ssmProvFeatureIfFeatureName": ssmProvFeatureIfFeatureName,
       "ssmProvFeatureIfForceRemove": ssmProvFeatureIfForceRemove,
       "ssmProvFeatureIfPartnerImageURI": ssmProvFeatureIfPartnerImageURI,
       "ssmProvFeatureIfRowStatus": ssmProvFeatureIfRowStatus,
       "ssmProvDppTable": ssmProvDppTable,
       "ssmProvDppEntry": ssmProvDppEntry,
       "ssmProvDppStartPort": ssmProvDppStartPort,
       "ssmProvDppEndPort": ssmProvDppEndPort,
       "ssmProvDppName": ssmProvDppName,
       "ciscoSsmProvMIBConform": ciscoSsmProvMIBConform,
       "ssmProvMIBCompliances": ssmProvMIBCompliances,
       "ssmProvMIBCompliance": ssmProvMIBCompliance,
       "ssmProvMIBGroups": ssmProvMIBGroups,
       "ssmProvFeatureGroup": ssmProvFeatureGroup,
       "ssmProvFeatureIfGroup": ssmProvFeatureIfGroup,
       "ssmProvDppGroup": ssmProvDppGroup}
)

# SNMP MIB module (CISCO-VISM-CODEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VISM-CODEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:47 2024
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

(voice,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "voice")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoVismCodecMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 97)
)
ciscoVismCodecMIB.setRevisions(
        ("2005-05-24 00:00",
         "2004-01-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VismCodecTemplateCnfGrp_ObjectIdentity = ObjectIdentity
vismCodecTemplateCnfGrp = _VismCodecTemplateCnfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 7)
)
_VismCodecTemplateCnfGrpTable_Object = MibTable
vismCodecTemplateCnfGrpTable = _VismCodecTemplateCnfGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 7, 1)
)
if mibBuilder.loadTexts:
    vismCodecTemplateCnfGrpTable.setStatus("current")
_VismCodecTemplateCnfGrpEntry_Object = MibTableRow
vismCodecTemplateCnfGrpEntry = _VismCodecTemplateCnfGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 7, 1, 1)
)
vismCodecTemplateCnfGrpEntry.setIndexNames(
    (0, "CISCO-VISM-CODEC-MIB", "vismCodecTemplateNum"),
)
if mibBuilder.loadTexts:
    vismCodecTemplateCnfGrpEntry.setStatus("current")


class _VismCodecTemplateNum_Type(Integer32):
    """Custom type vismCodecTemplateNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VismCodecTemplateNum_Type.__name__ = "Integer32"
_VismCodecTemplateNum_Object = MibTableColumn
vismCodecTemplateNum = _VismCodecTemplateNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 7, 1, 1, 1),
    _VismCodecTemplateNum_Type()
)
vismCodecTemplateNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismCodecTemplateNum.setStatus("current")


class _VismCodecSupported_Type(Integer32):
    """Custom type vismCodecSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismCodecSupported_Type.__name__ = "Integer32"
_VismCodecSupported_Object = MibTableColumn
vismCodecSupported = _VismCodecSupported_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 7, 1, 1, 2),
    _VismCodecSupported_Type()
)
vismCodecSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismCodecSupported.setStatus("current")


class _VismCodecTemplateMaxChanCount_Type(Integer32):
    """Custom type vismCodecTemplateMaxChanCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismCodecTemplateMaxChanCount_Type.__name__ = "Integer32"
_VismCodecTemplateMaxChanCount_Object = MibTableColumn
vismCodecTemplateMaxChanCount = _VismCodecTemplateMaxChanCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 7, 1, 1, 3),
    _VismCodecTemplateMaxChanCount_Type()
)
vismCodecTemplateMaxChanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismCodecTemplateMaxChanCount.setStatus("current")
_VismCodecCnfGrp_ObjectIdentity = ObjectIdentity
vismCodecCnfGrp = _VismCodecCnfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18)
)
_VismCodecCnfTable_Object = MibTable
vismCodecCnfTable = _VismCodecCnfTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1)
)
if mibBuilder.loadTexts:
    vismCodecCnfTable.setStatus("current")
_VismCodecCnfEntry_Object = MibTableRow
vismCodecCnfEntry = _VismCodecCnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1)
)
vismCodecCnfEntry.setIndexNames(
    (0, "CISCO-VISM-CODEC-MIB", "vismCodecCnfIndex"),
)
if mibBuilder.loadTexts:
    vismCodecCnfEntry.setStatus("current")


class _VismCodecCnfIndex_Type(Integer32):
    """Custom type vismCodecCnfIndex based on Integer32"""
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("clearChannel", 6),
          ("g711a", 2),
          ("g711u", 1),
          ("g723ah", 12),
          ("g723al", 14),
          ("g723h", 11),
          ("g723l", 13),
          ("g726r16000", 7),
          ("g726r24000", 8),
          ("g726r32000", 3),
          ("g726r40000", 9),
          ("g729a", 4),
          ("g729ab", 5),
          ("lossless", 15))
    )


_VismCodecCnfIndex_Type.__name__ = "Integer32"
_VismCodecCnfIndex_Object = MibTableColumn
vismCodecCnfIndex = _VismCodecCnfIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1, 1),
    _VismCodecCnfIndex_Type()
)
vismCodecCnfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismCodecCnfIndex.setStatus("current")


class _VismCodecName_Type(SnmpAdminString):
    """Custom type vismCodecName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_VismCodecName_Type.__name__ = "SnmpAdminString"
_VismCodecName_Object = MibTableColumn
vismCodecName = _VismCodecName_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1, 2),
    _VismCodecName_Type()
)
vismCodecName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismCodecName.setStatus("current")


class _VismCodecPktPeriod_Type(Integer32):
    """Custom type vismCodecPktPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40,
              60)
        )
    )
    namedValues = NamedValues(
        *(("fourty", 40),
          ("sixty", 60),
          ("ten", 10),
          ("thirty", 30),
          ("twenty", 20))
    )


_VismCodecPktPeriod_Type.__name__ = "Integer32"
_VismCodecPktPeriod_Object = MibTableColumn
vismCodecPktPeriod = _VismCodecPktPeriod_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1, 3),
    _VismCodecPktPeriod_Type()
)
vismCodecPktPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCodecPktPeriod.setStatus("current")
if mibBuilder.loadTexts:
    vismCodecPktPeriod.setUnits("milliseconds")


class _VismCodecPreference_Type(Integer32):
    """Custom type vismCodecPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VismCodecPreference_Type.__name__ = "Integer32"
_VismCodecPreference_Object = MibTableColumn
vismCodecPreference = _VismCodecPreference_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1, 4),
    _VismCodecPreference_Type()
)
vismCodecPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCodecPreference.setStatus("current")


class _VismCodecString_Type(SnmpAdminString):
    """Custom type vismCodecString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_VismCodecString_Type.__name__ = "SnmpAdminString"
_VismCodecString_Object = MibTableColumn
vismCodecString = _VismCodecString_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1, 5),
    _VismCodecString_Type()
)
vismCodecString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCodecString.setStatus("current")


class _VismCodecIanaType_Type(Integer32):
    """Custom type vismCodecIanaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_VismCodecIanaType_Type.__name__ = "Integer32"
_VismCodecIanaType_Object = MibTableColumn
vismCodecIanaType = _VismCodecIanaType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1, 6),
    _VismCodecIanaType_Type()
)
vismCodecIanaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCodecIanaType.setStatus("current")


class _VismAltCodecString1_Type(SnmpAdminString):
    """Custom type vismAltCodecString1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VismAltCodecString1_Type.__name__ = "SnmpAdminString"
_VismAltCodecString1_Object = MibTableColumn
vismAltCodecString1 = _VismAltCodecString1_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1, 7),
    _VismAltCodecString1_Type()
)
vismAltCodecString1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAltCodecString1.setStatus("current")


class _VismAltCodecString2_Type(SnmpAdminString):
    """Custom type vismAltCodecString2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VismAltCodecString2_Type.__name__ = "SnmpAdminString"
_VismAltCodecString2_Object = MibTableColumn
vismAltCodecString2 = _VismAltCodecString2_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1, 8),
    _VismAltCodecString2_Type()
)
vismAltCodecString2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAltCodecString2.setStatus("current")


class _VismAltCodecString3_Type(SnmpAdminString):
    """Custom type vismAltCodecString3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VismAltCodecString3_Type.__name__ = "SnmpAdminString"
_VismAltCodecString3_Object = MibTableColumn
vismAltCodecString3 = _VismAltCodecString3_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1, 9),
    _VismAltCodecString3_Type()
)
vismAltCodecString3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAltCodecString3.setStatus("current")
_CiscoVismCodecMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVismCodecMIBConformance = _CiscoVismCodecMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 97, 2)
)
_CiscoVismCodecMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVismCodecMIBCompliances = _CiscoVismCodecMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 97, 2, 1)
)
_CiscoVismCodecMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVismCodecMIBGroups = _CiscoVismCodecMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 97, 2, 2)
)

# Managed Objects groups

ciscoVismCodecCnfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 97, 2, 2, 1)
)
ciscoVismCodecCnfGroup.setObjects(
      *(("CISCO-VISM-CODEC-MIB", "vismCodecCnfIndex"),
        ("CISCO-VISM-CODEC-MIB", "vismCodecName"),
        ("CISCO-VISM-CODEC-MIB", "vismCodecPktPeriod"),
        ("CISCO-VISM-CODEC-MIB", "vismCodecPreference"),
        ("CISCO-VISM-CODEC-MIB", "vismCodecString"),
        ("CISCO-VISM-CODEC-MIB", "vismCodecIanaType"))
)
if mibBuilder.loadTexts:
    ciscoVismCodecCnfGroup.setStatus("current")

ciscoVismCodecTemplateGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 97, 2, 2, 2)
)
ciscoVismCodecTemplateGrp.setObjects(
      *(("CISCO-VISM-CODEC-MIB", "vismCodecTemplateNum"),
        ("CISCO-VISM-CODEC-MIB", "vismCodecSupported"),
        ("CISCO-VISM-CODEC-MIB", "vismCodecTemplateMaxChanCount"))
)
if mibBuilder.loadTexts:
    ciscoVismCodecTemplateGrp.setStatus("current")

ciscoAltVismCodecCnfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 97, 2, 2, 3)
)
ciscoAltVismCodecCnfGroup.setObjects(
      *(("CISCO-VISM-CODEC-MIB", "vismAltCodecString1"),
        ("CISCO-VISM-CODEC-MIB", "vismAltCodecString2"),
        ("CISCO-VISM-CODEC-MIB", "vismAltCodecString3"))
)
if mibBuilder.loadTexts:
    ciscoAltVismCodecCnfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVismCodecCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 97, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoVismCodecCompliance.setStatus(
        "deprecated"
    )

ciscoVismCodecComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 97, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoVismCodecComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VISM-CODEC-MIB",
    **{"vismCodecTemplateCnfGrp": vismCodecTemplateCnfGrp,
       "vismCodecTemplateCnfGrpTable": vismCodecTemplateCnfGrpTable,
       "vismCodecTemplateCnfGrpEntry": vismCodecTemplateCnfGrpEntry,
       "vismCodecTemplateNum": vismCodecTemplateNum,
       "vismCodecSupported": vismCodecSupported,
       "vismCodecTemplateMaxChanCount": vismCodecTemplateMaxChanCount,
       "vismCodecCnfGrp": vismCodecCnfGrp,
       "vismCodecCnfTable": vismCodecCnfTable,
       "vismCodecCnfEntry": vismCodecCnfEntry,
       "vismCodecCnfIndex": vismCodecCnfIndex,
       "vismCodecName": vismCodecName,
       "vismCodecPktPeriod": vismCodecPktPeriod,
       "vismCodecPreference": vismCodecPreference,
       "vismCodecString": vismCodecString,
       "vismCodecIanaType": vismCodecIanaType,
       "vismAltCodecString1": vismAltCodecString1,
       "vismAltCodecString2": vismAltCodecString2,
       "vismAltCodecString3": vismAltCodecString3,
       "ciscoVismCodecMIB": ciscoVismCodecMIB,
       "ciscoVismCodecMIBConformance": ciscoVismCodecMIBConformance,
       "ciscoVismCodecMIBCompliances": ciscoVismCodecMIBCompliances,
       "ciscoVismCodecCompliance": ciscoVismCodecCompliance,
       "ciscoVismCodecComplianceRev1": ciscoVismCodecComplianceRev1,
       "ciscoVismCodecMIBGroups": ciscoVismCodecMIBGroups,
       "ciscoVismCodecCnfGroup": ciscoVismCodecCnfGroup,
       "ciscoVismCodecTemplateGrp": ciscoVismCodecTemplateGrp,
       "ciscoAltVismCodecCnfGroup": ciscoAltVismCodecCnfGroup}
)

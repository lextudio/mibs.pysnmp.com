# SNMP MIB module (CISCO-ATM-TRAFFIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-TRAFFIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:04 2024
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

(atmTrafficDescrParamEntry,) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmTrafficDescrParamEntry")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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

ciscoAtmTrafficExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11)
)
ciscoAtmTrafficExtMIB.setRevisions(
        ("2002-08-26 00:00",
         "2001-11-01 00:00",
         "1997-05-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoAtmTrafficExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmTrafficExtMIBObjects = _CiscoAtmTrafficExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1)
)
_CiscoAtmTrafficTypeExt_ObjectIdentity = ObjectIdentity
ciscoAtmTrafficTypeExt = _CiscoAtmTrafficTypeExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1)
)
_AtmNoClpNoScrCdvt_ObjectIdentity = ObjectIdentity
atmNoClpNoScrCdvt = _AtmNoClpNoScrCdvt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    atmNoClpNoScrCdvt.setStatus("deprecated")
_AtmClpScrMbsCdvt_ObjectIdentity = ObjectIdentity
atmClpScrMbsCdvt = _AtmClpScrMbsCdvt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 2)
)
if mibBuilder.loadTexts:
    atmClpScrMbsCdvt.setStatus("current")
_AtmNoClpScrMbsCdvt_ObjectIdentity = ObjectIdentity
atmNoClpScrMbsCdvt = _AtmNoClpScrMbsCdvt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 3)
)
if mibBuilder.loadTexts:
    atmNoClpScrMbsCdvt.setStatus("current")
_AtmNoClpMcr_ObjectIdentity = ObjectIdentity
atmNoClpMcr = _AtmNoClpMcr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 4)
)
if mibBuilder.loadTexts:
    atmNoClpMcr.setStatus("current")
_AtmNoClpMcrCdvt_ObjectIdentity = ObjectIdentity
atmNoClpMcrCdvt = _AtmNoClpMcrCdvt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 5)
)
if mibBuilder.loadTexts:
    atmNoClpMcrCdvt.setStatus("current")
_CiscoAtmTrafficTableExt_ObjectIdentity = ObjectIdentity
ciscoAtmTrafficTableExt = _CiscoAtmTrafficTableExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2)
)
_AtmTrafficDescrParamExtTable_Object = MibTable
atmTrafficDescrParamExtTable = _AtmTrafficDescrParamExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    atmTrafficDescrParamExtTable.setStatus("current")
_AtmTrafficDescrParamExtEntry_Object = MibTableRow
atmTrafficDescrParamExtEntry = _AtmTrafficDescrParamExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    atmTrafficDescrParamExtEntry.setStatus("current")


class _AtmTrafficExplicitServCategory_Type(Integer32):
    """Custom type atmTrafficExplicitServCategory based on Integer32"""
    defaultValue = 6

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
        *(("abr", 4),
          ("cbr", 1),
          ("notDef", 6),
          ("ubr", 5),
          ("vbrNrt", 3),
          ("vbrRt", 2))
    )


_AtmTrafficExplicitServCategory_Type.__name__ = "Integer32"
_AtmTrafficExplicitServCategory_Object = MibTableColumn
atmTrafficExplicitServCategory = _AtmTrafficExplicitServCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1, 1),
    _AtmTrafficExplicitServCategory_Type()
)
atmTrafficExplicitServCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficExplicitServCategory.setStatus("current")


class _AtmTrafficDerivedServCategory_Type(Integer32):
    """Custom type atmTrafficDerivedServCategory based on Integer32"""
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
        *(("abr", 4),
          ("cbr", 1),
          ("ubr", 5),
          ("vbrNrt", 3),
          ("vbrRt", 2))
    )


_AtmTrafficDerivedServCategory_Type.__name__ = "Integer32"
_AtmTrafficDerivedServCategory_Object = MibTableColumn
atmTrafficDerivedServCategory = _AtmTrafficDerivedServCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1, 2),
    _AtmTrafficDerivedServCategory_Type()
)
atmTrafficDerivedServCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrafficDerivedServCategory.setStatus("current")
_AtmTrafficDescriptorName_Type = SnmpAdminString
_AtmTrafficDescriptorName_Object = MibTableColumn
atmTrafficDescriptorName = _AtmTrafficDescriptorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1, 3),
    _AtmTrafficDescriptorName_Type()
)
atmTrafficDescriptorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficDescriptorName.setStatus("current")
_CiscoAtmTrafficExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAtmTrafficExtMIBConformance = _CiscoAtmTrafficExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 3)
)
_CiscoAtmTrafficExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAtmTrafficExtMIBCompliances = _CiscoAtmTrafficExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 1)
)
_CiscoAtmTrafficExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAtmTrafficExtMIBGroups = _CiscoAtmTrafficExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 2)
)
atmTrafficDescrParamEntry.registerAugmentions(
    ("CISCO-ATM-TRAFFIC-MIB",
     "atmTrafficDescrParamExtEntry")
)
atmTrafficDescrParamExtEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())

# Managed Objects groups

ciscoAtmTrafficTableExtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 2, 1)
)
ciscoAtmTrafficTableExtMIBGroup.setObjects(
      *(("CISCO-ATM-TRAFFIC-MIB", "atmTrafficExplicitServCategory"),
        ("CISCO-ATM-TRAFFIC-MIB", "atmTrafficDerivedServCategory"))
)
if mibBuilder.loadTexts:
    ciscoAtmTrafficTableExtMIBGroup.setStatus("current")

ciscoAtmTrafficNmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 2, 2)
)
ciscoAtmTrafficNmsGroup.setObjects(
    ("CISCO-ATM-TRAFFIC-MIB", "atmTrafficDescriptorName")
)
if mibBuilder.loadTexts:
    ciscoAtmTrafficNmsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAtmTrafficExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmTrafficExtMIBCompliance.setStatus(
        "deprecated"
    )

ciscoAtmTrafficExtMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoAtmTrafficExtMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-TRAFFIC-MIB",
    **{"ciscoAtmTrafficExtMIB": ciscoAtmTrafficExtMIB,
       "ciscoAtmTrafficExtMIBObjects": ciscoAtmTrafficExtMIBObjects,
       "ciscoAtmTrafficTypeExt": ciscoAtmTrafficTypeExt,
       "atmNoClpNoScrCdvt": atmNoClpNoScrCdvt,
       "atmClpScrMbsCdvt": atmClpScrMbsCdvt,
       "atmNoClpScrMbsCdvt": atmNoClpScrMbsCdvt,
       "atmNoClpMcr": atmNoClpMcr,
       "atmNoClpMcrCdvt": atmNoClpMcrCdvt,
       "ciscoAtmTrafficTableExt": ciscoAtmTrafficTableExt,
       "atmTrafficDescrParamExtTable": atmTrafficDescrParamExtTable,
       "atmTrafficDescrParamExtEntry": atmTrafficDescrParamExtEntry,
       "atmTrafficExplicitServCategory": atmTrafficExplicitServCategory,
       "atmTrafficDerivedServCategory": atmTrafficDerivedServCategory,
       "atmTrafficDescriptorName": atmTrafficDescriptorName,
       "ciscoAtmTrafficExtMIBConformance": ciscoAtmTrafficExtMIBConformance,
       "ciscoAtmTrafficExtMIBCompliances": ciscoAtmTrafficExtMIBCompliances,
       "ciscoAtmTrafficExtMIBCompliance": ciscoAtmTrafficExtMIBCompliance,
       "ciscoAtmTrafficExtMIBComplianceRev1": ciscoAtmTrafficExtMIBComplianceRev1,
       "ciscoAtmTrafficExtMIBGroups": ciscoAtmTrafficExtMIBGroups,
       "ciscoAtmTrafficTableExtMIBGroup": ciscoAtmTrafficTableExtMIBGroup,
       "ciscoAtmTrafficNmsGroup": ciscoAtmTrafficNmsGroup}
)

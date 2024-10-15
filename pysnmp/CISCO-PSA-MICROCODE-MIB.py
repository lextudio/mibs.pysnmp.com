# SNMP MIB module (CISCO-PSA-MICROCODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PSA-MICROCODE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:12 2024
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

(entPhysicalDescr,
 entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalDescr",
    "entPhysicalIndex",
    "entPhysicalName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoPsaMicrocodeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 259)
)
ciscoPsaMicrocodeMIB.setRevisions(
        ("2002-06-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PsaMicrocodeBundleId(Integer32, TextualConvention):
    status = "current"
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("bgppaGE", 12),
          ("bgppaPOS", 11),
          ("cscGE", 29),
          ("eoMplsGE", 23),
          ("frtpPOS", 24),
          ("inputAcl128GE", 15),
          ("inputAcl128POS", 14),
          ("inputAcl128Taz", 26),
          ("inputAcl448GE", 19),
          ("inputAcl448POS", 18),
          ("ipColorPOS", 13),
          ("linkBundleDMGE", 33),
          ("linkBundleDMPOS", 31),
          ("linkBundleSMGE", 32),
          ("linkBundleSMPOS", 30),
          ("none", 2),
          ("outputAcl128GE", 17),
          ("outputAcl128POS", 16),
          ("outputAcl448GE", 21),
          ("outputAcl448POS", 20),
          ("outputAclATM", 25),
          ("pircGE", 8),
          ("pircPOS", 7),
          ("serverCard", 22),
          ("uRPFGE", 28),
          ("uRPFPOS", 9),
          ("unknown", 1),
          ("vanillaGE", 4),
          ("vanillaInuit", 5),
          ("vanillaPOS", 3),
          ("vanillaTaz", 6),
          ("vrfSelectionGE", 27),
          ("vrfSelectionPOS", 10))
    )



class PsaMicrocodeFeatures(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoPsaMicrocodeMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoPsaMicrocodeMIBNotifs = _CiscoPsaMicrocodeMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 0)
)
_CiscoPsaMicrocodeMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPsaMicrocodeMIBObjects = _CiscoPsaMicrocodeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 1)
)
_CpmcModulePsa_ObjectIdentity = ObjectIdentity
cpmcModulePsa = _CpmcModulePsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1)
)
_CpmcModulePsaTable_Object = MibTable
cpmcModulePsaTable = _CpmcModulePsaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cpmcModulePsaTable.setStatus("current")
_CpmcModulePsaEntry_Object = MibTableRow
cpmcModulePsaEntry = _CpmcModulePsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1, 1, 1)
)
cpmcModulePsaEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cpmcModulePsaEntry.setStatus("current")
_CpmcModulePsaCurrBundleId_Type = PsaMicrocodeBundleId
_CpmcModulePsaCurrBundleId_Object = MibTableColumn
cpmcModulePsaCurrBundleId = _CpmcModulePsaCurrBundleId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1, 1, 1, 1),
    _CpmcModulePsaCurrBundleId_Type()
)
cpmcModulePsaCurrBundleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmcModulePsaCurrBundleId.setStatus("current")
_CpmcModulePsaPrevBundleId_Type = PsaMicrocodeBundleId
_CpmcModulePsaPrevBundleId_Object = MibTableColumn
cpmcModulePsaPrevBundleId = _CpmcModulePsaPrevBundleId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1, 1, 1, 2),
    _CpmcModulePsaPrevBundleId_Type()
)
cpmcModulePsaPrevBundleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmcModulePsaPrevBundleId.setStatus("current")
_CpmcModulePsaFeaturesEnabled_Type = PsaMicrocodeFeatures
_CpmcModulePsaFeaturesEnabled_Object = MibTableColumn
cpmcModulePsaFeaturesEnabled = _CpmcModulePsaFeaturesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1, 1, 1, 3),
    _CpmcModulePsaFeaturesEnabled_Type()
)
cpmcModulePsaFeaturesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmcModulePsaFeaturesEnabled.setStatus("current")
_CpmcModulePsaFeaturesDisabled_Type = PsaMicrocodeFeatures
_CpmcModulePsaFeaturesDisabled_Object = MibTableColumn
cpmcModulePsaFeaturesDisabled = _CpmcModulePsaFeaturesDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 1, 1, 1, 4),
    _CpmcModulePsaFeaturesDisabled_Type()
)
cpmcModulePsaFeaturesDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmcModulePsaFeaturesDisabled.setStatus("current")
_CpmcBundle_ObjectIdentity = ObjectIdentity
cpmcBundle = _CpmcBundle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 2)
)
_CpmcBundleTable_Object = MibTable
cpmcBundleTable = _CpmcBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cpmcBundleTable.setStatus("current")
_CpmcBundleEntry_Object = MibTableRow
cpmcBundleEntry = _CpmcBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 2, 1, 1)
)
cpmcBundleEntry.setIndexNames(
    (0, "CISCO-PSA-MICROCODE-MIB", "cpmcBundleId"),
)
if mibBuilder.loadTexts:
    cpmcBundleEntry.setStatus("current")
_CpmcBundleId_Type = PsaMicrocodeBundleId
_CpmcBundleId_Object = MibTableColumn
cpmcBundleId = _CpmcBundleId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 2, 1, 1, 1),
    _CpmcBundleId_Type()
)
cpmcBundleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmcBundleId.setStatus("current")
_CpmcBundleFeatures_Type = PsaMicrocodeFeatures
_CpmcBundleFeatures_Object = MibTableColumn
cpmcBundleFeatures = _CpmcBundleFeatures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 2, 1, 1, 2),
    _CpmcBundleFeatures_Type()
)
cpmcBundleFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmcBundleFeatures.setStatus("current")
_CpmcNotif_ObjectIdentity = ObjectIdentity
cpmcNotif = _CpmcNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 3)
)


class _CpmcNotifEnables_Type(TruthValue):
    """Custom type cpmcNotifEnables based on TruthValue"""


_CpmcNotifEnables_Object = MibScalar
cpmcNotifEnables = _CpmcNotifEnables_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 1, 3, 1),
    _CpmcNotifEnables_Type()
)
cpmcNotifEnables.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmcNotifEnables.setStatus("current")
_CiscoPsaMicrocodeMIBConformance_ObjectIdentity = ObjectIdentity
ciscoPsaMicrocodeMIBConformance = _CiscoPsaMicrocodeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 2)
)
_CiscoPsaMicrocodeMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPsaMicrocodeMIBCompliances = _CiscoPsaMicrocodeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 2, 1)
)
_CiscoPsaMicrocodeMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPsaMicrocodeMIBGroups = _CiscoPsaMicrocodeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 2, 2)
)

# Managed Objects groups

ciscoPsaMicrocodeParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 2, 2, 1)
)
ciscoPsaMicrocodeParamsGroup.setObjects(
      *(("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaCurrBundleId"),
        ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaPrevBundleId"),
        ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaFeaturesEnabled"),
        ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaFeaturesDisabled"),
        ("CISCO-PSA-MICROCODE-MIB", "cpmcBundleFeatures"),
        ("CISCO-PSA-MICROCODE-MIB", "cpmcNotifEnables"))
)
if mibBuilder.loadTexts:
    ciscoPsaMicrocodeParamsGroup.setStatus("current")


# Notification objects

ciscoPsaMicrocodeReload = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 0, 1)
)
ciscoPsaMicrocodeReload.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaCurrBundleId"),
        ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaPrevBundleId"),
        ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaFeaturesEnabled"),
        ("CISCO-PSA-MICROCODE-MIB", "cpmcModulePsaFeaturesDisabled"))
)
if mibBuilder.loadTexts:
    ciscoPsaMicrocodeReload.setStatus(
        "current"
    )


# Notifications groups

ciscoPsaMicrocodeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 2, 2, 2)
)
ciscoPsaMicrocodeNotifGroup.setObjects(
    ("CISCO-PSA-MICROCODE-MIB", "ciscoPsaMicrocodeReload")
)
if mibBuilder.loadTexts:
    ciscoPsaMicrocodeNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoPsaMicrocodeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 259, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPsaMicrocodeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PSA-MICROCODE-MIB",
    **{"PsaMicrocodeBundleId": PsaMicrocodeBundleId,
       "PsaMicrocodeFeatures": PsaMicrocodeFeatures,
       "ciscoPsaMicrocodeMIB": ciscoPsaMicrocodeMIB,
       "ciscoPsaMicrocodeMIBNotifs": ciscoPsaMicrocodeMIBNotifs,
       "ciscoPsaMicrocodeReload": ciscoPsaMicrocodeReload,
       "ciscoPsaMicrocodeMIBObjects": ciscoPsaMicrocodeMIBObjects,
       "cpmcModulePsa": cpmcModulePsa,
       "cpmcModulePsaTable": cpmcModulePsaTable,
       "cpmcModulePsaEntry": cpmcModulePsaEntry,
       "cpmcModulePsaCurrBundleId": cpmcModulePsaCurrBundleId,
       "cpmcModulePsaPrevBundleId": cpmcModulePsaPrevBundleId,
       "cpmcModulePsaFeaturesEnabled": cpmcModulePsaFeaturesEnabled,
       "cpmcModulePsaFeaturesDisabled": cpmcModulePsaFeaturesDisabled,
       "cpmcBundle": cpmcBundle,
       "cpmcBundleTable": cpmcBundleTable,
       "cpmcBundleEntry": cpmcBundleEntry,
       "cpmcBundleId": cpmcBundleId,
       "cpmcBundleFeatures": cpmcBundleFeatures,
       "cpmcNotif": cpmcNotif,
       "cpmcNotifEnables": cpmcNotifEnables,
       "ciscoPsaMicrocodeMIBConformance": ciscoPsaMicrocodeMIBConformance,
       "ciscoPsaMicrocodeMIBCompliances": ciscoPsaMicrocodeMIBCompliances,
       "ciscoPsaMicrocodeMIBCompliance": ciscoPsaMicrocodeMIBCompliance,
       "ciscoPsaMicrocodeMIBGroups": ciscoPsaMicrocodeMIBGroups,
       "ciscoPsaMicrocodeParamsGroup": ciscoPsaMicrocodeParamsGroup,
       "ciscoPsaMicrocodeNotifGroup": ciscoPsaMicrocodeNotifGroup}
)

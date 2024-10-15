# SNMP MIB module (PDN-IF-EXT-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-IF-EXT-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:44 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdnIfExt,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdnIfExt")

(pdnIfExtConfig,) = mibBuilder.importSymbols(
    "PDN-IFEXT-MIB",
    "pdnIfExtConfig")

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

pdnIfExtEncapConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3)
)
pdnIfExtEncapConfig.setRevisions(
        ("2003-12-16 09:00",
         "2001-11-13 00:00",
         "2001-11-12 00:00",
         "2000-05-11 00:00",
         "2000-05-03 00:00",
         "2000-05-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PdnLinkRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("uplink", 1))
    )



# MIB Managed Objects in the order of their OIDs

_PdnIfXLinkConfigTable_Object = MibTable
pdnIfXLinkConfigTable = _PdnIfXLinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 3)
)
if mibBuilder.loadTexts:
    pdnIfXLinkConfigTable.setStatus("current")
_PdnIfXLinkConfigEntry_Object = MibTableRow
pdnIfXLinkConfigEntry = _PdnIfXLinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 3, 1)
)
pdnIfXLinkConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnIfXLinkConfigEntry.setStatus("current")
_PdnIfXLinkConfigRole_Type = PdnLinkRole
_PdnIfXLinkConfigRole_Object = MibTableColumn
pdnIfXLinkConfigRole = _PdnIfXLinkConfigRole_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 1, 3, 1, 1),
    _PdnIfXLinkConfigRole_Type()
)
pdnIfXLinkConfigRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnIfXLinkConfigRole.setStatus("current")
_PdnIfMultiprotocolEncapConfigTable_Object = MibTable
pdnIfMultiprotocolEncapConfigTable = _PdnIfMultiprotocolEncapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 1)
)
if mibBuilder.loadTexts:
    pdnIfMultiprotocolEncapConfigTable.setStatus("current")
_PdnIfMultiprotocolEncapConfigEntry_Object = MibTableRow
pdnIfMultiprotocolEncapConfigEntry = _PdnIfMultiprotocolEncapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 1, 1)
)
pdnIfMultiprotocolEncapConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnIfMultiprotocolEncapConfigEntry.setStatus("current")


class _PdnIfMultiprotocolEncapConfigIPRoutedPDUs_Type(Integer32):
    """Custom type pdnIfMultiprotocolEncapConfigIPRoutedPDUs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("llcSnap", 2),
          ("none", 1),
          ("vcBasedMultiplexing", 3))
    )


_PdnIfMultiprotocolEncapConfigIPRoutedPDUs_Type.__name__ = "Integer32"
_PdnIfMultiprotocolEncapConfigIPRoutedPDUs_Object = MibTableColumn
pdnIfMultiprotocolEncapConfigIPRoutedPDUs = _PdnIfMultiprotocolEncapConfigIPRoutedPDUs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 1, 1, 1),
    _PdnIfMultiprotocolEncapConfigIPRoutedPDUs_Type()
)
pdnIfMultiprotocolEncapConfigIPRoutedPDUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnIfMultiprotocolEncapConfigIPRoutedPDUs.setStatus("current")


class _PdnIfMultiprotocolEncapConfigBridgedPDUs_Type(Integer32):
    """Custom type pdnIfMultiprotocolEncapConfigBridgedPDUs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("llcSnap", 2),
          ("none", 1),
          ("vcBasedMultiplexing", 3))
    )


_PdnIfMultiprotocolEncapConfigBridgedPDUs_Type.__name__ = "Integer32"
_PdnIfMultiprotocolEncapConfigBridgedPDUs_Object = MibTableColumn
pdnIfMultiprotocolEncapConfigBridgedPDUs = _PdnIfMultiprotocolEncapConfigBridgedPDUs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 1, 1, 2),
    _PdnIfMultiprotocolEncapConfigBridgedPDUs_Type()
)
pdnIfMultiprotocolEncapConfigBridgedPDUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnIfMultiprotocolEncapConfigBridgedPDUs.setStatus("current")
_PdnIfMultiprotocolEncapMIBConformance_ObjectIdentity = ObjectIdentity
pdnIfMultiprotocolEncapMIBConformance = _PdnIfMultiprotocolEncapMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2)
)
_PdnIfMultiprotocolEncapMIBGroups_ObjectIdentity = ObjectIdentity
pdnIfMultiprotocolEncapMIBGroups = _PdnIfMultiprotocolEncapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2, 1)
)
_PdnIfMultiprotocolEncapCompliances_ObjectIdentity = ObjectIdentity
pdnIfMultiprotocolEncapCompliances = _PdnIfMultiprotocolEncapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2, 2)
)
_PdnIfXConfigMIBConformance_ObjectIdentity = ObjectIdentity
pdnIfXConfigMIBConformance = _PdnIfXConfigMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 4)
)
_PdnIfXConfigMIBGroups_ObjectIdentity = ObjectIdentity
pdnIfXConfigMIBGroups = _PdnIfXConfigMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 4, 1)
)

# Managed Objects groups

pdnIfMultiprotocolEncapsulationOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2, 1, 1)
)
pdnIfMultiprotocolEncapsulationOptionalGroup.setObjects(
      *(("PDN-IF-EXT-CONFIG-MIB", "pdnIfMultiprotocolEncapConfigIPRoutedPDUs"),
        ("PDN-IF-EXT-CONFIG-MIB", "pdnIfMultiprotocolEncapConfigBridgedPDUs"))
)
if mibBuilder.loadTexts:
    pdnIfMultiprotocolEncapsulationOptionalGroup.setStatus("current")

pdnIfXLinkConfigOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 4, 1, 1)
)
pdnIfXLinkConfigOptionalGroup.setObjects(
    ("PDN-IF-EXT-CONFIG-MIB", "pdnIfXLinkConfigRole")
)
if mibBuilder.loadTexts:
    pdnIfXLinkConfigOptionalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnIfMultiprotocolEncapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 12, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pdnIfMultiprotocolEncapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-IF-EXT-CONFIG-MIB",
    **{"PdnLinkRole": PdnLinkRole,
       "pdnIfXLinkConfigTable": pdnIfXLinkConfigTable,
       "pdnIfXLinkConfigEntry": pdnIfXLinkConfigEntry,
       "pdnIfXLinkConfigRole": pdnIfXLinkConfigRole,
       "pdnIfExtEncapConfig": pdnIfExtEncapConfig,
       "pdnIfMultiprotocolEncapConfigTable": pdnIfMultiprotocolEncapConfigTable,
       "pdnIfMultiprotocolEncapConfigEntry": pdnIfMultiprotocolEncapConfigEntry,
       "pdnIfMultiprotocolEncapConfigIPRoutedPDUs": pdnIfMultiprotocolEncapConfigIPRoutedPDUs,
       "pdnIfMultiprotocolEncapConfigBridgedPDUs": pdnIfMultiprotocolEncapConfigBridgedPDUs,
       "pdnIfMultiprotocolEncapMIBConformance": pdnIfMultiprotocolEncapMIBConformance,
       "pdnIfMultiprotocolEncapMIBGroups": pdnIfMultiprotocolEncapMIBGroups,
       "pdnIfMultiprotocolEncapsulationOptionalGroup": pdnIfMultiprotocolEncapsulationOptionalGroup,
       "pdnIfMultiprotocolEncapCompliances": pdnIfMultiprotocolEncapCompliances,
       "pdnIfMultiprotocolEncapCompliance": pdnIfMultiprotocolEncapCompliance,
       "pdnIfXConfigMIBConformance": pdnIfXConfigMIBConformance,
       "pdnIfXConfigMIBGroups": pdnIfXConfigMIBGroups,
       "pdnIfXLinkConfigOptionalGroup": pdnIfXLinkConfigOptionalGroup}
)

# SNMP MIB module (Juniper-TSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-TSM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:29 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniIfType,) = mibBuilder.importSymbols(
    "Juniper-UNI-IF-MIB",
    "JuniIfType")

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

juniTsmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72)
)
juniTsmMIB.setRevisions(
        ("2005-05-23 14:37",
         "2005-04-27 22:57",
         "2003-10-23 20:45")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniTsmLocationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adapterPort", 3),
          ("slotAdapterPort", 2),
          ("slotPort", 1),
          ("unknown", 0))
    )



class JuniTsmLocationValue(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



# MIB Managed Objects in the order of their OIDs

_JuniTsmObjects_ObjectIdentity = ObjectIdentity
juniTsmObjects = _JuniTsmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1)
)
_JuniTsmData_ObjectIdentity = ObjectIdentity
juniTsmData = _JuniTsmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1)
)
_JuniTsmLocationType_Type = JuniTsmLocationType
_JuniTsmLocationType_Object = MibScalar
juniTsmLocationType = _JuniTsmLocationType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 1),
    _JuniTsmLocationType_Type()
)
juniTsmLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTsmLocationType.setStatus("current")
_JuniTsmPortTable_Object = MibTable
juniTsmPortTable = _JuniTsmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniTsmPortTable.setStatus("current")
_JuniTsmPortEntry_Object = MibTableRow
juniTsmPortEntry = _JuniTsmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2, 1)
)
juniTsmPortEntry.setIndexNames(
    (0, "Juniper-TSM-MIB", "juniTsmPortLocation"),
)
if mibBuilder.loadTexts:
    juniTsmPortEntry.setStatus("current")
_JuniTsmPortLocation_Type = JuniTsmLocationValue
_JuniTsmPortLocation_Object = MibTableColumn
juniTsmPortLocation = _JuniTsmPortLocation_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2, 1, 1),
    _JuniTsmPortLocation_Type()
)
juniTsmPortLocation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniTsmPortLocation.setStatus("current")


class _JuniTsmPortType_Type(Integer32):
    """Custom type juniTsmPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("generalPurposeDynamic", 2),
          ("generalPurposeStatic", 1),
          ("securityDynamic", 4),
          ("securityStatic", 3))
    )


_JuniTsmPortType_Type.__name__ = "Integer32"
_JuniTsmPortType_Object = MibTableColumn
juniTsmPortType = _JuniTsmPortType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2, 1, 2),
    _JuniTsmPortType_Type()
)
juniTsmPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTsmPortType.setStatus("current")
_JuniTsmPortHwPresent_Type = TruthValue
_JuniTsmPortHwPresent_Object = MibTableColumn
juniTsmPortHwPresent = _JuniTsmPortHwPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2, 1, 3),
    _JuniTsmPortHwPresent_Type()
)
juniTsmPortHwPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTsmPortHwPresent.setStatus("current")


class _JuniTsmPortAvailableInterfaces_Type(Integer32):
    """Custom type juniTsmPortAvailableInterfaces based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16000),
    )


_JuniTsmPortAvailableInterfaces_Type.__name__ = "Integer32"
_JuniTsmPortAvailableInterfaces_Object = MibTableColumn
juniTsmPortAvailableInterfaces = _JuniTsmPortAvailableInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2, 1, 4),
    _JuniTsmPortAvailableInterfaces_Type()
)
juniTsmPortAvailableInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTsmPortAvailableInterfaces.setStatus("current")


class _JuniTsmPortProvisionedInterfaces_Type(Integer32):
    """Custom type juniTsmPortProvisionedInterfaces based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 16000),
    )


_JuniTsmPortProvisionedInterfaces_Type.__name__ = "Integer32"
_JuniTsmPortProvisionedInterfaces_Object = MibTableColumn
juniTsmPortProvisionedInterfaces = _JuniTsmPortProvisionedInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2, 1, 5),
    _JuniTsmPortProvisionedInterfaces_Type()
)
juniTsmPortProvisionedInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniTsmPortProvisionedInterfaces.setStatus("current")
_JuniTsmAppRegistryTable_Object = MibTable
juniTsmAppRegistryTable = _JuniTsmAppRegistryTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 3)
)
if mibBuilder.loadTexts:
    juniTsmAppRegistryTable.setStatus("current")
_JuniTsmAppRegistryEntry_Object = MibTableRow
juniTsmAppRegistryEntry = _JuniTsmAppRegistryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 3, 1)
)
juniTsmAppRegistryEntry.setIndexNames(
    (0, "Juniper-TSM-MIB", "juniTsmAppRegistryIndex"),
)
if mibBuilder.loadTexts:
    juniTsmAppRegistryEntry.setStatus("current")


class _JuniTsmAppRegistryIndex_Type(Integer32):
    """Custom type juniTsmAppRegistryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JuniTsmAppRegistryIndex_Type.__name__ = "Integer32"
_JuniTsmAppRegistryIndex_Object = MibTableColumn
juniTsmAppRegistryIndex = _JuniTsmAppRegistryIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 3, 1, 1),
    _JuniTsmAppRegistryIndex_Type()
)
juniTsmAppRegistryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniTsmAppRegistryIndex.setStatus("current")
_JuniTsmAppRegistryIfType_Type = JuniIfType
_JuniTsmAppRegistryIfType_Object = MibTableColumn
juniTsmAppRegistryIfType = _JuniTsmAppRegistryIfType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 3, 1, 2),
    _JuniTsmAppRegistryIfType_Type()
)
juniTsmAppRegistryIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTsmAppRegistryIfType.setStatus("current")
_JuniTsmAppRegistryName_Type = DisplayString
_JuniTsmAppRegistryName_Object = MibTableColumn
juniTsmAppRegistryName = _JuniTsmAppRegistryName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 3, 1, 3),
    _JuniTsmAppRegistryName_Type()
)
juniTsmAppRegistryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTsmAppRegistryName.setStatus("current")


class _JuniTsmAppRegistryInterfaceLimit_Type(Integer32):
    """Custom type juniTsmAppRegistryInterfaceLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JuniTsmAppRegistryInterfaceLimit_Type.__name__ = "Integer32"
_JuniTsmAppRegistryInterfaceLimit_Object = MibTableColumn
juniTsmAppRegistryInterfaceLimit = _JuniTsmAppRegistryInterfaceLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 3, 1, 4),
    _JuniTsmAppRegistryInterfaceLimit_Type()
)
juniTsmAppRegistryInterfaceLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTsmAppRegistryInterfaceLimit.setStatus("current")
_JuniTsmApplicationTable_Object = MibTable
juniTsmApplicationTable = _JuniTsmApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 4)
)
if mibBuilder.loadTexts:
    juniTsmApplicationTable.setStatus("current")
_JuniTsmApplicationEntry_Object = MibTableRow
juniTsmApplicationEntry = _JuniTsmApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 4, 1)
)
juniTsmApplicationEntry.setIndexNames(
    (0, "Juniper-TSM-MIB", "juniTsmPortLocation"),
    (0, "Juniper-TSM-MIB", "juniTsmAppRegistryIndex"),
)
if mibBuilder.loadTexts:
    juniTsmApplicationEntry.setStatus("current")


class _JuniTsmApplicationMaxInterfaces_Type(Integer32):
    """Custom type juniTsmApplicationMaxInterfaces based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JuniTsmApplicationMaxInterfaces_Type.__name__ = "Integer32"
_JuniTsmApplicationMaxInterfaces_Object = MibTableColumn
juniTsmApplicationMaxInterfaces = _JuniTsmApplicationMaxInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 4, 1, 1),
    _JuniTsmApplicationMaxInterfaces_Type()
)
juniTsmApplicationMaxInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTsmApplicationMaxInterfaces.setStatus("current")
_JuniTsmApplicationActiveInterfaces_Type = Gauge32
_JuniTsmApplicationActiveInterfaces_Object = MibTableColumn
juniTsmApplicationActiveInterfaces = _JuniTsmApplicationActiveInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 4, 1, 2),
    _JuniTsmApplicationActiveInterfaces_Type()
)
juniTsmApplicationActiveInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTsmApplicationActiveInterfaces.setStatus("current")
_JuniTsmMIBConformance_ObjectIdentity = ObjectIdentity
juniTsmMIBConformance = _JuniTsmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 4)
)
_JuniTsmMIBCompliances_ObjectIdentity = ObjectIdentity
juniTsmMIBCompliances = _JuniTsmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 4, 1)
)
_JuniTsmMIBGroups_ObjectIdentity = ObjectIdentity
juniTsmMIBGroups = _JuniTsmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 4, 2)
)

# Managed Objects groups

juniTsmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 4, 2, 1)
)
juniTsmGroup.setObjects(
      *(("Juniper-TSM-MIB", "juniTsmLocationType"),
        ("Juniper-TSM-MIB", "juniTsmPortType"),
        ("Juniper-TSM-MIB", "juniTsmPortHwPresent"),
        ("Juniper-TSM-MIB", "juniTsmPortAvailableInterfaces"),
        ("Juniper-TSM-MIB", "juniTsmPortProvisionedInterfaces"),
        ("Juniper-TSM-MIB", "juniTsmAppRegistryIfType"),
        ("Juniper-TSM-MIB", "juniTsmAppRegistryName"),
        ("Juniper-TSM-MIB", "juniTsmAppRegistryInterfaceLimit"),
        ("Juniper-TSM-MIB", "juniTsmApplicationMaxInterfaces"),
        ("Juniper-TSM-MIB", "juniTsmApplicationActiveInterfaces"))
)
if mibBuilder.loadTexts:
    juniTsmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniTsmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniTsmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-TSM-MIB",
    **{"JuniTsmLocationType": JuniTsmLocationType,
       "JuniTsmLocationValue": JuniTsmLocationValue,
       "juniTsmMIB": juniTsmMIB,
       "juniTsmObjects": juniTsmObjects,
       "juniTsmData": juniTsmData,
       "juniTsmLocationType": juniTsmLocationType,
       "juniTsmPortTable": juniTsmPortTable,
       "juniTsmPortEntry": juniTsmPortEntry,
       "juniTsmPortLocation": juniTsmPortLocation,
       "juniTsmPortType": juniTsmPortType,
       "juniTsmPortHwPresent": juniTsmPortHwPresent,
       "juniTsmPortAvailableInterfaces": juniTsmPortAvailableInterfaces,
       "juniTsmPortProvisionedInterfaces": juniTsmPortProvisionedInterfaces,
       "juniTsmAppRegistryTable": juniTsmAppRegistryTable,
       "juniTsmAppRegistryEntry": juniTsmAppRegistryEntry,
       "juniTsmAppRegistryIndex": juniTsmAppRegistryIndex,
       "juniTsmAppRegistryIfType": juniTsmAppRegistryIfType,
       "juniTsmAppRegistryName": juniTsmAppRegistryName,
       "juniTsmAppRegistryInterfaceLimit": juniTsmAppRegistryInterfaceLimit,
       "juniTsmApplicationTable": juniTsmApplicationTable,
       "juniTsmApplicationEntry": juniTsmApplicationEntry,
       "juniTsmApplicationMaxInterfaces": juniTsmApplicationMaxInterfaces,
       "juniTsmApplicationActiveInterfaces": juniTsmApplicationActiveInterfaces,
       "juniTsmMIBConformance": juniTsmMIBConformance,
       "juniTsmMIBCompliances": juniTsmMIBCompliances,
       "juniTsmCompliance": juniTsmCompliance,
       "juniTsmMIBGroups": juniTsmMIBGroups,
       "juniTsmGroup": juniTsmGroup}
)

# SNMP MIB module (RBTWS-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBTWS-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:36 2024
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

(rbtwsMibs,) = mibBuilder.importSymbols(
    "RBTWS-ROOT-MIB",
    "rbtwsMibs")

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

rbtwsPortMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6)
)
rbtwsPortMib.setRevisions(
        ("2008-05-19 00:04",
         "2006-11-09 00:01",
         "2006-04-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RbtwsPhysPortNumber(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )



class RbtwsPortMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("directAttachAP", 1),
          ("networkPort", 2),
          ("wired", 3))
    )



class RbtwsPortPoeMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("poeDisable", 2),
          ("poeEnable", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RbtwsPortObjects_ObjectIdentity = ObjectIdentity
rbtwsPortObjects = _RbtwsPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1)
)
_RbtwsPortDataObjects_ObjectIdentity = ObjectIdentity
rbtwsPortDataObjects = _RbtwsPortDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1)
)
_RbtwsPortConfigTable_Object = MibTable
rbtwsPortConfigTable = _RbtwsPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbtwsPortConfigTable.setStatus("current")
_RbtwsPortConfigEntry_Object = MibTableRow
rbtwsPortConfigEntry = _RbtwsPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1)
)
rbtwsPortConfigEntry.setIndexNames(
    (0, "RBTWS-PORT-MIB", "rbtwsPortConfigPortNumber"),
)
if mibBuilder.loadTexts:
    rbtwsPortConfigEntry.setStatus("current")
_RbtwsPortConfigPortNumber_Type = RbtwsPhysPortNumber
_RbtwsPortConfigPortNumber_Object = MibTableColumn
rbtwsPortConfigPortNumber = _RbtwsPortConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1, 1),
    _RbtwsPortConfigPortNumber_Type()
)
rbtwsPortConfigPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsPortConfigPortNumber.setStatus("current")
_RbtwsPortConfigPortMode_Type = RbtwsPortMode
_RbtwsPortConfigPortMode_Object = MibTableColumn
rbtwsPortConfigPortMode = _RbtwsPortConfigPortMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1, 2),
    _RbtwsPortConfigPortMode_Type()
)
rbtwsPortConfigPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsPortConfigPortMode.setStatus("current")
_RbtwsPortConfigPoeMode_Type = RbtwsPortPoeMode
_RbtwsPortConfigPoeMode_Object = MibTableColumn
rbtwsPortConfigPoeMode = _RbtwsPortConfigPoeMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1, 3),
    _RbtwsPortConfigPoeMode_Type()
)
rbtwsPortConfigPoeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsPortConfigPoeMode.setStatus("current")
_RbtwsPortConfigTrunkMaster_Type = RbtwsPhysPortNumber
_RbtwsPortConfigTrunkMaster_Object = MibTableColumn
rbtwsPortConfigTrunkMaster = _RbtwsPortConfigTrunkMaster_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1, 4),
    _RbtwsPortConfigTrunkMaster_Type()
)
rbtwsPortConfigTrunkMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsPortConfigTrunkMaster.setStatus("current")
_RbtwsPortConformance_ObjectIdentity = ObjectIdentity
rbtwsPortConformance = _RbtwsPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2)
)
_RbtwsPortCompliances_ObjectIdentity = ObjectIdentity
rbtwsPortCompliances = _RbtwsPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2, 1)
)
_RbtwsPortGroups_ObjectIdentity = ObjectIdentity
rbtwsPortGroups = _RbtwsPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2, 2)
)

# Managed Objects groups

rbtwsPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2, 2, 1)
)
rbtwsPortConfigGroup.setObjects(
      *(("RBTWS-PORT-MIB", "rbtwsPortConfigPortMode"),
        ("RBTWS-PORT-MIB", "rbtwsPortConfigPoeMode"),
        ("RBTWS-PORT-MIB", "rbtwsPortConfigTrunkMaster"))
)
if mibBuilder.loadTexts:
    rbtwsPortConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbtwsPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbtwsPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBTWS-PORT-MIB",
    **{"RbtwsPhysPortNumber": RbtwsPhysPortNumber,
       "RbtwsPortMode": RbtwsPortMode,
       "RbtwsPortPoeMode": RbtwsPortPoeMode,
       "rbtwsPortMib": rbtwsPortMib,
       "rbtwsPortObjects": rbtwsPortObjects,
       "rbtwsPortDataObjects": rbtwsPortDataObjects,
       "rbtwsPortConfigTable": rbtwsPortConfigTable,
       "rbtwsPortConfigEntry": rbtwsPortConfigEntry,
       "rbtwsPortConfigPortNumber": rbtwsPortConfigPortNumber,
       "rbtwsPortConfigPortMode": rbtwsPortConfigPortMode,
       "rbtwsPortConfigPoeMode": rbtwsPortConfigPoeMode,
       "rbtwsPortConfigTrunkMaster": rbtwsPortConfigTrunkMaster,
       "rbtwsPortConformance": rbtwsPortConformance,
       "rbtwsPortCompliances": rbtwsPortCompliances,
       "rbtwsPortCompliance": rbtwsPortCompliance,
       "rbtwsPortGroups": rbtwsPortGroups,
       "rbtwsPortConfigGroup": rbtwsPortConfigGroup}
)

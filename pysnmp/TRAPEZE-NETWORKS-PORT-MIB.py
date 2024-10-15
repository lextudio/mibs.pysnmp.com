# SNMP MIB module (TRAPEZE-NETWORKS-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:34 2024
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

(TrpzPhysPortNumber,
 TrpzPhysPortNumberOrZero) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-BASIC-TC",
    "TrpzPhysPortNumber",
    "TrpzPhysPortNumberOrZero")

(trpzMibs,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs")


# MODULE-IDENTITY

trpzPortMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 6)
)
trpzPortMib.setRevisions(
        ("2008-10-23 00:10",
         "2008-05-19 00:04",
         "2006-11-09 00:01",
         "2006-04-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TrpzPortMode(Integer32, TextualConvention):
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



class TrpzPortPoeMode(Integer32, TextualConvention):
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

_TrpzPortObjects_ObjectIdentity = ObjectIdentity
trpzPortObjects = _TrpzPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 6, 1)
)
_TrpzPortDataObjects_ObjectIdentity = ObjectIdentity
trpzPortDataObjects = _TrpzPortDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1)
)
_TrpzPortConfigTable_Object = MibTable
trpzPortConfigTable = _TrpzPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    trpzPortConfigTable.setStatus("current")
_TrpzPortConfigEntry_Object = MibTableRow
trpzPortConfigEntry = _TrpzPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1)
)
trpzPortConfigEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigPortNumber"),
)
if mibBuilder.loadTexts:
    trpzPortConfigEntry.setStatus("current")
_TrpzPortConfigPortNumber_Type = TrpzPhysPortNumber
_TrpzPortConfigPortNumber_Object = MibTableColumn
trpzPortConfigPortNumber = _TrpzPortConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1, 1),
    _TrpzPortConfigPortNumber_Type()
)
trpzPortConfigPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzPortConfigPortNumber.setStatus("current")
_TrpzPortConfigPortMode_Type = TrpzPortMode
_TrpzPortConfigPortMode_Object = MibTableColumn
trpzPortConfigPortMode = _TrpzPortConfigPortMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1, 2),
    _TrpzPortConfigPortMode_Type()
)
trpzPortConfigPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzPortConfigPortMode.setStatus("current")
_TrpzPortConfigPoeMode_Type = TrpzPortPoeMode
_TrpzPortConfigPoeMode_Object = MibTableColumn
trpzPortConfigPoeMode = _TrpzPortConfigPoeMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1, 3),
    _TrpzPortConfigPoeMode_Type()
)
trpzPortConfigPoeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzPortConfigPoeMode.setStatus("current")
_TrpzPortConfigTrunkMaster_Type = TrpzPhysPortNumberOrZero
_TrpzPortConfigTrunkMaster_Object = MibTableColumn
trpzPortConfigTrunkMaster = _TrpzPortConfigTrunkMaster_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1, 4),
    _TrpzPortConfigTrunkMaster_Type()
)
trpzPortConfigTrunkMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzPortConfigTrunkMaster.setStatus("current")
_TrpzPortConformance_ObjectIdentity = ObjectIdentity
trpzPortConformance = _TrpzPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2)
)
_TrpzPortCompliances_ObjectIdentity = ObjectIdentity
trpzPortCompliances = _TrpzPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2, 1)
)
_TrpzPortGroups_ObjectIdentity = ObjectIdentity
trpzPortGroups = _TrpzPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2, 2)
)

# Managed Objects groups

trpzPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2, 2, 1)
)
trpzPortConfigGroup.setObjects(
      *(("TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigPortMode"),
        ("TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigPoeMode"),
        ("TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigTrunkMaster"))
)
if mibBuilder.loadTexts:
    trpzPortConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

trpzPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    trpzPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-PORT-MIB",
    **{"TrpzPortMode": TrpzPortMode,
       "TrpzPortPoeMode": TrpzPortPoeMode,
       "trpzPortMib": trpzPortMib,
       "trpzPortObjects": trpzPortObjects,
       "trpzPortDataObjects": trpzPortDataObjects,
       "trpzPortConfigTable": trpzPortConfigTable,
       "trpzPortConfigEntry": trpzPortConfigEntry,
       "trpzPortConfigPortNumber": trpzPortConfigPortNumber,
       "trpzPortConfigPortMode": trpzPortConfigPortMode,
       "trpzPortConfigPoeMode": trpzPortConfigPoeMode,
       "trpzPortConfigTrunkMaster": trpzPortConfigTrunkMaster,
       "trpzPortConformance": trpzPortConformance,
       "trpzPortCompliances": trpzPortCompliances,
       "trpzPortCompliance": trpzPortCompliance,
       "trpzPortGroups": trpzPortGroups,
       "trpzPortConfigGroup": trpzPortConfigGroup}
)

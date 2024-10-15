# SNMP MIB module (CISCO-MAU-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MAU-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:15 2024
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

(ifJackEntry,
 ifMauIfIndex,
 ifMauIndex) = mibBuilder.importSymbols(
    "MAU-MIB",
    "ifJackEntry",
    "ifMauIfIndex",
    "ifMauIndex")

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

ciscoMauExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 398)
)
ciscoMauExtMIB.setRevisions(
        ("2008-03-05 00:00",
         "2004-04-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmExtMIBNotifs_ObjectIdentity = ObjectIdentity
cmExtMIBNotifs = _CmExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 0)
)
_CmExtMIBObjects_ObjectIdentity = ObjectIdentity
cmExtMIBObjects = _CmExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 1)
)
_CmExtMauConfig_ObjectIdentity = ObjectIdentity
cmExtMauConfig = _CmExtMauConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 1)
)
_CmExtJackConfigTable_Object = MibTable
cmExtJackConfigTable = _CmExtJackConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cmExtJackConfigTable.setStatus("current")
_CmExtJackConfigEntry_Object = MibTableRow
cmExtJackConfigEntry = _CmExtJackConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cmExtJackConfigEntry.setStatus("current")


class _CmExtJackState_Type(Integer32):
    """Custom type cmExtJackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CmExtJackState_Type.__name__ = "Integer32"
_CmExtJackState_Object = MibTableColumn
cmExtJackState = _CmExtJackState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 1, 1, 1, 1),
    _CmExtJackState_Type()
)
cmExtJackState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmExtJackState.setStatus("current")
_CmExtAutoMdixConfig_ObjectIdentity = ObjectIdentity
cmExtAutoMdixConfig = _CmExtAutoMdixConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 2)
)
_CmExtIfAutoMdixConfigTable_Object = MibTable
cmExtIfAutoMdixConfigTable = _CmExtIfAutoMdixConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cmExtIfAutoMdixConfigTable.setStatus("current")
_CmExtIfAutoMdixConfigEntry_Object = MibTableRow
cmExtIfAutoMdixConfigEntry = _CmExtIfAutoMdixConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 2, 1, 1)
)
cmExtIfAutoMdixConfigEntry.setIndexNames(
    (0, "MAU-MIB", "ifMauIfIndex"),
    (0, "MAU-MIB", "ifMauIndex"),
)
if mibBuilder.loadTexts:
    cmExtIfAutoMdixConfigEntry.setStatus("current")
_CmExtIfAutoMdixEnabled_Type = TruthValue
_CmExtIfAutoMdixEnabled_Object = MibTableColumn
cmExtIfAutoMdixEnabled = _CmExtIfAutoMdixEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 2, 1, 1, 1),
    _CmExtIfAutoMdixEnabled_Type()
)
cmExtIfAutoMdixEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmExtIfAutoMdixEnabled.setStatus("current")
_CmExtIfMau_ObjectIdentity = ObjectIdentity
cmExtIfMau = _CmExtIfMau_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 3)
)
_CmExtIfMauTrafficTable_Object = MibTable
cmExtIfMauTrafficTable = _CmExtIfMauTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cmExtIfMauTrafficTable.setStatus("current")
_CmExtIfMauTrafficEntry_Object = MibTableRow
cmExtIfMauTrafficEntry = _CmExtIfMauTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 3, 1, 1)
)
cmExtIfMauTrafficEntry.setIndexNames(
    (0, "MAU-MIB", "ifMauIfIndex"),
    (0, "MAU-MIB", "ifMauIndex"),
)
if mibBuilder.loadTexts:
    cmExtIfMauTrafficEntry.setStatus("current")


class _CmExtIfMauTrafficType_Type(Integer32):
    """Custom type cmExtIfMauTrafficType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminControl", 2),
          ("other", 1),
          ("user", 3))
    )


_CmExtIfMauTrafficType_Type.__name__ = "Integer32"
_CmExtIfMauTrafficType_Object = MibTableColumn
cmExtIfMauTrafficType = _CmExtIfMauTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 3, 1, 1, 1),
    _CmExtIfMauTrafficType_Type()
)
cmExtIfMauTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmExtIfMauTrafficType.setStatus("current")
_CmExtMIBConformance_ObjectIdentity = ObjectIdentity
cmExtMIBConformance = _CmExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 2)
)
_CmExtMIBCompliances_ObjectIdentity = ObjectIdentity
cmExtMIBCompliances = _CmExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 1)
)
_CmExtMIBGroups_ObjectIdentity = ObjectIdentity
cmExtMIBGroups = _CmExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 2)
)
ifJackEntry.registerAugmentions(
    ("CISCO-MAU-EXT-MIB",
     "cmExtJackConfigEntry")
)
cmExtJackConfigEntry.setIndexNames(*ifJackEntry.getIndexNames())

# Managed Objects groups

cmExtJackConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 2, 1)
)
cmExtJackConfigGroup.setObjects(
    ("CISCO-MAU-EXT-MIB", "cmExtJackState")
)
if mibBuilder.loadTexts:
    cmExtJackConfigGroup.setStatus("current")

cmExtIfAutoMdixConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 2, 2)
)
cmExtIfAutoMdixConfigGroup.setObjects(
    ("CISCO-MAU-EXT-MIB", "cmExtIfAutoMdixEnabled")
)
if mibBuilder.loadTexts:
    cmExtIfAutoMdixConfigGroup.setStatus("current")

cmExtIfMauTrafficGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 2, 3)
)
cmExtIfMauTrafficGroup.setObjects(
    ("CISCO-MAU-EXT-MIB", "cmExtIfMauTrafficType")
)
if mibBuilder.loadTexts:
    cmExtIfMauTrafficGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cmExtMIBCompliance.setStatus(
        "deprecated"
    )

cmExtMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cmExtMIBCompliance2.setStatus(
        "deprecated"
    )

cmExtMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cmExtMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MAU-EXT-MIB",
    **{"ciscoMauExtMIB": ciscoMauExtMIB,
       "cmExtMIBNotifs": cmExtMIBNotifs,
       "cmExtMIBObjects": cmExtMIBObjects,
       "cmExtMauConfig": cmExtMauConfig,
       "cmExtJackConfigTable": cmExtJackConfigTable,
       "cmExtJackConfigEntry": cmExtJackConfigEntry,
       "cmExtJackState": cmExtJackState,
       "cmExtAutoMdixConfig": cmExtAutoMdixConfig,
       "cmExtIfAutoMdixConfigTable": cmExtIfAutoMdixConfigTable,
       "cmExtIfAutoMdixConfigEntry": cmExtIfAutoMdixConfigEntry,
       "cmExtIfAutoMdixEnabled": cmExtIfAutoMdixEnabled,
       "cmExtIfMau": cmExtIfMau,
       "cmExtIfMauTrafficTable": cmExtIfMauTrafficTable,
       "cmExtIfMauTrafficEntry": cmExtIfMauTrafficEntry,
       "cmExtIfMauTrafficType": cmExtIfMauTrafficType,
       "cmExtMIBConformance": cmExtMIBConformance,
       "cmExtMIBCompliances": cmExtMIBCompliances,
       "cmExtMIBCompliance": cmExtMIBCompliance,
       "cmExtMIBCompliance2": cmExtMIBCompliance2,
       "cmExtMIBCompliance3": cmExtMIBCompliance3,
       "cmExtMIBGroups": cmExtMIBGroups,
       "cmExtJackConfigGroup": cmExtJackConfigGroup,
       "cmExtIfAutoMdixConfigGroup": cmExtIfAutoMdixConfigGroup,
       "cmExtIfMauTrafficGroup": cmExtIfMauTrafficGroup}
)

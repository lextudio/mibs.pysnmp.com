# SNMP MIB module (CISCO-IETF-ATM2-PVCTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-ATM2-PVCTRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:56 2024
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

(atmInterfaceConfEntry,
 atmVclVci,
 atmVclVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmInterfaceConfEntry",
    "atmVclVci",
    "atmVclVpi")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoIetfAtm2PvctrapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 29)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Atm2MIBObjects_ObjectIdentity = ObjectIdentity
atm2MIBObjects = _Atm2MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 1)
)
_AtmInterfaceExtTable_Object = MibTable
atmInterfaceExtTable = _AtmInterfaceExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14)
)
if mibBuilder.loadTexts:
    atmInterfaceExtTable.setStatus("current")
_AtmInterfaceExtEntry_Object = MibTableRow
atmInterfaceExtEntry = _AtmInterfaceExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14, 1)
)
if mibBuilder.loadTexts:
    atmInterfaceExtEntry.setStatus("current")
_AtmIntfPvcFailures_Type = Counter32
_AtmIntfPvcFailures_Object = MibTableColumn
atmIntfPvcFailures = _AtmIntfPvcFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14, 1, 20),
    _AtmIntfPvcFailures_Type()
)
atmIntfPvcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfPvcFailures.setStatus("current")
_AtmIntfCurrentlyFailingPVcls_Type = Gauge32
_AtmIntfCurrentlyFailingPVcls_Object = MibTableColumn
atmIntfCurrentlyFailingPVcls = _AtmIntfCurrentlyFailingPVcls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14, 1, 22),
    _AtmIntfCurrentlyFailingPVcls_Type()
)
atmIntfCurrentlyFailingPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfCurrentlyFailingPVcls.setStatus("current")


class _AtmIntfPvcFailuresTrapEnable_Type(TruthValue):
    """Custom type atmIntfPvcFailuresTrapEnable based on TruthValue"""


_AtmIntfPvcFailuresTrapEnable_Object = MibTableColumn
atmIntfPvcFailuresTrapEnable = _AtmIntfPvcFailuresTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14, 1, 23),
    _AtmIntfPvcFailuresTrapEnable_Type()
)
atmIntfPvcFailuresTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfPvcFailuresTrapEnable.setStatus("current")


class _AtmIntfPvcNotificationInterval_Type(Integer32):
    """Custom type atmIntfPvcNotificationInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AtmIntfPvcNotificationInterval_Type.__name__ = "Integer32"
_AtmIntfPvcNotificationInterval_Object = MibTableColumn
atmIntfPvcNotificationInterval = _AtmIntfPvcNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14, 1, 24),
    _AtmIntfPvcNotificationInterval_Type()
)
atmIntfPvcNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfPvcNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    atmIntfPvcNotificationInterval.setUnits("seconds")


class _AtmPreviouslyFailedPVclInterval_Type(Integer32):
    """Custom type atmPreviouslyFailedPVclInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AtmPreviouslyFailedPVclInterval_Type.__name__ = "Integer32"
_AtmPreviouslyFailedPVclInterval_Object = MibTableColumn
atmPreviouslyFailedPVclInterval = _AtmPreviouslyFailedPVclInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14, 1, 25),
    _AtmPreviouslyFailedPVclInterval_Type()
)
atmPreviouslyFailedPVclInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPreviouslyFailedPVclInterval.setStatus("current")
if mibBuilder.loadTexts:
    atmPreviouslyFailedPVclInterval.setUnits("seconds")
_AtmCurrentlyFailingPVclTable_Object = MibTable
atmCurrentlyFailingPVclTable = _AtmCurrentlyFailingPVclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 21)
)
if mibBuilder.loadTexts:
    atmCurrentlyFailingPVclTable.setStatus("current")
_AtmCurrentlyFailingPVclEntry_Object = MibTableRow
atmCurrentlyFailingPVclEntry = _AtmCurrentlyFailingPVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 21, 1)
)
atmCurrentlyFailingPVclEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    atmCurrentlyFailingPVclEntry.setStatus("current")
_AtmCurrentlyFailingPVclTimeStamp_Type = TimeStamp
_AtmCurrentlyFailingPVclTimeStamp_Object = MibTableColumn
atmCurrentlyFailingPVclTimeStamp = _AtmCurrentlyFailingPVclTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 21, 1, 1),
    _AtmCurrentlyFailingPVclTimeStamp_Type()
)
atmCurrentlyFailingPVclTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCurrentlyFailingPVclTimeStamp.setStatus("current")
_AtmPreviouslyFailedPVclTimeStamp_Type = TimeStamp
_AtmPreviouslyFailedPVclTimeStamp_Object = MibTableColumn
atmPreviouslyFailedPVclTimeStamp = _AtmPreviouslyFailedPVclTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 21, 1, 2),
    _AtmPreviouslyFailedPVclTimeStamp_Type()
)
atmPreviouslyFailedPVclTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPreviouslyFailedPVclTimeStamp.setStatus("current")
_Atm2MIBTraps_ObjectIdentity = ObjectIdentity
atm2MIBTraps = _Atm2MIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 2)
)
_AtmPvcTraps_ObjectIdentity = ObjectIdentity
atmPvcTraps = _AtmPvcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 2, 1)
)
_AtmPvcTrapsPrefix_ObjectIdentity = ObjectIdentity
atmPvcTrapsPrefix = _AtmPvcTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 2, 1, 0)
)
_Atm2MIBConformance_ObjectIdentity = ObjectIdentity
atm2MIBConformance = _Atm2MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 3)
)
_Atm2MIBGroups_ObjectIdentity = ObjectIdentity
atm2MIBGroups = _Atm2MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 3, 1)
)
_Atm2MIBCompliances_ObjectIdentity = ObjectIdentity
atm2MIBCompliances = _Atm2MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 3, 2)
)
atmInterfaceConfEntry.registerAugmentions(
    ("CISCO-IETF-ATM2-PVCTRAP-MIB",
     "atmInterfaceExtEntry")
)
atmInterfaceExtEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())

# Managed Objects groups

atmSwitchServcHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 3, 1, 1)
)
atmSwitchServcHostGroup.setObjects(
      *(("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfPvcFailures"),
        ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfCurrentlyFailingPVcls"),
        ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfPvcFailuresTrapEnable"),
        ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfPvcNotificationInterval"),
        ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmPreviouslyFailedPVclInterval"),
        ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmCurrentlyFailingPVclTimeStamp"),
        ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmPreviouslyFailedPVclTimeStamp"))
)
if mibBuilder.loadTexts:
    atmSwitchServcHostGroup.setStatus("current")


# Notification objects

atmIntfPvcFailuresTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 2, 1, 0, 1)
)
atmIntfPvcFailuresTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfPvcFailures"),
        ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfCurrentlyFailingPVcls"))
)
if mibBuilder.loadTexts:
    atmIntfPvcFailuresTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

atm2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 29, 3, 2, 1)
)
if mibBuilder.loadTexts:
    atm2MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-ATM2-PVCTRAP-MIB",
    **{"ciscoIetfAtm2PvctrapMIB": ciscoIetfAtm2PvctrapMIB,
       "atm2MIBObjects": atm2MIBObjects,
       "atmInterfaceExtTable": atmInterfaceExtTable,
       "atmInterfaceExtEntry": atmInterfaceExtEntry,
       "atmIntfPvcFailures": atmIntfPvcFailures,
       "atmIntfCurrentlyFailingPVcls": atmIntfCurrentlyFailingPVcls,
       "atmIntfPvcFailuresTrapEnable": atmIntfPvcFailuresTrapEnable,
       "atmIntfPvcNotificationInterval": atmIntfPvcNotificationInterval,
       "atmPreviouslyFailedPVclInterval": atmPreviouslyFailedPVclInterval,
       "atmCurrentlyFailingPVclTable": atmCurrentlyFailingPVclTable,
       "atmCurrentlyFailingPVclEntry": atmCurrentlyFailingPVclEntry,
       "atmCurrentlyFailingPVclTimeStamp": atmCurrentlyFailingPVclTimeStamp,
       "atmPreviouslyFailedPVclTimeStamp": atmPreviouslyFailedPVclTimeStamp,
       "atm2MIBTraps": atm2MIBTraps,
       "atmPvcTraps": atmPvcTraps,
       "atmPvcTrapsPrefix": atmPvcTrapsPrefix,
       "atmIntfPvcFailuresTrap": atmIntfPvcFailuresTrap,
       "atm2MIBConformance": atm2MIBConformance,
       "atm2MIBGroups": atm2MIBGroups,
       "atmSwitchServcHostGroup": atmSwitchServcHostGroup,
       "atm2MIBCompliances": atm2MIBCompliances,
       "atm2MIBCompliance": atm2MIBCompliance}
)

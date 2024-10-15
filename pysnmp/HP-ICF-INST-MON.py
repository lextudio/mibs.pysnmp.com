# SNMP MIB module (HP-ICF-INST-MON) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-INST-MON
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:32 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

hpicfInstMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35)
)
hpicfInstMonMIB.setRevisions(
        ("2008-12-04 00:00",
         "2006-01-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfInstMonObjects_ObjectIdentity = ObjectIdentity
hpicfInstMonObjects = _HpicfInstMonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1)
)


class _HpicfInstMonLogEnable_Type(TruthValue):
    """Custom type hpicfInstMonLogEnable based on TruthValue"""


_HpicfInstMonLogEnable_Object = MibScalar
hpicfInstMonLogEnable = _HpicfInstMonLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 1),
    _HpicfInstMonLogEnable_Type()
)
hpicfInstMonLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfInstMonLogEnable.setStatus("current")


class _HpicfInstMonTrapEnable_Type(TruthValue):
    """Custom type hpicfInstMonTrapEnable based on TruthValue"""


_HpicfInstMonTrapEnable_Object = MibScalar
hpicfInstMonTrapEnable = _HpicfInstMonTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 2),
    _HpicfInstMonTrapEnable_Type()
)
hpicfInstMonTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfInstMonTrapEnable.setStatus("current")
_HpicfInstMonParameterTable_Object = MibTable
hpicfInstMonParameterTable = _HpicfInstMonParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfInstMonParameterTable.setStatus("current")
_HpicfInstMonParameterEntry_Object = MibTableRow
hpicfInstMonParameterEntry = _HpicfInstMonParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 3, 1)
)
hpicfInstMonParameterEntry.setIndexNames(
    (0, "HP-ICF-INST-MON", "hpicfInstMonInterfaceIndex"),
    (0, "HP-ICF-INST-MON", "hpicfInstMonParameterIndex"),
)
if mibBuilder.loadTexts:
    hpicfInstMonParameterEntry.setStatus("current")
_HpicfInstMonInterfaceIndex_Type = InterfaceIndexOrZero
_HpicfInstMonInterfaceIndex_Object = MibTableColumn
hpicfInstMonInterfaceIndex = _HpicfInstMonInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 3, 1, 1),
    _HpicfInstMonInterfaceIndex_Type()
)
hpicfInstMonInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfInstMonInterfaceIndex.setStatus("current")


class _HpicfInstMonParameterIndex_Type(Integer32):
    """Custom type hpicfInstMonParameterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfInstMonParameterIndex_Type.__name__ = "Integer32"
_HpicfInstMonParameterIndex_Object = MibTableColumn
hpicfInstMonParameterIndex = _HpicfInstMonParameterIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 3, 1, 2),
    _HpicfInstMonParameterIndex_Type()
)
hpicfInstMonParameterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfInstMonParameterIndex.setStatus("current")


class _HpicfInstMonParameterName_Type(DisplayString):
    """Custom type hpicfInstMonParameterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HpicfInstMonParameterName_Type.__name__ = "DisplayString"
_HpicfInstMonParameterName_Object = MibTableColumn
hpicfInstMonParameterName = _HpicfInstMonParameterName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 3, 1, 3),
    _HpicfInstMonParameterName_Type()
)
hpicfInstMonParameterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfInstMonParameterName.setStatus("current")
_HpicfInstMonParameterThreshold_Type = Integer32
_HpicfInstMonParameterThreshold_Object = MibTableColumn
hpicfInstMonParameterThreshold = _HpicfInstMonParameterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 3, 1, 4),
    _HpicfInstMonParameterThreshold_Type()
)
hpicfInstMonParameterThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfInstMonParameterThreshold.setStatus("current")


class _HpicfInstMonNotificationText_Type(DisplayString):
    """Custom type hpicfInstMonNotificationText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfInstMonNotificationText_Type.__name__ = "DisplayString"
_HpicfInstMonNotificationText_Object = MibScalar
hpicfInstMonNotificationText = _HpicfInstMonNotificationText_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 4),
    _HpicfInstMonNotificationText_Type()
)
hpicfInstMonNotificationText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfInstMonNotificationText.setStatus("current")


class _HpicfInstConfig_Type(TruthValue):
    """Custom type hpicfInstConfig based on TruthValue"""


_HpicfInstConfig_Object = MibScalar
hpicfInstConfig = _HpicfInstConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 6),
    _HpicfInstConfig_Type()
)
hpicfInstConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfInstConfig.setStatus("current")
_HpicfInstMonConformance_ObjectIdentity = ObjectIdentity
hpicfInstMonConformance = _HpicfInstMonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2)
)
_HpicfInstMonGroups_ObjectIdentity = ObjectIdentity
hpicfInstMonGroups = _HpicfInstMonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2, 1)
)
_HpicfInstMonCompliances_ObjectIdentity = ObjectIdentity
hpicfInstMonCompliances = _HpicfInstMonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2, 2)
)

# Managed Objects groups

hpicfInstMonBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2, 1, 2)
)
hpicfInstMonBaseGroup.setObjects(
      *(("HP-ICF-INST-MON", "hpicfInstMonLogEnable"),
        ("HP-ICF-INST-MON", "hpicfInstMonTrapEnable"),
        ("HP-ICF-INST-MON", "hpicfInstMonParameterName"),
        ("HP-ICF-INST-MON", "hpicfInstMonParameterThreshold"))
)
if mibBuilder.loadTexts:
    hpicfInstMonBaseGroup.setStatus("current")

hpicfInstConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2, 1, 3)
)
hpicfInstConfigGroup.setObjects(
    ("HP-ICF-INST-MON", "hpicfInstConfig")
)
if mibBuilder.loadTexts:
    hpicfInstConfigGroup.setStatus("current")

hpicfInstMonNotifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2, 1, 4)
)
hpicfInstMonNotifyGroup.setObjects(
    ("HP-ICF-INST-MON", "hpicfInstMonNotificationText")
)
if mibBuilder.loadTexts:
    hpicfInstMonNotifyGroup.setStatus("current")


# Notification objects

hpicfInstMonNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 5)
)
hpicfInstMonNotification.setObjects(
    ("HP-ICF-INST-MON", "hpicfInstMonNotificationText")
)
if mibBuilder.loadTexts:
    hpicfInstMonNotification.setStatus(
        "current"
    )


# Notifications groups

hpicfInstMonNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2, 1, 1)
)
hpicfInstMonNotificationGroup.setObjects(
    ("HP-ICF-INST-MON", "hpicfInstMonNotification")
)
if mibBuilder.loadTexts:
    hpicfInstMonNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfInstMonBaseCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfInstMonBaseCompliance.setStatus(
        "current"
    )

hpicfInstConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfInstConfigCompliance.setStatus(
        "current"
    )

hpicfInstMonNotifyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfInstMonNotifyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-INST-MON",
    **{"hpicfInstMonMIB": hpicfInstMonMIB,
       "hpicfInstMonObjects": hpicfInstMonObjects,
       "hpicfInstMonLogEnable": hpicfInstMonLogEnable,
       "hpicfInstMonTrapEnable": hpicfInstMonTrapEnable,
       "hpicfInstMonParameterTable": hpicfInstMonParameterTable,
       "hpicfInstMonParameterEntry": hpicfInstMonParameterEntry,
       "hpicfInstMonInterfaceIndex": hpicfInstMonInterfaceIndex,
       "hpicfInstMonParameterIndex": hpicfInstMonParameterIndex,
       "hpicfInstMonParameterName": hpicfInstMonParameterName,
       "hpicfInstMonParameterThreshold": hpicfInstMonParameterThreshold,
       "hpicfInstMonNotificationText": hpicfInstMonNotificationText,
       "hpicfInstMonNotification": hpicfInstMonNotification,
       "hpicfInstConfig": hpicfInstConfig,
       "hpicfInstMonConformance": hpicfInstMonConformance,
       "hpicfInstMonGroups": hpicfInstMonGroups,
       "hpicfInstMonNotificationGroup": hpicfInstMonNotificationGroup,
       "hpicfInstMonBaseGroup": hpicfInstMonBaseGroup,
       "hpicfInstConfigGroup": hpicfInstConfigGroup,
       "hpicfInstMonNotifyGroup": hpicfInstMonNotifyGroup,
       "hpicfInstMonCompliances": hpicfInstMonCompliances,
       "hpicfInstMonBaseCompliance": hpicfInstMonBaseCompliance,
       "hpicfInstConfigCompliance": hpicfInstConfigCompliance,
       "hpicfInstMonNotifyCompliance": hpicfInstMonNotifyCompliance}
)

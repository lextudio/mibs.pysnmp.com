# SNMP MIB module (VPLS-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VPLS-LDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:12 2024
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

(pwID,
 pwIndex) = mibBuilder.importSymbols(
    "PW-STD-MIB",
    "pwID",
    "pwIndex")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(vplsConfigIndex,
 vplsConfigName) = mibBuilder.importSymbols(
    "VPLS-GENERIC-MIB",
    "vplsConfigIndex",
    "vplsConfigName")


# MODULE-IDENTITY

vplsLdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 275)
)
vplsLdpMIB.setRevisions(
        ("2014-05-19 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VplsLdpNotifications_ObjectIdentity = ObjectIdentity
vplsLdpNotifications = _VplsLdpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 275, 0)
)
_VplsLdpObjects_ObjectIdentity = ObjectIdentity
vplsLdpObjects = _VplsLdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 275, 1)
)
_VplsLdpConfigTable_Object = MibTable
vplsLdpConfigTable = _VplsLdpConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 275, 1, 1)
)
if mibBuilder.loadTexts:
    vplsLdpConfigTable.setStatus("current")
_VplsLdpConfigEntry_Object = MibTableRow
vplsLdpConfigEntry = _VplsLdpConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 275, 1, 1, 1)
)
vplsLdpConfigEntry.setIndexNames(
    (0, "VPLS-GENERIC-MIB", "vplsConfigIndex"),
)
if mibBuilder.loadTexts:
    vplsLdpConfigEntry.setStatus("current")


class _VplsLdpConfigMacAddrWithdraw_Type(TruthValue):
    """Custom type vplsLdpConfigMacAddrWithdraw based on TruthValue"""


_VplsLdpConfigMacAddrWithdraw_Object = MibTableColumn
vplsLdpConfigMacAddrWithdraw = _VplsLdpConfigMacAddrWithdraw_Object(
    (1, 3, 6, 1, 2, 1, 10, 275, 1, 1, 1, 1),
    _VplsLdpConfigMacAddrWithdraw_Type()
)
vplsLdpConfigMacAddrWithdraw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vplsLdpConfigMacAddrWithdraw.setStatus("current")
_VplsLdpPwBindTable_Object = MibTable
vplsLdpPwBindTable = _VplsLdpPwBindTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 275, 1, 2)
)
if mibBuilder.loadTexts:
    vplsLdpPwBindTable.setStatus("current")
_VplsLdpPwBindEntry_Object = MibTableRow
vplsLdpPwBindEntry = _VplsLdpPwBindEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 275, 1, 2, 1)
)
vplsLdpPwBindEntry.setIndexNames(
    (0, "VPLS-GENERIC-MIB", "vplsConfigIndex"),
    (0, "PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    vplsLdpPwBindEntry.setStatus("current")


class _VplsLdpPwBindMacAddressLimit_Type(Unsigned32):
    """Custom type vplsLdpPwBindMacAddressLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VplsLdpPwBindMacAddressLimit_Type.__name__ = "Unsigned32"
_VplsLdpPwBindMacAddressLimit_Object = MibTableColumn
vplsLdpPwBindMacAddressLimit = _VplsLdpPwBindMacAddressLimit_Object(
    (1, 3, 6, 1, 2, 1, 10, 275, 1, 2, 1, 1),
    _VplsLdpPwBindMacAddressLimit_Type()
)
vplsLdpPwBindMacAddressLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vplsLdpPwBindMacAddressLimit.setStatus("current")
_VplsLdpConformance_ObjectIdentity = ObjectIdentity
vplsLdpConformance = _VplsLdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 275, 2)
)
_VplsLdpCompliances_ObjectIdentity = ObjectIdentity
vplsLdpCompliances = _VplsLdpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 275, 2, 1)
)
_VplsLdpGroups_ObjectIdentity = ObjectIdentity
vplsLdpGroups = _VplsLdpGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 275, 2, 2)
)

# Managed Objects groups

vplsLdpGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 275, 2, 2, 1)
)
vplsLdpGroup.setObjects(
      *(("VPLS-LDP-MIB", "vplsLdpConfigMacAddrWithdraw"),
        ("VPLS-LDP-MIB", "vplsLdpPwBindMacAddressLimit"))
)
if mibBuilder.loadTexts:
    vplsLdpGroup.setStatus("current")


# Notification objects

vplsLdpPwBindMacTableFull = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 275, 0, 1)
)
vplsLdpPwBindMacTableFull.setObjects(
      *(("VPLS-GENERIC-MIB", "vplsConfigName"),
        ("PW-STD-MIB", "pwID"))
)
if mibBuilder.loadTexts:
    vplsLdpPwBindMacTableFull.setStatus(
        "current"
    )


# Notifications groups

vplsLdpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 275, 2, 2, 2)
)
vplsLdpNotificationGroup.setObjects(
    ("VPLS-LDP-MIB", "vplsLdpPwBindMacTableFull")
)
if mibBuilder.loadTexts:
    vplsLdpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vplsLdpModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 275, 2, 1, 1)
)
if mibBuilder.loadTexts:
    vplsLdpModuleFullCompliance.setStatus(
        "current"
    )

vplsLdpModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 275, 2, 1, 2)
)
if mibBuilder.loadTexts:
    vplsLdpModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VPLS-LDP-MIB",
    **{"vplsLdpMIB": vplsLdpMIB,
       "vplsLdpNotifications": vplsLdpNotifications,
       "vplsLdpPwBindMacTableFull": vplsLdpPwBindMacTableFull,
       "vplsLdpObjects": vplsLdpObjects,
       "vplsLdpConfigTable": vplsLdpConfigTable,
       "vplsLdpConfigEntry": vplsLdpConfigEntry,
       "vplsLdpConfigMacAddrWithdraw": vplsLdpConfigMacAddrWithdraw,
       "vplsLdpPwBindTable": vplsLdpPwBindTable,
       "vplsLdpPwBindEntry": vplsLdpPwBindEntry,
       "vplsLdpPwBindMacAddressLimit": vplsLdpPwBindMacAddressLimit,
       "vplsLdpConformance": vplsLdpConformance,
       "vplsLdpCompliances": vplsLdpCompliances,
       "vplsLdpModuleFullCompliance": vplsLdpModuleFullCompliance,
       "vplsLdpModuleReadOnlyCompliance": vplsLdpModuleReadOnlyCompliance,
       "vplsLdpGroups": vplsLdpGroups,
       "vplsLdpGroup": vplsLdpGroup,
       "vplsLdpNotificationGroup": vplsLdpNotificationGroup}
)

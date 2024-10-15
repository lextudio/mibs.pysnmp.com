# SNMP MIB module (ZYXEL-IGMP-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-IGMP-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:00 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelIgmpFilter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 30)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelIgmpFilteringSetup_ObjectIdentity = ObjectIdentity
zyxelIgmpFilteringSetup = _ZyxelIgmpFilteringSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 30, 1)
)
_ZyIgmpFilteringState_Type = EnabledStatus
_ZyIgmpFilteringState_Object = MibScalar
zyIgmpFilteringState = _ZyIgmpFilteringState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 30, 1, 1),
    _ZyIgmpFilteringState_Type()
)
zyIgmpFilteringState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpFilteringState.setStatus("current")
_ZyIgmpFilteringMaxNumberOfProfiles_Type = Integer32
_ZyIgmpFilteringMaxNumberOfProfiles_Object = MibScalar
zyIgmpFilteringMaxNumberOfProfiles = _ZyIgmpFilteringMaxNumberOfProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 30, 1, 2),
    _ZyIgmpFilteringMaxNumberOfProfiles_Type()
)
zyIgmpFilteringMaxNumberOfProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpFilteringMaxNumberOfProfiles.setStatus("current")
_ZyxelIgmpFilteringProfileTable_Object = MibTable
zyxelIgmpFilteringProfileTable = _ZyxelIgmpFilteringProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 30, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelIgmpFilteringProfileTable.setStatus("current")
_ZyxelIgmpFilteringProfileEntry_Object = MibTableRow
zyxelIgmpFilteringProfileEntry = _ZyxelIgmpFilteringProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 30, 1, 3, 1)
)
zyxelIgmpFilteringProfileEntry.setIndexNames(
    (0, "ZYXEL-IGMP-FILTER-MIB", "zyIgmpFilteringProfileName"),
    (0, "ZYXEL-IGMP-FILTER-MIB", "zyIgmpFilteringProfileStartIpAddress"),
    (0, "ZYXEL-IGMP-FILTER-MIB", "zyIgmpFilteringProfileEndIpAddress"),
)
if mibBuilder.loadTexts:
    zyxelIgmpFilteringProfileEntry.setStatus("current")
_ZyIgmpFilteringProfileName_Type = DisplayString
_ZyIgmpFilteringProfileName_Object = MibTableColumn
zyIgmpFilteringProfileName = _ZyIgmpFilteringProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 30, 1, 3, 1, 1),
    _ZyIgmpFilteringProfileName_Type()
)
zyIgmpFilteringProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIgmpFilteringProfileName.setStatus("current")
_ZyIgmpFilteringProfileStartIpAddress_Type = IpAddress
_ZyIgmpFilteringProfileStartIpAddress_Object = MibTableColumn
zyIgmpFilteringProfileStartIpAddress = _ZyIgmpFilteringProfileStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 30, 1, 3, 1, 2),
    _ZyIgmpFilteringProfileStartIpAddress_Type()
)
zyIgmpFilteringProfileStartIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIgmpFilteringProfileStartIpAddress.setStatus("current")
_ZyIgmpFilteringProfileEndIpAddress_Type = IpAddress
_ZyIgmpFilteringProfileEndIpAddress_Object = MibTableColumn
zyIgmpFilteringProfileEndIpAddress = _ZyIgmpFilteringProfileEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 30, 1, 3, 1, 3),
    _ZyIgmpFilteringProfileEndIpAddress_Type()
)
zyIgmpFilteringProfileEndIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIgmpFilteringProfileEndIpAddress.setStatus("current")
_ZyIgmpFilteringProfileRowStatus_Type = RowStatus
_ZyIgmpFilteringProfileRowStatus_Object = MibTableColumn
zyIgmpFilteringProfileRowStatus = _ZyIgmpFilteringProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 30, 1, 3, 1, 4),
    _ZyIgmpFilteringProfileRowStatus_Type()
)
zyIgmpFilteringProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyIgmpFilteringProfileRowStatus.setStatus("current")
_ZyxelIgmpFilteringPortTable_Object = MibTable
zyxelIgmpFilteringPortTable = _ZyxelIgmpFilteringPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 30, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelIgmpFilteringPortTable.setStatus("current")
_ZyxelIgmpFilteringPortEntry_Object = MibTableRow
zyxelIgmpFilteringPortEntry = _ZyxelIgmpFilteringPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 30, 1, 4, 1)
)
zyxelIgmpFilteringPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelIgmpFilteringPortEntry.setStatus("current")
_ZyIgmpFilteringPortProfile_Type = DisplayString
_ZyIgmpFilteringPortProfile_Object = MibTableColumn
zyIgmpFilteringPortProfile = _ZyIgmpFilteringPortProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 30, 1, 4, 1, 1),
    _ZyIgmpFilteringPortProfile_Type()
)
zyIgmpFilteringPortProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpFilteringPortProfile.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-IGMP-FILTER-MIB",
    **{"zyxelIgmpFilter": zyxelIgmpFilter,
       "zyxelIgmpFilteringSetup": zyxelIgmpFilteringSetup,
       "zyIgmpFilteringState": zyIgmpFilteringState,
       "zyIgmpFilteringMaxNumberOfProfiles": zyIgmpFilteringMaxNumberOfProfiles,
       "zyxelIgmpFilteringProfileTable": zyxelIgmpFilteringProfileTable,
       "zyxelIgmpFilteringProfileEntry": zyxelIgmpFilteringProfileEntry,
       "zyIgmpFilteringProfileName": zyIgmpFilteringProfileName,
       "zyIgmpFilteringProfileStartIpAddress": zyIgmpFilteringProfileStartIpAddress,
       "zyIgmpFilteringProfileEndIpAddress": zyIgmpFilteringProfileEndIpAddress,
       "zyIgmpFilteringProfileRowStatus": zyIgmpFilteringProfileRowStatus,
       "zyxelIgmpFilteringPortTable": zyxelIgmpFilteringPortTable,
       "zyxelIgmpFilteringPortEntry": zyxelIgmpFilteringPortEntry,
       "zyIgmpFilteringPortProfile": zyIgmpFilteringPortProfile}
)

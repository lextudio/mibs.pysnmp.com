# SNMP MIB module (ZYXEL-DHCP-OPTION82-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-DHCP-OPTION82-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:32 2024
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

zyxelDhcpOption82Profile = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 17)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelDhcpOption82ProfileSetup_ObjectIdentity = ObjectIdentity
zyxelDhcpOption82ProfileSetup = _ZyxelDhcpOption82ProfileSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 17, 1)
)
_ZyDhcpOption82ProfileMaxNumberOfProfiles_Type = Integer32
_ZyDhcpOption82ProfileMaxNumberOfProfiles_Object = MibScalar
zyDhcpOption82ProfileMaxNumberOfProfiles = _ZyDhcpOption82ProfileMaxNumberOfProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 17, 1, 1),
    _ZyDhcpOption82ProfileMaxNumberOfProfiles_Type()
)
zyDhcpOption82ProfileMaxNumberOfProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpOption82ProfileMaxNumberOfProfiles.setStatus("current")
_ZyxelDhcpOption82ProfileTable_Object = MibTable
zyxelDhcpOption82ProfileTable = _ZyxelDhcpOption82ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 17, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelDhcpOption82ProfileTable.setStatus("current")
_ZyxelDhcpOption82ProfileEntry_Object = MibTableRow
zyxelDhcpOption82ProfileEntry = _ZyxelDhcpOption82ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 17, 1, 2, 1)
)
zyxelDhcpOption82ProfileEntry.setIndexNames(
    (0, "ZYXEL-DHCP-OPTION82-PROFILE-MIB", "zyDhcpOption82ProfileName"),
)
if mibBuilder.loadTexts:
    zyxelDhcpOption82ProfileEntry.setStatus("current")
_ZyDhcpOption82ProfileName_Type = DisplayString
_ZyDhcpOption82ProfileName_Object = MibTableColumn
zyDhcpOption82ProfileName = _ZyDhcpOption82ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 17, 1, 2, 1, 1),
    _ZyDhcpOption82ProfileName_Type()
)
zyDhcpOption82ProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyDhcpOption82ProfileName.setStatus("current")
_ZyDhcpOption82ProfileCircuitIdState_Type = EnabledStatus
_ZyDhcpOption82ProfileCircuitIdState_Object = MibTableColumn
zyDhcpOption82ProfileCircuitIdState = _ZyDhcpOption82ProfileCircuitIdState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 17, 1, 2, 1, 2),
    _ZyDhcpOption82ProfileCircuitIdState_Type()
)
zyDhcpOption82ProfileCircuitIdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpOption82ProfileCircuitIdState.setStatus("current")
_ZyDhcpOption82ProfileCircuitIdSlotPortState_Type = EnabledStatus
_ZyDhcpOption82ProfileCircuitIdSlotPortState_Object = MibTableColumn
zyDhcpOption82ProfileCircuitIdSlotPortState = _ZyDhcpOption82ProfileCircuitIdSlotPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 17, 1, 2, 1, 3),
    _ZyDhcpOption82ProfileCircuitIdSlotPortState_Type()
)
zyDhcpOption82ProfileCircuitIdSlotPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpOption82ProfileCircuitIdSlotPortState.setStatus("current")
_ZyDhcpOption82ProfileCircuitIdVidState_Type = EnabledStatus
_ZyDhcpOption82ProfileCircuitIdVidState_Object = MibTableColumn
zyDhcpOption82ProfileCircuitIdVidState = _ZyDhcpOption82ProfileCircuitIdVidState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 17, 1, 2, 1, 4),
    _ZyDhcpOption82ProfileCircuitIdVidState_Type()
)
zyDhcpOption82ProfileCircuitIdVidState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpOption82ProfileCircuitIdVidState.setStatus("current")
_ZyDhcpOption82ProfileCircuitIdHostnameState_Type = EnabledStatus
_ZyDhcpOption82ProfileCircuitIdHostnameState_Object = MibTableColumn
zyDhcpOption82ProfileCircuitIdHostnameState = _ZyDhcpOption82ProfileCircuitIdHostnameState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 17, 1, 2, 1, 5),
    _ZyDhcpOption82ProfileCircuitIdHostnameState_Type()
)
zyDhcpOption82ProfileCircuitIdHostnameState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpOption82ProfileCircuitIdHostnameState.setStatus("current")
_ZyDhcpOption82ProfileCircuitIdString_Type = DisplayString
_ZyDhcpOption82ProfileCircuitIdString_Object = MibTableColumn
zyDhcpOption82ProfileCircuitIdString = _ZyDhcpOption82ProfileCircuitIdString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 17, 1, 2, 1, 6),
    _ZyDhcpOption82ProfileCircuitIdString_Type()
)
zyDhcpOption82ProfileCircuitIdString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpOption82ProfileCircuitIdString.setStatus("current")
_ZyDhcpOption82ProfileRemoteIdState_Type = EnabledStatus
_ZyDhcpOption82ProfileRemoteIdState_Object = MibTableColumn
zyDhcpOption82ProfileRemoteIdState = _ZyDhcpOption82ProfileRemoteIdState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 17, 1, 2, 1, 7),
    _ZyDhcpOption82ProfileRemoteIdState_Type()
)
zyDhcpOption82ProfileRemoteIdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpOption82ProfileRemoteIdState.setStatus("current")
_ZyDhcpOption82ProfileRemoteIdMacAddressState_Type = EnabledStatus
_ZyDhcpOption82ProfileRemoteIdMacAddressState_Object = MibTableColumn
zyDhcpOption82ProfileRemoteIdMacAddressState = _ZyDhcpOption82ProfileRemoteIdMacAddressState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 17, 1, 2, 1, 8),
    _ZyDhcpOption82ProfileRemoteIdMacAddressState_Type()
)
zyDhcpOption82ProfileRemoteIdMacAddressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpOption82ProfileRemoteIdMacAddressState.setStatus("current")
_ZyDhcpOption82ProfileRemoteIdString_Type = DisplayString
_ZyDhcpOption82ProfileRemoteIdString_Object = MibTableColumn
zyDhcpOption82ProfileRemoteIdString = _ZyDhcpOption82ProfileRemoteIdString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 17, 1, 2, 1, 9),
    _ZyDhcpOption82ProfileRemoteIdString_Type()
)
zyDhcpOption82ProfileRemoteIdString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpOption82ProfileRemoteIdString.setStatus("current")
_ZyDhcpOption82ProfileRowstatus_Type = RowStatus
_ZyDhcpOption82ProfileRowstatus_Object = MibTableColumn
zyDhcpOption82ProfileRowstatus = _ZyDhcpOption82ProfileRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 17, 1, 2, 1, 10),
    _ZyDhcpOption82ProfileRowstatus_Type()
)
zyDhcpOption82ProfileRowstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpOption82ProfileRowstatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-DHCP-OPTION82-PROFILE-MIB",
    **{"zyxelDhcpOption82Profile": zyxelDhcpOption82Profile,
       "zyxelDhcpOption82ProfileSetup": zyxelDhcpOption82ProfileSetup,
       "zyDhcpOption82ProfileMaxNumberOfProfiles": zyDhcpOption82ProfileMaxNumberOfProfiles,
       "zyxelDhcpOption82ProfileTable": zyxelDhcpOption82ProfileTable,
       "zyxelDhcpOption82ProfileEntry": zyxelDhcpOption82ProfileEntry,
       "zyDhcpOption82ProfileName": zyDhcpOption82ProfileName,
       "zyDhcpOption82ProfileCircuitIdState": zyDhcpOption82ProfileCircuitIdState,
       "zyDhcpOption82ProfileCircuitIdSlotPortState": zyDhcpOption82ProfileCircuitIdSlotPortState,
       "zyDhcpOption82ProfileCircuitIdVidState": zyDhcpOption82ProfileCircuitIdVidState,
       "zyDhcpOption82ProfileCircuitIdHostnameState": zyDhcpOption82ProfileCircuitIdHostnameState,
       "zyDhcpOption82ProfileCircuitIdString": zyDhcpOption82ProfileCircuitIdString,
       "zyDhcpOption82ProfileRemoteIdState": zyDhcpOption82ProfileRemoteIdState,
       "zyDhcpOption82ProfileRemoteIdMacAddressState": zyDhcpOption82ProfileRemoteIdMacAddressState,
       "zyDhcpOption82ProfileRemoteIdString": zyDhcpOption82ProfileRemoteIdString,
       "zyDhcpOption82ProfileRowstatus": zyDhcpOption82ProfileRowstatus}
)

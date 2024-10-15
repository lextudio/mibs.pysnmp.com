# SNMP MIB module (Gadzoox-1-Control-FIle) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Gadzoox-1-Control-FIle
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:32 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gadzoox_ObjectIdentity = ObjectIdentity
gadzoox = _Gadzoox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754)
)
_NetMgmt_Type = Integer32
_NetMgmt_Object = MibScalar
netMgmt = _NetMgmt_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1),
    _NetMgmt_Type()
)
netMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMgmt.setStatus("mandatory")
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1)
)
_Zoning_ObjectIdentity = ObjectIdentity
zoning = _Zoning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3)
)
_NlPendingZoneTable_Type = Integer32
_NlPendingZoneTable_Object = MibScalar
nlPendingZoneTable = _NlPendingZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 7),
    _NlPendingZoneTable_Type()
)
nlPendingZoneTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlPendingZoneTable.setStatus("mandatory")
_NlPendingZoneMemberTable_Type = Integer32
_NlPendingZoneMemberTable_Object = MibScalar
nlPendingZoneMemberTable = _NlPendingZoneMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 9),
    _NlPendingZoneMemberTable_Type()
)
nlPendingZoneMemberTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlPendingZoneMemberTable.setStatus("mandatory")
_NlActiveZoneTable_Type = Integer32
_NlActiveZoneTable_Object = MibScalar
nlActiveZoneTable = _NlActiveZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 11),
    _NlActiveZoneTable_Type()
)
nlActiveZoneTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlActiveZoneTable.setStatus("mandatory")
_NlActiveZoneMemberTable_Type = Integer32
_NlActiveZoneMemberTable_Object = MibScalar
nlActiveZoneMemberTable = _NlActiveZoneMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 13),
    _NlActiveZoneMemberTable_Type()
)
nlActiveZoneMemberTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlActiveZoneMemberTable.setStatus("mandatory")
_Download_ObjectIdentity = ObjectIdentity
download = _Download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 3)
)
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 4)
)
_Discovery_ObjectIdentity = ObjectIdentity
discovery = _Discovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 5)
)
_Monitor_ObjectIdentity = ObjectIdentity
monitor = _Monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 6)
)
_Proxy_ObjectIdentity = ObjectIdentity
proxy = _Proxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7)
)
_DeviceTable_Type = Integer32
_DeviceTable_Object = MibScalar
deviceTable = _DeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9),
    _DeviceTable_Type()
)
deviceTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTable.setStatus("mandatory")
_Policy_ObjectIdentity = ObjectIdentity
policy = _Policy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 11)
)
_Gbic_ObjectIdentity = ObjectIdentity
gbic = _Gbic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 8)
)
_GbicTable_Type = Integer32
_GbicTable_Object = MibScalar
gbicTable = _GbicTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 1, 8, 1),
    _GbicTable_Type()
)
gbicTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbicTable.setStatus("mandatory")
_Hub_ObjectIdentity = ObjectIdentity
hub = _Hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 2)
)
_AreaSwitch_ObjectIdentity = ObjectIdentity
areaSwitch = _AreaSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 3)
)
_ChannelAgent_ObjectIdentity = ObjectIdentity
channelAgent = _ChannelAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 4)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 5)
)
_TrapIPaddrTable_Type = Integer32
_TrapIPaddrTable_Object = MibScalar
trapIPaddrTable = _TrapIPaddrTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 5, 1),
    _TrapIPaddrTable_Type()
)
trapIPaddrTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIPaddrTable.setStatus("mandatory")
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6)
)
_CapChas_ObjectIdentity = ObjectIdentity
capChas = _CapChas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1)
)
_CapChasTable_Type = Integer32
_CapChasTable_Object = MibScalar
capChasTable = _CapChasTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1),
    _CapChasTable_Type()
)
capChasTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChasTable.setStatus("mandatory")
_CapChasSlotTable_Type = Integer32
_CapChasSlotTable_Object = MibScalar
capChasSlotTable = _CapChasSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 2),
    _CapChasSlotTable_Type()
)
capChasSlotTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capChasSlotTable.setStatus("mandatory")
_CapPim_ObjectIdentity = ObjectIdentity
capPim = _CapPim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2)
)
_CapPimTable_Type = Integer32
_CapPimTable_Object = MibScalar
capPimTable = _CapPimTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 1),
    _CapPimTable_Type()
)
capPimTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capPimTable.setStatus("mandatory")
_CapPortTable_Type = Integer32
_CapPortTable_Object = MibScalar
capPortTable = _CapPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2),
    _CapPortTable_Type()
)
capPortTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capPortTable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Gadzoox-1-Control-FIle",
    **{"gadzoox": gadzoox,
       "netMgmt": netMgmt,
       "common": common,
       "system": system,
       "zoning": zoning,
       "nlPendingZoneTable": nlPendingZoneTable,
       "nlPendingZoneMemberTable": nlPendingZoneMemberTable,
       "nlActiveZoneTable": nlActiveZoneTable,
       "nlActiveZoneMemberTable": nlActiveZoneMemberTable,
       "download": download,
       "security": security,
       "discovery": discovery,
       "monitor": monitor,
       "proxy": proxy,
       "deviceTable": deviceTable,
       "policy": policy,
       "gbic": gbic,
       "gbicTable": gbicTable,
       "hub": hub,
       "areaSwitch": areaSwitch,
       "channelAgent": channelAgent,
       "traps": traps,
       "trapIPaddrTable": trapIPaddrTable,
       "switch": switch,
       "capChas": capChas,
       "capChasTable": capChasTable,
       "capChasSlotTable": capChasSlotTable,
       "capPim": capPim,
       "capPimTable": capPimTable,
       "capPortTable": capPortTable}
)

# SNMP MIB module (WOLLONGONG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WOLLONGONG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:19 2024
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

_Wollongong_ObjectIdentity = ObjectIdentity
wollongong = _Wollongong_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6)
)
_Model_ObjectIdentity = ObjectIdentity
model = _Model_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6, 1)
)
_Vms4_ObjectIdentity = ObjectIdentity
vms4 = _Vms4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6, 1, 1)
)
_Vms5_ObjectIdentity = ObjectIdentity
vms5 = _Vms5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6, 1, 2)
)
_Sun3_ObjectIdentity = ObjectIdentity
sun3 = _Sun3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6, 1, 3)
)
_SysV386_ObjectIdentity = ObjectIdentity
sysV386 = _SysV386_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6, 1, 4)
)
_Att3B2_ObjectIdentity = ObjectIdentity
att3B2 = _Att3B2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6, 1, 5)
)
_Ncr_ObjectIdentity = ObjectIdentity
ncr = _Ncr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6, 1, 6)
)
_Dos_ObjectIdentity = ObjectIdentity
dos = _Dos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6, 1, 7)
)
_Dostcp_ObjectIdentity = ObjectIdentity
dostcp = _Dostcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6, 1, 7, 1)
)
_Dosroute_ObjectIdentity = ObjectIdentity
dosroute = _Dosroute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6, 1, 7, 2)
)
_Dosruntime_ObjectIdentity = ObjectIdentity
dosruntime = _Dosruntime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6, 1, 7, 3)
)
_Os2_ObjectIdentity = ObjectIdentity
os2 = _Os2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6, 1, 8)
)
_Mac_ObjectIdentity = ObjectIdentity
mac = _Mac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6, 1, 9)
)
_Proxy_ObjectIdentity = ObjectIdentity
proxy = _Proxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6, 2)
)
_LANbridgeTab_Object = MibTable
lANbridgeTab = _LANbridgeTab_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    lANbridgeTab.setStatus("optional")
_LANbridgeEnt_Object = MibTableRow
lANbridgeEnt = _LANbridgeEnt_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lANbridgeEnt.setStatus("optional")
_TwgLBUpTime_Type = TimeTicks
_TwgLBUpTime_Object = MibTableColumn
twgLBUpTime = _TwgLBUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 1),
    _TwgLBUpTime_Type()
)
twgLBUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twgLBUpTime.setStatus("optional")
_TwgLBNeigh1_Type = OctetString
_TwgLBNeigh1_Object = MibTableColumn
twgLBNeigh1 = _TwgLBNeigh1_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 2),
    _TwgLBNeigh1_Type()
)
twgLBNeigh1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twgLBNeigh1.setStatus("optional")
_TwgLBNeigh2_Type = OctetString
_TwgLBNeigh2_Object = MibTableColumn
twgLBNeigh2 = _TwgLBNeigh2_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 3),
    _TwgLBNeigh2_Type()
)
twgLBNeigh2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twgLBNeigh2.setStatus("optional")
_TwgLBInFrames1_Type = Counter32
_TwgLBInFrames1_Object = MibTableColumn
twgLBInFrames1 = _TwgLBInFrames1_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 4),
    _TwgLBInFrames1_Type()
)
twgLBInFrames1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twgLBInFrames1.setStatus("optional")
_TwgLBInFrames2_Type = Counter32
_TwgLBInFrames2_Object = MibTableColumn
twgLBInFrames2 = _TwgLBInFrames2_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 5),
    _TwgLBInFrames2_Type()
)
twgLBInFrames2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twgLBInFrames2.setStatus("optional")
_TwgLBOutFrames1_Type = Counter32
_TwgLBOutFrames1_Object = MibTableColumn
twgLBOutFrames1 = _TwgLBOutFrames1_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 6),
    _TwgLBOutFrames1_Type()
)
twgLBOutFrames1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twgLBOutFrames1.setStatus("optional")
_TwgLBOutFrames2_Type = Counter32
_TwgLBOutFrames2_Object = MibTableColumn
twgLBOutFrames2 = _TwgLBOutFrames2_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 7),
    _TwgLBOutFrames2_Type()
)
twgLBOutFrames2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twgLBOutFrames2.setStatus("optional")
_TwgLBBadFrames1_Type = Counter32
_TwgLBBadFrames1_Object = MibTableColumn
twgLBBadFrames1 = _TwgLBBadFrames1_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 8),
    _TwgLBBadFrames1_Type()
)
twgLBBadFrames1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twgLBBadFrames1.setStatus("optional")
_TwgLBBadFrames2_Type = Counter32
_TwgLBBadFrames2_Object = MibTableColumn
twgLBBadFrames2 = _TwgLBBadFrames2_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 9),
    _TwgLBBadFrames2_Type()
)
twgLBBadFrames2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twgLBBadFrames2.setStatus("optional")
_TwgLBCollisions_Type = Counter32
_TwgLBCollisions_Object = MibTableColumn
twgLBCollisions = _TwgLBCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 10),
    _TwgLBCollisions_Type()
)
twgLBCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twgLBCollisions.setStatus("optional")
_TwgLBInOwnFrames1_Type = Counter32
_TwgLBInOwnFrames1_Object = MibTableColumn
twgLBInOwnFrames1 = _TwgLBInOwnFrames1_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 11),
    _TwgLBInOwnFrames1_Type()
)
twgLBInOwnFrames1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twgLBInOwnFrames1.setStatus("optional")
_TwgLBInOwnFrames2_Type = Counter32
_TwgLBInOwnFrames2_Object = MibTableColumn
twgLBInOwnFrames2 = _TwgLBInOwnFrames2_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 12),
    _TwgLBInOwnFrames2_Type()
)
twgLBInOwnFrames2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twgLBInOwnFrames2.setStatus("optional")
_TwgLBOutOwnFrames1_Type = Counter32
_TwgLBOutOwnFrames1_Object = MibTableColumn
twgLBOutOwnFrames1 = _TwgLBOutOwnFrames1_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 13),
    _TwgLBOutOwnFrames1_Type()
)
twgLBOutOwnFrames1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twgLBOutOwnFrames1.setStatus("optional")
_TwgLBOutOwnFrames2_Type = Counter32
_TwgLBOutOwnFrames2_Object = MibTableColumn
twgLBOutOwnFrames2 = _TwgLBOutOwnFrames2_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 14),
    _TwgLBOutOwnFrames2_Type()
)
twgLBOutOwnFrames2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twgLBOutOwnFrames2.setStatus("optional")
_TwgLBReboot_Type = Integer32
_TwgLBReboot_Object = MibTableColumn
twgLBReboot = _TwgLBReboot_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 15),
    _TwgLBReboot_Type()
)
twgLBReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    twgLBReboot.setStatus("optional")
_TwgLBStatus_Type = Integer32
_TwgLBStatus_Object = MibTableColumn
twgLBStatus = _TwgLBStatus_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 16),
    _TwgLBStatus_Type()
)
twgLBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twgLBStatus.setStatus("optional")
_TwgLBState1_Type = Integer32
_TwgLBState1_Object = MibTableColumn
twgLBState1 = _TwgLBState1_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 17),
    _TwgLBState1_Type()
)
twgLBState1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twgLBState1.setStatus("optional")
_TwgLBState2_Type = Integer32
_TwgLBState2_Object = MibTableColumn
twgLBState2 = _TwgLBState2_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 18),
    _TwgLBState2_Type()
)
twgLBState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twgLBState2.setStatus("optional")
_TwgLBAddr1_Type = OctetString
_TwgLBAddr1_Object = MibTableColumn
twgLBAddr1 = _TwgLBAddr1_Object(
    (1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 19),
    _TwgLBAddr1_Type()
)
twgLBAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twgLBAddr1.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WOLLONGONG-MIB",
    **{"wollongong": wollongong,
       "model": model,
       "vms4": vms4,
       "vms5": vms5,
       "sun3": sun3,
       "sysV386": sysV386,
       "att3B2": att3B2,
       "ncr": ncr,
       "dos": dos,
       "dostcp": dostcp,
       "dosroute": dosroute,
       "dosruntime": dosruntime,
       "os2": os2,
       "mac": mac,
       "proxy": proxy,
       "lANbridgeTab": lANbridgeTab,
       "lANbridgeEnt": lANbridgeEnt,
       "twgLBUpTime": twgLBUpTime,
       "twgLBNeigh1": twgLBNeigh1,
       "twgLBNeigh2": twgLBNeigh2,
       "twgLBInFrames1": twgLBInFrames1,
       "twgLBInFrames2": twgLBInFrames2,
       "twgLBOutFrames1": twgLBOutFrames1,
       "twgLBOutFrames2": twgLBOutFrames2,
       "twgLBBadFrames1": twgLBBadFrames1,
       "twgLBBadFrames2": twgLBBadFrames2,
       "twgLBCollisions": twgLBCollisions,
       "twgLBInOwnFrames1": twgLBInOwnFrames1,
       "twgLBInOwnFrames2": twgLBInOwnFrames2,
       "twgLBOutOwnFrames1": twgLBOutOwnFrames1,
       "twgLBOutOwnFrames2": twgLBOutOwnFrames2,
       "twgLBReboot": twgLBReboot,
       "twgLBStatus": twgLBStatus,
       "twgLBState1": twgLBState1,
       "twgLBState2": twgLBState2,
       "twgLBAddr1": twgLBAddr1}
)

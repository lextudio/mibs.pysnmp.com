# SNMP MIB module (LIGO-GENERIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIGO-GENERIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:11 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ligoMgmt,) = mibBuilder.importSymbols(
    "LIGOWAVE-MIB",
    "ligoMgmt")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysLocation,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation")

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

ligoGenericMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 1)
)
ligoGenericMIB.setRevisions(
        ("2016-01-15 00:00",
         "2009-02-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LigoGenericMIBObjects_ObjectIdentity = ObjectIdentity
ligoGenericMIBObjects = _LigoGenericMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 1, 1)
)
_LigoGenericNotifs_ObjectIdentity = ObjectIdentity
ligoGenericNotifs = _LigoGenericNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 1, 1, 0)
)
_LigoGenericInfo_ObjectIdentity = ObjectIdentity
ligoGenericInfo = _LigoGenericInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 1, 1, 1)
)
_LigoPingHostsTable_Object = MibTable
ligoPingHostsTable = _LigoPingHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ligoPingHostsTable.setStatus("current")
_LigoPingHostsEntry_Object = MibTableRow
ligoPingHostsEntry = _LigoPingHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 1, 1, 1, 2, 1)
)
ligoPingHostsEntry.setIndexNames(
    (0, "LIGO-GENERIC-MIB", "ligoPingAddrType"),
    (0, "LIGO-GENERIC-MIB", "ligoPingAddr"),
)
if mibBuilder.loadTexts:
    ligoPingHostsEntry.setStatus("current")
_LigoPingAddrType_Type = InetAddressType
_LigoPingAddrType_Object = MibTableColumn
ligoPingAddrType = _LigoPingAddrType_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 1, 1, 1, 2, 1, 1),
    _LigoPingAddrType_Type()
)
ligoPingAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ligoPingAddrType.setStatus("current")
_LigoPingAddr_Type = InetAddress
_LigoPingAddr_Object = MibTableColumn
ligoPingAddr = _LigoPingAddr_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 1, 1, 1, 2, 1, 2),
    _LigoPingAddr_Type()
)
ligoPingAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ligoPingAddr.setStatus("current")
_LigoPingTime_Type = Integer32
_LigoPingTime_Object = MibTableColumn
ligoPingTime = _LigoPingTime_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 1, 1, 1, 2, 1, 3),
    _LigoPingTime_Type()
)
ligoPingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoPingTime.setStatus("current")
if mibBuilder.loadTexts:
    ligoPingTime.setUnits("ms")
_LigoPingHost_Type = DisplayString
_LigoPingHost_Object = MibTableColumn
ligoPingHost = _LigoPingHost_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 1, 1, 1, 2, 1, 4),
    _LigoPingHost_Type()
)
ligoPingHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoPingHost.setStatus("current")

# Managed Objects groups


# Notification objects

ligoPowerLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 1, 1, 0, 1)
)
ligoPowerLoss.setObjects(
    ("SNMPv2-MIB", "sysLocation")
)
if mibBuilder.loadTexts:
    ligoPowerLoss.setStatus(
        "current"
    )

ligoAdministrativeReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 1, 1, 0, 2)
)
ligoAdministrativeReboot.setObjects(
    ("SNMPv2-MIB", "sysLocation")
)
if mibBuilder.loadTexts:
    ligoAdministrativeReboot.setStatus(
        "current"
    )

ligoHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 1, 1, 0, 3)
)
ligoHeartbeat.setObjects(
    ("SNMPv2-MIB", "sysLocation")
)
if mibBuilder.loadTexts:
    ligoHeartbeat.setStatus(
        "current"
    )

ligoHighPing = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 1, 1, 0, 4)
)
ligoHighPing.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("LIGO-GENERIC-MIB", "ligoPingTime"))
)
if mibBuilder.loadTexts:
    ligoHighPing.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIGO-GENERIC-MIB",
    **{"ligoGenericMIB": ligoGenericMIB,
       "ligoGenericMIBObjects": ligoGenericMIBObjects,
       "ligoGenericNotifs": ligoGenericNotifs,
       "ligoPowerLoss": ligoPowerLoss,
       "ligoAdministrativeReboot": ligoAdministrativeReboot,
       "ligoHeartbeat": ligoHeartbeat,
       "ligoHighPing": ligoHighPing,
       "ligoGenericInfo": ligoGenericInfo,
       "ligoPingHostsTable": ligoPingHostsTable,
       "ligoPingHostsEntry": ligoPingHostsEntry,
       "ligoPingAddrType": ligoPingAddrType,
       "ligoPingAddr": ligoPingAddr,
       "ligoPingTime": ligoPingTime,
       "ligoPingHost": ligoPingHost}
)

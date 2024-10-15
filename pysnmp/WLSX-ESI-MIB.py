# SNMP MIB module (WLSX-ESI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WLSX-ESI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:06 2024
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

(wlsxEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsxEnterpriseMibModules")

(ArubaESIServerMode,
 ArubaESIServerStatus) = mibBuilder.importSymbols(
    "ARUBA-TC",
    "ArubaESIServerMode",
    "ArubaESIServerStatus")

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
 TextualConvention,
 TimeTicks,
 Unsigned32,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "TextualConvention",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "snmpModules")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

wlsxESIMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10)
)
wlsxESIMIB.setRevisions(
        ("1910-01-26 18:06",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxESIConfigGroup_ObjectIdentity = ObjectIdentity
wlsxESIConfigGroup = _WlsxESIConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1)
)
_WlsxESIServerTable_Object = MibTable
wlsxESIServerTable = _WlsxESIServerTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    wlsxESIServerTable.setStatus("current")
_WlsxESIServerEntry_Object = MibTableRow
wlsxESIServerEntry = _WlsxESIServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1)
)
wlsxESIServerEntry.setIndexNames(
    (0, "WLSX-ESI-MIB", "esiServerName"),
)
if mibBuilder.loadTexts:
    wlsxESIServerEntry.setStatus("current")
_EsiServerName_Type = DisplayString
_EsiServerName_Object = MibTableColumn
esiServerName = _EsiServerName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 1),
    _EsiServerName_Type()
)
esiServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    esiServerName.setStatus("current")
_EsiServerGroup_Type = DisplayString
_EsiServerGroup_Object = MibTableColumn
esiServerGroup = _EsiServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 2),
    _EsiServerGroup_Type()
)
esiServerGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiServerGroup.setStatus("current")
_EsiServerMode_Type = ArubaESIServerMode
_EsiServerMode_Object = MibTableColumn
esiServerMode = _EsiServerMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 3),
    _EsiServerMode_Type()
)
esiServerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiServerMode.setStatus("current")
_EsiServerTrustedIP_Type = IpAddress
_EsiServerTrustedIP_Object = MibTableColumn
esiServerTrustedIP = _EsiServerTrustedIP_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 4),
    _EsiServerTrustedIP_Type()
)
esiServerTrustedIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiServerTrustedIP.setStatus("current")
_EsiServerUntrustedIP_Type = IpAddress
_EsiServerUntrustedIP_Object = MibTableColumn
esiServerUntrustedIP = _EsiServerUntrustedIP_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 5),
    _EsiServerUntrustedIP_Type()
)
esiServerUntrustedIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiServerUntrustedIP.setStatus("current")
_EsiServerTrustedSlot_Type = Integer32
_EsiServerTrustedSlot_Object = MibTableColumn
esiServerTrustedSlot = _EsiServerTrustedSlot_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 6),
    _EsiServerTrustedSlot_Type()
)
esiServerTrustedSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiServerTrustedSlot.setStatus("current")
_EsiServerTrustedPort_Type = Integer32
_EsiServerTrustedPort_Object = MibTableColumn
esiServerTrustedPort = _EsiServerTrustedPort_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 7),
    _EsiServerTrustedPort_Type()
)
esiServerTrustedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiServerTrustedPort.setStatus("current")
_EsiServerUntrustedSlot_Type = Integer32
_EsiServerUntrustedSlot_Object = MibTableColumn
esiServerUntrustedSlot = _EsiServerUntrustedSlot_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 8),
    _EsiServerUntrustedSlot_Type()
)
esiServerUntrustedSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiServerUntrustedSlot.setStatus("current")
_EsiServerUntrustedPort_Type = Integer32
_EsiServerUntrustedPort_Object = MibTableColumn
esiServerUntrustedPort = _EsiServerUntrustedPort_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 9),
    _EsiServerUntrustedPort_Type()
)
esiServerUntrustedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiServerUntrustedPort.setStatus("current")
_EsiServerStatus_Type = ArubaESIServerStatus
_EsiServerStatus_Object = MibTableColumn
esiServerStatus = _EsiServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 10),
    _EsiServerStatus_Type()
)
esiServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiServerStatus.setStatus("current")
_EsiServerTrustedModule_Type = Integer32
_EsiServerTrustedModule_Object = MibTableColumn
esiServerTrustedModule = _EsiServerTrustedModule_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 11),
    _EsiServerTrustedModule_Type()
)
esiServerTrustedModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiServerTrustedModule.setStatus("current")
_EsiServerUntrustedModule_Type = Integer32
_EsiServerUntrustedModule_Object = MibTableColumn
esiServerUntrustedModule = _EsiServerUntrustedModule_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 12),
    _EsiServerUntrustedModule_Type()
)
esiServerUntrustedModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiServerUntrustedModule.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-ESI-MIB",
    **{"wlsxESIMIB": wlsxESIMIB,
       "wlsxESIConfigGroup": wlsxESIConfigGroup,
       "wlsxESIServerTable": wlsxESIServerTable,
       "wlsxESIServerEntry": wlsxESIServerEntry,
       "esiServerName": esiServerName,
       "esiServerGroup": esiServerGroup,
       "esiServerMode": esiServerMode,
       "esiServerTrustedIP": esiServerTrustedIP,
       "esiServerUntrustedIP": esiServerUntrustedIP,
       "esiServerTrustedSlot": esiServerTrustedSlot,
       "esiServerTrustedPort": esiServerTrustedPort,
       "esiServerUntrustedSlot": esiServerUntrustedSlot,
       "esiServerUntrustedPort": esiServerUntrustedPort,
       "esiServerStatus": esiServerStatus,
       "esiServerTrustedModule": esiServerTrustedModule,
       "esiServerUntrustedModule": esiServerUntrustedModule}
)

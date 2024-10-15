# SNMP MIB module (ZYXEL-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-RADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:41 2024
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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelRadius = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelRadiusServerSetup_ObjectIdentity = ObjectIdentity
zyxelRadiusServerSetup = _ZyxelRadiusServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 1)
)
_ZyxelRadiusAuthenticationServerSetup_ObjectIdentity = ObjectIdentity
zyxelRadiusAuthenticationServerSetup = _ZyxelRadiusAuthenticationServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 1, 1)
)


class _ZyRadiusAuthenticationServerMode_Type(Integer32):
    """Custom type zyRadiusAuthenticationServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("indexPriority", 1),
          ("roundRobin", 2))
    )


_ZyRadiusAuthenticationServerMode_Type.__name__ = "Integer32"
_ZyRadiusAuthenticationServerMode_Object = MibScalar
zyRadiusAuthenticationServerMode = _ZyRadiusAuthenticationServerMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 1, 1, 1),
    _ZyRadiusAuthenticationServerMode_Type()
)
zyRadiusAuthenticationServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRadiusAuthenticationServerMode.setStatus("current")
_ZyRadiusAuthenticationServerTimeout_Type = Integer32
_ZyRadiusAuthenticationServerTimeout_Object = MibScalar
zyRadiusAuthenticationServerTimeout = _ZyRadiusAuthenticationServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 1, 1, 2),
    _ZyRadiusAuthenticationServerTimeout_Type()
)
zyRadiusAuthenticationServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRadiusAuthenticationServerTimeout.setStatus("current")
_ZyxelRadiusAuthenticationServerTable_Object = MibTable
zyxelRadiusAuthenticationServerTable = _ZyxelRadiusAuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 1, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelRadiusAuthenticationServerTable.setStatus("current")
_ZyxelRadiusAuthenticationServerEntry_Object = MibTableRow
zyxelRadiusAuthenticationServerEntry = _ZyxelRadiusAuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 1, 1, 3, 1)
)
zyxelRadiusAuthenticationServerEntry.setIndexNames(
    (0, "ZYXEL-RADIUS-MIB", "zyRadiusAuthenticationServerIndex"),
)
if mibBuilder.loadTexts:
    zyxelRadiusAuthenticationServerEntry.setStatus("current")
_ZyRadiusAuthenticationServerIndex_Type = Integer32
_ZyRadiusAuthenticationServerIndex_Object = MibTableColumn
zyRadiusAuthenticationServerIndex = _ZyRadiusAuthenticationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 1, 1, 3, 1, 1),
    _ZyRadiusAuthenticationServerIndex_Type()
)
zyRadiusAuthenticationServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyRadiusAuthenticationServerIndex.setStatus("current")
_ZyRadiusAuthenticationServerIpAddr_Type = IpAddress
_ZyRadiusAuthenticationServerIpAddr_Object = MibTableColumn
zyRadiusAuthenticationServerIpAddr = _ZyRadiusAuthenticationServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 1, 1, 3, 1, 2),
    _ZyRadiusAuthenticationServerIpAddr_Type()
)
zyRadiusAuthenticationServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRadiusAuthenticationServerIpAddr.setStatus("current")
_ZyRadiusAuthenticationServerUdpPort_Type = Integer32
_ZyRadiusAuthenticationServerUdpPort_Object = MibTableColumn
zyRadiusAuthenticationServerUdpPort = _ZyRadiusAuthenticationServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 1, 1, 3, 1, 3),
    _ZyRadiusAuthenticationServerUdpPort_Type()
)
zyRadiusAuthenticationServerUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRadiusAuthenticationServerUdpPort.setStatus("current")
_ZyRadiusAuthenticationServerSharedSecret_Type = DisplayString
_ZyRadiusAuthenticationServerSharedSecret_Object = MibTableColumn
zyRadiusAuthenticationServerSharedSecret = _ZyRadiusAuthenticationServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 1, 1, 3, 1, 4),
    _ZyRadiusAuthenticationServerSharedSecret_Type()
)
zyRadiusAuthenticationServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRadiusAuthenticationServerSharedSecret.setStatus("current")
_ZyxelRadiusAccountingServerSetup_ObjectIdentity = ObjectIdentity
zyxelRadiusAccountingServerSetup = _ZyxelRadiusAccountingServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 1, 2)
)
_ZyRadiusAccountingServerTimeout_Type = Integer32
_ZyRadiusAccountingServerTimeout_Object = MibScalar
zyRadiusAccountingServerTimeout = _ZyRadiusAccountingServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 1, 2, 1),
    _ZyRadiusAccountingServerTimeout_Type()
)
zyRadiusAccountingServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRadiusAccountingServerTimeout.setStatus("current")
_ZyxelRadiusAccountingServerTable_Object = MibTable
zyxelRadiusAccountingServerTable = _ZyxelRadiusAccountingServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 1, 2, 2)
)
if mibBuilder.loadTexts:
    zyxelRadiusAccountingServerTable.setStatus("current")
_ZyxelRadiusAccountingServerEntry_Object = MibTableRow
zyxelRadiusAccountingServerEntry = _ZyxelRadiusAccountingServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 1, 2, 2, 1)
)
zyxelRadiusAccountingServerEntry.setIndexNames(
    (0, "ZYXEL-RADIUS-MIB", "zyRadiusAccountingServerIndex"),
)
if mibBuilder.loadTexts:
    zyxelRadiusAccountingServerEntry.setStatus("current")
_ZyRadiusAccountingServerIndex_Type = Integer32
_ZyRadiusAccountingServerIndex_Object = MibTableColumn
zyRadiusAccountingServerIndex = _ZyRadiusAccountingServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 1, 2, 2, 1, 1),
    _ZyRadiusAccountingServerIndex_Type()
)
zyRadiusAccountingServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyRadiusAccountingServerIndex.setStatus("current")
_ZyRadiusAccountingServerIpAddr_Type = IpAddress
_ZyRadiusAccountingServerIpAddr_Object = MibTableColumn
zyRadiusAccountingServerIpAddr = _ZyRadiusAccountingServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 1, 2, 2, 1, 2),
    _ZyRadiusAccountingServerIpAddr_Type()
)
zyRadiusAccountingServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRadiusAccountingServerIpAddr.setStatus("current")
_ZyRadiusAccountingServerUdpPort_Type = Integer32
_ZyRadiusAccountingServerUdpPort_Object = MibTableColumn
zyRadiusAccountingServerUdpPort = _ZyRadiusAccountingServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 1, 2, 2, 1, 3),
    _ZyRadiusAccountingServerUdpPort_Type()
)
zyRadiusAccountingServerUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRadiusAccountingServerUdpPort.setStatus("current")
_ZyRadiusAccountingServerSharedSecret_Type = DisplayString
_ZyRadiusAccountingServerSharedSecret_Object = MibTableColumn
zyRadiusAccountingServerSharedSecret = _ZyRadiusAccountingServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 1, 2, 2, 1, 4),
    _ZyRadiusAccountingServerSharedSecret_Type()
)
zyRadiusAccountingServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRadiusAccountingServerSharedSecret.setStatus("current")
_ZyxelRadiusServerNotifications_ObjectIdentity = ObjectIdentity
zyxelRadiusServerNotifications = _ZyxelRadiusServerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 2)
)

# Managed Objects groups


# Notification objects

zyRadiusServerAuthenticationServerNotReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 2, 1)
)
zyRadiusServerAuthenticationServerNotReachable.setObjects(
    ("ZYXEL-RADIUS-MIB", "zyRadiusAuthenticationServerIndex")
)
if mibBuilder.loadTexts:
    zyRadiusServerAuthenticationServerNotReachable.setStatus(
        "current"
    )

zyRadiusServerAccountingServerNotReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 2, 2)
)
zyRadiusServerAccountingServerNotReachable.setObjects(
    ("ZYXEL-RADIUS-MIB", "zyRadiusAccountingServerIndex")
)
if mibBuilder.loadTexts:
    zyRadiusServerAccountingServerNotReachable.setStatus(
        "current"
    )

zyRadiusServerAuthenticationServerNotReachableRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 2, 3)
)
zyRadiusServerAuthenticationServerNotReachableRecovered.setObjects(
    ("ZYXEL-RADIUS-MIB", "zyRadiusAuthenticationServerIndex")
)
if mibBuilder.loadTexts:
    zyRadiusServerAuthenticationServerNotReachableRecovered.setStatus(
        "current"
    )

zyRadiusServerAccountingServerNotReachableRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 71, 2, 4)
)
zyRadiusServerAccountingServerNotReachableRecovered.setObjects(
    ("ZYXEL-RADIUS-MIB", "zyRadiusAccountingServerIndex")
)
if mibBuilder.loadTexts:
    zyRadiusServerAccountingServerNotReachableRecovered.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-RADIUS-MIB",
    **{"zyxelRadius": zyxelRadius,
       "zyxelRadiusServerSetup": zyxelRadiusServerSetup,
       "zyxelRadiusAuthenticationServerSetup": zyxelRadiusAuthenticationServerSetup,
       "zyRadiusAuthenticationServerMode": zyRadiusAuthenticationServerMode,
       "zyRadiusAuthenticationServerTimeout": zyRadiusAuthenticationServerTimeout,
       "zyxelRadiusAuthenticationServerTable": zyxelRadiusAuthenticationServerTable,
       "zyxelRadiusAuthenticationServerEntry": zyxelRadiusAuthenticationServerEntry,
       "zyRadiusAuthenticationServerIndex": zyRadiusAuthenticationServerIndex,
       "zyRadiusAuthenticationServerIpAddr": zyRadiusAuthenticationServerIpAddr,
       "zyRadiusAuthenticationServerUdpPort": zyRadiusAuthenticationServerUdpPort,
       "zyRadiusAuthenticationServerSharedSecret": zyRadiusAuthenticationServerSharedSecret,
       "zyxelRadiusAccountingServerSetup": zyxelRadiusAccountingServerSetup,
       "zyRadiusAccountingServerTimeout": zyRadiusAccountingServerTimeout,
       "zyxelRadiusAccountingServerTable": zyxelRadiusAccountingServerTable,
       "zyxelRadiusAccountingServerEntry": zyxelRadiusAccountingServerEntry,
       "zyRadiusAccountingServerIndex": zyRadiusAccountingServerIndex,
       "zyRadiusAccountingServerIpAddr": zyRadiusAccountingServerIpAddr,
       "zyRadiusAccountingServerUdpPort": zyRadiusAccountingServerUdpPort,
       "zyRadiusAccountingServerSharedSecret": zyRadiusAccountingServerSharedSecret,
       "zyxelRadiusServerNotifications": zyxelRadiusServerNotifications,
       "zyRadiusServerAuthenticationServerNotReachable": zyRadiusServerAuthenticationServerNotReachable,
       "zyRadiusServerAccountingServerNotReachable": zyRadiusServerAccountingServerNotReachable,
       "zyRadiusServerAuthenticationServerNotReachableRecovered": zyRadiusServerAuthenticationServerNotReachableRecovered,
       "zyRadiusServerAccountingServerNotReachableRecovered": zyRadiusServerAccountingServerNotReachableRecovered}
)

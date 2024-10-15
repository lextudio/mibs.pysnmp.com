# SNMP MIB module (ZYXEL-TACACS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-TACACS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:56 2024
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

zyxelTacacs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelTacacsServerSetup_ObjectIdentity = ObjectIdentity
zyxelTacacsServerSetup = _ZyxelTacacsServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 1)
)
_ZyxelTacacsAuthenticationServerSetup_ObjectIdentity = ObjectIdentity
zyxelTacacsAuthenticationServerSetup = _ZyxelTacacsAuthenticationServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 1, 1)
)


class _ZyTacacsAuthenticationServerMode_Type(Integer32):
    """Custom type zyTacacsAuthenticationServerMode based on Integer32"""
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


_ZyTacacsAuthenticationServerMode_Type.__name__ = "Integer32"
_ZyTacacsAuthenticationServerMode_Object = MibScalar
zyTacacsAuthenticationServerMode = _ZyTacacsAuthenticationServerMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 1, 1, 1),
    _ZyTacacsAuthenticationServerMode_Type()
)
zyTacacsAuthenticationServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTacacsAuthenticationServerMode.setStatus("current")
_ZyTacacsAuthenticationServerTimeout_Type = Integer32
_ZyTacacsAuthenticationServerTimeout_Object = MibScalar
zyTacacsAuthenticationServerTimeout = _ZyTacacsAuthenticationServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 1, 1, 2),
    _ZyTacacsAuthenticationServerTimeout_Type()
)
zyTacacsAuthenticationServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTacacsAuthenticationServerTimeout.setStatus("current")
_ZyxelTacacsAuthenticationServerTable_Object = MibTable
zyxelTacacsAuthenticationServerTable = _ZyxelTacacsAuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 1, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelTacacsAuthenticationServerTable.setStatus("current")
_ZyxelTacacsAuthenticationServerEntry_Object = MibTableRow
zyxelTacacsAuthenticationServerEntry = _ZyxelTacacsAuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 1, 1, 3, 1)
)
zyxelTacacsAuthenticationServerEntry.setIndexNames(
    (0, "ZYXEL-TACACS-MIB", "zyTacacsAuthenticationServerIndex"),
)
if mibBuilder.loadTexts:
    zyxelTacacsAuthenticationServerEntry.setStatus("current")
_ZyTacacsAuthenticationServerIndex_Type = Integer32
_ZyTacacsAuthenticationServerIndex_Object = MibTableColumn
zyTacacsAuthenticationServerIndex = _ZyTacacsAuthenticationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 1, 1, 3, 1, 1),
    _ZyTacacsAuthenticationServerIndex_Type()
)
zyTacacsAuthenticationServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyTacacsAuthenticationServerIndex.setStatus("current")
_ZyTacacsAuthenticationServerIpAddress_Type = IpAddress
_ZyTacacsAuthenticationServerIpAddress_Object = MibTableColumn
zyTacacsAuthenticationServerIpAddress = _ZyTacacsAuthenticationServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 1, 1, 3, 1, 2),
    _ZyTacacsAuthenticationServerIpAddress_Type()
)
zyTacacsAuthenticationServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTacacsAuthenticationServerIpAddress.setStatus("current")
_ZyTacacsAuthenticationServerTcpPort_Type = Integer32
_ZyTacacsAuthenticationServerTcpPort_Object = MibTableColumn
zyTacacsAuthenticationServerTcpPort = _ZyTacacsAuthenticationServerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 1, 1, 3, 1, 3),
    _ZyTacacsAuthenticationServerTcpPort_Type()
)
zyTacacsAuthenticationServerTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTacacsAuthenticationServerTcpPort.setStatus("current")
_ZyTacacsAuthenticationServerSharedSecret_Type = DisplayString
_ZyTacacsAuthenticationServerSharedSecret_Object = MibTableColumn
zyTacacsAuthenticationServerSharedSecret = _ZyTacacsAuthenticationServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 1, 1, 3, 1, 4),
    _ZyTacacsAuthenticationServerSharedSecret_Type()
)
zyTacacsAuthenticationServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTacacsAuthenticationServerSharedSecret.setStatus("current")
_ZyxelTacacsAccountingServerSetup_ObjectIdentity = ObjectIdentity
zyxelTacacsAccountingServerSetup = _ZyxelTacacsAccountingServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 1, 2)
)
_ZyTacacsAccountingServerTimeout_Type = Integer32
_ZyTacacsAccountingServerTimeout_Object = MibScalar
zyTacacsAccountingServerTimeout = _ZyTacacsAccountingServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 1, 2, 1),
    _ZyTacacsAccountingServerTimeout_Type()
)
zyTacacsAccountingServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTacacsAccountingServerTimeout.setStatus("current")
_ZyxelTacacsAccountingServerTable_Object = MibTable
zyxelTacacsAccountingServerTable = _ZyxelTacacsAccountingServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 1, 2, 2)
)
if mibBuilder.loadTexts:
    zyxelTacacsAccountingServerTable.setStatus("current")
_ZyxelTacacsAccountingServerEntry_Object = MibTableRow
zyxelTacacsAccountingServerEntry = _ZyxelTacacsAccountingServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 1, 2, 2, 1)
)
zyxelTacacsAccountingServerEntry.setIndexNames(
    (0, "ZYXEL-TACACS-MIB", "zyTacacsAccountingServerIndex"),
)
if mibBuilder.loadTexts:
    zyxelTacacsAccountingServerEntry.setStatus("current")
_ZyTacacsAccountingServerIndex_Type = Integer32
_ZyTacacsAccountingServerIndex_Object = MibTableColumn
zyTacacsAccountingServerIndex = _ZyTacacsAccountingServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 1, 2, 2, 1, 1),
    _ZyTacacsAccountingServerIndex_Type()
)
zyTacacsAccountingServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyTacacsAccountingServerIndex.setStatus("current")
_ZyTacacsAccountingServerIpAddress_Type = IpAddress
_ZyTacacsAccountingServerIpAddress_Object = MibTableColumn
zyTacacsAccountingServerIpAddress = _ZyTacacsAccountingServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 1, 2, 2, 1, 2),
    _ZyTacacsAccountingServerIpAddress_Type()
)
zyTacacsAccountingServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTacacsAccountingServerIpAddress.setStatus("current")
_ZyTacacsAccountingServerTcpPort_Type = Integer32
_ZyTacacsAccountingServerTcpPort_Object = MibTableColumn
zyTacacsAccountingServerTcpPort = _ZyTacacsAccountingServerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 1, 2, 2, 1, 3),
    _ZyTacacsAccountingServerTcpPort_Type()
)
zyTacacsAccountingServerTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTacacsAccountingServerTcpPort.setStatus("current")
_ZyTacacsAccountingServerSharedSecret_Type = DisplayString
_ZyTacacsAccountingServerSharedSecret_Object = MibTableColumn
zyTacacsAccountingServerSharedSecret = _ZyTacacsAccountingServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 1, 2, 2, 1, 4),
    _ZyTacacsAccountingServerSharedSecret_Type()
)
zyTacacsAccountingServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTacacsAccountingServerSharedSecret.setStatus("current")
_ZyxelTacacsServerNotifications_ObjectIdentity = ObjectIdentity
zyxelTacacsServerNotifications = _ZyxelTacacsServerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 2)
)

# Managed Objects groups


# Notification objects

zyTacacsServerAuthenticationServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 2, 1)
)
zyTacacsServerAuthenticationServerUnreachable.setObjects(
    ("ZYXEL-TACACS-MIB", "zyTacacsAccountingServerIndex")
)
if mibBuilder.loadTexts:
    zyTacacsServerAuthenticationServerUnreachable.setStatus(
        "current"
    )

zyTacacsServerAccountingServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 2, 2)
)
zyTacacsServerAccountingServerUnreachable.setObjects(
    ("ZYXEL-TACACS-MIB", "zyTacacsAccountingServerIndex")
)
if mibBuilder.loadTexts:
    zyTacacsServerAccountingServerUnreachable.setStatus(
        "current"
    )

zyTacacsServerAuthenticationServerUnreachableRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 2, 3)
)
zyTacacsServerAuthenticationServerUnreachableRecovered.setObjects(
    ("ZYXEL-TACACS-MIB", "zyTacacsAccountingServerIndex")
)
if mibBuilder.loadTexts:
    zyTacacsServerAuthenticationServerUnreachableRecovered.setStatus(
        "current"
    )

zyTacacsServerAccountingServerUnreachableRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 83, 2, 4)
)
zyTacacsServerAccountingServerUnreachableRecovered.setObjects(
    ("ZYXEL-TACACS-MIB", "zyTacacsAccountingServerIndex")
)
if mibBuilder.loadTexts:
    zyTacacsServerAccountingServerUnreachableRecovered.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-TACACS-MIB",
    **{"zyxelTacacs": zyxelTacacs,
       "zyxelTacacsServerSetup": zyxelTacacsServerSetup,
       "zyxelTacacsAuthenticationServerSetup": zyxelTacacsAuthenticationServerSetup,
       "zyTacacsAuthenticationServerMode": zyTacacsAuthenticationServerMode,
       "zyTacacsAuthenticationServerTimeout": zyTacacsAuthenticationServerTimeout,
       "zyxelTacacsAuthenticationServerTable": zyxelTacacsAuthenticationServerTable,
       "zyxelTacacsAuthenticationServerEntry": zyxelTacacsAuthenticationServerEntry,
       "zyTacacsAuthenticationServerIndex": zyTacacsAuthenticationServerIndex,
       "zyTacacsAuthenticationServerIpAddress": zyTacacsAuthenticationServerIpAddress,
       "zyTacacsAuthenticationServerTcpPort": zyTacacsAuthenticationServerTcpPort,
       "zyTacacsAuthenticationServerSharedSecret": zyTacacsAuthenticationServerSharedSecret,
       "zyxelTacacsAccountingServerSetup": zyxelTacacsAccountingServerSetup,
       "zyTacacsAccountingServerTimeout": zyTacacsAccountingServerTimeout,
       "zyxelTacacsAccountingServerTable": zyxelTacacsAccountingServerTable,
       "zyxelTacacsAccountingServerEntry": zyxelTacacsAccountingServerEntry,
       "zyTacacsAccountingServerIndex": zyTacacsAccountingServerIndex,
       "zyTacacsAccountingServerIpAddress": zyTacacsAccountingServerIpAddress,
       "zyTacacsAccountingServerTcpPort": zyTacacsAccountingServerTcpPort,
       "zyTacacsAccountingServerSharedSecret": zyTacacsAccountingServerSharedSecret,
       "zyxelTacacsServerNotifications": zyxelTacacsServerNotifications,
       "zyTacacsServerAuthenticationServerUnreachable": zyTacacsServerAuthenticationServerUnreachable,
       "zyTacacsServerAccountingServerUnreachable": zyTacacsServerAccountingServerUnreachable,
       "zyTacacsServerAuthenticationServerUnreachableRecovered": zyTacacsServerAuthenticationServerUnreachableRecovered,
       "zyTacacsServerAccountingServerUnreachableRecovered": zyTacacsServerAccountingServerUnreachableRecovered}
)

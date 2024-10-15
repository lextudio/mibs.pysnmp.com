# SNMP MIB module (STN-PPTP-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-PPTP-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:14 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(stnNotification,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnNotification")

(stnEngineCpu,
 stnEngineIndex,
 stnEngineSlot) = mibBuilder.importSymbols(
    "STN-CHASSIS-MIB",
    "stnEngineCpu",
    "stnEngineIndex",
    "stnEngineSlot")

(stnPptpTraps,) = mibBuilder.importSymbols(
    "STN-PPTP-MIB",
    "stnPptpTraps")

(stnRouterIndex,
 stnSubnetInterfaceIndex) = mibBuilder.importSymbols(
    "STN-ROUTER-MIB",
    "stnRouterIndex",
    "stnSubnetInterfaceIndex")


# MODULE-IDENTITY

stnPptpTrap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnPptpTrapVars_ObjectIdentity = ObjectIdentity
stnPptpTrapVars = _StnPptpTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 1)
)
_StnPptpTunnelLocalHostname_Type = DisplayString
_StnPptpTunnelLocalHostname_Object = MibScalar
stnPptpTunnelLocalHostname = _StnPptpTunnelLocalHostname_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 1, 1),
    _StnPptpTunnelLocalHostname_Type()
)
stnPptpTunnelLocalHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelLocalHostname.setStatus("current")
_StnPptpTunnelLocalIpAddress_Type = IpAddress
_StnPptpTunnelLocalIpAddress_Object = MibScalar
stnPptpTunnelLocalIpAddress = _StnPptpTunnelLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 1, 2),
    _StnPptpTunnelLocalIpAddress_Type()
)
stnPptpTunnelLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelLocalIpAddress.setStatus("current")
_StnPptpTunnelRemoteHostname_Type = DisplayString
_StnPptpTunnelRemoteHostname_Object = MibScalar
stnPptpTunnelRemoteHostname = _StnPptpTunnelRemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 1, 3),
    _StnPptpTunnelRemoteHostname_Type()
)
stnPptpTunnelRemoteHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelRemoteHostname.setStatus("current")
_StnPptpTunnelRemoteIpAddress_Type = IpAddress
_StnPptpTunnelRemoteIpAddress_Object = MibScalar
stnPptpTunnelRemoteIpAddress = _StnPptpTunnelRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 1, 4),
    _StnPptpTunnelRemoteIpAddress_Type()
)
stnPptpTunnelRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelRemoteIpAddress.setStatus("current")
_StnPptpNotificationPrefix_ObjectIdentity = ObjectIdentity
stnPptpNotificationPrefix = _StnPptpNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 2)
)
_StnPptpNotification_ObjectIdentity = ObjectIdentity
stnPptpNotification = _StnPptpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 2, 0)
)

# Managed Objects groups


# Notification objects

stnTunnelPptpAuthenFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 2, 0, 1)
)
stnTunnelPptpAuthenFailure.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("STN-ROUTER-MIB", "stnSubnetInterfaceIndex"),
        ("STN-PPTP-TRAP-MIB", "stnPptpTunnelLocalHostname"),
        ("STN-PPTP-TRAP-MIB", "stnPptpTunnelRemoteHostname"),
        ("STN-PPTP-TRAP-MIB", "stnPptpTunnelRemoteIpAddress"))
)
if mibBuilder.loadTexts:
    stnTunnelPptpAuthenFailure.setStatus(
        "current"
    )

stnTunnelPptpLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 2, 0, 2)
)
stnTunnelPptpLimitExceeded.setObjects(
      *(("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"))
)
if mibBuilder.loadTexts:
    stnTunnelPptpLimitExceeded.setStatus(
        "current"
    )

stnTunnelPacProvLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 2, 0, 3)
)
stnTunnelPacProvLimitExceeded.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("STN-ROUTER-MIB", "stnSubnetInterfaceIndex"),
        ("STN-PPTP-TRAP-MIB", "stnPptpTunnelLocalHostname"),
        ("STN-PPTP-TRAP-MIB", "stnPptpTunnelLocalIpAddress"))
)
if mibBuilder.loadTexts:
    stnTunnelPacProvLimitExceeded.setStatus(
        "current"
    )

stnTunnelPnsProvLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 2, 0, 4)
)
stnTunnelPnsProvLimitExceeded.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("STN-ROUTER-MIB", "stnSubnetInterfaceIndex"),
        ("STN-PPTP-TRAP-MIB", "stnPptpTunnelLocalHostname"),
        ("STN-PPTP-TRAP-MIB", "stnPptpTunnelLocalIpAddress"))
)
if mibBuilder.loadTexts:
    stnTunnelPnsProvLimitExceeded.setStatus(
        "current"
    )

stnCallPptpLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 2, 0, 5)
)
stnCallPptpLimitExceeded.setObjects(
      *(("STN-CHASSIS-MIB", "stnEngineIndex"),
        ("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"))
)
if mibBuilder.loadTexts:
    stnCallPptpLimitExceeded.setStatus(
        "current"
    )

stnCallPacProvLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 2, 0, 6)
)
stnCallPacProvLimitExceeded.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("STN-ROUTER-MIB", "stnSubnetInterfaceIndex"),
        ("STN-PPTP-TRAP-MIB", "stnPptpTunnelLocalHostname"),
        ("STN-PPTP-TRAP-MIB", "stnPptpTunnelRemoteHostname"),
        ("STN-PPTP-TRAP-MIB", "stnPptpTunnelRemoteIpAddress"))
)
if mibBuilder.loadTexts:
    stnCallPacProvLimitExceeded.setStatus(
        "current"
    )

stnCallPnsProvLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 2, 0, 7)
)
stnCallPnsProvLimitExceeded.setObjects(
      *(("STN-ROUTER-MIB", "stnRouterIndex"),
        ("STN-ROUTER-MIB", "stnSubnetInterfaceIndex"),
        ("STN-PPTP-TRAP-MIB", "stnPptpTunnelLocalHostname"),
        ("STN-PPTP-TRAP-MIB", "stnPptpTunnelRemoteHostname"),
        ("STN-PPTP-TRAP-MIB", "stnPptpTunnelRemoteIpAddress"))
)
if mibBuilder.loadTexts:
    stnCallPnsProvLimitExceeded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-PPTP-TRAP-MIB",
    **{"stnPptpTrap": stnPptpTrap,
       "stnPptpTrapVars": stnPptpTrapVars,
       "stnPptpTunnelLocalHostname": stnPptpTunnelLocalHostname,
       "stnPptpTunnelLocalIpAddress": stnPptpTunnelLocalIpAddress,
       "stnPptpTunnelRemoteHostname": stnPptpTunnelRemoteHostname,
       "stnPptpTunnelRemoteIpAddress": stnPptpTunnelRemoteIpAddress,
       "stnPptpNotificationPrefix": stnPptpNotificationPrefix,
       "stnPptpNotification": stnPptpNotification,
       "stnTunnelPptpAuthenFailure": stnTunnelPptpAuthenFailure,
       "stnTunnelPptpLimitExceeded": stnTunnelPptpLimitExceeded,
       "stnTunnelPacProvLimitExceeded": stnTunnelPacProvLimitExceeded,
       "stnTunnelPnsProvLimitExceeded": stnTunnelPnsProvLimitExceeded,
       "stnCallPptpLimitExceeded": stnCallPptpLimitExceeded,
       "stnCallPacProvLimitExceeded": stnCallPacProvLimitExceeded,
       "stnCallPnsProvLimitExceeded": stnCallPnsProvLimitExceeded}
)

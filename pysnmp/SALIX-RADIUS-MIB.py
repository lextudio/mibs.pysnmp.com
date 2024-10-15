# SNMP MIB module (SALIX-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SALIX-RADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:34 2024
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

(atmfM4TrapAlarmSeverity,) = mibBuilder.importSymbols(
    "ATM-FORUM-M4-MIB",
    "atmfM4TrapAlarmSeverity")

(salixGeneric,) = mibBuilder.importSymbols(
    "SALIX-MIB",
    "salixGeneric")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

salixRadiusMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SalixRadiusMIBObjects_ObjectIdentity = ObjectIdentity
salixRadiusMIBObjects = _SalixRadiusMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8, 1)
)
_SalixRadiusServerConfigTable_Object = MibTable
salixRadiusServerConfigTable = _SalixRadiusServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    salixRadiusServerConfigTable.setStatus("current")
_SalixRadiusServerConfigEntry_Object = MibTableRow
salixRadiusServerConfigEntry = _SalixRadiusServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8, 1, 1, 1)
)
salixRadiusServerConfigEntry.setIndexNames(
    (0, "SALIX-RADIUS-MIB", "salixRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    salixRadiusServerConfigEntry.setStatus("current")


class _SalixRadiusServerIndex_Type(Integer32):
    """Custom type salixRadiusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SalixRadiusServerIndex_Type.__name__ = "Integer32"
_SalixRadiusServerIndex_Object = MibTableColumn
salixRadiusServerIndex = _SalixRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8, 1, 1, 1, 1),
    _SalixRadiusServerIndex_Type()
)
salixRadiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixRadiusServerIndex.setStatus("current")
_SalixRadiusServerIpAddress_Type = IpAddress
_SalixRadiusServerIpAddress_Object = MibTableColumn
salixRadiusServerIpAddress = _SalixRadiusServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8, 1, 1, 1, 2),
    _SalixRadiusServerIpAddress_Type()
)
salixRadiusServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixRadiusServerIpAddress.setStatus("current")


class _SalixRadiusServerUdpPort_Type(Integer32):
    """Custom type salixRadiusServerUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SalixRadiusServerUdpPort_Type.__name__ = "Integer32"
_SalixRadiusServerUdpPort_Object = MibTableColumn
salixRadiusServerUdpPort = _SalixRadiusServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8, 1, 1, 1, 3),
    _SalixRadiusServerUdpPort_Type()
)
salixRadiusServerUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixRadiusServerUdpPort.setStatus("current")


class _SalixRadiusServerSharedSecret_Type(OctetString):
    """Custom type salixRadiusServerSharedSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_SalixRadiusServerSharedSecret_Type.__name__ = "OctetString"
_SalixRadiusServerSharedSecret_Object = MibTableColumn
salixRadiusServerSharedSecret = _SalixRadiusServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8, 1, 1, 1, 4),
    _SalixRadiusServerSharedSecret_Type()
)
salixRadiusServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixRadiusServerSharedSecret.setStatus("current")
_SalixRadiusServerEnabled_Type = TruthValue
_SalixRadiusServerEnabled_Object = MibTableColumn
salixRadiusServerEnabled = _SalixRadiusServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8, 1, 1, 1, 5),
    _SalixRadiusServerEnabled_Type()
)
salixRadiusServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixRadiusServerEnabled.setStatus("current")


class _SalixUserAuthenticationMethod_Type(Integer32):
    """Custom type salixUserAuthenticationMethod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("internal", 0),
          ("radius", 1),
          ("tacacs", 2),
          ("tacacsplus", 4),
          ("xtacacs", 3))
    )


_SalixUserAuthenticationMethod_Type.__name__ = "Integer32"
_SalixUserAuthenticationMethod_Object = MibScalar
salixUserAuthenticationMethod = _SalixUserAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8, 1, 2),
    _SalixUserAuthenticationMethod_Type()
)
salixUserAuthenticationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixUserAuthenticationMethod.setStatus("current")
_SalixRadiusMIBTraps_ObjectIdentity = ObjectIdentity
salixRadiusMIBTraps = _SalixRadiusMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8, 2)
)
_SalixRadiusMIBTrapPrefix_ObjectIdentity = ObjectIdentity
salixRadiusMIBTrapPrefix = _SalixRadiusMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8, 2, 0)
)
_SalixRadiusMIBCompliance_ObjectIdentity = ObjectIdentity
salixRadiusMIBCompliance = _SalixRadiusMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8, 3)
)
_SalixRadiusGroups_ObjectIdentity = ObjectIdentity
salixRadiusGroups = _SalixRadiusGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8, 3, 1)
)
_SalixRadiusCompliances_ObjectIdentity = ObjectIdentity
salixRadiusCompliances = _SalixRadiusCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8, 3, 2)
)

# Managed Objects groups

salixRadiusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8, 3, 1, 1)
)
salixRadiusGroup.setObjects(
      *(("SALIX-RADIUS-MIB", "salixRadiusServerIndex"),
        ("SALIX-RADIUS-MIB", "salixRadiusServerIpAddress"),
        ("SALIX-RADIUS-MIB", "salixRadiusServerUdpPort"),
        ("SALIX-RADIUS-MIB", "salixRadiusServerSharedSecret"),
        ("SALIX-RADIUS-MIB", "salixRadiusServerEnabled"))
)
if mibBuilder.loadTexts:
    salixRadiusGroup.setStatus("current")


# Notification objects

salixRadiusAccessRequestTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8, 2, 0, 1)
)
salixRadiusAccessRequestTimeout.setObjects(
      *(("SALIX-RADIUS-MIB", "salixRadiusServerIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    salixRadiusAccessRequestTimeout.setStatus(
        "current"
    )

salixRadiusAccessDenied = NotificationType(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8, 2, 0, 2)
)
salixRadiusAccessDenied.setObjects(
      *(("SALIX-RADIUS-MIB", "salixRadiusServerIndex"),
        ("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity"))
)
if mibBuilder.loadTexts:
    salixRadiusAccessDenied.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

salixRadiusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2158, 2, 8, 3, 2, 1)
)
if mibBuilder.loadTexts:
    salixRadiusCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SALIX-RADIUS-MIB",
    **{"salixRadiusMIB": salixRadiusMIB,
       "salixRadiusMIBObjects": salixRadiusMIBObjects,
       "salixRadiusServerConfigTable": salixRadiusServerConfigTable,
       "salixRadiusServerConfigEntry": salixRadiusServerConfigEntry,
       "salixRadiusServerIndex": salixRadiusServerIndex,
       "salixRadiusServerIpAddress": salixRadiusServerIpAddress,
       "salixRadiusServerUdpPort": salixRadiusServerUdpPort,
       "salixRadiusServerSharedSecret": salixRadiusServerSharedSecret,
       "salixRadiusServerEnabled": salixRadiusServerEnabled,
       "salixUserAuthenticationMethod": salixUserAuthenticationMethod,
       "salixRadiusMIBTraps": salixRadiusMIBTraps,
       "salixRadiusMIBTrapPrefix": salixRadiusMIBTrapPrefix,
       "salixRadiusAccessRequestTimeout": salixRadiusAccessRequestTimeout,
       "salixRadiusAccessDenied": salixRadiusAccessDenied,
       "salixRadiusMIBCompliance": salixRadiusMIBCompliance,
       "salixRadiusGroups": salixRadiusGroups,
       "salixRadiusGroup": salixRadiusGroup,
       "salixRadiusCompliances": salixRadiusCompliances,
       "salixRadiusCompliance": salixRadiusCompliance}
)

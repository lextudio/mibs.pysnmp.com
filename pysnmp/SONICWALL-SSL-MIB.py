# SNMP MIB module (SONICWALL-SSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONICWALL-SSL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:37 2024
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
 NotificationType,
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
    "NotificationType",
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

sonicWallSSLMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3884, 2)
)
sonicWallSSLMIB.setRevisions(
        ("2001-02-08 13:30",
         "2001-02-07 10:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonicWall_ObjectIdentity = ObjectIdentity
sonicWall = _SonicWall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3884)
)
_SslTraps_ObjectIdentity = ObjectIdentity
sslTraps = _SslTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3884, 2, 0)
)
_Information_ObjectIdentity = ObjectIdentity
information = _Information_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3884, 2, 1)
)
_LastConfigChangeInitiator_Type = IpAddress
_LastConfigChangeInitiator_Object = MibScalar
lastConfigChangeInitiator = _LastConfigChangeInitiator_Object(
    (1, 3, 6, 1, 4, 1, 3884, 2, 1, 4),
    _LastConfigChangeInitiator_Type()
)
lastConfigChangeInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConfigChangeInitiator.setStatus("mandatory")
_LastConfigChangeCmd_Type = Integer32
_LastConfigChangeCmd_Object = MibScalar
lastConfigChangeCmd = _LastConfigChangeCmd_Object(
    (1, 3, 6, 1, 4, 1, 3884, 2, 1, 5),
    _LastConfigChangeCmd_Type()
)
lastConfigChangeCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConfigChangeCmd.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpuUtilChangeHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 3884, 0, 1)
)
if mibBuilder.loadTexts:
    cpuUtilChangeHi.setStatus(
        ""
    )

cpuUtilChangeLo = NotificationType(
    (1, 3, 6, 1, 4, 1, 3884, 0, 2)
)
if mibBuilder.loadTexts:
    cpuUtilChangeLo.setStatus(
        ""
    )

sslTpsChangeHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 3884, 0, 3)
)
if mibBuilder.loadTexts:
    sslTpsChangeHi.setStatus(
        ""
    )

sslTpsChangeLo = NotificationType(
    (1, 3, 6, 1, 4, 1, 3884, 0, 4)
)
if mibBuilder.loadTexts:
    sslTpsChangeLo.setStatus(
        ""
    )

sslTotalConnectsChangeHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 3884, 0, 5)
)
if mibBuilder.loadTexts:
    sslTotalConnectsChangeHi.setStatus(
        ""
    )

sslTotalConnectsChangeLo = NotificationType(
    (1, 3, 6, 1, 4, 1, 3884, 0, 6)
)
if mibBuilder.loadTexts:
    sslTotalConnectsChangeLo.setStatus(
        ""
    )

configChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3884, 0, 7)
)
configChange.setObjects(
      *(("SONICWALL-SSL-MIB", "lastConfigChangeInitiator"),
        ("SONICWALL-SSL-MIB", "lastConfigChangeCmd"))
)
if mibBuilder.loadTexts:
    configChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONICWALL-SSL-MIB",
    **{"sonicWall": sonicWall,
       "cpuUtilChangeHi": cpuUtilChangeHi,
       "cpuUtilChangeLo": cpuUtilChangeLo,
       "sslTpsChangeHi": sslTpsChangeHi,
       "sslTpsChangeLo": sslTpsChangeLo,
       "sslTotalConnectsChangeHi": sslTotalConnectsChangeHi,
       "sslTotalConnectsChangeLo": sslTotalConnectsChangeLo,
       "configChange": configChange,
       "sonicWallSSLMIB": sonicWallSSLMIB,
       "sslTraps": sslTraps,
       "information": information,
       "lastConfigChangeInitiator": lastConfigChangeInitiator,
       "lastConfigChangeCmd": lastConfigChangeCmd}
)

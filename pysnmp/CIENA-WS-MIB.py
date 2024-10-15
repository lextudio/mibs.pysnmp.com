# SNMP MIB module (CIENA-WS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-WS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:10 2024
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

ciena = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271)
)
ciena.setRevisions(
        ("2010-09-27 23:17",
         "2016-07-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Waveserver_ObjectIdentity = ObjectIdentity
waveserver = _Waveserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3)
)
if mibBuilder.loadTexts:
    waveserver.setStatus("current")
_CienaWsConfigV1_ObjectIdentity = ObjectIdentity
cienaWsConfigV1 = _CienaWsConfigV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 1)
)
if mibBuilder.loadTexts:
    cienaWsConfigV1.setStatus("current")
_CienaWsNotifications_ObjectIdentity = ObjectIdentity
cienaWsNotifications = _CienaWsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2)
)
if mibBuilder.loadTexts:
    cienaWsNotifications.setStatus("current")
_CienaWsNotificationsControlModule_ObjectIdentity = ObjectIdentity
cienaWsNotificationsControlModule = _CienaWsNotificationsControlModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cienaWsNotificationsControlModule.setStatus("current")
_CienaWsStatistics_ObjectIdentity = ObjectIdentity
cienaWsStatistics = _CienaWsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 3)
)
if mibBuilder.loadTexts:
    cienaWsStatistics.setStatus("obsolete")
_CienaWsConfig_ObjectIdentity = ObjectIdentity
cienaWsConfig = _CienaWsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4)
)
if mibBuilder.loadTexts:
    cienaWsConfig.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-MIB",
    **{"ciena": ciena,
       "waveserver": waveserver,
       "cienaWsConfigV1": cienaWsConfigV1,
       "cienaWsNotifications": cienaWsNotifications,
       "cienaWsNotificationsControlModule": cienaWsNotificationsControlModule,
       "cienaWsStatistics": cienaWsStatistics,
       "cienaWsConfig": cienaWsConfig}
)

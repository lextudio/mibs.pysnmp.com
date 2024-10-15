# SNMP MIB module (SPRING-TIDE-NETWORKS-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SPRING-TIDE-NETWORKS-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:25 2024
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

springtidenet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnProducts_ObjectIdentity = ObjectIdentity
stnProducts = _StnProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 1)
)
if mibBuilder.loadTexts:
    stnProducts.setStatus("current")
_StnSystems_ObjectIdentity = ObjectIdentity
stnSystems = _StnSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2)
)
if mibBuilder.loadTexts:
    stnSystems.setStatus("current")
_StnConfig_ObjectIdentity = ObjectIdentity
stnConfig = _StnConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 99)
)
_StnNotificationPrefix_ObjectIdentity = ObjectIdentity
stnNotificationPrefix = _StnNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100)
)
_StnNotification_ObjectIdentity = ObjectIdentity
stnNotification = _StnNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 100, 0)
)
_StnExtensions_ObjectIdentity = ObjectIdentity
stnExtensions = _StnExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 3)
)
if mibBuilder.loadTexts:
    stnExtensions.setStatus("current")
_StnTemporary_ObjectIdentity = ObjectIdentity
stnTemporary = _StnTemporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 4)
)
if mibBuilder.loadTexts:
    stnTemporary.setStatus("current")
_StnTmpProtocols_ObjectIdentity = ObjectIdentity
stnTmpProtocols = _StnTmpProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1)
)
_StnMibModules_ObjectIdentity = ObjectIdentity
stnMibModules = _StnMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 5)
)
if mibBuilder.loadTexts:
    stnMibModules.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    **{"springtidenet": springtidenet,
       "stnProducts": stnProducts,
       "stnSystems": stnSystems,
       "stnConfig": stnConfig,
       "stnNotificationPrefix": stnNotificationPrefix,
       "stnNotification": stnNotification,
       "stnExtensions": stnExtensions,
       "stnTemporary": stnTemporary,
       "stnTmpProtocols": stnTmpProtocols,
       "stnMibModules": stnMibModules}
)

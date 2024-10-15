# SNMP MIB module (PYSNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PYSNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:25 2024
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

pysnmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20408)
)
pysnmp.setRevisions(
        ("2017-04-14 00:00",
         "2005-05-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PysnmpObjects_ObjectIdentity = ObjectIdentity
pysnmpObjects = _PysnmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20408, 1)
)
_PysnmpExamples_ObjectIdentity = ObjectIdentity
pysnmpExamples = _PysnmpExamples_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20408, 2)
)
_PysnmpEnumerations_ObjectIdentity = ObjectIdentity
pysnmpEnumerations = _PysnmpEnumerations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20408, 3)
)
_PysnmpModuleIDs_ObjectIdentity = ObjectIdentity
pysnmpModuleIDs = _PysnmpModuleIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20408, 3, 1)
)
_PysnmpAgentOIDs_ObjectIdentity = ObjectIdentity
pysnmpAgentOIDs = _PysnmpAgentOIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20408, 3, 2)
)
_PysnmpDomains_ObjectIdentity = ObjectIdentity
pysnmpDomains = _PysnmpDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20408, 3, 3)
)
_PysnmpNotificationPrefix_ObjectIdentity = ObjectIdentity
pysnmpNotificationPrefix = _PysnmpNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20408, 4)
)
_PysnmpNotifications_ObjectIdentity = ObjectIdentity
pysnmpNotifications = _PysnmpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20408, 4, 0)
)
_PysnmpNotificationObjects_ObjectIdentity = ObjectIdentity
pysnmpNotificationObjects = _PysnmpNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20408, 4, 1)
)
_PysnmpConformance_ObjectIdentity = ObjectIdentity
pysnmpConformance = _PysnmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20408, 5)
)
_PysnmpCompliances_ObjectIdentity = ObjectIdentity
pysnmpCompliances = _PysnmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20408, 5, 1)
)
_PysnmpGroups_ObjectIdentity = ObjectIdentity
pysnmpGroups = _PysnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20408, 5, 2)
)
_PysnmpExperimental_ObjectIdentity = ObjectIdentity
pysnmpExperimental = _PysnmpExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20408, 9999)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PYSNMP-MIB",
    **{"pysnmp": pysnmp,
       "pysnmpObjects": pysnmpObjects,
       "pysnmpExamples": pysnmpExamples,
       "pysnmpEnumerations": pysnmpEnumerations,
       "pysnmpModuleIDs": pysnmpModuleIDs,
       "pysnmpAgentOIDs": pysnmpAgentOIDs,
       "pysnmpDomains": pysnmpDomains,
       "pysnmpNotificationPrefix": pysnmpNotificationPrefix,
       "pysnmpNotifications": pysnmpNotifications,
       "pysnmpNotificationObjects": pysnmpNotificationObjects,
       "pysnmpConformance": pysnmpConformance,
       "pysnmpCompliances": pysnmpCompliances,
       "pysnmpGroups": pysnmpGroups,
       "pysnmpExperimental": pysnmpExperimental}
)

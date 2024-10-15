# SNMP MIB module (NOKIA-NE3S-REGISTRATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-NE3S-REGISTRATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:37 2024
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

(nokiaSnmpInterface,) = mibBuilder.importSymbols(
    "NOKIA-OID-REGISTRATION-MIB",
    "nokiaSnmpInterface")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NoiFaultManagement_ObjectIdentity = ObjectIdentity
noiFaultManagement = _NoiFaultManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 1)
)
_NoiOpenInterfaceModule_ObjectIdentity = ObjectIdentity
noiOpenInterfaceModule = _NoiOpenInterfaceModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 1)
)
_NoiFaultManagementVariable_ObjectIdentity = ObjectIdentity
noiFaultManagementVariable = _NoiFaultManagementVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 2)
)
_NoiAlarmNotificationDef_ObjectIdentity = ObjectIdentity
noiAlarmNotificationDef = _NoiAlarmNotificationDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 3)
)
_NoiAlarmNotification_ObjectIdentity = ObjectIdentity
noiAlarmNotification = _NoiAlarmNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 3, 0)
)
_NoiAlarmTables_ObjectIdentity = ObjectIdentity
noiAlarmTables = _NoiAlarmTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 4)
)
_NoiAlarmLog_ObjectIdentity = ObjectIdentity
noiAlarmLog = _NoiAlarmLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 5)
)
_NoiFMCompliance_ObjectIdentity = ObjectIdentity
noiFMCompliance = _NoiFMCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 6)
)
_NoiConfigurationManagement_ObjectIdentity = ObjectIdentity
noiConfigurationManagement = _NoiConfigurationManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 2)
)
_NoiConfigurationManagementVariable_ObjectIdentity = ObjectIdentity
noiConfigurationManagementVariable = _NoiConfigurationManagementVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 2, 2)
)
_NoiConfigurationManagementNotificationDef_ObjectIdentity = ObjectIdentity
noiConfigurationManagementNotificationDef = _NoiConfigurationManagementNotificationDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 2, 3)
)
_NoiConfigurationManagementNotification_ObjectIdentity = ObjectIdentity
noiConfigurationManagementNotification = _NoiConfigurationManagementNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 2, 3, 0)
)
_NoiConfigurationManagementCompliance_ObjectIdentity = ObjectIdentity
noiConfigurationManagementCompliance = _NoiConfigurationManagementCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 2, 4)
)
_NoiPerformanceManagement_ObjectIdentity = ObjectIdentity
noiPerformanceManagement = _NoiPerformanceManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 3)
)
_NoiPmVariable_ObjectIdentity = ObjectIdentity
noiPmVariable = _NoiPmVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 2)
)
_NoiPmNotificationDef_ObjectIdentity = ObjectIdentity
noiPmNotificationDef = _NoiPmNotificationDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 3)
)
_NoiPmNotification_ObjectIdentity = ObjectIdentity
noiPmNotification = _NoiPmNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 3, 0)
)
_NoiPmTable_ObjectIdentity = ObjectIdentity
noiPmTable = _NoiPmTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 4)
)
_NoiPmCompliance_ObjectIdentity = ObjectIdentity
noiPmCompliance = _NoiPmCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-NE3S-REGISTRATION-MIB",
    **{"noiFaultManagement": noiFaultManagement,
       "noiOpenInterfaceModule": noiOpenInterfaceModule,
       "noiFaultManagementVariable": noiFaultManagementVariable,
       "noiAlarmNotificationDef": noiAlarmNotificationDef,
       "noiAlarmNotification": noiAlarmNotification,
       "noiAlarmTables": noiAlarmTables,
       "noiAlarmLog": noiAlarmLog,
       "noiFMCompliance": noiFMCompliance,
       "noiConfigurationManagement": noiConfigurationManagement,
       "noiConfigurationManagementVariable": noiConfigurationManagementVariable,
       "noiConfigurationManagementNotificationDef": noiConfigurationManagementNotificationDef,
       "noiConfigurationManagementNotification": noiConfigurationManagementNotification,
       "noiConfigurationManagementCompliance": noiConfigurationManagementCompliance,
       "noiPerformanceManagement": noiPerformanceManagement,
       "noiPmVariable": noiPmVariable,
       "noiPmNotificationDef": noiPmNotificationDef,
       "noiPmNotification": noiPmNotification,
       "noiPmTable": noiPmTable,
       "noiPmCompliance": noiPmCompliance}
)

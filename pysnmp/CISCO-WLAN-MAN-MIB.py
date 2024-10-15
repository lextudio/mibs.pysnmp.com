# SNMP MIB module (CISCO-WLAN-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WLAN-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:42 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoWlanManMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 415)
)
ciscoWlanManMIB.setRevisions(
        ("2004-03-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWlanManMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoWlanManMIBNotifs = _CiscoWlanManMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 415, 0)
)
_CiscoWlanManMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWlanManMIBObjects = _CiscoWlanManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 415, 1)
)
_CwmDeviceConfig_ObjectIdentity = ObjectIdentity
cwmDeviceConfig = _CwmDeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 1)
)
_CwmHttpServerEnabled_Type = TruthValue
_CwmHttpServerEnabled_Object = MibScalar
cwmHttpServerEnabled = _CwmHttpServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 1, 1),
    _CwmHttpServerEnabled_Type()
)
cwmHttpServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwmHttpServerEnabled.setStatus("current")
_CwmTelnetLoginEnabled_Type = TruthValue
_CwmTelnetLoginEnabled_Object = MibScalar
cwmTelnetLoginEnabled = _CwmTelnetLoginEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 1, 2),
    _CwmTelnetLoginEnabled_Type()
)
cwmTelnetLoginEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwmTelnetLoginEnabled.setStatus("current")
_CwmNetworkConfig_ObjectIdentity = ObjectIdentity
cwmNetworkConfig = _CwmNetworkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 2)
)
_CiscoWlanManMIBConform_ObjectIdentity = ObjectIdentity
ciscoWlanManMIBConform = _CiscoWlanManMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 415, 2)
)
_CiscoWlanManMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWlanManMIBCompliances = _CiscoWlanManMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 1)
)
_CiscoWlanManMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWlanManMIBGroups = _CiscoWlanManMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 2)
)

# Managed Objects groups

cwmWirelessDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 2, 1)
)
cwmWirelessDeviceGroup.setObjects(
      *(("CISCO-WLAN-MAN-MIB", "cwmHttpServerEnabled"),
        ("CISCO-WLAN-MAN-MIB", "cwmTelnetLoginEnabled"))
)
if mibBuilder.loadTexts:
    cwmWirelessDeviceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWlanManMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWlanManMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WLAN-MAN-MIB",
    **{"ciscoWlanManMIB": ciscoWlanManMIB,
       "ciscoWlanManMIBNotifs": ciscoWlanManMIBNotifs,
       "ciscoWlanManMIBObjects": ciscoWlanManMIBObjects,
       "cwmDeviceConfig": cwmDeviceConfig,
       "cwmHttpServerEnabled": cwmHttpServerEnabled,
       "cwmTelnetLoginEnabled": cwmTelnetLoginEnabled,
       "cwmNetworkConfig": cwmNetworkConfig,
       "ciscoWlanManMIBConform": ciscoWlanManMIBConform,
       "ciscoWlanManMIBCompliances": ciscoWlanManMIBCompliances,
       "ciscoWlanManMIBCompliance": ciscoWlanManMIBCompliance,
       "ciscoWlanManMIBGroups": ciscoWlanManMIBGroups,
       "cwmWirelessDeviceGroup": cwmWirelessDeviceGroup}
)

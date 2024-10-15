# SNMP MIB module (HP-ICF-USBPORT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-USBPORT
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:24 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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


# MODULE-IDENTITY

hpicfUSBPortMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53)
)
hpicfUSBPortMIB.setRevisions(
        ("2009-03-11 00:00",
         "2008-09-17 00:00",
         "2008-09-10 00:00",
         "2008-06-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfUSBPortNotifications_ObjectIdentity = ObjectIdentity
hpicfUSBPortNotifications = _HpicfUSBPortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 0)
)
_HpicfUSBPortConfig_ObjectIdentity = ObjectIdentity
hpicfUSBPortConfig = _HpicfUSBPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 1)
)


class _HpicfUSBPortStatus_Type(Integer32):
    """Custom type hpicfUSBPortStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notPresent", 0))
    )


_HpicfUSBPortStatus_Type.__name__ = "Integer32"
_HpicfUSBPortStatus_Object = MibScalar
hpicfUSBPortStatus = _HpicfUSBPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 1, 1),
    _HpicfUSBPortStatus_Type()
)
hpicfUSBPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUSBPortStatus.setStatus("current")


class _HpicfUSBPortZeroPowerStatus_Type(Integer32):
    """Custom type hpicfUSBPortZeroPowerStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 1),
          ("powerOn", 2),
          ("powerUnavailable", 0))
    )


_HpicfUSBPortZeroPowerStatus_Type.__name__ = "Integer32"
_HpicfUSBPortZeroPowerStatus_Object = MibScalar
hpicfUSBPortZeroPowerStatus = _HpicfUSBPortZeroPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 1, 2),
    _HpicfUSBPortZeroPowerStatus_Type()
)
hpicfUSBPortZeroPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUSBPortZeroPowerStatus.setStatus("current")
_HpicfUSBPortConformance_ObjectIdentity = ObjectIdentity
hpicfUSBPortConformance = _HpicfUSBPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 2)
)
_HpicfUSBPortGroups_ObjectIdentity = ObjectIdentity
hpicfUSBPortGroups = _HpicfUSBPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 2, 1)
)
_HpicfUSBPortCompliances_ObjectIdentity = ObjectIdentity
hpicfUSBPortCompliances = _HpicfUSBPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 2, 2)
)

# Managed Objects groups

hpicfUSBPortBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 2, 1, 1)
)
hpicfUSBPortBaseGroup.setObjects(
      *(("HP-ICF-USBPORT", "hpicfUSBPortStatus"),
        ("HP-ICF-USBPORT", "hpicfUSBPortZeroPowerStatus"))
)
if mibBuilder.loadTexts:
    hpicfUSBPortBaseGroup.setStatus("current")


# Notification objects

hpicfUSBPortEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 0, 1)
)
if mibBuilder.loadTexts:
    hpicfUSBPortEnabled.setStatus(
        "current"
    )

hpicfUSBPortDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 0, 2)
)
if mibBuilder.loadTexts:
    hpicfUSBPortDisabled.setStatus(
        "current"
    )


# Notifications groups

hpicfUSBPortNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 2, 1, 2)
)
hpicfUSBPortNotificationGroup.setObjects(
      *(("HP-ICF-USBPORT", "hpicfUSBPortEnabled"),
        ("HP-ICF-USBPORT", "hpicfUSBPortDisabled"))
)
if mibBuilder.loadTexts:
    hpicfUSBPortNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfUSBPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfUSBPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-USBPORT",
    **{"hpicfUSBPortMIB": hpicfUSBPortMIB,
       "hpicfUSBPortNotifications": hpicfUSBPortNotifications,
       "hpicfUSBPortEnabled": hpicfUSBPortEnabled,
       "hpicfUSBPortDisabled": hpicfUSBPortDisabled,
       "hpicfUSBPortConfig": hpicfUSBPortConfig,
       "hpicfUSBPortStatus": hpicfUSBPortStatus,
       "hpicfUSBPortZeroPowerStatus": hpicfUSBPortZeroPowerStatus,
       "hpicfUSBPortConformance": hpicfUSBPortConformance,
       "hpicfUSBPortGroups": hpicfUSBPortGroups,
       "hpicfUSBPortBaseGroup": hpicfUSBPortBaseGroup,
       "hpicfUSBPortNotificationGroup": hpicfUSBPortNotificationGroup,
       "hpicfUSBPortCompliances": hpicfUSBPortCompliances,
       "hpicfUSBPortCompliance": hpicfUSBPortCompliance}
)

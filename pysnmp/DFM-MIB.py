# SNMP MIB module (DFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DFM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:20 2024
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

dfmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 733)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SmNotificationTrap_ObjectIdentity = ObjectIdentity
smNotificationTrap = _SmNotificationTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 733, 0)
)
_SmNotificationData_ObjectIdentity = ObjectIdentity
smNotificationData = _SmNotificationData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 733, 2)
)
_SmGenericNotify_ObjectIdentity = ObjectIdentity
smGenericNotify = _SmGenericNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 733, 2, 1)
)
_SmNotifTimestamp_Type = Counter32
_SmNotifTimestamp_Object = MibScalar
smNotifTimestamp = _SmNotifTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 733, 2, 1, 1),
    _SmNotifTimestamp_Type()
)
smNotifTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smNotifTimestamp.setStatus("current")
_SmNotifServer_Type = OctetString
_SmNotifServer_Object = MibScalar
smNotifServer = _SmNotifServer_Object(
    (1, 3, 6, 1, 4, 1, 733, 2, 1, 2),
    _SmNotifServer_Type()
)
smNotifServer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smNotifServer.setStatus("current")
_SmNotifClass_Type = OctetString
_SmNotifClass_Object = MibScalar
smNotifClass = _SmNotifClass_Object(
    (1, 3, 6, 1, 4, 1, 733, 2, 1, 3),
    _SmNotifClass_Type()
)
smNotifClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smNotifClass.setStatus("current")
_SmNotifInstance_Type = OctetString
_SmNotifInstance_Object = MibScalar
smNotifInstance = _SmNotifInstance_Object(
    (1, 3, 6, 1, 4, 1, 733, 2, 1, 4),
    _SmNotifInstance_Type()
)
smNotifInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smNotifInstance.setStatus("current")
_SmNotifEventName_Type = OctetString
_SmNotifEventName_Object = MibScalar
smNotifEventName = _SmNotifEventName_Object(
    (1, 3, 6, 1, 4, 1, 733, 2, 1, 5),
    _SmNotifEventName_Type()
)
smNotifEventName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smNotifEventName.setStatus("current")
_SmNotifInstanceID_Type = OctetString
_SmNotifInstanceID_Object = MibScalar
smNotifInstanceID = _SmNotifInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 733, 2, 1, 6),
    _SmNotifInstanceID_Type()
)
smNotifInstanceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smNotifInstanceID.setStatus("current")
_SmNotifDescription_Type = OctetString
_SmNotifDescription_Object = MibScalar
smNotifDescription = _SmNotifDescription_Object(
    (1, 3, 6, 1, 4, 1, 733, 2, 1, 7),
    _SmNotifDescription_Type()
)
smNotifDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smNotifDescription.setStatus("current")
_SmNotifCertainty_Type = OctetString
_SmNotifCertainty_Object = MibScalar
smNotifCertainty = _SmNotifCertainty_Object(
    (1, 3, 6, 1, 4, 1, 733, 2, 1, 8),
    _SmNotifCertainty_Type()
)
smNotifCertainty.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smNotifCertainty.setStatus("current")


class _SmNotifSeverity_Type(Integer32):
    """Custom type smNotifSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("informational", 2),
          ("major", 5),
          ("minor", 4),
          ("notApplicable", 1),
          ("severe", 6),
          ("warning", 3))
    )


_SmNotifSeverity_Type.__name__ = "Integer32"
_SmNotifSeverity_Object = MibScalar
smNotifSeverity = _SmNotifSeverity_Object(
    (1, 3, 6, 1, 4, 1, 733, 2, 1, 9),
    _SmNotifSeverity_Type()
)
smNotifSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smNotifSeverity.setStatus("current")

# Managed Objects groups


# Notification objects

smTrapCertaintyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 733, 0, 2)
)
smTrapCertaintyChange.setObjects(
      *(("DFM-MIB", "smNotifTimestamp"),
        ("DFM-MIB", "smNotifServer"),
        ("DFM-MIB", "smNotifClass"),
        ("DFM-MIB", "smNotifInstance"),
        ("DFM-MIB", "smNotifEventName"),
        ("DFM-MIB", "smNotifInstanceID"),
        ("DFM-MIB", "smNotifDescription"),
        ("DFM-MIB", "smNotifCertainty"),
        ("DFM-MIB", "smNotifSeverity"))
)
if mibBuilder.loadTexts:
    smTrapCertaintyChange.setStatus(
        "current"
    )

smTrapSeverityChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 733, 0, 3)
)
smTrapSeverityChange.setObjects(
      *(("DFM-MIB", "smNotifTimestamp"),
        ("DFM-MIB", "smNotifServer"),
        ("DFM-MIB", "smNotifClass"),
        ("DFM-MIB", "smNotifInstance"),
        ("DFM-MIB", "smNotifEventName"),
        ("DFM-MIB", "smNotifInstanceID"),
        ("DFM-MIB", "smNotifDescription"),
        ("DFM-MIB", "smNotifCertainty"),
        ("DFM-MIB", "smNotifSeverity"))
)
if mibBuilder.loadTexts:
    smTrapSeverityChange.setStatus(
        "current"
    )

smTrapNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 733, 0, 4)
)
smTrapNotification.setObjects(
      *(("DFM-MIB", "smNotifTimestamp"),
        ("DFM-MIB", "smNotifServer"),
        ("DFM-MIB", "smNotifClass"),
        ("DFM-MIB", "smNotifInstance"),
        ("DFM-MIB", "smNotifEventName"),
        ("DFM-MIB", "smNotifInstanceID"),
        ("DFM-MIB", "smNotifDescription"),
        ("DFM-MIB", "smNotifCertainty"),
        ("DFM-MIB", "smNotifSeverity"))
)
if mibBuilder.loadTexts:
    smTrapNotification.setStatus(
        "current"
    )

smTrapNotificationClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 733, 0, 7)
)
smTrapNotificationClear.setObjects(
      *(("DFM-MIB", "smNotifTimestamp"),
        ("DFM-MIB", "smNotifServer"),
        ("DFM-MIB", "smNotifClass"),
        ("DFM-MIB", "smNotifInstance"),
        ("DFM-MIB", "smNotifEventName"),
        ("DFM-MIB", "smNotifInstanceID"),
        ("DFM-MIB", "smNotifDescription"),
        ("DFM-MIB", "smNotifCertainty"),
        ("DFM-MIB", "smNotifSeverity"))
)
if mibBuilder.loadTexts:
    smTrapNotificationClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DFM-MIB",
    **{"dfmMIB": dfmMIB,
       "smNotificationTrap": smNotificationTrap,
       "smTrapCertaintyChange": smTrapCertaintyChange,
       "smTrapSeverityChange": smTrapSeverityChange,
       "smTrapNotification": smTrapNotification,
       "smTrapNotificationClear": smTrapNotificationClear,
       "smNotificationData": smNotificationData,
       "smGenericNotify": smGenericNotify,
       "smNotifTimestamp": smNotifTimestamp,
       "smNotifServer": smNotifServer,
       "smNotifClass": smNotifClass,
       "smNotifInstance": smNotifInstance,
       "smNotifEventName": smNotifEventName,
       "smNotifInstanceID": smNotifInstanceID,
       "smNotifDescription": smNotifDescription,
       "smNotifCertainty": smNotifCertainty,
       "smNotifSeverity": smNotifSeverity}
)

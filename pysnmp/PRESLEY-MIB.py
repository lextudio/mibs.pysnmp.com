# SNMP MIB module (PRESLEY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PRESLEY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:37 2024
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

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_Generic_ObjectIdentity = ObjectIdentity
generic = _Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10)
)
_AlertLed_ObjectIdentity = ObjectIdentity
alertLed = _AlertLed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 23)
)


class _AlertLedState_Type(Integer32):
    """Custom type alertLedState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AlertLedState_Type.__name__ = "Integer32"
_AlertLedState_Object = MibScalar
alertLedState = _AlertLedState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 23, 1),
    _AlertLedState_Type()
)
alertLedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertLedState.setStatus("mandatory")
_AlertTable_Object = MibTable
alertTable = _AlertTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 23, 3)
)
if mibBuilder.loadTexts:
    alertTable.setStatus("mandatory")
_AlertTableEntry_Object = MibTableRow
alertTableEntry = _AlertTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 23, 3, 1)
)
alertTableEntry.setIndexNames(
    (0, "PRESLEY-MIB", "alertIdentifier"),
)
if mibBuilder.loadTexts:
    alertTableEntry.setStatus("mandatory")


class _AlertIdentifier_Type(Integer32):
    """Custom type alertIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("alertLedTest", 9),
          ("coaxPortPartitioned", 4),
          ("loginSecurityViolation", 5),
          ("networkErrorRate", 2),
          ("networkUtilization", 1),
          ("portSecurityViolation", 7),
          ("snmpSecurityViolation", 6),
          ("stationConnectivity", 8),
          ("utpPortPartitioned", 3))
    )


_AlertIdentifier_Type.__name__ = "Integer32"
_AlertIdentifier_Object = MibTableColumn
alertIdentifier = _AlertIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 23, 3, 1, 1),
    _AlertIdentifier_Type()
)
alertIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertIdentifier.setStatus("mandatory")


class _AlertDescription_Type(DisplayString):
    """Custom type alertDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlertDescription_Type.__name__ = "DisplayString"
_AlertDescription_Object = MibTableColumn
alertDescription = _AlertDescription_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 23, 3, 1, 2),
    _AlertDescription_Type()
)
alertDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertDescription.setStatus("mandatory")


class _AlertStatus_Type(Integer32):
    """Custom type alertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AlertStatus_Type.__name__ = "Integer32"
_AlertStatus_Object = MibTableColumn
alertStatus = _AlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 23, 3, 1, 3),
    _AlertStatus_Type()
)
alertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertStatus.setStatus("mandatory")


class _AlertType_Type(Integer32):
    """Custom type alertType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("latched", 3),
          ("state", 2),
          ("threshold", 1))
    )


_AlertType_Type.__name__ = "Integer32"
_AlertType_Object = MibTableColumn
alertType = _AlertType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 23, 3, 1, 4),
    _AlertType_Type()
)
alertType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertType.setStatus("mandatory")


class _AlertConfiguration_Type(Integer32):
    """Custom type alertConfiguration based on Integer32"""
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
        *(("acknowledge", 6),
          ("disabled", 2),
          ("enabled", 1),
          ("high", 3),
          ("low", 5),
          ("medium", 4))
    )


_AlertConfiguration_Type.__name__ = "Integer32"
_AlertConfiguration_Object = MibTableColumn
alertConfiguration = _AlertConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 23, 3, 1, 5),
    _AlertConfiguration_Type()
)
alertConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertConfiguration.setStatus("mandatory")

# Managed Objects groups


# Notification objects

alertLedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 73)
)
alertLedTrap.setObjects(
      *(("PRESLEY-MIB", "alertLedState"),
        ("PRESLEY-MIB", "alertDescription"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    alertLedTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRESLEY-MIB",
    **{"a3Com": a3Com,
       "alertLedTrap": alertLedTrap,
       "generic": generic,
       "alertLed": alertLed,
       "alertLedState": alertLedState,
       "alertTable": alertTable,
       "alertTableEntry": alertTableEntry,
       "alertIdentifier": alertIdentifier,
       "alertDescription": alertDescription,
       "alertStatus": alertStatus,
       "alertType": alertType,
       "alertConfiguration": alertConfiguration}
)

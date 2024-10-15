# SNMP MIB module (V320-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/V320-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:59 2024
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
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

sub10OID = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39003)
)
sub10OID.setRevisions(
        ("2011-11-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Terminal2_ObjectIdentity = ObjectIdentity
terminal2 = _Terminal2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 2)
)


class _TerminalLinkQuality_Type(Integer32):
    """Custom type terminalLinkQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("red", 3),
          ("unknown", 10),
          ("yellow", 2))
    )


_TerminalLinkQuality_Type.__name__ = "Integer32"
_TerminalLinkQuality_Object = MibScalar
terminalLinkQuality = _TerminalLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 39003, 2, 1),
    _TerminalLinkQuality_Type()
)
terminalLinkQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminalLinkQuality.setStatus("current")
_TerminalReceivePower_Type = Integer32
_TerminalReceivePower_Object = MibScalar
terminalReceivePower = _TerminalReceivePower_Object(
    (1, 3, 6, 1, 4, 1, 39003, 2, 10),
    _TerminalReceivePower_Type()
)
terminalReceivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminalReceivePower.setStatus("current")
_TerminalTemperature_Type = Integer32
_TerminalTemperature_Object = MibScalar
terminalTemperature = _TerminalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 39003, 2, 11),
    _TerminalTemperature_Type()
)
terminalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminalTemperature.setStatus("current")
_TerminalLockDetector_Type = Integer32
_TerminalLockDetector_Object = MibScalar
terminalLockDetector = _TerminalLockDetector_Object(
    (1, 3, 6, 1, 4, 1, 39003, 2, 12),
    _TerminalLockDetector_Type()
)
terminalLockDetector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminalLockDetector.setStatus("current")


class _TerminalLinkQualityImproved_Type(Integer32):
    """Custom type terminalLinkQualityImproved based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("red2green", 1),
          ("red2yellow", 2),
          ("yellow2green", 3))
    )


_TerminalLinkQualityImproved_Type.__name__ = "Integer32"
_TerminalLinkQualityImproved_Object = MibScalar
terminalLinkQualityImproved = _TerminalLinkQualityImproved_Object(
    (1, 3, 6, 1, 4, 1, 39003, 2, 13),
    _TerminalLinkQualityImproved_Type()
)
terminalLinkQualityImproved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminalLinkQualityImproved.setStatus("current")


class _TerminalLinkQualityReduced_Type(Integer32):
    """Custom type terminalLinkQualityReduced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green2red", 2),
          ("green2yellow", 1),
          ("yellow2red", 3))
    )


_TerminalLinkQualityReduced_Type.__name__ = "Integer32"
_TerminalLinkQualityReduced_Object = MibScalar
terminalLinkQualityReduced = _TerminalLinkQualityReduced_Object(
    (1, 3, 6, 1, 4, 1, 39003, 2, 14),
    _TerminalLinkQualityReduced_Type()
)
terminalLinkQualityReduced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminalLinkQualityReduced.setStatus("current")
_TerminalFirmwareversion_Type = OctetString
_TerminalFirmwareversion_Object = MibScalar
terminalFirmwareversion = _TerminalFirmwareversion_Object(
    (1, 3, 6, 1, 4, 1, 39003, 2, 21),
    _TerminalFirmwareversion_Type()
)
terminalFirmwareversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminalFirmwareversion.setStatus("current")
_TerminalTraps_ObjectIdentity = ObjectIdentity
terminalTraps = _TerminalTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39003, 2, 22)
)
_TerminalAuxVoltage_Type = OctetString
_TerminalAuxVoltage_Object = MibScalar
terminalAuxVoltage = _TerminalAuxVoltage_Object(
    (1, 3, 6, 1, 4, 1, 39003, 2, 25),
    _TerminalAuxVoltage_Type()
)
terminalAuxVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminalAuxVoltage.setStatus("current")

# Managed Objects groups

terminalObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39003, 2, 24)
)
terminalObjectGroup.setObjects(
      *(("V320-MIB", "terminalLinkQualityReduced"),
        ("V320-MIB", "terminalLinkQualityImproved"),
        ("V320-MIB", "terminalReceivePower"),
        ("V320-MIB", "terminalLinkQuality"),
        ("V320-MIB", "terminalTemperature"),
        ("V320-MIB", "terminalLockDetector"),
        ("V320-MIB", "terminalFirmwareversion"),
        ("V320-MIB", "terminalAuxVoltage"))
)
if mibBuilder.loadTexts:
    terminalObjectGroup.setStatus("current")


# Notification objects

terminalLinkQualityImprovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39003, 2, 22, 1)
)
terminalLinkQualityImprovedTrap.setObjects(
    ("V320-MIB", "terminalLinkQualityImproved")
)
if mibBuilder.loadTexts:
    terminalLinkQualityImprovedTrap.setStatus(
        "current"
    )

terminalLinkQualityReducedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39003, 2, 22, 2)
)
terminalLinkQualityReducedTrap.setObjects(
    ("V320-MIB", "terminalLinkQualityReduced")
)
if mibBuilder.loadTexts:
    terminalLinkQualityReducedTrap.setStatus(
        "current"
    )

terminalTemperatureHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39003, 2, 22, 3)
)
terminalTemperatureHighTrap.setObjects(
    ("V320-MIB", "terminalTemperature")
)
if mibBuilder.loadTexts:
    terminalTemperatureHighTrap.setStatus(
        "current"
    )

terminalTemperatureLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39003, 2, 22, 4)
)
terminalTemperatureLowTrap.setObjects(
    ("V320-MIB", "terminalTemperature")
)
if mibBuilder.loadTexts:
    terminalTemperatureLowTrap.setStatus(
        "current"
    )


# Notifications groups

terminalNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 39003, 2, 23)
)
terminalNotificationGroup.setObjects(
      *(("V320-MIB", "terminalLinkQualityImprovedTrap"),
        ("V320-MIB", "terminalLinkQualityReducedTrap"),
        ("V320-MIB", "terminalTemperatureHighTrap"),
        ("V320-MIB", "terminalTemperatureLowTrap"))
)
if mibBuilder.loadTexts:
    terminalNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "V320-MIB",
    **{"sub10OID": sub10OID,
       "terminal2": terminal2,
       "terminalLinkQuality": terminalLinkQuality,
       "terminalReceivePower": terminalReceivePower,
       "terminalTemperature": terminalTemperature,
       "terminalLockDetector": terminalLockDetector,
       "terminalLinkQualityImproved": terminalLinkQualityImproved,
       "terminalLinkQualityReduced": terminalLinkQualityReduced,
       "terminalFirmwareversion": terminalFirmwareversion,
       "terminalTraps": terminalTraps,
       "terminalLinkQualityImprovedTrap": terminalLinkQualityImprovedTrap,
       "terminalLinkQualityReducedTrap": terminalLinkQualityReducedTrap,
       "terminalTemperatureHighTrap": terminalTemperatureHighTrap,
       "terminalTemperatureLowTrap": terminalTemperatureLowTrap,
       "terminalNotificationGroup": terminalNotificationGroup,
       "terminalObjectGroup": terminalObjectGroup,
       "terminalAuxVoltage": terminalAuxVoltage}
)

# SNMP MIB module (AT-LOOPPROTECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-LOOPPROTECT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:24 2024
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

atLoopProtect = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54)
)
atLoopProtect.setRevisions(
        ("2012-06-19 00:00",
         "2010-09-07 00:00",
         "2010-06-15 01:00",
         "2008-08-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtLoopProtectTrap_ObjectIdentity = ObjectIdentity
atLoopProtectTrap = _AtLoopProtectTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 0)
)


class _AtLoopProtectAction_Type(Integer32):
    """Custom type atLoopProtectAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("atLoopProtectAction-LearnDisable", 0),
          ("atLoopProtectAction-LearnEnable", 1),
          ("atLoopProtectAction-LinkDown", 4),
          ("atLoopProtectAction-LinkUp", 5),
          ("atLoopProtectAction-PortDisable", 2),
          ("atLoopProtectAction-PortEnable", 3),
          ("atLoopProtectAction-VlanDisable", 6),
          ("atLoopProtectAction-VlanEnable", 7))
    )


_AtLoopProtectAction_Type.__name__ = "Integer32"
_AtLoopProtectAction_Object = MibScalar
atLoopProtectAction = _AtLoopProtectAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 1),
    _AtLoopProtectAction_Type()
)
atLoopProtectAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    atLoopProtectAction.setStatus("current")
_AtLoopProtectIfIndex_Type = InterfaceIndex
_AtLoopProtectIfIndex_Object = MibScalar
atLoopProtectIfIndex = _AtLoopProtectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 2),
    _AtLoopProtectIfIndex_Type()
)
atLoopProtectIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLoopProtectIfIndex.setStatus("current")
_AtLoopProtectVlanId_Type = Integer32
_AtLoopProtectVlanId_Object = MibScalar
atLoopProtectVlanId = _AtLoopProtectVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 3),
    _AtLoopProtectVlanId_Type()
)
atLoopProtectVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLoopProtectVlanId.setStatus("current")
_AtLoopProtectRxLDFIfIndex_Type = InterfaceIndex
_AtLoopProtectRxLDFIfIndex_Object = MibScalar
atLoopProtectRxLDFIfIndex = _AtLoopProtectRxLDFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 4),
    _AtLoopProtectRxLDFIfIndex_Type()
)
atLoopProtectRxLDFIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLoopProtectRxLDFIfIndex.setStatus("current")
_AtLoopProtectRxLDFVlanId_Type = Integer32
_AtLoopProtectRxLDFVlanId_Object = MibScalar
atLoopProtectRxLDFVlanId = _AtLoopProtectRxLDFVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 5),
    _AtLoopProtectRxLDFVlanId_Type()
)
atLoopProtectRxLDFVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLoopProtectRxLDFVlanId.setStatus("current")

# Managed Objects groups


# Notification objects

atLoopProtectDetectedLoopBlockedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 0, 1)
)
atLoopProtectDetectedLoopBlockedTrap.setObjects(
      *(("AT-LOOPPROTECT-MIB", "atLoopProtectIfIndex"),
        ("AT-LOOPPROTECT-MIB", "atLoopProtectVlanId"),
        ("AT-LOOPPROTECT-MIB", "atLoopProtectAction"))
)
if mibBuilder.loadTexts:
    atLoopProtectDetectedLoopBlockedTrap.setStatus(
        "current"
    )

atLoopProtectRecoverLoopBlockedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 0, 2)
)
atLoopProtectRecoverLoopBlockedTrap.setObjects(
      *(("AT-LOOPPROTECT-MIB", "atLoopProtectIfIndex"),
        ("AT-LOOPPROTECT-MIB", "atLoopProtectVlanId"),
        ("AT-LOOPPROTECT-MIB", "atLoopProtectAction"))
)
if mibBuilder.loadTexts:
    atLoopProtectRecoverLoopBlockedTrap.setStatus(
        "current"
    )

atLoopProtectDetectedByLoopDetectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 0, 3)
)
atLoopProtectDetectedByLoopDetectionTrap.setObjects(
      *(("AT-LOOPPROTECT-MIB", "atLoopProtectIfIndex"),
        ("AT-LOOPPROTECT-MIB", "atLoopProtectVlanId"),
        ("AT-LOOPPROTECT-MIB", "atLoopProtectRxLDFIfIndex"),
        ("AT-LOOPPROTECT-MIB", "atLoopProtectRxLDFVlanId"))
)
if mibBuilder.loadTexts:
    atLoopProtectDetectedByLoopDetectionTrap.setStatus(
        "current"
    )

atLoopProtectDetectedByThrashLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 0, 4)
)
atLoopProtectDetectedByThrashLimitTrap.setObjects(
      *(("AT-LOOPPROTECT-MIB", "atLoopProtectIfIndex"),
        ("AT-LOOPPROTECT-MIB", "atLoopProtectVlanId"))
)
if mibBuilder.loadTexts:
    atLoopProtectDetectedByThrashLimitTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-LOOPPROTECT-MIB",
    **{"atLoopProtect": atLoopProtect,
       "atLoopProtectTrap": atLoopProtectTrap,
       "atLoopProtectDetectedLoopBlockedTrap": atLoopProtectDetectedLoopBlockedTrap,
       "atLoopProtectRecoverLoopBlockedTrap": atLoopProtectRecoverLoopBlockedTrap,
       "atLoopProtectDetectedByLoopDetectionTrap": atLoopProtectDetectedByLoopDetectionTrap,
       "atLoopProtectDetectedByThrashLimitTrap": atLoopProtectDetectedByThrashLimitTrap,
       "atLoopProtectAction": atLoopProtectAction,
       "atLoopProtectIfIndex": atLoopProtectIfIndex,
       "atLoopProtectVlanId": atLoopProtectVlanId,
       "atLoopProtectRxLDFIfIndex": atLoopProtectRxLDFIfIndex,
       "atLoopProtectRxLDFVlanId": atLoopProtectRxLDFVlanId}
)

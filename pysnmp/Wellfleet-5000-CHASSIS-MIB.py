# SNMP MIB module (Wellfleet-5000-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-5000-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:43 2024
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

(wfHardwareConfig,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfHardwareConfig")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfHw5000Chassis_ObjectIdentity = ObjectIdentity
wfHw5000Chassis = _WfHw5000Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 6)
)
_WfHw5000ChassisBase_ObjectIdentity = ObjectIdentity
wfHw5000ChassisBase = _WfHw5000ChassisBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 6, 1)
)


class _WfHw5000NumSlots_Type(Integer32):
    """Custom type wfHw5000NumSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfHw5000NumSlots_Type.__name__ = "Integer32"
_WfHw5000NumSlots_Object = MibScalar
wfHw5000NumSlots = _WfHw5000NumSlots_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 6, 1, 1),
    _WfHw5000NumSlots_Type()
)
wfHw5000NumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHw5000NumSlots.setStatus("mandatory")


class _WfHw5000BpSerialNumber_Type(DisplayString):
    """Custom type wfHw5000BpSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WfHw5000BpSerialNumber_Type.__name__ = "DisplayString"
_WfHw5000BpSerialNumber_Object = MibScalar
wfHw5000BpSerialNumber = _WfHw5000BpSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 6, 1, 2),
    _WfHw5000BpSerialNumber_Type()
)
wfHw5000BpSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHw5000BpSerialNumber.setStatus("mandatory")
_WfHw5000ModuleTable_Object = MibTable
wfHw5000ModuleTable = _WfHw5000ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    wfHw5000ModuleTable.setStatus("mandatory")
_WfHw5000ModuleEntry_Object = MibTableRow
wfHw5000ModuleEntry = _WfHw5000ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 6, 2, 1)
)
wfHw5000ModuleEntry.setIndexNames(
    (0, "Wellfleet-5000-CHASSIS-MIB", "wfHw5000ModuleSlot"),
)
if mibBuilder.loadTexts:
    wfHw5000ModuleEntry.setStatus("mandatory")


class _WfHw5000ModuleSlot_Type(Integer32):
    """Custom type wfHw5000ModuleSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_WfHw5000ModuleSlot_Type.__name__ = "Integer32"
_WfHw5000ModuleSlot_Object = MibTableColumn
wfHw5000ModuleSlot = _WfHw5000ModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 6, 2, 1, 1),
    _WfHw5000ModuleSlot_Type()
)
wfHw5000ModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHw5000ModuleSlot.setStatus("mandatory")


class _WfHw5000ModuleDescription_Type(DisplayString):
    """Custom type wfHw5000ModuleDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WfHw5000ModuleDescription_Type.__name__ = "DisplayString"
_WfHw5000ModuleDescription_Object = MibTableColumn
wfHw5000ModuleDescription = _WfHw5000ModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 6, 2, 1, 2),
    _WfHw5000ModuleDescription_Type()
)
wfHw5000ModuleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHw5000ModuleDescription.setStatus("mandatory")
_WfHw5000ModuleId_Type = Integer32
_WfHw5000ModuleId_Object = MibTableColumn
wfHw5000ModuleId = _WfHw5000ModuleId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 6, 2, 1, 3),
    _WfHw5000ModuleId_Type()
)
wfHw5000ModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHw5000ModuleId.setStatus("mandatory")


class _WfHw5000ModuleRev_Type(DisplayString):
    """Custom type wfHw5000ModuleRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WfHw5000ModuleRev_Type.__name__ = "DisplayString"
_WfHw5000ModuleRev_Object = MibTableColumn
wfHw5000ModuleRev = _WfHw5000ModuleRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 6, 2, 1, 4),
    _WfHw5000ModuleRev_Type()
)
wfHw5000ModuleRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHw5000ModuleRev.setStatus("mandatory")


class _WfHw5000ModuleSerialNumber_Type(DisplayString):
    """Custom type wfHw5000ModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WfHw5000ModuleSerialNumber_Type.__name__ = "DisplayString"
_WfHw5000ModuleSerialNumber_Object = MibTableColumn
wfHw5000ModuleSerialNumber = _WfHw5000ModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 6, 2, 1, 5),
    _WfHw5000ModuleSerialNumber_Type()
)
wfHw5000ModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHw5000ModuleSerialNumber.setStatus("mandatory")
_WfHw5000ModuleIpAddress_Type = IpAddress
_WfHw5000ModuleIpAddress_Object = MibTableColumn
wfHw5000ModuleIpAddress = _WfHw5000ModuleIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 6, 2, 1, 6),
    _WfHw5000ModuleIpAddress_Type()
)
wfHw5000ModuleIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHw5000ModuleIpAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-5000-CHASSIS-MIB",
    **{"wfHw5000Chassis": wfHw5000Chassis,
       "wfHw5000ChassisBase": wfHw5000ChassisBase,
       "wfHw5000NumSlots": wfHw5000NumSlots,
       "wfHw5000BpSerialNumber": wfHw5000BpSerialNumber,
       "wfHw5000ModuleTable": wfHw5000ModuleTable,
       "wfHw5000ModuleEntry": wfHw5000ModuleEntry,
       "wfHw5000ModuleSlot": wfHw5000ModuleSlot,
       "wfHw5000ModuleDescription": wfHw5000ModuleDescription,
       "wfHw5000ModuleId": wfHw5000ModuleId,
       "wfHw5000ModuleRev": wfHw5000ModuleRev,
       "wfHw5000ModuleSerialNumber": wfHw5000ModuleSerialNumber,
       "wfHw5000ModuleIpAddress": wfHw5000ModuleIpAddress}
)

# SNMP MIB module (CTRON-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-DEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:42 2024
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

(ctDevice,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctDevice")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CommonDev_ObjectIdentity = ObjectIdentity
commonDev = _CommonDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 1)
)
_ComDeviceIPAddress_Type = IpAddress
_ComDeviceIPAddress_Object = MibScalar
comDeviceIPAddress = _ComDeviceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 1, 1),
    _ComDeviceIPAddress_Type()
)
comDeviceIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comDeviceIPAddress.setStatus("mandatory")


class _ComDeviceTime_Type(DisplayString):
    """Custom type comDeviceTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_ComDeviceTime_Type.__name__ = "DisplayString"
_ComDeviceTime_Object = MibScalar
comDeviceTime = _ComDeviceTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 1, 2),
    _ComDeviceTime_Type()
)
comDeviceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comDeviceTime.setStatus("mandatory")


class _ComDeviceDate_Type(DisplayString):
    """Custom type comDeviceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ComDeviceDate_Type.__name__ = "DisplayString"
_ComDeviceDate_Object = MibScalar
comDeviceDate = _ComDeviceDate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 1, 3),
    _ComDeviceDate_Type()
)
comDeviceDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comDeviceDate.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-DEVICE-MIB",
    **{"commonDev": commonDev,
       "comDeviceIPAddress": comDeviceIPAddress,
       "comDeviceTime": comDeviceTime,
       "comDeviceDate": comDeviceDate}
)

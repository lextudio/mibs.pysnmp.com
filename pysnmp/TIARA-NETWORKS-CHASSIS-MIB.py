# SNMP MIB module (TIARA-NETWORKS-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-NETWORKS-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:36 2024
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

(tiaraMgmt,) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-SMI",
    "tiaraMgmt")


# MODULE-IDENTITY

tiaraChassisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 2)
)
tiaraChassisMib.setRevisions(
        ("1900-01-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ChassisType_Type(DisplayString):
    """Custom type chassisType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChassisType_Type.__name__ = "DisplayString"
_ChassisType_Object = MibScalar
chassisType = _ChassisType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 2, 1),
    _ChassisType_Type()
)
chassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisType.setStatus("current")


class _ChassisSerialNumber_Type(DisplayString):
    """Custom type chassisSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_ChassisSerialNumber_Type.__name__ = "DisplayString"
_ChassisSerialNumber_Object = MibScalar
chassisSerialNumber = _ChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 2, 2),
    _ChassisSerialNumber_Type()
)
chassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSerialNumber.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-NETWORKS-CHASSIS-MIB",
    **{"tiaraChassisMib": tiaraChassisMib,
       "chassisType": chassisType,
       "chassisSerialNumber": chassisSerialNumber}
)

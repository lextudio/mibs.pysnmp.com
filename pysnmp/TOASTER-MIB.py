# SNMP MIB module (TOASTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TOASTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:31 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Epilogue_ObjectIdentity = ObjectIdentity
epilogue = _Epilogue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12)
)
_Toaster_ObjectIdentity = ObjectIdentity
toaster = _Toaster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12, 2)
)
_ToasterManufacturer_Type = DisplayString
_ToasterManufacturer_Object = MibScalar
toasterManufacturer = _ToasterManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 12, 2, 1),
    _ToasterManufacturer_Type()
)
toasterManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    toasterManufacturer.setStatus("mandatory")
_ToasterModelNumber_Type = DisplayString
_ToasterModelNumber_Object = MibScalar
toasterModelNumber = _ToasterModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 12, 2, 2),
    _ToasterModelNumber_Type()
)
toasterModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    toasterModelNumber.setStatus("mandatory")


class _ToasterControl_Type(Integer32):
    """Custom type toasterControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ToasterControl_Type.__name__ = "Integer32"
_ToasterControl_Object = MibScalar
toasterControl = _ToasterControl_Object(
    (1, 3, 6, 1, 4, 1, 12, 2, 3),
    _ToasterControl_Type()
)
toasterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    toasterControl.setStatus("mandatory")


class _ToasterDoneness_Type(Integer32):
    """Custom type toasterDoneness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ToasterDoneness_Type.__name__ = "Integer32"
_ToasterDoneness_Object = MibScalar
toasterDoneness = _ToasterDoneness_Object(
    (1, 3, 6, 1, 4, 1, 12, 2, 4),
    _ToasterDoneness_Type()
)
toasterDoneness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    toasterDoneness.setStatus("mandatory")


class _ToasterToastType_Type(Integer32):
    """Custom type toasterToastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("frozen-bagel", 5),
          ("frozen-waffle", 4),
          ("hash-brown", 6),
          ("other", 7),
          ("wheat-bread", 2),
          ("white-bread", 1),
          ("wonder-bread", 3))
    )


_ToasterToastType_Type.__name__ = "Integer32"
_ToasterToastType_Object = MibScalar
toasterToastType = _ToasterToastType_Object(
    (1, 3, 6, 1, 4, 1, 12, 2, 5),
    _ToasterToastType_Type()
)
toasterToastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    toasterToastType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TOASTER-MIB",
    **{"epilogue": epilogue,
       "toaster": toaster,
       "toasterManufacturer": toasterManufacturer,
       "toasterModelNumber": toasterModelNumber,
       "toasterControl": toasterControl,
       "toasterDoneness": toasterDoneness,
       "toasterToastType": toasterToastType}
)

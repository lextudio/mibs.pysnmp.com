# SNMP MIB module (EPON-EOC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EPON-EOC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:53 2024
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

eponeoc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34592)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OperSwitch(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )



class DeviceStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 5),
          ("normal", 4),
          ("notPresent", 1),
          ("offline", 2),
          ("online", 3))
    )



class DataDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("upstream", 1))
    )



class DeviceOperation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("delete", 6),
          ("reset", 2),
          ("restore", 5),
          ("saveConfig", 4))
    )



class LedStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blink", 3),
          ("off", 2),
          ("on", 1))
    )



class DeviceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16842752,
              16843009,
              16974083,
              16974084,
              16974086,
              16974087,
              16974088,
              16974089,
              16974090,
              16974091,
              16974092,
              16974094,
              16974095,
              16974337,
              16974338,
              16974593,
              16974594,
              16974850,
              17039617,
              17040129,
              17105153,
              17105409,
              17105665,
              825241960,
              825242728,
              825307496,
              825307757,
              825308269,
              858797160)
        )
    )
    namedValues = NamedValues(
        *(("CHASSIS", 16843009),
          ("EPON", 16842752),
          ("EPON-1U", 17105153),
          ("OLT", 17105409),
          ("ONU1D", 16974086),
          ("ONU1D-G", 16974087),
          ("ONU1FE", 825241960),
          ("ONU1GE", 825307496),
          ("ONU24D", 17039617),
          ("ONU2D-G", 16974088),
          ("ONU2D-GM", 16974095),
          ("ONU2D-M", 16974092),
          ("ONU2GE", 825307757),
          ("ONU3D-M", 16974090),
          ("ONU4D", 16974091),
          ("ONU4D-B", 16974083),
          ("ONU4D-GM", 16974094),
          ("ONU4D-P", 16974089),
          ("ONU4D1R", 16974593),
          ("ONU4D1R-P", 16974594),
          ("ONU4D2P", 16974337),
          ("ONU4D2P-P", 16974338),
          ("ONU4D2P1R", 17040129),
          ("ONU4D2P1R-P", 16974850),
          ("ONU4FE", 825242728),
          ("ONU4FE1RF", 858797160),
          ("ONU4GE", 825308269),
          ("ONU8D-B", 16974084),
          ("PON", 17105665))
    )



# MIB Managed Objects in the order of their OIDs

_IpProduct_ObjectIdentity = ObjectIdentity
ipProduct = _IpProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1)
)
if mibBuilder.loadTexts:
    ipProduct.setStatus("current")
_MediaConverter_ObjectIdentity = ObjectIdentity
mediaConverter = _MediaConverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1)
)
if mibBuilder.loadTexts:
    mediaConverter.setStatus("current")
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 2)
)
if mibBuilder.loadTexts:
    switch.setStatus("current")
_Epon_ObjectIdentity = ObjectIdentity
epon = _Epon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3)
)
if mibBuilder.loadTexts:
    epon.setStatus("current")
_Eoc_ObjectIdentity = ObjectIdentity
eoc = _Eoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 4)
)
if mibBuilder.loadTexts:
    eoc.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EPON-EOC-MIB",
    **{"OperSwitch": OperSwitch,
       "DeviceStatus": DeviceStatus,
       "DataDirection": DataDirection,
       "DeviceOperation": DeviceOperation,
       "LedStatus": LedStatus,
       "DeviceType": DeviceType,
       "eponeoc": eponeoc,
       "ipProduct": ipProduct,
       "mediaConverter": mediaConverter,
       "switch": switch,
       "epon": epon,
       "eoc": eoc}
)

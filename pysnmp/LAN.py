# SNMP MIB module (LAN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LAN
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:50 2024
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lanInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortSpeedType(Integer32, TextualConvention):
    status = "current"
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
        *(("auto", 1),
          ("fullDulplex10", 2),
          ("fullDulplex100", 4),
          ("fullDulplex1000", 6),
          ("halfDulplex10", 3),
          ("halfDulplex100", 5),
          ("halfDulplex1000", 7),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_Pepwave_ObjectIdentity = ObjectIdentity
pepwave = _Pepwave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662)
)
_ProductMib_ObjectIdentity = ObjectIdentity
productMib = _ProductMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200)
)
_GeneralMib_ObjectIdentity = ObjectIdentity
generalMib = _GeneralMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1)
)
_LanMib_ObjectIdentity = ObjectIdentity
lanMib = _LanMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 3)
)
_LanStatus_ObjectIdentity = ObjectIdentity
lanStatus = _LanStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 3, 1, 1)
)
_LanIp_Type = IpAddress
_LanIp_Object = MibScalar
lanIp = _LanIp_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 3, 1, 1, 1),
    _LanIp_Type()
)
lanIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanIp.setStatus("current")
_LanSubnetMask_Type = IpAddress
_LanSubnetMask_Object = MibScalar
lanSubnetMask = _LanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 3, 1, 1, 2),
    _LanSubnetMask_Type()
)
lanSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSubnetMask.setStatus("current")
_LanSpeed_Type = PortSpeedType
_LanSpeed_Object = MibScalar
lanSpeed = _LanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 3, 1, 1, 3),
    _LanSpeed_Type()
)
lanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanSpeed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LAN",
    **{"PortSpeedType": PortSpeedType,
       "pepwave": pepwave,
       "productMib": productMib,
       "generalMib": generalMib,
       "lanMib": lanMib,
       "lanInfo": lanInfo,
       "lanStatus": lanStatus,
       "lanIp": lanIp,
       "lanSubnetMask": lanSubnetMask,
       "lanSpeed": lanSpeed}
)

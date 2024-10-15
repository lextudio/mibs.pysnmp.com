# SNMP MIB module (CTRON-UPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-UPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:51 2024
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

(ctUPowerSupply,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctUPowerSupply")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtUPS_ObjectIdentity = ObjectIdentity
ctUPS = _CtUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4, 1)
)


class _CtUpsID_Type(Integer32):
    """Custom type ctUpsID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268)
        )
    )
    namedValues = NamedValues(
        *(("aPCGeneric", 268),
          ("aPCModel1250", 261),
          ("aPCModel2000", 262),
          ("aPCModel370", 257),
          ("aPCModel400", 258),
          ("aPCModel600", 259),
          ("aPCModel900", 260),
          ("matrix3000", 263),
          ("matrix5000", 264),
          ("other", 1),
          ("su1400", 266),
          ("su2000XL", 267),
          ("su700", 265))
    )


_CtUpsID_Type.__name__ = "Integer32"
_CtUpsID_Object = MibScalar
ctUpsID = _CtUpsID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4, 1, 1),
    _CtUpsID_Type()
)
ctUpsID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctUpsID.setStatus("mandatory")
_CtUpsUpTime_Type = Integer32
_CtUpsUpTime_Object = MibScalar
ctUpsUpTime = _CtUpsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4, 1, 2),
    _CtUpsUpTime_Type()
)
ctUpsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctUpsUpTime.setStatus("deprecated")
_CtUpsDisable_Type = Integer32
_CtUpsDisable_Object = MibScalar
ctUpsDisable = _CtUpsDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4, 1, 3),
    _CtUpsDisable_Type()
)
ctUpsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctUpsDisable.setStatus("deprecated")
_CtUpsDisconnect_Type = Integer32
_CtUpsDisconnect_Object = MibScalar
ctUpsDisconnect = _CtUpsDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4, 1, 4),
    _CtUpsDisconnect_Type()
)
ctUpsDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctUpsDisconnect.setStatus("mandatory")


class _CtUpsTest_Type(Integer32):
    """Custom type ctUpsTest based on Integer32"""
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
        *(("badBattery", 3),
          ("noRecentTest", 4),
          ("underTest", 5),
          ("unitFailed", 2),
          ("unitOK", 1))
    )


_CtUpsTest_Type.__name__ = "Integer32"
_CtUpsTest_Object = MibScalar
ctUpsTest = _CtUpsTest_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4, 1, 5),
    _CtUpsTest_Type()
)
ctUpsTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctUpsTest.setStatus("mandatory")
_CtUpsBatteryCapacity_Type = Integer32
_CtUpsBatteryCapacity_Object = MibScalar
ctUpsBatteryCapacity = _CtUpsBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4, 1, 6),
    _CtUpsBatteryCapacity_Type()
)
ctUpsBatteryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctUpsBatteryCapacity.setStatus("mandatory")
_CtUpsACLineVoltsIn_Type = Integer32
_CtUpsACLineVoltsIn_Object = MibScalar
ctUpsACLineVoltsIn = _CtUpsACLineVoltsIn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4, 1, 7),
    _CtUpsACLineVoltsIn_Type()
)
ctUpsACLineVoltsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctUpsACLineVoltsIn.setStatus("mandatory")
_CtUpsBatteryVoltsOut_Type = Integer32
_CtUpsBatteryVoltsOut_Object = MibScalar
ctUpsBatteryVoltsOut = _CtUpsBatteryVoltsOut_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4, 1, 8),
    _CtUpsBatteryVoltsOut_Type()
)
ctUpsBatteryVoltsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctUpsBatteryVoltsOut.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-UPS-MIB",
    **{"ctUPS": ctUPS,
       "ctUpsID": ctUpsID,
       "ctUpsUpTime": ctUpsUpTime,
       "ctUpsDisable": ctUpsDisable,
       "ctUpsDisconnect": ctUpsDisconnect,
       "ctUpsTest": ctUpsTest,
       "ctUpsBatteryCapacity": ctUpsBatteryCapacity,
       "ctUpsACLineVoltsIn": ctUpsACLineVoltsIn,
       "ctUpsBatteryVoltsOut": ctUpsBatteryVoltsOut}
)

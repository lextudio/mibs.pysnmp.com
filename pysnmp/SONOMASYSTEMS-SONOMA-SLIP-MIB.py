# SNMP MIB module (SONOMASYSTEMS-SONOMA-SLIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONOMASYSTEMS-SONOMA-SLIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:47 2024
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

(sonomaApplications,) = mibBuilder.importSymbols(
    "SONOMASYSTEMS-SONOMA-MIB",
    "sonomaApplications")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Slip_ObjectIdentity = ObjectIdentity
slip = _Slip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 2)
)


class _SlipSpeed_Type(Integer32):
    """Custom type slipSpeed based on Integer32"""
    defaultValue = 3

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
        *(("sp115200", 7),
          ("sp19200", 4),
          ("sp2400", 1),
          ("sp38400", 5),
          ("sp4800", 2),
          ("sp57600", 6),
          ("sp9600", 3))
    )


_SlipSpeed_Type.__name__ = "Integer32"
_SlipSpeed_Object = MibScalar
slipSpeed = _SlipSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 2, 1),
    _SlipSpeed_Type()
)
slipSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slipSpeed.setStatus("mandatory")


class _SlipDataBits_Type(Integer32):
    """Custom type slipDataBits based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("db8", 3)
    )


_SlipDataBits_Type.__name__ = "Integer32"
_SlipDataBits_Object = MibScalar
slipDataBits = _SlipDataBits_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 2, 2),
    _SlipDataBits_Type()
)
slipDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipDataBits.setStatus("mandatory")


class _SlipParity_Type(Integer32):
    """Custom type slipParity based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("none", 3)
    )


_SlipParity_Type.__name__ = "Integer32"
_SlipParity_Object = MibScalar
slipParity = _SlipParity_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 2, 3),
    _SlipParity_Type()
)
slipParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipParity.setStatus("mandatory")


class _SlipStopBits_Type(Integer32):
    """Custom type slipStopBits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sb1", 1),
          ("sb2", 2))
    )


_SlipStopBits_Type.__name__ = "Integer32"
_SlipStopBits_Object = MibScalar
slipStopBits = _SlipStopBits_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 2, 4),
    _SlipStopBits_Type()
)
slipStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slipStopBits.setStatus("mandatory")


class _SlipFlowControl_Type(Integer32):
    """Custom type slipFlowControl based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("none", 3)
    )


_SlipFlowControl_Type.__name__ = "Integer32"
_SlipFlowControl_Object = MibScalar
slipFlowControl = _SlipFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 2, 5),
    _SlipFlowControl_Type()
)
slipFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipFlowControl.setStatus("mandatory")


class _SlipType_Type(Integer32):
    """Custom type slipType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compressed", 2),
          ("uncompressed", 1))
    )


_SlipType_Type.__name__ = "Integer32"
_SlipType_Object = MibScalar
slipType = _SlipType_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 2, 6),
    _SlipType_Type()
)
slipType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slipType.setStatus("mandatory")


class _SlipMtu_Type(Integer32):
    """Custom type slipMtu based on Integer32"""
    defaultValue = 1006

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_SlipMtu_Type.__name__ = "Integer32"
_SlipMtu_Object = MibScalar
slipMtu = _SlipMtu_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 8, 2, 7),
    _SlipMtu_Type()
)
slipMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slipMtu.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONOMASYSTEMS-SONOMA-SLIP-MIB",
    **{"slip": slip,
       "slipSpeed": slipSpeed,
       "slipDataBits": slipDataBits,
       "slipParity": slipParity,
       "slipStopBits": slipStopBits,
       "slipFlowControl": slipFlowControl,
       "slipType": slipType,
       "slipMtu": slipMtu}
)

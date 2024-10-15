# SNMP MIB module (BIANCA-BRICK-HIDDENVPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-HIDDENVPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:28 2024
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

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Admin_ObjectIdentity = ObjectIdentity
admin = _Admin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 1)
)
_BiboAdmLed_ObjectIdentity = ObjectIdentity
biboAdmLed = _BiboAdmLed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 253)
)


class _BiboAdmLedStatus_Type(Integer32):
    """Custom type biboAdmLedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blink", 3),
          ("flash", 4),
          ("off", 1),
          ("on", 2))
    )


_BiboAdmLedStatus_Type.__name__ = "Integer32"
_BiboAdmLedStatus_Object = MibScalar
biboAdmLedStatus = _BiboAdmLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 253, 1),
    _BiboAdmLedStatus_Type()
)
biboAdmLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmLedStatus.setStatus("mandatory")


class _BiboAdmLedMgmt_Type(Integer32):
    """Custom type biboAdmLedMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blink", 3),
          ("flash", 4),
          ("off", 1),
          ("on", 2))
    )


_BiboAdmLedMgmt_Type.__name__ = "Integer32"
_BiboAdmLedMgmt_Object = MibScalar
biboAdmLedMgmt = _BiboAdmLedMgmt_Object(
    (1, 3, 6, 1, 4, 1, 272, 253, 2),
    _BiboAdmLedMgmt_Type()
)
biboAdmLedMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmLedMgmt.setStatus("mandatory")


class _BiboAdmLedHA_Type(Integer32):
    """Custom type biboAdmLedHA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blink", 3),
          ("flash", 4),
          ("off", 1),
          ("on", 2))
    )


_BiboAdmLedHA_Type.__name__ = "Integer32"
_BiboAdmLedHA_Object = MibScalar
biboAdmLedHA = _BiboAdmLedHA_Object(
    (1, 3, 6, 1, 4, 1, 272, 253, 3),
    _BiboAdmLedHA_Type()
)
biboAdmLedHA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmLedHA.setStatus("mandatory")


class _BiboAdmLedInternet_Type(Integer32):
    """Custom type biboAdmLedInternet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blink", 3),
          ("flash", 4),
          ("off", 1),
          ("on", 2))
    )


_BiboAdmLedInternet_Type.__name__ = "Integer32"
_BiboAdmLedInternet_Object = MibScalar
biboAdmLedInternet = _BiboAdmLedInternet_Object(
    (1, 3, 6, 1, 4, 1, 272, 253, 4),
    _BiboAdmLedInternet_Type()
)
biboAdmLedInternet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmLedInternet.setStatus("mandatory")


class _BiboAdmLedSwitch_Type(Integer32):
    """Custom type biboAdmLedSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blink", 3),
          ("linkact", 4),
          ("off", 1),
          ("on", 2))
    )


_BiboAdmLedSwitch_Type.__name__ = "Integer32"
_BiboAdmLedSwitch_Object = MibScalar
biboAdmLedSwitch = _BiboAdmLedSwitch_Object(
    (1, 3, 6, 1, 4, 1, 272, 253, 5),
    _BiboAdmLedSwitch_Type()
)
biboAdmLedSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboAdmLedSwitch.setStatus("mandatory")


class _BiboAdmLedMeter_Type(Integer32):
    """Custom type biboAdmLedMeter based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_BiboAdmLedMeter_Type.__name__ = "Integer32"
_BiboAdmLedMeter_Object = MibScalar
biboAdmLedMeter = _BiboAdmLedMeter_Object(
    (1, 3, 6, 1, 4, 1, 272, 253, 6),
    _BiboAdmLedMeter_Type()
)
biboAdmLedMeter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboAdmLedMeter.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-HIDDENVPN-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "admin": admin,
       "biboAdmLed": biboAdmLed,
       "biboAdmLedStatus": biboAdmLedStatus,
       "biboAdmLedMgmt": biboAdmLedMgmt,
       "biboAdmLedHA": biboAdmLedHA,
       "biboAdmLedInternet": biboAdmLedInternet,
       "biboAdmLedSwitch": biboAdmLedSwitch,
       "biboAdmLedMeter": biboAdmLedMeter}
)

# SNMP MIB module (RADLAN-BaudRate-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-BaudRate-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:50 2024
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

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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

rlRs232 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 104)
)
rlRs232.setRevisions(
        ("2005-04-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlRs232MibVersion_Type = Integer32
_RlRs232MibVersion_Object = MibScalar
rlRs232MibVersion = _RlRs232MibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 104, 1),
    _RlRs232MibVersion_Type()
)
rlRs232MibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRs232MibVersion.setStatus("current")


class _RlRs232AutoBaudRateStatus_Type(Integer32):
    """Custom type rlRs232AutoBaudRateStatus based on Integer32"""
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


_RlRs232AutoBaudRateStatus_Type.__name__ = "Integer32"
_RlRs232AutoBaudRateStatus_Object = MibScalar
rlRs232AutoBaudRateStatus = _RlRs232AutoBaudRateStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 104, 2),
    _RlRs232AutoBaudRateStatus_Type()
)
rlRs232AutoBaudRateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRs232AutoBaudRateStatus.setStatus("current")


class _RlRs232AutoBaudRateStatusAfterReset_Type(Integer32):
    """Custom type rlRs232AutoBaudRateStatusAfterReset based on Integer32"""
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


_RlRs232AutoBaudRateStatusAfterReset_Type.__name__ = "Integer32"
_RlRs232AutoBaudRateStatusAfterReset_Object = MibScalar
rlRs232AutoBaudRateStatusAfterReset = _RlRs232AutoBaudRateStatusAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 104, 3),
    _RlRs232AutoBaudRateStatusAfterReset_Type()
)
rlRs232AutoBaudRateStatusAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRs232AutoBaudRateStatusAfterReset.setStatus("current")


class _RlRs232BaudRate_Type(Integer32):
    """Custom type rlRs232BaudRate based on Integer32"""
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
        *(("baud115200", 7),
          ("baud19200", 4),
          ("baud2400", 1),
          ("baud38400", 5),
          ("baud4800", 2),
          ("baud57600", 6),
          ("baud9600", 3))
    )


_RlRs232BaudRate_Type.__name__ = "Integer32"
_RlRs232BaudRate_Object = MibScalar
rlRs232BaudRate = _RlRs232BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 104, 4),
    _RlRs232BaudRate_Type()
)
rlRs232BaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRs232BaudRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-BaudRate-MIB",
    **{"rlRs232": rlRs232,
       "rlRs232MibVersion": rlRs232MibVersion,
       "rlRs232AutoBaudRateStatus": rlRs232AutoBaudRateStatus,
       "rlRs232AutoBaudRateStatusAfterReset": rlRs232AutoBaudRateStatusAfterReset,
       "rlRs232BaudRate": rlRs232BaudRate}
)

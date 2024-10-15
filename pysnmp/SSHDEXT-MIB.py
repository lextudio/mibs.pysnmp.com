# SNMP MIB module (SSHDEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SSHDEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:45 2024
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

(sshdExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "sshdExt")

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

apSshdMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 43, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApSshdKeepAlive_Type(Integer32):
    """Custom type apSshdKeepAlive based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSshdKeepAlive_Type.__name__ = "Integer32"
_ApSshdKeepAlive_Object = MibScalar
apSshdKeepAlive = _ApSshdKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 43, 2),
    _ApSshdKeepAlive_Type()
)
apSshdKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSshdKeepAlive.setStatus("current")


class _ApSshdKeyRegenerationInterval_Type(Integer32):
    """Custom type apSshdKeyRegenerationInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_ApSshdKeyRegenerationInterval_Type.__name__ = "Integer32"
_ApSshdKeyRegenerationInterval_Object = MibScalar
apSshdKeyRegenerationInterval = _ApSshdKeyRegenerationInterval_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 43, 3),
    _ApSshdKeyRegenerationInterval_Type()
)
apSshdKeyRegenerationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSshdKeyRegenerationInterval.setStatus("current")


class _ApSshdPort_Type(Integer32):
    """Custom type apSshdPort based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22, 65535),
    )


_ApSshdPort_Type.__name__ = "Integer32"
_ApSshdPort_Object = MibScalar
apSshdPort = _ApSshdPort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 43, 4),
    _ApSshdPort_Type()
)
apSshdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSshdPort.setStatus("current")


class _ApSshdServerKeyBits_Type(Integer32):
    """Custom type apSshdServerKeyBits based on Integer32"""
    defaultValue = 768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 65535),
    )


_ApSshdServerKeyBits_Type.__name__ = "Integer32"
_ApSshdServerKeyBits_Object = MibScalar
apSshdServerKeyBits = _ApSshdServerKeyBits_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 43, 5),
    _ApSshdServerKeyBits_Type()
)
apSshdServerKeyBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSshdServerKeyBits.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SSHDEXT-MIB",
    **{"apSshdMib": apSshdMib,
       "apSshdKeepAlive": apSshdKeepAlive,
       "apSshdKeyRegenerationInterval": apSshdKeyRegenerationInterval,
       "apSshdPort": apSshdPort,
       "apSshdServerKeyBits": apSshdServerKeyBits}
)

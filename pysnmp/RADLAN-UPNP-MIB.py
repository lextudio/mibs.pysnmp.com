# SNMP MIB module (RADLAN-UPNP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-UPNP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:43:53 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlUPnP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 109)
)
rlUPnP.setRevisions(
        ("2006-03-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlUPnPUniqueDeviceName_Type = DisplayString
_RlUPnPUniqueDeviceName_Object = MibScalar
rlUPnPUniqueDeviceName = _RlUPnPUniqueDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 89, 109, 1),
    _RlUPnPUniqueDeviceName_Type()
)
rlUPnPUniqueDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlUPnPUniqueDeviceName.setStatus("current")


class _RlUPnPEnabling_Type(Integer32):
    """Custom type rlUPnPEnabling based on Integer32"""
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


_RlUPnPEnabling_Type.__name__ = "Integer32"
_RlUPnPEnabling_Object = MibScalar
rlUPnPEnabling = _RlUPnPEnabling_Object(
    (1, 3, 6, 1, 4, 1, 89, 109, 2),
    _RlUPnPEnabling_Type()
)
rlUPnPEnabling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlUPnPEnabling.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-UPNP-MIB",
    **{"rlUPnP": rlUPnP,
       "rlUPnPUniqueDeviceName": rlUPnPUniqueDeviceName,
       "rlUPnPEnabling": rlUPnPEnabling}
)

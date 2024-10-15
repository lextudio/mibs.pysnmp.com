# SNMP MIB module (HPNSARPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPNSARPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:24 2024
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

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaRPS_ObjectIdentity = ObjectIdentity
hpnsaRPS = _HpnsaRPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 22)
)
_HpnsaRPSMibRev_ObjectIdentity = ObjectIdentity
hpnsaRPSMibRev = _HpnsaRPSMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 22, 1)
)


class _HpnsaRPSMibRevMajor_Type(Integer32):
    """Custom type hpnsaRPSMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnsaRPSMibRevMajor_Type.__name__ = "Integer32"
_HpnsaRPSMibRevMajor_Object = MibScalar
hpnsaRPSMibRevMajor = _HpnsaRPSMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 22, 1, 1),
    _HpnsaRPSMibRevMajor_Type()
)
hpnsaRPSMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRPSMibRevMajor.setStatus("mandatory")


class _HpnsaRPSMibRevMinor_Type(Integer32):
    """Custom type hpnsaRPSMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaRPSMibRevMinor_Type.__name__ = "Integer32"
_HpnsaRPSMibRevMinor_Object = MibScalar
hpnsaRPSMibRevMinor = _HpnsaRPSMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 22, 1, 2),
    _HpnsaRPSMibRevMinor_Type()
)
hpnsaRPSMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaRPSMibRevMinor.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSARPS-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaRPS": hpnsaRPS,
       "hpnsaRPSMibRev": hpnsaRPSMibRev,
       "hpnsaRPSMibRevMajor": hpnsaRPSMibRevMajor,
       "hpnsaRPSMibRevMinor": hpnsaRPSMibRevMinor}
)

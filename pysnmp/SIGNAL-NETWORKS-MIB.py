# SNMP MIB module (SIGNAL-NETWORKS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SIGNAL-NETWORKS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:52:18 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Signal_networks_ObjectIdentity = ObjectIdentity
signal_networks = _Signal_networks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27243)
)
_Icm_ObjectIdentity = ObjectIdentity
icm = _Icm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27243, 1)
)
_Icm_system_ObjectIdentity = ObjectIdentity
icm_system = _Icm_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27243, 1, 1)
)


class _IcmDescr_Type(DisplayString):
    """Custom type icmDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IcmDescr_Type.__name__ = "DisplayString"
_IcmDescr_Object = MibScalar
icmDescr = _IcmDescr_Object(
    (1, 3, 6, 1, 4, 1, 27243, 1, 1, 1),
    _IcmDescr_Type()
)
icmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmDescr.setStatus("mandatory")


class _IcmContact_Type(DisplayString):
    """Custom type icmContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IcmContact_Type.__name__ = "DisplayString"
_IcmContact_Object = MibScalar
icmContact = _IcmContact_Object(
    (1, 3, 6, 1, 4, 1, 27243, 1, 1, 2),
    _IcmContact_Type()
)
icmContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmContact.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIGNAL-NETWORKS-MIB",
    **{"signal-networks": signal_networks,
       "icm": icm,
       "icm-system": icm_system,
       "icmDescr": icmDescr,
       "icmContact": icmContact}
)

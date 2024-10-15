# SNMP MIB module (TRAPEZE-NETWORKS-REGISTRATION-DEVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-REGISTRATION-DEVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:35 2024
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

(trpzRegistration,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzRegistration")


# MODULE-IDENTITY

trpzRegistrationDevicesMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 6)
)
trpzRegistrationDevicesMib.setRevisions(
        ("2011-08-09 00:32",
         "2011-03-08 00:22",
         "2010-12-02 00:11",
         "2009-12-18 00:10",
         "2007-11-30 00:01",
         "2007-08-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MobilityExchange_ObjectIdentity = ObjectIdentity
mobilityExchange = _MobilityExchange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 1)
)
_MobilityExchange20_ObjectIdentity = ObjectIdentity
mobilityExchange20 = _MobilityExchange20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 1, 1)
)
_MobilityExchange8_ObjectIdentity = ObjectIdentity
mobilityExchange8 = _MobilityExchange8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 1, 2)
)
_MobilityExchange400_ObjectIdentity = ObjectIdentity
mobilityExchange400 = _MobilityExchange400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 1, 3)
)
_MobilityExchangeR2_ObjectIdentity = ObjectIdentity
mobilityExchangeR2 = _MobilityExchangeR2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 1, 4)
)
_MobilityExchange216_ObjectIdentity = ObjectIdentity
mobilityExchange216 = _MobilityExchange216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 1, 6)
)
_MobilityExchange200_ObjectIdentity = ObjectIdentity
mobilityExchange200 = _MobilityExchange200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 1, 7)
)
_MobilityExchange2800_ObjectIdentity = ObjectIdentity
mobilityExchange2800 = _MobilityExchange2800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 1, 12)
)
_MobilityExchange800_ObjectIdentity = ObjectIdentity
mobilityExchange800 = _MobilityExchange800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 1, 13)
)
_MobilityPoint_ObjectIdentity = ObjectIdentity
mobilityPoint = _MobilityPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 2)
)
_MobilityPoint101_ObjectIdentity = ObjectIdentity
mobilityPoint101 = _MobilityPoint101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 2, 1)
)
_MobilityPoint122_ObjectIdentity = ObjectIdentity
mobilityPoint122 = _MobilityPoint122_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 2, 2)
)
_MobilityPoint241_ObjectIdentity = ObjectIdentity
mobilityPoint241 = _MobilityPoint241_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 2, 3)
)
_MobilityPoint252_ObjectIdentity = ObjectIdentity
mobilityPoint252 = _MobilityPoint252_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 2, 4)
)
_WirelessLANController_ObjectIdentity = ObjectIdentity
wirelessLANController = _WirelessLANController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 3)
)
_WirelessLANController880R_ObjectIdentity = ObjectIdentity
wirelessLANController880R = _WirelessLANController880R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 3, 1)
)
_WirelessLANController8_ObjectIdentity = ObjectIdentity
wirelessLANController8 = _WirelessLANController8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 3, 2)
)
_WirelessLANController2_ObjectIdentity = ObjectIdentity
wirelessLANController2 = _WirelessLANController2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 3, 3)
)
_WirelessLANController800r_ObjectIdentity = ObjectIdentity
wirelessLANController800r = _WirelessLANController800r_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 3, 4)
)
_WirelessLANController2800_ObjectIdentity = ObjectIdentity
wirelessLANController2800 = _WirelessLANController2800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 3, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-REGISTRATION-DEVICES-MIB",
    **{"mobilityExchange": mobilityExchange,
       "mobilityExchange20": mobilityExchange20,
       "mobilityExchange8": mobilityExchange8,
       "mobilityExchange400": mobilityExchange400,
       "mobilityExchangeR2": mobilityExchangeR2,
       "mobilityExchange216": mobilityExchange216,
       "mobilityExchange200": mobilityExchange200,
       "mobilityExchange2800": mobilityExchange2800,
       "mobilityExchange800": mobilityExchange800,
       "mobilityPoint": mobilityPoint,
       "mobilityPoint101": mobilityPoint101,
       "mobilityPoint122": mobilityPoint122,
       "mobilityPoint241": mobilityPoint241,
       "mobilityPoint252": mobilityPoint252,
       "wirelessLANController": wirelessLANController,
       "wirelessLANController880R": wirelessLANController880R,
       "wirelessLANController8": wirelessLANController8,
       "wirelessLANController2": wirelessLANController2,
       "wirelessLANController800r": wirelessLANController800r,
       "wirelessLANController2800": wirelessLANController2800,
       "trpzRegistrationDevicesMib": trpzRegistrationDevicesMib}
)

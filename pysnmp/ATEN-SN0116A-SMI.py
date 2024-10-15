# SNMP MIB module (ATEN-SN0116A-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATEN-SN0116A-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:43 2024
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

(sn3101,) = mibBuilder.importSymbols(
    "ATEN-PRODUCTS-MIB",
    "sn3101")

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

_Rs232_ObjectIdentity = ObjectIdentity
rs232 = _Rs232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2, 1)
)
_Usrcfg_ObjectIdentity = ObjectIdentity
usrcfg = _Usrcfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2, 2)
)
_Session_ObjectIdentity = ObjectIdentity
session = _Session_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2, 3)
)
_ImageCurrentVersion_ObjectIdentity = ObjectIdentity
imageCurrentVersion = _ImageCurrentVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2, 4)
)
_ImageNewVersion_ObjectIdentity = ObjectIdentity
imageNewVersion = _ImageNewVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2, 5)
)
_PortAlert_ObjectIdentity = ObjectIdentity
portAlert = _PortAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATEN-SN0116A-SMI",
    **{"rs232": rs232,
       "usrcfg": usrcfg,
       "session": session,
       "imageCurrentVersion": imageCurrentVersion,
       "imageNewVersion": imageNewVersion,
       "portAlert": portAlert}
)

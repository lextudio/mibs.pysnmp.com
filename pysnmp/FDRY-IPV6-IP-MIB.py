# SNMP MIB module (FDRY-IPV6-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FDRY-IPV6-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:41 2024
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

(RtrStatus,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-IP-MIB",
    "RtrStatus")

(fdryIpv6,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "fdryIpv6")

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

fdryIpv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1)
)
fdryIpv6MIB.setRevisions(
        ("2010-07-26 00:00",
         "2010-05-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FdryIpv6GlobalObjects_ObjectIdentity = ObjectIdentity
fdryIpv6GlobalObjects = _FdryIpv6GlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1, 1)
)
_FdryIpv6LoadShare_Type = RtrStatus
_FdryIpv6LoadShare_Object = MibScalar
fdryIpv6LoadShare = _FdryIpv6LoadShare_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1, 1, 1),
    _FdryIpv6LoadShare_Type()
)
fdryIpv6LoadShare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryIpv6LoadShare.setStatus("current")
_FdryIpv6LoadShareNumOfPaths_Type = Unsigned32
_FdryIpv6LoadShareNumOfPaths_Object = MibScalar
fdryIpv6LoadShareNumOfPaths = _FdryIpv6LoadShareNumOfPaths_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1, 1, 2),
    _FdryIpv6LoadShareNumOfPaths_Type()
)
fdryIpv6LoadShareNumOfPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryIpv6LoadShareNumOfPaths.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FDRY-IPV6-IP-MIB",
    **{"fdryIpv6MIB": fdryIpv6MIB,
       "fdryIpv6GlobalObjects": fdryIpv6GlobalObjects,
       "fdryIpv6LoadShare": fdryIpv6LoadShare,
       "fdryIpv6LoadShareNumOfPaths": fdryIpv6LoadShareNumOfPaths}
)

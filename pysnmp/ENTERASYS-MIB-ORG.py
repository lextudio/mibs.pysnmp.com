# SNMP MIB module (ENTERASYS-MIB-ORG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-MIB-ORG
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:12 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

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

etsysMibOrg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 3)
)
etsysMibOrg.setRevisions(
        ("2010-08-17 12:15",
         "2010-06-02 11:30",
         "2010-03-25 20:29",
         "2009-12-07 14:41",
         "2009-08-10 18:56",
         "2009-08-04 13:43",
         "2009-07-02 13:34",
         "2009-02-20 16:20",
         "2009-02-12 15:04",
         "2009-01-07 21:18",
         "2008-07-23 14:11",
         "2008-04-10 14:51",
         "2007-02-27 18:16",
         "2006-03-06 13:53",
         "2005-11-14 16:48",
         "2005-01-26 22:18",
         "2005-01-25 15:41",
         "2005-01-12 21:00",
         "2004-08-24 13:29",
         "2004-08-19 21:20",
         "2004-08-17 17:03",
         "2004-08-13 16:57",
         "2004-08-05 20:25",
         "2004-07-29 18:59",
         "2004-07-28 16:24",
         "2004-06-02 13:40",
         "2004-04-02 22:53",
         "2004-02-13 20:00",
         "2004-02-03 15:33",
         "2003-11-14 16:01",
         "2003-11-06 15:15",
         "2003-10-21 15:39",
         "2003-10-16 12:16",
         "2003-08-19 20:53",
         "2003-06-13 18:09",
         "2003-05-16 20:07",
         "2002-12-20 15:19",
         "2002-12-13 20:54",
         "2002-11-01 21:20",
         "2002-10-08 20:27",
         "2002-09-25 20:03",
         "2002-09-13 19:30",
         "2002-08-07 18:51",
         "2002-07-18 15:31",
         "2002-06-24 21:34",
         "2002-05-07 17:55",
         "2002-04-05 15:01",
         "2002-03-14 20:54",
         "2002-02-20 20:02",
         "2002-01-24 18:23",
         "2001-08-16 13:00",
         "2001-08-14 19:30",
         "2001-05-22 13:00",
         "2001-04-02 21:00",
         "2001-01-24 17:00",
         "2000-11-28 14:00",
         "2000-10-03 18:44")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-MIB-ORG",
    **{"etsysMibOrg": etsysMibOrg}
)

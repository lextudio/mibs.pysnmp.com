# SNMP MIB module (ENTERASYS-OIDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-OIDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:03 2024
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

(etsysModules,
 etsysOids) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules",
    "etsysOids")

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

enterasysOidsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 2)
)
enterasysOidsMib.setRevisions(
        ("2011-01-13 19:27",
         "2010-12-20 18:41",
         "2010-12-14 13:37",
         "2010-12-02 18:33",
         "2010-11-18 18:18",
         "2010-10-04 12:55",
         "2010-09-08 14:39",
         "2010-06-23 17:58",
         "2010-06-10 14:27",
         "2010-06-03 15:12",
         "2010-05-04 19:53",
         "2010-03-05 13:53",
         "2009-10-26 17:15",
         "2009-10-26 15:30",
         "2009-09-30 20:04",
         "2009-08-27 13:07",
         "2009-08-25 01:12",
         "2009-07-08 15:37",
         "2009-07-02 17:38",
         "2009-06-22 19:44",
         "2009-04-07 16:02",
         "2009-03-31 17:13",
         "2009-03-05 13:58",
         "2009-01-05 15:08",
         "2008-11-17 16:04",
         "2008-08-13 19:04",
         "2008-06-10 12:59",
         "2008-04-24 14:00",
         "2008-03-13 20:58",
         "2008-01-24 20:08",
         "2008-01-10 20:09",
         "2007-10-30 19:10",
         "2007-10-15 13:10",
         "2007-08-30 18:08",
         "2007-08-29 15:16",
         "2007-06-25 18:22",
         "2007-06-14 18:25",
         "2007-06-04 15:43",
         "2007-05-29 13:12",
         "2007-04-20 11:58",
         "2007-04-16 14:43",
         "2007-04-05 15:32",
         "2007-02-27 17:49",
         "2007-01-25 15:58",
         "2007-01-23 21:01",
         "2006-10-31 19:54",
         "2006-09-29 12:58",
         "2006-09-20 14:51",
         "2006-08-25 15:02",
         "2006-08-16 13:44",
         "2006-08-07 12:31",
         "2006-08-03 13:57",
         "2006-06-19 18:32",
         "2006-03-09 19:14",
         "2006-02-16 14:42",
         "2006-02-09 20:06",
         "2006-02-06 20:31",
         "2005-11-10 19:58",
         "2005-10-11 14:42",
         "2005-09-21 16:03",
         "2005-08-31 18:22",
         "2005-06-21 12:45",
         "2005-04-19 18:49",
         "2005-04-12 17:14",
         "2005-02-20 23:50",
         "2005-02-10 19:39",
         "2005-01-12 18:02",
         "2005-01-11 19:56",
         "2004-08-24 13:29",
         "2004-08-11 19:24",
         "2004-08-04 21:18",
         "2004-06-01 19:42",
         "2004-05-18 15:53",
         "2004-04-16 19:15",
         "2004-04-02 18:38",
         "2004-03-19 19:55",
         "2004-03-15 19:31",
         "2004-03-15 17:11",
         "2004-02-26 14:55",
         "2004-02-19 14:19",
         "2004-02-17 21:31",
         "2004-01-27 16:43",
         "2003-12-12 17:13",
         "2003-10-23 15:27",
         "2003-10-14 15:04",
         "2003-09-19 20:44",
         "2003-09-17 14:26",
         "2003-08-29 21:00",
         "2003-08-19 19:32",
         "2003-07-30 16:43",
         "2003-07-28 16:36",
         "2003-07-17 13:53",
         "2003-07-09 20:41",
         "2003-07-02 17:25",
         "2003-06-05 15:09",
         "2003-06-03 13:08",
         "2003-05-14 21:08",
         "2003-05-07 20:48",
         "2003-04-25 20:32",
         "2003-04-17 13:58",
         "2003-04-17 13:58",
         "2003-03-05 15:35",
         "2003-02-24 15:06",
         "2002-12-31 20:51",
         "2002-12-31 19:20",
         "2002-12-13 19:26",
         "2002-12-03 14:20",
         "2002-10-29 14:13",
         "2002-08-30 21:05",
         "2002-08-29 19:23",
         "2002-08-27 15:03",
         "2002-07-12 14:21",
         "2002-06-27 21:09",
         "2002-06-06 18:41",
         "2002-05-30 17:11",
         "2002-04-23 19:43",
         "2002-04-08 20:35",
         "2002-04-02 18:56",
         "2002-03-14 20:45",
         "2002-01-14 19:03",
         "2002-01-09 18:19",
         "2001-12-19 16:33",
         "2001-12-13 20:13",
         "2001-11-09 16:18",
         "2001-11-08 20:01",
         "2001-09-26 18:00",
         "2001-08-01 12:30",
         "2001-07-26 17:30",
         "2001-07-12 19:30",
         "2001-06-26 19:00",
         "2001-05-03 13:00",
         "2001-04-18 15:00",
         "2001-04-02 17:00",
         "2001-03-30 15:00",
         "2001-03-01 14:00",
         "2001-02-22 16:00",
         "2000-12-20 19:00",
         "2000-11-09 21:00",
         "2000-10-17 16:16",
         "2000-09-29 19:00",
         "2000-05-19 00:00",
         "2000-05-17 00:10",
         "2000-05-17 00:00",
         "2000-05-11 00:00",
         "2000-05-01 00:00",
         "2000-04-27 00:00",
         "2000-03-31 00:00",
         "2000-03-22 00:00",
         "2000-03-16 18:00",
         "2000-03-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysOidDevice_ObjectIdentity = ObjectIdentity
etsysOidDevice = _EtsysOidDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1)
)
_EtsysOidDevEmpty_ObjectIdentity = ObjectIdentity
etsysOidDevEmpty = _EtsysOidDevEmpty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysOidDevEmpty.setStatus("current")
_EtsysOidDev6G306x06_ObjectIdentity = ObjectIdentity
etsysOidDev6G306x06 = _EtsysOidDev6G306x06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 2)
)
if mibBuilder.loadTexts:
    etsysOidDev6G306x06.setStatus("current")
_EtsysOidDev6H302x48_ObjectIdentity = ObjectIdentity
etsysOidDev6H302x48 = _EtsysOidDev6H302x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 3)
)
if mibBuilder.loadTexts:
    etsysOidDev6H302x48.setStatus("current")
_EtsysOidDev6H303x48_ObjectIdentity = ObjectIdentity
etsysOidDev6H303x48 = _EtsysOidDev6H303x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 4)
)
if mibBuilder.loadTexts:
    etsysOidDev6H303x48.setStatus("current")
_EtsysOidDev6H352x25_ObjectIdentity = ObjectIdentity
etsysOidDev6H352x25 = _EtsysOidDev6H352x25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 5)
)
if mibBuilder.loadTexts:
    etsysOidDev6H352x25.setStatus("current")
_EtsysOidDev6H308x24_ObjectIdentity = ObjectIdentity
etsysOidDev6H308x24 = _EtsysOidDev6H308x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 6)
)
if mibBuilder.loadTexts:
    etsysOidDev6H308x24.setStatus("current")
_EtsysOidDev6E308x24_ObjectIdentity = ObjectIdentity
etsysOidDev6E308x24 = _EtsysOidDev6E308x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 7)
)
if mibBuilder.loadTexts:
    etsysOidDev6E308x24.setStatus("current")
_EtsysOidDev6C107_ObjectIdentity = ObjectIdentity
etsysOidDev6C107 = _EtsysOidDev6C107_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 8)
)
if mibBuilder.loadTexts:
    etsysOidDev6C107.setStatus("current")
_EtsysOidDevEls1000x8SX_ObjectIdentity = ObjectIdentity
etsysOidDevEls1000x8SX = _EtsysOidDevEls1000x8SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 9)
)
if mibBuilder.loadTexts:
    etsysOidDevEls1000x8SX.setStatus("current")
_EtsysOidDevEls100x48TX2M_ObjectIdentity = ObjectIdentity
etsysOidDevEls100x48TX2M = _EtsysOidDevEls100x48TX2M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 10)
)
if mibBuilder.loadTexts:
    etsysOidDevEls100x48TX2M.setStatus("current")
_EtsysOidDevEls100x24TX2M_ObjectIdentity = ObjectIdentity
etsysOidDevEls100x24TX2M = _EtsysOidDevEls100x24TX2M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 11)
)
if mibBuilder.loadTexts:
    etsysOidDevEls100x24TX2M.setStatus("current")
_EtsysOidDevDepricated001_ObjectIdentity = ObjectIdentity
etsysOidDevDepricated001 = _EtsysOidDevDepricated001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 12)
)
if mibBuilder.loadTexts:
    etsysOidDevDepricated001.setStatus("deprecated")
_EtsysOidDev6H308x48_ObjectIdentity = ObjectIdentity
etsysOidDev6H308x48 = _EtsysOidDev6H308x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 13)
)
if mibBuilder.loadTexts:
    etsysOidDev6H308x48.setStatus("current")
_EtsysOidDev6E308x48_ObjectIdentity = ObjectIdentity
etsysOidDev6E308x48 = _EtsysOidDev6E308x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 14)
)
if mibBuilder.loadTexts:
    etsysOidDev6E308x48.setStatus("current")
_EtsysOidDev6H202x48_ObjectIdentity = ObjectIdentity
etsysOidDev6H202x48 = _EtsysOidDev6H202x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 15)
)
if mibBuilder.loadTexts:
    etsysOidDev6H202x48.setStatus("current")
_EtsysOidDev9E531x24_ObjectIdentity = ObjectIdentity
etsysOidDev9E531x24 = _EtsysOidDev9E531x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 16)
)
if mibBuilder.loadTexts:
    etsysOidDev9E531x24.setStatus("current")
_EtsysOidDevVG4x3DES_ObjectIdentity = ObjectIdentity
etsysOidDevVG4x3DES = _EtsysOidDevVG4x3DES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 17)
)
if mibBuilder.loadTexts:
    etsysOidDevVG4x3DES.setStatus("deprecated")
_EtsysOidDev6H002x48_ObjectIdentity = ObjectIdentity
etsysOidDev6H002x48 = _EtsysOidDev6H002x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 18)
)
if mibBuilder.loadTexts:
    etsysOidDev6H002x48.setStatus("current")
_EtsysOidDev6H003x48_ObjectIdentity = ObjectIdentity
etsysOidDev6H003x48 = _EtsysOidDev6H003x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 19)
)
if mibBuilder.loadTexts:
    etsysOidDev6H003x48.setStatus("current")
_EtsysOidDev6G066x06_ObjectIdentity = ObjectIdentity
etsysOidDev6G066x06 = _EtsysOidDev6G066x06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 20)
)
if mibBuilder.loadTexts:
    etsysOidDev6G066x06.setStatus("current")
_EtsysOidDev6G063x06_ObjectIdentity = ObjectIdentity
etsysOidDev6G063x06 = _EtsysOidDev6G063x06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 21)
)
if mibBuilder.loadTexts:
    etsysOidDev6G063x06.setStatus("current")
_EtsysOidDevVG6_ObjectIdentity = ObjectIdentity
etsysOidDevVG6 = _EtsysOidDevVG6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 22)
)
if mibBuilder.loadTexts:
    etsysOidDevVG6.setStatus("current")
_EtsysOidDevER16_ObjectIdentity = ObjectIdentity
etsysOidDevER16 = _EtsysOidDevER16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 23)
)
if mibBuilder.loadTexts:
    etsysOidDevER16.setStatus("current")
_EtsysOidDev5SSRMx02_ObjectIdentity = ObjectIdentity
etsysOidDev5SSRMx02 = _EtsysOidDev5SSRMx02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 24)
)
if mibBuilder.loadTexts:
    etsysOidDev5SSRMx02.setStatus("current")
_EtsysOidDevVHx8TX1UM_ObjectIdentity = ObjectIdentity
etsysOidDevVHx8TX1UM = _EtsysOidDevVHx8TX1UM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 25)
)
if mibBuilder.loadTexts:
    etsysOidDevVHx8TX1UM.setStatus("current")
_EtsysOidDevVHx2402xL3_ObjectIdentity = ObjectIdentity
etsysOidDevVHx2402xL3 = _EtsysOidDevVHx2402xL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 26)
)
if mibBuilder.loadTexts:
    etsysOidDevVHx2402xL3.setStatus("current")
_EtsysOidDevVHx8GxL3_ObjectIdentity = ObjectIdentity
etsysOidDevVHx8GxL3 = _EtsysOidDevVHx8GxL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 27)
)
if mibBuilder.loadTexts:
    etsysOidDevVHx8GxL3.setStatus("current")
_EtsysOidDev5H162x50_ObjectIdentity = ObjectIdentity
etsysOidDev5H162x50 = _EtsysOidDev5H162x50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 28)
)
if mibBuilder.loadTexts:
    etsysOidDev5H162x50.setStatus("current")
_EtsysOidDev5H163x50_ObjectIdentity = ObjectIdentity
etsysOidDev5H163x50 = _EtsysOidDev5H163x50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 29)
)
if mibBuilder.loadTexts:
    etsysOidDev5H163x50.setStatus("current")
_EtsysOidDevRBTR2xA_ObjectIdentity = ObjectIdentity
etsysOidDevRBTR2xA = _EtsysOidDevRBTR2xA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 30)
)
if mibBuilder.loadTexts:
    etsysOidDevRBTR2xA.setStatus("current")
_EtsysOidDevVHx8TX1MF_ObjectIdentity = ObjectIdentity
etsysOidDevVHx8TX1MF = _EtsysOidDevVHx8TX1MF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 31)
)
if mibBuilder.loadTexts:
    etsysOidDevVHx8TX1MF.setStatus("current")
_EtsysOidDevXPx1000_ObjectIdentity = ObjectIdentity
etsysOidDevXPx1000 = _EtsysOidDevXPx1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 32)
)
if mibBuilder.loadTexts:
    etsysOidDevXPx1000.setStatus("current")
_EtsysOidDevANGx2000_ObjectIdentity = ObjectIdentity
etsysOidDevANGx2000 = _EtsysOidDevANGx2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 33)
)
if mibBuilder.loadTexts:
    etsysOidDevANGx2000.setStatus("current")
_EtsysOidDev1H152x50_ObjectIdentity = ObjectIdentity
etsysOidDev1H152x50 = _EtsysOidDev1H152x50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 34)
)
if mibBuilder.loadTexts:
    etsysOidDev1H152x50.setStatus("current")
_EtsysOidDev1G154x09_ObjectIdentity = ObjectIdentity
etsysOidDev1G154x09 = _EtsysOidDev1G154x09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 35)
)
if mibBuilder.loadTexts:
    etsysOidDev1G154x09.setStatus("current")
_EtsysOidDev1G276x13_ObjectIdentity = ObjectIdentity
etsysOidDev1G276x13 = _EtsysOidDev1G276x13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 36)
)
if mibBuilder.loadTexts:
    etsysOidDev1G276x13.setStatus("current")
_EtsysOidDevVHxSMGMTxL3_ObjectIdentity = ObjectIdentity
etsysOidDevVHxSMGMTxL3 = _EtsysOidDevVHxSMGMTxL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 37)
)
if mibBuilder.loadTexts:
    etsysOidDevVHxSMGMTxL3.setStatus("deprecated")
_EtsysOidDevANGx1102_ObjectIdentity = ObjectIdentity
etsysOidDevANGx1102 = _EtsysOidDevANGx1102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 38)
)
if mibBuilder.loadTexts:
    etsysOidDevANGx1102.setStatus("current")
_EtsysOidDevANGx1105_ObjectIdentity = ObjectIdentity
etsysOidDevANGx1105 = _EtsysOidDevANGx1105_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 39)
)
if mibBuilder.loadTexts:
    etsysOidDevANGx1105.setStatus("current")
_EtsysOidDevANGx3000_ObjectIdentity = ObjectIdentity
etsysOidDevANGx3000 = _EtsysOidDevANGx3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 40)
)
if mibBuilder.loadTexts:
    etsysOidDevANGx3000.setStatus("current")
_EtsysOidDevANGx7000_ObjectIdentity = ObjectIdentity
etsysOidDevANGx7000 = _EtsysOidDevANGx7000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 41)
)
if mibBuilder.loadTexts:
    etsysOidDevANGx7000.setStatus("current")
_EtsysOidDevXPx2400_ObjectIdentity = ObjectIdentity
etsysOidDevXPx2400 = _EtsysOidDevXPx2400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 42)
)
if mibBuilder.loadTexts:
    etsysOidDevXPx2400.setStatus("current")
_EtsysOidDevVHx8G02S_ObjectIdentity = ObjectIdentity
etsysOidDevVHx8G02S = _EtsysOidDevVHx8G02S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 43)
)
if mibBuilder.loadTexts:
    etsysOidDevVHx8G02S.setStatus("current")
_EtsysOidDev6G302x06_ObjectIdentity = ObjectIdentity
etsysOidDev6G302x06 = _EtsysOidDev6G302x06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 44)
)
if mibBuilder.loadTexts:
    etsysOidDev6G302x06.setStatus("current")
_EtsysOidDevXSRx1850_ObjectIdentity = ObjectIdentity
etsysOidDevXSRx1850 = _EtsysOidDevXSRx1850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 45)
)
if mibBuilder.loadTexts:
    etsysOidDevXSRx1850.setStatus("current")
_EtsysOidDevVHx2402S2_ObjectIdentity = ObjectIdentity
etsysOidDevVHx2402S2 = _EtsysOidDevVHx2402S2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 46)
)
if mibBuilder.loadTexts:
    etsysOidDevVHx2402S2.setStatus("current")
_EtsysOidDevVHx2202GT_ObjectIdentity = ObjectIdentity
etsysOidDevVHx2202GT = _EtsysOidDevVHx2202GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 47)
)
if mibBuilder.loadTexts:
    etsysOidDevVHx2202GT.setStatus("current")
_EtsysOidDevC5M200_ObjectIdentity = ObjectIdentity
etsysOidDevC5M200 = _EtsysOidDevC5M200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 48)
)
if mibBuilder.loadTexts:
    etsysOidDevC5M200.setStatus("deprecated")
_EtsysOidDevC1H124x48_ObjectIdentity = ObjectIdentity
etsysOidDevC1H124x48 = _EtsysOidDevC1H124x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 49)
)
if mibBuilder.loadTexts:
    etsysOidDevC1H124x48.setStatus("current")
_EtsysOidDevC2M200_ObjectIdentity = ObjectIdentity
etsysOidDevC2M200 = _EtsysOidDevC2M200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 50)
)
if mibBuilder.loadTexts:
    etsysOidDevC2M200.setStatus("deprecated")
_EtsysOidDevMatrixE7_ObjectIdentity = ObjectIdentity
etsysOidDevMatrixE7 = _EtsysOidDevMatrixE7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 51)
)
if mibBuilder.loadTexts:
    etsysOidDevMatrixE7.setStatus("current")
_EtsysOidDevMatrixN7_ObjectIdentity = ObjectIdentity
etsysOidDevMatrixN7 = _EtsysOidDevMatrixN7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 52)
)
if mibBuilder.loadTexts:
    etsysOidDevMatrixN7.setStatus("current")
_EtsysOidDevMatrixN3_ObjectIdentity = ObjectIdentity
etsysOidDevMatrixN3 = _EtsysOidDevMatrixN3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 53)
)
if mibBuilder.loadTexts:
    etsysOidDevMatrixN3.setStatus("current")
_EtsysOidDevXSRx1100_ObjectIdentity = ObjectIdentity
etsysOidDevXSRx1100 = _EtsysOidDevXSRx1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 54)
)
if mibBuilder.loadTexts:
    etsysOidDevXSRx1100.setStatus("deprecated")
_EtsysOidDevXSRx3020_ObjectIdentity = ObjectIdentity
etsysOidDevXSRx3020 = _EtsysOidDevXSRx3020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 55)
)
if mibBuilder.loadTexts:
    etsysOidDevXSRx3020.setStatus("current")
_EtsysOidDevXSRx3150_ObjectIdentity = ObjectIdentity
etsysOidDevXSRx3150 = _EtsysOidDevXSRx3150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 56)
)
if mibBuilder.loadTexts:
    etsysOidDevXSRx3150.setStatus("current")
_EtsysOidDevXSRx3250_ObjectIdentity = ObjectIdentity
etsysOidDevXSRx3250 = _EtsysOidDevXSRx3250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 57)
)
if mibBuilder.loadTexts:
    etsysOidDevXSRx3250.setStatus("current")
_EtsysOidDevXSRx4100_ObjectIdentity = ObjectIdentity
etsysOidDevXSRx4100 = _EtsysOidDevXSRx4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 58)
)
if mibBuilder.loadTexts:
    etsysOidDevXSRx4100.setStatus("current")
_EtsysOidDev1H582x25_ObjectIdentity = ObjectIdentity
etsysOidDev1H582x25 = _EtsysOidDev1H582x25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 59)
)
if mibBuilder.loadTexts:
    etsysOidDev1H582x25.setStatus("current")
_EtsysOidDev1G587x09_ObjectIdentity = ObjectIdentity
etsysOidDev1G587x09 = _EtsysOidDev1G587x09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 60)
)
if mibBuilder.loadTexts:
    etsysOidDev1G587x09.setStatus("current")
_EtsysOidDevC1G124x24_ObjectIdentity = ObjectIdentity
etsysOidDevC1G124x24 = _EtsysOidDevC1G124x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 61)
)
if mibBuilder.loadTexts:
    etsysOidDevC1G124x24.setStatus("current")
_EtsysOidDevV2H124x24_ObjectIdentity = ObjectIdentity
etsysOidDevV2H124x24 = _EtsysOidDevV2H124x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 62)
)
if mibBuilder.loadTexts:
    etsysOidDevV2H124x24.setStatus("current")
_EtsysOidDevRBTR3xA_ObjectIdentity = ObjectIdentity
etsysOidDevRBTR3xA = _EtsysOidDevRBTR3xA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 63)
)
if mibBuilder.loadTexts:
    etsysOidDevRBTR3xA.setStatus("current")
_EtsysOidDevRBTR4xA_ObjectIdentity = ObjectIdentity
etsysOidDevRBTR4xA = _EtsysOidDevRBTR4xA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 64)
)
if mibBuilder.loadTexts:
    etsysOidDevRBTR4xA.setStatus("current")
_EtsysOidDevMatrixE7Gold_ObjectIdentity = ObjectIdentity
etsysOidDevMatrixE7Gold = _EtsysOidDevMatrixE7Gold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 65)
)
if mibBuilder.loadTexts:
    etsysOidDevMatrixE7Gold.setStatus("current")
_EtsysOidDevMatrixN7Gold_ObjectIdentity = ObjectIdentity
etsysOidDevMatrixN7Gold = _EtsysOidDevMatrixN7Gold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 66)
)
if mibBuilder.loadTexts:
    etsysOidDevMatrixN7Gold.setStatus("current")
_EtsysOidDevMatrixN3Gold_ObjectIdentity = ObjectIdentity
etsysOidDevMatrixN3Gold = _EtsysOidDevMatrixN3Gold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 67)
)
if mibBuilder.loadTexts:
    etsysOidDevMatrixN3Gold.setStatus("current")
_EtsysOidDevV2H124xPOE_ObjectIdentity = ObjectIdentity
etsysOidDevV2H124xPOE = _EtsysOidDevV2H124xPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 68)
)
if mibBuilder.loadTexts:
    etsysOidDevV2H124xPOE.setStatus("current")
_EtsysOidDevDFEGoldRouter_ObjectIdentity = ObjectIdentity
etsysOidDevDFEGoldRouter = _EtsysOidDevDFEGoldRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 69)
)
if mibBuilder.loadTexts:
    etsysOidDevDFEGoldRouter.setStatus("current")
_EtsysOidDevDFEPlatinumRouter_ObjectIdentity = ObjectIdentity
etsysOidDevDFEPlatinumRouter = _EtsysOidDevDFEPlatinumRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 70)
)
if mibBuilder.loadTexts:
    etsysOidDevDFEPlatinumRouter.setStatus("current")
_EtsysOidDevDragonIdsAppliance_ObjectIdentity = ObjectIdentity
etsysOidDevDragonIdsAppliance = _EtsysOidDevDragonIdsAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 71)
)
if mibBuilder.loadTexts:
    etsysOidDevDragonIdsAppliance.setStatus("current")
_EtsysOidDevXSRx1205_ObjectIdentity = ObjectIdentity
etsysOidDevXSRx1205 = _EtsysOidDevXSRx1205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 72)
)
if mibBuilder.loadTexts:
    etsysOidDevXSRx1205.setStatus("current")
_EtsysOidDevXSRx1220_ObjectIdentity = ObjectIdentity
etsysOidDevXSRx1220 = _EtsysOidDevXSRx1220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 73)
)
if mibBuilder.loadTexts:
    etsysOidDevXSRx1220.setStatus("current")
_EtsysOidDevXSRx1225_ObjectIdentity = ObjectIdentity
etsysOidDevXSRx1225 = _EtsysOidDevXSRx1225_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 74)
)
if mibBuilder.loadTexts:
    etsysOidDevXSRx1225.setStatus("current")
_EtsysOidDevXSRx1230_ObjectIdentity = ObjectIdentity
etsysOidDevXSRx1230 = _EtsysOidDevXSRx1230_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 75)
)
if mibBuilder.loadTexts:
    etsysOidDevXSRx1230.setStatus("current")
_EtsysOidDevXSRx1235_ObjectIdentity = ObjectIdentity
etsysOidDevXSRx1235 = _EtsysOidDevXSRx1235_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 76)
)
if mibBuilder.loadTexts:
    etsysOidDevXSRx1235.setStatus("current")
_EtsysOidDev2G4072x52_ObjectIdentity = ObjectIdentity
etsysOidDev2G4072x52 = _EtsysOidDev2G4072x52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 77)
)
if mibBuilder.loadTexts:
    etsysOidDev2G4072x52.setStatus("current")
_EtsysOidDevMatrixN5PoEGold_ObjectIdentity = ObjectIdentity
etsysOidDevMatrixN5PoEGold = _EtsysOidDevMatrixN5PoEGold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 78)
)
if mibBuilder.loadTexts:
    etsysOidDevMatrixN5PoEGold.setStatus("current")
_EtsysOidDevMatrixN5PoEPlatinum_ObjectIdentity = ObjectIdentity
etsysOidDevMatrixN5PoEPlatinum = _EtsysOidDevMatrixN5PoEPlatinum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 79)
)
if mibBuilder.loadTexts:
    etsysOidDevMatrixN5PoEPlatinum.setStatus("current")
_EtsysOidDevMatrixX4_ObjectIdentity = ObjectIdentity
etsysOidDevMatrixX4 = _EtsysOidDevMatrixX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 80)
)
if mibBuilder.loadTexts:
    etsysOidDevMatrixX4.setStatus("current")
_EtsysOidDevMatrixX8_ObjectIdentity = ObjectIdentity
etsysOidDevMatrixX8 = _EtsysOidDevMatrixX8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 81)
)
if mibBuilder.loadTexts:
    etsysOidDevMatrixX8.setStatus("current")
_EtsysOidDevMatrixX16_ObjectIdentity = ObjectIdentity
etsysOidDevMatrixX16 = _EtsysOidDevMatrixX16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 82)
)
if mibBuilder.loadTexts:
    etsysOidDevMatrixX16.setStatus("current")
_EtsysOidDevMatrixN1_ObjectIdentity = ObjectIdentity
etsysOidDevMatrixN1 = _EtsysOidDevMatrixN1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 83)
)
if mibBuilder.loadTexts:
    etsysOidDevMatrixN1.setStatus("current")
_EtsysOidDevMatrixN1Gold_ObjectIdentity = ObjectIdentity
etsysOidDevMatrixN1Gold = _EtsysOidDevMatrixN1Gold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 84)
)
if mibBuilder.loadTexts:
    etsysOidDevMatrixN1Gold.setStatus("current")
_EtsysOidDevRBTSAxAA_ObjectIdentity = ObjectIdentity
etsysOidDevRBTSAxAA = _EtsysOidDevRBTSAxAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 85)
)
if mibBuilder.loadTexts:
    etsysOidDevRBTSAxAA.setStatus("current")
_EtsysOidDevRBTSAxAB_ObjectIdentity = ObjectIdentity
etsysOidDevRBTSAxAB = _EtsysOidDevRBTSAxAB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 86)
)
if mibBuilder.loadTexts:
    etsysOidDevRBTSAxAB.setStatus("current")
_EtsysOidDevA2H124x24_ObjectIdentity = ObjectIdentity
etsysOidDevA2H124x24 = _EtsysOidDevA2H124x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 87)
)
if mibBuilder.loadTexts:
    etsysOidDevA2H124x24.setStatus("current")
_EtsysOidDevA2H124x24P_ObjectIdentity = ObjectIdentity
etsysOidDevA2H124x24P = _EtsysOidDevA2H124x24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 88)
)
if mibBuilder.loadTexts:
    etsysOidDevA2H124x24P.setStatus("current")
_EtsysOidDevA2H124x48_ObjectIdentity = ObjectIdentity
etsysOidDevA2H124x48 = _EtsysOidDevA2H124x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 89)
)
if mibBuilder.loadTexts:
    etsysOidDevA2H124x48.setStatus("current")
_EtsysOidDevA2H124x48P_ObjectIdentity = ObjectIdentity
etsysOidDevA2H124x48P = _EtsysOidDevA2H124x48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 90)
)
if mibBuilder.loadTexts:
    etsysOidDevA2H124x48P.setStatus("current")
_EtsysOidDevA2H124x24FX_ObjectIdentity = ObjectIdentity
etsysOidDevA2H124x24FX = _EtsysOidDevA2H124x24FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 91)
)
if mibBuilder.loadTexts:
    etsysOidDevA2H124x24FX.setStatus("current")
_EtsysOidDevRBT4102_ObjectIdentity = ObjectIdentity
etsysOidDevRBT4102 = _EtsysOidDevRBT4102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 92)
)
if mibBuilder.loadTexts:
    etsysOidDevRBT4102.setStatus("current")
_EtsysOidDevNSTAGxGE250xTX_ObjectIdentity = ObjectIdentity
etsysOidDevNSTAGxGE250xTX = _EtsysOidDevNSTAGxGE250xTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 93)
)
if mibBuilder.loadTexts:
    etsysOidDevNSTAGxGE250xTX.setStatus("current")
_EtsysOidDevNSTAGxGE500xTX_ObjectIdentity = ObjectIdentity
etsysOidDevNSTAGxGE500xTX = _EtsysOidDevNSTAGxGE500xTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 94)
)
if mibBuilder.loadTexts:
    etsysOidDevNSTAGxGE500xTX.setStatus("current")
_EtsysOidDevA2H254x16_ObjectIdentity = ObjectIdentity
etsysOidDevA2H254x16 = _EtsysOidDevA2H254x16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 95)
)
if mibBuilder.loadTexts:
    etsysOidDevA2H254x16.setStatus("current")
_EtsysOidDevC3G124x24_ObjectIdentity = ObjectIdentity
etsysOidDevC3G124x24 = _EtsysOidDevC3G124x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 96)
)
if mibBuilder.loadTexts:
    etsysOidDevC3G124x24.setStatus("current")
_EtsysOidDevC3G124x24P_ObjectIdentity = ObjectIdentity
etsysOidDevC3G124x24P = _EtsysOidDevC3G124x24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 97)
)
if mibBuilder.loadTexts:
    etsysOidDevC3G124x24P.setStatus("current")
_EtsysOidDevC3G124x48_ObjectIdentity = ObjectIdentity
etsysOidDevC3G124x48 = _EtsysOidDevC3G124x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 98)
)
if mibBuilder.loadTexts:
    etsysOidDevC3G124x48.setStatus("current")
_EtsysOidDevC3G124x48P_ObjectIdentity = ObjectIdentity
etsysOidDevC3G124x48P = _EtsysOidDevC3G124x48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 99)
)
if mibBuilder.loadTexts:
    etsysOidDevC3G124x48P.setStatus("current")
_EtsysOidDevB3G124x24_ObjectIdentity = ObjectIdentity
etsysOidDevB3G124x24 = _EtsysOidDevB3G124x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 100)
)
if mibBuilder.loadTexts:
    etsysOidDevB3G124x24.setStatus("current")
_EtsysOidDevB3G124x24P_ObjectIdentity = ObjectIdentity
etsysOidDevB3G124x24P = _EtsysOidDevB3G124x24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 101)
)
if mibBuilder.loadTexts:
    etsysOidDevB3G124x24P.setStatus("current")
_EtsysOidDevB3G124x48_ObjectIdentity = ObjectIdentity
etsysOidDevB3G124x48 = _EtsysOidDevB3G124x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 102)
)
if mibBuilder.loadTexts:
    etsysOidDevB3G124x48.setStatus("current")
_EtsysOidDevB3G124x48P_ObjectIdentity = ObjectIdentity
etsysOidDevB3G124x48P = _EtsysOidDevB3G124x48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 103)
)
if mibBuilder.loadTexts:
    etsysOidDevB3G124x48P.setStatus("current")
_EtsysOidDevI3H252x02_ObjectIdentity = ObjectIdentity
etsysOidDevI3H252x02 = _EtsysOidDevI3H252x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 104)
)
if mibBuilder.loadTexts:
    etsysOidDevI3H252x02.setStatus("current")
_EtsysOidDevSNSxTAGxLPA_ObjectIdentity = ObjectIdentity
etsysOidDevSNSxTAGxLPA = _EtsysOidDevSNSxTAGxLPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 105)
)
if mibBuilder.loadTexts:
    etsysOidDevSNSxTAGxLPA.setStatus("current")
_EtsysOidDevSNSxTAGxHPA_ObjectIdentity = ObjectIdentity
etsysOidDevSNSxTAGxHPA = _EtsysOidDevSNSxTAGxHPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 106)
)
if mibBuilder.loadTexts:
    etsysOidDevSNSxTAGxHPA.setStatus("current")
_EtsysOidDevSNSxTAGxBASE_ObjectIdentity = ObjectIdentity
etsysOidDevSNSxTAGxBASE = _EtsysOidDevSNSxTAGxBASE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 107)
)
if mibBuilder.loadTexts:
    etsysOidDevSNSxTAGxBASE.setStatus("current")
_EtsysOidDev7SxNSTAGx01_ObjectIdentity = ObjectIdentity
etsysOidDev7SxNSTAGx01 = _EtsysOidDev7SxNSTAGx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 108)
)
if mibBuilder.loadTexts:
    etsysOidDev7SxNSTAGx01.setStatus("current")
_EtsysOidDevSNSxPCCxWBA_ObjectIdentity = ObjectIdentity
etsysOidDevSNSxPCCxWBA = _EtsysOidDevSNSxPCCxWBA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 109)
)
if mibBuilder.loadTexts:
    etsysOidDevSNSxPCCxWBA.setStatus("current")
_EtsysOidDevA2H123x24_ObjectIdentity = ObjectIdentity
etsysOidDevA2H123x24 = _EtsysOidDevA2H123x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 110)
)
if mibBuilder.loadTexts:
    etsysOidDevA2H123x24.setStatus("current")
_EtsysOidDevB3H124x24FX_ObjectIdentity = ObjectIdentity
etsysOidDevB3H124x24FX = _EtsysOidDevB3H124x24FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 111)
)
if mibBuilder.loadTexts:
    etsysOidDevB3H124x24FX.setStatus("current")
_EtsysOidDevC3H124x24FX_ObjectIdentity = ObjectIdentity
etsysOidDevC3H124x24FX = _EtsysOidDevC3H124x24FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 112)
)
if mibBuilder.loadTexts:
    etsysOidDevC3H124x24FX.setStatus("current")
_EtsysOidDevC3K122x24_ObjectIdentity = ObjectIdentity
etsysOidDevC3K122x24 = _EtsysOidDevC3K122x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 113)
)
if mibBuilder.loadTexts:
    etsysOidDevC3K122x24.setStatus("current")
_EtsysOidDevC3K172x24_ObjectIdentity = ObjectIdentity
etsysOidDevC3K172x24 = _EtsysOidDevC3K172x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 114)
)
if mibBuilder.loadTexts:
    etsysOidDevC3K172x24.setStatus("current")
_EtsysOidDevC3Kx2XFP_ObjectIdentity = ObjectIdentity
etsysOidDevC3Kx2XFP = _EtsysOidDevC3Kx2XFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 115)
)
if mibBuilder.loadTexts:
    etsysOidDevC3Kx2XFP.setStatus("current")
_EtsysOidDevSNSxNSSxA_ObjectIdentity = ObjectIdentity
etsysOidDevSNSxNSSxA = _EtsysOidDevSNSxNSSxA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 116)
)
if mibBuilder.loadTexts:
    etsysOidDevSNSxNSSxA.setStatus("current")
_EtsysOidDevG3G124x24_ObjectIdentity = ObjectIdentity
etsysOidDevG3G124x24 = _EtsysOidDevG3G124x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 117)
)
if mibBuilder.loadTexts:
    etsysOidDevG3G124x24.setStatus("current")
_EtsysOidDevG3G170x24_ObjectIdentity = ObjectIdentity
etsysOidDevG3G170x24 = _EtsysOidDevG3G170x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 118)
)
if mibBuilder.loadTexts:
    etsysOidDevG3G170x24.setStatus("current")
_EtsysOidDevD2G124x12_ObjectIdentity = ObjectIdentity
etsysOidDevD2G124x12 = _EtsysOidDevD2G124x12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 119)
)
if mibBuilder.loadTexts:
    etsysOidDevD2G124x12.setStatus("current")
_EtsysOidDevD2G124x12P_ObjectIdentity = ObjectIdentity
etsysOidDevD2G124x12P = _EtsysOidDevD2G124x12P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 120)
)
if mibBuilder.loadTexts:
    etsysOidDevD2G124x12P.setStatus("current")
_EtsysOidDevRBTx8500_ObjectIdentity = ObjectIdentity
etsysOidDevRBTx8500 = _EtsysOidDevRBTx8500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 121)
)
if mibBuilder.loadTexts:
    etsysOidDevRBTx8500.setStatus("current")
_EtsysOidDevMatrixN1NAC_ObjectIdentity = ObjectIdentity
etsysOidDevMatrixN1NAC = _EtsysOidDevMatrixN1NAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 122)
)
if mibBuilder.loadTexts:
    etsysOidDevMatrixN1NAC.setStatus("current")
_EtsysOidDev7SxNSNACGx01NPS_ObjectIdentity = ObjectIdentity
etsysOidDev7SxNSNACGx01NPS = _EtsysOidDev7SxNSNACGx01NPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 123)
)
if mibBuilder.loadTexts:
    etsysOidDev7SxNSNACGx01NPS.setStatus("current")
_EtsysOidDevG3G124x24P_ObjectIdentity = ObjectIdentity
etsysOidDevG3G124x24P = _EtsysOidDevG3G124x24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 124)
)
if mibBuilder.loadTexts:
    etsysOidDevG3G124x24P.setStatus("current")
_EtsysOidDevC3K122x24P_ObjectIdentity = ObjectIdentity
etsysOidDevC3K122x24P = _EtsysOidDevC3K122x24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 125)
)
if mibBuilder.loadTexts:
    etsysOidDevC3K122x24P.setStatus("current")
_EtsysOidDevNACxAx2K_ObjectIdentity = ObjectIdentity
etsysOidDevNACxAx2K = _EtsysOidDevNACxAx2K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 126)
)
if mibBuilder.loadTexts:
    etsysOidDevNACxAx2K.setStatus("deprecated")
_EtsysOidDevNACxAx3K_ObjectIdentity = ObjectIdentity
etsysOidDevNACxAx3K = _EtsysOidDevNACxAx3K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 127)
)
if mibBuilder.loadTexts:
    etsysOidDevNACxAx3K.setStatus("deprecated")
_EtsysOidDevSSAxT4068x0252_ObjectIdentity = ObjectIdentity
etsysOidDevSSAxT4068x0252 = _EtsysOidDevSSAxT4068x0252_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 128)
)
if mibBuilder.loadTexts:
    etsysOidDevSSAxT4068x0252.setStatus("current")
_EtsysOidDevSSAxT1068x0652_ObjectIdentity = ObjectIdentity
etsysOidDevSSAxT1068x0652 = _EtsysOidDevSSAxT1068x0652_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 129)
)
if mibBuilder.loadTexts:
    etsysOidDevSSAxT1068x0652.setStatus("current")
_EtsysOidDevSSAxG1018x0652_ObjectIdentity = ObjectIdentity
etsysOidDevSSAxG1018x0652 = _EtsysOidDevSSAxG1018x0652_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 130)
)
if mibBuilder.loadTexts:
    etsysOidDevSSAxG1018x0652.setStatus("current")
_EtsysOidDevS3_ObjectIdentity = ObjectIdentity
etsysOidDevS3 = _EtsysOidDevS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 131)
)
if mibBuilder.loadTexts:
    etsysOidDevS3.setStatus("current")
_EtsysOidDevS4_ObjectIdentity = ObjectIdentity
etsysOidDevS4 = _EtsysOidDevS4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 132)
)
if mibBuilder.loadTexts:
    etsysOidDevS4.setStatus("current")
_EtsysOidDevS8_ObjectIdentity = ObjectIdentity
etsysOidDevS8 = _EtsysOidDevS8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 133)
)
if mibBuilder.loadTexts:
    etsysOidDevS8.setStatus("current")
_EtsysOidDevB5G124x24_ObjectIdentity = ObjectIdentity
etsysOidDevB5G124x24 = _EtsysOidDevB5G124x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 134)
)
if mibBuilder.loadTexts:
    etsysOidDevB5G124x24.setStatus("current")
_EtsysOidDevB5G124x24P2_ObjectIdentity = ObjectIdentity
etsysOidDevB5G124x24P2 = _EtsysOidDevB5G124x24P2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 135)
)
if mibBuilder.loadTexts:
    etsysOidDevB5G124x24P2.setStatus("current")
_EtsysOidDevB5G124x48_ObjectIdentity = ObjectIdentity
etsysOidDevB5G124x48 = _EtsysOidDevB5G124x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 136)
)
if mibBuilder.loadTexts:
    etsysOidDevB5G124x48.setStatus("current")
_EtsysOidDevB5G124x48P2_ObjectIdentity = ObjectIdentity
etsysOidDevB5G124x48P2 = _EtsysOidDevB5G124x48P2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 137)
)
if mibBuilder.loadTexts:
    etsysOidDevB5G124x48P2.setStatus("current")
_EtsysOidDevB5K125x24_ObjectIdentity = ObjectIdentity
etsysOidDevB5K125x24 = _EtsysOidDevB5K125x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 138)
)
if mibBuilder.loadTexts:
    etsysOidDevB5K125x24.setStatus("current")
_EtsysOidDevB5K125x24P2_ObjectIdentity = ObjectIdentity
etsysOidDevB5K125x24P2 = _EtsysOidDevB5K125x24P2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 139)
)
if mibBuilder.loadTexts:
    etsysOidDevB5K125x24P2.setStatus("current")
_EtsysOidDevB5K125x48_ObjectIdentity = ObjectIdentity
etsysOidDevB5K125x48 = _EtsysOidDevB5K125x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 140)
)
if mibBuilder.loadTexts:
    etsysOidDevB5K125x48.setStatus("current")
_EtsysOidDevB5K125x48P2_ObjectIdentity = ObjectIdentity
etsysOidDevB5K125x48P2 = _EtsysOidDevB5K125x48P2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 141)
)
if mibBuilder.loadTexts:
    etsysOidDevB5K125x48P2.setStatus("current")
_EtsysOidDevC5G124x24_ObjectIdentity = ObjectIdentity
etsysOidDevC5G124x24 = _EtsysOidDevC5G124x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 142)
)
if mibBuilder.loadTexts:
    etsysOidDevC5G124x24.setStatus("current")
_EtsysOidDevC5G124x24P2_ObjectIdentity = ObjectIdentity
etsysOidDevC5G124x24P2 = _EtsysOidDevC5G124x24P2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 143)
)
if mibBuilder.loadTexts:
    etsysOidDevC5G124x24P2.setStatus("current")
_EtsysOidDevC5G124x48_ObjectIdentity = ObjectIdentity
etsysOidDevC5G124x48 = _EtsysOidDevC5G124x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 144)
)
if mibBuilder.loadTexts:
    etsysOidDevC5G124x48.setStatus("current")
_EtsysOidDevC5G124x48P2_ObjectIdentity = ObjectIdentity
etsysOidDevC5G124x48P2 = _EtsysOidDevC5G124x48P2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 145)
)
if mibBuilder.loadTexts:
    etsysOidDevC5G124x48P2.setStatus("current")
_EtsysOidDevC5K125x24_ObjectIdentity = ObjectIdentity
etsysOidDevC5K125x24 = _EtsysOidDevC5K125x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 146)
)
if mibBuilder.loadTexts:
    etsysOidDevC5K125x24.setStatus("current")
_EtsysOidDevC5K125x24P2_ObjectIdentity = ObjectIdentity
etsysOidDevC5K125x24P2 = _EtsysOidDevC5K125x24P2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 147)
)
if mibBuilder.loadTexts:
    etsysOidDevC5K125x24P2.setStatus("current")
_EtsysOidDevC5K125x48_ObjectIdentity = ObjectIdentity
etsysOidDevC5K125x48 = _EtsysOidDevC5K125x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 148)
)
if mibBuilder.loadTexts:
    etsysOidDevC5K125x48.setStatus("current")
_EtsysOidDevC5K125x48P2_ObjectIdentity = ObjectIdentity
etsysOidDevC5K125x48P2 = _EtsysOidDevC5K125x48P2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 149)
)
if mibBuilder.loadTexts:
    etsysOidDevC5K125x48P2.setStatus("current")
_EtsysOidDevC5K175x24_ObjectIdentity = ObjectIdentity
etsysOidDevC5K175x24 = _EtsysOidDevC5K175x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 150)
)
if mibBuilder.loadTexts:
    etsysOidDevC5K175x24.setStatus("current")
_EtsysOidDevNACxAx10_ObjectIdentity = ObjectIdentity
etsysOidDevNACxAx10 = _EtsysOidDevNACxAx10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 151)
)
if mibBuilder.loadTexts:
    etsysOidDevNACxAx10.setStatus("current")
_EtsysOidDevNACxAx20_ObjectIdentity = ObjectIdentity
etsysOidDevNACxAx20 = _EtsysOidDevNACxAx20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 152)
)
if mibBuilder.loadTexts:
    etsysOidDevNACxAx20.setStatus("current")
_EtsysOidDevNACxV_ObjectIdentity = ObjectIdentity
etsysOidDevNACxV = _EtsysOidDevNACxV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 153)
)
if mibBuilder.loadTexts:
    etsysOidDevNACxV.setStatus("current")
_EtsysOidDevA4H124x24TX_ObjectIdentity = ObjectIdentity
etsysOidDevA4H124x24TX = _EtsysOidDevA4H124x24TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 154)
)
if mibBuilder.loadTexts:
    etsysOidDevA4H124x24TX.setStatus("current")
_EtsysOidDevA4H124x24FX_ObjectIdentity = ObjectIdentity
etsysOidDevA4H124x24FX = _EtsysOidDevA4H124x24FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 155)
)
if mibBuilder.loadTexts:
    etsysOidDevA4H124x24FX.setStatus("current")
_EtsysOidDevA4H124x8F8T_ObjectIdentity = ObjectIdentity
etsysOidDevA4H124x8F8T = _EtsysOidDevA4H124x8F8T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 156)
)
if mibBuilder.loadTexts:
    etsysOidDevA4H124x8F8T.setStatus("obsolete")
_EtsysOidDevA4H124x24_ObjectIdentity = ObjectIdentity
etsysOidDevA4H124x24 = _EtsysOidDevA4H124x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 157)
)
if mibBuilder.loadTexts:
    etsysOidDevA4H124x24.setStatus("current")
_EtsysOidDevA4H124x24P_ObjectIdentity = ObjectIdentity
etsysOidDevA4H124x24P = _EtsysOidDevA4H124x24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 158)
)
if mibBuilder.loadTexts:
    etsysOidDevA4H124x24P.setStatus("current")
_EtsysOidDevA4H124x48_ObjectIdentity = ObjectIdentity
etsysOidDevA4H124x48 = _EtsysOidDevA4H124x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 159)
)
if mibBuilder.loadTexts:
    etsysOidDevA4H124x48.setStatus("current")
_EtsysOidDevA4H124x48P_ObjectIdentity = ObjectIdentity
etsysOidDevA4H124x48P = _EtsysOidDevA4H124x48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 160)
)
if mibBuilder.loadTexts:
    etsysOidDevA4H124x48P.setStatus("current")
_EtsysOidDevA4H254x8F8T_ObjectIdentity = ObjectIdentity
etsysOidDevA4H254x8F8T = _EtsysOidDevA4H254x8F8T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 161)
)
if mibBuilder.loadTexts:
    etsysOidDevA4H254x8F8T.setStatus("obsolete")
_EtsysOidDevK6_ObjectIdentity = ObjectIdentity
etsysOidDevK6 = _EtsysOidDevK6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 162)
)
if mibBuilder.loadTexts:
    etsysOidDevK6.setStatus("current")
_EtsysOidDevK10_ObjectIdentity = ObjectIdentity
etsysOidDevK10 = _EtsysOidDevK10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 163)
)
if mibBuilder.loadTexts:
    etsysOidDevK10.setStatus("current")
_EtsysOidDevS6_ObjectIdentity = ObjectIdentity
etsysOidDevS6 = _EtsysOidDevS6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 164)
)
if mibBuilder.loadTexts:
    etsysOidDevS6.setStatus("current")
_EtsysOidDevSSAxT5068x0652_ObjectIdentity = ObjectIdentity
etsysOidDevSSAxT5068x0652 = _EtsysOidDevSSAxT5068x0652_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 505)
)
if mibBuilder.loadTexts:
    etsysOidDevSSAxT5068x0652.setStatus("current")
_EtsysOidDevSSAxG5018x0652_ObjectIdentity = ObjectIdentity
etsysOidDevSSAxG5018x0652 = _EtsysOidDevSSAxG5018x0652_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 1, 506)
)
if mibBuilder.loadTexts:
    etsysOidDevSSAxG5018x0652.setStatus("current")
_EtsysOidPhy_ObjectIdentity = ObjectIdentity
etsysOidPhy = _EtsysOidPhy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2)
)
_EtsysOidPhyEmpty_ObjectIdentity = ObjectIdentity
etsysOidPhyEmpty = _EtsysOidPhyEmpty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysOidPhyEmpty.setStatus("current")
_EtsysOidPhyMGBICxMT01_ObjectIdentity = ObjectIdentity
etsysOidPhyMGBICxMT01 = _EtsysOidPhyMGBICxMT01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 2)
)
if mibBuilder.loadTexts:
    etsysOidPhyMGBICxMT01.setStatus("current")
_EtsysOidPhyMGBICxMT09_ObjectIdentity = ObjectIdentity
etsysOidPhyMGBICxMT09 = _EtsysOidPhyMGBICxMT09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 3)
)
if mibBuilder.loadTexts:
    etsysOidPhyMGBICxMT09.setStatus("current")
_EtsysOidPhyMGBICxLC01_ObjectIdentity = ObjectIdentity
etsysOidPhyMGBICxLC01 = _EtsysOidPhyMGBICxLC01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 4)
)
if mibBuilder.loadTexts:
    etsysOidPhyMGBICxLC01.setStatus("current")
_EtsysOidPhyMGBICxLC09_ObjectIdentity = ObjectIdentity
etsysOidPhyMGBICxLC09 = _EtsysOidPhyMGBICxLC09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 5)
)
if mibBuilder.loadTexts:
    etsysOidPhyMGBICxLC09.setStatus("current")
_EtsysOidPhyFrtPnlFastEthRJ45_ObjectIdentity = ObjectIdentity
etsysOidPhyFrtPnlFastEthRJ45 = _EtsysOidPhyFrtPnlFastEthRJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 6)
)
if mibBuilder.loadTexts:
    etsysOidPhyFrtPnlFastEthRJ45.setStatus("current")
_EtsysOidPhyFrtPnlFastEthRJ21_ObjectIdentity = ObjectIdentity
etsysOidPhyFrtPnlFastEthRJ21 = _EtsysOidPhyFrtPnlFastEthRJ21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 7)
)
if mibBuilder.loadTexts:
    etsysOidPhyFrtPnlFastEthRJ21.setStatus("current")
_EtsysOidPhyFrtPnlGigEthRJ45_ObjectIdentity = ObjectIdentity
etsysOidPhyFrtPnlGigEthRJ45 = _EtsysOidPhyFrtPnlGigEthRJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 8)
)
if mibBuilder.loadTexts:
    etsysOidPhyFrtPnlGigEthRJ45.setStatus("current")
_EtsysOidPhyBackplaneFTM1_ObjectIdentity = ObjectIdentity
etsysOidPhyBackplaneFTM1 = _EtsysOidPhyBackplaneFTM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 9)
)
if mibBuilder.loadTexts:
    etsysOidPhyBackplaneFTM1.setStatus("current")
_EtsysOidPhy7H4203x72_ObjectIdentity = ObjectIdentity
etsysOidPhy7H4203x72 = _EtsysOidPhy7H4203x72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 10)
)
if mibBuilder.loadTexts:
    etsysOidPhy7H4203x72.setStatus("current")
_EtsysOidPhy7H4273x52_ObjectIdentity = ObjectIdentity
etsysOidPhy7H4273x52 = _EtsysOidPhy7H4273x52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 11)
)
if mibBuilder.loadTexts:
    etsysOidPhy7H4273x52.setStatus("current")
_EtsysOidPhy7H4303x48_ObjectIdentity = ObjectIdentity
etsysOidPhy7H4303x48 = _EtsysOidPhy7H4303x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 12)
)
if mibBuilder.loadTexts:
    etsysOidPhy7H4303x48.setStatus("deprecated")
_EtsysOidPhy7G4270x12_ObjectIdentity = ObjectIdentity
etsysOidPhy7G4270x12 = _EtsysOidPhy7G4270x12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 13)
)
if mibBuilder.loadTexts:
    etsysOidPhy7G4270x12.setStatus("current")
_EtsysOidPhy7G4202x12_ObjectIdentity = ObjectIdentity
etsysOidPhy7G4202x12 = _EtsysOidPhy7G4202x12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 14)
)
if mibBuilder.loadTexts:
    etsysOidPhy7G4202x12.setStatus("deprecated")
_EtsysOidPhy7G4370x08_ObjectIdentity = ObjectIdentity
etsysOidPhy7G4370x08 = _EtsysOidPhy7G4370x08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 15)
)
if mibBuilder.loadTexts:
    etsysOidPhy7G4370x08.setStatus("deprecated")
_EtsysOidPhy7K420Xx01_ObjectIdentity = ObjectIdentity
etsysOidPhy7K420Xx01 = _EtsysOidPhy7K420Xx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 16)
)
if mibBuilder.loadTexts:
    etsysOidPhy7K420Xx01.setStatus("current")
_EtsysOidPhy6C207x1_ObjectIdentity = ObjectIdentity
etsysOidPhy6C207x1 = _EtsysOidPhy6C207x1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 17)
)
if mibBuilder.loadTexts:
    etsysOidPhy6C207x1.setStatus("current")
_EtsysOidPhy6C207x2_ObjectIdentity = ObjectIdentity
etsysOidPhy6C207x2 = _EtsysOidPhy6C207x2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 18)
)
if mibBuilder.loadTexts:
    etsysOidPhy6C207x2.setStatus("current")
_EtsysOidPhy6C407_ObjectIdentity = ObjectIdentity
etsysOidPhy6C407 = _EtsysOidPhy6C407_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 19)
)
if mibBuilder.loadTexts:
    etsysOidPhy6C407.setStatus("current")
_EtsysOidPhy5C205x3_ObjectIdentity = ObjectIdentity
etsysOidPhy5C205x3 = _EtsysOidPhy5C205x3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 20)
)
if mibBuilder.loadTexts:
    etsysOidPhy5C205x3.setStatus("current")
_EtsysOidPhy5C205x2_ObjectIdentity = ObjectIdentity
etsysOidPhy5C205x2 = _EtsysOidPhy5C205x2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 21)
)
if mibBuilder.loadTexts:
    etsysOidPhy5C205x2.setStatus("current")
_EtsysOidPhy5C405_ObjectIdentity = ObjectIdentity
etsysOidPhy5C405 = _EtsysOidPhy5C405_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 22)
)
if mibBuilder.loadTexts:
    etsysOidPhy5C405.setStatus("current")
_EtsysOidPhy6C107_ObjectIdentity = ObjectIdentity
etsysOidPhy6C107 = _EtsysOidPhy6C107_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 23)
)
if mibBuilder.loadTexts:
    etsysOidPhy6C107.setStatus("current")
_EtsysOidPhy5C105_ObjectIdentity = ObjectIdentity
etsysOidPhy5C105 = _EtsysOidPhy5C105_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 24)
)
if mibBuilder.loadTexts:
    etsysOidPhy5C105.setStatus("current")
_EtsysOidPhy10GbExSR_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExSR = _EtsysOidPhy10GbExSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 25)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExSR.setStatus("current")
_EtsysOidPhy10GbExLR_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExLR = _EtsysOidPhy10GbExLR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 26)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExLR.setStatus("current")
_EtsysOidPhy10GbExER_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExER = _EtsysOidPhy10GbExER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 27)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExER.setStatus("current")
_EtsysOidPhy10GbExSW_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExSW = _EtsysOidPhy10GbExSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 28)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExSW.setStatus("current")
_EtsysOidPhy10GbExLW_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExLW = _EtsysOidPhy10GbExLW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 29)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExLW.setStatus("current")
_EtsysOidPhy10GbExEW_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExEW = _EtsysOidPhy10GbExEW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 30)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExEW.setStatus("current")
_EtsysOidPhy10GbExLX4_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExLX4 = _EtsysOidPhy10GbExLX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 31)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExLX4.setStatus("current")
_EtsysOidPhy1Hx16TX_ObjectIdentity = ObjectIdentity
etsysOidPhy1Hx16TX = _EtsysOidPhy1Hx16TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 32)
)
if mibBuilder.loadTexts:
    etsysOidPhy1Hx16TX.setStatus("current")
_EtsysOidPhy1Gx2GBIC_ObjectIdentity = ObjectIdentity
etsysOidPhy1Gx2GBIC = _EtsysOidPhy1Gx2GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 33)
)
if mibBuilder.loadTexts:
    etsysOidPhy1Gx2GBIC.setStatus("current")
_EtsysOidPhy1Gx2MGBIC_ObjectIdentity = ObjectIdentity
etsysOidPhy1Gx2MGBIC = _EtsysOidPhy1Gx2MGBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 34)
)
if mibBuilder.loadTexts:
    etsysOidPhy1Gx2MGBIC.setStatus("current")
_EtsysOidPhy1Hx2TX_ObjectIdentity = ObjectIdentity
etsysOidPhy1Hx2TX = _EtsysOidPhy1Hx2TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 35)
)
if mibBuilder.loadTexts:
    etsysOidPhy1Hx2TX.setStatus("current")
_EtsysOidPhyZPIMxZ1_ObjectIdentity = ObjectIdentity
etsysOidPhyZPIMxZ1 = _EtsysOidPhyZPIMxZ1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 36)
)
if mibBuilder.loadTexts:
    etsysOidPhyZPIMxZ1.setStatus("current")
_EtsysOidPhyER16xCS_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xCS = _EtsysOidPhyER16xCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 37)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xCS.setStatus("current")
_EtsysOidPhyXPx16_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx16 = _EtsysOidPhyXPx16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 38)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx16.setStatus("current")
_EtsysOidPhyXPx8_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx8 = _EtsysOidPhyXPx8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 39)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx8.setStatus("current")
_EtsysOidPhyXPx2xB128_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xB128 = _EtsysOidPhyXPx2xB128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 40)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xB128.setStatus("current")
_EtsysOidPhyXPx2xGSX_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xGSX = _EtsysOidPhyXPx2xGSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 41)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xGSX.setStatus("current")
_EtsysOidPhyER16x04_ObjectIdentity = ObjectIdentity
etsysOidPhyER16x04 = _EtsysOidPhyER16x04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 42)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16x04.setStatus("current")
_EtsysOidPhyER16x08_ObjectIdentity = ObjectIdentity
etsysOidPhyER16x08 = _EtsysOidPhyER16x08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 43)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16x08.setStatus("current")
_EtsysOidPhyER16xSXx08_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xSXx08 = _EtsysOidPhyER16xSXx08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 44)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xSXx08.setStatus("current")
_EtsysOidPhyER16xTXx24_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xTXx24 = _EtsysOidPhyER16xTXx24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 45)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xTXx24.setStatus("current")
_EtsysOidPhyER16xTXx32_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xTXx32 = _EtsysOidPhyER16xTXx32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 46)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xTXx32.setStatus("current")
_EtsysOidPhyER16xAC_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xAC = _EtsysOidPhyER16xAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 47)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xAC.setStatus("current")
_EtsysOidPhyER16xFN_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xFN = _EtsysOidPhyER16xFN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 48)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xFN.setStatus("current")
_EtsysOidPhyER16xCK_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xCK = _EtsysOidPhyER16xCK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 49)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xCK.setStatus("current")
_EtsysOidPhyER16xSF_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xSF = _EtsysOidPhyER16xSF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 50)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xSF.setStatus("current")
_EtsysOidPhyER16xCM3_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xCM3 = _EtsysOidPhyER16xCM3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 51)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xCM3.setStatus("current")
_EtsysOidPhyER16xCM4_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xCM4 = _EtsysOidPhyER16xCM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 52)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xCM4.setStatus("current")
_EtsysOidPhySSRxPSx16_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxPSx16 = _EtsysOidPhySSRxPSx16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 53)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxPSx16.setStatus("current")
_EtsysOidPhySSRxPSx16xDC_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxPSx16xDC = _EtsysOidPhySSRxPSx16xDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 54)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxPSx16xDC.setStatus("current")
_EtsysOidPhySSRxSFx16_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxSFx16 = _EtsysOidPhySSRxSFx16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 55)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxSFx16.setStatus("current")
_EtsysOidPhySSRxFANx16_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxFANx16 = _EtsysOidPhySSRxFANx16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 56)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxFANx16.setStatus("current")
_EtsysOidPhySSRxPSx8_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxPSx8 = _EtsysOidPhySSRxPSx8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 57)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxPSx8.setStatus("current")
_EtsysOidPhySSRxPSx8xDC_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxPSx8xDC = _EtsysOidPhySSRxPSx8xDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 58)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxPSx8xDC.setStatus("current")
_EtsysOidPhySSRxFANx8_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxFANx8 = _EtsysOidPhySSRxFANx8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 59)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxFANx8.setStatus("current")
_EtsysOidPhyXPxPCMCIA_ObjectIdentity = ObjectIdentity
etsysOidPhyXPxPCMCIA = _EtsysOidPhyXPxPCMCIA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 60)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPxPCMCIA.setStatus("current")
_EtsysOidPhyXPxPCMCIAx16LN_ObjectIdentity = ObjectIdentity
etsysOidPhyXPxPCMCIAx16LN = _EtsysOidPhyXPxPCMCIAx16LN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 61)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPxPCMCIAx16LN.setStatus("current")
_EtsysOidPhyXPxPCMCIAx16AT_ObjectIdentity = ObjectIdentity
etsysOidPhyXPxPCMCIAx16AT = _EtsysOidPhyXPxPCMCIAx16AT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 62)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPxPCMCIAx16AT.setStatus("current")
_EtsysOidPhyXPxPCMCIAx32AT_ObjectIdentity = ObjectIdentity
etsysOidPhyXPxPCMCIAx32AT = _EtsysOidPhyXPxPCMCIAx32AT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 63)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPxPCMCIAx32AT.setStatus("current")
_EtsysOidPhySSRxCM2_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxCM2 = _EtsysOidPhySSRxCM2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 64)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxCM2.setStatus("current")
_EtsysOidPhySSRxCM3_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxCM3 = _EtsysOidPhySSRxCM3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 65)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxCM3.setStatus("current")
_EtsysOidPhySSRxCM4_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxCM4 = _EtsysOidPhySSRxCM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 66)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxCM4.setStatus("current")
_EtsysOidPhy10100T_ObjectIdentity = ObjectIdentity
etsysOidPhy10100T = _EtsysOidPhy10100T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 67)
)
if mibBuilder.loadTexts:
    etsysOidPhy10100T.setStatus("deprecated")
_EtsysOidPhySSRxARE_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxARE = _EtsysOidPhySSRxARE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 68)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxARE.setStatus("current")
_EtsysOidPhySSRxATM29x02_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxATM29x02 = _EtsysOidPhySSRxATM29x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 69)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxATM29x02.setStatus("current")
_EtsysOidPhySSRxGTX32x02_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxGTX32x02 = _EtsysOidPhySSRxGTX32x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 70)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxGTX32x02.setStatus("current")
_EtsysOidPhySSRxGSX11x02_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxGSX11x02 = _EtsysOidPhySSRxGSX11x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 71)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxGSX11x02.setStatus("current")
_EtsysOidPhySSRxGSX21x02_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxGSX21x02 = _EtsysOidPhySSRxGSX21x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 72)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxGSX21x02.setStatus("current")
_EtsysOidPhySSRxGSX21x02xAA_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxGSX21x02xAA = _EtsysOidPhySSRxGSX21x02xAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 73)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxGSX21x02xAA.setStatus("current")
_EtsysOidPhySSRxGSX31x02_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxGSX31x02 = _EtsysOidPhySSRxGSX31x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 74)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxGSX31x02.setStatus("current")
_EtsysOidPhySSRxGLX19x02_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxGLX19x02 = _EtsysOidPhySSRxGLX19x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 75)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxGLX19x02.setStatus("current")
_EtsysOidPhySSRxGLX29x02_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxGLX29x02 = _EtsysOidPhySSRxGLX29x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 76)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxGLX29x02.setStatus("current")
_EtsysOidPhySSRxGLX29x02xAA_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxGLX29x02xAA = _EtsysOidPhySSRxGLX29x02xAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 77)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxGLX29x02xAA.setStatus("current")
_EtsysOidPhySSRxGLX39x02_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxGLX39x02 = _EtsysOidPhySSRxGLX39x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 78)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxGLX39x02.setStatus("current")
_EtsysOidPhySSRxGLH39x02_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxGLH39x02 = _EtsysOidPhySSRxGLH39x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 79)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxGLH39x02.setStatus("current")
_EtsysOidPhySSRxGLX70x01_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxGLX70x01 = _EtsysOidPhySSRxGLX70x01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 80)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxGLX70x01.setStatus("current")
_EtsysOidPhySSRxGLX70x01xAA_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxGLX70x01xAA = _EtsysOidPhySSRxGLX70x01xAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 81)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxGLX70x01xAA.setStatus("current")
_EtsysOidPhySSRxHTX12x08_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxHTX12x08 = _EtsysOidPhySSRxHTX12x08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 82)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxHTX12x08.setStatus("current")
_EtsysOidPhySSRxHTX12x08xAA_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxHTX12x08xAA = _EtsysOidPhySSRxHTX12x08xAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 83)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxHTX12x08xAA.setStatus("current")
_EtsysOidPhySSRxHTX22x08_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxHTX22x08 = _EtsysOidPhySSRxHTX22x08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 84)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxHTX22x08.setStatus("current")
_EtsysOidPhySSRxHTX22x08xAA_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxHTX22x08xAA = _EtsysOidPhySSRxHTX22x08xAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 85)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxHTX22x08xAA.setStatus("current")
_EtsysOidPhySSRxHTX32x16_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxHTX32x16 = _EtsysOidPhySSRxHTX32x16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 86)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxHTX32x16.setStatus("current")
_EtsysOidPhySSRxHFX11x08_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxHFX11x08 = _EtsysOidPhySSRxHFX11x08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 87)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxHFX11x08.setStatus("current")
_EtsysOidPhySSRxHFX21x08_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxHFX21x08 = _EtsysOidPhySSRxHFX21x08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 88)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxHFX21x08.setStatus("current")
_EtsysOidPhySSRxHFX21x08xAA_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxHFX21x08xAA = _EtsysOidPhySSRxHFX21x08xAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 89)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxHFX21x08xAA.setStatus("current")
_EtsysOidPhySSRxHFX29x08_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxHFX29x08 = _EtsysOidPhySSRxHFX29x08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 90)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxHFX29x08.setStatus("current")
_EtsysOidPhySSRxHFX29x08xAA_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxHFX29x08xAA = _EtsysOidPhySSRxHFX29x08xAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 91)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxHFX29x08xAA.setStatus("current")
_EtsysOidPhySSRxFDDIx02_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxFDDIx02 = _EtsysOidPhySSRxFDDIx02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 92)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxFDDIx02.setStatus("current")
_EtsysOidPhySSRxHSSIx02_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxHSSIx02 = _EtsysOidPhySSRxHSSIx02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 93)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxHSSIx02.setStatus("current")
_EtsysOidPhySSRxHSSIx02xAA_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxHSSIx02xAA = _EtsysOidPhySSRxHSSIx02xAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 94)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxHSSIx02xAA.setStatus("current")
_EtsysOidPhySSRxSERCx04_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxSERCx04 = _EtsysOidPhySSRxSERCx04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 95)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxSERCx04.setStatus("current")
_EtsysOidPhySSRxSERCx04xAA_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxSERCx04xAA = _EtsysOidPhySSRxSERCx04xAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 96)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxSERCx04xAA.setStatus("current")
_EtsysOidPhySSRxSERCEx04_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxSERCEx04 = _EtsysOidPhySSRxSERCEx04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 97)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxSERCEx04.setStatus("current")
_EtsysOidPhySSRxSERCEx04xAA_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxSERCEx04xAA = _EtsysOidPhySSRxSERCEx04xAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 98)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxSERCEx04xAA.setStatus("current")
_EtsysOidPhySSRxPOS21x04_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxPOS21x04 = _EtsysOidPhySSRxPOS21x04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 99)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxPOS21x04.setStatus("current")
_EtsysOidPhySSRxPOS29x04_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxPOS29x04 = _EtsysOidPhySSRxPOS29x04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 100)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxPOS29x04.setStatus("current")
_EtsysOidPhySSRxPOS31x02_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxPOS31x02 = _EtsysOidPhySSRxPOS31x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 101)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxPOS31x02.setStatus("current")
_EtsysOidPhySSRxPOS39x02_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxPOS39x02 = _EtsysOidPhySSRxPOS39x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 102)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxPOS39x02.setStatus("current")
_EtsysOidPhyXP2IntCM_ObjectIdentity = ObjectIdentity
etsysOidPhyXP2IntCM = _EtsysOidPhyXP2IntCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 103)
)
if mibBuilder.loadTexts:
    etsysOidPhyXP2IntCM.setStatus("current")
_EtsysOidPhyXP2IntPs_ObjectIdentity = ObjectIdentity
etsysOidPhyXP2IntPs = _EtsysOidPhyXP2IntPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 104)
)
if mibBuilder.loadTexts:
    etsysOidPhyXP2IntPs.setStatus("current")
_EtsysOidPhyXP2IntTX08_ObjectIdentity = ObjectIdentity
etsysOidPhyXP2IntTX08 = _EtsysOidPhyXP2IntTX08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 105)
)
if mibBuilder.loadTexts:
    etsysOidPhyXP2IntTX08.setStatus("current")
_EtsysOidPhyXPx2xTX_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xTX = _EtsysOidPhyXPx2xTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 106)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xTX.setStatus("current")
_EtsysOidPhyXPx2xTXxAA_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xTXxAA = _EtsysOidPhyXPx2xTXxAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 107)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xTXxAA.setStatus("current")
_EtsysOidPhyXPx2xLX_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xLX = _EtsysOidPhyXPx2xLX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 108)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xLX.setStatus("current")
_EtsysOidPhyXPx2xLXxAA_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xLXxAA = _EtsysOidPhyXPx2xLXxAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 109)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xLXxAA.setStatus("current")
_EtsysOidPhyXPx2xLX70_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xLX70 = _EtsysOidPhyXPx2xLX70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 110)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xLX70.setStatus("current")
_EtsysOidPhyXPx2xLX70xAA_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xLX70xAA = _EtsysOidPhyXPx2xLX70xAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 111)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xLX70xAA.setStatus("current")
_EtsysOidPhyXPx2xSX_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xSX = _EtsysOidPhyXPx2xSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 112)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xSX.setStatus("current")
_EtsysOidPhyXPx2xSXxAA_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xSXxAA = _EtsysOidPhyXPx2xSXxAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 113)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xSXxAA.setStatus("current")
_EtsysOidPhyXPx2xFX_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xFX = _EtsysOidPhyXPx2xFX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 114)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xFX.setStatus("current")
_EtsysOidPhyXPx2xFXxAA_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xFXxAA = _EtsysOidPhyXPx2xFXxAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 115)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xFXxAA.setStatus("current")
_EtsysOidPhyXPx2xHSSIxAA_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xHSSIxAA = _EtsysOidPhyXPx2xHSSIxAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 116)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xHSSIxAA.setStatus("current")
_EtsysOidPhyXPx2xSER_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xSER = _EtsysOidPhyXPx2xSER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 117)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xSER.setStatus("current")
_EtsysOidPhyXPx2xSERxAA_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xSERxAA = _EtsysOidPhyXPx2xSERxAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 118)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xSERxAA.setStatus("current")
_EtsysOidPhyXPx2xSERC_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xSERC = _EtsysOidPhyXPx2xSERC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 119)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xSERC.setStatus("current")
_EtsysOidPhyXPx2xSERCxAA_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xSERCxAA = _EtsysOidPhyXPx2xSERCxAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 120)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xSERCxAA.setStatus("current")
_EtsysOidPhyXPx2xSERCE_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xSERCE = _EtsysOidPhyXPx2xSERCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 121)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xSERCE.setStatus("current")
_EtsysOidPhyXPx2xSERCExAA_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xSERCExAA = _EtsysOidPhyXPx2xSERCExAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 122)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xSERCExAA.setStatus("current")
_EtsysOidPhyXPxAPHYx21_ObjectIdentity = ObjectIdentity
etsysOidPhyXPxAPHYx21 = _EtsysOidPhyXPxAPHYx21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 123)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPxAPHYx21.setStatus("current")
_EtsysOidPhyXPxAPHYx22_ObjectIdentity = ObjectIdentity
etsysOidPhyXPxAPHYx22 = _EtsysOidPhyXPxAPHYx22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 124)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPxAPHYx22.setStatus("current")
_EtsysOidPhyXPxAPHYx29IR_ObjectIdentity = ObjectIdentity
etsysOidPhyXPxAPHYx29IR = _EtsysOidPhyXPxAPHYx29IR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 125)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPxAPHYx29IR.setStatus("current")
_EtsysOidPhyXPxAPHYx67_ObjectIdentity = ObjectIdentity
etsysOidPhyXPxAPHYx67 = _EtsysOidPhyXPxAPHYx67_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 126)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPxAPHYx67.setStatus("current")
_EtsysOidPhyXPxAPHYx77_ObjectIdentity = ObjectIdentity
etsysOidPhyXPxAPHYx77 = _EtsysOidPhyXPxAPHYx77_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 127)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPxAPHYx77.setStatus("current")
_EtsysOidPhyXPxAPHYx82_ObjectIdentity = ObjectIdentity
etsysOidPhyXPxAPHYx82 = _EtsysOidPhyXPxAPHYx82_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 128)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPxAPHYx82.setStatus("current")
_EtsysOidPhyXPxAPHYx92_ObjectIdentity = ObjectIdentity
etsysOidPhyXPxAPHYx92 = _EtsysOidPhyXPxAPHYx92_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 129)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPxAPHYx92.setStatus("current")
_EtsysOidPhyXPxFPHYx01_ObjectIdentity = ObjectIdentity
etsysOidPhyXPxFPHYx01 = _EtsysOidPhyXPxFPHYx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 130)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPxFPHYx01.setStatus("current")
_EtsysOidPhyXPxFPHYx02_ObjectIdentity = ObjectIdentity
etsysOidPhyXPxFPHYx02 = _EtsysOidPhyXPxFPHYx02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 131)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPxFPHYx02.setStatus("current")
_EtsysOidPhyXPxFPHYx09_ObjectIdentity = ObjectIdentity
etsysOidPhyXPxFPHYx09 = _EtsysOidPhyXPxFPHYx09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 132)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPxFPHYx09.setStatus("current")
_EtsysOidPhyHssiPort_ObjectIdentity = ObjectIdentity
etsysOidPhyHssiPort = _EtsysOidPhyHssiPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 133)
)
if mibBuilder.loadTexts:
    etsysOidPhyHssiPort.setStatus("current")
_EtsysOidPhySerialConnection_ObjectIdentity = ObjectIdentity
etsysOidPhySerialConnection = _EtsysOidPhySerialConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 134)
)
if mibBuilder.loadTexts:
    etsysOidPhySerialConnection.setStatus("current")
_EtsysOidPhySerialEia530AConnection_ObjectIdentity = ObjectIdentity
etsysOidPhySerialEia530AConnection = _EtsysOidPhySerialEia530AConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 135)
)
if mibBuilder.loadTexts:
    etsysOidPhySerialEia530AConnection.setStatus("current")
_EtsysOidPhySerialEia530Connection_ObjectIdentity = ObjectIdentity
etsysOidPhySerialEia530Connection = _EtsysOidPhySerialEia530Connection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 136)
)
if mibBuilder.loadTexts:
    etsysOidPhySerialEia530Connection.setStatus("current")
_EtsysOidPhySerialV35Connection_ObjectIdentity = ObjectIdentity
etsysOidPhySerialV35Connection = _EtsysOidPhySerialV35Connection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 137)
)
if mibBuilder.loadTexts:
    etsysOidPhySerialV35Connection.setStatus("current")
_EtsysOidPhySerialX21Connection_ObjectIdentity = ObjectIdentity
etsysOidPhySerialX21Connection = _EtsysOidPhySerialX21Connection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 138)
)
if mibBuilder.loadTexts:
    etsysOidPhySerialX21Connection.setStatus("current")
_EtsysOidPhyGigEthSXPort_ObjectIdentity = ObjectIdentity
etsysOidPhyGigEthSXPort = _EtsysOidPhyGigEthSXPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 139)
)
if mibBuilder.loadTexts:
    etsysOidPhyGigEthSXPort.setStatus("current")
_EtsysOidPhyGigEthLXPort_ObjectIdentity = ObjectIdentity
etsysOidPhyGigEthLXPort = _EtsysOidPhyGigEthLXPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 140)
)
if mibBuilder.loadTexts:
    etsysOidPhyGigEthLXPort.setStatus("current")
_EtsysOidPhyGigEthLLXPort_ObjectIdentity = ObjectIdentity
etsysOidPhyGigEthLLXPort = _EtsysOidPhyGigEthLLXPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 141)
)
if mibBuilder.loadTexts:
    etsysOidPhyGigEthLLXPort.setStatus("current")
_EtsysOidPhy6SSRLCGigEthBkplnPort_ObjectIdentity = ObjectIdentity
etsysOidPhy6SSRLCGigEthBkplnPort = _EtsysOidPhy6SSRLCGigEthBkplnPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 142)
)
if mibBuilder.loadTexts:
    etsysOidPhy6SSRLCGigEthBkplnPort.setStatus("deprecated")
_EtsysOidPhyGPIMx01_ObjectIdentity = ObjectIdentity
etsysOidPhyGPIMx01 = _EtsysOidPhyGPIMx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 143)
)
if mibBuilder.loadTexts:
    etsysOidPhyGPIMx01.setStatus("current")
_EtsysOidPhyGPIMx08_ObjectIdentity = ObjectIdentity
etsysOidPhyGPIMx08 = _EtsysOidPhyGPIMx08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 144)
)
if mibBuilder.loadTexts:
    etsysOidPhyGPIMx08.setStatus("current")
_EtsysOidPhyGPIMx09_ObjectIdentity = ObjectIdentity
etsysOidPhyGPIMx09 = _EtsysOidPhyGPIMx09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 145)
)
if mibBuilder.loadTexts:
    etsysOidPhyGPIMx09.setStatus("current")
_EtsysOidPhyFastEthMMFPort_ObjectIdentity = ObjectIdentity
etsysOidPhyFastEthMMFPort = _EtsysOidPhyFastEthMMFPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 146)
)
if mibBuilder.loadTexts:
    etsysOidPhyFastEthMMFPort.setStatus("current")
_EtsysOidPhyFastEthSMFPort_ObjectIdentity = ObjectIdentity
etsysOidPhyFastEthSMFPort = _EtsysOidPhyFastEthSMFPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 147)
)
if mibBuilder.loadTexts:
    etsysOidPhyFastEthSMFPort.setStatus("current")
_EtsysOidPhyER16Slot_ObjectIdentity = ObjectIdentity
etsysOidPhyER16Slot = _EtsysOidPhyER16Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 148)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16Slot.setStatus("current")
_EtsysOidPhyXP8Slot_ObjectIdentity = ObjectIdentity
etsysOidPhyXP8Slot = _EtsysOidPhyXP8Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 149)
)
if mibBuilder.loadTexts:
    etsysOidPhyXP8Slot.setStatus("current")
_EtsysOidPhyXP2Slot_ObjectIdentity = ObjectIdentity
etsysOidPhyXP2Slot = _EtsysOidPhyXP2Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 150)
)
if mibBuilder.loadTexts:
    etsysOidPhyXP2Slot.setStatus("current")
_EtsysOidPhyXP8IntFlash_ObjectIdentity = ObjectIdentity
etsysOidPhyXP8IntFlash = _EtsysOidPhyXP8IntFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 151)
)
if mibBuilder.loadTexts:
    etsysOidPhyXP8IntFlash.setStatus("current")
_EtsysOidPhyPOSOC3MMF_ObjectIdentity = ObjectIdentity
etsysOidPhyPOSOC3MMF = _EtsysOidPhyPOSOC3MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 152)
)
if mibBuilder.loadTexts:
    etsysOidPhyPOSOC3MMF.setStatus("current")
_EtsysOidPhyPOSOC3SMF_ObjectIdentity = ObjectIdentity
etsysOidPhyPOSOC3SMF = _EtsysOidPhyPOSOC3SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 153)
)
if mibBuilder.loadTexts:
    etsysOidPhyPOSOC3SMF.setStatus("current")
_EtsysOidPhyPOSOC12MMF_ObjectIdentity = ObjectIdentity
etsysOidPhyPOSOC12MMF = _EtsysOidPhyPOSOC12MMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 154)
)
if mibBuilder.loadTexts:
    etsysOidPhyPOSOC12MMF.setStatus("current")
_EtsysOidPhyPOSOC12SMF_ObjectIdentity = ObjectIdentity
etsysOidPhyPOSOC12SMF = _EtsysOidPhyPOSOC12SMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 155)
)
if mibBuilder.loadTexts:
    etsysOidPhyPOSOC12SMF.setStatus("current")
_EtsysOidPhy100BASEMTRJMMF_ObjectIdentity = ObjectIdentity
etsysOidPhy100BASEMTRJMMF = _EtsysOidPhy100BASEMTRJMMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 156)
)
if mibBuilder.loadTexts:
    etsysOidPhy100BASEMTRJMMF.setStatus("current")
_EtsysOidPhy1000BASET_ObjectIdentity = ObjectIdentity
etsysOidPhy1000BASET = _EtsysOidPhy1000BASET_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 157)
)
if mibBuilder.loadTexts:
    etsysOidPhy1000BASET.setStatus("deprecated")
_EtsysOidPhyXPx2xAtm_ObjectIdentity = ObjectIdentity
etsysOidPhyXPx2xAtm = _EtsysOidPhyXPx2xAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 158)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPx2xAtm.setStatus("current")
_EtsysOidPhyPortSlot_ObjectIdentity = ObjectIdentity
etsysOidPhyPortSlot = _EtsysOidPhyPortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 159)
)
if mibBuilder.loadTexts:
    etsysOidPhyPortSlot.setStatus("deprecated")
_EtsysOidPhyER16xFDDIx02_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xFDDIx02 = _EtsysOidPhyER16xFDDIx02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 160)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xFDDIx02.setStatus("current")
_EtsysOidPhyER16xATM29x02_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xATM29x02 = _EtsysOidPhyER16xATM29x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 161)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xATM29x02.setStatus("current")
_EtsysOidPhyER16xSERCx04xAA_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xSERCx04xAA = _EtsysOidPhyER16xSERCx04xAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 162)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xSERCx04xAA.setStatus("current")
_EtsysOidPhyER16xSERCEx04xA_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xSERCEx04xA = _EtsysOidPhyER16xSERCEx04xA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 163)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xSERCEx04xA.setStatus("current")
_EtsysOidPhyER16xHSSIx02xAA_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xHSSIx02xAA = _EtsysOidPhyER16xHSSIx02xAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 164)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xHSSIx02xAA.setStatus("current")
_EtsysOidPhyXPMemory64_ObjectIdentity = ObjectIdentity
etsysOidPhyXPMemory64 = _EtsysOidPhyXPMemory64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 165)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPMemory64.setStatus("current")
_EtsysOidPhyXPMemory128_ObjectIdentity = ObjectIdentity
etsysOidPhyXPMemory128 = _EtsysOidPhyXPMemory128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 166)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPMemory128.setStatus("current")
_EtsysOidPhyXPMemory256_ObjectIdentity = ObjectIdentity
etsysOidPhyXPMemory256 = _EtsysOidPhyXPMemory256_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 167)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPMemory256.setStatus("current")
_EtsysOidPhyXP8PowerSupplySlot_ObjectIdentity = ObjectIdentity
etsysOidPhyXP8PowerSupplySlot = _EtsysOidPhyXP8PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 168)
)
if mibBuilder.loadTexts:
    etsysOidPhyXP8PowerSupplySlot.setStatus("current")
_EtsysOidPhyXP16PowerSupplySlot_ObjectIdentity = ObjectIdentity
etsysOidPhyXP16PowerSupplySlot = _EtsysOidPhyXP16PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 169)
)
if mibBuilder.loadTexts:
    etsysOidPhyXP16PowerSupplySlot.setStatus("current")
_EtsysOidPhyER16PowerSupplySlot_ObjectIdentity = ObjectIdentity
etsysOidPhyER16PowerSupplySlot = _EtsysOidPhyER16PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 170)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16PowerSupplySlot.setStatus("current")
_EtsysOidPhyXP16SwitchingFabricSlot_ObjectIdentity = ObjectIdentity
etsysOidPhyXP16SwitchingFabricSlot = _EtsysOidPhyXP16SwitchingFabricSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 171)
)
if mibBuilder.loadTexts:
    etsysOidPhyXP16SwitchingFabricSlot.setStatus("current")
_EtsysOidPhyER16SwitchingFabricSlot_ObjectIdentity = ObjectIdentity
etsysOidPhyER16SwitchingFabricSlot = _EtsysOidPhyER16SwitchingFabricSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 172)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16SwitchingFabricSlot.setStatus("current")
_EtsysOidPhyNIMxSERx02_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxSERx02 = _EtsysOidPhyNIMxSERx02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 173)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxSERx02.setStatus("current")
_EtsysOidPhyNIMxSERx04_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxSERx04 = _EtsysOidPhyNIMxSERx04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 174)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxSERx04.setStatus("current")
_EtsysOidPhyNIMxT1E1x01_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxT1E1x01 = _EtsysOidPhyNIMxT1E1x01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 175)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxT1E1x01.setStatus("current")
_EtsysOidPhyNIMxT1E1x02_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxT1E1x02 = _EtsysOidPhyNIMxT1E1x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 176)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxT1E1x02.setStatus("current")
_EtsysOidPhyNIMxT1E1x04_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxT1E1x04 = _EtsysOidPhyNIMxT1E1x04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 177)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxT1E1x04.setStatus("current")
_EtsysOidPhyNIMxCT1E1x01_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxCT1E1x01 = _EtsysOidPhyNIMxCT1E1x01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 178)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxCT1E1x01.setStatus("current")
_EtsysOidPhyNIMxCT1E1x02_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxCT1E1x02 = _EtsysOidPhyNIMxCT1E1x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 179)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxCT1E1x02.setStatus("current")
_EtsysOidPhyNIMxCT1E1x04_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxCT1E1x04 = _EtsysOidPhyNIMxCT1E1x04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 180)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxCT1E1x04.setStatus("current")
_EtsysOidPhyER16xHFX31x24_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xHFX31x24 = _EtsysOidPhyER16xHFX31x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 181)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xHFX31x24.setStatus("current")
_EtsysOidPhyER16xHFX39x24_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xHFX39x24 = _EtsysOidPhyER16xHFX39x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 182)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xHFX39x24.setStatus("current")
_EtsysOidPhyER16xGTX32x04_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xGTX32x04 = _EtsysOidPhyER16xGTX32x04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 183)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xGTX32x04.setStatus("current")
_EtsysOidPhyER16xGTX32x08_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xGTX32x08 = _EtsysOidPhyER16xGTX32x08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 184)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xGTX32x08.setStatus("current")
_EtsysOidPhySSRxGTX32x04_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxGTX32x04 = _EtsysOidPhySSRxGTX32x04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 185)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxGTX32x04.setStatus("current")
_EtsysOidPhySSRxGSX31x04_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxGSX31x04 = _EtsysOidPhySSRxGSX31x04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 186)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxGSX31x04.setStatus("current")
_EtsysOidPhySSRxGLX39x04_ObjectIdentity = ObjectIdentity
etsysOidPhySSRxGLX39x04 = _EtsysOidPhySSRxGLX39x04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 187)
)
if mibBuilder.loadTexts:
    etsysOidPhySSRxGLX39x04.setStatus("current")
_EtsysOidPhy5SlotFTM1Backplane_ObjectIdentity = ObjectIdentity
etsysOidPhy5SlotFTM1Backplane = _EtsysOidPhy5SlotFTM1Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 188)
)
if mibBuilder.loadTexts:
    etsysOidPhy5SlotFTM1Backplane.setStatus("current")
_EtsysOidPhy7SlotFTM1Backplane_ObjectIdentity = ObjectIdentity
etsysOidPhy7SlotFTM1Backplane = _EtsysOidPhy7SlotFTM1Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 189)
)
if mibBuilder.loadTexts:
    etsysOidPhy7SlotFTM1Backplane.setStatus("current")
_EtsysOidPhy7SlotFTM2Backplane_ObjectIdentity = ObjectIdentity
etsysOidPhy7SlotFTM2Backplane = _EtsysOidPhy7SlotFTM2Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 190)
)
if mibBuilder.loadTexts:
    etsysOidPhy7SlotFTM2Backplane.setStatus("current")
_EtsysOidPhyER16xOS26x01_ObjectIdentity = ObjectIdentity
etsysOidPhyER16xOS26x01 = _EtsysOidPhyER16xOS26x01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 191)
)
if mibBuilder.loadTexts:
    etsysOidPhyER16xOS26x01.setStatus("current")
_EtsysOidPhyMPC8240_ObjectIdentity = ObjectIdentity
etsysOidPhyMPC8240 = _EtsysOidPhyMPC8240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 192)
)
if mibBuilder.loadTexts:
    etsysOidPhyMPC8240.setStatus("current")
_EtsysOidPhyMPC8245_ObjectIdentity = ObjectIdentity
etsysOidPhyMPC8245 = _EtsysOidPhyMPC8245_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 193)
)
if mibBuilder.loadTexts:
    etsysOidPhyMPC8245.setStatus("current")
_EtsysOidPhy7G4202x30_ObjectIdentity = ObjectIdentity
etsysOidPhy7G4202x30 = _EtsysOidPhy7G4202x30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 194)
)
if mibBuilder.loadTexts:
    etsysOidPhy7G4202x30.setStatus("current")
_EtsysOidPhy7Gx6MGBIC_ObjectIdentity = ObjectIdentity
etsysOidPhy7Gx6MGBIC = _EtsysOidPhy7Gx6MGBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 195)
)
if mibBuilder.loadTexts:
    etsysOidPhy7Gx6MGBIC.setStatus("current")
_EtsysOidPhy7H4382x49_ObjectIdentity = ObjectIdentity
etsysOidPhy7H4382x49 = _EtsysOidPhy7H4382x49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 196)
)
if mibBuilder.loadTexts:
    etsysOidPhy7H4382x49.setStatus("current")
_EtsysOidPhy7K4290x02_ObjectIdentity = ObjectIdentity
etsysOidPhy7K4290x02 = _EtsysOidPhy7K4290x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 197)
)
if mibBuilder.loadTexts:
    etsysOidPhy7K4290x02.setStatus("current")
_EtsysOidPhy7H4204x48_ObjectIdentity = ObjectIdentity
etsysOidPhy7H4204x48 = _EtsysOidPhy7H4204x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 198)
)
if mibBuilder.loadTexts:
    etsysOidPhy7H4204x48.setStatus("current")
_EtsysOidPhy2H412x49R_ObjectIdentity = ObjectIdentity
etsysOidPhy2H412x49R = _EtsysOidPhy2H412x49R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 199)
)
if mibBuilder.loadTexts:
    etsysOidPhy2H412x49R.setStatus("current")
_EtsysOidPhy6C207x3_ObjectIdentity = ObjectIdentity
etsysOidPhy6C207x3 = _EtsysOidPhy6C207x3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 200)
)
if mibBuilder.loadTexts:
    etsysOidPhy6C207x3.setStatus("current")
_EtsysOidPhy6C203x1_ObjectIdentity = ObjectIdentity
etsysOidPhy6C203x1 = _EtsysOidPhy6C203x1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 201)
)
if mibBuilder.loadTexts:
    etsysOidPhy6C203x1.setStatus("obsolete")
_EtsysOidPhy6C403_ObjectIdentity = ObjectIdentity
etsysOidPhy6C403 = _EtsysOidPhy6C403_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 202)
)
if mibBuilder.loadTexts:
    etsysOidPhy6C403.setStatus("obsolete")
_EtsysOidPhy6C103_ObjectIdentity = ObjectIdentity
etsysOidPhy6C103 = _EtsysOidPhy6C103_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 203)
)
if mibBuilder.loadTexts:
    etsysOidPhy6C103.setStatus("obsolete")
_EtsysOidPhyVHxSMGMT2_ObjectIdentity = ObjectIdentity
etsysOidPhyVHxSMGMT2 = _EtsysOidPhyVHxSMGMT2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 204)
)
if mibBuilder.loadTexts:
    etsysOidPhyVHxSMGMT2.setStatus("current")
_EtsysOidPhyVHxRTMxL3_ObjectIdentity = ObjectIdentity
etsysOidPhyVHxRTMxL3 = _EtsysOidPhyVHxRTMxL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 205)
)
if mibBuilder.loadTexts:
    etsysOidPhyVHxRTMxL3.setStatus("current")
_EtsysOidPhyGPIMx02_ObjectIdentity = ObjectIdentity
etsysOidPhyGPIMx02 = _EtsysOidPhyGPIMx02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 206)
)
if mibBuilder.loadTexts:
    etsysOidPhyGPIMx02.setStatus("current")
_EtsysOidPhyNIMxBRIxSTx01_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxBRIxSTx01 = _EtsysOidPhyNIMxBRIxSTx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 207)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxBRIxSTx01.setStatus("current")
_EtsysOidPhyNIMxBRIxSTx02_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxBRIxSTx02 = _EtsysOidPhyNIMxBRIxSTx02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 208)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxBRIxSTx02.setStatus("current")
_EtsysOidPhyNIMxBRIxUx01_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxBRIxUx01 = _EtsysOidPhyNIMxBRIxUx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 209)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxBRIxUx01.setStatus("current")
_EtsysOidPhyNIMxBRIxUx02_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxBRIxUx02 = _EtsysOidPhyNIMxBRIxUx02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 210)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxBRIxUx02.setStatus("current")
_EtsysOidPhyC5C105_ObjectIdentity = ObjectIdentity
etsysOidPhyC5C105 = _EtsysOidPhyC5C105_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 211)
)
if mibBuilder.loadTexts:
    etsysOidPhyC5C105.setStatus("deprecated")
_EtsysOidPhyC5C305_ObjectIdentity = ObjectIdentity
etsysOidPhyC5C305 = _EtsysOidPhyC5C305_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 212)
)
if mibBuilder.loadTexts:
    etsysOidPhyC5C305.setStatus("deprecated")
_EtsysOidPhyC5C205x1_ObjectIdentity = ObjectIdentity
etsysOidPhyC5C205x1 = _EtsysOidPhyC5C205x1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 213)
)
if mibBuilder.loadTexts:
    etsysOidPhyC5C205x1.setStatus("deprecated")
_EtsysOidPhyC5H124x48_ObjectIdentity = ObjectIdentity
etsysOidPhyC5H124x48 = _EtsysOidPhyC5H124x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 214)
)
if mibBuilder.loadTexts:
    etsysOidPhyC5H124x48.setStatus("deprecated")
_EtsysOidPhyC5G124x36_ObjectIdentity = ObjectIdentity
etsysOidPhyC5G124x36 = _EtsysOidPhyC5G124x36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 215)
)
if mibBuilder.loadTexts:
    etsysOidPhyC5G124x36.setStatus("deprecated")
_EtsysOidPhyC5G122x24_ObjectIdentity = ObjectIdentity
etsysOidPhyC5G122x24 = _EtsysOidPhyC5G122x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 216)
)
if mibBuilder.loadTexts:
    etsysOidPhyC5G122x24.setStatus("deprecated")
_EtsysOidPhyC5G114x4_ObjectIdentity = ObjectIdentity
etsysOidPhyC5G114x4 = _EtsysOidPhyC5G114x4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 217)
)
if mibBuilder.loadTexts:
    etsysOidPhyC5G114x4.setStatus("deprecated")
_EtsysOidPhyC5G124x4_ObjectIdentity = ObjectIdentity
etsysOidPhyC5G124x4 = _EtsysOidPhyC5G124x4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 218)
)
if mibBuilder.loadTexts:
    etsysOidPhyC5G124x4.setStatus("deprecated")
_EtsysOidPhyC5M100_ObjectIdentity = ObjectIdentity
etsysOidPhyC5M100 = _EtsysOidPhyC5M100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 219)
)
if mibBuilder.loadTexts:
    etsysOidPhyC5M100.setStatus("deprecated")
_EtsysOidPhyC2H124x48_ObjectIdentity = ObjectIdentity
etsysOidPhyC2H124x48 = _EtsysOidPhyC2H124x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 220)
)
if mibBuilder.loadTexts:
    etsysOidPhyC2H124x48.setStatus("current")
_EtsysOidPhyC2G124x36_ObjectIdentity = ObjectIdentity
etsysOidPhyC2G124x36 = _EtsysOidPhyC2G124x36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 221)
)
if mibBuilder.loadTexts:
    etsysOidPhyC2G124x36.setStatus("deprecated")
_EtsysOidPhyC2G122x24_ObjectIdentity = ObjectIdentity
etsysOidPhyC2G122x24 = _EtsysOidPhyC2G122x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 222)
)
if mibBuilder.loadTexts:
    etsysOidPhyC2G122x24.setStatus("deprecated")
_EtsysOidPhyC2M100_ObjectIdentity = ObjectIdentity
etsysOidPhyC2M100 = _EtsysOidPhyC2M100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 223)
)
if mibBuilder.loadTexts:
    etsysOidPhyC2M100.setStatus("deprecated")
_EtsysOidPhyC2C105_ObjectIdentity = ObjectIdentity
etsysOidPhyC2C105 = _EtsysOidPhyC2C105_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 224)
)
if mibBuilder.loadTexts:
    etsysOidPhyC2C105.setStatus("deprecated")
_EtsysOidPhyC2C100_ObjectIdentity = ObjectIdentity
etsysOidPhyC2C100 = _EtsysOidPhyC2C100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 225)
)
if mibBuilder.loadTexts:
    etsysOidPhyC2C100.setStatus("deprecated")
_EtsysOidPhy7G4270x10_ObjectIdentity = ObjectIdentity
etsysOidPhy7G4270x10 = _EtsysOidPhy7G4270x10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 226)
)
if mibBuilder.loadTexts:
    etsysOidPhy7G4270x10.setStatus("current")
_EtsysOidPhy7H4202x72_ObjectIdentity = ObjectIdentity
etsysOidPhy7H4202x72 = _EtsysOidPhy7H4202x72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 227)
)
if mibBuilder.loadTexts:
    etsysOidPhy7H4202x72.setStatus("current")
_EtsysOidPhy7C107_ObjectIdentity = ObjectIdentity
etsysOidPhy7C107 = _EtsysOidPhy7C107_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 228)
)
if mibBuilder.loadTexts:
    etsysOidPhy7C107.setStatus("current")
_EtsysOidPhy7C103_ObjectIdentity = ObjectIdentity
etsysOidPhy7C103 = _EtsysOidPhy7C103_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 229)
)
if mibBuilder.loadTexts:
    etsysOidPhy7C103.setStatus("current")
_EtsysOidPhy7C203x1_ObjectIdentity = ObjectIdentity
etsysOidPhy7C203x1 = _EtsysOidPhy7C203x1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 230)
)
if mibBuilder.loadTexts:
    etsysOidPhy7C203x1.setStatus("current")
_EtsysOidPhy7C403_ObjectIdentity = ObjectIdentity
etsysOidPhy7C403 = _EtsysOidPhy7C403_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 231)
)
if mibBuilder.loadTexts:
    etsysOidPhy7C403.setStatus("current")
_EtsysOidPhy7G4275x12_ObjectIdentity = ObjectIdentity
etsysOidPhy7G4275x12 = _EtsysOidPhy7G4275x12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 232)
)
if mibBuilder.loadTexts:
    etsysOidPhy7G4275x12.setStatus("current")
_EtsysOidPhy7G4270x09_ObjectIdentity = ObjectIdentity
etsysOidPhy7G4270x09 = _EtsysOidPhy7G4270x09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 233)
)
if mibBuilder.loadTexts:
    etsysOidPhy7G4270x09.setStatus("current")
_EtsysOidPhyNIMxC16T3x01_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxC16T3x01 = _EtsysOidPhyNIMxC16T3x01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 234)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxC16T3x01.setStatus("current")
_EtsysOidPhyNIMxC16E3x01_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxC16E3x01 = _EtsysOidPhyNIMxC16E3x01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 235)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxC16E3x01.setStatus("current")
_EtsysOidPhyNIMxT3E3x01_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxT3E3x01 = _EtsysOidPhyNIMxT3E3x01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 236)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxT3E3x01.setStatus("current")
_EtsysOidPhyNIMxC16T3Sx01_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxC16T3Sx01 = _EtsysOidPhyNIMxC16T3Sx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 237)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxC16T3Sx01.setStatus("current")
_EtsysOidPhyNIMxC16E3Sx01_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxC16E3Sx01 = _EtsysOidPhyNIMxC16E3Sx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 238)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxC16E3Sx01.setStatus("current")
_EtsysOidPhyNIMxC16T3GSx01_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxC16T3GSx01 = _EtsysOidPhyNIMxC16T3GSx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 239)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxC16T3GSx01.setStatus("current")
_EtsysOidPhyNIMxT3Sx01_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxT3Sx01 = _EtsysOidPhyNIMxT3Sx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 240)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxT3Sx01.setStatus("current")
_EtsysOidPhyNIMxE3Sx01_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxE3Sx01 = _EtsysOidPhyNIMxE3Sx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 241)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxE3Sx01.setStatus("current")
_EtsysOidPhyNIMxETHxTGRx01_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxETHxTGRx01 = _EtsysOidPhyNIMxETHxTGRx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 242)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxETHxTGRx01.setStatus("deprecated")
_EtsysOidPhyNIMxADSLxACx01_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxADSLxACx01 = _EtsysOidPhyNIMxADSLxACx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 243)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxADSLxACx01.setStatus("current")
_EtsysOidPhyNIMxADSLxBx01_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxADSLxBx01 = _EtsysOidPhyNIMxADSLxBx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 244)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxADSLxBx01.setStatus("current")
_EtsysOidPhy7H4383x49_ObjectIdentity = ObjectIdentity
etsysOidPhy7H4383x49 = _EtsysOidPhy7H4383x49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 245)
)
if mibBuilder.loadTexts:
    etsysOidPhy7H4383x49.setStatus("current")
_EtsysOidPhy7H4284x49_ObjectIdentity = ObjectIdentity
etsysOidPhy7H4284x49 = _EtsysOidPhy7H4284x49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 246)
)
if mibBuilder.loadTexts:
    etsysOidPhy7H4284x49.setStatus("current")
_EtsysOidPhyV2G121x1_ObjectIdentity = ObjectIdentity
etsysOidPhyV2G121x1 = _EtsysOidPhyV2G121x1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 247)
)
if mibBuilder.loadTexts:
    etsysOidPhyV2G121x1.setStatus("current")
_EtsysOidPhyV2G112x2_ObjectIdentity = ObjectIdentity
etsysOidPhyV2G112x2 = _EtsysOidPhyV2G112x2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 248)
)
if mibBuilder.loadTexts:
    etsysOidPhyV2G112x2.setStatus("current")
_EtsysOidPhyV2G151x1M_ObjectIdentity = ObjectIdentity
etsysOidPhyV2G151x1M = _EtsysOidPhyV2G151x1M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 249)
)
if mibBuilder.loadTexts:
    etsysOidPhyV2G151x1M.setStatus("current")
_EtsysOidPhyV2G151x1S_ObjectIdentity = ObjectIdentity
etsysOidPhyV2G151x1S = _EtsysOidPhyV2G151x1S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 250)
)
if mibBuilder.loadTexts:
    etsysOidPhyV2G151x1S.setStatus("current")
_EtsysOidPhy1Hx8FX_ObjectIdentity = ObjectIdentity
etsysOidPhy1Hx8FX = _EtsysOidPhy1Hx8FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 251)
)
if mibBuilder.loadTexts:
    etsysOidPhy1Hx8FX.setStatus("current")
_EtsysOidPhyE1FxdAcPwrSup_ObjectIdentity = ObjectIdentity
etsysOidPhyE1FxdAcPwrSup = _EtsysOidPhyE1FxdAcPwrSup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 252)
)
if mibBuilder.loadTexts:
    etsysOidPhyE1FxdAcPwrSup.setStatus("current")
_EtsysOidPhyNIMxETHRx01_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxETHRx01 = _EtsysOidPhyNIMxETHRx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 253)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxETHRx01.setStatus("current")
_EtsysOidPhyNIMxFIBRx01_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxFIBRx01 = _EtsysOidPhyNIMxFIBRx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 254)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxFIBRx01.setStatus("current")
_EtsysOidPhyNIMxDIRELAYx02_ObjectIdentity = ObjectIdentity
etsysOidPhyNIMxDIRELAYx02 = _EtsysOidPhyNIMxDIRELAYx02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 255)
)
if mibBuilder.loadTexts:
    etsysOidPhyNIMxDIRELAYx02.setStatus("current")
_EtsysOidPhy7G4202x60_ObjectIdentity = ObjectIdentity
etsysOidPhy7G4202x60 = _EtsysOidPhy7G4202x60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 256)
)
if mibBuilder.loadTexts:
    etsysOidPhy7G4202x60.setStatus("current")
_EtsysOidPhy7G4282x41_ObjectIdentity = ObjectIdentity
etsysOidPhy7G4282x41 = _EtsysOidPhy7G4282x41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 257)
)
if mibBuilder.loadTexts:
    etsysOidPhy7G4282x41.setStatus("current")
_EtsysOidPhyMGBICNoConnector_ObjectIdentity = ObjectIdentity
etsysOidPhyMGBICNoConnector = _EtsysOidPhyMGBICNoConnector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 258)
)
if mibBuilder.loadTexts:
    etsysOidPhyMGBICNoConnector.setStatus("current")
_EtsysOidPhyN7PowerSupplySlot_ObjectIdentity = ObjectIdentity
etsysOidPhyN7PowerSupplySlot = _EtsysOidPhyN7PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 259)
)
if mibBuilder.loadTexts:
    etsysOidPhyN7PowerSupplySlot.setStatus("current")
_EtsysOidPhyN7FanTraySlot_ObjectIdentity = ObjectIdentity
etsysOidPhyN7FanTraySlot = _EtsysOidPhyN7FanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 260)
)
if mibBuilder.loadTexts:
    etsysOidPhyN7FanTraySlot.setStatus("current")
_EtsysOidPhyN7ModuleSlot_ObjectIdentity = ObjectIdentity
etsysOidPhyN7ModuleSlot = _EtsysOidPhyN7ModuleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 261)
)
if mibBuilder.loadTexts:
    etsysOidPhyN7ModuleSlot.setStatus("current")
_EtsysOidPhyN3PowerSupplySlot_ObjectIdentity = ObjectIdentity
etsysOidPhyN3PowerSupplySlot = _EtsysOidPhyN3PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 262)
)
if mibBuilder.loadTexts:
    etsysOidPhyN3PowerSupplySlot.setStatus("current")
_EtsysOidPhyN3FanTraySlot_ObjectIdentity = ObjectIdentity
etsysOidPhyN3FanTraySlot = _EtsysOidPhyN3FanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 263)
)
if mibBuilder.loadTexts:
    etsysOidPhyN3FanTraySlot.setStatus("current")
_EtsysOidPhyN3ModuleSlot_ObjectIdentity = ObjectIdentity
etsysOidPhyN3ModuleSlot = _EtsysOidPhyN3ModuleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 264)
)
if mibBuilder.loadTexts:
    etsysOidPhyN3ModuleSlot.setStatus("current")
_EtsysOidPhyE7PowerSupplySlot_ObjectIdentity = ObjectIdentity
etsysOidPhyE7PowerSupplySlot = _EtsysOidPhyE7PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 265)
)
if mibBuilder.loadTexts:
    etsysOidPhyE7PowerSupplySlot.setStatus("current")
_EtsysOidPhyE7FanTraySlot_ObjectIdentity = ObjectIdentity
etsysOidPhyE7FanTraySlot = _EtsysOidPhyE7FanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 266)
)
if mibBuilder.loadTexts:
    etsysOidPhyE7FanTraySlot.setStatus("current")
_EtsysOidPhyE7ModuleSlot_ObjectIdentity = ObjectIdentity
etsysOidPhyE7ModuleSlot = _EtsysOidPhyE7ModuleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 267)
)
if mibBuilder.loadTexts:
    etsysOidPhyE7ModuleSlot.setStatus("current")
_EtsysOidPhyRj45ConsolePort_ObjectIdentity = ObjectIdentity
etsysOidPhyRj45ConsolePort = _EtsysOidPhyRj45ConsolePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 268)
)
if mibBuilder.loadTexts:
    etsysOidPhyRj45ConsolePort.setStatus("current")
_EtsysOidPhyMGBICx02_ObjectIdentity = ObjectIdentity
etsysOidPhyMGBICx02 = _EtsysOidPhyMGBICx02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 269)
)
if mibBuilder.loadTexts:
    etsysOidPhyMGBICx02.setStatus("current")
_EtsysOidPhyMGBICx08_ObjectIdentity = ObjectIdentity
etsysOidPhyMGBICx08 = _EtsysOidPhyMGBICx08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 270)
)
if mibBuilder.loadTexts:
    etsysOidPhyMGBICx08.setStatus("current")
_EtsysOidPhy4H4203x72_ObjectIdentity = ObjectIdentity
etsysOidPhy4H4203x72 = _EtsysOidPhy4H4203x72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 271)
)
if mibBuilder.loadTexts:
    etsysOidPhy4H4203x72.setStatus("current")
_EtsysOidPhy4H4283x49_ObjectIdentity = ObjectIdentity
etsysOidPhy4H4283x49 = _EtsysOidPhy4H4283x49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 272)
)
if mibBuilder.loadTexts:
    etsysOidPhy4H4283x49.setStatus("current")
_EtsysOidPhy4G4282x41_ObjectIdentity = ObjectIdentity
etsysOidPhy4G4282x41 = _EtsysOidPhy4G4282x41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 273)
)
if mibBuilder.loadTexts:
    etsysOidPhy4G4282x41.setStatus("current")
_EtsysOidPhy4G4202x60_ObjectIdentity = ObjectIdentity
etsysOidPhy4G4202x60 = _EtsysOidPhy4G4202x60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 274)
)
if mibBuilder.loadTexts:
    etsysOidPhy4G4202x60.setStatus("current")
_EtsysOidPhy4H4282x49_ObjectIdentity = ObjectIdentity
etsysOidPhy4H4282x49 = _EtsysOidPhy4H4282x49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 275)
)
if mibBuilder.loadTexts:
    etsysOidPhy4H4282x49.setStatus("current")
_EtsysOidPhy4H4202x72_ObjectIdentity = ObjectIdentity
etsysOidPhy4H4202x72 = _EtsysOidPhy4H4202x72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 276)
)
if mibBuilder.loadTexts:
    etsysOidPhy4H4202x72.setStatus("current")
_EtsysOidPhy4H4284x49_ObjectIdentity = ObjectIdentity
etsysOidPhy4H4284x49 = _EtsysOidPhy4H4284x49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 277)
)
if mibBuilder.loadTexts:
    etsysOidPhy4H4284x49.setStatus("current")
_EtsysOidPhy7H4382x25_ObjectIdentity = ObjectIdentity
etsysOidPhy7H4382x25 = _EtsysOidPhy7H4382x25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 278)
)
if mibBuilder.loadTexts:
    etsysOidPhy7H4382x25.setStatus("current")
_EtsysOidPhyNoXenpak_ObjectIdentity = ObjectIdentity
etsysOidPhyNoXenpak = _EtsysOidPhyNoXenpak_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 279)
)
if mibBuilder.loadTexts:
    etsysOidPhyNoXenpak.setStatus("current")
_EtsysOidPhy4H4285x49_ObjectIdentity = ObjectIdentity
etsysOidPhy4H4285x49 = _EtsysOidPhy4H4285x49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 280)
)
if mibBuilder.loadTexts:
    etsysOidPhy4H4285x49.setStatus("current")
_EtsysOidPhy7H4385x49_ObjectIdentity = ObjectIdentity
etsysOidPhy7H4385x49 = _EtsysOidPhy7H4385x49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 281)
)
if mibBuilder.loadTexts:
    etsysOidPhy7H4385x49.setStatus("current")
_EtsysOidPhy7G4280x19_ObjectIdentity = ObjectIdentity
etsysOidPhy7G4280x19 = _EtsysOidPhy7G4280x19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 282)
)
if mibBuilder.loadTexts:
    etsysOidPhy7G4280x19.setStatus("current")
_EtsysOidPhyC2G124x24_ObjectIdentity = ObjectIdentity
etsysOidPhyC2G124x24 = _EtsysOidPhyC2G124x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 283)
)
if mibBuilder.loadTexts:
    etsysOidPhyC2G124x24.setStatus("current")
_EtsysOidPhyC2G124x48_ObjectIdentity = ObjectIdentity
etsysOidPhyC2G124x48 = _EtsysOidPhyC2G124x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 284)
)
if mibBuilder.loadTexts:
    etsysOidPhyC2G124x48.setStatus("current")
_EtsysOidPhyC2K122x24_ObjectIdentity = ObjectIdentity
etsysOidPhyC2K122x24 = _EtsysOidPhyC2K122x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 285)
)
if mibBuilder.loadTexts:
    etsysOidPhyC2K122x24.setStatus("current")
_EtsysOidPhyC2H124x48P_ObjectIdentity = ObjectIdentity
etsysOidPhyC2H124x48P = _EtsysOidPhyC2H124x48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 286)
)
if mibBuilder.loadTexts:
    etsysOidPhyC2H124x48P.setStatus("current")
_EtsysOidPhyC2G124x48P_ObjectIdentity = ObjectIdentity
etsysOidPhyC2G124x48P = _EtsysOidPhyC2G124x48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 287)
)
if mibBuilder.loadTexts:
    etsysOidPhyC2G124x48P.setStatus("current")
_EtsysOidPhy7G4202x72_ObjectIdentity = ObjectIdentity
etsysOidPhy7G4202x72 = _EtsysOidPhy7G4202x72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 288)
)
if mibBuilder.loadTexts:
    etsysOidPhy7G4202x72.setStatus("current")
_EtsysOidPhy7G4205x72_ObjectIdentity = ObjectIdentity
etsysOidPhy7G4205x72 = _EtsysOidPhy7G4205x72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 289)
)
if mibBuilder.loadTexts:
    etsysOidPhy7G4205x72.setStatus("current")
_EtsysOidPhy7G4282x49_ObjectIdentity = ObjectIdentity
etsysOidPhy7G4282x49 = _EtsysOidPhy7G4282x49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 290)
)
if mibBuilder.loadTexts:
    etsysOidPhy7G4282x49.setStatus("current")
_EtsysOidPhy7G4285x49_ObjectIdentity = ObjectIdentity
etsysOidPhy7G4285x49 = _EtsysOidPhy7G4285x49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 291)
)
if mibBuilder.loadTexts:
    etsysOidPhy7G4285x49.setStatus("current")
_EtsysOidPhy4G4202x72_ObjectIdentity = ObjectIdentity
etsysOidPhy4G4202x72 = _EtsysOidPhy4G4202x72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 292)
)
if mibBuilder.loadTexts:
    etsysOidPhy4G4202x72.setStatus("current")
_EtsysOidPhy4G4205x72_ObjectIdentity = ObjectIdentity
etsysOidPhy4G4205x72 = _EtsysOidPhy4G4205x72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 293)
)
if mibBuilder.loadTexts:
    etsysOidPhy4G4205x72.setStatus("current")
_EtsysOidPhy4G4282x49_ObjectIdentity = ObjectIdentity
etsysOidPhy4G4282x49 = _EtsysOidPhy4G4282x49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 294)
)
if mibBuilder.loadTexts:
    etsysOidPhy4G4282x49.setStatus("current")
_EtsysOidPhy4G4285x49_ObjectIdentity = ObjectIdentity
etsysOidPhy4G4285x49 = _EtsysOidPhy4G4285x49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 295)
)
if mibBuilder.loadTexts:
    etsysOidPhy4G4285x49.setStatus("current")
_EtsysOidPhyMGBICxLC03_ObjectIdentity = ObjectIdentity
etsysOidPhyMGBICxLC03 = _EtsysOidPhyMGBICxLC03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 296)
)
if mibBuilder.loadTexts:
    etsysOidPhyMGBICxLC03.setStatus("current")
_EtsysOidPhyNxPOE_ObjectIdentity = ObjectIdentity
etsysOidPhyNxPOE = _EtsysOidPhyNxPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 297)
)
if mibBuilder.loadTexts:
    etsysOidPhyNxPOE.setStatus("current")
_EtsysOidPhyNxPOEx1200W_ObjectIdentity = ObjectIdentity
etsysOidPhyNxPOEx1200W = _EtsysOidPhyNxPOEx1200W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 298)
)
if mibBuilder.loadTexts:
    etsysOidPhyNxPOEx1200W.setStatus("current")
_EtsysOidPhyNxPOEPowerSupplySlot_ObjectIdentity = ObjectIdentity
etsysOidPhyNxPOEPowerSupplySlot = _EtsysOidPhyNxPOEPowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 299)
)
if mibBuilder.loadTexts:
    etsysOidPhyNxPOEPowerSupplySlot.setStatus("current")
_EtsysOidPhy7C105xP_ObjectIdentity = ObjectIdentity
etsysOidPhy7C105xP = _EtsysOidPhy7C105xP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 300)
)
if mibBuilder.loadTexts:
    etsysOidPhy7C105xP.setStatus("current")
_EtsysOidPhy7C205x1_ObjectIdentity = ObjectIdentity
etsysOidPhy7C205x1 = _EtsysOidPhy7C205x1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 301)
)
if mibBuilder.loadTexts:
    etsysOidPhy7C205x1.setStatus("current")
_EtsysOidPhy7C405_ObjectIdentity = ObjectIdentity
etsysOidPhy7C405 = _EtsysOidPhy7C405_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 302)
)
if mibBuilder.loadTexts:
    etsysOidPhy7C405.setStatus("current")
_EtsysOidPhyN5PoEPowerSupplySlot_ObjectIdentity = ObjectIdentity
etsysOidPhyN5PoEPowerSupplySlot = _EtsysOidPhyN5PoEPowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 303)
)
if mibBuilder.loadTexts:
    etsysOidPhyN5PoEPowerSupplySlot.setStatus("current")
_EtsysOidPhyN5PoEFanTraySlot_ObjectIdentity = ObjectIdentity
etsysOidPhyN5PoEFanTraySlot = _EtsysOidPhyN5PoEFanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 304)
)
if mibBuilder.loadTexts:
    etsysOidPhyN5PoEFanTraySlot.setStatus("current")
_EtsysOidPhyN5PoEModuleSlot_ObjectIdentity = ObjectIdentity
etsysOidPhyN5PoEModuleSlot = _EtsysOidPhyN5PoEModuleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 305)
)
if mibBuilder.loadTexts:
    etsysOidPhyN5PoEModuleSlot.setStatus("current")
_EtsysOidPhyV2H124x24FX_ObjectIdentity = ObjectIdentity
etsysOidPhyV2H124x24FX = _EtsysOidPhyV2H124x24FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 306)
)
if mibBuilder.loadTexts:
    etsysOidPhyV2H124x24FX.setStatus("current")
_EtsysOidPhy7Gx6MGBICxA_ObjectIdentity = ObjectIdentity
etsysOidPhy7Gx6MGBICxA = _EtsysOidPhy7Gx6MGBICxA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 307)
)
if mibBuilder.loadTexts:
    etsysOidPhy7Gx6MGBICxA.setStatus("current")
_EtsysOidPhyN5PoEPoEPowerSupplySlot_ObjectIdentity = ObjectIdentity
etsysOidPhyN5PoEPoEPowerSupplySlot = _EtsysOidPhyN5PoEPoEPowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 308)
)
if mibBuilder.loadTexts:
    etsysOidPhyN5PoEPoEPowerSupplySlot.setStatus("current")
_EtsysOidPhy7C117_ObjectIdentity = ObjectIdentity
etsysOidPhy7C117 = _EtsysOidPhy7C117_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 309)
)
if mibBuilder.loadTexts:
    etsysOidPhy7C117.setStatus("current")
_EtsysOidPhy7C115xP_ObjectIdentity = ObjectIdentity
etsysOidPhy7C115xP = _EtsysOidPhy7C115xP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 310)
)
if mibBuilder.loadTexts:
    etsysOidPhy7C115xP.setStatus("current")
_EtsysOidPhy7C113_ObjectIdentity = ObjectIdentity
etsysOidPhy7C113 = _EtsysOidPhy7C113_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 311)
)
if mibBuilder.loadTexts:
    etsysOidPhy7C113.setStatus("current")
_EtsysOidPhy7C111_ObjectIdentity = ObjectIdentity
etsysOidPhy7C111 = _EtsysOidPhy7C111_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 312)
)
if mibBuilder.loadTexts:
    etsysOidPhy7C111.setStatus("current")
_EtsysOidPhyN1ModuleSlot_ObjectIdentity = ObjectIdentity
etsysOidPhyN1ModuleSlot = _EtsysOidPhyN1ModuleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 313)
)
if mibBuilder.loadTexts:
    etsysOidPhyN1ModuleSlot.setStatus("current")
_EtsysOidPhyB2G124x24_ObjectIdentity = ObjectIdentity
etsysOidPhyB2G124x24 = _EtsysOidPhyB2G124x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 314)
)
if mibBuilder.loadTexts:
    etsysOidPhyB2G124x24.setStatus("current")
_EtsysOidPhyB2G124x48_ObjectIdentity = ObjectIdentity
etsysOidPhyB2G124x48 = _EtsysOidPhyB2G124x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 315)
)
if mibBuilder.loadTexts:
    etsysOidPhyB2G124x48.setStatus("current")
_EtsysOidPhyB2G124x48P_ObjectIdentity = ObjectIdentity
etsysOidPhyB2G124x48P = _EtsysOidPhyB2G124x48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 316)
)
if mibBuilder.loadTexts:
    etsysOidPhyB2G124x48P.setStatus("current")
_EtsysOidPhyB2H124x48_ObjectIdentity = ObjectIdentity
etsysOidPhyB2H124x48 = _EtsysOidPhyB2H124x48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 317)
)
if mibBuilder.loadTexts:
    etsysOidPhyB2H124x48.setStatus("current")
_EtsysOidPhyB2H124x48P_ObjectIdentity = ObjectIdentity
etsysOidPhyB2H124x48P = _EtsysOidPhyB2H124x48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 318)
)
if mibBuilder.loadTexts:
    etsysOidPhyB2H124x48P.setStatus("current")
_EtsysOidPhyB2G124x24P_ObjectIdentity = ObjectIdentity
etsysOidPhyB2G124x24P = _EtsysOidPhyB2G124x24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 319)
)
if mibBuilder.loadTexts:
    etsysOidPhyB2G124x24P.setStatus("current")
_EtsysOidPhyB2H124x24_ObjectIdentity = ObjectIdentity
etsysOidPhyB2H124x24 = _EtsysOidPhyB2H124x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 320)
)
if mibBuilder.loadTexts:
    etsysOidPhyB2H124x24.setStatus("current")
_EtsysOidPhyB2H124x24P_ObjectIdentity = ObjectIdentity
etsysOidPhyB2H124x24P = _EtsysOidPhyB2H124x24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 321)
)
if mibBuilder.loadTexts:
    etsysOidPhyB2H124x24P.setStatus("current")
_EtsysOidPhyB2H124x24FX_ObjectIdentity = ObjectIdentity
etsysOidPhyB2H124x24FX = _EtsysOidPhyB2H124x24FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 322)
)
if mibBuilder.loadTexts:
    etsysOidPhyB2H124x24FX.setStatus("current")
_EtsysOidPhyX16xC_ObjectIdentity = ObjectIdentity
etsysOidPhyX16xC = _EtsysOidPhyX16xC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 323)
)
if mibBuilder.loadTexts:
    etsysOidPhyX16xC.setStatus("current")
_EtsysOidPhyX8xC_ObjectIdentity = ObjectIdentity
etsysOidPhyX8xC = _EtsysOidPhyX8xC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 324)
)
if mibBuilder.loadTexts:
    etsysOidPhyX8xC.setStatus("current")
_EtsysOidPhyX4xC_ObjectIdentity = ObjectIdentity
etsysOidPhyX4xC = _EtsysOidPhyX4xC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 325)
)
if mibBuilder.loadTexts:
    etsysOidPhyX4xC.setStatus("current")
_EtsysOidPhyX16Backplane_ObjectIdentity = ObjectIdentity
etsysOidPhyX16Backplane = _EtsysOidPhyX16Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 326)
)
if mibBuilder.loadTexts:
    etsysOidPhyX16Backplane.setStatus("current")
_EtsysOidPhyX8Backplane_ObjectIdentity = ObjectIdentity
etsysOidPhyX8Backplane = _EtsysOidPhyX8Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 327)
)
if mibBuilder.loadTexts:
    etsysOidPhyX8Backplane.setStatus("current")
_EtsysOidPhyX4Backplane_ObjectIdentity = ObjectIdentity
etsysOidPhyX4Backplane = _EtsysOidPhyX4Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 328)
)
if mibBuilder.loadTexts:
    etsysOidPhyX4Backplane.setStatus("current")
_EtsysOidPhyXxFan_ObjectIdentity = ObjectIdentity
etsysOidPhyXxFan = _EtsysOidPhyXxFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 329)
)
if mibBuilder.loadTexts:
    etsysOidPhyXxFan.setStatus("current")
_EtsysOidPhyXxAC_ObjectIdentity = ObjectIdentity
etsysOidPhyXxAC = _EtsysOidPhyXxAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 330)
)
if mibBuilder.loadTexts:
    etsysOidPhyXxAC.setStatus("current")
_EtsysOidPhyXxCMx00_ObjectIdentity = ObjectIdentity
etsysOidPhyXxCMx00 = _EtsysOidPhyXxCMx00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 331)
)
if mibBuilder.loadTexts:
    etsysOidPhyXxCMx00.setStatus("current")
_EtsysOidPhyX4xCMFx160x00_ObjectIdentity = ObjectIdentity
etsysOidPhyX4xCMFx160x00 = _EtsysOidPhyX4xCMFx160x00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 332)
)
if mibBuilder.loadTexts:
    etsysOidPhyX4xCMFx160x00.setStatus("current")
_EtsysOidPhyX16xF640_ObjectIdentity = ObjectIdentity
etsysOidPhyX16xF640 = _EtsysOidPhyX16xF640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 333)
)
if mibBuilder.loadTexts:
    etsysOidPhyX16xF640.setStatus("current")
_EtsysOidPhyX8xF320_ObjectIdentity = ObjectIdentity
etsysOidPhyX8xF320 = _EtsysOidPhyX8xF320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 334)
)
if mibBuilder.loadTexts:
    etsysOidPhyX8xF320.setStatus("current")
_EtsysOidPhyXxM2x00_ObjectIdentity = ObjectIdentity
etsysOidPhyXxM2x00 = _EtsysOidPhyXxM2x00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 335)
)
if mibBuilder.loadTexts:
    etsysOidPhyXxM2x00.setStatus("current")
_EtsysOidPhyXxG32x00_ObjectIdentity = ObjectIdentity
etsysOidPhyXxG32x00 = _EtsysOidPhyXxG32x00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 336)
)
if mibBuilder.loadTexts:
    etsysOidPhyXxG32x00.setStatus("current")
_EtsysOidPhyXxT48x01_ObjectIdentity = ObjectIdentity
etsysOidPhyXxT48x01 = _EtsysOidPhyXxT48x01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 337)
)
if mibBuilder.loadTexts:
    etsysOidPhyXxT48x01.setStatus("current")
_EtsysOidPhyXxM2x01_ObjectIdentity = ObjectIdentity
etsysOidPhyXxM2x01 = _EtsysOidPhyXxM2x01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 338)
)
if mibBuilder.loadTexts:
    etsysOidPhyXxM2x01.setStatus("current")
_EtsysOidPhyXxM4x01_ObjectIdentity = ObjectIdentity
etsysOidPhyXxM4x01 = _EtsysOidPhyXxM4x01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 339)
)
if mibBuilder.loadTexts:
    etsysOidPhyXxM4x01.setStatus("current")
_EtsysOidPhyXxG20x01_ObjectIdentity = ObjectIdentity
etsysOidPhyXxG20x01 = _EtsysOidPhyXxG20x01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 340)
)
if mibBuilder.loadTexts:
    etsysOidPhyXxG20x01.setStatus("current")
_EtsysOidPhyXxG40x01_ObjectIdentity = ObjectIdentity
etsysOidPhyXxG40x01 = _EtsysOidPhyXxG40x01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 341)
)
if mibBuilder.loadTexts:
    etsysOidPhyXxG40x01.setStatus("current")
_EtsysOidPhyXIOModuleSlot_ObjectIdentity = ObjectIdentity
etsysOidPhyXIOModuleSlot = _EtsysOidPhyXIOModuleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 342)
)
if mibBuilder.loadTexts:
    etsysOidPhyXIOModuleSlot.setStatus("current")
_EtsysOidPhyXControlModuleSlot_ObjectIdentity = ObjectIdentity
etsysOidPhyXControlModuleSlot = _EtsysOidPhyXControlModuleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 343)
)
if mibBuilder.loadTexts:
    etsysOidPhyXControlModuleSlot.setStatus("current")
_EtsysOidPhyXFabricModuleSlot_ObjectIdentity = ObjectIdentity
etsysOidPhyXFabricModuleSlot = _EtsysOidPhyXFabricModuleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 344)
)
if mibBuilder.loadTexts:
    etsysOidPhyXFabricModuleSlot.setStatus("current")
_EtsysOidPhyXPowerSupplySlot_ObjectIdentity = ObjectIdentity
etsysOidPhyXPowerSupplySlot = _EtsysOidPhyXPowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 345)
)
if mibBuilder.loadTexts:
    etsysOidPhyXPowerSupplySlot.setStatus("current")
_EtsysOidPhyXFanTraySlot_ObjectIdentity = ObjectIdentity
etsysOidPhyXFanTraySlot = _EtsysOidPhyXFanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 346)
)
if mibBuilder.loadTexts:
    etsysOidPhyXFanTraySlot.setStatus("current")
_EtsysOidPhySFPxGBIC_ObjectIdentity = ObjectIdentity
etsysOidPhySFPxGBIC = _EtsysOidPhySFPxGBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 347)
)
if mibBuilder.loadTexts:
    etsysOidPhySFPxGBIC.setStatus("current")
_EtsysOidPhyXFPxGBIC_ObjectIdentity = ObjectIdentity
etsysOidPhyXFPxGBIC = _EtsysOidPhyXFPxGBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 348)
)
if mibBuilder.loadTexts:
    etsysOidPhyXFPxGBIC.setStatus("current")
_EtsysOidPhyXxT32x00_ObjectIdentity = ObjectIdentity
etsysOidPhyXxT32x00 = _EtsysOidPhyXxT32x00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 349)
)
if mibBuilder.loadTexts:
    etsysOidPhyXxT32x00.setStatus("current")
_EtsysOidPhyC2G134x24P_ObjectIdentity = ObjectIdentity
etsysOidPhyC2G134x24P = _EtsysOidPhyC2G134x24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 350)
)
if mibBuilder.loadTexts:
    etsysOidPhyC2G134x24P.setStatus("current")
_EtsysOidPhyXxGT16x00_ObjectIdentity = ObjectIdentity
etsysOidPhyXxGT16x00 = _EtsysOidPhyXxGT16x00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 351)
)
if mibBuilder.loadTexts:
    etsysOidPhyXxGT16x00.setStatus("current")
_EtsysOidPhyGigEthIntNEMPort_ObjectIdentity = ObjectIdentity
etsysOidPhyGigEthIntNEMPort = _EtsysOidPhyGigEthIntNEMPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 352)
)
if mibBuilder.loadTexts:
    etsysOidPhyGigEthIntNEMPort.setStatus("current")
_EtsysOidPhy7SxDSNSA7x01_ObjectIdentity = ObjectIdentity
etsysOidPhy7SxDSNSA7x01 = _EtsysOidPhy7SxDSNSA7x01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 353)
)
if mibBuilder.loadTexts:
    etsysOidPhy7SxDSNSA7x01.setStatus("current")
_EtsysOidPhy7SxNSTAGx01_ObjectIdentity = ObjectIdentity
etsysOidPhy7SxNSTAGx01 = _EtsysOidPhy7SxNSTAGx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 354)
)
if mibBuilder.loadTexts:
    etsysOidPhy7SxNSTAGx01.setStatus("current")
_EtsysOidPhyXxM8x01_ObjectIdentity = ObjectIdentity
etsysOidPhyXxM8x01 = _EtsysOidPhyXxM8x01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 355)
)
if mibBuilder.loadTexts:
    etsysOidPhyXxM8x01.setStatus("current")
_EtsysOidPhy7SxDSNSA7x01NPS_ObjectIdentity = ObjectIdentity
etsysOidPhy7SxDSNSA7x01NPS = _EtsysOidPhy7SxDSNSA7x01NPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 356)
)
if mibBuilder.loadTexts:
    etsysOidPhy7SxDSNSA7x01NPS.setStatus("current")
_EtsysOidPhy7SxNSTAGx01xNPS_ObjectIdentity = ObjectIdentity
etsysOidPhy7SxNSTAGx01xNPS = _EtsysOidPhy7SxNSTAGx01xNPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 357)
)
if mibBuilder.loadTexts:
    etsysOidPhy7SxNSTAGx01xNPS.setStatus("current")
_EtsysOidPhy9603805_ObjectIdentity = ObjectIdentity
etsysOidPhy9603805 = _EtsysOidPhy9603805_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 358)
)
if mibBuilder.loadTexts:
    etsysOidPhy9603805.setStatus("current")
_EtsysOidPhy9603806_ObjectIdentity = ObjectIdentity
etsysOidPhy9603806 = _EtsysOidPhy9603806_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 359)
)
if mibBuilder.loadTexts:
    etsysOidPhy9603806.setStatus("current")
_EtsysOidPhyC2G170x24_ObjectIdentity = ObjectIdentity
etsysOidPhyC2G170x24 = _EtsysOidPhyC2G170x24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 360)
)
if mibBuilder.loadTexts:
    etsysOidPhyC2G170x24.setStatus("current")
_EtsysOidPhy7G4082x25_ObjectIdentity = ObjectIdentity
etsysOidPhy7G4082x25 = _EtsysOidPhy7G4082x25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 361)
)
if mibBuilder.loadTexts:
    etsysOidPhy7G4082x25.setStatus("current")
_EtsysOidPhyI3Hx12TX_ObjectIdentity = ObjectIdentity
etsysOidPhyI3Hx12TX = _EtsysOidPhyI3Hx12TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 362)
)
if mibBuilder.loadTexts:
    etsysOidPhyI3Hx12TX.setStatus("current")
_EtsysOidPhyI3Hx4FXxMM_ObjectIdentity = ObjectIdentity
etsysOidPhyI3Hx4FXxMM = _EtsysOidPhyI3Hx4FXxMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 363)
)
if mibBuilder.loadTexts:
    etsysOidPhyI3Hx4FXxMM.setStatus("current")
_EtsysOidPhyI3Hx8FXxMM_ObjectIdentity = ObjectIdentity
etsysOidPhyI3Hx8FXxMM = _EtsysOidPhyI3Hx8FXxMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 364)
)
if mibBuilder.loadTexts:
    etsysOidPhyI3Hx8FXxMM.setStatus("current")
_EtsysOidPhyI3Hx8TXx2FX_ObjectIdentity = ObjectIdentity
etsysOidPhyI3Hx8TXx2FX = _EtsysOidPhyI3Hx8TXx2FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 365)
)
if mibBuilder.loadTexts:
    etsysOidPhyI3Hx8TXx2FX.setStatus("current")
_EtsysOidPhy7Gx6MGBICxB_ObjectIdentity = ObjectIdentity
etsysOidPhy7Gx6MGBICxB = _EtsysOidPhy7Gx6MGBICxB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 366)
)
if mibBuilder.loadTexts:
    etsysOidPhy7Gx6MGBICxB.setStatus("current")
_EtsysOidPhy7Kx2XFPx6MGBIC_ObjectIdentity = ObjectIdentity
etsysOidPhy7Kx2XFPx6MGBIC = _EtsysOidPhy7Kx2XFPx6MGBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 367)
)
if mibBuilder.loadTexts:
    etsysOidPhy7Kx2XFPx6MGBIC.setStatus("current")
_EtsysOidPhy7GR4280x19_ObjectIdentity = ObjectIdentity
etsysOidPhy7GR4280x19 = _EtsysOidPhy7GR4280x19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 368)
)
if mibBuilder.loadTexts:
    etsysOidPhy7GR4280x19.setStatus("current")
_EtsysOidPhy7GR4270x12_ObjectIdentity = ObjectIdentity
etsysOidPhy7GR4270x12 = _EtsysOidPhy7GR4270x12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 369)
)
if mibBuilder.loadTexts:
    etsysOidPhy7GR4270x12.setStatus("current")
_EtsysOidPhy7GR4202x30_ObjectIdentity = ObjectIdentity
etsysOidPhy7GR4202x30 = _EtsysOidPhy7GR4202x30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 370)
)
if mibBuilder.loadTexts:
    etsysOidPhy7GR4202x30.setStatus("current")
_EtsysOidPhy7KR4290x02_ObjectIdentity = ObjectIdentity
etsysOidPhy7KR4290x02 = _EtsysOidPhy7KR4290x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 371)
)
if mibBuilder.loadTexts:
    etsysOidPhy7KR4290x02.setStatus("current")
_EtsysOidPhyNoXfp_ObjectIdentity = ObjectIdentity
etsysOidPhyNoXfp = _EtsysOidPhyNoXfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 372)
)
if mibBuilder.loadTexts:
    etsysOidPhyNoXfp.setStatus("current")
_EtsysOidPhyMGBICxLC04_ObjectIdentity = ObjectIdentity
etsysOidPhyMGBICxLC04 = _EtsysOidPhyMGBICxLC04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 373)
)
if mibBuilder.loadTexts:
    etsysOidPhyMGBICxLC04.setStatus("current")
_EtsysOidPhy10GbExSRxXFP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExSRxXFP = _EtsysOidPhy10GbExSRxXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 374)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExSRxXFP.setStatus("current")
_EtsysOidPhy10GbExLRxXFP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExLRxXFP = _EtsysOidPhy10GbExLRxXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 375)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExLRxXFP.setStatus("current")
_EtsysOidPhy10GbExERxXFP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExERxXFP = _EtsysOidPhy10GbExERxXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 376)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExERxXFP.setStatus("current")
_EtsysOidPhy10GbExCX4xXFP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExCX4xXFP = _EtsysOidPhy10GbExCX4xXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 377)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExCX4xXFP.setStatus("current")
_EtsysOidPhy10GbExCX4_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExCX4 = _EtsysOidPhy10GbExCX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 378)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExCX4.setStatus("current")
_EtsysOidPhy10GbExSWxXFP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExSWxXFP = _EtsysOidPhy10GbExSWxXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 379)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExSWxXFP.setStatus("current")
_EtsysOidPhy10GbExLWxXFP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExLWxXFP = _EtsysOidPhy10GbExLWxXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 380)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExLWxXFP.setStatus("current")
_EtsysOidPhy10GbExEWxXFP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExEWxXFP = _EtsysOidPhy10GbExEWxXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 381)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExEWxXFP.setStatus("current")
_EtsysOidPhy10GbExLX4xXFP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExLX4xXFP = _EtsysOidPhy10GbExLX4xXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 382)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExLX4xXFP.setStatus("current")
_EtsysOidPhy10GbExZRxXFP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExZRxXFP = _EtsysOidPhy10GbExZRxXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 383)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExZRxXFP.setStatus("current")
_EtsysOidPhy10GbExZWxXFP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExZWxXFP = _EtsysOidPhy10GbExZWxXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 384)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExZWxXFP.setStatus("current")
_EtsysOidPhy10GbExZR_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExZR = _EtsysOidPhy10GbExZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 385)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExZR.setStatus("current")
_EtsysOidPhy10GbExZW_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExZW = _EtsysOidPhy10GbExZW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 386)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExZW.setStatus("current")
_EtsysOidPhyMGBICxLC05_ObjectIdentity = ObjectIdentity
etsysOidPhyMGBICxLC05 = _EtsysOidPhyMGBICxLC05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 387)
)
if mibBuilder.loadTexts:
    etsysOidPhyMGBICxLC05.setStatus("current")
_EtsysOidPhy7K4297x02_ObjectIdentity = ObjectIdentity
etsysOidPhy7K4297x02 = _EtsysOidPhy7K4297x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 388)
)
if mibBuilder.loadTexts:
    etsysOidPhy7K4297x02.setStatus("current")
_EtsysOidPhy7K4297x04_ObjectIdentity = ObjectIdentity
etsysOidPhy7K4297x04 = _EtsysOidPhy7K4297x04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 389)
)
if mibBuilder.loadTexts:
    etsysOidPhy7K4297x04.setStatus("current")
_EtsysOidPhy7KR4297x02_ObjectIdentity = ObjectIdentity
etsysOidPhy7KR4297x02 = _EtsysOidPhy7KR4297x02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 390)
)
if mibBuilder.loadTexts:
    etsysOidPhy7KR4297x02.setStatus("current")
_EtsysOidPhy7KR4297x04_ObjectIdentity = ObjectIdentity
etsysOidPhy7KR4297x04 = _EtsysOidPhy7KR4297x04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 391)
)
if mibBuilder.loadTexts:
    etsysOidPhy7KR4297x04.setStatus("current")
_EtsysOidPhy7S4280x19_ObjectIdentity = ObjectIdentity
etsysOidPhy7S4280x19 = _EtsysOidPhy7S4280x19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 392)
)
if mibBuilder.loadTexts:
    etsysOidPhy7S4280x19.setStatus("current")
_EtsysOidPhy2S4082x25_ObjectIdentity = ObjectIdentity
etsysOidPhy2S4082x25 = _EtsysOidPhy2S4082x25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 393)
)
if mibBuilder.loadTexts:
    etsysOidPhy2S4082x25.setStatus("current")
_EtsysOidPhy7SxNSNACGx01xNPS_ObjectIdentity = ObjectIdentity
etsysOidPhy7SxNSNACGx01xNPS = _EtsysOidPhy7SxNSNACGx01xNPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 394)
)
if mibBuilder.loadTexts:
    etsysOidPhy7SxNSNACGx01xNPS.setStatus("current")
_EtsysOidPhyMGBICxLC07_ObjectIdentity = ObjectIdentity
etsysOidPhyMGBICxLC07 = _EtsysOidPhyMGBICxLC07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 395)
)
if mibBuilder.loadTexts:
    etsysOidPhyMGBICxLC07.setStatus("current")
_EtsysOidPhy7SxNACGx01_ObjectIdentity = ObjectIdentity
etsysOidPhy7SxNACGx01 = _EtsysOidPhy7SxNACGx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 396)
)
if mibBuilder.loadTexts:
    etsysOidPhy7SxNACGx01.setStatus("current")
_EtsysOidPhy7SxC20N_ObjectIdentity = ObjectIdentity
etsysOidPhy7SxC20N = _EtsysOidPhy7SxC20N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 397)
)
if mibBuilder.loadTexts:
    etsysOidPhy7SxC20N.setStatus("current")
_EtsysOidPhy10GbExSRxSFPP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExSRxSFPP = _EtsysOidPhy10GbExSRxSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 398)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExSRxSFPP.setStatus("current")
_EtsysOidPhy10GbExLRxSFPP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExLRxSFPP = _EtsysOidPhy10GbExLRxSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 399)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExLRxSFPP.setStatus("current")
_EtsysOidPhy10GbExLRMxSFPP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExLRMxSFPP = _EtsysOidPhy10GbExLRMxSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 400)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExLRMxSFPP.setStatus("current")
_EtsysOidPhy10GbExC01xSFPP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExC01xSFPP = _EtsysOidPhy10GbExC01xSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 401)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExC01xSFPP.setStatus("current")
_EtsysOidPhy10GbExC03xSFPP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExC03xSFPP = _EtsysOidPhy10GbExC03xSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 402)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExC03xSFPP.setStatus("current")
_EtsysOidPhy10GbExC10xSFPP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExC10xSFPP = _EtsysOidPhy10GbExC10xSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 403)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExC10xSFPP.setStatus("current")
_EtsysOidPhy10GbExC20xSFPP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExC20xSFPP = _EtsysOidPhy10GbExC20xSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 404)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExC20xSFPP.setStatus("current")
_EtsysOidPhySFPPNoConnector_ObjectIdentity = ObjectIdentity
etsysOidPhySFPPNoConnector = _EtsysOidPhySFPPNoConnector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 405)
)
if mibBuilder.loadTexts:
    etsysOidPhySFPPNoConnector.setStatus("current")
_EtsysOidPhy10GbExLRMxXFP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GbExLRMxXFP = _EtsysOidPhy10GbExLRMxXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 406)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GbExLRMxXFP.setStatus("current")
_EtsysOidPhy7SxDNSAx01_ObjectIdentity = ObjectIdentity
etsysOidPhy7SxDNSAx01 = _EtsysOidPhy7SxDNSAx01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 407)
)
if mibBuilder.loadTexts:
    etsysOidPhy7SxDNSAx01.setStatus("current")
_EtsysOidPhyS3xCHASSIS_ObjectIdentity = ObjectIdentity
etsysOidPhyS3xCHASSIS = _EtsysOidPhyS3xCHASSIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 408)
)
if mibBuilder.loadTexts:
    etsysOidPhyS3xCHASSIS.setStatus("current")
_EtsysOidPhyS4xCHASSIS_ObjectIdentity = ObjectIdentity
etsysOidPhyS4xCHASSIS = _EtsysOidPhyS4xCHASSIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 409)
)
if mibBuilder.loadTexts:
    etsysOidPhyS4xCHASSIS.setStatus("current")
_EtsysOidPhyS8xCHASSIS_ObjectIdentity = ObjectIdentity
etsysOidPhyS8xCHASSIS = _EtsysOidPhyS8xCHASSIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 410)
)
if mibBuilder.loadTexts:
    etsysOidPhyS8xCHASSIS.setStatus("current")
_EtsysOidPhySxFAN_ObjectIdentity = ObjectIdentity
etsysOidPhySxFAN = _EtsysOidPhySxFAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 411)
)
if mibBuilder.loadTexts:
    etsysOidPhySxFAN.setStatus("current")
_EtsysOidPhySxACxPS_ObjectIdentity = ObjectIdentity
etsysOidPhySxACxPS = _EtsysOidPhySxACxPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 412)
)
if mibBuilder.loadTexts:
    etsysOidPhySxACxPS.setStatus("current")
_EtsysOidPhySxPOExPS_ObjectIdentity = ObjectIdentity
etsysOidPhySxPOExPS = _EtsysOidPhySxPOExPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 413)
)
if mibBuilder.loadTexts:
    etsysOidPhySxPOExPS.setStatus("current")
_EtsysOidPhySxPOEx4BAY_ObjectIdentity = ObjectIdentity
etsysOidPhySxPOEx4BAY = _EtsysOidPhySxPOEx4BAY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 414)
)
if mibBuilder.loadTexts:
    etsysOidPhySxPOEx4BAY.setStatus("current")
_EtsysOidPhySxPOEx8BAY_ObjectIdentity = ObjectIdentity
etsysOidPhySxPOEx8BAY = _EtsysOidPhySxPOEx8BAY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 415)
)
if mibBuilder.loadTexts:
    etsysOidPhySxPOEx8BAY.setStatus("current")
_EtsysOidPhySPowerSupplySlot_ObjectIdentity = ObjectIdentity
etsysOidPhySPowerSupplySlot = _EtsysOidPhySPowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 416)
)
if mibBuilder.loadTexts:
    etsysOidPhySPowerSupplySlot.setStatus("current")
_EtsysOidPhySFanTraySlot_ObjectIdentity = ObjectIdentity
etsysOidPhySFanTraySlot = _EtsysOidPhySFanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 417)
)
if mibBuilder.loadTexts:
    etsysOidPhySFanTraySlot.setStatus("current")
_EtsysOidPhySIOModuleSlot_ObjectIdentity = ObjectIdentity
etsysOidPhySIOModuleSlot = _EtsysOidPhySIOModuleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 418)
)
if mibBuilder.loadTexts:
    etsysOidPhySIOModuleSlot.setStatus("current")
_EtsysOidPhySFabricModuleSlot_ObjectIdentity = ObjectIdentity
etsysOidPhySFabricModuleSlot = _EtsysOidPhySFabricModuleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 419)
)
if mibBuilder.loadTexts:
    etsysOidPhySFabricModuleSlot.setStatus("current")
_EtsysOidPhySPoEPowerSupplySlot_ObjectIdentity = ObjectIdentity
etsysOidPhySPoEPowerSupplySlot = _EtsysOidPhySPoEPowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 420)
)
if mibBuilder.loadTexts:
    etsysOidPhySPoEPowerSupplySlot.setStatus("current")
_EtsysOidPhySK1208x0808xF6_ObjectIdentity = ObjectIdentity
etsysOidPhySK1208x0808xF6 = _EtsysOidPhySK1208x0808xF6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 421)
)
if mibBuilder.loadTexts:
    etsysOidPhySK1208x0808xF6.setStatus("current")
_EtsysOidPhyST4106x0348xF6_ObjectIdentity = ObjectIdentity
etsysOidPhyST4106x0348xF6 = _EtsysOidPhyST4106x0348xF6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 422)
)
if mibBuilder.loadTexts:
    etsysOidPhyST4106x0348xF6.setStatus("current")
_EtsysOidPhyST1206x0848xF6_ObjectIdentity = ObjectIdentity
etsysOidPhyST1206x0848xF6 = _EtsysOidPhyST1206x0848xF6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 423)
)
if mibBuilder.loadTexts:
    etsysOidPhyST1206x0848xF6.setStatus("current")
_EtsysOidPhySG1201x0848xF6_ObjectIdentity = ObjectIdentity
etsysOidPhySG1201x0848xF6 = _EtsysOidPhySG1201x0848xF6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 424)
)
if mibBuilder.loadTexts:
    etsysOidPhySG1201x0848xF6.setStatus("current")
_EtsysOidPhySK1008x0816_ObjectIdentity = ObjectIdentity
etsysOidPhySK1008x0816 = _EtsysOidPhySK1008x0816_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 425)
)
if mibBuilder.loadTexts:
    etsysOidPhySK1008x0816.setStatus("current")
_EtsysOidPhyST4106x0248_ObjectIdentity = ObjectIdentity
etsysOidPhyST4106x0248 = _EtsysOidPhyST4106x0248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 426)
)
if mibBuilder.loadTexts:
    etsysOidPhyST4106x0248.setStatus("current")
_EtsysOidPhyST4006x0272_ObjectIdentity = ObjectIdentity
etsysOidPhyST4006x0272 = _EtsysOidPhyST4006x0272_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 427)
)
if mibBuilder.loadTexts:
    etsysOidPhyST4006x0272.setStatus("current")
_EtsysOidPhyST1206x0848_ObjectIdentity = ObjectIdentity
etsysOidPhyST1206x0848 = _EtsysOidPhyST1206x0848_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 428)
)
if mibBuilder.loadTexts:
    etsysOidPhyST1206x0848.setStatus("current")
_EtsysOidPhySG4101x0248_ObjectIdentity = ObjectIdentity
etsysOidPhySG4101x0248 = _EtsysOidPhySG4101x0248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 429)
)
if mibBuilder.loadTexts:
    etsysOidPhySG4101x0248.setStatus("current")
_EtsysOidPhySG1201x0848_ObjectIdentity = ObjectIdentity
etsysOidPhySG1201x0848 = _EtsysOidPhySG1201x0848_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 430)
)
if mibBuilder.loadTexts:
    etsysOidPhySG1201x0848.setStatus("current")
_EtsysOidPhySOptModType1Slot_ObjectIdentity = ObjectIdentity
etsysOidPhySOptModType1Slot = _EtsysOidPhySOptModType1Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 431)
)
if mibBuilder.loadTexts:
    etsysOidPhySOptModType1Slot.setStatus("current")
_EtsysOidPhySOptModType2Slot_ObjectIdentity = ObjectIdentity
etsysOidPhySOptModType2Slot = _EtsysOidPhySOptModType2Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 432)
)
if mibBuilder.loadTexts:
    etsysOidPhySOptModType2Slot.setStatus("current")
_EtsysOidPhySOK1208x0104_ObjectIdentity = ObjectIdentity
etsysOidPhySOK1208x0104 = _EtsysOidPhySOK1208x0104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 433)
)
if mibBuilder.loadTexts:
    etsysOidPhySOK1208x0104.setStatus("current")
_EtsysOidPhySOK1208x0102_ObjectIdentity = ObjectIdentity
etsysOidPhySOK1208x0102 = _EtsysOidPhySOK1208x0102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 434)
)
if mibBuilder.loadTexts:
    etsysOidPhySOK1208x0102.setStatus("current")
_EtsysOidPhySOK1208x0204_ObjectIdentity = ObjectIdentity
etsysOidPhySOK1208x0204 = _EtsysOidPhySOK1208x0204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 435)
)
if mibBuilder.loadTexts:
    etsysOidPhySOK1208x0204.setStatus("current")
_EtsysOidPhySOG1201x0112_ObjectIdentity = ObjectIdentity
etsysOidPhySOG1201x0112 = _EtsysOidPhySOG1201x0112_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 436)
)
if mibBuilder.loadTexts:
    etsysOidPhySOG1201x0112.setStatus("current")
_EtsysOidPhyNN0100x0100xF2_ObjectIdentity = ObjectIdentity
etsysOidPhyNN0100x0100xF2 = _EtsysOidPhyNN0100x0100xF2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 437)
)
if mibBuilder.loadTexts:
    etsysOidPhyNN0100x0100xF2.setStatus("current")
_EtsysOidPhyNT4106x0248_ObjectIdentity = ObjectIdentity
etsysOidPhyNT4106x0248 = _EtsysOidPhyNT4106x0248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 438)
)
if mibBuilder.loadTexts:
    etsysOidPhyNT4106x0248.setStatus("current")
_EtsysOidPhyNT4006x0272_ObjectIdentity = ObjectIdentity
etsysOidPhyNT4006x0272 = _EtsysOidPhyNT4006x0272_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 439)
)
if mibBuilder.loadTexts:
    etsysOidPhyNT4006x0272.setStatus("current")
_EtsysOidPhyNT1006x0448_ObjectIdentity = ObjectIdentity
etsysOidPhyNT1006x0448 = _EtsysOidPhyNT1006x0448_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 440)
)
if mibBuilder.loadTexts:
    etsysOidPhyNT1006x0448.setStatus("current")
_EtsysOidPhyNK1008x0408_ObjectIdentity = ObjectIdentity
etsysOidPhyNK1008x0408 = _EtsysOidPhyNK1008x0408_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 441)
)
if mibBuilder.loadTexts:
    etsysOidPhyNK1008x0408.setStatus("current")
_EtsysOidPhyNG1001x0448_ObjectIdentity = ObjectIdentity
etsysOidPhyNG1001x0448 = _EtsysOidPhyNG1001x0448_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 442)
)
if mibBuilder.loadTexts:
    etsysOidPhyNG1001x0448.setStatus("current")
_EtsysOidPhyNG4101x0248_ObjectIdentity = ObjectIdentity
etsysOidPhyNG4101x0248 = _EtsysOidPhyNG4101x0248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 443)
)
if mibBuilder.loadTexts:
    etsysOidPhyNG4101x0248.setStatus("current")
_EtsysOidPhyNGNOptModSlot_ObjectIdentity = ObjectIdentity
etsysOidPhyNGNOptModSlot = _EtsysOidPhyNGNOptModSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 444)
)
if mibBuilder.loadTexts:
    etsysOidPhyNGNOptModSlot.setStatus("current")
_EtsysOidPhyNOK1208x0102_ObjectIdentity = ObjectIdentity
etsysOidPhyNOK1208x0102 = _EtsysOidPhyNOK1208x0102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 445)
)
if mibBuilder.loadTexts:
    etsysOidPhyNOK1208x0102.setStatus("current")
_EtsysOidPhyNOK1208x0104_ObjectIdentity = ObjectIdentity
etsysOidPhyNOK1208x0104 = _EtsysOidPhyNOK1208x0104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 446)
)
if mibBuilder.loadTexts:
    etsysOidPhyNOK1208x0104.setStatus("current")
_EtsysOidPhyNOG1201x0112_ObjectIdentity = ObjectIdentity
etsysOidPhyNOG1201x0112 = _EtsysOidPhyNOG1201x0112_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 447)
)
if mibBuilder.loadTexts:
    etsysOidPhyNOG1201x0112.setStatus("current")
_EtsysOidPhySSAxACxPSx600W_ObjectIdentity = ObjectIdentity
etsysOidPhySSAxACxPSx600W = _EtsysOidPhySSAxACxPSx600W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 448)
)
if mibBuilder.loadTexts:
    etsysOidPhySSAxACxPSx600W.setStatus("current")
_EtsysOidPhySSAxACxPSx1000W_ObjectIdentity = ObjectIdentity
etsysOidPhySSAxACxPSx1000W = _EtsysOidPhySSAxACxPSx1000W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 449)
)
if mibBuilder.loadTexts:
    etsysOidPhySSAxACxPSx1000W.setStatus("current")
_EtsysOidPhySSAPowerSupplySlot_ObjectIdentity = ObjectIdentity
etsysOidPhySSAPowerSupplySlot = _EtsysOidPhySSAPowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 450)
)
if mibBuilder.loadTexts:
    etsysOidPhySSAPowerSupplySlot.setStatus("current")
_EtsysOidPhy10GBxERxSFPP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GBxERxSFPP = _EtsysOidPhy10GBxERxSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 451)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GBxERxSFPP.setStatus("current")
_EtsysOidPhyUSBAPort_ObjectIdentity = ObjectIdentity
etsysOidPhyUSBAPort = _EtsysOidPhyUSBAPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 452)
)
if mibBuilder.loadTexts:
    etsysOidPhyUSBAPort.setStatus("current")
_EtsysOidPhyUSBMicroABPort_ObjectIdentity = ObjectIdentity
etsysOidPhyUSBMicroABPort = _EtsysOidPhyUSBMicroABPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 453)
)
if mibBuilder.loadTexts:
    etsysOidPhyUSBMicroABPort.setStatus("current")
_EtsysOidPhyS8Backplane_ObjectIdentity = ObjectIdentity
etsysOidPhyS8Backplane = _EtsysOidPhyS8Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 454)
)
if mibBuilder.loadTexts:
    etsysOidPhyS8Backplane.setStatus("current")
_EtsysOidPhyS4Backplane_ObjectIdentity = ObjectIdentity
etsysOidPhyS4Backplane = _EtsysOidPhyS4Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 455)
)
if mibBuilder.loadTexts:
    etsysOidPhyS4Backplane.setStatus("current")
_EtsysOidPhyS3Backplane_ObjectIdentity = ObjectIdentity
etsysOidPhyS3Backplane = _EtsysOidPhyS3Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 456)
)
if mibBuilder.loadTexts:
    etsysOidPhyS3Backplane.setStatus("current")
_EtsysOidPhyN5Backplane_ObjectIdentity = ObjectIdentity
etsysOidPhyN5Backplane = _EtsysOidPhyN5Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 457)
)
if mibBuilder.loadTexts:
    etsysOidPhyN5Backplane.setStatus("current")
_EtsysOidPhyN3Backplane_ObjectIdentity = ObjectIdentity
etsysOidPhyN3Backplane = _EtsysOidPhyN3Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 458)
)
if mibBuilder.loadTexts:
    etsysOidPhyN3Backplane.setStatus("current")
_EtsysOidPhyN1Backplane_ObjectIdentity = ObjectIdentity
etsysOidPhyN1Backplane = _EtsysOidPhyN1Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 459)
)
if mibBuilder.loadTexts:
    etsysOidPhyN1Backplane.setStatus("current")
_EtsysOidPhySOT1206x0112_ObjectIdentity = ObjectIdentity
etsysOidPhySOT1206x0112 = _EtsysOidPhySOT1206x0112_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 460)
)
if mibBuilder.loadTexts:
    etsysOidPhySOT1206x0112.setStatus("current")
_EtsysOidPhyNOT1206x0112_ObjectIdentity = ObjectIdentity
etsysOidPhyNOT1206x0112 = _EtsysOidPhyNOT1206x0112_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 461)
)
if mibBuilder.loadTexts:
    etsysOidPhyNOT1206x0112.setStatus("current")
_EtsysOidPhyConsolePortUsbMicroAB_ObjectIdentity = ObjectIdentity
etsysOidPhyConsolePortUsbMicroAB = _EtsysOidPhyConsolePortUsbMicroAB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 462)
)
if mibBuilder.loadTexts:
    etsysOidPhyConsolePortUsbMicroAB.setStatus("current")
_EtsysOidPhySSAxFAN_ObjectIdentity = ObjectIdentity
etsysOidPhySSAxFAN = _EtsysOidPhySSAxFAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 463)
)
if mibBuilder.loadTexts:
    etsysOidPhySSAxFAN.setStatus("current")
_EtsysOidPhyNSAxFAN_ObjectIdentity = ObjectIdentity
etsysOidPhyNSAxFAN = _EtsysOidPhyNSAxFAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 464)
)
if mibBuilder.loadTexts:
    etsysOidPhyNSAxFAN.setStatus("current")
_EtsysOidPhyNSAxACxPS_ObjectIdentity = ObjectIdentity
etsysOidPhyNSAxACxPS = _EtsysOidPhyNSAxACxPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 465)
)
if mibBuilder.loadTexts:
    etsysOidPhyNSAxACxPS.setStatus("current")
_EtsysOidPhyN1xFAN_ObjectIdentity = ObjectIdentity
etsysOidPhyN1xFAN = _EtsysOidPhyN1xFAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 466)
)
if mibBuilder.loadTexts:
    etsysOidPhyN1xFAN.setStatus("current")
_EtsysOidPhyN1xACxPS_ObjectIdentity = ObjectIdentity
etsysOidPhyN1xACxPS = _EtsysOidPhyN1xACxPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 467)
)
if mibBuilder.loadTexts:
    etsysOidPhyN1xACxPS.setStatus("current")
_EtsysOidPhy10GBxLWxSFPP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GBxLWxSFPP = _EtsysOidPhy10GBxLWxSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 468)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GBxLWxSFPP.setStatus("current")
_EtsysOidPhy10GBxLWxXFP_ObjectIdentity = ObjectIdentity
etsysOidPhy10GBxLWxXFP = _EtsysOidPhy10GBxLWxXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 469)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GBxLWxXFP.setStatus("current")
_EtsysOidPhy10GBxLWx20_ObjectIdentity = ObjectIdentity
etsysOidPhy10GBxLWx20 = _EtsysOidPhy10GBxLWx20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 470)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GBxLWx20.setStatus("current")
_EtsysOidPhy10GBxLWx10_ObjectIdentity = ObjectIdentity
etsysOidPhy10GBxLWx10 = _EtsysOidPhy10GBxLWx10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 471)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GBxLWx10.setStatus("current")
_EtsysOidPhy10GBxLWx05_ObjectIdentity = ObjectIdentity
etsysOidPhy10GBxLWx05 = _EtsysOidPhy10GBxLWx05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 472)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GBxLWx05.setStatus("current")
_EtsysOidPhy10GBxLWx03_ObjectIdentity = ObjectIdentity
etsysOidPhy10GBxLWx03 = _EtsysOidPhy10GBxLWx03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 473)
)
if mibBuilder.loadTexts:
    etsysOidPhy10GBxLWx03.setStatus("current")
_EtsysOidPhyMGBICxBX10xD_ObjectIdentity = ObjectIdentity
etsysOidPhyMGBICxBX10xD = _EtsysOidPhyMGBICxBX10xD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 474)
)
if mibBuilder.loadTexts:
    etsysOidPhyMGBICxBX10xD.setStatus("current")
_EtsysOidPhyMGBICxBX10xU_ObjectIdentity = ObjectIdentity
etsysOidPhyMGBICxBX10xU = _EtsysOidPhyMGBICxBX10xU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 475)
)
if mibBuilder.loadTexts:
    etsysOidPhyMGBICxBX10xU.setStatus("current")
_EtsysOidPhyIncompatiblePluggable_ObjectIdentity = ObjectIdentity
etsysOidPhyIncompatiblePluggable = _EtsysOidPhyIncompatiblePluggable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 476)
)
if mibBuilder.loadTexts:
    etsysOidPhyIncompatiblePluggable.setStatus("current")
_EtsysOidPhySK5208x0808xF6_ObjectIdentity = ObjectIdentity
etsysOidPhySK5208x0808xF6 = _EtsysOidPhySK5208x0808xF6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 477)
)
if mibBuilder.loadTexts:
    etsysOidPhySK5208x0808xF6.setStatus("current")
_EtsysOidPhyST5206x0848xF6_ObjectIdentity = ObjectIdentity
etsysOidPhyST5206x0848xF6 = _EtsysOidPhyST5206x0848xF6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 478)
)
if mibBuilder.loadTexts:
    etsysOidPhyST5206x0848xF6.setStatus("current")
_EtsysOidPhySG5201x0848xF6_ObjectIdentity = ObjectIdentity
etsysOidPhySG5201x0848xF6 = _EtsysOidPhySG5201x0848xF6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 479)
)
if mibBuilder.loadTexts:
    etsysOidPhySG5201x0848xF6.setStatus("current")
_EtsysOidPhyK6xCHASSIS_ObjectIdentity = ObjectIdentity
etsysOidPhyK6xCHASSIS = _EtsysOidPhyK6xCHASSIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 480)
)
if mibBuilder.loadTexts:
    etsysOidPhyK6xCHASSIS.setStatus("current")
_EtsysOidPhyK10xCHASSIS_ObjectIdentity = ObjectIdentity
etsysOidPhyK10xCHASSIS = _EtsysOidPhyK10xCHASSIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 481)
)
if mibBuilder.loadTexts:
    etsysOidPhyK10xCHASSIS.setStatus("current")
_EtsysOidPhyK6xFAN_ObjectIdentity = ObjectIdentity
etsysOidPhyK6xFAN = _EtsysOidPhyK6xFAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 482)
)
if mibBuilder.loadTexts:
    etsysOidPhyK6xFAN.setStatus("current")
_EtsysOidPhyK10xFAN_ObjectIdentity = ObjectIdentity
etsysOidPhyK10xFAN = _EtsysOidPhyK10xFAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 483)
)
if mibBuilder.loadTexts:
    etsysOidPhyK10xFAN.setStatus("current")
_EtsysOidPhyKxACxPSx1440W_ObjectIdentity = ObjectIdentity
etsysOidPhyKxACxPSx1440W = _EtsysOidPhyKxACxPSx1440W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 484)
)
if mibBuilder.loadTexts:
    etsysOidPhyKxACxPSx1440W.setStatus("current")
_EtsysOidPhyKxPOExExtConn_ObjectIdentity = ObjectIdentity
etsysOidPhyKxPOExExtConn = _EtsysOidPhyKxPOExExtConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 485)
)
if mibBuilder.loadTexts:
    etsysOidPhyKxPOExExtConn.setStatus("current")
_EtsysOidPhyKPowerSupplySlot_ObjectIdentity = ObjectIdentity
etsysOidPhyKPowerSupplySlot = _EtsysOidPhyKPowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 486)
)
if mibBuilder.loadTexts:
    etsysOidPhyKPowerSupplySlot.setStatus("current")
_EtsysOidPhyK6FanTraySlot_ObjectIdentity = ObjectIdentity
etsysOidPhyK6FanTraySlot = _EtsysOidPhyK6FanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 487)
)
if mibBuilder.loadTexts:
    etsysOidPhyK6FanTraySlot.setStatus("current")
_EtsysOidPhyK10FanTraySlot_ObjectIdentity = ObjectIdentity
etsysOidPhyK10FanTraySlot = _EtsysOidPhyK10FanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 488)
)
if mibBuilder.loadTexts:
    etsysOidPhyK10FanTraySlot.setStatus("current")
_EtsysOidPhyKLineCardSlot_ObjectIdentity = ObjectIdentity
etsysOidPhyKLineCardSlot = _EtsysOidPhyKLineCardSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 489)
)
if mibBuilder.loadTexts:
    etsysOidPhyKLineCardSlot.setStatus("current")
_EtsysOidPhyKFabricModuleSlot_ObjectIdentity = ObjectIdentity
etsysOidPhyKFabricModuleSlot = _EtsysOidPhyKFabricModuleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 490)
)
if mibBuilder.loadTexts:
    etsysOidPhyKFabricModuleSlot.setStatus("current")
_EtsysOidPhyKK2008x0204xF1_ObjectIdentity = ObjectIdentity
etsysOidPhyKK2008x0204xF1 = _EtsysOidPhyKK2008x0204xF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 491)
)
if mibBuilder.loadTexts:
    etsysOidPhyKK2008x0204xF1.setStatus("current")
_EtsysOidPhyKK2008x0204xF2_ObjectIdentity = ObjectIdentity
etsysOidPhyKK2008x0204xF2 = _EtsysOidPhyKK2008x0204xF2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 492)
)
if mibBuilder.loadTexts:
    etsysOidPhyKK2008x0204xF2.setStatus("current")
_EtsysOidPhyKK2000x0000xF1_ObjectIdentity = ObjectIdentity
etsysOidPhyKK2000x0000xF1 = _EtsysOidPhyKK2000x0000xF1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 493)
)
if mibBuilder.loadTexts:
    etsysOidPhyKK2000x0000xF1.setStatus("current")
_EtsysOidPhyKK2000x0000xF2_ObjectIdentity = ObjectIdentity
etsysOidPhyKK2000x0000xF2 = _EtsysOidPhyKK2000x0000xF2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 494)
)
if mibBuilder.loadTexts:
    etsysOidPhyKK2000x0000xF2.setStatus("current")
_EtsysOidPhyKT2006x0224_ObjectIdentity = ObjectIdentity
etsysOidPhyKT2006x0224 = _EtsysOidPhyKT2006x0224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 495)
)
if mibBuilder.loadTexts:
    etsysOidPhyKT2006x0224.setStatus("current")
_EtsysOidPhyKG2001x0224_ObjectIdentity = ObjectIdentity
etsysOidPhyKG2001x0224 = _EtsysOidPhyKG2001x0224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 496)
)
if mibBuilder.loadTexts:
    etsysOidPhyKG2001x0224.setStatus("current")
_EtsysOidPhyKK2008x0204_ObjectIdentity = ObjectIdentity
etsysOidPhyKK2008x0204 = _EtsysOidPhyKK2008x0204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 497)
)
if mibBuilder.loadTexts:
    etsysOidPhyKK2008x0204.setStatus("current")
_EtsysOidPhyK6Backplane_ObjectIdentity = ObjectIdentity
etsysOidPhyK6Backplane = _EtsysOidPhyK6Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 498)
)
if mibBuilder.loadTexts:
    etsysOidPhyK6Backplane.setStatus("current")
_EtsysOidPhyK10Backplane_ObjectIdentity = ObjectIdentity
etsysOidPhyK10Backplane = _EtsysOidPhyK10Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 499)
)
if mibBuilder.loadTexts:
    etsysOidPhyK10Backplane.setStatus("current")
_EtsysOidPhySxDCxPS_ObjectIdentity = ObjectIdentity
etsysOidPhySxDCxPS = _EtsysOidPhySxDCxPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 500)
)
if mibBuilder.loadTexts:
    etsysOidPhySxDCxPS.setStatus("current")
_EtsysOidPhyMGBICxBX40xD_ObjectIdentity = ObjectIdentity
etsysOidPhyMGBICxBX40xD = _EtsysOidPhyMGBICxBX40xD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 501)
)
if mibBuilder.loadTexts:
    etsysOidPhyMGBICxBX40xD.setStatus("current")
_EtsysOidPhyMGBICxBX40xU_ObjectIdentity = ObjectIdentity
etsysOidPhyMGBICxBX40xU = _EtsysOidPhyMGBICxBX40xU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 502)
)
if mibBuilder.loadTexts:
    etsysOidPhyMGBICxBX40xU.setStatus("current")
_EtsysOidPhyMGBICxBX120xD_ObjectIdentity = ObjectIdentity
etsysOidPhyMGBICxBX120xD = _EtsysOidPhyMGBICxBX120xD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 503)
)
if mibBuilder.loadTexts:
    etsysOidPhyMGBICxBX120xD.setStatus("current")
_EtsysOidPhyMGBICxBX120xU_ObjectIdentity = ObjectIdentity
etsysOidPhyMGBICxBX120xU = _EtsysOidPhyMGBICxBX120xU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 504)
)
if mibBuilder.loadTexts:
    etsysOidPhyMGBICxBX120xU.setStatus("current")
_EtsysOidPhyS6xCHASSIS_ObjectIdentity = ObjectIdentity
etsysOidPhyS6xCHASSIS = _EtsysOidPhyS6xCHASSIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 507)
)
if mibBuilder.loadTexts:
    etsysOidPhyS6xCHASSIS.setStatus("current")
_EtsysOidPhyS6Backplane_ObjectIdentity = ObjectIdentity
etsysOidPhyS6Backplane = _EtsysOidPhyS6Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 2, 508)
)
if mibBuilder.loadTexts:
    etsysOidPhyS6Backplane.setStatus("current")
_EtsysOidOther_ObjectIdentity = ObjectIdentity
etsysOidOther = _EtsysOidOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3)
)
_EtsysOidIEEE8023adLagInterface_ObjectIdentity = ObjectIdentity
etsysOidIEEE8023adLagInterface = _EtsysOidIEEE8023adLagInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 1)
)
if mibBuilder.loadTexts:
    etsysOidIEEE8023adLagInterface.setStatus("current")
_EtsysOidOtherLicenseKeyId_ObjectIdentity = ObjectIdentity
etsysOidOtherLicenseKeyId = _EtsysOidOtherLicenseKeyId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-OIDS-MIB",
    **{"enterasysOidsMib": enterasysOidsMib,
       "etsysOidDevice": etsysOidDevice,
       "etsysOidDevEmpty": etsysOidDevEmpty,
       "etsysOidDev6G306x06": etsysOidDev6G306x06,
       "etsysOidDev6H302x48": etsysOidDev6H302x48,
       "etsysOidDev6H303x48": etsysOidDev6H303x48,
       "etsysOidDev6H352x25": etsysOidDev6H352x25,
       "etsysOidDev6H308x24": etsysOidDev6H308x24,
       "etsysOidDev6E308x24": etsysOidDev6E308x24,
       "etsysOidDev6C107": etsysOidDev6C107,
       "etsysOidDevEls1000x8SX": etsysOidDevEls1000x8SX,
       "etsysOidDevEls100x48TX2M": etsysOidDevEls100x48TX2M,
       "etsysOidDevEls100x24TX2M": etsysOidDevEls100x24TX2M,
       "etsysOidDevDepricated001": etsysOidDevDepricated001,
       "etsysOidDev6H308x48": etsysOidDev6H308x48,
       "etsysOidDev6E308x48": etsysOidDev6E308x48,
       "etsysOidDev6H202x48": etsysOidDev6H202x48,
       "etsysOidDev9E531x24": etsysOidDev9E531x24,
       "etsysOidDevVG4x3DES": etsysOidDevVG4x3DES,
       "etsysOidDev6H002x48": etsysOidDev6H002x48,
       "etsysOidDev6H003x48": etsysOidDev6H003x48,
       "etsysOidDev6G066x06": etsysOidDev6G066x06,
       "etsysOidDev6G063x06": etsysOidDev6G063x06,
       "etsysOidDevVG6": etsysOidDevVG6,
       "etsysOidDevER16": etsysOidDevER16,
       "etsysOidDev5SSRMx02": etsysOidDev5SSRMx02,
       "etsysOidDevVHx8TX1UM": etsysOidDevVHx8TX1UM,
       "etsysOidDevVHx2402xL3": etsysOidDevVHx2402xL3,
       "etsysOidDevVHx8GxL3": etsysOidDevVHx8GxL3,
       "etsysOidDev5H162x50": etsysOidDev5H162x50,
       "etsysOidDev5H163x50": etsysOidDev5H163x50,
       "etsysOidDevRBTR2xA": etsysOidDevRBTR2xA,
       "etsysOidDevVHx8TX1MF": etsysOidDevVHx8TX1MF,
       "etsysOidDevXPx1000": etsysOidDevXPx1000,
       "etsysOidDevANGx2000": etsysOidDevANGx2000,
       "etsysOidDev1H152x50": etsysOidDev1H152x50,
       "etsysOidDev1G154x09": etsysOidDev1G154x09,
       "etsysOidDev1G276x13": etsysOidDev1G276x13,
       "etsysOidDevVHxSMGMTxL3": etsysOidDevVHxSMGMTxL3,
       "etsysOidDevANGx1102": etsysOidDevANGx1102,
       "etsysOidDevANGx1105": etsysOidDevANGx1105,
       "etsysOidDevANGx3000": etsysOidDevANGx3000,
       "etsysOidDevANGx7000": etsysOidDevANGx7000,
       "etsysOidDevXPx2400": etsysOidDevXPx2400,
       "etsysOidDevVHx8G02S": etsysOidDevVHx8G02S,
       "etsysOidDev6G302x06": etsysOidDev6G302x06,
       "etsysOidDevXSRx1850": etsysOidDevXSRx1850,
       "etsysOidDevVHx2402S2": etsysOidDevVHx2402S2,
       "etsysOidDevVHx2202GT": etsysOidDevVHx2202GT,
       "etsysOidDevC5M200": etsysOidDevC5M200,
       "etsysOidDevC1H124x48": etsysOidDevC1H124x48,
       "etsysOidDevC2M200": etsysOidDevC2M200,
       "etsysOidDevMatrixE7": etsysOidDevMatrixE7,
       "etsysOidDevMatrixN7": etsysOidDevMatrixN7,
       "etsysOidDevMatrixN3": etsysOidDevMatrixN3,
       "etsysOidDevXSRx1100": etsysOidDevXSRx1100,
       "etsysOidDevXSRx3020": etsysOidDevXSRx3020,
       "etsysOidDevXSRx3150": etsysOidDevXSRx3150,
       "etsysOidDevXSRx3250": etsysOidDevXSRx3250,
       "etsysOidDevXSRx4100": etsysOidDevXSRx4100,
       "etsysOidDev1H582x25": etsysOidDev1H582x25,
       "etsysOidDev1G587x09": etsysOidDev1G587x09,
       "etsysOidDevC1G124x24": etsysOidDevC1G124x24,
       "etsysOidDevV2H124x24": etsysOidDevV2H124x24,
       "etsysOidDevRBTR3xA": etsysOidDevRBTR3xA,
       "etsysOidDevRBTR4xA": etsysOidDevRBTR4xA,
       "etsysOidDevMatrixE7Gold": etsysOidDevMatrixE7Gold,
       "etsysOidDevMatrixN7Gold": etsysOidDevMatrixN7Gold,
       "etsysOidDevMatrixN3Gold": etsysOidDevMatrixN3Gold,
       "etsysOidDevV2H124xPOE": etsysOidDevV2H124xPOE,
       "etsysOidDevDFEGoldRouter": etsysOidDevDFEGoldRouter,
       "etsysOidDevDFEPlatinumRouter": etsysOidDevDFEPlatinumRouter,
       "etsysOidDevDragonIdsAppliance": etsysOidDevDragonIdsAppliance,
       "etsysOidDevXSRx1205": etsysOidDevXSRx1205,
       "etsysOidDevXSRx1220": etsysOidDevXSRx1220,
       "etsysOidDevXSRx1225": etsysOidDevXSRx1225,
       "etsysOidDevXSRx1230": etsysOidDevXSRx1230,
       "etsysOidDevXSRx1235": etsysOidDevXSRx1235,
       "etsysOidDev2G4072x52": etsysOidDev2G4072x52,
       "etsysOidDevMatrixN5PoEGold": etsysOidDevMatrixN5PoEGold,
       "etsysOidDevMatrixN5PoEPlatinum": etsysOidDevMatrixN5PoEPlatinum,
       "etsysOidDevMatrixX4": etsysOidDevMatrixX4,
       "etsysOidDevMatrixX8": etsysOidDevMatrixX8,
       "etsysOidDevMatrixX16": etsysOidDevMatrixX16,
       "etsysOidDevMatrixN1": etsysOidDevMatrixN1,
       "etsysOidDevMatrixN1Gold": etsysOidDevMatrixN1Gold,
       "etsysOidDevRBTSAxAA": etsysOidDevRBTSAxAA,
       "etsysOidDevRBTSAxAB": etsysOidDevRBTSAxAB,
       "etsysOidDevA2H124x24": etsysOidDevA2H124x24,
       "etsysOidDevA2H124x24P": etsysOidDevA2H124x24P,
       "etsysOidDevA2H124x48": etsysOidDevA2H124x48,
       "etsysOidDevA2H124x48P": etsysOidDevA2H124x48P,
       "etsysOidDevA2H124x24FX": etsysOidDevA2H124x24FX,
       "etsysOidDevRBT4102": etsysOidDevRBT4102,
       "etsysOidDevNSTAGxGE250xTX": etsysOidDevNSTAGxGE250xTX,
       "etsysOidDevNSTAGxGE500xTX": etsysOidDevNSTAGxGE500xTX,
       "etsysOidDevA2H254x16": etsysOidDevA2H254x16,
       "etsysOidDevC3G124x24": etsysOidDevC3G124x24,
       "etsysOidDevC3G124x24P": etsysOidDevC3G124x24P,
       "etsysOidDevC3G124x48": etsysOidDevC3G124x48,
       "etsysOidDevC3G124x48P": etsysOidDevC3G124x48P,
       "etsysOidDevB3G124x24": etsysOidDevB3G124x24,
       "etsysOidDevB3G124x24P": etsysOidDevB3G124x24P,
       "etsysOidDevB3G124x48": etsysOidDevB3G124x48,
       "etsysOidDevB3G124x48P": etsysOidDevB3G124x48P,
       "etsysOidDevI3H252x02": etsysOidDevI3H252x02,
       "etsysOidDevSNSxTAGxLPA": etsysOidDevSNSxTAGxLPA,
       "etsysOidDevSNSxTAGxHPA": etsysOidDevSNSxTAGxHPA,
       "etsysOidDevSNSxTAGxBASE": etsysOidDevSNSxTAGxBASE,
       "etsysOidDev7SxNSTAGx01": etsysOidDev7SxNSTAGx01,
       "etsysOidDevSNSxPCCxWBA": etsysOidDevSNSxPCCxWBA,
       "etsysOidDevA2H123x24": etsysOidDevA2H123x24,
       "etsysOidDevB3H124x24FX": etsysOidDevB3H124x24FX,
       "etsysOidDevC3H124x24FX": etsysOidDevC3H124x24FX,
       "etsysOidDevC3K122x24": etsysOidDevC3K122x24,
       "etsysOidDevC3K172x24": etsysOidDevC3K172x24,
       "etsysOidDevC3Kx2XFP": etsysOidDevC3Kx2XFP,
       "etsysOidDevSNSxNSSxA": etsysOidDevSNSxNSSxA,
       "etsysOidDevG3G124x24": etsysOidDevG3G124x24,
       "etsysOidDevG3G170x24": etsysOidDevG3G170x24,
       "etsysOidDevD2G124x12": etsysOidDevD2G124x12,
       "etsysOidDevD2G124x12P": etsysOidDevD2G124x12P,
       "etsysOidDevRBTx8500": etsysOidDevRBTx8500,
       "etsysOidDevMatrixN1NAC": etsysOidDevMatrixN1NAC,
       "etsysOidDev7SxNSNACGx01NPS": etsysOidDev7SxNSNACGx01NPS,
       "etsysOidDevG3G124x24P": etsysOidDevG3G124x24P,
       "etsysOidDevC3K122x24P": etsysOidDevC3K122x24P,
       "etsysOidDevNACxAx2K": etsysOidDevNACxAx2K,
       "etsysOidDevNACxAx3K": etsysOidDevNACxAx3K,
       "etsysOidDevSSAxT4068x0252": etsysOidDevSSAxT4068x0252,
       "etsysOidDevSSAxT1068x0652": etsysOidDevSSAxT1068x0652,
       "etsysOidDevSSAxG1018x0652": etsysOidDevSSAxG1018x0652,
       "etsysOidDevS3": etsysOidDevS3,
       "etsysOidDevS4": etsysOidDevS4,
       "etsysOidDevS8": etsysOidDevS8,
       "etsysOidDevB5G124x24": etsysOidDevB5G124x24,
       "etsysOidDevB5G124x24P2": etsysOidDevB5G124x24P2,
       "etsysOidDevB5G124x48": etsysOidDevB5G124x48,
       "etsysOidDevB5G124x48P2": etsysOidDevB5G124x48P2,
       "etsysOidDevB5K125x24": etsysOidDevB5K125x24,
       "etsysOidDevB5K125x24P2": etsysOidDevB5K125x24P2,
       "etsysOidDevB5K125x48": etsysOidDevB5K125x48,
       "etsysOidDevB5K125x48P2": etsysOidDevB5K125x48P2,
       "etsysOidDevC5G124x24": etsysOidDevC5G124x24,
       "etsysOidDevC5G124x24P2": etsysOidDevC5G124x24P2,
       "etsysOidDevC5G124x48": etsysOidDevC5G124x48,
       "etsysOidDevC5G124x48P2": etsysOidDevC5G124x48P2,
       "etsysOidDevC5K125x24": etsysOidDevC5K125x24,
       "etsysOidDevC5K125x24P2": etsysOidDevC5K125x24P2,
       "etsysOidDevC5K125x48": etsysOidDevC5K125x48,
       "etsysOidDevC5K125x48P2": etsysOidDevC5K125x48P2,
       "etsysOidDevC5K175x24": etsysOidDevC5K175x24,
       "etsysOidDevNACxAx10": etsysOidDevNACxAx10,
       "etsysOidDevNACxAx20": etsysOidDevNACxAx20,
       "etsysOidDevNACxV": etsysOidDevNACxV,
       "etsysOidDevA4H124x24TX": etsysOidDevA4H124x24TX,
       "etsysOidDevA4H124x24FX": etsysOidDevA4H124x24FX,
       "etsysOidDevA4H124x8F8T": etsysOidDevA4H124x8F8T,
       "etsysOidDevA4H124x24": etsysOidDevA4H124x24,
       "etsysOidDevA4H124x24P": etsysOidDevA4H124x24P,
       "etsysOidDevA4H124x48": etsysOidDevA4H124x48,
       "etsysOidDevA4H124x48P": etsysOidDevA4H124x48P,
       "etsysOidDevA4H254x8F8T": etsysOidDevA4H254x8F8T,
       "etsysOidDevK6": etsysOidDevK6,
       "etsysOidDevK10": etsysOidDevK10,
       "etsysOidDevS6": etsysOidDevS6,
       "etsysOidDevSSAxT5068x0652": etsysOidDevSSAxT5068x0652,
       "etsysOidDevSSAxG5018x0652": etsysOidDevSSAxG5018x0652,
       "etsysOidPhy": etsysOidPhy,
       "etsysOidPhyEmpty": etsysOidPhyEmpty,
       "etsysOidPhyMGBICxMT01": etsysOidPhyMGBICxMT01,
       "etsysOidPhyMGBICxMT09": etsysOidPhyMGBICxMT09,
       "etsysOidPhyMGBICxLC01": etsysOidPhyMGBICxLC01,
       "etsysOidPhyMGBICxLC09": etsysOidPhyMGBICxLC09,
       "etsysOidPhyFrtPnlFastEthRJ45": etsysOidPhyFrtPnlFastEthRJ45,
       "etsysOidPhyFrtPnlFastEthRJ21": etsysOidPhyFrtPnlFastEthRJ21,
       "etsysOidPhyFrtPnlGigEthRJ45": etsysOidPhyFrtPnlGigEthRJ45,
       "etsysOidPhyBackplaneFTM1": etsysOidPhyBackplaneFTM1,
       "etsysOidPhy7H4203x72": etsysOidPhy7H4203x72,
       "etsysOidPhy7H4273x52": etsysOidPhy7H4273x52,
       "etsysOidPhy7H4303x48": etsysOidPhy7H4303x48,
       "etsysOidPhy7G4270x12": etsysOidPhy7G4270x12,
       "etsysOidPhy7G4202x12": etsysOidPhy7G4202x12,
       "etsysOidPhy7G4370x08": etsysOidPhy7G4370x08,
       "etsysOidPhy7K420Xx01": etsysOidPhy7K420Xx01,
       "etsysOidPhy6C207x1": etsysOidPhy6C207x1,
       "etsysOidPhy6C207x2": etsysOidPhy6C207x2,
       "etsysOidPhy6C407": etsysOidPhy6C407,
       "etsysOidPhy5C205x3": etsysOidPhy5C205x3,
       "etsysOidPhy5C205x2": etsysOidPhy5C205x2,
       "etsysOidPhy5C405": etsysOidPhy5C405,
       "etsysOidPhy6C107": etsysOidPhy6C107,
       "etsysOidPhy5C105": etsysOidPhy5C105,
       "etsysOidPhy10GbExSR": etsysOidPhy10GbExSR,
       "etsysOidPhy10GbExLR": etsysOidPhy10GbExLR,
       "etsysOidPhy10GbExER": etsysOidPhy10GbExER,
       "etsysOidPhy10GbExSW": etsysOidPhy10GbExSW,
       "etsysOidPhy10GbExLW": etsysOidPhy10GbExLW,
       "etsysOidPhy10GbExEW": etsysOidPhy10GbExEW,
       "etsysOidPhy10GbExLX4": etsysOidPhy10GbExLX4,
       "etsysOidPhy1Hx16TX": etsysOidPhy1Hx16TX,
       "etsysOidPhy1Gx2GBIC": etsysOidPhy1Gx2GBIC,
       "etsysOidPhy1Gx2MGBIC": etsysOidPhy1Gx2MGBIC,
       "etsysOidPhy1Hx2TX": etsysOidPhy1Hx2TX,
       "etsysOidPhyZPIMxZ1": etsysOidPhyZPIMxZ1,
       "etsysOidPhyER16xCS": etsysOidPhyER16xCS,
       "etsysOidPhyXPx16": etsysOidPhyXPx16,
       "etsysOidPhyXPx8": etsysOidPhyXPx8,
       "etsysOidPhyXPx2xB128": etsysOidPhyXPx2xB128,
       "etsysOidPhyXPx2xGSX": etsysOidPhyXPx2xGSX,
       "etsysOidPhyER16x04": etsysOidPhyER16x04,
       "etsysOidPhyER16x08": etsysOidPhyER16x08,
       "etsysOidPhyER16xSXx08": etsysOidPhyER16xSXx08,
       "etsysOidPhyER16xTXx24": etsysOidPhyER16xTXx24,
       "etsysOidPhyER16xTXx32": etsysOidPhyER16xTXx32,
       "etsysOidPhyER16xAC": etsysOidPhyER16xAC,
       "etsysOidPhyER16xFN": etsysOidPhyER16xFN,
       "etsysOidPhyER16xCK": etsysOidPhyER16xCK,
       "etsysOidPhyER16xSF": etsysOidPhyER16xSF,
       "etsysOidPhyER16xCM3": etsysOidPhyER16xCM3,
       "etsysOidPhyER16xCM4": etsysOidPhyER16xCM4,
       "etsysOidPhySSRxPSx16": etsysOidPhySSRxPSx16,
       "etsysOidPhySSRxPSx16xDC": etsysOidPhySSRxPSx16xDC,
       "etsysOidPhySSRxSFx16": etsysOidPhySSRxSFx16,
       "etsysOidPhySSRxFANx16": etsysOidPhySSRxFANx16,
       "etsysOidPhySSRxPSx8": etsysOidPhySSRxPSx8,
       "etsysOidPhySSRxPSx8xDC": etsysOidPhySSRxPSx8xDC,
       "etsysOidPhySSRxFANx8": etsysOidPhySSRxFANx8,
       "etsysOidPhyXPxPCMCIA": etsysOidPhyXPxPCMCIA,
       "etsysOidPhyXPxPCMCIAx16LN": etsysOidPhyXPxPCMCIAx16LN,
       "etsysOidPhyXPxPCMCIAx16AT": etsysOidPhyXPxPCMCIAx16AT,
       "etsysOidPhyXPxPCMCIAx32AT": etsysOidPhyXPxPCMCIAx32AT,
       "etsysOidPhySSRxCM2": etsysOidPhySSRxCM2,
       "etsysOidPhySSRxCM3": etsysOidPhySSRxCM3,
       "etsysOidPhySSRxCM4": etsysOidPhySSRxCM4,
       "etsysOidPhy10100T": etsysOidPhy10100T,
       "etsysOidPhySSRxARE": etsysOidPhySSRxARE,
       "etsysOidPhySSRxATM29x02": etsysOidPhySSRxATM29x02,
       "etsysOidPhySSRxGTX32x02": etsysOidPhySSRxGTX32x02,
       "etsysOidPhySSRxGSX11x02": etsysOidPhySSRxGSX11x02,
       "etsysOidPhySSRxGSX21x02": etsysOidPhySSRxGSX21x02,
       "etsysOidPhySSRxGSX21x02xAA": etsysOidPhySSRxGSX21x02xAA,
       "etsysOidPhySSRxGSX31x02": etsysOidPhySSRxGSX31x02,
       "etsysOidPhySSRxGLX19x02": etsysOidPhySSRxGLX19x02,
       "etsysOidPhySSRxGLX29x02": etsysOidPhySSRxGLX29x02,
       "etsysOidPhySSRxGLX29x02xAA": etsysOidPhySSRxGLX29x02xAA,
       "etsysOidPhySSRxGLX39x02": etsysOidPhySSRxGLX39x02,
       "etsysOidPhySSRxGLH39x02": etsysOidPhySSRxGLH39x02,
       "etsysOidPhySSRxGLX70x01": etsysOidPhySSRxGLX70x01,
       "etsysOidPhySSRxGLX70x01xAA": etsysOidPhySSRxGLX70x01xAA,
       "etsysOidPhySSRxHTX12x08": etsysOidPhySSRxHTX12x08,
       "etsysOidPhySSRxHTX12x08xAA": etsysOidPhySSRxHTX12x08xAA,
       "etsysOidPhySSRxHTX22x08": etsysOidPhySSRxHTX22x08,
       "etsysOidPhySSRxHTX22x08xAA": etsysOidPhySSRxHTX22x08xAA,
       "etsysOidPhySSRxHTX32x16": etsysOidPhySSRxHTX32x16,
       "etsysOidPhySSRxHFX11x08": etsysOidPhySSRxHFX11x08,
       "etsysOidPhySSRxHFX21x08": etsysOidPhySSRxHFX21x08,
       "etsysOidPhySSRxHFX21x08xAA": etsysOidPhySSRxHFX21x08xAA,
       "etsysOidPhySSRxHFX29x08": etsysOidPhySSRxHFX29x08,
       "etsysOidPhySSRxHFX29x08xAA": etsysOidPhySSRxHFX29x08xAA,
       "etsysOidPhySSRxFDDIx02": etsysOidPhySSRxFDDIx02,
       "etsysOidPhySSRxHSSIx02": etsysOidPhySSRxHSSIx02,
       "etsysOidPhySSRxHSSIx02xAA": etsysOidPhySSRxHSSIx02xAA,
       "etsysOidPhySSRxSERCx04": etsysOidPhySSRxSERCx04,
       "etsysOidPhySSRxSERCx04xAA": etsysOidPhySSRxSERCx04xAA,
       "etsysOidPhySSRxSERCEx04": etsysOidPhySSRxSERCEx04,
       "etsysOidPhySSRxSERCEx04xAA": etsysOidPhySSRxSERCEx04xAA,
       "etsysOidPhySSRxPOS21x04": etsysOidPhySSRxPOS21x04,
       "etsysOidPhySSRxPOS29x04": etsysOidPhySSRxPOS29x04,
       "etsysOidPhySSRxPOS31x02": etsysOidPhySSRxPOS31x02,
       "etsysOidPhySSRxPOS39x02": etsysOidPhySSRxPOS39x02,
       "etsysOidPhyXP2IntCM": etsysOidPhyXP2IntCM,
       "etsysOidPhyXP2IntPs": etsysOidPhyXP2IntPs,
       "etsysOidPhyXP2IntTX08": etsysOidPhyXP2IntTX08,
       "etsysOidPhyXPx2xTX": etsysOidPhyXPx2xTX,
       "etsysOidPhyXPx2xTXxAA": etsysOidPhyXPx2xTXxAA,
       "etsysOidPhyXPx2xLX": etsysOidPhyXPx2xLX,
       "etsysOidPhyXPx2xLXxAA": etsysOidPhyXPx2xLXxAA,
       "etsysOidPhyXPx2xLX70": etsysOidPhyXPx2xLX70,
       "etsysOidPhyXPx2xLX70xAA": etsysOidPhyXPx2xLX70xAA,
       "etsysOidPhyXPx2xSX": etsysOidPhyXPx2xSX,
       "etsysOidPhyXPx2xSXxAA": etsysOidPhyXPx2xSXxAA,
       "etsysOidPhyXPx2xFX": etsysOidPhyXPx2xFX,
       "etsysOidPhyXPx2xFXxAA": etsysOidPhyXPx2xFXxAA,
       "etsysOidPhyXPx2xHSSIxAA": etsysOidPhyXPx2xHSSIxAA,
       "etsysOidPhyXPx2xSER": etsysOidPhyXPx2xSER,
       "etsysOidPhyXPx2xSERxAA": etsysOidPhyXPx2xSERxAA,
       "etsysOidPhyXPx2xSERC": etsysOidPhyXPx2xSERC,
       "etsysOidPhyXPx2xSERCxAA": etsysOidPhyXPx2xSERCxAA,
       "etsysOidPhyXPx2xSERCE": etsysOidPhyXPx2xSERCE,
       "etsysOidPhyXPx2xSERCExAA": etsysOidPhyXPx2xSERCExAA,
       "etsysOidPhyXPxAPHYx21": etsysOidPhyXPxAPHYx21,
       "etsysOidPhyXPxAPHYx22": etsysOidPhyXPxAPHYx22,
       "etsysOidPhyXPxAPHYx29IR": etsysOidPhyXPxAPHYx29IR,
       "etsysOidPhyXPxAPHYx67": etsysOidPhyXPxAPHYx67,
       "etsysOidPhyXPxAPHYx77": etsysOidPhyXPxAPHYx77,
       "etsysOidPhyXPxAPHYx82": etsysOidPhyXPxAPHYx82,
       "etsysOidPhyXPxAPHYx92": etsysOidPhyXPxAPHYx92,
       "etsysOidPhyXPxFPHYx01": etsysOidPhyXPxFPHYx01,
       "etsysOidPhyXPxFPHYx02": etsysOidPhyXPxFPHYx02,
       "etsysOidPhyXPxFPHYx09": etsysOidPhyXPxFPHYx09,
       "etsysOidPhyHssiPort": etsysOidPhyHssiPort,
       "etsysOidPhySerialConnection": etsysOidPhySerialConnection,
       "etsysOidPhySerialEia530AConnection": etsysOidPhySerialEia530AConnection,
       "etsysOidPhySerialEia530Connection": etsysOidPhySerialEia530Connection,
       "etsysOidPhySerialV35Connection": etsysOidPhySerialV35Connection,
       "etsysOidPhySerialX21Connection": etsysOidPhySerialX21Connection,
       "etsysOidPhyGigEthSXPort": etsysOidPhyGigEthSXPort,
       "etsysOidPhyGigEthLXPort": etsysOidPhyGigEthLXPort,
       "etsysOidPhyGigEthLLXPort": etsysOidPhyGigEthLLXPort,
       "etsysOidPhy6SSRLCGigEthBkplnPort": etsysOidPhy6SSRLCGigEthBkplnPort,
       "etsysOidPhyGPIMx01": etsysOidPhyGPIMx01,
       "etsysOidPhyGPIMx08": etsysOidPhyGPIMx08,
       "etsysOidPhyGPIMx09": etsysOidPhyGPIMx09,
       "etsysOidPhyFastEthMMFPort": etsysOidPhyFastEthMMFPort,
       "etsysOidPhyFastEthSMFPort": etsysOidPhyFastEthSMFPort,
       "etsysOidPhyER16Slot": etsysOidPhyER16Slot,
       "etsysOidPhyXP8Slot": etsysOidPhyXP8Slot,
       "etsysOidPhyXP2Slot": etsysOidPhyXP2Slot,
       "etsysOidPhyXP8IntFlash": etsysOidPhyXP8IntFlash,
       "etsysOidPhyPOSOC3MMF": etsysOidPhyPOSOC3MMF,
       "etsysOidPhyPOSOC3SMF": etsysOidPhyPOSOC3SMF,
       "etsysOidPhyPOSOC12MMF": etsysOidPhyPOSOC12MMF,
       "etsysOidPhyPOSOC12SMF": etsysOidPhyPOSOC12SMF,
       "etsysOidPhy100BASEMTRJMMF": etsysOidPhy100BASEMTRJMMF,
       "etsysOidPhy1000BASET": etsysOidPhy1000BASET,
       "etsysOidPhyXPx2xAtm": etsysOidPhyXPx2xAtm,
       "etsysOidPhyPortSlot": etsysOidPhyPortSlot,
       "etsysOidPhyER16xFDDIx02": etsysOidPhyER16xFDDIx02,
       "etsysOidPhyER16xATM29x02": etsysOidPhyER16xATM29x02,
       "etsysOidPhyER16xSERCx04xAA": etsysOidPhyER16xSERCx04xAA,
       "etsysOidPhyER16xSERCEx04xA": etsysOidPhyER16xSERCEx04xA,
       "etsysOidPhyER16xHSSIx02xAA": etsysOidPhyER16xHSSIx02xAA,
       "etsysOidPhyXPMemory64": etsysOidPhyXPMemory64,
       "etsysOidPhyXPMemory128": etsysOidPhyXPMemory128,
       "etsysOidPhyXPMemory256": etsysOidPhyXPMemory256,
       "etsysOidPhyXP8PowerSupplySlot": etsysOidPhyXP8PowerSupplySlot,
       "etsysOidPhyXP16PowerSupplySlot": etsysOidPhyXP16PowerSupplySlot,
       "etsysOidPhyER16PowerSupplySlot": etsysOidPhyER16PowerSupplySlot,
       "etsysOidPhyXP16SwitchingFabricSlot": etsysOidPhyXP16SwitchingFabricSlot,
       "etsysOidPhyER16SwitchingFabricSlot": etsysOidPhyER16SwitchingFabricSlot,
       "etsysOidPhyNIMxSERx02": etsysOidPhyNIMxSERx02,
       "etsysOidPhyNIMxSERx04": etsysOidPhyNIMxSERx04,
       "etsysOidPhyNIMxT1E1x01": etsysOidPhyNIMxT1E1x01,
       "etsysOidPhyNIMxT1E1x02": etsysOidPhyNIMxT1E1x02,
       "etsysOidPhyNIMxT1E1x04": etsysOidPhyNIMxT1E1x04,
       "etsysOidPhyNIMxCT1E1x01": etsysOidPhyNIMxCT1E1x01,
       "etsysOidPhyNIMxCT1E1x02": etsysOidPhyNIMxCT1E1x02,
       "etsysOidPhyNIMxCT1E1x04": etsysOidPhyNIMxCT1E1x04,
       "etsysOidPhyER16xHFX31x24": etsysOidPhyER16xHFX31x24,
       "etsysOidPhyER16xHFX39x24": etsysOidPhyER16xHFX39x24,
       "etsysOidPhyER16xGTX32x04": etsysOidPhyER16xGTX32x04,
       "etsysOidPhyER16xGTX32x08": etsysOidPhyER16xGTX32x08,
       "etsysOidPhySSRxGTX32x04": etsysOidPhySSRxGTX32x04,
       "etsysOidPhySSRxGSX31x04": etsysOidPhySSRxGSX31x04,
       "etsysOidPhySSRxGLX39x04": etsysOidPhySSRxGLX39x04,
       "etsysOidPhy5SlotFTM1Backplane": etsysOidPhy5SlotFTM1Backplane,
       "etsysOidPhy7SlotFTM1Backplane": etsysOidPhy7SlotFTM1Backplane,
       "etsysOidPhy7SlotFTM2Backplane": etsysOidPhy7SlotFTM2Backplane,
       "etsysOidPhyER16xOS26x01": etsysOidPhyER16xOS26x01,
       "etsysOidPhyMPC8240": etsysOidPhyMPC8240,
       "etsysOidPhyMPC8245": etsysOidPhyMPC8245,
       "etsysOidPhy7G4202x30": etsysOidPhy7G4202x30,
       "etsysOidPhy7Gx6MGBIC": etsysOidPhy7Gx6MGBIC,
       "etsysOidPhy7H4382x49": etsysOidPhy7H4382x49,
       "etsysOidPhy7K4290x02": etsysOidPhy7K4290x02,
       "etsysOidPhy7H4204x48": etsysOidPhy7H4204x48,
       "etsysOidPhy2H412x49R": etsysOidPhy2H412x49R,
       "etsysOidPhy6C207x3": etsysOidPhy6C207x3,
       "etsysOidPhy6C203x1": etsysOidPhy6C203x1,
       "etsysOidPhy6C403": etsysOidPhy6C403,
       "etsysOidPhy6C103": etsysOidPhy6C103,
       "etsysOidPhyVHxSMGMT2": etsysOidPhyVHxSMGMT2,
       "etsysOidPhyVHxRTMxL3": etsysOidPhyVHxRTMxL3,
       "etsysOidPhyGPIMx02": etsysOidPhyGPIMx02,
       "etsysOidPhyNIMxBRIxSTx01": etsysOidPhyNIMxBRIxSTx01,
       "etsysOidPhyNIMxBRIxSTx02": etsysOidPhyNIMxBRIxSTx02,
       "etsysOidPhyNIMxBRIxUx01": etsysOidPhyNIMxBRIxUx01,
       "etsysOidPhyNIMxBRIxUx02": etsysOidPhyNIMxBRIxUx02,
       "etsysOidPhyC5C105": etsysOidPhyC5C105,
       "etsysOidPhyC5C305": etsysOidPhyC5C305,
       "etsysOidPhyC5C205x1": etsysOidPhyC5C205x1,
       "etsysOidPhyC5H124x48": etsysOidPhyC5H124x48,
       "etsysOidPhyC5G124x36": etsysOidPhyC5G124x36,
       "etsysOidPhyC5G122x24": etsysOidPhyC5G122x24,
       "etsysOidPhyC5G114x4": etsysOidPhyC5G114x4,
       "etsysOidPhyC5G124x4": etsysOidPhyC5G124x4,
       "etsysOidPhyC5M100": etsysOidPhyC5M100,
       "etsysOidPhyC2H124x48": etsysOidPhyC2H124x48,
       "etsysOidPhyC2G124x36": etsysOidPhyC2G124x36,
       "etsysOidPhyC2G122x24": etsysOidPhyC2G122x24,
       "etsysOidPhyC2M100": etsysOidPhyC2M100,
       "etsysOidPhyC2C105": etsysOidPhyC2C105,
       "etsysOidPhyC2C100": etsysOidPhyC2C100,
       "etsysOidPhy7G4270x10": etsysOidPhy7G4270x10,
       "etsysOidPhy7H4202x72": etsysOidPhy7H4202x72,
       "etsysOidPhy7C107": etsysOidPhy7C107,
       "etsysOidPhy7C103": etsysOidPhy7C103,
       "etsysOidPhy7C203x1": etsysOidPhy7C203x1,
       "etsysOidPhy7C403": etsysOidPhy7C403,
       "etsysOidPhy7G4275x12": etsysOidPhy7G4275x12,
       "etsysOidPhy7G4270x09": etsysOidPhy7G4270x09,
       "etsysOidPhyNIMxC16T3x01": etsysOidPhyNIMxC16T3x01,
       "etsysOidPhyNIMxC16E3x01": etsysOidPhyNIMxC16E3x01,
       "etsysOidPhyNIMxT3E3x01": etsysOidPhyNIMxT3E3x01,
       "etsysOidPhyNIMxC16T3Sx01": etsysOidPhyNIMxC16T3Sx01,
       "etsysOidPhyNIMxC16E3Sx01": etsysOidPhyNIMxC16E3Sx01,
       "etsysOidPhyNIMxC16T3GSx01": etsysOidPhyNIMxC16T3GSx01,
       "etsysOidPhyNIMxT3Sx01": etsysOidPhyNIMxT3Sx01,
       "etsysOidPhyNIMxE3Sx01": etsysOidPhyNIMxE3Sx01,
       "etsysOidPhyNIMxETHxTGRx01": etsysOidPhyNIMxETHxTGRx01,
       "etsysOidPhyNIMxADSLxACx01": etsysOidPhyNIMxADSLxACx01,
       "etsysOidPhyNIMxADSLxBx01": etsysOidPhyNIMxADSLxBx01,
       "etsysOidPhy7H4383x49": etsysOidPhy7H4383x49,
       "etsysOidPhy7H4284x49": etsysOidPhy7H4284x49,
       "etsysOidPhyV2G121x1": etsysOidPhyV2G121x1,
       "etsysOidPhyV2G112x2": etsysOidPhyV2G112x2,
       "etsysOidPhyV2G151x1M": etsysOidPhyV2G151x1M,
       "etsysOidPhyV2G151x1S": etsysOidPhyV2G151x1S,
       "etsysOidPhy1Hx8FX": etsysOidPhy1Hx8FX,
       "etsysOidPhyE1FxdAcPwrSup": etsysOidPhyE1FxdAcPwrSup,
       "etsysOidPhyNIMxETHRx01": etsysOidPhyNIMxETHRx01,
       "etsysOidPhyNIMxFIBRx01": etsysOidPhyNIMxFIBRx01,
       "etsysOidPhyNIMxDIRELAYx02": etsysOidPhyNIMxDIRELAYx02,
       "etsysOidPhy7G4202x60": etsysOidPhy7G4202x60,
       "etsysOidPhy7G4282x41": etsysOidPhy7G4282x41,
       "etsysOidPhyMGBICNoConnector": etsysOidPhyMGBICNoConnector,
       "etsysOidPhyN7PowerSupplySlot": etsysOidPhyN7PowerSupplySlot,
       "etsysOidPhyN7FanTraySlot": etsysOidPhyN7FanTraySlot,
       "etsysOidPhyN7ModuleSlot": etsysOidPhyN7ModuleSlot,
       "etsysOidPhyN3PowerSupplySlot": etsysOidPhyN3PowerSupplySlot,
       "etsysOidPhyN3FanTraySlot": etsysOidPhyN3FanTraySlot,
       "etsysOidPhyN3ModuleSlot": etsysOidPhyN3ModuleSlot,
       "etsysOidPhyE7PowerSupplySlot": etsysOidPhyE7PowerSupplySlot,
       "etsysOidPhyE7FanTraySlot": etsysOidPhyE7FanTraySlot,
       "etsysOidPhyE7ModuleSlot": etsysOidPhyE7ModuleSlot,
       "etsysOidPhyRj45ConsolePort": etsysOidPhyRj45ConsolePort,
       "etsysOidPhyMGBICx02": etsysOidPhyMGBICx02,
       "etsysOidPhyMGBICx08": etsysOidPhyMGBICx08,
       "etsysOidPhy4H4203x72": etsysOidPhy4H4203x72,
       "etsysOidPhy4H4283x49": etsysOidPhy4H4283x49,
       "etsysOidPhy4G4282x41": etsysOidPhy4G4282x41,
       "etsysOidPhy4G4202x60": etsysOidPhy4G4202x60,
       "etsysOidPhy4H4282x49": etsysOidPhy4H4282x49,
       "etsysOidPhy4H4202x72": etsysOidPhy4H4202x72,
       "etsysOidPhy4H4284x49": etsysOidPhy4H4284x49,
       "etsysOidPhy7H4382x25": etsysOidPhy7H4382x25,
       "etsysOidPhyNoXenpak": etsysOidPhyNoXenpak,
       "etsysOidPhy4H4285x49": etsysOidPhy4H4285x49,
       "etsysOidPhy7H4385x49": etsysOidPhy7H4385x49,
       "etsysOidPhy7G4280x19": etsysOidPhy7G4280x19,
       "etsysOidPhyC2G124x24": etsysOidPhyC2G124x24,
       "etsysOidPhyC2G124x48": etsysOidPhyC2G124x48,
       "etsysOidPhyC2K122x24": etsysOidPhyC2K122x24,
       "etsysOidPhyC2H124x48P": etsysOidPhyC2H124x48P,
       "etsysOidPhyC2G124x48P": etsysOidPhyC2G124x48P,
       "etsysOidPhy7G4202x72": etsysOidPhy7G4202x72,
       "etsysOidPhy7G4205x72": etsysOidPhy7G4205x72,
       "etsysOidPhy7G4282x49": etsysOidPhy7G4282x49,
       "etsysOidPhy7G4285x49": etsysOidPhy7G4285x49,
       "etsysOidPhy4G4202x72": etsysOidPhy4G4202x72,
       "etsysOidPhy4G4205x72": etsysOidPhy4G4205x72,
       "etsysOidPhy4G4282x49": etsysOidPhy4G4282x49,
       "etsysOidPhy4G4285x49": etsysOidPhy4G4285x49,
       "etsysOidPhyMGBICxLC03": etsysOidPhyMGBICxLC03,
       "etsysOidPhyNxPOE": etsysOidPhyNxPOE,
       "etsysOidPhyNxPOEx1200W": etsysOidPhyNxPOEx1200W,
       "etsysOidPhyNxPOEPowerSupplySlot": etsysOidPhyNxPOEPowerSupplySlot,
       "etsysOidPhy7C105xP": etsysOidPhy7C105xP,
       "etsysOidPhy7C205x1": etsysOidPhy7C205x1,
       "etsysOidPhy7C405": etsysOidPhy7C405,
       "etsysOidPhyN5PoEPowerSupplySlot": etsysOidPhyN5PoEPowerSupplySlot,
       "etsysOidPhyN5PoEFanTraySlot": etsysOidPhyN5PoEFanTraySlot,
       "etsysOidPhyN5PoEModuleSlot": etsysOidPhyN5PoEModuleSlot,
       "etsysOidPhyV2H124x24FX": etsysOidPhyV2H124x24FX,
       "etsysOidPhy7Gx6MGBICxA": etsysOidPhy7Gx6MGBICxA,
       "etsysOidPhyN5PoEPoEPowerSupplySlot": etsysOidPhyN5PoEPoEPowerSupplySlot,
       "etsysOidPhy7C117": etsysOidPhy7C117,
       "etsysOidPhy7C115xP": etsysOidPhy7C115xP,
       "etsysOidPhy7C113": etsysOidPhy7C113,
       "etsysOidPhy7C111": etsysOidPhy7C111,
       "etsysOidPhyN1ModuleSlot": etsysOidPhyN1ModuleSlot,
       "etsysOidPhyB2G124x24": etsysOidPhyB2G124x24,
       "etsysOidPhyB2G124x48": etsysOidPhyB2G124x48,
       "etsysOidPhyB2G124x48P": etsysOidPhyB2G124x48P,
       "etsysOidPhyB2H124x48": etsysOidPhyB2H124x48,
       "etsysOidPhyB2H124x48P": etsysOidPhyB2H124x48P,
       "etsysOidPhyB2G124x24P": etsysOidPhyB2G124x24P,
       "etsysOidPhyB2H124x24": etsysOidPhyB2H124x24,
       "etsysOidPhyB2H124x24P": etsysOidPhyB2H124x24P,
       "etsysOidPhyB2H124x24FX": etsysOidPhyB2H124x24FX,
       "etsysOidPhyX16xC": etsysOidPhyX16xC,
       "etsysOidPhyX8xC": etsysOidPhyX8xC,
       "etsysOidPhyX4xC": etsysOidPhyX4xC,
       "etsysOidPhyX16Backplane": etsysOidPhyX16Backplane,
       "etsysOidPhyX8Backplane": etsysOidPhyX8Backplane,
       "etsysOidPhyX4Backplane": etsysOidPhyX4Backplane,
       "etsysOidPhyXxFan": etsysOidPhyXxFan,
       "etsysOidPhyXxAC": etsysOidPhyXxAC,
       "etsysOidPhyXxCMx00": etsysOidPhyXxCMx00,
       "etsysOidPhyX4xCMFx160x00": etsysOidPhyX4xCMFx160x00,
       "etsysOidPhyX16xF640": etsysOidPhyX16xF640,
       "etsysOidPhyX8xF320": etsysOidPhyX8xF320,
       "etsysOidPhyXxM2x00": etsysOidPhyXxM2x00,
       "etsysOidPhyXxG32x00": etsysOidPhyXxG32x00,
       "etsysOidPhyXxT48x01": etsysOidPhyXxT48x01,
       "etsysOidPhyXxM2x01": etsysOidPhyXxM2x01,
       "etsysOidPhyXxM4x01": etsysOidPhyXxM4x01,
       "etsysOidPhyXxG20x01": etsysOidPhyXxG20x01,
       "etsysOidPhyXxG40x01": etsysOidPhyXxG40x01,
       "etsysOidPhyXIOModuleSlot": etsysOidPhyXIOModuleSlot,
       "etsysOidPhyXControlModuleSlot": etsysOidPhyXControlModuleSlot,
       "etsysOidPhyXFabricModuleSlot": etsysOidPhyXFabricModuleSlot,
       "etsysOidPhyXPowerSupplySlot": etsysOidPhyXPowerSupplySlot,
       "etsysOidPhyXFanTraySlot": etsysOidPhyXFanTraySlot,
       "etsysOidPhySFPxGBIC": etsysOidPhySFPxGBIC,
       "etsysOidPhyXFPxGBIC": etsysOidPhyXFPxGBIC,
       "etsysOidPhyXxT32x00": etsysOidPhyXxT32x00,
       "etsysOidPhyC2G134x24P": etsysOidPhyC2G134x24P,
       "etsysOidPhyXxGT16x00": etsysOidPhyXxGT16x00,
       "etsysOidPhyGigEthIntNEMPort": etsysOidPhyGigEthIntNEMPort,
       "etsysOidPhy7SxDSNSA7x01": etsysOidPhy7SxDSNSA7x01,
       "etsysOidPhy7SxNSTAGx01": etsysOidPhy7SxNSTAGx01,
       "etsysOidPhyXxM8x01": etsysOidPhyXxM8x01,
       "etsysOidPhy7SxDSNSA7x01NPS": etsysOidPhy7SxDSNSA7x01NPS,
       "etsysOidPhy7SxNSTAGx01xNPS": etsysOidPhy7SxNSTAGx01xNPS,
       "etsysOidPhy9603805": etsysOidPhy9603805,
       "etsysOidPhy9603806": etsysOidPhy9603806,
       "etsysOidPhyC2G170x24": etsysOidPhyC2G170x24,
       "etsysOidPhy7G4082x25": etsysOidPhy7G4082x25,
       "etsysOidPhyI3Hx12TX": etsysOidPhyI3Hx12TX,
       "etsysOidPhyI3Hx4FXxMM": etsysOidPhyI3Hx4FXxMM,
       "etsysOidPhyI3Hx8FXxMM": etsysOidPhyI3Hx8FXxMM,
       "etsysOidPhyI3Hx8TXx2FX": etsysOidPhyI3Hx8TXx2FX,
       "etsysOidPhy7Gx6MGBICxB": etsysOidPhy7Gx6MGBICxB,
       "etsysOidPhy7Kx2XFPx6MGBIC": etsysOidPhy7Kx2XFPx6MGBIC,
       "etsysOidPhy7GR4280x19": etsysOidPhy7GR4280x19,
       "etsysOidPhy7GR4270x12": etsysOidPhy7GR4270x12,
       "etsysOidPhy7GR4202x30": etsysOidPhy7GR4202x30,
       "etsysOidPhy7KR4290x02": etsysOidPhy7KR4290x02,
       "etsysOidPhyNoXfp": etsysOidPhyNoXfp,
       "etsysOidPhyMGBICxLC04": etsysOidPhyMGBICxLC04,
       "etsysOidPhy10GbExSRxXFP": etsysOidPhy10GbExSRxXFP,
       "etsysOidPhy10GbExLRxXFP": etsysOidPhy10GbExLRxXFP,
       "etsysOidPhy10GbExERxXFP": etsysOidPhy10GbExERxXFP,
       "etsysOidPhy10GbExCX4xXFP": etsysOidPhy10GbExCX4xXFP,
       "etsysOidPhy10GbExCX4": etsysOidPhy10GbExCX4,
       "etsysOidPhy10GbExSWxXFP": etsysOidPhy10GbExSWxXFP,
       "etsysOidPhy10GbExLWxXFP": etsysOidPhy10GbExLWxXFP,
       "etsysOidPhy10GbExEWxXFP": etsysOidPhy10GbExEWxXFP,
       "etsysOidPhy10GbExLX4xXFP": etsysOidPhy10GbExLX4xXFP,
       "etsysOidPhy10GbExZRxXFP": etsysOidPhy10GbExZRxXFP,
       "etsysOidPhy10GbExZWxXFP": etsysOidPhy10GbExZWxXFP,
       "etsysOidPhy10GbExZR": etsysOidPhy10GbExZR,
       "etsysOidPhy10GbExZW": etsysOidPhy10GbExZW,
       "etsysOidPhyMGBICxLC05": etsysOidPhyMGBICxLC05,
       "etsysOidPhy7K4297x02": etsysOidPhy7K4297x02,
       "etsysOidPhy7K4297x04": etsysOidPhy7K4297x04,
       "etsysOidPhy7KR4297x02": etsysOidPhy7KR4297x02,
       "etsysOidPhy7KR4297x04": etsysOidPhy7KR4297x04,
       "etsysOidPhy7S4280x19": etsysOidPhy7S4280x19,
       "etsysOidPhy2S4082x25": etsysOidPhy2S4082x25,
       "etsysOidPhy7SxNSNACGx01xNPS": etsysOidPhy7SxNSNACGx01xNPS,
       "etsysOidPhyMGBICxLC07": etsysOidPhyMGBICxLC07,
       "etsysOidPhy7SxNACGx01": etsysOidPhy7SxNACGx01,
       "etsysOidPhy7SxC20N": etsysOidPhy7SxC20N,
       "etsysOidPhy10GbExSRxSFPP": etsysOidPhy10GbExSRxSFPP,
       "etsysOidPhy10GbExLRxSFPP": etsysOidPhy10GbExLRxSFPP,
       "etsysOidPhy10GbExLRMxSFPP": etsysOidPhy10GbExLRMxSFPP,
       "etsysOidPhy10GbExC01xSFPP": etsysOidPhy10GbExC01xSFPP,
       "etsysOidPhy10GbExC03xSFPP": etsysOidPhy10GbExC03xSFPP,
       "etsysOidPhy10GbExC10xSFPP": etsysOidPhy10GbExC10xSFPP,
       "etsysOidPhy10GbExC20xSFPP": etsysOidPhy10GbExC20xSFPP,
       "etsysOidPhySFPPNoConnector": etsysOidPhySFPPNoConnector,
       "etsysOidPhy10GbExLRMxXFP": etsysOidPhy10GbExLRMxXFP,
       "etsysOidPhy7SxDNSAx01": etsysOidPhy7SxDNSAx01,
       "etsysOidPhyS3xCHASSIS": etsysOidPhyS3xCHASSIS,
       "etsysOidPhyS4xCHASSIS": etsysOidPhyS4xCHASSIS,
       "etsysOidPhyS8xCHASSIS": etsysOidPhyS8xCHASSIS,
       "etsysOidPhySxFAN": etsysOidPhySxFAN,
       "etsysOidPhySxACxPS": etsysOidPhySxACxPS,
       "etsysOidPhySxPOExPS": etsysOidPhySxPOExPS,
       "etsysOidPhySxPOEx4BAY": etsysOidPhySxPOEx4BAY,
       "etsysOidPhySxPOEx8BAY": etsysOidPhySxPOEx8BAY,
       "etsysOidPhySPowerSupplySlot": etsysOidPhySPowerSupplySlot,
       "etsysOidPhySFanTraySlot": etsysOidPhySFanTraySlot,
       "etsysOidPhySIOModuleSlot": etsysOidPhySIOModuleSlot,
       "etsysOidPhySFabricModuleSlot": etsysOidPhySFabricModuleSlot,
       "etsysOidPhySPoEPowerSupplySlot": etsysOidPhySPoEPowerSupplySlot,
       "etsysOidPhySK1208x0808xF6": etsysOidPhySK1208x0808xF6,
       "etsysOidPhyST4106x0348xF6": etsysOidPhyST4106x0348xF6,
       "etsysOidPhyST1206x0848xF6": etsysOidPhyST1206x0848xF6,
       "etsysOidPhySG1201x0848xF6": etsysOidPhySG1201x0848xF6,
       "etsysOidPhySK1008x0816": etsysOidPhySK1008x0816,
       "etsysOidPhyST4106x0248": etsysOidPhyST4106x0248,
       "etsysOidPhyST4006x0272": etsysOidPhyST4006x0272,
       "etsysOidPhyST1206x0848": etsysOidPhyST1206x0848,
       "etsysOidPhySG4101x0248": etsysOidPhySG4101x0248,
       "etsysOidPhySG1201x0848": etsysOidPhySG1201x0848,
       "etsysOidPhySOptModType1Slot": etsysOidPhySOptModType1Slot,
       "etsysOidPhySOptModType2Slot": etsysOidPhySOptModType2Slot,
       "etsysOidPhySOK1208x0104": etsysOidPhySOK1208x0104,
       "etsysOidPhySOK1208x0102": etsysOidPhySOK1208x0102,
       "etsysOidPhySOK1208x0204": etsysOidPhySOK1208x0204,
       "etsysOidPhySOG1201x0112": etsysOidPhySOG1201x0112,
       "etsysOidPhyNN0100x0100xF2": etsysOidPhyNN0100x0100xF2,
       "etsysOidPhyNT4106x0248": etsysOidPhyNT4106x0248,
       "etsysOidPhyNT4006x0272": etsysOidPhyNT4006x0272,
       "etsysOidPhyNT1006x0448": etsysOidPhyNT1006x0448,
       "etsysOidPhyNK1008x0408": etsysOidPhyNK1008x0408,
       "etsysOidPhyNG1001x0448": etsysOidPhyNG1001x0448,
       "etsysOidPhyNG4101x0248": etsysOidPhyNG4101x0248,
       "etsysOidPhyNGNOptModSlot": etsysOidPhyNGNOptModSlot,
       "etsysOidPhyNOK1208x0102": etsysOidPhyNOK1208x0102,
       "etsysOidPhyNOK1208x0104": etsysOidPhyNOK1208x0104,
       "etsysOidPhyNOG1201x0112": etsysOidPhyNOG1201x0112,
       "etsysOidPhySSAxACxPSx600W": etsysOidPhySSAxACxPSx600W,
       "etsysOidPhySSAxACxPSx1000W": etsysOidPhySSAxACxPSx1000W,
       "etsysOidPhySSAPowerSupplySlot": etsysOidPhySSAPowerSupplySlot,
       "etsysOidPhy10GBxERxSFPP": etsysOidPhy10GBxERxSFPP,
       "etsysOidPhyUSBAPort": etsysOidPhyUSBAPort,
       "etsysOidPhyUSBMicroABPort": etsysOidPhyUSBMicroABPort,
       "etsysOidPhyS8Backplane": etsysOidPhyS8Backplane,
       "etsysOidPhyS4Backplane": etsysOidPhyS4Backplane,
       "etsysOidPhyS3Backplane": etsysOidPhyS3Backplane,
       "etsysOidPhyN5Backplane": etsysOidPhyN5Backplane,
       "etsysOidPhyN3Backplane": etsysOidPhyN3Backplane,
       "etsysOidPhyN1Backplane": etsysOidPhyN1Backplane,
       "etsysOidPhySOT1206x0112": etsysOidPhySOT1206x0112,
       "etsysOidPhyNOT1206x0112": etsysOidPhyNOT1206x0112,
       "etsysOidPhyConsolePortUsbMicroAB": etsysOidPhyConsolePortUsbMicroAB,
       "etsysOidPhySSAxFAN": etsysOidPhySSAxFAN,
       "etsysOidPhyNSAxFAN": etsysOidPhyNSAxFAN,
       "etsysOidPhyNSAxACxPS": etsysOidPhyNSAxACxPS,
       "etsysOidPhyN1xFAN": etsysOidPhyN1xFAN,
       "etsysOidPhyN1xACxPS": etsysOidPhyN1xACxPS,
       "etsysOidPhy10GBxLWxSFPP": etsysOidPhy10GBxLWxSFPP,
       "etsysOidPhy10GBxLWxXFP": etsysOidPhy10GBxLWxXFP,
       "etsysOidPhy10GBxLWx20": etsysOidPhy10GBxLWx20,
       "etsysOidPhy10GBxLWx10": etsysOidPhy10GBxLWx10,
       "etsysOidPhy10GBxLWx05": etsysOidPhy10GBxLWx05,
       "etsysOidPhy10GBxLWx03": etsysOidPhy10GBxLWx03,
       "etsysOidPhyMGBICxBX10xD": etsysOidPhyMGBICxBX10xD,
       "etsysOidPhyMGBICxBX10xU": etsysOidPhyMGBICxBX10xU,
       "etsysOidPhyIncompatiblePluggable": etsysOidPhyIncompatiblePluggable,
       "etsysOidPhySK5208x0808xF6": etsysOidPhySK5208x0808xF6,
       "etsysOidPhyST5206x0848xF6": etsysOidPhyST5206x0848xF6,
       "etsysOidPhySG5201x0848xF6": etsysOidPhySG5201x0848xF6,
       "etsysOidPhyK6xCHASSIS": etsysOidPhyK6xCHASSIS,
       "etsysOidPhyK10xCHASSIS": etsysOidPhyK10xCHASSIS,
       "etsysOidPhyK6xFAN": etsysOidPhyK6xFAN,
       "etsysOidPhyK10xFAN": etsysOidPhyK10xFAN,
       "etsysOidPhyKxACxPSx1440W": etsysOidPhyKxACxPSx1440W,
       "etsysOidPhyKxPOExExtConn": etsysOidPhyKxPOExExtConn,
       "etsysOidPhyKPowerSupplySlot": etsysOidPhyKPowerSupplySlot,
       "etsysOidPhyK6FanTraySlot": etsysOidPhyK6FanTraySlot,
       "etsysOidPhyK10FanTraySlot": etsysOidPhyK10FanTraySlot,
       "etsysOidPhyKLineCardSlot": etsysOidPhyKLineCardSlot,
       "etsysOidPhyKFabricModuleSlot": etsysOidPhyKFabricModuleSlot,
       "etsysOidPhyKK2008x0204xF1": etsysOidPhyKK2008x0204xF1,
       "etsysOidPhyKK2008x0204xF2": etsysOidPhyKK2008x0204xF2,
       "etsysOidPhyKK2000x0000xF1": etsysOidPhyKK2000x0000xF1,
       "etsysOidPhyKK2000x0000xF2": etsysOidPhyKK2000x0000xF2,
       "etsysOidPhyKT2006x0224": etsysOidPhyKT2006x0224,
       "etsysOidPhyKG2001x0224": etsysOidPhyKG2001x0224,
       "etsysOidPhyKK2008x0204": etsysOidPhyKK2008x0204,
       "etsysOidPhyK6Backplane": etsysOidPhyK6Backplane,
       "etsysOidPhyK10Backplane": etsysOidPhyK10Backplane,
       "etsysOidPhySxDCxPS": etsysOidPhySxDCxPS,
       "etsysOidPhyMGBICxBX40xD": etsysOidPhyMGBICxBX40xD,
       "etsysOidPhyMGBICxBX40xU": etsysOidPhyMGBICxBX40xU,
       "etsysOidPhyMGBICxBX120xD": etsysOidPhyMGBICxBX120xD,
       "etsysOidPhyMGBICxBX120xU": etsysOidPhyMGBICxBX120xU,
       "etsysOidPhyS6xCHASSIS": etsysOidPhyS6xCHASSIS,
       "etsysOidPhyS6Backplane": etsysOidPhyS6Backplane,
       "etsysOidOther": etsysOidOther,
       "etsysOidIEEE8023adLagInterface": etsysOidIEEE8023adLagInterface,
       "etsysOidOtherLicenseKeyId": etsysOidOtherLicenseKeyId}
)

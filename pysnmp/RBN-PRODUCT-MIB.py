# SNMP MIB module (RBN-PRODUCT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-PRODUCT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:19 2024
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

(rbnEntities,
 rbnModules,
 rbnProducts) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnEntities",
    "rbnModules",
    "rbnProducts")

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

rbnProductMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5, 1)
)
rbnProductMIB.setRevisions(
        ("2012-03-19 18:00",
         "2012-02-10 18:00",
         "2011-06-02 18:00",
         "2011-01-19 18:00",
         "2010-10-01 00:00",
         "2010-08-27 00:00",
         "2010-04-01 00:00",
         "2010-01-27 00:00",
         "2009-10-05 00:00",
         "2009-09-24 00:00",
         "2009-09-13 00:00",
         "2009-09-10 00:00",
         "2009-07-16 00:00",
         "2009-02-04 00:00",
         "2009-01-20 00:00",
         "2008-09-23 00:00",
         "2008-07-02 00:00",
         "2008-05-20 00:00",
         "2008-05-08 00:00",
         "2007-09-20 00:00",
         "2007-08-08 00:00",
         "2007-05-09 00:00",
         "2007-02-28 00:00",
         "2007-02-14 00:00",
         "2007-02-05 00:00",
         "2005-12-27 00:00",
         "2005-03-01 00:00",
         "2004-11-05 00:00",
         "2004-05-11 00:00",
         "2003-09-25 00:00",
         "2003-07-24 00:00",
         "2003-05-19 17:00",
         "2003-05-05 00:00",
         "2003-03-25 00:00",
         "2002-06-13 00:00",
         "2002-06-06 00:00",
         "2001-12-12 00:00",
         "2001-09-26 17:00",
         "2001-07-25 10:00",
         "2001-05-15 15:07",
         "2001-05-04 16:42",
         "2001-02-13 18:57",
         "2001-02-13 10:07",
         "2001-02-01 17:07",
         "2001-01-05 18:34",
         "2000-12-28 17:04",
         "2000-11-15 17:04",
         "2000-11-02 14:54",
         "2000-10-25 15:23",
         "2000-10-20 17:30",
         "2000-09-26 13:30",
         "2000-09-25 11:20",
         "2000-07-19 15:44",
         "2000-07-06 21:50",
         "2000-06-16 17:00",
         "2000-06-13 17:00",
         "2000-05-18 00:00",
         "1999-07-08 17:12",
         "1998-08-05 19:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnSMS1000_ObjectIdentity = ObjectIdentity
rbnSMS1000 = _RbnSMS1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 1, 1)
)
if mibBuilder.loadTexts:
    rbnSMS1000.setStatus("current")
_RbnSMS500_ObjectIdentity = ObjectIdentity
rbnSMS500 = _RbnSMS500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 1, 2)
)
if mibBuilder.loadTexts:
    rbnSMS500.setStatus("current")
_RbnSMS1800_ObjectIdentity = ObjectIdentity
rbnSMS1800 = _RbnSMS1800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 1, 3)
)
if mibBuilder.loadTexts:
    rbnSMS1800.setStatus("current")
_RbnSMS10000_ObjectIdentity = ObjectIdentity
rbnSMS10000 = _RbnSMS10000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 1, 4)
)
if mibBuilder.loadTexts:
    rbnSMS10000.setStatus("current")
_RbnSmartEdge800_ObjectIdentity = ObjectIdentity
rbnSmartEdge800 = _RbnSmartEdge800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 1, 10)
)
if mibBuilder.loadTexts:
    rbnSmartEdge800.setStatus("current")
_RbnSmartEdge400_ObjectIdentity = ObjectIdentity
rbnSmartEdge400 = _RbnSmartEdge400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 1, 11)
)
if mibBuilder.loadTexts:
    rbnSmartEdge400.setStatus("current")
_RbnSmartEdge100_ObjectIdentity = ObjectIdentity
rbnSmartEdge100 = _RbnSmartEdge100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 1, 12)
)
if mibBuilder.loadTexts:
    rbnSmartEdge100.setStatus("current")
_RbnSmartEdge1200_ObjectIdentity = ObjectIdentity
rbnSmartEdge1200 = _RbnSmartEdge1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 1, 13)
)
if mibBuilder.loadTexts:
    rbnSmartEdge1200.setStatus("current")
_RbnSM480_ObjectIdentity = ObjectIdentity
rbnSM480 = _RbnSM480_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 1, 14)
)
if mibBuilder.loadTexts:
    rbnSM480.setStatus("current")
_RbnSmartEdge600_ObjectIdentity = ObjectIdentity
rbnSmartEdge600 = _RbnSmartEdge600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 1, 15)
)
if mibBuilder.loadTexts:
    rbnSmartEdge600.setStatus("current")
_RbnSM240_ObjectIdentity = ObjectIdentity
rbnSM240 = _RbnSM240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 1, 16)
)
if mibBuilder.loadTexts:
    rbnSM240.setStatus("current")
_RbnSSR8020_ObjectIdentity = ObjectIdentity
rbnSSR8020 = _RbnSSR8020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 1, 17)
)
if mibBuilder.loadTexts:
    rbnSSR8020.setStatus("current")
_RbnSSR8010_ObjectIdentity = ObjectIdentity
rbnSSR8010 = _RbnSSR8010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 1, 18)
)
if mibBuilder.loadTexts:
    rbnSSR8010.setStatus("current")
_RbnSSR8006_ObjectIdentity = ObjectIdentity
rbnSSR8006 = _RbnSSR8006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 1, 19)
)
if mibBuilder.loadTexts:
    rbnSSR8006.setStatus("current")
_RbnEntityTypeOther_ObjectIdentity = ObjectIdentity
rbnEntityTypeOther = _RbnEntityTypeOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 1)
)
if mibBuilder.loadTexts:
    rbnEntityTypeOther.setStatus("current")
_RbnEntityTypeUnknown_ObjectIdentity = ObjectIdentity
rbnEntityTypeUnknown = _RbnEntityTypeUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 2)
)
if mibBuilder.loadTexts:
    rbnEntityTypeUnknown.setStatus("current")
_RbnEntityTypeChassis_ObjectIdentity = ObjectIdentity
rbnEntityTypeChassis = _RbnEntityTypeChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 3)
)
if mibBuilder.loadTexts:
    rbnEntityTypeChassis.setStatus("current")
_RbnEntChassisSMS1000_ObjectIdentity = ObjectIdentity
rbnEntChassisSMS1000 = _RbnEntChassisSMS1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 3, 1)
)
if mibBuilder.loadTexts:
    rbnEntChassisSMS1000.setStatus("current")
_RbnEntChassisSMS500_ObjectIdentity = ObjectIdentity
rbnEntChassisSMS500 = _RbnEntChassisSMS500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 3, 2)
)
if mibBuilder.loadTexts:
    rbnEntChassisSMS500.setStatus("current")
_RbnEntChassisSMS1800_ObjectIdentity = ObjectIdentity
rbnEntChassisSMS1800 = _RbnEntChassisSMS1800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 3, 3)
)
if mibBuilder.loadTexts:
    rbnEntChassisSMS1800.setStatus("current")
_RbnEntChassisSMS10000_ObjectIdentity = ObjectIdentity
rbnEntChassisSMS10000 = _RbnEntChassisSMS10000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 3, 4)
)
if mibBuilder.loadTexts:
    rbnEntChassisSMS10000.setStatus("current")
_RbnEntChassisSE800_ObjectIdentity = ObjectIdentity
rbnEntChassisSE800 = _RbnEntChassisSE800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 3, 6)
)
if mibBuilder.loadTexts:
    rbnEntChassisSE800.setStatus("current")
_RbnEntChassisSE400_ObjectIdentity = ObjectIdentity
rbnEntChassisSE400 = _RbnEntChassisSE400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 3, 7)
)
if mibBuilder.loadTexts:
    rbnEntChassisSE400.setStatus("current")
_RbnEntChassisSE100_ObjectIdentity = ObjectIdentity
rbnEntChassisSE100 = _RbnEntChassisSE100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 3, 8)
)
if mibBuilder.loadTexts:
    rbnEntChassisSE100.setStatus("current")
_RbnEntChassisSE1200_ObjectIdentity = ObjectIdentity
rbnEntChassisSE1200 = _RbnEntChassisSE1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 3, 9)
)
if mibBuilder.loadTexts:
    rbnEntChassisSE1200.setStatus("current")
_RbnEntChassisSM480_ObjectIdentity = ObjectIdentity
rbnEntChassisSM480 = _RbnEntChassisSM480_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 3, 10)
)
if mibBuilder.loadTexts:
    rbnEntChassisSM480.setStatus("current")
_RbnEntChassisSE600_ObjectIdentity = ObjectIdentity
rbnEntChassisSE600 = _RbnEntChassisSE600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 3, 11)
)
if mibBuilder.loadTexts:
    rbnEntChassisSE600.setStatus("current")
_RbnEntChassisSM240_ObjectIdentity = ObjectIdentity
rbnEntChassisSM240 = _RbnEntChassisSM240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 3, 12)
)
if mibBuilder.loadTexts:
    rbnEntChassisSM240.setStatus("current")
_RbnEntChassisSE1200H_ObjectIdentity = ObjectIdentity
rbnEntChassisSE1200H = _RbnEntChassisSE1200H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 3, 13)
)
if mibBuilder.loadTexts:
    rbnEntChassisSE1200H.setStatus("current")
_RbnEntChassisSSR8020_ObjectIdentity = ObjectIdentity
rbnEntChassisSSR8020 = _RbnEntChassisSSR8020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 3, 14)
)
if mibBuilder.loadTexts:
    rbnEntChassisSSR8020.setStatus("current")
_RbnEntChassisSSR8010_ObjectIdentity = ObjectIdentity
rbnEntChassisSSR8010 = _RbnEntChassisSSR8010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 3, 15)
)
if mibBuilder.loadTexts:
    rbnEntChassisSSR8010.setStatus("current")
_RbnEntChassisSSR8006_ObjectIdentity = ObjectIdentity
rbnEntChassisSSR8006 = _RbnEntChassisSSR8006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 3, 16)
)
if mibBuilder.loadTexts:
    rbnEntChassisSSR8006.setStatus("current")
_RbnEntityTypeBackplane_ObjectIdentity = ObjectIdentity
rbnEntityTypeBackplane = _RbnEntityTypeBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4)
)
if mibBuilder.loadTexts:
    rbnEntityTypeBackplane.setStatus("current")
_RbnEntBackplaneSMS1000Data_ObjectIdentity = ObjectIdentity
rbnEntBackplaneSMS1000Data = _RbnEntBackplaneSMS1000Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4, 1)
)
if mibBuilder.loadTexts:
    rbnEntBackplaneSMS1000Data.setStatus("current")
_RbnEntBackplaneSMS1000Power_ObjectIdentity = ObjectIdentity
rbnEntBackplaneSMS1000Power = _RbnEntBackplaneSMS1000Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4, 2)
)
if mibBuilder.loadTexts:
    rbnEntBackplaneSMS1000Power.setStatus("current")
_RbnEntBackplaneSMS500Data_ObjectIdentity = ObjectIdentity
rbnEntBackplaneSMS500Data = _RbnEntBackplaneSMS500Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4, 3)
)
if mibBuilder.loadTexts:
    rbnEntBackplaneSMS500Data.setStatus("current")
_RbnEntBackplaneSMS500Power_ObjectIdentity = ObjectIdentity
rbnEntBackplaneSMS500Power = _RbnEntBackplaneSMS500Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4, 4)
)
if mibBuilder.loadTexts:
    rbnEntBackplaneSMS500Power.setStatus("current")
_RbnEntBackplaneSMS1800Data_ObjectIdentity = ObjectIdentity
rbnEntBackplaneSMS1800Data = _RbnEntBackplaneSMS1800Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4, 5)
)
if mibBuilder.loadTexts:
    rbnEntBackplaneSMS1800Data.setStatus("current")
_RbnEntBackplaneSMS1800Power_ObjectIdentity = ObjectIdentity
rbnEntBackplaneSMS1800Power = _RbnEntBackplaneSMS1800Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4, 6)
)
if mibBuilder.loadTexts:
    rbnEntBackplaneSMS1800Power.setStatus("current")
_RbnEntBackplaneSMS10000Midplane_ObjectIdentity = ObjectIdentity
rbnEntBackplaneSMS10000Midplane = _RbnEntBackplaneSMS10000Midplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4, 7)
)
if mibBuilder.loadTexts:
    rbnEntBackplaneSMS10000Midplane.setStatus("current")
_RbnEntBackplaneSE800Data_ObjectIdentity = ObjectIdentity
rbnEntBackplaneSE800Data = _RbnEntBackplaneSE800Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4, 10)
)
if mibBuilder.loadTexts:
    rbnEntBackplaneSE800Data.setStatus("current")
_RbnEntBackplaneSE400Data_ObjectIdentity = ObjectIdentity
rbnEntBackplaneSE400Data = _RbnEntBackplaneSE400Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4, 11)
)
if mibBuilder.loadTexts:
    rbnEntBackplaneSE400Data.setStatus("current")
_RbnEntBackplaneSE100Data_ObjectIdentity = ObjectIdentity
rbnEntBackplaneSE100Data = _RbnEntBackplaneSE100Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4, 12)
)
if mibBuilder.loadTexts:
    rbnEntBackplaneSE100Data.setStatus("current")
_RbnEntBackplaneSE1200Data_ObjectIdentity = ObjectIdentity
rbnEntBackplaneSE1200Data = _RbnEntBackplaneSE1200Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4, 13)
)
if mibBuilder.loadTexts:
    rbnEntBackplaneSE1200Data.setStatus("current")
_RbnEntBackplaneSM480Data_ObjectIdentity = ObjectIdentity
rbnEntBackplaneSM480Data = _RbnEntBackplaneSM480Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4, 14)
)
if mibBuilder.loadTexts:
    rbnEntBackplaneSM480Data.setStatus("current")
_RbnEntBackplaneSE600Data_ObjectIdentity = ObjectIdentity
rbnEntBackplaneSE600Data = _RbnEntBackplaneSE600Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4, 15)
)
if mibBuilder.loadTexts:
    rbnEntBackplaneSE600Data.setStatus("current")
_RbnEntBackplaneSM240Data_ObjectIdentity = ObjectIdentity
rbnEntBackplaneSM240Data = _RbnEntBackplaneSM240Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4, 16)
)
if mibBuilder.loadTexts:
    rbnEntBackplaneSM240Data.setStatus("current")
_RbnEntBackplaneSE1200HData_ObjectIdentity = ObjectIdentity
rbnEntBackplaneSE1200HData = _RbnEntBackplaneSE1200HData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4, 17)
)
if mibBuilder.loadTexts:
    rbnEntBackplaneSE1200HData.setStatus("current")
_RbnEntBackplaneSSR8020Data_ObjectIdentity = ObjectIdentity
rbnEntBackplaneSSR8020Data = _RbnEntBackplaneSSR8020Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4, 18)
)
if mibBuilder.loadTexts:
    rbnEntBackplaneSSR8020Data.setStatus("current")
_RbnEntBackplaneSSR8010Data_ObjectIdentity = ObjectIdentity
rbnEntBackplaneSSR8010Data = _RbnEntBackplaneSSR8010Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4, 19)
)
if mibBuilder.loadTexts:
    rbnEntBackplaneSSR8010Data.setStatus("current")
_RbnEntBackplaneSSR8006Data_ObjectIdentity = ObjectIdentity
rbnEntBackplaneSSR8006Data = _RbnEntBackplaneSSR8006Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 4, 20)
)
if mibBuilder.loadTexts:
    rbnEntBackplaneSSR8006Data.setStatus("current")
_RbnEntityTypeContainer_ObjectIdentity = ObjectIdentity
rbnEntityTypeContainer = _RbnEntityTypeContainer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5)
)
if mibBuilder.loadTexts:
    rbnEntityTypeContainer.setStatus("current")
_RbnEntContainerSMS1000Data_ObjectIdentity = ObjectIdentity
rbnEntContainerSMS1000Data = _RbnEntContainerSMS1000Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 1)
)
if mibBuilder.loadTexts:
    rbnEntContainerSMS1000Data.setStatus("current")
_RbnEntContainerSMS1000Power_ObjectIdentity = ObjectIdentity
rbnEntContainerSMS1000Power = _RbnEntContainerSMS1000Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 2)
)
if mibBuilder.loadTexts:
    rbnEntContainerSMS1000Power.setStatus("current")
_RbnEntContainerSMS500Data_ObjectIdentity = ObjectIdentity
rbnEntContainerSMS500Data = _RbnEntContainerSMS500Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 3)
)
if mibBuilder.loadTexts:
    rbnEntContainerSMS500Data.setStatus("current")
_RbnEntContainerSMS500Power_ObjectIdentity = ObjectIdentity
rbnEntContainerSMS500Power = _RbnEntContainerSMS500Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 4)
)
if mibBuilder.loadTexts:
    rbnEntContainerSMS500Power.setStatus("current")
_RbnEntContainerSMS1800Data_ObjectIdentity = ObjectIdentity
rbnEntContainerSMS1800Data = _RbnEntContainerSMS1800Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 5)
)
if mibBuilder.loadTexts:
    rbnEntContainerSMS1800Data.setStatus("current")
_RbnEntContainerSMS1800Power_ObjectIdentity = ObjectIdentity
rbnEntContainerSMS1800Power = _RbnEntContainerSMS1800Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 6)
)
if mibBuilder.loadTexts:
    rbnEntContainerSMS1800Power.setStatus("current")
_RbnEntContainerSMS10000Fabric_ObjectIdentity = ObjectIdentity
rbnEntContainerSMS10000Fabric = _RbnEntContainerSMS10000Fabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 7)
)
if mibBuilder.loadTexts:
    rbnEntContainerSMS10000Fabric.setStatus("current")
_RbnEntContainerSMS10000Timing_ObjectIdentity = ObjectIdentity
rbnEntContainerSMS10000Timing = _RbnEntContainerSMS10000Timing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 8)
)
if mibBuilder.loadTexts:
    rbnEntContainerSMS10000Timing.setStatus("current")
_RbnEntContainerSMS10000SMCM_ObjectIdentity = ObjectIdentity
rbnEntContainerSMS10000SMCM = _RbnEntContainerSMS10000SMCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 9)
)
if mibBuilder.loadTexts:
    rbnEntContainerSMS10000SMCM.setStatus("current")
_RbnEntContainerSMS10000IO_ObjectIdentity = ObjectIdentity
rbnEntContainerSMS10000IO = _RbnEntContainerSMS10000IO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 10)
)
if mibBuilder.loadTexts:
    rbnEntContainerSMS10000IO.setStatus("current")
_RbnEntContainerSE800Data_ObjectIdentity = ObjectIdentity
rbnEntContainerSE800Data = _RbnEntContainerSE800Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 14)
)
if mibBuilder.loadTexts:
    rbnEntContainerSE800Data.setStatus("current")
_RbnEntContainerSE400Data_ObjectIdentity = ObjectIdentity
rbnEntContainerSE400Data = _RbnEntContainerSE400Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 15)
)
if mibBuilder.loadTexts:
    rbnEntContainerSE400Data.setStatus("current")
_RbnEntContainerSE100Data_ObjectIdentity = ObjectIdentity
rbnEntContainerSE100Data = _RbnEntContainerSE100Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 16)
)
if mibBuilder.loadTexts:
    rbnEntContainerSE100Data.setStatus("current")
_RbnEntContainerSE100Carrier_ObjectIdentity = ObjectIdentity
rbnEntContainerSE100Carrier = _RbnEntContainerSE100Carrier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 17)
)
if mibBuilder.loadTexts:
    rbnEntContainerSE100Carrier.setStatus("current")
_RbnEntContainerSE1200Data_ObjectIdentity = ObjectIdentity
rbnEntContainerSE1200Data = _RbnEntContainerSE1200Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 18)
)
if mibBuilder.loadTexts:
    rbnEntContainerSE1200Data.setStatus("current")
_RbnEntContainerSM480Data_ObjectIdentity = ObjectIdentity
rbnEntContainerSM480Data = _RbnEntContainerSM480Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 19)
)
if mibBuilder.loadTexts:
    rbnEntContainerSM480Data.setStatus("current")
_RbnEntContainerSE600Data_ObjectIdentity = ObjectIdentity
rbnEntContainerSE600Data = _RbnEntContainerSE600Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 20)
)
if mibBuilder.loadTexts:
    rbnEntContainerSE600Data.setStatus("current")
_RbnEntContainerSM240Data_ObjectIdentity = ObjectIdentity
rbnEntContainerSM240Data = _RbnEntContainerSM240Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 21)
)
if mibBuilder.loadTexts:
    rbnEntContainerSM240Data.setStatus("current")
_RbnEntContainerSE1200HData_ObjectIdentity = ObjectIdentity
rbnEntContainerSE1200HData = _RbnEntContainerSE1200HData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 22)
)
if mibBuilder.loadTexts:
    rbnEntContainerSE1200HData.setStatus("current")
_RbnEntContainerSSR8020FanTray_ObjectIdentity = ObjectIdentity
rbnEntContainerSSR8020FanTray = _RbnEntContainerSSR8020FanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 23)
)
if mibBuilder.loadTexts:
    rbnEntContainerSSR8020FanTray.setStatus("current")
_RbnEntContainerSSR8020PowerModule_ObjectIdentity = ObjectIdentity
rbnEntContainerSSR8020PowerModule = _RbnEntContainerSSR8020PowerModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 24)
)
if mibBuilder.loadTexts:
    rbnEntContainerSSR8020PowerModule.setStatus("current")
_RbnEntContainerSSR8020Data_ObjectIdentity = ObjectIdentity
rbnEntContainerSSR8020Data = _RbnEntContainerSSR8020Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 25)
)
if mibBuilder.loadTexts:
    rbnEntContainerSSR8020Data.setStatus("current")
_RbnEntContainerSSR8010FanTray_ObjectIdentity = ObjectIdentity
rbnEntContainerSSR8010FanTray = _RbnEntContainerSSR8010FanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 26)
)
if mibBuilder.loadTexts:
    rbnEntContainerSSR8010FanTray.setStatus("current")
_RbnEntContainerSSR8010PowerModule_ObjectIdentity = ObjectIdentity
rbnEntContainerSSR8010PowerModule = _RbnEntContainerSSR8010PowerModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 27)
)
if mibBuilder.loadTexts:
    rbnEntContainerSSR8010PowerModule.setStatus("current")
_RbnEntContainerSSR8010Data_ObjectIdentity = ObjectIdentity
rbnEntContainerSSR8010Data = _RbnEntContainerSSR8010Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 28)
)
if mibBuilder.loadTexts:
    rbnEntContainerSSR8010Data.setStatus("current")
_RbnEntContainerSSR8006FanTray_ObjectIdentity = ObjectIdentity
rbnEntContainerSSR8006FanTray = _RbnEntContainerSSR8006FanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 29)
)
if mibBuilder.loadTexts:
    rbnEntContainerSSR8006FanTray.setStatus("current")
_RbnEntContainerSSR8006PowerModule_ObjectIdentity = ObjectIdentity
rbnEntContainerSSR8006PowerModule = _RbnEntContainerSSR8006PowerModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 30)
)
if mibBuilder.loadTexts:
    rbnEntContainerSSR8006PowerModule.setStatus("current")
_RbnEntContainerSSR8006Data_ObjectIdentity = ObjectIdentity
rbnEntContainerSSR8006Data = _RbnEntContainerSSR8006Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 5, 31)
)
if mibBuilder.loadTexts:
    rbnEntContainerSSR8006Data.setStatus("current")
_RbnEntityTypePowerSupply_ObjectIdentity = ObjectIdentity
rbnEntityTypePowerSupply = _RbnEntityTypePowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 6)
)
if mibBuilder.loadTexts:
    rbnEntityTypePowerSupply.setStatus("current")
_RbnEntPowerSupplyUnknown_ObjectIdentity = ObjectIdentity
rbnEntPowerSupplyUnknown = _RbnEntPowerSupplyUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 6, 1)
)
if mibBuilder.loadTexts:
    rbnEntPowerSupplyUnknown.setStatus("current")
_RbnEntPowerSupplySMS1000AC_ObjectIdentity = ObjectIdentity
rbnEntPowerSupplySMS1000AC = _RbnEntPowerSupplySMS1000AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 6, 2)
)
if mibBuilder.loadTexts:
    rbnEntPowerSupplySMS1000AC.setStatus("current")
_RbnEntPowerSupplySMS1000DC_ObjectIdentity = ObjectIdentity
rbnEntPowerSupplySMS1000DC = _RbnEntPowerSupplySMS1000DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 6, 3)
)
if mibBuilder.loadTexts:
    rbnEntPowerSupplySMS1000DC.setStatus("current")
_RbnEntPowerSupplySMS500AC_ObjectIdentity = ObjectIdentity
rbnEntPowerSupplySMS500AC = _RbnEntPowerSupplySMS500AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 6, 4)
)
if mibBuilder.loadTexts:
    rbnEntPowerSupplySMS500AC.setStatus("current")
_RbnEntPowerSupplySMS500DC_ObjectIdentity = ObjectIdentity
rbnEntPowerSupplySMS500DC = _RbnEntPowerSupplySMS500DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 6, 5)
)
if mibBuilder.loadTexts:
    rbnEntPowerSupplySMS500DC.setStatus("current")
_RbnEntPowerSupplySMS1800AC_ObjectIdentity = ObjectIdentity
rbnEntPowerSupplySMS1800AC = _RbnEntPowerSupplySMS1800AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 6, 6)
)
if mibBuilder.loadTexts:
    rbnEntPowerSupplySMS1800AC.setStatus("current")
_RbnEntPowerSupplySMS1800DC_ObjectIdentity = ObjectIdentity
rbnEntPowerSupplySMS1800DC = _RbnEntPowerSupplySMS1800DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 6, 7)
)
if mibBuilder.loadTexts:
    rbnEntPowerSupplySMS1800DC.setStatus("current")
_RbnEntPowerModuleSSR_ObjectIdentity = ObjectIdentity
rbnEntPowerModuleSSR = _RbnEntPowerModuleSSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 6, 10)
)
if mibBuilder.loadTexts:
    rbnEntPowerModuleSSR.setStatus("current")
_RbnEntityTypeFan_ObjectIdentity = ObjectIdentity
rbnEntityTypeFan = _RbnEntityTypeFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 7)
)
if mibBuilder.loadTexts:
    rbnEntityTypeFan.setStatus("current")
_RbnEntFanSE800_ObjectIdentity = ObjectIdentity
rbnEntFanSE800 = _RbnEntFanSE800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 7, 1)
)
if mibBuilder.loadTexts:
    rbnEntFanSE800.setStatus("current")
_RbnEntFanSE400_ObjectIdentity = ObjectIdentity
rbnEntFanSE400 = _RbnEntFanSE400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 7, 2)
)
if mibBuilder.loadTexts:
    rbnEntFanSE400.setStatus("current")
_RbnEntFanSE1200_ObjectIdentity = ObjectIdentity
rbnEntFanSE1200 = _RbnEntFanSE1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 7, 3)
)
if mibBuilder.loadTexts:
    rbnEntFanSE1200.setStatus("current")
_RbnEntFanSM480_ObjectIdentity = ObjectIdentity
rbnEntFanSM480 = _RbnEntFanSM480_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 7, 4)
)
if mibBuilder.loadTexts:
    rbnEntFanSM480.setStatus("current")
_RbnEntFanSE600_ObjectIdentity = ObjectIdentity
rbnEntFanSE600 = _RbnEntFanSE600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 7, 5)
)
if mibBuilder.loadTexts:
    rbnEntFanSE600.setStatus("current")
_RbnEntFanSM240_ObjectIdentity = ObjectIdentity
rbnEntFanSM240 = _RbnEntFanSM240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 7, 6)
)
if mibBuilder.loadTexts:
    rbnEntFanSM240.setStatus("current")
_RbnEntFanSE1200H_ObjectIdentity = ObjectIdentity
rbnEntFanSE1200H = _RbnEntFanSE1200H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 7, 7)
)
if mibBuilder.loadTexts:
    rbnEntFanSE1200H.setStatus("current")
_RbnEntFanTraySSR_ObjectIdentity = ObjectIdentity
rbnEntFanTraySSR = _RbnEntFanTraySSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 7, 8)
)
if mibBuilder.loadTexts:
    rbnEntFanTraySSR.setStatus("current")
_RbnEntityTypeSensor_ObjectIdentity = ObjectIdentity
rbnEntityTypeSensor = _RbnEntityTypeSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 8)
)
if mibBuilder.loadTexts:
    rbnEntityTypeSensor.setStatus("current")
_RbnEntSensorAlarmSE400_ObjectIdentity = ObjectIdentity
rbnEntSensorAlarmSE400 = _RbnEntSensorAlarmSE400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 8, 1)
)
if mibBuilder.loadTexts:
    rbnEntSensorAlarmSE400.setStatus("current")
_RbnEntSensorAlarmSE600_ObjectIdentity = ObjectIdentity
rbnEntSensorAlarmSE600 = _RbnEntSensorAlarmSE600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 8, 2)
)
if mibBuilder.loadTexts:
    rbnEntSensorAlarmSE600.setStatus("current")
_RbnEntSensorAlarmSM240_ObjectIdentity = ObjectIdentity
rbnEntSensorAlarmSM240 = _RbnEntSensorAlarmSM240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 8, 3)
)
if mibBuilder.loadTexts:
    rbnEntSensorAlarmSM240.setStatus("current")
_RbnEntityTypeModule_ObjectIdentity = ObjectIdentity
rbnEntityTypeModule = _RbnEntityTypeModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9)
)
if mibBuilder.loadTexts:
    rbnEntityTypeModule.setStatus("current")
_RbnEntModuleUnknown_ObjectIdentity = ObjectIdentity
rbnEntModuleUnknown = _RbnEntModuleUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 1)
)
if mibBuilder.loadTexts:
    rbnEntModuleUnknown.setStatus("current")
_RbnEntModuleSMSAIMOC3_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSAIMOC3 = _RbnEntModuleSMSAIMOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 3)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSAIMOC3.setStatus("current")
_RbnEntModuleSMSAIMDS3_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSAIMDS3 = _RbnEntModuleSMSAIMDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 4)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSAIMDS3.setStatus("current")
_RbnEntModuleSMSAIME3_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSAIME3 = _RbnEntModuleSMSAIME3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 5)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSAIME3.setStatus("current")
_RbnEntModuleSMSEIM_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSEIM = _RbnEntModuleSMSEIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 6)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSEIM.setStatus("current")
_RbnEntModuleSMSPIMDS3_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSPIMDS3 = _RbnEntModuleSMSPIMDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 7)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSPIMDS3.setStatus("current")
_RbnEntModuleSMSPIME3_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSPIME3 = _RbnEntModuleSMSPIME3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 8)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSPIME3.setStatus("current")
_RbnEntModuleSMSPIMHSSI_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSPIMHSSI = _RbnEntModuleSMSPIMHSSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 9)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSPIMHSSI.setStatus("current")
_RbnEntModuleSMSFE1_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSFE1 = _RbnEntModuleSMSFE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 10)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSFE1.setStatus("current")
_RbnEntModuleSMSFE2_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSFE2 = _RbnEntModuleSMSFE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 12)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSFE2.setStatus("current")
_RbnEntModuleSMSPIMDS1_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSPIMDS1 = _RbnEntModuleSMSPIMDS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 14)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSPIMDS1.setStatus("current")
_RbnEntModuleSMSPIMCDS3_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSPIMCDS3 = _RbnEntModuleSMSPIMCDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 15)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSPIMCDS3.setStatus("current")
_RbnEntModuleSMSCE1_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSCE1 = _RbnEntModuleSMSCE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 16)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSCE1.setStatus("current")
_RbnEntModuleSMSCE2_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSCE2 = _RbnEntModuleSMSCE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 17)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSCE2.setStatus("current")
_RbnEntModuleSMSCE3_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSCE3 = _RbnEntModuleSMSCE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 18)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSCE3.setStatus("current")
_RbnEntModuleSMSAIMT1_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSAIMT1 = _RbnEntModuleSMSAIMT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 20)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSAIMT1.setStatus("current")
_RbnEntModuleSMSPIME1_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSPIME1 = _RbnEntModuleSMSPIME1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 22)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSPIME1.setStatus("current")
_RbnEntModuleSMSAIME1_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSAIME1 = _RbnEntModuleSMSAIME1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 23)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSAIME1.setStatus("current")
_RbnEntModuleSMSPOSOC3_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSPOSOC3 = _RbnEntModuleSMSPOSOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 24)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSPOSOC3.setStatus("current")
_RbnEntModuleSMSPOSOC12_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSPOSOC12 = _RbnEntModuleSMSPOSOC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 25)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSPOSOC12.setStatus("current")
_RbnEntModuleSMSGIGEIM_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSGIGEIM = _RbnEntModuleSMSGIGEIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 26)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSGIGEIM.setStatus("current")
_RbnEntModuleSMSAIMOC12_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSAIMOC12 = _RbnEntModuleSMSAIMOC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 27)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSAIMOC12.setStatus("current")
_RbnEntModuleSMSIPSEC_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSIPSEC = _RbnEntModuleSMSIPSEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 28)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSIPSEC.setStatus("current")
_RbnEntModuleSMSFABRIC_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSFABRIC = _RbnEntModuleSMSFABRIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 29)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSFABRIC.setStatus("current")
_RbnEntModuleSMSCM_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSCM = _RbnEntModuleSMSCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 30)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSCM.setStatus("current")
_RbnEntModuleSMSTIMING_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSTIMING = _RbnEntModuleSMSTIMING_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 31)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSTIMING.setStatus("current")
_RbnEntModuleSMSSM_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSSM = _RbnEntModuleSMSSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 32)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSSM.setStatus("current")
_RbnEntModuleSMSFE3_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSFE3 = _RbnEntModuleSMSFE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 35)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSFE3.setStatus("current")
_RbnEntModuleSMSXFE_ObjectIdentity = ObjectIdentity
rbnEntModuleSMSXFE = _RbnEntModuleSMSXFE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 40)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMSXFE.setStatus("current")
_RbnEntModuleSEXC_ObjectIdentity = ObjectIdentity
rbnEntModuleSEXC = _RbnEntModuleSEXC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 41)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEXC.setStatus("current")
_RbnEntModuleSEEIM_ObjectIdentity = ObjectIdentity
rbnEntModuleSEEIM = _RbnEntModuleSEEIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 42)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEEIM.setStatus("current")
_RbnEntModuleSEGIGEIM_ObjectIdentity = ObjectIdentity
rbnEntModuleSEGIGEIM = _RbnEntModuleSEGIGEIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 43)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEGIGEIM.setStatus("current")
_RbnEntModuleSEPOSOC12_ObjectIdentity = ObjectIdentity
rbnEntModuleSEPOSOC12 = _RbnEntModuleSEPOSOC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 44)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEPOSOC12.setStatus("current")
_RbnEntModuleSEPOSOC48_ObjectIdentity = ObjectIdentity
rbnEntModuleSEPOSOC48 = _RbnEntModuleSEPOSOC48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 45)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEPOSOC48.setStatus("current")
_RbnEntModuleSEPOSOC3_ObjectIdentity = ObjectIdentity
rbnEntModuleSEPOSOC3 = _RbnEntModuleSEPOSOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 46)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEPOSOC3.setStatus("current")
_RbnEntModuleSECHOC12DS1_ObjectIdentity = ObjectIdentity
rbnEntModuleSECHOC12DS1 = _RbnEntModuleSECHOC12DS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 47)
)
if mibBuilder.loadTexts:
    rbnEntModuleSECHOC12DS1.setStatus("current")
_RbnEntModuleSECHOC12DS3_ObjectIdentity = ObjectIdentity
rbnEntModuleSECHOC12DS3 = _RbnEntModuleSECHOC12DS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 48)
)
if mibBuilder.loadTexts:
    rbnEntModuleSECHOC12DS3.setStatus("current")
_RbnEntModuleSEAIMOC3_ObjectIdentity = ObjectIdentity
rbnEntModuleSEAIMOC3 = _RbnEntModuleSEAIMOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 49)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEAIMOC3.setStatus("current")
_RbnEntModuleSEAIMOC12_ObjectIdentity = ObjectIdentity
rbnEntModuleSEAIMOC12 = _RbnEntModuleSEAIMOC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 50)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEAIMOC12.setStatus("current")
_RbnEntModuleSECHDS3_ObjectIdentity = ObjectIdentity
rbnEntModuleSECHDS3 = _RbnEntModuleSECHDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 51)
)
if mibBuilder.loadTexts:
    rbnEntModuleSECHDS3.setStatus("current")
_RbnEntModuleSEDS3_ObjectIdentity = ObjectIdentity
rbnEntModuleSEDS3 = _RbnEntModuleSEDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 52)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEDS3.setStatus("current")
_RbnEntModuleSEAIMDS3_ObjectIdentity = ObjectIdentity
rbnEntModuleSEAIMDS3 = _RbnEntModuleSEAIMDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 53)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEAIMDS3.setStatus("current")
_RbnEntModuleSECHSTM1E1_ObjectIdentity = ObjectIdentity
rbnEntModuleSECHSTM1E1 = _RbnEntModuleSECHSTM1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 54)
)
if mibBuilder.loadTexts:
    rbnEntModuleSECHSTM1E1.setStatus("current")
_RbnEntModuleSEE1_ObjectIdentity = ObjectIdentity
rbnEntModuleSEE1 = _RbnEntModuleSEE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 55)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEE1.setStatus("current")
_RbnEntModuleSEXC3_ObjectIdentity = ObjectIdentity
rbnEntModuleSEXC3 = _RbnEntModuleSEXC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 56)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEXC3.setStatus("current")
_RbnEntModuleSEE3_ObjectIdentity = ObjectIdentity
rbnEntModuleSEE3 = _RbnEntModuleSEE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 57)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEE3.setStatus("current")
_RbnEntModuleSEAIMOC12E_ObjectIdentity = ObjectIdentity
rbnEntModuleSEAIMOC12E = _RbnEntModuleSEAIMOC12E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 58)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEAIMOC12E.setStatus("current")
_RbnEntModuleSEGIGETM_ObjectIdentity = ObjectIdentity
rbnEntModuleSEGIGETM = _RbnEntModuleSEGIGETM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 59)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEGIGETM.setStatus("current")
_RbnEntModuleSE10GIGEIM_ObjectIdentity = ObjectIdentity
rbnEntModuleSE10GIGEIM = _RbnEntModuleSE10GIGEIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 60)
)
if mibBuilder.loadTexts:
    rbnEntModuleSE10GIGEIM.setStatus("current")
_RbnEntModuleSE100XC_ObjectIdentity = ObjectIdentity
rbnEntModuleSE100XC = _RbnEntModuleSE100XC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 61)
)
if mibBuilder.loadTexts:
    rbnEntModuleSE100XC.setStatus("current")
_RbnEntModuleSE100EMIC_ObjectIdentity = ObjectIdentity
rbnEntModuleSE100EMIC = _RbnEntModuleSE100EMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 62)
)
if mibBuilder.loadTexts:
    rbnEntModuleSE100EMIC.setStatus("current")
_RbnEntModuleSE100FXMIC_ObjectIdentity = ObjectIdentity
rbnEntModuleSE100FXMIC = _RbnEntModuleSE100FXMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 63)
)
if mibBuilder.loadTexts:
    rbnEntModuleSE100FXMIC.setStatus("current")
_RbnEntModuleSE100GERJMIC_ObjectIdentity = ObjectIdentity
rbnEntModuleSE100GERJMIC = _RbnEntModuleSE100GERJMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 64)
)
if mibBuilder.loadTexts:
    rbnEntModuleSE100GERJMIC.setStatus("current")
_RbnEntModuleSE100GEFXMIC_ObjectIdentity = ObjectIdentity
rbnEntModuleSE100GEFXMIC = _RbnEntModuleSE100GEFXMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 65)
)
if mibBuilder.loadTexts:
    rbnEntModuleSE100GEFXMIC.setStatus("current")
_RbnEntModuleSEXC4_ObjectIdentity = ObjectIdentity
rbnEntModuleSEXC4 = _RbnEntModuleSEXC4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 66)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEXC4.setStatus("current")
_RbnEntModuleSE100AIMOC3MIC_ObjectIdentity = ObjectIdentity
rbnEntModuleSE100AIMOC3MIC = _RbnEntModuleSE100AIMOC3MIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 67)
)
if mibBuilder.loadTexts:
    rbnEntModuleSE100AIMOC3MIC.setStatus("current")
_RbnEntModuleSEASE_ObjectIdentity = ObjectIdentity
rbnEntModuleSEASE = _RbnEntModuleSEASE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 68)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEASE.setStatus("current")
_RbnEntModuleSEFE60GE2_ObjectIdentity = ObjectIdentity
rbnEntModuleSEFE60GE2 = _RbnEntModuleSEFE60GE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 69)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEFE60GE2.setStatus("current")
_RbnEntModuleSEPOSOC192_ObjectIdentity = ObjectIdentity
rbnEntModuleSEPOSOC192 = _RbnEntModuleSEPOSOC192_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 70)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEPOSOC192.setStatus("current")
_RbnEntModuleSE5PortGIGE_ObjectIdentity = ObjectIdentity
rbnEntModuleSE5PortGIGE = _RbnEntModuleSE5PortGIGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 71)
)
if mibBuilder.loadTexts:
    rbnEntModuleSE5PortGIGE.setStatus("current")
_RbnEntModuleSE20PortGIGE_ObjectIdentity = ObjectIdentity
rbnEntModuleSE20PortGIGE = _RbnEntModuleSE20PortGIGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 72)
)
if mibBuilder.loadTexts:
    rbnEntModuleSE20PortGIGE.setStatus("current")
_RbnEntModuleSE4Port10GIGE_ObjectIdentity = ObjectIdentity
rbnEntModuleSE4Port10GIGE = _RbnEntModuleSE4Port10GIGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 73)
)
if mibBuilder.loadTexts:
    rbnEntModuleSE4Port10GIGE.setStatus("current")
_RbnEntModuleSE10GIGETM_ObjectIdentity = ObjectIdentity
rbnEntModuleSE10GIGETM = _RbnEntModuleSE10GIGETM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 74)
)
if mibBuilder.loadTexts:
    rbnEntModuleSE10GIGETM.setStatus("current")
_RbnEntModuleSESSE_ObjectIdentity = ObjectIdentity
rbnEntModuleSESSE = _RbnEntModuleSESSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 75)
)
if mibBuilder.loadTexts:
    rbnEntModuleSESSE.setStatus("current")
_RbnEntModuleSE10PortGIGEDDR2_ObjectIdentity = ObjectIdentity
rbnEntModuleSE10PortGIGEDDR2 = _RbnEntModuleSE10PortGIGEDDR2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 76)
)
if mibBuilder.loadTexts:
    rbnEntModuleSE10PortGIGEDDR2.setStatus("current")
_RbnEntModuleSE4PortOC48_ObjectIdentity = ObjectIdentity
rbnEntModuleSE4PortOC48 = _RbnEntModuleSE4PortOC48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 77)
)
if mibBuilder.loadTexts:
    rbnEntModuleSE4PortOC48.setStatus("current")
_RbnEntModuleSE8PortOC3_ObjectIdentity = ObjectIdentity
rbnEntModuleSE8PortOC3 = _RbnEntModuleSE8PortOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 78)
)
if mibBuilder.loadTexts:
    rbnEntModuleSE8PortOC3.setStatus("current")
_RbnEntModuleSE8OR2PORTCHOC3OC12_ObjectIdentity = ObjectIdentity
rbnEntModuleSE8OR2PORTCHOC3OC12 = _RbnEntModuleSE8OR2PORTCHOC3OC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 79)
)
if mibBuilder.loadTexts:
    rbnEntModuleSE8OR2PORTCHOC3OC12.setStatus("current")
_RbnEntModuleSEASE2_ObjectIdentity = ObjectIdentity
rbnEntModuleSEASE2 = _RbnEntModuleSEASE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 80)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEASE2.setStatus("current")
_RbnEntModuleSE1Port10GEOC192_ObjectIdentity = ObjectIdentity
rbnEntModuleSE1Port10GEOC192 = _RbnEntModuleSE1Port10GEOC192_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 81)
)
if mibBuilder.loadTexts:
    rbnEntModuleSE1Port10GEOC192.setStatus("current")
_RbnEntModuleSEPos8xOC3_ObjectIdentity = ObjectIdentity
rbnEntModuleSEPos8xOC3 = _RbnEntModuleSEPos8xOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 82)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEPos8xOC3.setStatus("current")
_RbnEntModuleSEPos4xOC12_ObjectIdentity = ObjectIdentity
rbnEntModuleSEPos4xOC12 = _RbnEntModuleSEPos4xOC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 83)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEPos4xOC12.setStatus("current")
_RbnEntModuleSEAtm2xOC12_ObjectIdentity = ObjectIdentity
rbnEntModuleSEAtm2xOC12 = _RbnEntModuleSEAtm2xOC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 84)
)
if mibBuilder.loadTexts:
    rbnEntModuleSEAtm2xOC12.setStatus("current")
_RbnEntModuleSM10GIGEIM_ObjectIdentity = ObjectIdentity
rbnEntModuleSM10GIGEIM = _RbnEntModuleSM10GIGEIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 101)
)
if mibBuilder.loadTexts:
    rbnEntModuleSM10GIGEIM.setStatus("current")
_RbnEntModuleSMRP2_ObjectIdentity = ObjectIdentity
rbnEntModuleSMRP2 = _RbnEntModuleSMRP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 102)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMRP2.setStatus("current")
_RbnEntModuleSMGIGEIM_ObjectIdentity = ObjectIdentity
rbnEntModuleSMGIGEIM = _RbnEntModuleSMGIGEIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 104)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMGIGEIM.setStatus("current")
_RbnEntModuleSMGIGETM_ObjectIdentity = ObjectIdentity
rbnEntModuleSMGIGETM = _RbnEntModuleSMGIGETM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 105)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMGIGETM.setStatus("current")
_RbnEntModuleSM10GIGETM_ObjectIdentity = ObjectIdentity
rbnEntModuleSM10GIGETM = _RbnEntModuleSM10GIGETM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 106)
)
if mibBuilder.loadTexts:
    rbnEntModuleSM10GIGETM.setStatus("current")
_RbnEntModuleSMFE60GE2_ObjectIdentity = ObjectIdentity
rbnEntModuleSMFE60GE2 = _RbnEntModuleSMFE60GE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 107)
)
if mibBuilder.loadTexts:
    rbnEntModuleSMFE60GE2.setStatus("current")
_RbnEntModuleSM20PortGIGE_ObjectIdentity = ObjectIdentity
rbnEntModuleSM20PortGIGE = _RbnEntModuleSM20PortGIGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 108)
)
if mibBuilder.loadTexts:
    rbnEntModuleSM20PortGIGE.setStatus("current")
_RbnEntModuleSM4Port10GIGE_ObjectIdentity = ObjectIdentity
rbnEntModuleSM4Port10GIGE = _RbnEntModuleSM4Port10GIGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 109)
)
if mibBuilder.loadTexts:
    rbnEntModuleSM4Port10GIGE.setStatus("current")
_RbnEntModuleSM10PortGIGEDDR2_ObjectIdentity = ObjectIdentity
rbnEntModuleSM10PortGIGEDDR2 = _RbnEntModuleSM10PortGIGEDDR2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 110)
)
if mibBuilder.loadTexts:
    rbnEntModuleSM10PortGIGEDDR2.setStatus("current")
_RbnEntModuleSM1Port10GEOC192_ObjectIdentity = ObjectIdentity
rbnEntModuleSM1Port10GEOC192 = _RbnEntModuleSM1Port10GEOC192_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 111)
)
if mibBuilder.loadTexts:
    rbnEntModuleSM1Port10GEOC192.setStatus("current")
_RbnEntModuleSM8OR2PORTCHOC3OC12_ObjectIdentity = ObjectIdentity
rbnEntModuleSM8OR2PORTCHOC3OC12 = _RbnEntModuleSM8OR2PORTCHOC3OC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 112)
)
if mibBuilder.loadTexts:
    rbnEntModuleSM8OR2PORTCHOC3OC12.setStatus("current")
_RbnEntModuleSSRALSW_ObjectIdentity = ObjectIdentity
rbnEntModuleSSRALSW = _RbnEntModuleSSRALSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 201)
)
if mibBuilder.loadTexts:
    rbnEntModuleSSRALSW.setStatus("current")
_RbnEntModuleSSRRPSW_ObjectIdentity = ObjectIdentity
rbnEntModuleSSRRPSW = _RbnEntModuleSSRRPSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 202)
)
if mibBuilder.loadTexts:
    rbnEntModuleSSRRPSW.setStatus("current")
_RbnEntModuleSSRSW_ObjectIdentity = ObjectIdentity
rbnEntModuleSSRSW = _RbnEntModuleSSRSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 203)
)
if mibBuilder.loadTexts:
    rbnEntModuleSSRSW.setStatus("current")
_RbnEntModuleSSR40Port1GE_ObjectIdentity = ObjectIdentity
rbnEntModuleSSR40Port1GE = _RbnEntModuleSSR40Port1GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 204)
)
if mibBuilder.loadTexts:
    rbnEntModuleSSR40Port1GE.setStatus("current")
_RbnEntModuleSSR10Port10GE_ObjectIdentity = ObjectIdentity
rbnEntModuleSSR10Port10GE = _RbnEntModuleSSR10Port10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 205)
)
if mibBuilder.loadTexts:
    rbnEntModuleSSR10Port10GE.setStatus("current")
_RbnEntModuleSSC1_ObjectIdentity = ObjectIdentity
rbnEntModuleSSC1 = _RbnEntModuleSSC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 207)
)
if mibBuilder.loadTexts:
    rbnEntModuleSSC1.setStatus("current")
_RbnEntModuleSSR2Port40GEor100GE_ObjectIdentity = ObjectIdentity
rbnEntModuleSSR2Port40GEor100GE = _RbnEntModuleSSR2Port40GEor100GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 9, 210)
)
if mibBuilder.loadTexts:
    rbnEntModuleSSR2Port40GEor100GE.setStatus("current")
_RbnEntityTypePort_ObjectIdentity = ObjectIdentity
rbnEntityTypePort = _RbnEntityTypePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10)
)
if mibBuilder.loadTexts:
    rbnEntityTypePort.setStatus("current")
_RbnEntPortUnknown_ObjectIdentity = ObjectIdentity
rbnEntPortUnknown = _RbnEntPortUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 1)
)
if mibBuilder.loadTexts:
    rbnEntPortUnknown.setStatus("current")
_RbnEntPortSMSAIMOC3_ObjectIdentity = ObjectIdentity
rbnEntPortSMSAIMOC3 = _RbnEntPortSMSAIMOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 3)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSAIMOC3.setStatus("current")
_RbnEntPortSMSAIMDS3_ObjectIdentity = ObjectIdentity
rbnEntPortSMSAIMDS3 = _RbnEntPortSMSAIMDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 4)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSAIMDS3.setStatus("current")
_RbnEntPortSMSAIME3_ObjectIdentity = ObjectIdentity
rbnEntPortSMSAIME3 = _RbnEntPortSMSAIME3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 5)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSAIME3.setStatus("current")
_RbnEntPortSMSEIM_ObjectIdentity = ObjectIdentity
rbnEntPortSMSEIM = _RbnEntPortSMSEIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 6)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSEIM.setStatus("current")
_RbnEntPortSMSPIMDS3_ObjectIdentity = ObjectIdentity
rbnEntPortSMSPIMDS3 = _RbnEntPortSMSPIMDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 7)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSPIMDS3.setStatus("current")
_RbnEntPortSMSPIME3_ObjectIdentity = ObjectIdentity
rbnEntPortSMSPIME3 = _RbnEntPortSMSPIME3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 8)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSPIME3.setStatus("current")
_RbnEntPortSMSPIMHSSI_ObjectIdentity = ObjectIdentity
rbnEntPortSMSPIMHSSI = _RbnEntPortSMSPIMHSSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 9)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSPIMHSSI.setStatus("current")
_RbnEntPortSMSPIMDS1_ObjectIdentity = ObjectIdentity
rbnEntPortSMSPIMDS1 = _RbnEntPortSMSPIMDS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 14)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSPIMDS1.setStatus("current")
_RbnEntPortSMSPIMCDS3_ObjectIdentity = ObjectIdentity
rbnEntPortSMSPIMCDS3 = _RbnEntPortSMSPIMCDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 15)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSPIMCDS3.setStatus("current")
_RbnEntPortSMSCE1MGMT_ObjectIdentity = ObjectIdentity
rbnEntPortSMSCE1MGMT = _RbnEntPortSMSCE1MGMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 16)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSCE1MGMT.setStatus("current")
_RbnEntPortSMSCE2MGMT_ObjectIdentity = ObjectIdentity
rbnEntPortSMSCE2MGMT = _RbnEntPortSMSCE2MGMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 17)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSCE2MGMT.setStatus("current")
_RbnEntPortSMSCE3MGMT_ObjectIdentity = ObjectIdentity
rbnEntPortSMSCE3MGMT = _RbnEntPortSMSCE3MGMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 18)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSCE3MGMT.setStatus("current")
_RbnEntPortSMSAIMT1_ObjectIdentity = ObjectIdentity
rbnEntPortSMSAIMT1 = _RbnEntPortSMSAIMT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 20)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSAIMT1.setStatus("current")
_RbnEntPortSMSPIME1_ObjectIdentity = ObjectIdentity
rbnEntPortSMSPIME1 = _RbnEntPortSMSPIME1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 22)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSPIME1.setStatus("current")
_RbnEntPortSMSAIME1_ObjectIdentity = ObjectIdentity
rbnEntPortSMSAIME1 = _RbnEntPortSMSAIME1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 23)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSAIME1.setStatus("current")
_RbnEntPortSMSPOSOC3_ObjectIdentity = ObjectIdentity
rbnEntPortSMSPOSOC3 = _RbnEntPortSMSPOSOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 24)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSPOSOC3.setStatus("current")
_RbnEntPortSMSPOSOC12_ObjectIdentity = ObjectIdentity
rbnEntPortSMSPOSOC12 = _RbnEntPortSMSPOSOC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 25)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSPOSOC12.setStatus("current")
_RbnEntPortSMSGIGEIM_ObjectIdentity = ObjectIdentity
rbnEntPortSMSGIGEIM = _RbnEntPortSMSGIGEIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 26)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSGIGEIM.setStatus("current")
_RbnEntPortSMSAIMOC12_ObjectIdentity = ObjectIdentity
rbnEntPortSMSAIMOC12 = _RbnEntPortSMSAIMOC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 27)
)
if mibBuilder.loadTexts:
    rbnEntPortSMSAIMOC12.setStatus("current")
_RbnEntPortSEXCMGMT_ObjectIdentity = ObjectIdentity
rbnEntPortSEXCMGMT = _RbnEntPortSEXCMGMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 41)
)
if mibBuilder.loadTexts:
    rbnEntPortSEXCMGMT.setStatus("current")
_RbnEntPortSEEIM_ObjectIdentity = ObjectIdentity
rbnEntPortSEEIM = _RbnEntPortSEEIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 42)
)
if mibBuilder.loadTexts:
    rbnEntPortSEEIM.setStatus("current")
_RbnEntPortSEGIGEIM_ObjectIdentity = ObjectIdentity
rbnEntPortSEGIGEIM = _RbnEntPortSEGIGEIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 43)
)
if mibBuilder.loadTexts:
    rbnEntPortSEGIGEIM.setStatus("current")
_RbnEntPortSEPOSOC12_ObjectIdentity = ObjectIdentity
rbnEntPortSEPOSOC12 = _RbnEntPortSEPOSOC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 44)
)
if mibBuilder.loadTexts:
    rbnEntPortSEPOSOC12.setStatus("current")
_RbnEntPortSEPOSOC48_ObjectIdentity = ObjectIdentity
rbnEntPortSEPOSOC48 = _RbnEntPortSEPOSOC48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 45)
)
if mibBuilder.loadTexts:
    rbnEntPortSEPOSOC48.setStatus("current")
_RbnEntPortSEPOSOC3_ObjectIdentity = ObjectIdentity
rbnEntPortSEPOSOC3 = _RbnEntPortSEPOSOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 46)
)
if mibBuilder.loadTexts:
    rbnEntPortSEPOSOC3.setStatus("current")
_RbnEntPortSECHOC12DS1_ObjectIdentity = ObjectIdentity
rbnEntPortSECHOC12DS1 = _RbnEntPortSECHOC12DS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 47)
)
if mibBuilder.loadTexts:
    rbnEntPortSECHOC12DS1.setStatus("current")
_RbnEntPortSECHOC12DS3_ObjectIdentity = ObjectIdentity
rbnEntPortSECHOC12DS3 = _RbnEntPortSECHOC12DS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 48)
)
if mibBuilder.loadTexts:
    rbnEntPortSECHOC12DS3.setStatus("current")
_RbnEntPortSEAIMOC3_ObjectIdentity = ObjectIdentity
rbnEntPortSEAIMOC3 = _RbnEntPortSEAIMOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 49)
)
if mibBuilder.loadTexts:
    rbnEntPortSEAIMOC3.setStatus("current")
_RbnEntPortSEAIMOC12_ObjectIdentity = ObjectIdentity
rbnEntPortSEAIMOC12 = _RbnEntPortSEAIMOC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 50)
)
if mibBuilder.loadTexts:
    rbnEntPortSEAIMOC12.setStatus("current")
_RbnEntPortSECHDS3_ObjectIdentity = ObjectIdentity
rbnEntPortSECHDS3 = _RbnEntPortSECHDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 51)
)
if mibBuilder.loadTexts:
    rbnEntPortSECHDS3.setStatus("current")
_RbnEntPortSEDS3_ObjectIdentity = ObjectIdentity
rbnEntPortSEDS3 = _RbnEntPortSEDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 52)
)
if mibBuilder.loadTexts:
    rbnEntPortSEDS3.setStatus("current")
_RbnEntPortSEAIMDS3_ObjectIdentity = ObjectIdentity
rbnEntPortSEAIMDS3 = _RbnEntPortSEAIMDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 53)
)
if mibBuilder.loadTexts:
    rbnEntPortSEAIMDS3.setStatus("current")
_RbnEntPortSECHSTM1E1_ObjectIdentity = ObjectIdentity
rbnEntPortSECHSTM1E1 = _RbnEntPortSECHSTM1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 54)
)
if mibBuilder.loadTexts:
    rbnEntPortSECHSTM1E1.setStatus("current")
_RbnEntPortSEE1_ObjectIdentity = ObjectIdentity
rbnEntPortSEE1 = _RbnEntPortSEE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 55)
)
if mibBuilder.loadTexts:
    rbnEntPortSEE1.setStatus("current")
_RbnEntPortSEXC3MGMT_ObjectIdentity = ObjectIdentity
rbnEntPortSEXC3MGMT = _RbnEntPortSEXC3MGMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 56)
)
if mibBuilder.loadTexts:
    rbnEntPortSEXC3MGMT.setStatus("current")
_RbnEntPortSEE3_ObjectIdentity = ObjectIdentity
rbnEntPortSEE3 = _RbnEntPortSEE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 57)
)
if mibBuilder.loadTexts:
    rbnEntPortSEE3.setStatus("current")
_RbnEntPortSEAIMOC12E_ObjectIdentity = ObjectIdentity
rbnEntPortSEAIMOC12E = _RbnEntPortSEAIMOC12E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 58)
)
if mibBuilder.loadTexts:
    rbnEntPortSEAIMOC12E.setStatus("current")
_RbnEntPortSEGIGETM_ObjectIdentity = ObjectIdentity
rbnEntPortSEGIGETM = _RbnEntPortSEGIGETM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 59)
)
if mibBuilder.loadTexts:
    rbnEntPortSEGIGETM.setStatus("current")
_RbnEntPortSE10GIGEIM_ObjectIdentity = ObjectIdentity
rbnEntPortSE10GIGEIM = _RbnEntPortSE10GIGEIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 60)
)
if mibBuilder.loadTexts:
    rbnEntPortSE10GIGEIM.setStatus("current")
_RbnEntPortSE100XCMGMT_ObjectIdentity = ObjectIdentity
rbnEntPortSE100XCMGMT = _RbnEntPortSE100XCMGMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 61)
)
if mibBuilder.loadTexts:
    rbnEntPortSE100XCMGMT.setStatus("current")
_RbnEntPortSE100EIM_ObjectIdentity = ObjectIdentity
rbnEntPortSE100EIM = _RbnEntPortSE100EIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 62)
)
if mibBuilder.loadTexts:
    rbnEntPortSE100EIM.setStatus("current")
_RbnEntPortSE100FXIM_ObjectIdentity = ObjectIdentity
rbnEntPortSE100FXIM = _RbnEntPortSE100FXIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 63)
)
if mibBuilder.loadTexts:
    rbnEntPortSE100FXIM.setStatus("current")
_RbnEntPortSE100GERJIM_ObjectIdentity = ObjectIdentity
rbnEntPortSE100GERJIM = _RbnEntPortSE100GERJIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 64)
)
if mibBuilder.loadTexts:
    rbnEntPortSE100GERJIM.setStatus("current")
_RbnEntPortSE100GEFXIM_ObjectIdentity = ObjectIdentity
rbnEntPortSE100GEFXIM = _RbnEntPortSE100GEFXIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 65)
)
if mibBuilder.loadTexts:
    rbnEntPortSE100GEFXIM.setStatus("current")
_RbnEntPortSEXC4MGMT_ObjectIdentity = ObjectIdentity
rbnEntPortSEXC4MGMT = _RbnEntPortSEXC4MGMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 66)
)
if mibBuilder.loadTexts:
    rbnEntPortSEXC4MGMT.setStatus("current")
_RbnEntPortSE100AIMOC3_ObjectIdentity = ObjectIdentity
rbnEntPortSE100AIMOC3 = _RbnEntPortSE100AIMOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 67)
)
if mibBuilder.loadTexts:
    rbnEntPortSE100AIMOC3.setStatus("current")
_RbnEntPortSEPOSOC192_ObjectIdentity = ObjectIdentity
rbnEntPortSEPOSOC192 = _RbnEntPortSEPOSOC192_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 68)
)
if mibBuilder.loadTexts:
    rbnEntPortSEPOSOC192.setStatus("current")
_RbnEntPortSE10GIGETM_ObjectIdentity = ObjectIdentity
rbnEntPortSE10GIGETM = _RbnEntPortSE10GIGETM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 69)
)
if mibBuilder.loadTexts:
    rbnEntPortSE10GIGETM.setStatus("current")
_RbnEntPortSECHOC3OC12_ObjectIdentity = ObjectIdentity
rbnEntPortSECHOC3OC12 = _RbnEntPortSECHOC3OC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 70)
)
if mibBuilder.loadTexts:
    rbnEntPortSECHOC3OC12.setStatus("current")
_RbnEntPortSECHOC3_ObjectIdentity = ObjectIdentity
rbnEntPortSECHOC3 = _RbnEntPortSECHOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 71)
)
if mibBuilder.loadTexts:
    rbnEntPortSECHOC3.setStatus("current")
_RbnEntPortSM10GIGEIM_ObjectIdentity = ObjectIdentity
rbnEntPortSM10GIGEIM = _RbnEntPortSM10GIGEIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 101)
)
if mibBuilder.loadTexts:
    rbnEntPortSM10GIGEIM.setStatus("current")
_RbnEntPortSMRPMGMT_ObjectIdentity = ObjectIdentity
rbnEntPortSMRPMGMT = _RbnEntPortSMRPMGMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 103)
)
if mibBuilder.loadTexts:
    rbnEntPortSMRPMGMT.setStatus("current")
_RbnEntPortSMGIGEIM_ObjectIdentity = ObjectIdentity
rbnEntPortSMGIGEIM = _RbnEntPortSMGIGEIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 104)
)
if mibBuilder.loadTexts:
    rbnEntPortSMGIGEIM.setStatus("current")
_RbnEntPortSMGIGETM_ObjectIdentity = ObjectIdentity
rbnEntPortSMGIGETM = _RbnEntPortSMGIGETM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 105)
)
if mibBuilder.loadTexts:
    rbnEntPortSMGIGETM.setStatus("current")
_RbnEntPortSM10GIGETM_ObjectIdentity = ObjectIdentity
rbnEntPortSM10GIGETM = _RbnEntPortSM10GIGETM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 106)
)
if mibBuilder.loadTexts:
    rbnEntPortSM10GIGETM.setStatus("current")
_RbnEntPortSMEIM_ObjectIdentity = ObjectIdentity
rbnEntPortSMEIM = _RbnEntPortSMEIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 107)
)
if mibBuilder.loadTexts:
    rbnEntPortSMEIM.setStatus("current")
_RbnEntPortSMCHOC3OC12_ObjectIdentity = ObjectIdentity
rbnEntPortSMCHOC3OC12 = _RbnEntPortSMCHOC3OC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 108)
)
if mibBuilder.loadTexts:
    rbnEntPortSMCHOC3OC12.setStatus("current")
_RbnEntPortSMCHOC3_ObjectIdentity = ObjectIdentity
rbnEntPortSMCHOC3 = _RbnEntPortSMCHOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 109)
)
if mibBuilder.loadTexts:
    rbnEntPortSMCHOC3.setStatus("current")
_RbnEntPortSSR1GE_ObjectIdentity = ObjectIdentity
rbnEntPortSSR1GE = _RbnEntPortSSR1GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 201)
)
if mibBuilder.loadTexts:
    rbnEntPortSSR1GE.setStatus("current")
_RbnEntPortSSR10GE_ObjectIdentity = ObjectIdentity
rbnEntPortSSR10GE = _RbnEntPortSSR10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 202)
)
if mibBuilder.loadTexts:
    rbnEntPortSSR10GE.setStatus("current")
_RbnEntPortSSRRPSWMgmt_ObjectIdentity = ObjectIdentity
rbnEntPortSSRRPSWMgmt = _RbnEntPortSSRRPSWMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 203)
)
if mibBuilder.loadTexts:
    rbnEntPortSSRRPSWMgmt.setStatus("current")
_RbnEntPortSSR100GE_ObjectIdentity = ObjectIdentity
rbnEntPortSSR100GE = _RbnEntPortSSR100GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 204)
)
if mibBuilder.loadTexts:
    rbnEntPortSSR100GE.setStatus("current")
_RbnEntPortSSR40GE_ObjectIdentity = ObjectIdentity
rbnEntPortSSR40GE = _RbnEntPortSSR40GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 205)
)
if mibBuilder.loadTexts:
    rbnEntPortSSR40GE.setStatus("current")
_RbnEntPortSSR40GEor100GE_ObjectIdentity = ObjectIdentity
rbnEntPortSSR40GEor100GE = _RbnEntPortSSR40GEor100GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 10, 206)
)
if mibBuilder.loadTexts:
    rbnEntPortSSR40GEor100GE.setStatus("current")
_RbnEntityTypeStack_ObjectIdentity = ObjectIdentity
rbnEntityTypeStack = _RbnEntityTypeStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 11)
)
if mibBuilder.loadTexts:
    rbnEntityTypeStack.setStatus("current")
_RbnEntityTypeCPU_ObjectIdentity = ObjectIdentity
rbnEntityTypeCPU = _RbnEntityTypeCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 12)
)
if mibBuilder.loadTexts:
    rbnEntityTypeCPU.setStatus("current")
_RbnEntCpuUnknown_ObjectIdentity = ObjectIdentity
rbnEntCpuUnknown = _RbnEntCpuUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 12, 1)
)
if mibBuilder.loadTexts:
    rbnEntCpuUnknown.setStatus("current")
_RbnEntCpuOcteon_ObjectIdentity = ObjectIdentity
rbnEntCpuOcteon = _RbnEntCpuOcteon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 12, 2)
)
if mibBuilder.loadTexts:
    rbnEntCpuOcteon.setStatus("current")
_RbnEntityTypeDisk_ObjectIdentity = ObjectIdentity
rbnEntityTypeDisk = _RbnEntityTypeDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 13)
)
if mibBuilder.loadTexts:
    rbnEntityTypeDisk.setStatus("current")
_RbnEntDiskUnknown_ObjectIdentity = ObjectIdentity
rbnEntDiskUnknown = _RbnEntDiskUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 13, 1)
)
if mibBuilder.loadTexts:
    rbnEntDiskUnknown.setStatus("current")
_RbnEntDiskSSE_ObjectIdentity = ObjectIdentity
rbnEntDiskSSE = _RbnEntDiskSSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 13, 2)
)
if mibBuilder.loadTexts:
    rbnEntDiskSSE.setStatus("current")
_RbnEntityTypeMemory_ObjectIdentity = ObjectIdentity
rbnEntityTypeMemory = _RbnEntityTypeMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6, 14)
)
if mibBuilder.loadTexts:
    rbnEntityTypeMemory.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-PRODUCT-MIB",
    **{"rbnSMS1000": rbnSMS1000,
       "rbnSMS500": rbnSMS500,
       "rbnSMS1800": rbnSMS1800,
       "rbnSMS10000": rbnSMS10000,
       "rbnSmartEdge800": rbnSmartEdge800,
       "rbnSmartEdge400": rbnSmartEdge400,
       "rbnSmartEdge100": rbnSmartEdge100,
       "rbnSmartEdge1200": rbnSmartEdge1200,
       "rbnSM480": rbnSM480,
       "rbnSmartEdge600": rbnSmartEdge600,
       "rbnSM240": rbnSM240,
       "rbnSSR8020": rbnSSR8020,
       "rbnSSR8010": rbnSSR8010,
       "rbnSSR8006": rbnSSR8006,
       "rbnProductMIB": rbnProductMIB,
       "rbnEntityTypeOther": rbnEntityTypeOther,
       "rbnEntityTypeUnknown": rbnEntityTypeUnknown,
       "rbnEntityTypeChassis": rbnEntityTypeChassis,
       "rbnEntChassisSMS1000": rbnEntChassisSMS1000,
       "rbnEntChassisSMS500": rbnEntChassisSMS500,
       "rbnEntChassisSMS1800": rbnEntChassisSMS1800,
       "rbnEntChassisSMS10000": rbnEntChassisSMS10000,
       "rbnEntChassisSE800": rbnEntChassisSE800,
       "rbnEntChassisSE400": rbnEntChassisSE400,
       "rbnEntChassisSE100": rbnEntChassisSE100,
       "rbnEntChassisSE1200": rbnEntChassisSE1200,
       "rbnEntChassisSM480": rbnEntChassisSM480,
       "rbnEntChassisSE600": rbnEntChassisSE600,
       "rbnEntChassisSM240": rbnEntChassisSM240,
       "rbnEntChassisSE1200H": rbnEntChassisSE1200H,
       "rbnEntChassisSSR8020": rbnEntChassisSSR8020,
       "rbnEntChassisSSR8010": rbnEntChassisSSR8010,
       "rbnEntChassisSSR8006": rbnEntChassisSSR8006,
       "rbnEntityTypeBackplane": rbnEntityTypeBackplane,
       "rbnEntBackplaneSMS1000Data": rbnEntBackplaneSMS1000Data,
       "rbnEntBackplaneSMS1000Power": rbnEntBackplaneSMS1000Power,
       "rbnEntBackplaneSMS500Data": rbnEntBackplaneSMS500Data,
       "rbnEntBackplaneSMS500Power": rbnEntBackplaneSMS500Power,
       "rbnEntBackplaneSMS1800Data": rbnEntBackplaneSMS1800Data,
       "rbnEntBackplaneSMS1800Power": rbnEntBackplaneSMS1800Power,
       "rbnEntBackplaneSMS10000Midplane": rbnEntBackplaneSMS10000Midplane,
       "rbnEntBackplaneSE800Data": rbnEntBackplaneSE800Data,
       "rbnEntBackplaneSE400Data": rbnEntBackplaneSE400Data,
       "rbnEntBackplaneSE100Data": rbnEntBackplaneSE100Data,
       "rbnEntBackplaneSE1200Data": rbnEntBackplaneSE1200Data,
       "rbnEntBackplaneSM480Data": rbnEntBackplaneSM480Data,
       "rbnEntBackplaneSE600Data": rbnEntBackplaneSE600Data,
       "rbnEntBackplaneSM240Data": rbnEntBackplaneSM240Data,
       "rbnEntBackplaneSE1200HData": rbnEntBackplaneSE1200HData,
       "rbnEntBackplaneSSR8020Data": rbnEntBackplaneSSR8020Data,
       "rbnEntBackplaneSSR8010Data": rbnEntBackplaneSSR8010Data,
       "rbnEntBackplaneSSR8006Data": rbnEntBackplaneSSR8006Data,
       "rbnEntityTypeContainer": rbnEntityTypeContainer,
       "rbnEntContainerSMS1000Data": rbnEntContainerSMS1000Data,
       "rbnEntContainerSMS1000Power": rbnEntContainerSMS1000Power,
       "rbnEntContainerSMS500Data": rbnEntContainerSMS500Data,
       "rbnEntContainerSMS500Power": rbnEntContainerSMS500Power,
       "rbnEntContainerSMS1800Data": rbnEntContainerSMS1800Data,
       "rbnEntContainerSMS1800Power": rbnEntContainerSMS1800Power,
       "rbnEntContainerSMS10000Fabric": rbnEntContainerSMS10000Fabric,
       "rbnEntContainerSMS10000Timing": rbnEntContainerSMS10000Timing,
       "rbnEntContainerSMS10000SMCM": rbnEntContainerSMS10000SMCM,
       "rbnEntContainerSMS10000IO": rbnEntContainerSMS10000IO,
       "rbnEntContainerSE800Data": rbnEntContainerSE800Data,
       "rbnEntContainerSE400Data": rbnEntContainerSE400Data,
       "rbnEntContainerSE100Data": rbnEntContainerSE100Data,
       "rbnEntContainerSE100Carrier": rbnEntContainerSE100Carrier,
       "rbnEntContainerSE1200Data": rbnEntContainerSE1200Data,
       "rbnEntContainerSM480Data": rbnEntContainerSM480Data,
       "rbnEntContainerSE600Data": rbnEntContainerSE600Data,
       "rbnEntContainerSM240Data": rbnEntContainerSM240Data,
       "rbnEntContainerSE1200HData": rbnEntContainerSE1200HData,
       "rbnEntContainerSSR8020FanTray": rbnEntContainerSSR8020FanTray,
       "rbnEntContainerSSR8020PowerModule": rbnEntContainerSSR8020PowerModule,
       "rbnEntContainerSSR8020Data": rbnEntContainerSSR8020Data,
       "rbnEntContainerSSR8010FanTray": rbnEntContainerSSR8010FanTray,
       "rbnEntContainerSSR8010PowerModule": rbnEntContainerSSR8010PowerModule,
       "rbnEntContainerSSR8010Data": rbnEntContainerSSR8010Data,
       "rbnEntContainerSSR8006FanTray": rbnEntContainerSSR8006FanTray,
       "rbnEntContainerSSR8006PowerModule": rbnEntContainerSSR8006PowerModule,
       "rbnEntContainerSSR8006Data": rbnEntContainerSSR8006Data,
       "rbnEntityTypePowerSupply": rbnEntityTypePowerSupply,
       "rbnEntPowerSupplyUnknown": rbnEntPowerSupplyUnknown,
       "rbnEntPowerSupplySMS1000AC": rbnEntPowerSupplySMS1000AC,
       "rbnEntPowerSupplySMS1000DC": rbnEntPowerSupplySMS1000DC,
       "rbnEntPowerSupplySMS500AC": rbnEntPowerSupplySMS500AC,
       "rbnEntPowerSupplySMS500DC": rbnEntPowerSupplySMS500DC,
       "rbnEntPowerSupplySMS1800AC": rbnEntPowerSupplySMS1800AC,
       "rbnEntPowerSupplySMS1800DC": rbnEntPowerSupplySMS1800DC,
       "rbnEntPowerModuleSSR": rbnEntPowerModuleSSR,
       "rbnEntityTypeFan": rbnEntityTypeFan,
       "rbnEntFanSE800": rbnEntFanSE800,
       "rbnEntFanSE400": rbnEntFanSE400,
       "rbnEntFanSE1200": rbnEntFanSE1200,
       "rbnEntFanSM480": rbnEntFanSM480,
       "rbnEntFanSE600": rbnEntFanSE600,
       "rbnEntFanSM240": rbnEntFanSM240,
       "rbnEntFanSE1200H": rbnEntFanSE1200H,
       "rbnEntFanTraySSR": rbnEntFanTraySSR,
       "rbnEntityTypeSensor": rbnEntityTypeSensor,
       "rbnEntSensorAlarmSE400": rbnEntSensorAlarmSE400,
       "rbnEntSensorAlarmSE600": rbnEntSensorAlarmSE600,
       "rbnEntSensorAlarmSM240": rbnEntSensorAlarmSM240,
       "rbnEntityTypeModule": rbnEntityTypeModule,
       "rbnEntModuleUnknown": rbnEntModuleUnknown,
       "rbnEntModuleSMSAIMOC3": rbnEntModuleSMSAIMOC3,
       "rbnEntModuleSMSAIMDS3": rbnEntModuleSMSAIMDS3,
       "rbnEntModuleSMSAIME3": rbnEntModuleSMSAIME3,
       "rbnEntModuleSMSEIM": rbnEntModuleSMSEIM,
       "rbnEntModuleSMSPIMDS3": rbnEntModuleSMSPIMDS3,
       "rbnEntModuleSMSPIME3": rbnEntModuleSMSPIME3,
       "rbnEntModuleSMSPIMHSSI": rbnEntModuleSMSPIMHSSI,
       "rbnEntModuleSMSFE1": rbnEntModuleSMSFE1,
       "rbnEntModuleSMSFE2": rbnEntModuleSMSFE2,
       "rbnEntModuleSMSPIMDS1": rbnEntModuleSMSPIMDS1,
       "rbnEntModuleSMSPIMCDS3": rbnEntModuleSMSPIMCDS3,
       "rbnEntModuleSMSCE1": rbnEntModuleSMSCE1,
       "rbnEntModuleSMSCE2": rbnEntModuleSMSCE2,
       "rbnEntModuleSMSCE3": rbnEntModuleSMSCE3,
       "rbnEntModuleSMSAIMT1": rbnEntModuleSMSAIMT1,
       "rbnEntModuleSMSPIME1": rbnEntModuleSMSPIME1,
       "rbnEntModuleSMSAIME1": rbnEntModuleSMSAIME1,
       "rbnEntModuleSMSPOSOC3": rbnEntModuleSMSPOSOC3,
       "rbnEntModuleSMSPOSOC12": rbnEntModuleSMSPOSOC12,
       "rbnEntModuleSMSGIGEIM": rbnEntModuleSMSGIGEIM,
       "rbnEntModuleSMSAIMOC12": rbnEntModuleSMSAIMOC12,
       "rbnEntModuleSMSIPSEC": rbnEntModuleSMSIPSEC,
       "rbnEntModuleSMSFABRIC": rbnEntModuleSMSFABRIC,
       "rbnEntModuleSMSCM": rbnEntModuleSMSCM,
       "rbnEntModuleSMSTIMING": rbnEntModuleSMSTIMING,
       "rbnEntModuleSMSSM": rbnEntModuleSMSSM,
       "rbnEntModuleSMSFE3": rbnEntModuleSMSFE3,
       "rbnEntModuleSMSXFE": rbnEntModuleSMSXFE,
       "rbnEntModuleSEXC": rbnEntModuleSEXC,
       "rbnEntModuleSEEIM": rbnEntModuleSEEIM,
       "rbnEntModuleSEGIGEIM": rbnEntModuleSEGIGEIM,
       "rbnEntModuleSEPOSOC12": rbnEntModuleSEPOSOC12,
       "rbnEntModuleSEPOSOC48": rbnEntModuleSEPOSOC48,
       "rbnEntModuleSEPOSOC3": rbnEntModuleSEPOSOC3,
       "rbnEntModuleSECHOC12DS1": rbnEntModuleSECHOC12DS1,
       "rbnEntModuleSECHOC12DS3": rbnEntModuleSECHOC12DS3,
       "rbnEntModuleSEAIMOC3": rbnEntModuleSEAIMOC3,
       "rbnEntModuleSEAIMOC12": rbnEntModuleSEAIMOC12,
       "rbnEntModuleSECHDS3": rbnEntModuleSECHDS3,
       "rbnEntModuleSEDS3": rbnEntModuleSEDS3,
       "rbnEntModuleSEAIMDS3": rbnEntModuleSEAIMDS3,
       "rbnEntModuleSECHSTM1E1": rbnEntModuleSECHSTM1E1,
       "rbnEntModuleSEE1": rbnEntModuleSEE1,
       "rbnEntModuleSEXC3": rbnEntModuleSEXC3,
       "rbnEntModuleSEE3": rbnEntModuleSEE3,
       "rbnEntModuleSEAIMOC12E": rbnEntModuleSEAIMOC12E,
       "rbnEntModuleSEGIGETM": rbnEntModuleSEGIGETM,
       "rbnEntModuleSE10GIGEIM": rbnEntModuleSE10GIGEIM,
       "rbnEntModuleSE100XC": rbnEntModuleSE100XC,
       "rbnEntModuleSE100EMIC": rbnEntModuleSE100EMIC,
       "rbnEntModuleSE100FXMIC": rbnEntModuleSE100FXMIC,
       "rbnEntModuleSE100GERJMIC": rbnEntModuleSE100GERJMIC,
       "rbnEntModuleSE100GEFXMIC": rbnEntModuleSE100GEFXMIC,
       "rbnEntModuleSEXC4": rbnEntModuleSEXC4,
       "rbnEntModuleSE100AIMOC3MIC": rbnEntModuleSE100AIMOC3MIC,
       "rbnEntModuleSEASE": rbnEntModuleSEASE,
       "rbnEntModuleSEFE60GE2": rbnEntModuleSEFE60GE2,
       "rbnEntModuleSEPOSOC192": rbnEntModuleSEPOSOC192,
       "rbnEntModuleSE5PortGIGE": rbnEntModuleSE5PortGIGE,
       "rbnEntModuleSE20PortGIGE": rbnEntModuleSE20PortGIGE,
       "rbnEntModuleSE4Port10GIGE": rbnEntModuleSE4Port10GIGE,
       "rbnEntModuleSE10GIGETM": rbnEntModuleSE10GIGETM,
       "rbnEntModuleSESSE": rbnEntModuleSESSE,
       "rbnEntModuleSE10PortGIGEDDR2": rbnEntModuleSE10PortGIGEDDR2,
       "rbnEntModuleSE4PortOC48": rbnEntModuleSE4PortOC48,
       "rbnEntModuleSE8PortOC3": rbnEntModuleSE8PortOC3,
       "rbnEntModuleSE8OR2PORTCHOC3OC12": rbnEntModuleSE8OR2PORTCHOC3OC12,
       "rbnEntModuleSEASE2": rbnEntModuleSEASE2,
       "rbnEntModuleSE1Port10GEOC192": rbnEntModuleSE1Port10GEOC192,
       "rbnEntModuleSEPos8xOC3": rbnEntModuleSEPos8xOC3,
       "rbnEntModuleSEPos4xOC12": rbnEntModuleSEPos4xOC12,
       "rbnEntModuleSEAtm2xOC12": rbnEntModuleSEAtm2xOC12,
       "rbnEntModuleSM10GIGEIM": rbnEntModuleSM10GIGEIM,
       "rbnEntModuleSMRP2": rbnEntModuleSMRP2,
       "rbnEntModuleSMGIGEIM": rbnEntModuleSMGIGEIM,
       "rbnEntModuleSMGIGETM": rbnEntModuleSMGIGETM,
       "rbnEntModuleSM10GIGETM": rbnEntModuleSM10GIGETM,
       "rbnEntModuleSMFE60GE2": rbnEntModuleSMFE60GE2,
       "rbnEntModuleSM20PortGIGE": rbnEntModuleSM20PortGIGE,
       "rbnEntModuleSM4Port10GIGE": rbnEntModuleSM4Port10GIGE,
       "rbnEntModuleSM10PortGIGEDDR2": rbnEntModuleSM10PortGIGEDDR2,
       "rbnEntModuleSM1Port10GEOC192": rbnEntModuleSM1Port10GEOC192,
       "rbnEntModuleSM8OR2PORTCHOC3OC12": rbnEntModuleSM8OR2PORTCHOC3OC12,
       "rbnEntModuleSSRALSW": rbnEntModuleSSRALSW,
       "rbnEntModuleSSRRPSW": rbnEntModuleSSRRPSW,
       "rbnEntModuleSSRSW": rbnEntModuleSSRSW,
       "rbnEntModuleSSR40Port1GE": rbnEntModuleSSR40Port1GE,
       "rbnEntModuleSSR10Port10GE": rbnEntModuleSSR10Port10GE,
       "rbnEntModuleSSC1": rbnEntModuleSSC1,
       "rbnEntModuleSSR2Port40GEor100GE": rbnEntModuleSSR2Port40GEor100GE,
       "rbnEntityTypePort": rbnEntityTypePort,
       "rbnEntPortUnknown": rbnEntPortUnknown,
       "rbnEntPortSMSAIMOC3": rbnEntPortSMSAIMOC3,
       "rbnEntPortSMSAIMDS3": rbnEntPortSMSAIMDS3,
       "rbnEntPortSMSAIME3": rbnEntPortSMSAIME3,
       "rbnEntPortSMSEIM": rbnEntPortSMSEIM,
       "rbnEntPortSMSPIMDS3": rbnEntPortSMSPIMDS3,
       "rbnEntPortSMSPIME3": rbnEntPortSMSPIME3,
       "rbnEntPortSMSPIMHSSI": rbnEntPortSMSPIMHSSI,
       "rbnEntPortSMSPIMDS1": rbnEntPortSMSPIMDS1,
       "rbnEntPortSMSPIMCDS3": rbnEntPortSMSPIMCDS3,
       "rbnEntPortSMSCE1MGMT": rbnEntPortSMSCE1MGMT,
       "rbnEntPortSMSCE2MGMT": rbnEntPortSMSCE2MGMT,
       "rbnEntPortSMSCE3MGMT": rbnEntPortSMSCE3MGMT,
       "rbnEntPortSMSAIMT1": rbnEntPortSMSAIMT1,
       "rbnEntPortSMSPIME1": rbnEntPortSMSPIME1,
       "rbnEntPortSMSAIME1": rbnEntPortSMSAIME1,
       "rbnEntPortSMSPOSOC3": rbnEntPortSMSPOSOC3,
       "rbnEntPortSMSPOSOC12": rbnEntPortSMSPOSOC12,
       "rbnEntPortSMSGIGEIM": rbnEntPortSMSGIGEIM,
       "rbnEntPortSMSAIMOC12": rbnEntPortSMSAIMOC12,
       "rbnEntPortSEXCMGMT": rbnEntPortSEXCMGMT,
       "rbnEntPortSEEIM": rbnEntPortSEEIM,
       "rbnEntPortSEGIGEIM": rbnEntPortSEGIGEIM,
       "rbnEntPortSEPOSOC12": rbnEntPortSEPOSOC12,
       "rbnEntPortSEPOSOC48": rbnEntPortSEPOSOC48,
       "rbnEntPortSEPOSOC3": rbnEntPortSEPOSOC3,
       "rbnEntPortSECHOC12DS1": rbnEntPortSECHOC12DS1,
       "rbnEntPortSECHOC12DS3": rbnEntPortSECHOC12DS3,
       "rbnEntPortSEAIMOC3": rbnEntPortSEAIMOC3,
       "rbnEntPortSEAIMOC12": rbnEntPortSEAIMOC12,
       "rbnEntPortSECHDS3": rbnEntPortSECHDS3,
       "rbnEntPortSEDS3": rbnEntPortSEDS3,
       "rbnEntPortSEAIMDS3": rbnEntPortSEAIMDS3,
       "rbnEntPortSECHSTM1E1": rbnEntPortSECHSTM1E1,
       "rbnEntPortSEE1": rbnEntPortSEE1,
       "rbnEntPortSEXC3MGMT": rbnEntPortSEXC3MGMT,
       "rbnEntPortSEE3": rbnEntPortSEE3,
       "rbnEntPortSEAIMOC12E": rbnEntPortSEAIMOC12E,
       "rbnEntPortSEGIGETM": rbnEntPortSEGIGETM,
       "rbnEntPortSE10GIGEIM": rbnEntPortSE10GIGEIM,
       "rbnEntPortSE100XCMGMT": rbnEntPortSE100XCMGMT,
       "rbnEntPortSE100EIM": rbnEntPortSE100EIM,
       "rbnEntPortSE100FXIM": rbnEntPortSE100FXIM,
       "rbnEntPortSE100GERJIM": rbnEntPortSE100GERJIM,
       "rbnEntPortSE100GEFXIM": rbnEntPortSE100GEFXIM,
       "rbnEntPortSEXC4MGMT": rbnEntPortSEXC4MGMT,
       "rbnEntPortSE100AIMOC3": rbnEntPortSE100AIMOC3,
       "rbnEntPortSEPOSOC192": rbnEntPortSEPOSOC192,
       "rbnEntPortSE10GIGETM": rbnEntPortSE10GIGETM,
       "rbnEntPortSECHOC3OC12": rbnEntPortSECHOC3OC12,
       "rbnEntPortSECHOC3": rbnEntPortSECHOC3,
       "rbnEntPortSM10GIGEIM": rbnEntPortSM10GIGEIM,
       "rbnEntPortSMRPMGMT": rbnEntPortSMRPMGMT,
       "rbnEntPortSMGIGEIM": rbnEntPortSMGIGEIM,
       "rbnEntPortSMGIGETM": rbnEntPortSMGIGETM,
       "rbnEntPortSM10GIGETM": rbnEntPortSM10GIGETM,
       "rbnEntPortSMEIM": rbnEntPortSMEIM,
       "rbnEntPortSMCHOC3OC12": rbnEntPortSMCHOC3OC12,
       "rbnEntPortSMCHOC3": rbnEntPortSMCHOC3,
       "rbnEntPortSSR1GE": rbnEntPortSSR1GE,
       "rbnEntPortSSR10GE": rbnEntPortSSR10GE,
       "rbnEntPortSSRRPSWMgmt": rbnEntPortSSRRPSWMgmt,
       "rbnEntPortSSR100GE": rbnEntPortSSR100GE,
       "rbnEntPortSSR40GE": rbnEntPortSSR40GE,
       "rbnEntPortSSR40GEor100GE": rbnEntPortSSR40GEor100GE,
       "rbnEntityTypeStack": rbnEntityTypeStack,
       "rbnEntityTypeCPU": rbnEntityTypeCPU,
       "rbnEntCpuUnknown": rbnEntCpuUnknown,
       "rbnEntCpuOcteon": rbnEntCpuOcteon,
       "rbnEntityTypeDisk": rbnEntityTypeDisk,
       "rbnEntDiskUnknown": rbnEntDiskUnknown,
       "rbnEntDiskSSE": rbnEntDiskSSE,
       "rbnEntityTypeMemory": rbnEntityTypeMemory}
)

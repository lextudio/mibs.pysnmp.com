# SNMP MIB module (CROSSBEAM-SYSTEMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CROSSBEAM-SYSTEMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:46 2024
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

crossbeamSystemsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 3, 1)
)
crossbeamSystemsMIB.setRevisions(
        ("2003-05-09 00:00",
         "2002-03-15 00:00",
         "2004-03-10 00:00",
         "2004-05-10 00:00",
         "2004-07-07 00:00",
         "2005-08-22 00:00",
         "2005-10-25 00:00",
         "2006-02-07 00:00",
         "2010-04-14 00:00",
         "2010-06-17 00:00",
         "2010-08-10 00:00",
         "2010-08-11 00:00",
         "2010-10-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CrossbeamSystems_ObjectIdentity = ObjectIdentity
crossbeamSystems = _CrossbeamSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848)
)
_CbsProducts_ObjectIdentity = ObjectIdentity
cbsProducts = _CbsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1)
)
_CbsX40_ObjectIdentity = ObjectIdentity
cbsX40 = _CbsX40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1)
)
_CbsX40Chassis_ObjectIdentity = ObjectIdentity
cbsX40Chassis = _CbsX40Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 1)
)
_CbsX40Modules_ObjectIdentity = ObjectIdentity
cbsX40Modules = _CbsX40Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2)
)
_CbsCPModules_ObjectIdentity = ObjectIdentity
cbsCPModules = _CbsCPModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 1)
)
_CbsCPM4100_ObjectIdentity = ObjectIdentity
cbsCPM4100 = _CbsCPM4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 1, 1)
)
_CbsCPM8100_ObjectIdentity = ObjectIdentity
cbsCPM8100 = _CbsCPM8100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 1, 2)
)
_CbsCPM8400_ObjectIdentity = ObjectIdentity
cbsCPM8400 = _CbsCPM8400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 1, 3)
)
_CbsCPM8600_ObjectIdentity = ObjectIdentity
cbsCPM8600 = _CbsCPM8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 1, 4)
)
_CbsCPM9600_ObjectIdentity = ObjectIdentity
cbsCPM9600 = _CbsCPM9600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 1, 5)
)
_CbsAPModules_ObjectIdentity = ObjectIdentity
cbsAPModules = _CbsAPModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2)
)
_CbsAPM4100_ObjectIdentity = ObjectIdentity
cbsAPM4100 = _CbsAPM4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 1)
)
_CbsAPM4200_ObjectIdentity = ObjectIdentity
cbsAPM4200 = _CbsAPM4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 2)
)
_CbsAPM4250_ObjectIdentity = ObjectIdentity
cbsAPM4250 = _CbsAPM4250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 3)
)
_CbsAPM8200_ObjectIdentity = ObjectIdentity
cbsAPM8200 = _CbsAPM8200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 4)
)
_CbsAPM8400_ObjectIdentity = ObjectIdentity
cbsAPM8400 = _CbsAPM8400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 5)
)
_CbsAPM8600_ObjectIdentity = ObjectIdentity
cbsAPM8600 = _CbsAPM8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 6)
)
_CbsAPM8650_ObjectIdentity = ObjectIdentity
cbsAPM8650 = _CbsAPM8650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 7)
)
_CbsAPM9600_ObjectIdentity = ObjectIdentity
cbsAPM9600 = _CbsAPM9600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 8)
)
_CbsAPM2030_ObjectIdentity = ObjectIdentity
cbsAPM2030 = _CbsAPM2030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 9)
)
_CbsNPModules_ObjectIdentity = ObjectIdentity
cbsNPModules = _CbsNPModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3)
)
_CbsNPM4100_ObjectIdentity = ObjectIdentity
cbsNPM4100 = _CbsNPM4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 1)
)
_CbsNPM4110_ObjectIdentity = ObjectIdentity
cbsNPM4110 = _CbsNPM4110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 2)
)
_CbsNPM8200_ObjectIdentity = ObjectIdentity
cbsNPM8200 = _CbsNPM8200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 3)
)
_CbsNPM8210_ObjectIdentity = ObjectIdentity
cbsNPM8210 = _CbsNPM8210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 4)
)
_CbsNPM8600_ObjectIdentity = ObjectIdentity
cbsNPM8600 = _CbsNPM8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 5)
)
_CbsNPM8650_ObjectIdentity = ObjectIdentity
cbsNPM8650 = _CbsNPM8650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 6)
)
_CbsNPM8620_ObjectIdentity = ObjectIdentity
cbsNPM8620 = _CbsNPM8620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 7)
)
_CbsNPM30_ObjectIdentity = ObjectIdentity
cbsNPM30 = _CbsNPM30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 8)
)
_CbsNPM20_ObjectIdentity = ObjectIdentity
cbsNPM20 = _CbsNPM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 9)
)
_CbsXSeries_ObjectIdentity = ObjectIdentity
cbsXSeries = _CbsXSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 2)
)
_CbsXChassis_ObjectIdentity = ObjectIdentity
cbsXChassis = _CbsXChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 2, 1)
)
_CbsX45Chassis_ObjectIdentity = ObjectIdentity
cbsX45Chassis = _CbsX45Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 2, 1, 1)
)
_CbsX80Chassis_ObjectIdentity = ObjectIdentity
cbsX80Chassis = _CbsX80Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 2, 1, 2)
)
_CbsX60Chassis_ObjectIdentity = ObjectIdentity
cbsX60Chassis = _CbsX60Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 2, 1, 3)
)
_CbsX20Chassis_ObjectIdentity = ObjectIdentity
cbsX20Chassis = _CbsX20Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 2, 1, 4)
)
_CbsX30Chassis_ObjectIdentity = ObjectIdentity
cbsX30Chassis = _CbsX30Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 2, 1, 5)
)
_CbsCSeries_ObjectIdentity = ObjectIdentity
cbsCSeries = _CbsCSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 3)
)
_CbsCChassis_ObjectIdentity = ObjectIdentity
cbsCChassis = _CbsCChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 3, 1)
)
_CbsC30Chassis_ObjectIdentity = ObjectIdentity
cbsC30Chassis = _CbsC30Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 1)
)
_CbsC10Chassis_ObjectIdentity = ObjectIdentity
cbsC10Chassis = _CbsC10Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 2)
)
_CbsC30iChassis_ObjectIdentity = ObjectIdentity
cbsC30iChassis = _CbsC30iChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 3)
)
_CbsC2Chassis_ObjectIdentity = ObjectIdentity
cbsC2Chassis = _CbsC2Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 4)
)
_CbsC6Chassis_ObjectIdentity = ObjectIdentity
cbsC6Chassis = _CbsC6Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 5)
)
_CbsC12Chassis_ObjectIdentity = ObjectIdentity
cbsC12Chassis = _CbsC12Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 6)
)
_CbsC25Chassis_ObjectIdentity = ObjectIdentity
cbsC25Chassis = _CbsC25Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 7)
)
_CbsMgmt_ObjectIdentity = ObjectIdentity
cbsMgmt = _CbsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 2)
)
_CbsMIBs_ObjectIdentity = ObjectIdentity
cbsMIBs = _CbsMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 3)
)
_CbsTraps_ObjectIdentity = ObjectIdentity
cbsTraps = _CbsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CROSSBEAM-SYSTEMS-MIB",
    **{"crossbeamSystems": crossbeamSystems,
       "cbsProducts": cbsProducts,
       "cbsX40": cbsX40,
       "cbsX40Chassis": cbsX40Chassis,
       "cbsX40Modules": cbsX40Modules,
       "cbsCPModules": cbsCPModules,
       "cbsCPM4100": cbsCPM4100,
       "cbsCPM8100": cbsCPM8100,
       "cbsCPM8400": cbsCPM8400,
       "cbsCPM8600": cbsCPM8600,
       "cbsCPM9600": cbsCPM9600,
       "cbsAPModules": cbsAPModules,
       "cbsAPM4100": cbsAPM4100,
       "cbsAPM4200": cbsAPM4200,
       "cbsAPM4250": cbsAPM4250,
       "cbsAPM8200": cbsAPM8200,
       "cbsAPM8400": cbsAPM8400,
       "cbsAPM8600": cbsAPM8600,
       "cbsAPM8650": cbsAPM8650,
       "cbsAPM9600": cbsAPM9600,
       "cbsAPM2030": cbsAPM2030,
       "cbsNPModules": cbsNPModules,
       "cbsNPM4100": cbsNPM4100,
       "cbsNPM4110": cbsNPM4110,
       "cbsNPM8200": cbsNPM8200,
       "cbsNPM8210": cbsNPM8210,
       "cbsNPM8600": cbsNPM8600,
       "cbsNPM8650": cbsNPM8650,
       "cbsNPM8620": cbsNPM8620,
       "cbsNPM30": cbsNPM30,
       "cbsNPM20": cbsNPM20,
       "cbsXSeries": cbsXSeries,
       "cbsXChassis": cbsXChassis,
       "cbsX45Chassis": cbsX45Chassis,
       "cbsX80Chassis": cbsX80Chassis,
       "cbsX60Chassis": cbsX60Chassis,
       "cbsX20Chassis": cbsX20Chassis,
       "cbsX30Chassis": cbsX30Chassis,
       "cbsCSeries": cbsCSeries,
       "cbsCChassis": cbsCChassis,
       "cbsC30Chassis": cbsC30Chassis,
       "cbsC10Chassis": cbsC10Chassis,
       "cbsC30iChassis": cbsC30iChassis,
       "cbsC2Chassis": cbsC2Chassis,
       "cbsC6Chassis": cbsC6Chassis,
       "cbsC12Chassis": cbsC12Chassis,
       "cbsC25Chassis": cbsC25Chassis,
       "cbsMgmt": cbsMgmt,
       "cbsMIBs": cbsMIBs,
       "crossbeamSystemsMIB": crossbeamSystemsMIB,
       "cbsTraps": cbsTraps}
)

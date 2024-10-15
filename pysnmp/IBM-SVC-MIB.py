# SNMP MIB module (IBM-SVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM-SVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:40 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

ibm2145TSVE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 190)
)
ibm2145TSVE.setRevisions(
        ("2017-01-12 00:00",
         "2016-11-01 00:00",
         "2016-07-14 00:00",
         "2016-04-28 00:00",
         "2016-01-22 00:00",
         "2015-11-25 00:00",
         "2015-04-17 00:00",
         "2014-09-01 00:00",
         "2013-09-24 00:00",
         "2013-09-24 00:00",
         "2013-09-24 00:00",
         "2012-11-06 00:00",
         "2012-04-19 00:00",
         "2011-05-26 00:00",
         "2011-05-26 00:00",
         "2010-05-07 00:00",
         "2009-09-01 00:00",
         "2008-05-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Ibm2145TSVEObjects_ObjectIdentity = ObjectIdentity
ibm2145TSVEObjects = _Ibm2145TSVEObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4)
)
_TsveMACH_Type = SnmpAdminString
_TsveMACH_Object = MibScalar
tsveMACH = _TsveMACH_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 1),
    _TsveMACH_Type()
)
tsveMACH.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tsveMACH.setStatus("current")
_TsveSERI_Type = SnmpAdminString
_TsveSERI_Object = MibScalar
tsveSERI = _TsveSERI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 2),
    _TsveSERI_Type()
)
tsveSERI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tsveSERI.setStatus("current")
_TsveERRI_Type = SnmpAdminString
_TsveERRI_Object = MibScalar
tsveERRI = _TsveERRI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 3),
    _TsveERRI_Type()
)
tsveERRI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tsveERRI.setStatus("current")
_TsveERRC_Type = SnmpAdminString
_TsveERRC_Object = MibScalar
tsveERRC = _TsveERRC_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 4),
    _TsveERRC_Type()
)
tsveERRC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tsveERRC.setStatus("current")
_TsveSWVE_Type = SnmpAdminString
_TsveSWVE_Object = MibScalar
tsveSWVE = _TsveSWVE_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 5),
    _TsveSWVE_Type()
)
tsveSWVE.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tsveSWVE.setStatus("current")
_TsveFRUP_Type = SnmpAdminString
_TsveFRUP_Object = MibScalar
tsveFRUP = _TsveFRUP_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 6),
    _TsveFRUP_Type()
)
tsveFRUP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tsveFRUP.setStatus("current")
_TsveCLUS_Type = SnmpAdminString
_TsveCLUS_Object = MibScalar
tsveCLUS = _TsveCLUS_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 7),
    _TsveCLUS_Type()
)
tsveCLUS.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tsveCLUS.setStatus("current")
_TsveNODE_Type = SnmpAdminString
_TsveNODE_Object = MibScalar
tsveNODE = _TsveNODE_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 8),
    _TsveNODE_Type()
)
tsveNODE.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tsveNODE.setStatus("current")
_TsveERRS_Type = SnmpAdminString
_TsveERRS_Object = MibScalar
tsveERRS = _TsveERRS_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 9),
    _TsveERRS_Type()
)
tsveERRS.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tsveERRS.setStatus("current")
_TsveTIME_Type = SnmpAdminString
_TsveTIME_Object = MibScalar
tsveTIME = _TsveTIME_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 10),
    _TsveTIME_Type()
)
tsveTIME.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tsveTIME.setStatus("current")
_TsveOBJT_Type = SnmpAdminString
_TsveOBJT_Object = MibScalar
tsveOBJT = _TsveOBJT_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 11),
    _TsveOBJT_Type()
)
tsveOBJT.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tsveOBJT.setStatus("current")
_TsveOBJI_Type = SnmpAdminString
_TsveOBJI_Object = MibScalar
tsveOBJI = _TsveOBJI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 12),
    _TsveOBJI_Type()
)
tsveOBJI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tsveOBJI.setStatus("current")
_TsveADD1_Type = SnmpAdminString
_TsveADD1_Object = MibScalar
tsveADD1 = _TsveADD1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 13),
    _TsveADD1_Type()
)
tsveADD1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tsveADD1.setStatus("current")
_TsveADD2_Type = SnmpAdminString
_TsveADD2_Object = MibScalar
tsveADD2 = _TsveADD2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 14),
    _TsveADD2_Type()
)
tsveADD2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tsveADD2.setStatus("current")
_TsveCOPY_Type = SnmpAdminString
_TsveCOPY_Object = MibScalar
tsveCOPY = _TsveCOPY_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 15),
    _TsveCOPY_Type()
)
tsveCOPY.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tsveCOPY.setStatus("current")
_TsveMPNO_Type = SnmpAdminString
_TsveMPNO_Object = MibScalar
tsveMPNO = _TsveMPNO_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 16),
    _TsveMPNO_Type()
)
tsveMPNO.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tsveMPNO.setStatus("current")
_TsveOBJN_Type = SnmpAdminString
_TsveOBJN_Object = MibScalar
tsveOBJN = _TsveOBJN_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 17),
    _TsveOBJN_Type()
)
tsveOBJN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tsveOBJN.setStatus("current")
_TsveIDAL_Type = SnmpAdminString
_TsveIDAL_Object = MibScalar
tsveIDAL = _TsveIDAL_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 4, 18),
    _TsveIDAL_Type()
)
tsveIDAL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tsveIDAL.setStatus("current")
_Ibm2145TSVEConformance_ObjectIdentity = ObjectIdentity
ibm2145TSVEConformance = _Ibm2145TSVEConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 5)
)
_TsveCompliances_ObjectIdentity = ObjectIdentity
tsveCompliances = _TsveCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 5, 1)
)
_TsveGroups_ObjectIdentity = ObjectIdentity
tsveGroups = _TsveGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 5, 2)
)

# Managed Objects groups

tsveRequiredObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 5, 2, 1)
)
tsveRequiredObjectsGroup.setObjects(
      *(("IBM-SVC-MIB", "tsveMACH"),
        ("IBM-SVC-MIB", "tsveSERI"),
        ("IBM-SVC-MIB", "tsveERRI"),
        ("IBM-SVC-MIB", "tsveERRC"),
        ("IBM-SVC-MIB", "tsveSWVE"),
        ("IBM-SVC-MIB", "tsveFRUP"),
        ("IBM-SVC-MIB", "tsveCLUS"),
        ("IBM-SVC-MIB", "tsveNODE"),
        ("IBM-SVC-MIB", "tsveERRS"),
        ("IBM-SVC-MIB", "tsveTIME"),
        ("IBM-SVC-MIB", "tsveOBJT"),
        ("IBM-SVC-MIB", "tsveOBJI"),
        ("IBM-SVC-MIB", "tsveADD1"),
        ("IBM-SVC-MIB", "tsveADD2"),
        ("IBM-SVC-MIB", "tsveCOPY"),
        ("IBM-SVC-MIB", "tsveMPNO"),
        ("IBM-SVC-MIB", "tsveOBJN"),
        ("IBM-SVC-MIB", "tsveIDAL"))
)
if mibBuilder.loadTexts:
    tsveRequiredObjectsGroup.setStatus("current")


# Notification objects

tsveETrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 1)
)
tsveETrap.setObjects(
      *(("IBM-SVC-MIB", "tsveMACH"),
        ("IBM-SVC-MIB", "tsveSERI"),
        ("IBM-SVC-MIB", "tsveERRI"),
        ("IBM-SVC-MIB", "tsveERRC"),
        ("IBM-SVC-MIB", "tsveSWVE"),
        ("IBM-SVC-MIB", "tsveFRUP"),
        ("IBM-SVC-MIB", "tsveCLUS"),
        ("IBM-SVC-MIB", "tsveNODE"),
        ("IBM-SVC-MIB", "tsveERRS"),
        ("IBM-SVC-MIB", "tsveTIME"),
        ("IBM-SVC-MIB", "tsveOBJT"),
        ("IBM-SVC-MIB", "tsveOBJI"),
        ("IBM-SVC-MIB", "tsveADD1"),
        ("IBM-SVC-MIB", "tsveADD2"),
        ("IBM-SVC-MIB", "tsveCOPY"),
        ("IBM-SVC-MIB", "tsveMPNO"),
        ("IBM-SVC-MIB", "tsveOBJN"),
        ("IBM-SVC-MIB", "tsveIDAL"))
)
if mibBuilder.loadTexts:
    tsveETrap.setStatus(
        "current"
    )

tsveWTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 2)
)
tsveWTrap.setObjects(
      *(("IBM-SVC-MIB", "tsveMACH"),
        ("IBM-SVC-MIB", "tsveSERI"),
        ("IBM-SVC-MIB", "tsveERRI"),
        ("IBM-SVC-MIB", "tsveERRC"),
        ("IBM-SVC-MIB", "tsveSWVE"),
        ("IBM-SVC-MIB", "tsveFRUP"),
        ("IBM-SVC-MIB", "tsveCLUS"),
        ("IBM-SVC-MIB", "tsveNODE"),
        ("IBM-SVC-MIB", "tsveERRS"),
        ("IBM-SVC-MIB", "tsveTIME"),
        ("IBM-SVC-MIB", "tsveOBJT"),
        ("IBM-SVC-MIB", "tsveOBJI"),
        ("IBM-SVC-MIB", "tsveADD1"),
        ("IBM-SVC-MIB", "tsveADD2"),
        ("IBM-SVC-MIB", "tsveCOPY"),
        ("IBM-SVC-MIB", "tsveMPNO"),
        ("IBM-SVC-MIB", "tsveOBJN"),
        ("IBM-SVC-MIB", "tsveIDAL"))
)
if mibBuilder.loadTexts:
    tsveWTrap.setStatus(
        "current"
    )

tsveITrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 3)
)
tsveITrap.setObjects(
      *(("IBM-SVC-MIB", "tsveMACH"),
        ("IBM-SVC-MIB", "tsveSERI"),
        ("IBM-SVC-MIB", "tsveERRI"),
        ("IBM-SVC-MIB", "tsveERRC"),
        ("IBM-SVC-MIB", "tsveSWVE"),
        ("IBM-SVC-MIB", "tsveFRUP"),
        ("IBM-SVC-MIB", "tsveCLUS"),
        ("IBM-SVC-MIB", "tsveNODE"),
        ("IBM-SVC-MIB", "tsveERRS"),
        ("IBM-SVC-MIB", "tsveTIME"),
        ("IBM-SVC-MIB", "tsveOBJT"),
        ("IBM-SVC-MIB", "tsveOBJI"),
        ("IBM-SVC-MIB", "tsveADD1"),
        ("IBM-SVC-MIB", "tsveADD2"),
        ("IBM-SVC-MIB", "tsveCOPY"),
        ("IBM-SVC-MIB", "tsveMPNO"),
        ("IBM-SVC-MIB", "tsveOBJN"),
        ("IBM-SVC-MIB", "tsveIDAL"))
)
if mibBuilder.loadTexts:
    tsveITrap.setStatus(
        "current"
    )


# Notifications groups

tsveNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 5, 2, 2)
)
tsveNotifGroup.setObjects(
      *(("IBM-SVC-MIB", "tsveETrap"),
        ("IBM-SVC-MIB", "tsveWTrap"),
        ("IBM-SVC-MIB", "tsveITrap"))
)
if mibBuilder.loadTexts:
    tsveNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tsveCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2, 6, 190, 5, 1, 1)
)
if mibBuilder.loadTexts:
    tsveCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-SVC-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "ibm2145TSVE": ibm2145TSVE,
       "tsveETrap": tsveETrap,
       "tsveWTrap": tsveWTrap,
       "tsveITrap": tsveITrap,
       "ibm2145TSVEObjects": ibm2145TSVEObjects,
       "tsveMACH": tsveMACH,
       "tsveSERI": tsveSERI,
       "tsveERRI": tsveERRI,
       "tsveERRC": tsveERRC,
       "tsveSWVE": tsveSWVE,
       "tsveFRUP": tsveFRUP,
       "tsveCLUS": tsveCLUS,
       "tsveNODE": tsveNODE,
       "tsveERRS": tsveERRS,
       "tsveTIME": tsveTIME,
       "tsveOBJT": tsveOBJT,
       "tsveOBJI": tsveOBJI,
       "tsveADD1": tsveADD1,
       "tsveADD2": tsveADD2,
       "tsveCOPY": tsveCOPY,
       "tsveMPNO": tsveMPNO,
       "tsveOBJN": tsveOBJN,
       "tsveIDAL": tsveIDAL,
       "ibm2145TSVEConformance": ibm2145TSVEConformance,
       "tsveCompliances": tsveCompliances,
       "tsveCompliance": tsveCompliance,
       "tsveGroups": tsveGroups,
       "tsveRequiredObjectsGroup": tsveRequiredObjectsGroup,
       "tsveNotifGroup": tsveNotifGroup}
)

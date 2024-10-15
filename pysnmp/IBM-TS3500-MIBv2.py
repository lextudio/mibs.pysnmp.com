# SNMP MIB module (IBM-TS3500-MIBv2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM-TS3500-MIBv2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:41 2024
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

ibm3584 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182)
)
ibm3584.setRevisions(
        ("2009-09-23 00:00",
         "2009-04-06 00:00",
         "2009-04-06 00:00",
         "2008-07-16 00:00",
         "2008-07-16 00:00",
         "2008-07-16 00:00",
         "2006-01-12 00:00",
         "2006-01-03 00:00",
         "2005-06-15 00:00",
         "2005-05-03 00:00",
         "2004-12-01 00:00",
         "2004-03-04 00:00",
         "2004-03-03 00:00",
         "2004-02-03 00:00",
         "2003-10-22 00:00",
         "2002-04-23 00:00",
         "2001-01-01 00:00")
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
_Ibm3584MIB_ObjectIdentity = ObjectIdentity
ibm3584MIB = _Ibm3584MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1)
)
_Ibm3584MIBTraps_ObjectIdentity = ObjectIdentity
ibm3584MIBTraps = _Ibm3584MIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0)
)
_Ibm3584MIBAdmin_ObjectIdentity = ObjectIdentity
ibm3584MIBAdmin = _Ibm3584MIBAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 1)
)
_Ibm3584MIBObjects_ObjectIdentity = ObjectIdentity
ibm3584MIBObjects = _Ibm3584MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2)
)
_Ibm3584MIBGroupMTMNLSN_ObjectIdentity = ObjectIdentity
ibm3584MIBGroupMTMNLSN = _Ibm3584MIBGroupMTMNLSN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 11)
)


class _Ibm3584MIBObjectsMTMNLSN_Type(DisplayString):
    """Custom type ibm3584MIBObjectsMTMNLSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Ibm3584MIBObjectsMTMNLSN_Type.__name__ = "DisplayString"
_Ibm3584MIBObjectsMTMNLSN_Object = MibScalar
ibm3584MIBObjectsMTMNLSN = _Ibm3584MIBObjectsMTMNLSN_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 11, 1),
    _Ibm3584MIBObjectsMTMNLSN_Type()
)
ibm3584MIBObjectsMTMNLSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3584MIBObjectsMTMNLSN.setStatus("current")
_Ibm3584MIBGroupSKASCASCQ_ObjectIdentity = ObjectIdentity
ibm3584MIBGroupSKASCASCQ = _Ibm3584MIBGroupSKASCASCQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 21)
)


class _Ibm3584MIBObjectsSKASCASCQ_Type(DisplayString):
    """Custom type ibm3584MIBObjectsSKASCASCQ based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Ibm3584MIBObjectsSKASCASCQ_Type.__name__ = "DisplayString"
_Ibm3584MIBObjectsSKASCASCQ_Object = MibScalar
ibm3584MIBObjectsSKASCASCQ = _Ibm3584MIBObjectsSKASCASCQ_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 21, 1),
    _Ibm3584MIBObjectsSKASCASCQ_Type()
)
ibm3584MIBObjectsSKASCASCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3584MIBObjectsSKASCASCQ.setStatus("current")
_Ibm3584MIBGroupHECHECQ_ObjectIdentity = ObjectIdentity
ibm3584MIBGroupHECHECQ = _Ibm3584MIBGroupHECHECQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 31)
)


class _Ibm3584MIBObjectsHECHECQ_Type(DisplayString):
    """Custom type ibm3584MIBObjectsHECHECQ based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_Ibm3584MIBObjectsHECHECQ_Type.__name__ = "DisplayString"
_Ibm3584MIBObjectsHECHECQ_Object = MibScalar
ibm3584MIBObjectsHECHECQ = _Ibm3584MIBObjectsHECHECQ_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 31, 1),
    _Ibm3584MIBObjectsHECHECQ_Type()
)
ibm3584MIBObjectsHECHECQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3584MIBObjectsHECHECQ.setStatus("current")
_Ibm3584MIBGroupTA_ObjectIdentity = ObjectIdentity
ibm3584MIBGroupTA = _Ibm3584MIBGroupTA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 41)
)


class _Ibm3584MIBObjectsTA_Type(DisplayString):
    """Custom type ibm3584MIBObjectsTA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_Ibm3584MIBObjectsTA_Type.__name__ = "DisplayString"
_Ibm3584MIBObjectsTA_Object = MibScalar
ibm3584MIBObjectsTA = _Ibm3584MIBObjectsTA_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 41, 1),
    _Ibm3584MIBObjectsTA_Type()
)
ibm3584MIBObjectsTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3584MIBObjectsTA.setStatus("current")
_Ibm3584MIBGroupURC_ObjectIdentity = ObjectIdentity
ibm3584MIBGroupURC = _Ibm3584MIBGroupURC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 51)
)


class _Ibm3584MIBObjectsURC_Type(DisplayString):
    """Custom type ibm3584MIBObjectsURC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_Ibm3584MIBObjectsURC_Type.__name__ = "DisplayString"
_Ibm3584MIBObjectsURC_Object = MibScalar
ibm3584MIBObjectsURC = _Ibm3584MIBObjectsURC_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 51, 1),
    _Ibm3584MIBObjectsURC_Type()
)
ibm3584MIBObjectsURC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3584MIBObjectsURC.setStatus("current")
_Ibm3584MIBGroupFFFD_ObjectIdentity = ObjectIdentity
ibm3584MIBGroupFFFD = _Ibm3584MIBGroupFFFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 61)
)


class _Ibm3584MIBObjectsFFFD_Type(DisplayString):
    """Custom type ibm3584MIBObjectsFFFD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_Ibm3584MIBObjectsFFFD_Type.__name__ = "DisplayString"
_Ibm3584MIBObjectsFFFD_Object = MibScalar
ibm3584MIBObjectsFFFD = _Ibm3584MIBObjectsFFFD_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 61, 1),
    _Ibm3584MIBObjectsFFFD_Type()
)
ibm3584MIBObjectsFFFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3584MIBObjectsFFFD.setStatus("current")
_Ibm3584MIBGroupTD_ObjectIdentity = ObjectIdentity
ibm3584MIBGroupTD = _Ibm3584MIBGroupTD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 71)
)


class _Ibm3584MIBObjectsTD_Type(DisplayString):
    """Custom type ibm3584MIBObjectsTD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Ibm3584MIBObjectsTD_Type.__name__ = "DisplayString"
_Ibm3584MIBObjectsTD_Object = MibScalar
ibm3584MIBObjectsTD = _Ibm3584MIBObjectsTD_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 71, 1),
    _Ibm3584MIBObjectsTD_Type()
)
ibm3584MIBObjectsTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3584MIBObjectsTD.setStatus("current")
_Ibm3584MIBGroupFSC_ObjectIdentity = ObjectIdentity
ibm3584MIBGroupFSC = _Ibm3584MIBGroupFSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 81)
)


class _Ibm3584MIBObjectsFSC_Type(DisplayString):
    """Custom type ibm3584MIBObjectsFSC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_Ibm3584MIBObjectsFSC_Type.__name__ = "DisplayString"
_Ibm3584MIBObjectsFSC_Object = MibScalar
ibm3584MIBObjectsFSC = _Ibm3584MIBObjectsFSC_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 81, 1),
    _Ibm3584MIBObjectsFSC_Type()
)
ibm3584MIBObjectsFSC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3584MIBObjectsFSC.setStatus("current")
_Ibm3584MIBGroupSCD_ObjectIdentity = ObjectIdentity
ibm3584MIBGroupSCD = _Ibm3584MIBGroupSCD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 91)
)


class _Ibm3584MIBObjectsSCD_Type(DisplayString):
    """Custom type ibm3584MIBObjectsSCD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Ibm3584MIBObjectsSCD_Type.__name__ = "DisplayString"
_Ibm3584MIBObjectsSCD_Object = MibScalar
ibm3584MIBObjectsSCD = _Ibm3584MIBObjectsSCD_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 91, 1),
    _Ibm3584MIBObjectsSCD_Type()
)
ibm3584MIBObjectsSCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3584MIBObjectsSCD.setStatus("current")
_Ibm3584MIBGroupVOLSER_ObjectIdentity = ObjectIdentity
ibm3584MIBGroupVOLSER = _Ibm3584MIBGroupVOLSER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 101)
)


class _Ibm3584MIBObjectsVOLSER_Type(DisplayString):
    """Custom type ibm3584MIBObjectsVOLSER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Ibm3584MIBObjectsVOLSER_Type.__name__ = "DisplayString"
_Ibm3584MIBObjectsVOLSER_Object = MibScalar
ibm3584MIBObjectsVOLSER = _Ibm3584MIBObjectsVOLSER_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 101, 1),
    _Ibm3584MIBObjectsVOLSER_Type()
)
ibm3584MIBObjectsVOLSER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3584MIBObjectsVOLSER.setStatus("current")
_Ibm3584MIBGroupLL_ObjectIdentity = ObjectIdentity
ibm3584MIBGroupLL = _Ibm3584MIBGroupLL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 111)
)


class _Ibm3584MIBObjectsLL_Type(DisplayString):
    """Custom type ibm3584MIBObjectsLL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Ibm3584MIBObjectsLL_Type.__name__ = "DisplayString"
_Ibm3584MIBObjectsLL_Object = MibScalar
ibm3584MIBObjectsLL = _Ibm3584MIBObjectsLL_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 111, 1),
    _Ibm3584MIBObjectsLL_Type()
)
ibm3584MIBObjectsLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3584MIBObjectsLL.setStatus("current")
_Ibm3584MIBGroupWWNN_ObjectIdentity = ObjectIdentity
ibm3584MIBGroupWWNN = _Ibm3584MIBGroupWWNN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 121)
)


class _Ibm3584MIBObjectsWWNN_Type(DisplayString):
    """Custom type ibm3584MIBObjectsWWNN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Ibm3584MIBObjectsWWNN_Type.__name__ = "DisplayString"
_Ibm3584MIBObjectsWWNN_Object = MibScalar
ibm3584MIBObjectsWWNN = _Ibm3584MIBObjectsWWNN_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 121, 1),
    _Ibm3584MIBObjectsWWNN_Type()
)
ibm3584MIBObjectsWWNN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3584MIBObjectsWWNN.setStatus("current")
_Ibm3584MIBGroupEA_ObjectIdentity = ObjectIdentity
ibm3584MIBGroupEA = _Ibm3584MIBGroupEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 131)
)
_Ibm3584MIBObjectsEA_Type = Integer32
_Ibm3584MIBObjectsEA_Object = MibScalar
ibm3584MIBObjectsEA = _Ibm3584MIBObjectsEA_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 131, 1),
    _Ibm3584MIBObjectsEA_Type()
)
ibm3584MIBObjectsEA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3584MIBObjectsEA.setStatus("current")
_Ibm3584MIBGroupDrvSN_ObjectIdentity = ObjectIdentity
ibm3584MIBGroupDrvSN = _Ibm3584MIBGroupDrvSN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 141)
)


class _Ibm3584MIBObjectsDrvSN_Type(DisplayString):
    """Custom type ibm3584MIBObjectsDrvSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_Ibm3584MIBObjectsDrvSN_Type.__name__ = "DisplayString"
_Ibm3584MIBObjectsDrvSN_Object = MibScalar
ibm3584MIBObjectsDrvSN = _Ibm3584MIBObjectsDrvSN_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 141, 1),
    _Ibm3584MIBObjectsDrvSN_Type()
)
ibm3584MIBObjectsDrvSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3584MIBObjectsDrvSN.setStatus("current")
_Ibm3584MIBSeverity_ObjectIdentity = ObjectIdentity
ibm3584MIBSeverity = _Ibm3584MIBSeverity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 151)
)


class _Ibm3584MIBObjectsSeverity_Type(Integer32):
    """Custom type ibm3584MIBObjectsSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("authentication", 7),
          ("configuration", 5),
          ("critical", 3),
          ("informational", 1),
          ("security", 6),
          ("unknown", 4),
          ("warning", 2))
    )


_Ibm3584MIBObjectsSeverity_Type.__name__ = "Integer32"
_Ibm3584MIBObjectsSeverity_Object = MibScalar
ibm3584MIBObjectsSeverity = _Ibm3584MIBObjectsSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 151, 1),
    _Ibm3584MIBObjectsSeverity_Type()
)
ibm3584MIBObjectsSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3584MIBObjectsSeverity.setStatus("current")
_Ibm3584MIBUserID_ObjectIdentity = ObjectIdentity
ibm3584MIBUserID = _Ibm3584MIBUserID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 171)
)


class _Ibm3584MIBObjectsUserID_Type(DisplayString):
    """Custom type ibm3584MIBObjectsUserID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Ibm3584MIBObjectsUserID_Type.__name__ = "DisplayString"
_Ibm3584MIBObjectsUserID_Object = MibScalar
ibm3584MIBObjectsUserID = _Ibm3584MIBObjectsUserID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 2, 171, 1),
    _Ibm3584MIBObjectsUserID_Type()
)
ibm3584MIBObjectsUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm3584MIBObjectsUserID.setStatus("current")
_Ibm3584MIBConformance_ObjectIdentity = ObjectIdentity
ibm3584MIBConformance = _Ibm3584MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 3)
)
_Ibm3584MIBCompliances_ObjectIdentity = ObjectIdentity
ibm3584MIBCompliances = _Ibm3584MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 3, 1)
)
_Ibm3584MIBGroups_ObjectIdentity = ObjectIdentity
ibm3584MIBGroups = _Ibm3584MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 3, 2)
)

# Managed Objects groups

ibm3584MIBObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 3, 2, 3)
)
ibm3584MIBObjectsGroup.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsEA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584MIBObjectsGroup.setStatus("current")


# Notification objects

ibm3584Trap001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 1)
)
ibm3584Trap001.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap001.setStatus(
        "current"
    )

ibm3584Trap002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 2)
)
ibm3584Trap002.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap002.setStatus(
        "current"
    )

ibm3584Trap003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 3)
)
ibm3584Trap003.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap003.setStatus(
        "current"
    )

ibm3584Trap004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 4)
)
ibm3584Trap004.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap004.setStatus(
        "current"
    )

ibm3584Trap005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 5)
)
ibm3584Trap005.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap005.setStatus(
        "current"
    )

ibm3584Trap006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 6)
)
ibm3584Trap006.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap006.setStatus(
        "current"
    )

ibm3584Trap007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 7)
)
ibm3584Trap007.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap007.setStatus(
        "current"
    )

ibm3584Trap008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 8)
)
ibm3584Trap008.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap008.setStatus(
        "current"
    )

ibm3584Trap009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 9)
)
ibm3584Trap009.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap009.setStatus(
        "current"
    )

ibm3584Trap010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 10)
)
ibm3584Trap010.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap010.setStatus(
        "current"
    )

ibm3584Trap011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 11)
)
ibm3584Trap011.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap011.setStatus(
        "current"
    )

ibm3584Trap012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 12)
)
ibm3584Trap012.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap012.setStatus(
        "current"
    )

ibm3584Trap013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 13)
)
ibm3584Trap013.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap013.setStatus(
        "current"
    )

ibm3584Trap014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 14)
)
ibm3584Trap014.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap014.setStatus(
        "current"
    )

ibm3584Trap015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 15)
)
ibm3584Trap015.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap015.setStatus(
        "current"
    )

ibm3584Trap016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 16)
)
ibm3584Trap016.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap016.setStatus(
        "current"
    )

ibm3584Trap017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 17)
)
ibm3584Trap017.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap017.setStatus(
        "current"
    )

ibm3584Trap018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 18)
)
ibm3584Trap018.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap018.setStatus(
        "current"
    )

ibm3584Trap019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 19)
)
ibm3584Trap019.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap019.setStatus(
        "current"
    )

ibm3584Trap020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 20)
)
ibm3584Trap020.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap020.setStatus(
        "current"
    )

ibm3584Trap021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 21)
)
ibm3584Trap021.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap021.setStatus(
        "current"
    )

ibm3584Trap022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 22)
)
ibm3584Trap022.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap022.setStatus(
        "current"
    )

ibm3584Trap023 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 23)
)
ibm3584Trap023.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap023.setStatus(
        "current"
    )

ibm3584Trap024 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 24)
)
ibm3584Trap024.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap024.setStatus(
        "current"
    )

ibm3584Trap025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 25)
)
ibm3584Trap025.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap025.setStatus(
        "current"
    )

ibm3584Trap026 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 26)
)
ibm3584Trap026.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap026.setStatus(
        "current"
    )

ibm3584Trap027 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 27)
)
ibm3584Trap027.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap027.setStatus(
        "current"
    )

ibm3584Trap028 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 28)
)
ibm3584Trap028.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap028.setStatus(
        "current"
    )

ibm3584Trap029 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 29)
)
ibm3584Trap029.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap029.setStatus(
        "current"
    )

ibm3584Trap030 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 30)
)
ibm3584Trap030.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap030.setStatus(
        "current"
    )

ibm3584Trap031 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 31)
)
ibm3584Trap031.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap031.setStatus(
        "current"
    )

ibm3584Trap032 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 32)
)
ibm3584Trap032.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsHECHECQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap032.setStatus(
        "current"
    )

ibm3584Trap201 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 201)
)
ibm3584Trap201.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap201.setStatus(
        "current"
    )

ibm3584Trap202 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 202)
)
ibm3584Trap202.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap202.setStatus(
        "current"
    )

ibm3584Trap203 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 203)
)
ibm3584Trap203.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap203.setStatus(
        "current"
    )

ibm3584Trap204 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 204)
)
ibm3584Trap204.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap204.setStatus(
        "current"
    )

ibm3584Trap205 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 205)
)
ibm3584Trap205.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap205.setStatus(
        "current"
    )

ibm3584Trap206 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 206)
)
ibm3584Trap206.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap206.setStatus(
        "current"
    )

ibm3584Trap207 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 207)
)
ibm3584Trap207.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap207.setStatus(
        "current"
    )

ibm3584Trap208 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 208)
)
ibm3584Trap208.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap208.setStatus(
        "current"
    )

ibm3584Trap209 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 209)
)
ibm3584Trap209.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap209.setStatus(
        "current"
    )

ibm3584Trap210 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 210)
)
ibm3584Trap210.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap210.setStatus(
        "current"
    )

ibm3584Trap211 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 211)
)
ibm3584Trap211.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap211.setStatus(
        "current"
    )

ibm3584Trap212 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 212)
)
ibm3584Trap212.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap212.setStatus(
        "current"
    )

ibm3584Trap213 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 213)
)
ibm3584Trap213.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap213.setStatus(
        "current"
    )

ibm3584Trap214 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 214)
)
ibm3584Trap214.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap214.setStatus(
        "current"
    )

ibm3584Trap215 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 215)
)
ibm3584Trap215.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap215.setStatus(
        "current"
    )

ibm3584Trap216 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 216)
)
ibm3584Trap216.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap216.setStatus(
        "current"
    )

ibm3584Trap217 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 217)
)
ibm3584Trap217.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap217.setStatus(
        "current"
    )

ibm3584Trap218 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 218)
)
ibm3584Trap218.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap218.setStatus(
        "current"
    )

ibm3584Trap219 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 219)
)
ibm3584Trap219.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap219.setStatus(
        "current"
    )

ibm3584Trap220 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 220)
)
ibm3584Trap220.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap220.setStatus(
        "current"
    )

ibm3584Trap221 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 221)
)
ibm3584Trap221.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap221.setStatus(
        "current"
    )

ibm3584Trap222 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 222)
)
ibm3584Trap222.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap222.setStatus(
        "current"
    )

ibm3584Trap223 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 223)
)
ibm3584Trap223.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap223.setStatus(
        "current"
    )

ibm3584Trap224 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 224)
)
ibm3584Trap224.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap224.setStatus(
        "current"
    )

ibm3584Trap225 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 225)
)
ibm3584Trap225.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap225.setStatus(
        "current"
    )

ibm3584Trap226 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 226)
)
ibm3584Trap226.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap226.setStatus(
        "current"
    )

ibm3584Trap227 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 227)
)
ibm3584Trap227.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap227.setStatus(
        "current"
    )

ibm3584Trap228 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 228)
)
ibm3584Trap228.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap228.setStatus(
        "current"
    )

ibm3584Trap229 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 229)
)
ibm3584Trap229.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap229.setStatus(
        "current"
    )

ibm3584Trap230 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 230)
)
ibm3584Trap230.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap230.setStatus(
        "current"
    )

ibm3584Trap231 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 231)
)
ibm3584Trap231.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap231.setStatus(
        "current"
    )

ibm3584Trap232 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 232)
)
ibm3584Trap232.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap232.setStatus(
        "current"
    )

ibm3584Trap233 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 233)
)
ibm3584Trap233.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap233.setStatus(
        "current"
    )

ibm3584Trap234 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 234)
)
ibm3584Trap234.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap234.setStatus(
        "current"
    )

ibm3584Trap235 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 235)
)
ibm3584Trap235.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap235.setStatus(
        "current"
    )

ibm3584Trap236 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 236)
)
ibm3584Trap236.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap236.setStatus(
        "current"
    )

ibm3584Trap237 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 237)
)
ibm3584Trap237.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap237.setStatus(
        "current"
    )

ibm3584Trap238 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 238)
)
ibm3584Trap238.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap238.setStatus(
        "current"
    )

ibm3584Trap239 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 239)
)
ibm3584Trap239.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap239.setStatus(
        "current"
    )

ibm3584Trap240 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 240)
)
ibm3584Trap240.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap240.setStatus(
        "current"
    )

ibm3584Trap241 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 241)
)
ibm3584Trap241.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap241.setStatus(
        "current"
    )

ibm3584Trap242 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 242)
)
ibm3584Trap242.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap242.setStatus(
        "current"
    )

ibm3584Trap243 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 243)
)
ibm3584Trap243.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap243.setStatus(
        "current"
    )

ibm3584Trap244 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 244)
)
ibm3584Trap244.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap244.setStatus(
        "current"
    )

ibm3584Trap245 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 245)
)
ibm3584Trap245.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap245.setStatus(
        "current"
    )

ibm3584Trap246 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 246)
)
ibm3584Trap246.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap246.setStatus(
        "current"
    )

ibm3584Trap250 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 250)
)
ibm3584Trap250.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap250.setStatus(
        "current"
    )

ibm3584Trap251 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 251)
)
ibm3584Trap251.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap251.setStatus(
        "current"
    )

ibm3584Trap252 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 252)
)
ibm3584Trap252.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap252.setStatus(
        "current"
    )

ibm3584Trap253 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 253)
)
ibm3584Trap253.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap253.setStatus(
        "current"
    )

ibm3584Trap254 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 254)
)
ibm3584Trap254.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap254.setStatus(
        "current"
    )

ibm3584Trap255 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 255)
)
ibm3584Trap255.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap255.setStatus(
        "current"
    )

ibm3584Trap256 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 256)
)
ibm3584Trap256.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap256.setStatus(
        "current"
    )

ibm3584Trap257 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 257)
)
ibm3584Trap257.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap257.setStatus(
        "current"
    )

ibm3584Trap258 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 258)
)
ibm3584Trap258.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap258.setStatus(
        "current"
    )

ibm3584Trap259 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 259)
)
ibm3584Trap259.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap259.setStatus(
        "current"
    )

ibm3584Trap260 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 260)
)
ibm3584Trap260.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSKASCASCQ"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsURC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFSC"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSCD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsFFFD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap260.setStatus(
        "current"
    )

ibm3584Trap401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 401)
)
ibm3584Trap401.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap401.setStatus(
        "current"
    )

ibm3584Trap402 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 402)
)
ibm3584Trap402.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap402.setStatus(
        "current"
    )

ibm3584Trap403 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 403)
)
ibm3584Trap403.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap403.setStatus(
        "current"
    )

ibm3584Trap404 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 404)
)
ibm3584Trap404.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap404.setStatus(
        "current"
    )

ibm3584Trap405 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 405)
)
ibm3584Trap405.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap405.setStatus(
        "current"
    )

ibm3584Trap406 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 406)
)
ibm3584Trap406.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap406.setStatus(
        "current"
    )

ibm3584Trap407 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 407)
)
ibm3584Trap407.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap407.setStatus(
        "current"
    )

ibm3584Trap408 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 408)
)
ibm3584Trap408.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap408.setStatus(
        "current"
    )

ibm3584Trap409 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 409)
)
ibm3584Trap409.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap409.setStatus(
        "current"
    )

ibm3584Trap410 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 410)
)
ibm3584Trap410.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap410.setStatus(
        "current"
    )

ibm3584Trap411 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 411)
)
ibm3584Trap411.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap411.setStatus(
        "current"
    )

ibm3584Trap412 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 412)
)
ibm3584Trap412.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap412.setStatus(
        "current"
    )

ibm3584Trap413 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 413)
)
ibm3584Trap413.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsEA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap413.setStatus(
        "current"
    )

ibm3584Trap414 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 414)
)
ibm3584Trap414.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap414.setStatus(
        "current"
    )

ibm3584Trap415 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 415)
)
ibm3584Trap415.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap415.setStatus(
        "current"
    )

ibm3584Trap416 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 416)
)
ibm3584Trap416.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap416.setStatus(
        "current"
    )

ibm3584Trap417 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 417)
)
ibm3584Trap417.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap417.setStatus(
        "current"
    )

ibm3584Trap418 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 418)
)
ibm3584Trap418.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap418.setStatus(
        "current"
    )

ibm3584Trap419 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 419)
)
ibm3584Trap419.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap419.setStatus(
        "current"
    )

ibm3584Trap420 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 420)
)
ibm3584Trap420.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap420.setStatus(
        "current"
    )

ibm3584Trap421 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 421)
)
ibm3584Trap421.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap421.setStatus(
        "current"
    )

ibm3584Trap422 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 422)
)
ibm3584Trap422.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap422.setStatus(
        "current"
    )

ibm3584Trap440 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 440)
)
ibm3584Trap440.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsUserID"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap440.setStatus(
        "current"
    )

ibm3584Trap441 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 441)
)
ibm3584Trap441.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsUserID"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap441.setStatus(
        "current"
    )

ibm3584Trap442 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 442)
)
ibm3584Trap442.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsUserID"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap442.setStatus(
        "current"
    )

ibm3584Trap443 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 443)
)
ibm3584Trap443.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsUserID"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap443.setStatus(
        "current"
    )

ibm3584Trap444 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 444)
)
ibm3584Trap444.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsUserID"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap444.setStatus(
        "current"
    )

ibm3584Trap445 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 445)
)
ibm3584Trap445.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsUserID"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsEA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap445.setStatus(
        "current"
    )

ibm3584Trap446 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 446)
)
ibm3584Trap446.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsUserID"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsVOLSER"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsEA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap446.setStatus(
        "current"
    )

ibm3584Trap447 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 447)
)
ibm3584Trap447.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsUserID"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap447.setStatus(
        "current"
    )

ibm3584Trap448 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 448)
)
ibm3584Trap448.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsUserID"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap448.setStatus(
        "current"
    )

ibm3584Trap449 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 449)
)
ibm3584Trap449.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsUserID"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsEA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap449.setStatus(
        "current"
    )

ibm3584Trap450 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 450)
)
ibm3584Trap450.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsUserID"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsEA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap450.setStatus(
        "current"
    )

ibm3584Trap451 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 451)
)
ibm3584Trap451.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsUserID"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsLL"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsWWNN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsEA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsDrvSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap451.setStatus(
        "current"
    )

ibm3584Trap452 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 0, 452)
)
ibm3584Trap452.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584MIBObjectsMTMNLSN"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTA"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsTD"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsUserID"),
        ("IBM-TS3500-MIBv2", "ibm3584MIBObjectsSeverity"))
)
if mibBuilder.loadTexts:
    ibm3584Trap452.setStatus(
        "current"
    )


# Notifications groups

ibm3584MIBNotificationsGroup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 3, 2, 1)
)
ibm3584MIBNotificationsGroup1.setObjects(
      *(("IBM-TS3500-MIBv2", "ibm3584Trap001"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap002"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap003"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap004"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap005"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap006"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap007"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap008"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap009"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap010"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap011"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap012"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap013"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap014"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap015"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap016"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap017"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap018"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap019"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap020"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap021"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap022"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap023"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap024"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap025"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap026"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap027"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap028"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap029"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap030"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap031"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap032"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap201"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap202"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap203"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap204"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap205"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap206"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap207"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap208"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap209"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap210"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap211"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap212"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap213"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap214"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap215"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap216"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap217"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap218"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap219"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap220"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap221"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap222"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap223"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap224"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap225"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap226"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap227"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap228"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap229"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap230"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap231"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap232"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap233"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap234"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap235"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap236"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap237"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap238"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap239"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap240"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap241"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap242"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap243"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap244"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap245"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap246"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap250"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap251"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap252"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap253"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap254"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap255"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap256"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap257"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap258"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap259"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap260"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap401"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap402"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap403"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap404"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap405"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap406"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap407"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap408"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap409"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap410"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap411"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap412"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap413"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap414"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap415"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap416"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap417"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap418"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap419"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap420"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap421"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap422"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap440"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap441"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap442"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap443"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap444"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap445"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap446"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap447"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap448"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap449"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap450"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap451"),
        ("IBM-TS3500-MIBv2", "ibm3584Trap452"))
)
if mibBuilder.loadTexts:
    ibm3584MIBNotificationsGroup1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ibm3584MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2, 6, 182, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ibm3584MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-TS3500-MIBv2",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "ibm3584": ibm3584,
       "ibm3584MIB": ibm3584MIB,
       "ibm3584MIBTraps": ibm3584MIBTraps,
       "ibm3584Trap001": ibm3584Trap001,
       "ibm3584Trap002": ibm3584Trap002,
       "ibm3584Trap003": ibm3584Trap003,
       "ibm3584Trap004": ibm3584Trap004,
       "ibm3584Trap005": ibm3584Trap005,
       "ibm3584Trap006": ibm3584Trap006,
       "ibm3584Trap007": ibm3584Trap007,
       "ibm3584Trap008": ibm3584Trap008,
       "ibm3584Trap009": ibm3584Trap009,
       "ibm3584Trap010": ibm3584Trap010,
       "ibm3584Trap011": ibm3584Trap011,
       "ibm3584Trap012": ibm3584Trap012,
       "ibm3584Trap013": ibm3584Trap013,
       "ibm3584Trap014": ibm3584Trap014,
       "ibm3584Trap015": ibm3584Trap015,
       "ibm3584Trap016": ibm3584Trap016,
       "ibm3584Trap017": ibm3584Trap017,
       "ibm3584Trap018": ibm3584Trap018,
       "ibm3584Trap019": ibm3584Trap019,
       "ibm3584Trap020": ibm3584Trap020,
       "ibm3584Trap021": ibm3584Trap021,
       "ibm3584Trap022": ibm3584Trap022,
       "ibm3584Trap023": ibm3584Trap023,
       "ibm3584Trap024": ibm3584Trap024,
       "ibm3584Trap025": ibm3584Trap025,
       "ibm3584Trap026": ibm3584Trap026,
       "ibm3584Trap027": ibm3584Trap027,
       "ibm3584Trap028": ibm3584Trap028,
       "ibm3584Trap029": ibm3584Trap029,
       "ibm3584Trap030": ibm3584Trap030,
       "ibm3584Trap031": ibm3584Trap031,
       "ibm3584Trap032": ibm3584Trap032,
       "ibm3584Trap201": ibm3584Trap201,
       "ibm3584Trap202": ibm3584Trap202,
       "ibm3584Trap203": ibm3584Trap203,
       "ibm3584Trap204": ibm3584Trap204,
       "ibm3584Trap205": ibm3584Trap205,
       "ibm3584Trap206": ibm3584Trap206,
       "ibm3584Trap207": ibm3584Trap207,
       "ibm3584Trap208": ibm3584Trap208,
       "ibm3584Trap209": ibm3584Trap209,
       "ibm3584Trap210": ibm3584Trap210,
       "ibm3584Trap211": ibm3584Trap211,
       "ibm3584Trap212": ibm3584Trap212,
       "ibm3584Trap213": ibm3584Trap213,
       "ibm3584Trap214": ibm3584Trap214,
       "ibm3584Trap215": ibm3584Trap215,
       "ibm3584Trap216": ibm3584Trap216,
       "ibm3584Trap217": ibm3584Trap217,
       "ibm3584Trap218": ibm3584Trap218,
       "ibm3584Trap219": ibm3584Trap219,
       "ibm3584Trap220": ibm3584Trap220,
       "ibm3584Trap221": ibm3584Trap221,
       "ibm3584Trap222": ibm3584Trap222,
       "ibm3584Trap223": ibm3584Trap223,
       "ibm3584Trap224": ibm3584Trap224,
       "ibm3584Trap225": ibm3584Trap225,
       "ibm3584Trap226": ibm3584Trap226,
       "ibm3584Trap227": ibm3584Trap227,
       "ibm3584Trap228": ibm3584Trap228,
       "ibm3584Trap229": ibm3584Trap229,
       "ibm3584Trap230": ibm3584Trap230,
       "ibm3584Trap231": ibm3584Trap231,
       "ibm3584Trap232": ibm3584Trap232,
       "ibm3584Trap233": ibm3584Trap233,
       "ibm3584Trap234": ibm3584Trap234,
       "ibm3584Trap235": ibm3584Trap235,
       "ibm3584Trap236": ibm3584Trap236,
       "ibm3584Trap237": ibm3584Trap237,
       "ibm3584Trap238": ibm3584Trap238,
       "ibm3584Trap239": ibm3584Trap239,
       "ibm3584Trap240": ibm3584Trap240,
       "ibm3584Trap241": ibm3584Trap241,
       "ibm3584Trap242": ibm3584Trap242,
       "ibm3584Trap243": ibm3584Trap243,
       "ibm3584Trap244": ibm3584Trap244,
       "ibm3584Trap245": ibm3584Trap245,
       "ibm3584Trap246": ibm3584Trap246,
       "ibm3584Trap250": ibm3584Trap250,
       "ibm3584Trap251": ibm3584Trap251,
       "ibm3584Trap252": ibm3584Trap252,
       "ibm3584Trap253": ibm3584Trap253,
       "ibm3584Trap254": ibm3584Trap254,
       "ibm3584Trap255": ibm3584Trap255,
       "ibm3584Trap256": ibm3584Trap256,
       "ibm3584Trap257": ibm3584Trap257,
       "ibm3584Trap258": ibm3584Trap258,
       "ibm3584Trap259": ibm3584Trap259,
       "ibm3584Trap260": ibm3584Trap260,
       "ibm3584Trap401": ibm3584Trap401,
       "ibm3584Trap402": ibm3584Trap402,
       "ibm3584Trap403": ibm3584Trap403,
       "ibm3584Trap404": ibm3584Trap404,
       "ibm3584Trap405": ibm3584Trap405,
       "ibm3584Trap406": ibm3584Trap406,
       "ibm3584Trap407": ibm3584Trap407,
       "ibm3584Trap408": ibm3584Trap408,
       "ibm3584Trap409": ibm3584Trap409,
       "ibm3584Trap410": ibm3584Trap410,
       "ibm3584Trap411": ibm3584Trap411,
       "ibm3584Trap412": ibm3584Trap412,
       "ibm3584Trap413": ibm3584Trap413,
       "ibm3584Trap414": ibm3584Trap414,
       "ibm3584Trap415": ibm3584Trap415,
       "ibm3584Trap416": ibm3584Trap416,
       "ibm3584Trap417": ibm3584Trap417,
       "ibm3584Trap418": ibm3584Trap418,
       "ibm3584Trap419": ibm3584Trap419,
       "ibm3584Trap420": ibm3584Trap420,
       "ibm3584Trap421": ibm3584Trap421,
       "ibm3584Trap422": ibm3584Trap422,
       "ibm3584Trap440": ibm3584Trap440,
       "ibm3584Trap441": ibm3584Trap441,
       "ibm3584Trap442": ibm3584Trap442,
       "ibm3584Trap443": ibm3584Trap443,
       "ibm3584Trap444": ibm3584Trap444,
       "ibm3584Trap445": ibm3584Trap445,
       "ibm3584Trap446": ibm3584Trap446,
       "ibm3584Trap447": ibm3584Trap447,
       "ibm3584Trap448": ibm3584Trap448,
       "ibm3584Trap449": ibm3584Trap449,
       "ibm3584Trap450": ibm3584Trap450,
       "ibm3584Trap451": ibm3584Trap451,
       "ibm3584Trap452": ibm3584Trap452,
       "ibm3584MIBAdmin": ibm3584MIBAdmin,
       "ibm3584MIBObjects": ibm3584MIBObjects,
       "ibm3584MIBGroupMTMNLSN": ibm3584MIBGroupMTMNLSN,
       "ibm3584MIBObjectsMTMNLSN": ibm3584MIBObjectsMTMNLSN,
       "ibm3584MIBGroupSKASCASCQ": ibm3584MIBGroupSKASCASCQ,
       "ibm3584MIBObjectsSKASCASCQ": ibm3584MIBObjectsSKASCASCQ,
       "ibm3584MIBGroupHECHECQ": ibm3584MIBGroupHECHECQ,
       "ibm3584MIBObjectsHECHECQ": ibm3584MIBObjectsHECHECQ,
       "ibm3584MIBGroupTA": ibm3584MIBGroupTA,
       "ibm3584MIBObjectsTA": ibm3584MIBObjectsTA,
       "ibm3584MIBGroupURC": ibm3584MIBGroupURC,
       "ibm3584MIBObjectsURC": ibm3584MIBObjectsURC,
       "ibm3584MIBGroupFFFD": ibm3584MIBGroupFFFD,
       "ibm3584MIBObjectsFFFD": ibm3584MIBObjectsFFFD,
       "ibm3584MIBGroupTD": ibm3584MIBGroupTD,
       "ibm3584MIBObjectsTD": ibm3584MIBObjectsTD,
       "ibm3584MIBGroupFSC": ibm3584MIBGroupFSC,
       "ibm3584MIBObjectsFSC": ibm3584MIBObjectsFSC,
       "ibm3584MIBGroupSCD": ibm3584MIBGroupSCD,
       "ibm3584MIBObjectsSCD": ibm3584MIBObjectsSCD,
       "ibm3584MIBGroupVOLSER": ibm3584MIBGroupVOLSER,
       "ibm3584MIBObjectsVOLSER": ibm3584MIBObjectsVOLSER,
       "ibm3584MIBGroupLL": ibm3584MIBGroupLL,
       "ibm3584MIBObjectsLL": ibm3584MIBObjectsLL,
       "ibm3584MIBGroupWWNN": ibm3584MIBGroupWWNN,
       "ibm3584MIBObjectsWWNN": ibm3584MIBObjectsWWNN,
       "ibm3584MIBGroupEA": ibm3584MIBGroupEA,
       "ibm3584MIBObjectsEA": ibm3584MIBObjectsEA,
       "ibm3584MIBGroupDrvSN": ibm3584MIBGroupDrvSN,
       "ibm3584MIBObjectsDrvSN": ibm3584MIBObjectsDrvSN,
       "ibm3584MIBSeverity": ibm3584MIBSeverity,
       "ibm3584MIBObjectsSeverity": ibm3584MIBObjectsSeverity,
       "ibm3584MIBUserID": ibm3584MIBUserID,
       "ibm3584MIBObjectsUserID": ibm3584MIBObjectsUserID,
       "ibm3584MIBConformance": ibm3584MIBConformance,
       "ibm3584MIBCompliances": ibm3584MIBCompliances,
       "ibm3584MIBCompliance": ibm3584MIBCompliance,
       "ibm3584MIBGroups": ibm3584MIBGroups,
       "ibm3584MIBNotificationsGroup1": ibm3584MIBNotificationsGroup1,
       "ibm3584MIBObjectsGroup": ibm3584MIBObjectsGroup}
)

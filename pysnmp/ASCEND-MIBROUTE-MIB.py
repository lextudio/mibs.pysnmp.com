# SNMP MIB module (ASCEND-MIBROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:07 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibrouteProfile_ObjectIdentity = ObjectIdentity
mibrouteProfile = _MibrouteProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 105)
)
_MibrouteProfileTable_Object = MibTable
mibrouteProfileTable = _MibrouteProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 105, 1)
)
if mibBuilder.loadTexts:
    mibrouteProfileTable.setStatus("mandatory")
_MibrouteProfileEntry_Object = MibTableRow
mibrouteProfileEntry = _MibrouteProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 105, 1, 1)
)
mibrouteProfileEntry.setIndexNames(
    (0, "ASCEND-MIBROUTE-MIB", "routeProfile-Name"),
)
if mibBuilder.loadTexts:
    mibrouteProfileEntry.setStatus("mandatory")
_RouteProfile_Name_Type = DisplayString
_RouteProfile_Name_Object = MibScalar
routeProfile_Name = _RouteProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 105, 1, 1, 1),
    _RouteProfile_Name_Type()
)
routeProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeProfile_Name.setStatus("mandatory")
_RouteProfile_DestAddress_Type = IpAddress
_RouteProfile_DestAddress_Object = MibScalar
routeProfile_DestAddress = _RouteProfile_DestAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 105, 1, 1, 2),
    _RouteProfile_DestAddress_Type()
)
routeProfile_DestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeProfile_DestAddress.setStatus("mandatory")
_RouteProfile_GatewayAddress_Type = IpAddress
_RouteProfile_GatewayAddress_Object = MibScalar
routeProfile_GatewayAddress = _RouteProfile_GatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 105, 1, 1, 3),
    _RouteProfile_GatewayAddress_Type()
)
routeProfile_GatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeProfile_GatewayAddress.setStatus("mandatory")
_RouteProfile_Metric_Type = Integer32
_RouteProfile_Metric_Object = MibScalar
routeProfile_Metric = _RouteProfile_Metric_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 105, 1, 1, 4),
    _RouteProfile_Metric_Type()
)
routeProfile_Metric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeProfile_Metric.setStatus("mandatory")
_RouteProfile_Cost_Type = Integer32
_RouteProfile_Cost_Object = MibScalar
routeProfile_Cost = _RouteProfile_Cost_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 105, 1, 1, 5),
    _RouteProfile_Cost_Type()
)
routeProfile_Cost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeProfile_Cost.setStatus("mandatory")
_RouteProfile_Preference_Type = Integer32
_RouteProfile_Preference_Object = MibScalar
routeProfile_Preference = _RouteProfile_Preference_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 105, 1, 1, 6),
    _RouteProfile_Preference_Type()
)
routeProfile_Preference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeProfile_Preference.setStatus("mandatory")


class _RouteProfile_ThirdParty_Type(Integer32):
    """Custom type routeProfile_ThirdParty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RouteProfile_ThirdParty_Type.__name__ = "Integer32"
_RouteProfile_ThirdParty_Object = MibScalar
routeProfile_ThirdParty = _RouteProfile_ThirdParty_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 105, 1, 1, 7),
    _RouteProfile_ThirdParty_Type()
)
routeProfile_ThirdParty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeProfile_ThirdParty.setStatus("mandatory")


class _RouteProfile_AseType_Type(Integer32):
    """Custom type routeProfile_AseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_RouteProfile_AseType_Type.__name__ = "Integer32"
_RouteProfile_AseType_Object = MibScalar
routeProfile_AseType = _RouteProfile_AseType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 105, 1, 1, 8),
    _RouteProfile_AseType_Type()
)
routeProfile_AseType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeProfile_AseType.setStatus("mandatory")
_RouteProfile_AseTag_Type = DisplayString
_RouteProfile_AseTag_Object = MibScalar
routeProfile_AseTag = _RouteProfile_AseTag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 105, 1, 1, 9),
    _RouteProfile_AseTag_Type()
)
routeProfile_AseTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeProfile_AseTag.setStatus("mandatory")


class _RouteProfile_PrivateRoute_Type(Integer32):
    """Custom type routeProfile_PrivateRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RouteProfile_PrivateRoute_Type.__name__ = "Integer32"
_RouteProfile_PrivateRoute_Object = MibScalar
routeProfile_PrivateRoute = _RouteProfile_PrivateRoute_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 105, 1, 1, 10),
    _RouteProfile_PrivateRoute_Type()
)
routeProfile_PrivateRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeProfile_PrivateRoute.setStatus("mandatory")


class _RouteProfile_ActiveRoute_Type(Integer32):
    """Custom type routeProfile_ActiveRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RouteProfile_ActiveRoute_Type.__name__ = "Integer32"
_RouteProfile_ActiveRoute_Object = MibScalar
routeProfile_ActiveRoute = _RouteProfile_ActiveRoute_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 105, 1, 1, 11),
    _RouteProfile_ActiveRoute_Type()
)
routeProfile_ActiveRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeProfile_ActiveRoute.setStatus("mandatory")


class _RouteProfile_Ase7Adv_Type(Integer32):
    """Custom type routeProfile_Ase7Adv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("doNotAdvertise", 3),
          ("n-A", 1))
    )


_RouteProfile_Ase7Adv_Type.__name__ = "Integer32"
_RouteProfile_Ase7Adv_Object = MibScalar
routeProfile_Ase7Adv = _RouteProfile_Ase7Adv_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 105, 1, 1, 12),
    _RouteProfile_Ase7Adv_Type()
)
routeProfile_Ase7Adv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeProfile_Ase7Adv.setStatus("mandatory")
_RouteProfile_Vrouter_Type = DisplayString
_RouteProfile_Vrouter_Object = MibScalar
routeProfile_Vrouter = _RouteProfile_Vrouter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 105, 1, 1, 13),
    _RouteProfile_Vrouter_Type()
)
routeProfile_Vrouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeProfile_Vrouter.setStatus("mandatory")
_RouteProfile_InterVrouter_Type = DisplayString
_RouteProfile_InterVrouter_Object = MibScalar
routeProfile_InterVrouter = _RouteProfile_InterVrouter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 105, 1, 1, 14),
    _RouteProfile_InterVrouter_Type()
)
routeProfile_InterVrouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeProfile_InterVrouter.setStatus("mandatory")


class _RouteProfile_Action_o_Type(Integer32):
    """Custom type routeProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_RouteProfile_Action_o_Type.__name__ = "Integer32"
_RouteProfile_Action_o_Object = MibScalar
routeProfile_Action_o = _RouteProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 105, 1, 1, 15),
    _RouteProfile_Action_o_Type()
)
routeProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeProfile_Action_o.setStatus("mandatory")
_RouteProfile_Netmask_Type = IpAddress
_RouteProfile_Netmask_Object = MibScalar
routeProfile_Netmask = _RouteProfile_Netmask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 105, 1, 1, 16),
    _RouteProfile_Netmask_Type()
)
routeProfile_Netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeProfile_Netmask.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBROUTE-MIB",
    **{"DisplayString": DisplayString,
       "mibrouteProfile": mibrouteProfile,
       "mibrouteProfileTable": mibrouteProfileTable,
       "mibrouteProfileEntry": mibrouteProfileEntry,
       "routeProfile-Name": routeProfile_Name,
       "routeProfile-DestAddress": routeProfile_DestAddress,
       "routeProfile-GatewayAddress": routeProfile_GatewayAddress,
       "routeProfile-Metric": routeProfile_Metric,
       "routeProfile-Cost": routeProfile_Cost,
       "routeProfile-Preference": routeProfile_Preference,
       "routeProfile-ThirdParty": routeProfile_ThirdParty,
       "routeProfile-AseType": routeProfile_AseType,
       "routeProfile-AseTag": routeProfile_AseTag,
       "routeProfile-PrivateRoute": routeProfile_PrivateRoute,
       "routeProfile-ActiveRoute": routeProfile_ActiveRoute,
       "routeProfile-Ase7Adv": routeProfile_Ase7Adv,
       "routeProfile-Vrouter": routeProfile_Vrouter,
       "routeProfile-InterVrouter": routeProfile_InterVrouter,
       "routeProfile-Action-o": routeProfile_Action_o,
       "routeProfile-Netmask": routeProfile_Netmask}
)

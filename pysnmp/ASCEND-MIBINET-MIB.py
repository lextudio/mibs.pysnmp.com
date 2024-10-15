# SNMP MIB module (ASCEND-MIBINET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBINET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:42 2024
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

_MibinternetProfile_ObjectIdentity = ObjectIdentity
mibinternetProfile = _MibinternetProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 1)
)
_MibinternetProfileTable_Object = MibTable
mibinternetProfileTable = _MibinternetProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1)
)
if mibBuilder.loadTexts:
    mibinternetProfileTable.setStatus("mandatory")
_MibinternetProfileEntry_Object = MibTableRow
mibinternetProfileEntry = _MibinternetProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1)
)
mibinternetProfileEntry.setIndexNames(
    (0, "ASCEND-MIBINET-MIB", "internetProfile-Station"),
)
if mibBuilder.loadTexts:
    mibinternetProfileEntry.setStatus("mandatory")
_InternetProfile_Station_Type = DisplayString
_InternetProfile_Station_Object = MibScalar
internetProfile_Station = _InternetProfile_Station_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 1),
    _InternetProfile_Station_Type()
)
internetProfile_Station.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_Station.setStatus("mandatory")


class _InternetProfile_Active_Type(Integer32):
    """Custom type internetProfile_Active based on Integer32"""
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


_InternetProfile_Active_Type.__name__ = "Integer32"
_InternetProfile_Active_Object = MibScalar
internetProfile_Active = _InternetProfile_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 2),
    _InternetProfile_Active_Type()
)
internetProfile_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_Active.setStatus("mandatory")


class _InternetProfile_EncapsulationProtocol_Type(Integer32):
    """Custom type internetProfile_EncapsulationProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              17,
              18,
              21,
              22,
              23,
              24,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("ara", 15),
          ("atm", 21),
          ("atmCircuit", 24),
          ("atmFrameRelayCircuit", 22),
          ("atmIma", 28),
          ("atmSvcSig", 27),
          ("combinet", 9),
          ("cslip", 5),
          ("dtpt", 8),
          ("euraw", 12),
          ("euui", 13),
          ("frameRelay", 6),
          ("frameRelayCircuit", 10),
          ("hdlcNrm", 23),
          ("mp", 2),
          ("mpp", 1),
          ("ppp", 3),
          ("rfc1356X25", 14),
          ("slip", 4),
          ("t3pos", 17),
          ("tcpRaw", 7),
          ("visa2", 26),
          ("x25pad", 11),
          ("x32", 18))
    )


_InternetProfile_EncapsulationProtocol_Type.__name__ = "Integer32"
_InternetProfile_EncapsulationProtocol_Object = MibScalar
internetProfile_EncapsulationProtocol = _InternetProfile_EncapsulationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 3),
    _InternetProfile_EncapsulationProtocol_Type()
)
internetProfile_EncapsulationProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_EncapsulationProtocol.setStatus("mandatory")


class _InternetProfile_CalledNumberType_Type(Integer32):
    """Custom type internetProfile_CalledNumberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("abbrev", 7),
          ("international", 2),
          ("local", 5),
          ("national", 3),
          ("networkSpecific", 4),
          ("unknown", 1))
    )


_InternetProfile_CalledNumberType_Type.__name__ = "Integer32"
_InternetProfile_CalledNumberType_Object = MibScalar
internetProfile_CalledNumberType = _InternetProfile_CalledNumberType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 4),
    _InternetProfile_CalledNumberType_Type()
)
internetProfile_CalledNumberType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_CalledNumberType.setStatus("mandatory")
_InternetProfile_DialNumber_Type = DisplayString
_InternetProfile_DialNumber_Object = MibScalar
internetProfile_DialNumber = _InternetProfile_DialNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 5),
    _InternetProfile_DialNumber_Type()
)
internetProfile_DialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_DialNumber.setStatus("mandatory")
_InternetProfile_Clid_Type = DisplayString
_InternetProfile_Clid_Object = MibScalar
internetProfile_Clid = _InternetProfile_Clid_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 6),
    _InternetProfile_Clid_Type()
)
internetProfile_Clid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_Clid.setStatus("mandatory")


class _InternetProfile_IpOptions_IpRoutingEnabled_Type(Integer32):
    """Custom type internetProfile_IpOptions_IpRoutingEnabled based on Integer32"""
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


_InternetProfile_IpOptions_IpRoutingEnabled_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_IpRoutingEnabled_Object = MibScalar
internetProfile_IpOptions_IpRoutingEnabled = _InternetProfile_IpOptions_IpRoutingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 7),
    _InternetProfile_IpOptions_IpRoutingEnabled_Type()
)
internetProfile_IpOptions_IpRoutingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_IpRoutingEnabled.setStatus("mandatory")


class _InternetProfile_IpOptions_VjHeaderPrediction_Type(Integer32):
    """Custom type internetProfile_IpOptions_VjHeaderPrediction based on Integer32"""
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


_InternetProfile_IpOptions_VjHeaderPrediction_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_VjHeaderPrediction_Object = MibScalar
internetProfile_IpOptions_VjHeaderPrediction = _InternetProfile_IpOptions_VjHeaderPrediction_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 8),
    _InternetProfile_IpOptions_VjHeaderPrediction_Type()
)
internetProfile_IpOptions_VjHeaderPrediction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_VjHeaderPrediction.setStatus("mandatory")
_InternetProfile_IpOptions_RemoteAddress_Type = IpAddress
_InternetProfile_IpOptions_RemoteAddress_Object = MibScalar
internetProfile_IpOptions_RemoteAddress = _InternetProfile_IpOptions_RemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 9),
    _InternetProfile_IpOptions_RemoteAddress_Type()
)
internetProfile_IpOptions_RemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_RemoteAddress.setStatus("mandatory")
_InternetProfile_IpOptions_NetmaskRemote_Type = IpAddress
_InternetProfile_IpOptions_NetmaskRemote_Object = MibScalar
internetProfile_IpOptions_NetmaskRemote = _InternetProfile_IpOptions_NetmaskRemote_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 10),
    _InternetProfile_IpOptions_NetmaskRemote_Type()
)
internetProfile_IpOptions_NetmaskRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_NetmaskRemote.setStatus("mandatory")
_InternetProfile_IpOptions_LocalAddress_Type = IpAddress
_InternetProfile_IpOptions_LocalAddress_Object = MibScalar
internetProfile_IpOptions_LocalAddress = _InternetProfile_IpOptions_LocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 11),
    _InternetProfile_IpOptions_LocalAddress_Type()
)
internetProfile_IpOptions_LocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_LocalAddress.setStatus("mandatory")
_InternetProfile_IpOptions_NetmaskLocal_Type = IpAddress
_InternetProfile_IpOptions_NetmaskLocal_Object = MibScalar
internetProfile_IpOptions_NetmaskLocal = _InternetProfile_IpOptions_NetmaskLocal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 12),
    _InternetProfile_IpOptions_NetmaskLocal_Type()
)
internetProfile_IpOptions_NetmaskLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_NetmaskLocal.setStatus("mandatory")
_InternetProfile_IpOptions_RoutingMetric_Type = Integer32
_InternetProfile_IpOptions_RoutingMetric_Object = MibScalar
internetProfile_IpOptions_RoutingMetric = _InternetProfile_IpOptions_RoutingMetric_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 13),
    _InternetProfile_IpOptions_RoutingMetric_Type()
)
internetProfile_IpOptions_RoutingMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_RoutingMetric.setStatus("mandatory")
_InternetProfile_IpOptions_Preference_Type = Integer32
_InternetProfile_IpOptions_Preference_Object = MibScalar
internetProfile_IpOptions_Preference = _InternetProfile_IpOptions_Preference_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 14),
    _InternetProfile_IpOptions_Preference_Type()
)
internetProfile_IpOptions_Preference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_Preference.setStatus("mandatory")
_InternetProfile_IpOptions_DownPreference_Type = Integer32
_InternetProfile_IpOptions_DownPreference_Object = MibScalar
internetProfile_IpOptions_DownPreference = _InternetProfile_IpOptions_DownPreference_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 15),
    _InternetProfile_IpOptions_DownPreference_Type()
)
internetProfile_IpOptions_DownPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_DownPreference.setStatus("mandatory")


class _InternetProfile_IpOptions_PrivateRoute_Type(Integer32):
    """Custom type internetProfile_IpOptions_PrivateRoute based on Integer32"""
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


_InternetProfile_IpOptions_PrivateRoute_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_PrivateRoute_Object = MibScalar
internetProfile_IpOptions_PrivateRoute = _InternetProfile_IpOptions_PrivateRoute_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 16),
    _InternetProfile_IpOptions_PrivateRoute_Type()
)
internetProfile_IpOptions_PrivateRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_PrivateRoute.setStatus("mandatory")


class _InternetProfile_IpOptions_MulticastAllowed_Type(Integer32):
    """Custom type internetProfile_IpOptions_MulticastAllowed based on Integer32"""
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


_InternetProfile_IpOptions_MulticastAllowed_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_MulticastAllowed_Object = MibScalar
internetProfile_IpOptions_MulticastAllowed = _InternetProfile_IpOptions_MulticastAllowed_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 17),
    _InternetProfile_IpOptions_MulticastAllowed_Type()
)
internetProfile_IpOptions_MulticastAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_MulticastAllowed.setStatus("mandatory")
_InternetProfile_IpOptions_AddressPool_Type = Integer32
_InternetProfile_IpOptions_AddressPool_Object = MibScalar
internetProfile_IpOptions_AddressPool = _InternetProfile_IpOptions_AddressPool_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 18),
    _InternetProfile_IpOptions_AddressPool_Type()
)
internetProfile_IpOptions_AddressPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_AddressPool.setStatus("mandatory")
_InternetProfile_IpOptions_IpDirect_Type = IpAddress
_InternetProfile_IpOptions_IpDirect_Object = MibScalar
internetProfile_IpOptions_IpDirect = _InternetProfile_IpOptions_IpDirect_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 19),
    _InternetProfile_IpOptions_IpDirect_Type()
)
internetProfile_IpOptions_IpDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_IpDirect.setStatus("mandatory")


class _InternetProfile_IpOptions_Rip_Type(Integer32):
    """Custom type internetProfile_IpOptions_Rip based on Integer32"""
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
        *(("routingOff", 1),
          ("routingRecvOnly", 3),
          ("routingRecvOnlyV2", 6),
          ("routingSendAndRecv", 4),
          ("routingSendAndRecvV2", 7),
          ("routingSendOnly", 2),
          ("routingSendOnlyV2", 5))
    )


_InternetProfile_IpOptions_Rip_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_Rip_Object = MibScalar
internetProfile_IpOptions_Rip = _InternetProfile_IpOptions_Rip_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 20),
    _InternetProfile_IpOptions_Rip_Type()
)
internetProfile_IpOptions_Rip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_Rip.setStatus("mandatory")
_InternetProfile_IpOptions_RouteFilter_Type = DisplayString
_InternetProfile_IpOptions_RouteFilter_Object = MibScalar
internetProfile_IpOptions_RouteFilter = _InternetProfile_IpOptions_RouteFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 21),
    _InternetProfile_IpOptions_RouteFilter_Type()
)
internetProfile_IpOptions_RouteFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_RouteFilter.setStatus("mandatory")


class _InternetProfile_IpOptions_SourceIpCheck_Type(Integer32):
    """Custom type internetProfile_IpOptions_SourceIpCheck based on Integer32"""
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


_InternetProfile_IpOptions_SourceIpCheck_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_SourceIpCheck_Object = MibScalar
internetProfile_IpOptions_SourceIpCheck = _InternetProfile_IpOptions_SourceIpCheck_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 22),
    _InternetProfile_IpOptions_SourceIpCheck_Type()
)
internetProfile_IpOptions_SourceIpCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_SourceIpCheck.setStatus("mandatory")


class _InternetProfile_IpOptions_OspfOptions_Active_Type(Integer32):
    """Custom type internetProfile_IpOptions_OspfOptions_Active based on Integer32"""
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


_InternetProfile_IpOptions_OspfOptions_Active_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_OspfOptions_Active_Object = MibScalar
internetProfile_IpOptions_OspfOptions_Active = _InternetProfile_IpOptions_OspfOptions_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 23),
    _InternetProfile_IpOptions_OspfOptions_Active_Type()
)
internetProfile_IpOptions_OspfOptions_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_Active.setStatus("mandatory")
_InternetProfile_IpOptions_OspfOptions_Area_Type = IpAddress
_InternetProfile_IpOptions_OspfOptions_Area_Object = MibScalar
internetProfile_IpOptions_OspfOptions_Area = _InternetProfile_IpOptions_OspfOptions_Area_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 24),
    _InternetProfile_IpOptions_OspfOptions_Area_Type()
)
internetProfile_IpOptions_OspfOptions_Area.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_Area.setStatus("mandatory")


class _InternetProfile_IpOptions_OspfOptions_AreaType_Type(Integer32):
    """Custom type internetProfile_IpOptions_OspfOptions_AreaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nSSA", 3),
          ("normal", 1),
          ("stub", 2))
    )


_InternetProfile_IpOptions_OspfOptions_AreaType_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_OspfOptions_AreaType_Object = MibScalar
internetProfile_IpOptions_OspfOptions_AreaType = _InternetProfile_IpOptions_OspfOptions_AreaType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 25),
    _InternetProfile_IpOptions_OspfOptions_AreaType_Type()
)
internetProfile_IpOptions_OspfOptions_AreaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_AreaType.setStatus("mandatory")
_InternetProfile_IpOptions_OspfOptions_HelloInterval_Type = Integer32
_InternetProfile_IpOptions_OspfOptions_HelloInterval_Object = MibScalar
internetProfile_IpOptions_OspfOptions_HelloInterval = _InternetProfile_IpOptions_OspfOptions_HelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 26),
    _InternetProfile_IpOptions_OspfOptions_HelloInterval_Type()
)
internetProfile_IpOptions_OspfOptions_HelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_HelloInterval.setStatus("mandatory")
_InternetProfile_IpOptions_OspfOptions_DeadInterval_Type = Integer32
_InternetProfile_IpOptions_OspfOptions_DeadInterval_Object = MibScalar
internetProfile_IpOptions_OspfOptions_DeadInterval = _InternetProfile_IpOptions_OspfOptions_DeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 27),
    _InternetProfile_IpOptions_OspfOptions_DeadInterval_Type()
)
internetProfile_IpOptions_OspfOptions_DeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_DeadInterval.setStatus("mandatory")
_InternetProfile_IpOptions_OspfOptions_Priority_Type = Integer32
_InternetProfile_IpOptions_OspfOptions_Priority_Object = MibScalar
internetProfile_IpOptions_OspfOptions_Priority = _InternetProfile_IpOptions_OspfOptions_Priority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 28),
    _InternetProfile_IpOptions_OspfOptions_Priority_Type()
)
internetProfile_IpOptions_OspfOptions_Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_Priority.setStatus("mandatory")


class _InternetProfile_IpOptions_OspfOptions_AuthenType_Type(Integer32):
    """Custom type internetProfile_IpOptions_OspfOptions_AuthenType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("none", 1),
          ("simple", 2))
    )


_InternetProfile_IpOptions_OspfOptions_AuthenType_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_OspfOptions_AuthenType_Object = MibScalar
internetProfile_IpOptions_OspfOptions_AuthenType = _InternetProfile_IpOptions_OspfOptions_AuthenType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 29),
    _InternetProfile_IpOptions_OspfOptions_AuthenType_Type()
)
internetProfile_IpOptions_OspfOptions_AuthenType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_AuthenType.setStatus("mandatory")
_InternetProfile_IpOptions_OspfOptions_AuthKey_Type = DisplayString
_InternetProfile_IpOptions_OspfOptions_AuthKey_Object = MibScalar
internetProfile_IpOptions_OspfOptions_AuthKey = _InternetProfile_IpOptions_OspfOptions_AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 30),
    _InternetProfile_IpOptions_OspfOptions_AuthKey_Type()
)
internetProfile_IpOptions_OspfOptions_AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_AuthKey.setStatus("mandatory")
_InternetProfile_IpOptions_OspfOptions_KeyId_Type = Integer32
_InternetProfile_IpOptions_OspfOptions_KeyId_Object = MibScalar
internetProfile_IpOptions_OspfOptions_KeyId = _InternetProfile_IpOptions_OspfOptions_KeyId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 31),
    _InternetProfile_IpOptions_OspfOptions_KeyId_Type()
)
internetProfile_IpOptions_OspfOptions_KeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_KeyId.setStatus("mandatory")
_InternetProfile_IpOptions_OspfOptions_Cost_Type = Integer32
_InternetProfile_IpOptions_OspfOptions_Cost_Object = MibScalar
internetProfile_IpOptions_OspfOptions_Cost = _InternetProfile_IpOptions_OspfOptions_Cost_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 32),
    _InternetProfile_IpOptions_OspfOptions_Cost_Type()
)
internetProfile_IpOptions_OspfOptions_Cost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_Cost.setStatus("mandatory")
_InternetProfile_IpOptions_OspfOptions_DownCost_Type = Integer32
_InternetProfile_IpOptions_OspfOptions_DownCost_Object = MibScalar
internetProfile_IpOptions_OspfOptions_DownCost = _InternetProfile_IpOptions_OspfOptions_DownCost_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 33),
    _InternetProfile_IpOptions_OspfOptions_DownCost_Type()
)
internetProfile_IpOptions_OspfOptions_DownCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_DownCost.setStatus("mandatory")


class _InternetProfile_IpOptions_OspfOptions_AseType_Type(Integer32):
    """Custom type internetProfile_IpOptions_OspfOptions_AseType based on Integer32"""
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


_InternetProfile_IpOptions_OspfOptions_AseType_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_OspfOptions_AseType_Object = MibScalar
internetProfile_IpOptions_OspfOptions_AseType = _InternetProfile_IpOptions_OspfOptions_AseType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 34),
    _InternetProfile_IpOptions_OspfOptions_AseType_Type()
)
internetProfile_IpOptions_OspfOptions_AseType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_AseType.setStatus("mandatory")
_InternetProfile_IpOptions_OspfOptions_AseTag_Type = DisplayString
_InternetProfile_IpOptions_OspfOptions_AseTag_Object = MibScalar
internetProfile_IpOptions_OspfOptions_AseTag = _InternetProfile_IpOptions_OspfOptions_AseTag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 35),
    _InternetProfile_IpOptions_OspfOptions_AseTag_Type()
)
internetProfile_IpOptions_OspfOptions_AseTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_AseTag.setStatus("mandatory")
_InternetProfile_IpOptions_OspfOptions_TransitDelay_Type = Integer32
_InternetProfile_IpOptions_OspfOptions_TransitDelay_Object = MibScalar
internetProfile_IpOptions_OspfOptions_TransitDelay = _InternetProfile_IpOptions_OspfOptions_TransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 36),
    _InternetProfile_IpOptions_OspfOptions_TransitDelay_Type()
)
internetProfile_IpOptions_OspfOptions_TransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_TransitDelay.setStatus("mandatory")
_InternetProfile_IpOptions_OspfOptions_RetransmitInterval_Type = Integer32
_InternetProfile_IpOptions_OspfOptions_RetransmitInterval_Object = MibScalar
internetProfile_IpOptions_OspfOptions_RetransmitInterval = _InternetProfile_IpOptions_OspfOptions_RetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 37),
    _InternetProfile_IpOptions_OspfOptions_RetransmitInterval_Type()
)
internetProfile_IpOptions_OspfOptions_RetransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_RetransmitInterval.setStatus("mandatory")


class _InternetProfile_IpOptions_OspfOptions_NonMulticast_Type(Integer32):
    """Custom type internetProfile_IpOptions_OspfOptions_NonMulticast based on Integer32"""
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


_InternetProfile_IpOptions_OspfOptions_NonMulticast_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_OspfOptions_NonMulticast_Object = MibScalar
internetProfile_IpOptions_OspfOptions_NonMulticast = _InternetProfile_IpOptions_OspfOptions_NonMulticast_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 38),
    _InternetProfile_IpOptions_OspfOptions_NonMulticast_Type()
)
internetProfile_IpOptions_OspfOptions_NonMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_NonMulticast.setStatus("mandatory")
_InternetProfile_IpOptions_MulticastRateLimit_Type = Integer32
_InternetProfile_IpOptions_MulticastRateLimit_Object = MibScalar
internetProfile_IpOptions_MulticastRateLimit = _InternetProfile_IpOptions_MulticastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 39),
    _InternetProfile_IpOptions_MulticastRateLimit_Type()
)
internetProfile_IpOptions_MulticastRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_MulticastRateLimit.setStatus("mandatory")
_InternetProfile_IpOptions_MulticastGroupLeaveDelay_Type = Integer32
_InternetProfile_IpOptions_MulticastGroupLeaveDelay_Object = MibScalar
internetProfile_IpOptions_MulticastGroupLeaveDelay = _InternetProfile_IpOptions_MulticastGroupLeaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 40),
    _InternetProfile_IpOptions_MulticastGroupLeaveDelay_Type()
)
internetProfile_IpOptions_MulticastGroupLeaveDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_MulticastGroupLeaveDelay.setStatus("mandatory")
_InternetProfile_IpOptions_ClientDnsPrimaryAddr_Type = IpAddress
_InternetProfile_IpOptions_ClientDnsPrimaryAddr_Object = MibScalar
internetProfile_IpOptions_ClientDnsPrimaryAddr = _InternetProfile_IpOptions_ClientDnsPrimaryAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 41),
    _InternetProfile_IpOptions_ClientDnsPrimaryAddr_Type()
)
internetProfile_IpOptions_ClientDnsPrimaryAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_ClientDnsPrimaryAddr.setStatus("mandatory")
_InternetProfile_IpOptions_ClientDnsSecondaryAddr_Type = IpAddress
_InternetProfile_IpOptions_ClientDnsSecondaryAddr_Object = MibScalar
internetProfile_IpOptions_ClientDnsSecondaryAddr = _InternetProfile_IpOptions_ClientDnsSecondaryAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 42),
    _InternetProfile_IpOptions_ClientDnsSecondaryAddr_Type()
)
internetProfile_IpOptions_ClientDnsSecondaryAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_ClientDnsSecondaryAddr.setStatus("mandatory")


class _InternetProfile_IpOptions_ClientDnsAddrAssign_Type(Integer32):
    """Custom type internetProfile_IpOptions_ClientDnsAddrAssign based on Integer32"""
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


_InternetProfile_IpOptions_ClientDnsAddrAssign_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_ClientDnsAddrAssign_Object = MibScalar
internetProfile_IpOptions_ClientDnsAddrAssign = _InternetProfile_IpOptions_ClientDnsAddrAssign_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 43),
    _InternetProfile_IpOptions_ClientDnsAddrAssign_Type()
)
internetProfile_IpOptions_ClientDnsAddrAssign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_ClientDnsAddrAssign.setStatus("mandatory")
_InternetProfile_IpOptions_ClientDefaultGateway_Type = IpAddress
_InternetProfile_IpOptions_ClientDefaultGateway_Object = MibScalar
internetProfile_IpOptions_ClientDefaultGateway = _InternetProfile_IpOptions_ClientDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 44),
    _InternetProfile_IpOptions_ClientDefaultGateway_Type()
)
internetProfile_IpOptions_ClientDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_ClientDefaultGateway.setStatus("mandatory")


class _InternetProfile_IpOptions_TosOptions_Active_Type(Integer32):
    """Custom type internetProfile_IpOptions_TosOptions_Active based on Integer32"""
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


_InternetProfile_IpOptions_TosOptions_Active_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_TosOptions_Active_Object = MibScalar
internetProfile_IpOptions_TosOptions_Active = _InternetProfile_IpOptions_TosOptions_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 45),
    _InternetProfile_IpOptions_TosOptions_Active_Type()
)
internetProfile_IpOptions_TosOptions_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_TosOptions_Active.setStatus("mandatory")


class _InternetProfile_IpOptions_TosOptions_Precedence_Type(Integer32):
    """Custom type internetProfile_IpOptions_TosOptions_Precedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              33,
              65,
              97,
              129,
              161,
              193,
              225)
        )
    )
    namedValues = NamedValues(
        *(("n-000", 1),
          ("n-001", 33),
          ("n-010", 65),
          ("n-011", 97),
          ("n-100", 129),
          ("n-101", 161),
          ("n-110", 193),
          ("n-111", 225))
    )


_InternetProfile_IpOptions_TosOptions_Precedence_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_TosOptions_Precedence_Object = MibScalar
internetProfile_IpOptions_TosOptions_Precedence = _InternetProfile_IpOptions_TosOptions_Precedence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 46),
    _InternetProfile_IpOptions_TosOptions_Precedence_Type()
)
internetProfile_IpOptions_TosOptions_Precedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_TosOptions_Precedence.setStatus("mandatory")


class _InternetProfile_IpOptions_TosOptions_TypeOfService_Type(Integer32):
    """Custom type internetProfile_IpOptions_TosOptions_TypeOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              9,
              17)
        )
    )
    namedValues = NamedValues(
        *(("cost", 3),
          ("latency", 17),
          ("normal", 1),
          ("reliability", 5),
          ("throughput", 9))
    )


_InternetProfile_IpOptions_TosOptions_TypeOfService_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_TosOptions_TypeOfService_Object = MibScalar
internetProfile_IpOptions_TosOptions_TypeOfService = _InternetProfile_IpOptions_TosOptions_TypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 47),
    _InternetProfile_IpOptions_TosOptions_TypeOfService_Type()
)
internetProfile_IpOptions_TosOptions_TypeOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_TosOptions_TypeOfService.setStatus("mandatory")


class _InternetProfile_IpOptions_TosOptions_ApplyTo_Type(Integer32):
    """Custom type internetProfile_IpOptions_TosOptions_ApplyTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1025,
              2049,
              3073)
        )
    )
    namedValues = NamedValues(
        *(("both", 3073),
          ("incoming", 1025),
          ("outgoing", 2049))
    )


_InternetProfile_IpOptions_TosOptions_ApplyTo_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_TosOptions_ApplyTo_Object = MibScalar
internetProfile_IpOptions_TosOptions_ApplyTo = _InternetProfile_IpOptions_TosOptions_ApplyTo_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 48),
    _InternetProfile_IpOptions_TosOptions_ApplyTo_Type()
)
internetProfile_IpOptions_TosOptions_ApplyTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_TosOptions_ApplyTo.setStatus("mandatory")
_InternetProfile_IpOptions_TosFilter_Type = DisplayString
_InternetProfile_IpOptions_TosFilter_Object = MibScalar
internetProfile_IpOptions_TosFilter = _InternetProfile_IpOptions_TosFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 49),
    _InternetProfile_IpOptions_TosFilter_Type()
)
internetProfile_IpOptions_TosFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_TosFilter.setStatus("mandatory")


class _InternetProfile_IpxOptions_IpxRoutingEnabled_Type(Integer32):
    """Custom type internetProfile_IpxOptions_IpxRoutingEnabled based on Integer32"""
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


_InternetProfile_IpxOptions_IpxRoutingEnabled_Type.__name__ = "Integer32"
_InternetProfile_IpxOptions_IpxRoutingEnabled_Object = MibScalar
internetProfile_IpxOptions_IpxRoutingEnabled = _InternetProfile_IpxOptions_IpxRoutingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 50),
    _InternetProfile_IpxOptions_IpxRoutingEnabled_Type()
)
internetProfile_IpxOptions_IpxRoutingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpxOptions_IpxRoutingEnabled.setStatus("mandatory")


class _InternetProfile_IpxOptions_PeerMode_Type(Integer32):
    """Custom type internetProfile_IpxOptions_PeerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dialinPeer", 2),
          ("routerPeer", 1))
    )


_InternetProfile_IpxOptions_PeerMode_Type.__name__ = "Integer32"
_InternetProfile_IpxOptions_PeerMode_Object = MibScalar
internetProfile_IpxOptions_PeerMode = _InternetProfile_IpxOptions_PeerMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 51),
    _InternetProfile_IpxOptions_PeerMode_Type()
)
internetProfile_IpxOptions_PeerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpxOptions_PeerMode.setStatus("mandatory")


class _InternetProfile_IpxOptions_Rip_Type(Integer32):
    """Custom type internetProfile_IpxOptions_Rip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("off", 4),
          ("recv", 3),
          ("send", 2))
    )


_InternetProfile_IpxOptions_Rip_Type.__name__ = "Integer32"
_InternetProfile_IpxOptions_Rip_Object = MibScalar
internetProfile_IpxOptions_Rip = _InternetProfile_IpxOptions_Rip_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 52),
    _InternetProfile_IpxOptions_Rip_Type()
)
internetProfile_IpxOptions_Rip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpxOptions_Rip.setStatus("mandatory")


class _InternetProfile_IpxOptions_Sap_Type(Integer32):
    """Custom type internetProfile_IpxOptions_Sap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("off", 4),
          ("recv", 3),
          ("send", 2))
    )


_InternetProfile_IpxOptions_Sap_Type.__name__ = "Integer32"
_InternetProfile_IpxOptions_Sap_Object = MibScalar
internetProfile_IpxOptions_Sap = _InternetProfile_IpxOptions_Sap_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 53),
    _InternetProfile_IpxOptions_Sap_Type()
)
internetProfile_IpxOptions_Sap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpxOptions_Sap.setStatus("mandatory")


class _InternetProfile_IpxOptions_DialQuery_Type(Integer32):
    """Custom type internetProfile_IpxOptions_DialQuery based on Integer32"""
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


_InternetProfile_IpxOptions_DialQuery_Type.__name__ = "Integer32"
_InternetProfile_IpxOptions_DialQuery_Object = MibScalar
internetProfile_IpxOptions_DialQuery = _InternetProfile_IpxOptions_DialQuery_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 54),
    _InternetProfile_IpxOptions_DialQuery_Type()
)
internetProfile_IpxOptions_DialQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpxOptions_DialQuery.setStatus("mandatory")
_InternetProfile_IpxOptions_NetNumber_Type = DisplayString
_InternetProfile_IpxOptions_NetNumber_Object = MibScalar
internetProfile_IpxOptions_NetNumber = _InternetProfile_IpxOptions_NetNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 55),
    _InternetProfile_IpxOptions_NetNumber_Type()
)
internetProfile_IpxOptions_NetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpxOptions_NetNumber.setStatus("mandatory")
_InternetProfile_IpxOptions_NetAlias_Type = DisplayString
_InternetProfile_IpxOptions_NetAlias_Object = MibScalar
internetProfile_IpxOptions_NetAlias = _InternetProfile_IpxOptions_NetAlias_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 56),
    _InternetProfile_IpxOptions_NetAlias_Type()
)
internetProfile_IpxOptions_NetAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpxOptions_NetAlias.setStatus("mandatory")
_InternetProfile_IpxOptions_SapFilter_Type = DisplayString
_InternetProfile_IpxOptions_SapFilter_Object = MibScalar
internetProfile_IpxOptions_SapFilter = _InternetProfile_IpxOptions_SapFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 57),
    _InternetProfile_IpxOptions_SapFilter_Type()
)
internetProfile_IpxOptions_SapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpxOptions_SapFilter.setStatus("mandatory")


class _InternetProfile_IpxOptions_IpxSpoofing_Type(Integer32):
    """Custom type internetProfile_IpxOptions_IpxSpoofing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clientSpoofing", 2),
          ("none", 1),
          ("serverSpoofing", 3))
    )


_InternetProfile_IpxOptions_IpxSpoofing_Type.__name__ = "Integer32"
_InternetProfile_IpxOptions_IpxSpoofing_Object = MibScalar
internetProfile_IpxOptions_IpxSpoofing = _InternetProfile_IpxOptions_IpxSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 58),
    _InternetProfile_IpxOptions_IpxSpoofing_Type()
)
internetProfile_IpxOptions_IpxSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpxOptions_IpxSpoofing.setStatus("mandatory")
_InternetProfile_IpxOptions_SpoofingTimeout_Type = Integer32
_InternetProfile_IpxOptions_SpoofingTimeout_Object = MibScalar
internetProfile_IpxOptions_SpoofingTimeout = _InternetProfile_IpxOptions_SpoofingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 59),
    _InternetProfile_IpxOptions_SpoofingTimeout_Type()
)
internetProfile_IpxOptions_SpoofingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpxOptions_SpoofingTimeout.setStatus("mandatory")


class _InternetProfile_IpxOptions_IpxSapHsProxy_Type(Integer32):
    """Custom type internetProfile_IpxOptions_IpxSapHsProxy based on Integer32"""
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


_InternetProfile_IpxOptions_IpxSapHsProxy_Type.__name__ = "Integer32"
_InternetProfile_IpxOptions_IpxSapHsProxy_Object = MibScalar
internetProfile_IpxOptions_IpxSapHsProxy = _InternetProfile_IpxOptions_IpxSapHsProxy_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 60),
    _InternetProfile_IpxOptions_IpxSapHsProxy_Type()
)
internetProfile_IpxOptions_IpxSapHsProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpxOptions_IpxSapHsProxy.setStatus("mandatory")


class _InternetProfile_IpxOptions_IpxHeaderCompression_Type(Integer32):
    """Custom type internetProfile_IpxOptions_IpxHeaderCompression based on Integer32"""
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


_InternetProfile_IpxOptions_IpxHeaderCompression_Type.__name__ = "Integer32"
_InternetProfile_IpxOptions_IpxHeaderCompression_Object = MibScalar
internetProfile_IpxOptions_IpxHeaderCompression = _InternetProfile_IpxOptions_IpxHeaderCompression_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 61),
    _InternetProfile_IpxOptions_IpxHeaderCompression_Type()
)
internetProfile_IpxOptions_IpxHeaderCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpxOptions_IpxHeaderCompression.setStatus("mandatory")
_InternetProfile_BridgingOptions_BridgingGroup_Type = Integer32
_InternetProfile_BridgingOptions_BridgingGroup_Object = MibScalar
internetProfile_BridgingOptions_BridgingGroup = _InternetProfile_BridgingOptions_BridgingGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 62),
    _InternetProfile_BridgingOptions_BridgingGroup_Type()
)
internetProfile_BridgingOptions_BridgingGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_BridgingOptions_BridgingGroup.setStatus("mandatory")


class _InternetProfile_BridgingOptions_DialOnBroadcast_Type(Integer32):
    """Custom type internetProfile_BridgingOptions_DialOnBroadcast based on Integer32"""
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


_InternetProfile_BridgingOptions_DialOnBroadcast_Type.__name__ = "Integer32"
_InternetProfile_BridgingOptions_DialOnBroadcast_Object = MibScalar
internetProfile_BridgingOptions_DialOnBroadcast = _InternetProfile_BridgingOptions_DialOnBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 63),
    _InternetProfile_BridgingOptions_DialOnBroadcast_Type()
)
internetProfile_BridgingOptions_DialOnBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_BridgingOptions_DialOnBroadcast.setStatus("mandatory")


class _InternetProfile_BridgingOptions_IpxSpoofing_Type(Integer32):
    """Custom type internetProfile_BridgingOptions_IpxSpoofing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clientSpoofing", 2),
          ("none", 1),
          ("serverSpoofing", 3))
    )


_InternetProfile_BridgingOptions_IpxSpoofing_Type.__name__ = "Integer32"
_InternetProfile_BridgingOptions_IpxSpoofing_Object = MibScalar
internetProfile_BridgingOptions_IpxSpoofing = _InternetProfile_BridgingOptions_IpxSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 64),
    _InternetProfile_BridgingOptions_IpxSpoofing_Type()
)
internetProfile_BridgingOptions_IpxSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_BridgingOptions_IpxSpoofing.setStatus("mandatory")
_InternetProfile_BridgingOptions_SpoofingTimeout_Type = Integer32
_InternetProfile_BridgingOptions_SpoofingTimeout_Object = MibScalar
internetProfile_BridgingOptions_SpoofingTimeout = _InternetProfile_BridgingOptions_SpoofingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 65),
    _InternetProfile_BridgingOptions_SpoofingTimeout_Type()
)
internetProfile_BridgingOptions_SpoofingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_BridgingOptions_SpoofingTimeout.setStatus("mandatory")


class _InternetProfile_BridgingOptions_BridgeType_Type(Integer32):
    """Custom type internetProfile_BridgingOptions_BridgeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipxClientBridging", 2),
          ("noBridging", 3),
          ("transparentBridging", 1))
    )


_InternetProfile_BridgingOptions_BridgeType_Type.__name__ = "Integer32"
_InternetProfile_BridgingOptions_BridgeType_Object = MibScalar
internetProfile_BridgingOptions_BridgeType = _InternetProfile_BridgingOptions_BridgeType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 66),
    _InternetProfile_BridgingOptions_BridgeType_Type()
)
internetProfile_BridgingOptions_BridgeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_BridgingOptions_BridgeType.setStatus("mandatory")
_InternetProfile_SessionOptions_CallFilter_Type = DisplayString
_InternetProfile_SessionOptions_CallFilter_Object = MibScalar
internetProfile_SessionOptions_CallFilter = _InternetProfile_SessionOptions_CallFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 67),
    _InternetProfile_SessionOptions_CallFilter_Type()
)
internetProfile_SessionOptions_CallFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_CallFilter.setStatus("mandatory")
_InternetProfile_SessionOptions_DataFilter_Type = DisplayString
_InternetProfile_SessionOptions_DataFilter_Object = MibScalar
internetProfile_SessionOptions_DataFilter = _InternetProfile_SessionOptions_DataFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 68),
    _InternetProfile_SessionOptions_DataFilter_Type()
)
internetProfile_SessionOptions_DataFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_DataFilter.setStatus("mandatory")


class _InternetProfile_SessionOptions_FilterPersistence_Type(Integer32):
    """Custom type internetProfile_SessionOptions_FilterPersistence based on Integer32"""
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


_InternetProfile_SessionOptions_FilterPersistence_Type.__name__ = "Integer32"
_InternetProfile_SessionOptions_FilterPersistence_Object = MibScalar
internetProfile_SessionOptions_FilterPersistence = _InternetProfile_SessionOptions_FilterPersistence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 69),
    _InternetProfile_SessionOptions_FilterPersistence_Type()
)
internetProfile_SessionOptions_FilterPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_FilterPersistence.setStatus("mandatory")
_InternetProfile_SessionOptions_IdleTimer_Type = Integer32
_InternetProfile_SessionOptions_IdleTimer_Object = MibScalar
internetProfile_SessionOptions_IdleTimer = _InternetProfile_SessionOptions_IdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 70),
    _InternetProfile_SessionOptions_IdleTimer_Type()
)
internetProfile_SessionOptions_IdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_IdleTimer.setStatus("mandatory")


class _InternetProfile_SessionOptions_TsIdleMode_Type(Integer32):
    """Custom type internetProfile_SessionOptions_TsIdleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inputOnlyIdle", 2),
          ("inputOutputIdle", 3),
          ("noIdle", 1))
    )


_InternetProfile_SessionOptions_TsIdleMode_Type.__name__ = "Integer32"
_InternetProfile_SessionOptions_TsIdleMode_Object = MibScalar
internetProfile_SessionOptions_TsIdleMode = _InternetProfile_SessionOptions_TsIdleMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 71),
    _InternetProfile_SessionOptions_TsIdleMode_Type()
)
internetProfile_SessionOptions_TsIdleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_TsIdleMode.setStatus("mandatory")
_InternetProfile_SessionOptions_TsIdleTimer_Type = Integer32
_InternetProfile_SessionOptions_TsIdleTimer_Object = MibScalar
internetProfile_SessionOptions_TsIdleTimer = _InternetProfile_SessionOptions_TsIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 72),
    _InternetProfile_SessionOptions_TsIdleTimer_Type()
)
internetProfile_SessionOptions_TsIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_TsIdleTimer.setStatus("mandatory")
_InternetProfile_SessionOptions_Backup_Type = DisplayString
_InternetProfile_SessionOptions_Backup_Object = MibScalar
internetProfile_SessionOptions_Backup = _InternetProfile_SessionOptions_Backup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 73),
    _InternetProfile_SessionOptions_Backup_Type()
)
internetProfile_SessionOptions_Backup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_Backup.setStatus("mandatory")
_InternetProfile_SessionOptions_Secondary_Type = DisplayString
_InternetProfile_SessionOptions_Secondary_Object = MibScalar
internetProfile_SessionOptions_Secondary = _InternetProfile_SessionOptions_Secondary_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 74),
    _InternetProfile_SessionOptions_Secondary_Type()
)
internetProfile_SessionOptions_Secondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_Secondary.setStatus("mandatory")
_InternetProfile_SessionOptions_MaxCallDuration_Type = Integer32
_InternetProfile_SessionOptions_MaxCallDuration_Object = MibScalar
internetProfile_SessionOptions_MaxCallDuration = _InternetProfile_SessionOptions_MaxCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 76),
    _InternetProfile_SessionOptions_MaxCallDuration_Type()
)
internetProfile_SessionOptions_MaxCallDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_MaxCallDuration.setStatus("mandatory")


class _InternetProfile_SessionOptions_VtpGateway_Type(Integer32):
    """Custom type internetProfile_SessionOptions_VtpGateway based on Integer32"""
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


_InternetProfile_SessionOptions_VtpGateway_Type.__name__ = "Integer32"
_InternetProfile_SessionOptions_VtpGateway_Object = MibScalar
internetProfile_SessionOptions_VtpGateway = _InternetProfile_SessionOptions_VtpGateway_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 77),
    _InternetProfile_SessionOptions_VtpGateway_Type()
)
internetProfile_SessionOptions_VtpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_VtpGateway.setStatus("mandatory")
_InternetProfile_SessionOptions_Blockcountlimit_Type = Integer32
_InternetProfile_SessionOptions_Blockcountlimit_Object = MibScalar
internetProfile_SessionOptions_Blockcountlimit = _InternetProfile_SessionOptions_Blockcountlimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 78),
    _InternetProfile_SessionOptions_Blockcountlimit_Type()
)
internetProfile_SessionOptions_Blockcountlimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_Blockcountlimit.setStatus("mandatory")
_InternetProfile_SessionOptions_Blockduration_Type = Integer32
_InternetProfile_SessionOptions_Blockduration_Object = MibScalar
internetProfile_SessionOptions_Blockduration = _InternetProfile_SessionOptions_Blockduration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 79),
    _InternetProfile_SessionOptions_Blockduration_Type()
)
internetProfile_SessionOptions_Blockduration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_Blockduration.setStatus("mandatory")
_InternetProfile_SessionOptions_MaxVtpTunnels_Type = Integer32
_InternetProfile_SessionOptions_MaxVtpTunnels_Object = MibScalar
internetProfile_SessionOptions_MaxVtpTunnels = _InternetProfile_SessionOptions_MaxVtpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 81),
    _InternetProfile_SessionOptions_MaxVtpTunnels_Type()
)
internetProfile_SessionOptions_MaxVtpTunnels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_MaxVtpTunnels.setStatus("mandatory")
_InternetProfile_SessionOptions_RedialDelayLimit_Type = Integer32
_InternetProfile_SessionOptions_RedialDelayLimit_Object = MibScalar
internetProfile_SessionOptions_RedialDelayLimit = _InternetProfile_SessionOptions_RedialDelayLimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 82),
    _InternetProfile_SessionOptions_RedialDelayLimit_Type()
)
internetProfile_SessionOptions_RedialDelayLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_RedialDelayLimit.setStatus("mandatory")


class _InternetProfile_SessionOptions_SesRateType_Type(Integer32):
    """Custom type internetProfile_SessionOptions_SesRateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("adslCap", 3),
          ("adslCell", 4),
          ("adslDmt", 5),
          ("disabled", 1),
          ("sdsl", 2))
    )


_InternetProfile_SessionOptions_SesRateType_Type.__name__ = "Integer32"
_InternetProfile_SessionOptions_SesRateType_Object = MibScalar
internetProfile_SessionOptions_SesRateType = _InternetProfile_SessionOptions_SesRateType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 83),
    _InternetProfile_SessionOptions_SesRateType_Type()
)
internetProfile_SessionOptions_SesRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_SesRateType.setStatus("mandatory")


class _InternetProfile_SessionOptions_SesRateMode_Type(Integer32):
    """Custom type internetProfile_SessionOptions_SesRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autobaud", 2),
          ("singlebaud", 3))
    )


_InternetProfile_SessionOptions_SesRateMode_Type.__name__ = "Integer32"
_InternetProfile_SessionOptions_SesRateMode_Object = MibScalar
internetProfile_SessionOptions_SesRateMode = _InternetProfile_SessionOptions_SesRateMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 84),
    _InternetProfile_SessionOptions_SesRateMode_Type()
)
internetProfile_SessionOptions_SesRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_SesRateMode.setStatus("mandatory")


class _InternetProfile_SessionOptions_SesAdslCapUpRate_Type(Integer32):
    """Custom type internetProfile_SessionOptions_SesAdslCapUpRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(51,
              52,
              53,
              54,
              55,
              56,
              57)
        )
    )
    namedValues = NamedValues(
        *(("n-1088000", 51),
          ("n-272000", 57),
          ("n-408000", 56),
          ("n-544000", 55),
          ("n-680000", 54),
          ("n-816000", 53),
          ("n-952000", 52))
    )


_InternetProfile_SessionOptions_SesAdslCapUpRate_Type.__name__ = "Integer32"
_InternetProfile_SessionOptions_SesAdslCapUpRate_Object = MibScalar
internetProfile_SessionOptions_SesAdslCapUpRate = _InternetProfile_SessionOptions_SesAdslCapUpRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 85),
    _InternetProfile_SessionOptions_SesAdslCapUpRate_Type()
)
internetProfile_SessionOptions_SesAdslCapUpRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_SesAdslCapUpRate.setStatus("mandatory")


class _InternetProfile_SessionOptions_SesAdslCapDownRate_Type(Integer32):
    """Custom type internetProfile_SessionOptions_SesAdslCapDownRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("n-1280000", 11),
          ("n-1600000", 10),
          ("n-1920000", 9),
          ("n-2240000", 8),
          ("n-2560000", 7),
          ("n-2688000", 6),
          ("n-3200000", 5),
          ("n-4480000", 4),
          ("n-5120000", 3),
          ("n-6272000", 2),
          ("n-640000", 13),
          ("n-7168000", 1),
          ("n-960000", 12))
    )


_InternetProfile_SessionOptions_SesAdslCapDownRate_Type.__name__ = "Integer32"
_InternetProfile_SessionOptions_SesAdslCapDownRate_Object = MibScalar
internetProfile_SessionOptions_SesAdslCapDownRate = _InternetProfile_SessionOptions_SesAdslCapDownRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 86),
    _InternetProfile_SessionOptions_SesAdslCapDownRate_Type()
)
internetProfile_SessionOptions_SesAdslCapDownRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_SesAdslCapDownRate.setStatus("mandatory")


class _InternetProfile_SessionOptions_SesSdslRate_Type(Integer32):
    """Custom type internetProfile_SessionOptions_SesSdslRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("n-1040000", 15),
          ("n-1152000", 16),
          ("n-1168000", 6),
          ("n-144000", 1),
          ("n-1536000", 17),
          ("n-1552000", 7),
          ("n-1568000", 18),
          ("n-160000", 9),
          ("n-1680000", 19),
          ("n-192000", 10),
          ("n-1920000", 20),
          ("n-208000", 11),
          ("n-2160000", 21),
          ("n-2320000", 8),
          ("n-272000", 2),
          ("n-384000", 12),
          ("n-400000", 3),
          ("n-416000", 13),
          ("n-528000", 4),
          ("n-768000", 14),
          ("n-784000", 5))
    )


_InternetProfile_SessionOptions_SesSdslRate_Type.__name__ = "Integer32"
_InternetProfile_SessionOptions_SesSdslRate_Object = MibScalar
internetProfile_SessionOptions_SesSdslRate = _InternetProfile_SessionOptions_SesSdslRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 87),
    _InternetProfile_SessionOptions_SesSdslRate_Type()
)
internetProfile_SessionOptions_SesSdslRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_SesSdslRate.setStatus("mandatory")


class _InternetProfile_SessionOptions_SesAdslDmtUpRate_Type(Integer32):
    """Custom type internetProfile_SessionOptions_SesAdslDmtUpRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161)
        )
    )
    namedValues = NamedValues(
        *(("n-1088000", 152),
          ("n-128000", 161),
          ("n-256000", 160),
          ("n-384000", 159),
          ("n-512000", 158),
          ("n-640000", 157),
          ("n-768000", 156),
          ("n-800000", 155),
          ("n-896000", 154),
          ("n-928000", 153),
          ("upstrmMegMax", 151))
    )


_InternetProfile_SessionOptions_SesAdslDmtUpRate_Type.__name__ = "Integer32"
_InternetProfile_SessionOptions_SesAdslDmtUpRate_Object = MibScalar
internetProfile_SessionOptions_SesAdslDmtUpRate = _InternetProfile_SessionOptions_SesAdslDmtUpRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 88),
    _InternetProfile_SessionOptions_SesAdslDmtUpRate_Type()
)
internetProfile_SessionOptions_SesAdslDmtUpRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_SesAdslDmtUpRate.setStatus("mandatory")


class _InternetProfile_SessionOptions_SesAdslDmtDownRate_Type(Integer32):
    """Custom type internetProfile_SessionOptions_SesAdslDmtDownRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122)
        )
    )
    namedValues = NamedValues(
        *(("dwnstrmMegMax", 101),
          ("n-128000", 122),
          ("n-1280000", 115),
          ("n-1600000", 114),
          ("n-1920000", 113),
          ("n-2240000", 112),
          ("n-256000", 121),
          ("n-2560000", 111),
          ("n-2688000", 110),
          ("n-3200000", 109),
          ("n-384000", 120),
          ("n-4480000", 108),
          ("n-512000", 119),
          ("n-5120000", 107),
          ("n-6272000", 106),
          ("n-640000", 118),
          ("n-7168000", 105),
          ("n-768000", 117),
          ("n-8000000", 104),
          ("n-8960000", 103),
          ("n-9504000", 102),
          ("n-960000", 116))
    )


_InternetProfile_SessionOptions_SesAdslDmtDownRate_Type.__name__ = "Integer32"
_InternetProfile_SessionOptions_SesAdslDmtDownRate_Object = MibScalar
internetProfile_SessionOptions_SesAdslDmtDownRate = _InternetProfile_SessionOptions_SesAdslDmtDownRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 89),
    _InternetProfile_SessionOptions_SesAdslDmtDownRate_Type()
)
internetProfile_SessionOptions_SesAdslDmtDownRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_SesAdslDmtDownRate.setStatus("mandatory")
_InternetProfile_SessionOptions_RxDataRateLimit_Type = Integer32
_InternetProfile_SessionOptions_RxDataRateLimit_Object = MibScalar
internetProfile_SessionOptions_RxDataRateLimit = _InternetProfile_SessionOptions_RxDataRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 90),
    _InternetProfile_SessionOptions_RxDataRateLimit_Type()
)
internetProfile_SessionOptions_RxDataRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_RxDataRateLimit.setStatus("mandatory")
_InternetProfile_SessionOptions_TxDataRateLimit_Type = Integer32
_InternetProfile_SessionOptions_TxDataRateLimit_Object = MibScalar
internetProfile_SessionOptions_TxDataRateLimit = _InternetProfile_SessionOptions_TxDataRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 91),
    _InternetProfile_SessionOptions_TxDataRateLimit_Type()
)
internetProfile_SessionOptions_TxDataRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_TxDataRateLimit.setStatus("mandatory")


class _InternetProfile_TelcoOptions_AnswerOriginate_Type(Integer32):
    """Custom type internetProfile_TelcoOptions_AnswerOriginate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ansAndOrig", 1),
          ("answerOnly", 2),
          ("originateOnly", 3))
    )


_InternetProfile_TelcoOptions_AnswerOriginate_Type.__name__ = "Integer32"
_InternetProfile_TelcoOptions_AnswerOriginate_Object = MibScalar
internetProfile_TelcoOptions_AnswerOriginate = _InternetProfile_TelcoOptions_AnswerOriginate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 92),
    _InternetProfile_TelcoOptions_AnswerOriginate_Type()
)
internetProfile_TelcoOptions_AnswerOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TelcoOptions_AnswerOriginate.setStatus("mandatory")


class _InternetProfile_TelcoOptions_Callback_Type(Integer32):
    """Custom type internetProfile_TelcoOptions_Callback based on Integer32"""
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


_InternetProfile_TelcoOptions_Callback_Type.__name__ = "Integer32"
_InternetProfile_TelcoOptions_Callback_Object = MibScalar
internetProfile_TelcoOptions_Callback = _InternetProfile_TelcoOptions_Callback_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 93),
    _InternetProfile_TelcoOptions_Callback_Type()
)
internetProfile_TelcoOptions_Callback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TelcoOptions_Callback.setStatus("mandatory")


class _InternetProfile_TelcoOptions_CallType_Type(Integer32):
    """Custom type internetProfile_TelcoOptions_CallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("aodi", 7),
          ("bri", 4),
          ("dChan", 6),
          ("ft1", 2),
          ("ft1Bo", 5),
          ("ft1Mpp", 3),
          ("megamax", 8),
          ("off", 1))
    )


_InternetProfile_TelcoOptions_CallType_Type.__name__ = "Integer32"
_InternetProfile_TelcoOptions_CallType_Object = MibScalar
internetProfile_TelcoOptions_CallType = _InternetProfile_TelcoOptions_CallType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 94),
    _InternetProfile_TelcoOptions_CallType_Type()
)
internetProfile_TelcoOptions_CallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TelcoOptions_CallType.setStatus("mandatory")
_InternetProfile_TelcoOptions_NailedGroups_Type = DisplayString
_InternetProfile_TelcoOptions_NailedGroups_Object = MibScalar
internetProfile_TelcoOptions_NailedGroups = _InternetProfile_TelcoOptions_NailedGroups_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 95),
    _InternetProfile_TelcoOptions_NailedGroups_Type()
)
internetProfile_TelcoOptions_NailedGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TelcoOptions_NailedGroups.setStatus("mandatory")


class _InternetProfile_TelcoOptions_Ft1Caller_Type(Integer32):
    """Custom type internetProfile_TelcoOptions_Ft1Caller based on Integer32"""
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


_InternetProfile_TelcoOptions_Ft1Caller_Type.__name__ = "Integer32"
_InternetProfile_TelcoOptions_Ft1Caller_Object = MibScalar
internetProfile_TelcoOptions_Ft1Caller = _InternetProfile_TelcoOptions_Ft1Caller_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 96),
    _InternetProfile_TelcoOptions_Ft1Caller_Type()
)
internetProfile_TelcoOptions_Ft1Caller.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TelcoOptions_Ft1Caller.setStatus("mandatory")


class _InternetProfile_TelcoOptions_Force56kbps_Type(Integer32):
    """Custom type internetProfile_TelcoOptions_Force56kbps based on Integer32"""
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


_InternetProfile_TelcoOptions_Force56kbps_Type.__name__ = "Integer32"
_InternetProfile_TelcoOptions_Force56kbps_Object = MibScalar
internetProfile_TelcoOptions_Force56kbps = _InternetProfile_TelcoOptions_Force56kbps_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 97),
    _InternetProfile_TelcoOptions_Force56kbps_Type()
)
internetProfile_TelcoOptions_Force56kbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TelcoOptions_Force56kbps.setStatus("mandatory")


class _InternetProfile_TelcoOptions_DataService_Type(Integer32):
    """Custom type internetProfile_TelcoOptions_DataService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              39,
              40,
              41,
              42,
              43,
              44,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              255,
              263)
        )
    )
    namedValues = NamedValues(
        *(("atmSvc", 70),
          ("atmodem", 44),
          ("dws384Clear", 14),
          ("frameRelaySvc", 71),
          ("iptoip", 263),
          ("modem", 43),
          ("modem31khzAudio", 82),
          ("n-1024Clear", 24),
          ("n-1088Clear", 25),
          ("n-1152Clear", 26),
          ("n-1216Clear", 27),
          ("n-1280Clear", 28),
          ("n-128kClear", 10),
          ("n-1344Clear", 29),
          ("n-1408Clear", 30),
          ("n-14456kV110", 74),
          ("n-14456krV110", 76),
          ("n-14464kV110", 78),
          ("n-14464krV110", 80),
          ("n-144kClear", 255),
          ("n-1472Clear", 31),
          ("n-1536kClear", 8),
          ("n-1536kRestricted", 9),
          ("n-1600Clear", 32),
          ("n-1664Clear", 33),
          ("n-1728Clear", 34),
          ("n-1792Clear", 35),
          ("n-1856Clear", 36),
          ("n-1920Clear", 37),
          ("n-19256kV110", 49),
          ("n-19256krV110", 54),
          ("n-19264kV110", 59),
          ("n-19264krV110", 64),
          ("n-192kClear", 11),
          ("n-2456kV110", 46),
          ("n-2456krV110", 51),
          ("n-2464kV110", 56),
          ("n-2464krV110", 61),
          ("n-256kClear", 12),
          ("n-28856kV110", 75),
          ("n-28856krV110", 77),
          ("n-28864kV110", 79),
          ("n-28864krV110", 81),
          ("n-320kClear", 13),
          ("n-38456kV110", 50),
          ("n-38456krV110", 55),
          ("n-38464kV110", 60),
          ("n-38464krV110", 65),
          ("n-384kClear", 7),
          ("n-384kRestricted", 6),
          ("n-448Clear", 15),
          ("n-4856kV110", 47),
          ("n-4856krV110", 52),
          ("n-4864kV110", 57),
          ("n-4864krV110", 62),
          ("n-512Clear", 16),
          ("n-56kClear", 5),
          ("n-56kRestricted", 2),
          ("n-56kV110Clear", 42),
          ("n-576Clear", 17),
          ("n-640Clear", 18),
          ("n-64kClear", 3),
          ("n-64kRestricted", 4),
          ("n-64kX30Restricted", 41),
          ("n-704Clear", 19),
          ("n-768Clear", 20),
          ("n-832Clear", 21),
          ("n-896Clear", 22),
          ("n-960Clear", 23),
          ("n-9656kV110", 48),
          ("n-9656krV110", 53),
          ("n-9664kV110", 58),
          ("n-9664krV110", 63),
          ("phs64k", 67),
          ("v110ClearBearer", 40),
          ("v32", 66),
          ("voice", 1),
          ("voiceOverIp", 68),
          ("vpnTunnel", 72),
          ("wormarq", 73),
          ("x25Svc", 83),
          ("x30RestrictedBearer", 39))
    )


_InternetProfile_TelcoOptions_DataService_Type.__name__ = "Integer32"
_InternetProfile_TelcoOptions_DataService_Object = MibScalar
internetProfile_TelcoOptions_DataService = _InternetProfile_TelcoOptions_DataService_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 98),
    _InternetProfile_TelcoOptions_DataService_Type()
)
internetProfile_TelcoOptions_DataService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TelcoOptions_DataService.setStatus("mandatory")
_InternetProfile_TelcoOptions_CallByCall_Type = Integer32
_InternetProfile_TelcoOptions_CallByCall_Object = MibScalar
internetProfile_TelcoOptions_CallByCall = _InternetProfile_TelcoOptions_CallByCall_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 99),
    _InternetProfile_TelcoOptions_CallByCall_Type()
)
internetProfile_TelcoOptions_CallByCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TelcoOptions_CallByCall.setStatus("mandatory")
_InternetProfile_TelcoOptions_BillingNumber_Type = DisplayString
_InternetProfile_TelcoOptions_BillingNumber_Object = MibScalar
internetProfile_TelcoOptions_BillingNumber = _InternetProfile_TelcoOptions_BillingNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 100),
    _InternetProfile_TelcoOptions_BillingNumber_Type()
)
internetProfile_TelcoOptions_BillingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TelcoOptions_BillingNumber.setStatus("mandatory")
_InternetProfile_TelcoOptions_TransitNumber_Type = DisplayString
_InternetProfile_TelcoOptions_TransitNumber_Object = MibScalar
internetProfile_TelcoOptions_TransitNumber = _InternetProfile_TelcoOptions_TransitNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 101),
    _InternetProfile_TelcoOptions_TransitNumber_Type()
)
internetProfile_TelcoOptions_TransitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TelcoOptions_TransitNumber.setStatus("mandatory")


class _InternetProfile_TelcoOptions_ExpectCallback_Type(Integer32):
    """Custom type internetProfile_TelcoOptions_ExpectCallback based on Integer32"""
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


_InternetProfile_TelcoOptions_ExpectCallback_Type.__name__ = "Integer32"
_InternetProfile_TelcoOptions_ExpectCallback_Object = MibScalar
internetProfile_TelcoOptions_ExpectCallback = _InternetProfile_TelcoOptions_ExpectCallback_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 102),
    _InternetProfile_TelcoOptions_ExpectCallback_Type()
)
internetProfile_TelcoOptions_ExpectCallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TelcoOptions_ExpectCallback.setStatus("mandatory")


class _InternetProfile_TelcoOptions_DialoutAllowed_Type(Integer32):
    """Custom type internetProfile_TelcoOptions_DialoutAllowed based on Integer32"""
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


_InternetProfile_TelcoOptions_DialoutAllowed_Type.__name__ = "Integer32"
_InternetProfile_TelcoOptions_DialoutAllowed_Object = MibScalar
internetProfile_TelcoOptions_DialoutAllowed = _InternetProfile_TelcoOptions_DialoutAllowed_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 103),
    _InternetProfile_TelcoOptions_DialoutAllowed_Type()
)
internetProfile_TelcoOptions_DialoutAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TelcoOptions_DialoutAllowed.setStatus("mandatory")
_InternetProfile_TelcoOptions_DelayCallback_Type = Integer32
_InternetProfile_TelcoOptions_DelayCallback_Object = MibScalar
internetProfile_TelcoOptions_DelayCallback = _InternetProfile_TelcoOptions_DelayCallback_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 104),
    _InternetProfile_TelcoOptions_DelayCallback_Type()
)
internetProfile_TelcoOptions_DelayCallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TelcoOptions_DelayCallback.setStatus("mandatory")


class _InternetProfile_PppOptions_SendAuthMode_Type(Integer32):
    """Custom type internetProfile_PppOptions_SendAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("anyPppAuth", 4),
          ("cacheTokenPppAuth", 8),
          ("chapPppAuth", 3),
          ("desPapPppAuth", 5),
          ("msChapPppAuth", 9),
          ("noPppAuth", 1),
          ("papPppAuth", 2),
          ("papPreferred", 10),
          ("tokenChapPppAuth", 7),
          ("tokenPapPppAuth", 6))
    )


_InternetProfile_PppOptions_SendAuthMode_Type.__name__ = "Integer32"
_InternetProfile_PppOptions_SendAuthMode_Object = MibScalar
internetProfile_PppOptions_SendAuthMode = _InternetProfile_PppOptions_SendAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 105),
    _InternetProfile_PppOptions_SendAuthMode_Type()
)
internetProfile_PppOptions_SendAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_SendAuthMode.setStatus("mandatory")
_InternetProfile_PppOptions_SendPassword_Type = DisplayString
_InternetProfile_PppOptions_SendPassword_Object = MibScalar
internetProfile_PppOptions_SendPassword = _InternetProfile_PppOptions_SendPassword_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 106),
    _InternetProfile_PppOptions_SendPassword_Type()
)
internetProfile_PppOptions_SendPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_SendPassword.setStatus("mandatory")
_InternetProfile_PppOptions_SubstituteSendName_Type = DisplayString
_InternetProfile_PppOptions_SubstituteSendName_Object = MibScalar
internetProfile_PppOptions_SubstituteSendName = _InternetProfile_PppOptions_SubstituteSendName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 107),
    _InternetProfile_PppOptions_SubstituteSendName_Type()
)
internetProfile_PppOptions_SubstituteSendName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_SubstituteSendName.setStatus("mandatory")
_InternetProfile_PppOptions_RecvPassword_Type = DisplayString
_InternetProfile_PppOptions_RecvPassword_Object = MibScalar
internetProfile_PppOptions_RecvPassword = _InternetProfile_PppOptions_RecvPassword_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 108),
    _InternetProfile_PppOptions_RecvPassword_Type()
)
internetProfile_PppOptions_RecvPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_RecvPassword.setStatus("mandatory")


class _InternetProfile_PppOptions_LinkCompression_Type(Integer32):
    """Custom type internetProfile_PppOptions_LinkCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("mppc", 5),
          ("msStac", 4),
          ("none", 1),
          ("stac", 2),
          ("stac9", 3))
    )


_InternetProfile_PppOptions_LinkCompression_Type.__name__ = "Integer32"
_InternetProfile_PppOptions_LinkCompression_Object = MibScalar
internetProfile_PppOptions_LinkCompression = _InternetProfile_PppOptions_LinkCompression_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 109),
    _InternetProfile_PppOptions_LinkCompression_Type()
)
internetProfile_PppOptions_LinkCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_LinkCompression.setStatus("mandatory")
_InternetProfile_PppOptions_Mru_Type = Integer32
_InternetProfile_PppOptions_Mru_Object = MibScalar
internetProfile_PppOptions_Mru = _InternetProfile_PppOptions_Mru_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 110),
    _InternetProfile_PppOptions_Mru_Type()
)
internetProfile_PppOptions_Mru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_Mru.setStatus("mandatory")


class _InternetProfile_PppOptions_Lqm_Type(Integer32):
    """Custom type internetProfile_PppOptions_Lqm based on Integer32"""
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


_InternetProfile_PppOptions_Lqm_Type.__name__ = "Integer32"
_InternetProfile_PppOptions_Lqm_Object = MibScalar
internetProfile_PppOptions_Lqm = _InternetProfile_PppOptions_Lqm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 111),
    _InternetProfile_PppOptions_Lqm_Type()
)
internetProfile_PppOptions_Lqm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_Lqm.setStatus("mandatory")
_InternetProfile_PppOptions_LqmMinimumPeriod_Type = Integer32
_InternetProfile_PppOptions_LqmMinimumPeriod_Object = MibScalar
internetProfile_PppOptions_LqmMinimumPeriod = _InternetProfile_PppOptions_LqmMinimumPeriod_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 112),
    _InternetProfile_PppOptions_LqmMinimumPeriod_Type()
)
internetProfile_PppOptions_LqmMinimumPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_LqmMinimumPeriod.setStatus("mandatory")
_InternetProfile_PppOptions_LqmMaximumPeriod_Type = Integer32
_InternetProfile_PppOptions_LqmMaximumPeriod_Object = MibScalar
internetProfile_PppOptions_LqmMaximumPeriod = _InternetProfile_PppOptions_LqmMaximumPeriod_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 113),
    _InternetProfile_PppOptions_LqmMaximumPeriod_Type()
)
internetProfile_PppOptions_LqmMaximumPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_LqmMaximumPeriod.setStatus("mandatory")


class _InternetProfile_PppOptions_CbcpEnabled_Type(Integer32):
    """Custom type internetProfile_PppOptions_CbcpEnabled based on Integer32"""
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


_InternetProfile_PppOptions_CbcpEnabled_Type.__name__ = "Integer32"
_InternetProfile_PppOptions_CbcpEnabled_Object = MibScalar
internetProfile_PppOptions_CbcpEnabled = _InternetProfile_PppOptions_CbcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 114),
    _InternetProfile_PppOptions_CbcpEnabled_Type()
)
internetProfile_PppOptions_CbcpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_CbcpEnabled.setStatus("mandatory")


class _InternetProfile_PppOptions_ModeCallbackControl_Type(Integer32):
    """Custom type internetProfile_PppOptions_ModeCallbackControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cbcpAll", 8),
          ("cbcpNoCallback", 2),
          ("cbcpProfileNum", 4),
          ("cbcpUserNumber", 3))
    )


_InternetProfile_PppOptions_ModeCallbackControl_Type.__name__ = "Integer32"
_InternetProfile_PppOptions_ModeCallbackControl_Object = MibScalar
internetProfile_PppOptions_ModeCallbackControl = _InternetProfile_PppOptions_ModeCallbackControl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 115),
    _InternetProfile_PppOptions_ModeCallbackControl_Type()
)
internetProfile_PppOptions_ModeCallbackControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_ModeCallbackControl.setStatus("mandatory")
_InternetProfile_PppOptions_DelayCallbackControl_Type = Integer32
_InternetProfile_PppOptions_DelayCallbackControl_Object = MibScalar
internetProfile_PppOptions_DelayCallbackControl = _InternetProfile_PppOptions_DelayCallbackControl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 116),
    _InternetProfile_PppOptions_DelayCallbackControl_Type()
)
internetProfile_PppOptions_DelayCallbackControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_DelayCallbackControl.setStatus("mandatory")
_InternetProfile_PppOptions_TrunkGroupCallbackControl_Type = Integer32
_InternetProfile_PppOptions_TrunkGroupCallbackControl_Object = MibScalar
internetProfile_PppOptions_TrunkGroupCallbackControl = _InternetProfile_PppOptions_TrunkGroupCallbackControl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 117),
    _InternetProfile_PppOptions_TrunkGroupCallbackControl_Type()
)
internetProfile_PppOptions_TrunkGroupCallbackControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_TrunkGroupCallbackControl.setStatus("mandatory")


class _InternetProfile_PppOptions_SplitCodeDotUserEnabled_Type(Integer32):
    """Custom type internetProfile_PppOptions_SplitCodeDotUserEnabled based on Integer32"""
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


_InternetProfile_PppOptions_SplitCodeDotUserEnabled_Type.__name__ = "Integer32"
_InternetProfile_PppOptions_SplitCodeDotUserEnabled_Object = MibScalar
internetProfile_PppOptions_SplitCodeDotUserEnabled = _InternetProfile_PppOptions_SplitCodeDotUserEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 118),
    _InternetProfile_PppOptions_SplitCodeDotUserEnabled_Type()
)
internetProfile_PppOptions_SplitCodeDotUserEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_SplitCodeDotUserEnabled.setStatus("mandatory")


class _InternetProfile_PppOptions_PppInterfaceType_Type(Integer32):
    """Custom type internetProfile_PppOptions_PppInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aal5", 3),
          ("frameRelay", 2),
          ("hdlcLike", 1),
          ("x25", 4))
    )


_InternetProfile_PppOptions_PppInterfaceType_Type.__name__ = "Integer32"
_InternetProfile_PppOptions_PppInterfaceType_Object = MibScalar
internetProfile_PppOptions_PppInterfaceType = _InternetProfile_PppOptions_PppInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 119),
    _InternetProfile_PppOptions_PppInterfaceType_Type()
)
internetProfile_PppOptions_PppInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_PppInterfaceType.setStatus("mandatory")
_InternetProfile_MpOptions_BaseChannelCount_Type = Integer32
_InternetProfile_MpOptions_BaseChannelCount_Object = MibScalar
internetProfile_MpOptions_BaseChannelCount = _InternetProfile_MpOptions_BaseChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 120),
    _InternetProfile_MpOptions_BaseChannelCount_Type()
)
internetProfile_MpOptions_BaseChannelCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_MpOptions_BaseChannelCount.setStatus("mandatory")
_InternetProfile_MpOptions_MinimumChannels_Type = Integer32
_InternetProfile_MpOptions_MinimumChannels_Object = MibScalar
internetProfile_MpOptions_MinimumChannels = _InternetProfile_MpOptions_MinimumChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 121),
    _InternetProfile_MpOptions_MinimumChannels_Type()
)
internetProfile_MpOptions_MinimumChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_MpOptions_MinimumChannels.setStatus("mandatory")
_InternetProfile_MpOptions_MaximumChannels_Type = Integer32
_InternetProfile_MpOptions_MaximumChannels_Object = MibScalar
internetProfile_MpOptions_MaximumChannels = _InternetProfile_MpOptions_MaximumChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 122),
    _InternetProfile_MpOptions_MaximumChannels_Type()
)
internetProfile_MpOptions_MaximumChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_MpOptions_MaximumChannels.setStatus("mandatory")


class _InternetProfile_MpOptions_BacpEnable_Type(Integer32):
    """Custom type internetProfile_MpOptions_BacpEnable based on Integer32"""
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


_InternetProfile_MpOptions_BacpEnable_Type.__name__ = "Integer32"
_InternetProfile_MpOptions_BacpEnable_Object = MibScalar
internetProfile_MpOptions_BacpEnable = _InternetProfile_MpOptions_BacpEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 123),
    _InternetProfile_MpOptions_BacpEnable_Type()
)
internetProfile_MpOptions_BacpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_MpOptions_BacpEnable.setStatus("mandatory")
_InternetProfile_MppOptions_AuxSendPassword_Type = DisplayString
_InternetProfile_MppOptions_AuxSendPassword_Object = MibScalar
internetProfile_MppOptions_AuxSendPassword = _InternetProfile_MppOptions_AuxSendPassword_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 124),
    _InternetProfile_MppOptions_AuxSendPassword_Type()
)
internetProfile_MppOptions_AuxSendPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_MppOptions_AuxSendPassword.setStatus("mandatory")


class _InternetProfile_MppOptions_DynamicAlgorithm_Type(Integer32):
    """Custom type internetProfile_MppOptions_DynamicAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("constant", 1),
          ("linear", 2),
          ("quadratic", 3))
    )


_InternetProfile_MppOptions_DynamicAlgorithm_Type.__name__ = "Integer32"
_InternetProfile_MppOptions_DynamicAlgorithm_Object = MibScalar
internetProfile_MppOptions_DynamicAlgorithm = _InternetProfile_MppOptions_DynamicAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 125),
    _InternetProfile_MppOptions_DynamicAlgorithm_Type()
)
internetProfile_MppOptions_DynamicAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_MppOptions_DynamicAlgorithm.setStatus("mandatory")


class _InternetProfile_MppOptions_BandwidthMonitorDirection_Type(Integer32):
    """Custom type internetProfile_MppOptions_BandwidthMonitorDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("transmit", 1),
          ("transmitRecv", 2))
    )


_InternetProfile_MppOptions_BandwidthMonitorDirection_Type.__name__ = "Integer32"
_InternetProfile_MppOptions_BandwidthMonitorDirection_Object = MibScalar
internetProfile_MppOptions_BandwidthMonitorDirection = _InternetProfile_MppOptions_BandwidthMonitorDirection_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 126),
    _InternetProfile_MppOptions_BandwidthMonitorDirection_Type()
)
internetProfile_MppOptions_BandwidthMonitorDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_MppOptions_BandwidthMonitorDirection.setStatus("mandatory")
_InternetProfile_MppOptions_IncrementChannelCount_Type = Integer32
_InternetProfile_MppOptions_IncrementChannelCount_Object = MibScalar
internetProfile_MppOptions_IncrementChannelCount = _InternetProfile_MppOptions_IncrementChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 127),
    _InternetProfile_MppOptions_IncrementChannelCount_Type()
)
internetProfile_MppOptions_IncrementChannelCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_MppOptions_IncrementChannelCount.setStatus("mandatory")
_InternetProfile_MppOptions_DecrementChannelCount_Type = Integer32
_InternetProfile_MppOptions_DecrementChannelCount_Object = MibScalar
internetProfile_MppOptions_DecrementChannelCount = _InternetProfile_MppOptions_DecrementChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 128),
    _InternetProfile_MppOptions_DecrementChannelCount_Type()
)
internetProfile_MppOptions_DecrementChannelCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_MppOptions_DecrementChannelCount.setStatus("mandatory")
_InternetProfile_MppOptions_SecondsHistory_Type = Integer32
_InternetProfile_MppOptions_SecondsHistory_Object = MibScalar
internetProfile_MppOptions_SecondsHistory = _InternetProfile_MppOptions_SecondsHistory_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 129),
    _InternetProfile_MppOptions_SecondsHistory_Type()
)
internetProfile_MppOptions_SecondsHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_MppOptions_SecondsHistory.setStatus("mandatory")
_InternetProfile_MppOptions_AddPersistence_Type = Integer32
_InternetProfile_MppOptions_AddPersistence_Object = MibScalar
internetProfile_MppOptions_AddPersistence = _InternetProfile_MppOptions_AddPersistence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 130),
    _InternetProfile_MppOptions_AddPersistence_Type()
)
internetProfile_MppOptions_AddPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_MppOptions_AddPersistence.setStatus("mandatory")
_InternetProfile_MppOptions_SubPersistence_Type = Integer32
_InternetProfile_MppOptions_SubPersistence_Object = MibScalar
internetProfile_MppOptions_SubPersistence = _InternetProfile_MppOptions_SubPersistence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 131),
    _InternetProfile_MppOptions_SubPersistence_Type()
)
internetProfile_MppOptions_SubPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_MppOptions_SubPersistence.setStatus("mandatory")
_InternetProfile_MppOptions_TargetUtilization_Type = Integer32
_InternetProfile_MppOptions_TargetUtilization_Object = MibScalar
internetProfile_MppOptions_TargetUtilization = _InternetProfile_MppOptions_TargetUtilization_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 132),
    _InternetProfile_MppOptions_TargetUtilization_Type()
)
internetProfile_MppOptions_TargetUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_MppOptions_TargetUtilization.setStatus("mandatory")
_InternetProfile_FrOptions_FrameRelayProfile_Type = DisplayString
_InternetProfile_FrOptions_FrameRelayProfile_Object = MibScalar
internetProfile_FrOptions_FrameRelayProfile = _InternetProfile_FrOptions_FrameRelayProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 133),
    _InternetProfile_FrOptions_FrameRelayProfile_Type()
)
internetProfile_FrOptions_FrameRelayProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_FrOptions_FrameRelayProfile.setStatus("mandatory")
_InternetProfile_FrOptions_Dlci_Type = Integer32
_InternetProfile_FrOptions_Dlci_Object = MibScalar
internetProfile_FrOptions_Dlci = _InternetProfile_FrOptions_Dlci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 134),
    _InternetProfile_FrOptions_Dlci_Type()
)
internetProfile_FrOptions_Dlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_FrOptions_Dlci.setStatus("mandatory")
_InternetProfile_FrOptions_CircuitName_Type = DisplayString
_InternetProfile_FrOptions_CircuitName_Object = MibScalar
internetProfile_FrOptions_CircuitName = _InternetProfile_FrOptions_CircuitName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 135),
    _InternetProfile_FrOptions_CircuitName_Type()
)
internetProfile_FrOptions_CircuitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_FrOptions_CircuitName.setStatus("mandatory")


class _InternetProfile_FrOptions_FrDirectEnabled_Type(Integer32):
    """Custom type internetProfile_FrOptions_FrDirectEnabled based on Integer32"""
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


_InternetProfile_FrOptions_FrDirectEnabled_Type.__name__ = "Integer32"
_InternetProfile_FrOptions_FrDirectEnabled_Object = MibScalar
internetProfile_FrOptions_FrDirectEnabled = _InternetProfile_FrOptions_FrDirectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 136),
    _InternetProfile_FrOptions_FrDirectEnabled_Type()
)
internetProfile_FrOptions_FrDirectEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_FrOptions_FrDirectEnabled.setStatus("mandatory")
_InternetProfile_FrOptions_FrDirectProfile_Type = DisplayString
_InternetProfile_FrOptions_FrDirectProfile_Object = MibScalar
internetProfile_FrOptions_FrDirectProfile = _InternetProfile_FrOptions_FrDirectProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 137),
    _InternetProfile_FrOptions_FrDirectProfile_Type()
)
internetProfile_FrOptions_FrDirectProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_FrOptions_FrDirectProfile.setStatus("mandatory")
_InternetProfile_FrOptions_FrDirectDlci_Type = Integer32
_InternetProfile_FrOptions_FrDirectDlci_Object = MibScalar
internetProfile_FrOptions_FrDirectDlci = _InternetProfile_FrOptions_FrDirectDlci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 138),
    _InternetProfile_FrOptions_FrDirectDlci_Type()
)
internetProfile_FrOptions_FrDirectDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_FrOptions_FrDirectDlci.setStatus("mandatory")
_InternetProfile_TcpClearOptions_Host_Type = DisplayString
_InternetProfile_TcpClearOptions_Host_Object = MibScalar
internetProfile_TcpClearOptions_Host = _InternetProfile_TcpClearOptions_Host_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 139),
    _InternetProfile_TcpClearOptions_Host_Type()
)
internetProfile_TcpClearOptions_Host.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TcpClearOptions_Host.setStatus("mandatory")
_InternetProfile_TcpClearOptions_Port_Type = Integer32
_InternetProfile_TcpClearOptions_Port_Object = MibScalar
internetProfile_TcpClearOptions_Port = _InternetProfile_TcpClearOptions_Port_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 140),
    _InternetProfile_TcpClearOptions_Port_Type()
)
internetProfile_TcpClearOptions_Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TcpClearOptions_Port.setStatus("mandatory")
_InternetProfile_TcpClearOptions_Host2_Type = DisplayString
_InternetProfile_TcpClearOptions_Host2_Object = MibScalar
internetProfile_TcpClearOptions_Host2 = _InternetProfile_TcpClearOptions_Host2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 141),
    _InternetProfile_TcpClearOptions_Host2_Type()
)
internetProfile_TcpClearOptions_Host2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TcpClearOptions_Host2.setStatus("mandatory")
_InternetProfile_TcpClearOptions_Port2_Type = Integer32
_InternetProfile_TcpClearOptions_Port2_Object = MibScalar
internetProfile_TcpClearOptions_Port2 = _InternetProfile_TcpClearOptions_Port2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 142),
    _InternetProfile_TcpClearOptions_Port2_Type()
)
internetProfile_TcpClearOptions_Port2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TcpClearOptions_Port2.setStatus("mandatory")
_InternetProfile_TcpClearOptions_Host3_Type = DisplayString
_InternetProfile_TcpClearOptions_Host3_Object = MibScalar
internetProfile_TcpClearOptions_Host3 = _InternetProfile_TcpClearOptions_Host3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 143),
    _InternetProfile_TcpClearOptions_Host3_Type()
)
internetProfile_TcpClearOptions_Host3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TcpClearOptions_Host3.setStatus("mandatory")
_InternetProfile_TcpClearOptions_Port3_Type = Integer32
_InternetProfile_TcpClearOptions_Port3_Object = MibScalar
internetProfile_TcpClearOptions_Port3 = _InternetProfile_TcpClearOptions_Port3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 144),
    _InternetProfile_TcpClearOptions_Port3_Type()
)
internetProfile_TcpClearOptions_Port3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TcpClearOptions_Port3.setStatus("mandatory")
_InternetProfile_TcpClearOptions_Host4_Type = DisplayString
_InternetProfile_TcpClearOptions_Host4_Object = MibScalar
internetProfile_TcpClearOptions_Host4 = _InternetProfile_TcpClearOptions_Host4_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 145),
    _InternetProfile_TcpClearOptions_Host4_Type()
)
internetProfile_TcpClearOptions_Host4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TcpClearOptions_Host4.setStatus("mandatory")
_InternetProfile_TcpClearOptions_Port4_Type = Integer32
_InternetProfile_TcpClearOptions_Port4_Object = MibScalar
internetProfile_TcpClearOptions_Port4 = _InternetProfile_TcpClearOptions_Port4_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 146),
    _InternetProfile_TcpClearOptions_Port4_Type()
)
internetProfile_TcpClearOptions_Port4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TcpClearOptions_Port4.setStatus("mandatory")


class _InternetProfile_TcpClearOptions_DetectEndOfPacket_Type(Integer32):
    """Custom type internetProfile_TcpClearOptions_DetectEndOfPacket based on Integer32"""
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


_InternetProfile_TcpClearOptions_DetectEndOfPacket_Type.__name__ = "Integer32"
_InternetProfile_TcpClearOptions_DetectEndOfPacket_Object = MibScalar
internetProfile_TcpClearOptions_DetectEndOfPacket = _InternetProfile_TcpClearOptions_DetectEndOfPacket_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 147),
    _InternetProfile_TcpClearOptions_DetectEndOfPacket_Type()
)
internetProfile_TcpClearOptions_DetectEndOfPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TcpClearOptions_DetectEndOfPacket.setStatus("mandatory")
_InternetProfile_TcpClearOptions_EndOfPacketPattern_Type = DisplayString
_InternetProfile_TcpClearOptions_EndOfPacketPattern_Object = MibScalar
internetProfile_TcpClearOptions_EndOfPacketPattern = _InternetProfile_TcpClearOptions_EndOfPacketPattern_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 148),
    _InternetProfile_TcpClearOptions_EndOfPacketPattern_Type()
)
internetProfile_TcpClearOptions_EndOfPacketPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TcpClearOptions_EndOfPacketPattern.setStatus("mandatory")
_InternetProfile_TcpClearOptions_FlushLength_Type = Integer32
_InternetProfile_TcpClearOptions_FlushLength_Object = MibScalar
internetProfile_TcpClearOptions_FlushLength = _InternetProfile_TcpClearOptions_FlushLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 149),
    _InternetProfile_TcpClearOptions_FlushLength_Type()
)
internetProfile_TcpClearOptions_FlushLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TcpClearOptions_FlushLength.setStatus("mandatory")
_InternetProfile_TcpClearOptions_FlushTime_Type = Integer32
_InternetProfile_TcpClearOptions_FlushTime_Object = MibScalar
internetProfile_TcpClearOptions_FlushTime = _InternetProfile_TcpClearOptions_FlushTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 150),
    _InternetProfile_TcpClearOptions_FlushTime_Type()
)
internetProfile_TcpClearOptions_FlushTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TcpClearOptions_FlushTime.setStatus("mandatory")
_InternetProfile_AraOptions_RecvPassword_Type = DisplayString
_InternetProfile_AraOptions_RecvPassword_Object = MibScalar
internetProfile_AraOptions_RecvPassword = _InternetProfile_AraOptions_RecvPassword_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 151),
    _InternetProfile_AraOptions_RecvPassword_Type()
)
internetProfile_AraOptions_RecvPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AraOptions_RecvPassword.setStatus("mandatory")
_InternetProfile_AraOptions_MaximumConnectTime_Type = Integer32
_InternetProfile_AraOptions_MaximumConnectTime_Object = MibScalar
internetProfile_AraOptions_MaximumConnectTime = _InternetProfile_AraOptions_MaximumConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 152),
    _InternetProfile_AraOptions_MaximumConnectTime_Type()
)
internetProfile_AraOptions_MaximumConnectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AraOptions_MaximumConnectTime.setStatus("mandatory")
_InternetProfile_X25Options_X25Profile_Type = DisplayString
_InternetProfile_X25Options_X25Profile_Object = MibScalar
internetProfile_X25Options_X25Profile = _InternetProfile_X25Options_X25Profile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 157),
    _InternetProfile_X25Options_X25Profile_Type()
)
internetProfile_X25Options_X25Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_X25Profile.setStatus("mandatory")
_InternetProfile_X25Options_Lcn_Type = Integer32
_InternetProfile_X25Options_Lcn_Object = MibScalar
internetProfile_X25Options_Lcn = _InternetProfile_X25Options_Lcn_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 158),
    _InternetProfile_X25Options_Lcn_Type()
)
internetProfile_X25Options_Lcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_Lcn.setStatus("mandatory")


class _InternetProfile_X25Options_X3Profile_Type(Integer32):
    """Custom type internetProfile_X25Options_X3Profile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("ccSspProfile", 5),
          ("ccTspProfile", 6),
          ("crtProfile", 1),
          ("customProfile", 11),
          ("defaultProfile", 3),
          ("hardcopyProfile", 7),
          ("hdxProfile", 8),
          ("infonetProfile", 2),
          ("nullProfile", 10),
          ("posProfile", 12),
          ("scenProfile", 4),
          ("sharkProfile", 9))
    )


_InternetProfile_X25Options_X3Profile_Type.__name__ = "Integer32"
_InternetProfile_X25Options_X3Profile_Object = MibScalar
internetProfile_X25Options_X3Profile = _InternetProfile_X25Options_X3Profile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 159),
    _InternetProfile_X25Options_X3Profile_Type()
)
internetProfile_X25Options_X3Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_X3Profile.setStatus("mandatory")
_InternetProfile_X25Options_MaxCalls_Type = Integer32
_InternetProfile_X25Options_MaxCalls_Object = MibScalar
internetProfile_X25Options_MaxCalls = _InternetProfile_X25Options_MaxCalls_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 160),
    _InternetProfile_X25Options_MaxCalls_Type()
)
internetProfile_X25Options_MaxCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_MaxCalls.setStatus("mandatory")


class _InternetProfile_X25Options_VcTimerEnable_Type(Integer32):
    """Custom type internetProfile_X25Options_VcTimerEnable based on Integer32"""
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


_InternetProfile_X25Options_VcTimerEnable_Type.__name__ = "Integer32"
_InternetProfile_X25Options_VcTimerEnable_Object = MibScalar
internetProfile_X25Options_VcTimerEnable = _InternetProfile_X25Options_VcTimerEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 161),
    _InternetProfile_X25Options_VcTimerEnable_Type()
)
internetProfile_X25Options_VcTimerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_VcTimerEnable.setStatus("mandatory")


class _InternetProfile_X25Options_X25EncapsType_Type(Integer32):
    """Custom type internetProfile_X25Options_X25EncapsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("aodi", 5),
          ("null", 3),
          ("ppp", 4),
          ("rfc877", 1),
          ("snap", 2))
    )


_InternetProfile_X25Options_X25EncapsType_Type.__name__ = "Integer32"
_InternetProfile_X25Options_X25EncapsType_Object = MibScalar
internetProfile_X25Options_X25EncapsType = _InternetProfile_X25Options_X25EncapsType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 162),
    _InternetProfile_X25Options_X25EncapsType_Type()
)
internetProfile_X25Options_X25EncapsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_X25EncapsType.setStatus("mandatory")


class _InternetProfile_X25Options_ReverseCharge_Type(Integer32):
    """Custom type internetProfile_X25Options_ReverseCharge based on Integer32"""
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


_InternetProfile_X25Options_ReverseCharge_Type.__name__ = "Integer32"
_InternetProfile_X25Options_ReverseCharge_Object = MibScalar
internetProfile_X25Options_ReverseCharge = _InternetProfile_X25Options_ReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 164),
    _InternetProfile_X25Options_ReverseCharge_Type()
)
internetProfile_X25Options_ReverseCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_ReverseCharge.setStatus("mandatory")


class _InternetProfile_X25Options_CallMode_Type(Integer32):
    """Custom type internetProfile_X25Options_CallMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("incoming", 3),
          ("outgoing", 2))
    )


_InternetProfile_X25Options_CallMode_Type.__name__ = "Integer32"
_InternetProfile_X25Options_CallMode_Object = MibScalar
internetProfile_X25Options_CallMode = _InternetProfile_X25Options_CallMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 165),
    _InternetProfile_X25Options_CallMode_Type()
)
internetProfile_X25Options_CallMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_CallMode.setStatus("mandatory")
_InternetProfile_X25Options_InactivityTimer_Type = Integer32
_InternetProfile_X25Options_InactivityTimer_Object = MibScalar
internetProfile_X25Options_InactivityTimer = _InternetProfile_X25Options_InactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 167),
    _InternetProfile_X25Options_InactivityTimer_Type()
)
internetProfile_X25Options_InactivityTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_X25Options_InactivityTimer.setStatus("mandatory")
_InternetProfile_X25Options_X25Rpoa_Type = DisplayString
_InternetProfile_X25Options_X25Rpoa_Object = MibScalar
internetProfile_X25Options_X25Rpoa = _InternetProfile_X25Options_X25Rpoa_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 169),
    _InternetProfile_X25Options_X25Rpoa_Type()
)
internetProfile_X25Options_X25Rpoa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_X25Rpoa.setStatus("mandatory")
_InternetProfile_X25Options_X25CugIndex_Type = DisplayString
_InternetProfile_X25Options_X25CugIndex_Object = MibScalar
internetProfile_X25Options_X25CugIndex = _InternetProfile_X25Options_X25CugIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 170),
    _InternetProfile_X25Options_X25CugIndex_Type()
)
internetProfile_X25Options_X25CugIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_X25CugIndex.setStatus("mandatory")
_InternetProfile_X25Options_X25Nui_Type = DisplayString
_InternetProfile_X25Options_X25Nui_Object = MibScalar
internetProfile_X25Options_X25Nui = _InternetProfile_X25Options_X25Nui_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 171),
    _InternetProfile_X25Options_X25Nui_Type()
)
internetProfile_X25Options_X25Nui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_X25Nui.setStatus("mandatory")
_InternetProfile_X25Options_PadBanner_Type = DisplayString
_InternetProfile_X25Options_PadBanner_Object = MibScalar
internetProfile_X25Options_PadBanner = _InternetProfile_X25Options_PadBanner_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 172),
    _InternetProfile_X25Options_PadBanner_Type()
)
internetProfile_X25Options_PadBanner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_X25Options_PadBanner.setStatus("mandatory")
_InternetProfile_X25Options_PadPrompt_Type = DisplayString
_InternetProfile_X25Options_PadPrompt_Object = MibScalar
internetProfile_X25Options_PadPrompt = _InternetProfile_X25Options_PadPrompt_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 173),
    _InternetProfile_X25Options_PadPrompt_Type()
)
internetProfile_X25Options_PadPrompt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_X25Options_PadPrompt.setStatus("mandatory")
_InternetProfile_X25Options_PadNuiPrompt_Type = DisplayString
_InternetProfile_X25Options_PadNuiPrompt_Object = MibScalar
internetProfile_X25Options_PadNuiPrompt = _InternetProfile_X25Options_PadNuiPrompt_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 174),
    _InternetProfile_X25Options_PadNuiPrompt_Type()
)
internetProfile_X25Options_PadNuiPrompt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_X25Options_PadNuiPrompt.setStatus("mandatory")
_InternetProfile_X25Options_PadNuiPwPrompt_Type = DisplayString
_InternetProfile_X25Options_PadNuiPwPrompt_Object = MibScalar
internetProfile_X25Options_PadNuiPwPrompt = _InternetProfile_X25Options_PadNuiPwPrompt_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 175),
    _InternetProfile_X25Options_PadNuiPwPrompt_Type()
)
internetProfile_X25Options_PadNuiPwPrompt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_X25Options_PadNuiPwPrompt.setStatus("mandatory")
_InternetProfile_X25Options_PadAlias1_Type = DisplayString
_InternetProfile_X25Options_PadAlias1_Object = MibScalar
internetProfile_X25Options_PadAlias1 = _InternetProfile_X25Options_PadAlias1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 176),
    _InternetProfile_X25Options_PadAlias1_Type()
)
internetProfile_X25Options_PadAlias1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_X25Options_PadAlias1.setStatus("mandatory")
_InternetProfile_X25Options_PadAlias2_Type = DisplayString
_InternetProfile_X25Options_PadAlias2_Object = MibScalar
internetProfile_X25Options_PadAlias2 = _InternetProfile_X25Options_PadAlias2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 177),
    _InternetProfile_X25Options_PadAlias2_Type()
)
internetProfile_X25Options_PadAlias2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_X25Options_PadAlias2.setStatus("mandatory")
_InternetProfile_X25Options_PadAlias3_Type = DisplayString
_InternetProfile_X25Options_PadAlias3_Object = MibScalar
internetProfile_X25Options_PadAlias3 = _InternetProfile_X25Options_PadAlias3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 178),
    _InternetProfile_X25Options_PadAlias3_Type()
)
internetProfile_X25Options_PadAlias3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_X25Options_PadAlias3.setStatus("mandatory")


class _InternetProfile_X25Options_PadDiagDisp_Type(Integer32):
    """Custom type internetProfile_X25Options_PadDiagDisp based on Integer32"""
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


_InternetProfile_X25Options_PadDiagDisp_Type.__name__ = "Integer32"
_InternetProfile_X25Options_PadDiagDisp_Object = MibScalar
internetProfile_X25Options_PadDiagDisp = _InternetProfile_X25Options_PadDiagDisp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 179),
    _InternetProfile_X25Options_PadDiagDisp_Type()
)
internetProfile_X25Options_PadDiagDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_PadDiagDisp.setStatus("mandatory")
_InternetProfile_X25Options_PadDefaultListen_Type = DisplayString
_InternetProfile_X25Options_PadDefaultListen_Object = MibScalar
internetProfile_X25Options_PadDefaultListen = _InternetProfile_X25Options_PadDefaultListen_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 180),
    _InternetProfile_X25Options_PadDefaultListen_Type()
)
internetProfile_X25Options_PadDefaultListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_PadDefaultListen.setStatus("mandatory")
_InternetProfile_X25Options_PadDefaultPw_Type = DisplayString
_InternetProfile_X25Options_PadDefaultPw_Object = MibScalar
internetProfile_X25Options_PadDefaultPw = _InternetProfile_X25Options_PadDefaultPw_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 181),
    _InternetProfile_X25Options_PadDefaultPw_Type()
)
internetProfile_X25Options_PadDefaultPw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_PadDefaultPw.setStatus("mandatory")
_InternetProfile_EuOptions_DceAddr_Type = Integer32
_InternetProfile_EuOptions_DceAddr_Object = MibScalar
internetProfile_EuOptions_DceAddr = _InternetProfile_EuOptions_DceAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 182),
    _InternetProfile_EuOptions_DceAddr_Type()
)
internetProfile_EuOptions_DceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_EuOptions_DceAddr.setStatus("mandatory")
_InternetProfile_EuOptions_DteAddr_Type = Integer32
_InternetProfile_EuOptions_DteAddr_Object = MibScalar
internetProfile_EuOptions_DteAddr = _InternetProfile_EuOptions_DteAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 183),
    _InternetProfile_EuOptions_DteAddr_Type()
)
internetProfile_EuOptions_DteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_EuOptions_DteAddr.setStatus("mandatory")
_InternetProfile_EuOptions_Mru_Type = Integer32
_InternetProfile_EuOptions_Mru_Object = MibScalar
internetProfile_EuOptions_Mru = _InternetProfile_EuOptions_Mru_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 184),
    _InternetProfile_EuOptions_Mru_Type()
)
internetProfile_EuOptions_Mru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_EuOptions_Mru.setStatus("mandatory")
_InternetProfile_X75Options_KFramesOutstanding_Type = Integer32
_InternetProfile_X75Options_KFramesOutstanding_Object = MibScalar
internetProfile_X75Options_KFramesOutstanding = _InternetProfile_X75Options_KFramesOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 185),
    _InternetProfile_X75Options_KFramesOutstanding_Type()
)
internetProfile_X75Options_KFramesOutstanding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X75Options_KFramesOutstanding.setStatus("mandatory")
_InternetProfile_X75Options_N2Retransmissions_Type = Integer32
_InternetProfile_X75Options_N2Retransmissions_Object = MibScalar
internetProfile_X75Options_N2Retransmissions = _InternetProfile_X75Options_N2Retransmissions_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 186),
    _InternetProfile_X75Options_N2Retransmissions_Type()
)
internetProfile_X75Options_N2Retransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X75Options_N2Retransmissions.setStatus("mandatory")
_InternetProfile_X75Options_T1RetranTimer_Type = Integer32
_InternetProfile_X75Options_T1RetranTimer_Object = MibScalar
internetProfile_X75Options_T1RetranTimer = _InternetProfile_X75Options_T1RetranTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 187),
    _InternetProfile_X75Options_T1RetranTimer_Type()
)
internetProfile_X75Options_T1RetranTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X75Options_T1RetranTimer.setStatus("mandatory")
_InternetProfile_X75Options_FrameLength_Type = Integer32
_InternetProfile_X75Options_FrameLength_Object = MibScalar
internetProfile_X75Options_FrameLength = _InternetProfile_X75Options_FrameLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 188),
    _InternetProfile_X75Options_FrameLength_Type()
)
internetProfile_X75Options_FrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X75Options_FrameLength.setStatus("mandatory")


class _InternetProfile_AppletalkOptions_AtalkRoutingEnabled_Type(Integer32):
    """Custom type internetProfile_AppletalkOptions_AtalkRoutingEnabled based on Integer32"""
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


_InternetProfile_AppletalkOptions_AtalkRoutingEnabled_Type.__name__ = "Integer32"
_InternetProfile_AppletalkOptions_AtalkRoutingEnabled_Object = MibScalar
internetProfile_AppletalkOptions_AtalkRoutingEnabled = _InternetProfile_AppletalkOptions_AtalkRoutingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 189),
    _InternetProfile_AppletalkOptions_AtalkRoutingEnabled_Type()
)
internetProfile_AppletalkOptions_AtalkRoutingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AppletalkOptions_AtalkRoutingEnabled.setStatus("mandatory")
_InternetProfile_AppletalkOptions_AtalkStaticZoneName_Type = DisplayString
_InternetProfile_AppletalkOptions_AtalkStaticZoneName_Object = MibScalar
internetProfile_AppletalkOptions_AtalkStaticZoneName = _InternetProfile_AppletalkOptions_AtalkStaticZoneName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 190),
    _InternetProfile_AppletalkOptions_AtalkStaticZoneName_Type()
)
internetProfile_AppletalkOptions_AtalkStaticZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AppletalkOptions_AtalkStaticZoneName.setStatus("mandatory")
_InternetProfile_AppletalkOptions_AtalkStaticNetStart_Type = Integer32
_InternetProfile_AppletalkOptions_AtalkStaticNetStart_Object = MibScalar
internetProfile_AppletalkOptions_AtalkStaticNetStart = _InternetProfile_AppletalkOptions_AtalkStaticNetStart_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 191),
    _InternetProfile_AppletalkOptions_AtalkStaticNetStart_Type()
)
internetProfile_AppletalkOptions_AtalkStaticNetStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AppletalkOptions_AtalkStaticNetStart.setStatus("mandatory")
_InternetProfile_AppletalkOptions_AtalkStaticNetEnd_Type = Integer32
_InternetProfile_AppletalkOptions_AtalkStaticNetEnd_Object = MibScalar
internetProfile_AppletalkOptions_AtalkStaticNetEnd = _InternetProfile_AppletalkOptions_AtalkStaticNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 192),
    _InternetProfile_AppletalkOptions_AtalkStaticNetEnd_Type()
)
internetProfile_AppletalkOptions_AtalkStaticNetEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AppletalkOptions_AtalkStaticNetEnd.setStatus("mandatory")


class _InternetProfile_AppletalkOptions_AtalkPeerMode_Type(Integer32):
    """Custom type internetProfile_AppletalkOptions_AtalkPeerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dialinPeer", 2),
          ("routerPeer", 1))
    )


_InternetProfile_AppletalkOptions_AtalkPeerMode_Type.__name__ = "Integer32"
_InternetProfile_AppletalkOptions_AtalkPeerMode_Object = MibScalar
internetProfile_AppletalkOptions_AtalkPeerMode = _InternetProfile_AppletalkOptions_AtalkPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 193),
    _InternetProfile_AppletalkOptions_AtalkPeerMode_Type()
)
internetProfile_AppletalkOptions_AtalkPeerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AppletalkOptions_AtalkPeerMode.setStatus("mandatory")


class _InternetProfile_UsrRadOptions_AcctType_Type(Integer32):
    """Custom type internetProfile_UsrRadOptions_AcctType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("global", 1),
          ("local", 2))
    )


_InternetProfile_UsrRadOptions_AcctType_Type.__name__ = "Integer32"
_InternetProfile_UsrRadOptions_AcctType_Object = MibScalar
internetProfile_UsrRadOptions_AcctType = _InternetProfile_UsrRadOptions_AcctType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 194),
    _InternetProfile_UsrRadOptions_AcctType_Type()
)
internetProfile_UsrRadOptions_AcctType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_UsrRadOptions_AcctType.setStatus("mandatory")
_InternetProfile_UsrRadOptions_AcctHost_Type = IpAddress
_InternetProfile_UsrRadOptions_AcctHost_Object = MibScalar
internetProfile_UsrRadOptions_AcctHost = _InternetProfile_UsrRadOptions_AcctHost_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 195),
    _InternetProfile_UsrRadOptions_AcctHost_Type()
)
internetProfile_UsrRadOptions_AcctHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_UsrRadOptions_AcctHost.setStatus("mandatory")
_InternetProfile_UsrRadOptions_AcctPort_Type = Integer32
_InternetProfile_UsrRadOptions_AcctPort_Object = MibScalar
internetProfile_UsrRadOptions_AcctPort = _InternetProfile_UsrRadOptions_AcctPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 196),
    _InternetProfile_UsrRadOptions_AcctPort_Type()
)
internetProfile_UsrRadOptions_AcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_UsrRadOptions_AcctPort.setStatus("mandatory")
_InternetProfile_UsrRadOptions_AcctKey_Type = DisplayString
_InternetProfile_UsrRadOptions_AcctKey_Object = MibScalar
internetProfile_UsrRadOptions_AcctKey = _InternetProfile_UsrRadOptions_AcctKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 197),
    _InternetProfile_UsrRadOptions_AcctKey_Type()
)
internetProfile_UsrRadOptions_AcctKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_UsrRadOptions_AcctKey.setStatus("mandatory")
_InternetProfile_UsrRadOptions_AcctTimeout_Type = Integer32
_InternetProfile_UsrRadOptions_AcctTimeout_Object = MibScalar
internetProfile_UsrRadOptions_AcctTimeout = _InternetProfile_UsrRadOptions_AcctTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 198),
    _InternetProfile_UsrRadOptions_AcctTimeout_Type()
)
internetProfile_UsrRadOptions_AcctTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_UsrRadOptions_AcctTimeout.setStatus("mandatory")


class _InternetProfile_UsrRadOptions_AcctIdBase_Type(Integer32):
    """Custom type internetProfile_UsrRadOptions_AcctIdBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acctBase10", 1),
          ("acctBase16", 2))
    )


_InternetProfile_UsrRadOptions_AcctIdBase_Type.__name__ = "Integer32"
_InternetProfile_UsrRadOptions_AcctIdBase_Object = MibScalar
internetProfile_UsrRadOptions_AcctIdBase = _InternetProfile_UsrRadOptions_AcctIdBase_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 199),
    _InternetProfile_UsrRadOptions_AcctIdBase_Type()
)
internetProfile_UsrRadOptions_AcctIdBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_UsrRadOptions_AcctIdBase.setStatus("mandatory")
_InternetProfile_CalledNumber_Type = DisplayString
_InternetProfile_CalledNumber_Object = MibScalar
internetProfile_CalledNumber = _InternetProfile_CalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 200),
    _InternetProfile_CalledNumber_Type()
)
internetProfile_CalledNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_CalledNumber.setStatus("mandatory")


class _InternetProfile_DhcpOptions_ReplyEnabled_Type(Integer32):
    """Custom type internetProfile_DhcpOptions_ReplyEnabled based on Integer32"""
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


_InternetProfile_DhcpOptions_ReplyEnabled_Type.__name__ = "Integer32"
_InternetProfile_DhcpOptions_ReplyEnabled_Object = MibScalar
internetProfile_DhcpOptions_ReplyEnabled = _InternetProfile_DhcpOptions_ReplyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 201),
    _InternetProfile_DhcpOptions_ReplyEnabled_Type()
)
internetProfile_DhcpOptions_ReplyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_DhcpOptions_ReplyEnabled.setStatus("mandatory")
_InternetProfile_DhcpOptions_PoolNumber_Type = Integer32
_InternetProfile_DhcpOptions_PoolNumber_Object = MibScalar
internetProfile_DhcpOptions_PoolNumber = _InternetProfile_DhcpOptions_PoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 202),
    _InternetProfile_DhcpOptions_PoolNumber_Type()
)
internetProfile_DhcpOptions_PoolNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_DhcpOptions_PoolNumber.setStatus("mandatory")
_InternetProfile_DhcpOptions_MaximumLeases_Type = Integer32
_InternetProfile_DhcpOptions_MaximumLeases_Object = MibScalar
internetProfile_DhcpOptions_MaximumLeases = _InternetProfile_DhcpOptions_MaximumLeases_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 203),
    _InternetProfile_DhcpOptions_MaximumLeases_Type()
)
internetProfile_DhcpOptions_MaximumLeases.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_DhcpOptions_MaximumLeases.setStatus("mandatory")
_InternetProfile_T3posOptions_X25Profile_Type = DisplayString
_InternetProfile_T3posOptions_X25Profile_Object = MibScalar
internetProfile_T3posOptions_X25Profile = _InternetProfile_T3posOptions_X25Profile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 205),
    _InternetProfile_T3posOptions_X25Profile_Type()
)
internetProfile_T3posOptions_X25Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_X25Profile.setStatus("mandatory")
_InternetProfile_T3posOptions_MaxCalls_Type = Integer32
_InternetProfile_T3posOptions_MaxCalls_Object = MibScalar
internetProfile_T3posOptions_MaxCalls = _InternetProfile_T3posOptions_MaxCalls_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 206),
    _InternetProfile_T3posOptions_MaxCalls_Type()
)
internetProfile_T3posOptions_MaxCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_MaxCalls.setStatus("mandatory")
_InternetProfile_T3posOptions_AutoCallX121Address_Type = DisplayString
_InternetProfile_T3posOptions_AutoCallX121Address_Object = MibScalar
internetProfile_T3posOptions_AutoCallX121Address = _InternetProfile_T3posOptions_AutoCallX121Address_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 207),
    _InternetProfile_T3posOptions_AutoCallX121Address_Type()
)
internetProfile_T3posOptions_AutoCallX121Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_AutoCallX121Address.setStatus("mandatory")


class _InternetProfile_T3posOptions_ReverseCharge_Type(Integer32):
    """Custom type internetProfile_T3posOptions_ReverseCharge based on Integer32"""
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


_InternetProfile_T3posOptions_ReverseCharge_Type.__name__ = "Integer32"
_InternetProfile_T3posOptions_ReverseCharge_Object = MibScalar
internetProfile_T3posOptions_ReverseCharge = _InternetProfile_T3posOptions_ReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 208),
    _InternetProfile_T3posOptions_ReverseCharge_Type()
)
internetProfile_T3posOptions_ReverseCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_ReverseCharge.setStatus("mandatory")
_InternetProfile_T3posOptions_Answer_Type = DisplayString
_InternetProfile_T3posOptions_Answer_Object = MibScalar
internetProfile_T3posOptions_Answer = _InternetProfile_T3posOptions_Answer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 209),
    _InternetProfile_T3posOptions_Answer_Type()
)
internetProfile_T3posOptions_Answer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_Answer.setStatus("mandatory")


class _InternetProfile_T3posOptions_T3PosHostInitMode_Type(Integer32):
    """Custom type internetProfile_T3posOptions_T3PosHostInitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("binLocal", 2),
          ("blind", 4),
          ("local", 1),
          ("transparent", 3),
          ("unknown", 5))
    )


_InternetProfile_T3posOptions_T3PosHostInitMode_Type.__name__ = "Integer32"
_InternetProfile_T3posOptions_T3PosHostInitMode_Object = MibScalar
internetProfile_T3posOptions_T3PosHostInitMode = _InternetProfile_T3posOptions_T3PosHostInitMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 210),
    _InternetProfile_T3posOptions_T3PosHostInitMode_Type()
)
internetProfile_T3posOptions_T3PosHostInitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_T3PosHostInitMode.setStatus("mandatory")


class _InternetProfile_T3posOptions_T3PosDteInitMode_Type(Integer32):
    """Custom type internetProfile_T3posOptions_T3PosDteInitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("binLocal", 2),
          ("blind", 4),
          ("local", 1),
          ("transparent", 3),
          ("unknown", 5))
    )


_InternetProfile_T3posOptions_T3PosDteInitMode_Type.__name__ = "Integer32"
_InternetProfile_T3posOptions_T3PosDteInitMode_Object = MibScalar
internetProfile_T3posOptions_T3PosDteInitMode = _InternetProfile_T3posOptions_T3PosDteInitMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 211),
    _InternetProfile_T3posOptions_T3PosDteInitMode_Type()
)
internetProfile_T3posOptions_T3PosDteInitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_T3PosDteInitMode.setStatus("mandatory")


class _InternetProfile_T3posOptions_T3PosEnqHandling_Type(Integer32):
    """Custom type internetProfile_T3posOptions_T3PosEnqHandling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_InternetProfile_T3posOptions_T3PosEnqHandling_Type.__name__ = "Integer32"
_InternetProfile_T3posOptions_T3PosEnqHandling_Object = MibScalar
internetProfile_T3posOptions_T3PosEnqHandling = _InternetProfile_T3posOptions_T3PosEnqHandling_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 212),
    _InternetProfile_T3posOptions_T3PosEnqHandling_Type()
)
internetProfile_T3posOptions_T3PosEnqHandling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_T3PosEnqHandling.setStatus("mandatory")


class _InternetProfile_T3posOptions_T3PosMaxBlockSize_Type(Integer32):
    """Custom type internetProfile_T3posOptions_T3PosMaxBlockSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n-1024", 2),
          ("n-512", 1))
    )


_InternetProfile_T3posOptions_T3PosMaxBlockSize_Type.__name__ = "Integer32"
_InternetProfile_T3posOptions_T3PosMaxBlockSize_Object = MibScalar
internetProfile_T3posOptions_T3PosMaxBlockSize = _InternetProfile_T3posOptions_T3PosMaxBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 213),
    _InternetProfile_T3posOptions_T3PosMaxBlockSize_Type()
)
internetProfile_T3posOptions_T3PosMaxBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_T3PosMaxBlockSize.setStatus("mandatory")
_InternetProfile_T3posOptions_T3PosT1_Type = Integer32
_InternetProfile_T3posOptions_T3PosT1_Object = MibScalar
internetProfile_T3posOptions_T3PosT1 = _InternetProfile_T3posOptions_T3PosT1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 214),
    _InternetProfile_T3posOptions_T3PosT1_Type()
)
internetProfile_T3posOptions_T3PosT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_T3PosT1.setStatus("mandatory")
_InternetProfile_T3posOptions_T3PosT2_Type = Integer32
_InternetProfile_T3posOptions_T3PosT2_Object = MibScalar
internetProfile_T3posOptions_T3PosT2 = _InternetProfile_T3posOptions_T3PosT2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 215),
    _InternetProfile_T3posOptions_T3PosT2_Type()
)
internetProfile_T3posOptions_T3PosT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_T3PosT2.setStatus("mandatory")
_InternetProfile_T3posOptions_T3PosT3_Type = Integer32
_InternetProfile_T3posOptions_T3PosT3_Object = MibScalar
internetProfile_T3posOptions_T3PosT3 = _InternetProfile_T3posOptions_T3PosT3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 216),
    _InternetProfile_T3posOptions_T3PosT3_Type()
)
internetProfile_T3posOptions_T3PosT3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_T3PosT3.setStatus("mandatory")
_InternetProfile_T3posOptions_T3PosT4_Type = Integer32
_InternetProfile_T3posOptions_T3PosT4_Object = MibScalar
internetProfile_T3posOptions_T3PosT4 = _InternetProfile_T3posOptions_T3PosT4_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 217),
    _InternetProfile_T3posOptions_T3PosT4_Type()
)
internetProfile_T3posOptions_T3PosT4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_T3PosT4.setStatus("mandatory")
_InternetProfile_T3posOptions_T3PosT5_Type = Integer32
_InternetProfile_T3posOptions_T3PosT5_Object = MibScalar
internetProfile_T3posOptions_T3PosT5 = _InternetProfile_T3posOptions_T3PosT5_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 218),
    _InternetProfile_T3posOptions_T3PosT5_Type()
)
internetProfile_T3posOptions_T3PosT5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_T3PosT5.setStatus("mandatory")
_InternetProfile_T3posOptions_T3PosT6_Type = Integer32
_InternetProfile_T3posOptions_T3PosT6_Object = MibScalar
internetProfile_T3posOptions_T3PosT6 = _InternetProfile_T3posOptions_T3PosT6_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 219),
    _InternetProfile_T3posOptions_T3PosT6_Type()
)
internetProfile_T3posOptions_T3PosT6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_T3PosT6.setStatus("mandatory")


class _InternetProfile_T3posOptions_T3PosMethodOfHostNotif_Type(Integer32):
    """Custom type internetProfile_T3posOptions_T3PosMethodOfHostNotif based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("callRequestPacket", 2),
          ("modeSwitchFrame", 3),
          ("none", 1))
    )


_InternetProfile_T3posOptions_T3PosMethodOfHostNotif_Type.__name__ = "Integer32"
_InternetProfile_T3posOptions_T3PosMethodOfHostNotif_Object = MibScalar
internetProfile_T3posOptions_T3PosMethodOfHostNotif = _InternetProfile_T3posOptions_T3PosMethodOfHostNotif_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 220),
    _InternetProfile_T3posOptions_T3PosMethodOfHostNotif_Type()
)
internetProfile_T3posOptions_T3PosMethodOfHostNotif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_T3PosMethodOfHostNotif.setStatus("mandatory")


class _InternetProfile_T3posOptions_T3PosPidSelection_Type(Integer32):
    """Custom type internetProfile_T3posOptions_T3PosPidSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t3pos", 2),
          ("x29", 1))
    )


_InternetProfile_T3posOptions_T3PosPidSelection_Type.__name__ = "Integer32"
_InternetProfile_T3posOptions_T3PosPidSelection_Object = MibScalar
internetProfile_T3posOptions_T3PosPidSelection = _InternetProfile_T3posOptions_T3PosPidSelection_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 221),
    _InternetProfile_T3posOptions_T3PosPidSelection_Type()
)
internetProfile_T3posOptions_T3PosPidSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_T3PosPidSelection.setStatus("mandatory")


class _InternetProfile_T3posOptions_T3PosAckSuppression_Type(Integer32):
    """Custom type internetProfile_T3posOptions_T3PosAckSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_InternetProfile_T3posOptions_T3PosAckSuppression_Type.__name__ = "Integer32"
_InternetProfile_T3posOptions_T3PosAckSuppression_Object = MibScalar
internetProfile_T3posOptions_T3PosAckSuppression = _InternetProfile_T3posOptions_T3PosAckSuppression_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 222),
    _InternetProfile_T3posOptions_T3PosAckSuppression_Type()
)
internetProfile_T3posOptions_T3PosAckSuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_T3PosAckSuppression.setStatus("mandatory")
_InternetProfile_T3posOptions_X25Rpoa_Type = DisplayString
_InternetProfile_T3posOptions_X25Rpoa_Object = MibScalar
internetProfile_T3posOptions_X25Rpoa = _InternetProfile_T3posOptions_X25Rpoa_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 223),
    _InternetProfile_T3posOptions_X25Rpoa_Type()
)
internetProfile_T3posOptions_X25Rpoa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_X25Rpoa.setStatus("mandatory")
_InternetProfile_T3posOptions_X25CugIndex_Type = DisplayString
_InternetProfile_T3posOptions_X25CugIndex_Object = MibScalar
internetProfile_T3posOptions_X25CugIndex = _InternetProfile_T3posOptions_X25CugIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 224),
    _InternetProfile_T3posOptions_X25CugIndex_Type()
)
internetProfile_T3posOptions_X25CugIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_X25CugIndex.setStatus("mandatory")
_InternetProfile_T3posOptions_X25Nui_Type = DisplayString
_InternetProfile_T3posOptions_X25Nui_Object = MibScalar
internetProfile_T3posOptions_X25Nui = _InternetProfile_T3posOptions_X25Nui_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 225),
    _InternetProfile_T3posOptions_X25Nui_Type()
)
internetProfile_T3posOptions_X25Nui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_X25Nui.setStatus("mandatory")


class _InternetProfile_T3posOptions_DataFormat_Type(Integer32):
    """Custom type internetProfile_T3posOptions_DataFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dataFormat7e1", 1),
          ("dataFormat7m1", 3),
          ("dataFormat7o1", 2),
          ("dataFormat7s1", 4),
          ("dataFormat8n1", 5))
    )


_InternetProfile_T3posOptions_DataFormat_Type.__name__ = "Integer32"
_InternetProfile_T3posOptions_DataFormat_Object = MibScalar
internetProfile_T3posOptions_DataFormat = _InternetProfile_T3posOptions_DataFormat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 226),
    _InternetProfile_T3posOptions_DataFormat_Type()
)
internetProfile_T3posOptions_DataFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_DataFormat.setStatus("mandatory")


class _InternetProfile_T3posOptions_LinkAccessType_Type(Integer32):
    """Custom type internetProfile_T3posOptions_LinkAccessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("axtypeDedicated", 1),
          ("axtypeDialIn", 2))
    )


_InternetProfile_T3posOptions_LinkAccessType_Type.__name__ = "Integer32"
_InternetProfile_T3posOptions_LinkAccessType_Object = MibScalar
internetProfile_T3posOptions_LinkAccessType = _InternetProfile_T3posOptions_LinkAccessType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 227),
    _InternetProfile_T3posOptions_LinkAccessType_Type()
)
internetProfile_T3posOptions_LinkAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_T3posOptions_LinkAccessType.setStatus("mandatory")


class _InternetProfile_FramedOnly_Type(Integer32):
    """Custom type internetProfile_FramedOnly based on Integer32"""
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


_InternetProfile_FramedOnly_Type.__name__ = "Integer32"
_InternetProfile_FramedOnly_Object = MibScalar
internetProfile_FramedOnly = _InternetProfile_FramedOnly_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 228),
    _InternetProfile_FramedOnly_Type()
)
internetProfile_FramedOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_FramedOnly.setStatus("mandatory")
_InternetProfile_AltdialNumber1_Type = DisplayString
_InternetProfile_AltdialNumber1_Object = MibScalar
internetProfile_AltdialNumber1 = _InternetProfile_AltdialNumber1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 229),
    _InternetProfile_AltdialNumber1_Type()
)
internetProfile_AltdialNumber1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AltdialNumber1.setStatus("mandatory")
_InternetProfile_AltdialNumber2_Type = DisplayString
_InternetProfile_AltdialNumber2_Object = MibScalar
internetProfile_AltdialNumber2 = _InternetProfile_AltdialNumber2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 230),
    _InternetProfile_AltdialNumber2_Type()
)
internetProfile_AltdialNumber2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AltdialNumber2.setStatus("mandatory")
_InternetProfile_AltdialNumber3_Type = DisplayString
_InternetProfile_AltdialNumber3_Object = MibScalar
internetProfile_AltdialNumber3 = _InternetProfile_AltdialNumber3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 231),
    _InternetProfile_AltdialNumber3_Type()
)
internetProfile_AltdialNumber3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AltdialNumber3.setStatus("mandatory")
_InternetProfile_X32Options_X32Profile_Type = DisplayString
_InternetProfile_X32Options_X32Profile_Object = MibScalar
internetProfile_X32Options_X32Profile = _InternetProfile_X32Options_X32Profile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 232),
    _InternetProfile_X32Options_X32Profile_Type()
)
internetProfile_X32Options_X32Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X32Options_X32Profile.setStatus("mandatory")


class _InternetProfile_X32Options_CallMode_Type(Integer32):
    """Custom type internetProfile_X32Options_CallMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("incoming", 3),
          ("outgoing", 2))
    )


_InternetProfile_X32Options_CallMode_Type.__name__ = "Integer32"
_InternetProfile_X32Options_CallMode_Object = MibScalar
internetProfile_X32Options_CallMode = _InternetProfile_X32Options_CallMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 233),
    _InternetProfile_X32Options_CallMode_Type()
)
internetProfile_X32Options_CallMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_X32Options_CallMode.setStatus("mandatory")


class _InternetProfile_TunnelOptions_ProfileType_Type(Integer32):
    """Custom type internetProfile_TunnelOptions_ProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dialoutProfile", 4),
          ("disabled", 1),
          ("gatewayProfile", 3),
          ("mobileClient", 2))
    )


_InternetProfile_TunnelOptions_ProfileType_Type.__name__ = "Integer32"
_InternetProfile_TunnelOptions_ProfileType_Object = MibScalar
internetProfile_TunnelOptions_ProfileType = _InternetProfile_TunnelOptions_ProfileType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 234),
    _InternetProfile_TunnelOptions_ProfileType_Type()
)
internetProfile_TunnelOptions_ProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TunnelOptions_ProfileType.setStatus("mandatory")


class _InternetProfile_TunnelOptions_TunnelingProtocol_Type(Integer32):
    """Custom type internetProfile_TunnelOptions_TunnelingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("atmpProtocol", 5),
          ("disabled", 1),
          ("ipinipProtocol", 8),
          ("l2fProtocol", 3),
          ("l2tpProtocol", 4),
          ("pptpProtocol", 2),
          ("vtpProtocol", 6))
    )


_InternetProfile_TunnelOptions_TunnelingProtocol_Type.__name__ = "Integer32"
_InternetProfile_TunnelOptions_TunnelingProtocol_Object = MibScalar
internetProfile_TunnelOptions_TunnelingProtocol = _InternetProfile_TunnelOptions_TunnelingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 235),
    _InternetProfile_TunnelOptions_TunnelingProtocol_Type()
)
internetProfile_TunnelOptions_TunnelingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TunnelOptions_TunnelingProtocol.setStatus("mandatory")
_InternetProfile_TunnelOptions_MaxTunnels_Type = Integer32
_InternetProfile_TunnelOptions_MaxTunnels_Object = MibScalar
internetProfile_TunnelOptions_MaxTunnels = _InternetProfile_TunnelOptions_MaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 236),
    _InternetProfile_TunnelOptions_MaxTunnels_Type()
)
internetProfile_TunnelOptions_MaxTunnels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TunnelOptions_MaxTunnels.setStatus("mandatory")


class _InternetProfile_TunnelOptions_AtmpHaRip_Type(Integer32):
    """Custom type internetProfile_TunnelOptions_AtmpHaRip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ripOff", 1),
          ("ripSendV2", 2))
    )


_InternetProfile_TunnelOptions_AtmpHaRip_Type.__name__ = "Integer32"
_InternetProfile_TunnelOptions_AtmpHaRip_Object = MibScalar
internetProfile_TunnelOptions_AtmpHaRip = _InternetProfile_TunnelOptions_AtmpHaRip_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 237),
    _InternetProfile_TunnelOptions_AtmpHaRip_Type()
)
internetProfile_TunnelOptions_AtmpHaRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TunnelOptions_AtmpHaRip.setStatus("mandatory")
_InternetProfile_TunnelOptions_PrimaryTunnelServer_Type = DisplayString
_InternetProfile_TunnelOptions_PrimaryTunnelServer_Object = MibScalar
internetProfile_TunnelOptions_PrimaryTunnelServer = _InternetProfile_TunnelOptions_PrimaryTunnelServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 238),
    _InternetProfile_TunnelOptions_PrimaryTunnelServer_Type()
)
internetProfile_TunnelOptions_PrimaryTunnelServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TunnelOptions_PrimaryTunnelServer.setStatus("mandatory")
_InternetProfile_TunnelOptions_SecondaryTunnelServer_Type = DisplayString
_InternetProfile_TunnelOptions_SecondaryTunnelServer_Object = MibScalar
internetProfile_TunnelOptions_SecondaryTunnelServer = _InternetProfile_TunnelOptions_SecondaryTunnelServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 239),
    _InternetProfile_TunnelOptions_SecondaryTunnelServer_Type()
)
internetProfile_TunnelOptions_SecondaryTunnelServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TunnelOptions_SecondaryTunnelServer.setStatus("mandatory")
_InternetProfile_TunnelOptions_UdpPort_Type = Integer32
_InternetProfile_TunnelOptions_UdpPort_Object = MibScalar
internetProfile_TunnelOptions_UdpPort = _InternetProfile_TunnelOptions_UdpPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 240),
    _InternetProfile_TunnelOptions_UdpPort_Type()
)
internetProfile_TunnelOptions_UdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TunnelOptions_UdpPort.setStatus("mandatory")
_InternetProfile_TunnelOptions_Password_Type = DisplayString
_InternetProfile_TunnelOptions_Password_Object = MibScalar
internetProfile_TunnelOptions_Password = _InternetProfile_TunnelOptions_Password_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 241),
    _InternetProfile_TunnelOptions_Password_Type()
)
internetProfile_TunnelOptions_Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TunnelOptions_Password.setStatus("mandatory")
_InternetProfile_TunnelOptions_HomeNetworkName_Type = DisplayString
_InternetProfile_TunnelOptions_HomeNetworkName_Object = MibScalar
internetProfile_TunnelOptions_HomeNetworkName = _InternetProfile_TunnelOptions_HomeNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 242),
    _InternetProfile_TunnelOptions_HomeNetworkName_Type()
)
internetProfile_TunnelOptions_HomeNetworkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TunnelOptions_HomeNetworkName.setStatus("mandatory")


class _InternetProfile_PriNumberingPlanId_Type(Integer32):
    """Custom type internetProfile_PriNumberingPlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("iSDN", 2),
          ("private", 10),
          ("unknown", 1))
    )


_InternetProfile_PriNumberingPlanId_Type.__name__ = "Integer32"
_InternetProfile_PriNumberingPlanId_Object = MibScalar
internetProfile_PriNumberingPlanId = _InternetProfile_PriNumberingPlanId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 244),
    _InternetProfile_PriNumberingPlanId_Type()
)
internetProfile_PriNumberingPlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PriNumberingPlanId.setStatus("mandatory")
_InternetProfile_Vrouter_Type = DisplayString
_InternetProfile_Vrouter_Object = MibScalar
internetProfile_Vrouter = _InternetProfile_Vrouter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 245),
    _InternetProfile_Vrouter_Type()
)
internetProfile_Vrouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_Vrouter.setStatus("mandatory")


class _InternetProfile_AtmOptions_Atm1483type_Type(Integer32):
    """Custom type internetProfile_AtmOptions_Atm1483type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aal5Llc", 1),
          ("aal5Vc", 2))
    )


_InternetProfile_AtmOptions_Atm1483type_Type.__name__ = "Integer32"
_InternetProfile_AtmOptions_Atm1483type_Object = MibScalar
internetProfile_AtmOptions_Atm1483type = _InternetProfile_AtmOptions_Atm1483type_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 246),
    _InternetProfile_AtmOptions_Atm1483type_Type()
)
internetProfile_AtmOptions_Atm1483type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_Atm1483type.setStatus("mandatory")
_InternetProfile_AtmOptions_Vpi_Type = Integer32
_InternetProfile_AtmOptions_Vpi_Object = MibScalar
internetProfile_AtmOptions_Vpi = _InternetProfile_AtmOptions_Vpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 247),
    _InternetProfile_AtmOptions_Vpi_Type()
)
internetProfile_AtmOptions_Vpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_Vpi.setStatus("mandatory")
_InternetProfile_AtmOptions_Vci_Type = Integer32
_InternetProfile_AtmOptions_Vci_Object = MibScalar
internetProfile_AtmOptions_Vci = _InternetProfile_AtmOptions_Vci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 248),
    _InternetProfile_AtmOptions_Vci_Type()
)
internetProfile_AtmOptions_Vci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_Vci.setStatus("mandatory")


class _InternetProfile_Action_o_Type(Integer32):
    """Custom type internetProfile_Action_o based on Integer32"""
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


_InternetProfile_Action_o_Type.__name__ = "Integer32"
_InternetProfile_Action_o_Object = MibScalar
internetProfile_Action_o = _InternetProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 249),
    _InternetProfile_Action_o_Type()
)
internetProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_Action_o.setStatus("mandatory")


class _InternetProfile_IpOptions_OspfOptions_NetworkType_Type(Integer32):
    """Custom type internetProfile_IpOptions_OspfOptions_NetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("nonBroadcast", 3),
          ("pointToPoint", 4))
    )


_InternetProfile_IpOptions_OspfOptions_NetworkType_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_OspfOptions_NetworkType_Object = MibScalar
internetProfile_IpOptions_OspfOptions_NetworkType = _InternetProfile_IpOptions_OspfOptions_NetworkType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 250),
    _InternetProfile_IpOptions_OspfOptions_NetworkType_Type()
)
internetProfile_IpOptions_OspfOptions_NetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_NetworkType.setStatus("mandatory")
_InternetProfile_IpOptions_OspfOptions_PollInterval_Type = Integer32
_InternetProfile_IpOptions_OspfOptions_PollInterval_Object = MibScalar
internetProfile_IpOptions_OspfOptions_PollInterval = _InternetProfile_IpOptions_OspfOptions_PollInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 251),
    _InternetProfile_IpOptions_OspfOptions_PollInterval_Type()
)
internetProfile_IpOptions_OspfOptions_PollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_PollInterval.setStatus("mandatory")
_InternetProfile_IpOptions_OspfOptions_Md5AuthKey_Type = DisplayString
_InternetProfile_IpOptions_OspfOptions_Md5AuthKey_Object = MibScalar
internetProfile_IpOptions_OspfOptions_Md5AuthKey = _InternetProfile_IpOptions_OspfOptions_Md5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 252),
    _InternetProfile_IpOptions_OspfOptions_Md5AuthKey_Type()
)
internetProfile_IpOptions_OspfOptions_Md5AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_OspfOptions_Md5AuthKey.setStatus("mandatory")
_InternetProfile_BridgingOptions_Fill2_Type = Integer32
_InternetProfile_BridgingOptions_Fill2_Object = MibScalar
internetProfile_BridgingOptions_Fill2 = _InternetProfile_BridgingOptions_Fill2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 253),
    _InternetProfile_BridgingOptions_Fill2_Type()
)
internetProfile_BridgingOptions_Fill2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_BridgingOptions_Fill2.setStatus("mandatory")


class _InternetProfile_TelcoOptions_NasPortType_Type(Integer32):
    """Custom type internetProfile_TelcoOptions_NasPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("analog", 3),
          ("any", 1),
          ("arqPdcIsdn", 12),
          ("async", 4),
          ("digital", 2),
          ("isdnSync", 6),
          ("sync", 5),
          ("v110IsdnAsync", 8),
          ("v120IsdnAsync", 7),
          ("v32IsdnAsync", 10),
          ("vdspAsyncIsdn", 11),
          ("virtual", 9))
    )


_InternetProfile_TelcoOptions_NasPortType_Type.__name__ = "Integer32"
_InternetProfile_TelcoOptions_NasPortType_Object = MibScalar
internetProfile_TelcoOptions_NasPortType = _InternetProfile_TelcoOptions_NasPortType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 254),
    _InternetProfile_TelcoOptions_NasPortType_Type()
)
internetProfile_TelcoOptions_NasPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TelcoOptions_NasPortType.setStatus("mandatory")


class _InternetProfile_MpOptions_BodEnable_Type(Integer32):
    """Custom type internetProfile_MpOptions_BodEnable based on Integer32"""
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


_InternetProfile_MpOptions_BodEnable_Type.__name__ = "Integer32"
_InternetProfile_MpOptions_BodEnable_Object = MibScalar
internetProfile_MpOptions_BodEnable = _InternetProfile_MpOptions_BodEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 255),
    _InternetProfile_MpOptions_BodEnable_Type()
)
internetProfile_MpOptions_BodEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_MpOptions_BodEnable.setStatus("mandatory")
_InternetProfile_AtmOptions_NailedGroup_Type = Integer32
_InternetProfile_AtmOptions_NailedGroup_Object = MibScalar
internetProfile_AtmOptions_NailedGroup = _InternetProfile_AtmOptions_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 256),
    _InternetProfile_AtmOptions_NailedGroup_Type()
)
internetProfile_AtmOptions_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_NailedGroup.setStatus("mandatory")


class _InternetProfile_AtmOptions_AtmServiceType_Type(Integer32):
    """Custom type internetProfile_AtmOptions_AtmServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("atmAbrService", 3),
          ("atmCbrService", 2),
          ("atmUbrService", 1),
          ("atmVbrService", 4))
    )


_InternetProfile_AtmOptions_AtmServiceType_Type.__name__ = "Integer32"
_InternetProfile_AtmOptions_AtmServiceType_Object = MibScalar
internetProfile_AtmOptions_AtmServiceType = _InternetProfile_AtmOptions_AtmServiceType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 257),
    _InternetProfile_AtmOptions_AtmServiceType_Type()
)
internetProfile_AtmOptions_AtmServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_AtmServiceType.setStatus("mandatory")
_InternetProfile_AtmOptions_AtmServiceRate_Type = Integer32
_InternetProfile_AtmOptions_AtmServiceRate_Object = MibScalar
internetProfile_AtmOptions_AtmServiceRate = _InternetProfile_AtmOptions_AtmServiceRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 258),
    _InternetProfile_AtmOptions_AtmServiceRate_Type()
)
internetProfile_AtmOptions_AtmServiceRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_AtmServiceRate.setStatus("mandatory")
_InternetProfile_HdlcNrmOptions_SnrmResponseTimeout_Type = Integer32
_InternetProfile_HdlcNrmOptions_SnrmResponseTimeout_Object = MibScalar
internetProfile_HdlcNrmOptions_SnrmResponseTimeout = _InternetProfile_HdlcNrmOptions_SnrmResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 259),
    _InternetProfile_HdlcNrmOptions_SnrmResponseTimeout_Type()
)
internetProfile_HdlcNrmOptions_SnrmResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_HdlcNrmOptions_SnrmResponseTimeout.setStatus("mandatory")
_InternetProfile_HdlcNrmOptions_SnrmRetryCounter_Type = Integer32
_InternetProfile_HdlcNrmOptions_SnrmRetryCounter_Object = MibScalar
internetProfile_HdlcNrmOptions_SnrmRetryCounter = _InternetProfile_HdlcNrmOptions_SnrmRetryCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 260),
    _InternetProfile_HdlcNrmOptions_SnrmRetryCounter_Type()
)
internetProfile_HdlcNrmOptions_SnrmRetryCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_HdlcNrmOptions_SnrmRetryCounter.setStatus("mandatory")
_InternetProfile_HdlcNrmOptions_PollTimeout_Type = Integer32
_InternetProfile_HdlcNrmOptions_PollTimeout_Object = MibScalar
internetProfile_HdlcNrmOptions_PollTimeout = _InternetProfile_HdlcNrmOptions_PollTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 261),
    _InternetProfile_HdlcNrmOptions_PollTimeout_Type()
)
internetProfile_HdlcNrmOptions_PollTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_HdlcNrmOptions_PollTimeout.setStatus("mandatory")
_InternetProfile_HdlcNrmOptions_PollRate_Type = Integer32
_InternetProfile_HdlcNrmOptions_PollRate_Object = MibScalar
internetProfile_HdlcNrmOptions_PollRate = _InternetProfile_HdlcNrmOptions_PollRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 262),
    _InternetProfile_HdlcNrmOptions_PollRate_Type()
)
internetProfile_HdlcNrmOptions_PollRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_HdlcNrmOptions_PollRate.setStatus("mandatory")
_InternetProfile_HdlcNrmOptions_PollRetryCount_Type = Integer32
_InternetProfile_HdlcNrmOptions_PollRetryCount_Object = MibScalar
internetProfile_HdlcNrmOptions_PollRetryCount = _InternetProfile_HdlcNrmOptions_PollRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 263),
    _InternetProfile_HdlcNrmOptions_PollRetryCount_Type()
)
internetProfile_HdlcNrmOptions_PollRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_HdlcNrmOptions_PollRetryCount.setStatus("mandatory")


class _InternetProfile_HdlcNrmOptions_Primary_Type(Integer32):
    """Custom type internetProfile_HdlcNrmOptions_Primary based on Integer32"""
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


_InternetProfile_HdlcNrmOptions_Primary_Type.__name__ = "Integer32"
_InternetProfile_HdlcNrmOptions_Primary_Object = MibScalar
internetProfile_HdlcNrmOptions_Primary = _InternetProfile_HdlcNrmOptions_Primary_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 264),
    _InternetProfile_HdlcNrmOptions_Primary_Type()
)
internetProfile_HdlcNrmOptions_Primary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_HdlcNrmOptions_Primary.setStatus("mandatory")


class _InternetProfile_AtmConnectOptions_Atm1483type_Type(Integer32):
    """Custom type internetProfile_AtmConnectOptions_Atm1483type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aal5Llc", 1),
          ("aal5Vc", 2))
    )


_InternetProfile_AtmConnectOptions_Atm1483type_Type.__name__ = "Integer32"
_InternetProfile_AtmConnectOptions_Atm1483type_Object = MibScalar
internetProfile_AtmConnectOptions_Atm1483type = _InternetProfile_AtmConnectOptions_Atm1483type_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 265),
    _InternetProfile_AtmConnectOptions_Atm1483type_Type()
)
internetProfile_AtmConnectOptions_Atm1483type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_Atm1483type.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_Vpi_Type = Integer32
_InternetProfile_AtmConnectOptions_Vpi_Object = MibScalar
internetProfile_AtmConnectOptions_Vpi = _InternetProfile_AtmConnectOptions_Vpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 266),
    _InternetProfile_AtmConnectOptions_Vpi_Type()
)
internetProfile_AtmConnectOptions_Vpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_Vpi.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_Vci_Type = Integer32
_InternetProfile_AtmConnectOptions_Vci_Object = MibScalar
internetProfile_AtmConnectOptions_Vci = _InternetProfile_AtmConnectOptions_Vci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 267),
    _InternetProfile_AtmConnectOptions_Vci_Type()
)
internetProfile_AtmConnectOptions_Vci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_Vci.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_NailedGroup_Type = Integer32
_InternetProfile_AtmConnectOptions_NailedGroup_Object = MibScalar
internetProfile_AtmConnectOptions_NailedGroup = _InternetProfile_AtmConnectOptions_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 268),
    _InternetProfile_AtmConnectOptions_NailedGroup_Type()
)
internetProfile_AtmConnectOptions_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_NailedGroup.setStatus("mandatory")


class _InternetProfile_AtmConnectOptions_AtmServiceType_Type(Integer32):
    """Custom type internetProfile_AtmConnectOptions_AtmServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("atmAbrService", 3),
          ("atmCbrService", 2),
          ("atmUbrService", 1),
          ("atmVbrService", 4))
    )


_InternetProfile_AtmConnectOptions_AtmServiceType_Type.__name__ = "Integer32"
_InternetProfile_AtmConnectOptions_AtmServiceType_Object = MibScalar
internetProfile_AtmConnectOptions_AtmServiceType = _InternetProfile_AtmConnectOptions_AtmServiceType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 269),
    _InternetProfile_AtmConnectOptions_AtmServiceType_Type()
)
internetProfile_AtmConnectOptions_AtmServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_AtmServiceType.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_AtmServiceRate_Type = Integer32
_InternetProfile_AtmConnectOptions_AtmServiceRate_Object = MibScalar
internetProfile_AtmConnectOptions_AtmServiceRate = _InternetProfile_AtmConnectOptions_AtmServiceRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 270),
    _InternetProfile_AtmConnectOptions_AtmServiceRate_Type()
)
internetProfile_AtmConnectOptions_AtmServiceRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_AtmServiceRate.setStatus("mandatory")
_InternetProfile_Visa2Options_IdleCharacterDelay_Type = Integer32
_InternetProfile_Visa2Options_IdleCharacterDelay_Object = MibScalar
internetProfile_Visa2Options_IdleCharacterDelay = _InternetProfile_Visa2Options_IdleCharacterDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 271),
    _InternetProfile_Visa2Options_IdleCharacterDelay_Type()
)
internetProfile_Visa2Options_IdleCharacterDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_Visa2Options_IdleCharacterDelay.setStatus("mandatory")
_InternetProfile_Visa2Options_FirstDataForwardCharacter_Type = DisplayString
_InternetProfile_Visa2Options_FirstDataForwardCharacter_Object = MibScalar
internetProfile_Visa2Options_FirstDataForwardCharacter = _InternetProfile_Visa2Options_FirstDataForwardCharacter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 272),
    _InternetProfile_Visa2Options_FirstDataForwardCharacter_Type()
)
internetProfile_Visa2Options_FirstDataForwardCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_Visa2Options_FirstDataForwardCharacter.setStatus("mandatory")
_InternetProfile_Visa2Options_SecondDataForwardCharacter_Type = DisplayString
_InternetProfile_Visa2Options_SecondDataForwardCharacter_Object = MibScalar
internetProfile_Visa2Options_SecondDataForwardCharacter = _InternetProfile_Visa2Options_SecondDataForwardCharacter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 273),
    _InternetProfile_Visa2Options_SecondDataForwardCharacter_Type()
)
internetProfile_Visa2Options_SecondDataForwardCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_Visa2Options_SecondDataForwardCharacter.setStatus("mandatory")
_InternetProfile_Visa2Options_ThirdDataForwardCharacter_Type = DisplayString
_InternetProfile_Visa2Options_ThirdDataForwardCharacter_Object = MibScalar
internetProfile_Visa2Options_ThirdDataForwardCharacter = _InternetProfile_Visa2Options_ThirdDataForwardCharacter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 274),
    _InternetProfile_Visa2Options_ThirdDataForwardCharacter_Type()
)
internetProfile_Visa2Options_ThirdDataForwardCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_Visa2Options_ThirdDataForwardCharacter.setStatus("mandatory")
_InternetProfile_Visa2Options_FourthDataForwardCharacter_Type = DisplayString
_InternetProfile_Visa2Options_FourthDataForwardCharacter_Object = MibScalar
internetProfile_Visa2Options_FourthDataForwardCharacter = _InternetProfile_Visa2Options_FourthDataForwardCharacter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 275),
    _InternetProfile_Visa2Options_FourthDataForwardCharacter_Type()
)
internetProfile_Visa2Options_FourthDataForwardCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_Visa2Options_FourthDataForwardCharacter.setStatus("mandatory")
_InternetProfile_Visa2Options_o1CharSequence_Type = DisplayString
_InternetProfile_Visa2Options_o1CharSequence_Object = MibScalar
internetProfile_Visa2Options_o1CharSequence = _InternetProfile_Visa2Options_o1CharSequence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 276),
    _InternetProfile_Visa2Options_o1CharSequence_Type()
)
internetProfile_Visa2Options_o1CharSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_Visa2Options_o1CharSequence.setStatus("mandatory")
_InternetProfile_Visa2Options_o2CharSequence_Type = DisplayString
_InternetProfile_Visa2Options_o2CharSequence_Object = MibScalar
internetProfile_Visa2Options_o2CharSequence = _InternetProfile_Visa2Options_o2CharSequence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 277),
    _InternetProfile_Visa2Options_o2CharSequence_Type()
)
internetProfile_Visa2Options_o2CharSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_Visa2Options_o2CharSequence.setStatus("mandatory")


class _InternetProfile_SdtnPacketsServer_Type(Integer32):
    """Custom type internetProfile_SdtnPacketsServer based on Integer32"""
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


_InternetProfile_SdtnPacketsServer_Type.__name__ = "Integer32"
_InternetProfile_SdtnPacketsServer_Object = MibScalar
internetProfile_SdtnPacketsServer = _InternetProfile_SdtnPacketsServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 278),
    _InternetProfile_SdtnPacketsServer_Type()
)
internetProfile_SdtnPacketsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SdtnPacketsServer.setStatus("mandatory")
_InternetProfile_oATString_Type = DisplayString
_InternetProfile_oATString_Object = MibScalar
internetProfile_oATString = _InternetProfile_oATString_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 279),
    _InternetProfile_oATString_Type()
)
internetProfile_oATString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_oATString.setStatus("mandatory")


class _InternetProfile_PortRedirectOptions_Protocol_Type(Integer32):
    """Custom type internetProfile_PortRedirectOptions_Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7,
              18)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tcp", 7),
          ("udp", 18))
    )


_InternetProfile_PortRedirectOptions_Protocol_Type.__name__ = "Integer32"
_InternetProfile_PortRedirectOptions_Protocol_Object = MibScalar
internetProfile_PortRedirectOptions_Protocol = _InternetProfile_PortRedirectOptions_Protocol_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 280),
    _InternetProfile_PortRedirectOptions_Protocol_Type()
)
internetProfile_PortRedirectOptions_Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PortRedirectOptions_Protocol.setStatus("mandatory")
_InternetProfile_PortRedirectOptions_PortNumber_Type = Integer32
_InternetProfile_PortRedirectOptions_PortNumber_Object = MibScalar
internetProfile_PortRedirectOptions_PortNumber = _InternetProfile_PortRedirectOptions_PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 281),
    _InternetProfile_PortRedirectOptions_PortNumber_Type()
)
internetProfile_PortRedirectOptions_PortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PortRedirectOptions_PortNumber.setStatus("mandatory")
_InternetProfile_PortRedirectOptions_RedirectAddress_Type = IpAddress
_InternetProfile_PortRedirectOptions_RedirectAddress_Object = MibScalar
internetProfile_PortRedirectOptions_RedirectAddress = _InternetProfile_PortRedirectOptions_RedirectAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 282),
    _InternetProfile_PortRedirectOptions_RedirectAddress_Type()
)
internetProfile_PortRedirectOptions_RedirectAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PortRedirectOptions_RedirectAddress.setStatus("mandatory")


class _InternetProfile_SharedProf_Type(Integer32):
    """Custom type internetProfile_SharedProf based on Integer32"""
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


_InternetProfile_SharedProf_Type.__name__ = "Integer32"
_InternetProfile_SharedProf_Object = MibScalar
internetProfile_SharedProf = _InternetProfile_SharedProf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 283),
    _InternetProfile_SharedProf_Type()
)
internetProfile_SharedProf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SharedProf.setStatus("mandatory")


class _InternetProfile_MpOptions_CallbackrequestEnable_Type(Integer32):
    """Custom type internetProfile_MpOptions_CallbackrequestEnable based on Integer32"""
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


_InternetProfile_MpOptions_CallbackrequestEnable_Type.__name__ = "Integer32"
_InternetProfile_MpOptions_CallbackrequestEnable_Object = MibScalar
internetProfile_MpOptions_CallbackrequestEnable = _InternetProfile_MpOptions_CallbackrequestEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 284),
    _InternetProfile_MpOptions_CallbackrequestEnable_Type()
)
internetProfile_MpOptions_CallbackrequestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_MpOptions_CallbackrequestEnable.setStatus("mandatory")


class _InternetProfile_BridgingOptions_Egress_Type(Integer32):
    """Custom type internetProfile_BridgingOptions_Egress based on Integer32"""
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


_InternetProfile_BridgingOptions_Egress_Type.__name__ = "Integer32"
_InternetProfile_BridgingOptions_Egress_Object = MibScalar
internetProfile_BridgingOptions_Egress = _InternetProfile_BridgingOptions_Egress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 285),
    _InternetProfile_BridgingOptions_Egress_Type()
)
internetProfile_BridgingOptions_Egress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_BridgingOptions_Egress.setStatus("mandatory")
_InternetProfile_SessionOptions_TrafficShaper_Type = Integer32
_InternetProfile_SessionOptions_TrafficShaper_Object = MibScalar
internetProfile_SessionOptions_TrafficShaper = _InternetProfile_SessionOptions_TrafficShaper_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 286),
    _InternetProfile_SessionOptions_TrafficShaper_Type()
)
internetProfile_SessionOptions_TrafficShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_TrafficShaper.setStatus("mandatory")
_InternetProfile_FrOptions_MfrBundleName_Type = DisplayString
_InternetProfile_FrOptions_MfrBundleName_Object = MibScalar
internetProfile_FrOptions_MfrBundleName = _InternetProfile_FrOptions_MfrBundleName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 287),
    _InternetProfile_FrOptions_MfrBundleName_Type()
)
internetProfile_FrOptions_MfrBundleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_FrOptions_MfrBundleName.setStatus("mandatory")


class _InternetProfile_PppoeOptions_Pppoe_Type(Integer32):
    """Custom type internetProfile_PppoeOptions_Pppoe based on Integer32"""
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


_InternetProfile_PppoeOptions_Pppoe_Type.__name__ = "Integer32"
_InternetProfile_PppoeOptions_Pppoe_Object = MibScalar
internetProfile_PppoeOptions_Pppoe = _InternetProfile_PppoeOptions_Pppoe_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 288),
    _InternetProfile_PppoeOptions_Pppoe_Type()
)
internetProfile_PppoeOptions_Pppoe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppoeOptions_Pppoe.setStatus("mandatory")


class _InternetProfile_PppoeOptions_BridgeNonPppoe_Type(Integer32):
    """Custom type internetProfile_PppoeOptions_BridgeNonPppoe based on Integer32"""
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


_InternetProfile_PppoeOptions_BridgeNonPppoe_Type.__name__ = "Integer32"
_InternetProfile_PppoeOptions_BridgeNonPppoe_Object = MibScalar
internetProfile_PppoeOptions_BridgeNonPppoe = _InternetProfile_PppoeOptions_BridgeNonPppoe_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 289),
    _InternetProfile_PppoeOptions_BridgeNonPppoe_Type()
)
internetProfile_PppoeOptions_BridgeNonPppoe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppoeOptions_BridgeNonPppoe.setStatus("mandatory")


class _InternetProfile_BirOptions_Enable_Type(Integer32):
    """Custom type internetProfile_BirOptions_Enable based on Integer32"""
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


_InternetProfile_BirOptions_Enable_Type.__name__ = "Integer32"
_InternetProfile_BirOptions_Enable_Object = MibScalar
internetProfile_BirOptions_Enable = _InternetProfile_BirOptions_Enable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 290),
    _InternetProfile_BirOptions_Enable_Type()
)
internetProfile_BirOptions_Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_BirOptions_Enable.setStatus("mandatory")


class _InternetProfile_BirOptions_ProxyArp_Type(Integer32):
    """Custom type internetProfile_BirOptions_ProxyArp based on Integer32"""
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


_InternetProfile_BirOptions_ProxyArp_Type.__name__ = "Integer32"
_InternetProfile_BirOptions_ProxyArp_Object = MibScalar
internetProfile_BirOptions_ProxyArp = _InternetProfile_BirOptions_ProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 291),
    _InternetProfile_BirOptions_ProxyArp_Type()
)
internetProfile_BirOptions_ProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_BirOptions_ProxyArp.setStatus("mandatory")
_InternetProfile_SubAddress_Type = DisplayString
_InternetProfile_SubAddress_Object = MibScalar
internetProfile_SubAddress = _InternetProfile_SubAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 292),
    _InternetProfile_SubAddress_Type()
)
internetProfile_SubAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SubAddress.setStatus("mandatory")
_InternetProfile_IpOptions_ClientWinsPrimaryAddr_Type = IpAddress
_InternetProfile_IpOptions_ClientWinsPrimaryAddr_Object = MibScalar
internetProfile_IpOptions_ClientWinsPrimaryAddr = _InternetProfile_IpOptions_ClientWinsPrimaryAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 293),
    _InternetProfile_IpOptions_ClientWinsPrimaryAddr_Type()
)
internetProfile_IpOptions_ClientWinsPrimaryAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_ClientWinsPrimaryAddr.setStatus("mandatory")
_InternetProfile_IpOptions_ClientWinsSecondaryAddr_Type = IpAddress
_InternetProfile_IpOptions_ClientWinsSecondaryAddr_Object = MibScalar
internetProfile_IpOptions_ClientWinsSecondaryAddr = _InternetProfile_IpOptions_ClientWinsSecondaryAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 294),
    _InternetProfile_IpOptions_ClientWinsSecondaryAddr_Type()
)
internetProfile_IpOptions_ClientWinsSecondaryAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_ClientWinsSecondaryAddr.setStatus("mandatory")


class _InternetProfile_IpOptions_ClientWinsAddrAssign_Type(Integer32):
    """Custom type internetProfile_IpOptions_ClientWinsAddrAssign based on Integer32"""
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


_InternetProfile_IpOptions_ClientWinsAddrAssign_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_ClientWinsAddrAssign_Object = MibScalar
internetProfile_IpOptions_ClientWinsAddrAssign = _InternetProfile_IpOptions_ClientWinsAddrAssign_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 295),
    _InternetProfile_IpOptions_ClientWinsAddrAssign_Type()
)
internetProfile_IpOptions_ClientWinsAddrAssign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_ClientWinsAddrAssign.setStatus("mandatory")
_InternetProfile_IpOptions_PrivateRouteTable_Type = DisplayString
_InternetProfile_IpOptions_PrivateRouteTable_Object = MibScalar
internetProfile_IpOptions_PrivateRouteTable = _InternetProfile_IpOptions_PrivateRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 296),
    _InternetProfile_IpOptions_PrivateRouteTable_Type()
)
internetProfile_IpOptions_PrivateRouteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_PrivateRouteTable.setStatus("mandatory")


class _InternetProfile_IpOptions_PrivateRouteProfileRequired_Type(Integer32):
    """Custom type internetProfile_IpOptions_PrivateRouteProfileRequired based on Integer32"""
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


_InternetProfile_IpOptions_PrivateRouteProfileRequired_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_PrivateRouteProfileRequired_Object = MibScalar
internetProfile_IpOptions_PrivateRouteProfileRequired = _InternetProfile_IpOptions_PrivateRouteProfileRequired_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 297),
    _InternetProfile_IpOptions_PrivateRouteProfileRequired_Type()
)
internetProfile_IpOptions_PrivateRouteProfileRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_PrivateRouteProfileRequired.setStatus("mandatory")


class _InternetProfile_SessionOptions_FilterRequired_Type(Integer32):
    """Custom type internetProfile_SessionOptions_FilterRequired based on Integer32"""
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


_InternetProfile_SessionOptions_FilterRequired_Type.__name__ = "Integer32"
_InternetProfile_SessionOptions_FilterRequired_Object = MibScalar
internetProfile_SessionOptions_FilterRequired = _InternetProfile_SessionOptions_FilterRequired_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 298),
    _InternetProfile_SessionOptions_FilterRequired_Type()
)
internetProfile_SessionOptions_FilterRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_FilterRequired.setStatus("mandatory")
_InternetProfile_SessionOptions_MaxtapLogServer_Type = DisplayString
_InternetProfile_SessionOptions_MaxtapLogServer_Object = MibScalar
internetProfile_SessionOptions_MaxtapLogServer = _InternetProfile_SessionOptions_MaxtapLogServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 299),
    _InternetProfile_SessionOptions_MaxtapLogServer_Type()
)
internetProfile_SessionOptions_MaxtapLogServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_MaxtapLogServer.setStatus("mandatory")
_InternetProfile_SessionOptions_MaxtapDataServer_Type = DisplayString
_InternetProfile_SessionOptions_MaxtapDataServer_Object = MibScalar
internetProfile_SessionOptions_MaxtapDataServer = _InternetProfile_SessionOptions_MaxtapDataServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 300),
    _InternetProfile_SessionOptions_MaxtapDataServer_Type()
)
internetProfile_SessionOptions_MaxtapDataServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_MaxtapDataServer.setStatus("mandatory")
_InternetProfile_PppOptions_Mtu_Type = Integer32
_InternetProfile_PppOptions_Mtu_Object = MibScalar
internetProfile_PppOptions_Mtu = _InternetProfile_PppOptions_Mtu_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 301),
    _InternetProfile_PppOptions_Mtu_Type()
)
internetProfile_PppOptions_Mtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_Mtu.setStatus("mandatory")


class _InternetProfile_FrOptions_CircuitType_Type(Integer32):
    """Custom type internetProfile_FrOptions_CircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_InternetProfile_FrOptions_CircuitType_Type.__name__ = "Integer32"
_InternetProfile_FrOptions_CircuitType_Object = MibScalar
internetProfile_FrOptions_CircuitType = _InternetProfile_FrOptions_CircuitType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 302),
    _InternetProfile_FrOptions_CircuitType_Type()
)
internetProfile_FrOptions_CircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_FrOptions_CircuitType.setStatus("mandatory")


class _InternetProfile_FrOptions_FrLinkType_Type(Integer32):
    """Custom type internetProfile_FrOptions_FrLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hostLink", 2),
          ("transparentLink", 1),
          ("trunkLink", 3))
    )


_InternetProfile_FrOptions_FrLinkType_Type.__name__ = "Integer32"
_InternetProfile_FrOptions_FrLinkType_Object = MibScalar
internetProfile_FrOptions_FrLinkType = _InternetProfile_FrOptions_FrLinkType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 303),
    _InternetProfile_FrOptions_FrLinkType_Type()
)
internetProfile_FrOptions_FrLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_FrOptions_FrLinkType.setStatus("mandatory")


class _InternetProfile_AtmOptions_VpSwitching_Type(Integer32):
    """Custom type internetProfile_AtmOptions_VpSwitching based on Integer32"""
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


_InternetProfile_AtmOptions_VpSwitching_Type.__name__ = "Integer32"
_InternetProfile_AtmOptions_VpSwitching_Object = MibScalar
internetProfile_AtmOptions_VpSwitching = _InternetProfile_AtmOptions_VpSwitching_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 304),
    _InternetProfile_AtmOptions_VpSwitching_Type()
)
internetProfile_AtmOptions_VpSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_VpSwitching.setStatus("mandatory")


class _InternetProfile_AtmOptions_AtmDirectEnabled_Type(Integer32):
    """Custom type internetProfile_AtmOptions_AtmDirectEnabled based on Integer32"""
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


_InternetProfile_AtmOptions_AtmDirectEnabled_Type.__name__ = "Integer32"
_InternetProfile_AtmOptions_AtmDirectEnabled_Object = MibScalar
internetProfile_AtmOptions_AtmDirectEnabled = _InternetProfile_AtmOptions_AtmDirectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 306),
    _InternetProfile_AtmOptions_AtmDirectEnabled_Type()
)
internetProfile_AtmOptions_AtmDirectEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_AtmDirectEnabled.setStatus("mandatory")
_InternetProfile_AtmOptions_AtmDirectProfile_Type = DisplayString
_InternetProfile_AtmOptions_AtmDirectProfile_Object = MibScalar
internetProfile_AtmOptions_AtmDirectProfile = _InternetProfile_AtmOptions_AtmDirectProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 307),
    _InternetProfile_AtmOptions_AtmDirectProfile_Type()
)
internetProfile_AtmOptions_AtmDirectProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_AtmDirectProfile.setStatus("mandatory")


class _InternetProfile_AtmOptions_SvcOptions_Enabled_Type(Integer32):
    """Custom type internetProfile_AtmOptions_SvcOptions_Enabled based on Integer32"""
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


_InternetProfile_AtmOptions_SvcOptions_Enabled_Type.__name__ = "Integer32"
_InternetProfile_AtmOptions_SvcOptions_Enabled_Object = MibScalar
internetProfile_AtmOptions_SvcOptions_Enabled = _InternetProfile_AtmOptions_SvcOptions_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 308),
    _InternetProfile_AtmOptions_SvcOptions_Enabled_Type()
)
internetProfile_AtmOptions_SvcOptions_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SvcOptions_Enabled.setStatus("mandatory")


class _InternetProfile_AtmOptions_AtmInverseArp_Type(Integer32):
    """Custom type internetProfile_AtmOptions_AtmInverseArp based on Integer32"""
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


_InternetProfile_AtmOptions_AtmInverseArp_Type.__name__ = "Integer32"
_InternetProfile_AtmOptions_AtmInverseArp_Object = MibScalar
internetProfile_AtmOptions_AtmInverseArp = _InternetProfile_AtmOptions_AtmInverseArp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 327),
    _InternetProfile_AtmOptions_AtmInverseArp_Type()
)
internetProfile_AtmOptions_AtmInverseArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_AtmInverseArp.setStatus("mandatory")


class _InternetProfile_AtmConnectOptions_VpSwitching_Type(Integer32):
    """Custom type internetProfile_AtmConnectOptions_VpSwitching based on Integer32"""
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


_InternetProfile_AtmConnectOptions_VpSwitching_Type.__name__ = "Integer32"
_InternetProfile_AtmConnectOptions_VpSwitching_Object = MibScalar
internetProfile_AtmConnectOptions_VpSwitching = _InternetProfile_AtmConnectOptions_VpSwitching_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 328),
    _InternetProfile_AtmConnectOptions_VpSwitching_Type()
)
internetProfile_AtmConnectOptions_VpSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_VpSwitching.setStatus("mandatory")


class _InternetProfile_AtmConnectOptions_AtmDirectEnabled_Type(Integer32):
    """Custom type internetProfile_AtmConnectOptions_AtmDirectEnabled based on Integer32"""
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


_InternetProfile_AtmConnectOptions_AtmDirectEnabled_Type.__name__ = "Integer32"
_InternetProfile_AtmConnectOptions_AtmDirectEnabled_Object = MibScalar
internetProfile_AtmConnectOptions_AtmDirectEnabled = _InternetProfile_AtmConnectOptions_AtmDirectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 330),
    _InternetProfile_AtmConnectOptions_AtmDirectEnabled_Type()
)
internetProfile_AtmConnectOptions_AtmDirectEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_AtmDirectEnabled.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_AtmDirectProfile_Type = DisplayString
_InternetProfile_AtmConnectOptions_AtmDirectProfile_Object = MibScalar
internetProfile_AtmConnectOptions_AtmDirectProfile = _InternetProfile_AtmConnectOptions_AtmDirectProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 331),
    _InternetProfile_AtmConnectOptions_AtmDirectProfile_Type()
)
internetProfile_AtmConnectOptions_AtmDirectProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_AtmDirectProfile.setStatus("mandatory")


class _InternetProfile_AtmConnectOptions_SvcOptions_Enabled_Type(Integer32):
    """Custom type internetProfile_AtmConnectOptions_SvcOptions_Enabled based on Integer32"""
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


_InternetProfile_AtmConnectOptions_SvcOptions_Enabled_Type.__name__ = "Integer32"
_InternetProfile_AtmConnectOptions_SvcOptions_Enabled_Object = MibScalar
internetProfile_AtmConnectOptions_SvcOptions_Enabled = _InternetProfile_AtmConnectOptions_SvcOptions_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 332),
    _InternetProfile_AtmConnectOptions_SvcOptions_Enabled_Type()
)
internetProfile_AtmConnectOptions_SvcOptions_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SvcOptions_Enabled.setStatus("mandatory")


class _InternetProfile_AtmConnectOptions_AtmInverseArp_Type(Integer32):
    """Custom type internetProfile_AtmConnectOptions_AtmInverseArp based on Integer32"""
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


_InternetProfile_AtmConnectOptions_AtmInverseArp_Type.__name__ = "Integer32"
_InternetProfile_AtmConnectOptions_AtmInverseArp_Object = MibScalar
internetProfile_AtmConnectOptions_AtmInverseArp = _InternetProfile_AtmConnectOptions_AtmInverseArp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 351),
    _InternetProfile_AtmConnectOptions_AtmInverseArp_Type()
)
internetProfile_AtmConnectOptions_AtmInverseArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_AtmInverseArp.setStatus("mandatory")
_InternetProfile_AtmQosOptions_UsrUpStreamContract_Type = DisplayString
_InternetProfile_AtmQosOptions_UsrUpStreamContract_Object = MibScalar
internetProfile_AtmQosOptions_UsrUpStreamContract = _InternetProfile_AtmQosOptions_UsrUpStreamContract_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 352),
    _InternetProfile_AtmQosOptions_UsrUpStreamContract_Type()
)
internetProfile_AtmQosOptions_UsrUpStreamContract.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmQosOptions_UsrUpStreamContract.setStatus("mandatory")
_InternetProfile_AtmQosOptions_UsrDnStreamContract_Type = DisplayString
_InternetProfile_AtmQosOptions_UsrDnStreamContract_Object = MibScalar
internetProfile_AtmQosOptions_UsrDnStreamContract = _InternetProfile_AtmQosOptions_UsrDnStreamContract_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 353),
    _InternetProfile_AtmQosOptions_UsrDnStreamContract_Type()
)
internetProfile_AtmQosOptions_UsrDnStreamContract.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmQosOptions_UsrDnStreamContract.setStatus("mandatory")


class _InternetProfile_PppOptions_BiDirectionalAuth_Type(Integer32):
    """Custom type internetProfile_PppOptions_BiDirectionalAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 2),
          ("none", 1),
          ("required", 3))
    )


_InternetProfile_PppOptions_BiDirectionalAuth_Type.__name__ = "Integer32"
_InternetProfile_PppOptions_BiDirectionalAuth_Object = MibScalar
internetProfile_PppOptions_BiDirectionalAuth = _InternetProfile_PppOptions_BiDirectionalAuth_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 354),
    _InternetProfile_PppOptions_BiDirectionalAuth_Type()
)
internetProfile_PppOptions_BiDirectionalAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_BiDirectionalAuth.setStatus("mandatory")
_InternetProfile_PppOptions_SubstituteRecvName_Type = DisplayString
_InternetProfile_PppOptions_SubstituteRecvName_Object = MibScalar
internetProfile_PppOptions_SubstituteRecvName = _InternetProfile_PppOptions_SubstituteRecvName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 355),
    _InternetProfile_PppOptions_SubstituteRecvName_Type()
)
internetProfile_PppOptions_SubstituteRecvName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_SubstituteRecvName.setStatus("mandatory")
_InternetProfile_TunnelOptions_Vrouter_Type = DisplayString
_InternetProfile_TunnelOptions_Vrouter_Object = MibScalar
internetProfile_TunnelOptions_Vrouter = _InternetProfile_TunnelOptions_Vrouter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 356),
    _InternetProfile_TunnelOptions_Vrouter_Type()
)
internetProfile_TunnelOptions_Vrouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TunnelOptions_Vrouter.setStatus("mandatory")


class _InternetProfile_AtmOptions_VcFaultManagement_Type(Integer32):
    """Custom type internetProfile_AtmOptions_VcFaultManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("endToEndLoopback", 3),
          ("none", 1),
          ("segmentLoopback", 2))
    )


_InternetProfile_AtmOptions_VcFaultManagement_Type.__name__ = "Integer32"
_InternetProfile_AtmOptions_VcFaultManagement_Object = MibScalar
internetProfile_AtmOptions_VcFaultManagement = _InternetProfile_AtmOptions_VcFaultManagement_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 357),
    _InternetProfile_AtmOptions_VcFaultManagement_Type()
)
internetProfile_AtmOptions_VcFaultManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_VcFaultManagement.setStatus("mandatory")
_InternetProfile_AtmOptions_VcMaxLoopbackCellLoss_Type = Integer32
_InternetProfile_AtmOptions_VcMaxLoopbackCellLoss_Object = MibScalar
internetProfile_AtmOptions_VcMaxLoopbackCellLoss = _InternetProfile_AtmOptions_VcMaxLoopbackCellLoss_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 358),
    _InternetProfile_AtmOptions_VcMaxLoopbackCellLoss_Type()
)
internetProfile_AtmOptions_VcMaxLoopbackCellLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_VcMaxLoopbackCellLoss.setStatus("mandatory")


class _InternetProfile_AtmOptions_Fr08Mode_Type(Integer32):
    """Custom type internetProfile_AtmOptions_Fr08Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("translation", 1),
          ("transparent", 2))
    )


_InternetProfile_AtmOptions_Fr08Mode_Type.__name__ = "Integer32"
_InternetProfile_AtmOptions_Fr08Mode_Object = MibScalar
internetProfile_AtmOptions_Fr08Mode = _InternetProfile_AtmOptions_Fr08Mode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 367),
    _InternetProfile_AtmOptions_Fr08Mode_Type()
)
internetProfile_AtmOptions_Fr08Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_Fr08Mode.setStatus("mandatory")


class _InternetProfile_HdlcNrmOptions_AsyncDrop_Type(Integer32):
    """Custom type internetProfile_HdlcNrmOptions_AsyncDrop based on Integer32"""
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


_InternetProfile_HdlcNrmOptions_AsyncDrop_Type.__name__ = "Integer32"
_InternetProfile_HdlcNrmOptions_AsyncDrop_Object = MibScalar
internetProfile_HdlcNrmOptions_AsyncDrop = _InternetProfile_HdlcNrmOptions_AsyncDrop_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 368),
    _InternetProfile_HdlcNrmOptions_AsyncDrop_Type()
)
internetProfile_HdlcNrmOptions_AsyncDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_HdlcNrmOptions_AsyncDrop.setStatus("mandatory")


class _InternetProfile_AtmConnectOptions_VcFaultManagement_Type(Integer32):
    """Custom type internetProfile_AtmConnectOptions_VcFaultManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("endToEndLoopback", 3),
          ("none", 1),
          ("segmentLoopback", 2))
    )


_InternetProfile_AtmConnectOptions_VcFaultManagement_Type.__name__ = "Integer32"
_InternetProfile_AtmConnectOptions_VcFaultManagement_Object = MibScalar
internetProfile_AtmConnectOptions_VcFaultManagement = _InternetProfile_AtmConnectOptions_VcFaultManagement_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 369),
    _InternetProfile_AtmConnectOptions_VcFaultManagement_Type()
)
internetProfile_AtmConnectOptions_VcFaultManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_VcFaultManagement.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_VcMaxLoopbackCellLoss_Type = Integer32
_InternetProfile_AtmConnectOptions_VcMaxLoopbackCellLoss_Object = MibScalar
internetProfile_AtmConnectOptions_VcMaxLoopbackCellLoss = _InternetProfile_AtmConnectOptions_VcMaxLoopbackCellLoss_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 370),
    _InternetProfile_AtmConnectOptions_VcMaxLoopbackCellLoss_Type()
)
internetProfile_AtmConnectOptions_VcMaxLoopbackCellLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_VcMaxLoopbackCellLoss.setStatus("mandatory")


class _InternetProfile_AtmConnectOptions_Fr08Mode_Type(Integer32):
    """Custom type internetProfile_AtmConnectOptions_Fr08Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("translation", 1),
          ("transparent", 2))
    )


_InternetProfile_AtmConnectOptions_Fr08Mode_Type.__name__ = "Integer32"
_InternetProfile_AtmConnectOptions_Fr08Mode_Object = MibScalar
internetProfile_AtmConnectOptions_Fr08Mode = _InternetProfile_AtmConnectOptions_Fr08Mode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 379),
    _InternetProfile_AtmConnectOptions_Fr08Mode_Type()
)
internetProfile_AtmConnectOptions_Fr08Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_Fr08Mode.setStatus("mandatory")
_InternetProfile_MppOptions_X25chanTargetUtilization_Type = Integer32
_InternetProfile_MppOptions_X25chanTargetUtilization_Object = MibScalar
internetProfile_MppOptions_X25chanTargetUtilization = _InternetProfile_MppOptions_X25chanTargetUtilization_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 380),
    _InternetProfile_MppOptions_X25chanTargetUtilization_Type()
)
internetProfile_MppOptions_X25chanTargetUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_MppOptions_X25chanTargetUtilization.setStatus("mandatory")


class _InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_NumberingPlan_Type(Integer32):
    """Custom type internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_NumberingPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("aesa", 3),
          ("isdn", 2),
          ("undefined", 1),
          ("unknown", 5),
          ("x121", 9))
    )


_InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_NumberingPlan_Type.__name__ = "Integer32"
_InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_NumberingPlan_Object = MibScalar
internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_NumberingPlan = _InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_NumberingPlan_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 381),
    _InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_NumberingPlan_Type()
)
internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_NumberingPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_NumberingPlan.setStatus("mandatory")
_InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_E164NativeAddress_Type = DisplayString
_InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_E164NativeAddress_Object = MibScalar
internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_E164NativeAddress = _InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_E164NativeAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 382),
    _InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_E164NativeAddress_Type()
)
internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_E164NativeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_E164NativeAddress.setStatus("mandatory")


class _InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format_Type(Integer32):
    """Custom type internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("customAesa", 5),
          ("dccAesa", 2),
          ("e164Aesa", 4),
          ("icdAesa", 6),
          ("undefined", 1))
    )


_InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format_Type.__name__ = "Integer32"
_InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format_Object = MibScalar
internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format = _InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 383),
    _InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format_Type()
)
internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format.setStatus("mandatory")
_InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Afi_Type = DisplayString
_InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Afi_Object = MibScalar
internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Afi = _InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Afi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 384),
    _InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Afi_Type()
)
internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Afi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Afi.setStatus("mandatory")
_InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Idi_Type = DisplayString
_InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Idi_Object = MibScalar
internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Idi = _InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Idi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 385),
    _InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Idi_Type()
)
internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Idi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Idi.setStatus("mandatory")
_InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_HoDsp_Type = DisplayString
_InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_HoDsp_Object = MibScalar
internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_HoDsp = _InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_HoDsp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 386),
    _InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_HoDsp_Type()
)
internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_HoDsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_HoDsp.setStatus("mandatory")
_InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Esi_Type = DisplayString
_InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Esi_Object = MibScalar
internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Esi = _InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Esi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 387),
    _InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Esi_Type()
)
internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Esi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Esi.setStatus("mandatory")
_InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Sel_Type = DisplayString
_InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Sel_Object = MibScalar
internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Sel = _InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Sel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 388),
    _InternetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Sel_Type()
)
internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Sel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Sel.setStatus("mandatory")


class _InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan_Type(Integer32):
    """Custom type internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("aesa", 3),
          ("isdn", 2),
          ("undefined", 1),
          ("unknown", 5),
          ("x121", 9))
    )


_InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan_Type.__name__ = "Integer32"
_InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan_Object = MibScalar
internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan = _InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 389),
    _InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan_Type()
)
internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan.setStatus("mandatory")
_InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_E164NativeAddress_Type = DisplayString
_InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_E164NativeAddress_Object = MibScalar
internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_E164NativeAddress = _InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_E164NativeAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 390),
    _InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_E164NativeAddress_Type()
)
internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_E164NativeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_E164NativeAddress.setStatus("mandatory")


class _InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format_Type(Integer32):
    """Custom type internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("customAesa", 5),
          ("dccAesa", 2),
          ("e164Aesa", 4),
          ("icdAesa", 6),
          ("undefined", 1))
    )


_InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format_Type.__name__ = "Integer32"
_InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format_Object = MibScalar
internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format = _InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 391),
    _InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format_Type()
)
internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format.setStatus("mandatory")
_InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Afi_Type = DisplayString
_InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Afi_Object = MibScalar
internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Afi = _InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Afi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 392),
    _InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Afi_Type()
)
internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Afi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Afi.setStatus("mandatory")
_InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Idi_Type = DisplayString
_InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Idi_Object = MibScalar
internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Idi = _InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Idi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 393),
    _InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Idi_Type()
)
internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Idi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Idi.setStatus("mandatory")
_InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_HoDsp_Type = DisplayString
_InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_HoDsp_Object = MibScalar
internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_HoDsp = _InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_HoDsp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 394),
    _InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_HoDsp_Type()
)
internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_HoDsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_HoDsp.setStatus("mandatory")
_InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Esi_Type = DisplayString
_InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Esi_Object = MibScalar
internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Esi = _InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Esi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 395),
    _InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Esi_Type()
)
internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Esi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Esi.setStatus("mandatory")
_InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Sel_Type = DisplayString
_InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Sel_Object = MibScalar
internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Sel = _InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Sel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 396),
    _InternetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Sel_Type()
)
internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Sel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Sel.setStatus("mandatory")


class _InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_NumberingPlan_Type(Integer32):
    """Custom type internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_NumberingPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("aesa", 3),
          ("isdn", 2),
          ("undefined", 1),
          ("unknown", 5),
          ("x121", 9))
    )


_InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_NumberingPlan_Type.__name__ = "Integer32"
_InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_NumberingPlan_Object = MibScalar
internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_NumberingPlan = _InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_NumberingPlan_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 397),
    _InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_NumberingPlan_Type()
)
internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_NumberingPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_NumberingPlan.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_E164NativeAddress_Type = DisplayString
_InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_E164NativeAddress_Object = MibScalar
internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_E164NativeAddress = _InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_E164NativeAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 398),
    _InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_E164NativeAddress_Type()
)
internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_E164NativeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_E164NativeAddress.setStatus("mandatory")


class _InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format_Type(Integer32):
    """Custom type internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("customAesa", 5),
          ("dccAesa", 2),
          ("e164Aesa", 4),
          ("icdAesa", 6),
          ("undefined", 1))
    )


_InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format_Type.__name__ = "Integer32"
_InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format_Object = MibScalar
internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format = _InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 399),
    _InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format_Type()
)
internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Afi_Type = DisplayString
_InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Afi_Object = MibScalar
internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Afi = _InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Afi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 400),
    _InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Afi_Type()
)
internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Afi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Afi.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Idi_Type = DisplayString
_InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Idi_Object = MibScalar
internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Idi = _InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Idi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 401),
    _InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Idi_Type()
)
internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Idi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Idi.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_HoDsp_Type = DisplayString
_InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_HoDsp_Object = MibScalar
internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_HoDsp = _InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_HoDsp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 402),
    _InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_HoDsp_Type()
)
internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_HoDsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_HoDsp.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Esi_Type = DisplayString
_InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Esi_Object = MibScalar
internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Esi = _InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Esi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 403),
    _InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Esi_Type()
)
internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Esi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Esi.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Sel_Type = DisplayString
_InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Sel_Object = MibScalar
internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Sel = _InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Sel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 404),
    _InternetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Sel_Type()
)
internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Sel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Sel.setStatus("mandatory")


class _InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan_Type(Integer32):
    """Custom type internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("aesa", 3),
          ("isdn", 2),
          ("undefined", 1),
          ("unknown", 5),
          ("x121", 9))
    )


_InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan_Type.__name__ = "Integer32"
_InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan_Object = MibScalar
internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan = _InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 405),
    _InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan_Type()
)
internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_E164NativeAddress_Type = DisplayString
_InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_E164NativeAddress_Object = MibScalar
internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_E164NativeAddress = _InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_E164NativeAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 406),
    _InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_E164NativeAddress_Type()
)
internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_E164NativeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_E164NativeAddress.setStatus("mandatory")


class _InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format_Type(Integer32):
    """Custom type internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("customAesa", 5),
          ("dccAesa", 2),
          ("e164Aesa", 4),
          ("icdAesa", 6),
          ("undefined", 1))
    )


_InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format_Type.__name__ = "Integer32"
_InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format_Object = MibScalar
internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format = _InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 407),
    _InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format_Type()
)
internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Afi_Type = DisplayString
_InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Afi_Object = MibScalar
internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Afi = _InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Afi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 408),
    _InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Afi_Type()
)
internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Afi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Afi.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Idi_Type = DisplayString
_InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Idi_Object = MibScalar
internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Idi = _InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Idi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 409),
    _InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Idi_Type()
)
internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Idi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Idi.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_HoDsp_Type = DisplayString
_InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_HoDsp_Object = MibScalar
internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_HoDsp = _InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_HoDsp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 410),
    _InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_HoDsp_Type()
)
internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_HoDsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_HoDsp.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Esi_Type = DisplayString
_InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Esi_Object = MibScalar
internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Esi = _InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Esi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 411),
    _InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Esi_Type()
)
internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Esi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Esi.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Sel_Type = DisplayString
_InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Sel_Object = MibScalar
internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Sel = _InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Sel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 412),
    _InternetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Sel_Type()
)
internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Sel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Sel.setStatus("mandatory")
_InternetProfile_TunnelOptions_ClientAuthId_Type = DisplayString
_InternetProfile_TunnelOptions_ClientAuthId_Object = MibScalar
internetProfile_TunnelOptions_ClientAuthId = _InternetProfile_TunnelOptions_ClientAuthId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 413),
    _InternetProfile_TunnelOptions_ClientAuthId_Type()
)
internetProfile_TunnelOptions_ClientAuthId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TunnelOptions_ClientAuthId.setStatus("mandatory")
_InternetProfile_SessionOptions_CirTimer_Type = Integer32
_InternetProfile_SessionOptions_CirTimer_Object = MibScalar
internetProfile_SessionOptions_CirTimer = _InternetProfile_SessionOptions_CirTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 414),
    _InternetProfile_SessionOptions_CirTimer_Type()
)
internetProfile_SessionOptions_CirTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_CirTimer.setStatus("mandatory")


class _InternetProfile_SessionOptions_Priority_Type(Integer32):
    """Custom type internetProfile_SessionOptions_Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("normal", 1))
    )


_InternetProfile_SessionOptions_Priority_Type.__name__ = "Integer32"
_InternetProfile_SessionOptions_Priority_Object = MibScalar
internetProfile_SessionOptions_Priority = _InternetProfile_SessionOptions_Priority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 415),
    _InternetProfile_SessionOptions_Priority_Type()
)
internetProfile_SessionOptions_Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_SessionOptions_Priority.setStatus("mandatory")
_InternetProfile_HdlcNrmOptions_StationPollAddress_Type = Integer32
_InternetProfile_HdlcNrmOptions_StationPollAddress_Object = MibScalar
internetProfile_HdlcNrmOptions_StationPollAddress = _InternetProfile_HdlcNrmOptions_StationPollAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 416),
    _InternetProfile_HdlcNrmOptions_StationPollAddress_Type()
)
internetProfile_HdlcNrmOptions_StationPollAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_HdlcNrmOptions_StationPollAddress.setStatus("mandatory")
_InternetProfile_TunnelOptions_ServerAuthId_Type = DisplayString
_InternetProfile_TunnelOptions_ServerAuthId_Object = MibScalar
internetProfile_TunnelOptions_ServerAuthId = _InternetProfile_TunnelOptions_ServerAuthId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 417),
    _InternetProfile_TunnelOptions_ServerAuthId_Type()
)
internetProfile_TunnelOptions_ServerAuthId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TunnelOptions_ServerAuthId.setStatus("mandatory")
_InternetProfile_TunnelOptions_AssignmentId_Type = DisplayString
_InternetProfile_TunnelOptions_AssignmentId_Object = MibScalar
internetProfile_TunnelOptions_AssignmentId = _InternetProfile_TunnelOptions_AssignmentId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 418),
    _InternetProfile_TunnelOptions_AssignmentId_Type()
)
internetProfile_TunnelOptions_AssignmentId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TunnelOptions_AssignmentId.setStatus("mandatory")
_InternetProfile_IpOptions_NatProfileName_Type = DisplayString
_InternetProfile_IpOptions_NatProfileName_Object = MibScalar
internetProfile_IpOptions_NatProfileName = _InternetProfile_IpOptions_NatProfileName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 419),
    _InternetProfile_IpOptions_NatProfileName_Type()
)
internetProfile_IpOptions_NatProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_NatProfileName.setStatus("mandatory")


class _InternetProfile_AutoProfiles_Type(Integer32):
    """Custom type internetProfile_AutoProfiles based on Integer32"""
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


_InternetProfile_AutoProfiles_Type.__name__ = "Integer32"
_InternetProfile_AutoProfiles_Object = MibScalar
internetProfile_AutoProfiles = _InternetProfile_AutoProfiles_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 420),
    _InternetProfile_AutoProfiles_Type()
)
internetProfile_AutoProfiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AutoProfiles.setStatus("mandatory")
_InternetProfile_IpOptions_AddressRealm_Type = Integer32
_InternetProfile_IpOptions_AddressRealm_Object = MibScalar
internetProfile_IpOptions_AddressRealm = _InternetProfile_IpOptions_AddressRealm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 421),
    _InternetProfile_IpOptions_AddressRealm_Type()
)
internetProfile_IpOptions_AddressRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_AddressRealm.setStatus("mandatory")


class _InternetProfile_PppOptions_PppCircuit_Type(Integer32):
    """Custom type internetProfile_PppOptions_PppCircuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("transparent", 2))
    )


_InternetProfile_PppOptions_PppCircuit_Type.__name__ = "Integer32"
_InternetProfile_PppOptions_PppCircuit_Object = MibScalar
internetProfile_PppOptions_PppCircuit = _InternetProfile_PppOptions_PppCircuit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 422),
    _InternetProfile_PppOptions_PppCircuit_Type()
)
internetProfile_PppOptions_PppCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_PppCircuit.setStatus("mandatory")
_InternetProfile_PppOptions_PppCircuitName_Type = DisplayString
_InternetProfile_PppOptions_PppCircuitName_Object = MibScalar
internetProfile_PppOptions_PppCircuitName = _InternetProfile_PppOptions_PppCircuitName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 423),
    _InternetProfile_PppOptions_PppCircuitName_Type()
)
internetProfile_PppOptions_PppCircuitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PppOptions_PppCircuitName.setStatus("mandatory")


class _InternetProfile_X32Options_X32ApplMode_Type(Integer32):
    """Custom type internetProfile_X32Options_X32ApplMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("isdnCircuitMode", 2),
          ("isdnPacketMode", 3),
          ("last", 4),
          ("netToNet", 1))
    )


_InternetProfile_X32Options_X32ApplMode_Type.__name__ = "Integer32"
_InternetProfile_X32Options_X32ApplMode_Object = MibScalar
internetProfile_X32Options_X32ApplMode = _InternetProfile_X32Options_X32ApplMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 424),
    _InternetProfile_X32Options_X32ApplMode_Type()
)
internetProfile_X32Options_X32ApplMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X32Options_X32ApplMode.setStatus("mandatory")
_InternetProfile_CrossConnectIndex_Type = Integer32
_InternetProfile_CrossConnectIndex_Object = MibScalar
internetProfile_CrossConnectIndex = _InternetProfile_CrossConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 425),
    _InternetProfile_CrossConnectIndex_Type()
)
internetProfile_CrossConnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_CrossConnectIndex.setStatus("mandatory")


class _InternetProfile_AtmOptions_CastType_Type(Integer32):
    """Custom type internetProfile_AtmOptions_CastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("p2mpleaf", 4),
          ("p2mproot", 3),
          ("p2p", 2))
    )


_InternetProfile_AtmOptions_CastType_Type.__name__ = "Integer32"
_InternetProfile_AtmOptions_CastType_Object = MibScalar
internetProfile_AtmOptions_CastType = _InternetProfile_AtmOptions_CastType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 426),
    _InternetProfile_AtmOptions_CastType_Type()
)
internetProfile_AtmOptions_CastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_CastType.setStatus("mandatory")


class _InternetProfile_AtmOptions_ConnKind_Type(Integer32):
    """Custom type internetProfile_AtmOptions_ConnKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 2),
          ("spvcInitiator", 5),
          ("spvcTarget", 6),
          ("svcIncoming", 3),
          ("svcOutgoing", 4))
    )


_InternetProfile_AtmOptions_ConnKind_Type.__name__ = "Integer32"
_InternetProfile_AtmOptions_ConnKind_Object = MibScalar
internetProfile_AtmOptions_ConnKind = _InternetProfile_AtmOptions_ConnKind_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 427),
    _InternetProfile_AtmOptions_ConnKind_Type()
)
internetProfile_AtmOptions_ConnKind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_ConnKind.setStatus("mandatory")
_InternetProfile_AtmOptions_TargetAtmAddress_Type = DisplayString
_InternetProfile_AtmOptions_TargetAtmAddress_Object = MibScalar
internetProfile_AtmOptions_TargetAtmAddress = _InternetProfile_AtmOptions_TargetAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 428),
    _InternetProfile_AtmOptions_TargetAtmAddress_Type()
)
internetProfile_AtmOptions_TargetAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_TargetAtmAddress.setStatus("mandatory")


class _InternetProfile_AtmOptions_TargetSelect_Type(Integer32):
    """Custom type internetProfile_AtmOptions_TargetSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("required", 2))
    )


_InternetProfile_AtmOptions_TargetSelect_Type.__name__ = "Integer32"
_InternetProfile_AtmOptions_TargetSelect_Object = MibScalar
internetProfile_AtmOptions_TargetSelect = _InternetProfile_AtmOptions_TargetSelect_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 429),
    _InternetProfile_AtmOptions_TargetSelect_Type()
)
internetProfile_AtmOptions_TargetSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_TargetSelect.setStatus("mandatory")
_InternetProfile_AtmOptions_TargetVpi_Type = Integer32
_InternetProfile_AtmOptions_TargetVpi_Object = MibScalar
internetProfile_AtmOptions_TargetVpi = _InternetProfile_AtmOptions_TargetVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 430),
    _InternetProfile_AtmOptions_TargetVpi_Type()
)
internetProfile_AtmOptions_TargetVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_TargetVpi.setStatus("mandatory")
_InternetProfile_AtmOptions_TargetVci_Type = Integer32
_InternetProfile_AtmOptions_TargetVci_Object = MibScalar
internetProfile_AtmOptions_TargetVci = _InternetProfile_AtmOptions_TargetVci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 431),
    _InternetProfile_AtmOptions_TargetVci_Type()
)
internetProfile_AtmOptions_TargetVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_TargetVci.setStatus("mandatory")
_InternetProfile_AtmOptions_AtmCircuitProfile_Type = DisplayString
_InternetProfile_AtmOptions_AtmCircuitProfile_Object = MibScalar
internetProfile_AtmOptions_AtmCircuitProfile = _InternetProfile_AtmOptions_AtmCircuitProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 432),
    _InternetProfile_AtmOptions_AtmCircuitProfile_Type()
)
internetProfile_AtmOptions_AtmCircuitProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_AtmCircuitProfile.setStatus("mandatory")


class _InternetProfile_AtmConnectOptions_CastType_Type(Integer32):
    """Custom type internetProfile_AtmConnectOptions_CastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("p2mpleaf", 4),
          ("p2mproot", 3),
          ("p2p", 2))
    )


_InternetProfile_AtmConnectOptions_CastType_Type.__name__ = "Integer32"
_InternetProfile_AtmConnectOptions_CastType_Object = MibScalar
internetProfile_AtmConnectOptions_CastType = _InternetProfile_AtmConnectOptions_CastType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 433),
    _InternetProfile_AtmConnectOptions_CastType_Type()
)
internetProfile_AtmConnectOptions_CastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_CastType.setStatus("mandatory")


class _InternetProfile_AtmConnectOptions_ConnKind_Type(Integer32):
    """Custom type internetProfile_AtmConnectOptions_ConnKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 2),
          ("spvcInitiator", 5),
          ("spvcTarget", 6),
          ("svcIncoming", 3),
          ("svcOutgoing", 4))
    )


_InternetProfile_AtmConnectOptions_ConnKind_Type.__name__ = "Integer32"
_InternetProfile_AtmConnectOptions_ConnKind_Object = MibScalar
internetProfile_AtmConnectOptions_ConnKind = _InternetProfile_AtmConnectOptions_ConnKind_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 434),
    _InternetProfile_AtmConnectOptions_ConnKind_Type()
)
internetProfile_AtmConnectOptions_ConnKind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_ConnKind.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_TargetAtmAddress_Type = DisplayString
_InternetProfile_AtmConnectOptions_TargetAtmAddress_Object = MibScalar
internetProfile_AtmConnectOptions_TargetAtmAddress = _InternetProfile_AtmConnectOptions_TargetAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 435),
    _InternetProfile_AtmConnectOptions_TargetAtmAddress_Type()
)
internetProfile_AtmConnectOptions_TargetAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_TargetAtmAddress.setStatus("mandatory")


class _InternetProfile_AtmConnectOptions_TargetSelect_Type(Integer32):
    """Custom type internetProfile_AtmConnectOptions_TargetSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("required", 2))
    )


_InternetProfile_AtmConnectOptions_TargetSelect_Type.__name__ = "Integer32"
_InternetProfile_AtmConnectOptions_TargetSelect_Object = MibScalar
internetProfile_AtmConnectOptions_TargetSelect = _InternetProfile_AtmConnectOptions_TargetSelect_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 436),
    _InternetProfile_AtmConnectOptions_TargetSelect_Type()
)
internetProfile_AtmConnectOptions_TargetSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_TargetSelect.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_TargetVpi_Type = Integer32
_InternetProfile_AtmConnectOptions_TargetVpi_Object = MibScalar
internetProfile_AtmConnectOptions_TargetVpi = _InternetProfile_AtmConnectOptions_TargetVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 437),
    _InternetProfile_AtmConnectOptions_TargetVpi_Type()
)
internetProfile_AtmConnectOptions_TargetVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_TargetVpi.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_TargetVci_Type = Integer32
_InternetProfile_AtmConnectOptions_TargetVci_Object = MibScalar
internetProfile_AtmConnectOptions_TargetVci = _InternetProfile_AtmConnectOptions_TargetVci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 438),
    _InternetProfile_AtmConnectOptions_TargetVci_Type()
)
internetProfile_AtmConnectOptions_TargetVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_TargetVci.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_AtmCircuitProfile_Type = DisplayString
_InternetProfile_AtmConnectOptions_AtmCircuitProfile_Object = MibScalar
internetProfile_AtmConnectOptions_AtmCircuitProfile = _InternetProfile_AtmConnectOptions_AtmCircuitProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 439),
    _InternetProfile_AtmConnectOptions_AtmCircuitProfile_Type()
)
internetProfile_AtmConnectOptions_AtmCircuitProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_AtmCircuitProfile.setStatus("mandatory")


class _InternetProfile_AtmAalOptions_AalEnabled_Type(Integer32):
    """Custom type internetProfile_AtmAalOptions_AalEnabled based on Integer32"""
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


_InternetProfile_AtmAalOptions_AalEnabled_Type.__name__ = "Integer32"
_InternetProfile_AtmAalOptions_AalEnabled_Object = MibScalar
internetProfile_AtmAalOptions_AalEnabled = _InternetProfile_AtmAalOptions_AalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 440),
    _InternetProfile_AtmAalOptions_AalEnabled_Type()
)
internetProfile_AtmAalOptions_AalEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_AtmAalOptions_AalEnabled.setStatus("mandatory")


class _InternetProfile_AtmAalOptions_AalType_Type(Integer32):
    """Custom type internetProfile_AtmAalOptions_AalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aal0", 1),
          ("aal5", 2),
          ("unspecified", 3))
    )


_InternetProfile_AtmAalOptions_AalType_Type.__name__ = "Integer32"
_InternetProfile_AtmAalOptions_AalType_Object = MibScalar
internetProfile_AtmAalOptions_AalType = _InternetProfile_AtmAalOptions_AalType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 441),
    _InternetProfile_AtmAalOptions_AalType_Type()
)
internetProfile_AtmAalOptions_AalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmAalOptions_AalType.setStatus("mandatory")
_InternetProfile_AtmAalOptions_TransmitSduSize_Type = Integer32
_InternetProfile_AtmAalOptions_TransmitSduSize_Object = MibScalar
internetProfile_AtmAalOptions_TransmitSduSize = _InternetProfile_AtmAalOptions_TransmitSduSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 442),
    _InternetProfile_AtmAalOptions_TransmitSduSize_Type()
)
internetProfile_AtmAalOptions_TransmitSduSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmAalOptions_TransmitSduSize.setStatus("mandatory")
_InternetProfile_AtmAalOptions_ReceiveSduSize_Type = Integer32
_InternetProfile_AtmAalOptions_ReceiveSduSize_Object = MibScalar
internetProfile_AtmAalOptions_ReceiveSduSize = _InternetProfile_AtmAalOptions_ReceiveSduSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 443),
    _InternetProfile_AtmAalOptions_ReceiveSduSize_Type()
)
internetProfile_AtmAalOptions_ReceiveSduSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmAalOptions_ReceiveSduSize.setStatus("mandatory")


class _InternetProfile_ConnUser_Type(Integer32):
    """Custom type internetProfile_ConnUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpcs", 2),
          ("default", 1))
    )


_InternetProfile_ConnUser_Type.__name__ = "Integer32"
_InternetProfile_ConnUser_Object = MibScalar
internetProfile_ConnUser = _InternetProfile_ConnUser_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 444),
    _InternetProfile_ConnUser_Type()
)
internetProfile_ConnUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_ConnUser.setStatus("mandatory")
_InternetProfile_AtmOptions_SpvcRetryInterval_Type = Integer32
_InternetProfile_AtmOptions_SpvcRetryInterval_Object = MibScalar
internetProfile_AtmOptions_SpvcRetryInterval = _InternetProfile_AtmOptions_SpvcRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 448),
    _InternetProfile_AtmOptions_SpvcRetryInterval_Type()
)
internetProfile_AtmOptions_SpvcRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SpvcRetryInterval.setStatus("mandatory")
_InternetProfile_AtmOptions_SpvcRetryThreshold_Type = Integer32
_InternetProfile_AtmOptions_SpvcRetryThreshold_Object = MibScalar
internetProfile_AtmOptions_SpvcRetryThreshold = _InternetProfile_AtmOptions_SpvcRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 449),
    _InternetProfile_AtmOptions_SpvcRetryThreshold_Type()
)
internetProfile_AtmOptions_SpvcRetryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SpvcRetryThreshold.setStatus("mandatory")
_InternetProfile_AtmOptions_SpvcRetryLimit_Type = Integer32
_InternetProfile_AtmOptions_SpvcRetryLimit_Object = MibScalar
internetProfile_AtmOptions_SpvcRetryLimit = _InternetProfile_AtmOptions_SpvcRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 450),
    _InternetProfile_AtmOptions_SpvcRetryLimit_Type()
)
internetProfile_AtmOptions_SpvcRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_SpvcRetryLimit.setStatus("mandatory")


class _InternetProfile_AtmOptions_OamAisF5_Type(Integer32):
    """Custom type internetProfile_AtmOptions_OamAisF5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("endToEnd", 3),
          ("segment", 2))
    )


_InternetProfile_AtmOptions_OamAisF5_Type.__name__ = "Integer32"
_InternetProfile_AtmOptions_OamAisF5_Object = MibScalar
internetProfile_AtmOptions_OamAisF5 = _InternetProfile_AtmOptions_OamAisF5_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 451),
    _InternetProfile_AtmOptions_OamAisF5_Type()
)
internetProfile_AtmOptions_OamAisF5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_OamAisF5.setStatus("mandatory")


class _InternetProfile_AtmOptions_OamSupport_Type(Integer32):
    """Custom type internetProfile_AtmOptions_OamSupport based on Integer32"""
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


_InternetProfile_AtmOptions_OamSupport_Type.__name__ = "Integer32"
_InternetProfile_AtmOptions_OamSupport_Object = MibScalar
internetProfile_AtmOptions_OamSupport = _InternetProfile_AtmOptions_OamSupport_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 452),
    _InternetProfile_AtmOptions_OamSupport_Type()
)
internetProfile_AtmOptions_OamSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_OamSupport.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_SpvcRetryInterval_Type = Integer32
_InternetProfile_AtmConnectOptions_SpvcRetryInterval_Object = MibScalar
internetProfile_AtmConnectOptions_SpvcRetryInterval = _InternetProfile_AtmConnectOptions_SpvcRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 453),
    _InternetProfile_AtmConnectOptions_SpvcRetryInterval_Type()
)
internetProfile_AtmConnectOptions_SpvcRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SpvcRetryInterval.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_SpvcRetryThreshold_Type = Integer32
_InternetProfile_AtmConnectOptions_SpvcRetryThreshold_Object = MibScalar
internetProfile_AtmConnectOptions_SpvcRetryThreshold = _InternetProfile_AtmConnectOptions_SpvcRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 454),
    _InternetProfile_AtmConnectOptions_SpvcRetryThreshold_Type()
)
internetProfile_AtmConnectOptions_SpvcRetryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SpvcRetryThreshold.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_SpvcRetryLimit_Type = Integer32
_InternetProfile_AtmConnectOptions_SpvcRetryLimit_Object = MibScalar
internetProfile_AtmConnectOptions_SpvcRetryLimit = _InternetProfile_AtmConnectOptions_SpvcRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 455),
    _InternetProfile_AtmConnectOptions_SpvcRetryLimit_Type()
)
internetProfile_AtmConnectOptions_SpvcRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_SpvcRetryLimit.setStatus("mandatory")


class _InternetProfile_AtmConnectOptions_OamAisF5_Type(Integer32):
    """Custom type internetProfile_AtmConnectOptions_OamAisF5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("endToEnd", 3),
          ("segment", 2))
    )


_InternetProfile_AtmConnectOptions_OamAisF5_Type.__name__ = "Integer32"
_InternetProfile_AtmConnectOptions_OamAisF5_Object = MibScalar
internetProfile_AtmConnectOptions_OamAisF5 = _InternetProfile_AtmConnectOptions_OamAisF5_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 456),
    _InternetProfile_AtmConnectOptions_OamAisF5_Type()
)
internetProfile_AtmConnectOptions_OamAisF5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_OamAisF5.setStatus("mandatory")


class _InternetProfile_AtmConnectOptions_OamSupport_Type(Integer32):
    """Custom type internetProfile_AtmConnectOptions_OamSupport based on Integer32"""
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


_InternetProfile_AtmConnectOptions_OamSupport_Type.__name__ = "Integer32"
_InternetProfile_AtmConnectOptions_OamSupport_Object = MibScalar
internetProfile_AtmConnectOptions_OamSupport = _InternetProfile_AtmConnectOptions_OamSupport_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 457),
    _InternetProfile_AtmConnectOptions_OamSupport_Type()
)
internetProfile_AtmConnectOptions_OamSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_OamSupport.setStatus("mandatory")


class _InternetProfile_ModemOnHoldTimeout_Type(Integer32):
    """Custom type internetProfile_ModemOnHoldTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("connProfileUseGlobal", 15),
          ("mohDisabled", 1),
          ("n-10SecMohTimeout", 2),
          ("n-12MinMohTimeout", 12),
          ("n-16MinMohTimeout", 13),
          ("n-1MinMohTimeout", 6),
          ("n-20SecMohTimeout", 3),
          ("n-2MinMohTimeout", 7),
          ("n-30SecMohTimeout", 4),
          ("n-3MinMohTimeout", 8),
          ("n-40SecMohTimeout", 5),
          ("n-4MinMohTimeout", 9),
          ("n-6MinMohTimeout", 10),
          ("n-8MinMohTimeout", 11),
          ("noLimitMohTimeout", 14))
    )


_InternetProfile_ModemOnHoldTimeout_Type.__name__ = "Integer32"
_InternetProfile_ModemOnHoldTimeout_Object = MibScalar
internetProfile_ModemOnHoldTimeout = _InternetProfile_ModemOnHoldTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 458),
    _InternetProfile_ModemOnHoldTimeout_Type()
)
internetProfile_ModemOnHoldTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_ModemOnHoldTimeout.setStatus("mandatory")


class _InternetProfile_IpOptions_TosOptions_MarkingType_Type(Integer32):
    """Custom type internetProfile_IpOptions_TosOptions_MarkingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 2),
          ("precedenceTos", 1))
    )


_InternetProfile_IpOptions_TosOptions_MarkingType_Type.__name__ = "Integer32"
_InternetProfile_IpOptions_TosOptions_MarkingType_Object = MibScalar
internetProfile_IpOptions_TosOptions_MarkingType = _InternetProfile_IpOptions_TosOptions_MarkingType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 459),
    _InternetProfile_IpOptions_TosOptions_MarkingType_Type()
)
internetProfile_IpOptions_TosOptions_MarkingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_TosOptions_MarkingType.setStatus("mandatory")
_InternetProfile_IpOptions_TosOptions_Dscp_Type = DisplayString
_InternetProfile_IpOptions_TosOptions_Dscp_Object = MibScalar
internetProfile_IpOptions_TosOptions_Dscp = _InternetProfile_IpOptions_TosOptions_Dscp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 460),
    _InternetProfile_IpOptions_TosOptions_Dscp_Type()
)
internetProfile_IpOptions_TosOptions_Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpOptions_TosOptions_Dscp.setStatus("mandatory")
_InternetProfile_X25Options_RemoteX25Address_Type = DisplayString
_InternetProfile_X25Options_RemoteX25Address_Object = MibScalar
internetProfile_X25Options_RemoteX25Address = _InternetProfile_X25Options_RemoteX25Address_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 461),
    _InternetProfile_X25Options_RemoteX25Address_Type()
)
internetProfile_X25Options_RemoteX25Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_RemoteX25Address.setStatus("mandatory")
_InternetProfile_X25Options_AnswerX25Address_Type = DisplayString
_InternetProfile_X25Options_AnswerX25Address_Object = MibScalar
internetProfile_X25Options_AnswerX25Address = _InternetProfile_X25Options_AnswerX25Address_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 462),
    _InternetProfile_X25Options_AnswerX25Address_Type()
)
internetProfile_X25Options_AnswerX25Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_AnswerX25Address.setStatus("mandatory")
_InternetProfile_X25Options_Windowsize_Type = Integer32
_InternetProfile_X25Options_Windowsize_Object = MibScalar
internetProfile_X25Options_Windowsize = _InternetProfile_X25Options_Windowsize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 463),
    _InternetProfile_X25Options_Windowsize_Type()
)
internetProfile_X25Options_Windowsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_Windowsize.setStatus("mandatory")


class _InternetProfile_X25Options_Packetsize_Type(Integer32):
    """Custom type internetProfile_X25Options_Packetsize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("n-10", 11),
          ("n-11", 12),
          ("n-12", 13),
          ("n-6", 7),
          ("n-7", 8),
          ("n-8", 9),
          ("n-9", 10))
    )


_InternetProfile_X25Options_Packetsize_Type.__name__ = "Integer32"
_InternetProfile_X25Options_Packetsize_Object = MibScalar
internetProfile_X25Options_Packetsize = _InternetProfile_X25Options_Packetsize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 464),
    _InternetProfile_X25Options_Packetsize_Type()
)
internetProfile_X25Options_Packetsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_Packetsize.setStatus("mandatory")
_InternetProfile_MaxSharedUsers_Type = Integer32
_InternetProfile_MaxSharedUsers_Object = MibScalar
internetProfile_MaxSharedUsers = _InternetProfile_MaxSharedUsers_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 465),
    _InternetProfile_MaxSharedUsers_Type()
)
internetProfile_MaxSharedUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_MaxSharedUsers.setStatus("mandatory")
_InternetProfile_AtmOptions_Mtu_Type = Integer32
_InternetProfile_AtmOptions_Mtu_Object = MibScalar
internetProfile_AtmOptions_Mtu = _InternetProfile_AtmOptions_Mtu_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 468),
    _InternetProfile_AtmOptions_Mtu_Type()
)
internetProfile_AtmOptions_Mtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmOptions_Mtu.setStatus("mandatory")
_InternetProfile_AtmConnectOptions_Mtu_Type = Integer32
_InternetProfile_AtmConnectOptions_Mtu_Object = MibScalar
internetProfile_AtmConnectOptions_Mtu = _InternetProfile_AtmConnectOptions_Mtu_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 469),
    _InternetProfile_AtmConnectOptions_Mtu_Type()
)
internetProfile_AtmConnectOptions_Mtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmConnectOptions_Mtu.setStatus("mandatory")


class _InternetProfile_AtmQosOptions_SubtendingHops_Type(Integer32):
    """Custom type internetProfile_AtmQosOptions_SubtendingHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("n-0Level", 1),
          ("n-1Level", 2),
          ("n-2Level", 3),
          ("n-3Level", 4))
    )


_InternetProfile_AtmQosOptions_SubtendingHops_Type.__name__ = "Integer32"
_InternetProfile_AtmQosOptions_SubtendingHops_Object = MibScalar
internetProfile_AtmQosOptions_SubtendingHops = _InternetProfile_AtmQosOptions_SubtendingHops_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 470),
    _InternetProfile_AtmQosOptions_SubtendingHops_Type()
)
internetProfile_AtmQosOptions_SubtendingHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_AtmQosOptions_SubtendingHops.setStatus("mandatory")
_InternetProfile_X25Options_X121SourceAddress_Type = DisplayString
_InternetProfile_X25Options_X121SourceAddress_Object = MibScalar
internetProfile_X25Options_X121SourceAddress = _InternetProfile_X25Options_X121SourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 471),
    _InternetProfile_X25Options_X121SourceAddress_Type()
)
internetProfile_X25Options_X121SourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_X121SourceAddress.setStatus("mandatory")


class _InternetProfile_X25Options_PosAuth_Type(Integer32):
    """Custom type internetProfile_X25Options_PosAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_InternetProfile_X25Options_PosAuth_Type.__name__ = "Integer32"
_InternetProfile_X25Options_PosAuth_Object = MibScalar
internetProfile_X25Options_PosAuth = _InternetProfile_X25Options_PosAuth_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 472),
    _InternetProfile_X25Options_PosAuth_Type()
)
internetProfile_X25Options_PosAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_X25Options_PosAuth.setStatus("mandatory")


class _InternetProfile_TunnelOptions_TosCopying_Type(Integer32):
    """Custom type internetProfile_TunnelOptions_TosCopying based on Integer32"""
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


_InternetProfile_TunnelOptions_TosCopying_Type.__name__ = "Integer32"
_InternetProfile_TunnelOptions_TosCopying_Object = MibScalar
internetProfile_TunnelOptions_TosCopying = _InternetProfile_TunnelOptions_TosCopying_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 473),
    _InternetProfile_TunnelOptions_TosCopying_Type()
)
internetProfile_TunnelOptions_TosCopying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_TunnelOptions_TosCopying.setStatus("mandatory")


class _InternetProfile_IpsecOptions_Enabled_Type(Integer32):
    """Custom type internetProfile_IpsecOptions_Enabled based on Integer32"""
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


_InternetProfile_IpsecOptions_Enabled_Type.__name__ = "Integer32"
_InternetProfile_IpsecOptions_Enabled_Object = MibScalar
internetProfile_IpsecOptions_Enabled = _InternetProfile_IpsecOptions_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 474),
    _InternetProfile_IpsecOptions_Enabled_Type()
)
internetProfile_IpsecOptions_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpsecOptions_Enabled.setStatus("mandatory")
_InternetProfile_IpsecOptions_SecurityPolicyDatabase_Type = DisplayString
_InternetProfile_IpsecOptions_SecurityPolicyDatabase_Object = MibScalar
internetProfile_IpsecOptions_SecurityPolicyDatabase = _InternetProfile_IpsecOptions_SecurityPolicyDatabase_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 475),
    _InternetProfile_IpsecOptions_SecurityPolicyDatabase_Type()
)
internetProfile_IpsecOptions_SecurityPolicyDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpsecOptions_SecurityPolicyDatabase.setStatus("mandatory")


class _InternetProfile_PriorityOptions_PacketClassification_Type(Integer32):
    """Custom type internetProfile_PriorityOptions_PacketClassification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qosTag", 2),
          ("udpPortRange", 3))
    )


_InternetProfile_PriorityOptions_PacketClassification_Type.__name__ = "Integer32"
_InternetProfile_PriorityOptions_PacketClassification_Object = MibScalar
internetProfile_PriorityOptions_PacketClassification = _InternetProfile_PriorityOptions_PacketClassification_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 477),
    _InternetProfile_PriorityOptions_PacketClassification_Type()
)
internetProfile_PriorityOptions_PacketClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PriorityOptions_PacketClassification.setStatus("mandatory")
_InternetProfile_PriorityOptions_MaxRtpPacketDelay_Type = Integer32
_InternetProfile_PriorityOptions_MaxRtpPacketDelay_Object = MibScalar
internetProfile_PriorityOptions_MaxRtpPacketDelay = _InternetProfile_PriorityOptions_MaxRtpPacketDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 478),
    _InternetProfile_PriorityOptions_MaxRtpPacketDelay_Type()
)
internetProfile_PriorityOptions_MaxRtpPacketDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PriorityOptions_MaxRtpPacketDelay.setStatus("mandatory")
_InternetProfile_PriorityOptions_MinimumRtpPort_Type = Integer32
_InternetProfile_PriorityOptions_MinimumRtpPort_Object = MibScalar
internetProfile_PriorityOptions_MinimumRtpPort = _InternetProfile_PriorityOptions_MinimumRtpPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 479),
    _InternetProfile_PriorityOptions_MinimumRtpPort_Type()
)
internetProfile_PriorityOptions_MinimumRtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PriorityOptions_MinimumRtpPort.setStatus("mandatory")
_InternetProfile_PriorityOptions_MaximumRtpPort_Type = Integer32
_InternetProfile_PriorityOptions_MaximumRtpPort_Object = MibScalar
internetProfile_PriorityOptions_MaximumRtpPort = _InternetProfile_PriorityOptions_MaximumRtpPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 480),
    _InternetProfile_PriorityOptions_MaximumRtpPort_Type()
)
internetProfile_PriorityOptions_MaximumRtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PriorityOptions_MaximumRtpPort.setStatus("mandatory")
_InternetProfile_PriorityOptions_NoHighPrioPktDuration_Type = Integer32
_InternetProfile_PriorityOptions_NoHighPrioPktDuration_Object = MibScalar
internetProfile_PriorityOptions_NoHighPrioPktDuration = _InternetProfile_PriorityOptions_NoHighPrioPktDuration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 481),
    _InternetProfile_PriorityOptions_NoHighPrioPktDuration_Type()
)
internetProfile_PriorityOptions_NoHighPrioPktDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PriorityOptions_NoHighPrioPktDuration.setStatus("mandatory")


class _InternetProfile_PriorityOptions_Enabled_Type(Integer32):
    """Custom type internetProfile_PriorityOptions_Enabled based on Integer32"""
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


_InternetProfile_PriorityOptions_Enabled_Type.__name__ = "Integer32"
_InternetProfile_PriorityOptions_Enabled_Object = MibScalar
internetProfile_PriorityOptions_Enabled = _InternetProfile_PriorityOptions_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 1, 1, 482),
    _InternetProfile_PriorityOptions_Enabled_Type()
)
internetProfile_PriorityOptions_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_PriorityOptions_Enabled.setStatus("mandatory")
_MibinternetProfile_IpxOptions_IpxSapHsProxyNetTable_Object = MibTable
mibinternetProfile_IpxOptions_IpxSapHsProxyNetTable = _MibinternetProfile_IpxOptions_IpxSapHsProxyNetTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 2)
)
if mibBuilder.loadTexts:
    mibinternetProfile_IpxOptions_IpxSapHsProxyNetTable.setStatus("mandatory")
_MibinternetProfile_IpxOptions_IpxSapHsProxyNetEntry_Object = MibTableRow
mibinternetProfile_IpxOptions_IpxSapHsProxyNetEntry = _MibinternetProfile_IpxOptions_IpxSapHsProxyNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 2, 1)
)
mibinternetProfile_IpxOptions_IpxSapHsProxyNetEntry.setIndexNames(
    (0, "ASCEND-MIBINET-MIB", "internetProfile-IpxOptions-IpxSapHsProxyNet-Station"),
    (0, "ASCEND-MIBINET-MIB", "internetProfile-IpxOptions-IpxSapHsProxyNet-Index-o"),
)
if mibBuilder.loadTexts:
    mibinternetProfile_IpxOptions_IpxSapHsProxyNetEntry.setStatus("mandatory")
_InternetProfile_IpxOptions_IpxSapHsProxyNet_Station_Type = DisplayString
_InternetProfile_IpxOptions_IpxSapHsProxyNet_Station_Object = MibScalar
internetProfile_IpxOptions_IpxSapHsProxyNet_Station = _InternetProfile_IpxOptions_IpxSapHsProxyNet_Station_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 2, 1, 1),
    _InternetProfile_IpxOptions_IpxSapHsProxyNet_Station_Type()
)
internetProfile_IpxOptions_IpxSapHsProxyNet_Station.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_IpxOptions_IpxSapHsProxyNet_Station.setStatus("mandatory")
_InternetProfile_IpxOptions_IpxSapHsProxyNet_Index_o_Type = Integer32
_InternetProfile_IpxOptions_IpxSapHsProxyNet_Index_o_Object = MibScalar
internetProfile_IpxOptions_IpxSapHsProxyNet_Index_o = _InternetProfile_IpxOptions_IpxSapHsProxyNet_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 2, 1, 2),
    _InternetProfile_IpxOptions_IpxSapHsProxyNet_Index_o_Type()
)
internetProfile_IpxOptions_IpxSapHsProxyNet_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internetProfile_IpxOptions_IpxSapHsProxyNet_Index_o.setStatus("mandatory")
_InternetProfile_IpxOptions_IpxSapHsProxyNet_Type = Integer32
_InternetProfile_IpxOptions_IpxSapHsProxyNet_Object = MibScalar
internetProfile_IpxOptions_IpxSapHsProxyNet = _InternetProfile_IpxOptions_IpxSapHsProxyNet_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 1, 2, 1, 3),
    _InternetProfile_IpxOptions_IpxSapHsProxyNet_Type()
)
internetProfile_IpxOptions_IpxSapHsProxyNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internetProfile_IpxOptions_IpxSapHsProxyNet.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBINET-MIB",
    **{"DisplayString": DisplayString,
       "mibinternetProfile": mibinternetProfile,
       "mibinternetProfileTable": mibinternetProfileTable,
       "mibinternetProfileEntry": mibinternetProfileEntry,
       "internetProfile-Station": internetProfile_Station,
       "internetProfile-Active": internetProfile_Active,
       "internetProfile-EncapsulationProtocol": internetProfile_EncapsulationProtocol,
       "internetProfile-CalledNumberType": internetProfile_CalledNumberType,
       "internetProfile-DialNumber": internetProfile_DialNumber,
       "internetProfile-Clid": internetProfile_Clid,
       "internetProfile-IpOptions-IpRoutingEnabled": internetProfile_IpOptions_IpRoutingEnabled,
       "internetProfile-IpOptions-VjHeaderPrediction": internetProfile_IpOptions_VjHeaderPrediction,
       "internetProfile-IpOptions-RemoteAddress": internetProfile_IpOptions_RemoteAddress,
       "internetProfile-IpOptions-NetmaskRemote": internetProfile_IpOptions_NetmaskRemote,
       "internetProfile-IpOptions-LocalAddress": internetProfile_IpOptions_LocalAddress,
       "internetProfile-IpOptions-NetmaskLocal": internetProfile_IpOptions_NetmaskLocal,
       "internetProfile-IpOptions-RoutingMetric": internetProfile_IpOptions_RoutingMetric,
       "internetProfile-IpOptions-Preference": internetProfile_IpOptions_Preference,
       "internetProfile-IpOptions-DownPreference": internetProfile_IpOptions_DownPreference,
       "internetProfile-IpOptions-PrivateRoute": internetProfile_IpOptions_PrivateRoute,
       "internetProfile-IpOptions-MulticastAllowed": internetProfile_IpOptions_MulticastAllowed,
       "internetProfile-IpOptions-AddressPool": internetProfile_IpOptions_AddressPool,
       "internetProfile-IpOptions-IpDirect": internetProfile_IpOptions_IpDirect,
       "internetProfile-IpOptions-Rip": internetProfile_IpOptions_Rip,
       "internetProfile-IpOptions-RouteFilter": internetProfile_IpOptions_RouteFilter,
       "internetProfile-IpOptions-SourceIpCheck": internetProfile_IpOptions_SourceIpCheck,
       "internetProfile-IpOptions-OspfOptions-Active": internetProfile_IpOptions_OspfOptions_Active,
       "internetProfile-IpOptions-OspfOptions-Area": internetProfile_IpOptions_OspfOptions_Area,
       "internetProfile-IpOptions-OspfOptions-AreaType": internetProfile_IpOptions_OspfOptions_AreaType,
       "internetProfile-IpOptions-OspfOptions-HelloInterval": internetProfile_IpOptions_OspfOptions_HelloInterval,
       "internetProfile-IpOptions-OspfOptions-DeadInterval": internetProfile_IpOptions_OspfOptions_DeadInterval,
       "internetProfile-IpOptions-OspfOptions-Priority": internetProfile_IpOptions_OspfOptions_Priority,
       "internetProfile-IpOptions-OspfOptions-AuthenType": internetProfile_IpOptions_OspfOptions_AuthenType,
       "internetProfile-IpOptions-OspfOptions-AuthKey": internetProfile_IpOptions_OspfOptions_AuthKey,
       "internetProfile-IpOptions-OspfOptions-KeyId": internetProfile_IpOptions_OspfOptions_KeyId,
       "internetProfile-IpOptions-OspfOptions-Cost": internetProfile_IpOptions_OspfOptions_Cost,
       "internetProfile-IpOptions-OspfOptions-DownCost": internetProfile_IpOptions_OspfOptions_DownCost,
       "internetProfile-IpOptions-OspfOptions-AseType": internetProfile_IpOptions_OspfOptions_AseType,
       "internetProfile-IpOptions-OspfOptions-AseTag": internetProfile_IpOptions_OspfOptions_AseTag,
       "internetProfile-IpOptions-OspfOptions-TransitDelay": internetProfile_IpOptions_OspfOptions_TransitDelay,
       "internetProfile-IpOptions-OspfOptions-RetransmitInterval": internetProfile_IpOptions_OspfOptions_RetransmitInterval,
       "internetProfile-IpOptions-OspfOptions-NonMulticast": internetProfile_IpOptions_OspfOptions_NonMulticast,
       "internetProfile-IpOptions-MulticastRateLimit": internetProfile_IpOptions_MulticastRateLimit,
       "internetProfile-IpOptions-MulticastGroupLeaveDelay": internetProfile_IpOptions_MulticastGroupLeaveDelay,
       "internetProfile-IpOptions-ClientDnsPrimaryAddr": internetProfile_IpOptions_ClientDnsPrimaryAddr,
       "internetProfile-IpOptions-ClientDnsSecondaryAddr": internetProfile_IpOptions_ClientDnsSecondaryAddr,
       "internetProfile-IpOptions-ClientDnsAddrAssign": internetProfile_IpOptions_ClientDnsAddrAssign,
       "internetProfile-IpOptions-ClientDefaultGateway": internetProfile_IpOptions_ClientDefaultGateway,
       "internetProfile-IpOptions-TosOptions-Active": internetProfile_IpOptions_TosOptions_Active,
       "internetProfile-IpOptions-TosOptions-Precedence": internetProfile_IpOptions_TosOptions_Precedence,
       "internetProfile-IpOptions-TosOptions-TypeOfService": internetProfile_IpOptions_TosOptions_TypeOfService,
       "internetProfile-IpOptions-TosOptions-ApplyTo": internetProfile_IpOptions_TosOptions_ApplyTo,
       "internetProfile-IpOptions-TosFilter": internetProfile_IpOptions_TosFilter,
       "internetProfile-IpxOptions-IpxRoutingEnabled": internetProfile_IpxOptions_IpxRoutingEnabled,
       "internetProfile-IpxOptions-PeerMode": internetProfile_IpxOptions_PeerMode,
       "internetProfile-IpxOptions-Rip": internetProfile_IpxOptions_Rip,
       "internetProfile-IpxOptions-Sap": internetProfile_IpxOptions_Sap,
       "internetProfile-IpxOptions-DialQuery": internetProfile_IpxOptions_DialQuery,
       "internetProfile-IpxOptions-NetNumber": internetProfile_IpxOptions_NetNumber,
       "internetProfile-IpxOptions-NetAlias": internetProfile_IpxOptions_NetAlias,
       "internetProfile-IpxOptions-SapFilter": internetProfile_IpxOptions_SapFilter,
       "internetProfile-IpxOptions-IpxSpoofing": internetProfile_IpxOptions_IpxSpoofing,
       "internetProfile-IpxOptions-SpoofingTimeout": internetProfile_IpxOptions_SpoofingTimeout,
       "internetProfile-IpxOptions-IpxSapHsProxy": internetProfile_IpxOptions_IpxSapHsProxy,
       "internetProfile-IpxOptions-IpxHeaderCompression": internetProfile_IpxOptions_IpxHeaderCompression,
       "internetProfile-BridgingOptions-BridgingGroup": internetProfile_BridgingOptions_BridgingGroup,
       "internetProfile-BridgingOptions-DialOnBroadcast": internetProfile_BridgingOptions_DialOnBroadcast,
       "internetProfile-BridgingOptions-IpxSpoofing": internetProfile_BridgingOptions_IpxSpoofing,
       "internetProfile-BridgingOptions-SpoofingTimeout": internetProfile_BridgingOptions_SpoofingTimeout,
       "internetProfile-BridgingOptions-BridgeType": internetProfile_BridgingOptions_BridgeType,
       "internetProfile-SessionOptions-CallFilter": internetProfile_SessionOptions_CallFilter,
       "internetProfile-SessionOptions-DataFilter": internetProfile_SessionOptions_DataFilter,
       "internetProfile-SessionOptions-FilterPersistence": internetProfile_SessionOptions_FilterPersistence,
       "internetProfile-SessionOptions-IdleTimer": internetProfile_SessionOptions_IdleTimer,
       "internetProfile-SessionOptions-TsIdleMode": internetProfile_SessionOptions_TsIdleMode,
       "internetProfile-SessionOptions-TsIdleTimer": internetProfile_SessionOptions_TsIdleTimer,
       "internetProfile-SessionOptions-Backup": internetProfile_SessionOptions_Backup,
       "internetProfile-SessionOptions-Secondary": internetProfile_SessionOptions_Secondary,
       "internetProfile-SessionOptions-MaxCallDuration": internetProfile_SessionOptions_MaxCallDuration,
       "internetProfile-SessionOptions-VtpGateway": internetProfile_SessionOptions_VtpGateway,
       "internetProfile-SessionOptions-Blockcountlimit": internetProfile_SessionOptions_Blockcountlimit,
       "internetProfile-SessionOptions-Blockduration": internetProfile_SessionOptions_Blockduration,
       "internetProfile-SessionOptions-MaxVtpTunnels": internetProfile_SessionOptions_MaxVtpTunnels,
       "internetProfile-SessionOptions-RedialDelayLimit": internetProfile_SessionOptions_RedialDelayLimit,
       "internetProfile-SessionOptions-SesRateType": internetProfile_SessionOptions_SesRateType,
       "internetProfile-SessionOptions-SesRateMode": internetProfile_SessionOptions_SesRateMode,
       "internetProfile-SessionOptions-SesAdslCapUpRate": internetProfile_SessionOptions_SesAdslCapUpRate,
       "internetProfile-SessionOptions-SesAdslCapDownRate": internetProfile_SessionOptions_SesAdslCapDownRate,
       "internetProfile-SessionOptions-SesSdslRate": internetProfile_SessionOptions_SesSdslRate,
       "internetProfile-SessionOptions-SesAdslDmtUpRate": internetProfile_SessionOptions_SesAdslDmtUpRate,
       "internetProfile-SessionOptions-SesAdslDmtDownRate": internetProfile_SessionOptions_SesAdslDmtDownRate,
       "internetProfile-SessionOptions-RxDataRateLimit": internetProfile_SessionOptions_RxDataRateLimit,
       "internetProfile-SessionOptions-TxDataRateLimit": internetProfile_SessionOptions_TxDataRateLimit,
       "internetProfile-TelcoOptions-AnswerOriginate": internetProfile_TelcoOptions_AnswerOriginate,
       "internetProfile-TelcoOptions-Callback": internetProfile_TelcoOptions_Callback,
       "internetProfile-TelcoOptions-CallType": internetProfile_TelcoOptions_CallType,
       "internetProfile-TelcoOptions-NailedGroups": internetProfile_TelcoOptions_NailedGroups,
       "internetProfile-TelcoOptions-Ft1Caller": internetProfile_TelcoOptions_Ft1Caller,
       "internetProfile-TelcoOptions-Force56kbps": internetProfile_TelcoOptions_Force56kbps,
       "internetProfile-TelcoOptions-DataService": internetProfile_TelcoOptions_DataService,
       "internetProfile-TelcoOptions-CallByCall": internetProfile_TelcoOptions_CallByCall,
       "internetProfile-TelcoOptions-BillingNumber": internetProfile_TelcoOptions_BillingNumber,
       "internetProfile-TelcoOptions-TransitNumber": internetProfile_TelcoOptions_TransitNumber,
       "internetProfile-TelcoOptions-ExpectCallback": internetProfile_TelcoOptions_ExpectCallback,
       "internetProfile-TelcoOptions-DialoutAllowed": internetProfile_TelcoOptions_DialoutAllowed,
       "internetProfile-TelcoOptions-DelayCallback": internetProfile_TelcoOptions_DelayCallback,
       "internetProfile-PppOptions-SendAuthMode": internetProfile_PppOptions_SendAuthMode,
       "internetProfile-PppOptions-SendPassword": internetProfile_PppOptions_SendPassword,
       "internetProfile-PppOptions-SubstituteSendName": internetProfile_PppOptions_SubstituteSendName,
       "internetProfile-PppOptions-RecvPassword": internetProfile_PppOptions_RecvPassword,
       "internetProfile-PppOptions-LinkCompression": internetProfile_PppOptions_LinkCompression,
       "internetProfile-PppOptions-Mru": internetProfile_PppOptions_Mru,
       "internetProfile-PppOptions-Lqm": internetProfile_PppOptions_Lqm,
       "internetProfile-PppOptions-LqmMinimumPeriod": internetProfile_PppOptions_LqmMinimumPeriod,
       "internetProfile-PppOptions-LqmMaximumPeriod": internetProfile_PppOptions_LqmMaximumPeriod,
       "internetProfile-PppOptions-CbcpEnabled": internetProfile_PppOptions_CbcpEnabled,
       "internetProfile-PppOptions-ModeCallbackControl": internetProfile_PppOptions_ModeCallbackControl,
       "internetProfile-PppOptions-DelayCallbackControl": internetProfile_PppOptions_DelayCallbackControl,
       "internetProfile-PppOptions-TrunkGroupCallbackControl": internetProfile_PppOptions_TrunkGroupCallbackControl,
       "internetProfile-PppOptions-SplitCodeDotUserEnabled": internetProfile_PppOptions_SplitCodeDotUserEnabled,
       "internetProfile-PppOptions-PppInterfaceType": internetProfile_PppOptions_PppInterfaceType,
       "internetProfile-MpOptions-BaseChannelCount": internetProfile_MpOptions_BaseChannelCount,
       "internetProfile-MpOptions-MinimumChannels": internetProfile_MpOptions_MinimumChannels,
       "internetProfile-MpOptions-MaximumChannels": internetProfile_MpOptions_MaximumChannels,
       "internetProfile-MpOptions-BacpEnable": internetProfile_MpOptions_BacpEnable,
       "internetProfile-MppOptions-AuxSendPassword": internetProfile_MppOptions_AuxSendPassword,
       "internetProfile-MppOptions-DynamicAlgorithm": internetProfile_MppOptions_DynamicAlgorithm,
       "internetProfile-MppOptions-BandwidthMonitorDirection": internetProfile_MppOptions_BandwidthMonitorDirection,
       "internetProfile-MppOptions-IncrementChannelCount": internetProfile_MppOptions_IncrementChannelCount,
       "internetProfile-MppOptions-DecrementChannelCount": internetProfile_MppOptions_DecrementChannelCount,
       "internetProfile-MppOptions-SecondsHistory": internetProfile_MppOptions_SecondsHistory,
       "internetProfile-MppOptions-AddPersistence": internetProfile_MppOptions_AddPersistence,
       "internetProfile-MppOptions-SubPersistence": internetProfile_MppOptions_SubPersistence,
       "internetProfile-MppOptions-TargetUtilization": internetProfile_MppOptions_TargetUtilization,
       "internetProfile-FrOptions-FrameRelayProfile": internetProfile_FrOptions_FrameRelayProfile,
       "internetProfile-FrOptions-Dlci": internetProfile_FrOptions_Dlci,
       "internetProfile-FrOptions-CircuitName": internetProfile_FrOptions_CircuitName,
       "internetProfile-FrOptions-FrDirectEnabled": internetProfile_FrOptions_FrDirectEnabled,
       "internetProfile-FrOptions-FrDirectProfile": internetProfile_FrOptions_FrDirectProfile,
       "internetProfile-FrOptions-FrDirectDlci": internetProfile_FrOptions_FrDirectDlci,
       "internetProfile-TcpClearOptions-Host": internetProfile_TcpClearOptions_Host,
       "internetProfile-TcpClearOptions-Port": internetProfile_TcpClearOptions_Port,
       "internetProfile-TcpClearOptions-Host2": internetProfile_TcpClearOptions_Host2,
       "internetProfile-TcpClearOptions-Port2": internetProfile_TcpClearOptions_Port2,
       "internetProfile-TcpClearOptions-Host3": internetProfile_TcpClearOptions_Host3,
       "internetProfile-TcpClearOptions-Port3": internetProfile_TcpClearOptions_Port3,
       "internetProfile-TcpClearOptions-Host4": internetProfile_TcpClearOptions_Host4,
       "internetProfile-TcpClearOptions-Port4": internetProfile_TcpClearOptions_Port4,
       "internetProfile-TcpClearOptions-DetectEndOfPacket": internetProfile_TcpClearOptions_DetectEndOfPacket,
       "internetProfile-TcpClearOptions-EndOfPacketPattern": internetProfile_TcpClearOptions_EndOfPacketPattern,
       "internetProfile-TcpClearOptions-FlushLength": internetProfile_TcpClearOptions_FlushLength,
       "internetProfile-TcpClearOptions-FlushTime": internetProfile_TcpClearOptions_FlushTime,
       "internetProfile-AraOptions-RecvPassword": internetProfile_AraOptions_RecvPassword,
       "internetProfile-AraOptions-MaximumConnectTime": internetProfile_AraOptions_MaximumConnectTime,
       "internetProfile-X25Options-X25Profile": internetProfile_X25Options_X25Profile,
       "internetProfile-X25Options-Lcn": internetProfile_X25Options_Lcn,
       "internetProfile-X25Options-X3Profile": internetProfile_X25Options_X3Profile,
       "internetProfile-X25Options-MaxCalls": internetProfile_X25Options_MaxCalls,
       "internetProfile-X25Options-VcTimerEnable": internetProfile_X25Options_VcTimerEnable,
       "internetProfile-X25Options-X25EncapsType": internetProfile_X25Options_X25EncapsType,
       "internetProfile-X25Options-ReverseCharge": internetProfile_X25Options_ReverseCharge,
       "internetProfile-X25Options-CallMode": internetProfile_X25Options_CallMode,
       "internetProfile-X25Options-InactivityTimer": internetProfile_X25Options_InactivityTimer,
       "internetProfile-X25Options-X25Rpoa": internetProfile_X25Options_X25Rpoa,
       "internetProfile-X25Options-X25CugIndex": internetProfile_X25Options_X25CugIndex,
       "internetProfile-X25Options-X25Nui": internetProfile_X25Options_X25Nui,
       "internetProfile-X25Options-PadBanner": internetProfile_X25Options_PadBanner,
       "internetProfile-X25Options-PadPrompt": internetProfile_X25Options_PadPrompt,
       "internetProfile-X25Options-PadNuiPrompt": internetProfile_X25Options_PadNuiPrompt,
       "internetProfile-X25Options-PadNuiPwPrompt": internetProfile_X25Options_PadNuiPwPrompt,
       "internetProfile-X25Options-PadAlias1": internetProfile_X25Options_PadAlias1,
       "internetProfile-X25Options-PadAlias2": internetProfile_X25Options_PadAlias2,
       "internetProfile-X25Options-PadAlias3": internetProfile_X25Options_PadAlias3,
       "internetProfile-X25Options-PadDiagDisp": internetProfile_X25Options_PadDiagDisp,
       "internetProfile-X25Options-PadDefaultListen": internetProfile_X25Options_PadDefaultListen,
       "internetProfile-X25Options-PadDefaultPw": internetProfile_X25Options_PadDefaultPw,
       "internetProfile-EuOptions-DceAddr": internetProfile_EuOptions_DceAddr,
       "internetProfile-EuOptions-DteAddr": internetProfile_EuOptions_DteAddr,
       "internetProfile-EuOptions-Mru": internetProfile_EuOptions_Mru,
       "internetProfile-X75Options-KFramesOutstanding": internetProfile_X75Options_KFramesOutstanding,
       "internetProfile-X75Options-N2Retransmissions": internetProfile_X75Options_N2Retransmissions,
       "internetProfile-X75Options-T1RetranTimer": internetProfile_X75Options_T1RetranTimer,
       "internetProfile-X75Options-FrameLength": internetProfile_X75Options_FrameLength,
       "internetProfile-AppletalkOptions-AtalkRoutingEnabled": internetProfile_AppletalkOptions_AtalkRoutingEnabled,
       "internetProfile-AppletalkOptions-AtalkStaticZoneName": internetProfile_AppletalkOptions_AtalkStaticZoneName,
       "internetProfile-AppletalkOptions-AtalkStaticNetStart": internetProfile_AppletalkOptions_AtalkStaticNetStart,
       "internetProfile-AppletalkOptions-AtalkStaticNetEnd": internetProfile_AppletalkOptions_AtalkStaticNetEnd,
       "internetProfile-AppletalkOptions-AtalkPeerMode": internetProfile_AppletalkOptions_AtalkPeerMode,
       "internetProfile-UsrRadOptions-AcctType": internetProfile_UsrRadOptions_AcctType,
       "internetProfile-UsrRadOptions-AcctHost": internetProfile_UsrRadOptions_AcctHost,
       "internetProfile-UsrRadOptions-AcctPort": internetProfile_UsrRadOptions_AcctPort,
       "internetProfile-UsrRadOptions-AcctKey": internetProfile_UsrRadOptions_AcctKey,
       "internetProfile-UsrRadOptions-AcctTimeout": internetProfile_UsrRadOptions_AcctTimeout,
       "internetProfile-UsrRadOptions-AcctIdBase": internetProfile_UsrRadOptions_AcctIdBase,
       "internetProfile-CalledNumber": internetProfile_CalledNumber,
       "internetProfile-DhcpOptions-ReplyEnabled": internetProfile_DhcpOptions_ReplyEnabled,
       "internetProfile-DhcpOptions-PoolNumber": internetProfile_DhcpOptions_PoolNumber,
       "internetProfile-DhcpOptions-MaximumLeases": internetProfile_DhcpOptions_MaximumLeases,
       "internetProfile-T3posOptions-X25Profile": internetProfile_T3posOptions_X25Profile,
       "internetProfile-T3posOptions-MaxCalls": internetProfile_T3posOptions_MaxCalls,
       "internetProfile-T3posOptions-AutoCallX121Address": internetProfile_T3posOptions_AutoCallX121Address,
       "internetProfile-T3posOptions-ReverseCharge": internetProfile_T3posOptions_ReverseCharge,
       "internetProfile-T3posOptions-Answer": internetProfile_T3posOptions_Answer,
       "internetProfile-T3posOptions-T3PosHostInitMode": internetProfile_T3posOptions_T3PosHostInitMode,
       "internetProfile-T3posOptions-T3PosDteInitMode": internetProfile_T3posOptions_T3PosDteInitMode,
       "internetProfile-T3posOptions-T3PosEnqHandling": internetProfile_T3posOptions_T3PosEnqHandling,
       "internetProfile-T3posOptions-T3PosMaxBlockSize": internetProfile_T3posOptions_T3PosMaxBlockSize,
       "internetProfile-T3posOptions-T3PosT1": internetProfile_T3posOptions_T3PosT1,
       "internetProfile-T3posOptions-T3PosT2": internetProfile_T3posOptions_T3PosT2,
       "internetProfile-T3posOptions-T3PosT3": internetProfile_T3posOptions_T3PosT3,
       "internetProfile-T3posOptions-T3PosT4": internetProfile_T3posOptions_T3PosT4,
       "internetProfile-T3posOptions-T3PosT5": internetProfile_T3posOptions_T3PosT5,
       "internetProfile-T3posOptions-T3PosT6": internetProfile_T3posOptions_T3PosT6,
       "internetProfile-T3posOptions-T3PosMethodOfHostNotif": internetProfile_T3posOptions_T3PosMethodOfHostNotif,
       "internetProfile-T3posOptions-T3PosPidSelection": internetProfile_T3posOptions_T3PosPidSelection,
       "internetProfile-T3posOptions-T3PosAckSuppression": internetProfile_T3posOptions_T3PosAckSuppression,
       "internetProfile-T3posOptions-X25Rpoa": internetProfile_T3posOptions_X25Rpoa,
       "internetProfile-T3posOptions-X25CugIndex": internetProfile_T3posOptions_X25CugIndex,
       "internetProfile-T3posOptions-X25Nui": internetProfile_T3posOptions_X25Nui,
       "internetProfile-T3posOptions-DataFormat": internetProfile_T3posOptions_DataFormat,
       "internetProfile-T3posOptions-LinkAccessType": internetProfile_T3posOptions_LinkAccessType,
       "internetProfile-FramedOnly": internetProfile_FramedOnly,
       "internetProfile-AltdialNumber1": internetProfile_AltdialNumber1,
       "internetProfile-AltdialNumber2": internetProfile_AltdialNumber2,
       "internetProfile-AltdialNumber3": internetProfile_AltdialNumber3,
       "internetProfile-X32Options-X32Profile": internetProfile_X32Options_X32Profile,
       "internetProfile-X32Options-CallMode": internetProfile_X32Options_CallMode,
       "internetProfile-TunnelOptions-ProfileType": internetProfile_TunnelOptions_ProfileType,
       "internetProfile-TunnelOptions-TunnelingProtocol": internetProfile_TunnelOptions_TunnelingProtocol,
       "internetProfile-TunnelOptions-MaxTunnels": internetProfile_TunnelOptions_MaxTunnels,
       "internetProfile-TunnelOptions-AtmpHaRip": internetProfile_TunnelOptions_AtmpHaRip,
       "internetProfile-TunnelOptions-PrimaryTunnelServer": internetProfile_TunnelOptions_PrimaryTunnelServer,
       "internetProfile-TunnelOptions-SecondaryTunnelServer": internetProfile_TunnelOptions_SecondaryTunnelServer,
       "internetProfile-TunnelOptions-UdpPort": internetProfile_TunnelOptions_UdpPort,
       "internetProfile-TunnelOptions-Password": internetProfile_TunnelOptions_Password,
       "internetProfile-TunnelOptions-HomeNetworkName": internetProfile_TunnelOptions_HomeNetworkName,
       "internetProfile-PriNumberingPlanId": internetProfile_PriNumberingPlanId,
       "internetProfile-Vrouter": internetProfile_Vrouter,
       "internetProfile-AtmOptions-Atm1483type": internetProfile_AtmOptions_Atm1483type,
       "internetProfile-AtmOptions-Vpi": internetProfile_AtmOptions_Vpi,
       "internetProfile-AtmOptions-Vci": internetProfile_AtmOptions_Vci,
       "internetProfile-Action-o": internetProfile_Action_o,
       "internetProfile-IpOptions-OspfOptions-NetworkType": internetProfile_IpOptions_OspfOptions_NetworkType,
       "internetProfile-IpOptions-OspfOptions-PollInterval": internetProfile_IpOptions_OspfOptions_PollInterval,
       "internetProfile-IpOptions-OspfOptions-Md5AuthKey": internetProfile_IpOptions_OspfOptions_Md5AuthKey,
       "internetProfile-BridgingOptions-Fill2": internetProfile_BridgingOptions_Fill2,
       "internetProfile-TelcoOptions-NasPortType": internetProfile_TelcoOptions_NasPortType,
       "internetProfile-MpOptions-BodEnable": internetProfile_MpOptions_BodEnable,
       "internetProfile-AtmOptions-NailedGroup": internetProfile_AtmOptions_NailedGroup,
       "internetProfile-AtmOptions-AtmServiceType": internetProfile_AtmOptions_AtmServiceType,
       "internetProfile-AtmOptions-AtmServiceRate": internetProfile_AtmOptions_AtmServiceRate,
       "internetProfile-HdlcNrmOptions-SnrmResponseTimeout": internetProfile_HdlcNrmOptions_SnrmResponseTimeout,
       "internetProfile-HdlcNrmOptions-SnrmRetryCounter": internetProfile_HdlcNrmOptions_SnrmRetryCounter,
       "internetProfile-HdlcNrmOptions-PollTimeout": internetProfile_HdlcNrmOptions_PollTimeout,
       "internetProfile-HdlcNrmOptions-PollRate": internetProfile_HdlcNrmOptions_PollRate,
       "internetProfile-HdlcNrmOptions-PollRetryCount": internetProfile_HdlcNrmOptions_PollRetryCount,
       "internetProfile-HdlcNrmOptions-Primary": internetProfile_HdlcNrmOptions_Primary,
       "internetProfile-AtmConnectOptions-Atm1483type": internetProfile_AtmConnectOptions_Atm1483type,
       "internetProfile-AtmConnectOptions-Vpi": internetProfile_AtmConnectOptions_Vpi,
       "internetProfile-AtmConnectOptions-Vci": internetProfile_AtmConnectOptions_Vci,
       "internetProfile-AtmConnectOptions-NailedGroup": internetProfile_AtmConnectOptions_NailedGroup,
       "internetProfile-AtmConnectOptions-AtmServiceType": internetProfile_AtmConnectOptions_AtmServiceType,
       "internetProfile-AtmConnectOptions-AtmServiceRate": internetProfile_AtmConnectOptions_AtmServiceRate,
       "internetProfile-Visa2Options-IdleCharacterDelay": internetProfile_Visa2Options_IdleCharacterDelay,
       "internetProfile-Visa2Options-FirstDataForwardCharacter": internetProfile_Visa2Options_FirstDataForwardCharacter,
       "internetProfile-Visa2Options-SecondDataForwardCharacter": internetProfile_Visa2Options_SecondDataForwardCharacter,
       "internetProfile-Visa2Options-ThirdDataForwardCharacter": internetProfile_Visa2Options_ThirdDataForwardCharacter,
       "internetProfile-Visa2Options-FourthDataForwardCharacter": internetProfile_Visa2Options_FourthDataForwardCharacter,
       "internetProfile-Visa2Options-o1CharSequence": internetProfile_Visa2Options_o1CharSequence,
       "internetProfile-Visa2Options-o2CharSequence": internetProfile_Visa2Options_o2CharSequence,
       "internetProfile-SdtnPacketsServer": internetProfile_SdtnPacketsServer,
       "internetProfile-oATString": internetProfile_oATString,
       "internetProfile-PortRedirectOptions-Protocol": internetProfile_PortRedirectOptions_Protocol,
       "internetProfile-PortRedirectOptions-PortNumber": internetProfile_PortRedirectOptions_PortNumber,
       "internetProfile-PortRedirectOptions-RedirectAddress": internetProfile_PortRedirectOptions_RedirectAddress,
       "internetProfile-SharedProf": internetProfile_SharedProf,
       "internetProfile-MpOptions-CallbackrequestEnable": internetProfile_MpOptions_CallbackrequestEnable,
       "internetProfile-BridgingOptions-Egress": internetProfile_BridgingOptions_Egress,
       "internetProfile-SessionOptions-TrafficShaper": internetProfile_SessionOptions_TrafficShaper,
       "internetProfile-FrOptions-MfrBundleName": internetProfile_FrOptions_MfrBundleName,
       "internetProfile-PppoeOptions-Pppoe": internetProfile_PppoeOptions_Pppoe,
       "internetProfile-PppoeOptions-BridgeNonPppoe": internetProfile_PppoeOptions_BridgeNonPppoe,
       "internetProfile-BirOptions-Enable": internetProfile_BirOptions_Enable,
       "internetProfile-BirOptions-ProxyArp": internetProfile_BirOptions_ProxyArp,
       "internetProfile-SubAddress": internetProfile_SubAddress,
       "internetProfile-IpOptions-ClientWinsPrimaryAddr": internetProfile_IpOptions_ClientWinsPrimaryAddr,
       "internetProfile-IpOptions-ClientWinsSecondaryAddr": internetProfile_IpOptions_ClientWinsSecondaryAddr,
       "internetProfile-IpOptions-ClientWinsAddrAssign": internetProfile_IpOptions_ClientWinsAddrAssign,
       "internetProfile-IpOptions-PrivateRouteTable": internetProfile_IpOptions_PrivateRouteTable,
       "internetProfile-IpOptions-PrivateRouteProfileRequired": internetProfile_IpOptions_PrivateRouteProfileRequired,
       "internetProfile-SessionOptions-FilterRequired": internetProfile_SessionOptions_FilterRequired,
       "internetProfile-SessionOptions-MaxtapLogServer": internetProfile_SessionOptions_MaxtapLogServer,
       "internetProfile-SessionOptions-MaxtapDataServer": internetProfile_SessionOptions_MaxtapDataServer,
       "internetProfile-PppOptions-Mtu": internetProfile_PppOptions_Mtu,
       "internetProfile-FrOptions-CircuitType": internetProfile_FrOptions_CircuitType,
       "internetProfile-FrOptions-FrLinkType": internetProfile_FrOptions_FrLinkType,
       "internetProfile-AtmOptions-VpSwitching": internetProfile_AtmOptions_VpSwitching,
       "internetProfile-AtmOptions-AtmDirectEnabled": internetProfile_AtmOptions_AtmDirectEnabled,
       "internetProfile-AtmOptions-AtmDirectProfile": internetProfile_AtmOptions_AtmDirectProfile,
       "internetProfile-AtmOptions-SvcOptions-Enabled": internetProfile_AtmOptions_SvcOptions_Enabled,
       "internetProfile-AtmOptions-AtmInverseArp": internetProfile_AtmOptions_AtmInverseArp,
       "internetProfile-AtmConnectOptions-VpSwitching": internetProfile_AtmConnectOptions_VpSwitching,
       "internetProfile-AtmConnectOptions-AtmDirectEnabled": internetProfile_AtmConnectOptions_AtmDirectEnabled,
       "internetProfile-AtmConnectOptions-AtmDirectProfile": internetProfile_AtmConnectOptions_AtmDirectProfile,
       "internetProfile-AtmConnectOptions-SvcOptions-Enabled": internetProfile_AtmConnectOptions_SvcOptions_Enabled,
       "internetProfile-AtmConnectOptions-AtmInverseArp": internetProfile_AtmConnectOptions_AtmInverseArp,
       "internetProfile-AtmQosOptions-UsrUpStreamContract": internetProfile_AtmQosOptions_UsrUpStreamContract,
       "internetProfile-AtmQosOptions-UsrDnStreamContract": internetProfile_AtmQosOptions_UsrDnStreamContract,
       "internetProfile-PppOptions-BiDirectionalAuth": internetProfile_PppOptions_BiDirectionalAuth,
       "internetProfile-PppOptions-SubstituteRecvName": internetProfile_PppOptions_SubstituteRecvName,
       "internetProfile-TunnelOptions-Vrouter": internetProfile_TunnelOptions_Vrouter,
       "internetProfile-AtmOptions-VcFaultManagement": internetProfile_AtmOptions_VcFaultManagement,
       "internetProfile-AtmOptions-VcMaxLoopbackCellLoss": internetProfile_AtmOptions_VcMaxLoopbackCellLoss,
       "internetProfile-AtmOptions-Fr08Mode": internetProfile_AtmOptions_Fr08Mode,
       "internetProfile-HdlcNrmOptions-AsyncDrop": internetProfile_HdlcNrmOptions_AsyncDrop,
       "internetProfile-AtmConnectOptions-VcFaultManagement": internetProfile_AtmConnectOptions_VcFaultManagement,
       "internetProfile-AtmConnectOptions-VcMaxLoopbackCellLoss": internetProfile_AtmConnectOptions_VcMaxLoopbackCellLoss,
       "internetProfile-AtmConnectOptions-Fr08Mode": internetProfile_AtmConnectOptions_Fr08Mode,
       "internetProfile-MppOptions-X25chanTargetUtilization": internetProfile_MppOptions_X25chanTargetUtilization,
       "internetProfile-AtmOptions-SvcOptions-IncomingCallerAddr-NumberingPlan": internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_NumberingPlan,
       "internetProfile-AtmOptions-SvcOptions-IncomingCallerAddr-E164NativeAddress": internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_E164NativeAddress,
       "internetProfile-AtmOptions-SvcOptions-IncomingCallerAddr-AesaAddress-Format": internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format,
       "internetProfile-AtmOptions-SvcOptions-IncomingCallerAddr-AesaAddress-IdpPortion-Afi": internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Afi,
       "internetProfile-AtmOptions-SvcOptions-IncomingCallerAddr-AesaAddress-IdpPortion-Idi": internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Idi,
       "internetProfile-AtmOptions-SvcOptions-IncomingCallerAddr-AesaAddress-DspPortion-HoDsp": internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_HoDsp,
       "internetProfile-AtmOptions-SvcOptions-IncomingCallerAddr-AesaAddress-DspPortion-Esi": internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Esi,
       "internetProfile-AtmOptions-SvcOptions-IncomingCallerAddr-AesaAddress-DspPortion-Sel": internetProfile_AtmOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Sel,
       "internetProfile-AtmOptions-SvcOptions-OutgoingCalledAddr-NumberingPlan": internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan,
       "internetProfile-AtmOptions-SvcOptions-OutgoingCalledAddr-E164NativeAddress": internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_E164NativeAddress,
       "internetProfile-AtmOptions-SvcOptions-OutgoingCalledAddr-AesaAddress-Format": internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format,
       "internetProfile-AtmOptions-SvcOptions-OutgoingCalledAddr-AesaAddress-IdpPortion-Afi": internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Afi,
       "internetProfile-AtmOptions-SvcOptions-OutgoingCalledAddr-AesaAddress-IdpPortion-Idi": internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Idi,
       "internetProfile-AtmOptions-SvcOptions-OutgoingCalledAddr-AesaAddress-DspPortion-HoDsp": internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_HoDsp,
       "internetProfile-AtmOptions-SvcOptions-OutgoingCalledAddr-AesaAddress-DspPortion-Esi": internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Esi,
       "internetProfile-AtmOptions-SvcOptions-OutgoingCalledAddr-AesaAddress-DspPortion-Sel": internetProfile_AtmOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Sel,
       "internetProfile-AtmConnectOptions-SvcOptions-IncomingCallerAddr-NumberingPlan": internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_NumberingPlan,
       "internetProfile-AtmConnectOptions-SvcOptions-IncomingCallerAddr-E164NativeAddress": internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_E164NativeAddress,
       "internetProfile-AtmConnectOptions-SvcOptions-IncomingCallerAddr-AesaAddress-Format": internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_Format,
       "internetProfile-AtmConnectOptions-SvcOptions-IncomingCallerAddr-AesaAddress-IdpPortion-Afi": internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Afi,
       "internetProfile-AtmConnectOptions-SvcOptions-IncomingCallerAddr-AesaAddress-IdpPortion-Idi": internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_IdpPortion_Idi,
       "internetProfile-AtmConnectOptions-SvcOptions-IncomingCallerAddr-AesaAddress-DspPortion-HoDsp": internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_HoDsp,
       "internetProfile-AtmConnectOptions-SvcOptions-IncomingCallerAddr-AesaAddress-DspPortion-Esi": internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Esi,
       "internetProfile-AtmConnectOptions-SvcOptions-IncomingCallerAddr-AesaAddress-DspPortion-Sel": internetProfile_AtmConnectOptions_SvcOptions_IncomingCallerAddr_AesaAddress_DspPortion_Sel,
       "internetProfile-AtmConnectOptions-SvcOptions-OutgoingCalledAddr-NumberingPlan": internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_NumberingPlan,
       "internetProfile-AtmConnectOptions-SvcOptions-OutgoingCalledAddr-E164NativeAddress": internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_E164NativeAddress,
       "internetProfile-AtmConnectOptions-SvcOptions-OutgoingCalledAddr-AesaAddress-Format": internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_Format,
       "internetProfile-AtmConnectOptions-SvcOptions-OutgoingCalledAddr-AesaAddress-IdpPortion-Afi": internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Afi,
       "internetProfile-AtmConnectOptions-SvcOptions-OutgoingCalledAddr-AesaAddress-IdpPortion-Idi": internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_IdpPortion_Idi,
       "internetProfile-AtmConnectOptions-SvcOptions-OutgoingCalledAddr-AesaAddress-DspPortion-HoDsp": internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_HoDsp,
       "internetProfile-AtmConnectOptions-SvcOptions-OutgoingCalledAddr-AesaAddress-DspPortion-Esi": internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Esi,
       "internetProfile-AtmConnectOptions-SvcOptions-OutgoingCalledAddr-AesaAddress-DspPortion-Sel": internetProfile_AtmConnectOptions_SvcOptions_OutgoingCalledAddr_AesaAddress_DspPortion_Sel,
       "internetProfile-TunnelOptions-ClientAuthId": internetProfile_TunnelOptions_ClientAuthId,
       "internetProfile-SessionOptions-CirTimer": internetProfile_SessionOptions_CirTimer,
       "internetProfile-SessionOptions-Priority": internetProfile_SessionOptions_Priority,
       "internetProfile-HdlcNrmOptions-StationPollAddress": internetProfile_HdlcNrmOptions_StationPollAddress,
       "internetProfile-TunnelOptions-ServerAuthId": internetProfile_TunnelOptions_ServerAuthId,
       "internetProfile-TunnelOptions-AssignmentId": internetProfile_TunnelOptions_AssignmentId,
       "internetProfile-IpOptions-NatProfileName": internetProfile_IpOptions_NatProfileName,
       "internetProfile-AutoProfiles": internetProfile_AutoProfiles,
       "internetProfile-IpOptions-AddressRealm": internetProfile_IpOptions_AddressRealm,
       "internetProfile-PppOptions-PppCircuit": internetProfile_PppOptions_PppCircuit,
       "internetProfile-PppOptions-PppCircuitName": internetProfile_PppOptions_PppCircuitName,
       "internetProfile-X32Options-X32ApplMode": internetProfile_X32Options_X32ApplMode,
       "internetProfile-CrossConnectIndex": internetProfile_CrossConnectIndex,
       "internetProfile-AtmOptions-CastType": internetProfile_AtmOptions_CastType,
       "internetProfile-AtmOptions-ConnKind": internetProfile_AtmOptions_ConnKind,
       "internetProfile-AtmOptions-TargetAtmAddress": internetProfile_AtmOptions_TargetAtmAddress,
       "internetProfile-AtmOptions-TargetSelect": internetProfile_AtmOptions_TargetSelect,
       "internetProfile-AtmOptions-TargetVpi": internetProfile_AtmOptions_TargetVpi,
       "internetProfile-AtmOptions-TargetVci": internetProfile_AtmOptions_TargetVci,
       "internetProfile-AtmOptions-AtmCircuitProfile": internetProfile_AtmOptions_AtmCircuitProfile,
       "internetProfile-AtmConnectOptions-CastType": internetProfile_AtmConnectOptions_CastType,
       "internetProfile-AtmConnectOptions-ConnKind": internetProfile_AtmConnectOptions_ConnKind,
       "internetProfile-AtmConnectOptions-TargetAtmAddress": internetProfile_AtmConnectOptions_TargetAtmAddress,
       "internetProfile-AtmConnectOptions-TargetSelect": internetProfile_AtmConnectOptions_TargetSelect,
       "internetProfile-AtmConnectOptions-TargetVpi": internetProfile_AtmConnectOptions_TargetVpi,
       "internetProfile-AtmConnectOptions-TargetVci": internetProfile_AtmConnectOptions_TargetVci,
       "internetProfile-AtmConnectOptions-AtmCircuitProfile": internetProfile_AtmConnectOptions_AtmCircuitProfile,
       "internetProfile-AtmAalOptions-AalEnabled": internetProfile_AtmAalOptions_AalEnabled,
       "internetProfile-AtmAalOptions-AalType": internetProfile_AtmAalOptions_AalType,
       "internetProfile-AtmAalOptions-TransmitSduSize": internetProfile_AtmAalOptions_TransmitSduSize,
       "internetProfile-AtmAalOptions-ReceiveSduSize": internetProfile_AtmAalOptions_ReceiveSduSize,
       "internetProfile-ConnUser": internetProfile_ConnUser,
       "internetProfile-AtmOptions-SpvcRetryInterval": internetProfile_AtmOptions_SpvcRetryInterval,
       "internetProfile-AtmOptions-SpvcRetryThreshold": internetProfile_AtmOptions_SpvcRetryThreshold,
       "internetProfile-AtmOptions-SpvcRetryLimit": internetProfile_AtmOptions_SpvcRetryLimit,
       "internetProfile-AtmOptions-OamAisF5": internetProfile_AtmOptions_OamAisF5,
       "internetProfile-AtmOptions-OamSupport": internetProfile_AtmOptions_OamSupport,
       "internetProfile-AtmConnectOptions-SpvcRetryInterval": internetProfile_AtmConnectOptions_SpvcRetryInterval,
       "internetProfile-AtmConnectOptions-SpvcRetryThreshold": internetProfile_AtmConnectOptions_SpvcRetryThreshold,
       "internetProfile-AtmConnectOptions-SpvcRetryLimit": internetProfile_AtmConnectOptions_SpvcRetryLimit,
       "internetProfile-AtmConnectOptions-OamAisF5": internetProfile_AtmConnectOptions_OamAisF5,
       "internetProfile-AtmConnectOptions-OamSupport": internetProfile_AtmConnectOptions_OamSupport,
       "internetProfile-ModemOnHoldTimeout": internetProfile_ModemOnHoldTimeout,
       "internetProfile-IpOptions-TosOptions-MarkingType": internetProfile_IpOptions_TosOptions_MarkingType,
       "internetProfile-IpOptions-TosOptions-Dscp": internetProfile_IpOptions_TosOptions_Dscp,
       "internetProfile-X25Options-RemoteX25Address": internetProfile_X25Options_RemoteX25Address,
       "internetProfile-X25Options-AnswerX25Address": internetProfile_X25Options_AnswerX25Address,
       "internetProfile-X25Options-Windowsize": internetProfile_X25Options_Windowsize,
       "internetProfile-X25Options-Packetsize": internetProfile_X25Options_Packetsize,
       "internetProfile-MaxSharedUsers": internetProfile_MaxSharedUsers,
       "internetProfile-AtmOptions-Mtu": internetProfile_AtmOptions_Mtu,
       "internetProfile-AtmConnectOptions-Mtu": internetProfile_AtmConnectOptions_Mtu,
       "internetProfile-AtmQosOptions-SubtendingHops": internetProfile_AtmQosOptions_SubtendingHops,
       "internetProfile-X25Options-X121SourceAddress": internetProfile_X25Options_X121SourceAddress,
       "internetProfile-X25Options-PosAuth": internetProfile_X25Options_PosAuth,
       "internetProfile-TunnelOptions-TosCopying": internetProfile_TunnelOptions_TosCopying,
       "internetProfile-IpsecOptions-Enabled": internetProfile_IpsecOptions_Enabled,
       "internetProfile-IpsecOptions-SecurityPolicyDatabase": internetProfile_IpsecOptions_SecurityPolicyDatabase,
       "internetProfile-PriorityOptions-PacketClassification": internetProfile_PriorityOptions_PacketClassification,
       "internetProfile-PriorityOptions-MaxRtpPacketDelay": internetProfile_PriorityOptions_MaxRtpPacketDelay,
       "internetProfile-PriorityOptions-MinimumRtpPort": internetProfile_PriorityOptions_MinimumRtpPort,
       "internetProfile-PriorityOptions-MaximumRtpPort": internetProfile_PriorityOptions_MaximumRtpPort,
       "internetProfile-PriorityOptions-NoHighPrioPktDuration": internetProfile_PriorityOptions_NoHighPrioPktDuration,
       "internetProfile-PriorityOptions-Enabled": internetProfile_PriorityOptions_Enabled,
       "mibinternetProfile-IpxOptions-IpxSapHsProxyNetTable": mibinternetProfile_IpxOptions_IpxSapHsProxyNetTable,
       "mibinternetProfile-IpxOptions-IpxSapHsProxyNetEntry": mibinternetProfile_IpxOptions_IpxSapHsProxyNetEntry,
       "internetProfile-IpxOptions-IpxSapHsProxyNet-Station": internetProfile_IpxOptions_IpxSapHsProxyNet_Station,
       "internetProfile-IpxOptions-IpxSapHsProxyNet-Index-o": internetProfile_IpxOptions_IpxSapHsProxyNet_Index_o,
       "internetProfile-IpxOptions-IpxSapHsProxyNet": internetProfile_IpxOptions_IpxSapHsProxyNet}
)

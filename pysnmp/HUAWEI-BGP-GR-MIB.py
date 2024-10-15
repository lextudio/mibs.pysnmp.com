# SNMP MIB module (HUAWEI-BGP-GR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BGP-GR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:54 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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

hwBgpGRMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Status(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )



class AFIType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              25,
              196)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 2),
          ("ipv6", 3),
          ("l2vpn", 196),
          ("notspecified", 1),
          ("vpls", 25))
    )



class SAFIType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              65,
              128)
        )
    )
    namedValues = NamedValues(
        *(("mpls", 5),
          ("multicast", 3),
          ("notspecified", 1),
          ("unicast", 2),
          ("unicastandmulticast", 4),
          ("vpls", 65),
          ("vpnv4", 128))
    )



class GRRole(Integer32, TextualConvention):
    status = "current"
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
        *(("grnegotiatefail", 4),
          ("grnormal", 1),
          ("helper", 3),
          ("restarter", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HwBgpGRMIBObjects_ObjectIdentity = ObjectIdentity
hwBgpGRMIBObjects = _HwBgpGRMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1)
)
_HwBgpGRCapability_Type = Status
_HwBgpGRCapability_Object = MibScalar
hwBgpGRCapability = _HwBgpGRCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 1),
    _HwBgpGRCapability_Type()
)
hwBgpGRCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBgpGRCapability.setStatus("current")


class _HwBgpGRRestartTime_Type(Integer32):
    """Custom type hwBgpGRRestartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 600),
    )


_HwBgpGRRestartTime_Type.__name__ = "Integer32"
_HwBgpGRRestartTime_Object = MibScalar
hwBgpGRRestartTime = _HwBgpGRRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 2),
    _HwBgpGRRestartTime_Type()
)
hwBgpGRRestartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBgpGRRestartTime.setStatus("current")


class _HwBgpGRWaitForRibTime_Type(Integer32):
    """Custom type hwBgpGRWaitForRibTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3000),
    )


_HwBgpGRWaitForRibTime_Type.__name__ = "Integer32"
_HwBgpGRWaitForRibTime_Object = MibScalar
hwBgpGRWaitForRibTime = _HwBgpGRWaitForRibTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 3),
    _HwBgpGRWaitForRibTime_Type()
)
hwBgpGRWaitForRibTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBgpGRWaitForRibTime.setStatus("current")
_HwBgpGRStatusInfoTable_Object = MibTable
hwBgpGRStatusInfoTable = _HwBgpGRStatusInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4)
)
if mibBuilder.loadTexts:
    hwBgpGRStatusInfoTable.setStatus("current")
_HwBgpGRStatusInfoEntry_Object = MibTableRow
hwBgpGRStatusInfoEntry = _HwBgpGRStatusInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4, 1)
)
hwBgpGRStatusInfoEntry.setIndexNames(
    (0, "HUAWEI-BGP-GR-MIB", "hwBgpGRStatAddressFamily"),
    (0, "HUAWEI-BGP-GR-MIB", "hwBgpGRStatSubAddressFamily"),
    (0, "HUAWEI-BGP-GR-MIB", "hwBgpGRStatInstanceID"),
    (0, "HUAWEI-BGP-GR-MIB", "hwBgpGRStatPeerAddress"),
)
if mibBuilder.loadTexts:
    hwBgpGRStatusInfoEntry.setStatus("current")
_HwBgpGRStatAddressFamily_Type = AFIType
_HwBgpGRStatAddressFamily_Object = MibTableColumn
hwBgpGRStatAddressFamily = _HwBgpGRStatAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4, 1, 1),
    _HwBgpGRStatAddressFamily_Type()
)
hwBgpGRStatAddressFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBgpGRStatAddressFamily.setStatus("current")
_HwBgpGRStatSubAddressFamily_Type = SAFIType
_HwBgpGRStatSubAddressFamily_Object = MibTableColumn
hwBgpGRStatSubAddressFamily = _HwBgpGRStatSubAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4, 1, 2),
    _HwBgpGRStatSubAddressFamily_Type()
)
hwBgpGRStatSubAddressFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBgpGRStatSubAddressFamily.setStatus("current")
_HwBgpGRStatInstanceID_Type = Unsigned32
_HwBgpGRStatInstanceID_Object = MibTableColumn
hwBgpGRStatInstanceID = _HwBgpGRStatInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4, 1, 3),
    _HwBgpGRStatInstanceID_Type()
)
hwBgpGRStatInstanceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBgpGRStatInstanceID.setStatus("current")
_HwBgpGRStatPeerAddress_Type = InetAddress
_HwBgpGRStatPeerAddress_Object = MibTableColumn
hwBgpGRStatPeerAddress = _HwBgpGRStatPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4, 1, 4),
    _HwBgpGRStatPeerAddress_Type()
)
hwBgpGRStatPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBgpGRStatPeerAddress.setStatus("current")
_HwBgpGRStatLocalGRRole_Type = GRRole
_HwBgpGRStatLocalGRRole_Object = MibTableColumn
hwBgpGRStatLocalGRRole = _HwBgpGRStatLocalGRRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4, 1, 5),
    _HwBgpGRStatLocalGRRole_Type()
)
hwBgpGRStatLocalGRRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpGRStatLocalGRRole.setStatus("current")
_HwBgpGRTrap_ObjectIdentity = ObjectIdentity
hwBgpGRTrap = _HwBgpGRTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 2)
)
_HwBgpGRMIBConformance_ObjectIdentity = ObjectIdentity
hwBgpGRMIBConformance = _HwBgpGRMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3)
)
_HwBgpGRMIBCompliances_ObjectIdentity = ObjectIdentity
hwBgpGRMIBCompliances = _HwBgpGRMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3, 1)
)
_HwBgpGRMIBGroups_ObjectIdentity = ObjectIdentity
hwBgpGRMIBGroups = _HwBgpGRMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3, 2)
)

# Managed Objects groups

hwBgpGRCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3, 2, 1)
)
hwBgpGRCfgGroup.setObjects(
      *(("HUAWEI-BGP-GR-MIB", "hwBgpGRRestartTime"),
        ("HUAWEI-BGP-GR-MIB", "hwBgpGRWaitForRibTime"),
        ("HUAWEI-BGP-GR-MIB", "hwBgpGRCapability"))
)
if mibBuilder.loadTexts:
    hwBgpGRCfgGroup.setStatus("current")

hwBgpGRStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3, 2, 2)
)
hwBgpGRStatGroup.setObjects(
    ("HUAWEI-BGP-GR-MIB", "hwBgpGRStatLocalGRRole")
)
if mibBuilder.loadTexts:
    hwBgpGRStatGroup.setStatus("current")


# Notification objects

hwBgpGRRestarterEnterGR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 2, 1)
)
hwBgpGRRestarterEnterGR.setObjects(
    ("HUAWEI-BGP-GR-MIB", "hwBgpGRStatLocalGRRole")
)
if mibBuilder.loadTexts:
    hwBgpGRRestarterEnterGR.setStatus(
        "current"
    )

hwBgpGRRestarterExitGR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 2, 2)
)
hwBgpGRRestarterExitGR.setObjects(
    ("HUAWEI-BGP-GR-MIB", "hwBgpGRStatLocalGRRole")
)
if mibBuilder.loadTexts:
    hwBgpGRRestarterExitGR.setStatus(
        "current"
    )

hwBgpGRHelperGRRestartTimeOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 2, 3)
)
hwBgpGRHelperGRRestartTimeOut.setObjects(
    ("HUAWEI-BGP-GR-MIB", "hwBgpGRStatLocalGRRole")
)
if mibBuilder.loadTexts:
    hwBgpGRHelperGRRestartTimeOut.setStatus(
        "current"
    )

hwBgpGRHelperGRWaitForEndofRibTimeOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 2, 4)
)
hwBgpGRHelperGRWaitForEndofRibTimeOut.setObjects(
    ("HUAWEI-BGP-GR-MIB", "hwBgpGRStatLocalGRRole")
)
if mibBuilder.loadTexts:
    hwBgpGRHelperGRWaitForEndofRibTimeOut.setStatus(
        "current"
    )


# Notifications groups

hwBgpGRTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3, 2, 3)
)
hwBgpGRTrapGroup.setObjects(
      *(("HUAWEI-BGP-GR-MIB", "hwBgpGRRestarterEnterGR"),
        ("HUAWEI-BGP-GR-MIB", "hwBgpGRRestarterExitGR"),
        ("HUAWEI-BGP-GR-MIB", "hwBgpGRHelperGRRestartTimeOut"),
        ("HUAWEI-BGP-GR-MIB", "hwBgpGRHelperGRWaitForEndofRibTimeOut"))
)
if mibBuilder.loadTexts:
    hwBgpGRTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwBgpGRMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwBgpGRMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BGP-GR-MIB",
    **{"Status": Status,
       "AFIType": AFIType,
       "SAFIType": SAFIType,
       "GRRole": GRRole,
       "hwBgpGRMIB": hwBgpGRMIB,
       "hwBgpGRMIBObjects": hwBgpGRMIBObjects,
       "hwBgpGRCapability": hwBgpGRCapability,
       "hwBgpGRRestartTime": hwBgpGRRestartTime,
       "hwBgpGRWaitForRibTime": hwBgpGRWaitForRibTime,
       "hwBgpGRStatusInfoTable": hwBgpGRStatusInfoTable,
       "hwBgpGRStatusInfoEntry": hwBgpGRStatusInfoEntry,
       "hwBgpGRStatAddressFamily": hwBgpGRStatAddressFamily,
       "hwBgpGRStatSubAddressFamily": hwBgpGRStatSubAddressFamily,
       "hwBgpGRStatInstanceID": hwBgpGRStatInstanceID,
       "hwBgpGRStatPeerAddress": hwBgpGRStatPeerAddress,
       "hwBgpGRStatLocalGRRole": hwBgpGRStatLocalGRRole,
       "hwBgpGRTrap": hwBgpGRTrap,
       "hwBgpGRRestarterEnterGR": hwBgpGRRestarterEnterGR,
       "hwBgpGRRestarterExitGR": hwBgpGRRestarterExitGR,
       "hwBgpGRHelperGRRestartTimeOut": hwBgpGRHelperGRRestartTimeOut,
       "hwBgpGRHelperGRWaitForEndofRibTimeOut": hwBgpGRHelperGRWaitForEndofRibTimeOut,
       "hwBgpGRMIBConformance": hwBgpGRMIBConformance,
       "hwBgpGRMIBCompliances": hwBgpGRMIBCompliances,
       "hwBgpGRMIBCompliance": hwBgpGRMIBCompliance,
       "hwBgpGRMIBGroups": hwBgpGRMIBGroups,
       "hwBgpGRCfgGroup": hwBgpGRCfgGroup,
       "hwBgpGRStatGroup": hwBgpGRStatGroup,
       "hwBgpGRTrapGroup": hwBgpGRTrapGroup}
)

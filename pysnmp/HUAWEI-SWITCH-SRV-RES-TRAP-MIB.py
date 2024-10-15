# SNMP MIB module (HUAWEI-SWITCH-SRV-RES-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SWITCH-SRV-RES-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:05 2024
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

hwSwitchSrvResTrapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 334)
)
hwSwitchSrvResTrapMIB.setRevisions(
        ("2014-08-06 08:58",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSrvResTrapObject_ObjectIdentity = ObjectIdentity
hwSrvResTrapObject = _HwSrvResTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 1)
)


class _HwSrvServiceId_Type(Integer32):
    """Custom type hwSrvServiceId based on Integer32"""
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
        *(("dldpInterface", 2),
          ("gvrpInterface", 1),
          ("igmpSnoopingQuerier", 3),
          ("multicastUserVlan", 4),
          ("portSecMac", 5),
          ("sflowInterface", 7),
          ("stormControlInterface", 6))
    )


_HwSrvServiceId_Type.__name__ = "Integer32"
_HwSrvServiceId_Object = MibScalar
hwSrvServiceId = _HwSrvServiceId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 1, 1),
    _HwSrvServiceId_Type()
)
hwSrvServiceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSrvServiceId.setStatus("current")


class _HwSrvServiceDescr_Type(OctetString):
    """Custom type hwSrvServiceDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwSrvServiceDescr_Type.__name__ = "OctetString"
_HwSrvServiceDescr_Object = MibScalar
hwSrvServiceDescr = _HwSrvServiceDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 1, 2),
    _HwSrvServiceDescr_Type()
)
hwSrvServiceDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSrvServiceDescr.setStatus("current")
_HwSrvRecommendThreshold_Type = Unsigned32
_HwSrvRecommendThreshold_Object = MibScalar
hwSrvRecommendThreshold = _HwSrvRecommendThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 1, 3),
    _HwSrvRecommendThreshold_Type()
)
hwSrvRecommendThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSrvRecommendThreshold.setStatus("current")
_HwSrvResTraps_ObjectIdentity = ObjectIdentity
hwSrvResTraps = _HwSrvResTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 2)
)
_HwSrvSeviceResTrap_ObjectIdentity = ObjectIdentity
hwSrvSeviceResTrap = _HwSrvSeviceResTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 2, 1)
)
_HwSrvResTrapConformance_ObjectIdentity = ObjectIdentity
hwSrvResTrapConformance = _HwSrvResTrapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 100)
)
_HwSrvResTrapCompliances_ObjectIdentity = ObjectIdentity
hwSrvResTrapCompliances = _HwSrvResTrapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 100, 1)
)
_HwSrvResTrapGroups_ObjectIdentity = ObjectIdentity
hwSrvResTrapGroups = _HwSrvResTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 100, 2)
)

# Managed Objects groups

hwSrvResObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 100, 2, 1)
)
hwSrvResObjectGroup.setObjects(
      *(("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceId"),
        ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceDescr"),
        ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvRecommendThreshold"))
)
if mibBuilder.loadTexts:
    hwSrvResObjectGroup.setStatus("current")


# Notification objects

hwSrvServiceExceedThreshould = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 2, 1, 1)
)
hwSrvServiceExceedThreshould.setObjects(
      *(("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceId"),
        ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceDescr"),
        ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvRecommendThreshold"))
)
if mibBuilder.loadTexts:
    hwSrvServiceExceedThreshould.setStatus(
        "current"
    )

hwSrvServiceExceedThreshouldResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 2, 1, 2)
)
hwSrvServiceExceedThreshouldResume.setObjects(
      *(("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceId"),
        ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceDescr"),
        ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvRecommendThreshold"))
)
if mibBuilder.loadTexts:
    hwSrvServiceExceedThreshouldResume.setStatus(
        "current"
    )


# Notifications groups

hwSrvResTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 100, 2, 2)
)
hwSrvResTrapGroup.setObjects(
      *(("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceExceedThreshould"),
        ("HUAWEI-SWITCH-SRV-RES-TRAP-MIB", "hwSrvServiceExceedThreshouldResume"))
)
if mibBuilder.loadTexts:
    hwSrvResTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwSrvResTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 334, 100, 1, 1)
)
if mibBuilder.loadTexts:
    hwSrvResTrapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SWITCH-SRV-RES-TRAP-MIB",
    **{"hwSwitchSrvResTrapMIB": hwSwitchSrvResTrapMIB,
       "hwSrvResTrapObject": hwSrvResTrapObject,
       "hwSrvServiceId": hwSrvServiceId,
       "hwSrvServiceDescr": hwSrvServiceDescr,
       "hwSrvRecommendThreshold": hwSrvRecommendThreshold,
       "hwSrvResTraps": hwSrvResTraps,
       "hwSrvSeviceResTrap": hwSrvSeviceResTrap,
       "hwSrvServiceExceedThreshould": hwSrvServiceExceedThreshould,
       "hwSrvServiceExceedThreshouldResume": hwSrvServiceExceedThreshouldResume,
       "hwSrvResTrapConformance": hwSrvResTrapConformance,
       "hwSrvResTrapCompliances": hwSrvResTrapCompliances,
       "hwSrvResTrapCompliance": hwSrvResTrapCompliance,
       "hwSrvResTrapGroups": hwSrvResTrapGroups,
       "hwSrvResObjectGroup": hwSrvResObjectGroup,
       "hwSrvResTrapGroup": hwSrvResTrapGroup}
)

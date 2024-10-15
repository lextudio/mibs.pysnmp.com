# SNMP MIB module (HUAWEI-RPR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-RPR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:46 2024
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

(RprSpan,
 rprIfCurrentStatus,
 rprIfIndex,
 rprIfRingOperModes,
 rprIfWrapConfig,
 rprSpanId,
 rprSpanIfIndex,
 rprSpanTotalRingletReservedRate,
 rprTopoImageEastProtectionStatus,
 rprTopoImageIfIndex,
 rprTopoImageMacAddress,
 rprTopoImageRinglet0Hops,
 rprTopoImageRinglet1Hops,
 rprTopoImageStationIfIndex,
 rprTopoImageStatus,
 rprTopoImageWestProtectionStatus) = mibBuilder.importSymbols(
    "IEEE-802DOT17-RPR-MIB",
    "RprSpan",
    "rprIfCurrentStatus",
    "rprIfIndex",
    "rprIfRingOperModes",
    "rprIfWrapConfig",
    "rprSpanId",
    "rprSpanIfIndex",
    "rprSpanTotalRingletReservedRate",
    "rprTopoImageEastProtectionStatus",
    "rprTopoImageIfIndex",
    "rprTopoImageMacAddress",
    "rprTopoImageRinglet0Hops",
    "rprTopoImageRinglet1Hops",
    "rprTopoImageStationIfIndex",
    "rprTopoImageStatus",
    "rprTopoImageWestProtectionStatus")

(InterfaceIndex,
 ifIndex,
 ifName,
 ifPhysAddress) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex",
    "ifName",
    "ifPhysAddress")

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

hwRPR = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwRPRObjects_ObjectIdentity = ObjectIdentity
hwRPRObjects = _HwRPRObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1)
)
_HwRPRIfEventTable_Object = MibTable
hwRPRIfEventTable = _HwRPRIfEventTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 1)
)
if mibBuilder.loadTexts:
    hwRPRIfEventTable.setStatus("current")
_HwRPRIfEventEntry_Object = MibTableRow
hwRPRIfEventEntry = _HwRPRIfEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 1, 1)
)
hwRPRIfEventEntry.setIndexNames(
    (0, "HUAWEI-RPR-MIB", "hwRPRLogicIfIndex"),
    (0, "HUAWEI-RPR-MIB", "hwRPRLogicIfSpanId"),
)
if mibBuilder.loadTexts:
    hwRPRIfEventEntry.setStatus("current")
_HwRPRLogicIfIndex_Type = InterfaceIndex
_HwRPRLogicIfIndex_Object = MibTableColumn
hwRPRLogicIfIndex = _HwRPRLogicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 1, 1, 1),
    _HwRPRLogicIfIndex_Type()
)
hwRPRLogicIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRPRLogicIfIndex.setStatus("current")
_HwRPRLogicIfSpanId_Type = RprSpan
_HwRPRLogicIfSpanId_Object = MibTableColumn
hwRPRLogicIfSpanId = _HwRPRLogicIfSpanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 1, 1, 2),
    _HwRPRLogicIfSpanId_Type()
)
hwRPRLogicIfSpanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRPRLogicIfSpanId.setStatus("current")


class _HwRPRLogicIfEvent_Type(Integer32):
    """Custom type hwRPRLogicIfEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mateerr", 3),
          ("sd", 1),
          ("sf", 2))
    )


_HwRPRLogicIfEvent_Type.__name__ = "Integer32"
_HwRPRLogicIfEvent_Object = MibTableColumn
hwRPRLogicIfEvent = _HwRPRLogicIfEvent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 1, 1, 3),
    _HwRPRLogicIfEvent_Type()
)
hwRPRLogicIfEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRPRLogicIfEvent.setStatus("current")


class _HwRPRPhyIfEvent_Type(Integer32):
    """Custom type hwRPRPhyIfEvent based on Integer32"""
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
        *(("keepalive", 9),
          ("mateState", 10),
          ("miscabling", 8),
          ("sdHFramerAISst", 6),
          ("sdHFramerLOFst", 4),
          ("sdHFramerLOSst", 3),
          ("sdHFramerRDIst", 5),
          ("sdHFramerREIst", 7),
          ("sdHFramerSDst", 1),
          ("sdHFramerSFst", 2))
    )


_HwRPRPhyIfEvent_Type.__name__ = "Integer32"
_HwRPRPhyIfEvent_Object = MibTableColumn
hwRPRPhyIfEvent = _HwRPRPhyIfEvent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 1, 1, 4),
    _HwRPRPhyIfEvent_Type()
)
hwRPRPhyIfEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRPRPhyIfEvent.setStatus("current")
_HwRPRIfConfigTable_Object = MibTable
hwRPRIfConfigTable = _HwRPRIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 2)
)
if mibBuilder.loadTexts:
    hwRPRIfConfigTable.setStatus("current")
_HwRPRIfConfigEntry_Object = MibTableRow
hwRPRIfConfigEntry = _HwRPRIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 2, 1)
)
hwRPRIfConfigEntry.setIndexNames(
    (0, "HUAWEI-RPR-MIB", "hwRPRIfConfigIfIndex"),
)
if mibBuilder.loadTexts:
    hwRPRIfConfigEntry.setStatus("current")
_HwRPRIfConfigIfIndex_Type = InterfaceIndex
_HwRPRIfConfigIfIndex_Object = MibTableColumn
hwRPRIfConfigIfIndex = _HwRPRIfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 2, 1, 1),
    _HwRPRIfConfigIfIndex_Type()
)
hwRPRIfConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRPRIfConfigIfIndex.setStatus("current")


class _HwRPRLogicIfTotalBandWidth_Type(Integer32):
    """Custom type hwRPRLogicIfTotalBandWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1000,
              2488,
              10000)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth1000", 1000),
          ("bandwidth10000", 10000),
          ("bandwidth2488", 2488))
    )


_HwRPRLogicIfTotalBandWidth_Type.__name__ = "Integer32"
_HwRPRLogicIfTotalBandWidth_Object = MibTableColumn
hwRPRLogicIfTotalBandWidth = _HwRPRLogicIfTotalBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 1, 2, 1, 2),
    _HwRPRLogicIfTotalBandWidth_Type()
)
hwRPRLogicIfTotalBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRPRLogicIfTotalBandWidth.setStatus("current")
_HwRPRTraps_ObjectIdentity = ObjectIdentity
hwRPRTraps = _HwRPRTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2)
)
_HwRPRTrapConformance_ObjectIdentity = ObjectIdentity
hwRPRTrapConformance = _HwRPRTrapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 3)
)
_HwRPRTrapCompliances_ObjectIdentity = ObjectIdentity
hwRPRTrapCompliances = _HwRPRTrapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 3, 1)
)
_HwRPRTrapGroups_ObjectIdentity = ObjectIdentity
hwRPRTrapGroups = _HwRPRTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 3, 2)
)

# Managed Objects groups

hwRPRIfEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 3, 2, 1)
)
hwRPRIfEventGroup.setObjects(
      *(("HUAWEI-RPR-MIB", "hwRPRLogicIfIndex"),
        ("HUAWEI-RPR-MIB", "hwRPRLogicIfSpanId"),
        ("HUAWEI-RPR-MIB", "hwRPRPhyIfEvent"),
        ("HUAWEI-RPR-MIB", "hwRPRLogicIfEvent"))
)
if mibBuilder.loadTexts:
    hwRPRIfEventGroup.setStatus("current")

hwRPRIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 3, 2, 3)
)
hwRPRIfConfigGroup.setObjects(
    ("HUAWEI-RPR-MIB", "hwRPRLogicIfTotalBandWidth")
)
if mibBuilder.loadTexts:
    hwRPRIfConfigGroup.setStatus("current")


# Notification objects

hwRPRexcessReservedRateDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 1)
)
hwRPRexcessReservedRateDefect.setObjects(
    ("IEEE-802DOT17-RPR-MIB", "rprSpanTotalRingletReservedRate")
)
if mibBuilder.loadTexts:
    hwRPRexcessReservedRateDefect.setStatus(
        "current"
    )

hwRPRprotMisconfigDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 2)
)
hwRPRprotMisconfigDefect.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprIfWrapConfig"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfRingOperModes"))
)
if mibBuilder.loadTexts:
    hwRPRprotMisconfigDefect.setStatus(
        "current"
    )

hwRPRtopoChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 3)
)
hwRPRtopoChange.setObjects(
      *(("IEEE-802DOT17-RPR-MIB", "rprTopoImageStationIfIndex"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageStatus"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageWestProtectionStatus"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageEastProtectionStatus"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfCurrentStatus"))
)
if mibBuilder.loadTexts:
    hwRPRtopoChange.setStatus(
        "current"
    )

hwRPRtopoInvalidDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 4)
)
hwRPRtopoInvalidDefect.setObjects(
      *(("IF-MIB", "ifPhysAddress"),
        ("IEEE-802DOT17-RPR-MIB", "rprIfCurrentStatus"))
)
if mibBuilder.loadTexts:
    hwRPRtopoInvalidDefect.setStatus(
        "current"
    )

hwRPRduplicateMacAddressDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 5)
)
hwRPRduplicateMacAddressDefect.setObjects(
      *(("IF-MIB", "ifPhysAddress"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageRinglet0Hops"),
        ("IEEE-802DOT17-RPR-MIB", "rprTopoImageRinglet1Hops"))
)
if mibBuilder.loadTexts:
    hwRPRduplicateMacAddressDefect.setStatus(
        "current"
    )

hwRPRtopoInstabilityDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 6)
)
hwRPRtopoInstabilityDefect.setObjects(
    ("IF-MIB", "ifPhysAddress")
)
if mibBuilder.loadTexts:
    hwRPRtopoInstabilityDefect.setStatus(
        "current"
    )

hwRPRtopoStabilityRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 7)
)
hwRPRtopoStabilityRestore.setObjects(
    ("IF-MIB", "ifPhysAddress")
)
if mibBuilder.loadTexts:
    hwRPRtopoStabilityRestore.setStatus(
        "current"
    )

hwRPRPhyIfEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 8)
)
hwRPRPhyIfEventTrap.setObjects(
      *(("HUAWEI-RPR-MIB", "hwRPRLogicIfIndex"),
        ("HUAWEI-RPR-MIB", "hwRPRLogicIfSpanId"),
        ("HUAWEI-RPR-MIB", "hwRPRPhyIfEvent"))
)
if mibBuilder.loadTexts:
    hwRPRPhyIfEventTrap.setStatus(
        "current"
    )

hwRPRLogicIfEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 9)
)
hwRPRLogicIfEventTrap.setObjects(
      *(("HUAWEI-RPR-MIB", "hwRPRLogicIfIndex"),
        ("HUAWEI-RPR-MIB", "hwRPRLogicIfSpanId"),
        ("HUAWEI-RPR-MIB", "hwRPRLogicIfEvent"))
)
if mibBuilder.loadTexts:
    hwRPRLogicIfEventTrap.setStatus(
        "current"
    )

hwRPRNodeConErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 10)
)
hwRPRNodeConErr.setObjects(
    ("IF-MIB", "ifName")
)
if mibBuilder.loadTexts:
    hwRPRNodeConErr.setStatus(
        "current"
    )

hwRPRNodeConErrResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 11)
)
hwRPRNodeConErrResume.setObjects(
    ("IF-MIB", "ifName")
)
if mibBuilder.loadTexts:
    hwRPRNodeConErrResume.setStatus(
        "current"
    )

hwRPRNodeMisCabling = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 12)
)
hwRPRNodeMisCabling.setObjects(
    ("IF-MIB", "ifName")
)
if mibBuilder.loadTexts:
    hwRPRNodeMisCabling.setStatus(
        "current"
    )

hwRPRNodeMisCablingResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 13)
)
hwRPRNodeMisCablingResume.setObjects(
    ("IF-MIB", "ifName")
)
if mibBuilder.loadTexts:
    hwRPRNodeMisCablingResume.setStatus(
        "current"
    )

hwRPRMateErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 14)
)
hwRPRMateErr.setObjects(
    ("IF-MIB", "ifName")
)
if mibBuilder.loadTexts:
    hwRPRMateErr.setStatus(
        "current"
    )

hwRPRMateErrResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 15)
)
hwRPRMateErrResume.setObjects(
    ("IF-MIB", "ifName")
)
if mibBuilder.loadTexts:
    hwRPRMateErrResume.setStatus(
        "current"
    )

hwRPRLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 16)
)
hwRPRLOS.setObjects(
    ("IF-MIB", "ifName")
)
if mibBuilder.loadTexts:
    hwRPRLOS.setStatus(
        "current"
    )

hwRPRLOSResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 2, 17)
)
hwRPRLOSResume.setObjects(
    ("IF-MIB", "ifName")
)
if mibBuilder.loadTexts:
    hwRPRLOSResume.setStatus(
        "current"
    )


# Notifications groups

hwRPRTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 3, 2, 2)
)
hwRPRTrapGroup.setObjects(
      *(("HUAWEI-RPR-MIB", "hwRPRexcessReservedRateDefect"),
        ("HUAWEI-RPR-MIB", "hwRPRprotMisconfigDefect"),
        ("HUAWEI-RPR-MIB", "hwRPRtopoChange"),
        ("HUAWEI-RPR-MIB", "hwRPRtopoInvalidDefect"),
        ("HUAWEI-RPR-MIB", "hwRPRduplicateMacAddressDefect"),
        ("HUAWEI-RPR-MIB", "hwRPRtopoInstabilityDefect"),
        ("HUAWEI-RPR-MIB", "hwRPRtopoStabilityRestore"),
        ("HUAWEI-RPR-MIB", "hwRPRPhyIfEventTrap"),
        ("HUAWEI-RPR-MIB", "hwRPRLogicIfEventTrap"),
        ("HUAWEI-RPR-MIB", "hwRPRNodeConErr"),
        ("HUAWEI-RPR-MIB", "hwRPRNodeConErrResume"),
        ("HUAWEI-RPR-MIB", "hwRPRNodeMisCabling"),
        ("HUAWEI-RPR-MIB", "hwRPRNodeMisCablingResume"),
        ("HUAWEI-RPR-MIB", "hwRPRMateErr"),
        ("HUAWEI-RPR-MIB", "hwRPRMateErrResume"),
        ("HUAWEI-RPR-MIB", "hwRPRLOS"),
        ("HUAWEI-RPR-MIB", "hwRPRLOSResume"))
)
if mibBuilder.loadTexts:
    hwRPRTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwRPRTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 36, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwRPRTrapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-RPR-MIB",
    **{"hwRPR": hwRPR,
       "hwRPRObjects": hwRPRObjects,
       "hwRPRIfEventTable": hwRPRIfEventTable,
       "hwRPRIfEventEntry": hwRPRIfEventEntry,
       "hwRPRLogicIfIndex": hwRPRLogicIfIndex,
       "hwRPRLogicIfSpanId": hwRPRLogicIfSpanId,
       "hwRPRLogicIfEvent": hwRPRLogicIfEvent,
       "hwRPRPhyIfEvent": hwRPRPhyIfEvent,
       "hwRPRIfConfigTable": hwRPRIfConfigTable,
       "hwRPRIfConfigEntry": hwRPRIfConfigEntry,
       "hwRPRIfConfigIfIndex": hwRPRIfConfigIfIndex,
       "hwRPRLogicIfTotalBandWidth": hwRPRLogicIfTotalBandWidth,
       "hwRPRTraps": hwRPRTraps,
       "hwRPRexcessReservedRateDefect": hwRPRexcessReservedRateDefect,
       "hwRPRprotMisconfigDefect": hwRPRprotMisconfigDefect,
       "hwRPRtopoChange": hwRPRtopoChange,
       "hwRPRtopoInvalidDefect": hwRPRtopoInvalidDefect,
       "hwRPRduplicateMacAddressDefect": hwRPRduplicateMacAddressDefect,
       "hwRPRtopoInstabilityDefect": hwRPRtopoInstabilityDefect,
       "hwRPRtopoStabilityRestore": hwRPRtopoStabilityRestore,
       "hwRPRPhyIfEventTrap": hwRPRPhyIfEventTrap,
       "hwRPRLogicIfEventTrap": hwRPRLogicIfEventTrap,
       "hwRPRNodeConErr": hwRPRNodeConErr,
       "hwRPRNodeConErrResume": hwRPRNodeConErrResume,
       "hwRPRNodeMisCabling": hwRPRNodeMisCabling,
       "hwRPRNodeMisCablingResume": hwRPRNodeMisCablingResume,
       "hwRPRMateErr": hwRPRMateErr,
       "hwRPRMateErrResume": hwRPRMateErrResume,
       "hwRPRLOS": hwRPRLOS,
       "hwRPRLOSResume": hwRPRLOSResume,
       "hwRPRTrapConformance": hwRPRTrapConformance,
       "hwRPRTrapCompliances": hwRPRTrapCompliances,
       "hwRPRTrapCompliance": hwRPRTrapCompliance,
       "hwRPRTrapGroups": hwRPRTrapGroups,
       "hwRPRIfEventGroup": hwRPRIfEventGroup,
       "hwRPRTrapGroup": hwRPRTrapGroup,
       "hwRPRIfConfigGroup": hwRPRIfConfigGroup}
)

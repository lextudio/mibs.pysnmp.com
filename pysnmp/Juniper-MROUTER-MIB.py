# SNMP MIB module (Juniper-MROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-MROUTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:49 2024
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

(IANAipMRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipMRouteProtocol")

(ipMRouteEntry,
 ipMRouteInterfaceEntry) = mibBuilder.importSymbols(
    "IPMROUTE-STD-MIB",
    "ipMRouteEntry",
    "ipMRouteInterfaceEntry")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniInterfaceLocationType,
 JuniInterfaceLocationValue) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniInterfaceLocationType",
    "JuniInterfaceLocationValue")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

juniMRouterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65)
)
juniMRouterMIB.setRevisions(
        ("2006-09-18 08:09",
         "2006-09-02 11:02",
         "2006-06-15 10:13",
         "2002-10-28 20:06")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniMRouterMIBObject_ObjectIdentity = ObjectIdentity
juniMRouterMIBObject = _JuniMRouterMIBObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1)
)
_JuniMcastTraps_ObjectIdentity = ObjectIdentity
juniMcastTraps = _JuniMcastTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 1)
)
_JuniMcastObjects_ObjectIdentity = ObjectIdentity
juniMcastObjects = _JuniMcastObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2)
)
_JuniMcastRpfRouteTable_Object = MibTable
juniMcastRpfRouteTable = _JuniMcastRpfRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 1)
)
if mibBuilder.loadTexts:
    juniMcastRpfRouteTable.setStatus("current")
_JuniMcastRpfRouteEntry_Object = MibTableRow
juniMcastRpfRouteEntry = _JuniMcastRpfRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 1, 1)
)
juniMcastRpfRouteEntry.setIndexNames(
    (0, "Juniper-MROUTER-MIB", "juniMcastRouteStaticDest"),
    (0, "Juniper-MROUTER-MIB", "juniMcastRouteStaticMask"),
)
if mibBuilder.loadTexts:
    juniMcastRpfRouteEntry.setStatus("current")
_JuniMcastRouteStaticDest_Type = IpAddress
_JuniMcastRouteStaticDest_Object = MibTableColumn
juniMcastRouteStaticDest = _JuniMcastRouteStaticDest_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 1, 1, 1),
    _JuniMcastRouteStaticDest_Type()
)
juniMcastRouteStaticDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMcastRouteStaticDest.setStatus("current")
_JuniMcastRouteStaticMask_Type = IpAddress
_JuniMcastRouteStaticMask_Object = MibTableColumn
juniMcastRouteStaticMask = _JuniMcastRouteStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 1, 1, 2),
    _JuniMcastRouteStaticMask_Type()
)
juniMcastRouteStaticMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMcastRouteStaticMask.setStatus("current")


class _JuniMcastRouteStaticRtPreference_Type(Integer32):
    """Custom type juniMcastRouteStaticRtPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniMcastRouteStaticRtPreference_Type.__name__ = "Integer32"
_JuniMcastRouteStaticRtPreference_Object = MibTableColumn
juniMcastRouteStaticRtPreference = _JuniMcastRouteStaticRtPreference_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 1, 1, 3),
    _JuniMcastRouteStaticRtPreference_Type()
)
juniMcastRouteStaticRtPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMcastRouteStaticRtPreference.setStatus("current")
_JuniMcastRouteStaticRpfHop_Type = IpAddress
_JuniMcastRouteStaticRpfHop_Object = MibTableColumn
juniMcastRouteStaticRpfHop = _JuniMcastRouteStaticRpfHop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 1, 1, 4),
    _JuniMcastRouteStaticRpfHop_Type()
)
juniMcastRouteStaticRpfHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMcastRouteStaticRpfHop.setStatus("current")
_JuniMcastRouteStaticTag_Type = Unsigned32
_JuniMcastRouteStaticTag_Object = MibTableColumn
juniMcastRouteStaticTag = _JuniMcastRouteStaticTag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 1, 1, 5),
    _JuniMcastRouteStaticTag_Type()
)
juniMcastRouteStaticTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMcastRouteStaticTag.setStatus("current")
_JuniMcastRouteStaticRowStatus_Type = RowStatus
_JuniMcastRouteStaticRowStatus_Object = MibTableColumn
juniMcastRouteStaticRowStatus = _JuniMcastRouteStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 1, 1, 6),
    _JuniMcastRouteStaticRowStatus_Type()
)
juniMcastRouteStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMcastRouteStaticRowStatus.setStatus("current")
_JuniMRouteTable_Object = MibTable
juniMRouteTable = _JuniMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 2)
)
if mibBuilder.loadTexts:
    juniMRouteTable.setStatus("current")
_JuniMRouteEntry_Object = MibTableRow
juniMRouteEntry = _JuniMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    juniMRouteEntry.setStatus("current")
_JuniMRouteAdmBwAdaptive_Type = TruthValue
_JuniMRouteAdmBwAdaptive_Object = MibTableColumn
juniMRouteAdmBwAdaptive = _JuniMRouteAdmBwAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 2, 1, 1),
    _JuniMRouteAdmBwAdaptive_Type()
)
juniMRouteAdmBwAdaptive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMRouteAdmBwAdaptive.setStatus("current")
_JuniMRouteAdmBw_Type = Integer32
_JuniMRouteAdmBw_Object = MibTableColumn
juniMRouteAdmBw = _JuniMRouteAdmBw_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 2, 1, 2),
    _JuniMRouteAdmBw_Type()
)
juniMRouteAdmBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMRouteAdmBw.setStatus("current")
_JuniMRouteQosBwAdaptive_Type = TruthValue
_JuniMRouteQosBwAdaptive_Object = MibTableColumn
juniMRouteQosBwAdaptive = _JuniMRouteQosBwAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 2, 1, 3),
    _JuniMRouteQosBwAdaptive_Type()
)
juniMRouteQosBwAdaptive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMRouteQosBwAdaptive.setStatus("current")
_JuniMRouteQosBw_Type = Integer32
_JuniMRouteQosBw_Object = MibTableColumn
juniMRouteQosBw = _JuniMRouteQosBw_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 2, 1, 4),
    _JuniMRouteQosBw_Type()
)
juniMRouteQosBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMRouteQosBw.setStatus("current")
_JuniMRouteIsEcmp_Type = TruthValue
_JuniMRouteIsEcmp_Object = MibTableColumn
juniMRouteIsEcmp = _JuniMRouteIsEcmp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 2, 1, 5),
    _JuniMRouteIsEcmp_Type()
)
juniMRouteIsEcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMRouteIsEcmp.setStatus("current")
_JuniMRouteRpfDisabled_Type = TruthValue
_JuniMRouteRpfDisabled_Object = MibTableColumn
juniMRouteRpfDisabled = _JuniMRouteRpfDisabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 2, 1, 6),
    _JuniMRouteRpfDisabled_Type()
)
juniMRouteRpfDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMRouteRpfDisabled.setStatus("current")
_JuniMRouteOwnerProtoType_Type = IANAipMRouteProtocol
_JuniMRouteOwnerProtoType_Object = MibTableColumn
juniMRouteOwnerProtoType = _JuniMRouteOwnerProtoType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 2, 1, 7),
    _JuniMRouteOwnerProtoType_Type()
)
juniMRouteOwnerProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMRouteOwnerProtoType.setStatus("current")
_JuniMRoutePktFwd_Type = Counter64
_JuniMRoutePktFwd_Object = MibTableColumn
juniMRoutePktFwd = _JuniMRoutePktFwd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 2, 1, 8),
    _JuniMRoutePktFwd_Type()
)
juniMRoutePktFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMRoutePktFwd.setStatus("current")
_JuniMRouteOifCnt_Type = Integer32
_JuniMRouteOifCnt_Object = MibTableColumn
juniMRouteOifCnt = _JuniMRouteOifCnt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 2, 1, 9),
    _JuniMRouteOifCnt_Type()
)
juniMRouteOifCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMRouteOifCnt.setStatus("current")


class _JuniMcastRpfDisable_Type(DisplayString):
    """Custom type juniMcastRpfDisable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniMcastRpfDisable_Type.__name__ = "DisplayString"
_JuniMcastRpfDisable_Object = MibScalar
juniMcastRpfDisable = _JuniMcastRpfDisable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 3),
    _JuniMcastRpfDisable_Type()
)
juniMcastRpfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMcastRpfDisable.setStatus("current")
_JuniMRouteInterfaceTable_Object = MibTable
juniMRouteInterfaceTable = _JuniMRouteInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 4)
)
if mibBuilder.loadTexts:
    juniMRouteInterfaceTable.setStatus("current")
_JuniMRouteInterfaceEntry_Object = MibTableRow
juniMRouteInterfaceEntry = _JuniMRouteInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    juniMRouteInterfaceEntry.setStatus("current")


class _JuniMRouteInterfaceActiveGroups_Type(Integer32):
    """Custom type juniMRouteInterfaceActiveGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_JuniMRouteInterfaceActiveGroups_Type.__name__ = "Integer32"
_JuniMRouteInterfaceActiveGroups_Object = MibTableColumn
juniMRouteInterfaceActiveGroups = _JuniMRouteInterfaceActiveGroups_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 4, 1, 1),
    _JuniMRouteInterfaceActiveGroups_Type()
)
juniMRouteInterfaceActiveGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMRouteInterfaceActiveGroups.setStatus("current")


class _JuniMRouteInterfaceBlockedGroups_Type(Integer32):
    """Custom type juniMRouteInterfaceBlockedGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_JuniMRouteInterfaceBlockedGroups_Type.__name__ = "Integer32"
_JuniMRouteInterfaceBlockedGroups_Object = MibTableColumn
juniMRouteInterfaceBlockedGroups = _JuniMRouteInterfaceBlockedGroups_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 4, 1, 2),
    _JuniMRouteInterfaceBlockedGroups_Type()
)
juniMRouteInterfaceBlockedGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMRouteInterfaceBlockedGroups.setStatus("current")
_JuniMroutePortLocationType_Type = JuniInterfaceLocationType
_JuniMroutePortLocationType_Object = MibScalar
juniMroutePortLocationType = _JuniMroutePortLocationType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 5),
    _JuniMroutePortLocationType_Type()
)
juniMroutePortLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMroutePortLocationType.setStatus("current")
_JuniMRoutePortTable_Object = MibTable
juniMRoutePortTable = _JuniMRoutePortTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 6)
)
if mibBuilder.loadTexts:
    juniMRoutePortTable.setStatus("current")
_JuniMRoutePortEntry_Object = MibTableRow
juniMRoutePortEntry = _JuniMRoutePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 6, 1)
)
juniMRoutePortEntry.setIndexNames(
    (0, "Juniper-MROUTER-MIB", "juniMRoutePortLocationIndex"),
)
if mibBuilder.loadTexts:
    juniMRoutePortEntry.setStatus("current")
_JuniMRoutePortLocationIndex_Type = JuniInterfaceLocationValue
_JuniMRoutePortLocationIndex_Object = MibTableColumn
juniMRoutePortLocationIndex = _JuniMRoutePortLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 6, 1, 1),
    _JuniMRoutePortLocationIndex_Type()
)
juniMRoutePortLocationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMRoutePortLocationIndex.setStatus("current")


class _JuniMRoutePortMaxBw_Type(Integer32):
    """Custom type juniMRoutePortMaxBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniMRoutePortMaxBw_Type.__name__ = "Integer32"
_JuniMRoutePortMaxBw_Object = MibTableColumn
juniMRoutePortMaxBw = _JuniMRoutePortMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 6, 1, 2),
    _JuniMRoutePortMaxBw_Type()
)
juniMRoutePortMaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMRoutePortMaxBw.setStatus("current")


class _JuniMRoutePortPriorityBw_Type(Integer32):
    """Custom type juniMRoutePortPriorityBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniMRoutePortPriorityBw_Type.__name__ = "Integer32"
_JuniMRoutePortPriorityBw_Object = MibTableColumn
juniMRoutePortPriorityBw = _JuniMRoutePortPriorityBw_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 6, 1, 3),
    _JuniMRoutePortPriorityBw_Type()
)
juniMRoutePortPriorityBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMRoutePortPriorityBw.setStatus("current")


class _JuniMRoutePortHysteresis_Type(Integer32):
    """Custom type juniMRoutePortHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_JuniMRoutePortHysteresis_Type.__name__ = "Integer32"
_JuniMRoutePortHysteresis_Object = MibTableColumn
juniMRoutePortHysteresis = _JuniMRoutePortHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 6, 1, 4),
    _JuniMRoutePortHysteresis_Type()
)
juniMRoutePortHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMRoutePortHysteresis.setStatus("current")


class _JuniMRoutePortAdmittedBw_Type(Integer32):
    """Custom type juniMRoutePortAdmittedBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniMRoutePortAdmittedBw_Type.__name__ = "Integer32"
_JuniMRoutePortAdmittedBw_Object = MibTableColumn
juniMRoutePortAdmittedBw = _JuniMRoutePortAdmittedBw_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 6, 1, 5),
    _JuniMRoutePortAdmittedBw_Type()
)
juniMRoutePortAdmittedBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMRoutePortAdmittedBw.setStatus("current")


class _JuniMRoutePortSGCount_Type(Integer32):
    """Custom type juniMRoutePortSGCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniMRoutePortSGCount_Type.__name__ = "Integer32"
_JuniMRoutePortSGCount_Object = MibTableColumn
juniMRoutePortSGCount = _JuniMRoutePortSGCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 6, 1, 6),
    _JuniMRoutePortSGCount_Type()
)
juniMRoutePortSGCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMRoutePortSGCount.setStatus("current")


class _JuniMRoutePortLimit_Type(Integer32):
    """Custom type juniMRoutePortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniMRoutePortLimit_Type.__name__ = "Integer32"
_JuniMRoutePortLimit_Object = MibTableColumn
juniMRoutePortLimit = _JuniMRoutePortLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 2, 6, 1, 7),
    _JuniMRoutePortLimit_Type()
)
juniMRoutePortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMRoutePortLimit.setStatus("current")
_JuniMcastNotifyObject_ObjectIdentity = ObjectIdentity
juniMcastNotifyObject = _JuniMcastNotifyObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 3)
)
_JuniMcastNotificationObjects_ObjectIdentity = ObjectIdentity
juniMcastNotificationObjects = _JuniMcastNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 3, 1)
)
_JuniMRouteIfLocIndex_Type = JuniInterfaceLocationValue
_JuniMRouteIfLocIndex_Object = MibScalar
juniMRouteIfLocIndex = _JuniMRouteIfLocIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 3, 1, 1),
    _JuniMRouteIfLocIndex_Type()
)
juniMRouteIfLocIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniMRouteIfLocIndex.setStatus("current")
_JuniMcastConformance_ObjectIdentity = ObjectIdentity
juniMcastConformance = _JuniMcastConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 2)
)
_JuniMcastCompliances_ObjectIdentity = ObjectIdentity
juniMcastCompliances = _JuniMcastCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 2, 1)
)
_JuniMcastConfGroups_ObjectIdentity = ObjectIdentity
juniMcastConfGroups = _JuniMcastConfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 2, 2)
)
ipMRouteEntry.registerAugmentions(
    ("Juniper-MROUTER-MIB",
     "juniMRouteEntry")
)
juniMRouteEntry.setIndexNames(*ipMRouteEntry.getIndexNames())
ipMRouteInterfaceEntry.registerAugmentions(
    ("Juniper-MROUTER-MIB",
     "juniMRouteInterfaceEntry")
)
juniMRouteInterfaceEntry.setIndexNames(*ipMRouteInterfaceEntry.getIndexNames())

# Managed Objects groups

juniMcastRpfRouteConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 2, 2, 1)
)
juniMcastRpfRouteConfGroup.setObjects(
      *(("Juniper-MROUTER-MIB", "juniMcastRouteStaticRtPreference"),
        ("Juniper-MROUTER-MIB", "juniMcastRouteStaticRpfHop"),
        ("Juniper-MROUTER-MIB", "juniMcastRouteStaticTag"),
        ("Juniper-MROUTER-MIB", "juniMcastRouteStaticRowStatus"))
)
if mibBuilder.loadTexts:
    juniMcastRpfRouteConfGroup.setStatus("current")

juniMRouteConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 2, 2, 2)
)
juniMRouteConfGroup.setObjects(
      *(("Juniper-MROUTER-MIB", "juniMRouteAdmBwAdaptive"),
        ("Juniper-MROUTER-MIB", "juniMRouteAdmBw"),
        ("Juniper-MROUTER-MIB", "juniMRouteQosBwAdaptive"),
        ("Juniper-MROUTER-MIB", "juniMRouteQosBw"),
        ("Juniper-MROUTER-MIB", "juniMRouteIsEcmp"),
        ("Juniper-MROUTER-MIB", "juniMRouteRpfDisabled"),
        ("Juniper-MROUTER-MIB", "juniMRouteOwnerProtoType"),
        ("Juniper-MROUTER-MIB", "juniMRoutePktFwd"),
        ("Juniper-MROUTER-MIB", "juniMRouteOifCnt"))
)
if mibBuilder.loadTexts:
    juniMRouteConfGroup.setStatus("current")

juniMcastGlobalConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 2, 2, 3)
)
juniMcastGlobalConfGroup.setObjects(
    ("Juniper-MROUTER-MIB", "juniMcastRpfDisable")
)
if mibBuilder.loadTexts:
    juniMcastGlobalConfGroup.setStatus("current")

juniMRoutePortConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 2, 2, 4)
)
juniMRoutePortConfGroup.setObjects(
      *(("Juniper-MROUTER-MIB", "juniMRouteInterfaceActiveGroups"),
        ("Juniper-MROUTER-MIB", "juniMRouteInterfaceBlockedGroups"),
        ("Juniper-MROUTER-MIB", "juniMroutePortLocationType"),
        ("Juniper-MROUTER-MIB", "juniMRoutePortMaxBw"),
        ("Juniper-MROUTER-MIB", "juniMRoutePortPriorityBw"),
        ("Juniper-MROUTER-MIB", "juniMRoutePortHysteresis"),
        ("Juniper-MROUTER-MIB", "juniMRoutePortAdmittedBw"),
        ("Juniper-MROUTER-MIB", "juniMRoutePortSGCount"),
        ("Juniper-MROUTER-MIB", "juniMRoutePortLimit"))
)
if mibBuilder.loadTexts:
    juniMRoutePortConfGroup.setStatus("current")


# Notification objects

juniMRoutePortBwExceded = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 1, 1)
)
juniMRoutePortBwExceded.setObjects(
    ("Juniper-MROUTER-MIB", "juniMRouteIfLocIndex")
)
if mibBuilder.loadTexts:
    juniMRoutePortBwExceded.setStatus(
        "current"
    )

juniMRoutePortBwReceded = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 1, 2)
)
juniMRoutePortBwReceded.setObjects(
    ("Juniper-MROUTER-MIB", "juniMRouteIfLocIndex")
)
if mibBuilder.loadTexts:
    juniMRoutePortBwReceded.setStatus(
        "current"
    )

juniMRoutePortPriorityBwExceded = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 1, 3)
)
juniMRoutePortPriorityBwExceded.setObjects(
    ("Juniper-MROUTER-MIB", "juniMRouteIfLocIndex")
)
if mibBuilder.loadTexts:
    juniMRoutePortPriorityBwExceded.setStatus(
        "current"
    )

juniMRoutePortPriorityBwReceded = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 1, 1, 4)
)
juniMRoutePortPriorityBwReceded.setObjects(
    ("Juniper-MROUTER-MIB", "juniMRouteIfLocIndex")
)
if mibBuilder.loadTexts:
    juniMRoutePortPriorityBwReceded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

juniMcastCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniMcastCompliance.setStatus(
        "obsolete"
    )

juniMcastCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniMcastCompliance2.setStatus(
        "obsolete"
    )

juniMcastCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 2, 1, 3)
)
if mibBuilder.loadTexts:
    juniMcastCompliance3.setStatus(
        "obsolete"
    )

juniMcastCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 65, 2, 1, 4)
)
if mibBuilder.loadTexts:
    juniMcastCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-MROUTER-MIB",
    **{"juniMRouterMIB": juniMRouterMIB,
       "juniMRouterMIBObject": juniMRouterMIBObject,
       "juniMcastTraps": juniMcastTraps,
       "juniMRoutePortBwExceded": juniMRoutePortBwExceded,
       "juniMRoutePortBwReceded": juniMRoutePortBwReceded,
       "juniMRoutePortPriorityBwExceded": juniMRoutePortPriorityBwExceded,
       "juniMRoutePortPriorityBwReceded": juniMRoutePortPriorityBwReceded,
       "juniMcastObjects": juniMcastObjects,
       "juniMcastRpfRouteTable": juniMcastRpfRouteTable,
       "juniMcastRpfRouteEntry": juniMcastRpfRouteEntry,
       "juniMcastRouteStaticDest": juniMcastRouteStaticDest,
       "juniMcastRouteStaticMask": juniMcastRouteStaticMask,
       "juniMcastRouteStaticRtPreference": juniMcastRouteStaticRtPreference,
       "juniMcastRouteStaticRpfHop": juniMcastRouteStaticRpfHop,
       "juniMcastRouteStaticTag": juniMcastRouteStaticTag,
       "juniMcastRouteStaticRowStatus": juniMcastRouteStaticRowStatus,
       "juniMRouteTable": juniMRouteTable,
       "juniMRouteEntry": juniMRouteEntry,
       "juniMRouteAdmBwAdaptive": juniMRouteAdmBwAdaptive,
       "juniMRouteAdmBw": juniMRouteAdmBw,
       "juniMRouteQosBwAdaptive": juniMRouteQosBwAdaptive,
       "juniMRouteQosBw": juniMRouteQosBw,
       "juniMRouteIsEcmp": juniMRouteIsEcmp,
       "juniMRouteRpfDisabled": juniMRouteRpfDisabled,
       "juniMRouteOwnerProtoType": juniMRouteOwnerProtoType,
       "juniMRoutePktFwd": juniMRoutePktFwd,
       "juniMRouteOifCnt": juniMRouteOifCnt,
       "juniMcastRpfDisable": juniMcastRpfDisable,
       "juniMRouteInterfaceTable": juniMRouteInterfaceTable,
       "juniMRouteInterfaceEntry": juniMRouteInterfaceEntry,
       "juniMRouteInterfaceActiveGroups": juniMRouteInterfaceActiveGroups,
       "juniMRouteInterfaceBlockedGroups": juniMRouteInterfaceBlockedGroups,
       "juniMroutePortLocationType": juniMroutePortLocationType,
       "juniMRoutePortTable": juniMRoutePortTable,
       "juniMRoutePortEntry": juniMRoutePortEntry,
       "juniMRoutePortLocationIndex": juniMRoutePortLocationIndex,
       "juniMRoutePortMaxBw": juniMRoutePortMaxBw,
       "juniMRoutePortPriorityBw": juniMRoutePortPriorityBw,
       "juniMRoutePortHysteresis": juniMRoutePortHysteresis,
       "juniMRoutePortAdmittedBw": juniMRoutePortAdmittedBw,
       "juniMRoutePortSGCount": juniMRoutePortSGCount,
       "juniMRoutePortLimit": juniMRoutePortLimit,
       "juniMcastNotifyObject": juniMcastNotifyObject,
       "juniMcastNotificationObjects": juniMcastNotificationObjects,
       "juniMRouteIfLocIndex": juniMRouteIfLocIndex,
       "juniMcastConformance": juniMcastConformance,
       "juniMcastCompliances": juniMcastCompliances,
       "juniMcastCompliance": juniMcastCompliance,
       "juniMcastCompliance2": juniMcastCompliance2,
       "juniMcastCompliance3": juniMcastCompliance3,
       "juniMcastCompliance4": juniMcastCompliance4,
       "juniMcastConfGroups": juniMcastConfGroups,
       "juniMcastRpfRouteConfGroup": juniMcastRpfRouteConfGroup,
       "juniMRouteConfGroup": juniMRouteConfGroup,
       "juniMcastGlobalConfGroup": juniMcastGlobalConfGroup,
       "juniMRoutePortConfGroup": juniMRoutePortConfGroup}
)

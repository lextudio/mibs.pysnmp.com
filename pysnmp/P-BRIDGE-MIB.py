# SNMP MIB module (P-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/P-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:58 2024
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

(dot1dBasePort,
 dot1dBasePortEntry,
 dot1dBridge,
 dot1dTp,
 dot1dTpPort) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort",
    "dot1dBasePortEntry",
    "dot1dBridge",
    "dot1dTp",
    "dot1dTpPort")

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
 MacAddress,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

pBridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 17, 6)
)
pBridgeMIB.setRevisions(
        ("2006-01-09 00:00",
         "1999-08-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(Integer32, TextualConvention):
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



# MIB Managed Objects in the order of their OIDs

_Dot1dTpHCPortTable_Object = MibTable
dot1dTpHCPortTable = _Dot1dTpHCPortTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 5)
)
if mibBuilder.loadTexts:
    dot1dTpHCPortTable.setStatus("current")
_Dot1dTpHCPortEntry_Object = MibTableRow
dot1dTpHCPortEntry = _Dot1dTpHCPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 5, 1)
)
dot1dTpHCPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dTpPort"),
)
if mibBuilder.loadTexts:
    dot1dTpHCPortEntry.setStatus("current")
_Dot1dTpHCPortInFrames_Type = Counter64
_Dot1dTpHCPortInFrames_Object = MibTableColumn
dot1dTpHCPortInFrames = _Dot1dTpHCPortInFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 5, 1, 1),
    _Dot1dTpHCPortInFrames_Type()
)
dot1dTpHCPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpHCPortInFrames.setStatus("current")
_Dot1dTpHCPortOutFrames_Type = Counter64
_Dot1dTpHCPortOutFrames_Object = MibTableColumn
dot1dTpHCPortOutFrames = _Dot1dTpHCPortOutFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 5, 1, 2),
    _Dot1dTpHCPortOutFrames_Type()
)
dot1dTpHCPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpHCPortOutFrames.setStatus("current")
_Dot1dTpHCPortInDiscards_Type = Counter64
_Dot1dTpHCPortInDiscards_Object = MibTableColumn
dot1dTpHCPortInDiscards = _Dot1dTpHCPortInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 5, 1, 3),
    _Dot1dTpHCPortInDiscards_Type()
)
dot1dTpHCPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpHCPortInDiscards.setStatus("current")
_Dot1dTpPortOverflowTable_Object = MibTable
dot1dTpPortOverflowTable = _Dot1dTpPortOverflowTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 6)
)
if mibBuilder.loadTexts:
    dot1dTpPortOverflowTable.setStatus("current")
_Dot1dTpPortOverflowEntry_Object = MibTableRow
dot1dTpPortOverflowEntry = _Dot1dTpPortOverflowEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 6, 1)
)
dot1dTpPortOverflowEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dTpPort"),
)
if mibBuilder.loadTexts:
    dot1dTpPortOverflowEntry.setStatus("current")
_Dot1dTpPortInOverflowFrames_Type = Counter32
_Dot1dTpPortInOverflowFrames_Object = MibTableColumn
dot1dTpPortInOverflowFrames = _Dot1dTpPortInOverflowFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 6, 1, 1),
    _Dot1dTpPortInOverflowFrames_Type()
)
dot1dTpPortInOverflowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortInOverflowFrames.setStatus("current")
_Dot1dTpPortOutOverflowFrames_Type = Counter32
_Dot1dTpPortOutOverflowFrames_Object = MibTableColumn
dot1dTpPortOutOverflowFrames = _Dot1dTpPortOutOverflowFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 6, 1, 2),
    _Dot1dTpPortOutOverflowFrames_Type()
)
dot1dTpPortOutOverflowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortOutOverflowFrames.setStatus("current")
_Dot1dTpPortInOverflowDiscards_Type = Counter32
_Dot1dTpPortInOverflowDiscards_Object = MibTableColumn
dot1dTpPortInOverflowDiscards = _Dot1dTpPortInOverflowDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 4, 6, 1, 3),
    _Dot1dTpPortInOverflowDiscards_Type()
)
dot1dTpPortInOverflowDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortInOverflowDiscards.setStatus("current")
_PBridgeMIBObjects_ObjectIdentity = ObjectIdentity
pBridgeMIBObjects = _PBridgeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 6, 1)
)
_Dot1dExtBase_ObjectIdentity = ObjectIdentity
dot1dExtBase = _Dot1dExtBase_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 1)
)


class _Dot1dDeviceCapabilities_Type(Bits):
    """Custom type dot1dDeviceCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dot1dExtendedFilteringServices", 0),
          ("dot1dLocalVlanCapable", 7),
          ("dot1dTrafficClasses", 1),
          ("dot1qConfigurablePvidTagging", 6),
          ("dot1qHybridCapable", 5),
          ("dot1qIVLCapable", 3),
          ("dot1qSVLCapable", 4),
          ("dot1qStaticEntryIndividualPort", 2))
    )

_Dot1dDeviceCapabilities_Type.__name__ = "Bits"
_Dot1dDeviceCapabilities_Object = MibScalar
dot1dDeviceCapabilities = _Dot1dDeviceCapabilities_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 1),
    _Dot1dDeviceCapabilities_Type()
)
dot1dDeviceCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dDeviceCapabilities.setStatus("current")


class _Dot1dTrafficClassesEnabled_Type(TruthValue):
    """Custom type dot1dTrafficClassesEnabled based on TruthValue"""


_Dot1dTrafficClassesEnabled_Object = MibScalar
dot1dTrafficClassesEnabled = _Dot1dTrafficClassesEnabled_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 2),
    _Dot1dTrafficClassesEnabled_Type()
)
dot1dTrafficClassesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dTrafficClassesEnabled.setStatus("current")


class _Dot1dGmrpStatus_Type(EnabledStatus):
    """Custom type dot1dGmrpStatus based on EnabledStatus"""


_Dot1dGmrpStatus_Object = MibScalar
dot1dGmrpStatus = _Dot1dGmrpStatus_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 3),
    _Dot1dGmrpStatus_Type()
)
dot1dGmrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dGmrpStatus.setStatus("current")
_Dot1dPortCapabilitiesTable_Object = MibTable
dot1dPortCapabilitiesTable = _Dot1dPortCapabilitiesTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dot1dPortCapabilitiesTable.setStatus("current")
_Dot1dPortCapabilitiesEntry_Object = MibTableRow
dot1dPortCapabilitiesEntry = _Dot1dPortCapabilitiesEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dot1dPortCapabilitiesEntry.setStatus("current")


class _Dot1dPortCapabilities_Type(Bits):
    """Custom type dot1dPortCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dot1qConfigurableAcceptableFrameTypes", 1),
          ("dot1qDot1qTagging", 0),
          ("dot1qIngressFiltering", 2))
    )

_Dot1dPortCapabilities_Type.__name__ = "Bits"
_Dot1dPortCapabilities_Object = MibTableColumn
dot1dPortCapabilities = _Dot1dPortCapabilities_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 4, 1, 1),
    _Dot1dPortCapabilities_Type()
)
dot1dPortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dPortCapabilities.setStatus("current")
_Dot1dPriority_ObjectIdentity = ObjectIdentity
dot1dPriority = _Dot1dPriority_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 2)
)
_Dot1dPortPriorityTable_Object = MibTable
dot1dPortPriorityTable = _Dot1dPortPriorityTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dot1dPortPriorityTable.setStatus("current")
_Dot1dPortPriorityEntry_Object = MibTableRow
dot1dPortPriorityEntry = _Dot1dPortPriorityEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dot1dPortPriorityEntry.setStatus("current")


class _Dot1dPortDefaultUserPriority_Type(Integer32):
    """Custom type dot1dPortDefaultUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1dPortDefaultUserPriority_Type.__name__ = "Integer32"
_Dot1dPortDefaultUserPriority_Object = MibTableColumn
dot1dPortDefaultUserPriority = _Dot1dPortDefaultUserPriority_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 1, 1, 1),
    _Dot1dPortDefaultUserPriority_Type()
)
dot1dPortDefaultUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortDefaultUserPriority.setStatus("current")


class _Dot1dPortNumTrafficClasses_Type(Integer32):
    """Custom type dot1dPortNumTrafficClasses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Dot1dPortNumTrafficClasses_Type.__name__ = "Integer32"
_Dot1dPortNumTrafficClasses_Object = MibTableColumn
dot1dPortNumTrafficClasses = _Dot1dPortNumTrafficClasses_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 1, 1, 2),
    _Dot1dPortNumTrafficClasses_Type()
)
dot1dPortNumTrafficClasses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortNumTrafficClasses.setStatus("current")
_Dot1dUserPriorityRegenTable_Object = MibTable
dot1dUserPriorityRegenTable = _Dot1dUserPriorityRegenTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dot1dUserPriorityRegenTable.setStatus("current")
_Dot1dUserPriorityRegenEntry_Object = MibTableRow
dot1dUserPriorityRegenEntry = _Dot1dUserPriorityRegenEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 2, 1)
)
dot1dUserPriorityRegenEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "P-BRIDGE-MIB", "dot1dUserPriority"),
)
if mibBuilder.loadTexts:
    dot1dUserPriorityRegenEntry.setStatus("current")


class _Dot1dUserPriority_Type(Integer32):
    """Custom type dot1dUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1dUserPriority_Type.__name__ = "Integer32"
_Dot1dUserPriority_Object = MibTableColumn
dot1dUserPriority = _Dot1dUserPriority_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 2, 1, 1),
    _Dot1dUserPriority_Type()
)
dot1dUserPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dUserPriority.setStatus("current")


class _Dot1dRegenUserPriority_Type(Integer32):
    """Custom type dot1dRegenUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1dRegenUserPriority_Type.__name__ = "Integer32"
_Dot1dRegenUserPriority_Object = MibTableColumn
dot1dRegenUserPriority = _Dot1dRegenUserPriority_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 2, 1, 2),
    _Dot1dRegenUserPriority_Type()
)
dot1dRegenUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dRegenUserPriority.setStatus("current")
_Dot1dTrafficClassTable_Object = MibTable
dot1dTrafficClassTable = _Dot1dTrafficClassTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dot1dTrafficClassTable.setStatus("current")
_Dot1dTrafficClassEntry_Object = MibTableRow
dot1dTrafficClassEntry = _Dot1dTrafficClassEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 3, 1)
)
dot1dTrafficClassEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "P-BRIDGE-MIB", "dot1dTrafficClassPriority"),
)
if mibBuilder.loadTexts:
    dot1dTrafficClassEntry.setStatus("current")


class _Dot1dTrafficClassPriority_Type(Integer32):
    """Custom type dot1dTrafficClassPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1dTrafficClassPriority_Type.__name__ = "Integer32"
_Dot1dTrafficClassPriority_Object = MibTableColumn
dot1dTrafficClassPriority = _Dot1dTrafficClassPriority_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 3, 1, 1),
    _Dot1dTrafficClassPriority_Type()
)
dot1dTrafficClassPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dTrafficClassPriority.setStatus("current")


class _Dot1dTrafficClass_Type(Integer32):
    """Custom type dot1dTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1dTrafficClass_Type.__name__ = "Integer32"
_Dot1dTrafficClass_Object = MibTableColumn
dot1dTrafficClass = _Dot1dTrafficClass_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 3, 1, 2),
    _Dot1dTrafficClass_Type()
)
dot1dTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dTrafficClass.setStatus("current")
_Dot1dPortOutboundAccessPriorityTable_Object = MibTable
dot1dPortOutboundAccessPriorityTable = _Dot1dPortOutboundAccessPriorityTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dot1dPortOutboundAccessPriorityTable.setStatus("current")
_Dot1dPortOutboundAccessPriorityEntry_Object = MibTableRow
dot1dPortOutboundAccessPriorityEntry = _Dot1dPortOutboundAccessPriorityEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 4, 1)
)
dot1dPortOutboundAccessPriorityEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "P-BRIDGE-MIB", "dot1dRegenUserPriority"),
)
if mibBuilder.loadTexts:
    dot1dPortOutboundAccessPriorityEntry.setStatus("current")


class _Dot1dPortOutboundAccessPriority_Type(Integer32):
    """Custom type dot1dPortOutboundAccessPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1dPortOutboundAccessPriority_Type.__name__ = "Integer32"
_Dot1dPortOutboundAccessPriority_Object = MibTableColumn
dot1dPortOutboundAccessPriority = _Dot1dPortOutboundAccessPriority_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 4, 1, 1),
    _Dot1dPortOutboundAccessPriority_Type()
)
dot1dPortOutboundAccessPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dPortOutboundAccessPriority.setStatus("current")
_Dot1dGarp_ObjectIdentity = ObjectIdentity
dot1dGarp = _Dot1dGarp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 3)
)
_Dot1dPortGarpTable_Object = MibTable
dot1dPortGarpTable = _Dot1dPortGarpTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dot1dPortGarpTable.setStatus("current")
_Dot1dPortGarpEntry_Object = MibTableRow
dot1dPortGarpEntry = _Dot1dPortGarpEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dot1dPortGarpEntry.setStatus("current")


class _Dot1dPortGarpJoinTime_Type(TimeInterval):
    """Custom type dot1dPortGarpJoinTime based on TimeInterval"""
    defaultValue = 20


_Dot1dPortGarpJoinTime_Object = MibTableColumn
dot1dPortGarpJoinTime = _Dot1dPortGarpJoinTime_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1, 1, 1),
    _Dot1dPortGarpJoinTime_Type()
)
dot1dPortGarpJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortGarpJoinTime.setStatus("current")


class _Dot1dPortGarpLeaveTime_Type(TimeInterval):
    """Custom type dot1dPortGarpLeaveTime based on TimeInterval"""
    defaultValue = 60


_Dot1dPortGarpLeaveTime_Object = MibTableColumn
dot1dPortGarpLeaveTime = _Dot1dPortGarpLeaveTime_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1, 1, 2),
    _Dot1dPortGarpLeaveTime_Type()
)
dot1dPortGarpLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortGarpLeaveTime.setStatus("current")


class _Dot1dPortGarpLeaveAllTime_Type(TimeInterval):
    """Custom type dot1dPortGarpLeaveAllTime based on TimeInterval"""
    defaultValue = 1000


_Dot1dPortGarpLeaveAllTime_Object = MibTableColumn
dot1dPortGarpLeaveAllTime = _Dot1dPortGarpLeaveAllTime_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1, 1, 3),
    _Dot1dPortGarpLeaveAllTime_Type()
)
dot1dPortGarpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortGarpLeaveAllTime.setStatus("current")
_Dot1dGmrp_ObjectIdentity = ObjectIdentity
dot1dGmrp = _Dot1dGmrp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 4)
)
_Dot1dPortGmrpTable_Object = MibTable
dot1dPortGmrpTable = _Dot1dPortGmrpTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dot1dPortGmrpTable.setStatus("current")
_Dot1dPortGmrpEntry_Object = MibTableRow
dot1dPortGmrpEntry = _Dot1dPortGmrpEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    dot1dPortGmrpEntry.setStatus("current")


class _Dot1dPortGmrpStatus_Type(EnabledStatus):
    """Custom type dot1dPortGmrpStatus based on EnabledStatus"""


_Dot1dPortGmrpStatus_Object = MibTableColumn
dot1dPortGmrpStatus = _Dot1dPortGmrpStatus_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1, 1),
    _Dot1dPortGmrpStatus_Type()
)
dot1dPortGmrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortGmrpStatus.setStatus("current")
_Dot1dPortGmrpFailedRegistrations_Type = Counter32
_Dot1dPortGmrpFailedRegistrations_Object = MibTableColumn
dot1dPortGmrpFailedRegistrations = _Dot1dPortGmrpFailedRegistrations_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1, 2),
    _Dot1dPortGmrpFailedRegistrations_Type()
)
dot1dPortGmrpFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dPortGmrpFailedRegistrations.setStatus("current")
_Dot1dPortGmrpLastPduOrigin_Type = MacAddress
_Dot1dPortGmrpLastPduOrigin_Object = MibTableColumn
dot1dPortGmrpLastPduOrigin = _Dot1dPortGmrpLastPduOrigin_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1, 3),
    _Dot1dPortGmrpLastPduOrigin_Type()
)
dot1dPortGmrpLastPduOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dPortGmrpLastPduOrigin.setStatus("current")


class _Dot1dPortRestrictedGroupRegistration_Type(TruthValue):
    """Custom type dot1dPortRestrictedGroupRegistration based on TruthValue"""


_Dot1dPortRestrictedGroupRegistration_Object = MibTableColumn
dot1dPortRestrictedGroupRegistration = _Dot1dPortRestrictedGroupRegistration_Object(
    (1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1, 4),
    _Dot1dPortRestrictedGroupRegistration_Type()
)
dot1dPortRestrictedGroupRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortRestrictedGroupRegistration.setStatus("current")
_PBridgeConformance_ObjectIdentity = ObjectIdentity
pBridgeConformance = _PBridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 6, 2)
)
_PBridgeGroups_ObjectIdentity = ObjectIdentity
pBridgeGroups = _PBridgeGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 6, 2, 1)
)
_PBridgeCompliances_ObjectIdentity = ObjectIdentity
pBridgeCompliances = _PBridgeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 6, 2, 2)
)
dot1dBasePortEntry.registerAugmentions(
    ("P-BRIDGE-MIB",
     "dot1dPortCapabilitiesEntry")
)
dot1dPortCapabilitiesEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
dot1dBasePortEntry.registerAugmentions(
    ("P-BRIDGE-MIB",
     "dot1dPortPriorityEntry")
)
dot1dPortPriorityEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
dot1dBasePortEntry.registerAugmentions(
    ("P-BRIDGE-MIB",
     "dot1dPortGarpEntry")
)
dot1dPortGarpEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
dot1dBasePortEntry.registerAugmentions(
    ("P-BRIDGE-MIB",
     "dot1dPortGmrpEntry")
)
dot1dPortGmrpEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())

# Managed Objects groups

pBridgeExtCapGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 1)
)
pBridgeExtCapGroup.setObjects(
      *(("P-BRIDGE-MIB", "dot1dDeviceCapabilities"),
        ("P-BRIDGE-MIB", "dot1dPortCapabilities"))
)
if mibBuilder.loadTexts:
    pBridgeExtCapGroup.setStatus("current")

pBridgeDeviceGmrpGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 2)
)
pBridgeDeviceGmrpGroup.setObjects(
    ("P-BRIDGE-MIB", "dot1dGmrpStatus")
)
if mibBuilder.loadTexts:
    pBridgeDeviceGmrpGroup.setStatus("current")

pBridgeDevicePriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 3)
)
pBridgeDevicePriorityGroup.setObjects(
    ("P-BRIDGE-MIB", "dot1dTrafficClassesEnabled")
)
if mibBuilder.loadTexts:
    pBridgeDevicePriorityGroup.setStatus("current")

pBridgeDefaultPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 4)
)
pBridgeDefaultPriorityGroup.setObjects(
    ("P-BRIDGE-MIB", "dot1dPortDefaultUserPriority")
)
if mibBuilder.loadTexts:
    pBridgeDefaultPriorityGroup.setStatus("current")

pBridgeRegenPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 5)
)
pBridgeRegenPriorityGroup.setObjects(
    ("P-BRIDGE-MIB", "dot1dRegenUserPriority")
)
if mibBuilder.loadTexts:
    pBridgeRegenPriorityGroup.setStatus("current")

pBridgePriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 6)
)
pBridgePriorityGroup.setObjects(
      *(("P-BRIDGE-MIB", "dot1dPortNumTrafficClasses"),
        ("P-BRIDGE-MIB", "dot1dTrafficClass"))
)
if mibBuilder.loadTexts:
    pBridgePriorityGroup.setStatus("current")

pBridgeAccessPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 7)
)
pBridgeAccessPriorityGroup.setObjects(
    ("P-BRIDGE-MIB", "dot1dPortOutboundAccessPriority")
)
if mibBuilder.loadTexts:
    pBridgeAccessPriorityGroup.setStatus("current")

pBridgePortGarpGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 8)
)
pBridgePortGarpGroup.setObjects(
      *(("P-BRIDGE-MIB", "dot1dPortGarpJoinTime"),
        ("P-BRIDGE-MIB", "dot1dPortGarpLeaveTime"),
        ("P-BRIDGE-MIB", "dot1dPortGarpLeaveAllTime"))
)
if mibBuilder.loadTexts:
    pBridgePortGarpGroup.setStatus("current")

pBridgePortGmrpGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 9)
)
pBridgePortGmrpGroup.setObjects(
      *(("P-BRIDGE-MIB", "dot1dPortGmrpStatus"),
        ("P-BRIDGE-MIB", "dot1dPortGmrpFailedRegistrations"),
        ("P-BRIDGE-MIB", "dot1dPortGmrpLastPduOrigin"))
)
if mibBuilder.loadTexts:
    pBridgePortGmrpGroup.setStatus("deprecated")

pBridgeHCPortGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 10)
)
pBridgeHCPortGroup.setObjects(
      *(("P-BRIDGE-MIB", "dot1dTpHCPortInFrames"),
        ("P-BRIDGE-MIB", "dot1dTpHCPortOutFrames"),
        ("P-BRIDGE-MIB", "dot1dTpHCPortInDiscards"))
)
if mibBuilder.loadTexts:
    pBridgeHCPortGroup.setStatus("current")

pBridgePortOverflowGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 11)
)
pBridgePortOverflowGroup.setObjects(
      *(("P-BRIDGE-MIB", "dot1dTpPortInOverflowFrames"),
        ("P-BRIDGE-MIB", "dot1dTpPortOutOverflowFrames"),
        ("P-BRIDGE-MIB", "dot1dTpPortInOverflowDiscards"))
)
if mibBuilder.loadTexts:
    pBridgePortOverflowGroup.setStatus("current")

pBridgePortGmrpGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 12)
)
pBridgePortGmrpGroup2.setObjects(
      *(("P-BRIDGE-MIB", "dot1dPortGmrpStatus"),
        ("P-BRIDGE-MIB", "dot1dPortGmrpFailedRegistrations"),
        ("P-BRIDGE-MIB", "dot1dPortGmrpLastPduOrigin"),
        ("P-BRIDGE-MIB", "dot1dPortRestrictedGroupRegistration"))
)
if mibBuilder.loadTexts:
    pBridgePortGmrpGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pBridgeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 17, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pBridgeCompliance.setStatus(
        "deprecated"
    )

pBridgeCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 17, 6, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pBridgeCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "P-BRIDGE-MIB",
    **{"EnabledStatus": EnabledStatus,
       "dot1dTpHCPortTable": dot1dTpHCPortTable,
       "dot1dTpHCPortEntry": dot1dTpHCPortEntry,
       "dot1dTpHCPortInFrames": dot1dTpHCPortInFrames,
       "dot1dTpHCPortOutFrames": dot1dTpHCPortOutFrames,
       "dot1dTpHCPortInDiscards": dot1dTpHCPortInDiscards,
       "dot1dTpPortOverflowTable": dot1dTpPortOverflowTable,
       "dot1dTpPortOverflowEntry": dot1dTpPortOverflowEntry,
       "dot1dTpPortInOverflowFrames": dot1dTpPortInOverflowFrames,
       "dot1dTpPortOutOverflowFrames": dot1dTpPortOutOverflowFrames,
       "dot1dTpPortInOverflowDiscards": dot1dTpPortInOverflowDiscards,
       "pBridgeMIB": pBridgeMIB,
       "pBridgeMIBObjects": pBridgeMIBObjects,
       "dot1dExtBase": dot1dExtBase,
       "dot1dDeviceCapabilities": dot1dDeviceCapabilities,
       "dot1dTrafficClassesEnabled": dot1dTrafficClassesEnabled,
       "dot1dGmrpStatus": dot1dGmrpStatus,
       "dot1dPortCapabilitiesTable": dot1dPortCapabilitiesTable,
       "dot1dPortCapabilitiesEntry": dot1dPortCapabilitiesEntry,
       "dot1dPortCapabilities": dot1dPortCapabilities,
       "dot1dPriority": dot1dPriority,
       "dot1dPortPriorityTable": dot1dPortPriorityTable,
       "dot1dPortPriorityEntry": dot1dPortPriorityEntry,
       "dot1dPortDefaultUserPriority": dot1dPortDefaultUserPriority,
       "dot1dPortNumTrafficClasses": dot1dPortNumTrafficClasses,
       "dot1dUserPriorityRegenTable": dot1dUserPriorityRegenTable,
       "dot1dUserPriorityRegenEntry": dot1dUserPriorityRegenEntry,
       "dot1dUserPriority": dot1dUserPriority,
       "dot1dRegenUserPriority": dot1dRegenUserPriority,
       "dot1dTrafficClassTable": dot1dTrafficClassTable,
       "dot1dTrafficClassEntry": dot1dTrafficClassEntry,
       "dot1dTrafficClassPriority": dot1dTrafficClassPriority,
       "dot1dTrafficClass": dot1dTrafficClass,
       "dot1dPortOutboundAccessPriorityTable": dot1dPortOutboundAccessPriorityTable,
       "dot1dPortOutboundAccessPriorityEntry": dot1dPortOutboundAccessPriorityEntry,
       "dot1dPortOutboundAccessPriority": dot1dPortOutboundAccessPriority,
       "dot1dGarp": dot1dGarp,
       "dot1dPortGarpTable": dot1dPortGarpTable,
       "dot1dPortGarpEntry": dot1dPortGarpEntry,
       "dot1dPortGarpJoinTime": dot1dPortGarpJoinTime,
       "dot1dPortGarpLeaveTime": dot1dPortGarpLeaveTime,
       "dot1dPortGarpLeaveAllTime": dot1dPortGarpLeaveAllTime,
       "dot1dGmrp": dot1dGmrp,
       "dot1dPortGmrpTable": dot1dPortGmrpTable,
       "dot1dPortGmrpEntry": dot1dPortGmrpEntry,
       "dot1dPortGmrpStatus": dot1dPortGmrpStatus,
       "dot1dPortGmrpFailedRegistrations": dot1dPortGmrpFailedRegistrations,
       "dot1dPortGmrpLastPduOrigin": dot1dPortGmrpLastPduOrigin,
       "dot1dPortRestrictedGroupRegistration": dot1dPortRestrictedGroupRegistration,
       "pBridgeConformance": pBridgeConformance,
       "pBridgeGroups": pBridgeGroups,
       "pBridgeExtCapGroup": pBridgeExtCapGroup,
       "pBridgeDeviceGmrpGroup": pBridgeDeviceGmrpGroup,
       "pBridgeDevicePriorityGroup": pBridgeDevicePriorityGroup,
       "pBridgeDefaultPriorityGroup": pBridgeDefaultPriorityGroup,
       "pBridgeRegenPriorityGroup": pBridgeRegenPriorityGroup,
       "pBridgePriorityGroup": pBridgePriorityGroup,
       "pBridgeAccessPriorityGroup": pBridgeAccessPriorityGroup,
       "pBridgePortGarpGroup": pBridgePortGarpGroup,
       "pBridgePortGmrpGroup": pBridgePortGmrpGroup,
       "pBridgeHCPortGroup": pBridgeHCPortGroup,
       "pBridgePortOverflowGroup": pBridgePortOverflowGroup,
       "pBridgePortGmrpGroup2": pBridgePortGmrpGroup2,
       "pBridgeCompliances": pBridgeCompliances,
       "pBridgeCompliance": pBridgeCompliance,
       "pBridgeCompliance2": pBridgeCompliance2}
)

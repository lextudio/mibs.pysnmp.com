# SNMP MIB module (MPLS-TE-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-TE-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:42 2024
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

(IndexIntegerNextFree,) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IndexIntegerNextFree")

(InterfaceIndexOrZero,
 ifCounterDiscontinuityGroup,
 ifGeneralInformationGroup) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifCounterDiscontinuityGroup",
    "ifGeneralInformationGroup")

(InetAddressPrefixLength,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressPrefixLength")

(MplsBitRate,
 MplsBurstSize,
 MplsExtendedTunnelId,
 MplsLSPID,
 MplsOwner,
 MplsPathIndex,
 MplsPathIndexOrZero,
 MplsTunnelAffinity,
 MplsTunnelIndex,
 MplsTunnelInstanceIndex,
 TeHopAddress,
 TeHopAddressAS,
 TeHopAddressType,
 TeHopAddressUnnum,
 mplsStdMIB) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsBitRate",
    "MplsBurstSize",
    "MplsExtendedTunnelId",
    "MplsLSPID",
    "MplsOwner",
    "MplsPathIndex",
    "MplsPathIndexOrZero",
    "MplsTunnelAffinity",
    "MplsTunnelIndex",
    "MplsTunnelInstanceIndex",
    "TeHopAddress",
    "TeHopAddressAS",
    "TeHopAddressType",
    "TeHopAddressUnnum",
    "mplsStdMIB")

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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "zeroDotZero")

(DisplayString,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mplsTeStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 3)
)
mplsTeStdMIB.setRevisions(
        ("2004-06-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsTeNotifications_ObjectIdentity = ObjectIdentity
mplsTeNotifications = _MplsTeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 0)
)
_MplsTeScalars_ObjectIdentity = ObjectIdentity
mplsTeScalars = _MplsTeScalars_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 1)
)
_MplsTunnelConfigured_Type = Unsigned32
_MplsTunnelConfigured_Object = MibScalar
mplsTunnelConfigured = _MplsTunnelConfigured_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 1, 1),
    _MplsTunnelConfigured_Type()
)
mplsTunnelConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelConfigured.setStatus("current")
_MplsTunnelActive_Type = Unsigned32
_MplsTunnelActive_Object = MibScalar
mplsTunnelActive = _MplsTunnelActive_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 1, 2),
    _MplsTunnelActive_Type()
)
mplsTunnelActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelActive.setStatus("current")


class _MplsTunnelTEDistProto_Type(Bits):
    """Custom type mplsTunnelTEDistProto based on Bits"""
    namedValues = NamedValues(
        *(("isis", 2),
          ("ospf", 1),
          ("other", 0))
    )

_MplsTunnelTEDistProto_Type.__name__ = "Bits"
_MplsTunnelTEDistProto_Object = MibScalar
mplsTunnelTEDistProto = _MplsTunnelTEDistProto_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 1, 3),
    _MplsTunnelTEDistProto_Type()
)
mplsTunnelTEDistProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelTEDistProto.setStatus("current")
_MplsTunnelMaxHops_Type = Unsigned32
_MplsTunnelMaxHops_Object = MibScalar
mplsTunnelMaxHops = _MplsTunnelMaxHops_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 1, 4),
    _MplsTunnelMaxHops_Type()
)
mplsTunnelMaxHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelMaxHops.setStatus("current")


class _MplsTunnelNotificationMaxRate_Type(Unsigned32):
    """Custom type mplsTunnelNotificationMaxRate based on Unsigned32"""
    defaultValue = 0


_MplsTunnelNotificationMaxRate_Object = MibScalar
mplsTunnelNotificationMaxRate = _MplsTunnelNotificationMaxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 1, 5),
    _MplsTunnelNotificationMaxRate_Type()
)
mplsTunnelNotificationMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsTunnelNotificationMaxRate.setStatus("current")
_MplsTeObjects_ObjectIdentity = ObjectIdentity
mplsTeObjects = _MplsTeObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2)
)


class _MplsTunnelIndexNext_Type(IndexIntegerNextFree):
    """Custom type mplsTunnelIndexNext based on IndexIntegerNextFree"""
    subtypeSpec = IndexIntegerNextFree.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsTunnelIndexNext_Type.__name__ = "IndexIntegerNextFree"
_MplsTunnelIndexNext_Object = MibScalar
mplsTunnelIndexNext = _MplsTunnelIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 1),
    _MplsTunnelIndexNext_Type()
)
mplsTunnelIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelIndexNext.setStatus("current")
_MplsTunnelTable_Object = MibTable
mplsTunnelTable = _MplsTunnelTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2)
)
if mibBuilder.loadTexts:
    mplsTunnelTable.setStatus("current")
_MplsTunnelEntry_Object = MibTableRow
mplsTunnelEntry = _MplsTunnelEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1)
)
mplsTunnelEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"),
)
if mibBuilder.loadTexts:
    mplsTunnelEntry.setStatus("current")
_MplsTunnelIndex_Type = MplsTunnelIndex
_MplsTunnelIndex_Object = MibTableColumn
mplsTunnelIndex = _MplsTunnelIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 1),
    _MplsTunnelIndex_Type()
)
mplsTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelIndex.setStatus("current")
_MplsTunnelInstance_Type = MplsTunnelInstanceIndex
_MplsTunnelInstance_Object = MibTableColumn
mplsTunnelInstance = _MplsTunnelInstance_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 2),
    _MplsTunnelInstance_Type()
)
mplsTunnelInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelInstance.setStatus("current")
_MplsTunnelIngressLSRId_Type = MplsExtendedTunnelId
_MplsTunnelIngressLSRId_Object = MibTableColumn
mplsTunnelIngressLSRId = _MplsTunnelIngressLSRId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 3),
    _MplsTunnelIngressLSRId_Type()
)
mplsTunnelIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelIngressLSRId.setStatus("current")
_MplsTunnelEgressLSRId_Type = MplsExtendedTunnelId
_MplsTunnelEgressLSRId_Object = MibTableColumn
mplsTunnelEgressLSRId = _MplsTunnelEgressLSRId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 4),
    _MplsTunnelEgressLSRId_Type()
)
mplsTunnelEgressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelEgressLSRId.setStatus("current")
_MplsTunnelName_Type = SnmpAdminString
_MplsTunnelName_Object = MibTableColumn
mplsTunnelName = _MplsTunnelName_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 5),
    _MplsTunnelName_Type()
)
mplsTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelName.setStatus("current")
_MplsTunnelDescr_Type = SnmpAdminString
_MplsTunnelDescr_Object = MibTableColumn
mplsTunnelDescr = _MplsTunnelDescr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 6),
    _MplsTunnelDescr_Type()
)
mplsTunnelDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelDescr.setStatus("current")


class _MplsTunnelIsIf_Type(TruthValue):
    """Custom type mplsTunnelIsIf based on TruthValue"""


_MplsTunnelIsIf_Object = MibTableColumn
mplsTunnelIsIf = _MplsTunnelIsIf_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 7),
    _MplsTunnelIsIf_Type()
)
mplsTunnelIsIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelIsIf.setStatus("current")


class _MplsTunnelIfIndex_Type(InterfaceIndexOrZero):
    """Custom type mplsTunnelIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_MplsTunnelIfIndex_Object = MibTableColumn
mplsTunnelIfIndex = _MplsTunnelIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 8),
    _MplsTunnelIfIndex_Type()
)
mplsTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelIfIndex.setStatus("current")
_MplsTunnelOwner_Type = MplsOwner
_MplsTunnelOwner_Object = MibTableColumn
mplsTunnelOwner = _MplsTunnelOwner_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 9),
    _MplsTunnelOwner_Type()
)
mplsTunnelOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelOwner.setStatus("current")


class _MplsTunnelRole_Type(Integer32):
    """Custom type mplsTunnelRole based on Integer32"""
    defaultValue = 1

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
        *(("head", 1),
          ("headTail", 4),
          ("tail", 3),
          ("transit", 2))
    )


_MplsTunnelRole_Type.__name__ = "Integer32"
_MplsTunnelRole_Object = MibTableColumn
mplsTunnelRole = _MplsTunnelRole_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 10),
    _MplsTunnelRole_Type()
)
mplsTunnelRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelRole.setStatus("current")


class _MplsTunnelXCPointer_Type(RowPointer):
    """Custom type mplsTunnelXCPointer based on RowPointer"""
    defaultValue = (0, 0)


_MplsTunnelXCPointer_Object = MibTableColumn
mplsTunnelXCPointer = _MplsTunnelXCPointer_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 11),
    _MplsTunnelXCPointer_Type()
)
mplsTunnelXCPointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelXCPointer.setStatus("current")


class _MplsTunnelSignallingProto_Type(Integer32):
    """Custom type mplsTunnelSignallingProto based on Integer32"""
    defaultValue = 1

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
        *(("crldp", 3),
          ("none", 1),
          ("other", 4),
          ("rsvp", 2))
    )


_MplsTunnelSignallingProto_Type.__name__ = "Integer32"
_MplsTunnelSignallingProto_Object = MibTableColumn
mplsTunnelSignallingProto = _MplsTunnelSignallingProto_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 12),
    _MplsTunnelSignallingProto_Type()
)
mplsTunnelSignallingProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSignallingProto.setStatus("current")


class _MplsTunnelSetupPrio_Type(Integer32):
    """Custom type mplsTunnelSetupPrio based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsTunnelSetupPrio_Type.__name__ = "Integer32"
_MplsTunnelSetupPrio_Object = MibTableColumn
mplsTunnelSetupPrio = _MplsTunnelSetupPrio_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 13),
    _MplsTunnelSetupPrio_Type()
)
mplsTunnelSetupPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSetupPrio.setStatus("current")


class _MplsTunnelHoldingPrio_Type(Integer32):
    """Custom type mplsTunnelHoldingPrio based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsTunnelHoldingPrio_Type.__name__ = "Integer32"
_MplsTunnelHoldingPrio_Object = MibTableColumn
mplsTunnelHoldingPrio = _MplsTunnelHoldingPrio_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 14),
    _MplsTunnelHoldingPrio_Type()
)
mplsTunnelHoldingPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHoldingPrio.setStatus("current")


class _MplsTunnelSessionAttributes_Type(Bits):
    """Custom type mplsTunnelSessionAttributes based on Bits"""
    namedValues = NamedValues(
        *(("fastReroute", 0),
          ("isPersistent", 2),
          ("isPinned", 3),
          ("mergingPermitted", 1),
          ("recordRoute", 4))
    )

_MplsTunnelSessionAttributes_Type.__name__ = "Bits"
_MplsTunnelSessionAttributes_Object = MibTableColumn
mplsTunnelSessionAttributes = _MplsTunnelSessionAttributes_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 15),
    _MplsTunnelSessionAttributes_Type()
)
mplsTunnelSessionAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSessionAttributes.setStatus("current")


class _MplsTunnelLocalProtectInUse_Type(TruthValue):
    """Custom type mplsTunnelLocalProtectInUse based on TruthValue"""


_MplsTunnelLocalProtectInUse_Object = MibTableColumn
mplsTunnelLocalProtectInUse = _MplsTunnelLocalProtectInUse_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 16),
    _MplsTunnelLocalProtectInUse_Type()
)
mplsTunnelLocalProtectInUse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelLocalProtectInUse.setStatus("current")


class _MplsTunnelResourcePointer_Type(RowPointer):
    """Custom type mplsTunnelResourcePointer based on RowPointer"""
    defaultValue = (0, 0)


_MplsTunnelResourcePointer_Object = MibTableColumn
mplsTunnelResourcePointer = _MplsTunnelResourcePointer_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 17),
    _MplsTunnelResourcePointer_Type()
)
mplsTunnelResourcePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourcePointer.setStatus("current")


class _MplsTunnelPrimaryInstance_Type(MplsTunnelInstanceIndex):
    """Custom type mplsTunnelPrimaryInstance based on MplsTunnelInstanceIndex"""
    defaultValue = 0


_MplsTunnelPrimaryInstance_Object = MibTableColumn
mplsTunnelPrimaryInstance = _MplsTunnelPrimaryInstance_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 18),
    _MplsTunnelPrimaryInstance_Type()
)
mplsTunnelPrimaryInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPrimaryInstance.setStatus("current")


class _MplsTunnelInstancePriority_Type(Unsigned32):
    """Custom type mplsTunnelInstancePriority based on Unsigned32"""
    defaultValue = 0


_MplsTunnelInstancePriority_Object = MibTableColumn
mplsTunnelInstancePriority = _MplsTunnelInstancePriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 19),
    _MplsTunnelInstancePriority_Type()
)
mplsTunnelInstancePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelInstancePriority.setStatus("current")


class _MplsTunnelHopTableIndex_Type(MplsPathIndexOrZero):
    """Custom type mplsTunnelHopTableIndex based on MplsPathIndexOrZero"""
    defaultValue = 0


_MplsTunnelHopTableIndex_Object = MibTableColumn
mplsTunnelHopTableIndex = _MplsTunnelHopTableIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 20),
    _MplsTunnelHopTableIndex_Type()
)
mplsTunnelHopTableIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopTableIndex.setStatus("current")


class _MplsTunnelPathInUse_Type(MplsPathIndexOrZero):
    """Custom type mplsTunnelPathInUse based on MplsPathIndexOrZero"""
    defaultValue = 0


_MplsTunnelPathInUse_Object = MibTableColumn
mplsTunnelPathInUse = _MplsTunnelPathInUse_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 21),
    _MplsTunnelPathInUse_Type()
)
mplsTunnelPathInUse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelPathInUse.setStatus("current")


class _MplsTunnelARHopTableIndex_Type(MplsPathIndexOrZero):
    """Custom type mplsTunnelARHopTableIndex based on MplsPathIndexOrZero"""
    defaultValue = 0


_MplsTunnelARHopTableIndex_Object = MibTableColumn
mplsTunnelARHopTableIndex = _MplsTunnelARHopTableIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 22),
    _MplsTunnelARHopTableIndex_Type()
)
mplsTunnelARHopTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopTableIndex.setStatus("current")


class _MplsTunnelCHopTableIndex_Type(MplsPathIndexOrZero):
    """Custom type mplsTunnelCHopTableIndex based on MplsPathIndexOrZero"""
    defaultValue = 0


_MplsTunnelCHopTableIndex_Object = MibTableColumn
mplsTunnelCHopTableIndex = _MplsTunnelCHopTableIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 23),
    _MplsTunnelCHopTableIndex_Type()
)
mplsTunnelCHopTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopTableIndex.setStatus("current")
_MplsTunnelIncludeAnyAffinity_Type = MplsTunnelAffinity
_MplsTunnelIncludeAnyAffinity_Object = MibTableColumn
mplsTunnelIncludeAnyAffinity = _MplsTunnelIncludeAnyAffinity_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 24),
    _MplsTunnelIncludeAnyAffinity_Type()
)
mplsTunnelIncludeAnyAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelIncludeAnyAffinity.setStatus("current")
_MplsTunnelIncludeAllAffinity_Type = MplsTunnelAffinity
_MplsTunnelIncludeAllAffinity_Object = MibTableColumn
mplsTunnelIncludeAllAffinity = _MplsTunnelIncludeAllAffinity_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 25),
    _MplsTunnelIncludeAllAffinity_Type()
)
mplsTunnelIncludeAllAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelIncludeAllAffinity.setStatus("current")


class _MplsTunnelExcludeAnyAffinity_Type(MplsTunnelAffinity):
    """Custom type mplsTunnelExcludeAnyAffinity based on MplsTunnelAffinity"""
    defaultValue = 0


_MplsTunnelExcludeAnyAffinity_Object = MibTableColumn
mplsTunnelExcludeAnyAffinity = _MplsTunnelExcludeAnyAffinity_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 26),
    _MplsTunnelExcludeAnyAffinity_Type()
)
mplsTunnelExcludeAnyAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExcludeAnyAffinity.setStatus("current")
_MplsTunnelTotalUpTime_Type = TimeTicks
_MplsTunnelTotalUpTime_Object = MibTableColumn
mplsTunnelTotalUpTime = _MplsTunnelTotalUpTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 27),
    _MplsTunnelTotalUpTime_Type()
)
mplsTunnelTotalUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelTotalUpTime.setStatus("current")
_MplsTunnelInstanceUpTime_Type = TimeTicks
_MplsTunnelInstanceUpTime_Object = MibTableColumn
mplsTunnelInstanceUpTime = _MplsTunnelInstanceUpTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 28),
    _MplsTunnelInstanceUpTime_Type()
)
mplsTunnelInstanceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelInstanceUpTime.setStatus("current")
_MplsTunnelPrimaryUpTime_Type = TimeTicks
_MplsTunnelPrimaryUpTime_Object = MibTableColumn
mplsTunnelPrimaryUpTime = _MplsTunnelPrimaryUpTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 29),
    _MplsTunnelPrimaryUpTime_Type()
)
mplsTunnelPrimaryUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPrimaryUpTime.setStatus("current")
_MplsTunnelPathChanges_Type = Counter32
_MplsTunnelPathChanges_Object = MibTableColumn
mplsTunnelPathChanges = _MplsTunnelPathChanges_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 30),
    _MplsTunnelPathChanges_Type()
)
mplsTunnelPathChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPathChanges.setStatus("current")
_MplsTunnelLastPathChange_Type = TimeTicks
_MplsTunnelLastPathChange_Object = MibTableColumn
mplsTunnelLastPathChange = _MplsTunnelLastPathChange_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 31),
    _MplsTunnelLastPathChange_Type()
)
mplsTunnelLastPathChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelLastPathChange.setStatus("current")
_MplsTunnelCreationTime_Type = TimeStamp
_MplsTunnelCreationTime_Object = MibTableColumn
mplsTunnelCreationTime = _MplsTunnelCreationTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 32),
    _MplsTunnelCreationTime_Type()
)
mplsTunnelCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCreationTime.setStatus("current")
_MplsTunnelStateTransitions_Type = Counter32
_MplsTunnelStateTransitions_Object = MibTableColumn
mplsTunnelStateTransitions = _MplsTunnelStateTransitions_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 33),
    _MplsTunnelStateTransitions_Type()
)
mplsTunnelStateTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelStateTransitions.setStatus("current")


class _MplsTunnelAdminStatus_Type(Integer32):
    """Custom type mplsTunnelAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MplsTunnelAdminStatus_Type.__name__ = "Integer32"
_MplsTunnelAdminStatus_Object = MibTableColumn
mplsTunnelAdminStatus = _MplsTunnelAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 34),
    _MplsTunnelAdminStatus_Type()
)
mplsTunnelAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelAdminStatus.setStatus("current")


class _MplsTunnelOperStatus_Type(Integer32):
    """Custom type mplsTunnelOperStatus based on Integer32"""
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
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_MplsTunnelOperStatus_Type.__name__ = "Integer32"
_MplsTunnelOperStatus_Object = MibTableColumn
mplsTunnelOperStatus = _MplsTunnelOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 35),
    _MplsTunnelOperStatus_Type()
)
mplsTunnelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelOperStatus.setStatus("current")
_MplsTunnelRowStatus_Type = RowStatus
_MplsTunnelRowStatus_Object = MibTableColumn
mplsTunnelRowStatus = _MplsTunnelRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 36),
    _MplsTunnelRowStatus_Type()
)
mplsTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelRowStatus.setStatus("current")


class _MplsTunnelStorageType_Type(StorageType):
    """Custom type mplsTunnelStorageType based on StorageType"""


_MplsTunnelStorageType_Object = MibTableColumn
mplsTunnelStorageType = _MplsTunnelStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 2, 1, 37),
    _MplsTunnelStorageType_Type()
)
mplsTunnelStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelStorageType.setStatus("current")
_MplsTunnelHopListIndexNext_Type = MplsPathIndexOrZero
_MplsTunnelHopListIndexNext_Object = MibScalar
mplsTunnelHopListIndexNext = _MplsTunnelHopListIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 3),
    _MplsTunnelHopListIndexNext_Type()
)
mplsTunnelHopListIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelHopListIndexNext.setStatus("current")
_MplsTunnelHopTable_Object = MibTable
mplsTunnelHopTable = _MplsTunnelHopTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 4)
)
if mibBuilder.loadTexts:
    mplsTunnelHopTable.setStatus("current")
_MplsTunnelHopEntry_Object = MibTableRow
mplsTunnelHopEntry = _MplsTunnelHopEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 4, 1)
)
mplsTunnelHopEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelHopListIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelHopPathOptionIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelHopIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelHopEntry.setStatus("current")
_MplsTunnelHopListIndex_Type = MplsPathIndex
_MplsTunnelHopListIndex_Object = MibTableColumn
mplsTunnelHopListIndex = _MplsTunnelHopListIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 4, 1, 1),
    _MplsTunnelHopListIndex_Type()
)
mplsTunnelHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelHopListIndex.setStatus("current")
_MplsTunnelHopPathOptionIndex_Type = MplsPathIndex
_MplsTunnelHopPathOptionIndex_Object = MibTableColumn
mplsTunnelHopPathOptionIndex = _MplsTunnelHopPathOptionIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 4, 1, 2),
    _MplsTunnelHopPathOptionIndex_Type()
)
mplsTunnelHopPathOptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelHopPathOptionIndex.setStatus("current")
_MplsTunnelHopIndex_Type = MplsPathIndex
_MplsTunnelHopIndex_Object = MibTableColumn
mplsTunnelHopIndex = _MplsTunnelHopIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 4, 1, 3),
    _MplsTunnelHopIndex_Type()
)
mplsTunnelHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelHopIndex.setStatus("current")


class _MplsTunnelHopAddrType_Type(TeHopAddressType):
    """Custom type mplsTunnelHopAddrType based on TeHopAddressType"""


_MplsTunnelHopAddrType_Object = MibTableColumn
mplsTunnelHopAddrType = _MplsTunnelHopAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 4, 1, 4),
    _MplsTunnelHopAddrType_Type()
)
mplsTunnelHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopAddrType.setStatus("current")


class _MplsTunnelHopIpAddr_Type(TeHopAddress):
    """Custom type mplsTunnelHopIpAddr based on TeHopAddress"""
    defaultHexValue = "00000000"


_MplsTunnelHopIpAddr_Object = MibTableColumn
mplsTunnelHopIpAddr = _MplsTunnelHopIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 4, 1, 5),
    _MplsTunnelHopIpAddr_Type()
)
mplsTunnelHopIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopIpAddr.setStatus("current")


class _MplsTunnelHopIpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type mplsTunnelHopIpPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 32


_MplsTunnelHopIpPrefixLen_Object = MibTableColumn
mplsTunnelHopIpPrefixLen = _MplsTunnelHopIpPrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 4, 1, 6),
    _MplsTunnelHopIpPrefixLen_Type()
)
mplsTunnelHopIpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopIpPrefixLen.setStatus("current")
_MplsTunnelHopAsNumber_Type = TeHopAddressAS
_MplsTunnelHopAsNumber_Object = MibTableColumn
mplsTunnelHopAsNumber = _MplsTunnelHopAsNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 4, 1, 7),
    _MplsTunnelHopAsNumber_Type()
)
mplsTunnelHopAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopAsNumber.setStatus("current")
_MplsTunnelHopAddrUnnum_Type = TeHopAddressUnnum
_MplsTunnelHopAddrUnnum_Object = MibTableColumn
mplsTunnelHopAddrUnnum = _MplsTunnelHopAddrUnnum_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 4, 1, 8),
    _MplsTunnelHopAddrUnnum_Type()
)
mplsTunnelHopAddrUnnum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopAddrUnnum.setStatus("current")
_MplsTunnelHopLspId_Type = MplsLSPID
_MplsTunnelHopLspId_Object = MibTableColumn
mplsTunnelHopLspId = _MplsTunnelHopLspId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 4, 1, 9),
    _MplsTunnelHopLspId_Type()
)
mplsTunnelHopLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopLspId.setStatus("current")


class _MplsTunnelHopType_Type(Integer32):
    """Custom type mplsTunnelHopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loose", 2),
          ("strict", 1))
    )


_MplsTunnelHopType_Type.__name__ = "Integer32"
_MplsTunnelHopType_Object = MibTableColumn
mplsTunnelHopType = _MplsTunnelHopType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 4, 1, 10),
    _MplsTunnelHopType_Type()
)
mplsTunnelHopType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopType.setStatus("current")


class _MplsTunnelHopInclude_Type(TruthValue):
    """Custom type mplsTunnelHopInclude based on TruthValue"""


_MplsTunnelHopInclude_Object = MibTableColumn
mplsTunnelHopInclude = _MplsTunnelHopInclude_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 4, 1, 11),
    _MplsTunnelHopInclude_Type()
)
mplsTunnelHopInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopInclude.setStatus("current")
_MplsTunnelHopPathOptionName_Type = SnmpAdminString
_MplsTunnelHopPathOptionName_Object = MibTableColumn
mplsTunnelHopPathOptionName = _MplsTunnelHopPathOptionName_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 4, 1, 12),
    _MplsTunnelHopPathOptionName_Type()
)
mplsTunnelHopPathOptionName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopPathOptionName.setStatus("current")


class _MplsTunnelHopEntryPathComp_Type(Integer32):
    """Custom type mplsTunnelHopEntryPathComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("explicit", 2))
    )


_MplsTunnelHopEntryPathComp_Type.__name__ = "Integer32"
_MplsTunnelHopEntryPathComp_Object = MibTableColumn
mplsTunnelHopEntryPathComp = _MplsTunnelHopEntryPathComp_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 4, 1, 13),
    _MplsTunnelHopEntryPathComp_Type()
)
mplsTunnelHopEntryPathComp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopEntryPathComp.setStatus("current")
_MplsTunnelHopRowStatus_Type = RowStatus
_MplsTunnelHopRowStatus_Object = MibTableColumn
mplsTunnelHopRowStatus = _MplsTunnelHopRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 4, 1, 14),
    _MplsTunnelHopRowStatus_Type()
)
mplsTunnelHopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopRowStatus.setStatus("current")


class _MplsTunnelHopStorageType_Type(StorageType):
    """Custom type mplsTunnelHopStorageType based on StorageType"""


_MplsTunnelHopStorageType_Object = MibTableColumn
mplsTunnelHopStorageType = _MplsTunnelHopStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 4, 1, 15),
    _MplsTunnelHopStorageType_Type()
)
mplsTunnelHopStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopStorageType.setStatus("current")


class _MplsTunnelResourceIndexNext_Type(Unsigned32):
    """Custom type mplsTunnelResourceIndexNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsTunnelResourceIndexNext_Type.__name__ = "Unsigned32"
_MplsTunnelResourceIndexNext_Object = MibScalar
mplsTunnelResourceIndexNext = _MplsTunnelResourceIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 5),
    _MplsTunnelResourceIndexNext_Type()
)
mplsTunnelResourceIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelResourceIndexNext.setStatus("current")
_MplsTunnelResourceTable_Object = MibTable
mplsTunnelResourceTable = _MplsTunnelResourceTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 6)
)
if mibBuilder.loadTexts:
    mplsTunnelResourceTable.setStatus("current")
_MplsTunnelResourceEntry_Object = MibTableRow
mplsTunnelResourceEntry = _MplsTunnelResourceEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 6, 1)
)
mplsTunnelResourceEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelResourceIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelResourceEntry.setStatus("current")


class _MplsTunnelResourceIndex_Type(Unsigned32):
    """Custom type mplsTunnelResourceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsTunnelResourceIndex_Type.__name__ = "Unsigned32"
_MplsTunnelResourceIndex_Object = MibTableColumn
mplsTunnelResourceIndex = _MplsTunnelResourceIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 6, 1, 1),
    _MplsTunnelResourceIndex_Type()
)
mplsTunnelResourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelResourceIndex.setStatus("current")
_MplsTunnelResourceMaxRate_Type = MplsBitRate
_MplsTunnelResourceMaxRate_Object = MibTableColumn
mplsTunnelResourceMaxRate = _MplsTunnelResourceMaxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 6, 1, 2),
    _MplsTunnelResourceMaxRate_Type()
)
mplsTunnelResourceMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelResourceMaxRate.setUnits("kilobits per second")
_MplsTunnelResourceMeanRate_Type = MplsBitRate
_MplsTunnelResourceMeanRate_Object = MibTableColumn
mplsTunnelResourceMeanRate = _MplsTunnelResourceMeanRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 6, 1, 3),
    _MplsTunnelResourceMeanRate_Type()
)
mplsTunnelResourceMeanRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceMeanRate.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelResourceMeanRate.setUnits("kilobits per second")
_MplsTunnelResourceMaxBurstSize_Type = MplsBurstSize
_MplsTunnelResourceMaxBurstSize_Object = MibTableColumn
mplsTunnelResourceMaxBurstSize = _MplsTunnelResourceMaxBurstSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 6, 1, 4),
    _MplsTunnelResourceMaxBurstSize_Type()
)
mplsTunnelResourceMaxBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceMaxBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelResourceMaxBurstSize.setUnits("bytes")
_MplsTunnelResourceMeanBurstSize_Type = MplsBurstSize
_MplsTunnelResourceMeanBurstSize_Object = MibTableColumn
mplsTunnelResourceMeanBurstSize = _MplsTunnelResourceMeanBurstSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 6, 1, 5),
    _MplsTunnelResourceMeanBurstSize_Type()
)
mplsTunnelResourceMeanBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceMeanBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelResourceMeanBurstSize.setUnits("bytes")
_MplsTunnelResourceExBurstSize_Type = MplsBurstSize
_MplsTunnelResourceExBurstSize_Object = MibTableColumn
mplsTunnelResourceExBurstSize = _MplsTunnelResourceExBurstSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 6, 1, 6),
    _MplsTunnelResourceExBurstSize_Type()
)
mplsTunnelResourceExBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceExBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelResourceExBurstSize.setUnits("bytes")


class _MplsTunnelResourceFrequency_Type(Integer32):
    """Custom type mplsTunnelResourceFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frequent", 2),
          ("unspecified", 1),
          ("veryFrequent", 3))
    )


_MplsTunnelResourceFrequency_Type.__name__ = "Integer32"
_MplsTunnelResourceFrequency_Object = MibTableColumn
mplsTunnelResourceFrequency = _MplsTunnelResourceFrequency_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 6, 1, 7),
    _MplsTunnelResourceFrequency_Type()
)
mplsTunnelResourceFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceFrequency.setStatus("current")


class _MplsTunnelResourceWeight_Type(Unsigned32):
    """Custom type mplsTunnelResourceWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsTunnelResourceWeight_Type.__name__ = "Unsigned32"
_MplsTunnelResourceWeight_Object = MibTableColumn
mplsTunnelResourceWeight = _MplsTunnelResourceWeight_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 6, 1, 8),
    _MplsTunnelResourceWeight_Type()
)
mplsTunnelResourceWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceWeight.setStatus("current")
_MplsTunnelResourceRowStatus_Type = RowStatus
_MplsTunnelResourceRowStatus_Object = MibTableColumn
mplsTunnelResourceRowStatus = _MplsTunnelResourceRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 6, 1, 9),
    _MplsTunnelResourceRowStatus_Type()
)
mplsTunnelResourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceRowStatus.setStatus("current")


class _MplsTunnelResourceStorageType_Type(StorageType):
    """Custom type mplsTunnelResourceStorageType based on StorageType"""


_MplsTunnelResourceStorageType_Object = MibTableColumn
mplsTunnelResourceStorageType = _MplsTunnelResourceStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 6, 1, 10),
    _MplsTunnelResourceStorageType_Type()
)
mplsTunnelResourceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceStorageType.setStatus("current")
_MplsTunnelARHopTable_Object = MibTable
mplsTunnelARHopTable = _MplsTunnelARHopTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 7)
)
if mibBuilder.loadTexts:
    mplsTunnelARHopTable.setStatus("current")
_MplsTunnelARHopEntry_Object = MibTableRow
mplsTunnelARHopEntry = _MplsTunnelARHopEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 7, 1)
)
mplsTunnelARHopEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelARHopListIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelARHopIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelARHopEntry.setStatus("current")
_MplsTunnelARHopListIndex_Type = MplsPathIndex
_MplsTunnelARHopListIndex_Object = MibTableColumn
mplsTunnelARHopListIndex = _MplsTunnelARHopListIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 7, 1, 1),
    _MplsTunnelARHopListIndex_Type()
)
mplsTunnelARHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelARHopListIndex.setStatus("current")
_MplsTunnelARHopIndex_Type = MplsPathIndex
_MplsTunnelARHopIndex_Object = MibTableColumn
mplsTunnelARHopIndex = _MplsTunnelARHopIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 7, 1, 2),
    _MplsTunnelARHopIndex_Type()
)
mplsTunnelARHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelARHopIndex.setStatus("current")


class _MplsTunnelARHopAddrType_Type(TeHopAddressType):
    """Custom type mplsTunnelARHopAddrType based on TeHopAddressType"""


_MplsTunnelARHopAddrType_Object = MibTableColumn
mplsTunnelARHopAddrType = _MplsTunnelARHopAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 7, 1, 3),
    _MplsTunnelARHopAddrType_Type()
)
mplsTunnelARHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopAddrType.setStatus("current")


class _MplsTunnelARHopIpAddr_Type(TeHopAddress):
    """Custom type mplsTunnelARHopIpAddr based on TeHopAddress"""
    defaultHexValue = "00000000"


_MplsTunnelARHopIpAddr_Object = MibTableColumn
mplsTunnelARHopIpAddr = _MplsTunnelARHopIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 7, 1, 4),
    _MplsTunnelARHopIpAddr_Type()
)
mplsTunnelARHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopIpAddr.setStatus("current")
_MplsTunnelARHopAddrUnnum_Type = TeHopAddressUnnum
_MplsTunnelARHopAddrUnnum_Object = MibTableColumn
mplsTunnelARHopAddrUnnum = _MplsTunnelARHopAddrUnnum_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 7, 1, 5),
    _MplsTunnelARHopAddrUnnum_Type()
)
mplsTunnelARHopAddrUnnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopAddrUnnum.setStatus("current")
_MplsTunnelARHopLspId_Type = MplsLSPID
_MplsTunnelARHopLspId_Object = MibTableColumn
mplsTunnelARHopLspId = _MplsTunnelARHopLspId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 7, 1, 6),
    _MplsTunnelARHopLspId_Type()
)
mplsTunnelARHopLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopLspId.setStatus("current")
_MplsTunnelCHopTable_Object = MibTable
mplsTunnelCHopTable = _MplsTunnelCHopTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 8)
)
if mibBuilder.loadTexts:
    mplsTunnelCHopTable.setStatus("current")
_MplsTunnelCHopEntry_Object = MibTableRow
mplsTunnelCHopEntry = _MplsTunnelCHopEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 8, 1)
)
mplsTunnelCHopEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelCHopListIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelCHopIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelCHopEntry.setStatus("current")
_MplsTunnelCHopListIndex_Type = MplsPathIndex
_MplsTunnelCHopListIndex_Object = MibTableColumn
mplsTunnelCHopListIndex = _MplsTunnelCHopListIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 8, 1, 1),
    _MplsTunnelCHopListIndex_Type()
)
mplsTunnelCHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelCHopListIndex.setStatus("current")
_MplsTunnelCHopIndex_Type = MplsPathIndex
_MplsTunnelCHopIndex_Object = MibTableColumn
mplsTunnelCHopIndex = _MplsTunnelCHopIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 8, 1, 2),
    _MplsTunnelCHopIndex_Type()
)
mplsTunnelCHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelCHopIndex.setStatus("current")


class _MplsTunnelCHopAddrType_Type(TeHopAddressType):
    """Custom type mplsTunnelCHopAddrType based on TeHopAddressType"""


_MplsTunnelCHopAddrType_Object = MibTableColumn
mplsTunnelCHopAddrType = _MplsTunnelCHopAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 8, 1, 3),
    _MplsTunnelCHopAddrType_Type()
)
mplsTunnelCHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopAddrType.setStatus("current")


class _MplsTunnelCHopIpAddr_Type(TeHopAddress):
    """Custom type mplsTunnelCHopIpAddr based on TeHopAddress"""
    defaultHexValue = "00000000"


_MplsTunnelCHopIpAddr_Object = MibTableColumn
mplsTunnelCHopIpAddr = _MplsTunnelCHopIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 8, 1, 4),
    _MplsTunnelCHopIpAddr_Type()
)
mplsTunnelCHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopIpAddr.setStatus("current")


class _MplsTunnelCHopIpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type mplsTunnelCHopIpPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 32


_MplsTunnelCHopIpPrefixLen_Object = MibTableColumn
mplsTunnelCHopIpPrefixLen = _MplsTunnelCHopIpPrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 8, 1, 5),
    _MplsTunnelCHopIpPrefixLen_Type()
)
mplsTunnelCHopIpPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopIpPrefixLen.setStatus("current")
_MplsTunnelCHopAsNumber_Type = TeHopAddressAS
_MplsTunnelCHopAsNumber_Object = MibTableColumn
mplsTunnelCHopAsNumber = _MplsTunnelCHopAsNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 8, 1, 6),
    _MplsTunnelCHopAsNumber_Type()
)
mplsTunnelCHopAsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopAsNumber.setStatus("current")
_MplsTunnelCHopAddrUnnum_Type = TeHopAddressUnnum
_MplsTunnelCHopAddrUnnum_Object = MibTableColumn
mplsTunnelCHopAddrUnnum = _MplsTunnelCHopAddrUnnum_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 8, 1, 7),
    _MplsTunnelCHopAddrUnnum_Type()
)
mplsTunnelCHopAddrUnnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopAddrUnnum.setStatus("current")
_MplsTunnelCHopLspId_Type = MplsLSPID
_MplsTunnelCHopLspId_Object = MibTableColumn
mplsTunnelCHopLspId = _MplsTunnelCHopLspId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 8, 1, 8),
    _MplsTunnelCHopLspId_Type()
)
mplsTunnelCHopLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopLspId.setStatus("current")


class _MplsTunnelCHopType_Type(Integer32):
    """Custom type mplsTunnelCHopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loose", 2),
          ("strict", 1))
    )


_MplsTunnelCHopType_Type.__name__ = "Integer32"
_MplsTunnelCHopType_Object = MibTableColumn
mplsTunnelCHopType = _MplsTunnelCHopType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 8, 1, 9),
    _MplsTunnelCHopType_Type()
)
mplsTunnelCHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopType.setStatus("current")
_MplsTunnelPerfTable_Object = MibTable
mplsTunnelPerfTable = _MplsTunnelPerfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 9)
)
if mibBuilder.loadTexts:
    mplsTunnelPerfTable.setStatus("current")
_MplsTunnelPerfEntry_Object = MibTableRow
mplsTunnelPerfEntry = _MplsTunnelPerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 9, 1)
)
if mibBuilder.loadTexts:
    mplsTunnelPerfEntry.setStatus("current")
_MplsTunnelPerfPackets_Type = Counter32
_MplsTunnelPerfPackets_Object = MibTableColumn
mplsTunnelPerfPackets = _MplsTunnelPerfPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 9, 1, 1),
    _MplsTunnelPerfPackets_Type()
)
mplsTunnelPerfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPerfPackets.setStatus("current")
_MplsTunnelPerfHCPackets_Type = Counter64
_MplsTunnelPerfHCPackets_Object = MibTableColumn
mplsTunnelPerfHCPackets = _MplsTunnelPerfHCPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 9, 1, 2),
    _MplsTunnelPerfHCPackets_Type()
)
mplsTunnelPerfHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPerfHCPackets.setStatus("current")
_MplsTunnelPerfErrors_Type = Counter32
_MplsTunnelPerfErrors_Object = MibTableColumn
mplsTunnelPerfErrors = _MplsTunnelPerfErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 9, 1, 3),
    _MplsTunnelPerfErrors_Type()
)
mplsTunnelPerfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPerfErrors.setStatus("current")
_MplsTunnelPerfBytes_Type = Counter32
_MplsTunnelPerfBytes_Object = MibTableColumn
mplsTunnelPerfBytes = _MplsTunnelPerfBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 9, 1, 4),
    _MplsTunnelPerfBytes_Type()
)
mplsTunnelPerfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPerfBytes.setStatus("current")
_MplsTunnelPerfHCBytes_Type = Counter64
_MplsTunnelPerfHCBytes_Object = MibTableColumn
mplsTunnelPerfHCBytes = _MplsTunnelPerfHCBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 9, 1, 5),
    _MplsTunnelPerfHCBytes_Type()
)
mplsTunnelPerfHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPerfHCBytes.setStatus("current")
_MplsTunnelCRLDPResTable_Object = MibTable
mplsTunnelCRLDPResTable = _MplsTunnelCRLDPResTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResTable.setStatus("current")
_MplsTunnelCRLDPResEntry_Object = MibTableRow
mplsTunnelCRLDPResEntry = _MplsTunnelCRLDPResEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 10, 1)
)
mplsTunnelCRLDPResEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelResourceIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResEntry.setStatus("current")
_MplsTunnelCRLDPResMeanBurstSize_Type = MplsBurstSize
_MplsTunnelCRLDPResMeanBurstSize_Object = MibTableColumn
mplsTunnelCRLDPResMeanBurstSize = _MplsTunnelCRLDPResMeanBurstSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 10, 1, 1),
    _MplsTunnelCRLDPResMeanBurstSize_Type()
)
mplsTunnelCRLDPResMeanBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResMeanBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResMeanBurstSize.setUnits("bytes")
_MplsTunnelCRLDPResExBurstSize_Type = MplsBurstSize
_MplsTunnelCRLDPResExBurstSize_Object = MibTableColumn
mplsTunnelCRLDPResExBurstSize = _MplsTunnelCRLDPResExBurstSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 10, 1, 2),
    _MplsTunnelCRLDPResExBurstSize_Type()
)
mplsTunnelCRLDPResExBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResExBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResExBurstSize.setUnits("bytes")


class _MplsTunnelCRLDPResFrequency_Type(Integer32):
    """Custom type mplsTunnelCRLDPResFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frequent", 2),
          ("unspecified", 1),
          ("veryFrequent", 3))
    )


_MplsTunnelCRLDPResFrequency_Type.__name__ = "Integer32"
_MplsTunnelCRLDPResFrequency_Object = MibTableColumn
mplsTunnelCRLDPResFrequency = _MplsTunnelCRLDPResFrequency_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 10, 1, 3),
    _MplsTunnelCRLDPResFrequency_Type()
)
mplsTunnelCRLDPResFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResFrequency.setStatus("current")


class _MplsTunnelCRLDPResWeight_Type(Unsigned32):
    """Custom type mplsTunnelCRLDPResWeight based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsTunnelCRLDPResWeight_Type.__name__ = "Unsigned32"
_MplsTunnelCRLDPResWeight_Object = MibTableColumn
mplsTunnelCRLDPResWeight = _MplsTunnelCRLDPResWeight_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 10, 1, 4),
    _MplsTunnelCRLDPResWeight_Type()
)
mplsTunnelCRLDPResWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResWeight.setStatus("current")


class _MplsTunnelCRLDPResFlags_Type(Unsigned32):
    """Custom type mplsTunnelCRLDPResFlags based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MplsTunnelCRLDPResFlags_Type.__name__ = "Unsigned32"
_MplsTunnelCRLDPResFlags_Object = MibTableColumn
mplsTunnelCRLDPResFlags = _MplsTunnelCRLDPResFlags_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 10, 1, 5),
    _MplsTunnelCRLDPResFlags_Type()
)
mplsTunnelCRLDPResFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResFlags.setStatus("current")
_MplsTunnelCRLDPResRowStatus_Type = RowStatus
_MplsTunnelCRLDPResRowStatus_Object = MibTableColumn
mplsTunnelCRLDPResRowStatus = _MplsTunnelCRLDPResRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 10, 1, 6),
    _MplsTunnelCRLDPResRowStatus_Type()
)
mplsTunnelCRLDPResRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResRowStatus.setStatus("current")


class _MplsTunnelCRLDPResStorageType_Type(StorageType):
    """Custom type mplsTunnelCRLDPResStorageType based on StorageType"""


_MplsTunnelCRLDPResStorageType_Object = MibTableColumn
mplsTunnelCRLDPResStorageType = _MplsTunnelCRLDPResStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 10, 1, 7),
    _MplsTunnelCRLDPResStorageType_Type()
)
mplsTunnelCRLDPResStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResStorageType.setStatus("current")


class _MplsTunnelNotificationEnable_Type(TruthValue):
    """Custom type mplsTunnelNotificationEnable based on TruthValue"""


_MplsTunnelNotificationEnable_Object = MibScalar
mplsTunnelNotificationEnable = _MplsTunnelNotificationEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 2, 11),
    _MplsTunnelNotificationEnable_Type()
)
mplsTunnelNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsTunnelNotificationEnable.setStatus("current")
_MplsTeConformance_ObjectIdentity = ObjectIdentity
mplsTeConformance = _MplsTeConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 3)
)
_MplsTeGroups_ObjectIdentity = ObjectIdentity
mplsTeGroups = _MplsTeGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 3, 1)
)
_MplsTeCompliances_ObjectIdentity = ObjectIdentity
mplsTeCompliances = _MplsTeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 3, 2)
)
mplsTunnelEntry.registerAugmentions(
    ("MPLS-TE-STD-MIB",
     "mplsTunnelPerfEntry")
)
mplsTunnelPerfEntry.setIndexNames(*mplsTunnelEntry.getIndexNames())

# Managed Objects groups

mplsTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 3, 1, 1)
)
mplsTunnelGroup.setObjects(
      *(("MPLS-TE-STD-MIB", "mplsTunnelIndexNext"),
        ("MPLS-TE-STD-MIB", "mplsTunnelName"),
        ("MPLS-TE-STD-MIB", "mplsTunnelDescr"),
        ("MPLS-TE-STD-MIB", "mplsTunnelOwner"),
        ("MPLS-TE-STD-MIB", "mplsTunnelXCPointer"),
        ("MPLS-TE-STD-MIB", "mplsTunnelIfIndex"),
        ("MPLS-TE-STD-MIB", "mplsTunnelHopTableIndex"),
        ("MPLS-TE-STD-MIB", "mplsTunnelARHopTableIndex"),
        ("MPLS-TE-STD-MIB", "mplsTunnelCHopTableIndex"),
        ("MPLS-TE-STD-MIB", "mplsTunnelAdminStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelOperStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelRowStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelNotificationEnable"),
        ("MPLS-TE-STD-MIB", "mplsTunnelStorageType"),
        ("MPLS-TE-STD-MIB", "mplsTunnelConfigured"),
        ("MPLS-TE-STD-MIB", "mplsTunnelActive"),
        ("MPLS-TE-STD-MIB", "mplsTunnelPrimaryInstance"),
        ("MPLS-TE-STD-MIB", "mplsTunnelPrimaryUpTime"),
        ("MPLS-TE-STD-MIB", "mplsTunnelPathChanges"),
        ("MPLS-TE-STD-MIB", "mplsTunnelLastPathChange"),
        ("MPLS-TE-STD-MIB", "mplsTunnelCreationTime"),
        ("MPLS-TE-STD-MIB", "mplsTunnelStateTransitions"),
        ("MPLS-TE-STD-MIB", "mplsTunnelIncludeAnyAffinity"),
        ("MPLS-TE-STD-MIB", "mplsTunnelIncludeAllAffinity"),
        ("MPLS-TE-STD-MIB", "mplsTunnelExcludeAnyAffinity"),
        ("MPLS-TE-STD-MIB", "mplsTunnelPerfPackets"),
        ("MPLS-TE-STD-MIB", "mplsTunnelPerfHCPackets"),
        ("MPLS-TE-STD-MIB", "mplsTunnelPerfErrors"),
        ("MPLS-TE-STD-MIB", "mplsTunnelPerfBytes"),
        ("MPLS-TE-STD-MIB", "mplsTunnelPerfHCBytes"),
        ("MPLS-TE-STD-MIB", "mplsTunnelResourcePointer"),
        ("MPLS-TE-STD-MIB", "mplsTunnelInstancePriority"),
        ("MPLS-TE-STD-MIB", "mplsTunnelPathInUse"),
        ("MPLS-TE-STD-MIB", "mplsTunnelRole"),
        ("MPLS-TE-STD-MIB", "mplsTunnelTotalUpTime"),
        ("MPLS-TE-STD-MIB", "mplsTunnelInstanceUpTime"),
        ("MPLS-TE-STD-MIB", "mplsTunnelResourceIndexNext"),
        ("MPLS-TE-STD-MIB", "mplsTunnelResourceMaxRate"),
        ("MPLS-TE-STD-MIB", "mplsTunnelResourceMeanRate"),
        ("MPLS-TE-STD-MIB", "mplsTunnelResourceMaxBurstSize"),
        ("MPLS-TE-STD-MIB", "mplsTunnelResourceMeanBurstSize"),
        ("MPLS-TE-STD-MIB", "mplsTunnelResourceExBurstSize"),
        ("MPLS-TE-STD-MIB", "mplsTunnelResourceFrequency"),
        ("MPLS-TE-STD-MIB", "mplsTunnelResourceWeight"),
        ("MPLS-TE-STD-MIB", "mplsTunnelResourceRowStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelResourceStorageType"),
        ("MPLS-TE-STD-MIB", "mplsTunnelARHopAddrType"),
        ("MPLS-TE-STD-MIB", "mplsTunnelARHopIpAddr"),
        ("MPLS-TE-STD-MIB", "mplsTunnelARHopAddrUnnum"),
        ("MPLS-TE-STD-MIB", "mplsTunnelARHopLspId"),
        ("MPLS-TE-STD-MIB", "mplsTunnelCHopAddrType"),
        ("MPLS-TE-STD-MIB", "mplsTunnelCHopIpAddr"),
        ("MPLS-TE-STD-MIB", "mplsTunnelCHopIpPrefixLen"),
        ("MPLS-TE-STD-MIB", "mplsTunnelCHopAsNumber"),
        ("MPLS-TE-STD-MIB", "mplsTunnelCHopAddrUnnum"),
        ("MPLS-TE-STD-MIB", "mplsTunnelCHopLspId"),
        ("MPLS-TE-STD-MIB", "mplsTunnelCHopType"))
)
if mibBuilder.loadTexts:
    mplsTunnelGroup.setStatus("current")

mplsTunnelManualGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 3, 1, 2)
)
mplsTunnelManualGroup.setObjects(
    ("MPLS-TE-STD-MIB", "mplsTunnelSignallingProto")
)
if mibBuilder.loadTexts:
    mplsTunnelManualGroup.setStatus("current")

mplsTunnelSignaledGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 3, 1, 3)
)
mplsTunnelSignaledGroup.setObjects(
      *(("MPLS-TE-STD-MIB", "mplsTunnelSetupPrio"),
        ("MPLS-TE-STD-MIB", "mplsTunnelHoldingPrio"),
        ("MPLS-TE-STD-MIB", "mplsTunnelSignallingProto"),
        ("MPLS-TE-STD-MIB", "mplsTunnelLocalProtectInUse"),
        ("MPLS-TE-STD-MIB", "mplsTunnelSessionAttributes"),
        ("MPLS-TE-STD-MIB", "mplsTunnelHopListIndexNext"),
        ("MPLS-TE-STD-MIB", "mplsTunnelHopAddrType"),
        ("MPLS-TE-STD-MIB", "mplsTunnelHopIpAddr"),
        ("MPLS-TE-STD-MIB", "mplsTunnelHopIpPrefixLen"),
        ("MPLS-TE-STD-MIB", "mplsTunnelHopAddrUnnum"),
        ("MPLS-TE-STD-MIB", "mplsTunnelHopAsNumber"),
        ("MPLS-TE-STD-MIB", "mplsTunnelHopLspId"),
        ("MPLS-TE-STD-MIB", "mplsTunnelHopType"),
        ("MPLS-TE-STD-MIB", "mplsTunnelHopInclude"),
        ("MPLS-TE-STD-MIB", "mplsTunnelHopPathOptionName"),
        ("MPLS-TE-STD-MIB", "mplsTunnelHopEntryPathComp"),
        ("MPLS-TE-STD-MIB", "mplsTunnelHopRowStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelHopStorageType"))
)
if mibBuilder.loadTexts:
    mplsTunnelSignaledGroup.setStatus("current")

mplsTunnelScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 3, 1, 4)
)
mplsTunnelScalarGroup.setObjects(
      *(("MPLS-TE-STD-MIB", "mplsTunnelConfigured"),
        ("MPLS-TE-STD-MIB", "mplsTunnelActive"),
        ("MPLS-TE-STD-MIB", "mplsTunnelTEDistProto"),
        ("MPLS-TE-STD-MIB", "mplsTunnelMaxHops"),
        ("MPLS-TE-STD-MIB", "mplsTunnelNotificationMaxRate"))
)
if mibBuilder.loadTexts:
    mplsTunnelScalarGroup.setStatus("current")

mplsTunnelIsIntfcGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 3, 1, 5)
)
mplsTunnelIsIntfcGroup.setObjects(
    ("MPLS-TE-STD-MIB", "mplsTunnelIsIf")
)
if mibBuilder.loadTexts:
    mplsTunnelIsIntfcGroup.setStatus("current")

mplsTunnelIsNotIntfcGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 3, 1, 6)
)
mplsTunnelIsNotIntfcGroup.setObjects(
    ("MPLS-TE-STD-MIB", "mplsTunnelIsIf")
)
if mibBuilder.loadTexts:
    mplsTunnelIsNotIntfcGroup.setStatus("current")

mplsTunnelCRLDPResOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 3, 1, 7)
)
mplsTunnelCRLDPResOptionalGroup.setObjects(
      *(("MPLS-TE-STD-MIB", "mplsTunnelCRLDPResMeanBurstSize"),
        ("MPLS-TE-STD-MIB", "mplsTunnelCRLDPResExBurstSize"),
        ("MPLS-TE-STD-MIB", "mplsTunnelCRLDPResFrequency"),
        ("MPLS-TE-STD-MIB", "mplsTunnelCRLDPResWeight"),
        ("MPLS-TE-STD-MIB", "mplsTunnelCRLDPResFlags"),
        ("MPLS-TE-STD-MIB", "mplsTunnelCRLDPResRowStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelCRLDPResStorageType"))
)
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResOptionalGroup.setStatus("current")


# Notification objects

mplsTunnelUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 0, 1)
)
mplsTunnelUp.setObjects(
      *(("MPLS-TE-STD-MIB", "mplsTunnelAdminStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    mplsTunnelUp.setStatus(
        "current"
    )

mplsTunnelDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 0, 2)
)
mplsTunnelDown.setObjects(
      *(("MPLS-TE-STD-MIB", "mplsTunnelAdminStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    mplsTunnelDown.setStatus(
        "current"
    )

mplsTunnelRerouted = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 0, 3)
)
mplsTunnelRerouted.setObjects(
      *(("MPLS-TE-STD-MIB", "mplsTunnelAdminStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    mplsTunnelRerouted.setStatus(
        "current"
    )

mplsTunnelReoptimized = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 0, 4)
)
mplsTunnelReoptimized.setObjects(
      *(("MPLS-TE-STD-MIB", "mplsTunnelAdminStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    mplsTunnelReoptimized.setStatus(
        "current"
    )


# Notifications groups

mplsTeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 3, 1, 8)
)
mplsTeNotificationGroup.setObjects(
      *(("MPLS-TE-STD-MIB", "mplsTunnelUp"),
        ("MPLS-TE-STD-MIB", "mplsTunnelDown"),
        ("MPLS-TE-STD-MIB", "mplsTunnelRerouted"),
        ("MPLS-TE-STD-MIB", "mplsTunnelReoptimized"))
)
if mibBuilder.loadTexts:
    mplsTeNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mplsTeModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mplsTeModuleFullCompliance.setStatus(
        "current"
    )

mplsTeModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    mplsTeModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-TE-STD-MIB",
    **{"mplsTeStdMIB": mplsTeStdMIB,
       "mplsTeNotifications": mplsTeNotifications,
       "mplsTunnelUp": mplsTunnelUp,
       "mplsTunnelDown": mplsTunnelDown,
       "mplsTunnelRerouted": mplsTunnelRerouted,
       "mplsTunnelReoptimized": mplsTunnelReoptimized,
       "mplsTeScalars": mplsTeScalars,
       "mplsTunnelConfigured": mplsTunnelConfigured,
       "mplsTunnelActive": mplsTunnelActive,
       "mplsTunnelTEDistProto": mplsTunnelTEDistProto,
       "mplsTunnelMaxHops": mplsTunnelMaxHops,
       "mplsTunnelNotificationMaxRate": mplsTunnelNotificationMaxRate,
       "mplsTeObjects": mplsTeObjects,
       "mplsTunnelIndexNext": mplsTunnelIndexNext,
       "mplsTunnelTable": mplsTunnelTable,
       "mplsTunnelEntry": mplsTunnelEntry,
       "mplsTunnelIndex": mplsTunnelIndex,
       "mplsTunnelInstance": mplsTunnelInstance,
       "mplsTunnelIngressLSRId": mplsTunnelIngressLSRId,
       "mplsTunnelEgressLSRId": mplsTunnelEgressLSRId,
       "mplsTunnelName": mplsTunnelName,
       "mplsTunnelDescr": mplsTunnelDescr,
       "mplsTunnelIsIf": mplsTunnelIsIf,
       "mplsTunnelIfIndex": mplsTunnelIfIndex,
       "mplsTunnelOwner": mplsTunnelOwner,
       "mplsTunnelRole": mplsTunnelRole,
       "mplsTunnelXCPointer": mplsTunnelXCPointer,
       "mplsTunnelSignallingProto": mplsTunnelSignallingProto,
       "mplsTunnelSetupPrio": mplsTunnelSetupPrio,
       "mplsTunnelHoldingPrio": mplsTunnelHoldingPrio,
       "mplsTunnelSessionAttributes": mplsTunnelSessionAttributes,
       "mplsTunnelLocalProtectInUse": mplsTunnelLocalProtectInUse,
       "mplsTunnelResourcePointer": mplsTunnelResourcePointer,
       "mplsTunnelPrimaryInstance": mplsTunnelPrimaryInstance,
       "mplsTunnelInstancePriority": mplsTunnelInstancePriority,
       "mplsTunnelHopTableIndex": mplsTunnelHopTableIndex,
       "mplsTunnelPathInUse": mplsTunnelPathInUse,
       "mplsTunnelARHopTableIndex": mplsTunnelARHopTableIndex,
       "mplsTunnelCHopTableIndex": mplsTunnelCHopTableIndex,
       "mplsTunnelIncludeAnyAffinity": mplsTunnelIncludeAnyAffinity,
       "mplsTunnelIncludeAllAffinity": mplsTunnelIncludeAllAffinity,
       "mplsTunnelExcludeAnyAffinity": mplsTunnelExcludeAnyAffinity,
       "mplsTunnelTotalUpTime": mplsTunnelTotalUpTime,
       "mplsTunnelInstanceUpTime": mplsTunnelInstanceUpTime,
       "mplsTunnelPrimaryUpTime": mplsTunnelPrimaryUpTime,
       "mplsTunnelPathChanges": mplsTunnelPathChanges,
       "mplsTunnelLastPathChange": mplsTunnelLastPathChange,
       "mplsTunnelCreationTime": mplsTunnelCreationTime,
       "mplsTunnelStateTransitions": mplsTunnelStateTransitions,
       "mplsTunnelAdminStatus": mplsTunnelAdminStatus,
       "mplsTunnelOperStatus": mplsTunnelOperStatus,
       "mplsTunnelRowStatus": mplsTunnelRowStatus,
       "mplsTunnelStorageType": mplsTunnelStorageType,
       "mplsTunnelHopListIndexNext": mplsTunnelHopListIndexNext,
       "mplsTunnelHopTable": mplsTunnelHopTable,
       "mplsTunnelHopEntry": mplsTunnelHopEntry,
       "mplsTunnelHopListIndex": mplsTunnelHopListIndex,
       "mplsTunnelHopPathOptionIndex": mplsTunnelHopPathOptionIndex,
       "mplsTunnelHopIndex": mplsTunnelHopIndex,
       "mplsTunnelHopAddrType": mplsTunnelHopAddrType,
       "mplsTunnelHopIpAddr": mplsTunnelHopIpAddr,
       "mplsTunnelHopIpPrefixLen": mplsTunnelHopIpPrefixLen,
       "mplsTunnelHopAsNumber": mplsTunnelHopAsNumber,
       "mplsTunnelHopAddrUnnum": mplsTunnelHopAddrUnnum,
       "mplsTunnelHopLspId": mplsTunnelHopLspId,
       "mplsTunnelHopType": mplsTunnelHopType,
       "mplsTunnelHopInclude": mplsTunnelHopInclude,
       "mplsTunnelHopPathOptionName": mplsTunnelHopPathOptionName,
       "mplsTunnelHopEntryPathComp": mplsTunnelHopEntryPathComp,
       "mplsTunnelHopRowStatus": mplsTunnelHopRowStatus,
       "mplsTunnelHopStorageType": mplsTunnelHopStorageType,
       "mplsTunnelResourceIndexNext": mplsTunnelResourceIndexNext,
       "mplsTunnelResourceTable": mplsTunnelResourceTable,
       "mplsTunnelResourceEntry": mplsTunnelResourceEntry,
       "mplsTunnelResourceIndex": mplsTunnelResourceIndex,
       "mplsTunnelResourceMaxRate": mplsTunnelResourceMaxRate,
       "mplsTunnelResourceMeanRate": mplsTunnelResourceMeanRate,
       "mplsTunnelResourceMaxBurstSize": mplsTunnelResourceMaxBurstSize,
       "mplsTunnelResourceMeanBurstSize": mplsTunnelResourceMeanBurstSize,
       "mplsTunnelResourceExBurstSize": mplsTunnelResourceExBurstSize,
       "mplsTunnelResourceFrequency": mplsTunnelResourceFrequency,
       "mplsTunnelResourceWeight": mplsTunnelResourceWeight,
       "mplsTunnelResourceRowStatus": mplsTunnelResourceRowStatus,
       "mplsTunnelResourceStorageType": mplsTunnelResourceStorageType,
       "mplsTunnelARHopTable": mplsTunnelARHopTable,
       "mplsTunnelARHopEntry": mplsTunnelARHopEntry,
       "mplsTunnelARHopListIndex": mplsTunnelARHopListIndex,
       "mplsTunnelARHopIndex": mplsTunnelARHopIndex,
       "mplsTunnelARHopAddrType": mplsTunnelARHopAddrType,
       "mplsTunnelARHopIpAddr": mplsTunnelARHopIpAddr,
       "mplsTunnelARHopAddrUnnum": mplsTunnelARHopAddrUnnum,
       "mplsTunnelARHopLspId": mplsTunnelARHopLspId,
       "mplsTunnelCHopTable": mplsTunnelCHopTable,
       "mplsTunnelCHopEntry": mplsTunnelCHopEntry,
       "mplsTunnelCHopListIndex": mplsTunnelCHopListIndex,
       "mplsTunnelCHopIndex": mplsTunnelCHopIndex,
       "mplsTunnelCHopAddrType": mplsTunnelCHopAddrType,
       "mplsTunnelCHopIpAddr": mplsTunnelCHopIpAddr,
       "mplsTunnelCHopIpPrefixLen": mplsTunnelCHopIpPrefixLen,
       "mplsTunnelCHopAsNumber": mplsTunnelCHopAsNumber,
       "mplsTunnelCHopAddrUnnum": mplsTunnelCHopAddrUnnum,
       "mplsTunnelCHopLspId": mplsTunnelCHopLspId,
       "mplsTunnelCHopType": mplsTunnelCHopType,
       "mplsTunnelPerfTable": mplsTunnelPerfTable,
       "mplsTunnelPerfEntry": mplsTunnelPerfEntry,
       "mplsTunnelPerfPackets": mplsTunnelPerfPackets,
       "mplsTunnelPerfHCPackets": mplsTunnelPerfHCPackets,
       "mplsTunnelPerfErrors": mplsTunnelPerfErrors,
       "mplsTunnelPerfBytes": mplsTunnelPerfBytes,
       "mplsTunnelPerfHCBytes": mplsTunnelPerfHCBytes,
       "mplsTunnelCRLDPResTable": mplsTunnelCRLDPResTable,
       "mplsTunnelCRLDPResEntry": mplsTunnelCRLDPResEntry,
       "mplsTunnelCRLDPResMeanBurstSize": mplsTunnelCRLDPResMeanBurstSize,
       "mplsTunnelCRLDPResExBurstSize": mplsTunnelCRLDPResExBurstSize,
       "mplsTunnelCRLDPResFrequency": mplsTunnelCRLDPResFrequency,
       "mplsTunnelCRLDPResWeight": mplsTunnelCRLDPResWeight,
       "mplsTunnelCRLDPResFlags": mplsTunnelCRLDPResFlags,
       "mplsTunnelCRLDPResRowStatus": mplsTunnelCRLDPResRowStatus,
       "mplsTunnelCRLDPResStorageType": mplsTunnelCRLDPResStorageType,
       "mplsTunnelNotificationEnable": mplsTunnelNotificationEnable,
       "mplsTeConformance": mplsTeConformance,
       "mplsTeGroups": mplsTeGroups,
       "mplsTunnelGroup": mplsTunnelGroup,
       "mplsTunnelManualGroup": mplsTunnelManualGroup,
       "mplsTunnelSignaledGroup": mplsTunnelSignaledGroup,
       "mplsTunnelScalarGroup": mplsTunnelScalarGroup,
       "mplsTunnelIsIntfcGroup": mplsTunnelIsIntfcGroup,
       "mplsTunnelIsNotIntfcGroup": mplsTunnelIsNotIntfcGroup,
       "mplsTunnelCRLDPResOptionalGroup": mplsTunnelCRLDPResOptionalGroup,
       "mplsTeNotificationGroup": mplsTeNotificationGroup,
       "mplsTeCompliances": mplsTeCompliances,
       "mplsTeModuleFullCompliance": mplsTeModuleFullCompliance,
       "mplsTeModuleReadOnlyCompliance": mplsTeModuleReadOnlyCompliance}
)

# SNMP MIB module (HP-SN-MPLS-TE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SN-MIBS
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:48 2024
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

(MplsBitRate,
 MplsBurstSize,
 MplsLSPID,
 MplsLsrIdentifier,
 MplsPathIndex,
 MplsPathIndexOrZero,
 MplsTunnelAffinity,
 MplsTunnelIndex,
 MplsTunnelInstanceIndex,
 mplsMIB) = mibBuilder.importSymbols(
    "HP-SN-MPLS-TC-MIB",
    "MplsBitRate",
    "MplsBurstSize",
    "MplsLSPID",
    "MplsLsrIdentifier",
    "MplsPathIndex",
    "MplsPathIndexOrZero",
    "MplsTunnelAffinity",
    "MplsTunnelIndex",
    "MplsTunnelInstanceIndex",
    "mplsMIB")

(snMpls,) = mibBuilder.importSymbols(
    "HP-SN-ROOT-MIB",
    "snMpls")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

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

mplsTeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3)
)
mplsTeMIB.setRevisions(
        ("2002-01-04 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsTeScalars_ObjectIdentity = ObjectIdentity
mplsTeScalars = _MplsTeScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 1)
)
_MplsTunnelConfigured_Type = Unsigned32
_MplsTunnelConfigured_Object = MibScalar
mplsTunnelConfigured = _MplsTunnelConfigured_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 1, 1),
    _MplsTunnelConfigured_Type()
)
mplsTunnelConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelConfigured.setStatus("current")
_MplsTunnelActive_Type = Unsigned32
_MplsTunnelActive_Object = MibScalar
mplsTunnelActive = _MplsTunnelActive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 1, 3),
    _MplsTunnelTEDistProto_Type()
)
mplsTunnelTEDistProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelTEDistProto.setStatus("current")
_MplsTunnelMaxHops_Type = Unsigned32
_MplsTunnelMaxHops_Object = MibScalar
mplsTunnelMaxHops = _MplsTunnelMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 1, 4),
    _MplsTunnelMaxHops_Type()
)
mplsTunnelMaxHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelMaxHops.setStatus("current")
_MplsTeObjects_ObjectIdentity = ObjectIdentity
mplsTeObjects = _MplsTeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2)
)


class _MplsTunnelIndexNext_Type(Integer32):
    """Custom type mplsTunnelIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsTunnelIndexNext_Type.__name__ = "Integer32"
_MplsTunnelIndexNext_Object = MibScalar
mplsTunnelIndexNext = _MplsTunnelIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 1),
    _MplsTunnelIndexNext_Type()
)
mplsTunnelIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelIndexNext.setStatus("current")
_MplsTunnelTable_Object = MibTable
mplsTunnelTable = _MplsTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2)
)
if mibBuilder.loadTexts:
    mplsTunnelTable.setStatus("current")
_MplsTunnelEntry_Object = MibTableRow
mplsTunnelEntry = _MplsTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1)
)
mplsTunnelEntry.setIndexNames(
    (0, "HP-SN-MPLS-TE-MIB", "mplsTunnelIndex"),
    (0, "HP-SN-MPLS-TE-MIB", "mplsTunnelInstance"),
    (0, "HP-SN-MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
    (0, "HP-SN-MPLS-TE-MIB", "mplsTunnelEgressLSRId"),
)
if mibBuilder.loadTexts:
    mplsTunnelEntry.setStatus("current")
_MplsTunnelIndex_Type = MplsTunnelIndex
_MplsTunnelIndex_Object = MibTableColumn
mplsTunnelIndex = _MplsTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 1),
    _MplsTunnelIndex_Type()
)
mplsTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelIndex.setStatus("current")
_MplsTunnelInstance_Type = MplsTunnelInstanceIndex
_MplsTunnelInstance_Object = MibTableColumn
mplsTunnelInstance = _MplsTunnelInstance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 2),
    _MplsTunnelInstance_Type()
)
mplsTunnelInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelInstance.setStatus("current")
_MplsTunnelIngressLSRId_Type = MplsLsrIdentifier
_MplsTunnelIngressLSRId_Object = MibTableColumn
mplsTunnelIngressLSRId = _MplsTunnelIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 3),
    _MplsTunnelIngressLSRId_Type()
)
mplsTunnelIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelIngressLSRId.setStatus("current")
_MplsTunnelEgressLSRId_Type = MplsLsrIdentifier
_MplsTunnelEgressLSRId_Object = MibTableColumn
mplsTunnelEgressLSRId = _MplsTunnelEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 4),
    _MplsTunnelEgressLSRId_Type()
)
mplsTunnelEgressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelEgressLSRId.setStatus("current")
_MplsTunnelName_Type = DisplayString
_MplsTunnelName_Object = MibTableColumn
mplsTunnelName = _MplsTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 5),
    _MplsTunnelName_Type()
)
mplsTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelName.setStatus("current")
_MplsTunnelDescr_Type = DisplayString
_MplsTunnelDescr_Object = MibTableColumn
mplsTunnelDescr = _MplsTunnelDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 6),
    _MplsTunnelDescr_Type()
)
mplsTunnelDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelDescr.setStatus("current")


class _MplsTunnelIsIf_Type(TruthValue):
    """Custom type mplsTunnelIsIf based on TruthValue"""


_MplsTunnelIsIf_Object = MibTableColumn
mplsTunnelIsIf = _MplsTunnelIsIf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 7),
    _MplsTunnelIsIf_Type()
)
mplsTunnelIsIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelIsIf.setStatus("current")
_MplsTunnelIfIndex_Type = InterfaceIndexOrZero
_MplsTunnelIfIndex_Object = MibTableColumn
mplsTunnelIfIndex = _MplsTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 8),
    _MplsTunnelIfIndex_Type()
)
mplsTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelIfIndex.setStatus("current")
_MplsTunnelXCPointer_Type = RowPointer
_MplsTunnelXCPointer_Object = MibTableColumn
mplsTunnelXCPointer = _MplsTunnelXCPointer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 10),
    _MplsTunnelSignallingProto_Type()
)
mplsTunnelSignallingProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSignallingProto.setStatus("current")


class _MplsTunnelSetupPrio_Type(Integer32):
    """Custom type mplsTunnelSetupPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsTunnelSetupPrio_Type.__name__ = "Integer32"
_MplsTunnelSetupPrio_Object = MibTableColumn
mplsTunnelSetupPrio = _MplsTunnelSetupPrio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 11),
    _MplsTunnelSetupPrio_Type()
)
mplsTunnelSetupPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSetupPrio.setStatus("current")


class _MplsTunnelHoldingPrio_Type(Integer32):
    """Custom type mplsTunnelHoldingPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsTunnelHoldingPrio_Type.__name__ = "Integer32"
_MplsTunnelHoldingPrio_Object = MibTableColumn
mplsTunnelHoldingPrio = _MplsTunnelHoldingPrio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 13),
    _MplsTunnelSessionAttributes_Type()
)
mplsTunnelSessionAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSessionAttributes.setStatus("current")


class _MplsTunnelOwner_Type(Integer32):
    """Custom type mplsTunnelOwner based on Integer32"""
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
        *(("admin", 1),
          ("crldp", 3),
          ("other", 5),
          ("policyAgent", 4),
          ("rsvp", 2))
    )


_MplsTunnelOwner_Type.__name__ = "Integer32"
_MplsTunnelOwner_Object = MibTableColumn
mplsTunnelOwner = _MplsTunnelOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 14),
    _MplsTunnelOwner_Type()
)
mplsTunnelOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelOwner.setStatus("current")
_MplsTunnelLocalProtectInUse_Type = TruthValue
_MplsTunnelLocalProtectInUse_Object = MibTableColumn
mplsTunnelLocalProtectInUse = _MplsTunnelLocalProtectInUse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 15),
    _MplsTunnelLocalProtectInUse_Type()
)
mplsTunnelLocalProtectInUse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelLocalProtectInUse.setStatus("current")
_MplsTunnelResourcePointer_Type = RowPointer
_MplsTunnelResourcePointer_Object = MibTableColumn
mplsTunnelResourcePointer = _MplsTunnelResourcePointer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 16),
    _MplsTunnelResourcePointer_Type()
)
mplsTunnelResourcePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourcePointer.setStatus("current")


class _MplsTunnelInstancePriority_Type(Unsigned32):
    """Custom type mplsTunnelInstancePriority based on Unsigned32"""
    defaultValue = 0


_MplsTunnelInstancePriority_Object = MibTableColumn
mplsTunnelInstancePriority = _MplsTunnelInstancePriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 17),
    _MplsTunnelInstancePriority_Type()
)
mplsTunnelInstancePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelInstancePriority.setStatus("current")
_MplsTunnelHopTableIndex_Type = MplsPathIndexOrZero
_MplsTunnelHopTableIndex_Object = MibTableColumn
mplsTunnelHopTableIndex = _MplsTunnelHopTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 18),
    _MplsTunnelHopTableIndex_Type()
)
mplsTunnelHopTableIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopTableIndex.setStatus("current")
_MplsTunnelARHopTableIndex_Type = MplsPathIndexOrZero
_MplsTunnelARHopTableIndex_Object = MibTableColumn
mplsTunnelARHopTableIndex = _MplsTunnelARHopTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 19),
    _MplsTunnelARHopTableIndex_Type()
)
mplsTunnelARHopTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopTableIndex.setStatus("current")
_MplsTunnelCHopTableIndex_Type = MplsPathIndexOrZero
_MplsTunnelCHopTableIndex_Object = MibTableColumn
mplsTunnelCHopTableIndex = _MplsTunnelCHopTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 20),
    _MplsTunnelCHopTableIndex_Type()
)
mplsTunnelCHopTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopTableIndex.setStatus("current")
_MplsTunnelPrimaryInstance_Type = MplsTunnelInstanceIndex
_MplsTunnelPrimaryInstance_Object = MibTableColumn
mplsTunnelPrimaryInstance = _MplsTunnelPrimaryInstance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 21),
    _MplsTunnelPrimaryInstance_Type()
)
mplsTunnelPrimaryInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPrimaryInstance.setStatus("current")
_MplsTunnelPrimaryTimeUp_Type = TimeTicks
_MplsTunnelPrimaryTimeUp_Object = MibTableColumn
mplsTunnelPrimaryTimeUp = _MplsTunnelPrimaryTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 22),
    _MplsTunnelPrimaryTimeUp_Type()
)
mplsTunnelPrimaryTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPrimaryTimeUp.setStatus("current")
_MplsTunnelPathChanges_Type = Counter32
_MplsTunnelPathChanges_Object = MibTableColumn
mplsTunnelPathChanges = _MplsTunnelPathChanges_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 23),
    _MplsTunnelPathChanges_Type()
)
mplsTunnelPathChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPathChanges.setStatus("current")
_MplsTunnelLastPathChange_Type = TimeTicks
_MplsTunnelLastPathChange_Object = MibTableColumn
mplsTunnelLastPathChange = _MplsTunnelLastPathChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 24),
    _MplsTunnelLastPathChange_Type()
)
mplsTunnelLastPathChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelLastPathChange.setStatus("current")
_MplsTunnelCreationTime_Type = TimeStamp
_MplsTunnelCreationTime_Object = MibTableColumn
mplsTunnelCreationTime = _MplsTunnelCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 25),
    _MplsTunnelCreationTime_Type()
)
mplsTunnelCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCreationTime.setStatus("current")
_MplsTunnelStateTransitions_Type = Counter32
_MplsTunnelStateTransitions_Object = MibTableColumn
mplsTunnelStateTransitions = _MplsTunnelStateTransitions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 26),
    _MplsTunnelStateTransitions_Type()
)
mplsTunnelStateTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelStateTransitions.setStatus("current")
_MplsTunnelIncludeAnyAffinity_Type = MplsTunnelAffinity
_MplsTunnelIncludeAnyAffinity_Object = MibTableColumn
mplsTunnelIncludeAnyAffinity = _MplsTunnelIncludeAnyAffinity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 27),
    _MplsTunnelIncludeAnyAffinity_Type()
)
mplsTunnelIncludeAnyAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelIncludeAnyAffinity.setStatus("current")
_MplsTunnelIncludeAllAffinity_Type = MplsTunnelAffinity
_MplsTunnelIncludeAllAffinity_Object = MibTableColumn
mplsTunnelIncludeAllAffinity = _MplsTunnelIncludeAllAffinity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 28),
    _MplsTunnelIncludeAllAffinity_Type()
)
mplsTunnelIncludeAllAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelIncludeAllAffinity.setStatus("current")
_MplsTunnelExcludeAllAffinity_Type = MplsTunnelAffinity
_MplsTunnelExcludeAllAffinity_Object = MibTableColumn
mplsTunnelExcludeAllAffinity = _MplsTunnelExcludeAllAffinity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 29),
    _MplsTunnelExcludeAllAffinity_Type()
)
mplsTunnelExcludeAllAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExcludeAllAffinity.setStatus("current")
_MplsTunnelPathInUse_Type = MplsPathIndexOrZero
_MplsTunnelPathInUse_Object = MibTableColumn
mplsTunnelPathInUse = _MplsTunnelPathInUse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 30),
    _MplsTunnelPathInUse_Type()
)
mplsTunnelPathInUse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelPathInUse.setStatus("current")


class _MplsTunnelRole_Type(Integer32):
    """Custom type mplsTunnelRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("head", 1),
          ("tail", 3),
          ("transit", 2))
    )


_MplsTunnelRole_Type.__name__ = "Integer32"
_MplsTunnelRole_Object = MibTableColumn
mplsTunnelRole = _MplsTunnelRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 31),
    _MplsTunnelRole_Type()
)
mplsTunnelRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelRole.setStatus("current")
_MplsTunnelTotalUpTime_Type = TimeTicks
_MplsTunnelTotalUpTime_Object = MibTableColumn
mplsTunnelTotalUpTime = _MplsTunnelTotalUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 32),
    _MplsTunnelTotalUpTime_Type()
)
mplsTunnelTotalUpTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelTotalUpTime.setStatus("current")
_MplsTunnelInstanceUpTime_Type = TimeTicks
_MplsTunnelInstanceUpTime_Object = MibTableColumn
mplsTunnelInstanceUpTime = _MplsTunnelInstanceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 33),
    _MplsTunnelInstanceUpTime_Type()
)
mplsTunnelInstanceUpTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelInstanceUpTime.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 34),
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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 35),
    _MplsTunnelOperStatus_Type()
)
mplsTunnelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelOperStatus.setStatus("current")
_MplsTunnelRowStatus_Type = RowStatus
_MplsTunnelRowStatus_Object = MibTableColumn
mplsTunnelRowStatus = _MplsTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 36),
    _MplsTunnelRowStatus_Type()
)
mplsTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelRowStatus.setStatus("current")
_MplsTunnelStorageType_Type = StorageType
_MplsTunnelStorageType_Object = MibTableColumn
mplsTunnelStorageType = _MplsTunnelStorageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 2, 1, 37),
    _MplsTunnelStorageType_Type()
)
mplsTunnelStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelStorageType.setStatus("current")


class _MplsTunnelHopListIndexNext_Type(Unsigned32):
    """Custom type mplsTunnelHopListIndexNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsTunnelHopListIndexNext_Type.__name__ = "Unsigned32"
_MplsTunnelHopListIndexNext_Object = MibScalar
mplsTunnelHopListIndexNext = _MplsTunnelHopListIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 3),
    _MplsTunnelHopListIndexNext_Type()
)
mplsTunnelHopListIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelHopListIndexNext.setStatus("current")
_MplsTunnelHopTable_Object = MibTable
mplsTunnelHopTable = _MplsTunnelHopTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 4)
)
if mibBuilder.loadTexts:
    mplsTunnelHopTable.setStatus("current")
_MplsTunnelHopEntry_Object = MibTableRow
mplsTunnelHopEntry = _MplsTunnelHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 4, 1)
)
mplsTunnelHopEntry.setIndexNames(
    (0, "HP-SN-MPLS-TE-MIB", "mplsTunnelHopListIndex"),
    (0, "HP-SN-MPLS-TE-MIB", "mplsTunnelHopPathOptionIndex"),
    (0, "HP-SN-MPLS-TE-MIB", "mplsTunnelHopIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelHopEntry.setStatus("current")
_MplsTunnelHopListIndex_Type = MplsPathIndex
_MplsTunnelHopListIndex_Object = MibTableColumn
mplsTunnelHopListIndex = _MplsTunnelHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 4, 1, 1),
    _MplsTunnelHopListIndex_Type()
)
mplsTunnelHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelHopListIndex.setStatus("current")
_MplsTunnelHopPathOptionIndex_Type = MplsPathIndex
_MplsTunnelHopPathOptionIndex_Object = MibTableColumn
mplsTunnelHopPathOptionIndex = _MplsTunnelHopPathOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 4, 1, 2),
    _MplsTunnelHopPathOptionIndex_Type()
)
mplsTunnelHopPathOptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelHopPathOptionIndex.setStatus("current")
_MplsTunnelHopIndex_Type = MplsPathIndex
_MplsTunnelHopIndex_Object = MibTableColumn
mplsTunnelHopIndex = _MplsTunnelHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 4, 1, 3),
    _MplsTunnelHopIndex_Type()
)
mplsTunnelHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelHopIndex.setStatus("current")


class _MplsTunnelHopAddrType_Type(Integer32):
    """Custom type mplsTunnelHopAddrType based on Integer32"""
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
        *(("asNumber", 3),
          ("ipV4", 1),
          ("ipV6", 2),
          ("lspid", 4))
    )


_MplsTunnelHopAddrType_Type.__name__ = "Integer32"
_MplsTunnelHopAddrType_Object = MibTableColumn
mplsTunnelHopAddrType = _MplsTunnelHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 4, 1, 4),
    _MplsTunnelHopAddrType_Type()
)
mplsTunnelHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopAddrType.setStatus("current")
_MplsTunnelHopIpv4Addr_Type = InetAddressIPv4
_MplsTunnelHopIpv4Addr_Object = MibTableColumn
mplsTunnelHopIpv4Addr = _MplsTunnelHopIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 4, 1, 5),
    _MplsTunnelHopIpv4Addr_Type()
)
mplsTunnelHopIpv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopIpv4Addr.setStatus("current")


class _MplsTunnelHopIpv4PrefixLen_Type(Unsigned32):
    """Custom type mplsTunnelHopIpv4PrefixLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_MplsTunnelHopIpv4PrefixLen_Type.__name__ = "Unsigned32"
_MplsTunnelHopIpv4PrefixLen_Object = MibTableColumn
mplsTunnelHopIpv4PrefixLen = _MplsTunnelHopIpv4PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 4, 1, 6),
    _MplsTunnelHopIpv4PrefixLen_Type()
)
mplsTunnelHopIpv4PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopIpv4PrefixLen.setStatus("current")
_MplsTunnelHopIpv6Addr_Type = InetAddressIPv6
_MplsTunnelHopIpv6Addr_Object = MibTableColumn
mplsTunnelHopIpv6Addr = _MplsTunnelHopIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 4, 1, 7),
    _MplsTunnelHopIpv6Addr_Type()
)
mplsTunnelHopIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopIpv6Addr.setStatus("current")


class _MplsTunnelHopIpv6PrefixLen_Type(Unsigned32):
    """Custom type mplsTunnelHopIpv6PrefixLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MplsTunnelHopIpv6PrefixLen_Type.__name__ = "Unsigned32"
_MplsTunnelHopIpv6PrefixLen_Object = MibTableColumn
mplsTunnelHopIpv6PrefixLen = _MplsTunnelHopIpv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 4, 1, 8),
    _MplsTunnelHopIpv6PrefixLen_Type()
)
mplsTunnelHopIpv6PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopIpv6PrefixLen.setStatus("current")


class _MplsTunnelHopAsNumber_Type(Unsigned32):
    """Custom type mplsTunnelHopAsNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsTunnelHopAsNumber_Type.__name__ = "Unsigned32"
_MplsTunnelHopAsNumber_Object = MibTableColumn
mplsTunnelHopAsNumber = _MplsTunnelHopAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 4, 1, 9),
    _MplsTunnelHopAsNumber_Type()
)
mplsTunnelHopAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopAsNumber.setStatus("current")
_MplsTunnelHopLspId_Type = MplsLSPID
_MplsTunnelHopLspId_Object = MibTableColumn
mplsTunnelHopLspId = _MplsTunnelHopLspId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 4, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 4, 1, 11),
    _MplsTunnelHopType_Type()
)
mplsTunnelHopType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopType.setStatus("current")


class _MplsTunnelHopIncludeExclude_Type(Integer32):
    """Custom type mplsTunnelHopIncludeExclude based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_MplsTunnelHopIncludeExclude_Type.__name__ = "Integer32"
_MplsTunnelHopIncludeExclude_Object = MibTableColumn
mplsTunnelHopIncludeExclude = _MplsTunnelHopIncludeExclude_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 4, 1, 12),
    _MplsTunnelHopIncludeExclude_Type()
)
mplsTunnelHopIncludeExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopIncludeExclude.setStatus("current")
_MplsTunnelHopPathOptionName_Type = DisplayString
_MplsTunnelHopPathOptionName_Object = MibTableColumn
mplsTunnelHopPathOptionName = _MplsTunnelHopPathOptionName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 4, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 4, 1, 14),
    _MplsTunnelHopEntryPathComp_Type()
)
mplsTunnelHopEntryPathComp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopEntryPathComp.setStatus("current")
_MplsTunnelHopRowStatus_Type = RowStatus
_MplsTunnelHopRowStatus_Object = MibTableColumn
mplsTunnelHopRowStatus = _MplsTunnelHopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 4, 1, 15),
    _MplsTunnelHopRowStatus_Type()
)
mplsTunnelHopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopRowStatus.setStatus("current")
_MplsTunnelHopStorageType_Type = StorageType
_MplsTunnelHopStorageType_Object = MibTableColumn
mplsTunnelHopStorageType = _MplsTunnelHopStorageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 4, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 5),
    _MplsTunnelResourceIndexNext_Type()
)
mplsTunnelResourceIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelResourceIndexNext.setStatus("current")
_MplsTunnelResourceTable_Object = MibTable
mplsTunnelResourceTable = _MplsTunnelResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 6)
)
if mibBuilder.loadTexts:
    mplsTunnelResourceTable.setStatus("current")
_MplsTunnelResourceEntry_Object = MibTableRow
mplsTunnelResourceEntry = _MplsTunnelResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 6, 1)
)
mplsTunnelResourceEntry.setIndexNames(
    (0, "HP-SN-MPLS-TE-MIB", "mplsTunnelResourceIndex"),
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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 6, 1, 1),
    _MplsTunnelResourceIndex_Type()
)
mplsTunnelResourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelResourceIndex.setStatus("current")
_MplsTunnelResourceMaxRate_Type = MplsBitRate
_MplsTunnelResourceMaxRate_Object = MibTableColumn
mplsTunnelResourceMaxRate = _MplsTunnelResourceMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 6, 1, 2),
    _MplsTunnelResourceMaxRate_Type()
)
mplsTunnelResourceMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelResourceMaxRate.setUnits("bits per second")
_MplsTunnelResourceMeanRate_Type = MplsBitRate
_MplsTunnelResourceMeanRate_Object = MibTableColumn
mplsTunnelResourceMeanRate = _MplsTunnelResourceMeanRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 6, 1, 3),
    _MplsTunnelResourceMeanRate_Type()
)
mplsTunnelResourceMeanRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceMeanRate.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelResourceMeanRate.setUnits("bits per second")
_MplsTunnelResourceMaxBurstSize_Type = MplsBurstSize
_MplsTunnelResourceMaxBurstSize_Object = MibTableColumn
mplsTunnelResourceMaxBurstSize = _MplsTunnelResourceMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 6, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 6, 1, 5),
    _MplsTunnelResourceMeanBurstSize_Type()
)
mplsTunnelResourceMeanBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceMeanBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelResourceMeanBurstSize.setUnits("bytes")
_MplsTunnelResourceExcessBurstSize_Type = MplsBurstSize
_MplsTunnelResourceExcessBurstSize_Object = MibTableColumn
mplsTunnelResourceExcessBurstSize = _MplsTunnelResourceExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 6, 1, 6),
    _MplsTunnelResourceExcessBurstSize_Type()
)
mplsTunnelResourceExcessBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceExcessBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelResourceExcessBurstSize.setUnits("bytes")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 6, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 6, 1, 8),
    _MplsTunnelResourceWeight_Type()
)
mplsTunnelResourceWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceWeight.setStatus("current")
_MplsTunnelResourceRowStatus_Type = RowStatus
_MplsTunnelResourceRowStatus_Object = MibTableColumn
mplsTunnelResourceRowStatus = _MplsTunnelResourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 6, 1, 9),
    _MplsTunnelResourceRowStatus_Type()
)
mplsTunnelResourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceRowStatus.setStatus("current")
_MplsTunnelResourceStorageType_Type = StorageType
_MplsTunnelResourceStorageType_Object = MibTableColumn
mplsTunnelResourceStorageType = _MplsTunnelResourceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 6, 1, 10),
    _MplsTunnelResourceStorageType_Type()
)
mplsTunnelResourceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceStorageType.setStatus("current")
_MplsTunnelARHopTable_Object = MibTable
mplsTunnelARHopTable = _MplsTunnelARHopTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 7)
)
if mibBuilder.loadTexts:
    mplsTunnelARHopTable.setStatus("current")
_MplsTunnelARHopEntry_Object = MibTableRow
mplsTunnelARHopEntry = _MplsTunnelARHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 7, 1)
)
mplsTunnelARHopEntry.setIndexNames(
    (0, "HP-SN-MPLS-TE-MIB", "mplsTunnelARHopListIndex"),
    (0, "HP-SN-MPLS-TE-MIB", "mplsTunnelARHopIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelARHopEntry.setStatus("current")
_MplsTunnelARHopListIndex_Type = MplsPathIndex
_MplsTunnelARHopListIndex_Object = MibTableColumn
mplsTunnelARHopListIndex = _MplsTunnelARHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 7, 1, 1),
    _MplsTunnelARHopListIndex_Type()
)
mplsTunnelARHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelARHopListIndex.setStatus("current")
_MplsTunnelARHopIndex_Type = MplsPathIndex
_MplsTunnelARHopIndex_Object = MibTableColumn
mplsTunnelARHopIndex = _MplsTunnelARHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 7, 1, 2),
    _MplsTunnelARHopIndex_Type()
)
mplsTunnelARHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelARHopIndex.setStatus("current")


class _MplsTunnelARHopAddrType_Type(Integer32):
    """Custom type mplsTunnelARHopAddrType based on Integer32"""
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
        *(("asNumber", 3),
          ("ipV4", 1),
          ("ipV6", 2),
          ("lspId", 4))
    )


_MplsTunnelARHopAddrType_Type.__name__ = "Integer32"
_MplsTunnelARHopAddrType_Object = MibTableColumn
mplsTunnelARHopAddrType = _MplsTunnelARHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 7, 1, 3),
    _MplsTunnelARHopAddrType_Type()
)
mplsTunnelARHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopAddrType.setStatus("current")
_MplsTunnelARHopIpv4Addr_Type = InetAddressIPv4
_MplsTunnelARHopIpv4Addr_Object = MibTableColumn
mplsTunnelARHopIpv4Addr = _MplsTunnelARHopIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 7, 1, 4),
    _MplsTunnelARHopIpv4Addr_Type()
)
mplsTunnelARHopIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopIpv4Addr.setStatus("current")


class _MplsTunnelARHopIpv4PrefixLen_Type(Unsigned32):
    """Custom type mplsTunnelARHopIpv4PrefixLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_MplsTunnelARHopIpv4PrefixLen_Type.__name__ = "Unsigned32"
_MplsTunnelARHopIpv4PrefixLen_Object = MibTableColumn
mplsTunnelARHopIpv4PrefixLen = _MplsTunnelARHopIpv4PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 7, 1, 5),
    _MplsTunnelARHopIpv4PrefixLen_Type()
)
mplsTunnelARHopIpv4PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopIpv4PrefixLen.setStatus("current")
_MplsTunnelARHopIpv6Addr_Type = InetAddressIPv6
_MplsTunnelARHopIpv6Addr_Object = MibTableColumn
mplsTunnelARHopIpv6Addr = _MplsTunnelARHopIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 7, 1, 6),
    _MplsTunnelARHopIpv6Addr_Type()
)
mplsTunnelARHopIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopIpv6Addr.setStatus("current")


class _MplsTunnelARHopIpv6PrefixLen_Type(Unsigned32):
    """Custom type mplsTunnelARHopIpv6PrefixLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MplsTunnelARHopIpv6PrefixLen_Type.__name__ = "Unsigned32"
_MplsTunnelARHopIpv6PrefixLen_Object = MibTableColumn
mplsTunnelARHopIpv6PrefixLen = _MplsTunnelARHopIpv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 7, 1, 7),
    _MplsTunnelARHopIpv6PrefixLen_Type()
)
mplsTunnelARHopIpv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopIpv6PrefixLen.setStatus("current")


class _MplsTunnelARHopAsNumber_Type(Unsigned32):
    """Custom type mplsTunnelARHopAsNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsTunnelARHopAsNumber_Type.__name__ = "Unsigned32"
_MplsTunnelARHopAsNumber_Object = MibTableColumn
mplsTunnelARHopAsNumber = _MplsTunnelARHopAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 7, 1, 8),
    _MplsTunnelARHopAsNumber_Type()
)
mplsTunnelARHopAsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopAsNumber.setStatus("current")
_MplsTunnelARHopLspId_Type = MplsLSPID
_MplsTunnelARHopLspId_Object = MibTableColumn
mplsTunnelARHopLspId = _MplsTunnelARHopLspId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 7, 1, 9),
    _MplsTunnelARHopLspId_Type()
)
mplsTunnelARHopLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopLspId.setStatus("current")
_MplsTunnelCHopTable_Object = MibTable
mplsTunnelCHopTable = _MplsTunnelCHopTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 8)
)
if mibBuilder.loadTexts:
    mplsTunnelCHopTable.setStatus("current")
_MplsTunnelCHopEntry_Object = MibTableRow
mplsTunnelCHopEntry = _MplsTunnelCHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 8, 1)
)
mplsTunnelCHopEntry.setIndexNames(
    (0, "HP-SN-MPLS-TE-MIB", "mplsTunnelCHopListIndex"),
    (0, "HP-SN-MPLS-TE-MIB", "mplsTunnelCHopIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelCHopEntry.setStatus("current")
_MplsTunnelCHopListIndex_Type = MplsPathIndex
_MplsTunnelCHopListIndex_Object = MibTableColumn
mplsTunnelCHopListIndex = _MplsTunnelCHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 8, 1, 1),
    _MplsTunnelCHopListIndex_Type()
)
mplsTunnelCHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelCHopListIndex.setStatus("current")
_MplsTunnelCHopIndex_Type = MplsPathIndex
_MplsTunnelCHopIndex_Object = MibTableColumn
mplsTunnelCHopIndex = _MplsTunnelCHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 8, 1, 2),
    _MplsTunnelCHopIndex_Type()
)
mplsTunnelCHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelCHopIndex.setStatus("current")


class _MplsTunnelCHopAddrType_Type(Integer32):
    """Custom type mplsTunnelCHopAddrType based on Integer32"""
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
        *(("asNumber", 3),
          ("ipV4", 1),
          ("ipV6", 2),
          ("lspId", 4))
    )


_MplsTunnelCHopAddrType_Type.__name__ = "Integer32"
_MplsTunnelCHopAddrType_Object = MibTableColumn
mplsTunnelCHopAddrType = _MplsTunnelCHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 8, 1, 3),
    _MplsTunnelCHopAddrType_Type()
)
mplsTunnelCHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopAddrType.setStatus("current")
_MplsTunnelCHopIpv4Addr_Type = InetAddressIPv4
_MplsTunnelCHopIpv4Addr_Object = MibTableColumn
mplsTunnelCHopIpv4Addr = _MplsTunnelCHopIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 8, 1, 4),
    _MplsTunnelCHopIpv4Addr_Type()
)
mplsTunnelCHopIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopIpv4Addr.setStatus("current")


class _MplsTunnelCHopIpv4PrefixLen_Type(Unsigned32):
    """Custom type mplsTunnelCHopIpv4PrefixLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_MplsTunnelCHopIpv4PrefixLen_Type.__name__ = "Unsigned32"
_MplsTunnelCHopIpv4PrefixLen_Object = MibTableColumn
mplsTunnelCHopIpv4PrefixLen = _MplsTunnelCHopIpv4PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 8, 1, 5),
    _MplsTunnelCHopIpv4PrefixLen_Type()
)
mplsTunnelCHopIpv4PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopIpv4PrefixLen.setStatus("current")
_MplsTunnelCHopIpv6Addr_Type = InetAddressIPv6
_MplsTunnelCHopIpv6Addr_Object = MibTableColumn
mplsTunnelCHopIpv6Addr = _MplsTunnelCHopIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 8, 1, 6),
    _MplsTunnelCHopIpv6Addr_Type()
)
mplsTunnelCHopIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopIpv6Addr.setStatus("current")


class _MplsTunnelCHopIpv6PrefixLen_Type(Unsigned32):
    """Custom type mplsTunnelCHopIpv6PrefixLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MplsTunnelCHopIpv6PrefixLen_Type.__name__ = "Unsigned32"
_MplsTunnelCHopIpv6PrefixLen_Object = MibTableColumn
mplsTunnelCHopIpv6PrefixLen = _MplsTunnelCHopIpv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 8, 1, 7),
    _MplsTunnelCHopIpv6PrefixLen_Type()
)
mplsTunnelCHopIpv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopIpv6PrefixLen.setStatus("current")


class _MplsTunnelCHopAsNumber_Type(Unsigned32):
    """Custom type mplsTunnelCHopAsNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsTunnelCHopAsNumber_Type.__name__ = "Unsigned32"
_MplsTunnelCHopAsNumber_Object = MibTableColumn
mplsTunnelCHopAsNumber = _MplsTunnelCHopAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 8, 1, 8),
    _MplsTunnelCHopAsNumber_Type()
)
mplsTunnelCHopAsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopAsNumber.setStatus("current")
_MplsTunnelCHopLspId_Type = MplsLSPID
_MplsTunnelCHopLspId_Object = MibTableColumn
mplsTunnelCHopLspId = _MplsTunnelCHopLspId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 8, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 8, 1, 10),
    _MplsTunnelCHopType_Type()
)
mplsTunnelCHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopType.setStatus("current")
_MplsTunnelPerfTable_Object = MibTable
mplsTunnelPerfTable = _MplsTunnelPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 9)
)
if mibBuilder.loadTexts:
    mplsTunnelPerfTable.setStatus("current")
_MplsTunnelPerfEntry_Object = MibTableRow
mplsTunnelPerfEntry = _MplsTunnelPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 9, 1)
)
if mibBuilder.loadTexts:
    mplsTunnelPerfEntry.setStatus("current")
_MplsTunnelPerfPackets_Type = Counter32
_MplsTunnelPerfPackets_Object = MibTableColumn
mplsTunnelPerfPackets = _MplsTunnelPerfPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 9, 1, 1),
    _MplsTunnelPerfPackets_Type()
)
mplsTunnelPerfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPerfPackets.setStatus("current")
_MplsTunnelPerfHCPackets_Type = Counter64
_MplsTunnelPerfHCPackets_Object = MibTableColumn
mplsTunnelPerfHCPackets = _MplsTunnelPerfHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 9, 1, 2),
    _MplsTunnelPerfHCPackets_Type()
)
mplsTunnelPerfHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPerfHCPackets.setStatus("current")
_MplsTunnelPerfErrors_Type = Counter32
_MplsTunnelPerfErrors_Object = MibTableColumn
mplsTunnelPerfErrors = _MplsTunnelPerfErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 9, 1, 3),
    _MplsTunnelPerfErrors_Type()
)
mplsTunnelPerfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPerfErrors.setStatus("current")
_MplsTunnelPerfBytes_Type = Counter32
_MplsTunnelPerfBytes_Object = MibTableColumn
mplsTunnelPerfBytes = _MplsTunnelPerfBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 9, 1, 4),
    _MplsTunnelPerfBytes_Type()
)
mplsTunnelPerfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPerfBytes.setStatus("current")
_MplsTunnelPerfHCBytes_Type = Counter64
_MplsTunnelPerfHCBytes_Object = MibTableColumn
mplsTunnelPerfHCBytes = _MplsTunnelPerfHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 9, 1, 5),
    _MplsTunnelPerfHCBytes_Type()
)
mplsTunnelPerfHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPerfHCBytes.setStatus("current")
_MplsTunnelCRLDPResTable_Object = MibTable
mplsTunnelCRLDPResTable = _MplsTunnelCRLDPResTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResTable.setStatus("current")
_MplsTunnelCRLDPResEntry_Object = MibTableRow
mplsTunnelCRLDPResEntry = _MplsTunnelCRLDPResEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 10, 1)
)
mplsTunnelCRLDPResEntry.setIndexNames(
    (0, "HP-SN-MPLS-TE-MIB", "mplsTunnelResourceIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResEntry.setStatus("current")
_MplsTunnelCRLDPResMeanBurstSize_Type = MplsBurstSize
_MplsTunnelCRLDPResMeanBurstSize_Object = MibTableColumn
mplsTunnelCRLDPResMeanBurstSize = _MplsTunnelCRLDPResMeanBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 10, 1, 2),
    _MplsTunnelCRLDPResMeanBurstSize_Type()
)
mplsTunnelCRLDPResMeanBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResMeanBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResMeanBurstSize.setUnits("bytes")
_MplsTunnelCRLDPResExcessBurstSize_Type = MplsBurstSize
_MplsTunnelCRLDPResExcessBurstSize_Object = MibTableColumn
mplsTunnelCRLDPResExcessBurstSize = _MplsTunnelCRLDPResExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 10, 1, 3),
    _MplsTunnelCRLDPResExcessBurstSize_Type()
)
mplsTunnelCRLDPResExcessBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResExcessBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResExcessBurstSize.setUnits("bytes")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 10, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 10, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 10, 1, 6),
    _MplsTunnelCRLDPResFlags_Type()
)
mplsTunnelCRLDPResFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResFlags.setStatus("current")
_MplsTunnelCRLDPResRowStatus_Type = RowStatus
_MplsTunnelCRLDPResRowStatus_Object = MibTableColumn
mplsTunnelCRLDPResRowStatus = _MplsTunnelCRLDPResRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 10, 1, 7),
    _MplsTunnelCRLDPResRowStatus_Type()
)
mplsTunnelCRLDPResRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResRowStatus.setStatus("current")
_MplsTunnelCRLDPResStorageType_Type = StorageType
_MplsTunnelCRLDPResStorageType_Object = MibTableColumn
mplsTunnelCRLDPResStorageType = _MplsTunnelCRLDPResStorageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 10, 1, 8),
    _MplsTunnelCRLDPResStorageType_Type()
)
mplsTunnelCRLDPResStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResStorageType.setStatus("current")


class _MplsTunnelTrapEnable_Type(TruthValue):
    """Custom type mplsTunnelTrapEnable based on TruthValue"""


_MplsTunnelTrapEnable_Object = MibScalar
mplsTunnelTrapEnable = _MplsTunnelTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 2, 11),
    _MplsTunnelTrapEnable_Type()
)
mplsTunnelTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsTunnelTrapEnable.setStatus("current")
_MplsTeNotifications_ObjectIdentity = ObjectIdentity
mplsTeNotifications = _MplsTeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 3)
)
_MplsTeNotifyPrefix_ObjectIdentity = ObjectIdentity
mplsTeNotifyPrefix = _MplsTeNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 3, 0)
)
_MplsTeConformance_ObjectIdentity = ObjectIdentity
mplsTeConformance = _MplsTeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 4)
)
_MplsTeGroups_ObjectIdentity = ObjectIdentity
mplsTeGroups = _MplsTeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 4, 1)
)
_MplsTeCompliances_ObjectIdentity = ObjectIdentity
mplsTeCompliances = _MplsTeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 4, 2)
)
mplsTunnelEntry.registerAugmentions(
    ("HP-SN-MPLS-TE-MIB",
     "mplsTunnelPerfEntry")
)
mplsTunnelPerfEntry.setIndexNames(*mplsTunnelEntry.getIndexNames())

# Managed Objects groups

mplsTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 4, 1, 1)
)
mplsTunnelGroup.setObjects(
      *(("HP-SN-MPLS-TE-MIB", "mplsTunnelIndexNext"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelName"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelDescr"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelOwner"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelXCPointer"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelIfIndex"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelHopTableIndex"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelARHopTableIndex"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelCHopTableIndex"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelAdminStatus"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelOperStatus"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelRowStatus"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelTrapEnable"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelStorageType"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelConfigured"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelActive"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelPrimaryInstance"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelPrimaryTimeUp"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelPathChanges"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelLastPathChange"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelCreationTime"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelStateTransitions"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelIncludeAnyAffinity"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelIncludeAllAffinity"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelExcludeAllAffinity"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelPerfPackets"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelPerfHCPackets"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelPerfErrors"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelPerfBytes"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelPerfHCBytes"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelResourcePointer"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelInstancePriority"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelPathInUse"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelRole"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelTotalUpTime"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelInstanceUpTime"))
)
if mibBuilder.loadTexts:
    mplsTunnelGroup.setStatus("current")

mplsTunnelManualGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 4, 1, 2)
)
mplsTunnelManualGroup.setObjects(
    ("HP-SN-MPLS-TE-MIB", "mplsTunnelSignallingProto")
)
if mibBuilder.loadTexts:
    mplsTunnelManualGroup.setStatus("current")

mplsTunnelSignaledGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 4, 1, 3)
)
mplsTunnelSignaledGroup.setObjects(
      *(("HP-SN-MPLS-TE-MIB", "mplsTunnelSetupPrio"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelHoldingPrio"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelSignallingProto"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelLocalProtectInUse"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelSessionAttributes"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelHopListIndexNext"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelHopAddrType"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelHopIpv4Addr"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelHopIpv4PrefixLen"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelHopIpv6Addr"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelHopIpv6PrefixLen"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelHopAsNumber"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelHopLspId"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelHopType"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelHopIncludeExclude"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelHopPathOptionName"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelHopEntryPathComp"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelHopRowStatus"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelHopStorageType"))
)
if mibBuilder.loadTexts:
    mplsTunnelSignaledGroup.setStatus("current")

mplsTunnelScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 4, 1, 4)
)
mplsTunnelScalarGroup.setObjects(
      *(("HP-SN-MPLS-TE-MIB", "mplsTunnelConfigured"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelActive"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelTEDistProto"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelMaxHops"))
)
if mibBuilder.loadTexts:
    mplsTunnelScalarGroup.setStatus("current")

mplsTunnelIsIntfcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 4, 1, 5)
)
mplsTunnelIsIntfcGroup.setObjects(
    ("HP-SN-MPLS-TE-MIB", "mplsTunnelIsIf")
)
if mibBuilder.loadTexts:
    mplsTunnelIsIntfcGroup.setStatus("current")

mplsTunnelIsNotIntfcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 4, 1, 6)
)
mplsTunnelIsNotIntfcGroup.setObjects(
    ("HP-SN-MPLS-TE-MIB", "mplsTunnelIsIf")
)
if mibBuilder.loadTexts:
    mplsTunnelIsNotIntfcGroup.setStatus("current")

mplsTunnelOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 4, 1, 7)
)
mplsTunnelOptionalGroup.setObjects(
      *(("HP-SN-MPLS-TE-MIB", "mplsTunnelResourceIndexNext"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelResourceMaxRate"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelResourceMeanRate"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelResourceMaxBurstSize"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelResourceMeanBurstSize"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelResourceExcessBurstSize"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelResourceFrequency"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelResourceWeight"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelResourceRowStatus"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelResourceStorageType"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelARHopAddrType"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelARHopIpv4Addr"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelARHopIpv4PrefixLen"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelARHopIpv6Addr"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelARHopIpv6PrefixLen"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelARHopAsNumber"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelARHopLspId"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelCHopAddrType"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelCHopIpv4Addr"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelCHopIpv4PrefixLen"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelCHopIpv6Addr"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelCHopIpv6PrefixLen"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelCHopAsNumber"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelCHopLspId"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelCHopType"))
)
if mibBuilder.loadTexts:
    mplsTunnelOptionalGroup.setStatus("current")

mplsTunnelCRLDPResOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 4, 1, 8)
)
mplsTunnelCRLDPResOptionalGroup.setObjects(
      *(("HP-SN-MPLS-TE-MIB", "mplsTunnelCRLDPResMeanBurstSize"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelCRLDPResExcessBurstSize"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelCRLDPResFrequency"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelCRLDPResWeight"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelCRLDPResFlags"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelCRLDPResRowStatus"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelCRLDPResStorageType"))
)
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResOptionalGroup.setStatus("current")


# Notification objects

mplsTunnelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 3, 0, 1)
)
mplsTunnelUp.setObjects(
      *(("HP-SN-MPLS-TE-MIB", "mplsTunnelAdminStatus"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    mplsTunnelUp.setStatus(
        "current"
    )

mplsTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 3, 0, 2)
)
mplsTunnelDown.setObjects(
      *(("HP-SN-MPLS-TE-MIB", "mplsTunnelAdminStatus"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    mplsTunnelDown.setStatus(
        "current"
    )

mplsTunnelRerouted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 3, 0, 3)
)
mplsTunnelRerouted.setObjects(
      *(("HP-SN-MPLS-TE-MIB", "mplsTunnelAdminStatus"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    mplsTunnelRerouted.setStatus(
        "current"
    )

mplsTunnelReoptimized = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 3, 0, 4)
)
mplsTunnelReoptimized.setObjects(
      *(("HP-SN-MPLS-TE-MIB", "mplsTunnelAdminStatus"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    mplsTunnelReoptimized.setStatus(
        "current"
    )


# Notifications groups

mplsTeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 4, 1, 9)
)
mplsTeNotificationGroup.setObjects(
      *(("HP-SN-MPLS-TE-MIB", "mplsTunnelUp"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelDown"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelRerouted"),
        ("HP-SN-MPLS-TE-MIB", "mplsTunnelReoptimized"))
)
if mibBuilder.loadTexts:
    mplsTeNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mplsTeModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mplsTeModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SN-MPLS-TE-MIB",
    **{"mplsTeMIB": mplsTeMIB,
       "mplsTeScalars": mplsTeScalars,
       "mplsTunnelConfigured": mplsTunnelConfigured,
       "mplsTunnelActive": mplsTunnelActive,
       "mplsTunnelTEDistProto": mplsTunnelTEDistProto,
       "mplsTunnelMaxHops": mplsTunnelMaxHops,
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
       "mplsTunnelXCPointer": mplsTunnelXCPointer,
       "mplsTunnelSignallingProto": mplsTunnelSignallingProto,
       "mplsTunnelSetupPrio": mplsTunnelSetupPrio,
       "mplsTunnelHoldingPrio": mplsTunnelHoldingPrio,
       "mplsTunnelSessionAttributes": mplsTunnelSessionAttributes,
       "mplsTunnelOwner": mplsTunnelOwner,
       "mplsTunnelLocalProtectInUse": mplsTunnelLocalProtectInUse,
       "mplsTunnelResourcePointer": mplsTunnelResourcePointer,
       "mplsTunnelInstancePriority": mplsTunnelInstancePriority,
       "mplsTunnelHopTableIndex": mplsTunnelHopTableIndex,
       "mplsTunnelARHopTableIndex": mplsTunnelARHopTableIndex,
       "mplsTunnelCHopTableIndex": mplsTunnelCHopTableIndex,
       "mplsTunnelPrimaryInstance": mplsTunnelPrimaryInstance,
       "mplsTunnelPrimaryTimeUp": mplsTunnelPrimaryTimeUp,
       "mplsTunnelPathChanges": mplsTunnelPathChanges,
       "mplsTunnelLastPathChange": mplsTunnelLastPathChange,
       "mplsTunnelCreationTime": mplsTunnelCreationTime,
       "mplsTunnelStateTransitions": mplsTunnelStateTransitions,
       "mplsTunnelIncludeAnyAffinity": mplsTunnelIncludeAnyAffinity,
       "mplsTunnelIncludeAllAffinity": mplsTunnelIncludeAllAffinity,
       "mplsTunnelExcludeAllAffinity": mplsTunnelExcludeAllAffinity,
       "mplsTunnelPathInUse": mplsTunnelPathInUse,
       "mplsTunnelRole": mplsTunnelRole,
       "mplsTunnelTotalUpTime": mplsTunnelTotalUpTime,
       "mplsTunnelInstanceUpTime": mplsTunnelInstanceUpTime,
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
       "mplsTunnelHopIpv4Addr": mplsTunnelHopIpv4Addr,
       "mplsTunnelHopIpv4PrefixLen": mplsTunnelHopIpv4PrefixLen,
       "mplsTunnelHopIpv6Addr": mplsTunnelHopIpv6Addr,
       "mplsTunnelHopIpv6PrefixLen": mplsTunnelHopIpv6PrefixLen,
       "mplsTunnelHopAsNumber": mplsTunnelHopAsNumber,
       "mplsTunnelHopLspId": mplsTunnelHopLspId,
       "mplsTunnelHopType": mplsTunnelHopType,
       "mplsTunnelHopIncludeExclude": mplsTunnelHopIncludeExclude,
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
       "mplsTunnelResourceExcessBurstSize": mplsTunnelResourceExcessBurstSize,
       "mplsTunnelResourceFrequency": mplsTunnelResourceFrequency,
       "mplsTunnelResourceWeight": mplsTunnelResourceWeight,
       "mplsTunnelResourceRowStatus": mplsTunnelResourceRowStatus,
       "mplsTunnelResourceStorageType": mplsTunnelResourceStorageType,
       "mplsTunnelARHopTable": mplsTunnelARHopTable,
       "mplsTunnelARHopEntry": mplsTunnelARHopEntry,
       "mplsTunnelARHopListIndex": mplsTunnelARHopListIndex,
       "mplsTunnelARHopIndex": mplsTunnelARHopIndex,
       "mplsTunnelARHopAddrType": mplsTunnelARHopAddrType,
       "mplsTunnelARHopIpv4Addr": mplsTunnelARHopIpv4Addr,
       "mplsTunnelARHopIpv4PrefixLen": mplsTunnelARHopIpv4PrefixLen,
       "mplsTunnelARHopIpv6Addr": mplsTunnelARHopIpv6Addr,
       "mplsTunnelARHopIpv6PrefixLen": mplsTunnelARHopIpv6PrefixLen,
       "mplsTunnelARHopAsNumber": mplsTunnelARHopAsNumber,
       "mplsTunnelARHopLspId": mplsTunnelARHopLspId,
       "mplsTunnelCHopTable": mplsTunnelCHopTable,
       "mplsTunnelCHopEntry": mplsTunnelCHopEntry,
       "mplsTunnelCHopListIndex": mplsTunnelCHopListIndex,
       "mplsTunnelCHopIndex": mplsTunnelCHopIndex,
       "mplsTunnelCHopAddrType": mplsTunnelCHopAddrType,
       "mplsTunnelCHopIpv4Addr": mplsTunnelCHopIpv4Addr,
       "mplsTunnelCHopIpv4PrefixLen": mplsTunnelCHopIpv4PrefixLen,
       "mplsTunnelCHopIpv6Addr": mplsTunnelCHopIpv6Addr,
       "mplsTunnelCHopIpv6PrefixLen": mplsTunnelCHopIpv6PrefixLen,
       "mplsTunnelCHopAsNumber": mplsTunnelCHopAsNumber,
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
       "mplsTunnelCRLDPResExcessBurstSize": mplsTunnelCRLDPResExcessBurstSize,
       "mplsTunnelCRLDPResFrequency": mplsTunnelCRLDPResFrequency,
       "mplsTunnelCRLDPResWeight": mplsTunnelCRLDPResWeight,
       "mplsTunnelCRLDPResFlags": mplsTunnelCRLDPResFlags,
       "mplsTunnelCRLDPResRowStatus": mplsTunnelCRLDPResRowStatus,
       "mplsTunnelCRLDPResStorageType": mplsTunnelCRLDPResStorageType,
       "mplsTunnelTrapEnable": mplsTunnelTrapEnable,
       "mplsTeNotifications": mplsTeNotifications,
       "mplsTeNotifyPrefix": mplsTeNotifyPrefix,
       "mplsTunnelUp": mplsTunnelUp,
       "mplsTunnelDown": mplsTunnelDown,
       "mplsTunnelRerouted": mplsTunnelRerouted,
       "mplsTunnelReoptimized": mplsTunnelReoptimized,
       "mplsTeConformance": mplsTeConformance,
       "mplsTeGroups": mplsTeGroups,
       "mplsTunnelGroup": mplsTunnelGroup,
       "mplsTunnelManualGroup": mplsTunnelManualGroup,
       "mplsTunnelSignaledGroup": mplsTunnelSignaledGroup,
       "mplsTunnelScalarGroup": mplsTunnelScalarGroup,
       "mplsTunnelIsIntfcGroup": mplsTunnelIsIntfcGroup,
       "mplsTunnelIsNotIntfcGroup": mplsTunnelIsNotIntfcGroup,
       "mplsTunnelOptionalGroup": mplsTunnelOptionalGroup,
       "mplsTunnelCRLDPResOptionalGroup": mplsTunnelCRLDPResOptionalGroup,
       "mplsTeNotificationGroup": mplsTeNotificationGroup,
       "mplsTeCompliances": mplsTeCompliances,
       "mplsTeModuleCompliance": mplsTeModuleCompliance}
)

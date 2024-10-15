# SNMP MIB module (A3COM-MLN-R1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-MLN-R1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:38 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_BrouterMIB_ObjectIdentity = ObjectIdentity
brouterMIB = _BrouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2)
)
_A3ComMLN_ObjectIdentity = ObjectIdentity
a3ComMLN = _A3ComMLN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 23)
)
_A3mlnMaxPorts_Type = Integer32
_A3mlnMaxPorts_Object = MibScalar
a3mlnMaxPorts = _A3mlnMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 1),
    _A3mlnMaxPorts_Type()
)
a3mlnMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnMaxPorts.setStatus("mandatory")
_A3mlnMaxPhyPorts_Type = Integer32
_A3mlnMaxPhyPorts_Object = MibScalar
a3mlnMaxPhyPorts = _A3mlnMaxPhyPorts_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 2),
    _A3mlnMaxPhyPorts_Type()
)
a3mlnMaxPhyPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnMaxPhyPorts.setStatus("mandatory")
_A3mlnCCSsaveErr_Type = Integer32
_A3mlnCCSsaveErr_Object = MibScalar
a3mlnCCSsaveErr = _A3mlnCCSsaveErr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 3),
    _A3mlnCCSsaveErr_Type()
)
a3mlnCCSsaveErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnCCSsaveErr.setStatus("mandatory")
_A3mlnCCSdelErr_Type = Integer32
_A3mlnCCSdelErr_Object = MibScalar
a3mlnCCSdelErr = _A3mlnCCSdelErr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 4),
    _A3mlnCCSdelErr_Type()
)
a3mlnCCSdelErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnCCSdelErr.setStatus("mandatory")


class _A3mlnSetStatus_Type(Integer32):
    """Custom type a3mlnSetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("setErr", 2),
          ("setNoErr", 1),
          ("setWarning", 3))
    )


_A3mlnSetStatus_Type.__name__ = "Integer32"
_A3mlnSetStatus_Object = MibScalar
a3mlnSetStatus = _A3mlnSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 5),
    _A3mlnSetStatus_Type()
)
a3mlnSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnSetStatus.setStatus("mandatory")


class _A3mlnSetMsg_Type(DisplayString):
    """Custom type a3mlnSetMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_A3mlnSetMsg_Type.__name__ = "DisplayString"
_A3mlnSetMsg_Object = MibScalar
a3mlnSetMsg = _A3mlnSetMsg_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 6),
    _A3mlnSetMsg_Type()
)
a3mlnSetMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnSetMsg.setStatus("mandatory")
_A3mlnPortTable_Object = MibTable
a3mlnPortTable = _A3mlnPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 7)
)
if mibBuilder.loadTexts:
    a3mlnPortTable.setStatus("mandatory")
_A3mlnPortEntry_Object = MibTableRow
a3mlnPortEntry = _A3mlnPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1)
)
a3mlnPortEntry.setIndexNames(
    (0, "A3COM-MLN-R1-MIB", "a3mlnPindex"),
)
if mibBuilder.loadTexts:
    a3mlnPortEntry.setStatus("mandatory")
_A3mlnPindex_Type = Integer32
_A3mlnPindex_Object = MibTableColumn
a3mlnPindex = _A3mlnPindex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 1),
    _A3mlnPindex_Type()
)
a3mlnPindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnPindex.setStatus("mandatory")


class _A3mlnPtype_Type(Integer32):
    """Custom type a3mlnPtype based on Integer32"""
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
        *(("groupPort", 2),
          ("memberPort", 3),
          ("ppmPort", 1),
          ("primaryPort", 4))
    )


_A3mlnPtype_Type.__name__ = "Integer32"
_A3mlnPtype_Object = MibTableColumn
a3mlnPtype = _A3mlnPtype_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 2),
    _A3mlnPtype_Type()
)
a3mlnPtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnPtype.setStatus("mandatory")


class _A3mlnPowner_Type(Integer32):
    """Custom type a3mlnPowner based on Integer32"""
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
        *(("ethernet", 1),
          ("fddi", 3),
          ("otherMedia", 4),
          ("tokenRing", 2))
    )


_A3mlnPowner_Type.__name__ = "Integer32"
_A3mlnPowner_Object = MibTableColumn
a3mlnPowner = _A3mlnPowner_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 3),
    _A3mlnPowner_Type()
)
a3mlnPowner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnPowner.setStatus("mandatory")
_A3mlnPlink_Type = Integer32
_A3mlnPlink_Object = MibTableColumn
a3mlnPlink = _A3mlnPlink_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 4),
    _A3mlnPlink_Type()
)
a3mlnPlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnPlink.setStatus("mandatory")


class _A3mlnPstState_Type(Integer32):
    """Custom type a3mlnPstState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("forwarding", 1),
          ("ignore", 3))
    )


_A3mlnPstState_Type.__name__ = "Integer32"
_A3mlnPstState_Object = MibTableColumn
a3mlnPstState = _A3mlnPstState_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 5),
    _A3mlnPstState_Type()
)
a3mlnPstState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnPstState.setStatus("mandatory")


class _A3mlnPtbState_Type(Integer32):
    """Custom type a3mlnPtbState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 3),
          ("learn", 1),
          ("noLearn", 2))
    )


_A3mlnPtbState_Type.__name__ = "Integer32"
_A3mlnPtbState_Object = MibTableColumn
a3mlnPtbState = _A3mlnPtbState_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 6),
    _A3mlnPtbState_Type()
)
a3mlnPtbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnPtbState.setStatus("mandatory")
_A3mlnPgrpPrimaryPort_Type = Integer32
_A3mlnPgrpPrimaryPort_Object = MibTableColumn
a3mlnPgrpPrimaryPort = _A3mlnPgrpPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 7),
    _A3mlnPgrpPrimaryPort_Type()
)
a3mlnPgrpPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnPgrpPrimaryPort.setStatus("mandatory")
_A3mlnPgrpSrcAdrPort_Type = Integer32
_A3mlnPgrpSrcAdrPort_Object = MibTableColumn
a3mlnPgrpSrcAdrPort = _A3mlnPgrpSrcAdrPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 8),
    _A3mlnPgrpSrcAdrPort_Type()
)
a3mlnPgrpSrcAdrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnPgrpSrcAdrPort.setStatus("mandatory")


class _A3mlnPgrpSrcAdrMedia_Type(Integer32):
    """Custom type a3mlnPgrpSrcAdrMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mediaMAC", 1),
          ("mediaOther", 2))
    )


_A3mlnPgrpSrcAdrMedia_Type.__name__ = "Integer32"
_A3mlnPgrpSrcAdrMedia_Object = MibTableColumn
a3mlnPgrpSrcAdrMedia = _A3mlnPgrpSrcAdrMedia_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 9),
    _A3mlnPgrpSrcAdrMedia_Type()
)
a3mlnPgrpSrcAdrMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnPgrpSrcAdrMedia.setStatus("mandatory")
_A3mlnPgrpSrcAdrValue_Type = PhysAddress
_A3mlnPgrpSrcAdrValue_Object = MibTableColumn
a3mlnPgrpSrcAdrValue = _A3mlnPgrpSrcAdrValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 10),
    _A3mlnPgrpSrcAdrValue_Type()
)
a3mlnPgrpSrcAdrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnPgrpSrcAdrValue.setStatus("mandatory")


class _A3mlnPgrpDescription_Type(DisplayString):
    """Custom type a3mlnPgrpDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_A3mlnPgrpDescription_Type.__name__ = "DisplayString"
_A3mlnPgrpDescription_Object = MibTableColumn
a3mlnPgrpDescription = _A3mlnPgrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 11),
    _A3mlnPgrpDescription_Type()
)
a3mlnPgrpDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnPgrpDescription.setStatus("mandatory")
_A3mlnGroupTable_Object = MibTable
a3mlnGroupTable = _A3mlnGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 8)
)
if mibBuilder.loadTexts:
    a3mlnGroupTable.setStatus("mandatory")
_A3mlnGroupEntry_Object = MibTableRow
a3mlnGroupEntry = _A3mlnGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1)
)
a3mlnGroupEntry.setIndexNames(
    (0, "A3COM-MLN-R1-MIB", "a3mlnGrpPort"),
)
if mibBuilder.loadTexts:
    a3mlnGroupEntry.setStatus("mandatory")
_A3mlnGrpPort_Type = Integer32
_A3mlnGrpPort_Object = MibTableColumn
a3mlnGrpPort = _A3mlnGrpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1, 1),
    _A3mlnGrpPort_Type()
)
a3mlnGrpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnGrpPort.setStatus("mandatory")


class _A3mlnGrpPortType_Type(Integer32):
    """Custom type a3mlnGrpPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("groupPort", 2)
    )


_A3mlnGrpPortType_Type.__name__ = "Integer32"
_A3mlnGrpPortType_Object = MibTableColumn
a3mlnGrpPortType = _A3mlnGrpPortType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1, 2),
    _A3mlnGrpPortType_Type()
)
a3mlnGrpPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnGrpPortType.setStatus("mandatory")


class _A3mlnGrpPortState_Type(Integer32):
    """Custom type a3mlnGrpPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_A3mlnGrpPortState_Type.__name__ = "Integer32"
_A3mlnGrpPortState_Object = MibTableColumn
a3mlnGrpPortState = _A3mlnGrpPortState_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1, 3),
    _A3mlnGrpPortState_Type()
)
a3mlnGrpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnGrpPortState.setStatus("mandatory")
_A3mlnGrpPrimaryPort_Type = Integer32
_A3mlnGrpPrimaryPort_Object = MibTableColumn
a3mlnGrpPrimaryPort = _A3mlnGrpPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1, 4),
    _A3mlnGrpPrimaryPort_Type()
)
a3mlnGrpPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnGrpPrimaryPort.setStatus("mandatory")


class _A3mlnGrpOwner_Type(Integer32):
    """Custom type a3mlnGrpOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("fddi", 3),
          ("tokenRing", 2))
    )


_A3mlnGrpOwner_Type.__name__ = "Integer32"
_A3mlnGrpOwner_Object = MibTableColumn
a3mlnGrpOwner = _A3mlnGrpOwner_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1, 5),
    _A3mlnGrpOwner_Type()
)
a3mlnGrpOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3mlnGrpOwner.setStatus("mandatory")
_A3mlnGrpMemberCount_Type = Integer32
_A3mlnGrpMemberCount_Object = MibTableColumn
a3mlnGrpMemberCount = _A3mlnGrpMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1, 6),
    _A3mlnGrpMemberCount_Type()
)
a3mlnGrpMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnGrpMemberCount.setStatus("mandatory")
_A3mlnGrpFirstMember_Type = Integer32
_A3mlnGrpFirstMember_Object = MibTableColumn
a3mlnGrpFirstMember = _A3mlnGrpFirstMember_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1, 7),
    _A3mlnGrpFirstMember_Type()
)
a3mlnGrpFirstMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnGrpFirstMember.setStatus("mandatory")


class _A3mlnGrpDescription_Type(DisplayString):
    """Custom type a3mlnGrpDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_A3mlnGrpDescription_Type.__name__ = "DisplayString"
_A3mlnGrpDescription_Object = MibTableColumn
a3mlnGrpDescription = _A3mlnGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1, 8),
    _A3mlnGrpDescription_Type()
)
a3mlnGrpDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3mlnGrpDescription.setStatus("mandatory")
_A3mlnGrpEntryStatus_Type = RowStatus
_A3mlnGrpEntryStatus_Object = MibTableColumn
a3mlnGrpEntryStatus = _A3mlnGrpEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1, 9),
    _A3mlnGrpEntryStatus_Type()
)
a3mlnGrpEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3mlnGrpEntryStatus.setStatus("mandatory")
_A3mlnMemberTable_Object = MibTable
a3mlnMemberTable = _A3mlnMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 9)
)
if mibBuilder.loadTexts:
    a3mlnMemberTable.setStatus("mandatory")
_A3mlnMemberEntry_Object = MibTableRow
a3mlnMemberEntry = _A3mlnMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 9, 1)
)
a3mlnMemberEntry.setIndexNames(
    (0, "A3COM-MLN-R1-MIB", "a3mlnMemGrpPort"),
    (0, "A3COM-MLN-R1-MIB", "a3mlnMemPort"),
)
if mibBuilder.loadTexts:
    a3mlnMemberEntry.setStatus("mandatory")
_A3mlnMemGrpPort_Type = Integer32
_A3mlnMemGrpPort_Object = MibTableColumn
a3mlnMemGrpPort = _A3mlnMemGrpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 9, 1, 1),
    _A3mlnMemGrpPort_Type()
)
a3mlnMemGrpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnMemGrpPort.setStatus("mandatory")
_A3mlnMemPort_Type = Integer32
_A3mlnMemPort_Object = MibTableColumn
a3mlnMemPort = _A3mlnMemPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 9, 1, 2),
    _A3mlnMemPort_Type()
)
a3mlnMemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnMemPort.setStatus("mandatory")


class _A3mlnMemOwner_Type(Integer32):
    """Custom type a3mlnMemOwner based on Integer32"""
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
        *(("ethernet", 1),
          ("fddi", 3),
          ("otherMedia", 4),
          ("tokenRing", 2))
    )


_A3mlnMemOwner_Type.__name__ = "Integer32"
_A3mlnMemOwner_Object = MibTableColumn
a3mlnMemOwner = _A3mlnMemOwner_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 9, 1, 3),
    _A3mlnMemOwner_Type()
)
a3mlnMemOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3mlnMemOwner.setStatus("mandatory")
_A3mlnMemEntryStatus_Type = RowStatus
_A3mlnMemEntryStatus_Object = MibTableColumn
a3mlnMemEntryStatus = _A3mlnMemEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 9, 1, 4),
    _A3mlnMemEntryStatus_Type()
)
a3mlnMemEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3mlnMemEntryStatus.setStatus("mandatory")
_A3mlnStatistics_ObjectIdentity = ObjectIdentity
a3mlnStatistics = _A3mlnStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 10)
)
_A3mlnStatSelGrpPort_Type = Integer32
_A3mlnStatSelGrpPort_Object = MibScalar
a3mlnStatSelGrpPort = _A3mlnStatSelGrpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 1),
    _A3mlnStatSelGrpPort_Type()
)
a3mlnStatSelGrpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnStatSelGrpPort.setStatus("mandatory")
_A3mlnStatSelMacAdr_Type = Integer32
_A3mlnStatSelMacAdr_Object = MibScalar
a3mlnStatSelMacAdr = _A3mlnStatSelMacAdr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 2),
    _A3mlnStatSelMacAdr_Type()
)
a3mlnStatSelMacAdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnStatSelMacAdr.setStatus("mandatory")
_A3mlnPortStatTable_Object = MibTable
a3mlnPortStatTable = _A3mlnPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 3)
)
if mibBuilder.loadTexts:
    a3mlnPortStatTable.setStatus("mandatory")
_A3mlnPortStatEntry_Object = MibTableRow
a3mlnPortStatEntry = _A3mlnPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 3, 1)
)
a3mlnPortStatEntry.setIndexNames(
    (0, "A3COM-MLN-R1-MIB", "a3mlnPStatIndex"),
)
if mibBuilder.loadTexts:
    a3mlnPortStatEntry.setStatus("mandatory")
_A3mlnPStatIndex_Type = Integer32
_A3mlnPStatIndex_Object = MibTableColumn
a3mlnPStatIndex = _A3mlnPStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 3, 1, 1),
    _A3mlnPStatIndex_Type()
)
a3mlnPStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnPStatIndex.setStatus("mandatory")
_A3mlnPStatRcvd_Type = Integer32
_A3mlnPStatRcvd_Object = MibTableColumn
a3mlnPStatRcvd = _A3mlnPStatRcvd_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 3, 1, 2),
    _A3mlnPStatRcvd_Type()
)
a3mlnPStatRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnPStatRcvd.setStatus("mandatory")
_A3mlnPStatXmit_Type = Integer32
_A3mlnPStatXmit_Object = MibTableColumn
a3mlnPStatXmit = _A3mlnPStatXmit_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 3, 1, 3),
    _A3mlnPStatXmit_Type()
)
a3mlnPStatXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnPStatXmit.setStatus("mandatory")
_A3mlnPStatStaMoveFrom_Type = Integer32
_A3mlnPStatStaMoveFrom_Object = MibTableColumn
a3mlnPStatStaMoveFrom = _A3mlnPStatStaMoveFrom_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 3, 1, 4),
    _A3mlnPStatStaMoveFrom_Type()
)
a3mlnPStatStaMoveFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnPStatStaMoveFrom.setStatus("mandatory")
_A3mlnPStatStaMoveTo_Type = Integer32
_A3mlnPStatStaMoveTo_Object = MibTableColumn
a3mlnPStatStaMoveTo = _A3mlnPStatStaMoveTo_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 3, 1, 5),
    _A3mlnPStatStaMoveTo_Type()
)
a3mlnPStatStaMoveTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnPStatStaMoveTo.setStatus("mandatory")
_A3mlnPStatSTAchange_Type = Integer32
_A3mlnPStatSTAchange_Object = MibTableColumn
a3mlnPStatSTAchange = _A3mlnPStatSTAchange_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 3, 1, 6),
    _A3mlnPStatSTAchange_Type()
)
a3mlnPStatSTAchange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3mlnPStatSTAchange.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-MLN-R1-MIB",
    **{"RowStatus": RowStatus,
       "a3Com": a3Com,
       "brouterMIB": brouterMIB,
       "a3ComMLN": a3ComMLN,
       "a3mlnMaxPorts": a3mlnMaxPorts,
       "a3mlnMaxPhyPorts": a3mlnMaxPhyPorts,
       "a3mlnCCSsaveErr": a3mlnCCSsaveErr,
       "a3mlnCCSdelErr": a3mlnCCSdelErr,
       "a3mlnSetStatus": a3mlnSetStatus,
       "a3mlnSetMsg": a3mlnSetMsg,
       "a3mlnPortTable": a3mlnPortTable,
       "a3mlnPortEntry": a3mlnPortEntry,
       "a3mlnPindex": a3mlnPindex,
       "a3mlnPtype": a3mlnPtype,
       "a3mlnPowner": a3mlnPowner,
       "a3mlnPlink": a3mlnPlink,
       "a3mlnPstState": a3mlnPstState,
       "a3mlnPtbState": a3mlnPtbState,
       "a3mlnPgrpPrimaryPort": a3mlnPgrpPrimaryPort,
       "a3mlnPgrpSrcAdrPort": a3mlnPgrpSrcAdrPort,
       "a3mlnPgrpSrcAdrMedia": a3mlnPgrpSrcAdrMedia,
       "a3mlnPgrpSrcAdrValue": a3mlnPgrpSrcAdrValue,
       "a3mlnPgrpDescription": a3mlnPgrpDescription,
       "a3mlnGroupTable": a3mlnGroupTable,
       "a3mlnGroupEntry": a3mlnGroupEntry,
       "a3mlnGrpPort": a3mlnGrpPort,
       "a3mlnGrpPortType": a3mlnGrpPortType,
       "a3mlnGrpPortState": a3mlnGrpPortState,
       "a3mlnGrpPrimaryPort": a3mlnGrpPrimaryPort,
       "a3mlnGrpOwner": a3mlnGrpOwner,
       "a3mlnGrpMemberCount": a3mlnGrpMemberCount,
       "a3mlnGrpFirstMember": a3mlnGrpFirstMember,
       "a3mlnGrpDescription": a3mlnGrpDescription,
       "a3mlnGrpEntryStatus": a3mlnGrpEntryStatus,
       "a3mlnMemberTable": a3mlnMemberTable,
       "a3mlnMemberEntry": a3mlnMemberEntry,
       "a3mlnMemGrpPort": a3mlnMemGrpPort,
       "a3mlnMemPort": a3mlnMemPort,
       "a3mlnMemOwner": a3mlnMemOwner,
       "a3mlnMemEntryStatus": a3mlnMemEntryStatus,
       "a3mlnStatistics": a3mlnStatistics,
       "a3mlnStatSelGrpPort": a3mlnStatSelGrpPort,
       "a3mlnStatSelMacAdr": a3mlnStatSelMacAdr,
       "a3mlnPortStatTable": a3mlnPortStatTable,
       "a3mlnPortStatEntry": a3mlnPortStatEntry,
       "a3mlnPStatIndex": a3mlnPStatIndex,
       "a3mlnPStatRcvd": a3mlnPStatRcvd,
       "a3mlnPStatXmit": a3mlnPStatXmit,
       "a3mlnPStatStaMoveFrom": a3mlnPStatStaMoveFrom,
       "a3mlnPStatStaMoveTo": a3mlnPStatStaMoveTo,
       "a3mlnPStatSTAchange": a3mlnPStatSTAchange}
)

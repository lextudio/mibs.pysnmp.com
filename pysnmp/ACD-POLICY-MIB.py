# SNMP MIB module (ACD-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACD-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:21 2024
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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acdPolicy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3)
)
acdPolicy.setRevisions(
        ("2011-10-10 01:00",
         "2011-02-28 01:00",
         "2010-11-10 01:00",
         "2008-06-15 01:00",
         "2008-05-01 01:00",
         "2008-02-06 01:00",
         "2007-05-15 01:00",
         "2007-03-28 01:00",
         "2006-08-06 01:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcdPolicyTable_Object = MibTable
acdPolicyTable = _AcdPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1)
)
if mibBuilder.loadTexts:
    acdPolicyTable.setStatus("current")
_AcdPolicyEntry_Object = MibTableRow
acdPolicyEntry = _AcdPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1)
)
acdPolicyEntry.setIndexNames(
    (0, "ACD-POLICY-MIB", "acdPolicyID"),
)
if mibBuilder.loadTexts:
    acdPolicyEntry.setStatus("current")
_AcdPolicyID_Type = Unsigned32
_AcdPolicyID_Object = MibTableColumn
acdPolicyID = _AcdPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 1),
    _AcdPolicyID_Type()
)
acdPolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPolicyID.setStatus("current")
_AcdPolicyListID_Type = Unsigned32
_AcdPolicyListID_Object = MibTableColumn
acdPolicyListID = _AcdPolicyListID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 2),
    _AcdPolicyListID_Type()
)
acdPolicyListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyListID.setStatus("current")
_AcdPolicyEntryID_Type = Unsigned32
_AcdPolicyEntryID_Object = MibTableColumn
acdPolicyEntryID = _AcdPolicyEntryID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 3),
    _AcdPolicyEntryID_Type()
)
acdPolicyEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyEntryID.setStatus("current")
_AcdPolicyEnable_Type = TruthValue
_AcdPolicyEnable_Object = MibTableColumn
acdPolicyEnable = _AcdPolicyEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 4),
    _AcdPolicyEnable_Type()
)
acdPolicyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyEnable.setStatus("current")


class _AcdPolicyFilterType_Type(Integer32):
    """Custom type acdPolicyFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4filter", 1),
          ("ipv6filter", 2),
          ("layer2filter", 0),
          ("vlist", 3))
    )


_AcdPolicyFilterType_Type.__name__ = "Integer32"
_AcdPolicyFilterType_Object = MibTableColumn
acdPolicyFilterType = _AcdPolicyFilterType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 5),
    _AcdPolicyFilterType_Type()
)
acdPolicyFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyFilterType.setStatus("current")
_AcdPolicyFilterIndex_Type = Unsigned32
_AcdPolicyFilterIndex_Object = MibTableColumn
acdPolicyFilterIndex = _AcdPolicyFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 6),
    _AcdPolicyFilterIndex_Type()
)
acdPolicyFilterIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyFilterIndex.setStatus("current")
_AcdPolicyDropEnable_Type = TruthValue
_AcdPolicyDropEnable_Object = MibTableColumn
acdPolicyDropEnable = _AcdPolicyDropEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 7),
    _AcdPolicyDropEnable_Type()
)
acdPolicyDropEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyDropEnable.setStatus("deprecated")
_AcdPolicyMonitorEnable_Type = TruthValue
_AcdPolicyMonitorEnable_Object = MibTableColumn
acdPolicyMonitorEnable = _AcdPolicyMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 8),
    _AcdPolicyMonitorEnable_Type()
)
acdPolicyMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyMonitorEnable.setStatus("current")


class _AcdPolicyMonitorIndex_Type(Integer32):
    """Custom type acdPolicyMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("monitor1", 1),
          ("monitor2", 2))
    )


_AcdPolicyMonitorIndex_Type.__name__ = "Integer32"
_AcdPolicyMonitorIndex_Object = MibTableColumn
acdPolicyMonitorIndex = _AcdPolicyMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 9),
    _AcdPolicyMonitorIndex_Type()
)
acdPolicyMonitorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyMonitorIndex.setStatus("current")
_AcdPolicyRegulatorEnable_Type = TruthValue
_AcdPolicyRegulatorEnable_Object = MibTableColumn
acdPolicyRegulatorEnable = _AcdPolicyRegulatorEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 10),
    _AcdPolicyRegulatorEnable_Type()
)
acdPolicyRegulatorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyRegulatorEnable.setStatus("current")
_AcdPolicyRegulatorIndex_Type = Unsigned32
_AcdPolicyRegulatorIndex_Object = MibTableColumn
acdPolicyRegulatorIndex = _AcdPolicyRegulatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 11),
    _AcdPolicyRegulatorIndex_Type()
)
acdPolicyRegulatorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyRegulatorIndex.setStatus("current")


class _AcdPolicyRegulatorMarking_Type(Integer32):
    """Custom type acdPolicyRegulatorMarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("red", 3),
          ("yellow", 2))
    )


_AcdPolicyRegulatorMarking_Type.__name__ = "Integer32"
_AcdPolicyRegulatorMarking_Object = MibTableColumn
acdPolicyRegulatorMarking = _AcdPolicyRegulatorMarking_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 12),
    _AcdPolicyRegulatorMarking_Type()
)
acdPolicyRegulatorMarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyRegulatorMarking.setStatus("current")


class _AcdPolicyAction_Type(Integer32):
    """Custom type acdPolicyAction based on Integer32"""
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
        *(("drop", 1),
          ("mgmtOAM", 3),
          ("mgmtOAMandDrop", 4),
          ("mgmtOAMandForward", 5),
          ("permit", 2))
    )


_AcdPolicyAction_Type.__name__ = "Integer32"
_AcdPolicyAction_Object = MibTableColumn
acdPolicyAction = _AcdPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 13),
    _AcdPolicyAction_Type()
)
acdPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyAction.setStatus("current")


class _AcdPolicyEvcMappingEncaps_Type(Integer32):
    """Custom type acdPolicyEvcMappingEncaps based on Integer32"""
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
        *(("none", 1),
          ("pop", 3),
          ("popAndReplace", 5),
          ("push", 2),
          ("pushAndPreserve", 6),
          ("replace", 4))
    )


_AcdPolicyEvcMappingEncaps_Type.__name__ = "Integer32"
_AcdPolicyEvcMappingEncaps_Object = MibTableColumn
acdPolicyEvcMappingEncaps = _AcdPolicyEvcMappingEncaps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 14),
    _AcdPolicyEvcMappingEncaps_Type()
)
acdPolicyEvcMappingEncaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyEvcMappingEncaps.setStatus("current")


class _AcdPolicyEvcMappingEtype_Type(Integer32):
    """Custom type acdPolicyEvcMappingEtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cvlan", 1),
          ("svlan", 2))
    )


_AcdPolicyEvcMappingEtype_Type.__name__ = "Integer32"
_AcdPolicyEvcMappingEtype_Object = MibTableColumn
acdPolicyEvcMappingEtype = _AcdPolicyEvcMappingEtype_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 15),
    _AcdPolicyEvcMappingEtype_Type()
)
acdPolicyEvcMappingEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyEvcMappingEtype.setStatus("current")


class _AcdPolicyEvcMappingVlanId_Type(Unsigned32):
    """Custom type acdPolicyEvcMappingVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AcdPolicyEvcMappingVlanId_Type.__name__ = "Unsigned32"
_AcdPolicyEvcMappingVlanId_Object = MibTableColumn
acdPolicyEvcMappingVlanId = _AcdPolicyEvcMappingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 16),
    _AcdPolicyEvcMappingVlanId_Type()
)
acdPolicyEvcMappingVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyEvcMappingVlanId.setStatus("current")


class _AcdPolicyCosMappingPcpAction_Type(Integer32):
    """Custom type acdPolicyCosMappingPcpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("direct", 2),
          ("map", 3),
          ("preserve", 1))
    )


_AcdPolicyCosMappingPcpAction_Type.__name__ = "Integer32"
_AcdPolicyCosMappingPcpAction_Object = MibTableColumn
acdPolicyCosMappingPcpAction = _AcdPolicyCosMappingPcpAction_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 17),
    _AcdPolicyCosMappingPcpAction_Type()
)
acdPolicyCosMappingPcpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyCosMappingPcpAction.setStatus("current")
_AcdPolicyCosMappingChoice1En_Type = TruthValue
_AcdPolicyCosMappingChoice1En_Object = MibTableColumn
acdPolicyCosMappingChoice1En = _AcdPolicyCosMappingChoice1En_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 18),
    _AcdPolicyCosMappingChoice1En_Type()
)
acdPolicyCosMappingChoice1En.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyCosMappingChoice1En.setStatus("current")


class _AcdPolicyCosMappingChoice1Type_Type(Integer32):
    """Custom type acdPolicyCosMappingChoice1Type based on Integer32"""
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
        *(("dscp", 4),
          ("pcpVlan", 1),
          ("pcpVlanInVlan", 2),
          ("pre", 3))
    )


_AcdPolicyCosMappingChoice1Type_Type.__name__ = "Integer32"
_AcdPolicyCosMappingChoice1Type_Object = MibTableColumn
acdPolicyCosMappingChoice1Type = _AcdPolicyCosMappingChoice1Type_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 19),
    _AcdPolicyCosMappingChoice1Type_Type()
)
acdPolicyCosMappingChoice1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyCosMappingChoice1Type.setStatus("current")
_AcdPolicyCosMappingChoice1Profile_Type = Unsigned32
_AcdPolicyCosMappingChoice1Profile_Object = MibTableColumn
acdPolicyCosMappingChoice1Profile = _AcdPolicyCosMappingChoice1Profile_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 20),
    _AcdPolicyCosMappingChoice1Profile_Type()
)
acdPolicyCosMappingChoice1Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyCosMappingChoice1Profile.setStatus("current")
_AcdPolicyCosMappingChoice1RegSet_Type = Unsigned32
_AcdPolicyCosMappingChoice1RegSet_Object = MibTableColumn
acdPolicyCosMappingChoice1RegSet = _AcdPolicyCosMappingChoice1RegSet_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 21),
    _AcdPolicyCosMappingChoice1RegSet_Type()
)
acdPolicyCosMappingChoice1RegSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyCosMappingChoice1RegSet.setStatus("current")
_AcdPolicyCosMappingChoice2En_Type = TruthValue
_AcdPolicyCosMappingChoice2En_Object = MibTableColumn
acdPolicyCosMappingChoice2En = _AcdPolicyCosMappingChoice2En_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 22),
    _AcdPolicyCosMappingChoice2En_Type()
)
acdPolicyCosMappingChoice2En.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyCosMappingChoice2En.setStatus("current")


class _AcdPolicyCosMappingChoice2Type_Type(Integer32):
    """Custom type acdPolicyCosMappingChoice2Type based on Integer32"""
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
        *(("dscp", 4),
          ("pcpVlan", 1),
          ("pcpVlanInVlan", 2),
          ("pre", 3))
    )


_AcdPolicyCosMappingChoice2Type_Type.__name__ = "Integer32"
_AcdPolicyCosMappingChoice2Type_Object = MibTableColumn
acdPolicyCosMappingChoice2Type = _AcdPolicyCosMappingChoice2Type_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 23),
    _AcdPolicyCosMappingChoice2Type_Type()
)
acdPolicyCosMappingChoice2Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyCosMappingChoice2Type.setStatus("current")
_AcdPolicyCosMappingChoice2Profile_Type = Unsigned32
_AcdPolicyCosMappingChoice2Profile_Object = MibTableColumn
acdPolicyCosMappingChoice2Profile = _AcdPolicyCosMappingChoice2Profile_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 24),
    _AcdPolicyCosMappingChoice2Profile_Type()
)
acdPolicyCosMappingChoice2Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyCosMappingChoice2Profile.setStatus("current")
_AcdPolicyCosMappingChoice2RegSet_Type = Unsigned32
_AcdPolicyCosMappingChoice2RegSet_Object = MibTableColumn
acdPolicyCosMappingChoice2RegSet = _AcdPolicyCosMappingChoice2RegSet_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 25),
    _AcdPolicyCosMappingChoice2RegSet_Type()
)
acdPolicyCosMappingChoice2RegSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyCosMappingChoice2RegSet.setStatus("current")


class _AcdPolicyDefaultMappingGreenCfi_Type(Unsigned32):
    """Custom type acdPolicyDefaultMappingGreenCfi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcdPolicyDefaultMappingGreenCfi_Type.__name__ = "Unsigned32"
_AcdPolicyDefaultMappingGreenCfi_Object = MibTableColumn
acdPolicyDefaultMappingGreenCfi = _AcdPolicyDefaultMappingGreenCfi_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 26),
    _AcdPolicyDefaultMappingGreenCfi_Type()
)
acdPolicyDefaultMappingGreenCfi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyDefaultMappingGreenCfi.setStatus("current")


class _AcdPolicyDefaultMappingGreenPrior_Type(Unsigned32):
    """Custom type acdPolicyDefaultMappingGreenPrior based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdPolicyDefaultMappingGreenPrior_Type.__name__ = "Unsigned32"
_AcdPolicyDefaultMappingGreenPrior_Object = MibTableColumn
acdPolicyDefaultMappingGreenPrior = _AcdPolicyDefaultMappingGreenPrior_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 27),
    _AcdPolicyDefaultMappingGreenPrior_Type()
)
acdPolicyDefaultMappingGreenPrior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyDefaultMappingGreenPrior.setStatus("current")


class _AcdPolicyDefaultMappingYellowCfi_Type(Unsigned32):
    """Custom type acdPolicyDefaultMappingYellowCfi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcdPolicyDefaultMappingYellowCfi_Type.__name__ = "Unsigned32"
_AcdPolicyDefaultMappingYellowCfi_Object = MibTableColumn
acdPolicyDefaultMappingYellowCfi = _AcdPolicyDefaultMappingYellowCfi_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 28),
    _AcdPolicyDefaultMappingYellowCfi_Type()
)
acdPolicyDefaultMappingYellowCfi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyDefaultMappingYellowCfi.setStatus("current")


class _AcdPolicyDefaultMappingYellowPrior_Type(Unsigned32):
    """Custom type acdPolicyDefaultMappingYellowPrior based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdPolicyDefaultMappingYellowPrior_Type.__name__ = "Unsigned32"
_AcdPolicyDefaultMappingYellowPrior_Object = MibTableColumn
acdPolicyDefaultMappingYellowPrior = _AcdPolicyDefaultMappingYellowPrior_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 29),
    _AcdPolicyDefaultMappingYellowPrior_Type()
)
acdPolicyDefaultMappingYellowPrior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyDefaultMappingYellowPrior.setStatus("current")
_AcdPolicyOutgoingPort_Type = ObjectIdentifier
_AcdPolicyOutgoingPort_Object = MibTableColumn
acdPolicyOutgoingPort = _AcdPolicyOutgoingPort_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 1, 1, 30),
    _AcdPolicyOutgoingPort_Type()
)
acdPolicyOutgoingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPolicyOutgoingPort.setStatus("current")
_AcdPolicyStatsTable_Object = MibTable
acdPolicyStatsTable = _AcdPolicyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 2)
)
if mibBuilder.loadTexts:
    acdPolicyStatsTable.setStatus("current")
_AcdPolicyStatsEntry_Object = MibTableRow
acdPolicyStatsEntry = _AcdPolicyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 2, 1)
)
acdPolicyStatsEntry.setIndexNames(
    (0, "ACD-POLICY-MIB", "acdPolicyStatsID"),
)
if mibBuilder.loadTexts:
    acdPolicyStatsEntry.setStatus("current")
_AcdPolicyStatsID_Type = Unsigned32
_AcdPolicyStatsID_Object = MibTableColumn
acdPolicyStatsID = _AcdPolicyStatsID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 2, 1, 1),
    _AcdPolicyStatsID_Type()
)
acdPolicyStatsID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPolicyStatsID.setStatus("current")
_AcdPolicyStatsListID_Type = Unsigned32
_AcdPolicyStatsListID_Object = MibTableColumn
acdPolicyStatsListID = _AcdPolicyStatsListID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 2, 1, 2),
    _AcdPolicyStatsListID_Type()
)
acdPolicyStatsListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyStatsListID.setStatus("current")
_AcdPolicyStatsEntryID_Type = Unsigned32
_AcdPolicyStatsEntryID_Object = MibTableColumn
acdPolicyStatsEntryID = _AcdPolicyStatsEntryID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 2, 1, 3),
    _AcdPolicyStatsEntryID_Type()
)
acdPolicyStatsEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyStatsEntryID.setStatus("current")
_AcdPolicyStatsInPkts_Type = Counter32
_AcdPolicyStatsInPkts_Object = MibTableColumn
acdPolicyStatsInPkts = _AcdPolicyStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 2, 1, 4),
    _AcdPolicyStatsInPkts_Type()
)
acdPolicyStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyStatsInPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPolicyStatsInPkts.setUnits("Packets")
_AcdPolicyStatsInOverflowPkts_Type = Counter32
_AcdPolicyStatsInOverflowPkts_Object = MibTableColumn
acdPolicyStatsInOverflowPkts = _AcdPolicyStatsInOverflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 2, 1, 5),
    _AcdPolicyStatsInOverflowPkts_Type()
)
acdPolicyStatsInOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyStatsInOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPolicyStatsInOverflowPkts.setUnits("Packets")
_AcdPolicyStatsInHCPkts_Type = Counter64
_AcdPolicyStatsInHCPkts_Object = MibTableColumn
acdPolicyStatsInHCPkts = _AcdPolicyStatsInHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 2, 1, 6),
    _AcdPolicyStatsInHCPkts_Type()
)
acdPolicyStatsInHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyStatsInHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPolicyStatsInHCPkts.setUnits("Packets")
_AcdPolicyStatsInOctets_Type = Counter32
_AcdPolicyStatsInOctets_Object = MibTableColumn
acdPolicyStatsInOctets = _AcdPolicyStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 2, 1, 7),
    _AcdPolicyStatsInOctets_Type()
)
acdPolicyStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyStatsInOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdPolicyStatsInOctets.setUnits("Octets")
_AcdPolicyStatsInOverflowOctets_Type = Counter32
_AcdPolicyStatsInOverflowOctets_Object = MibTableColumn
acdPolicyStatsInOverflowOctets = _AcdPolicyStatsInOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 2, 1, 8),
    _AcdPolicyStatsInOverflowOctets_Type()
)
acdPolicyStatsInOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyStatsInOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdPolicyStatsInOverflowOctets.setUnits("Octets")
_AcdPolicyStatsInHCOctets_Type = Counter64
_AcdPolicyStatsInHCOctets_Object = MibTableColumn
acdPolicyStatsInHCOctets = _AcdPolicyStatsInHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 2, 1, 9),
    _AcdPolicyStatsInHCOctets_Type()
)
acdPolicyStatsInHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyStatsInHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdPolicyStatsInHCOctets.setUnits("Octets")
_AcdPolicyStatsInPktsErr_Type = Counter32
_AcdPolicyStatsInPktsErr_Object = MibTableColumn
acdPolicyStatsInPktsErr = _AcdPolicyStatsInPktsErr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 2, 1, 10),
    _AcdPolicyStatsInPktsErr_Type()
)
acdPolicyStatsInPktsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyStatsInPktsErr.setStatus("current")
if mibBuilder.loadTexts:
    acdPolicyStatsInPktsErr.setUnits("Packets")
_AcdPolicyStatsInOverflowPktsErr_Type = Counter32
_AcdPolicyStatsInOverflowPktsErr_Object = MibTableColumn
acdPolicyStatsInOverflowPktsErr = _AcdPolicyStatsInOverflowPktsErr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 2, 1, 11),
    _AcdPolicyStatsInOverflowPktsErr_Type()
)
acdPolicyStatsInOverflowPktsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyStatsInOverflowPktsErr.setStatus("current")
if mibBuilder.loadTexts:
    acdPolicyStatsInOverflowPktsErr.setUnits("Packets")
_AcdPolicyStatsInHCPktsErr_Type = Counter64
_AcdPolicyStatsInHCPktsErr_Object = MibTableColumn
acdPolicyStatsInHCPktsErr = _AcdPolicyStatsInHCPktsErr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 2, 1, 12),
    _AcdPolicyStatsInHCPktsErr_Type()
)
acdPolicyStatsInHCPktsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyStatsInHCPktsErr.setStatus("current")
if mibBuilder.loadTexts:
    acdPolicyStatsInHCPktsErr.setUnits("Packets")
_AcdPolicyHistStatsTable_Object = MibTable
acdPolicyHistStatsTable = _AcdPolicyHistStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 3)
)
if mibBuilder.loadTexts:
    acdPolicyHistStatsTable.setStatus("current")
_AcdPolicyHistStatsEntry_Object = MibTableRow
acdPolicyHistStatsEntry = _AcdPolicyHistStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 3, 1)
)
acdPolicyHistStatsEntry.setIndexNames(
    (0, "ACD-POLICY-MIB", "acdPolicyHistStatsID"),
    (0, "ACD-POLICY-MIB", "acdPolicyHistStatsSampleIndex"),
)
if mibBuilder.loadTexts:
    acdPolicyHistStatsEntry.setStatus("current")
_AcdPolicyHistStatsID_Type = Unsigned32
_AcdPolicyHistStatsID_Object = MibTableColumn
acdPolicyHistStatsID = _AcdPolicyHistStatsID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 3, 1, 1),
    _AcdPolicyHistStatsID_Type()
)
acdPolicyHistStatsID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPolicyHistStatsID.setStatus("current")
_AcdPolicyHistStatsListID_Type = Unsigned32
_AcdPolicyHistStatsListID_Object = MibTableColumn
acdPolicyHistStatsListID = _AcdPolicyHistStatsListID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 3, 1, 2),
    _AcdPolicyHistStatsListID_Type()
)
acdPolicyHistStatsListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyHistStatsListID.setStatus("current")
_AcdPolicyHistStatsEntryID_Type = Unsigned32
_AcdPolicyHistStatsEntryID_Object = MibTableColumn
acdPolicyHistStatsEntryID = _AcdPolicyHistStatsEntryID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 3, 1, 3),
    _AcdPolicyHistStatsEntryID_Type()
)
acdPolicyHistStatsEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyHistStatsEntryID.setStatus("current")
_AcdPolicyHistStatsSampleIndex_Type = Unsigned32
_AcdPolicyHistStatsSampleIndex_Object = MibTableColumn
acdPolicyHistStatsSampleIndex = _AcdPolicyHistStatsSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 3, 1, 4),
    _AcdPolicyHistStatsSampleIndex_Type()
)
acdPolicyHistStatsSampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPolicyHistStatsSampleIndex.setStatus("current")


class _AcdPolicyHistStatsStatus_Type(Integer32):
    """Custom type acdPolicyHistStatsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AcdPolicyHistStatsStatus_Type.__name__ = "Integer32"
_AcdPolicyHistStatsStatus_Object = MibTableColumn
acdPolicyHistStatsStatus = _AcdPolicyHistStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 3, 1, 5),
    _AcdPolicyHistStatsStatus_Type()
)
acdPolicyHistStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyHistStatsStatus.setStatus("current")
_AcdPolicyHistStatsDuration_Type = Unsigned32
_AcdPolicyHistStatsDuration_Object = MibTableColumn
acdPolicyHistStatsDuration = _AcdPolicyHistStatsDuration_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 3, 1, 6),
    _AcdPolicyHistStatsDuration_Type()
)
acdPolicyHistStatsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyHistStatsDuration.setStatus("current")
_AcdPolicyHistStatsIntervalEnd_Type = DateAndTime
_AcdPolicyHistStatsIntervalEnd_Object = MibTableColumn
acdPolicyHistStatsIntervalEnd = _AcdPolicyHistStatsIntervalEnd_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 3, 1, 7),
    _AcdPolicyHistStatsIntervalEnd_Type()
)
acdPolicyHistStatsIntervalEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyHistStatsIntervalEnd.setStatus("current")
_AcdPolicyHistStatsInPkts_Type = Counter32
_AcdPolicyHistStatsInPkts_Object = MibTableColumn
acdPolicyHistStatsInPkts = _AcdPolicyHistStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 3, 1, 8),
    _AcdPolicyHistStatsInPkts_Type()
)
acdPolicyHistStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyHistStatsInPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPolicyHistStatsInPkts.setUnits("Packets")
_AcdPolicyHistStatsInOverflowPkts_Type = Counter32
_AcdPolicyHistStatsInOverflowPkts_Object = MibTableColumn
acdPolicyHistStatsInOverflowPkts = _AcdPolicyHistStatsInOverflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 3, 1, 9),
    _AcdPolicyHistStatsInOverflowPkts_Type()
)
acdPolicyHistStatsInOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyHistStatsInOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPolicyHistStatsInOverflowPkts.setUnits("Packets")
_AcdPolicyHistStatsInHCPkts_Type = Counter64
_AcdPolicyHistStatsInHCPkts_Object = MibTableColumn
acdPolicyHistStatsInHCPkts = _AcdPolicyHistStatsInHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 3, 1, 10),
    _AcdPolicyHistStatsInHCPkts_Type()
)
acdPolicyHistStatsInHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyHistStatsInHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPolicyHistStatsInHCPkts.setUnits("Packets")
_AcdPolicyHistStatsInOctets_Type = Counter32
_AcdPolicyHistStatsInOctets_Object = MibTableColumn
acdPolicyHistStatsInOctets = _AcdPolicyHistStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 3, 1, 11),
    _AcdPolicyHistStatsInOctets_Type()
)
acdPolicyHistStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyHistStatsInOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdPolicyHistStatsInOctets.setUnits("Octets")
_AcdPolicyHistStatsInOverflowOctets_Type = Counter32
_AcdPolicyHistStatsInOverflowOctets_Object = MibTableColumn
acdPolicyHistStatsInOverflowOctets = _AcdPolicyHistStatsInOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 3, 1, 12),
    _AcdPolicyHistStatsInOverflowOctets_Type()
)
acdPolicyHistStatsInOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyHistStatsInOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdPolicyHistStatsInOverflowOctets.setUnits("Octets")
_AcdPolicyHistStatsInHCOctets_Type = Counter64
_AcdPolicyHistStatsInHCOctets_Object = MibTableColumn
acdPolicyHistStatsInHCOctets = _AcdPolicyHistStatsInHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 3, 1, 13),
    _AcdPolicyHistStatsInHCOctets_Type()
)
acdPolicyHistStatsInHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyHistStatsInHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdPolicyHistStatsInHCOctets.setUnits("Octets")
_AcdPolicyHistStatsInPktsErr_Type = Counter32
_AcdPolicyHistStatsInPktsErr_Object = MibTableColumn
acdPolicyHistStatsInPktsErr = _AcdPolicyHistStatsInPktsErr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 3, 1, 14),
    _AcdPolicyHistStatsInPktsErr_Type()
)
acdPolicyHistStatsInPktsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyHistStatsInPktsErr.setStatus("current")
if mibBuilder.loadTexts:
    acdPolicyHistStatsInPktsErr.setUnits("Packets")
_AcdPolicyHistStatsInOverflowPktsErr_Type = Counter32
_AcdPolicyHistStatsInOverflowPktsErr_Object = MibTableColumn
acdPolicyHistStatsInOverflowPktsErr = _AcdPolicyHistStatsInOverflowPktsErr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 3, 1, 15),
    _AcdPolicyHistStatsInOverflowPktsErr_Type()
)
acdPolicyHistStatsInOverflowPktsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyHistStatsInOverflowPktsErr.setStatus("current")
if mibBuilder.loadTexts:
    acdPolicyHistStatsInOverflowPktsErr.setUnits("Packets")
_AcdPolicyHistStatsInHCPktsErr_Type = Counter64
_AcdPolicyHistStatsInHCPktsErr_Object = MibTableColumn
acdPolicyHistStatsInHCPktsErr = _AcdPolicyHistStatsInHCPktsErr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 3, 1, 16),
    _AcdPolicyHistStatsInHCPktsErr_Type()
)
acdPolicyHistStatsInHCPktsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyHistStatsInHCPktsErr.setStatus("current")
if mibBuilder.loadTexts:
    acdPolicyHistStatsInHCPktsErr.setUnits("Packets")
_AcdPolicyNotifications_ObjectIdentity = ObjectIdentity
acdPolicyNotifications = _AcdPolicyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 4)
)
_AcdPolicyMIBObjects_ObjectIdentity = ObjectIdentity
acdPolicyMIBObjects = _AcdPolicyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 5)
)
_AcdPolicyList_ObjectIdentity = ObjectIdentity
acdPolicyList = _AcdPolicyList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 5, 1)
)
_AcdPolicyListTable_Object = MibTable
acdPolicyListTable = _AcdPolicyListTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    acdPolicyListTable.setStatus("current")
_AcdPolicyListEntry_Object = MibTableRow
acdPolicyListEntry = _AcdPolicyListEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 5, 1, 1, 1)
)
acdPolicyListEntry.setIndexNames(
    (0, "ACD-POLICY-MIB", "acdPolicyListEntryID"),
)
if mibBuilder.loadTexts:
    acdPolicyListEntry.setStatus("current")
_AcdPolicyListEntryID_Type = Unsigned32
_AcdPolicyListEntryID_Object = MibTableColumn
acdPolicyListEntryID = _AcdPolicyListEntryID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 5, 1, 1, 1, 1),
    _AcdPolicyListEntryID_Type()
)
acdPolicyListEntryID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPolicyListEntryID.setStatus("current")


class _AcdPolicyListName_Type(DisplayString):
    """Custom type acdPolicyListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdPolicyListName_Type.__name__ = "DisplayString"
_AcdPolicyListName_Object = MibTableColumn
acdPolicyListName = _AcdPolicyListName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 5, 1, 1, 1, 2),
    _AcdPolicyListName_Type()
)
acdPolicyListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyListName.setStatus("current")
_AcdPolicyListNbrEntries_Type = Unsigned32
_AcdPolicyListNbrEntries_Object = MibTableColumn
acdPolicyListNbrEntries = _AcdPolicyListNbrEntries_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 5, 1, 1, 1, 3),
    _AcdPolicyListNbrEntries_Type()
)
acdPolicyListNbrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyListNbrEntries.setStatus("current")
_AcdPolicyPort_ObjectIdentity = ObjectIdentity
acdPolicyPort = _AcdPolicyPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 5, 2)
)
_AcdPolicyPortTable_Object = MibTable
acdPolicyPortTable = _AcdPolicyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    acdPolicyPortTable.setStatus("current")
_AcdPolicyPortEntry_Object = MibTableRow
acdPolicyPortEntry = _AcdPolicyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 5, 2, 1, 1)
)
acdPolicyPortEntry.setIndexNames(
    (0, "ACD-POLICY-MIB", "acdPolicyPortEntryID"),
)
if mibBuilder.loadTexts:
    acdPolicyPortEntry.setStatus("current")
_AcdPolicyPortEntryID_Type = Unsigned32
_AcdPolicyPortEntryID_Object = MibTableColumn
acdPolicyPortEntryID = _AcdPolicyPortEntryID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 5, 2, 1, 1, 1),
    _AcdPolicyPortEntryID_Type()
)
acdPolicyPortEntryID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPolicyPortEntryID.setStatus("current")
_AcdPolicyPortListID_Type = Unsigned32
_AcdPolicyPortListID_Object = MibTableColumn
acdPolicyPortListID = _AcdPolicyPortListID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 5, 2, 1, 1, 2),
    _AcdPolicyPortListID_Type()
)
acdPolicyPortListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyPortListID.setStatus("current")
_AcdPolicyTableTid_ObjectIdentity = ObjectIdentity
acdPolicyTableTid = _AcdPolicyTableTid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 5, 3)
)
_AcdPolicyTableLastChangeTid_Type = Unsigned32
_AcdPolicyTableLastChangeTid_Object = MibScalar
acdPolicyTableLastChangeTid = _AcdPolicyTableLastChangeTid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 5, 3, 1),
    _AcdPolicyTableLastChangeTid_Type()
)
acdPolicyTableLastChangeTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPolicyTableLastChangeTid.setStatus("current")
_AcdPolicyConformance_ObjectIdentity = ObjectIdentity
acdPolicyConformance = _AcdPolicyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 6)
)
_AcdPolicyCompliances_ObjectIdentity = ObjectIdentity
acdPolicyCompliances = _AcdPolicyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 6, 1)
)
_AcdPolicyGroups_ObjectIdentity = ObjectIdentity
acdPolicyGroups = _AcdPolicyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 6, 2)
)

# Managed Objects groups

acdPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 6, 2, 1)
)
acdPolicyGroup.setObjects(
      *(("ACD-POLICY-MIB", "acdPolicyListID"),
        ("ACD-POLICY-MIB", "acdPolicyEntryID"),
        ("ACD-POLICY-MIB", "acdPolicyEnable"),
        ("ACD-POLICY-MIB", "acdPolicyFilterType"),
        ("ACD-POLICY-MIB", "acdPolicyFilterIndex"),
        ("ACD-POLICY-MIB", "acdPolicyMonitorEnable"),
        ("ACD-POLICY-MIB", "acdPolicyMonitorIndex"),
        ("ACD-POLICY-MIB", "acdPolicyRegulatorEnable"),
        ("ACD-POLICY-MIB", "acdPolicyRegulatorIndex"),
        ("ACD-POLICY-MIB", "acdPolicyRegulatorMarking"),
        ("ACD-POLICY-MIB", "acdPolicyAction"),
        ("ACD-POLICY-MIB", "acdPolicyEvcMappingEncaps"),
        ("ACD-POLICY-MIB", "acdPolicyEvcMappingEtype"),
        ("ACD-POLICY-MIB", "acdPolicyEvcMappingVlanId"),
        ("ACD-POLICY-MIB", "acdPolicyCosMappingPcpAction"),
        ("ACD-POLICY-MIB", "acdPolicyCosMappingChoice1En"),
        ("ACD-POLICY-MIB", "acdPolicyCosMappingChoice1Type"),
        ("ACD-POLICY-MIB", "acdPolicyCosMappingChoice1Profile"),
        ("ACD-POLICY-MIB", "acdPolicyCosMappingChoice1RegSet"),
        ("ACD-POLICY-MIB", "acdPolicyCosMappingChoice2En"),
        ("ACD-POLICY-MIB", "acdPolicyCosMappingChoice2Type"),
        ("ACD-POLICY-MIB", "acdPolicyCosMappingChoice2Profile"),
        ("ACD-POLICY-MIB", "acdPolicyCosMappingChoice2RegSet"),
        ("ACD-POLICY-MIB", "acdPolicyDefaultMappingGreenCfi"),
        ("ACD-POLICY-MIB", "acdPolicyDefaultMappingGreenPrior"),
        ("ACD-POLICY-MIB", "acdPolicyDefaultMappingYellowCfi"),
        ("ACD-POLICY-MIB", "acdPolicyDefaultMappingYellowPrior"),
        ("ACD-POLICY-MIB", "acdPolicyOutgoingPort"))
)
if mibBuilder.loadTexts:
    acdPolicyGroup.setStatus("current")

acdPolicyStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 6, 2, 2)
)
acdPolicyStatsGroup.setObjects(
      *(("ACD-POLICY-MIB", "acdPolicyStatsListID"),
        ("ACD-POLICY-MIB", "acdPolicyStatsEntryID"),
        ("ACD-POLICY-MIB", "acdPolicyStatsInPkts"),
        ("ACD-POLICY-MIB", "acdPolicyStatsInOverflowPkts"),
        ("ACD-POLICY-MIB", "acdPolicyStatsInHCPkts"),
        ("ACD-POLICY-MIB", "acdPolicyStatsInOctets"),
        ("ACD-POLICY-MIB", "acdPolicyStatsInOverflowOctets"),
        ("ACD-POLICY-MIB", "acdPolicyStatsInHCOctets"),
        ("ACD-POLICY-MIB", "acdPolicyStatsInPktsErr"),
        ("ACD-POLICY-MIB", "acdPolicyStatsInOverflowPktsErr"),
        ("ACD-POLICY-MIB", "acdPolicyStatsInHCPktsErr"))
)
if mibBuilder.loadTexts:
    acdPolicyStatsGroup.setStatus("current")

acdPolicyHistStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 6, 2, 3)
)
acdPolicyHistStatsGroup.setObjects(
      *(("ACD-POLICY-MIB", "acdPolicyHistStatsListID"),
        ("ACD-POLICY-MIB", "acdPolicyHistStatsEntryID"),
        ("ACD-POLICY-MIB", "acdPolicyHistStatsStatus"),
        ("ACD-POLICY-MIB", "acdPolicyHistStatsDuration"),
        ("ACD-POLICY-MIB", "acdPolicyHistStatsIntervalEnd"),
        ("ACD-POLICY-MIB", "acdPolicyHistStatsInPkts"),
        ("ACD-POLICY-MIB", "acdPolicyHistStatsInOverflowPkts"),
        ("ACD-POLICY-MIB", "acdPolicyHistStatsInHCPkts"),
        ("ACD-POLICY-MIB", "acdPolicyHistStatsInOctets"),
        ("ACD-POLICY-MIB", "acdPolicyHistStatsInOverflowOctets"),
        ("ACD-POLICY-MIB", "acdPolicyHistStatsInHCOctets"),
        ("ACD-POLICY-MIB", "acdPolicyHistStatsInPktsErr"),
        ("ACD-POLICY-MIB", "acdPolicyHistStatsInOverflowPktsErr"),
        ("ACD-POLICY-MIB", "acdPolicyHistStatsInHCPktsErr"))
)
if mibBuilder.loadTexts:
    acdPolicyHistStatsGroup.setStatus("current")

acdPolicyDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 6, 2, 4)
)
acdPolicyDeprecatedGroup.setObjects(
    ("ACD-POLICY-MIB", "acdPolicyDropEnable")
)
if mibBuilder.loadTexts:
    acdPolicyDeprecatedGroup.setStatus("deprecated")

acdPolicyListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 6, 2, 5)
)
acdPolicyListGroup.setObjects(
      *(("ACD-POLICY-MIB", "acdPolicyListName"),
        ("ACD-POLICY-MIB", "acdPolicyListNbrEntries"))
)
if mibBuilder.loadTexts:
    acdPolicyListGroup.setStatus("current")

acdPolicyPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 6, 2, 6)
)
acdPolicyPortGroup.setObjects(
    ("ACD-POLICY-MIB", "acdPolicyPortListID")
)
if mibBuilder.loadTexts:
    acdPolicyPortGroup.setStatus("current")

acdPolicyTidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 6, 2, 7)
)
acdPolicyTidGroup.setObjects(
    ("ACD-POLICY-MIB", "acdPolicyTableLastChangeTid")
)
if mibBuilder.loadTexts:
    acdPolicyTidGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acdPolicyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    acdPolicyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-POLICY-MIB",
    **{"acdPolicy": acdPolicy,
       "acdPolicyTable": acdPolicyTable,
       "acdPolicyEntry": acdPolicyEntry,
       "acdPolicyID": acdPolicyID,
       "acdPolicyListID": acdPolicyListID,
       "acdPolicyEntryID": acdPolicyEntryID,
       "acdPolicyEnable": acdPolicyEnable,
       "acdPolicyFilterType": acdPolicyFilterType,
       "acdPolicyFilterIndex": acdPolicyFilterIndex,
       "acdPolicyDropEnable": acdPolicyDropEnable,
       "acdPolicyMonitorEnable": acdPolicyMonitorEnable,
       "acdPolicyMonitorIndex": acdPolicyMonitorIndex,
       "acdPolicyRegulatorEnable": acdPolicyRegulatorEnable,
       "acdPolicyRegulatorIndex": acdPolicyRegulatorIndex,
       "acdPolicyRegulatorMarking": acdPolicyRegulatorMarking,
       "acdPolicyAction": acdPolicyAction,
       "acdPolicyEvcMappingEncaps": acdPolicyEvcMappingEncaps,
       "acdPolicyEvcMappingEtype": acdPolicyEvcMappingEtype,
       "acdPolicyEvcMappingVlanId": acdPolicyEvcMappingVlanId,
       "acdPolicyCosMappingPcpAction": acdPolicyCosMappingPcpAction,
       "acdPolicyCosMappingChoice1En": acdPolicyCosMappingChoice1En,
       "acdPolicyCosMappingChoice1Type": acdPolicyCosMappingChoice1Type,
       "acdPolicyCosMappingChoice1Profile": acdPolicyCosMappingChoice1Profile,
       "acdPolicyCosMappingChoice1RegSet": acdPolicyCosMappingChoice1RegSet,
       "acdPolicyCosMappingChoice2En": acdPolicyCosMappingChoice2En,
       "acdPolicyCosMappingChoice2Type": acdPolicyCosMappingChoice2Type,
       "acdPolicyCosMappingChoice2Profile": acdPolicyCosMappingChoice2Profile,
       "acdPolicyCosMappingChoice2RegSet": acdPolicyCosMappingChoice2RegSet,
       "acdPolicyDefaultMappingGreenCfi": acdPolicyDefaultMappingGreenCfi,
       "acdPolicyDefaultMappingGreenPrior": acdPolicyDefaultMappingGreenPrior,
       "acdPolicyDefaultMappingYellowCfi": acdPolicyDefaultMappingYellowCfi,
       "acdPolicyDefaultMappingYellowPrior": acdPolicyDefaultMappingYellowPrior,
       "acdPolicyOutgoingPort": acdPolicyOutgoingPort,
       "acdPolicyStatsTable": acdPolicyStatsTable,
       "acdPolicyStatsEntry": acdPolicyStatsEntry,
       "acdPolicyStatsID": acdPolicyStatsID,
       "acdPolicyStatsListID": acdPolicyStatsListID,
       "acdPolicyStatsEntryID": acdPolicyStatsEntryID,
       "acdPolicyStatsInPkts": acdPolicyStatsInPkts,
       "acdPolicyStatsInOverflowPkts": acdPolicyStatsInOverflowPkts,
       "acdPolicyStatsInHCPkts": acdPolicyStatsInHCPkts,
       "acdPolicyStatsInOctets": acdPolicyStatsInOctets,
       "acdPolicyStatsInOverflowOctets": acdPolicyStatsInOverflowOctets,
       "acdPolicyStatsInHCOctets": acdPolicyStatsInHCOctets,
       "acdPolicyStatsInPktsErr": acdPolicyStatsInPktsErr,
       "acdPolicyStatsInOverflowPktsErr": acdPolicyStatsInOverflowPktsErr,
       "acdPolicyStatsInHCPktsErr": acdPolicyStatsInHCPktsErr,
       "acdPolicyHistStatsTable": acdPolicyHistStatsTable,
       "acdPolicyHistStatsEntry": acdPolicyHistStatsEntry,
       "acdPolicyHistStatsID": acdPolicyHistStatsID,
       "acdPolicyHistStatsListID": acdPolicyHistStatsListID,
       "acdPolicyHistStatsEntryID": acdPolicyHistStatsEntryID,
       "acdPolicyHistStatsSampleIndex": acdPolicyHistStatsSampleIndex,
       "acdPolicyHistStatsStatus": acdPolicyHistStatsStatus,
       "acdPolicyHistStatsDuration": acdPolicyHistStatsDuration,
       "acdPolicyHistStatsIntervalEnd": acdPolicyHistStatsIntervalEnd,
       "acdPolicyHistStatsInPkts": acdPolicyHistStatsInPkts,
       "acdPolicyHistStatsInOverflowPkts": acdPolicyHistStatsInOverflowPkts,
       "acdPolicyHistStatsInHCPkts": acdPolicyHistStatsInHCPkts,
       "acdPolicyHistStatsInOctets": acdPolicyHistStatsInOctets,
       "acdPolicyHistStatsInOverflowOctets": acdPolicyHistStatsInOverflowOctets,
       "acdPolicyHistStatsInHCOctets": acdPolicyHistStatsInHCOctets,
       "acdPolicyHistStatsInPktsErr": acdPolicyHistStatsInPktsErr,
       "acdPolicyHistStatsInOverflowPktsErr": acdPolicyHistStatsInOverflowPktsErr,
       "acdPolicyHistStatsInHCPktsErr": acdPolicyHistStatsInHCPktsErr,
       "acdPolicyNotifications": acdPolicyNotifications,
       "acdPolicyMIBObjects": acdPolicyMIBObjects,
       "acdPolicyList": acdPolicyList,
       "acdPolicyListTable": acdPolicyListTable,
       "acdPolicyListEntry": acdPolicyListEntry,
       "acdPolicyListEntryID": acdPolicyListEntryID,
       "acdPolicyListName": acdPolicyListName,
       "acdPolicyListNbrEntries": acdPolicyListNbrEntries,
       "acdPolicyPort": acdPolicyPort,
       "acdPolicyPortTable": acdPolicyPortTable,
       "acdPolicyPortEntry": acdPolicyPortEntry,
       "acdPolicyPortEntryID": acdPolicyPortEntryID,
       "acdPolicyPortListID": acdPolicyPortListID,
       "acdPolicyTableTid": acdPolicyTableTid,
       "acdPolicyTableLastChangeTid": acdPolicyTableLastChangeTid,
       "acdPolicyConformance": acdPolicyConformance,
       "acdPolicyCompliances": acdPolicyCompliances,
       "acdPolicyCompliance": acdPolicyCompliance,
       "acdPolicyGroups": acdPolicyGroups,
       "acdPolicyGroup": acdPolicyGroup,
       "acdPolicyStatsGroup": acdPolicyStatsGroup,
       "acdPolicyHistStatsGroup": acdPolicyHistStatsGroup,
       "acdPolicyDeprecatedGroup": acdPolicyDeprecatedGroup,
       "acdPolicyListGroup": acdPolicyListGroup,
       "acdPolicyPortGroup": acdPolicyPortGroup,
       "acdPolicyTidGroup": acdPolicyTidGroup}
)
